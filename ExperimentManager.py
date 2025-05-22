from stable_baselines3 import *
import pyRDDLGym
from pyRDDLGym_rl.core.agent import StableBaselinesAgent
from pyRDDLGym_rl.core.env import SimplifiedActionRDDLEnv
from AUX import aux
import torch
import numpy as np
import os
import csv


class ExperimentManager():
    def __init__(self, name='new', instance='instance1.rddl', run_from_scratch=True, average=10,
                 net_arch=[128, 64], train_episodes_interval=1):
        self.experiment_name = name
        self.instance = instance
        self.run_from_scratch = run_from_scratch
        self.average = average
        self.net_arch = net_arch
        self.train_episodes_interval = train_episodes_interval
        self.trained_episodes = 0
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_name = os.path.join(self.script_dir, 'logs', self.experiment_name+'.csv')
        self.model_name = os.path.join(self.script_dir, 'models', self.experiment_name+'.zip')


    def run_experiment(self, num_train_episodes):
        train_episodes = num_train_episodes

        abs_domain_file_location = os.path.join(self.script_dir, 'reservoir', 'domain.rddl')
        abs_instance_file_location = os.path.join(self.script_dir, 'reservoir', self.instance)

        myTrainEnv = pyRDDLGym.make(domain=abs_domain_file_location, instance=abs_instance_file_location,
                                    base_class=SimplifiedActionRDDLEnv)
        myEvalEnv = pyRDDLGym.make(domain=abs_domain_file_location, instance=abs_instance_file_location,
                                   base_class=SimplifiedActionRDDLEnv)
        horizon = myTrainEnv.horizon

        policy_kwargs = {
            "net_arch": self.net_arch,
            "activation_fn": torch.nn.Tanh  # Use ReLU activation
        }
        if not self.run_from_scratch and os.path.exists(self.model_name):
            model = PPO.load(self.model_name, myTrainEnv)
        else:
            model = PPO('MultiInputPolicy', myTrainEnv, policy_kwargs=policy_kwargs,
                        n_steps=self.train_episodes_interval * horizon,
                        batch_size=self.train_episodes_interval * horizon, n_epochs=1, verbose=0)

        returns = []
        for episode in range(train_episodes):
            model.learn(total_timesteps=self.train_episodes_interval * horizon, reset_num_timesteps=False)
            agent = StableBaselinesAgent(model, deterministic=True)
            r = self.evaluate(agent, myEvalEnv, episodes=self.average, seed=0, verbose=0)
            print('episode: ', episode, ' ended with: ', r)
            returns.append(r)
            self.trained_episodes += 1
        myTrainEnv.close()
        model.save(self.model_name)
        self.log_results(returns)

    def evaluate(self, agent, Env, episodes=1, verbose=False, seed=42):
        returns = []
        for eps in range(episodes):
            total_reward = 0
            state, _ = Env.reset(seed=seed + eps)
            for step in range(Env.horizon):
                action = agent.sample_action(state)
                next_state, reward, done, info, _ = Env.step(action)
                total_reward += reward
                if verbose:
                    print()
                    print(f'step       = {step}')
                    print(f'state      = {state}')
                    print(f'action     = {action}')
                    print(f'next state = {next_state}')
                    print(f'reward     = {reward}')
                state = next_state
                if done:
                    break
            if verbose:
                print(f'episode ended with reward {total_reward}')
            returns.append(total_reward)
        Env.close()
        return {'mean': np.mean(returns), 'std': np.std(returns)}

    def log_results(self, returns):
        # Only write header if file doesn't exist
        csv_file = self.log_name
        write_header = not os.path.exists(csv_file)

        # Open the file in append mode
        mode = 'a'
        if self.run_from_scratch:
            mode='w'
        csvfile = open(csv_file, mode=mode, newline='')
        writer = csv.DictWriter(csvfile, fieldnames=["mean_eval_reward", "std_eval_reward"])

        if write_header or self.run_from_scratch:
            writer.writeheader()

        for r in range(len(returns)):
            row = {
                'mean_eval_reward': returns[r]['mean'],
                'std_eval_reward': returns[r]['std']
            }
            writer.writerow(row)
        csvfile.close()
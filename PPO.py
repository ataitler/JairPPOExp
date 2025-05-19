import csv

#from stable_baselines3 import *
#import pyRDDLGym
#from pyRDDLGym_rl.core.agent import StableBaselinesAgent
#from pyRDDLGym_rl.core.env import SimplifiedActionRDDLEnv
from AUX import aux
#import torch
import sys
import csv
import matplotlib.pyplot as plt

def main():

    means = []
    stds = []
    upper_bound = []
    lower_bound = []
    csv_file = 'logs/instance10.csv'
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            mean = float(row['mean_eval_reward'])
            std = float(row['std_eval_reward'])
            means.append(mean)
            stds.append(std)
            upper_bound.append(mean + std)
            lower_bound.append(mean - std)

    x_axis = list(range(1, len(means)+1))

    plt.figure(figsize=(8, 5))
    plt.plot(x_axis, means, color='b', marker='o', label="Mean")  # Mean curve
    plt.fill_between(x_axis, lower_bound, upper_bound, color='b', alpha=0.2, label="±1 Std Dev")  # Shaded std envelope

    # Add labels and title
    plt.xlabel("episode")
    plt.ylabel("reward")
    plt.title("results")
    plt.legend()

    # Show the figure
    plt.show()






    sys.exit()

    #
    # myTrainEnv = pyRDDLGym.make(domain='reservoir/domain.rddl', instance='reservoir/instance1.rddl',
    #                        base_class=SimplifiedActionRDDLEnv)
    # myEvalEnv = pyRDDLGym.make(domain='reservoir/domain.rddl', instance='reservoir/instance1.rddl',
    #                             base_class=SimplifiedActionRDDLEnv)
    # HORIZON = myTrainEnv.horizon
    # TRAIN_EPISODES = 1
    #
    # policy_kwargs = {
    #     "net_arch": [128, 64],  # Two hidden layers with 64 neurons each
    #     "activation_fn": torch.nn.Tanh  # Use ReLU activation
    # }
    # model = PPO('MultiInputPolicy', myTrainEnv, policy_kwargs=policy_kwargs, verbose=0)
    #
    # returns = []
    # for episode in range(50):
    #     model.learn(total_timesteps=TRAIN_EPISODES*HORIZON, reset_num_timesteps=False)
    #     agent = StableBaselinesAgent(model, deterministic=True)
    #     r = aux.evaluate(agent, myEvalEnv, episodes=5, seed=0, verbose=0)
    #     print('episode: ', episode, ' ended with: ', r)
    #     returns.append(r)
    # myTrainEnv.close()
    #
    # aux.displayResults(returns)

if __name__ == "__main__":
    main()
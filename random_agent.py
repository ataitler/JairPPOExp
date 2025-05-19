import pyRDDLGym
from pyRDDLGym.core.visualizer.movie import MovieGenerator
from pyRDDLGym.core.policy import RandomAgent
from rddlrepository.core.manager import RDDLRepoManager


def main():
    ENV = 'Reservoir_Continuous'
    myEnv = pyRDDLGym.make(domain='reservoir/domain.rddl', instance='reservoir/instance1.rddl')

    agent = RandomAgent(action_space=myEnv.action_space,
                            num_actions=myEnv.max_allowed_actions,
                            seed=42)

    total_reward = 0
    state, _ = myEnv.reset()
    for step in range(myEnv.horizon):
        action = agent.sample_action()
        next_state, reward, done, info, _ = myEnv.step(action)
        total_reward += reward
        print()
        print(f'step       = {step}')
        print(f'state      = {state}')
        print(f'action     = {action}')
        print(f'next state = {next_state}')
        print(f'reward     = {reward}')
        state = next_state
        if done:
            break
    print(f'episode ended with reward {total_reward}')

    myEnv.close()



if __name__ == "__main__":
    main()
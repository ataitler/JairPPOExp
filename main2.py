import ExperimentManager
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--instance", type=str, help="The instance to run")
parser.add_argument("--seed", type=int, help="The experiment seed to use")
parser.add_argument("--istrain", type=int, help="train (true) or evaluation (false)")
parser.add_argument("--average", type=int, help="How many episode to average test on")
parser.add_argument("--ppo", type=int, help="is running on PPO 1 (true), or PPO 20 (false)")

args = parser.parse_args()



def main(instance, seed, is_train, average, ppo_type):
    instance2run = instance+'.rddl'
    exp_name = instance + '_run' + str(seed)
    Manager = ExperimentManager.ExperimentManager(name=exp_name, instance=instance2run, run_from_scratch=True,
                                                  average=1, train_episodes_interval=1)
    Manager.measure_results(is_train=is_train, num_episodes=average, ppo=ppo_type)


if __name__ == '__main__':
    main(args.instance, args.seed, bool(args.istrain), args.average, bool(args.ppo))

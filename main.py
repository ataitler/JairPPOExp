import ExperimentManager
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--instance", type=str, help="The instance to run")
parser.add_argument("--seed", type=int, help="The experiment seed to use")
parser.add_argument("--length", type=int, help="How many episode to train on")
parser.add_argument("--average", type=int, help="How many episode to average test on")

args = parser.parse_args()



def main(instance, seed, length, average):
    instance2run = instance+'.rddl'
    exp_name = instance + '_run' + str(seed)
    Manager = ExperimentManager.ExperimentManager(name=exp_name, instance=instance2run, run_from_scratch=False,
                                                  average=average, train_episodes_interval=1)
    Manager.run_experiment(num_train_episodes=length)


if __name__ == '__main__':
    main(args.instance, args.seed, args.length, args.average)

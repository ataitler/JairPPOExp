import ExperimentManager
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--instance", type=str, help="The instance to run")
parser.add_argument("--seed", type=int, help="The experiment seed to use")
parser.add_argument("--length", type=int, help="How many episode to train on")
parser.add_argument("--average", type=int, help="How many episode to average test on")

args = parser.parse_args()


# EXPERIMENT_NAME = ['instance1', 'instance3','instance10']
# RDDL_SUFFIX = '.rddl'
# EXPERIMENT_INSTANCE = [name + RDDL_SUFFIX for name in EXPERIMENT_NAME]
# # EXPERIMENT_INSTANCE = ['instance1.rddl', 'instance3.rddl','instance10.rddl']
# EXPERIMENT_LENGTH = [0,0,1]
#
#
#
# def main2():
#     for i in range(len(EXPERIMENT_NAME)):
#         print('Running experiment ' + EXPERIMENT_NAME[i] + ':')
#         Manager = ExperimentManager.ExperimentManager(name=EXPERIMENT_NAME[i], instance=EXPERIMENT_INSTANCE[i],
#                                                       run_from_scratch=False, average=5, train_episodes_interval=1)
#         Manager.run_experiment(num_train_episodes=EXPERIMENT_LENGTH[i])


def main(instance, seed, length, average):
    instance2run = instance+'.rddl'
    exp_name = instance + '_run' + str(seed)
    Manager = ExperimentManager.ExperimentManager(name=exp_name, instance=instance2run, run_from_scratch=False,
                                                  average=average, train_episodes_interval=1)
    Manager.run_experiment(num_train_episodes=length)


if __name__ == '__main__':
    main(args.instance, args.seed, args.length, args.average)

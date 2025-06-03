#!/bin/bash

# Check if exactly two arguments were passed
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <instance_num> <num_of_seeds> <experiment_length> <eval_avg>"
    exit 1
fi

# Check if both arguments are non-negative integers
if ! [[ "$1" =~ ^[0-9]+$ ]] || ! [[ "$2" =~ ^[0-9]+$ ]] || ! [[ "$1" =~ ^[0-9]+$ ]] || ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Error: All arguments must be positive integers."
    exit 1
fi

instance=instance$1
max_seed=$2
length=$3
avg=$4
# test_name=${instance}_run_${max_seed}

# Run the Python script $count times
for ((i=1; i<=max_seed; i++))
do
    test_name=${instance}_run_${i}
    #echo "instance $instance , number of seeds: $seed , for length: $length , avg: $avg"
    # echo "test_name $test_name , instance $instance , number of seeds: $max_seed , for length: $length , avg: $avg"
#    echo "runai-cmd --name "$test_name" -g 0.5 --cpu-limit 4 -- \"cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance $instance --seed $i --length $length --average $avg\""
    # runai-cmd --name test5 -g 0.5 --cpu-limit 4 -- "cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance instance1 --seed 1 --length 100 --average 5"
#    runai-cmd --name "$test_name" -g 0.5 --cpu-limit 4 -- "cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance \"$instance\" --seed \"$i\" --length \"$legnth\" --average \"$avg\""
    # runai-cmd --name instance1_run_1 -g 0.5 --cpu-limit 4 -- "cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance instance1 --seed 2 --length 10 --average 5"
    # runai submit -i registry.bgu.ac.il/hpc/jupyter-notebook:latest -e HOME=/gpfs0/bgu-ataitler/users/ataitler --name testing-runai-submit -g 0.5 --cpu-limit 4 -- "cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance instance1 --seed 2 --length 10 --average 5"
    runai submit -i registry.bgu.ac.il/hpc/jupyter-notebook:latest -e HOME=/gpfs0/bgu-ataitler/users/ataitler --name \"$test_name\" -g 0.5 --cpu-limit 4 -- "cd ~/code/JairPPOExp && source activate ~/env/JairExp && python main.py --instance \"$instance\" --seed \"$i\" --length \"$legnth\" --average \"$avg\""
done

import csv
import os
import sys


def concatenate_csv_columnwise_list(file_list, log_dir='logs', output_file='output'):
    base_folder = os.path.dirname(os.path.abspath(__file__))
    log_dir = log_dir
    for i in range(len(file_list)):
        file_list[i] = os.path.join(base_folder, log_dir, file_list[i])

    readers = []
    file_objects = list(map(open, file_list))

    for fobject in file_objects:
        readers.append(csv.reader(fobject))

    mean_out = open(os.path.join(base_folder, log_dir,output_file+'_mean.csv'), 'w', newline='', encoding='utf-8')
    std_out = open(os.path.join(base_folder, log_dir, output_file + '_std.csv'), 'w', newline='', encoding='utf-8')
    writer_mean = csv.writer(mean_out)
    writer_std = csv.writer(std_out)

    header = True
    for rows in zip(*readers):
        if header:
            header = False
            continue
        mean_row = []
        std_row = []
        for r in rows:
            mean_row.append(r[0])
            std_row.append(r[1])
        writer_mean.writerow(mean_row)
        writer_std.writerow(std_row)


def concatenate_csv_columnwise(file1, file2, output_file):
    dir = 'logs/'
    with open(dir+file1+'.csv', newline='', encoding='utf-8') as f1, \
         open(dir+file2+'.csv', newline='', encoding='utf-8') as f2, \
         open(dir+output_file+'_mean.csv', 'w', newline='', encoding='utf-8') as mean_out, \
         open(dir + output_file + '_std.csv', 'w', newline='', encoding='utf-8') as std_out:

        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        writer_mean = csv.writer(mean_out)
        writer_std = csv.writer(std_out)

        # Iterate rows from both files simultaneously
        header = True
        for row1, row2 in zip(reader1, reader2):
            if header:
                header = False
                continue
            # Concatenate columns of both rows
            mean_new_row = [row1[0]] + [row2[0]]
            std_new_row = [row1[1]] + [row2[1]]
            writer_mean.writerow(mean_new_row)
            writer_std.writerow(std_new_row)

# Example usage:
base_folder = os.path.dirname(os.path.abspath(__file__))
instance = "instance10_20u"
files_dir = os.path.join(base_folder, 'logs', instance)
files = os.listdir(files_dir)
concatenate_csv_columnwise_list(files, os.path.join('logs', instance), 'output10')





# concatenate_csv_columnwise('instance1_run1', 'instance1_run2', 'output')
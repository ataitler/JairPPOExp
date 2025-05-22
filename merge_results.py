import csv

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
        for row1, row2 in zip(reader1, reader2):
            # Concatenate columns of both rows
            mean_new_row = [row1[0]] + [row2[0]]
            std_new_row = [row1[1]] + [row2[1]]
            writer_mean.writerow(mean_new_row)
            writer_std.writerow(std_new_row)

# Example usage:
concatenate_csv_columnwise('instance1_run1', 'instance1_run2', 'output')
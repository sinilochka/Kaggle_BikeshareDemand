import math

def read_file_and_get_count(filename, count_column_index):
    file = open(filename)
    header = file.readline()
    result = {}
    for line in file:
        columns = line.strip().split(',')
        datetime = columns[0]
        count = int(columns[count_column_index])
        result[datetime] = count
    return result


submission_results = read_file_and_get_count('model_3_prediction.csv', 1)
real_results = read_file_and_get_count('validate.csv', 11)

print submission_results
print real_results

metric = 0
n = len(real_results)
for datetime in real_results:
    x = math.log(submission_results[datetime] + 1) - math.log(real_results[datetime] + 1)
    metric += x ** 2
print math.sqrt(metric / n)

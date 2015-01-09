file = open('validate.csv')
# file = open('test.csv')
header = file.readline()
prediction_file = open('model_1_prediction.csv', 'w')
# prediction_file = open('model_1_prediction_test.csv', 'w')
print >> prediction_file, "datetime,count"

for line in file:
    columns = line.strip().split(',')
    datetime = columns[0]
    atemp = float(columns[6])
    humidity = float(columns[7])
    wind_speed = float(columns[8])
    workingday = float(columns[3])

    value = 10.902039 + 0.310935 * atemp - 0.109140 * humidity + 0.043629 * wind_speed - 0.01 * workingday
    value = int(value ** 2)
    print >> prediction_file, datetime + "," + str(value)

prediction_file.close()
file.close()

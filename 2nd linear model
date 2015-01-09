file = open('test.csv')
header = file.readline()
prediction_file2 = open('model_2_prediction.csv', 'w')
print >> prediction_file2, "datetime,count"

for line in file:
    columns = line.strip().split(',')
    datetime = columns[0]
    atemp = float(columns[6])
    humidity = float(columns[7])
    wind_speed = float(columns[8])
    workingday = float(columns[3])

    value =  11.119507 + 0.310644 * atemp - 0.109745 * humidity + 0.033579 * wind_speed
    value = int(value ** 2)
    print >> prediction_file2, datetime + "," + str(value)

prediction_file2.close()
file.close()

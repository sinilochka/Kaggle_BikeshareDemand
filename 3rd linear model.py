def get_coef_by_season(season):
    d = {
        1: 0,
        2: 1.4848,
        3: 0.91,
        4: 2.59,
    }
    return d[season]



def get_coef_by_weather(weather):
    d = {
        1: 0,
        2: -0.20669779,
        3: -2.57610044,
        4: -2.29695149,
    }
    return d[season]


def get_coef_by_hour(hour):
    if hour == 1:
        return -1.54308908
    if hour == 2:
        return -2.59582686
    if hour == 3:
        return -3.65827180
    if hour == 4:
        return -4.09719585
    if hour == 5:
        return -2.24052005
    if hour == 6:
        return 1.70755668
    if hour == 7:
        return 6.90689624
    if hour == 8:
        return 11.16012949
    if hour == 9:
        return 7.53022264
    if hour == 10:
        return 5.38198412
    if hour == 11:
        return 6.17991359
    if hour == 12:
        return 7.43854058
    if hour == 13:
        return 7.21541975
    if hour == 14:
        return 6.61575006
    if hour == 15:
        return 7.00032312
    if hour == 16:
        return 8.98823249
    if hour == 17:
        return 12.89800066
    if hour == 18:
        return 12.11982428
    if hour == 19:
        return 9.44330287
    if hour == 20:
        return 7.08877059
    if hour == 21:
        return 5.38293247
    if hour == 22:
        return 3.98911200
    if hour == 23:
        return 2.10896250
    if hour == 0:
        return 0


file = open('test.csv')
# file = open('validate.csv')
header = file.readline()
prediction_file3 = open('model_3_prediction.csv', 'w')
print >> prediction_file3, "datetime,count"

for line in file:
    columns = line.strip().split(',')
    datetime = columns[0]
    hour = int(datetime[11:13])
    season = int(columns[1])
    workingday = float(columns[3])
    weather = int(columns[4])
    temp = float(columns[5])
    atemp = float(columns[6])
    humidity = float(columns[7])
    wind_speed = float(columns[8])

    value = 3.65851873 + get_coef_by_hour(hour) + \
            get_coef_by_season(season) + \
            get_coef_by_weather(weather) +\
            0.14842821 * temp + 0.07694609 * atemp \
            - 0.03044505 * humidity - 0.02473226 * wind_speed
    value = int(value ** 2)
    print >> prediction_file3, datetime + "," + str(value)

prediction_file3.close()
file.close()

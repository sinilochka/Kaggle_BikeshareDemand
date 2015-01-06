bikeshare = open('train.csv', 'r')
subtrain = open('subtrain.csv', 'w')
validate = open('validate.csv', 'w')
bikeshare.readline()
for line in bikeshare.readline():
    line = line.strip()
    columns = line.split(',')
    datetime = columns[0]
    if int(datetime[8:10]) <= 15:
            print >> subtrain, line.strip()
    else:
            print >> validate, line.strip()
subtrain.close()
validate.close()

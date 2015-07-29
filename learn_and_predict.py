
from sys import argv


def main():
    learn_file = open(argv[1])
    stats = {}

    for line in learn_file:
        s = line.strip().split('\t')
        count = int(s[1])
        hour = int(s[3])
        if hour not in stats:
            stats[hour] = []
        stats[hour].append(count)

    predict_file = open(argv[2])
    print "datetime,count\n"
    for line in predict_file:
        s = line.strip().split('\t')
        datetime = s[0]
        hour = int(s[3])
        prediction = 0
        if hour in stats:
            prediction = int(sum(stats[hour]) / len(stats[hour]))
        print "%s,%d" % (datetime, prediction)


if __name__ == '__main__':
    main()

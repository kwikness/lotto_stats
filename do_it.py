import csv
import sys


def tabulate_entry(number_list, tracking_dict):
    for x in number_list:
        if x not in tracking_dict:
            tracking_dict[x] = 0
        tracking_dict[x] = tracking_dict[x] + 1


filename = sys.argv[0]
with open('numbaz.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    tracking_dict = {}

    for row in csv_reader:
        tabulate_entry(row[1].split(' '), tracking_dict)

print sorted(((v,k) for k,v in tracking_dict.iteritems()), reverse=True)

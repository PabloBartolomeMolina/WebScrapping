import csv


def csvTable(champs_dict, csv_file):
    with open(csv_file, 'w') as f:
        for key in champs_dict.keys():
            f.write("%s,%s\n" % (key, champs_dict[key]))
    f.close()

import csv

def csvTable (champs_dict):
    with open('champions.csv', 'w') as f:
        for key in champs_dict.keys():
            f.write("%s,%s\n" % (key, champs_dict[key]))
    f.close()

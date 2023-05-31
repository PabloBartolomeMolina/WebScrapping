import matplotlib.pyplot as plt
import csv

x = []
y = []

def generate_graph(csvname):
    with open(csvname, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            if row[1] in x:
                y[x.index(row[1])] = y[x.index(row[1])] + 1
            else:
                x.append(row[1])
                y.append(1)

    plt.bar(x, y, color='g', width=0.72, label="Championships")
    plt.xlabel('Driver')
    plt.ylabel('Championships')
    plt.title('Number of championships per driver')
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt
import csv

x = []
y = []


def generate_graph(csvname):
    with open(csvname, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')  # Delimiter shall be adapted depending on the CSV file format.

        for row in plots:
            if row[1] in x:  # Check if driver has already appeared in the list.
                y[x.index(row[1])] = y[x.index(row[1])] + 1
            else:
                x.append(row[1])  # Append driver to the list to just increment his/her counter of championships.
                y.append(1)  # First championship for a given driver.

    plt.bar(x, y, color='g', width=0.72, label="Championships")  # Format of the bars of the graph.
    plt.xlabel('Driver')
    plt.ylabel('Championships')
    plt.xticks(rotation=90)  # Rotate for readability.
    plt.title('Number of championships per driver')
    plt.legend()
    plt.show()

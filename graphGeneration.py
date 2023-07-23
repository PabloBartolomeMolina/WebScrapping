import matplotlib.pyplot as plt
import csv

x = []
y = []

'''
# Function nos used within current functionalities
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
'''


def plot_yearVariation(stocks, currentYearVar, weekVar, monthVar, month3Var, month6Var, yearVar, year3Var, year5Var,
                       year10Var):
    index = 0
    for stock in stocks:
        varts = ['CurrentYear', '1 week', '1 month', '3 months', '6 months', '1 year', '3 years', '5 years', '10 years']
        # Get values in format 'float' to properly show them in the plots.
        counts = [float(currentYearVar[index].strip("%")), float(weekVar[index].strip("%")),
                  float(monthVar[index].strip("%")),
                  float(month3Var[index].strip("%")), float(month6Var[index].strip("%")),
                  float(yearVar[index].strip("%")),
                  float(year3Var[index].strip("%")), float(year5Var[index].strip("%")),
                  float(year10Var[index].strip("%"))]

        plt.ylim(min(counts), max(counts))
        plt.bar(varts, counts)
        plt.ylabel('Variation')
        plt.xticks(rotation=90)  # Make text of X-labels to appear vertically.
        strTitle = 'Variations stock "' + stock + '" (%)'
        plt.title(strTitle)
        for i in range(len(varts)):
            plt.text(i, counts[i] // 2, counts[i], ha='center', Bbox=dict(facecolor='white', alpha=85))
        plt.subplots_adjust()
        plt.tight_layout()

        plt.show()

        index = index + 1

import pandas as pd
# TODO: crear clase
import matplotlib.pyplot as plt


class DataLoader:
    def __init__(self, data):
        self.data = pd.read_csv(data)
        self.figure = plt.figure()

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'

    def show(self, ncolumns=None):
        """
        This function shows the data stored in self.data
        :type ncolumns: int
        :param ncolumns: Number of columns that you want to visualize, if empty will show all.
        """
        # TODO: Add a method for represent the data
        pd.set_option('display.max_columns', ncolumns)
        print(self.data.head())


dl = DataLoader('example.csv')
# dl.show()

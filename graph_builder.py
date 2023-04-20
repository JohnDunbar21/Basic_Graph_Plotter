from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from typing import List

class Graph:
    
    """
    Constructor generates a plot utilising the parameters passed in by the user.
    
    Best Fitted Curve is disabled by default, and must be enabled if it is required.
    """
    def __init__(self, x_axis: List[int], y_axis: List[int], x_units: str, y_units: str, title: str, x_label: str, y_label: str, best_curve=False) -> Figure:
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_units = x_units
        self.y_units = y_units
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.best_curve = best_curve
        return self.plot_data()
    
    """
    Creates the legend of the plot.
    
    Can also have best fitted curve if enabled.
    """    
    def generate_legend(self):
        if self.best_curve:
            legend = plt.legend([str(self.y_label), "Best Fitted Curve"], loc=1)
            return legend
        legend = plt.legend([str(self.y_label)], loc=1)
        return legend
    
    """
    Uses the numpy library to generate a polynomial best fitting curve using the
    axis values passed in the constructor
    """    
    def curve_fit(self):
        poly = np.polyfit(self.x_axis, self.y_axis, 2)
        p = np.poly1d(poly)
        return p(self.x_axis)
    
    """
    Plots the data and saves the file.
    """
    def plot_data(self):
        plt.figure(str(self.title))
        plt.title(str(self.title))
        plt.xlabel(str(self.x_label)+" ("+str(self.x_units)+")")
        plt.ylabel(str(self.y_label)+" ("+str(self.y_units)+")")
        plt.scatter(self.x_axis, self.y_axis, color="blue")
        if self.best_curve:
            plt.plot(self.x_axis, self.curve_fit(), color="red", linestyle="--")
        plt.grid()
        self.generate_legend()
        plt.savefig(str(self.title)+".png")
        plt.show()

#EXAMPLE USAGE
"""        
x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [0.7, 1.0, 1.9, 2.0, 2.3, 3.0, 3.9, 5.3, 6.8, 8.5, 9.1]
title = "Test"
x_l = "x_axis"
y_l = "y_axis"
        
Graph(x,"gra", y,"tis", title, x_l, y_l, True)
"""

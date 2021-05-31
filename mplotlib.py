import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""" 
    https://www.youtube.com/watch?v=wB9C0Mz9gSo&list=PLGLfVvz_LVvSX7fVd4OUFp_ODd86H0ZIY&index=84
"""

def main():
    simple_plots()

def simple_plots():
    x_1 = np.linspace(0,5,10)
    y_1 = x_1**2
    plt.plot(x_1,y_1)
    plt.show()


if __name__ == "__main__":
    main()
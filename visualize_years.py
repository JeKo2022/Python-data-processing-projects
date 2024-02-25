
# Minor AI: visualizing


from helpers import simple_get
from bs4 import BeautifulSoup
import re
import pandas as pd
from math import ceil
import argparse
import csv
import matplotlib.pyplot as plt

def main(input_file, output_file):
    '''
    generate a bar-plot years.png that show the average rating of the top
    5 movies per year (from 1930 to 2020).
    '''

    # read CSV file and create DataFrame
    input_df = pd.read_csv(input_file)

    # group by year compute average for every year
    grouped_df = input_df.groupby("YOR")
    group_means = grouped_df["rating"].mean()


    # get highest and lowest means for plotting
    best_average = group_means.max()
    lowest_average = group_means.min()

    # get best year
    best_year= group_means.idxmax()

    # plot relevant mean rating for YOR
    # matplotlib.pyplot.bar(x = bar positioning, y = height of bars, width = 0.8, bottom=None, *, align='center', data=None)
    plt.bar(group_means.index, group_means)
    plt.title(f"average movie rating per year: best year = {best_year}")
    plt.xlabel("years")
    plt.ylabel("ratings")

    # set y- axis to start around lowest_average for readibility
    plt.ylim(ymin = lowest_average - 0.25, ymax = best_average + 0.25)

    # save  DataFrame as a png file
    plt.savefig(output_file)


if __name__ == "__main__":

    # Create argument parses object
    parser = argparse.ArgumentParser(description = "visualizing top n movies")

    # Adding arguments
    parser.add_argument("input_file", help = "input file: (csv)")
    parser.add_argument("output_file", help = "output file: (csv)")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.input_file, args.output_file)

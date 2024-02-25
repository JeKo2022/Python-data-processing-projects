# Name: Jeanice Koorndijk
# Minor AI: transforming
# 22.11.2021

from helpers import simple_get
from bs4 import BeautifulSoup
import re
import pandas as pd
from math import ceil
import argparse
import csv

def main(input_file, output_file, Top_N_rated):
    '''
    creates a new file that contains a subset from movies.csv.
    filters the DataFrame such that it only contains the top N (default is 5)
    movies from every year.
    '''
    # read CSV file and create DataFrame with the data and labels from the file
    input_df_movies = pd.read_csv(input_file)

    # sort the values of the rating DataFrame
    sorted_movies = input_df_movies.sort_values("rating", ascending = False)

    # group by YOR
    grouped_sorted_movies = sorted_movies.groupby("YOR")

    # select top N rated movies from each YOR
    top_N_movies = grouped_sorted_movies.head(Top_N_rated)

    # sort by YOR
    top_N_movies = top_N_movies.sort_values("YOR", ascending = True)

    # save  DataFrame as a CSV file
    output_top_N_movies = top_N_movies.to_csv(output_file)

    return output_top_N_movies

if __name__ == "__main__":

    # Create argument parses object
    parser = argparse.ArgumentParser(description = "Transforming list to top n movies")

    # Adding arguments
    parser.add_argument("input_file", help = "output file: (csv)")
    parser.add_argument("output_file", help = "input file: (csv)")
    parser.add_argument("-n", "--Top_N_rated", type = int, default = 5, help = "top N rated movies (default: 5)")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.input_file, args.output_file, args.Top_N_rated)

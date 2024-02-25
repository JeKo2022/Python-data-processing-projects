# Name: Jeanice Koorndijk
# Minor AI: visualizing_actors
# 23.11.2021

from helpers import simple_get
from bs4 import BeautifulSoup
import re
import pandas as pd
from math import ceil
import argparse
import csv
import matplotlib.pyplot as plt
import numpy as np

def main(input_file, output_file):
    '''
    Function creates dictionaries for every movie on the list on the website.
    Using a for loop, relevant info is created added to specific dictionary.
    Function adds info of dicts into a dataframe creates a barplot of that df.
    '''

    # read input file into pandas DataFrame
    input_df = pd.read_csv(input_file)

    # set empty dictionary for actors (key) and occurences in list (values)
    dict_actors = {}

    # get individual actors and fill in dictionary
    str_actors = input_df['actors'].str.split(";")

    for list_actors in str_actors:
        if type(list_actors) is list:
            for actor in list_actors:
                if actor in dict_actors:
                    dict_actors[actor] += 1
                else:
                    dict_actors[actor] = 1

    # put dictionaries in dataframe
    column_names = ["occurences"]
    df_actors = pd.DataFrame.from_dict(dict_actors, orient = 'index', columns = column_names)
    top_50_df_actors = df_actors.sort_values(by = 'occurences', ascending = False).head(50)

    # plot barplot for actors and occurences (top 50)
    plt.bar(top_50_df_actors.index, top_50_df_actors["occurences"])
    plt.title("best actors")
    plt.xlabel("actors")
    plt.xticks(rotation = 90)
    plt.ylabel("occurences")

    #improve readability
    plt.ylim(ymin = 2)
    plt.subplots_adjust(bottom = 0.5)

    # save as png
    plt.savefig(output_file)

if __name__ == "__main__":

    # Create argument parses object
    parser = argparse.ArgumentParser(description = "visualizing actors")

    # Adding arguments
    parser.add_argument("input_file", help = "input file: (csv)")
    parser.add_argument("output_file", help = "output file: (png)")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.input_file, args.output_file)

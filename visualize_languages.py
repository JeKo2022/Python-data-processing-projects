
# Minor AI: crawler


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
    """
    Function creates nested dictionaries occurence of top 10 languages
    (of all time) for every decade.
    This is turned into dataframe and plotted as line plot.
    """

    # read CSV file and create DataFrame
    input_df = pd.read_csv(input_file)

    # create seperate df with only languages and split by semicolon
    languages_df = input_df[['languages', 'year']]
    languages_df['languages'] = languages_df['languages'].str.split(";")

    # explode for movies with multiple languages
    languages_df = languages_df.explode("languages")

    # count occurences of each language and select top 10
    language_count_top10 = languages_df["languages"].value_counts(ascending = False).head(10)

    # get df with decades
    languages_df["decades"] = languages_df["year"]//10*10

    # set empty dictionary for each languages
    # example: {'English': {1930: 43, 1940: 43,... 2010: 17},..}
    dict_language_searched = {}

    # get specific language
    for language_searched in language_count_top10.index:

        # declare empty dict for new language
        dict_decades = {}

        # create dict for every decade
        for decade in languages_df["decades"]:
            dict_decades[decade] = 0

        # add count to appropriate decade
        for language, decades in zip(languages_df.languages, languages_df.decades):
            if language == language_searched:
                dict_decades[decades] += 1

        # add dict decades to appropriate language
        dict_language_searched[language_searched] = dict_decades

    # put dictionary in dataframe
    df_top_decades = pd.DataFrame.from_dict(dict_language_searched, orient = 'index')

    # create line plot for languages and decades
    df_top_decades.T.plot.line()
    plt.title("the top 10 languages (that occur the most in our dataset) over time.")
    plt.xlabel("decades")
    plt.ylabel("languages")

    # save  dataFrame as a png file
    return plt.savefig(output_file)

if __name__ == "__main__":

    # Create argument parses object
    parser = argparse.ArgumentParser(description = "Web crawling for languages")

    # Adding arguments
    parser.add_argument("input_file", help = "output file: (csv)")
    parser.add_argument("output_file", help = "input file: (csv)")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.input_file, args.output_file)

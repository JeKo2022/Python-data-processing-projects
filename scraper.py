# Name: Jeanice Koorndijk
# Minor AI: scraper
# 17.11.2021

from helpers import simple_get
from bs4 import BeautifulSoup
import re
import pandas as pd
from math import ceil
import argparse
import csv

# set default imdb URL
IMDB_URL = 'https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced'

def main(output_file_name, start_year, end_year, n):
    '''
    Scrapes top movies from www.imdb.com between start_year and end_year.
    Continues scraping until at least a top 5 for each year can be created.
    Saves results to a CSV file.
    '''

    # Load website with BeautifulSoup
    html = simple_get(IMDB_URL)
    dom = BeautifulSoup(html, 'html.parser')

    # step 1: extracting a dataframe with relevant info about movies
    # extract dataframe with relevant info website
    movies_df = extract_movies(dom)

    # Save results to output file
    movies_df.to_csv(output_file_name, index=False)


    # step 2: scrape different URLs until at least 5 movies for every YOR.
    # set a counter to keep track of moviepages and navigate to next webpage
    count_movies = 1

    # set first URL
    current_URL = IMDB_URL

    # set evaluation to true to enter while loop for scraping
    evaluation = True

    # declare empty dataframe for use in while loop (large df)
    movies_df_N = pd.DataFrame()

    while evaluation == True:

        # adapt URL to start, end, and count
        current_URL = (f"https://www.imdb.com/search/title/?title_type=feature&release_date={start_year}-01-01,{end_year}-01-01&num_votes=5000,&sort=user_rating,desc&start={count_movies}&view=advanced")
        count_movies += 50

        # Load website with BeautifulSoup
        html = simple_get(current_URL)
        dom = BeautifulSoup(html, 'html.parser')

        # Extract dataframe with relevant info website and append to large df
        movies_df = extract_movies(dom)
        movies_df_N = movies_df_N.append(movies_df)

        # keep track of how many movies have been added for each YOR
        movie_count = movies_df_N["YOR"].value_counts()

        # get the YOR value count from the list with the lowest value.
        minimum_movies_year = movie_count.min()

        # see if lowest value is n to stop scraping (default: n = 5)
        minimum_amount = n - 1
        if minimum_movies_year > minimum_amount:
            evaluation = False

    #sort df by year
    movies_df_N = movies_df_N.sort_values(by="YOR", ascending = True)
    movies_df_N = movies_df_N.fillna("none")

    # Save results to output file
    movies_df_N.to_csv(output_file_name, index=False)

def extract_movies(dom):
    """
    Function creates dictionaries for every movie on the list on the website.
    Using a for loop, relevant info is created added to specific dictionary.
    Function adds info in each dict into a dataframe and returns that df.
    """

    # set empty lists and dictionary for scraped data (YOR = year of release)
    scraped_titles = []
    scraped_ratings = []
    scraped_YORs = []
    scraped_runtimes = []
    scraped_URLs = []
    list_dicts = []
    dict_movies = {}

    # get the all the info for the all the movies
    article = dom.find_all("div", class_ = "lister-item-content")

    # create loop to get relevant info for every movie
    for i in range(len(article)):

        # get title
        scraped_title = article[i].h3.a.text
        scraped_titles.append(scraped_title)

        # get rating
        rating = article[i].div.strong.text

        # get year of release (YOR) - strip YOR
        YOR = article[i].find("span", class_ = "lister-item-year text-muted unbold").text.strip("()")
        YOR = re.findall(r'\d+', YOR)
        YOR = "".join(YOR)
        YOR = int(YOR)

        # get credits
        credits = article[i].find("p", class_ = "")
        list_credits = credits.find_all("a", href = True)

        # remove director from credits
        actors = list_credits[1:]

        # empty actor list for new movie and get actors
        actor_list = []
        for actor in actors:
            actor_text = actor.get_text()
            actor_list.append(actor_text)

        # convert list of actors to string seperated by semicolon
        actors_str = ";".join(actor_list)

        # get runtime
        runtime = article[i].find("span", class_ = "runtime").text
        runtime = runtime.replace(" min", "")

        # get URL
        URL = article[i].find("a", href = True)['href']

        # put lists into dict for specific movie
        dict_movies[scraped_title] = [scraped_title, rating, YOR, actors_str, runtime, URL]

    # put dictionaries in dataframe
    column_names = ["scraped_title", "rating", "YOR", "actors", "runtime", "URL"]
    df_movies = pd.DataFrame.from_dict(dict_movies, orient = 'index', columns = column_names)

    return df_movies

if __name__ == "__main__":

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "extract top N movies from IMDB")

    # Adding arguments
    parser.add_argument("output", help = "output file (csv)")
    parser.add_argument("-s", "--start_year", type = int, default = 1930, help = "starting year (default: 1930)")
    parser.add_argument("-e", "--end_year", type = int, default = 2020, help = "starting year (default: 2020)")
    parser.add_argument("-m", "--n", type = int, default = 5, help = "top N")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.output, args.start_year, args.end_year, args.n)

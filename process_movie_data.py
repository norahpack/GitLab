#! /usr/bin/env python3
# A script that imports movie data and finds the top-5 highest grossing movies
import csv


def find_top_5(filename):
    """Finds the top 5 highest grossing movies in a CSV dataset.
       Input: filename, a string - points to filename of dataset
       Output: None
       Effect: should print five lines of text
    """
    # read in file contents as list of dictionaries
    with open(filename) as f:
        csvr = csv.DictReader(f)
        rows = [r for r in csvr]
    
    # Sort data and get top 5
    gross_sort = lambda x : int(x["Gross"])
    rows.sort(key=gross_sort)
    top_five = rows[:-6:-1]

    # Print out results
    for row in top_five:
        print("{row[Title]} ({row[Release Date]}) - ${row[Gross]}".format(
            row=row))


# Script to run
# Movie data comes from "Movie Gross and Ratings" dataset on Kaggle by Yashwanth Sharaf
# https://www.kaggle.com/datasets/thedevastator/movie-gross-and-ratings-from-1989-to-2014
if __name__ == "__main__":
    find_top_5("Movies_gross_rating.csv")

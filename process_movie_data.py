#! /usr/bin/env python3
# A script that imports movie data and finds the top-10 highest grossing movies
import csv


def find_top_10(filename):
    """Finds the top 10 highest grossing movies in a CSV dataset.
       Input: filename, a string - points to filename of dataset
       Output: None
       Effect: should print ten lines of text
    """
    # read in file contents as list of dictionaries
    with open(filename) as f:
        csvr = csv.DictReader(f)
        rows = [r for r in csvr]
    
    # Reformat some data types
    for row in rows:
        row["Gross"] = int(row["Gross"])
        row["Year"] = int(row["Release Date"][:4])

    # Sort data and get top 10
    gross_sort = lambda x : x["Gross"]
    rows.sort(key=gross_sort)
    top_ten = rows[:-11:-1]

    # Print out results
    for i, row in enumerate(top_ten):
        print("{ind}. {row[Title]} ({row[Year]}) - ${row[Gross]:,d}".format(
            ind=i+1,
            row=row))


# Script to run
# Movie data comes from "Movie Gross and Ratings" dataset on Kaggle by Yashwanth Sharaf
# https://www.kaggle.com/datasets/thedevastator/movie-gross-and-ratings-from-1989-to-2014
if __name__ == "__main__":
    find_top_10("Movies_gross_rating.csv")

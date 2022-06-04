# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(output_path, list_to_save):

    """Saves the CSV file to the specified output path. 
    
    Args: 
        Output_path (Path): Save CSV path

    Returns:
        A csv file that contains a filtered list of lists and saves it. 
    """

    header = list_to_save[0]

    output_path = Path("qualifying_loans.csv")

    with open(output_path, "w") as csvfile:
        #Creates the CSV writer
        csvwriter = csv.writer(csvfile, delimiter=",")

        #Writes the header to the CSV
        csvwriter.writerow(header)

        #Writes the data list to the CSV file
        for row in list_to_save:
            if row > list_to_save[0]:
                csvwriter.writerow(row)
        print(list_to_save)
    return list_to_save




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


def save_csv(output_path): 
    """This next function will use the csv library to save the qualifying data as a CSV file"""
    qualifying_loan = []
    output_path = Path("qualifying_loan.csv")
    header = ["Lender", "Max_loan_amount"]
    
    with open(output_path, "w", newline='') as csvfile:
        
        csvwriter = csv.write(csvfile) 
        
        csvwriter.writerow(header)

        for loan in qualifying_loan:
            csvwriter.writerow(loan.values())
        
    return qualifying_loan
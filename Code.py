# Author: Kem Meng
# Date: 06/09/2022

# Assumptions:
# the timestamps are ordered in date and time
# timestamps are in the interval of 0.5 hrs

# Import libraries here
from datetime import datetime
import pandas as pd
import numpy as np

# Build `wrangle` function
def wrangle(filepath):

    # Import the CSV file data into the DataFrame df.
    df = pd.read_csv(filepath, header=None)

    # Use the first column to create two separate columns in df: "timestamps" and "cars"
    df = df[0].str.split(" ", expand=True).rename(columns={0:"timestamps", 1:"cars"})

    # Make sure that the data type for these new column "cars" is int
    df["cars"] = df["cars"].astype('int64')

    # Convert the the data type for these new column "timestamps" to datetime
    #df["timestamps"] = pd.to_datetime(df["timestamps"], format="%Y-%m-%d %H:%M:%S")
    df["timestamps"] = pd.to_datetime(df["timestamps"], format="%Y-%m-%dT%H:%M:%S")
    

    # Sort data by "timestamps"
    df = df.sort_values("timestamps")

    return df


# Output the number of cars seen in total
def carsSeenInTotal(df):
    # alternative approach print(df.cars.sum())
    sum = 0
    for i in range(len(df)):
        sum += int(df["cars"][i])
    print("The number of cars seen in total:", sum)
    return sum


# Out put the number of cars seen on that day for all days listed in the input file
def carsSeenOnTheDay(df):
    carsPerday = df["timestamps"].astype(str).str.slice(0,10)
    print("\nThe number of cars seen on the day:\n", df.groupby(carsPerday).sum())
    return df.groupby(carsPerday).sum()
    
    
# Output the top 3 half hours with most cars, in the same format as the input file  
def topThree(df):
    df = df.sort_values("cars", ascending=False)

    # Make sure the 'timestamps' are the same format as the input file
    # (yyyy-mm-ddThh:mm:ss format, i.e. ISO 8601)
    df["timestamps"] = df["timestamps"].map(lambda x: x.isoformat())

    print("\nThe top 3 half hours with most cars:\n",df.head(3).to_string(index=False))
    return df.head(3).to_string(index=False)


# The 1.5 hour period with least cars (i.e. 3 contiguous half hour records)
def oneFiveHourPeriod(df):
    df["delta"] = df["timestamps"].diff(periods=2)
    df["check"] = df["delta"].astype(str).str.replace('0 days 01:00:00','yes')

    sum = 0
    dict = {}
    for i in range(len(df)):
        
        if(i >= 2):
            
            if(df["check"][i] == "yes" or df["check"][i] == "Nat"):
                sum = int(df["cars"][i] + df["cars"][i-2] + df["cars"][i-1])
                
                dict[str(df["timestamps"][i-2]) + "\n" + str(df["timestamps"][i-1]) + "\n" + str(df["timestamps"][i])] = sum
    
    print("\nThe 1.5 hour period with least cars:")
    print(min(dict, key=dict.get), "\nCars:", dict[min(dict, key=dict.get)])
    return dict[min(dict, key=dict.get)]






    
if __name__ == "__main__":

    df = wrangle("inputData.csv")

    carsSeenInTotal(df)

    carsSeenOnTheDay(df)

    topThree(df)

    oneFiveHourPeriod(df)

    #print(df)





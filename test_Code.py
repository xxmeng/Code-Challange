import unittest
from datetime import datetime
import pandas as pd
import numpy as np
from Code import wrangle, carsSeenInTotal, carsSeenOnTheDay, topThree, oneFiveHourPeriod

class TestWrangle(unittest.TestCase):

    def test_wrangle(self):
        filepath = "inputData.csv"
        testDf =  wrangle(filepath)
        self.assertAlmostEqual(wrangle("inputData.csv").info(), testDf.info())


    def test_carsSeenInTotal(self):
        testDf =  wrangle("inputData.csv")
        self.assertAlmostEqual(carsSeenInTotal(testDf), 398)

    
    def test_carsSeenOnTheDay(self):
        testDf =  wrangle("inputData.csv")
        df = carsSeenOnTheDay(testDf)
        self.assertAlmostEqual(df.iloc[1,0], 81)


    def test_topThree(self):
        testDf =  wrangle("inputData.csv")
        df = topThree(testDf)
        self.assertAlmostEqual(topThree(testDf), df)
        

    def test_oneFiveHourPeriod(self):
        testDf =  wrangle("inputData.csv")
        self.assertAlmostEqual(oneFiveHourPeriod(testDf), 31)
    



        

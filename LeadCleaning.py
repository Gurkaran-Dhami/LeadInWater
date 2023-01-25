#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:30:50 2023

@author: gurkarandhami
"""

import pandas as pd 
import datetime as datetime
import numpy as np 

LeadSample = pd.read_csv("LeadSamples.csv")
        

def CleaningYear(years):
    Amounts_dict = {}
    for rows in LeadSample.iterrows():
        dobj = datetime.datetime.strptime(rows[1][2], '%Y-%m-%d').date()
        dobj = dobj.strftime("%Y")
        if dobj == years:
            if rows[1][3] not in Amounts_dict:
                Amounts_dict[rows[1][3]] = [rows[1][4]]
            else:
                Amounts_dict[rows[1][3]].append(rows[1][4])
    
    Avg2014 = {}
    for vals in Amounts_dict:
        values = []
        for amounts in Amounts_dict[vals]:
            if str(amounts)[0] == '<':
                values.append(0)
            else: 
                values.append(float(amounts))
        
        Avg2014[vals] = np.mean(values)
    
    return Avg2014


Avg2014 = CleaningYear("2014")
Avg2015 = CleaningYear("2015")
Avg2016 = CleaningYear("2016")
Avg2017 = CleaningYear("2017")
Avg2018 = CleaningYear("2018")
Avg2019 = CleaningYear("2019")
Avg2020 = CleaningYear("2020")
Avg2021 = CleaningYear("2021")
Avg2022 = CleaningYear("2022")

def PopulatingClean(df, year):
    dict2014 = {}
    i = 0
    clean = pd.DataFrame(columns = ["PostalCode", "Year", "Amount"], 
                         index = list(range(1, len(df))))
    for vals in df: 
        dict2014["PostalCode"] = vals
        dict2014["Year"] = year
        dict2014["Amount"] = df[vals]
        clean.loc[i] = pd.Series(dict2014)
        i += 1
    return clean


CleanedLead2014 = PopulatingClean(Avg2014, "2014")
CleanedLead2015 = PopulatingClean(Avg2015, "2015")
CleanedLead2016 = PopulatingClean(Avg2016, "2016")
CleanedLead2017 = PopulatingClean(Avg2017, "2017")
CleanedLead2018 = PopulatingClean(Avg2018, "2018")
CleanedLead2019 = PopulatingClean(Avg2019, "2019")
CleanedLead2020 = PopulatingClean(Avg2020, "2020")
CleanedLead2021 = PopulatingClean(Avg2021, "2021")
CleanedLead2022 = PopulatingClean(Avg2022, "2022")

CleanedLead = CleanedLead2014.append(CleanedLead2015)
CleanedLead = CleanedLead.append(CleanedLead2016)
CleanedLead = CleanedLead.append(CleanedLead2017)
CleanedLead = CleanedLead.append(CleanedLead2018)
CleanedLead = CleanedLead.append(CleanedLead2019)
CleanedLead = CleanedLead.append(CleanedLead2020)
CleanedLead = CleanedLead.append(CleanedLead2021)
CleanedLead = CleanedLead.append(CleanedLead2022)

CleanedLead.to_csv("CleanedLeadFinal.csv")
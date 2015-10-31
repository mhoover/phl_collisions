""" This script takes in raw data from the city of Philadelphia on crashes
between 2011 and 2014, cleans the data up for analysis, and provides a 
pickled object for subsequent analytic use. It makes extensive use of 
Python's scientific capabilities and some custom functions found at 
github.com/mhoover/phl_collisions.
"""

# packages
import os
import pickle as pkl
import numpy as np
import pandas as pd
import seaborn as sns
from featurizer import make_binary_unk

# directory structure
dir = os.getcwd()
if not os.path.exists(dir + '/data'):
	os.makedirs(dir + '/data')
if not os.path.exists(dir + '/output'):
	os.makedirs(dir + '/output')

# raw data
crash = pd.read_csv(dir + '/data/phl_collisions_crash.csv', sep=None, 
                    engine='python')
person = pd.read_csv(dir + '/data/phl_collisions_person.csv', sep=None, 
                     engine='python')
road = pd.read_csv(dir + '/data/phl_collisions_roadway.csv', sep=None, 
                   engine='python')
vehicle = pd.read_csv(dir + '/data/phl_collisions_vehicle.csv', sep=None, 
                      engine='python')

# clean data
crash.SCH_BUS_IND = make_binary_unk(crash.SCH_BUS_IND, yesno=True)
crash.SCH_ZONE_IND = make_binary_unk(crash.SCH_ZONE_IND, yesno=True)

person.SEX = make_binary_unk(person.SEX, yesno=False)
person.TRANSPORTED = make_binary_unk(person.TRANSPORTED, yesno=True)
person(columns = {'SEX': 'female'}, inplace=True)

road.RDWY_ORIENT = road.RDWY_ORIENT.apply(lambda x: 'U' if (pd.isnull(x) or 
                                          x=='B') else x)

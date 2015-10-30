# raw data preparation
# written by: matt hoover (matthew.a.hoover@gmail.com)
# last edited: 17 oct 2015

# packages
import numpy as np
import pandas as pd
import seaborn as sns

# upfront matters
DIR = 'mhoover'

wd = '/Users/{}/Dropbox/ds/collisions/'.format(DIR)
dd = wd + 'data/'
od = wd + 'output/'

# data import
crash = pd.read_csv(dd + 'phl_collisions_crash.csv', sep=None, engine='python')
person = pd.read_csv(dd + 'phl_collisions_person.csv', sep=None, 
                     engine='python')
road = pd.read_csv(dd + 'phl_collisions_roadway.csv', sep=None, 
                   engine='python')
vehicle = pd.read_csv(dd + 'phl_collisions_vehicle.csv', sep=None, 
                      engine='python')



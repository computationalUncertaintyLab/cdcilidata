#mcandrew

import sys
import numpy as np
import pandas as pd

from weekpp.week import *

def fromEW2Season(w):
    w = str(w)
    yr,week = int(w[:4]), int(w[4:])

    if week >= 40:
        return "{:d}/{:d}".format(yr,yr+1)
    else:
        return "{:d}/{:d}".format(yr-1,yr)

if __name__ == "__main__":
 
    d = pd.read_csv("./ilidata_cdc_us_2020-07-22-15.csv")

    modelweeks = [ week(epiweek=str(w),modelweek=None).fromEpiWeek2ModelWeek().modelweek for w in d.epiweek.values]
    seasons    = [ fromEW2Season(w) for w in d.epiweek.values]
    
    d['modelweek'] = modelweeks
    d['season']    = seasons

    d.to_csv("./ilidata_cdc_us.csv")

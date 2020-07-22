#mcandrew

import sys
import numpy as np
import pandas as pd

from weekpp.week import *

if __name__ == "__main__":

    d = pd.read_csv("./ilidata_cdc_us.csv")

    def findPeakEW(x):
        ew   = x.sort_values("wili").iloc[0,:].epiweek
        ew   = str(ew)
        return ew
        
    peaks =  d.groupby(['season']).apply(findPeakEW)
    from40Peaks = peaks.apply( lambda x: week(epiweek=x).toFrom40Week().from40 )

    d = pd.concat([peaks,from40Peaks],1).rename(columns={0:"ew",1:'from40'})
    d.to_csv('seasonpeaks.csv')

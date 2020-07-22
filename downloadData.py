#mcandrew

import sys
import numpy as np
import pandas as pd

from downloadHelper.tools import *
from weekpp.week import *

if __name__ == "__main__":

    cdcDownloader = downloader(state="",region=['nat'])
    cdcDownloader.downloadILIdata().export("./ilidata_cdc_us")

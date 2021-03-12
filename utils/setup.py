import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
import math
from sklearn.cluster import KMeans
import seaborn as sns
from scipy import stats
from sklearn import metrics
from scipy.spatial.distance import cdist
from sklearn.neighbors import NearestNeighbors
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import parameters
import functions

if (cv. __version__ != "4.4.0"):
  print("Please install cv2 version 4.4.0")
  exit

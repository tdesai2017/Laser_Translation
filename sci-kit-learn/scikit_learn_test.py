import numpy as numpy
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


#as_matrix converts Dataframe to 2d array
data = pd.read_csv("train.csv").as_matrix()
clf = DecisionTreeClassifier()
#Everything except the first column (only using 21000/41999 images for this tutorial)
label_data = data[0:21000,1:]
#only the first column
labels = data[0:21000,0]


#looking at all data past 21000
# test_data = [0:21000,1:]
test_data = data[21000:,1:]


d = test_data[8]
#Each picture has 728 pixels --> d = 1d array --> sqrt(728) = 28 --> shapes it into a 28x28 image
#I think that this pixel software automatically creates a pixel map of 28x28 pixels, and uses that 
#for classification
d.shape = (28,28)
# for row in d:
#   print (row)
pt.imshow(255-d, cmap = 'gray')
pt.show()


"""
Syntax for array
data[rows, columns]
"""

print(d)





#digits.data --> provides all 'data' for each 'target'
"""
Example

Target: 0
Data: 
[ 0.  0.  5. 13.  9.  1.  0.  0.  0.  0. 13. 15. 10. 15.  5.  0.  0.  3.
 15.  2.  0. 11.  8.  0.  0.  4. 12.  0.  0.  8.  8.  0.  0.  5.  8.  0.
  0.  9.  8.  0.  0.  4. 11.  0.  1. 12.  7.  0.  0.  2. 14.  5. 10. 12.
  0.  0.  0.  0.  6. 13. 10.  0.  0.  0.]
"""


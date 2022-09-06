   1: >>> import pandas as pd
   2: >>> import numpy as np
   3: >>> df = pd.read_csv("mlbookcamp-code-master/mlbookcamp-code-master/chapter-02-car-price/data.csv")
   4: >>> lotus = df[df["Make"]=="Lotus"]
   5: >>> lotus_engines_cylinders = lotus[["Engine HP", "Engine Cylinders"]]
   6: >>> lotus_engines_cylinders.drop_duplicates()
      Engine HP  Engine Cylinders
3912      189.0               4.0
3913      218.0               4.0
3918      217.0               4.0
4216      350.0               8.0
4257      400.0               6.0
4259      276.0               6.0
4262      345.0               6.0
4292      257.0               4.0
4293      240.0               4.0
   7: >>> lotus_engines_cylinders.drop_duplicates().values
array([[189.,   4.],
       [218.,   4.],
       [217.,   4.],
       [350.,   8.],
       [400.,   6.],
       [276.,   6.],
       [345.,   6.],
       [257.,   4.],
       [240.,   4.]])
   8: >>> X = lotus_engines_cylinders.drop_duplicates().values
   9: >>> np.dot(X.T, X)
array([[7.31684e+05, 1.34100e+04],
       [1.34100e+04, 2.52000e+02]])
  10: >>> XTX = np.dot(X.T, X)
  11: >>> XTX_inv = np.linalg.inv(XTX)
  12: >>> y = np.array([1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800])
  13: >>> np.dot(XTX_inv, X.T) * y
array([[-1.45145106e+00,  2.27554657e-01,  1.71851173e-01,
        -3.55949211e+00,  5.80343386e+00, -2.39406462e+00,
         1.42221660e+00,  3.17391339e+00,  1.20098291e+00],
       [ 9.46982487e+01,  5.89254188e-01,  2.75982449e+00,
         2.16399957e+02, -2.77873207e+02,  1.51207962e+02,
        -5.18727169e+01, -1.48262613e+02, -5.12110350e+01]])
  14: >>> w = np.dot(XTX_inv, X.T) * y
  15: >>> w[0]
array([-1.45145106,  0.22755466,  0.17185117, -3.55949211,  5.80343386,
       -2.39406462,  1.4222166 ,  3.17391339,  1.20098291])
  16: >>> w[0].sum()
4.594944810094552
  17: >>> %history -n 1-17 -o -f homework1-question7.py -p

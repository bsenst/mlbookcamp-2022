   1: >>> import numpy as np
   2: >>> np.__version__
'1.20.2'
   9: >>> df = df.read_csv("mlbookcamp-code-master/mlbookcamp-code-master/chapter-02-car-price/data.csv")
  10: >>> df = pd.read_csv("mlbookcamp-code-master/mlbookcamp-code-master/chapter-02-car-price/data.csv")
  11: >>> df
          Make       Model  Year                Engine Fuel Type  Engine HP  ...  Vehicle Style highway MPG city mpg  Popularity   MSRP
0          BMW  1 Series M  2011     premium unleaded (required)      335.0  ...          Coupe          26       19        3916  46135
1          BMW    1 Series  2011     premium unleaded (required)      300.0  ...    Convertible          28       19        3916  40650
2          BMW    1 Series  2011     premium unleaded (required)      300.0  ...          Coupe          28       20        3916  36350
3          BMW    1 Series  2011     premium unleaded (required)      230.0  ...          Coupe          28       18        3916  29450
4          BMW    1 Series  2011     premium unleaded (required)      230.0  ...    Convertible          28       18        3916  34500
...        ...         ...   ...                             ...        ...  ...            ...         ...      ...         ...    ...
11909    Acura         ZDX  2012     premium unleaded (required)      300.0  ...  4dr Hatchback          23       16         204  46120
11910    Acura         ZDX  2012     premium unleaded (required)      300.0  ...  4dr Hatchback          23       16         204  56670
11911    Acura         ZDX  2012     premium unleaded (required)      300.0  ...  4dr Hatchback          23       16         204  50620
11912    Acura         ZDX  2013  premium unleaded (recommended)      300.0  ...  4dr Hatchback          23       16         204  50920
11913  Lincoln      Zephyr  2006                regular unleaded      221.0  ...          Sedan          26       17          61  28995

[11914 rows x 16 columns]
  12: >>> df["Make"].value_counts()
Chevrolet        1123
Ford              881
Volkswagen        809
Toyota            746
Dodge             626
Nissan            558
GMC               515
Honda             449
Mazda             423
Cadillac          397
Mercedes-Benz     353
Suzuki            351
BMW               334
Infiniti          330
Audi              328
Hyundai           303
Volvo             281
Subaru            256
Acura             252
Kia               231
Mitsubishi        213
Lexus             202
Buick             196
Chrysler          187
Pontiac           186
Lincoln           164
Oldsmobile        150
Land Rover        143
Porsche           136
Saab              111
Aston Martin       93
Plymouth           82
Bentley            74
Ferrari            69
FIAT               62
Scion              60
Maserati           58
Lamborghini        52
Rolls-Royce        31
Lotus              29
Tesla              18
HUMMER             17
Maybach            16
McLaren             5
Alfa Romeo          5
Spyker              3
Genesis             3
Bugatti             3
Name: Make, dtype: int64
  15: >>> len(df[df["Make"]=="Audi"]["Model"].unique())
34
  20:
>>> nans = 0
... for c in df.columns:
...     if df[c].hasnans:
...         nans += 1
... print(nans)
...
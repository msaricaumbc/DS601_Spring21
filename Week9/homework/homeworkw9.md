Each XLS or XLSX file contains a dataframe. 
Load each XLS or XLSX file in your Jupyter notebook. 
For each dataframe, address missing values by taking the following steps:
* Count the number of missing values in the dataframe; count the number of missing values per column
* Plot the distribution of data points using a histogram
* Create a lag plot (a lag plot shows t versus t+1)
* Based on the lag plot, state in a markdown cell whether the order of this data matters. 
* Do one of the following (not both):
  - If the order of the data matters, then interpolate the missing values
  - If the order of the data does not matter, fill in the missing data by sampling from the distribution
* Create a scatter plot using the columns in dataframe; no Nan entries should be present
Submit a single Jupyter notebook with your analysis of the XLS and XLSX files.

Perform interpolation or sampling programmatically using Python (not manually)
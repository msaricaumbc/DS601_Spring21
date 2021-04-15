# Homework: scaling file I/O experiment Part1


Write Python code that can create a CSV containing 10 columns of text data
Each entry in each row should be between 3 and 25 characters. The characters should be a mix of numeric and non-numeric. (Having all numeric data is not allowed.)
Adjacent rows in a CSV should not be the same
Generate files of size {0.1, 1, 5, 10, 100, 500} MB of data
Execution time for creating all of the CSV files should take less than 5 minutes.
Measure how much time it takes to write each CSV file to disk. In your measurement do not include the time used in creating the CSV files. Perform this measurement three times per file size. Each measurement is of a different CSV.
Measure how much time it takes for your computer to load the data into a Pandas dataframe. Perform this measurement three times per file size. Each measurement is of a different CSV.


Results: 
table of values (file size versus read time and write time for each experiment) 

Plot the average write times and average load times versus file size in a single plot


Submit your python notebook (.ipynb file) containing the code for the experiment and the results. 

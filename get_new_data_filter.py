#House Committee on Admin data http://disbursements.house.gov
#propublica historical data https://projects.propublica.org/represent/expenditures

import csv
import os

#rename sunlight columns to match fields with new house data
sunlight_header_new_col_names = ["BIOGUIDE_ID", "ORGANIZATION", "QUARTER", "SORT SUBTOTAL DESCRIPTION", "DATE", "VENDOR NAME", "PERFORM START DT", "PERFORM END DT", "DESCRIPTION", "AMOUNT", "YEAR", "TRANSCODE", "TRANSCODELONG", "TRANSCODEID", "RECORDID", "RECIP (orig.)"]
#list column headers in new house data
house_header_new_col_names = ['ORGANIZATION','PROGRAM','SORT SUBTOTAL DESCRIPTION','SORT SEQUENCE','TRANSACTION DATE','DATA SOURCE','DOCUMENT','VENDOR NAME','PERFORM START DT','PERFORM END DT','DESCRIPTION','AMOUNT']

#rewrite sunlight files with new col headers http://stackoverflow.com/questions/16306819/python-edit-csv-headers

sunlightFileNames = [
"2009Q3-detail.csv",
"2009Q4-detail.csv",
"2010Q1-detail.csv",
"2010Q2-detail.csv",
"2010Q3-detail.csv",
"2010Q4-detail.csv",
"2011Q1-detail.csv",
"2011Q2-detail.csv",
"2011Q3-detail.csv",
"2011Q4-detail.csv",
"2012Q1-detail.csv",
"2012Q2-detail.csv",
"2012Q3-detail.csv",
"2012Q4-detail.csv",
"2013Q1-detail.csv",
"2013Q2-detail.csv",
"2013Q3-detail.csv",
"2013Q4-detail.csv",
"2014Q1-detail.csv",
"2014Q2-detail.csv",
"2014Q3-detail.csv",
"2014Q4-detail.csv",
"2015Q1-detail.csv",
"2015Q2-detail.csv",
"2015Q3-detail.csv",
"2015Q4-detail.csv"
]

house_csv_files = [
"APR-JUNE-2016-SOD-DETAIL-GRID-REVISE-9_26_16.csv",
"OCT-DEC-2016-DETAIL-GRID.csv",
"JAN-MAR-2016-SOD-DETAIL-GRID_REVISED_9_26_16.csv",
"JULY-SEPT-2016-SOD-DETAIL-GRID.csv"
]

all_files = []

for fn in sunlightFileNames:

	outputFileName = os.path.splitext(fn)[0] + "_modified-to-filter.csv"
	all_files.append(outputFileName)

	with open(fn, newline='', encoding = "ISO-8859-1") as inFile, open(outputFileName, 'w', newline='', encoding = "ISO-8859-1") as outfile:

	    r = csv.reader(inFile)
	    w = csv.writer(outfile)

	    next(r, None)  # skip the first row from the reader, the old header
	    # write new header
	    w.writerow(sunlight_header_new_col_names)

	    # copy the rest
	    for row in r:
	        w.writerow(row)

for fn in house_csv_files:

	outputFileName = os.path.splitext(fn)[0] + "_modified-to-filter.csv"
	all_files.append(outputFileName)

	with open(fn, newline='', encoding = "ISO-8859-1") as inFile, open(outputFileName, 'w', newline='', encoding = "ISO-8859-1") as outfile:

	    r = csv.reader(inFile)
	    w = csv.writer(outfile)

	    next(r, None)  # skip the first row from the reader, the old header
	    # write new header
	    w.writerow(house_header_new_col_names)

	    # copy the rest
	    for row in r:
	    	if "TOTAL" not in row[3]: #get rid of total rows
	    		w.writerow(row)

#create variable with string file names for both old and new files to merge


#merge csvs with new files that have same col headers http://stackoverflow.com/questions/26599137/merge-csvs-in-python-with-different-columns



# First determine the field names from the top line of each input file
# Comment 1 below
fieldnames = []
for filename in all_files:
  with open(filename, "r", newline="", encoding = "ISO-8859-1") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        fieldnames.append(h)

fieldnames.append("DOCUMENT_FILE")

# Then copy the data
with open("filter_spending.csv", "w", newline="", encoding = "ISO-8859-1") as f_out:   # Comment 2 below
  writer = csv.DictWriter(f_out, fieldnames=fieldnames)
  f_out.write(",".join(fieldnames)+"\n")
  for filename in all_files:
    with open(filename, "r", newline="", encoding = "ISO-8859-1") as f_in:
      reader = csv.DictReader(f_in)  # Uses the field names in this file
      for line in reader:
      	#!!!! REPLACE FILTER ON NEXT LINE !!!!#
      	#!!!! REPLACE FILTER ON NEXT LINE !!!!#
      	#!!!! REPLACE FILTER ON NEXT LINE !!!!#
      	if 'REP.' in line['ORGANIZATION']: 
      		# Comment 3 below
      		line["DOCUMENT_FILE"] = filename
      		writer.writerow(line)
      	





# Comments from above:

# 1. You need to specify all the possible field names in advance to DictWriter, so you need to loop through all your CSV files twice: once to find all the headers, and once to read the data. There is no better solution, because all the headers need to be known before DictWriter can write the first line. This part would be more efficient using sets instead of lists (the in operator on a list is comparatively slow), but it won't make much difference for a few hundred headers. Sets would also lose the deterministic ordering of a list - your columns would come out in a different order each time you ran the code.
# 2. The above code is for Python 3, where weird things happen in the CSV module without newline="". Remove this for Python 2.
# 3. At this point, line is a dict with the field names as keys, and the column data as values. You can specify what to do with blank or unknown values in the DictReader and DictWriter constructors.




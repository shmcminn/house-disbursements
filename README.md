####House disbursement reports


Every quarter, the House of Representatives releases a .csv of its spending [here](http://disbursements.house.gov). The chamber started doing so in 2016, whereas before it would release a PDF file that the [Sunlight Foundation](http://www.sunlightfoundation.com) crawled and converted to a csv. 

This repo has the old Sunlight files as well as all 2016 data files included. To add new files from the House's quarterly releases, add their namesm as strings to the house_csv_files list.

The python script get_new_data.py combines them into a "master_spending.csv" file. get_new_data_filter.py does the same but allows filtering. create_file_subset_data.py is a type of filtering script as well, but only to view the first X number of lines in your file, and it assumes you already have your "master_spending.csv" file in the present working directory.

Lots of credit goes to StackOverflow commenters on these, with forum threads linked in the comments.

This is also my first github repo, so play nice as I figure out what I'm doing :) 

-Sean McMinn
Data reporter, CQ Roll Call
@shmcminn
seanmcminn@cqrollcall.com
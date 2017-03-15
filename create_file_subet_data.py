import csv

#note: relies on you creating master_spending.csv first, with get_new_data.py 
file_name = "master_spending.csv"

with open(file_name) as myfile:
    head = [next(myfile) for x in range(1)]
    print(head)

output_file = open('read_first_20.csv', 'w', encoding = "ISO-8859-1")

writer = csv.writer(output_file, delimiter=',')

with open(file_name, "r", encoding = "ISO-8859-1") as file:
    # use python's csv reader to access the contents
    # and create an object that represents the data
    csv_data = csv.reader(file)
    
    # write our header row to the output csv
    header_row = next(csv_data)
    
    writer.writerow(header_row)
    
    # loop through each row of the csv
    for i, row in enumerate(csv_data):
        
        # if statement
        # !!!! SET NUMBER BELOW TO DETERMINE HOW MANY ROWS TO SAVE!!!!#
        # !!!! SET NUMBER BELOW TO DETERMINE HOW MANY ROWS TO SAVE!!!!#
        # !!!! SET NUMBER BELOW TO DETERMINE HOW MANY ROWS TO SAVE!!!!#
        if i < 20:
            
            # write the row to the new csv file
            writer.writerow(row)

            
        # otherwise continue on
        else:
            continue
            
    # close the output file
    output_file.close()
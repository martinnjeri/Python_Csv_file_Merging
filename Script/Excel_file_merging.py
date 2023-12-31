import pandas as pd         # Import pandas for file reading and interpretation as pd
import glob                 # Import glob method which allows us to search files that match a specific pattern for this case csv file

files = glob.glob("..\Raw_Data/" + "*.csv")     # Specifiy the path the glod method is to search the pattern i.e "csv" files

frames = []                # Initialize an empty list where to add all the csv file

def csv_file_merge():

    for file in files:          # initialize a for loop to ilterate through the files generated by glob method

        data = pd.read_csv(file, header = 0, sep = ",") #read all the files using pandas and making them dataframes

        frames.append(data)     # Adding all the iterated csv panda read files into the empty list we create earlier above

    return frames

def writing_new_files():
    df = pd.concat(frames, ignore_index = True)     # Concatenate all the files appended in the empty files setting index to false



    df.to_excel("..\Output_Data/Merged_MOCK_DATA_excel.xlsx",header = True, index = False)
                # Writing a new excel file with a specified path
                # Set header to row 0 by header = 0
                # Set index to false


    df.to_csv("..\Output_Data/Merged_MOCK_DATA_csv.csv",sep = ",",header = True, index = False)
                # Writing a new csv file with a specified path
            # sep = ","
            # Set header to row 0 by header = 0
            # Set index to false

    return f"Merging of {len(files)} files {[file for file in files]} completed successfully!!"



csv_file_merge()
writing_new_files()

# y = input("Last: ")


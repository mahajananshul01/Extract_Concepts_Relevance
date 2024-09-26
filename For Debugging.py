import os
import pandas as pd

def read_text_files(path):
    # Initialize a list to store filename and text content
    data = []
    counter = 1
    
    # Loop through all files in the directory
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        
        # Check if it's a file and has a .txt extension
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            print(f"Processing file #{counter}: {file_name}")
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()  # Read the content of the file
                data.append([file_name, text])  # Append filename and text to the list
            counter += 1  # Increment the counter
    
    # Convert the list into a DataFrame
    df = pd.DataFrame(data, columns=['FileName', 'Text_Inside_File'])
    
    # Save the DataFrame as a CSV file
    csv_file_path = os.path.join(path, 'output_text_files.csv')
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    
    print(f"CSV file created: {csv_file_path}")
    
    # Return the DataFrame
    return df

# Example usage (you need to provide the path to your folder)
# df = read_text_files('/path/to/your/folder')

# To display the DataFrame
# print(df)









import os

def read_files_from_folder(folder_path):
    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a subfolder)
        if os.path.isfile(file_path):
            # Print the filename
            print(f"Reading file: {filename}")
            
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Print the content of the file (Optional)
                print(content)
                print('-' * 40)  # Just to separate output for readability

# Example usage
folder_path = '/path/to/your/folder'  # Replace with the actual folder path
read_files_from_folder(folder_path)





# Match "since beginning of this year" (r"since\s+(the\s+)?beginning\s+of\s+this\s+year", lambda m: (date(today.year, 1, 1), today)), # Match "since the beginning of this year" (r"since\s+(the\s+)?beginning\s+of\s+the\s+year", lambda m: (date(today.year, 1, 1), today)) 


from datetime import datetime, date

class DateRangeParser:
    @staticmethod
    def _parse_absolute_date(text: str) -> DateRange:
        parse_date = __class__._parse_date
        today = date.today()
        year = today.year
        patterns = [
            # Existing patterns like "from Aug 2023 till Mar 2024"
            (r"\bfrom\s+(\w+\s+\d{4})\s+(till|until)\s+(\w+\s+\d{4})",
             lambda m: (parse_date(m.group(1)), parse_date(m.group(3)))),
             
            # New pattern to match "this year" and "beginning of this year"
            (r"\bthis year\b", lambda _: (date(year, 1, 1), today)),
            (r"\bbeginning of this year\b", lambda _: (date(year, 1, 1), date(year, 1, 1))),
            
            # Other patterns for "since", "after", etc.
            (r"\bsince\s+(\w+\s+\d{4})", lambda m: (parse_date(m.group(1)), None)),
            (r"\bafter\s+(\w+\s+\d{4})\s+(till|until)\s+(\w+\s+\d{4})",
             lambda m: (parse_date(m.group(1)), parse_date(m.group(3)))),
        ]

        # Now iterate over the patterns to find a match
        for pattern, handler in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return handler(match)
        return None  # If no pattern matches, return None or handle appropriately

    @staticmethod
    def _parse_date(text: str) -> date:
        """This function would handle parsing the actual date string."""
        # Assuming this method already exists and parses date strings like "Aug 2023" into date objects
        pass






import pandas as pd
from datetime import timedelta

# Convert the 'PublishedDate' column to datetime
df_prod_metadata['PublishedDate'] = pd.to_datetime(df_prod_metadata['PublishedDate'], errors='coerce')

# Drop rows with NaN in 'PublishedDate'
df_prod_metadata = df_prod_metadata.dropna(subset=['PublishedDate'])

# Set the reference date to the maximum date in 'PublishedDate'
reference_date = df_prod_metadata['PublishedDate'].max()

# Calculate past month and past 6 months from the reference date
past_month = reference_date - timedelta(days=30.4 * 1)
past_6months = reference_date - timedelta(days=30.4 * 6)

# Filter the dataframe based on the date
df_tmp = df_prod_metadata.loc[df_prod_metadata['PublishedDate'] >= past_month]

# The rest of your code remains the same
past_month_num_list = []
past_month_perc_list = []

for tag in concept_tags_unique:
    num_with_tag = df_tmp.loc[df_tmp["Concept Tags"].str.contains(tag)].shape[0]
    perc_with_tag = num_with_tag / len(df_tmp)

    past_month_num_list.append(num_with_tag)
    past_month_perc_list.append(str(round(perc_with_tag * 100)) + '%')

output_table_1_df = pd.DataFrame()
output_table_1_df["Concept"] = concept_tags_unique
output_table_1_df["# of Docs this Month"] = past_month_num_list
output_table_1_df["% of Docs this Month"] = past_month_perc_list



******************


import pandas as pd
from datetime import datetime, timedelta

# Assuming df_prod_metadata is your dataframe and 'PublishedDate' is in datetime format
# Convert the 'PublishedDate' column to datetime if it's not already
df_prod_metadata['PublishedDate'] = pd.to_datetime(df_prod_metadata['PublishedDate'], errors='coerce')

# Get the reference date (max date in 'PublishedDate')
reference_date = df_prod_metadata['PublishedDate'].max()

# Calculate past month and past 6 months from the reference date
past_month = reference_date - timedelta(days=30.4 * 1)
past_6months = reference_date - timedelta(days=30.4 * 6)

print("Reference date is ->", reference_date)
print("Past month date is ->", past_month)
print("Past 6 months date is ->", past_6months)

# Now use past_month and past_6months to filter your dataframe
df_tmp = df_prod_metadata.loc[df_prod_metadata['PublishedDate'] >= past_month]











# Filter the dataframe based on the date
df_tmp = df_prod_metadata.loc[df_prod_metadata['PublishedDate'] >= past_month]

# Check if df_tmp is not empty
if len(df_tmp) > 0:
    past_month_num_list = []
    past_month_perc_list = []

    for tag in concept_tags_unique:
        num_with_tag = df_tmp.loc[df_tmp["Concept Tags"].str.contains(tag)].shape[0]
        perc_with_tag = num_with_tag / len(df_tmp)

        past_month_num_list.append(num_with_tag)
        past_month_perc_list.append(str(round(perc_with_tag * 100)) + '%')
else:
    # Handle the case where there are no documents in the filtered dataframe
    past_month_num_list = [0] * len(concept_tags_unique)
    past_month_perc_list = ['0%'] * len(concept_tags_unique)

output_table_1_df = pd.DataFrame()
output_table_1_df["Concept"] = concept_tags_unique
output_table_1_df["# of Docs this Month"] = past_month_num_list
output_table_1_df["% of Docs this Month"] = past_month_perc_list


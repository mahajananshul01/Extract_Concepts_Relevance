
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


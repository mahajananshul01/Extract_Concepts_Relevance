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


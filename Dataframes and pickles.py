import pandas as pd

#pieces of visit data split evenly
visits_part_1 = pd.read_pickle('web_visits_2017_part1.p')
visits_part_2 = pd.read_pickle('web_visits_2017_part2.p')

#final dataframes of visit and DL data
web_visit_df = pd.concat([visits_part_1, visits_part_2])  #316,806 pageviews (pdp and topics)
mmr_df = pd.read_pickle('Combined_MMR.p') #283,007 DLs

#combined dataframe
merged_df = pd.merge(mmr_df, web_visit_df, how='inner', on='VisitorGUID') #178.971

print(merged_df.head())
#TODO: combine duplicate columns.. or drop them and rename the ones with _x and _y
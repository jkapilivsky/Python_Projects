import pandas as pd
import pickle
import operator
import numpy as np

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




product_list = []
for product in merged_df['ProductFamily_x']:
    if product not in product_list:
        product_list.append(product)

def conversion():
    for prod in product_list:
        page_list =  []
        page_count = (merged_df['ProductFamily_x'] == prod).sum()
        DLs_count = (mmr_df['ProductFamily'] == prod).sum()
        #test_df = pd.DataFrame(data=page_count)
        #if page_count > 100 and DLs_count > 100:
        print(prod)
        print(DLs_count)
        print(page_count/DLs_count)


    #TODO sorted doesn't work!
    # jamie = sorted(page_count/DLs_count)
    # print(jamie)


def page_counter():
    products_list = []
    for product in merged_df['ProductFamily_x']:
        products_list.append(product)

    product_count = {}
    for product in products_list:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
    #for key, value in sorted(product_count.items(), key=operator.itemgetter(1), reverse=True):
        #print(value)
    return product_count


def download_counter():
    product_list = []
    for product in mmr_df['ProductFamily']:
        product_list.append(product)

    product_count = {}
    for product in product_list:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
    for key, value in sorted(product_count.items(), key=operator.itemgetter(1), reverse=True):
        print(key)
    return product_count









'''
mmr_dr columns

Day_Date                38482
Region                  38482
VisitorGUID             38482
IsFreeEmail             38482
NewToFranchise          38482
NumberOfProducts        38482
Product                 38482
ProductFamily           38482
Level2                  38482
IsCustomer              38482
IsNTF                   38482
IP_Address              38482
SiteID                  38482
Country                 38482
DQI                     34020
SpendRate               33406
Lead_Classification     38425
SalesVolume              7235
EmployeesTotal           7235
IsCore                  38482
IsElite8                38482
MintigoContactAdRank    35998
MintigoScore            35813'''

'''
web_visit columns
Region               533144
Weekday              533144
WebPagesId           533144
VisitDate            533144
IPAddress            533144
VisitorGUID          533144
TRK_SEG1             533144
Referring_Domains    510525
EntryPages           533141
Pages                533144
PageType             440305
Country              533144
Product              279602
ProductFamily        279602
SiteID               533144
Level_2              279602
IsSuspectedBot       533144
'''


'''
Merged_df columns 
Day_Date                178971
Region_x                178971
VisitorGUID             178971
IsFreeEmail             178971
NewToFranchise          178971
NumberOfProducts        178971
Product_x               178971
ProductFamily_x         178971
Level2                  178971
IsCustomer              178971
IsNTF                   178971
IP_Address              178971
SiteID_x                178971
Country_x               178971
DQI                     167221
SpendRate               160298
Lead_Classification     178727
SalesVolume              36167
EmployeesTotal           36167
IsCore                  178971
IsElite8                178971
MintigoContactAdRank    173768
MintigoScore            173041
Region_y                178971
Weekday                 178971
WebPagesId              178971
VisitDate               178971
IPAddress               178971
TRK_SEG1                178971
Referring_Domains       168944
EntryPages              178971
Pages                   178971
PageType                159091
Country_y               178971
Product_y               134471
ProductFamily_y         134471
SiteID_y                178971
Level_2                 134471
IsSuspectedBot          178971

'''



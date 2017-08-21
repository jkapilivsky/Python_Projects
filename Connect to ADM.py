import pyodbc
import pandas as pd
import pickle
import numpy as np

sdw_cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'sdw' , database = 'ADM')
sdw_cursor = sdw_cnxn.cursor()

stg_cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'aussdwstg01' , database = 'ADM')
stg_cursor = stg_cnxn.cursor()

#start of method 1
sql = '''

SELECT DISTINCT 
       [VisitDate]
      ,[VisitorGUID]
      ,[TRK_SEG1]
      ,[EntryPages]
      ,[Pages]
      ,[PageType]
      ,[Country]
      ,[Product]
      ,[ProductFamily]
      ,[SiteID]
      ,[Level_2]
FROM [ADM].[dbo].[vw_Tableau_NewWebPages]
Where (VisitDate >= '2017-01-01' and VisitDate <= '2017-08-15') 
  and SiteId = 1
  and Region = 'NA'
  and VisitorGUID is not null 
  and pages is not null 
  and Track_Seg is not Null 
  and Track_Seg != 'THW'
  and PageType in ('pdp', 'topics')
  and IsSuspectedBot = 0
  and ProductFamily is not null
     
'''

df = pd.read_sql(sql, stg_cnxn)
# a, b = np.vsplit(df, 2)
# pickle.dump(a,open('web_visits_2017_part1.p','wb'),protocol=pickle.HIGHEST_PROTOCOL)
# pickle.dump(b,open('web_visits_2017_part2.p','wb'),protocol=pickle.HIGHEST_PROTOCOL)

#pickle.dump(df,open('Combined_MMR.p','wb'),protocol=pickle.HIGHEST_PROTOCOL)


sdw_cnxn.close()
stg_cnxn.close()


#web_visit_pages...
'''
SELECT DISTINCT 
       [VisitDate]
      ,[VisitorGUID]
      ,[TRK_SEG1]
      ,[EntryPages]
      ,[Pages]
      ,[PageType]
      ,[Country]
      ,[Product]
      ,[ProductFamily]
      ,[SiteID]
      ,[Level_2]
FROM [ADM].[dbo].[vw_Tableau_NewWebPages]
Where (VisitDate >= '2017-01-01' and VisitDate <= '2017-08-15') 
  and SiteId = 1
  and Region = 'NA'
  and VisitorGUID is not null 
  and pages is not null 
  and Track_Seg is not Null 
  and Track_Seg != 'THW'
  and PageType in ('pdp', 'topics')
  and IsSuspectedBot = 0
  and ProductFamily is not null
  
  '''


#Combined_DL_MMR...
'''
SELECT DISTINCT [Day_Date]
      ,[Region]
      ,LOWER([VisitorGUID]) as VisitorGUID
      ,[IsFreeEmail]
      ,[NewToFranchise]
      ,[NumberOfProducts]
      ,[Product]
      ,[ProductFamily]
      ,[Level2]
      ,[IsCustomer]
      ,[IsNTF]
      ,[IP_Address]
      ,[SiteID]
      ,[Country]
      ,[DQI]
      ,[SpendRate]
      ,[Lead_Classification]
      ,[SalesVolume]
      ,[EmployeesTotal]
      ,[IsCore]
      ,[IsElite8]
      ,[MintigoContactAdRank]
      ,[MintigoScore]
  FROM [ADM].[dbo].[CombinedDownloads_MMR_BR]
   Where (Day_Date >= '2017-01-01' and Day_Date <= '2017-08-15')
   and siteid = 1
   and Region = 'NA'
   and VisitorGUID is not null
   and Track_Seg != 'THW'
   and VisitorGUID != '00000000-0000-0000-0000-000000000000'
   and ProductFamily is not null
   and Track_Seg is not null
  
  
  '''
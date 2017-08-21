import pyodbc


conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};' +
    ('SERVER={server},{port};'   +
     'DATABASE={database};'      +
     'TRUSTED_CONNECTION=yes').format(
            server= 'sdw',
              port= 1433,
          database= 'ADM')
)

print(conn)


# config = dict(server=   'localhost', # change this to your SQL Server hostname or IP address
#               port=      1433,                    # change this to your SQL Server port number [1433 is the default]
#               database='aussdwstg01',
#               username='TUL\jamie.kapilivsky',
#               password='!nst!nct330')
#
# print(config)
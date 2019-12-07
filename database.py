import pyodbc

server = '222.252.11.197,1433'
database = 'CHUAN_ERP_DATABASE' 
username = 'lamhien195' 
password = 'Hoplong6688' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

def get_connection():
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # print('Connection has been initial...')

        return cnxn
    except Exception as e:
        print('Connection error: ', e)
        return None

# get_connection()

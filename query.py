from database import get_connection
import pyodbc
import json
import decimal

connect = get_connection()

cursor = connect.cursor()

#Sample select query
# cursor.execute("SELECT * from KHO_XUAT_KHO WHERE NGAY_CHUNG_TU = '2019-12-03';") 
# cursor.execute("exec GetGiaNhapThapNhat('MH00229842')")
# cursor.execute("{call GetGiaNhapThapNhat(MH00229841)}")
sql = """\
{ CALL GetGiaNhapThapNhat (@tukhoa=?) }
"""
params = ('MH00229842')
cursor.execute(sql, params)

# rows = cursor.fetchone() 
rows = cursor.fetchall()
data = []
for row in rows:
    data.append([x for x in row])
# # # while row: 
# # #     print(row[0])
# # #     row = cursor.fetchone()
# # print(data)

# column_names = [column[0] for column in cursor.description]
# for row in rows:
#   data.append(dict(zip(column_names, row)))
# res = {
#     'price': data[0][]
#   }

def json_encode_decimal(obj):
  if isinstance(obj, decimal.Decimal):
    return str(obj)
  raise TypeError(repr(obj) + " is not JSON serializable")

d = json.dumps(data[0][3], default=json_encode_decimal)
d_1 = d.replace('"', '')

# print(data[0][3], type(data[0][3]))
print(type(rows), rows)
print(d)
print(d_1, type(d_1))
print(float(d_1))



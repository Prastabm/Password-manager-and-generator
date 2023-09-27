import oracledb

oracledb.init_oracle_client()
connection = oracledb.connect(user="prastab", password="mukhopadhyay", host="LAPTOP-2KQAITLT", port=1522, service_name= "orcl")
curs = connection.cursor()
sql="""insert into password (account, password)
             values(:acc, :psd)"""
curs.execute(sql, ["prastabm@gmail.com", "prastab123"])
connection.commit()
curs.execute("select * from password")
rows=curs.fetchall()
for row in rows:
    print(row)


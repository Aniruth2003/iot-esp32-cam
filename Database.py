import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

insert_query = 'INSERT INTO USERS VALUES (%s, %s, %s)'
search_query = 'select * from users where user_name = %s and user_password = %s'
select_query = 'SELECT * FROM users'

cur = connection.cursor()

data = ('admin', 'admin')

cur.execute(search_query, data)

# password = 'admin'
# name = 'admin'

user = cur.fetchall()
# print(user[1])
# for d in cur:
#     # print(d)
#     if id in d and name in d:
#         print(d)
    
connection.commit()

cur.close()
connection.close()
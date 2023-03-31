import pymysql
try:
    try:
        connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='niallipa',
            database='myself_bot',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Соединение с БД прошлои успешно.")
    except Exception as e:
        print(type(e), e)
        print("Соединение не удалось.")

    try:
        with connect.cursor() as cursor:
            sql_q = "SELECT * FROM myself_bot.users;"
            cursor.execute(sql_q)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print('#'*20)
    except Exception as e:
        print(type(e), e)
    finally:
        connect.close()
except Exception as e:
    print(type(e), e)
    print('1')

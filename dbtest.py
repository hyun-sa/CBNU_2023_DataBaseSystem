import pymysql


connect_info = pymysql.connect(host='192.168.56.101', port='4567', user='hyunsa', password='whalsdn1!', db='madang', charset='utf8')


with connect_info:
    with connect_info.cursor() as cursor:
        cursor.execute("INSERT INTO Book(bookid, bookname, publisher) VALUES(14, '스포츠 의학', 한솔의학서적');")
        connect_info.cummit()
        cursor.execute("SELECT * FROM book ORDER BY bookname")
        for data in cursor.fetchall():
            print(data)
        cursor.execute("DELETE FROM Book WHERE bookid = '11';")
        connect_info.cummit()
        cursor.execute("SELECT * FROM book ORDER BY bookname")
        for data in cursor.fetchall():
            print(data)


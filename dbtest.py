import pymysql


idx = -1
connect_info = pymysql.connect(host='192.168.56.101', port=4567, user='hyunsa', password='whalsdn1!', db='madang', charset='utf8')


def clear_screen():
    for _ in range(80):
        print()


def main_screen():
    global idx
    clear_screen()
    print("다음 항목을 선택하세요.")
    print("1. 책 추가")
    print("2. 책 삭제")
    print("3. 책 검색")
    print("4. 전체 책 조회")
    print("0. 종료")
    idx = int(input("번호 입력 : "))


def add_book():
    clear_screen()
    bnum = int(input("책 색인 번호를 입력하세요 : "))
    bname = input("책 이름을 입력하세요 : ")
    bpub = input("책 출판사를 입력하세요 : ")
    cursor.execute(f"INSERT INTO Book(bookid, bookname, publisher) VALUES({bnum}, '{bname}', '{bpub}');")
    connect_info.commit()
    print("추가되었습니다. Enter(Return)키를 입력하여 메인화면으로 돌아가십시오.")
    input()


def del_book():
    clear_screen()
    bnum = int(input("책 색인 번호를 입력하세요 : "))
    cursor.execute(f"DELETE FROM Book WHERE bookid = {bnum};")
    connect_info.commit()
    print("삭제되었습니다. Enter(Return)키를 입력하여 메인화면으로 돌아가십시오.")
    input()
    

def search_book():
    clear_screen()
    bnum = int(input("책 색인 번호를 입력하세요 : "))
    cursor.execute(f"SELECT * FROM Book WHERE bookid = {bnum};")
    for data in cursor.fetchall():
        print(data)
    print("검색되었습니다. Enter(Return)키를 입력하여 메인화면으로 돌아가십시오.")
    input()


def chk_book():
    clear_screen()
    cursor.execute(f"SELECT * FROM Book ORDER BY bookid")
    for data in cursor.fetchall():
        print(data)
    print("조회되었습니다. Enter(Return)키를 입력하여 메인화면으로 돌아가십시오.")
    input()


with connect_info:
    with connect_info.cursor() as cursor:
        while idx:
            main_screen()
            if idx == 1:
                add_book()
            elif idx == 2:
                del_book()
            elif idx == 3:
                search_book()
            elif idx == 4:
                chk_book()

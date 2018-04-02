from .pool import POOL
import pymysql
def select_time():
    conn = POOL.connection()
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql='select * from meetable.timeslot;'
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result
def select_room():
    conn = POOL.connection()
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql='select * from meetable.meetingroom;'
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

def filter_user(username,pwd):


    conn = POOL.connection()
    # print(conn)
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    # print(cursor)

    sql = "select * from meetable.userinfo where username=%s and password=%s;"
    cursor.execute(sql,(username,pwd))

    result = cursor.fetchone()
    print(result)

    conn.close()
    return result

def filter_record(time_str):
    conn = POOL.connection()
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql="select name,time_id,order_time,time_area,account,room_id,username from (select name,time_id,order_time,time_area,account,m.id as room_id from (select t.id as time_id,meet_room,order_time,time_area,account from meetable.orderrecord as o inner join meetable.timeslot as t on t.id = o.time_slot) as b inner join meetable.meetingroom as m on m.id = b.meet_room) as whl inner join meetable.userinfo as u on whl.account = u.id where order_time = %s;"
    cursor.execute(sql,(time_str,))
    result = cursor.fetchall()
    conn.close()
    return result

def insert(aid,mid,tid,otime):
    conn = POOL.connection()
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql = 'insert into meetable.orderrecord(account,meet_room,time_slot,order_time) values(%s,%s,%s,%s);'
    cursor.execute(sql,(aid, mid, tid, otime))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

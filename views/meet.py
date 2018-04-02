import time
from django.http import JsonResponse
from flask import session, Blueprint, request, render_template, redirect
from .utils import my_sql
import json

meetting = Blueprint("meet", __name__, template_folder="templates", static_folder="static", static_url_path="/static")


def get_room_time_data(time_list, room_list, time_str):
    # record_list = OrderRecord.objects.filter(order_time=time_str)
    record_list = my_sql.filter_record(time_str)
    data_dict = {}
    for item in room_list:
        data_dict[item.get("id")] = [
            {"name": item["name"], "isroom": True},
        ]
    for key, value in data_dict.items():
        for time_obj in time_list:
            dic = {"time_pk": time_obj["id"], "room_pk": key,
                   "order": None, "isbook": False}
            for item in record_list:
                if item["room_id"] == key and item["time_id"] == time_obj["id"]:
                    # print(1111)
                    dic = {
                        "username": item["username"], "room_name": item["name"],
                        "time_area": item["time_area"], "isbook": True, "room_pk": item["room_id"],
                        "time_pk": item["time_id"]
                    }
                    # print(dic)
            # print(dic)
            value.append(dic)
    # print(data_dict)
    return data_dict


@meetting.route("/app01/show/", methods=["GET", "POST"])
def show_meeting_room():
    if request.method == "GET":
        time_str = request.args.get("t")
        if not time_str:
            time_str = time.strftime('%Y-%m-%d', time.localtime())
        else:
            date_list = time_str.split("-")
            time_str = "-".join(reversed(date_list))
        time_list = my_sql.select_time()
        room_list = my_sql.select_room()
        _time=time_str.replace("-","年",1).replace("-","月",1) + "日"
        print(_time)
        data_dict = get_room_time_data(time_list, room_list, time_str)
        return render_template("show_room.html", time_list=time_list, room_list=room_list, data_dict=data_dict,time=_time)


@meetting.route("/app01/order/", methods=["POST", ])
def order():
    print(11111)
    t = request.form.get("time")
    print(t)
    if not t:
        time_str = time.strftime('%Y-%m-%d', time.localtime())
    else:
        date_list = t.split("-")
        time_str = "-".join(reversed(date_list))

    rpk = request.form.get("rpk")
    tpk = request.form.get("tpk")
    user_pk = session["user"]
    # OrderRecord.objects.create(account_id=user_pk,meet_room_id=rpk,time_slot_id=tpk,order_time=time_str)
    # aid, mid, tid, otime
    my_sql.insert(user_pk,rpk,tpk,time_str)
    ret = {"code":1000,"msg":"success"}
    return json.dumps(ret)


s = {1: [{'name': '一层会议室', 'isroom': True},
         {'username': 'whl', 'room_name': '一层会议室', 'time_area': '8：00--9：00', 'isbook': True, 'room_pk': 1,
          'time_pk': 1},
         {'time_pk': 2, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 3, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 4, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 5, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 6, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 7, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 8, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 9, 'room_pk': 1, 'order': None, 'isbook': False},
         {'time_pk': 10, 'room_pk': 1, 'order': None, 'isbook': False}],
     2: [{'name': '二层会议室', 'isroom': True},
         {'time_pk': 1, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 2, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 3, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 4, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 5, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 6, 'room_pk': 2, 'order': None, 'isbook': False},
         {'username': 'whl', 'room_name': '二层会议室', 'time_area': '14：00--15：00', 'isbook': True, 'room_pk': 2,
          'time_pk': 7},
         {'time_pk': 8, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 9, 'room_pk': 2, 'order': None, 'isbook': False},
         {'time_pk': 10, 'room_pk': 2, 'order': None, 'isbook': False}],
     3: [{'name': '三层会议室', 'isroom': True},
         {'time_pk': 1, 'room_pk': 3, 'order': None, 'isbook': False},
         {'time_pk': 2, 'room_pk': 3, 'order': None, 'isbook': False},
         {'time_pk': 3, 'room_pk': 3, 'order': None, 'isbook': False},
         {'username': 'alex', 'room_name': '三层会议室', 'time_area': '11：00--12：00', 'isbook': True, 'room_pk': 3,
          'time_pk': 4},
         {'time_pk': 5, 'room_pk': 3, 'order': None, 'isbook': False},
         {'time_pk': 6, 'room_pk': 3, 'order': None, 'isbook': False},
         {'time_pk': 7, 'room_pk': 3, 'order': None, 'isbook': False},
         {'time_pk': 8, 'room_pk': 3, 'order': None, 'isbook': False},
         {'username': 'alex', 'room_name': '三层会议室', 'time_area': '16：00--17：00', 'isbook': True, 'room_pk': 3,
          'time_pk': 9},
         {'time_pk': 10, 'room_pk': 3, 'order': None, 'isbook': False}],
     4: [{'name': '四层会议室', 'isroom': True},
         {'time_pk': 1, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 2, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 3, 'room_pk': 4, 'order': None, 'isbook': False},
         {'username': 'egon', 'room_name': '四层会议室', 'time_area': '11：00--12：00', 'isbook': True, 'room_pk': 4,
          'time_pk': 4},
         {'time_pk': 5, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 6, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 7, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 8, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 9, 'room_pk': 4, 'order': None, 'isbook': False},
         {'time_pk': 10, 'room_pk': 4, 'order': None, 'isbook': False}]}

v = [{'id': 1, 'time_area': '8：00--9：00'}, {'id': 2, 'time_area': '9：00--10：00'},
     {'id': 3, 'time_area': '10：00--11：00'}, {'id': 4, 'time_area': '11：00--12：00'},
     {'id': 5, 'time_area': '12：00--13：00'}, {'id': 6, 'time_area': '13：00--14：00'},
     {'id': 7, 'time_area': '14：00--15：00'}, {'id': 8, 'time_area': '15：00--16：00'},
     {'id': 9, 'time_area': '16：00--17：00'}, {'id': 10, 'time_area': '17：00--18：00'}]

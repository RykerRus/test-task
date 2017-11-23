# Программирование на языке высокого уровня (Python).
# Задание task_13_05_02. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!
import requests
import time
import matplotlib.pyplot as plt

def pop(data, url):
    result = [0, None]
    method = "friends.get"
    for a in data["response"]:
        try:
            b = len(requests.get((url + method),
                    {"user_id": a}).json()["response"])
            if b > result[0]:
                result = [b, a]
        except Exception as er:
            print("error", er)
            continue
    return result[1]

def friend_svyazi(data, token, url):
    result = [0, None, None]
    method = "friends.getMutual"
    i = 0
    for a in data["response"]:
        try:
            b = len(requests.get((url + method),
                                 {"target_uid": a,
                                  "access_token": token}).json()["response"])
            time.sleep(0.2)
            if b > result[0]:
                result = [b, a, i]
            i += 1
        except Exception as er:
            print("error 2", er)
            continue
    return result[1]

def data_plot(data):
    result = {}
    for a in data:
        if "universities" not in a or a["universities"] == []:
            continue
        if "name" in a["universities"][-1]:
            result[a["universities"][-1]["name"]] = (result.get(a["universities"][-1]
                                                     ["name"], 0) + 1)
    else:
        return result

class vk(object):
    def __init__(self, id_user, token):
        self._data = {"count": None, "list_friend": [], "friend_svyazi": None,
                      "friend_pop": None}
        self._url_m = "https://api.vk.com/method/"
        self._user_id = id_user
        self._access_token = token

    def __str__(self):
        string = ""
        pop = ""
        sv = ""
        for a in self._data["list_friend"]:
            string += ("Имя: {}\n"
                       "Фамилия: {}\n"
                       "id: {}\n"
                       "nick: {}\n"
                       "**********\n").format(a["first_name"],
                                              a["last_name"],
                                              a["uid"],
                                              a["nickname"])

            if a["uid"] == self._data["friend_pop"]:
                pop = ("Имя: {}\n"
                       "Фамилия: {}\n"
                       "id: {}\n"
                       "nick: {}\n").format(a["first_name"],
                                              a["last_name"],
                                              a["uid"],
                                              a["nickname"])
            if a["uid"] == self._data["friend_svyazi"]:
                sv = ("Имя: {}\n"
                       "Фамилия: {}\n"
                       "id: {}\n"
                       "nick: {}\n").format(a["first_name"],
                                              a["last_name"],
                                              a["uid"],
                                              a["nickname"])
        return ("Друзья:\n"
                "{}"
                "Количество друзей: {}\n"
                "Больше всего знакомых с: \n{}\n"
                "Самый популярный друг \n{}\n").format(string,
                                                    self._data["count"],
                                                    sv,
                                                    pop)

    def _load_info(self):
        r = requests.get((self._url_m + "friends.get"),
                         {"user_id": self._user_id,
                          "order": "hints",
                          "fields": "nickname,universities",
                          "name_case": "ins",
                          "access_token": self._access_token}).json()
        self._data["list_friend"] = r["response"]
        data_ = requests.get((self._url_m + "friends.get"), {"user_id": self._user_id}).json()
        self._data["friend_pop"] = (pop(data_, self._url_m))
        self._data["count"] = len(self._data["list_friend"])
        self._data["friend_svyazi"] = friend_svyazi(data_, self._access_token, self._url_m)

    def _makePlot(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title("Популярность университетов среди друзей")
        values = list()
        labels = list()
        for name, value in data_plot(self._data["list_friend"]).items():
            labels.append(name)
            values.append(value)
        # Смещение оси и легенды
        ax.pie(values, autopct="", radius=1.2)
        ax.set_position([0.2, 0.1, 1.5, 0.8])
        plt.legend(labels, bbox_to_anchor=(1., 0.8))
        ax.set_aspect("equal")
        fig.tight_layout()
        return fig

    def show_plot(self):
        self._makePlot()
        plt.show()

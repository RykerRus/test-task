from datetime import datetime
import shutil
import json
import os
import re
from distutils.dir_util import copy_tree


class Backup_manager:
    DATE_FORMAT = "%d.%m.%Y %H:%M:%S"

    def __init__(self):
        with open("settings.json", encoding="utf-8") as fh:
            self._settings = json.loads(fh.read())

    def copy(self, project_name):
        assert project_name in self._settings["projects"], \
            "Проекта с именем {} не существует".format(project_name)

        project = self._settings["projects"][project_name]

        if (project["options"]["confirm"]):
            answer = input("Вы действительно хотите совершить"
                           " копирование?(Для подтверждения введите"
                           " '+') - ")
            if (answer != "+"):
                return

        if (project["options"]["datetime_min"] != ""):
                project["options"]["datetime_min"] = \
                    datetime.strptime(project["options"]["datetime_min"],
                                      self.DATE_FORMAT)

        log_data = {}
        log_data["copy_start"] = datetime.now()
        log_data["files_amount"] = 0
        log_data["files_list"] = ""
        log_data["errors"] = ""

        for folder in project["folders"]:
            try:
                for f in os.scandir(path=folder["src"]):
                    if ((isinstance(project["options"]["datetime_min"],
                                    datetime))
                        and ((project["options"]["datetime_min"])) >
                            datetime.fromtimestamp(f.stat().st_mtime)):
                        continue

                    if (f.is_dir):
                        copy_tree(folder["src"], folder["dest"])
                    else:
                        shutil.copy2(folder["src"], folder["dest"])

                files = os.listdir(path=folder["src"])
                log_data["files_amount"] += len(files)
                log_data["files_list"] += ", ".join(files)
            except Exception as err:
                log_data["errors"] += str(err)

        log_data["copy_end"] = datetime.now()
        log_data["copy_time"] = log_data["copy_end"] - log_data["copy_start"]

        self._log(log_data)

    def _log(self, log_data):
        log_name = self._settings["log_filename"]

        with open(log_name, "a+", encoding="utf-8") as fh:
            fh.seek(0)
            data = fh.read()
            m = re.findall(r"Копирование №\d+", data)
            number = len(m) + 1
            log_str = ("Копирование №{}\n"
                       "  Начало копирования: {}\n"
                       "  Количество копируемых файлов: {}\n"
                       "  Список копируемых файлов: {}\n"
                       "  Конец копирования: {}\n"
                       "  Затраченное время: {}\n"
                       "  Ошибки: {}\n"
                       .format(number,
                               log_data["copy_start"]
                               .strftime(self.DATE_FORMAT),
                               log_data["files_amount"],
                               log_data["files_list"],
                               log_data["copy_end"]
                               .strftime(self.DATE_FORMAT),
                               log_data["copy_time"],
                               log_data["errors"]))

            print(log_str)
            fh.write(log_str)

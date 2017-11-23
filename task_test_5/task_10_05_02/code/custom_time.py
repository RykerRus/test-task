import json
import re


class Time:
    HOUR_MIN = 0
    HOUR_MAX = 24
    MINUTE_MIN = 0
    MINUTE_MAX = 60
    SECOND_MIN = 0
    SECOND_MAX = 60
    MICROSECOND_MIN = 0
    MICROSECOND_MAX = 1000000

    def __init__(self, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        if not ((isinstance(hour, int)) and (isinstance(minute, int)) and
                (isinstance(second, int)) and (isinstance(microsecond, int))
                and (isinstance(tzinfo, str) or tzinfo is None)):
                    raise ValueError("Агрументы не соответствуют"
                                     " необходимому типу!")
        if not ((self.HOUR_MIN <= hour < self.HOUR_MAX) and
                (self.MINUTE_MIN <= minute < self.MINUTE_MAX) and
                (self.SECOND_MIN <= second < self.SECOND_MAX) and
                (self.MICROSECOND_MIN <= microsecond < self.MICROSECOND_MAX)):
            raise ValueError("Нарушение границ допустимых значений!")

        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        self._tzinfo = tzinfo

        if (tzinfo):
            m = re.search(r"\s*(?P<tzname>\w+)(?P<operator>[+-])"
                          "(?P<hour>\d{1,2}):(?P<minute>\d{1,2})", tzinfo)
            self._tzinfo = None

            if (m):
                self._tzinfo = m.groupdict()
                self._tzinfo["hour"] = int(self._tzinfo["hour"])
                self._tzinfo["minute"] = int(self._tzinfo["minute"])

    def __str__(self):
        hour = self._hour
        minute = self._minute
        second = self._second

        if (self.hour < 10):
            hour = "0{}".format(hour)
        if (self.minute < 10):
            minute = "0{}".format(minute)
        if (self.second < 10):
            second = "0{}".format(second)

        time_str = "{}:{}:{}".format(hour, minute, second)

        if (self._microsecond):
            microsecond = self._microsecond
            microsecond_len = len(str(microsecond))

            if (microsecond_len < 6):
                zero_amount = 6 - microsecond_len
                zeros = "0" * zero_amount
                microsecond = "{}{}".format(zeros, microsecond)

            time_str = "{}.{}".format(time_str, microsecond)

        if (self._tzinfo):
            time_str = "{} {}{}".format(time_str, self._tzinfo["tzname"],
                                        self.utcoffset())

        return time_str

    def __bool__(self):
        return bool(self._to_minutes())

    def __eq__(self, other):
        if not (isinstance(other, Time)):
            return False

        return ((self._hour == other.hour) and
                (self._minute == other.minute) and
                (self._second == other.second) and
                (self._microsecond == other.microsecond))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not (isinstance(other, Time)):
            raise TypeError("Сравнение возможно только с экземпляром класса"
                            " Time!")

        return self._to_minutes() < other._to_minutes()

    def __gt__(self, other):
        if not (isinstance(other, Time)):
            raise TypeError("Сравнение возможно только с экземпляром класса"
                            " Time!")

        return self._to_minutes() > other._to_minutes()

    def __le__(self, other):
        if not (isinstance(other, Time)):
            raise TypeError("Сравнение возможно только с экземпляром класса"
                            " Time!")

        return self._to_minutes() <= other._to_minutes()

    def __ge__(self, other):
        if not (isinstance(other, Time)):
            raise TypeError("Сравнение возможно только с экземпляром класса"
                            " Time!")

        return self._to_minutes() >= other._to_minutes()

    def __hash__(self):
        return int(self._to_minutes())

    @classmethod
    def from_string(cls, str_value):
        # format "00:00:00", "00:00:00.000000", "00:00:00.000000 UTC+3:0"

        if not(isinstance(str_value, str)):
            raise TypeError("Аргумент должен быть строкой")

        m = re.search(r"(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)",
                      str_value)

        if not (m):
            raise ValueError("Не удалось создать экземпляр класса из строки")

        result = m.groupdict()
        hour = int(result["hour"])
        minute = int(result["minute"])
        second = int(result["second"])

        m2 = re.search(r"\.(?P<microsecond>\d+)", str_value)

        if (m2):
            result["microsecond"] = m2.groupdict()["microsecond"]
            microsecond = int(result["microsecond"])

            m3 = re.search(r"(?P<tzinfo>\s\w+[+-]\d{1,2}:\d{1,2})",
                           str_value)

            if (m3):
                tzinfo = m3.groupdict()["tzinfo"]

                return cls(hour, minute, second, microsecond, tzinfo)

            return cls(hour, minute, second, microsecond)

        return cls(hour, minute, second)

    def _to_minutes(self):
        minutes = ((self._hour * 60) + self._minute + (self._second / 60)
                   + (self._microsecond / 1000000 / 60))

        if (self._tzinfo):
            tz_minutes = self._tzinfo["hour"] * 60 + self._tzinfo["minute"]

            if (self._tzinfo["operator"] == "+"):
                minutes += tz_minutes
            else:
                minutes -= tz_minutes

        return minutes

    def save(self, filename):
        if not (isinstance(filename, str)):
            raise TypeError("Имя файла должно быть строкой!")

        with open("{}.json".format(filename), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(str(self), ensure_ascii=False, indent=4))

    def load(self, filename):
        if not (isinstance(filename, str)):
            raise TypeError("Имя файла должно быть строкой!")

        try:
            with open("{}.json".format(filename), encoding="utf-8") as fh:
                time_str = json.loads(fh.read())

                return self.from_string(time_str)
        except Exception as err:
            print("При загрузке файла произошла ошибка {}!".format(err))

    def isoformat(self):
        return self.__str__()

    def utcoffset(self):
        if (self._tzinfo):
            tz_hour = self._tzinfo["hour"]
            tz_minute = self._tzinfo["minute"]

            if (tz_hour < 10):
                tz_hour = "0{}".format(tz_hour)
            if (tz_minute < 10):
                tz_minute = "0{}".format(tz_minute)

            return "{}{}:{}".format(self._tzinfo["operator"], tz_hour,
                                    tz_minute)

    def tzname(self):
        if (self._tzinfo):
            return self._tzinfo["tzname"]

    @property
    def min(self):
        return str(Time())

    @property
    def max(self):
        return str(Time(23, 59, 59, 999999))

    @property
    def resolution(self):
        return str(Time(0, 0, 0, 1))

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @property
    def microsecond(self):
        return self._microsecond

    @property
    def tzinfo(self):
        return self._tzinfo

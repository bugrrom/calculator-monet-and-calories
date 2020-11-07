import datetime as dt


class Record:
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit

from datetime import datetime


def parseTime(timeStr):
    dt = datetime.strptime(timeStr, "%Y-%m-%dT%H:%M")
    return dt.timestamp()

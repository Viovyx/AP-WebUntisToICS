from datetime import timedelta
import requests_cache
import json
from src.mappers import mapClass, mapDay

baseUrl = "https://ap.webuntis.com/WebUntis/api/rest/view/v1"
headers = {"anonymous-school": "ap"}
session = requests_cache.CachedSession(cache_name="/tmp/cache", backend="sqlite")


def getClasses():
    url = baseUrl + "/timetable/filter"
    params = {"resourceType": "CLASS"}

    response = session.get(
        url=url, params=params, headers=headers, expire_after=timedelta(weeks=1)
    )
    data = response.json()
    classes = data["classes"]

    return list(map(mapClass, classes))


def getCurrentSchoolYear():
    url = baseUrl + "/schoolyears"

    response = session.get(url=url, headers=headers, expire_after=timedelta(weeks=1))
    data = response.json()[0]
    dates = data["dateRange"]

    return (dates["start"], dates["end"])


def getTimeTable(classId):
    url = baseUrl + "/timetable/entries"
    (start, end) = getCurrentSchoolYear()
    params = {
        "resourceType": "CLASS",
        "start": str(start),
        "end": str(end),
        "resources": int(classId),
    }

    response = session.get(
        url=url, params=params, headers=headers, expire_after=timedelta(minutes=15)
    )
    data = response.json()

    return list(map(mapDay, data["days"]))


def getLessons(classId):
    lessons = []
    timetable = getTimeTable(classId)

    for day in timetable:
        entries = day["entries"]

        if len(entries) > 0:
            for entry in entries:
                lessons.append(entry)

    return lessons

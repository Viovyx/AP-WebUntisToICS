from datetime import timedelta, datetime
import requests_cache
import json

baseUrl = "https://ap.webuntis.com/WebUntis/api/rest/view/v1"
headers = {"anonymous-school": "ap"}
session = requests_cache.CachedSession("cache")
thisClass = ""


def getClasses():
    url = baseUrl + "/timetable/filter"
    params = {"resourceType": "CLASS"}

    response = session.get(
        url=url, params=params, headers=headers, expire_after=timedelta(weeks=1)
    )
    data = response.json()
    classes = data["classes"]

    return list(map(mapClass, classes))


def mapClass(classData):
    return {"id": classData["class"]["id"], "name": classData["class"]["displayName"]}


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


def mapDay(day):
    global thisClass
    thisClass = day["resource"]["shortName"]
    entries = list(map(mapEntry, day["gridEntries"]))

    return {"date": day["date"], "entries": entries}


def mapEntry(entry):
    global thisClass
    classes = [
        el["current"]["displayName"]
        for el in (entry["position5"] if entry["position5"] else [])
    ]
    classes.append(thisClass)
    classes.sort()

    locations = [
        el["current"]["shortName"]
        for el in (entry["position3"] if entry["position3"] else [])
    ]

    return {
        "start": parseTime(entry["duration"]["start"]),
        "end": parseTime(entry["duration"]["end"]),
        "info": entry["lessonInfo"],
        "teacher": entry["position1"][0]["current"]["longName"],
        "subject": entry["position2"][0]["current"]["longName"],
        "locations": locations,
        "classes": classes,
    }


def parseTime(timeStr):
    dt = datetime.strptime(timeStr, "%Y-%m-%dT%H:%M")
    return dt.timestamp()


def getLessons(classId):
    lessons = []
    timetable = getTimeTable(classId)

    for day in timetable:
        entries = day["entries"]

        if len(entries) > 0:
            for entry in entries:
                lessons.append(entry)

    return lessons

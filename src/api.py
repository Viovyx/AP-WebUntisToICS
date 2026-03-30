from datetime import timedelta
import requests_cache

baseUrl = "https://ap.webuntis.com/WebUntis/api/rest/view/v1"
session = requests_cache.CachedSession("cache", expire_after=timedelta(days=1))


def getClasses():
    url = baseUrl + "/timetable/filter"
    params = {"resourceType": "CLASS"}
    headers = {"anonymous-school": "ap"}

    response = session.get(url=url, params=params, headers=headers)
    data = response.json()
    classes = data["classes"]

    return list(map(mapClass, classes))


def mapClass(classData):
    return {"id": classData["class"]["id"], "name": classData["class"]["displayName"]}

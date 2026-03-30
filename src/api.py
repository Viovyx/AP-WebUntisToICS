from datetime import timedelta
import requests_cache

baseUrl = "https://ap.webuntis.com/WebUntis/api/rest/view/v1"
session = requests_cache.CachedSession("cache")


def getClasses():
    url = baseUrl + "/timetable/filter"
    params = {"resourceType": "CLASS"}
    headers = {"anonymous-school": "ap"}

    response = session.get(
        url=url, params=params, headers=headers, expire_after=timedelta(weeks=1)
    )
    data = response.json()
    classes = data["classes"]

    return list(map(mapClass, classes))


def mapClass(classData):
    return {"id": classData["class"]["id"], "name": classData["class"]["displayName"]}

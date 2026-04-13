from src.helpers import parseTime


def mapClass(classData):
    return {"id": classData["class"]["id"], "name": classData["class"]["displayName"]}


def mapDay(day):
    thisClass = day["resource"]["shortName"]
    gridEntries = day["gridEntries"]
    entries = list(map(mapEntry, gridEntries, [thisClass] * len(gridEntries)))

    return {"date": day["date"], "entries": entries}


def mapEntry(entry, thisClass):
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

from datetime import datetime


def parseTime(timeStr):
    dt = datetime.strptime(timeStr, "%Y-%m-%dT%H:%M")
    return dt.timestamp()


def entriesSimilar(entry1, entry2):
    if entry1 == None:
        return

    if entry1["subject"] == entry2["subject"] and entry1["info"] == entry2["info"]:
        # Same event
        if entry1["start"] == entry2["start"] and entry1["end"] == entry2["end"]:
            # Same time
            return "same"
        elif entry1["end"] == entry2["start"]:
            # Combine events
            return "combine"
    else:
        return


def mergeEntries(entry1, entry2):
    thingsToMerge = ["teachers", "locations", "classes"]

    for thing in thingsToMerge:
        if entry1[thing] != entry2[thing]:
            entry1[thing] += entry2[thing]
            # Remove possible duplicates and sort
            entry1[thing] = list(dict.fromkeys(entry1[thing]))
            entry1[thing].sort()

    return entry1

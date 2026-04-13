from icalendar import Calendar, Event
from src.api import getLessons
from datetime import datetime
import pytz


def generateCalendar(classId):
    lessons = getLessons(classId)

    cal = Calendar()
    cal.add("prodid", "-//WebUntis Sync//webuntis-sync//EN")
    cal.add("version", "2.0")
    cal.add("x-wr-calname", "WebUntis Timetable")
    cal.add("x-wr-timezone", "Europe/Brussels")
    timezone = pytz.timezone("Europe/Brussels")

    for lessonId in range(len(lessons)):
        lesson = lessons[lessonId]
        event = Event()

        summary = lesson["subject"]
        uid = f"{lessonId}-{lesson["start"]}-{summary}@webuntis-sync"
        descriptionLines = [
            lesson["teacher"],
            " / ".join(lesson["classes"]),
        ]

        if lesson["info"]:
            descriptionLines.append("-" * 20)
            descriptionLines.append(f"ℹ️ {lesson["info"]}")
            summary += f" ({lesson["info"]})"

        event.add("summary", summary)
        event.add("description", "\n".join(descriptionLines))
        event.add("location", " / ".join(lesson["locations"]))
        event.add("dtstart", timezone.localize(datetime.fromtimestamp(lesson["start"])))
        event.add("dtend", timezone.localize(datetime.fromtimestamp(lesson["end"])))
        event.add("uid", uid)

        cal.add_component(event)

    return cal.to_ical()

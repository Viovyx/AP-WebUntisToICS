# [ap.webuntis.viovyx.com](https://ap.webuntis.viovyx.com/)

Easy to use .ics generator for importing your Webuntis calendar into your own calendar app.

## Usage
1. Go to the public url above
2. Find and select your class
3. Import the link in your calendar app of choice
   
This will sync with WebUntis whenever your client syncs the url.

### Tested clients
| Client | Rating | Reasoning |
|---|---|---|
| [Google calendar](https://calendar.google.com) | 3/5 | Very inconsistend syncing, no force sync. Widely available. 
| [Nextcloud calendar](https://apps.nextcloud.com/apps/calendar) | 4/5 | Inconsistend syncing, no force sync. Only on web.
| [ICSx⁵](https://github.com/bitfireAT/icsx5) | 5/5 | Syncs consistently, force sync option. Only on Android.

Theoretically this should work in any calendar client that supports importing from url and some might have better results, these are just the ones I've tested myself with my experience.

## Disclaimers
There is a built in cache that clears every 15min to prevent hitting a possible rate limit from WebUntis.

The public url is hosted using [Vercel](https://vercel.com/), so it is possible that it becomes unreachable from hitting the usage limit.
You can always fork and host this project yourself ofcourse.

Made to work for [AP Hogeschool WebUntis](https://ap.webuntis.com/)

## Issues
If you run into a bug or issue (that is not related to the [the disclaimers](#disclaimers)), please create an issue [here](https://github.com/Viovyx/AP-WebUntisToICS/issues), and I'll do my best to resolve it.

---
#### Credits
> I got inspiration from [this](https://github.com/K41680/WebUntisSync) original project, which I had been using up until I made this.

# [ap.webuntis.viovyx.com](https://ap.webuntis.viovyx.com/)

Easy to use .ics generator for importing your Webuntis calendar into your own calendar app.

> [!NOTE]
> **New feature: [Merging similar events](https://github.com/Viovyx/AP-WebUntisToICS/commit/3f6a658351f80b2a19f5602ab7ac850d1721ccf2)**
>
> Events that are duplicate (ex. same time & subject) will now be merged together.
> 
> I've done my best to triple check this features functionality but it may not work as expected for some edge cases.
> 
> If you notice that events are being merged incorrectly please create an issue and explain what's incorrect.

## Usage

1. Go to the public url above
2. Find and select your class
3. Import the link in your calendar app of choice

This will sync with WebUntis whenever your client syncs the url.

### Tested clients

| Client                                                         | Comment                                                     |
| -------------------------------------------------------------- | ----------------------------------------------------------- |
| [Google calendar](https://calendar.google.com)                 | Very inconsistend syncing, no force sync. Widely available. |
| [Nextcloud calendar](https://apps.nextcloud.com/apps/calendar) | Inconsistend syncing, no force sync. Only on web.           |
| [ICSx⁵](https://icsx5.bitfire.at/)                    | Syncs consistently, force sync option. Only on Android.     |

Theoretically this should work in any calendar client that supports importing from url and some might have better results, these are just the ones I've tested myself with my experience.

## Disclaimers

There is a built in cache that clears every 15min to prevent hitting a possible rate limit from WebUntis.

Made to work for [AP Hogeschool WebUntis](https://ap.webuntis.com/)

## Issues

If you run into a bug or issue (that is not related to the [the disclaimers](#disclaimers)), please create an issue [here](https://github.com/Viovyx/AP-WebUntisToICS/issues), and I'll do my best to resolve it.

---

#### Credits

> I got inspiration from [this](https://github.com/K41680/WebUntisSync) original project, which I had been using up until I made this.

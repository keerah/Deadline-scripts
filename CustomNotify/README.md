# Custom notify
 
 This is a custom event plugin for Deadline that allows flexible email notifications about the jobs.<br>
 It is a roughf cut, quite ugly yet, but works like a charm :)<br>
 Currently this pluging catches the events for:
 - Job submitted
 - Job started
 - Job resumed
 - Job suspended
 - Job finished
 - Job error
 - Job failed
 
 For each event you can specify a custom message, either plain text or html.
 
## Installation
 
Download the folder and place it into your Deadline repository's subfolder `\DeadlineRepository10\custom\events`.<br>
Use the Tools menu in superuser mode to change the settings.

## Roadmap

- Code optimization
- Sending reports with the notifications
- Multiple email recipients
- Selectable emails for each event

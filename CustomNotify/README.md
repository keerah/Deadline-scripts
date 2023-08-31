# Custom notify
 
 This is a custom event plugin for Deadline that allows flexible email notifications about the jobs.<br>
 It is a roughf cut, quite ugly coded yet, but works like a charm :)<br>

 <img width="524" alt="Screenshot 2023-08-31 022936" src="https://github.com/keerah/Deadline-scripts/assets/9025818/1c54abce-a7a8-44f9-84c8-9e5e3bea9c01">

 Currently this pluging catches the events for:
 - Job submitted
 - Job started
 - Job resumed
 - Job suspended
 - Job finished
 - Job error
 - Job failed
 
 For each of those events you can specify a custom message, either plain text or html.
 
## Installation
 
Download the folder and place it into your Deadline repository's subfolder `\DeadlineRepository10\custom\events`.<br>
Use the Tools -> Configure Events menu in Superuser mode to change the plugin settings.

## Roadmap

- Code optimization
- Sending reports with the notifications
- Multiple email recipients
- Selectable emails for each event

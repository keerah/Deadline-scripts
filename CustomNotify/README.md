# Custom notify
 
 This is a custom event plugin for Deadline that allows flexible email notifications about the jobs.<br>
 It is a roughf cut, quite ugly coded yet, but works like a charm :)<br>

<img width="522" alt="Screenshot 2023-08-31 023936" src="https://github.com/keerah/Deadline-scripts/assets/9025818/eb148cdd-1bd9-4a43-b92a-3175a28e528e">

 Currently this pluging catches the events for:
 - Job submitted
 - Job started
 - Job resumed
 - Job suspended
 - Job finished
 - Job error
 - Job failed
 
 For each of those events you can specify a custom message, either plain text or html.<br>
 SMTP support is quite narrow by now, tested with Google mail, supports STARTTLS.<br>
 I personally use it with the same email address for sender and reciever, quite simple.<br>
 
## Installation
 
Download the folder and place it into your Deadline repository's subfolder `\DeadlineRepository10\custom\events`.<br>
Use the Tools -> Configure Events menu (in Superuser mode) to change the plugin settings.

## Roadmap

- Code optimization
- Sending job reports with the notifications
- Multiple email recipients
- Per event On/Off toggle
- Selectable emails for each event (?)

# Apple Messages Unread Text Reminders

This is a small project which might have some value to others or so says my girlfriend.  The simple python script watches your Messages.app database and sends an HTTP Request trigger to IFTTT when you have not responded to a message.  IFTTT in turn sends you a text (or takes some other action) reminding you to respond.


## Getting Started

You will need a SQL database reader to find the `handle_id` of the conversation you want to watch

Setup an IFTTT account at IFTTT.com

### Prerequisites

You will need an always on machine which runs the watchdog and the Messages.app.  I use a virtual machine running on my home server.  Getting Messages.app working on a virtual machine is not plug and play but there are plenty of guides on how to do it available, it involves some ROM spoofing etc.  One day I will write a guide myself and post it on my blog (which currently doesn't exist).

You will need to set up an HTTP Request Trigger with IFTTT.com.  Setup the trigger to send a text message to your phone.


### Installing

Clone the repository to whatever directory you choose.  

Modify the `Personal_Info_Sample.py` with the correct values and rename it to `Personal_Info.py`.  If you fork this repo make sure the `Personal_Info.py` is added to your `.gitignore`

I use a `.command` file to launch the script using the Terminal on startup (Similar to a shell or bat script)


## Built With

* Python3
* IFTTT


## Authors

* **Drake Evans**


## Acknowledgments

* Your mother




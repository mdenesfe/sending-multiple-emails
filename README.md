# Mail Sending Application
This application sends all files in a specific folder to a given list of recipients using a given email account and password.

## Installation
1. Python3 is required to run the application.
2. Install the `os` and `smtplib` libraries.
3. Replace the `email_id` and `email_pass` variables with your own email account and password.
4. Define the recipient's email addresses in the `recipient_list` variable as a list.
5. To run the application, use the command `python mail.py`.

## Usage
The application sends all files in the directory where it is run to the recipients. If a file named 'mail.py' exists in the directory, it will not be sent.

## Contributors
- [mdenesfe](https://github.com/mdenesfe)

## Notes
- The application only works with Gmail, so if you are using a different mail provider you need to change the connection information or change the protocol.
- Also, python3 is required to run the code and the email_id and email_pass variables need to be changed with your own email account and password.

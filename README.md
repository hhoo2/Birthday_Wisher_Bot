# Birthday Wisher Bot

The Birthday Wisher Bot is a Python script designed to automate the process of sending personalized birthday emails to your friends and loved ones. It reads birthday data from a CSV file, checks if today is someone's birthday, and, if so, selects a random letter template, personalizes it with the recipient's name, and sends it via Gmail using a secure SMTP connection.

<b><a href="https://replit.com/@HayOo1/BirthdayWisherBot" style="color:purple;">Click here to use this program in Replit</a></b>

![alt text](/program.png)

## Features
Automated Birthday Emails: The script automates the process of sending personalized birthday emails, saving you time and ensuring your friends and loved ones receive heartfelt wishes on their special day.

## Configuration

Before using the Birthday Wisher Bot, follow these steps to set up and customize the script in main.py:

1. **Gmail Credentials**: Replace the placeholder values in the script with your Gmail email address and password.

   ```python
   MY_EMAIL = "your_email@gmail.com"
   MY_PASSWORD = "your_email_password"
   ```

2. **CSV Data**: Ensure that your CSV file (`birthdays.csv`) is properly formatted with columns: `name`, `email`, `year`, `month`, and `day`.

3. **Letter Templates**: Customize the letter templates in the `letter_template` folder or add your own templates. Ensure that the placeholders, such as `[NAME]`, are present in the templates for personalization.


## Usage

Run the script using the following command:

```bash
python birthday_wisher.py
```

The script will check if today is someone's birthday, choose a random letter template, personalize it, and send the email automatically.

**Note**: For security reasons, it is recommended to use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) if you have two-factor authentication enabled on your Gmail account.

Feel free to explore and modify the script according to your needs. Happy automating and spreading birthday joy! 🎉

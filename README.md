# Webscrap
Watch emag products

## Files to modify
- **modify.env** file
  * enter your *email* and *password* to access SMTP server
    ```
    userID = 'user@example.com'
    password = 'your_password'
    ```
    For gmail you need to have 2FA enabled then generate a mail app password ((search for "google app passwords"))
  * rename the file from *modify.env* to *.env*
  
- **modify_config.json** file 
  * enter your details (below are gmail settings for server and port)
    ```
    {
      "smtpServer": "smtp.gmail.com",
      "port": 587,
      "fromUser": "sender@example.com",
      "toUser": "to@example.com"
    }
    ```
  * rename the file from *modify_config.json* to *config.json*
  
## To do
- error handling

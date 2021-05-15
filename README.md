# Webscrap
Watch emag products

## Files to modify/configure in order to run scraper-csv-menu.py
- **modify.env** file
  * enter your *email* and *password* to access SMTP server
    ```
    userID = 'user@example.com'
    password = 'your_password'
    ```
    For gmail you need to have 2FA enabled then generate a mail app password (search for "google app passwords")
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

- **favorites.csv** file
  * modify/create file with structure: link,desidered price as below
    ```
    https://www.emag.ro/telefon-mobil-samsung-galaxy-a52-dual-sim-256gb-8gb-ram-5g-blue-sm-a526bzbheue/pd/DP3S0KMBM/,2000
    ```
  
## To do
- error handling
- test requirements.txt ($ pip install -r requirements.txt)

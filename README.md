# Bypass Google (bypass-google.pythonanywhere.com)
Bypass Google is a website that allows user to download any public Google Doc and Google Sheet as a .docx and .csv file respectively. Bypass Google is best utilized for "view-only" documents where downloading is blocked on the Google editor. The website makes use of BeautifulSoup, requests, pandas, and htmldocx to scrape and convert data along with Flask as the web server. Uploaded files are deleted in 1 day.

## How to use (guide with pictures on website)
1. Users copy the unique id of the Google Document from the URL
2. Users input the id into the input box
3. Select the type of document
4. Submit
5. Click the download link

## Installations
If you want to try the project on your machine you'll need to make sure you get all the packages used for the project. 

`pip install -r requirements.txt`
will download all of the necessary packages.
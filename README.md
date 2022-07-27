# Bypass Google [web app](bypass-google.pythonanywhere.com)

![Project Image](https://raw.githubusercontent.com/EdwardX29/bypass-google/main/.github/images/bypassProject.png)

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [Author Info](#author-info)

---

## Description

Bypass Google is a website that allows user to download any public Google Doc and Google Sheet as a .docx and .csv file respectively. Bypass Google is best utilized for "view-only" documents where downloading is blocked on the Google editor. The website makes use of BeautifulSoup, requests, pandas, and htmldocx to scrape and convert data along with Flask as the web server. Uploaded files are deleted in 1 day.

#### Technologies:

- Flask
- Bootstrap 5
- BeautifulSoup, Requests, Pandas, [htmldocx](https://pypi.org/project/htmldocx/)

[Back To The Top](#read-me-template)

---

## How To Use

#### Step-by-step guide
1. Go to https://bypass-google.pythonanywhere.com
2. Copy the ID of the document you want to download
![Step 2 image](https://raw.githubusercontent.com/EdwardX29/bypass-google/main/.github/images/doc-id2.png)
3. Enter the ID in the form
![Step 3 image](https://raw.githubusercontent.com/EdwardX29/bypass-google/main/.github/images/step2.png)
4. Select the type of file and click Bypass!
![Step 4 image](https://raw.githubusercontent.com/EdwardX29/bypass-google/main/.github/images/step3.png) 
5. Click the button to download the file.
![Step 5 image](https://raw.githubusercontent.com/EdwardX29/bypass-google/main/.github/images/step4.png) 

#### Installation
```bash
pip install -r requirements.txt # install packages
export FLASK_ENV=development # set development mode
flask run # run the app
```

---
## References
- [htmldocx library](https://pypi.org/project/htmldocx/)

[Back To The Top](#read-me-template)

---


## Author Info

- Github - [EdwardX29](https://github.com/EdwardX29)

[Back To The Top](#read-me-template)
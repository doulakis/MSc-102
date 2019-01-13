# Welcome to the MSc-102 Project!!!

### General Info
This project is not a complete project and should not considered as a professional work by viewers of this profile.
Also this document should considered by the professors the documentation of the final assesment that should not exceed 3000 words.


### Project URL (public access):

https://app.doulakis.com
You should register to use the application (for password reset please check the spam folder)

### For Project Management Details please refer to the wiki page here: 
https://github.com/doulakis/MSc-102/wiki or read the details above

## General Information
Here you can find all the information about the project.

**Open Issues**
In this [URL (JIRA)](https://jira.weiv.io/projects/M104/issues/?filter=allissues) you can find all the issues of the project. All issues are under the Initiative issue ([M102-2](https://jira.weiv.io/browse/M102-2)). This is an ogoing list and can be changed any time with additions and deletions of issues.

**Meeting Notes:**
In this [URL (Meeting Notes)](https://confluence.weiv.io/display/M1/Meeting+notes) you can find all the meeting notes of the project under the Knowledge page.

**Knowledge Base - Documentation:**
Here [KB](https://confluence.weiv.io/pages/viewpage.action?pageId=4784133) are all the information about the project.

### The **Hierarchy** of the project structure is as follow:

* Initiative
  * Epic
    * Story
    * Feature
    * Task
    * Bug
      * Sub-Task

### The **Workflow** has the statuses:

**ToDo:** It is a open issue the development not yet started.

**In Progress:** We are currently working on this issue.

**Done:** The issue is completed

### The **Priority** of the issues is as follow:

* Highest
* High
* Medium
* Low
* Lowest


### **Other Info**
You can find under this issue the estimation of each issue and worklogs.


## Team Members
* Stelios Doulakis (Project Manager, Backend Developer, Systems Administrator)
* Thomas Agorastoudis (Backend Developer)
* Haris Sarchosis (Frontend Developer)
* Nikolaos Martikas (Tester, Frontend Developer)


### Linux Deployment (CentOS 7)

##### Server Preparation

````
$ sudo yum update
$ sudo yum install -y  python3 python3-venv python3-dev
$ sudo yum install -y  mysql-server postfix supervisor httpd git
````

##### Clone the project
````
$ git clone https://github.com/doulakis/MSc-102
````
##### Enable the python virtual environment and install aditional packages
````
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn pymysql
`````

* For Windows users, run CMD with ADMIN rights first.
  activate from Scripts directory Scripts\activate


##### Setup the environmental variables

Copy the .flaskenvexample to .flaskenv  and change the lines with your own details:

```
LC_ALL= en_US.UTF-8
LANG = en_US.UTF-8
FLASK_APP = myapp.py
DATABASE_URL = 'mysql+pymysql://username:password@x.x.x.x/msc102'
MAIL_SERVER = smtp.yourserver.com
MAIL_PORT = 25
MAIL_USERNAME = yourapikey
MAIL_PASSWORD = yourpassword
```




##### Create MariaDB Database, User, etc..

Production DB:
```
mysql> create database msc-102 character set utf8 collate utf8_bin;
mysql> create user 'msc102'@'localhost' identified by '<your-password>';
mysql> grant all privileges on msc-102.* to 'msc102'@'localhost';
mysql> flush privileges;
mysql> quit;
```
Test DB:
```
mysql> create database msc-102_tests character set utf8 collate utf8_bin;
mysql> create user 'msc102_tests'@'localhost' identified by '<your-password>';
mysql> grant all privileges on msc-102_tests.* to 'msc102_tests'@'localhost';
mysql> flush privileges;
mysql> quit;
```

##### Run The DB Migration

```
(venv) $ flask db upgrade
``` 

##### Run the gunicorn

run the command and confirm that the app is running on localhost port: 8080

````
/pathtoproject/venv/bin/gunicorn -b localhost:8080 -w 4 myapp:app
````


##### Setup supervisord

use the config ./deployment/supervisord/app.ini

coppy the file into /etc/supervisor.d/

restart the service:

````
supervisorctl restart msc102
````

##### Setup HTTP Server as proxy

use the config under the ./deployment/apache/example_apache_vhost

change the details and copy it to /etc/httpd/conf.d

## Run Some Tests


You can run some tests (not completed) for the project by executing (in the root directory of the project) the below command:

```
python tests.py
```

##### Example Output:

````
test_avatar (__main__.UserModelCase) ... ok
test_follow (__main__.UserModelCase) ... ok
test_follow_posts (__main__.UserModelCase) ... ok
test_password_hashing (__main__.UserModelCase) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.613s

````
 #### Database Schema

![alt text](https://i.imgur.com/6Iscu5M.png)


## Technologies & Services


### Short Description of Packages (Check requirements.txt for full list)

- Flask

    Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
    

- Flask-Bootstrap

    Flask-Bootstrap packages Bootstrap into an extension that mostly consists of a blueprint named ‘bootstrap’. It can also create links to serve Bootstrap from a CDN.

- Flask-Login

    Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

- Flask-Mail
    
    The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts.

- Flask-Migrate

    Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface or through the Flask-Script extension.

- Flask-Moment
    
    Formatting of dates and times in Flask templates using moment.js.

- Flask-SQLAlchemy [More Details](http://flask-sqlalchemy.pocoo.org/2.3/)
    
    Flask SQLAlchemy is a Flask extension in order to support SQLAlechemy.
    SQLAlchemy is an Object Relational Mapper. You can use MySQL, PostgreSQL and other DBs. 
    For more details please click [here](https://docs.sqlalchemy.org/en/latest/)


- Flask-WTF & WTForms [More Details](https://wtforms.readthedocs.io/en/stable/) 

    Forms provide the highest level API in WTForms. They contain your field definitions, delegate validation, take input, aggregate errors, and in general function as the glue holding everything together.
    

- Werkzeug
    
    Werkzeug started as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility modules. It includes a powerful debugger, fully featured request and response objects, HTTP utilities to handle entity tags, cache control headers, HTTP dates, cookie handling, file uploads, a powerful URL routing system and a bunch of community contributed addon modules.
    It does Unicode and doesn't enforce a specific template engine, database adapter or anything else. It doesn't even enforce a specific way of handling requests and leaves all that up to the developer.

- Jinja2
    
    Jinja2 is a templating engine for Python.

- gunicorn

    Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.


#### Email Service
    
We used sendgrid free tier for email provider, we verified the domain in order to have DKIM and SPF records to avoid blacklist of our domain.

#### Hosting
The app is hosted in Digital Ocean Droplet free of charge. We use the GitHub Education package to redeem the available credits.
All the configuration of the server is manual.

#### SSL Report by SSL Labs

![alt text](https://i.imgur.com/1oFc1Qf.png)

[Click here to Run the report and get the results live](https://ssllabs.com/ssltest/analyze.html?d=app.doulakis.com&latest)

#### Let's Encrypt
The Domain is verified under Let's Encrypt which is a free, automated, and open certificate authority.

#### Gravatar API
An "avatar" is an image that represents you online—a little picture that appears next to your name when you interact with websites.
A Gravatar is a Globally Recognized Avatar. You upload it and create your profile just once, and then when you participate in any Gravatar-enabled site, your Gravatar image will automatically follow you there.
Gravatar is a free service for site owners, developers, and users. It is automatically included in every WordPress.com account and is run and supported by Automattic.











# Welcome to the MSc-102 Project!

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

### Project URL (public access):

https://app.doulakis.com
You should register to use the application (for password reset please check the spam folder)


### Project Structure



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


##### Setup the environmental variables

Copy the .flaskenvexample to .flaskenv  and change the lines with your own details:

```
LC_ALL= en_US.UTF-8
LANG = en_US.UTF-8
FLASK_APP = myapp.py
DATABASE_URL = 'mysql+pymysql://username:password@x.x.x.x/msc102'
MAIL_SERVER = smpt.yourserver.com
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

coppy the file into /et/supervisor.d/

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

OK

````



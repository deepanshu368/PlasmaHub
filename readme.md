# Frosthack-2021-Submission
This is the project submission of Team SSD of Frosthack 2021. This project is developed on windows operating system and we expect the user can run it on other OS as well.

Introduction Video of the project: 

https://drive.google.com/file/d/1XJjTp6QJh_0rdwUYHZsTHkrYMzC0VbSH/view?usp=drivesdk

youtube link:
https://www.youtube.com/watch?v=300IDNztclw

## Overview
India, the country with the second largest population is facing its one of the biggest challenges, Covid-19. The second wave of Covid-19 has proved to be fatal for India. And during this difficult time, a huge number of people are struggling due to coronavirus.

One solution that has proved to be most effective to recover from Covid-19 is by transferring the plasma of an already recovered Covid patient to the affected person. But the challenge here is the requirement of plasma in a large number to reach the maximum population in need. 

There are a lot of people who are willing to donate plasma and a lot of organisations who are in need of such donations. But there is no such good channel that can provide effective contact between these two. So this is where we come into action and provide that necessary channel that connects the donors and the organisations.

## Idea
To address the above problem , we here provide the solution by proposing a website that will act as a channel between the hospitals in need of plasma and the donors who are willing to donate.

We have provided the option for donors as well as hospitals to register on this website. If a donor wants to donate his/her plasma and is eligible to do so, then the person can register himself/herself on the website and set the preferences such as the hospitals and distance upto which the donor is comfortable to go and donate. When any particular hospital is in need of plasma of a specific blood group, then using our website they will be able to send out notifications to all the donors who clear the criteria and are in close vicinity of the hospital.

We believe that in this way there will be effective communication between the donors and hospitals and plasma will be available very easily even for the emergency cases.

## Installation and Dependencies


1) We need to load the files from the github.

2) In the "donate" sub-folder inside "donate" folder, we will need to go to "settings.py", and update gmail address and password with a valid gmail address and password, Also in the setting.py one needs to do changes in the 'DATABASES' dictionary, you have to change the postgres username, password,and database name.

#### Note: In order to send out email notifications to the donors, the user has to enable the "Less Secure App Access" in the Google Account settings.

3) We have used Python 3, Django 3.2, PostgreSQL 13.2 to operate the website as they are essential parts for storing database.
The following commands need to be run as they are the dependencies:

```pip install django```

```pip install psycopg2```

```pip install pillow```

4) After completing installation process, we need to create a database in PgAdmin(development platform for PostgreSQL), then we will open terminal with the address of the required folder(donate folder) and run following commands for successful execution:

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py sqlmigrate volunteers 0001```

```python manage.py runserver```

#### NOTE: One needs to create some data for the databsae, ie, the developer has to register some enteries initially beacause the database will run as empty initially.

Some of the images which are brief description of the webpages are:
![homepage](https://user-images.githubusercontent.com/56973333/117562155-6df35000-b0ba-11eb-9277-3eef788b8b04.png)

![homepage](https://user-images.githubusercontent.com/56361694/117562362-10600300-b0bc-11eb-9770-ec340132eba2.png)

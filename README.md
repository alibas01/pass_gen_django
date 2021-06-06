# Password Generator v1.0

A password generator application built with Django version 3.2.4

## Description

App generates random passwords 5-18 characther long, with uppercase, lowercase, numbers, special charachters in-demand options.
Additionally, app gives the opportunity to input a recognizable word and turns that word into a useful password.

## Snapshots

<p align="center">
<img src="https://raw.githubusercontent.com/alibas01/pass_gen_django/main/pass_gen/static/images/home.png" width="400" height="auto" />
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/alibas01/pass_gen_django/main/pass_gen/static/images/pass.png" width="400" height="auto" />
</p>

## Installation

Please make sure you have Python programming language available in your computer.
Depending on your Python and pip version you will use pip3 or pip / python3 or python. I will use python3 and pip3 in this instructions part.

- clone this repository;
- `pip3 install django` (you might need to use sudo or environment for permissions)
- `python3 manage.py migrate`

### Start the app

- `python3 manage.py runserver`
- visit `127.0.0.1:8000` or `localhost:8000` from your browser.

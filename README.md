# Recipe API

[![Build Status](https://app.travis-ci.com/taufanbudiman/recipe-api.svg?token=CojutyD1h4rRFp3u6q3p&branch=master)](https://app.travis-ci.com/taufanbudiman/recipe-api)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)

1. Overview

   a simple recipe API with rest api. build with python django.

2. Running Command in Container

    run test in container
    ```bash
    make test
    ```
   run makemigration django
   ```bash
   make makemigrations apps=core
   ```
   run migrate django
   ```bash
   make migrate
   ```
   create a superuser
   ```bash
   make create_superuser
   ```
   runserver docker
   ```bash
   make runserver
   ```

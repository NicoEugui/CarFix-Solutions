@echo off
rmdir /s /q migrations
pipenv run init
pipenv run migrate
pipenv run upgrade

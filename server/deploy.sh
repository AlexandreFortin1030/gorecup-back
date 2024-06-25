#!/bin/bash

read -p "Entrez le message du commit : " commit_message

git add .
git commit -m "$commit_message"
git push heroku master

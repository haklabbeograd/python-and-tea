* temperature sensor connected to openwrt router *

we are following instructions from http://haklabos.wordpress.com/projekti/digitemp/
upto and including section "Reading temperature from sensor".

* instructions how to deploy webapp to heroku *

add to .git/config file:

[remote "heroku"]
	url = git@heroku.com:stark-savannah-9456.git
	fetch = +refs/heads/*:refs/remotes/heroku/*

to deploy webapp to heroku execute these commands in local repo root directory:

heroku login # just once
heroku create # just once

git subtree push --prefix temperature-monitoring/tempmon-webapp heroku master
heroku run python manage.py syncdb


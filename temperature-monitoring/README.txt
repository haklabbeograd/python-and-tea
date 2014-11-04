* temperature sensor connected to openwrt router *

we are following instructions from http://haklabos.wordpress.com/projekti/digitemp/
upto and including section "Reading temperature from sensor".

* instructions how to deploy webapp to heroku *

to deploy webapp to heroku execute these commands:

heroku login # just once
heroku create # just once

depending on output from last command, add to .git/config file:

[remote "heroku"]
	url = git@heroku.com:<<<HEROKU-NAME-OF-APP>>>.git
	fetch = +refs/heads/*:refs/remotes/heroku/*

in local repo root directory execute:

git subtree push --prefix temperature-monitoring/tempmon-webapp heroku master
heroku run python manage.py syncdb


NEURONER
======

LIVARAVA-NEURONER

**Test site url:** https://your.domain.com.ua

**Test admin panel:** https://your.domain.com.ua

- Login: admin
- Password: admin

-------

Agreement
=========

- The `(.env)$` identifier of command line is indicates that there must be active virtual environment.

- In this manual path to the project, for example: `/full/path/to/the/your.domain.com.ua/` - it will be designated as `$BASE_DIR`.


Attention
=========

- Puthon support: `2.7`

-------

Quick start guide
=================

Clone
-----


    $ git clone git@github.com:kariavka/livarava-neuroner.git
    $ cd livarava-neuroner


Install virtualenv
------------------


    $ virtualenv --no-site-packages -p/usr/bin/python2.7 .env
    $ source .env/bin/activate
    (.env)$


Install packages
----------------


    (.env)$ pip install -r requirements.txt


Run project
----------------


    (.env)$ make migrate
    (.env)$ make createsuperuser
    (.env)$ make collectstatic
    (.env)$ make run

Deploy project
----------------


    $ cd /home/livarava-neuroner; make deploy;

BOWER USAGE
----------------


    (.env)$ npm install -g bower
    (.env)$ ./manage.py bower install
    (.env)$ make collectstatic

Reload uwsgi
----------------


    $ touch /home/livarava-neuroner/conf/reload.txt

Restart nginx
----------------

    $ sudo /etc/init.d/nginx restart

Create MySQL database
-----


    $ sudo mysql -uroot -p

    drop database if exists `neuroner`;
    CREATE DATABASE `neuroner` CHARACTER SET utf8 COLLATE utf8_general_ci;
    GRANT ALL ON `neuroner`.* TO `<USER>`@localhost IDENTIFIED BY '<PASSWORD>';
    FLUSH PRIVILEGES;

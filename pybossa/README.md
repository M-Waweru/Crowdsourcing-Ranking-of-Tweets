# What is PYBOSSA?

PYBOSSA is a technology built by [Scifabric](https://scifabric.com), for crowdsourcing or citizen science platforms.

PYBOSSA is an extremely flexible and versatile technology with a multitude of applications that
adapt to each specific case facilitating many of the daily tasks that take place in research
environments such as museums, art galleries, heritage institutions, libraries of any kind, market
research companies, hospitals, universities and all those organisations that manage data or require
information from their customers/users -such as airports, shopping malls, banks, hotel chains, etc.

PYBOSSA’s simplicity consists in its easy adjustment to any areas using any of the available
templates, this way every customer can then adapt it to their own needs.

PYBOSSA integrates with other data collection products such as Amazon S3, Twitter, Youtube,
Google Spreadsheets, Flickr, Raspberry Pi, etc. Through all these integrations
PYBOSSA allows data capture for further analysis made by users in a transparent and easy way.

- 📘 Documentation: [https://docs.pybossa.com](https://docs.pybossa.com)
- 🎬 Video: [Intro](https://www.youtube.com/watch?v=oH8fJAhRDJM)
- 🐦 Twitter: [@PyBossa](https://twitter.com/pybossa)
- 💬 Chat: [Gitter](https://gitter.im/Scifabric/pybossa)
- 📦 [PYBOSSA extras](https://github.com/Scifabric/)
- 👉 [Play with PYBOSSA online](https://crowdcrafting.org)

# PYBOSSA for python 3

PYBOSSA runs in python >= 3.6. While 3.8 has been released recently, it needs testing before officially support it.

If you have a python2.7 server, please, checkout the python2.7 branch and use that one for your server.


# Installing and Upgrading

**Important: if you are updating a server, please, be sure to check the
Database Migration scripts, as new changes could introduce new tables,
columns, etc, in the DB model. See the [Updating Section](https://docs.pybossa.com/installation/guide/#updating-pybossa) from the documentation**

See [installation instructions](https://docs.pybossa.com/installation/gettingstarted/).

# Running the Server
After following the Installation guide above

Commands to run once installed:

1. python3 -mvenv env

2. source env/bin/activate

3. redis-server

4. rqscheduler --host 127.0.0.1

5. redis-server contrib/sentinel.conf --sentinel

6. python app_context_rqworker.py scheduled_jobs super high medium low email maintenance

7. sudo service postgresql restart

8. python run.py


Commands to remember in installation:
1. Install python-ldap
apt-get install build-essential python3-dev python2.7-dev \
    libldap2-dev libsasl2-dev slapd ldap-utils tox \
    lcov valgrind

2. Install wheel in virtualenv
pip install wheel

## Copyright / License

Copyright 2020 [Scifabric LTD](https://scifabric.com).

Source Code License: The GNU Affero General Public License, either version 3 of the License
or (at your option) any later version. (see COPYING file)

The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

Documentation and media is under a Creative Commons Attribution License version
3.

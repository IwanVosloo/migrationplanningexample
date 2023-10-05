Introduction
============

This project is a showcase of the migration algorithm
provided by the [reahl-component](https://pypi.org/project/reahl-component) package.


Setup python virtual env to run example
=======================================


Using the makefile
------------------

```
make migrationexample_env
```

Do it yourself
--------------

```
python3 -m venv migrationexample_env
source migrationexample_env/bin/activate
```

Comprehensive example
---------------------

Look at the [Reahl web framework](https://www.reahl.org) example [here.](https://www.reahl.org/docs/7.0/tutorial/gettingstarted-install.d.html#install-python-with-virtualenv-support)


Setup Database
==============

The database url configured in
------------------------------

```
myproject/etc/reahl.config.py
```

Example DB url
--------------

```
reahlsystem.connection_uri = 'postgresql://reahl:reahl@postgres/reahl'
```



Start Postgres DB using docker
==============================

Use docker-compose
------------------

```
docker-compose up -d
```

Install and run example
=======================

```
make
```

Create DB schema and user
=========================


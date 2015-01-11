
``django-appenv9`` creates environment for developing reusable Django apps. Instead of preparing it from a scratch, you can focus on building your app.

Features
========

``django-appenv9`` provides:

* nice folder structure
* application schema
* demo project
* virtualenv for demo
* admin:admin account in demo
* automated package provisioning
* git repository
* makefile
* easy publishing on PyPI

Structure
=========

For app named ``my-test``, ``django-appenv9`` generates the following::

	django-my-test/
	├── demo
	│   ├── db.sqlite3
	│   ├── demo
	│   │   ├── __init__.py
	│   │   ├── settings.py
	│   │   ├── urls.py
	│   │   └── wsgi.py
	│   ├── main
	│   │   ├── admin.py
	│   │   ├── fixtures
	│   │   │   └── initial_data.json
	│   │   ├── forms.py
	│   │   ├── __init__.py
	│   │   ├── models.py
	│   │   ├── static
	│   │   ├── templates
	│   │   │   └── base.html
	│   │   ├── tests.py
	│   │   ├── urls.py
	│   │   ├── views.py
	│   ├── makefile
	│   ├── manage.py
	│   ├── requirements.txt
	│   └── virtualenv
	│       └── demo
	│           ├── ...
	├── LICENSE
	├── makefile
	├── MANIFEST.in
	├── README.rst
	├── setup.py
	├── my_test
	│   ├── admin.py
	│   ├── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   ├── urls.py
	│   └── views.py
	└── todo.txt



#Usage

`$ bash appenv9 myapp`

* Make sure to review the generated documents. You probably want to change things like app description. Look for `@todo` tags.

* To start a demo project at ``127.0.0.1:8000``, navigate to ``demo`` directory and type ``make``.

* In order to publish your app on PyPI execute the commands below. Before doing that make sure you have created `~/.pypirc` file similar to (this one here)[https://wiki.python.org/moin/TestPyPI] (point 2).

`
$ cd django-myapp
$ make deploy_test			# deploy to TestPyPI
$ make deploy_production	# deploy to real PyPI
`

You probably also want to switch to MASTER branch and create a new tag/release.

#Todo:

* This file
* Enable additional arguments in appenv9'
MD - > rst

update nowe rzeczy?

Default version of Django is 1.6.5. If you want to change that, edit ``appenv9`` script and replace default settings with desired ones.


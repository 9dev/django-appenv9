
#How it works

Creates a new reusable app schema along with demo project, git repository, virtualenv and other useful stuff.

#Usage

`$ bash appenv9 myapp`

* Make sure to review the generated documents. You probably want to change things like app description. Look for `@todo` tags.

* In order to publish your app on PyPI execute the commands below. Before doing that make sure you have created `~/.pypirc` file similar to (this one here)[https://wiki.python.org/moin/TestPyPI] (point 2).

`
$ cd django-myapp
$ make deploy_test			# deploy to TestPyPI
$ make deploy_production	# deploy to real PyPI
`

You probably also want to create a new git tag as well.

#Todo:

* This file
* Enable additional arguments in appenv9


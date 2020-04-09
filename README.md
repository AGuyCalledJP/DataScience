### DataScience Setup

This backend is built on python 3.7.6

To manage python versions install pyenv:
	brew update
	brew install pyenv

Once installed, use pyenv to dowload the target python version:
	pyenv install 3.7.6

Install virtualenv using pyenv:
	pyenv exec python -m pip install --upgrade pip
	pyenv exec python -m pip install virtualenv

Create your virtual environment:
	pyenv exec python3 -m virtualenv ENV

Then you can activate your virtual environment:
	source ENV/bin/activate

You can check your python version to be sure that everything went as expected
	python --version

Install all pip requirements:
	pip install -r requirements.txt

DATABASE SETUP:
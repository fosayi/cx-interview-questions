## Documentation

Please ensure that you are running on Python 3 and preferably you are using a linux machine

# install pipenv
pip install pipenv

# Create a new virtualenv using py3
cd shopping_basket
pipenv install --three

# To source your virtualenv
pipenv shell

# install unittest2 for py3 and pytest
pipenv install unittest2
pipenv install pytest

# Go into the shopping basket dir
cd shopping_basket

# run tests
pytest

## Steps to run the Tests ##

# install pipenv
pip install pipenv

# Create a new virtualenv using py3
cd shopping_basket
pipenv install --three

# Source your virtualenv
pipenv shell

# install unittest2 for py3 and pytest
pipenv install unittest2
pipenv install pytest

# Go into the shopping basket dir
cd shopping_basket

# run tests
pytest


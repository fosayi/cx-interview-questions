## Documentation

Please ensure that you are running on Python 3 and preferably you are using a linux machine

# install pipenv
pip install pipenv

# Create a new virtualenv using py3
cd shopping_basket;
pipenv install --three

# To source your virtualenv
pipenv shell

# To run the script basket_pricer_script.py

As long as your virtualenv is sourced and you have all dependencies installed, then you can simply run:
python basket_price_script.py

The response will be printed in the console.

If you want to test the basket_pricer component with different  baskets, offers and catalogue, you can do so by
modifying the basket_pricer_script.py.



##### UNITTESTS #########

# install unittest2 for py3 and pytest
pipenv install unittest2;
pipenv install pytest

# Go into the shopping basket dir
cd shopping_basket

# run tests
pytest
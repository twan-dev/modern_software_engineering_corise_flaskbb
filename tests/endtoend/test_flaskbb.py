import pytest
from playwright.sync_api import Page

###################################################################
# CoRise TODO: add a new fixture `translations` that calls the
# `compile_translations` function from flaskbb.utils.translations

# ADD CODE HERE

@pytest.fixture
def app():
    # TODO: ADD CODE HERE
    # Hint: create the app, and setup any default context like translations,
    # settings, DB, etc.
    pass

def test_load_home_page(live_server, page: Page):
    # TODO: ADD CODE HERE
    # Hint: Check out `flask.url_for` helper function to get the external url for 
    # an endpoint. Then go to it using playwright's `page.goto(url)`
    pass

###################################################################
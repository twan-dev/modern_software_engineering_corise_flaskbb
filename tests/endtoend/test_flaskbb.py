import pytest
from playwright.sync_api import Page
from flask import url_for
import os
from flaskbb import create_app
from flaskbb.configs.testing import TestingConfig as Config
from flaskbb.extensions import db
from flaskbb.utils.populate import create_default_groups, create_default_settings
from flaskbb.utils.translations import compile_translations
from playwright.sync_api import Page, expect
###################################################################
# CoRise TODO: add a new fixture `translations` that calls the
# `compile_translations` function from flaskbb.utils.translations

# ADD CODE HERE
os.environ['FLASK_ENV'] = 'development'

@pytest.fixture
def app():
    # Hint: create the app, and setup any default context like translations,
    # settings, DB, etc.
    # Hint: take a look at the tests/fixtures/app.py file for the details of 
    # how to configure the application.
    # TODO: ADD CODE HERE
    pass
    """application with context."""
    app = create_app(Config)

    with app.app_context():
        db.create_all()
        create_default_groups()
        create_default_settings()
        compile_translations()

    return app

def test_create_new_account(live_server, page: Page):    
    url=url_for('forum.index', _external=True)

# def test_load_home_page(live_server, page: Page):
#     # Hint: Check out `flask.url_for` helper function to get the external url for 
#     # an endpoint. Then go to it using playwright's `page.goto(url)`
#     # TODO: ADD CODE HERE
#     pass
    page.goto(url)
    expect(page).to_have_title("FlaskBB - A lightweight forum software in Flask")

###################################################################
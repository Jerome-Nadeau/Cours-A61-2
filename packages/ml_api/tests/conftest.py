import pytest

import os
import sys

# def add_parent_directory_to_path():
#     parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.append(parent_dir)

def add_subdirectories_to_path(rootdir):
    for dirpath, dirnames, filenames in os.walk(rootdir):
        sys.path.append(dirpath)

rootdir = os.path.dirname(os.path.abspath(__file__))
# add_parent_directory_to_path()
add_subdirectories_to_path(rootdir)

from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client

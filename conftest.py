import pytest
from metods.user_metods import User


@pytest.fixture
def user():
    user = User()
    user.post_reqest_create_user()
    yield user


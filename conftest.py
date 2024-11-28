import pytest
from metods.user_metods import User


@pytest.fixture
def user():
    user = User()
    user.post_reqest_create_user()
    yield user
    status, token_user = user.post_reqest_login_user()
    user.delite_reqest_delite_user(token_user['accessToken'])


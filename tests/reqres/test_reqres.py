import json

import pytest
from assertpy import assert_that
from requests import codes

from clients.reqres.reqres_client import ReqresClient

client = ReqresClient()
CREATE_USER_REQUEST_FILEPATH = 'create_user_request.json'


@pytest.mark.reqres
@pytest.mark.regression
class TestReqresService:

    @pytest.mark.smoke
    def test_total_users_per_page(self):
        """
        Validate that the amount of users that are returned in a single get all users call
        matches with the "per_page" attribute
        """
        response = client.get_users()
        response_payload = json.loads(response.text)

        assert_that(response.status_code).is_equal_to(codes.ok)

        users_per_page = int(response_payload['per_page'])
        amount_of_users = len(response_payload['data'])

        assert_that(users_per_page).is_equal_to(amount_of_users)

    def test_user_is_created(self):
        """
        Validate that the customer is able to create a new user and this one is added to de database
        """
        user_name = "John Test"
        user_job = "programmer"
        create_response = client.create_user(user_name, user_job)

        assert_that(create_response.status_code).is_equal_to(codes.created)
        new_user_id = create_response.json()['id']

        get_user_response = client.get_user(new_user_id)
        get_user_response_payload = get_user_response.json()

        assert_that(get_user_response.status_code, description="User was not created").is_equal_to(codes.ok)
        assert_that(get_user_response_payload['name']).is_equal_to(user_name)
        assert_that(get_user_response_payload['job']).is_equal_to(user_job)
        assert_that(get_user_response_payload['id']).is_equal_to(new_user_id)

import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util
import openpyxl

@pytest.fixture(scope="session")
def create_token():
    util = Util()  # Instantiate Util
    response = post_request(
            url=APIConstants.url_create_token(),
            headers=util.common_headers_json(),  # Use instance of Util
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
    verify_https_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    util = Util()  # Instantiate Util
    response = post_request(
            url=APIConstants.url_create_booking(),
            auth=None,
            headers=util.common_headers_json(),  # Use instance of Util
            payload=payload_create_booking(),
            in_json=False
        )

    booking_id = response.json()["bookingid"]

    verify_https_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id

@pytest.fixture(scope="session")
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials
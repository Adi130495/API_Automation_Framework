import openpyxl
import pytest
import requests
from conftest import read_credentials_from_excel
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.utils.utils import Util

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

def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }

    # Instantiate Util and then call the common_headers_json method
    util_instance = Util()

    response = post_request(
        url=APIConstants.url_create_token(),
        headers=util_instance.common_headers_json(),  # Call it using the instance
        auth=None,
        payload=payload,
        in_json=False
    )
    return response
@pytest.mark.parametrize("user_cred",read_credentials_from_excel("/Users/adityabhalerao/API_Automation_Framework/tests/test/data_driven_testing/testdata_ddt_apiauto.xlsx"))
def test_create_auth_with_excel(user_cred):
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = create_auth_request(username=username, password=password)
        print(response.status_code)
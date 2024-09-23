# Read the CSV or EXCEL File
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result

# Read the Excel - openpyxl
import openpyxl
import requests

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.utils.utils import Util

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

def test_create_auth_with_excel():
    file_path = "/Users/adityabhalerao/API_Automation_Framework/tests/test/data_driven_testing/testdata_ddt_apiauto.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = create_auth_request(username=username, password=password)
        print(response.status_code)
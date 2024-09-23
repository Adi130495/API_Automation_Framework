import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


def test_invalid_create_booking(self):
    util = Util()

    # Invalid payload without required fields
    invalid_payload = {
        "lastname": "Smith"  # Missing required fields
    }

    response = post_request(
        url=APIConstants.url_create_booking(),
        headers=util.common_headers_json(),
        auth=None,
        payload=invalid_payload,
        in_json=False
    )

    verify_https_status_code(response_data=response, expect_data=400)
    assert "error" in response.text, "No error message in response"

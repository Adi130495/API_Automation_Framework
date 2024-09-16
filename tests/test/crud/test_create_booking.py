import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_positive(self):
        response = post_request(
            url=APIConstants.url_create_booking(),
            auth=None,
            headers=Util().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )

        booking_id = response.json()["bookingid"]

        verify_https_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    def test_create_booking_negative(self):
        response = post_request(
            url=APIConstants.url_create_booking(),
            auth=None,
            headers=Util().common_headers_json(),
            payload={},
            in_json=False
        )

        verify_https_status_code(response_data=response, expect_data=500)

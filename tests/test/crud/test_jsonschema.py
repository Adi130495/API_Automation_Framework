# GET Response
# Create the JSON Schema -> https://www.jsonschema.net/
# Save that schema into the name.json file
# If you want to validate the JSON Schema -> https://www.jsonschemavalidator.net/

import json
import os

from jsonschema import validate
from jsonschema import ValidationError
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

class TestCreateBookingJSONSchema(object):
    def load_schema(self,file_name):
        with open(file_name,'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_schema(self):
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

        # Response with schema.json stored :-

        file_path = os.getcwd() + "/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("Incorrect JSON Schema")
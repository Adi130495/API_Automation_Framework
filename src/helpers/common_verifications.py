# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON schema
def verify_https_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed Expected Result != Actual Result"

def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is greater than zero"

def verify_response_key_should_not_be_none(key):
    assert key is not None
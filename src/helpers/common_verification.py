# common  functions verification,to verify headers,data,json schema,http statuscode
# common functions to be reused

def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "failed ststus code match"

def verify_response_key(key,expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key != 0,"failed- key is not empty" + key
    assert key > 0,"failed- key is greater than zero"

def verify_json_key_for_not_null_token (key):
    assert key != 0, "failed- key is not empty" + key #key is json payload

def verify_response_delete(response):
    assert "Created" in response


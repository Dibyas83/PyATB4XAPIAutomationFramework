# common verification functions ,to verify headers,data,json schema

def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "failed ststus code match"

def verify_response_key(key,expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key != "failed- key is not empty" + key
    assert key > 0,"failed- key is greater than zero"

def verify_json_key_for_not_null_token (key):
    assert key != "failed- key is not empty" + key #json payload

def verify_response_delete(key):
    assert "Created" in response


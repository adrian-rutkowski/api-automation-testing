import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"] == "application/json"


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"


def test_get_locations_for_us_90210_check_state_equals_california():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["state"] == "California"


def test_get_locations_for_us_90210_check_state_abbreviation_equals_ca():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["state abbreviation"] == "CA"


def test_get_locations_for_us_90210_check_latitude_equals_34_0901():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["latitude"] == "34.0901"


def test_get_locations_for_us_90210_check_longitude_equals_negative_118_4065():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["longitude"] == "-118.4065"


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1

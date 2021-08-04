import requests
import pytest
import csv

test_data_zip_codes = [
    ("pl", "78-600", "Wałcz"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze"),
    ("pl", "61-624", "Poznań"),
    ("pl", "50-545", "Wrocław")
    ]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name


def read_test_data_from_csv():
    test_data = []
    with open('test_data/test_data_zip_codes.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_test_data_from_csv())
def test_using_csv_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name

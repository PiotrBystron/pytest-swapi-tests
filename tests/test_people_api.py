"""
API tests for Star Wars API (SWAPI).

This test suite covers:
- GET /people/{id} — fetching person details (valid and invalid IDs)

Notes:
    - SWAPI is read-only, only GET requests are available.
    - Service returns 404 for invalid entities.
"""


import pytest
import requests
from pytest_html import extras as html_extras



# -------------------------------------------------------------------------------------
# GET
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize("people_id, expected_name, expected_height, expected_birth_year, expected_status_code", [
    (1, "Luke Skywalker", "172", "19BBY", 200),
    (2, "C-3PO", "167", "112BBY", 200),
    (83, "Tion Medon", "206", "unknown", 200),
])
def test_get_people_by_id(api_base_url, people_id, expected_name, expected_height, expected_birth_year, expected_status_code, record_property, extras):
    """Tests GET /people/{id} endpoint returns correct data."""
    response = requests.get(f"{api_base_url}/people/{people_id}")
    data = response.json()

    record_property("url", response.url)
    record_property("status_code", response.status_code)
    record_property("name", data["name"])

    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>GET /people/{people_id}</b><br>"
        f"Status: {response.status_code}<br>"
        f"Name: {data['name']}<br>"
        f"Height: {data['height']}<br>"
        f"Birth year: {data['birth_year']}<br>"
        f"</div>"
    ))

    assert response.status_code == expected_status_code
    assert data["name"] == expected_name
    assert data["height"] == expected_height
    assert data["birth_year"] == expected_birth_year



@pytest.mark.parametrize("invalid_id", [-1, 0, 84, 9999, "abc"])
def test_get_people_invalid_id(api_base_url, invalid_id):
    response = requests.get(f"{api_base_url}/people/{invalid_id}")
    assert response.status_code == 404


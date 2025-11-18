"""
API tests for Star Wars API (SWAPI).

This test suite covers:
- GET /planets/{id} — fetching planet details (valid and invalid IDs)

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
@pytest.mark.parametrize("planet_id, expected_name, expected_diameter, expected_population, expected_status_code", [
    (1, "Tatooine", "10465", "200000", 200),
    (3, "Yavin IV", "10200", "1000", 200),
    (60, "Umbara", "unknown", "unknown", 200),
])
def test_get_planet_by_id(api_base_url, planet_id, expected_name, expected_diameter, expected_population, expected_status_code, record_property, extras):
    """Tests GET /planets/{id} endpoint returns correct data."""
    response = requests.get(f"{api_base_url}/planets/{planet_id}")
    data = response.json()

    record_property("url", response.url)
    record_property("status_code", response.status_code)
    record_property("name", data["name"])

    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>GET /planets/{planet_id}</b><br>"
        f"Status: {response.status_code}<br>"
        f"Name: {data['name']}<br>"
        f"Diameter: {data['diameter']}<br>"
        f"Population: {data['population']}<br>"
        f"</div>"
    ))

    assert response.status_code == expected_status_code
    assert data["name"] == expected_name
    assert data["diameter"] == expected_diameter
    assert data["population"] == expected_population



@pytest.mark.parametrize("invalid_id", [-1, 0, 61, 9999, "abc"])
def test_get_planets_invalid_id(api_base_url, invalid_id):
    response = requests.get(f"{api_base_url}/planets/{invalid_id}")
    assert response.status_code == 404
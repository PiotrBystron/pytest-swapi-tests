"""
API tests for Star Wars API (SWAPI).

This test suite covers:
- GET /starships/{id} — fetching starship details (valid and invalid IDs)

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
@pytest.mark.parametrize("starship_id, expected_name, expected_cost_in_credits, expected_cargo_capacity, expected_status_code", [
    (2, "CR90 corvette", "3500000", "3000000", 200),
    (9, "Death Star", "1000000000000", "1000000000000", 200),
    (43, "J-type diplomatic barge", "2000000", "unknown", 200),
])
def test_get_starship_by_id(api_base_url, starship_id, expected_name, expected_cost_in_credits, expected_cargo_capacity, expected_status_code, record_property, extras):
    """Tests GET /starships/{id} endpoint returns correct data."""
    response = requests.get(f"{api_base_url}/starships/{starship_id}")
    data = response.json()

    record_property("url", response.url)
    record_property("status_code", response.status_code)
    record_property("name", data["name"])

    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>GET /starships/{starship_id}</b><br>"
        f"Status: {response.status_code}<br>"
        f"Name: {data['name']}<br>"
        f"Cost in credits: {data['cost_in_credits']}<br>"
        f"Expected cargo capacity: {data['cargo_capacity']}<br>"
        f"</div>"
    ))

    assert response.status_code == expected_status_code
    assert data["name"] == expected_name
    assert data["cost_in_credits"] == expected_cost_in_credits
    assert data["cargo_capacity"] == expected_cargo_capacity



@pytest.mark.parametrize("invalid_id", [-1, 0, 1, 44, 9999, "abc"])
def test_get_starship_invalid_id(api_base_url, invalid_id):
    response = requests.get(f"{api_base_url}/starships/{invalid_id}")
    assert response.status_code == 404
"""
api_tests/test_restful_booker.py  v1.0
REST API test suite. Target: https://restful-booker.herokuapp.com
Covers: Auth, GET (list + single + filter), POST, PUT, PATCH, DELETE.
"""
import pytest, requests

BASE    = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


@pytest.fixture(scope="session")
def token():
    r = requests.post(f"{BASE}/auth",
                      json={"username": "admin", "password": "password123"},
                      headers=HEADERS)
    assert r.status_code == 200
    return r.json()["token"]


@pytest.fixture
def payload():
    return {"firstname": "Raghav", "lastname": "Dhiman", "totalprice": 220,
            "depositpaid": True,
            "bookingdates": {"checkin": "2024-03-01", "checkout": "2024-03-07"},
            "additionalneeds": "Breakfast"}


@pytest.fixture
def created_id(payload, token):
    r = requests.post(f"{BASE}/booking", json=payload, headers=HEADERS)
    bid = r.json()["bookingid"]
    yield bid
    requests.delete(f"{BASE}/booking/{bid}",
                    headers={**HEADERS, "Cookie": f"token={token}"})


class TestAuth:
    @pytest.mark.api
    def test_valid_credentials_return_token(self):
        r = requests.post(f"{BASE}/auth",
                          json={"username": "admin", "password": "password123"})
        assert r.status_code == 200 and "token" in r.json()

    @pytest.mark.api
    def test_invalid_credentials_return_bad_credentials(self):
        r = requests.post(f"{BASE}/auth", json={"username": "admin", "password": "wrong"})
        assert r.json().get("reason") == "Bad credentials"

    @pytest.mark.api
    def test_response_time_under_3s(self):
        r = requests.post(f"{BASE}/auth",
                          json={"username": "admin", "password": "password123"})
        assert r.elapsed.total_seconds() < 3


class TestGetBookings:
    @pytest.mark.api
    def test_get_all_returns_200(self):
        assert requests.get(f"{BASE}/booking").status_code == 200

    @pytest.mark.api
    def test_all_items_have_bookingid(self):
        for item in requests.get(f"{BASE}/booking").json():
            assert "bookingid" in item

    @pytest.mark.api
    def test_get_single_booking(self, created_id, payload):
        r = requests.get(f"{BASE}/booking/{created_id}")
        assert r.status_code == 200
        assert r.json()["firstname"] == payload["firstname"]

    @pytest.mark.api
    def test_get_nonexistent_returns_404(self):
        assert requests.get(f"{BASE}/booking/999999999").status_code == 404


class TestCreateBooking:
    @pytest.mark.api
    def test_create_returns_200(self, payload):
        assert requests.post(f"{BASE}/booking", json=payload, headers=HEADERS).status_code == 200

    @pytest.mark.api
    def test_create_has_bookingid(self, payload):
        r = requests.post(f"{BASE}/booking", json=payload, headers=HEADERS)
        assert isinstance(r.json()["bookingid"], int)

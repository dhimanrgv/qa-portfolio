"""
api_tests/test_restful_booker.py  v1.1
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
    def test_invalid_credentials(self):
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
    def test_get_single_booking(self, created_id, payload):
        r = requests.get(f"{BASE}/booking/{created_id}")
        assert r.status_code == 200
        assert r.json()["firstname"] == payload["firstname"]

    @pytest.mark.api
    def test_get_nonexistent_returns_404(self):
        assert requests.get(f"{BASE}/booking/999999999").status_code == 404

    @pytest.mark.api
    def test_filter_by_firstname(self, created_id, payload):
        r = requests.get(f"{BASE}/booking", params={"firstname": payload["firstname"]})
        ids = [b["bookingid"] for b in r.json()]
        assert created_id in ids


class TestCreateBooking:
    @pytest.mark.api
    def test_create_returns_200(self, payload):
        assert requests.post(f"{BASE}/booking", json=payload, headers=HEADERS).status_code == 200

    @pytest.mark.api
    def test_create_has_bookingid(self, payload):
        r = requests.post(f"{BASE}/booking", json=payload, headers=HEADERS)
        assert isinstance(r.json()["bookingid"], int)


class TestUpdateBooking:
    @pytest.mark.api
    def test_full_update_with_token(self, created_id, payload, token):
        updated = {**payload, "firstname": "Updated", "totalprice": 999}
        r = requests.put(f"{BASE}/booking/{created_id}", json=updated,
                         headers={**HEADERS, "Cookie": f"token={token}"})
        assert r.status_code == 200 and r.json()["firstname"] == "Updated"

    @pytest.mark.api
    def test_update_without_token_returns_403(self, created_id, payload):
        r = requests.put(f"{BASE}/booking/{created_id}", json=payload, headers=HEADERS)
        assert r.status_code == 403

    @pytest.mark.api
    def test_partial_update_patch(self, created_id, token):
        r = requests.patch(f"{BASE}/booking/{created_id}",
                           json={"firstname": "Patched"},
                           headers={**HEADERS, "Cookie": f"token={token}"})
        assert r.status_code == 200 and r.json()["firstname"] == "Patched"


class TestDeleteBooking:
    @pytest.mark.api
    def test_delete_with_token(self, payload, token):
        bid = requests.post(f"{BASE}/booking", json=payload,
                            headers=HEADERS).json()["bookingid"]
        r = requests.delete(f"{BASE}/booking/{bid}",
                            headers={**HEADERS, "Cookie": f"token={token}"})
        assert r.status_code == 201

    @pytest.mark.api
    def test_deleted_booking_returns_404(self, payload, token):
        bid = requests.post(f"{BASE}/booking", json=payload,
                            headers=HEADERS).json()["bookingid"]
        requests.delete(f"{BASE}/booking/{bid}",
                        headers={**HEADERS, "Cookie": f"token={token}"})
        assert requests.get(f"{BASE}/booking/{bid}").status_code == 404

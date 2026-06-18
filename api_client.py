import requests
from requests.exceptions import HTTPError, RequestException, Timeout

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(api_url=API_URL, timeout_seconds=10):
    try:
        response = requests.get(api_url, timeout=timeout_seconds)
        response.raise_for_status()
    except Timeout as exc:
        raise ConnectionError(f"API request timed out after {timeout_seconds} seconds") from exc
    except HTTPError as exc:
        raise ConnectionError(f"API returned HTTP error {exc.response.status_code}") from exc
    except RequestException as exc:
        raise ConnectionError("Failed to connect to the API") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise ValueError("Invalid JSON response from API") from exc

    if not isinstance(data, list):
        raise ValueError("Unexpected API response format: expected a list of users")

    return data

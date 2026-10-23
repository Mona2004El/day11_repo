
import requests

username = input("Enter GitHub username: ").strip()

url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 404:
        print("User not found")
        raise SystemExit

    response.raise_for_status()

    user_data = response.json()

    print("Login:", user_data.get("login", "Not available"))
    print("Public repos:", user_data.get("public_repos", "Not available"))

    # Challenge
    print("Profile URL:", user_data.get("html_url", "Not available"))
    print("Followers:", user_data.get("followers", "Not available"))

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")

except requests.exceptions.RequestException as error:
    print(f"Network or HTTP error: {error}")
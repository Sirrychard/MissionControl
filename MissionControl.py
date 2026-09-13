import httpx
import certifi

API_URL = "https://ll.thespacedevs.com/2.3.0/launches/upcoming/"


def get_upcoming_launches():
    response = httpx.get(
        API_URL,
        params={
            "limit": 10
        },
        timeout=10.0,
        verify=certifi.where(),
        trust_env=False
    )

    response.raise_for_status()
    return response.json()


def main():
    data = get_upcoming_launches()

    print()
    print("========================================")
    print("           MISSION CONTROL")
    print("========================================")
    print(f"Upcoming launches found: {data['count']}")
    print()

    for launch in data["results"]:
        print(f"Mission: {launch['name']}")
        print(f"Launch:  {launch['net']}")
        print(f"Status:  {launch['status']['name']}")
        print("----------------------------------------")


if __name__ == "__main__":
    main()
import httpx
import certifi

from datetime import datetime
from models.Launch import Launch

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

# New model to receive the info and transform it into data
def parse_launch(data):
    return Launch(
        id=data["id"],
        name=data["name"],
        launch_time=datetime.fromisoformat(
            data["net"].replace("Z", "+00:00")
        ) if data.get("net") else None,
        status=data["status"]["name"],
        launch_service_provider=(
            data["launch_service_provider"]["name"]
            if data.get("launch_service_provider")
            else None
        ),
        rocket=(
            data["rocket"]["configuration"]["full_name"]
            if data.get("rocket") and data["rocket"].get("configuration")
            else None
        ),
        mission_description=(
            data["mission"]["description"]
            if data.get("mission")
            else None
        ),
        orbit=(
            data["mission"]["orbit"]["name"]
            if data.get("mission") and data["mission"].get("orbit")
            else None
        ),
        pad=(
            data["pad"]["name"]
            if data.get("pad")
            else None
        ),
        location=(
            data["pad"]["location"]["name"]
            if data.get("pad") and data["pad"].get("location")
            else None
        ),
        country=data.get("country_code"),
        probability=data.get("probability")
    )

def main():
    data = get_upcoming_launches()

    # parse data
    launches = [
        parse_launch(launch_data)
        for launch_data in data["results"]
        ]

    print()
    print("========================================")
    print("           MISSION CONTROL")
    print("========================================")
    print(f"Upcoming launches found: {data['count']}")
    print()

    for launch in launches:
        print(f"Mission: {launch.name}")
        print(f"Launch:  {launch.launch_time}")
        print(f"Status:  {launch.status}")
        print(f"Provider: {launch.launch_service_provider}")
        print(f"Rocket: {launch.rocket}")
        print("----------------------------------------")


if __name__ == "__main__":
    main()
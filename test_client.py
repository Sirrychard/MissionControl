from api_client.launch_library_client import LaunchLibraryClient


def main():

    client = LaunchLibraryClient()

    launches = client.get_all_upcoming_launches()

    print()
    print("========================================")
    print("       FULL LAUNCH SYNC TEST")
    print("========================================")
    print(f"Total launches retrieved: {len(launches)}")
    print()

    for launch in launches[:10]:
        print(launch["name"])


if __name__ == "__main__":
    main()
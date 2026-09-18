from database.database import SessionLocal
from application.launch_service import LaunchService


def main():

    session = SessionLocal()

    try:

        service = LaunchService()

        launches = service.get_all_launches(
            session
        )

        print()
        print("========================================")
        print("       DATABASE TEST")
        print("========================================")
        print(
            f"Launches in database: "
            f"{len(launches)}"
        )
        print()

        for launch in launches[:10]:
            print(
                f"{launch.name} | "
                f"{launch.launch_time}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    main()
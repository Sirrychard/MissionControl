from sqlalchemy.orm import Session
from datetime import datetime, timezone

from database.launch_model import LaunchRecord
from models.Launch import Launch
from sqlalchemy import or_

# This will serve as the connector from backend to frontend database
class LaunchService:

    def save_launches(
        self,
        session: Session,
        launches: list[Launch]
    ) -> int:

        saved_count = 0

        for launch in launches:

            existing_launch = session.get(
                LaunchRecord,
                launch.id
            )

            # handle new launches or updates
            if existing_launch:
                existing_launch.name = launch.name
                existing_launch.launch_time = launch.launch_time
                existing_launch.status = launch.status
                existing_launch.launch_service_provider = (
                    launch.launch_service_provider
                )
                existing_launch.rocket = launch.rocket
                existing_launch.mission_description = (
                    launch.mission_description
                )
                existing_launch.orbit = launch.orbit
                existing_launch.pad = launch.pad
                existing_launch.location = launch.location
                existing_launch.country = launch.country
                existing_launch.probability = launch.probability

            else:
                record = LaunchRecord(
                    id=launch.id,
                    name=launch.name,
                    launch_time=launch.launch_time,
                    status=launch.status,
                    launch_service_provider=(
                        launch.launch_service_provider
                    ),
                    rocket=launch.rocket,
                    mission_description=(
                        launch.mission_description
                    ),
                    orbit=launch.orbit,
                    pad=launch.pad,
                    location=launch.location,
                    country=launch.country,
                    probability=launch.probability
                )

                session.add(record)
                saved_count += 1

        session.commit()

        return saved_count

    def get_launches(
        self,
        session: Session,
        limit: int = 20,
        offset: int = 0,
        status: str | None = None,
        provider: str | None = None,
        country: str | None = None,
        search: str | None = None
    ) -> tuple[list[LaunchRecord], int]:

        query = session.query(LaunchRecord)

        if status:
            query = query.filter(
                LaunchRecord.status == status
            )

        if provider:
            query = query.filter(
                LaunchRecord.launch_service_provider.ilike(
                    f"%{provider}%"))

        if country:
            query = query.filter(
                LaunchRecord.country == country.upper())

        if search:
            search_pattern = f"%{search}%"

            query = query.filter(
                or_(
                    LaunchRecord.name.ilike(search_pattern),
                    LaunchRecord.rocket.ilike(search_pattern),
                    LaunchRecord.launch_service_provider.ilike(
                        search_pattern)))

        total = query.count()

        # Smart query now returns info needed
        launches = (
            query
            .order_by(LaunchRecord.launch_time)
            .offset(offset)
            .limit(limit)
            .all())

        return launches, total

    # This method retrieves upcoming launches
    def get_upcoming_launches(
        self,
        session: Session,
        limit: int = 10
    ) -> list[LaunchRecord]:

        now = datetime.now(timezone.utc) # only receive new launches
        return (
            session.query(LaunchRecord)
            .filter(
                LaunchRecord.launch_time.is_not(None),
                LaunchRecord.launch_time > now
            )
            .order_by(
                LaunchRecord.launch_time
            )
            .limit(limit)
            .all()
        )
    def get_launch_by_id(
        self,
        session: Session,
        launch_id: str
    ) -> LaunchRecord | None:

        return session.get(
            LaunchRecord,
            launch_id
        )

    # test
    def get_all_launches(
        self,
        session: Session
    ) -> list[LaunchRecord]:

        return (
            session.query(LaunchRecord)
            .order_by(LaunchRecord.launch_time)
            .all()
        )
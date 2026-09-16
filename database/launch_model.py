from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base

# This creates the database and then will fill it with api info
class LaunchRecord(Base):
    __tablename__ = "launches"

    id: Mapped[str] = mapped_column(
        String(100),
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    launch_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    launch_service_provider: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    rocket: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    mission_description: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    orbit: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
        
    )

    pad: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    country: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    probability: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )



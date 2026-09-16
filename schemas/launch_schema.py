from datetime import datetime
from pickletools import stringnl_noescape_pair
from pydantic import BaseModel
from sqlalchemy.orm import strategy_options

class LaunchSchema(BaseModel):
    id: str
    name: str
    launch_time: datetime | None
    status: str
    launch_service_provider: str | None
    rocket: str | None
    mission_description: str | None
    orbit: str | None
    pad: str | None
    location: str | None
    country: str | None
    probability: int | None

    class Config:
        from_attributes = True



# NEW SCHEMA TO HELP PAGINATION
class LaunchListSchema(BaseModel):
    items: list[LaunchSchema]
    total: int
    limit: int
    offset: int

from dataclasses import dataclass
from datetime import datetime

# storing info from the json api object on launch info
@dataclass 
class Launch:
    id: str
    name: str
    launch_time: datetime | None
    status: str
    launch_service_provider: str | None
    rocket : str | None
    mission_description: str | None
    orbit: str | None
    pad: str | None
    location: str | None
    country: str | None
    probability: int | None


from fastapi import FastAPI, HTTPException, Query

from database.database import SessionLocal
from application.launch_service import LaunchService
from schemas.launch_schema import (
    LaunchListSchema, LaunchSchema)

# CREATING MY OWN API
# I will use this api to connect to my database from the front end

app = FastAPI(
    title="Mission Control API",
    description="Spaceflight intelligence API",
    version="1.0.0"
)

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "Mission Control API"}


# Now retrieve info from database using this API
# Update to schema so that data is not just raw return
@app.get("/launches", response_model=LaunchListSchema)
def get_launches(
    limit: int = Query(
        default=20,
        ge=1,
        le=100
        ),
    offset: int = Query(
        default=0,
        ge=0
    ),
    status: str | None = None,
    provider: str | None = None,
    country: str | None = None,
    search: str | None = None
    ):

    session = SessionLocal()

    try:
        service = LaunchService()

        launches, total = service.get_launches(
            session=session,
            limit=limit,
            offset=offset,
            status=status,
            provider=provider,
            country=country,
            search=search
        )

        return {
    "items": launches,
    "total": total,
    "limit": limit,
    "offset": offset
}
    finally:
        session.close()

@app.get(
    "/launches/{launch_id}",
    response_model=LaunchSchema
)
def get_launch(
    launch_id: str
):

    session = SessionLocal()

    try:
        service = LaunchService()

        launch = service.get_launch_by_id(
            session,
            launch_id
        )

        if launch is None:
           raise HTTPException(
               status_code=404,
               detail="Launch not found")

        return launch

    finally:
        session.close()
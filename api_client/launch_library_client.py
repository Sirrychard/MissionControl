from os import error
import httpx
import certifi
import time
import logging

logger = logging.getLogger(__name__)

class LaunchLibraryClient:

    BASE_URL = "https://ll.thespacedevs.com/2.3.0"

    def get_upcoming_launches(
        self,
        limit: int = 100,
        offset: int = 0
    ):
        try:

            response = httpx.get(
                f"{self.BASE_URL}/launches/upcoming/",
                params={
                    "limit": limit,
                    "offset": offset
                },
                timeout=30.0,
                verify=certifi.where(),
                trust_env=False
            )

            if response.status_code == 429:

                retry_after = response.headers.get(
                    "Retry-After"
                )

                if retry_after:
                    wait_time = int(retry_after)

                    
                    logger.warning(
                        f"Rate limited. "
                        f"Waiting {wait_time} seconds...")

                    time.sleep(wait_time)

                    return self.get_upcoming_launches(
                        limit,
                        offset
                    )

                raise RuntimeError(
                    "Space Devs API rate limit reached."
                )

            response.raise_for_status()

            return response.json()

        except httpx.TimeoutException as error:

            logger.error(
                "Space Devs API request timed out.")

            raise RuntimeError(
                "Space Devs API request timed out."
            ) from error

        except httpx.RequestError as error:

            logger.error(
                "Unable to connect to Space Devs API.")

            raise RuntimeError(
                "Unable to connect to Space Devs API."
            ) from error

    # New pagination function
    def get_all_upcoming_launches(
        self,
        page_size: int = 100
        ):

            all_launches = []
            offset = 0

            while True:

                data = self.get_upcoming_launches(
                    limit=page_size,
                    offset=offset
                )

                #gather results
                launches = data["results"]

                all_launches.extend(launches)

                print(
                    f"Retrieved {len(all_launches)}"
                    f" of {data['count']} launches..."
                )
                logger.info(
                    f"Retrieved {len(all_launches)} "
                    f"of {data['count']} launches...")

                if not data.get("next"):
                    break

                time.sleep(2) # to handle api rejections

                offset += page_size


            return all_launches
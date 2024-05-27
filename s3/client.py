import os
from contextlib import asynccontextmanager

from aiobotocore.session import get_session

from .config import S3Config


class S3Client:
    def __init__(self, config: S3Config):
        self.config = {
            'aws_access_key_id': config.access_key,
            'aws_secret_access_key': config.secret_key,
            'endpoint_url': config.endpoint_url,
        }
        self.bucket = config.bucket
        self.session = get_session()

    @asynccontextmanager
    async def connect(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
        self,
        file_path: str,
        name: str | None = None,
    ):
        if not name:
            name = os.path.basename(file_path)
        async with self.connect() as client:
            with open(file_path, "rb") as file:
                await client.put_object(
                    Bucket=self.bucket,
                    Key=name,
                    Body=file,
                )

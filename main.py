import asyncio
import os

from dotenv import load_dotenv

from s3 import S3Client, S3Config


async def main():
    load_dotenv(".env")
    s3_client = S3Client(
        S3Config(
            access_key=os.environ.get("S3_ACCESS_KEY"),
            secret_key=os.environ.get("S3_SECRET_KEY"),
            endpoint_url=os.environ.get("S3_URL"),
            bucket=os.environ.get("S3_BUCKET"),
        )
    )
    await s3_client.upload_file("./files/softbananaslogo.jpg")

if __name__ == "__main__":
    asyncio.run(main())
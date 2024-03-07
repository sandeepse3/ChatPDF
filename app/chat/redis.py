from dotenv import load_dotenv
import os
import redis
load_dotenv()
client = redis.Redis.from_url(
    os.environ["REDIS_URI"],
    decode_responses=True
)
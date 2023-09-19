from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time
import datetime

# Configuration
token = "mytoken"
org = "myorg"  # Replace with your actual organization name
bucket = "mybucket"  # Replace with your bucket name

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)
end_time = datetime.datetime.now()  # current time
start_time = end_time - datetime.timedelta(days=30)  # 30 days ago

# Loop through each hour of the last 30 days
current_time = start_time
while current_time <= end_time:
    temperature = random.randint(20, 30)
    humidity = random.randint(50, 70)

    point = Point("room_metrics").tag("room", "living_room").field("temperature", temperature).field("humidity", humidity).time(current_time)
    write_api.write(bucket, org, point)

    # Increase by 1 hour
    current_time += datetime.timedelta(hours=1)

# Close the client resources
client.close()
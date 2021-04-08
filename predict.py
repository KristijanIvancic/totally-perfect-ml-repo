import json

import boto3
import numpy as np
from joblib import load
import psycopg2

# Configure input queue
sqs = boto3.resource("sqs")
queue = sqs.get_queue_by_name(QueueName="weather-input-queue")

# Configure output database
conn = psycopg2.connect("weather.us-east-1.rds.amazonaws.com")
cur = conn.cursor()

INSERT = """
    INSERT INTO weather_predictions (location, date, prediction)
    VALUES (%s, %s, %s)
"""


if __name__ == "__main__":

    model = load("model.joblib")

    # Read all messages from the queue
    for message in queue.receive_messages():

        # Get and format input data
        input_data = json.loads(message.body)
        formatted_input = np.array(input_data["features"])

        prediction = model.predict(formatted_input)

        # Insert prediction into the database
        cur.execute(INSERT, (input_data["location"], input_data["date"], prediction))
        conn.commit()

        # Let the queue know that the message is processed
        message.delete()

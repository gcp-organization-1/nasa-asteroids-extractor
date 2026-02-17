from google.cloud import storage
from config.settings import settings
import json

class GCSClient:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(settings.ASTEROIDS_BUCKET)

    def upload_raw_data_to_gcs(self, data, destination):
        blob = self.bucket.blob(destination)

        blob.upload_from_string(
            json.dumps(data),
            content_type="application/json"
        )
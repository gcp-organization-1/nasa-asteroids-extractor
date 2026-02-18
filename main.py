from extractor.asteroids_extractor import AsteroidsExtractor
from gcp.gcs import GCSClient
from config.logger import logger

def main(request):
    request_json = request.get_json(silent=True)

    start_date = request_json.get("start_date")
    end_date = request_json.get("end_date")


    if not start_date or not end_date:
        return {"error": "start_date and end_date are required"}, 400


    extractor = AsteroidsExtractor(start_date, end_date)
    gcs = GCSClient()
    filename = f"extracted/asteroids_{start_date}_{end_date}.json"
    try:
        data = extractor.get_asteroids_data()
        logger.info("Uploading raw data to cloud storage", data)
        gcs.upload_raw_data_to_gcs(data, filename)
        logger.info("Uploaded successfully")
        return {"message": "Extract complete", "file_path": filename}
    except Exception as e:
        return {"error": str(e)}, 500

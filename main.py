from extractor.asteroids_extractor import AsteroidsExtractor

def main(request):
    request_json = request.get_json(silent=True)

    start_date = request_json.get("start_date")
    end_date = request_json.get("end_date")


    if not start_date or not end_date:
        return {"error": "start_date and end_date are required"}, 400


    extractor = AsteroidsExtractor(start_date, end_date)
    try:
        data = extractor.get_asteroids_data()
        return data
    except Exception as e:
        return {"error": str(e)}, 500

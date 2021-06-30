

class SnowRescueService(object):
    def __init__(self, weather_forecast_service, municipal_services, press_service):
        self.municipal_services = municipal_services
        self.press_service = press_service
        self.weather_forecast_service = weather_forecast_service

    def check_forecast_and_rescue(self):
        print("TODO implementation here")
        print(self.weather_forecast_service.get_snow_fall_height_in_mm())

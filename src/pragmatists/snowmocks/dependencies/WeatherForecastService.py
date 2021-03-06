from abc import ABCMeta, abstractmethod


class WeatherForecastService:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_snow_fall_height_in_mm(self):
        pass

    @abstractmethod
    def get_average_temperature_in_celsius(self):
        pass
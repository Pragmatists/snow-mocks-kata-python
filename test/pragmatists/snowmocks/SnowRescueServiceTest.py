import unittest
from mock import Mock, call

from src.pragmatists.snowmocks import SnowRescueService
from src.pragmatists.snowmocks.dependencies.WeatherForecastService import WeatherForecastService
from src.pragmatists.snowmocks.dependencies.MunicipalServices import MunicipalServices
from src.pragmatists.snowmocks.dependencies.PressService import PressService

#A testcase is created by subclassing unittest.TestCase.
class SnowRescueServiceTest(unittest.TestCase):

    def setUp(self):
        # create test doubles
        self.press_service = Mock(spec=PressService)
        self.municipal_services = Mock(spec=MunicipalServices)
        self.weather_forecast_service = Mock(spec=WeatherForecastService)

        # itit service and inject test dubles as dependencies
        self.service = SnowRescueService.SnowRescueService(self.weather_forecast_service, self.municipal_services, self.press_service)


    #tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.
    def test_start_here(self):
        self.service.check_forecast_and_rescue()

if __name__ == '__main__':
    unittest.main()


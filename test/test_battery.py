import datetime
import unittest
from mycars.battery import NubbinBattery, SpindlerBattery


class Test_NubbinBattery(unittest.TestCase):
    def test_need_service(self):
       need_service = NubbinBattery(last_service_date=datetime.date(2015, 5, 12)).need_service()
       assert need_service == True

class Test_SpindlerBattery(unittest.TestCase):
    def test_need_service(self):
       need_service = SpindlerBattery(last_service_date=datetime.date(2015, 5, 12)).need_service()
       assert need_service == True

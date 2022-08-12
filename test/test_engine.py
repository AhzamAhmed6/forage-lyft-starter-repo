import datetime
import unittest

from mycars.engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class Test_CapuletEngine(unittest.TestCase):
    def test_need_service(self):
        need_service = CapuletEngine(last_service_mileage=70000, current_milage=140000).need_service()
        print(need_service)
        assert need_service==True

class Test_WilloughbyEngine(unittest.TestCase):
    def test_need_service(self):
        need_service = WilloughbyEngine(last_service_mileage=70000, current_milage=110000).need_service()
        print(need_service)
        assert need_service==False

class Test_SternmanEngine(unittest.TestCase):
    def test_need_service(self):
        need_service = SternmanEngine(warning_light=True).need_service()
        print(need_service)
        assert need_service==False
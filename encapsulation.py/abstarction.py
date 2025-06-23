from abc import ABC, abstractmethod
class vehicle(ABC):
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class car(vehicle):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("engine stop")
my_car =car()
my_car.start_engine()
my_car.stop_engine()
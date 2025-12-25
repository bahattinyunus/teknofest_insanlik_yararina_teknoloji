"""
Sensor Manager Module
Responsible for interfacing with physical sensors and hardware.
"""

import random

class SensorManager:
    def __init__(self):
        self.active_sensors = []
        
    def initialize_sensors(self):
        """
        Detects and initializes available sensors.
        """
        # Mock initialization
        self.active_sensors = ["Temp_01", "GPS_01", "Camera_Basic"]
        print(f"Sensors initialized: {self.active_sensors}")
        
    def read_all(self):
        """
        Reads data from all active sensors.
        
        Returns:
            dict: A dictionary mapping sensor IDs to their read values.
        """
        data = {}
        for sensor in self.active_sensors:
            # Simulate reading
            data[sensor] = random.random()
        return data

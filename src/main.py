"""
Teknofest Humanity Technology Project - Main Entry Point
Developed by: Bahattin Yunus Çetin
"""

import sys
import os

def main():
    """
    Main function to initialize the application.
    """
    print("--------------------------------------------------")
    print("   TEKNOFEST HUMANITY TECHNOLOGY SYSTEM STARTED   ")
    print("--------------------------------------------------")
    print("Initiating system check...")
    
    # Initialize Modules
    from modules.sensor_manager import SensorManager
    from modules.data_processor import process_data
    
    sensor_mgr = SensorManager()
    sensor_mgr.initialize_sensors()
    
    print("Reading sensors...")
    data = sensor_mgr.read_all()
    
    print("Processing data...")
    result = process_data(data)
    
    print(f"System Operational. Logic Result: {result}")

if __name__ == "__main__":
    main()

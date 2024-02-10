import threading
import logging
import time

# Third Party Imports
import pandas as pd

# Local Imports
from gpu_devices.gpu_devices.nvidia_gpu import Nvidia


format = "%(asctime)s: %(message)s"
logger = logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

class NvidiaPoller:
    """Class usedd to run NVIDIA metrics"""

    def __init__(self):
        """Constructor"""
        self.nvidia = Nvidia()
        self.handles = self.nvidia.get_handles()


    def collect_gpu_diagnostic_data(self):
        """Method used to collect diagnostic data"""
        for handle_n in self.handles:
            clock_info = self.nvidia.get_clock_info(handle_n)
            temperature = self.nvidia.get_temperature(handle_n)
            ecc_counts = self.nvidia.get_gpu_ecc_errors(handle_n)
            total_memory, free_memory, used_memory = self.nvidia.get_gpu_video_memory_info(handle_n)
            
        return handle_n, clock_info, temperature, ecc_counts, total_memory, free_memory, used_memory




        
def main():
    """Main method"""
    nvidia_poller = NvidiaPoller()
    polling_thread = threading.Thread(target=nvidia_poller.collect_gpu_diagnostic_data())
    polling_thread.daemon = True
    polling_thread.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting GPU Diagnostics!")



if __name__  == """__main__""":
    main()
    
# Local Imports
from gpu_devices.nvidia_gpu import Nvidia




class NvidiaDiagnostics:
    """Class used for running NVIDIA Diagnostic parameters"""

    def __init__(self):
        """Constructor"""
        self.nvidia_wrapper = Nvidia()
        self.handles = self.nvidia_wrapper.get_handles()

    def gpu_diagnostics(self):
        """Method used to run diagnostics on GPU"""

        try:
            while True:
                for _, handle in enumerate(self.handles):
                    clock_info = self.nvidia_wrapper.get_clock_info(handle)
                    temperature = self.nvidia_wrapper.get_temperature(handle)

                    return clock_info, temperature
        except KeyboardInterrupt:
            print("Cleared")
    
    
if __name__ == """__main__""":

    nvidia = NvidiaDiagnostics()
    clock_info = nvidia.gpu_diagnostics()
    print(clock_info)
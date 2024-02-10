import argparse
from gpu_devices.gpu_devices.nvidia_gpu import Nvidia



class NvidiaCLI:
    """Class used to interface with NVIDIA tools via command line interface"""


    def __init__(self, ecc=None, fan_speed=None, temp=None, power=None, pci=None, memory=None):
        """Constructor"""
        self.ecc = ecc 
        self.fan_speed = fan_speed
        self.temp = temp
        self.power = power
        self.pci = pci
        self.memory = memory
        self.nvidia_gpu = Nvidia()
    
    def get_handles(self):
        """Method used to get handles from GPU"""
        handles = self.nvidia_gpu.get_handles()

        return handles

    
    def run_individual_diagnostic(self):
        """Method used to run individual diagnostic"""
        handles = self.get_handles()
        for handle in handles:
            if self.ecc is not None:
                ecc_errors = self.nvidia_gpu.get_gpu_ecc_errors(handle)
            elif self.fan_speed is not None:
                fan_speed = self.nvidia_gpu.get_fan_speed(handle)
            elif self.temp is not None:
                temperature = self.nvidia_gpu.get_temperature(handle)
            elif self.power is not None:
                power_consumption = self.nvidia_gpu.get_power_info(handle)
            elif self.pci is not None:
                pci_diagnostics = self.nvidia_gpu.get_pci_information(handle)
            elif self.memory is not None:
                memory_diagnostics = self.nvidia_gpu.get_gpu_video_memory_info(handle)
            else:
                print("No diagnostics selected to run")        


    


if __name__ == """__main__""":
    args = argparse.ArgumentParser()
    args.add_argument("-e", "--ecc", type=str, help="Get ECC diagnostics from GPU")
    args.add_argument("-f", "--fanspeed", type=str, help="Get fan speed diagnostic data")
    args.add_argument("-t", "--temp", type=str, help="Get temperature diagnostic information from GPU")
    args.add_argument("-w", "--power", type=str, help="Get power consumption diagnostics from GPU")
    args.add_argument("-p", "--pci", type=str, help="Get pci diagnostics from GPU")
    args.add_argument("-m", "--memory", type=str, help="Get memory diagnostics from GPU")
    parsed_args = args.parse_args()
    ecc_diag = parsed_args.ecc
    fan_speed_diag = parsed_args.fanspeed
    temp_diag = parsed_args.temp
    power_diag = parsed_args.power
    pci_diag = parsed_args.pci
    memory_diag = parsed_args.memory
    nvidia_cli = NvidiaCLI(ecc=ecc_diag, fan_speed=fan_speed_diag, temp=temp_diag, power=power_diag, memory=memory_diag)



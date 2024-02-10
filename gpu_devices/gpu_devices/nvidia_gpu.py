from pynvml import *
from pynvml.smi import *
import pynvml
import subprocess

class Nvidia():
    """Class containing methods that will run GPU diagnostics on NVIDIA hardware"""

    def __init__(self):
        """Contstructor"""
        try:
            # Initialize NVML
            pynvml.nvmlInit()
            self.nvidia_instance = nvidia_smi.getInstance()
        except pynvml.NVMLError as error:
            print(f'{error}')
        finally:
            pynvml.nvmlShutdown()


    def query_memory(self):
        """Method used to query nvidia device memory"""
        self.nvidia_instance.DeviceQuery('memory.free, memory.total')
    
    def get_nvlink_utilization(self, handle):
        """Method used to get NVLINK utilization"""
        nvlink_utilization = nvml.nvmlDeviceGetNvLinkUtilizationCounter(handle)

        return nvlink_utilization

    def get_nvlink_error_counter(self, handle):
        """Method used to get NVLINK error counter"""
        nvlink_error_counter = nvml.nvmlDeviceGetNvLinkErrorCounter(handle)

        return nvlink_error_counter
    
    def get_nvlink_state(self, handle):
        """Method used to get NVLINK state"""
        nvlink_state = nvml.nvmlDeviceGetNvLinkState(handle)

        return nvlink_state

    def get_nvlink_utilization_control(self, handle):
        """Get NVLINK utilization control"""
        nvlink_utilization_control = pynvml.nvmlDeviceGetNvLinkUtilizationControl(handle)

        return nvlink_utilization_control
    
    def get_nvlink_power_threshold(self, handle):
        """Method used to get NVLINK low power threshold"""
        nvlink_power_threshold = pynvml.nvmlDeviceSetNvLinkDeviceLowPowerThreshold(handle)

        return nvlink_power_threshold

    
    def get_process_count_from_gpu(self, handle):
        """Method used to get process info from GPU"""
        process_count = pynvml.nvmlDeviceGetComputeRunningProcesses_v3(handle)
        
        
        return process_count
    
    def get_process_utilization(self, handle):
        """Method used to get process utilization"""
        process_utilization = pynvml.nvmlDeviceGetProcessUtilization(handle)

        return process_utilization
    
    def get_frame_buffer_usage(self, handle):
        """Method used to get frame buffer"""
        frame_buffer_counter = pynvml.nvmlVgpuInstanceGetFbUsage(handle)

        return frame_buffer_counter
    
    def get_frame_buffer_capture_stats(self, handle):
        """Method used to get frame buffer stats"""
        frame_buffer_stats = pynvml.nvmlDeviceGetFBCStats(handle)

        return frame_buffer_stats
    
    
    def get_led_state(self, handle):
        """Get LED state of from the GPU"""
        xid_errors = pynvml.nvmlUnitGetLedState

    def get_driver_version():
        """Getter method used to get driver version"""
        driver_version = nvmlSystemGetDriverVersion()
        
        return driver_version

    def get_retired_pages(self, handle):
        """Method used to get retired pages"""
        retired_pages = pynvml.nvmlDeviceGetRetiredPages(handle)

        return retired_pages

    def get_device_count(self):
        """Getter method used to get GPU device count from system"""
        device_count = pynvml.nvmlDeviceGetCount()

        return device_count
    
    def get_utilization_rates(self, handle):
        """Method used to get GPU utilization"""
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_utilization = utilization.gpu
        memory_utilization = utilization.memory

        return gpu_utilization, memory_utilization

    def get_power_info(self, handle):
        """Method used to get power info from GPU"""
        power_info = pynvml.nvmlDeviceGetPowerUsage(handle)
        
        return power_info / 1000.0

    def get_performance_state(self, handle):
        """Method used to get performance state of NVIDIA GPU"""
        performance_state = pynvml.nvmlDeviceGetPerformanceState(handle)

        return performance_state

    def get_clock_throttle_reasons(self, handle):
        """Method used to get GPU slow down temperature"""
        slow_down_temperature = pynvml.nvmlClocksThrottleReasonHwSlowdown(handle)

    def get_target_temperature(self, handle):
        """Method used to get target temeprature of GPU"""
        target_temperature = pynvml.nvmlDeviceGetTemperatureThreshold(handle)

        return target_temperature
    
    def get_firmware_version(self, handle):
        """Method used to firmware version from GPU"""
        firmware_version = pynvml.nvmlDeviceGetGspFirmwareVersion(handle)

        return firmware_version

    def get_clock_info(self, handle):
        """Method used to get clock info"""
        clock_info = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)

        return clock_info / 1000.0

    def get_gpu_multiinstance(self, handle):
        """Method used to check if GPU MIG is enabled"""
        mig_state = pynvml.nvmlDeviceGetMigMode(handle)

        return mig_state
    
    
    def get_fan_speed(self, handle):
        """Method used to get fan speed of GPU"""
        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        except pynvml.NVMLError as error:
            print(f"Error getting fan speed: {error}")
            raise error
        

    def get_gpu_ecc_errors(self, handle):
        """Method used to get ECC errors from GPU"""
        ecc_mode = pynvml.nvmlDeviceGetEccMode(handle)
        if ecc_mode == pynvml.NVML_FEATURE_ENABLED:
            ecc_counts = pynvml.nvmlDeviceGetDetailedEccErrors(handle)
        else:
            print("ECC not supported on this device")
        return ecc_counts

    def get_handles(self):
        """Method used to return handle"""
        device_count = self.get_device_count()
        handles= list()
        for i in range(device_count):
            handles.append(pynvml.nvmlDeviceGetHandleByIndex(0))

        return handles

    def get_temperature(self, handle):
        """Method used to get temeprature from GPU"""
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        return temperature 

    def get_gpu_video_memory_info(self, handle):
        """Method used to get memory info of GPU"""
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        total_memory = memory_info.total / (1024 ** 2)
        free_memory = memory_info.free / (1024 ** 2)
        used_memory = memory_info.used / (1024 ** 2)

        return total_memory, free_memory, used_memory
    
    def get_pci_information(self, handle):
        """Method used to return PCI information """
        pci_info = pynvml.nvmlDeviceGetPciInfo_v3(handle)
        bus  = pci_info.bus
        device_id = pci_info.device
        domain = pci_info.domain
        bus_type = pci_info.bustType
        bus_id = pci_info.busId

        return pci_info, bus, device_id, domain, bus_type, bus_id


    def get_clock_faults(self, handle):
        """Method used to get clock faults NVIDIA GPU """
        
        clock_faults = pynvml.nvmlDeviceGetCurrentClocksThrottleReasons(handle)
        
        return clock_faults
    
    def close_event(self):
        """Method used to shutdown NVML"""
        pynvml.nvmlShutdown()
            

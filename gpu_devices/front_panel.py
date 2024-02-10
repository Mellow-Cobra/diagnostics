# Standard Imports
import json
import sys

# Local Imports
from nvidia_gpu_diagnostics import NvidiaDiagnostics
from gpu_tools.furmark import Furmark

# Third Party Imports
import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QWidget, \
    QTabWidget, QApplication, QGridLayout, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class WorkerSignals(QObject):
    """Method defines the singals available from a running worker thread"""
    diag_info = pyqtSignal(list)
    

class GPUDiagnosticsThread(QRunnable):
    """Worker Thread class used to run GPU diagnostics"""
    
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.gpu_diag_routine = NvidiaDiagnostics()
        self.signals = WorkerSignals()
        
        
       
    
    def run(self):
        gpu_diag = list()
        
        for _ in range(100000):
            gpu_diag.append(self.gpu_diag_routine.gpu_diagnostics())
        self.signals.diag_info.emit(gpu_diag)

class FurmarkBenchmarkThread(QRunnable):
    """Worker Thread class used to run Furmark benchmark"""

    def __init__(self, height, width):
        """Constructor"""
        super().__init__()
        self.furmark_benchmark_routine = Furmark(height, width)

class FrontPanel(QWidget):
    """Class used for front panel"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("Diagnostics Tool")
        self.setGeometry(500, 500, 500, 500)
    
        # Main Layout
        main_layout = QVBoxLayout()

        # Tab Layout
        self.gpu_diagnostics_tab = QWidget()
        self.ssd_diagnostics_tab = QWidget()
        self.cpu_diagnostics_tab = QWidget()
        self.dimm_diagnostics_tab = QWidget()
        self.diagnostics_config_tab = QWidget()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.gpu_diagnostics_tab, "GPU Diagnostics Tab")
        self.tabs.addTab(self.ssd_diagnostics_tab, "SSD Diagnostics Tab")
        self.tabs.addTab(self.cpu_diagnostics_tab,  "CPU Diagnostics Tab")
        self.tabs.addTab(self.dimm_diagnostics_tab, "DIMM Diagnostics Tab")
        self.tabs.addTab(self.diagnostics_config_tab, "Diagnostic Utility Configuration Tab")

        

        # GPU Diagnostics Tab Layout
        gpu_diagnostics_tab_layout = QGridLayout()
        self.gpu_diag_output = QTextEdit()
        self.gpu_diagnostics = QPushButton("GPU Diagnostics")
        self.gpu_load_utilization = QPushButton("GPU Load Utilization")
        self.gpu_frame_buffer_usage = QPushButton("Frame Buffer Usage")
        self.fur_mark_bench_mark = QPushButton("Run Furmark Benchmark")
        gpu_diagnostics_tab_layout.addWidget(self.gpu_diagnostics, 0, 0)
        gpu_diagnostics_tab_layout.addWidget(self.gpu_load_utilization, 0 , 1)
        gpu_diagnostics_tab_layout.addWidget(self.gpu_frame_buffer_usage, 1, 0)
        gpu_diagnostics_tab_layout.addWidget(self.fur_mark_bench_mark, 1, 1)


        # Graph
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        gpu_diagnostics_tab_layout.addWidget(self.canvas, 3, 0)

        self.gpu_diagnostics.clicked.connect(self.on_run_gpu_diagnostics)
        self.gpu_diagnostics.clicked.connect(self.on_run_furmark_benchmark)
        self.gpu_diagnostics_tab.setLayout(gpu_diagnostics_tab_layout)

        # Config Tab Layout
        diag_config_tab_layout = QVBoxLayout()
        self.furmark_height = QLineEdit("Furmark Height")
        self.furmark_width = QLineEdit("Furmark Width")
        diag_config_tab_layout.addWidget(self.furmark_height)
        diag_config_tab_layout.addWidget(self.furmark_width)
        self.diagnostics_config_tab.setLayout(diag_config_tab_layout)
        

      

        
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.thread_pool = QThreadPool.globalInstance()

    def on_run_gpu_diagnostics(self):
        """Event handler for running GPU Diagnostics"""
        gpu_diagnostics_worker_thread = GPUDiagnosticsThread()
        self.thread_pool.start(gpu_diagnostics_worker_thread)
        gpu_diagnostics_worker_thread.signals.diag_info.connect(self.plot_diag_data)
    
    def on_run_furmark_benchmark(self):
        """Event handler for running furmark"""
        furmark_benchmark_worker_thread = FurmarkBenchmarkThread()
        self.thread_pool.start(furmark_benchmark_worker_thread)
    
    def read_config_file(self):
        """Method used to read config file"""
        with open(self.config_file, mode='r', encoding='utf-8') as diag_tool_config:
            json.load(diag_tool_config)
        
    def plot_diag_data(self, diag_info):
        clock = list()
        temperature = list()
        power_info = list()
        for _, data in enumerate(diag_info):
            clock.append(data[0])
        for _, data in enumerate(diag_info):
            temperature.append(data[1])
        for _, data in enumerate(diag_info):
            power_info.append(data[2])
        ax = self.figure.add_subplot(111)
        ax2 = self.figure.add_subplot(122)
        ax3 = self.figure.add_subplot(211)
        ax3.plot(power_info, "*-")
        ax2.plot(temperature, "*-")
        ax.plot(clock, '*-')
        self.canvas.draw()
    
   

        

app = QApplication(sys.argv)
window = FrontPanel()
window.show()
app.exec()
sys.exit(app.exec_())

        

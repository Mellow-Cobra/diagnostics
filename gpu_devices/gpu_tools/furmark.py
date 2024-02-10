import os
import subprocess
import pandas as pd
from typing import List 


class Furmark:

    def __init__(self, heights: List , widths: List, iterations: int, msaa_list: List):
        """Constructor"""
        self.heights = heights
        self.widths = widths
        self.iterations = iterations
        self.msaa_list = msaa_list

        if os.path.exists(r"C:\Program Files (x86)\Geeks3D\Benchmarks\FurMark"):
            os.chdir(r"C:\Program Files (x86)\Geeks3D\Benchmarks\FurMark")
        


    def run_resolution_sweep(self):
        ""
    
        for index, height in enumerate(self.heights):
            width = self.widths[index]
            msaa = self.msaa[index]
            stream = subprocess.run(rf".\furmark.exe /width={width} /height={height} /msaa={msaa}" \
                            r"/nogui /nomenubar /fullscreen /run_mode=1 /log_score", capture_output=True)
            output = stream.stdout()
            print(output)


    
    def parse_log_file():
        """Method used to parse results file for score, temperature, power, and current"""


if __name__ == """__main__""":
    widths = ["100", "400", "500", "600"]
    heights = ["339", "200", "700", "300"]
    msaas = ["1", "4", "5", "6"]
    furmark = Furmark(widths=widths, heights=heights, iterations=5, msaa_list=msaas)
    furmark.run_resolution_sweep()
    
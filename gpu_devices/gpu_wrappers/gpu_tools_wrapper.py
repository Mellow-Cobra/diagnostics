import argparse
import json 




class FurMarkCLI:
    """Class used for Furmark command line interface"""

    def __init__(self, height, width, msaa, iterations):
        """Constructor"""
        self.height = height
        self.width = width
        self.msaa = msaa
        self.iterations = iterations

class Radeon:
    """Class used for Radeon GPUs command line interface"""

    def __init__(self, height, width):
        """Constructor"""



if __name__ == """__main__""":
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", type=str, defualt="800", help="height of furmark stressor")
    parser.add_argument("-w", type=str, default="800", help="width of furmark stressor")
    parser.add_argument("--msaa", type=str, help="msaa for fur mark stressor")
    parser.add_argument("-i", type=int, default=1, help="number of iterations to run stressor")
    args = parser.parse_args()
    furMark = FurMarkCLI(height=args.h, width=args.w, msaa=args.msaa)
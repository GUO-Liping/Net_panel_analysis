#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# NetPanelAnalysis_V1_0_2主函数

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from part_to_compute import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
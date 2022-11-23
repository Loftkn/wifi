#!/usr/bin/python3

import sys
from PySide2 import *
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QMainWindow, QApplication)
from PySide2.QtCharts import QtCharts

from random import randrange
from functools import partial
import csv

# IMPORT GUI FILE
from ui_interface import *

## A LIST OF UI WIDGETS TO APPLY SHADOW
shadow_elements = {
    "left_menu_frame",
    "frame_3",
    "frame_15",
    "header_frame",
    "frame_9"
}

def read_wifipoints():
    print("GG")
    global wifi_points
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        next(csv_reader)
        for wifi in csv_reader:
            if wifi == []:
                break
            name = wifi[13].strip()
            if name == '':
                name = '#hidden#'
            wifi_points.append({'name': name,
                                   'MAC': wifi[0],
                                   'first_time': wifi[1].strip(),
                                  'last_time': wifi[2].strip(),
                                   'channel': wifi[3].strip(),
                                   'speed': wifi[4].strip(),
                                   'privacy': wifi[5].strip(),
                                  'cipher': wifi[6].strip(),
                                   'auth': wifi[7].strip(),
                                   'power': int(wifi[8].strip())
                                   })
    wifi_points = list(sorted(wifi_points, key=lambda item: item['power'], reverse=True))

## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        ## # Remove window tittle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ## # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        ## # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/pie-chart.svg"))
        # Set window tittle
        self.setWindowTitle("QT CHARTS")

        # Window Size grip to resize window
        QSizeGrip(self.ui.size_grip)

        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        #Left Menu toggle button (Show hide menu labels)
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        # Function to Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  

                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.header_frame.mouseMoveEvent = moveWindow

        # SHOW WINDOW
        self.show()
        # Apply shadow to widgets on shadow_elements list
        for x in shadow_elements:
                ## # Shadow effect style
                effect = QtWidgets.QGraphicsDropShadowEffect(self)
                effect.setBlurRadius(18)
                effect.setXOffset(0)
                effect.setYOffset(0)
                effect.setColor(QColor(0, 0, 0, 255))
                getattr(self.ui, x).setGraphicsEffect(effect)

        #navigate to Settings page
        self.ui.percentage_bar_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.read_wifipoints))
        self.ui.temperature_bar_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.nested_donut_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.line_chart_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi))
        self.ui.list_wifi_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi))
        self.ui.pushButton_100.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))

        self.create_list_wifi()
        self.create_nested_donuts()

    # Update restore button icon on msximizing or minimizing window
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

    # Slide left menu function
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_menu_frame.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-center.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(550)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation.start()


    # Add mouse events to the window
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    def create_nested_donuts(self):
        self.setMinimumSize(800, 600)
        self.donuts = []
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()
        self.chart.legend().setVisible(False)
        self.chart.setTitle("Nested donuts demo")
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_view.sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(sizePolicy)
        self.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.nested_donut_chart_cont.addWidget(self.chart_view, 0, 0, 9, 9)
        self.ui.frame_7.setStyleSheet(u"background-color: transparent")

        self.min_size = 0.1
        self.max_size = 0.9
        self.donut_count = 5

        self.setup_donuts()
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(1250)

    def setup_donuts(self):
        for i in range(self.donut_count):
            donut = QtCharts.QPieSeries()
            slccount = randrange(3, 6)
            for j in range(slccount):
                value = randrange(100, 200)

                slc = QtCharts.QPieSlice(str(value), value)
                slc.setLabelVisible(True)
                slc.setLabelColor(Qt.white)
                slc.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)

                # Connection using an extra parameter for the slot
                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))
                donut.append(slc)
                size = (self.max_size - self.min_size)/self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)



    def update_rotation(self):
        for donut in self.donuts:
            phase_shift =  randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def explode_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()
            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()
            donut = slc.series()
            idx = self.donuts.index(donut)
            #print(len(self.donuts))
            print(donut.count())
            for i in range(idx + 1, len(self.donuts)):
                self.donuts[i].setPieStartAngle(slice_endangle)
                self.donuts[i].setPieEndAngle(360 + slice_startangle)
            slc.doubleClicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.percentage_bar_chart))

        else:
            for donut in self.donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)

            self.update_timer.start()

        slc.setExploded(exploded)

    def create_list_wifi(self):
        global wifi_points
        categories = []
        low = QtCharts.QBarSet("Power")
        for i in range(0,len(wifi_points)):
            pwr = 100 + wifi_points[i]["power"]
            low.append(pwr)
            if(pwr > 100):
                low.append(pwr - 100)
            print(100 + wifi_points[i]["power"], wifi_points[i]["name"])
            categories.append(wifi_points[i]["name"])

        series = QtCharts.QStackedBarSeries()
        series.append(low)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)


        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisY = QtCharts.QValueAxis()
        axisY.setRange(0, 105 + wifi_points[0]["power"])
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisX)
        series.attachAxis(axisY)


        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chart_view.sizePolicy().hasHeightForWidth())
        chart_view.setSizePolicy(sizePolicy)
        chart_view.setMinimumSize(QSize(0, 10))
        self.ui.list_wifi_cont.addWidget(chart_view, 0, 0, 9, 9)
        self.ui.frame_2.setStyleSheet(u"background-color: transparent")



wifi_points = []

if __name__ == "__main__":
    read_wifipoints()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

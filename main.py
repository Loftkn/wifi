#!/usr/bin/python3


import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPainter, QColor
from PySide2.QtWidgets import QMainWindow, QWidget, QScrollArea, QVBoxLayout, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QSizePolicy, QFrame, QPushButton, QLabel
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPropertyAnimation, QSize, QTimer, Qt
import pyqtgraph as pg
from PySide2.QtCore import QPropertyAnimation, QSize, QTimer, Qt, QRect, QCoreApplication
from random import randrange
from functools import partial
import csv

from ui_interface import Ui_MainWindow


shadow_elements = {
    "left_menu_frame",
    "frame_3",
    "donuts_frame_15",
    "header_frame",
    "frame_9"
}


def read_wifipoints():
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
    wifi_points = list(sorted(wifi_points, key=lambda item: item['power'],
                              reverse=True))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.scrollArea = QScrollArea(self.ui.list_wifi_frame_19)
        self.ui.scrollArea.setObjectName(u"scrollArea")
        self.ui.scrollArea.setMaximumSize(QSize(16777215, 270))

        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.scrollAreaWidgetContents = QWidget()
        self.ui.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.ui.vbox = QVBoxLayout()
        for i in range(len(wifi_points)): # in range(len(wifi_points))
            exec(f'self.ui.list_wifi_frame{i} = QFrame()')
            exec(f'self.ui.list_wifi_frame{i}.setObjectName(u"list_wifi_frame0")')
            exec(f'self.ui.list_wifi_frame{i}.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)')
            exec(f'self.ui.list_wifi_frame{i}.setMinimumSize(QSize(123456,30))')

            exec(f'self.ui.list_wifi_pushButton{i} = QPushButton(self.ui.list_wifi_frame{i})')
            exec(f'self.ui.list_wifi_pushButton{i}.setObjectName(u"list_wifi_pushButton{i}")')
            exec(f'self.ui.list_wifi_pushButton{i}.setGeometry(QRect(730, 0, 80, 23))')

            exec(f'self.ui.list_wifi_label_{i} = QLabel(self.ui.list_wifi_frame{i})')
            exec(f'self.ui.list_wifi_label_{i}.setObjectName(u"list_wifi_label_{i}")')
            exec(f'self.ui.list_wifi_label_{i}.setGeometry(QRect(20, 10, 261, 16))')

            exec(f'self.ui.list_wifi_pushButton{i}.setText(QCoreApplication.translate("MainWindow", u"Go", None))')
            wifi = f'{wifi_points[i]["name"]} / {wifi_points[i]["MAC"]}'
            exec(f'self.ui.list_wifi_label_{i}.setText(QCoreApplication.translate("MainWindow", wifi, None))')
            #exec(f'self.ui.list_wifi_pushButton{i}.connect(lambda: print("{wifi_points[i]["name"]}"))')
            lmbd = "lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts)"
            exec(f'self.ui.list_wifi_pushButton{i}.clicked.connect({lmbd})')
            exec(f'self.ui.vbox.addWidget(self.ui.list_wifi_frame{i})')
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.vbox)
        self.ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 817, 270))
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)

        self.ui.verticalLayout_14.addWidget(self.ui.scrollArea)


        self.ui.horizontalSlider.setMinimum(2400)
        self.ui.horizontalSlider.setMaximum(5500)
        self.ui.horizontalSlider.setTickPosition(self.ui.horizontalSlider.TicksBelow)
        self.ui.horizontalSlider.setTickInterval(20)
        self.ui.horizontalSlider.valueChanged.connect(lambda: print(self.ui.horizontalSlider.value()))

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon(":/icons/icons/pie-chart.svg"))
        self.setWindowTitle("QT CHARTS")

        QSizeGrip(self.ui.size_grip)

        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow

        self.show()
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)

        self.ui.tools_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.read_wifipoints))
        self.ui.topology_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.nested_donut_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.wifi_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi))
        self.ui.list_wifi_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi))
        self.ui.list_wifi_pushButton0.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wifi_page))
        self.create_list_wifi()
        self.create_nested_donuts()
        self.create_wifi_page()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

    def slideLeftMenu(self):
        width = self.ui.left_menu_frame.width()

        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-center.svg"))

        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"maximumWidth")
        self.animation.setDuration(550)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

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
        self.ui.donuts_frame_7.setStyleSheet(u"background-color: transparent")

        self.min_size = 0.1
        self.max_size = 0.9
        self.donut_count = 5

        self.setup_donuts()
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(5000)

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

                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))
                donut.append(slc)
                size = (self.max_size - self.min_size)/self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)

    def update_rotation(self):
        read_wifipoints()
        for donut in self.donuts:
            phase_shift = randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def explode_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()
            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()
            donut = slc.series()
            idx = self.donuts.index(donut)
            for i in range(idx + 1, len(self.donuts)):
                self.donuts[i].setPieStartAngle(slice_endangle)
                self.donuts[i].setPieEndAngle(360 + slice_startangle)
            slc.doubleClicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi))

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
        for i in range(10):
            pwr = 100 + wifi_points[i]["power"]
            low.append(pwr)
            if pwr > 100:
                low.append(pwr - 100)
            print(100 + wifi_points[i]["power"], wifi_points[i]["name"])
            wifi_name_mac = f'{wifi_points[i]["name"]} / {wifi_points[i]["MAC"]}'
            categories.append(wifi_name_mac)

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
        self.ui.list_wifi_frame2.setStyleSheet(u"background-color: transparent")

    def create_wifi_page(self):
        global wifi_points
        categories = []
        low = QtCharts.QBarSet("Power")
        for i in range(15):
            pwr = 100 + wifi_points[i]["power"]
            low.append(pwr)
            if pwr > 100:
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

        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        x = [1,2,3,4,5,6]
        bargraph = pg.BarGraphItem(x = x, height = y1, width = 1, brush ='g')


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
        strng = "Wi-Fi\ndata"
        self.ui.wifi_page_label_text.setText(strng)
        self.ui.wifi_page_graph_cont.addWidget(chart_view, 0, 0, 9, 9)
        #self.ui.Graph_Box.setStyleSheet(u"background-color: transparent")

wifi_points = []

if __name__ == "__main__":
    read_wifipoints()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

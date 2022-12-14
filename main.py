#!/usr/bin/python3

import csv
from pygame import mixer
import time
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPainter, QFontMetricsF, QPen, QColor, QPalette, QFont, QPolygon
from PySide2.QtWidgets import QMainWindow, QWidget, QScrollArea, QVBoxLayout, QApplication, QGraphicsDropShadowEffect, \
    QSizeGrip, QSizePolicy, QFrame, QPushButton, QLabel, QSpinBox
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPropertyAnimation, QSize, QTimer, Qt, Signal, QRect, QCoreApplication, QPoint
import pyqtgraph as pg
from random import randrange
from functools import partial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from PyQt5.QtCore import pyqtSlot as pyqtSlot, pyqtProperty as pyqtProperty, pyqtSignal, QThread
from os import remove
from ui_interface import Ui_MainWindow
import threading
import subprocess
import math
import haversine as hs
from haversine import Unit

shadow_elements = {
    "left_menu_frame",
    "frame_3",
    "donuts_frame_15",
    "header_frame",
    "frame_9"
}
current_wifi = {}


def read_wifipoints():
    global wifi_points
    wifi_points = []  # temp
    with open('data-01.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        next(csv_reader)
        for wifi in csv_reader:
            if not wifi:
                break
            name = wifi[13].strip()
            if name == '':
                name = '#hidden#'
            pwr = 100 + int(wifi[8].strip())
            wifi_points.append({'name': name,
                                'MAC': wifi[0],
                                'first_time': wifi[1].strip(),
                                'last_time': wifi[2].strip(),
                                'channel': wifi[3].strip(),
                                'speed': wifi[4].strip(),
                                'privacy': wifi[5].strip(),
                                'cipher': wifi[6].strip(),
                                'auth': wifi[7].strip(),
                                'power': pwr
                                })
    wifi_points = list(sorted(wifi_points, key=lambda item: item['power'],
                              reverse=True))


def single_scan(mac, channel):
    global single_proc
    clean()
    single_proc = subprocess.Popen(['airodump-ng',
                                    '-w', 'single',
                                    '--gpsd',
                                    '--output-format', 'csv',
                                    '--background', '1',
                                    '-I', '1',
                                    '--bssid', mac,
                                    '-c', channel,
                                    SINGLEINTERFACE])
    time.sleep(2)
    track()


def general_scan():
    global general_proc
    clean()
    general_proc = subprocess.Popen(['airodump-ng',
                             '-w', 'data',
                             '--output-format', 'csv',
                             '--background', '1',
                             '-b', 'abg',
                             '-I', '1',
                             GENINTERFACE])
    time.sleep(300)

def show_kismet():
    with open('single-01.kismet.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for wifi in reader:
            kismet = {'name': wifi[2],
                      'MAC': wifi[3],
                      'channel': wifi[5],
                      'GPSMinLat': wifi[24],
                      'GPSMinLon': wifi[25],
                      'GPSMinAlt': wifi[26],
                      'GPSMinSpd': wifi[27],
                      'GPSMaxLat': wifi[28],
                      'GPSMaxLon': wifi[29],
                      'GPSMaxAlt': wifi[30],
                      'GPSMaxSpd': wifi[31],
                      'GPSBestLat': wifi[32],
                      'GPSBestLon': wifi[33],
                      'GPSBestAlt': wifi[34]
                      }
    self.compass = CompassWidget()
    position = self.compDegree([kismet[8],kismet[9]], [38.89, -77.032])
    self.compass.setAngle(position[0])

def clean():
    try:
        remove('data-01.csv')
    except FileNotFoundError:
        pass
    try:
        remove('single-01.csv')
    except FileNotFoundError:
        pass
    try:
        remove('single-01.kismet.csv')
    except FileNotFoundError:
        pass
    try:
        remove('single-01.gps')
    except FileNotFoundError:
        pass


def beep():
    mixer.init()
    sound = mixer.Sound("sound.wav")
    sound.play()


def show_data():
    with open('single-01.csv', 'r') as csv_file:
        try:
            reader = csv.reader(csv_file)
            next(reader)
            next(reader)
            return abs(int(next(reader)[8].strip()))
        except (StopIteration, IndexError):
            return 50


def show_data_clients():
    global clients
    # time.sleep(4)
    with open('single-01.csv', 'r') as file:
        clients = []
        reader = csv.reader(file)
        for _ in range(5):
            next(reader)
        for client in reader:
            if client == []:
                break
            clients.append((client[0], client[3], client[5]))


def track():
    global is_scanning
    MAX_TIME = 2.85
    MIN_TIME = 0.15
    MAX_POWER = 60
    MIN_POWER = 1

    last_pw = show_data()
    delay = ((last_pw - MIN_POWER)/(MAX_POWER-MIN_POWER))*(MAX_TIME-MIN_TIME) + MIN_TIME

    while True:
        if not is_scanning:
            break
        beep()
        time.sleep(delay)
        current_pw = show_data()
        delay = delay + ((current_pw - last_pw) * (MAX_TIME-MIN_TIME)) / (MAX_POWER-MIN_POWER)
        if delay < MIN_TIME or current_pw < MIN_POWER:
            current_pw = MIN_POWER
            delay = MIN_TIME
        if delay > MAX_TIME or current_pw > MAX_POWER:
            current_pw = MAX_POWER
            delay = MAX_TIME
        last_pw = current_pw


def link_buttons(obj, wifi):
    global current_wifi
    current_wifi = wifi
    string = 'WiFi name: ' + str(wifi['name']) + '\n' + \
             'MAC address: ' + str(wifi['MAC']) + '\n' + \
             'Channel: ' + str(wifi['channel']) + '\n' + \
             'Power: ' + str(wifi['power']) + '\n' + \
             'Privacy: ' + str(wifi['privacy']) + '\n'

    obj.wifi_page_label_text.setText(string)
    obj.stackedWidget.setCurrentWidget(obj.wifi_page)


def toogle_button(obj):
    global current_wifi, single_proc, is_scanning
    if obj.ui.checker:
        obj.timer = QtCore.QTimer()
        obj.timer.start(600)
        obj.ui.pushButton.setText("Stop")
        obj.timer.timeout.connect(obj.update_plot_data)
        obj.ui.checker = False
        is_scanning = True
        thr = threading.Thread(target=single_scan, args=(current_wifi['MAC'], current_wifi['channel']))
        thr.start()
        show_kismet()
    else:
        obj.timer = None
        obj.ui.pushButton.setText("Start")
        obj.ui.checker = True
        obj.clear_plot_data()
        is_scanning = False
        single_proc.kill()


def list_wifi_btn_clicked(obj):
    global current_wifi, is_scanning
    obj.ui.stackedWidget.setCurrentWidget(obj.ui.list_wifi)
    current_wifi = {}
    obj.clear_plot_data()
    if not obj.ui.checker:
        single_proc.kill()
        is_scanning = False
    #obj.timer.stop()
    obj.ui.checker = True
    obj.ui.pushButton.setText("Start")


def close_app(obj):
    global is_scanning
    if not obj.ui.checker:
        single_proc.kill()
        is_scanning = False
    obj.close()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.donut_count = None
        self.clickPosition = None
        self.animation = None
        self.donuts = None
        self.chart_view = None
        self.chart = None
        self.min_size = None
        self.max_size = None
        self.update_timer = None

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

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
        self.ui.close_window_button.clicked.connect(lambda: close_app(self))
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

        self.ui.scrollArea = QScrollArea(self.ui.list_wifi_frame_19)
        self.ui.scrollArea.setObjectName(u"scrollArea")
        self.ui.scrollArea.setMaximumSize(QSize(126700123, 500))

        self.ui.checker = True

        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.scrollAreaWidgetContents = QWidget()
        self.ui.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.ui.vbox = QVBoxLayout()

        self.ui.scrollAreaWidgetContents.setLayout(self.ui.vbox)
        self.ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 12345, 500))
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
        self.ui.gridLayout_7.addWidget(self.ui.scrollArea)


        self.customazingListWifi(wifi_points)
        self.ui.nested_donut_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.pushButton.clicked.connect(lambda: toogle_button(self))
        self.ui.pushButton_2.clicked.connect(lambda: self.create_topology())
        self.ui.list_wifi_btn.clicked.connect(lambda: list_wifi_btn_clicked(self))
        self.ui.pushButton_5.clicked.connect(partial(self.filterListWifi, [str(i) for i in range(1, 15)]))
        self.ui.pushButton_6.clicked.connect(partial(self.filterListWifi, [str(i) for i in range(36, 166)]))
        self.ui.pushButton_7.clicked.connect(self.btnFunc)
        self.ui.pushButton_4.clicked.connect(self.skipScan)

        self.create_list_wifi(wifi_points)
        self.create_nested_donuts()
        self.create_wifi_page()
        self.tools()


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

    def create_topology(obj):
        obj.ui.topology.checker = False
        # thr = threading.Thread(target=single_scan, args=(current_wifi['MAC'], current_wifi['channel']))
        # thr.start()
        show_data_clients()
        obj.topology()
        obj.ui.stackedWidget.setCurrentWidget(obj.ui.topology)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def skipScan(self):
        global general_proc
        self.thread.stop()
        general_proc.kill()
        read_wifipoints()
        self.loadFunc(wifi_points)
        self.create_list_wifi(wifi_points)
        self.create_nested_donuts()
        self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi)

    def filterListWifi(self, channels):
        filteredWFPoints = []
        if channels == "all":
            read_wifipoints()
            filteredWFPoints = wifi_points
        else:
            for i in range(len(wifi_points)):
                if wifi_points[i]['channel'] in channels:
                    filteredWFPoints.append(wifi_points[i])
        self.delCustomListWifi()
        self.customazingListWifi(filteredWFPoints)

    def customazingListWifi(self, wifiPoints):
        global btnKey
        global index
        index = -1
        self.ui.wifi_list = {}
        for i in range(len(wifiPoints)):
            key = 'list_wifi_frame' + str(i)

            self.ui.wifi_list[key] = QFrame()
            self.ui.wifi_list[key].setObjectName(key)
            self.ui.wifi_list[key].setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ui.wifi_list[key].setMinimumSize(QSize(167800, 40))
            self.ui.frame_width = self.ui.wifi_list[key].width()
            self.ui.frame_height = self.ui.wifi_list[key].height()

            btnKey = 'list_wifi_pushButton' + str(i)
            index = i
            self.ui.wifi_list[btnKey] = QPushButton(self.ui.wifi_list[key])
            self.ui.wifi_list[btnKey].setObjectName(btnKey)
            self.ui.wifi_list[btnKey].setMinimumSize(self.ui.frame_width, 30)
            self.ui.wifi_list[btnKey].setStyleSheet('text-align: left')

            wifi = str(wifiPoints[i]["name"]) + '\n' + str(wifiPoints[i]["MAC"])

            wifi_info = {'name': wifiPoints[i]['name'],
                         'MAC': wifiPoints[i]['MAC'],
                         'channel': wifiPoints[i]['channel'],
                         'power': wifiPoints[i]['power'],
                         'privacy': wifiPoints[i]['privacy']
                         }

            self.ui.wifi_list[btnKey].setText(wifi)
            self.ui.wifi_list[btnKey].clicked.connect(partial(link_buttons, self.ui, wifi_info))
            self.ui.vbox.addWidget(self.ui.wifi_list[key])
        global btnKeyIndex
        btnKeyIndex = index + 1
        self.create_list_wifi(wifiPoints)

    def loadFunc(self, wifi_points):
        self.delCustomListWifi()
        self.customazingListWifi(wifi_points)

    def delCustomListWifi(self):
        for i in reversed(range(btnKeyIndex)):
            delBut = "list_wifi_pushButton" + str(i)
            delFr = "list_wifi_frame" + str(i)
            self.ui.wifi_list[delBut].deleteLater()
            self.ui.wifi_list[delFr].deleteLater()

    def create_nested_donuts(self):
        self.setMinimumSize(800, 600)
        self.donuts = []
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()
        self.chart.legend().setVisible(False)
        self.chart.setTitle("Nested donuts")
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
        lng = len(wifi_points)
        if lng >= 5:
            self.donut_count = 5
        else:
            self.donut_count = lng

        self.setup_donuts()
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(5000)

    def setup_donuts(self):
        counter = 0
        for i in range(self.donut_count):
            donut = QtCharts.QPieSeries()
            slccount = 1
            if self.donut_count >= 5:
                if len(wifi_points) / 5 >= 1:
                    slccount = int(len(wifi_points) / 5)
            for j in range(slccount):
                value = wifi_points[counter]['name'][:3] + '...'

                slc = QtCharts.QPieSlice(str(value), counter)
                slc.setLabelVisible(True)
                slc.setLabelColor(Qt.white)
                slc.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)

                if slc.hovered[bool] is False:
                    newslc = QtCharts.QPieSlice(str(wifi_points[counter]['name']), counter)
                    newslc.setLabelVisible(True)
                    newslc.setLabelColor(Qt.white)
                    newslc.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)
                    slc.hovered[bool].connect(partial(self.explode_slice, slc=newslc))
                else:
                    slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))
                donut.append(slc)
                size = (self.max_size - self.min_size) / self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)
                counter += 1

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)

    def update_rotation(self):
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
            print(slc.label(), slc.value())
            valInt = int(slc.value())
            wifi_info = {'name': wifi_points[valInt]['name'],
                         'MAC': wifi_points[valInt]['MAC'],
                         'channel': wifi_points[valInt]['channel'],
                         'power': wifi_points[valInt]['power'],
                         'privacy': wifi_points[valInt]['privacy']
                         }
            slc.doubleClicked.connect(partial(link_buttons, self.ui, wifi_info))

        else:
            for donut in self.donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)

            self.update_timer.start()

        slc.setExploded(exploded)

    def create_list_wifi(self, wifiPoints):
        global optimum_length
        categories = []
        low = QtCharts.QBarSet("Power")
        if len(wifiPoints) > 10:
            optimum_length = 10
        elif len(wifiPoints) == 0:
            optimum_length = 0
        else:
            optimum_length = len(wifiPoints)
        for i in range(optimum_length):
            pwr = wifiPoints[i]["power"]
            low.append(pwr)
            wifi_name_mac = f'{wifiPoints[i]["name"]} / {wifiPoints[i]["MAC"]}'
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
        if optimum_length == 0:
            axisY.setRange(0, 0)
        else:
            axisY.setRange(0, 5 + wifiPoints[0]["power"])
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
        # self.ui.list_wifi_frame2.setStyleSheet(u"background-color: transparent")

    def create_wifi_page(self):
        self.chart_view = pg.PlotWidget()
        self.x = list(range(100))  # 100 time points
        self.y = [50 for _ in range(100)]  # 100 data points
        self.chart_view.setBackground('black')

        pen = pg.mkPen(color=(255, 255, 255))
        self.data_line = self.chart_view.plot(self.x, self.y, pen=pen)

        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(600)
        self.chart_view.setMaximumSize(QSize(16777215, 270))
        self.chart_view.setMinimumSize(QSize(16777215, 270))
        self.ui.wifi_page_graph_cont.addWidget(self.chart_view, 0, 0, 9, 9)

        self.compass = CompassWidget()
        #position = self.compDegree([40.76, -73.984], [38.89, -77.032])
        #self.compass.setAngle(position[0])
        #spinBox = QSpinBox()
        #spinBox.setRange(0, 359)
        #spinBox.valueChanged.connect(self.compass.setAngle)
        self.ui.gridLayout_3.addWidget(self.compass)
        #self.ui.gridLayout_3.addWidget(spinBox)

    def update_plot_data(self):
        powerlvl = show_data()
        if powerlvl:
            self.x = self.x[1:]  # Remove the first y element.
            self.y = self.y[1:]  # Remove the first

            self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
            # self.y.append(randint(0, 100))  # Add a new random value.
            self.y.append(100 - show_data())

            self.data_line.setData(self.x, self.y)  # Update the data.
            powerlvl = None

    def clear_plot_data(self):
        self.x.clear()
        self.y.clear()

        self.x = list(range(100))  # 100 time points
        self.y = [50 for _ in range(100)]  # 100 data points

        self.data_line.setData(self.x, self.y)  # Update the data.

    def compDegree(self, loc1, loc2):
        #parsing
        lat1 = math.radians(loc1[0])
        lat2 = math.radians(loc2[0])

        diffLong = math.radians(loc2[1] - loc1[1])

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                                               * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(x, y)

        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        dist = hs.haversine(loc1, loc2, unit=Unit.METERS)

        return compass_bearing, dist

    def topology(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        wifi_point = current_wifi['name']

        G = nx.Graph()
        G.add_node(wifi_point)
        for i in range(len(clients)):
            G.add_node(clients[i][0])
            G.add_edge(wifi_point, clients[i][0])


        nx.draw(G, with_labels=True)
        self.canvas.draw_idle()
        self.ui.temperature_bar_chart_cont.addWidget(self.canvas, 0, 0, 9, 9)

    def btnFunc(self):
        thr = threading.Thread(target=general_scan)
        thr.start()
        self.tools()
        self.ui.stackedWidget.setCurrentWidget(self.ui.tools)
        self.thread = Threadd()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.ui.pushButton_4.setEnabled(False)

    def signal_accept(self, msg):
        global general_proc
        self.ui.progressBar.setValue(int(msg))
        if self.ui.progressBar.value() == 20:
             self.ui.pushButton_4.setEnabled(True)
        elif self.ui.progressBar.value() == 99:
            general_proc.kill()
            self.thread.stop()
            read_wifipoints()
            self.loadFunc(wifi_points)
            self.create_list_wifi(wifi_points)
            self.ui.stackedWidget.setCurrentWidget(self.ui.list_wifi)
    def tools(self):
        self.load_text = QLabel()
        self.load_text.setObjectName(u"load_text")
        self.load_text.setAlignment(Qt.AlignCenter)
        self.load_text.setStyleSheet('font-size: 15px')
        self.load_text.setText(QCoreApplication.translate("MainWindow", u"Load Info\nYou can skip it ", None))
        self.ui.gridLayout_6.addWidget(self.load_text, 0, 0, 9, 9)
        #self.ui.percentage_bar_chart_cont.addWidget(self.ui.load_btn[btnKey], 0, 0, 9, 9)
        #self.ui.tools_frame.setStyleSheet(u"background-color: transparent")

class CompassWidget(QWidget):
    angleChanged = Signal(float)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._angle = 0.0
        self._margins = 10
        self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
                           225: "SW", 270: "W", 315: "NW"}

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        self.drawMarkings(painter)
        self.drawNeedle(painter)
        painter.end()

    def drawMarkings(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        scale = min((self.width() - self._margins) / 120.0,
                    (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)
        font = QFont(self.font())
        font.setPixelSize(10)
        metrics = QFontMetricsF(font)
        painter.setFont(font)
        painter.setPen(self.palette().color(QPalette.Highlight))
        i = 0
        while i < 360:
            if i % 45 == 0:
                painter.drawLine(0, -40, 0, -50)
                painter.drawText(-metrics.width(self._pointText[i]) / 2.0, -52,
                                 self._pointText[i])
            else:
                painter.drawLine(0, -45, 0, -50)
            painter.rotate(15)
            i += 15
        painter.restore()

    def drawNeedle(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self._angle)
        scale = min((self.width() - self._margins) / 120.0,
                    (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(self.palette().brush(QPalette.Shadow))
        painter.drawPolygon(
            QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0),
                      QPoint(0, 45), QPoint(-10, 0)])
        )
        painter.setBrush(self.palette().brush(QPalette.Highlight))
        painter.drawPolygon(
            QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25),
                      QPoint(0, -30), QPoint(-5, -25)])
        )
        painter.restore()

    def sizeHint(self):
        return QSize(150, 150)

    def angle(self):
        return self._angle

    @pyqtSlot(float)
    def setAngle(self, angle):
        if angle != self._angle:
            self._angle = angle
            self.angleChanged.emit(angle)
            self.update()

    angle = pyqtProperty(float, angle, setAngle)

class Threadd(QThread):
    _signal = pyqtSignal(int)
    def __init__(self):
        super(Threadd, self).__init__()
        self.running = True
        self.count = 0

#    def __del__(self):
#        self.wait()

    def run(self):
        while self.running and self.count < 100:
            time.sleep(3)
            self.count += 1
            self._signal.emit(self.count)

    def stop(self):
        self.running = False

wifi_points = []
single_proc = None
general_proc = None
current_wifi = None
optimum_length = None
is_scanning = None
clients = None
skipped = False
SINGLEINTERFACE = 'wlan0mon'
GENINTERFACE = 'wlan0mon'
#GENINTERFACE = 'wlp0s20f3mon'

if __name__ == "__main__":
    #read_wifipoints()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacerYeBma.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 670)
        MainWindow.setMinimumSize(QSize(0, 5))
        MainWindow.setMaximumSize(QSize(16777215, 16777213))
        MainWindow.setStyleSheet(u"*{color: #fff; border: none;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"NovaFlat")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"@font-face {\n"
                                         "    font-family: NovaFlat;\n"
                                         "    src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
                                         "}\n"
                                         "*{\n"
                                         "color: #fff;\n"
                                         "font-family: NovaFlat;\n"
                                         "font-size: 12px;\n"
                                         "border: nine;\n"
                                         "}\n"
                                         "#centralwidget{\n"
                                         "background-color: rgb(33, 43, 51);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame = QFrame(self.centralwidget)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(0, 0))
        self.left_menu_frame.setMaximumSize(QSize(200, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgba(61, 80, 95, 100)")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(61, 80, 95);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.icon = QLabel(self.frame_3)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(30, 30))
        self.icon.setMaximumSize(QSize(30, 30))
        self.icon.setPixmap(QPixmap(u":/icons/icons/pie-chart.svg"))
        self.icon.setScaledContents(True)
        self.icon.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.icon)

        self.text = QLabel(self.frame_3)
        self.text.setObjectName(u"text")
        font1 = QFont()
        font1.setFamily(u"NovaFlat")
        font1.setBold(True)
        font1.setWeight(75)
        self.text.setFont(font1)
        self.text.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.text)

        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"QFrame{background: none;}\n"
                                   "QPushButton{\n"
                                   "padding: 10px;\n"
                                   "border-radius: 5px;\n"
                                   "}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.nested_donut_btn = QPushButton(self.frame_12)
        self.nested_donut_btn.setObjectName(u"nested_donut_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nested_donut_btn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.nested_donut_btn)

        self.list_wifi_btn = QPushButton(self.frame_12)
        self.list_wifi_btn.setObjectName(u"list_wifi_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.list_wifi_btn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.list_wifi_btn)

        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.left_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{background: none;}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.horizontalLayout.addWidget(self.left_menu_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.header_frame = QFrame(self.main_body_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 32))
        self.header_frame.setMaximumSize(QSize(16777215, 16777215))
        self.header_frame.setStyleSheet(u"QFrame{background-color: rgb(61, 80, 95);}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.open_close_side_bar_btn = QPushButton(self.header_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/align-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon6)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)

        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.horizontalLayout_4.addWidget(self.frame_10, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QPushButton{\n"
                                    "	background-color: rgb(61, 80, 95);\n"
                                    "	border-radius: 15px;\n"
                                    "	border: 3px solid rgb(120, 157, 186);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "	background-color: rgb(120, 157, 186);\n"
                                    "}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.minimize_window_button = QPushButton(self.frame_11)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_11)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(30, 30))
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_11)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(30, 30))
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.close_window_button)

        self.horizontalLayout_4.addWidget(self.frame_11, 0, Qt.AlignRight | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.main_body_frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(61, 80, 95, 100)")
        self.tools = QWidget()
        self.tools.setObjectName(u"tools")
        self.verticalLayout_6 = QVBoxLayout(self.tools)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.tools_frame = QFrame(self.tools)
        self.tools_frame.setObjectName(u"tools_frame")
        sizePolicy.setHeightForWidth(self.tools_frame.sizePolicy().hasHeightForWidth())
        self.tools_frame.setSizePolicy(sizePolicy)
        #self.tools_frame.setMinimumSize(QSize(0, 300))
        self.tools_frame.setMaximumSize(QSize(126700, 1000))
        self.tools_frame.setStyleSheet(u"QFrame{background-color: none;}")
        self.tools_frame.setFrameShape(QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QFrame.Raised)
        self.percentage_bar_chart_cont = QGridLayout(self.tools_frame)
        self.percentage_bar_chart_cont.setObjectName(u"percentage_bar_chart_cont")
        self.percentage_bar_chart_cont.setAlignment(Qt.AlignTop)
        self.pushButton_4 = QPushButton(self.tools_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.percentage_bar_chart_cont.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.widget = QWidget(self.tools_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(123450, 500))
        #self.widget.setAlignment(Qt.AlignTop)
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setAlignment(Qt.AlignTop)

        self.percentage_bar_chart_cont.addWidget(self.widget, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.tools_frame)
        self.progressBar.setObjectName(u"progressBar")

        self.percentage_bar_chart_cont.addWidget(self.progressBar, 1, 0, 1, 1)

        self.verticalLayout_6.addWidget(self.tools_frame)

        self.stackedWidget.addWidget(self.tools)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.verticalLayout_11 = QVBoxLayout(self.nested_donuts)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.donuts_frame_15 = QFrame(self.nested_donuts)
        self.donuts_frame_15.setObjectName(u"donuts_frame_15")
        self.donuts_frame_15.setFrameShape(QFrame.StyledPanel)
        self.donuts_frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.donuts_frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.donuts_label_15 = QLabel(self.donuts_frame_15)
        self.donuts_label_15.setObjectName(u"donuts_label_15")
        self.donuts_label_15.setFont(font1)
        self.donuts_label_15.setStyleSheet(u"background-color: none;")
        self.donuts_label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.donuts_label_15)

        self.verticalLayout_11.addWidget(self.donuts_frame_15)

        self.donuts_frame_7 = QFrame(self.nested_donuts)
        self.donuts_frame_7.setObjectName(u"donuts_frame_7")
        sizePolicy.setHeightForWidth(self.donuts_frame_7.sizePolicy().hasHeightForWidth())
        self.donuts_frame_7.setSizePolicy(sizePolicy)
        self.donuts_frame_7.setMinimumSize(QSize(0, 300))
        self.donuts_frame_7.setStyleSheet(u"QFrame{background-color: none;}")
        self.donuts_frame_7.setFrameShape(QFrame.StyledPanel)
        self.donuts_frame_7.setFrameShadow(QFrame.Raised)
        self.nested_donut_chart_cont = QGridLayout(self.donuts_frame_7)
        self.nested_donut_chart_cont.setObjectName(u"nested_donut_chart_cont")

        self.verticalLayout_11.addWidget(self.donuts_frame_7)

        self.stackedWidget.addWidget(self.nested_donuts)
        self.wifi_page = QWidget()
        self.wifi_page.setObjectName(u"wifi_page")
        self.gridLayout_2 = QGridLayout(self.wifi_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.wifi_page)
        self.groupBox.setObjectName(u"groupBox")
        self.wifi_page_graph_cont = QGridLayout(self.groupBox)
        self.wifi_page_graph_cont.setObjectName(u"wifi_page_graph_cont")

        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.wifi_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.wifi_page_info_cont = QGridLayout(self.groupBox_2)
        self.wifi_page_info_cont.setObjectName(u"wifi_page_info_cont")
        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setAlignment(Qt.AlignTop)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet('background-color: #FF5722; border-radius: 15px; '
                                      'font-size: 20px; padding: 20')

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_3")
        self.pushButton_2.setStyleSheet('background-color: #FF5722; border-radius: 15px; '
                                        'font-size: 15px; padding: 22 10')

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.wifi_page_label_text = QLabel(self.frame_2)
        self.wifi_page_label_text.setObjectName(u"wifi_page_label_text")
        self.wifi_page_label_text.setAlignment(Qt.AlignLeft)
        self.wifi_page_label_text.setStyleSheet('font-size: 15px; background-color: transparent')
        self.gridLayout_4.addWidget(self.wifi_page_label_text, 0, 0, 1, 1)

        self.wifi_page_info_cont.addWidget(self.frame_2, 0, 0, 1, 1)
        #        self.wifi_page_info_cont.setMaximumSize(QSize(16777215, 16777215))

        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.wifi_page_info_cont.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.wifi_page)
        self.list_wifi = QWidget()
        self.list_wifi.setObjectName(u"list_wifi")
        self.verticalLayout_15 = QVBoxLayout(self.list_wifi)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.list_wifi_frame_19 = QFrame(self.list_wifi)
        self.list_wifi_frame_19.setObjectName(u"list_wifi_frame_19")
        self.list_wifi_frame_19.setFrameShape(QFrame.StyledPanel)
        self.list_wifi_frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.list_wifi_frame_19)
        self.gridLayout_5.setObjectName(u"verticalLayout_14")
        self.list_wifi_frame_18 = QFrame(self.list_wifi_frame_19)
        self.list_wifi_frame_18.setObjectName(u"list_wifi_frame_18")
        self.list_wifi_frame_18.setEnabled(True)
        self.list_wifi_frame_18.setMinimumSize(QSize(0, 10))
        self.list_wifi_frame_18.setMaximumSize(QSize(16777215, 700))
        self.list_wifi_frame_18.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.list_wifi_frame_18.setStyleSheet(u"QFrame{background-color: transparent;}")
        self.list_wifi_frame_18.setFrameShape(QFrame.StyledPanel)
        self.list_wifi_frame_18.setFrameShadow(QFrame.Raised)
        self.list_wifi_cont = QGridLayout(self.list_wifi_frame_18)
        self.list_wifi_cont.setObjectName(u"list_wifi_cont")
        self.list_wifi_cont.setSizeConstraint(QLayout.SetNoConstraint)

        self.gridLayout_5.addWidget(self.list_wifi_frame_18, 0, 0, 1, 3)

        self.pushButton_5 = QPushButton(self.list_wifi_frame_19)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.list_wifi_frame_19)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_5.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.list_wifi_frame_19)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_5.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.frame_5 = QFrame(self.list_wifi_frame_19)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setMaximumSize(QSize(16777215, 270))
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.gridLayout_5.addWidget(self.frame_5, 2, 0, 1, 3)

        self.verticalLayout_15.addWidget(self.list_wifi_frame_19)

        self.stackedWidget.addWidget(self.list_wifi)
        self.topology = QWidget()
        self.topology.setObjectName(u"topology")
        self.verticalLayout_9 = QVBoxLayout(self.topology)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.topology_frame_2 = QFrame(self.topology)
        self.topology_frame_2.setObjectName(u"topology_frame_2")
        sizePolicy.setHeightForWidth(self.topology_frame_2.sizePolicy().hasHeightForWidth())
        self.topology_frame_2.setSizePolicy(sizePolicy)
        self.topology_frame_2.setMinimumSize(QSize(0, 300))
        self.topology_frame_2.setStyleSheet(u"QFrame{background-color: none;}")
        self.topology_frame_2.setFrameShape(QFrame.StyledPanel)
        self.topology_frame_2.setFrameShadow(QFrame.Raised)
        self.temperature_bar_chart_cont = QGridLayout(self.topology_frame_2)
        self.temperature_bar_chart_cont.setObjectName(u"temperature_bar_chart_cont")

        self.verticalLayout_9.addWidget(self.topology_frame_2)

        self.stackedWidget.addWidget(self.topology)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.main_body_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.size_grip = QPushButton(self.frame_9)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))

        self.horizontalLayout_7.addWidget(self.size_grip)

        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignBottom)

        self.horizontalLayout.addWidget(self.main_body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.text.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi Hunter", None))
        self.nested_donut_btn.setText(QCoreApplication.translate("MainWindow", u"Donuts with Wi-Fi", None))
        self.list_wifi_btn.setText(QCoreApplication.translate("MainWindow", u"List Wi-Fi", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.donuts_label_15.setText(QCoreApplication.translate("MainWindow", u"Donuts", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
        self.wifi_page_label_text.setText(QCoreApplication.translate("MainWindow", u"No Info", None))
        self.size_grip.setText("")
        self.pushButton.setText("Start")
        self.pushButton_4.setText("Skip")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"2.4ГГц", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"5.0ГГц", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Topology", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainScreenStacked.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMdiArea, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1527, 829)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1521, 801))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setStyleSheet(u"font: 16pt \"Sitka\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.start_pushButton = QPushButton(self.page)
        self.start_pushButton.setObjectName(u"start_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.start_pushButton, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1499, 725))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_file_fields_pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.add_file_fields_pushButton.setObjectName(u"add_file_fields_pushButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_file_fields_pushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.add_file_fields_pushButton)

        self.delete_file_fields_pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.delete_file_fields_pushButton.setObjectName(u"delete_file_fields_pushButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_file_fields_pushButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.delete_file_fields_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.continue_to_data_vis_pushButton = QPushButton(self.page_2)
        self.continue_to_data_vis_pushButton.setObjectName(u"continue_to_data_vis_pushButton")

        self.verticalLayout.addWidget(self.continue_to_data_vis_pushButton)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget = QTreeWidget(self.page_3)
        self.treeWidget.headerItem().setText(0, "")
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(400, 0))
        self.treeWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        self.gridLayout_2.addWidget(self.treeWidget, 2, 1, 4, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_graph_title = QLineEdit(self.page_3)
        self.lineEdit_graph_title.setObjectName(u"lineEdit_graph_title")

        self.verticalLayout_7.addWidget(self.lineEdit_graph_title)

        self.lineEdit_x_axis_title = QLineEdit(self.page_3)
        self.lineEdit_x_axis_title.setObjectName(u"lineEdit_x_axis_title")

        self.verticalLayout_7.addWidget(self.lineEdit_x_axis_title)

        self.lineEdit_y_axis_title = QLineEdit(self.page_3)
        self.lineEdit_y_axis_title.setObjectName(u"lineEdit_y_axis_title")

        self.verticalLayout_7.addWidget(self.lineEdit_y_axis_title)

        self.pushButton_download_graphs = QPushButton(self.page_3)
        self.pushButton_download_graphs.setObjectName(u"pushButton_download_graphs")

        self.verticalLayout_7.addWidget(self.pushButton_download_graphs)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 6, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_values_2 = QLabel(self.page_3)
        self.label_values_2.setObjectName(u"label_values_2")
        self.label_values_2.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_9.addWidget(self.label_values_2)

        self.listWidget_values_file_id = QListWidget(self.page_3)
        self.listWidget_values_file_id.setObjectName(u"listWidget_values_file_id")
        self.listWidget_values_file_id.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values_file_id.setMouseTracking(True)
        self.listWidget_values_file_id.setAcceptDrops(True)
        self.listWidget_values_file_id.setDragEnabled(True)
        self.listWidget_values_file_id.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values_file_id.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_9.addWidget(self.listWidget_values_file_id)

        self.label_values_3 = QLabel(self.page_3)
        self.label_values_3.setObjectName(u"label_values_3")
        self.label_values_3.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_9.addWidget(self.label_values_3)

        self.listWidget_values_file_id_2 = QListWidget(self.page_3)
        self.listWidget_values_file_id_2.setObjectName(u"listWidget_values_file_id_2")
        self.listWidget_values_file_id_2.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values_file_id_2.setMouseTracking(True)
        self.listWidget_values_file_id_2.setAcceptDrops(True)
        self.listWidget_values_file_id_2.setDragEnabled(True)
        self.listWidget_values_file_id_2.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values_file_id_2.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_9.addWidget(self.listWidget_values_file_id_2)

        self.label_values_4 = QLabel(self.page_3)
        self.label_values_4.setObjectName(u"label_values_4")
        self.label_values_4.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_9.addWidget(self.label_values_4)

        self.listWidget_values_file_id_3 = QListWidget(self.page_3)
        self.listWidget_values_file_id_3.setObjectName(u"listWidget_values_file_id_3")
        self.listWidget_values_file_id_3.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values_file_id_3.setMouseTracking(True)
        self.listWidget_values_file_id_3.setAcceptDrops(True)
        self.listWidget_values_file_id_3.setDragEnabled(True)
        self.listWidget_values_file_id_3.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values_file_id_3.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_9.addWidget(self.listWidget_values_file_id_3)

        self.label_values_5 = QLabel(self.page_3)
        self.label_values_5.setObjectName(u"label_values_5")
        self.label_values_5.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_9.addWidget(self.label_values_5)

        self.listWidget_values_file_id_5 = QListWidget(self.page_3)
        self.listWidget_values_file_id_5.setObjectName(u"listWidget_values_file_id_5")
        self.listWidget_values_file_id_5.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values_file_id_5.setMouseTracking(True)
        self.listWidget_values_file_id_5.setAcceptDrops(True)
        self.listWidget_values_file_id_5.setDragEnabled(True)
        self.listWidget_values_file_id_5.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values_file_id_5.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_9.addWidget(self.listWidget_values_file_id_5)

        self.label_labels_2 = QLabel(self.page_3)
        self.label_labels_2.setObjectName(u"label_labels_2")
        self.label_labels_2.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_9.addWidget(self.label_labels_2)

        self.listWidget_labels_file_id = QListWidget(self.page_3)
        self.listWidget_labels_file_id.setObjectName(u"listWidget_labels_file_id")
        self.listWidget_labels_file_id.setMaximumSize(QSize(16777215, 25))
        self.listWidget_labels_file_id.setMouseTracking(True)
        self.listWidget_labels_file_id.setDragEnabled(True)
        self.listWidget_labels_file_id.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_labels_file_id.setBatchSize(1)
        self.listWidget_labels_file_id.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_9.addWidget(self.listWidget_labels_file_id)

        self.pushButton_add_data_field = QPushButton(self.page_3)
        self.pushButton_add_data_field.setObjectName(u"pushButton_add_data_field")
        self.pushButton_add_data_field.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.pushButton_add_data_field)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_graph_color_pushButton = QPushButton(self.page_3)
        self.select_graph_color_pushButton.setObjectName(u"select_graph_color_pushButton")
        self.select_graph_color_pushButton.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_2.addWidget(self.select_graph_color_pushButton)

        self.labels_checkBox_bar = QCheckBox(self.page_3)
        self.labels_checkBox_bar.setObjectName(u"labels_checkBox_bar")
        self.labels_checkBox_bar.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.labels_checkBox_bar)

        self.labels_checkBox_stacked = QCheckBox(self.page_3)
        self.labels_checkBox_stacked.setObjectName(u"labels_checkBox_stacked")
        self.labels_checkBox_stacked.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.labels_checkBox_stacked)

        self.legends_checkBox_stacked = QCheckBox(self.page_3)
        self.legends_checkBox_stacked.setObjectName(u"legends_checkBox_stacked")
        self.legends_checkBox_stacked.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.legends_checkBox_stacked)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.comboBox_chart_type = QComboBox(self.page_3)
        self.comboBox_chart_type.addItem("")
        self.comboBox_chart_type.addItem("")
        self.comboBox_chart_type.addItem("")
        self.comboBox_chart_type.addItem("")
        self.comboBox_chart_type.addItem("")
        self.comboBox_chart_type.setObjectName(u"comboBox_chart_type")

        self.gridLayout_2.addWidget(self.comboBox_chart_type, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_values = QLabel(self.page_3)
        self.label_values.setObjectName(u"label_values")
        self.label_values.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_8.addWidget(self.label_values)

        self.listWidget_values = QListWidget(self.page_3)
        self.listWidget_values.setObjectName(u"listWidget_values")
        self.listWidget_values.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values.setMouseTracking(True)
        self.listWidget_values.setAcceptDrops(True)
        self.listWidget_values.setDragEnabled(True)
        self.listWidget_values.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_8.addWidget(self.listWidget_values)

        self.label_values2 = QLabel(self.page_3)
        self.label_values2.setObjectName(u"label_values2")
        self.label_values2.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_8.addWidget(self.label_values2)

        self.listWidget_values2 = QListWidget(self.page_3)
        self.listWidget_values2.setObjectName(u"listWidget_values2")
        self.listWidget_values2.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values2.setMouseTracking(True)
        self.listWidget_values2.setAcceptDrops(True)
        self.listWidget_values2.setDragEnabled(True)
        self.listWidget_values2.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values2.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_8.addWidget(self.listWidget_values2)

        self.label_values3 = QLabel(self.page_3)
        self.label_values3.setObjectName(u"label_values3")
        self.label_values3.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_8.addWidget(self.label_values3)

        self.listWidget_values3 = QListWidget(self.page_3)
        self.listWidget_values3.setObjectName(u"listWidget_values3")
        self.listWidget_values3.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values3.setMouseTracking(True)
        self.listWidget_values3.setAcceptDrops(True)
        self.listWidget_values3.setDragEnabled(True)
        self.listWidget_values3.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values3.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_8.addWidget(self.listWidget_values3)

        self.label_values4 = QLabel(self.page_3)
        self.label_values4.setObjectName(u"label_values4")
        self.label_values4.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_8.addWidget(self.label_values4)

        self.listWidget_values4 = QListWidget(self.page_3)
        self.listWidget_values4.setObjectName(u"listWidget_values4")
        self.listWidget_values4.setMaximumSize(QSize(16777215, 25))
        self.listWidget_values4.setMouseTracking(True)
        self.listWidget_values4.setAcceptDrops(True)
        self.listWidget_values4.setDragEnabled(True)
        self.listWidget_values4.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_values4.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_8.addWidget(self.listWidget_values4)

        self.label_labels = QLabel(self.page_3)
        self.label_labels.setObjectName(u"label_labels")
        self.label_labels.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_8.addWidget(self.label_labels)

        self.listWidget_labels = QListWidget(self.page_3)
        self.listWidget_labels.setObjectName(u"listWidget_labels")
        self.listWidget_labels.setMaximumSize(QSize(16777215, 25))
        self.listWidget_labels.setMouseTracking(True)
        self.listWidget_labels.setDragEnabled(True)
        self.listWidget_labels.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_labels.setBatchSize(1)
        self.listWidget_labels.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_8.addWidget(self.listWidget_labels)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.mdiArea = QMdiArea(self.page_3)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setMinimumSize(QSize(0, 650))

        self.gridLayout_2.addWidget(self.mdiArea, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.listWidget_duplicate = QListWidget(self.page_3)
        self.listWidget_duplicate.setObjectName(u"listWidget_duplicate")
        self.listWidget_duplicate.setMaximumSize(QSize(16777215, 25))
        self.listWidget_duplicate.setMouseTracking(True)
        self.listWidget_duplicate.setDragEnabled(True)
        self.listWidget_duplicate.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_duplicate.setBatchSize(1)
        self.listWidget_duplicate.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.horizontalLayout_4.addWidget(self.listWidget_duplicate)

        self.vis_data_pushButton = QPushButton(self.page_3)
        self.vis_data_pushButton.setObjectName(u"vis_data_pushButton")

        self.horizontalLayout_4.addWidget(self.vis_data_pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.mdiArea.raise_()
        self.treeWidget.raise_()
        self.comboBox_chart_type.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Report Builder", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Files and Input ID values. To combine values use the same ID", None))
        self.add_file_fields_pushButton.setText(QCoreApplication.translate("MainWindow", u" Add", None))
        self.delete_file_fields_pushButton.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.continue_to_data_vis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Continue to Data Visualization", None))
        self.lineEdit_graph_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Graph Title", None))
        self.lineEdit_x_axis_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X-Axis", None))
        self.lineEdit_y_axis_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y-Axis", None))
        self.pushButton_download_graphs.setText(QCoreApplication.translate("MainWindow", u"Download Duplicated Graphs", None))
        self.label_values_2.setText(QCoreApplication.translate("MainWindow", u"Value 1 File ID", None))
        self.label_values_3.setText(QCoreApplication.translate("MainWindow", u"Value 2 File ID", None))
        self.label_values_4.setText(QCoreApplication.translate("MainWindow", u"Value 3 File ID", None))
        self.label_values_5.setText(QCoreApplication.translate("MainWindow", u"Value 4 File ID", None))
        self.label_labels_2.setText(QCoreApplication.translate("MainWindow", u"Label File ID", None))
        self.pushButton_add_data_field.setText("")
        self.select_graph_color_pushButton.setText(QCoreApplication.translate("MainWindow", u"Select Graph Color", None))
        self.labels_checkBox_bar.setText(QCoreApplication.translate("MainWindow", u"Bar Chart Labels", None))
        self.labels_checkBox_stacked.setText(QCoreApplication.translate("MainWindow", u"Stacked Bar Chart Labels", None))
        self.legends_checkBox_stacked.setText(QCoreApplication.translate("MainWindow", u"Stacked Bar Chart Legend", None))
        self.comboBox_chart_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.comboBox_chart_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.comboBox_chart_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Stacked Bar Chart", None))
        self.comboBox_chart_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.comboBox_chart_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Donut Chart", None))

        self.label_values.setText(QCoreApplication.translate("MainWindow", u"Values 1", None))
        self.label_values2.setText(QCoreApplication.translate("MainWindow", u"Values 2", None))
        self.label_values3.setText(QCoreApplication.translate("MainWindow", u"Values 3", None))
        self.label_values4.setText(QCoreApplication.translate("MainWindow", u"Values 4", None))
        self.label_labels.setText(QCoreApplication.translate("MainWindow", u"Labels", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Duplicate Chart On:", None))
        self.vis_data_pushButton.setText(QCoreApplication.translate("MainWindow", u"Visualize Data", None))
    # retranslateUi


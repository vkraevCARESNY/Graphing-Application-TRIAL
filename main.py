import sys

import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QEventLoop
from PySide6.QtWidgets import QFileDialog

# GUI Imports
from MainScreenStacked import*

# Internal Imports
from add_files_dynamically import*
from init_dataframes import*
from df_operations import*


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Saved variables
        # This gets file paths for the collection of variables
        self.get_file_paths = []
        # This gets my count of files added
        self.file_counter = 0
        # This just stores my dataframes
        self.dataframes = []
            # Chart obj
        self.chart = None
            # Chart name
        self.chart_name = ""
            # x-axis
        self.x_axis_name = ""
            # y-axis
        self.y_axis_name = ""
            # list of value ID's
        self.ID_list = []
            # filtered df
        self.filtered_df = None
            # current values
        self.values =None
            # Current Labels
        self.labels = None
            # Color
        self.color = None
            # Two or more varb
        self.value_list = []
            # Number of input vals
        self.number_of_varb = 0


        super().__init__()
        self.setupUi(self)

        # Hidden vals
        self.select_graph_color_pushButton.hide()
        self.labels_checkBox_bar.hide()
        self.labels_checkBox_stacked.hide()
        self.pushButton_download_graphs.hide()

        self.lineEdit_graph_title.hide()
        self.lineEdit_x_axis_title.hide()
        self.lineEdit_y_axis_title.hide()

        self.listWidget_values_file_id.hide()
        self.listWidget_labels_file_id.hide()

        self.label_values_2.hide()
        self.label_labels_2.hide()

        self.label_values2.hide()
        self.listWidget_values2.hide()

        self.listWidget_values_file_id_2.hide()
        self.label_values_3.hide()

        self.pushButton_add_data_field.hide()

        self.label_values_4.hide()
        self.listWidget_values_file_id_3.hide()
        self.label_values3.hide()
        self.listWidget_values3.hide()

        self.label_values_5.hide()
        self.listWidget_values_file_id_5.hide()
        self.label_values4.hide()
        self.listWidget_values4.hide()

        self.legends_checkBox_stacked.hide()


        # Main Screen Buttons
        self.start_pushButton.clicked.connect(self.start_program)

    # Sends to next page
    def next_page(self, page):
        self.stackedWidget.setCurrentIndex(page+1)

    def start_program(self):
        self.add_file_field_dynamically()

        self.next_page(0)

        self.add_file_fields_pushButton.clicked.connect(self.add_file_field_dynamically)
        self.delete_file_fields_pushButton.clicked.connect(self.delete_file_fields_dynamically)
        self.continue_to_data_vis_pushButton.clicked.connect(self.init_data)

    def delete_file_fields_dynamically(self):
        if self.file_counter > 1:
            vBox_layout = self.findChildren(QVBoxLayout)
            vert_layout = [x for x in vBox_layout if "verticalLayout_3" == x.objectName()]

            vert_children = vert_layout[0].findChildren(QHBoxLayout)

            hbox = [x for x in vert_children if str(self.file_counter) in x.objectName()]

            layout = hbox[0]
            self.clear_layout(layout)

            self.file_counter = self.file_counter - 1

    def clear_layout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())
            layout.deleteLater()
    def add_file_field_dynamically(self):
        self.file_counter += 1

        DynamicFileAddition(self, 1, self.file_counter)

        QPushButton_list = self.stackedWidget.findChildren(QPushButton)
        get_file_buttons = [x for x in QPushButton_list if
                            "File Button" in x.objectName() and str(self.file_counter) in x.objectName()]

        for i in range(len(get_file_buttons)):
            get_file_buttons[i].clicked.connect(self.get_file_dynamically)

        return
    def get_file_dynamically(self):
        file_path = (QFileDialog.getOpenFileNames(self, "Select a CSV File",
                                                  "",
                                                  "Excel CSV Files (*.csv)"))

        QLabel_list = self.stackedWidget.findChildren(QLabel)
        get_file_labels = [x for x in QLabel_list if "File Label" in x.objectName() and str(self.file_counter) in x.objectName()]


        get_file_labels[0].setText(file_path[0][0])

        self.get_file_paths.append(file_path[0][0])
        return
    def init_data(self):
        ID_lineEdit_list = self.stackedWidget.findChildren(QLineEdit)
        get_ID_vals = [x for x in ID_lineEdit_list if
                       "File ID Line Edit" in x.objectName()]
        for i in range(len(get_ID_vals)):
            temp_ID = get_ID_vals[i].text()
            self.ID_list.append(temp_ID)

        self.dataframes = get_dataframes(self.get_file_paths, self.ID_list)

        for i in range(len(self.dataframes)):
           children_to_add = []
           dataframe_col = self.dataframes[i][1].columns.values.tolist()
           tree_item_to_add = QTreeWidgetItem()
           tree_item_to_add.setText(0,self.dataframes[i][0])
           self.treeWidget.addTopLevelItem(tree_item_to_add)
           for j in range(len(dataframe_col)):
               temp_child = QTreeWidgetItem()
               temp_child.setText(0,dataframe_col[j])
               children_to_add.append(temp_child)
           tree_item_to_add.addChildren(children_to_add)

        self.next_page(1)

        # Checking for combination ID
        if len(self.ID_list) > 1 :
            self.listWidget_values_file_id.show()
            self.listWidget_labels_file_id.show()

            self.label_values_2.show()
            self.label_labels_2.show()


        # limits index to one total item
        self.listWidget_labels.itemChanged.connect(self.remove_combo_vals)
        self.listWidget_values.itemChanged.connect(self.remove_combo_vals)
        self.listWidget_duplicate.itemChanged.connect(self.remove_combo_vals)
        self.listWidget_values_file_id.itemChanged.connect(self.remove_combo_vals)
        self.listWidget_labels_file_id.itemChanged.connect(self.remove_combo_vals)

        self.listWidget_values_file_id.itemChanged.connect(self.remove_combo_vals)
        self.listWidget_labels_file_id.itemChanged.connect(self.remove_combo_vals)


        # Setting my variables
        self.lineEdit_graph_title.textChanged.connect(self.set_varb)
        self.lineEdit_x_axis_title.textChanged.connect(self.set_varb)
        self.lineEdit_y_axis_title.textChanged.connect(self.set_varb)

        # Init the data vis button
        self.vis_data_pushButton.clicked.connect(self.vis_data)

        # Buttons
        self.select_graph_color_pushButton.clicked.connect(lambda: self.get_color(self.chart))

        # Checkbox
        self.labels_checkBox_bar.clicked.connect(lambda: self.chart.set_bar_labs(self.chart, self.labels_checkBox_bar.isChecked(), self.values))

        self.labels_checkBox_stacked.clicked.connect(
            lambda: self.chart.set_bar_stacked_labs( self.labels_checkBox_stacked.isChecked(), self.value_list))

        self.comboBox_chart_type.currentIndexChanged.connect(self.set_widgets_for_vis)

        self.pushButton_add_data_field.clicked.connect(self.add_data_field)

        self.legends_checkBox_stacked.clicked.connect(lambda: self.chart.set_bar_stacked_legend(self.legends_checkBox_stacked.isChecked(),self.value_list))

    def set_widgets_for_vis(self):
        curr_val = self.comboBox_chart_type.currentText()
        if curr_val == "Stacked Bar Chart":
            self.listWidget_values2.show()
            self.label_values2.show()

            self.listWidget_values_file_id_2.show()
            self.label_values_3.show()

            self.pushButton_add_data_field.show()

            self.legends_checkBox_stacked.show()
    def add_data_field(self):
        if self.number_of_varb == 0:
            self.label_values_4.show()
            self.listWidget_values_file_id_3.show()
            self.label_values3.show()
            self.listWidget_values3.show()
            self.number_of_varb += 1
        elif self.number_of_varb == 1:
            self.label_values_5.show()
            self.listWidget_values_file_id_5.show()
            self.label_values4.show()
            self.listWidget_values4.show()


    def get_color(self, chart_obj):
        dlg = QtWidgets.QColorDialog(self)
        if self.color:
            dlg.setCurrentColor(QtGui.QColor(self.color))

        if dlg.exec():
            self.set_color(dlg.currentColor().name(), self.select_graph_color_pushButton, chart_obj)

    def set_color(self, color, signal, chart_obj):
        self.chart_col = color
        # This sets the button color
        signal.setStyleSheet("background-color: %s;" % color)

        chart_obj.set_color(color)

    def set_varb(self):
        signal = self.sender()
        value = signal.text()

        if signal.objectName() == "lineEdit_graph_title":
            self.chart_name = value
        if signal.objectName() == "lineEdit_x_axis_title":
            self.x_axis_name = value
        if signal.objectName() == "lineEdit_y_axis_title":
            self.y_axis_name = value
        return
    def vis_data(self):
        # Showing respective TextBoxes
        self.lineEdit_graph_title.show()
        # Then we must clear the layout
        layouts = self.mdiArea.findChildren(QVBoxLayout)

        if len(layouts) > 0:
            self.clear_chart(layouts[0])

        if self.comboBox_chart_type.currentText() == "Bar Chart":

            # Showing axes textbox
            self.lineEdit_x_axis_title.show()
            self.lineEdit_y_axis_title.show()

            # Getting the values
            value_id = self.listWidget_values.item(0).text()
            label_id = self.listWidget_labels.item(0).text()
            dupe_on = self.listWidget_duplicate.item(0).text()
            if dupe_on is not None:
                df_filter_vals = [value_id,label_id,dupe_on]
            else:
                df_filter_vals = [value_id,label_id]

            if len(self.ID_list) == 1:
                curr_df = self.dataframes[0][1]
                self.filtered_df = curr_df[df_filter_vals]

            if len(self.ID_list) != 1:
                df_id_1 = self.listWidget_values_file_id.item(0).text()
                df_id_2 = self.listWidget_labels_file_id.item(0).text()

                key_list = [(df_id_1,value_id),(df_id_2,label_id)]

                self.filtered_df = merge_df(dupe_on, key_list, self.dataframes)



            val_to_use = self.filtered_df[dupe_on].values.tolist()
            display_df = self.filtered_df.loc[self.filtered_df[dupe_on]==val_to_use[1]]
            labels_list = display_df[label_id].values.tolist()

            self.labels = [str(x) for x in labels_list]
            value_list = display_df[value_id].fillna(0).values.tolist()

            self.values = [int(x) for x in value_list]

            self.chart = BarCanvas(self, width=7, height=5, dpi=100, labels=self.labels, values=self.values, title=self.chart_name,
                                       x_lab=self.x_axis_name, y_lab=self.y_axis_name)
            toolbar_bar = NavigationToolbar(self.chart)

            layout = QVBoxLayout()
            layout.addWidget(toolbar_bar)
            layout.addWidget(self.chart)

            self.mdiArea.setLayout(layout)

            self.select_graph_color_pushButton.show()
            self.labels_checkBox_bar.show()
            self.labels_checkBox_stacked.hide()
            self.pushButton_download_graphs.show()
        if self.comboBox_chart_type.currentText() == "Stacked Bar Chart":
            # Showing respective Buttons
            self.select_graph_color_pushButton.show()
            # Showing respective checkbox
            self.labels_checkBox_bar.hide()
            self.labels_checkBox_stacked.show()
            # Showing axes textbox
            self.lineEdit_x_axis_title.show()
            self.lineEdit_y_axis_title.show()

            # Getting the values
            val_id_list = []
            value_id_1 = self.listWidget_values.item(0).text()
            val_id_list.append(value_id_1)
            value_id_2 = self.listWidget_values2.item(0).text()
            val_id_list.append(value_id_2)
            label_id = self.listWidget_labels.item(0).text()
            dupe_on = self.listWidget_duplicate.item(0).text()

            if self.listWidget_values3.item(0) is not None:
                value_id_3 = self.listWidget_values3.item(0).text()
                val_id_list.append(value_id_3)
            if self.listWidget_values4.item(0) is not None:
                value_id_4 = self.listWidget_values4.item(0).text()
                val_id_list.append(value_id_4)

            if dupe_on is not None:
                val_id_list.append(label_id)
            else:
                val_id_list.append(label_id)

            if len(self.ID_list) == 1:
                curr_df = self.dataframes[0][1]
                self.filtered_df = curr_df[val_id_list]

            if len(self.ID_list) != 1:
                df_id_list = []

                df_id_1 = self.listWidget_values_file_id.item(0).text()
                df_id_list.append(df_id_1)
                df_id_2 = self.listWidget_values_file_id_2.item(0).text()
                df_id_list.append(df_id_2)

                if self.listWidget_values3.item(0) is not None:
                    df_id_4 = self.listWidget_values_file_id_3.item(0).text()
                    df_id_list.append(df_id_4)
                if self.listWidget_values4.item(0) is not None:
                    df_id_5 = self.listWidget_values_file_id_5.item(0).text()
                    df_id_list.append(df_id_5)

                df_id_3 = self.listWidget_labels_file_id.item(0).text()
                df_id_list.append(df_id_3)

                key_list = list(zip(df_id_list,val_id_list))

                self.filtered_df = merge_df(dupe_on, key_list, self.dataframes)

            val_to_use = self.filtered_df[dupe_on].values.tolist()
            display_df = self.filtered_df.loc[self.filtered_df[dupe_on] == val_to_use[1]]

            labels_list = display_df[label_id].values.tolist()

            labels = [str(int(x)) for x in labels_list]

            for i in range(len(val_id_list)-1):
                if val_id_list[i] not in [labels,dupe_on]:
                    value_list = display_df[val_id_list[i]].fillna(0).values.tolist()
                    temp_val = [int(x) for x in value_list]
                    self.value_list.append(temp_val)



            self.chart = StackedBarCanvas(self, width=5, height=4, dpi=100, val_list = self.value_list,label=labels,title=self.chart_name,x_lab = self.x_axis_name,y_lab = self.y_axis_name)
            toolbar_bar = NavigationToolbar(self.chart)
            layout = QVBoxLayout()
            layout.addWidget(toolbar_bar)
            layout.addWidget(self.chart)

            self.mdiArea.setLayout(layout)

    def remove_combo_vals(self):
        signal = self.sender()
        if signal.count() > 1:
            signal.takeItem(1)

    def clear_chart(self, layout):
        for i in range(layout.count()):
            child = layout.itemAt(i)
            if child is not None and child.widget() is not None:
                child.widget().deleteLater()

        layout.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    window = MainWindow()
    window.show()
    app.exec()

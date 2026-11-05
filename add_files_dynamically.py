from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QWidget, \
    QTabWidget, QCheckBox, QMdiArea, QTableView
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# Internal
from plot_view import*


class DynamicFileAddition:
    def __init__(self,parent,page_index,file_counter):
        self.parent = parent

        index = str(file_counter)

        grid_layout = self.parent.findChildren(QVBoxLayout)

        file_grid_widget = [x for x in grid_layout if "verticalLayout_3" == x.objectName()]

        self.add_file_layout = QHBoxLayout()
        name = str(index) + " HBoxLayout File Add"
        self.add_file_layout.setObjectName(name)

        # Label
        self.file_label = QLabel()
        self.file_label.setText("No File Selected")
        name = "File Label " + index
        self.file_label.setObjectName(name)
        # Line edit
        self.line_edit_ID = QLineEdit()
        self.line_edit_ID.setPlaceholderText("Enter File ID")
        name = "File ID Line Edit " + index
        self.line_edit_ID.setObjectName(name)
        # Add File Button
        self.add_file_button = QPushButton()
        self.add_file_button.setText("Add File")
        name = "File Button " + index
        self.add_file_button.setObjectName(name)

        # Adding to layout
        self.add_file_layout.addWidget(self.file_label)
        self.add_file_layout.addWidget(self.line_edit_ID)
        self.add_file_layout.addWidget(self.add_file_button)

        # Adding to grid layout
        file_grid_widget[0].addLayout(self.add_file_layout)

        super().__init__()


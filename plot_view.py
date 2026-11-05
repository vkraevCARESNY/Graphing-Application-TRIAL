
import textwrap
from textwrap import wrap

import matplotlib
import numpy as np

from matplotlib import ticker
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches as mpatches

class BarCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100,labels = None, values=None,title=None,x_lab = None,y_lab = None):
        self.labels = labels
        self.values = values

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        self.bars = self.axes.bar(labels, values)
        self.axes.set_xticks(self.axes.get_xticks(),[textwrap.fill(label, 10) for label in labels],font="sitka")
        self.axes.set_xticklabels(labels)

        self.axes.tick_params(axis='x',labelsize=10,labelfontfamily="sitka")

        if title is not None:
            self.axes.set_title(title,font='sitka',fontsize=11)
        if x_lab is not None:
            self.axes.set_xlabel(x_lab,font='sitka',fontsize=11)
        if y_lab is not None:
            self.axes.set_ylabel(y_lab,font='sitka',fontsize=11)

        super().__init__(self.fig)

        # This here allows a dynamic updating of my chart value
        self.draw()
    def set_color(self,color):
        axes_children = self.axes.get_children()

        barlist = [x for x in axes_children if type(x) == matplotlib.patches.Rectangle]

        for i in range(len(barlist)-1):
            barlist[i].set_facecolor(color)

        self.draw()

    def set_bar_labs(self, checked, values):
        if checked == True:
            self.axes.bar_label(self.bars, labels=values, font="Sitka")
        else:
            for child in self.axes.get_children():
                if isinstance(child, matplotlib.text.Annotation):
                    child.remove()
        self.draw()
class PieCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, labels=None, values=None):
        self.labels = labels
        self.values = values

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        self.axes.pie(values,labels=labels)

        super().__init__(self.fig)

        # This here allows a dynamic updating of my chart value
        self.draw()

class StackedBarCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100,val_list = None,label=None,title=None,x_lab = None,y_lab = None):

        self.fig = Figure(figsize=(width, height+50), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.bar_list = []
        default_col = ['#344B6A','#0075A3','#A8D0DB','#D7D7D7']
        print(val_list)


        for i in range(len(val_list)):
            print(i)
            print(val_list[i])
            if i == 0:
                print('ran')
                for j in range(len(val_list[i])):
                    val_list[i][j] = abs(val_list[i + 1][j] - val_list[i][j])
                print(val_list[i])
                self.bar_list.append(self.axes.bar(label, val_list[i], color=default_col[i]))
                bottom_vals = np.array(val_list[i])
            elif i == len(val_list)-1:
                print("elif max ran")
                for j in range(len(val_list[i])):
                    val_list[i][j] = abs(val_list[i-1][j]-val_list[i][j])
                print(val_list[i])
                self.bar_list.append(self.axes.bar(label, val_list[i], color=default_col[i],bottom=bottom_vals))

            elif i > 0 and i < len(val_list)-1:
                print("elif other ran")
                self.bar_list.append(self.axes.bar(label, val_list[i], color=default_col[i], bottom=bottom_vals))
                bottom_vals = abs(bottom_vals+ np.array(val_list[i + 1] ))


        self.axes.set_xticks(self.axes.get_xticks(), [textwrap.fill(label, 10) for label in label], font="sitka")
        self.axes.set_xticklabels(label)

        self.axes.tick_params(axis='x',  labelsize=12, labelfontfamily="sitka")
        self.axes.tick_params(axis='y', labelsize=12, labelfontfamily="sitka")

        if title is not None:
            self.axes.set_title(title, font='sitka', fontsize=11)
        if x_lab is not None:
            self.axes.set_xlabel(x_lab, font='sitka', fontsize=11)
        if y_lab is not None:
            self.axes.set_ylabel(y_lab, font='sitka', fontsize=11)

        super().__init__(self.fig)

        # This here allows a dynamic updating of my chart value
        self.draw()

    def set_bar_stacked_labs(self, checked, val_list):


        if checked == True:
            for i in range(len(self.bar_list)):
                self.axes.bar_label(self.bar_list[i], labels=val_list, font="Sitka",label_type='center',size=10)
        else:
            for child in self.axes.get_children():
                if isinstance(child, matplotlib.text.Annotation):
                    child.remove()

        self.draw()
    def set_bar_stacked_legend(self,checked, val_list):
        legend_list = []

        if checked == True:
            for i in range(len(val_list)):

                patch = mpatches.Patch( label=val_list[i])
                legend_list.append(patch)

            self.legend = self.axes.legend(handles=legend_list)
            self.draw()
        else:
            self.legend.set_visible(False)

            self.draw()

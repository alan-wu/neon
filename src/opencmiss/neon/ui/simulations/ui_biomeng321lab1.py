# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/designer/simulations/biomeng321lab1.ui'
#
# Created: Fri Mar  4 13:11:44 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Biomeng321Lab1(object):
    def setupUi(self, shared_opengl_widget, Biomeng321Lab1):
        Biomeng321Lab1.setObjectName("Biomeng321Lab1")
        Biomeng321Lab1.resize(1066, 907)
        self.gridLayout_3 = QtGui.QGridLayout(Biomeng321Lab1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(Biomeng321Lab1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.tableWidgetDeformationGradient = QtGui.QTableWidget(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetDeformationGradient.sizePolicy().hasHeightForWidth())
        self.tableWidgetDeformationGradient.setSizePolicy(sizePolicy)
        self.tableWidgetDeformationGradient.setObjectName("tableWidgetDeformationGradient")
        self.tableWidgetDeformationGradient.setColumnCount(0)
        self.tableWidgetDeformationGradient.setRowCount(0)
        self.tableWidgetDeformationGradient.horizontalHeader().setVisible(False)
        self.tableWidgetDeformationGradient.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidgetDeformationGradient)
        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditInvariant1 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditInvariant1.setObjectName("lineEditInvariant1")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditInvariant1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditInvariant2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditInvariant2.setObjectName("lineEditInvariant2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditInvariant2)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditInvariant3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditInvariant3.setObjectName("lineEditInvariant3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditInvariant3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.tableWidgetRightCauchyGreenDeformation = QtGui.QTableWidget(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetRightCauchyGreenDeformation.sizePolicy().hasHeightForWidth())
        self.tableWidgetRightCauchyGreenDeformation.setSizePolicy(sizePolicy)
        self.tableWidgetRightCauchyGreenDeformation.setObjectName("tableWidgetRightCauchyGreenDeformation")
        self.tableWidgetRightCauchyGreenDeformation.setColumnCount(0)
        self.tableWidgetRightCauchyGreenDeformation.setRowCount(0)
        self.tableWidgetRightCauchyGreenDeformation.horizontalHeader().setVisible(False)
        self.tableWidgetRightCauchyGreenDeformation.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidgetRightCauchyGreenDeformation)
        self.gridLayout_2.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_9 = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)
        self.tableWidgetGreenLagrangeStrain = QtGui.QTableWidget(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetGreenLagrangeStrain.sizePolicy().hasHeightForWidth())
        self.tableWidgetGreenLagrangeStrain.setSizePolicy(sizePolicy)
        self.tableWidgetGreenLagrangeStrain.setObjectName("tableWidgetGreenLagrangeStrain")
        self.tableWidgetGreenLagrangeStrain.setColumnCount(0)
        self.tableWidgetGreenLagrangeStrain.setRowCount(0)
        self.tableWidgetGreenLagrangeStrain.horizontalHeader().setVisible(False)
        self.tableWidgetGreenLagrangeStrain.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidgetGreenLagrangeStrain, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.widgetSceneviewer = SceneviewerWidget(self.groupBox, shared_opengl_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetSceneviewer.sizePolicy().hasHeightForWidth())
        self.widgetSceneviewer.setSizePolicy(sizePolicy)
        self.widgetSceneviewer.setObjectName("widgetSceneviewer")
        self.gridLayout_4.addWidget(self.widgetSceneviewer, 0, 1, 2, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditHydrostaticPressure = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditHydrostaticPressure.setObjectName("lineEditHydrostaticPressure")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditHydrostaticPressure)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_11 = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.tableWidgetSecondPiolaKirchoffStress = QtGui.QTableWidget(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetSecondPiolaKirchoffStress.sizePolicy().hasHeightForWidth())
        self.tableWidgetSecondPiolaKirchoffStress.setSizePolicy(sizePolicy)
        self.tableWidgetSecondPiolaKirchoffStress.setObjectName("tableWidgetSecondPiolaKirchoffStress")
        self.tableWidgetSecondPiolaKirchoffStress.setColumnCount(0)
        self.tableWidgetSecondPiolaKirchoffStress.setRowCount(0)
        self.tableWidgetSecondPiolaKirchoffStress.horizontalHeader().setVisible(False)
        self.tableWidgetSecondPiolaKirchoffStress.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidgetSecondPiolaKirchoffStress, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidgetCauchyStress = QtGui.QTableWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetCauchyStress.sizePolicy().hasHeightForWidth())
        self.tableWidgetCauchyStress.setSizePolicy(sizePolicy)
        self.tableWidgetCauchyStress.setObjectName("tableWidgetCauchyStress")
        self.tableWidgetCauchyStress.setColumnCount(0)
        self.tableWidgetCauchyStress.setRowCount(0)
        self.tableWidgetCauchyStress.horizontalHeader().setVisible(False)
        self.tableWidgetCauchyStress.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.tableWidgetCauchyStress, 0, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_10, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Biomeng321Lab1)
        QtCore.QMetaObject.connectSlotsByName(Biomeng321Lab1)

    def retranslateUi(self, Biomeng321Lab1):
        Biomeng321Lab1.setWindowTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Biomeng321 Lab1", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Solution", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Strain Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Deformation Gradient Tensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Biomeng321Lab1", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Biomeng321Lab1", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Invariants", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Biomeng321Lab1", "I1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Biomeng321Lab1", "I2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Biomeng321Lab1", "I3:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Right Cauchy-Green Deformation Tensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Biomeng321Lab1", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Biomeng321Lab1", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Green-Lagrange Strain Tensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Biomeng321Lab1", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Biomeng321Lab1", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Stress Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Hydrostatic Pressure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Biomeng321Lab1", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Second Piola-Kirchhoff Stress Tensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Biomeng321Lab1", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Biomeng321Lab1", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Biomeng321Lab1", "Cauchy Stress Tensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Biomeng321Lab1", "sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Biomeng321Lab1", "=", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.neon.ui.zincwidgets.sceneviewerwidget import SceneviewerWidget

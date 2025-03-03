# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLhRIXM.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(284, 575)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #141414;\n"
"	font-family:\"Open Sans\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color:#141414;\n"
"}\n"
"\n"
"QLabel{ 									/*nazwa*/\n"
"	font-size:15px;\n"
"	color: #ffffff;\n"
"	background:#343434;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#close_btn{\n"
"	background-color: #343434;\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"#fn_bar_frame{										/*frame z nazwa, ikona*/\n"
"	background:#343434;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"\n"
"#button_frame{\n"
"	border-bottom-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"#button_frame QPushButton {\n"
"	background-color: #1f1f1f;\n"
"	color:#c8c8c8;\n"
"	font-size:25px;\n"
"	border-radius: 30px;\n"
"	width:60px;\n"
"	height:60px;\n"
"	padding: 0px;\n"
"	\n"
"\n"
"}\n"
"\n"
"#button_frame QPushButton:pressed {\n"
"	background-color: #434343;\n"
"	border-radius: 12.5px;\n"
"	color:#cbcbcb;\n"
"	\n"
"}\n"
"\n"
"#button_"
                        "frame QPushButton[class=\"group1\"] {\n"
"	background: #929292;\n"
"	color:#010101;\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group1\"]:pressed {\n"
"	background: #a4a4a4;\n"
"	color:#282828;\n"
"\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group2\"] {\n"
"	background: #484848;\n"
"	color:#e4e4e4;\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group2\"]:pressed {\n"
"	background:#656565;\n"
"	color:#e7e7e7;\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group3\"] {\n"
"	background: #d3d3d3;\n"
"	color:#000000;\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group3\"] :pressed{\n"
"	background: #dadada;\n"
"	color:#2b2b2b;\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group4\"] {\n"
"	background: #141414;\n"
"	color:#c8c8c8;\n"
"	font-size:30px;\n"
"	height:40px;\n"
"\n"
"\n"
"}\n"
"\n"
"#button_frame QPushButton[class=\"group4\"]:pressed {\n"
"	background-color: #3a3a3a;\n"
"	color:#c8c8c8;\n"
"	border-radius: 20px;\n"
"	\n"
"\n"
"}\n"
"\n"
"QLineEdit{								/*wynik m.in*/\n"
"\n"
"}\n"
"\n"
""
                        "#wynik_frame {\n"
"	border: none;\n"
"	background-color:#343434;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"#wynik_frame QLineEdit[class=\"linegroup1\"]{\n"
"	background-color: #343434;\n"
"	color: #e3e3e3;\n"
"	border: none;\n"
"	height:80px;\n"
"	padding: 0px 10px;\n"
"	font-size:64px;\n"
"\n"
"}\n"
"\n"
"#wynik_frame QLineEdit[class=\"linegroup2\"]{\n"
"	background-color: #343434;\n"
"	color: #c8c8c8;\n"
"	border: none;\n"
"	height:40px;\n"
"	padding: 0px 10px;\n"
"	padding-bottom:15px;\n"
"	font-size:40px;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fn_bar_frame = QFrame(Form)
        self.fn_bar_frame.setObjectName(u"fn_bar_frame")
        self.fn_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.fn_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.fn_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fn_bar_frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.calculator_icon = QLabel(self.fn_bar_frame)
        self.calculator_icon.setObjectName(u"calculator_icon")
        self.calculator_icon.setEnabled(True)
        self.calculator_icon.setMaximumSize(QSize(20, 20))
        self.calculator_icon.setFrameShape(QFrame.NoFrame)
        self.calculator_icon.setFrameShadow(QFrame.Plain)
        self.calculator_icon.setLineWidth(0)
        self.calculator_icon.setPixmap(QPixmap(u"calculator.png"))
        self.calculator_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.calculator_icon)

        self.app_name = QLabel(self.fn_bar_frame)
        self.app_name.setObjectName(u"app_name")

        self.horizontalLayout.addWidget(self.app_name)

        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.fn_bar_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setEnabled(True)
        self.close_btn.setMaximumSize(QSize(28, 28))
        self.close_btn.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"close3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_2.addWidget(self.fn_bar_frame)

        self.wynik_frame = QFrame(Form)
        self.wynik_frame.setObjectName(u"wynik_frame")
        self.wynik_frame.setFrameShape(QFrame.StyledPanel)
        self.wynik_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.wynik_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.wynik_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.wynik_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.wynik_frame)

        self.button_frame = QFrame(Form)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMaximumSize(QSize(16777215, 16777215))
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.button_frame)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.one = QPushButton(self.button_frame)
        self.one.setObjectName(u"one")

        self.gridLayout.addWidget(self.one, 4, 0, 1, 1)

        self.percentage = QPushButton(self.button_frame)
        self.percentage.setObjectName(u"percentage")

        self.gridLayout.addWidget(self.percentage, 1, 2, 1, 1)

        self.multiply = QPushButton(self.button_frame)
        self.multiply.setObjectName(u"multiply")

        self.gridLayout.addWidget(self.multiply, 2, 3, 1, 1)

        self.plus = QPushButton(self.button_frame)
        self.plus.setObjectName(u"plus")

        self.gridLayout.addWidget(self.plus, 4, 3, 1, 1)

        self.root = QPushButton(self.button_frame)
        self.root.setObjectName(u"root")

        self.gridLayout.addWidget(self.root, 0, 0, 1, 1)

        self.nine = QPushButton(self.button_frame)
        self.nine.setObjectName(u"nine")

        self.gridLayout.addWidget(self.nine, 2, 2, 1, 1)

        self.minus = QPushButton(self.button_frame)
        self.minus.setObjectName(u"minus")

        self.gridLayout.addWidget(self.minus, 3, 3, 1, 1)

        self.power = QPushButton(self.button_frame)
        self.power.setObjectName(u"power")

        self.gridLayout.addWidget(self.power, 0, 2, 1, 1)

        self.eight = QPushButton(self.button_frame)
        self.eight.setObjectName(u"eight")

        self.gridLayout.addWidget(self.eight, 2, 1, 1, 1)

        self.equal = QPushButton(self.button_frame)
        self.equal.setObjectName(u"equal")

        self.gridLayout.addWidget(self.equal, 5, 3, 1, 1)

        self.three = QPushButton(self.button_frame)
        self.three.setObjectName(u"three")

        self.gridLayout.addWidget(self.three, 4, 2, 1, 1)

        self.dot = QPushButton(self.button_frame)
        self.dot.setObjectName(u"dot")

        self.gridLayout.addWidget(self.dot, 5, 2, 1, 1)

        self.five = QPushButton(self.button_frame)
        self.five.setObjectName(u"five")

        self.gridLayout.addWidget(self.five, 3, 1, 1, 1)

        self.brackets = QPushButton(self.button_frame)
        self.brackets.setObjectName(u"brackets")

        self.gridLayout.addWidget(self.brackets, 1, 1, 1, 1)

        self.six = QPushButton(self.button_frame)
        self.six.setObjectName(u"six")

        self.gridLayout.addWidget(self.six, 3, 2, 1, 1)

        self.seven = QPushButton(self.button_frame)
        self.seven.setObjectName(u"seven")

        self.gridLayout.addWidget(self.seven, 2, 0, 1, 1)

        self.newton = QPushButton(self.button_frame)
        self.newton.setObjectName(u"newton")

        self.gridLayout.addWidget(self.newton, 0, 3, 1, 1)

        self.pi = QPushButton(self.button_frame)
        self.pi.setObjectName(u"pi")

        self.gridLayout.addWidget(self.pi, 0, 1, 1, 1)

        self.ac = QPushButton(self.button_frame)
        self.ac.setObjectName(u"ac")

        self.gridLayout.addWidget(self.ac, 1, 0, 1, 1)

        self.four = QPushButton(self.button_frame)
        self.four.setObjectName(u"four")

        self.gridLayout.addWidget(self.four, 3, 0, 1, 1)

        self.zero = QPushButton(self.button_frame)
        self.zero.setObjectName(u"zero")

        self.gridLayout.addWidget(self.zero, 5, 0, 1, 2)

        self.two = QPushButton(self.button_frame)
        self.two.setObjectName(u"two")

        self.gridLayout.addWidget(self.two, 4, 1, 1, 1)

        self.divide = QPushButton(self.button_frame)
        self.divide.setObjectName(u"divide")

        self.gridLayout.addWidget(self.divide, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.button_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.calculator_icon.setText("")
        self.app_name.setText(QCoreApplication.translate("Form", u"MLCalculator", None))
        self.close_btn.setText("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"|", None))
        self.lineEdit.setProperty("class", QCoreApplication.translate("Form", u"linegroup1", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setProperty("class", QCoreApplication.translate("Form", u"linegroup2", None))
        self.one.setText(QCoreApplication.translate("Form", u"1", None))
        self.percentage.setText(QCoreApplication.translate("Form", u"%", None))
        self.percentage.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
        self.multiply.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.multiply.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
        self.plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.plus.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
        self.root.setText(QCoreApplication.translate("Form", u"\u221a", None))
        self.root.setProperty("class", QCoreApplication.translate("Form", u"group4", None))
        self.nine.setText(QCoreApplication.translate("Form", u"9", None))
        self.minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.minus.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
        self.power.setText(QCoreApplication.translate("Form", u"^", None))
        self.power.setProperty("class", QCoreApplication.translate("Form", u"group4", None))
        self.eight.setText(QCoreApplication.translate("Form", u"8", None))
        self.equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.equal.setProperty("class", QCoreApplication.translate("Form", u"group3", None))
        self.three.setText(QCoreApplication.translate("Form", u"3", None))
        self.dot.setText(QCoreApplication.translate("Form", u".", None))
        self.five.setText(QCoreApplication.translate("Form", u"5", None))
        self.brackets.setText(QCoreApplication.translate("Form", u"( )", None))
        self.brackets.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
        self.six.setText(QCoreApplication.translate("Form", u"6", None))
        self.seven.setText(QCoreApplication.translate("Form", u"7", None))
        self.newton.setText(QCoreApplication.translate("Form", u"!", None))
        self.newton.setProperty("class", QCoreApplication.translate("Form", u"group4", None))
        self.pi.setText(QCoreApplication.translate("Form", u"\u03c0", None))
        self.pi.setProperty("class", QCoreApplication.translate("Form", u"group4", None))
        self.ac.setText(QCoreApplication.translate("Form", u"AC", None))
        self.ac.setProperty("class", QCoreApplication.translate("Form", u"group1", None))
        self.four.setText(QCoreApplication.translate("Form", u"4", None))
        self.zero.setText(QCoreApplication.translate("Form", u"0", None))
        self.two.setText(QCoreApplication.translate("Form", u"2", None))
        self.divide.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.divide.setProperty("class", QCoreApplication.translate("Form", u"group2", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icone__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1106, 725)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"} \n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(0, 0))
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 0, 0)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(65,65,65);\n"
"}\n"
"\n"
"QToolBox {\n"
"\n"
"text-align: left;\n"
"background-color: rgb(228,254,255);\n"
" \n"
"}\n"
"\n"
"QToolBox::tab {\n"
"\n"
"border-radius: 5px;\n"
"background-color: rgb(194,232,255);\n"
"text-align: left;\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton::hover {\n"
"\n"
"background-color: rgb(65,65,65);\n"
"border-top-left-radius: 15px\n"
" \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 74, 572))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setSizeIncrement(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setSizeIncrement(QSize(0, 0))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setSizeIncrement(QSize(0, 0))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setEnabled(True)
        self.page_2.setGeometry(QRect(0, 0, 79, 34))
        self.page_2.setSizeIncrement(QSize(0, 0))
        self.page_2.setStyleSheet(u"\n"
"background-color: rgb(62, 62, 62);")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 0, 9)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 9)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_toogle = QPushButton(self.top_frame)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/icones/icons8-card\u00e1pio-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toogle.setIcon(icon)
        self.btn_toogle.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_toogle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62,62,62);\n"
"\n"
" \n"
"\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(16777215, 16777215))
        self.logo.setFont(font)

        self.verticalLayout_6.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dig\";\n"
"}\n"
"\n"
"QFrame {\n"
"\n"
"background-color: rgb(231,231,231);\n"
" \n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 2)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")

        self.gridLayout.addWidget(self.txt_municipio, 4, 0, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")

        self.gridLayout.addWidget(self.txt_uf, 4, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")

        self.gridLayout.addWidget(self.txt_cep, 4, 2, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")

        self.gridLayout.addWidget(self.txt_telefone, 5, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setDragEnabled(False)
        self.txt_complemento.setReadOnly(False)
        self.txt_complemento.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_complemento, 3, 1, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout.addWidget(self.txt_email, 5, 1, 1, 2)

        self.lbl_empresas = QLabel(self.frame_4)
        self.lbl_empresas.setObjectName(u"lbl_empresas")
        self.lbl_empresas.setStyleSheet(u"color: rgb(0, 99, 140);\n"
"background-color: rgb(249, 249, 249);\n"
"")

        self.gridLayout.addWidget(self.lbl_empresas, 0, 0, 1, 3)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 3)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")

        self.gridLayout.addWidget(self.txt_numero, 3, 0, 1, 1)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")

        self.gridLayout.addWidget(self.txt_bairro, 3, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.btn_cadastrar_emp = QPushButton(self.tab)
        self.btn_cadastrar_emp.setObjectName(u"btn_cadastrar_emp")
        self.btn_cadastrar_emp.setMinimumSize(QSize(360, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_cadastrar_emp.setFont(font1)
        self.btn_cadastrar_emp.setStyleSheet(u"QPushButton::hover{\n"
"\n"
"background-color: rgb(0, 120, 255);\n"
"border-radius: 15px;\n"
"color: affff\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(243,243,243);\n"
" \n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.btn_cadastrar_emp, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"QHeaderView::section{\n"
"\n"
"background-color: rgb(140, 140, 140);\n"
"color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"\n"
"background-color: rgb(252,252,252);\n"
" \n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.tb_company)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0,24,74);\n"
"font: 11pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame {\n"
"\n"
"background-color: rgb(230,230,230);\n"
" \n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_exel = QPushButton(self.frame_3)
        self.btn_exel.setObjectName(u"btn_exel")
        self.btn_exel.setMinimumSize(QSize(120, 30))
        self.btn_exel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exel.setStyleSheet(u"QPushButton::hover {\n"
"\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(49,147,0);\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_exel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton::hover {\n"
"\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(255,120,0)\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton::hover {\n"
"\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(255,0,0)\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.pg_contatos)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.label_11 = QLabel(self.pg_contatos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_11)

        self.label_13 = QLabel(self.pg_contatos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_13)

        self.label_8 = QLabel(self.pg_contatos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_8)

        self.label_12 = QLabel(self.pg_contatos)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_12)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.main_container)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Arboni", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Loja Online", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/icone_loja.jpeg\"/></p></body></html>", None))
        self.txt_nome.setText("")
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_municipio.setText("")
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.txt_uf.setText("")
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setText("")
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_email.setText("")
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.lbl_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Empresas</span></p></body></html>", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.txt_bairro.setText("")
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.btn_cadastrar_emp.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Enpresas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"Gerar Exel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CONTATO</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/o-email.png\"/><span style=\" font-size:24pt; vertical-align:super;\">E-mail </span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Telefone <img src=\":/icones/chamada-telefonica.png\"/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; vertical-align:super;\"/><img src=\":/icones/instagram(1).png\"/><span style=\" font-size:14pt; vertical-align:super;\">Instragram</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">YouTube <img src=\":/icones/youtube.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arboni", None))
    # retranslateUi


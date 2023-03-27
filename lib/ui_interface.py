# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceyBXaFi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import lib.Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 612)
        icon = QIcon()
        icon.addFile(u":/Logos/CbpaLogo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit, QComboBox, QLabel, QDateEdit, QCheckBox{\n"
"height: 24px;\n"
"}\n"
"QPushButton{\n"
"border: none;\n"
"cursor: pointer;\n"
"}\n"
"#btnSave{\n"
"background-color: #bc2041;\n"
"border-radius: 4px;\n"
"}\n"
"QWidget{\n"
"color: #F0F3F8;\n"
"background-color: #41436A;\n"
"font-family: Inter;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"}\n"
"#SideBar QPushButton{\n"
"transition-duration: 0.4s;\n"
"border-radius: 4px;\n"
"}\n"
"#SideBar QPushButton:hover{\n"
"background-color: #974063;\n"
"}\n"
"QTableWidget{\n"
"background-color: #F0F3F8;\n"
"color: #41436A;\n"
"}\n"
"#newListActions QPushButton{\n"
"height: 24px;\n"
"}\n"
"QComboBox, QDateEdit, QLineEdit{\n"
"background-color: #F0F3F8;\n"
"border: 1px solid #F54768;\n"
"border-radius: 8px;\n"
"color: #41436A;\n"
"}\n"
"#contentField QPushButton{\n"
"border: 0.5px solid #F54768;\n"
"height: 24px;\n"
"border-radius: 12px;\n"
"transition-duration: 0.4s;\n"
"}\n"
"\n"
"#contentField QPushButton:hover{\n"
"background-color: #974063;\n"
"}\n"
"\n"
"#secM"
                        "ensual, #secPersonalizado, #secOInformes, #secDetallePers{\n"
"border:  1px solid #F54768;\n"
"padding: 4px;\n"
"border-radius: 16px\n"
"}\n"
"QHeaderView::section{\n"
"color: #202020;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SideBar = QWidget(self.centralwidget)
        self.SideBar.setObjectName(u"SideBar")
        self.verticalLayout_3 = QVBoxLayout(self.SideBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.opnMenu = QWidget(self.SideBar)
        self.opnMenu.setObjectName(u"opnMenu")
        self.verticalLayout_4 = QVBoxLayout(self.opnMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_3.addWidget(self.opnMenu, 0, Qt.AlignTop)

        self.actionMenu = QWidget(self.SideBar)
        self.actionMenu.setObjectName(u"actionMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionMenu.sizePolicy().hasHeightForWidth())
        self.actionMenu.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(True)
        self.actionMenu.setFont(font)
        self.verticalLayout = QVBoxLayout(self.actionMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnInsertList = QPushButton(self.actionMenu)
        self.btnInsertList.setObjectName(u"btnInsertList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnInsertList.sizePolicy().hasHeightForWidth())
        self.btnInsertList.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInsertList.setIcon(icon1)

        self.verticalLayout.addWidget(self.btnInsertList)

        self.btnViewList = QPushButton(self.actionMenu)
        self.btnViewList.setObjectName(u"btnViewList")
        sizePolicy1.setHeightForWidth(self.btnViewList.sizePolicy().hasHeightForWidth())
        self.btnViewList.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnViewList.setIcon(icon2)

        self.verticalLayout.addWidget(self.btnViewList)

        self.btnGenInforms = QPushButton(self.actionMenu)
        self.btnGenInforms.setObjectName(u"btnGenInforms")
        sizePolicy1.setHeightForWidth(self.btnGenInforms.sizePolicy().hasHeightForWidth())
        self.btnGenInforms.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenInforms.setIcon(icon3)

        self.verticalLayout.addWidget(self.btnGenInforms)

        self.btnAdminVols = QPushButton(self.actionMenu)
        self.btnAdminVols.setObjectName(u"btnAdminVols")
        sizePolicy1.setHeightForWidth(self.btnAdminVols.sizePolicy().hasHeightForWidth())
        self.btnAdminVols.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAdminVols.setIcon(icon4)

        self.verticalLayout.addWidget(self.btnAdminVols)


        self.verticalLayout_3.addWidget(self.actionMenu)

        self.infoMenu = QWidget(self.SideBar)
        self.infoMenu.setObjectName(u"infoMenu")
        self.verticalLayout_2 = QVBoxLayout(self.infoMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnInfo = QPushButton(self.infoMenu)
        self.btnInfo.setObjectName(u"btnInfo")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInfo.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.btnInfo)

        self.btnHelp = QPushButton(self.infoMenu)
        self.btnHelp.setObjectName(u"btnHelp")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.btnHelp)


        self.verticalLayout_3.addWidget(self.infoMenu)


        self.horizontalLayout.addWidget(self.SideBar)

        self.contentField = QStackedWidget(self.centralwidget)
        self.contentField.setObjectName(u"contentField")
        self.pageInsert = QWidget()
        self.pageInsert.setObjectName(u"pageInsert")
        self.verticalLayout_10 = QVBoxLayout(self.pageInsert)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.pageInsert)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.inpCorrCia = QLineEdit(self.pageInsert)
        self.inpCorrCia.setObjectName(u"inpCorrCia")

        self.horizontalLayout_6.addWidget(self.inpCorrCia)

        self.cbEfectiva = QCheckBox(self.pageInsert)
        self.cbEfectiva.setObjectName(u"cbEfectiva")

        self.horizontalLayout_6.addWidget(self.cbEfectiva)

        self.label_2 = QLabel(self.pageInsert)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.inpCorrGral = QLineEdit(self.pageInsert)
        self.inpCorrGral.setObjectName(u"inpCorrGral")

        self.horizontalLayout_6.addWidget(self.inpCorrGral)

        self.label_5 = QLabel(self.pageInsert)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.inpActo = QLineEdit(self.pageInsert)
        self.inpActo.setObjectName(u"inpActo")
        self.inpActo.setMaxLength(15)

        self.horizontalLayout_6.addWidget(self.inpActo)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.pageInsert)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.inpDireccion = QLineEdit(self.pageInsert)
        self.inpDireccion.setObjectName(u"inpDireccion")

        self.horizontalLayout_7.addWidget(self.inpDireccion)

        self.label_4 = QLabel(self.pageInsert)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.inpFecha = QDateEdit(self.pageInsert)
        self.inpFecha.setObjectName(u"inpFecha")

        self.horizontalLayout_7.addWidget(self.inpFecha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.liVols = QTableWidget(self.pageInsert)
        self.liVols.setObjectName(u"liVols")

        self.horizontalLayout_8.addWidget(self.liVols)

        self.newListActions = QVBoxLayout()
        self.newListActions.setObjectName(u"newListActions")
        self.newListActions.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_29 = QLabel(self.pageInsert)
        self.label_29.setObjectName(u"label_29")

        self.newListActions.addWidget(self.label_29)

        self.lblTotalLista = QLabel(self.pageInsert)
        self.lblTotalLista.setObjectName(u"lblTotalLista")

        self.newListActions.addWidget(self.lblTotalLista)

        self.label_6 = QLabel(self.pageInsert)
        self.label_6.setObjectName(u"label_6")

        self.newListActions.addWidget(self.label_6)

        self.inpVol = QLineEdit(self.pageInsert)
        self.inpVol.setObjectName(u"inpVol")

        self.newListActions.addWidget(self.inpVol)

        self.btnAddVol = QPushButton(self.pageInsert)
        self.btnAddVol.setObjectName(u"btnAddVol")

        self.newListActions.addWidget(self.btnAddVol)

        self.btnDelVol = QPushButton(self.pageInsert)
        self.btnDelVol.setObjectName(u"btnDelVol")

        self.newListActions.addWidget(self.btnDelVol)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.newListActions.addItem(self.verticalSpacer)

        self.btnSave = QPushButton(self.pageInsert)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMaximumSize(QSize(16777215, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon7)

        self.newListActions.addWidget(self.btnSave)


        self.horizontalLayout_8.addLayout(self.newListActions)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.contentField.addWidget(self.pageInsert)
        self.pageView = QWidget()
        self.pageView.setObjectName(u"pageView")
        self.horizontalLayout_2 = QHBoxLayout(self.pageView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.viewLl = QWidget(self.pageView)
        self.viewLl.setObjectName(u"viewLl")
        self.verticalLayout_8 = QVBoxLayout(self.viewLl)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.viewLl)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.inpSearchList = QLineEdit(self.viewLl)
        self.inpSearchList.setObjectName(u"inpSearchList")

        self.verticalLayout_8.addWidget(self.inpSearchList)

        self.liListsView = QTableWidget(self.viewLl)
        self.liListsView.setObjectName(u"liListsView")

        self.verticalLayout_8.addWidget(self.liListsView)


        self.horizontalLayout_2.addWidget(self.viewLl)

        self.editLl = QWidget(self.pageView)
        self.editLl.setObjectName(u"editLl")
        self.editLl.setEnabled(True)
        self.verticalLayout_5 = QVBoxLayout(self.editLl)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.actEdit = QWidget(self.editLl)
        self.actEdit.setObjectName(u"actEdit")
        self.verticalLayout_6 = QVBoxLayout(self.actEdit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.actEdit)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.inpCorrGenEdit = QLineEdit(self.actEdit)
        self.inpCorrGenEdit.setObjectName(u"inpCorrGenEdit")

        self.horizontalLayout_3.addWidget(self.inpCorrGenEdit)

        self.cbEfectivaEdit = QCheckBox(self.actEdit)
        self.cbEfectivaEdit.setObjectName(u"cbEfectivaEdit")

        self.horizontalLayout_3.addWidget(self.cbEfectivaEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.actEdit)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.fldActoEdit = QLineEdit(self.actEdit)
        self.fldActoEdit.setObjectName(u"fldActoEdit")
        self.fldActoEdit.setMaxLength(15)

        self.horizontalLayout_4.addWidget(self.fldActoEdit)

        self.label_11 = QLabel(self.actEdit)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.inpFechaEdit = QDateEdit(self.actEdit)
        self.inpFechaEdit.setObjectName(u"inpFechaEdit")

        self.horizontalLayout_4.addWidget(self.inpFechaEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.actEdit)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.inpDireccionEdit = QLineEdit(self.actEdit)
        self.inpDireccionEdit.setObjectName(u"inpDireccionEdit")

        self.horizontalLayout_5.addWidget(self.inpDireccionEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.actEdit)

        self.volsEdit = QWidget(self.editLl)
        self.volsEdit.setObjectName(u"volsEdit")
        self.verticalLayout_7 = QVBoxLayout(self.volsEdit)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_31 = QLabel(self.volsEdit)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_7.addWidget(self.label_31)

        self.lbl_cVolsEdit = QLabel(self.volsEdit)
        self.lbl_cVolsEdit.setObjectName(u"lbl_cVolsEdit")

        self.verticalLayout_7.addWidget(self.lbl_cVolsEdit)

        self.label_12 = QLabel(self.volsEdit)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)

        self.inpAddVolEdit = QLineEdit(self.volsEdit)
        self.inpAddVolEdit.setObjectName(u"inpAddVolEdit")

        self.verticalLayout_7.addWidget(self.inpAddVolEdit)

        self.btnAddVol_2 = QPushButton(self.volsEdit)
        self.btnAddVol_2.setObjectName(u"btnAddVol_2")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddVol_2.setIcon(icon8)

        self.verticalLayout_7.addWidget(self.btnAddVol_2)

        self.btnDelVol_2 = QPushButton(self.volsEdit)
        self.btnDelVol_2.setObjectName(u"btnDelVol_2")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDelVol_2.setIcon(icon9)

        self.verticalLayout_7.addWidget(self.btnDelVol_2)

        self.liVolsEdit = QTableWidget(self.volsEdit)
        self.liVolsEdit.setObjectName(u"liVolsEdit")

        self.verticalLayout_7.addWidget(self.liVolsEdit)


        self.verticalLayout_5.addWidget(self.volsEdit)

        self.btnSaveEdit = QPushButton(self.editLl)
        self.btnSaveEdit.setObjectName(u"btnSaveEdit")
        self.btnSaveEdit.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.btnSaveEdit)

        self.btnDeleteEdit = QPushButton(self.editLl)
        self.btnDeleteEdit.setObjectName(u"btnDeleteEdit")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeleteEdit.setIcon(icon10)

        self.verticalLayout_5.addWidget(self.btnDeleteEdit)


        self.horizontalLayout_2.addWidget(self.editLl)

        self.contentField.addWidget(self.pageView)
        self.pageInform = QWidget()
        self.pageInform.setObjectName(u"pageInform")
        self.verticalLayout_12 = QVBoxLayout(self.pageInform)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_4 = QSpacerItem(17, 178, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetMaximumSize)
        self.secMensual = QWidget(self.pageInform)
        self.secMensual.setObjectName(u"secMensual")
        self.verticalLayout_9 = QVBoxLayout(self.secMensual)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.secMensual)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.secMensual)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.cbMesInforme = QComboBox(self.secMensual)
        self.cbMesInforme.setObjectName(u"cbMesInforme")

        self.horizontalLayout_9.addWidget(self.cbMesInforme)

        self.label_15 = QLabel(self.secMensual)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.cbAnoInforme = QComboBox(self.secMensual)
        self.cbAnoInforme.setObjectName(u"cbAnoInforme")

        self.horizontalLayout_9.addWidget(self.cbAnoInforme)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btnResMen = QPushButton(self.secMensual)
        self.btnResMen.setObjectName(u"btnResMen")

        self.horizontalLayout_10.addWidget(self.btnResMen)

        self.btnSendResMen = QPushButton(self.secMensual)
        self.btnSendResMen.setObjectName(u"btnSendResMen")

        self.horizontalLayout_10.addWidget(self.btnSendResMen)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_13.addWidget(self.secMensual)

        self.secPersonalizado = QWidget(self.pageInform)
        self.secPersonalizado.setObjectName(u"secPersonalizado")
        self.verticalLayout_11 = QVBoxLayout(self.secPersonalizado)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_19 = QLabel(self.secPersonalizado)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_11.addWidget(self.label_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.secPersonalizado)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.infoFechaDesde = QDateEdit(self.secPersonalizado)
        self.infoFechaDesde.setObjectName(u"infoFechaDesde")

        self.horizontalLayout_11.addWidget(self.infoFechaDesde)

        self.label_17 = QLabel(self.secPersonalizado)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.infoFechaHasta = QDateEdit(self.secPersonalizado)
        self.infoFechaHasta.setObjectName(u"infoFechaHasta")

        self.horizontalLayout_11.addWidget(self.infoFechaHasta)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btnGenResEsp = QPushButton(self.secPersonalizado)
        self.btnGenResEsp.setObjectName(u"btnGenResEsp")

        self.horizontalLayout_12.addWidget(self.btnGenResEsp)

        self.btnGenArr = QPushButton(self.secPersonalizado)
        self.btnGenArr.setObjectName(u"btnGenArr")

        self.horizontalLayout_12.addWidget(self.btnGenArr)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_13.addWidget(self.secPersonalizado)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.secDetallePers = QWidget(self.pageInform)
        self.secDetallePers.setObjectName(u"secDetallePers")
        self.horizontalLayout_14 = QHBoxLayout(self.secDetallePers)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_30 = QLabel(self.secDetallePers)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_14.addWidget(self.label_30)

        self.fldInfoPersonal = QLineEdit(self.secDetallePers)
        self.fldInfoPersonal.setObjectName(u"fldInfoPersonal")

        self.horizontalLayout_14.addWidget(self.fldInfoPersonal)

        self.btnGenInfoP = QPushButton(self.secDetallePers)
        self.btnGenInfoP.setObjectName(u"btnGenInfoP")

        self.horizontalLayout_14.addWidget(self.btnGenInfoP)


        self.verticalLayout_12.addWidget(self.secDetallePers)

        self.secOInformes = QWidget(self.pageInform)
        self.secOInformes.setObjectName(u"secOInformes")
        self.horizontalLayout_15 = QHBoxLayout(self.secOInformes)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btnInfo90Dias = QPushButton(self.secOInformes)
        self.btnInfo90Dias.setObjectName(u"btnInfo90Dias")

        self.horizontalLayout_15.addWidget(self.btnInfo90Dias)


        self.verticalLayout_12.addWidget(self.secOInformes)

        self.verticalSpacer_2 = QSpacerItem(17, 178, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.contentField.addWidget(self.pageInform)
        self.pageVols = QWidget()
        self.pageVols.setObjectName(u"pageVols")
        self.horizontalLayout_21 = QHBoxLayout(self.pageVols)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget = QWidget(self.pageVols)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_13 = QVBoxLayout(self.widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.fldSrcAdminVols = QLineEdit(self.widget)
        self.fldSrcAdminVols.setObjectName(u"fldSrcAdminVols")

        self.horizontalLayout_16.addWidget(self.fldSrcAdminVols)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.tblAdminVols = QTableWidget(self.widget)
        self.tblAdminVols.setObjectName(u"tblAdminVols")

        self.verticalLayout_13.addWidget(self.tblAdminVols)


        self.horizontalLayout_21.addWidget(self.widget)

        self.widget_2 = QWidget(self.pageVols)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_14 = QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_14.addWidget(self.label_20)

        self.fldRegGral = QLineEdit(self.widget_2)
        self.fldRegGral.setObjectName(u"fldRegGral")

        self.verticalLayout_14.addWidget(self.fldRegGral)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_14.addWidget(self.label_21)

        self.fldRegCia = QLineEdit(self.widget_2)
        self.fldRegCia.setObjectName(u"fldRegCia")

        self.verticalLayout_14.addWidget(self.fldRegCia)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_14.addWidget(self.label_23)

        self.fldNombre = QLineEdit(self.widget_2)
        self.fldNombre.setObjectName(u"fldNombre")

        self.verticalLayout_14.addWidget(self.fldNombre)

        self.label_24 = QLabel(self.widget_2)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_14.addWidget(self.label_24)

        self.fldApellidoP = QLineEdit(self.widget_2)
        self.fldApellidoP.setObjectName(u"fldApellidoP")

        self.verticalLayout_14.addWidget(self.fldApellidoP)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_14.addWidget(self.label_25)

        self.fldApellidoM = QLineEdit(self.widget_2)
        self.fldApellidoM.setObjectName(u"fldApellidoM")

        self.verticalLayout_14.addWidget(self.fldApellidoM)

        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_14.addWidget(self.label_26)

        self.fldRut = QLineEdit(self.widget_2)
        self.fldRut.setObjectName(u"fldRut")

        self.verticalLayout_14.addWidget(self.fldRut)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_14.addWidget(self.label_27)

        self.fldeMail = QLineEdit(self.widget_2)
        self.fldeMail.setObjectName(u"fldeMail")

        self.verticalLayout_14.addWidget(self.fldeMail)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_14.addWidget(self.label_22)

        self.fldFechaIn = QDateEdit(self.widget_2)
        self.fldFechaIn.setObjectName(u"fldFechaIn")

        self.verticalLayout_14.addWidget(self.fldFechaIn)

        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_14.addWidget(self.label_28)

        self.cbSubEstado = QComboBox(self.widget_2)
        self.cbSubEstado.setObjectName(u"cbSubEstado")

        self.verticalLayout_14.addWidget(self.cbSubEstado)

        self.btnEditVol = QPushButton(self.widget_2)
        self.btnEditVol.setObjectName(u"btnEditVol")

        self.verticalLayout_14.addWidget(self.btnEditVol)

        self.btnAddVol_3 = QPushButton(self.widget_2)
        self.btnAddVol_3.setObjectName(u"btnAddVol_3")

        self.verticalLayout_14.addWidget(self.btnAddVol_3)


        self.horizontalLayout_21.addWidget(self.widget_2)

        self.contentField.addWidget(self.pageVols)

        self.horizontalLayout.addWidget(self.contentField)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.contentField.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Estadistica - Bomba Tobalaba", None))
        self.btnInsertList.setText(QCoreApplication.translate("MainWindow", u"Insertar Lista", None))
        self.btnViewList.setText(QCoreApplication.translate("MainWindow", u"Ver Servicios", None))
        self.btnGenInforms.setText(QCoreApplication.translate("MainWindow", u"Generar Informes", None))
        self.btnAdminVols.setText(QCoreApplication.translate("MainWindow", u"Administrar Bomberos", None))
        self.btnInfo.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Correlativo Compa\u00f1\u00eda", None))
        self.cbEfectiva.setText(QCoreApplication.translate("MainWindow", u"Obligaroria", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Correlativo General", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tipo de Acto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Total de Voluntarios:", None))
        self.lblTotalLista.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Registro Voluntario", None))
        self.btnAddVol.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnDelVol.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Buscar Acto de Servicio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Correlativo General", None))
        self.cbEfectivaEdit.setText(QCoreApplication.translate("MainWindow", u"Obligatorio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tipo de Acto", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Total de Voluntarios:", None))
        self.lbl_cVolsEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Voluntario", None))
        self.btnAddVol_2.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.btnDelVol_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnSaveEdit.setText(QCoreApplication.translate("MainWindow", u"Guardar Lista", None))
        self.btnDeleteEdit.setText(QCoreApplication.translate("MainWindow", u"Eliminar Lista", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Resumen Mensual", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.btnResMen.setText(QCoreApplication.translate("MainWindow", u"Generar Resumen", None))
        self.btnSendResMen.setText(QCoreApplication.translate("MainWindow", u"Enviar Resumen", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Resumen Espec\u00edfico", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fecha Desde", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fecha Hasta", None))
        self.btnGenResEsp.setText(QCoreApplication.translate("MainWindow", u"Generar Resumen", None))
        self.btnGenArr.setText(QCoreApplication.translate("MainWindow", u"Generar Arrastre", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Generar Informe por Personal:", None))
        self.btnGenInfoP.setText(QCoreApplication.translate("MainWindow", u"Generar Detalle", None))
        self.btnInfo90Dias.setText(QCoreApplication.translate("MainWindow", u"Informe 90 Dias", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reg. Greneral", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Registro General", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Registro Compa\u00f1\u00eda", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Rut", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fecha de Ingreso", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Sub-Estado", None))
        self.btnEditVol.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnAddVol_3.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi


from lib.ui_interface import Ui_MainWindow
from lib.connection import Conexion
from PySide6 import QtWidgets, QtCore, QtGui
import sys
import os.path
import pdfkit
import pandas as pd

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.information = {
            "version" : "1.1.1.0",
            "autor" : "Andrés Bahamondes Carvajal"
        }

        try:
            self.database = Conexion()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error conectandose a la base de datos.\n Código de error: {e}"
            )

        # Mostrar interfaz de ingreso
        self.btnInsertList.clicked.connect(lambda : self.contentField.setCurrentIndex(0))
        # Mostrar interfaz de edicion
        self.btnViewList.clicked.connect(lambda : self.contentField.setCurrentIndex(1))
        # Mostrar interfaz de informes
        self.btnGenInforms.clicked.connect(lambda : self.contentField.setCurrentIndex(2))
        # Mostrar interfaz de voluntarios
        self.btnAdminVols.clicked.connect(lambda : self.contentField.setCurrentIndex(3))
        # Mostrar interfaz de Licencias
        self.btnLicencias.clicked.connect(lambda : self.contentField.setCurrentIndex(4))

        # Mostrar info
        self.btnInfo.clicked.connect(self.show_app_info)
        # Mostrar ayuda
        self.btnHelp.clicked.connect(self.show_help_manual)
        self.lista = set()
        self.contentField.setCurrentIndex(0)

        self.btnInsertList.clicked.connect(self.clearFields)
        self.btnViewList.clicked.connect(self.buscar_listas)

        # Interfaz de Ingreso
        self.efectivaEstateIn = {2 : "OB", 0: "AB"}
        actos = QtWidgets.QCompleter(['SS.EE', 'SS.OO.', 'ACADEMIA', 'J. OFF', 'INCENDIO', 'I. FOREST.', 'C. ADM.', "CONS. DISC",
                                      'DESFILE CB', 'SS. EE. CB', 'ROMERIA CB'
                                      '10-0-1', '10-0-2', '10-0-3', '10-0-4', '10-0-5', '10-0-6', '10-0-7', '10-0-8',
                                      '10-1-1', '10-1-2', '10-1-3',
                                      '10-2-1', '10-2-2', '10-2-3',
                                      '10-3-1', '10-3-2', '10-3-3', '10-3-4', '10-3-5', '10-3-6', '10-3-7', '10-3-8', '10-3-9', '10-3-10',
                                      '10-4-1', '10-4-2', '10-4-3', '10-4-4', '10-4-5',
                                      '10-5-1', '10-5-2', '10-5-3',
                                      '10-6-1', '10-6-2', '10-6-3', '10-6-4',
                                      '10-7-1',
                                      '10-8-1', '10-8-2', '10-8-3', '10-8-4',
                                      '10-9-1', '10-9-2', '10-9-3', '10-9-4', '10-9-5', '10-9-6', '10-9-7', '10-9-8',
                                      '10-10-1', '10-10-2',
                                      '10-11', '10-12', '10-13', '10-14', '10-15', '10-16',
                                      '10-17-1', '10-17-2', '10-17-3'])
        actos.setCaseSensitivity(QtWidgets.QCompleter.caseSensitivity(actos).CaseInsensitive)
        self.inpActo.setCompleter(actos)
        self.lblTotalLista.setText(str(len(self.lista)))
        self.inpCorrCia.setMaxLength(7)
        self.inpActo.setMaxLength(10)
        self.inpDireccion.setMaxLength(100)
        self.liVols.setColumnCount(2)
        self.liVols.setHorizontalHeaderLabels(['Registro General', 'Nombre'])
        self.liVols.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.liVols.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.liVols.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        header = self.liVols.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.btnAddVol.clicked.connect(lambda: self.add_vol_to_list(self.inpVol.text()))
        self.inpVol.returnPressed.connect(lambda: self.add_vol_to_list(self.inpVol.text()))
        self.btnDelVol.clicked.connect(self.del_vol_to_list)
        self.btnSave.clicked.connect(self.save_list)
        
        #Interfaz de Edicion
        self.efectivaEditEstates = {2: "OB", 0:"AB"}
        self.cbEfectivaEditEstates = {"OB": QtCore.Qt.CheckState.Checked, "AB": QtCore.Qt.CheckState.Unchecked}
        self.liListsView.setColumnCount(4)
        self.liListsView.setHorizontalHeaderLabels(['Correlativo de Compañía', 'Fecha', 'Acto', 'Dirección'])
        self.buscar_listas()
        self.inpSearchList.textChanged.connect(self.buscar_listas)
        headerSrcList = self.liListsView.horizontalHeader()
        headerSrcList.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.liListsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.liListsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.liListsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.liListsView.selectionModel().selectionChanged.connect(self.getActo)
        self.liVolsEdit.setColumnCount(2)
        self.liVolsEdit.setHorizontalHeaderLabels(['Registro General', 'Nombre'])
        headerEditList = self.liVolsEdit.horizontalHeader()
        headerEditList.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerEditList.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.liVolsEdit.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.liVolsEdit.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.liVolsEdit.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.inpAddVolEdit.returnPressed.connect(lambda: self.add_vol_to_list(self.inpAddVolEdit.text()))
        self.btnAddVol_2.clicked.connect(lambda: self.add_vol_to_list(self.inpAddVolEdit.text()))
        self.btnDelVol_2.clicked.connect(self.del_vol_to_list)
        self.btnDeleteEdit.clicked.connect(self.delete_list)
        self.btnSaveEdit.clicked.connect(self.edit_list)
        self.fldActoEdit.setCompleter(actos)

        # Interfaz de Informes
        self.headeractos = ["Correlativo Compañia", "Tipo de Acto", "Correlativo General",
                            "Fecha",
                            "Direccion", "Lista", "Cant. Vols."]
        self.header = ["Reg. Gral", "Nombre", "Apellido Paterno", "Apellido Materno", "Listas totales", "Asistencia General",
                  "Listas Obligatorias",
                  "Asistencia Obligatorias"]

        self.informesPath = os.path.abspath('informes\\asistencia.xlsx')
        self.cbMesInforme.addItems(self.database.getMonth())
        self.cbAnoInforme.addItems(self.database.getYear())
        self.btnResMen.clicked.connect(self.resumenMensual)
        self.btnGenResEsp.clicked.connect(self.resumenEspecifico)
        self.btnInfo90Dias.clicked.connect(self.informe90dias)
        self.btnGenArr.clicked.connect(self.arrastre)
        self.btnSendResMen.clicked.connect(self.enviarCorreos)
        self.btnGenInfoP.clicked.connect(self.informePersonal)
        completer = QtWidgets.QCompleter(self.database.getVolsInfoPers())
        self.fldInfoPersonal.setCompleter(completer)


        # Interfaz de Administracion
        self.tblAdminVols.setColumnCount(2)
        self.tblAdminVols.setHorizontalHeaderLabels(['N° Registro', 'Nombre'])
        self.buscar_bomberos()
        self.tblAdminVols.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblAdminVols.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tblAdminVols.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblAdminVols.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblAdminVols.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fldSrcAdminVols.textChanged.connect(self.buscar_bomberos)
        self.tblAdminVols.selectionModel().selectionChanged.connect(self.getBombero)
        self.btnEditVol.clicked.connect(self.editar_vol)
        self.btnAddVol_3.clicked.connect(self.insert_vol)
        self.cbSubEstado.addItems(['ACTIVO', 'SUSPENDIDO', 'RENUNCIADO', 'SEPARADO', 'EXPULSADO'])

        #Interfaz Licencias
        self.cbVBCapitan.setTristate(True)
        self.LicenseAproved = 'Pendiente'
        self.LicenseStates = {2: 'Aprobado',0: 'Pendiente',1: 'Rechazado'}
        self.CBLicenseStates = {'Aprobado': QtCore.Qt.CheckState.Checked, 'Pendiente': QtCore.Qt.CheckState.Unchecked, 'Rechazado': QtCore.Qt.CheckState.PartiallyChecked}
        self.tblLicencias.setColumnCount(4)
        self.tblLicencias.setHorizontalHeaderLabels(['Correlativo', 'Nombre', 'Fecha Desde', 'Fecha Hasta'])
        self.buscarLicencias()
        self.tblLicencias.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblLicencias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblLicencias.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblLicencias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.inpSrcLic.textChanged.connect(self.buscarLicencias)
        self.tblLicencias.selectionModel().selectionChanged.connect(self.getLicencia)
        self.inpRegLic.textChanged.connect(self.buscarNombre)
        self.btnSaveLic.clicked.connect(self.saveLicencia)
        self.btnUpdateLic.clicked.connect(self.updateLicencia)
        self.btnNullLic.clicked.connect(self.borrarLicencia)

    def getSaveFile(self):
        file_filter = 'Todos los Archivos;; Archivo Excel (*.xlsx *.xls)'
        response = QtWidgets.QFileDialog.getSaveFileName(
            parent= self,
            caption='Guardar el Reporte',
            filter=file_filter,
            selectedFilter= 'Archivo Excel (*.xlsx *.xls)'
        )
        return response[0]

    def borrarLicencia(self):
        alerta = QtWidgets.QMessageBox.warning(
            self, "Aviso", "¿Seguro que desea anular la licencia?", buttons=QtWidgets.QMessageBox.Apply | QtWidgets.QMessageBox.Cancel
        )
        if alerta == QtWidgets.QMessageBox.Apply:
            try:
                self.database.deleteLicencia(self.inpCorrLic.text())
                self.buscarLicencias()
                QtWidgets.QMessageBox.information(self, "Licencias", "Licencia anulada con éxito")
            except Exception as e:
                dialogo = QtWidgets.QMessageBox.warning(
                    self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
                )

    def updateLicencia(self):
        try:
            self.database.licenciaUpdate(self.inpCorrLic.text(), self.inpRegLic.text(), self.dateDesdeLic.text(), self.dateHastaLic.text(), self.txtMotivoLic.toPlainText(), self.LicenseStates[self.cbVBCapitan.checkState().value])
            self.buscarLicencias()
            QtWidgets.QMessageBox.information(self, "Licencias", "Licencia actualizada con éxito")
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )

    def saveLicencia(self):
        try:
            self.database.nv_lic(self.inpCorrLic.text(), self.inpRegLic.text(), self.dateDesdeLic.text(), self.dateHastaLic.text(), self.txtMotivoLic.toPlainText(), self.LicenseStates[self.cbVBCapitan.checkState().value])
            QtWidgets.QMessageBox.information(self, "Licencias", "Licencia guardada con éxito")
            self.buscarLicencias()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )

    def buscarNombre(self):
        try:
            self.inpNomLic.setText(self.database.get_nameVols(self.inpRegLic.text()))
        except Exception as e:
            pass

    def getLicencia(self, seleccion):
        if seleccion.indexes():
            fila = seleccion.indexes()[0].row()
            cLic = self.tblLicencias.model().index(fila, 0).data()
            CorrLic, nReg, fDesde, fHasta, motivo, aprobado = self.database.get_LicCont(cLic)
            self.inpCorrLic.setText(CorrLic)
            self.inpNomLic.setText(self.database.get_nameVols(nReg))
            self.inpRegLic.setText(nReg)
            self.dateDesdeLic.setDate(fDesde)
            self.dateHastaLic.setDate(fHasta)
            self.txtMotivoLic.setText(motivo)
            self.cbVBCapitan.setCheckState(self.CBLicenseStates[aprobado])

    def buscarLicencias(self):
        self.clearTable(self.tblLicencias)
        # try:
        lics = self.database.get_ListLic(self.inpSrcLic.text())
        for i in range(len(lics)):
            cLic, nombre, apellido1, apellido2, fDesde, fHasta = lics[i]
            fNombre = f'{nombre} {apellido1} {apellido2}'
            self.tblLicencias.insertRow(i)
            self.tblLicencias.setItem(i, 0, QtWidgets.QTableWidgetItem(cLic))
            self.tblLicencias.setItem(i, 1, QtWidgets.QTableWidgetItem(fNombre))
            self.tblLicencias.setItem(i, 2, QtWidgets.QTableWidgetItem(str(fDesde)))
            self.tblLicencias.setItem(i, 3, QtWidgets.QTableWidgetItem(str(fHasta)))
        # except Exception as e:
        #     pass

    def informePersonal(self):
        try:
            informesPath = self.getSaveFile()
            headerAsis = ['Año', 'Listas Totales', 'Asistencia Total', 'Listas Obligatorias','Asistencia Obligatorias']
            headerActos = ["Correlativo Compañia", "Tipo de Acto", "Correlativo General",
                           "Fecha",
                           "Direccion", "Lista"]
            vol = self.fldInfoPersonal.text()
            vol = vol.split('-')
            vol[0] = vol[0].strip()
            asistencia, actos = self.database.getInformePersonal(vol[0])
            dfAsis = pd.DataFrame(asistencia)
            dfAct = pd.DataFrame(actos)
            excelWriter = pd.ExcelWriter(informesPath)
            dfAsis.to_excel(excelWriter, sheet_name='Asistencia', header=headerAsis, index= False)
            dfAct.to_excel(excelWriter, sheet_name='Actos', header=headerActos, index= False)
            excelWriter.close()
            os.startfile(informesPath)
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def enviarCorreos(self):
        alerta = QtWidgets.QMessageBox.warning(
            self, "Aviso", "Estará a punto de enviar los resúmenes individuales a los correos.\n ¿Desea Proceder?", buttons=QtWidgets.QMessageBox.Apply | QtWidgets.QMessageBox.Cancel)
        if alerta == QtWidgets.QMessageBox.Apply:
            try:
                self.database.send_messageMo(self.cbMesInforme.currentText(), self.cbAnoInforme.currentText())
                aviso = QtWidgets.QMessageBox.information(self, 'Enviando', 'Resumen enviado a los correos')
            except Exception as e:
                dialogo = QtWidgets.QMessageBox.warning(
                    self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
                )
                return
        else:
            return

    def arrastre(self):
        try:
            arrastrePath = self.getSaveFile()
            arrastre = self.database.getArrastre(self.infoFechaDesde.text(),self.infoFechaHasta.text())
            open(os.path.abspath('resources/template.html'), 'w').write(arrastre)
            with open(os.path.abspath('resources/template.html')) as f:
                pdfkit.from_file(f, arrastrePath, options={'page-size': 'Legal', 'encoding': 'UTF-8'})
            os.startfile(arrastrePath)
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el arrastre.\n Código de error: {e}"
            )
            return

    def informe90dias(self):
        header = ["Reg. Gral", "Nombre", "Apellido Paterno", "Apellido Materno"]
        try:
            path = self.getSaveFile()
            lista, actos = self.database.info90()
            dfActos = pd.DataFrame(actos)
            dfListas = pd.DataFrame(lista)
            exelWriter = pd.ExcelWriter(path)
            dfListas.to_excel(exelWriter, sheet_name="Voluntarios sin asistencia", header=header, index=False)
            dfActos.to_excel(exelWriter, sheet_name="Actos", header=self.headeractos, index=False)
            exelWriter.close()
            os.startfile(path)
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    def resumenEspecifico(self):
        try:
            path = self.getSaveFile()
            lista, actos, estadistica = self.database.resEspecifico(self.infoFechaDesde.text(), self.infoFechaHasta.text())
            dfActos = pd.DataFrame(actos)
            dfListas = pd.DataFrame(lista)
            dfEstadistica = pd.DataFrame(estadistica)
            exelWriter = pd.ExcelWriter(path)
            dfListas.to_excel(exelWriter, sheet_name="Asistencia Voluntarios", header=self.header, index=False)
            dfActos.to_excel(exelWriter, sheet_name="Actos", header=self.headeractos, index=False)
            dfEstadistica.to_excel(exelWriter, sheet_name="Estadistica", header=False, index=False)
            exelWriter.close()
            os.startfile(path)
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    def resumenMensual(self):
        try:
            informesPath = self.getSaveFile()
            headerEstadistica = ['Incendios', 'Estructurales', 'Rescates', 'Salvamentos', 'Materiales Peligrosos', 'Llamados de Comandancia']
            lista, actos, estadistica = self.database.resMensual(self.cbMesInforme.currentText(), self.cbAnoInforme.currentText())
            dfActos = pd.DataFrame(actos)
            dfListas = pd.DataFrame(lista)
            dfEstadistica = pd.DataFrame(estadistica)
            exelWriter = pd.ExcelWriter(informesPath)
            dfListas.to_excel(exelWriter, sheet_name="Asistencia Voluntarios", header=self.header, index=False)
            dfActos.to_excel(exelWriter, sheet_name="Actos", header=self.headeractos, index=False)
            dfEstadistica.to_excel(exelWriter, sheet_name="Estadistica", header=False, index=False)
            exelWriter.close()
            os.startfile(informesPath)

        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    def insert_vol(self):
        try:
            self.database.addVols(self.fldRegGral.text(), self.fldRegCia.text(), self.fldNombre.text(), self.fldApellidoP.text(), self.fldApellidoM.text(), self.fldRut.text(), self.fldeMail.text(), self.fldFechaIn.text(), self.cbSubEstado.currentText())
            self.buscar_bomberos()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def editar_vol(self):
        try:
            rGrali = self.tblAdminVols.model().index(self.tblAdminVols.currentRow(), 0).data()
            self.database.editVol(rGrali, self.fldRegGral.text(), self.fldRegCia.text(), self.fldNombre.text(), self.fldApellidoP.text(), self.fldApellidoM.text(), self.fldRut.text(), self.fldeMail.text(), self.fldFechaIn.text(), self.cbSubEstado.currentText())
            self.buscar_bomberos()
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Información actualizada exitosamente")
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
            self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def getBombero(self, seleccion):
        if seleccion.indexes():
            fila = seleccion.indexes()[0].row()
            cCia = self.tblAdminVols.model().index(fila, 0).data()
            rGral, nombre, apellido1, apellido2, email, rut, dv, rCia, fIngreso, sub_estado = self.database.getVols(cCia)
            self.fldRegGral.setText(rGral)
            self.fldRegCia.setText(str(rCia))
            self.fldNombre.setText(nombre)
            self.fldApellidoP.setText(apellido1)
            self.fldApellidoM.setText(apellido2)
            self.fldRut.setText(f'{rut}-{dv}')
            self.fldeMail.setText(email)
            self.fldFechaIn.setDate(fIngreso)
            self.cbSubEstado.setCurrentText(sub_estado)

    def buscar_bomberos(self):
        self.clearTable(self.tblAdminVols)
        vols = self.database.srcVols(self.fldSrcAdminVols.text())
        for i in range(len(vols)):
            rGral, nombre, apellido1, apellido2 = vols[i]
            self.tblAdminVols.insertRow(i)
            self.tblAdminVols.setItem(i, 0, QtWidgets.QTableWidgetItem(rGral))
            self.tblAdminVols.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{nombre} {apellido1} {apellido2}'))

    def edit_list(self):
        try:
            cCia = self.liListsView.model().index(self.liListsView.currentRow(), 0).data()
            self.database.editLista(cCia, self.fldActoEdit.text(), self.inpCorrGenEdit.text(), self.inpFechaEdit.text(), self.inpDireccionEdit.text(), self.efectivaEstateIn[self.cbEfectivaEdit.checkState().value], len(self.lista),self.lista)
            self.cbMesInforme.clear()
            self.cbAnoInforme.clear()
            self.cbMesInforme.addItems(self.database.getMonth())
            self.cbAnoInforme.addItems(self.database.getYear())
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Lista guardada exitosamente")
            self.buscar_listas()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
            self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def delete_list(self):
        alerta = QtWidgets.QMessageBox.warning(
            self, "Aviso", "¿Seguro que desea eliminar la lista?", buttons=QtWidgets.QMessageBox.Apply | QtWidgets.QMessageBox.Cancel
        )
        if alerta == QtWidgets.QMessageBox.Apply:
            try:
                self.database.delLista(self.liListsView.model().index(self.liListsView.currentRow(), 0).data())
                dialogo = QtWidgets.QMessageBox.information(
                    self, "Cambios aplicados", "Lista eliminada con exito"
                )
                self.buscar_listas()
            except Exception as e:
                dialogo = QtWidgets.QMessageBox.warning(
                    self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
                )
                return
        else:
            return

    def getActo(self, seleccion):
        if seleccion.indexes():
            self.lista.clear()
            fila = seleccion.indexes()[0].row()
            cCia = self.liListsView.model().index(fila, 0).data()
            acto, cGral, fecha, direccion, lista = self.database.getActos(cCia)
            self.inpCorrGenEdit.setText(str(cGral))
            self.fldActoEdit.setText(acto)
            self.inpDireccionEdit.setText(direccion)
            self.inpFechaEdit.setDate(fecha)
            self.cbEfectivaEdit.setCheckState(self.cbEfectivaEditEstates[lista])
            self.clearTable(self.liVolsEdit)
            vols = self.database.extVols(cCia)
            for i in range(len(vols)):
                rGral, nombre, apellido1, apellido2 = vols[i]
                self.liVolsEdit.insertRow(i)
                self.liVolsEdit.setItem(i, 0, QtWidgets.QTableWidgetItem(rGral))
                self.liVolsEdit.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{nombre} {apellido1} {apellido2}'))
                self.lista.add(rGral)
            self.lbl_cVolsEdit.setText(str(len(self.lista)))

    def buscar_listas(self):
        self.clearTable(self.liListsView)
        listas = self.database.srcLista(self.inpSearchList.text())
        for i in range(len(listas)):
            cCia, cGral, acto, direccion = listas[i]
            self.liListsView.insertRow(i)
            self.liListsView.setItem(i, 0, QtWidgets.QTableWidgetItem(cCia))
            self.liListsView.setItem(i, 1, QtWidgets.QTableWidgetItem(str(cGral)))
            self.liListsView.setItem(i, 2, QtWidgets.QTableWidgetItem(acto))
            self.liListsView.setItem(i, 3, QtWidgets.QTableWidgetItem(direccion))
    
    def add_vol_to_list(self, input_vol):
        try:
            reg, nombre, apellido, apellido2= self.database.addVolLista(input_vol)
            if self.contentField.currentIndex() == 0:
                rowPosition = self.liVols.rowCount()
                if input_vol not in self.lista:
                    self.liVols.insertRow(rowPosition)
                    self.liVols.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(reg))
                    self.liVols.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f'{nombre} {apellido} {apellido2}'))
                    self.inpVol.clear()
                    self.lista.add(reg)
                    self.lblTotalLista.setText(str(len(self.lista)))
                else:
                    self.inpVol.clear()
                    return
            elif self.contentField.currentIndex() == 1:
                rowPosition = self.liVolsEdit.rowCount()
                if input_vol not in self.lista:
                    self.liVolsEdit.insertRow(rowPosition)
                    self.liVolsEdit.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(reg))
                    self.liVolsEdit.setItem(rowPosition, 1,
                                            QtWidgets.QTableWidgetItem(f'{nombre} {apellido} {apellido2}'))
                    self.inpAddVolEdit.clear()
                    self.lista.add(reg)
                    self.lbl_cVolsEdit.setText(str(len(self.lista)))
                else:
                    self.inpAddVolEdit.clear()
                    return
                return
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
            self, "Error", f"Voluntario no encontrado.\n Código de error: {e}"
            )
            return

    def del_vol_to_list(self):
        if self.contentField.currentIndex() == 0:
            self.lista.remove(self.liVols.model().index(self.liVols.currentRow(), 0).data())
            self.liVols.removeRow(self.liVols.currentRow())
            self.lblTotalLista.setText(str(len(self.lista)))
        elif self.contentField.currentIndex() == 1:
            self.lista.remove(self.liVolsEdit.model().index(self.liVolsEdit.currentRow(), 0).data())
            self.liVolsEdit.removeRow(self.liVolsEdit.currentRow())
            self.lbl_cVolsEdit.setText(str(len(self.lista)))
            return

    def clearTable(self, table):
        for i in range(table.rowCount(), -1, -1):
            table.removeRow(i)

    def clearFields(self):
        self.lista.clear()
        self.inpActo.clear()
        self.inpDireccion.clear()
        self.inpCorrCia.clear()
        self.inpCorrGral.clear()
        self.clearTable(self.liVols)
        self.cbEfectiva.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.lblTotalLista.setText(str(len(self.lista)))
        self.cbMesInforme.clear()
        self.cbAnoInforme.clear()
        self.cbMesInforme.addItems(self.database.getMonth())
        self.cbAnoInforme.addItems(self.database.getYear())

    def save_list(self):
        try:
            self.database.addLista(self.inpCorrCia.text(), self.inpActo.text(), self.inpCorrGral.text(), self.inpFecha.text(), self.inpDireccion.text(), self.efectivaEstateIn[self.cbEfectiva.checkState().value], len(self.lista), self.lista)
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Lista guardada exitosamente")
            self.efectiva = "AB"
            self.clearFields()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def show_help_manual(self):
        os.startfile(os.path.abspath("resources\\Instructivo Sistema de Estadistica.pdf"))
        return
    def show_app_info(self):
        QtWidgets.QMessageBox.information(self, "Información", f"Versión: {self.information['version']} \nAutor: {self.information['autor']} \n © 2023 por Andrés Bahamondes")
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
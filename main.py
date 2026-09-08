from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6 import QtCore
import icone__rc
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from principal_ui import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(MainWindow, self).__init__ () 
    self.setupUi(self)
    self.setWindowTitle("teste")
    appIcon = QIcon("")
    self.setWindowIcon(appIcon)

    #########################################
    #TOGLE BUTTON
    self.btn_toogle.clicked.connect(self.leftMenu)
    #########################################

    #########################################
    #PAGINAS DO SISTEMA
    self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
    self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
    self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
    self.btn_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
    ###########################################################################################
    
    ###########################################################################################
    #PREENCHER AUTOMATICAMENTE TODOS OS CAMPOS
    self.txt_cnpj.editingFinished.connect(self.consult_api)
    ###########################################################################################
    
    ###########################################################################################
    #CADASTRAR EMPRESAS
    self.btn_cadastrar_emp.clicked.connect(self.cadastrar_empresas)
    ###########################################################################################
    
    ###########################################################################################
    #BUSCAR EMPRESAS
    #self..clicked.connect(self.excluir_empresas)
    ###########################################################################################
    self.buscas_empresas()
  
  def leftMenu(self):
    width = self.left_menu.width()
      
    if width == 9:
      newWidth = 200
    else:
      newWidth = 9
    
    self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
    self.animation.setDuration(500)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

  def consult_api(self):
    campos = consulta_cnpj(self.txt_cnpj.text())
    
    self.txt_nome.setText(campos[0])
    self.txt_logradouro.setText(campos[1])
    self.txt_numero.setText(campos[2])
    self.txt_complemento.setText(campos[3])
    self.txt_bairro.setText(campos[4])
    self.txt_municipio.setText(campos[5])
    self.txt_uf.setText(campos[6])
    self.txt_cep.setText(campos[7].replace('.', '').replace('-', ''))
    self.txt_telefone.setText(campos[8].replace('(', '').replace('-', '').replace(')', ''))
    self.txt_email.setText(campos[9])
  
  def cadastrar_empresas(self):
    
    db = Data_base()
    db.connect()
    
    fullDataSet = (
      
      self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(), self.txt_complemento.text(),
      self.txt_bairro.text(), self.txt_municipio.text(), self.txt_uf.text(), self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text()
      
    )
    #CADASTRAR NO BANCO DE DADOS
    resp = db.register_company(fullDataSet)
    
    if resp == "OK":
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle("Casdastro Realizado")
      msg.setText("Cadastro Realizado com sucesso")
      msg.exec()
      db.close_connection()
      
      return
    else:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setWindowTitle("Erro ao cadastrar")
      msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
      msg.exec()
      db.close_connection()
      return
    
  def buscas_empresas(self):
    db = Data_base()
    db.connect()
    result = db.select_all_companies()
    
    self.tb_company.clearContents()
    self.tb_company.setRowCount(len(result))
    print(result)
    
    for row, text in enumerate(result):
      for column, data in enumerate(text):
        self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))
        
    db.close_connection()

  def update_empresas(self):
    
    dados = []
    update_dados = []
    
    for row in range(self.tb_company.rowCount()):
      for column in range(self.tb_company.columnCount()):
        dados.append(self.tb_company.item(row, column).text())
        print(dados)
    
    

    
if __name__ == "__main__":
  
  db = Data_base()
  db.connect()
  db.create_table_company()
  db.close_connection()

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
          


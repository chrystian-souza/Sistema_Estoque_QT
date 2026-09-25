import sqlite3
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6 import QtCore
import icone__rc
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from principal_ui import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Data_base
import pandas as pd


class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(MainWindow, self).__init__ () 
    self.setupUi(self)
    self.setWindowTitle("teste")
    appIcon = QIcon("")
    self.setWindowIcon(appIcon)
   

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
    #ATUALIZAR DADOS
    self.btn_alterar.clicked.connect(self.update_empresas)
    ###########################################################################################
    #BUSCAR EMPRESAS
    #self..clicked.connect(self.excluir_empresas)
    ###########################################################################################
    ###########################################################################################
    #TOGLE BUTTON
    self.btn_toogle.clicked.connect(self.leftMenu)
    ###########################################################################################
    ###########################################################################################
    #EXCLUIR EMPRESAS
    self.btn_excluir.clicked.connect(self.delete_empresa)
    ###########################################################################################
    #GERAR EXCEL
    self.btn_exel.clicked.connect(self.gerar_exel)
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
      self.buscas_empresas()
      
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
    update_dados = []

    # PEGAR TODOS OS DADOS DA TABELA
    for row in range(self.tb_company.rowCount()):
        dados = []

        for column in range(self.tb_company.columnCount()):
            dados.append(self.tb_company.item(row, column).text())

        update_dados.append(dados)

    # ATUALIZAR DADOS DO BANCO
    db = Data_base()
    db.connect()

    for emp in update_dados:
        db.update_company(tuple(emp))

    db.close_connection()

    # MENSAGEM
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Atualização de dados")
    msg.setText("Dados atualizados com sucesso!")
    msg.exec()

    # ATUALIZAR A TABELA
    self.buscas_empresas()
    
  def delete_empresa(self):
    

    db = Data_base()
    db.connect()
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle('Excluir')
    msg.setText('Esse registro será excluido.')
    msg.setInformativeText('Você tem certeza que deseja excluir?')
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    resp = msg.exec()
    
    if resp == QMessageBox.Yes:
      cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
      result = db.delete_companies(cnpj)
      self.buscas_empresas()
      
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setInformativeText('EMPRESAS')
      msg.setText(result)
      msg.exec()
      
    db.close_connection() 
    
  def gerar_exel(self):
    cnx = None
    try:
        cnx = sqlite3.connect('system.db')
        empresas = pd.read_sql_query('SELECT * FROM Empresa', cnx)
        caminho_salvar = r"C:\Users\chrystian\Documents\Empresas.xlsx"

        # A operação que está falhando DEVE ficar dentro do try:
        empresas.to_excel(caminho_salvar, sheet_name='empresas', index=False)

        # Pop-up de Sucesso no Front
        QMessageBox.information(
            self,
            "Excel",
            "Relatório Excel gerado com sucesso!"
        )

    except PermissionError:
        # Pop-up específico para arquivo em uso no Excel
        QMessageBox.warning(
            self,
            "Arquivo Bloqueado",
            "Não foi possível salvar o arquivo!\n\n"
            "O arquivo 'Empresas.xlsx' já está aberto no Excel ou em outro programa. "
            "Feche-o e tente novamente."
        )

    except Exception as e:
        # Qualquer outro tipo de falha
        QMessageBox.critical(
            self,
            "Erro",
            f"Ocorreu um erro ao gerar o relatório:\n{e}"
        )

    finally:
        if cnx is not None:
            cnx.close()
            
            
if __name__ == "__main__":
  
  db = Data_base()
  db.connect()
  db.create_table_company()
  db.close_connection()

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
          


from scp import SCPClient
import paramiko
import os
import shutil
from fabric import Connection
import csv
from datetime import datetime
from activites_de_configuration import fetch2
from activites_du_parefeu import  fetch3
from activites_memoire import  fetch4
from activites_reseau import  fetch5
from activites_ssh import  fetch6
from activites_usb import  fetch7
from Advanced_Configuration_and_Power_Interface_events import  fetch8
from cmd_history import  fetch9
from cnx_actives import  fetch10
from device_detection import  fetch11
from kernel_logs import  fetch12
from processus import  fetch13
from status_des_services import  fetch14
from sys_alert import  fetch15
from sys_critical import  fetch16
from sys_debug import  fetch17
from sys_emerg import  fetch18
from sys_error import  fetch19
from sys_info import  fetch20
from sys_notice import  fetch21
from sys_warning import  fetch22
from system_boots import  fetch23
from transactions_effectuees import  fetch24
from utilisation_disque import  fetch25
import datetime
from datetime import datetime
from cipher_decipher_logic.AES_cipher_decipher import get_password
from PyQt5.QtWidgets import QWidget, QDialog
from Progress.Ui_Config_progress import Ui_Form3
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import threading
import multiprocessing
import subprocess
import sys

class MainWindow(QWidget):
    def __init__(self, machine_name, ip_add, local_path_in,csv_file):
        super().__init__()
        self.show_config_progress(machine_name, ip_add, local_path_in,csv_file)
        
    def show_config_progress(self, machine_name, ip_add, local_path_in,csv_file):
        self.config_progress_form = QDialog()
        self.ui_config_progress = Ui_Form3() 
        self.ui_config_progress.setupUi(self.config_progress_form)
        self.ui_config_progress.configprogress_finish.clicked.connect(self.config_progress_form.reject)
        self.ui_config_progress.configprogress_finish.setDisabled(True)
        # self.ui_config_progress.Loading.hide()
        self.config_progress_form.show()
        fetch_process = multiprocessing.Process(target=self.fetching_logs, args=(self, machine_name, ip_add, local_path_in,csv_file))
        fetch_process.start()
        
        
    def fetching_logs(self, machine_name, ip_add, local_path_in,csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if machine_name == row['Machine_Name'] and ip_add == row['ip_add']:
                    port = row['port']
                    username = row['linux_username']
                    ciphered_password = row['password']
                    #print(ciphered_password)
                    password1 = get_password(ciphered_password)
                    self.ui_config_progress.Loading.hide()
    # here
                    password=password1
                    #print(password)
                    host=ip_add
                    hostname=ip_add
                    ssh_client = ssh_client_creation(host, port, username, password)
                else:
                    pass
    
        # Établir une connexion avec les informations fournies
        conn = Connection(host, user=username, port=port, connect_kwargs={"password": password})
    
    
        # Utiliser la méthode sudo() pour exécuter la commande avec les privilèges sudo,
        # en spécifiant le mot de passe
        result1 = conn.sudo('rsync -av /var/log/ /home/journal', password=password, warn=True)
            
        result2 = conn.sudo('chmod -R a+rwx /home/journal', password=password, warn=True)
    
        commands = ['rm /home/journal/README']
        # Exécution des commandes avec sudo 
        results = test_cron(ssh_client, commands, password)
        # print(results) 
    
    
        
        # Récupérer la date du jour
        date_aujourdhui = datetime.now().strftime("%d-%m-%Y")
        
        maintenant = datetime.now()
    
        # Formater la date et l'heure selon vos besoins
        heure = maintenant.strftime("%H-%M")
    
    
        # Spécifier le chemin local en utilisant le nom de la machine
        
        # Définition de la variable add
        add = rf'{machine_name}/{machine_name}_{date_aujourdhui}_{heure}'
        
        filename=rf'{machine_name}_{date_aujourdhui}_{heure}'
        
    
        # Spécifier le chemin local en utilisant le nom de la machine
        local_path_verify = local_path_in + add
        
    
        # Supprimer le dossier existant s'il existe déjà
        if os.path.exists(local_path_verify):
            shutil.rmtree(local_path_verify)
            print("Le dossier existant a été supprimé.")
    
    
    
        # local_path_in est  Chemin local initial
    
        # Ajout de la valeur de la variable add au chemin local
        local_path = local_path_in + add
        
        # Créer le répertoire s'il n'existe pas déjà
        os.makedirs(local_path, exist_ok=True)
    
    
        # Télécharger le dossier
        remote_path = '/home/journal'
        download_folder(ip_add, remote_path, local_path, username, password)
    
    
        result4 = conn.sudo('rm -r /home/journal', password=password, warn=True)
        
        result=fetch2(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch3(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch4(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch5(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch6(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch7(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch8(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch9(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch10(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch11(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch12(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch13(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch14(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch15(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch16(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch17(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch18(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch19(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch20(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch21(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch22(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch23(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch24(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
        result=fetch25(machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename)
        self.ui_config_progress.configprogress_TextEdit.append(result)
    
def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client

def test_cron(ssh_client, commands, password):
    results2 = []  # Liste pour stocker les résultats des commandes
    
    for command in commands:
        # Exécute la commande spécifiée sur le serveur distant sans sudo
        stdin, stdout, stderr = ssh_client.exec_command(command, get_pty=True)
        
        # Récupère le résultat de la commande
        result2 = stdout.read().decode().strip()
        
        # Vérifie s'il y a eu des erreurs
        error = stderr.read().decode().strip()
        if error:
            results2.append(error)
        else:
            # Stocke le résultat dans la liste des résultats
            results2.append(result2)
    
    return results2



def download_folder(remote_host, remote_path, local_path, username, password):
    # Créer une connexion SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Se connecter à la machine distante
        ssh_client.connect(remote_host, username=username, password=password)

        # Initialiser SCPClient
        with SCPClient(ssh_client.get_transport()) as scp:
            # Télécharger le dossier distant
            scp.get(remote_path, local_path, recursive=True)

    except Exception as e:
        print(f"Erreur lors du téléchargement du dossier: {e}")

    finally:
        # Fermer la connexion SSH
        ssh_client.close()



def main(machine_name, ip_add, local_path_in,csv_file):
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication([])

    window = MainWindow('SERVER1','192.168.69.45','C:\\ProgramData\\REMT\\','Tests/LOGS/users.csv')
    app.exec_()

if __name__ == "__main__":
    main("SERVER1", "192.168.69.45", "C:\\ProgramData\\REMT\\", "Tests/LOGS/users.csv")
    
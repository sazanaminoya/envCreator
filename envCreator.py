# coding: utf-8

import os.path
import win32com.client
import subprocess
import logging


def installChoco():

    logging.debug("Start installing %s" % 'chocolatey')
    strCommand =   "@powershell -NoProfile -ExecutionPolicy Bypass -Command \"iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))\" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\\bin"
    subprocess.check_output(strCommand, shell=True)


def InstallChocoPkg():

    apps = ['git', 'virtualbox', 'vagrant', 'patheditor', 'winmerge', 'python', 'putty', 'winscp', 'sublimetext3']
    for app in apps:
        logging.debug("Start installing %s" % app)
        subprocess.check_output("choco install %s" % app, shell=True)


def prepareVagrant():

    shell = win32com.client.Dispatch('WScript.shell')
    wd = shell.SpecialFolders('MyDocuments')
    wd = os.path.join(wd, "workspace")

    subprocess.check_output("mkdir %s" % wd)
    subprocess.check_output("cd %s" % wd)
    subprocess.check_output("vagrant init ychubachi/enpit")


def createShortCut(path, scFileName, icon = None):

    if icon == None:
        icon = path

    shell = win32com.client.Dispatch('WScript.shell')
    desktop = shell.SpecialFolders('Desktop')
    wd = shell.SpecialFolders('MyDocuments')

    shCut = shell.CreateShortcut(os.path.join(desktop, scFileName + ".lnk"))
    shCut.TargetPath = path
    shCut.WindowStyle = 1
    shCut.IconLocation = icon
    shCut.WorkingDirectory = os.path.join(wd, "enPiT")

    shCut.Save()



LOG_FILENAME = 'envCreator.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

PATH_NAME = "C:\Program Files\Git\git-bash.exe"
PATH_NAME86 = "C:\Program Files (x86)\Git\git-bash.exe"
GITBASH_NAME = "git-bash"

installChoco()
InstallChocoPkg()
createShortCut(PATH_NAME, _NAME) if os.path.exists(PATH_NAME) else createShortCut(PATH_NAME86, _NAME)
prepareVagrant()

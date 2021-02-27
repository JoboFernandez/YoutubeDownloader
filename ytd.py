import time
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
import ytd_crawler
import os


files = []

class Ui_win_main(object):
    def setupUi(self, win_main):
        win_main.setObjectName("win_main")
        win_main.resize(500, 450)
        win_main.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(win_main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_addtoqueue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addtoqueue.setGeometry(QtCore.QRect(210, 145, 280, 55))
        self.btn_addtoqueue.setObjectName("btn_addtoqueue")
        self.grp_fileformat = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_fileformat.setGeometry(QtCore.QRect(10, 140, 190, 60))
        self.grp_fileformat.setObjectName("grp_fileformat")
        self.rdb_mp3 = QtWidgets.QRadioButton(self.grp_fileformat)
        self.rdb_mp3.setGeometry(QtCore.QRect(30, 25, 50, 20))
        self.rdb_mp3.setChecked(True)
        self.rdb_mp3.setObjectName("rdb_mp3")
        self.rdb_mp4 = QtWidgets.QRadioButton(self.grp_fileformat)
        self.rdb_mp4.setGeometry(QtCore.QRect(110, 25, 50, 20))
        self.rdb_mp4.setObjectName("rdb_mp4")
        self.pgb_downloadstatus = QtWidgets.QProgressBar(self.centralwidget)
        self.pgb_downloadstatus.setGeometry(QtCore.QRect(10, 360, 480, 25))
        self.pgb_downloadstatus.setProperty("value", 0)
        self.pgb_downloadstatus.setOrientation(QtCore.Qt.Horizontal)
        self.pgb_downloadstatus.setObjectName("pgb_downloadstatus")
        self.lbl_downloadstatus = QtWidgets.QLabel(self.centralwidget)
        self.lbl_downloadstatus.setGeometry(QtCore.QRect(10, 390, 480, 13))
        self.lbl_downloadstatus.setObjectName("lbl_downloadstatus")
        self.txt_queue = QtWidgets.QListWidget(self.centralwidget)
        self.txt_queue.setGeometry(QtCore.QRect(10, 220, 350, 120))
        self.txt_queue.setObjectName("txt_queue")
        self.btn_pushup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pushup.setGeometry(QtCore.QRect(370, 220, 120, 30))
        self.btn_pushup.setObjectName("btn_pushup")
        self.btn_pushdown = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pushdown.setGeometry(QtCore.QRect(370, 255, 120, 30))
        self.btn_pushdown.setObjectName("btn_pushdown")
        self.btn_deletequeue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deletequeue.setGeometry(QtCore.QRect(370, 310, 120, 30))
        self.btn_deletequeue.setObjectName("btn_deletequeue")
        self.frm_inputs = QtWidgets.QFrame(self.centralwidget)
        self.frm_inputs.setGeometry(QtCore.QRect(130, 10, 360, 120))
        self.frm_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_inputs.setObjectName("frm_inputs")
        self.txt_filepath = QtWidgets.QLineEdit(self.frm_inputs)
        self.txt_filepath.setGeometry(QtCore.QRect(0, 90, 360, 25))
        self.txt_filepath.setObjectName("txt_filepath")
        self.txt_ytdurl = QtWidgets.QLineEdit(self.frm_inputs)
        self.txt_ytdurl.setGeometry(QtCore.QRect(0, 10, 360, 25))
        self.txt_ytdurl.setObjectName("txt_ytdurl")
        self.txt_filename = QtWidgets.QLineEdit(self.frm_inputs)
        self.txt_filename.setGeometry(QtCore.QRect(0, 50, 360, 25))
        self.txt_filename.setObjectName("txt_filename")
        self.frm_labels = QtWidgets.QFrame(self.centralwidget)
        self.frm_labels.setGeometry(QtCore.QRect(10, 10, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frm_labels.setFont(font)
        self.frm_labels.setAutoFillBackground(False)
        self.frm_labels.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_labels.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_labels.setObjectName("frm_labels")
        self.lbl_filename = QtWidgets.QLabel(self.frm_labels)
        self.lbl_filename.setGeometry(QtCore.QRect(0, 50, 120, 20))
        self.lbl_filename.setObjectName("lbl_filename")
        self.lbl_ytdurl = QtWidgets.QLabel(self.frm_labels)
        self.lbl_ytdurl.setGeometry(QtCore.QRect(0, 10, 120, 20))
        self.lbl_ytdurl.setObjectName("lbl_ytdurl")
        self.lbl_filepath = QtWidgets.QLabel(self.frm_labels)
        self.lbl_filepath.setGeometry(QtCore.QRect(0, 90, 120, 20))
        self.lbl_filepath.setObjectName("lbl_filepath")
        win_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(win_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        win_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(win_main)
        self.statusbar.setObjectName("statusbar")
        win_main.setStatusBar(self.statusbar)
        self.mnu_aboutytd = QtWidgets.QAction(win_main)
        self.mnu_aboutytd.setObjectName("mnu_aboutytd")
        self.menuHelp.addAction(self.mnu_aboutytd)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(win_main)
        default_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        self.txt_filepath.setText(default_directory)
        QtCore.QMetaObject.connectSlotsByName(win_main)

        self.capture_events()

    def retranslateUi(self, win_main):
        _translate = QtCore.QCoreApplication.translate
        win_main.setWindowTitle(_translate("win_main", "Youtube Downloader"))
        self.btn_addtoqueue.setText(_translate("win_main", "ADD TO QUEUE"))
        self.grp_fileformat.setTitle(_translate("win_main", "File Format:"))
        self.rdb_mp3.setText(_translate("win_main", "MP3"))
        self.rdb_mp4.setText(_translate("win_main", "MP4"))
        self.lbl_downloadstatus.setText(_translate("win_main", "Queue is empty"))
        self.btn_pushup.setText(_translate("win_main", "Prioritize"))
        self.btn_pushdown.setText(_translate("win_main", "Deprioritize"))
        self.btn_deletequeue.setText(_translate("win_main", "Delete"))
        self.lbl_filename.setText(_translate("win_main", "File Name:"))
        self.lbl_ytdurl.setText(_translate("win_main", "Youtube URL:"))
        self.lbl_filepath.setText(_translate("win_main", "File Path:"))
        self.menuHelp.setTitle(_translate("win_main", "Help"))
        self.mnu_aboutytd.setText(_translate("win_main", "About YoutubeDownloader"))

    def capture_events(self):
        self.btn_addtoqueue.clicked.connect(self.btn_addtoqueue_click)
        self.btn_pushup.clicked.connect(lambda: self.btn_push_click(-1))
        self.btn_pushdown.clicked.connect(lambda: self.btn_push_click(1))
        self.btn_deletequeue.clicked.connect(self.btn_deletequeue_click)

    def btn_addtoqueue_click(self):
        # self.btn_addtoqueue.setEnabled(False)

        global files
        ytdurl = self.txt_ytdurl.text()
        fileextension = ".mp3" if self.rdb_mp3.isChecked() else ".mp4"
        filename = self.txt_filename.text() + fileextension
        filepath = self.txt_filepath.text()

        # self.update_status(filename, 5, "Checking for file duplicates")
        if self.file_isDuplicated(ytdurl, filepath, filename):
            pass
        else:
            files.append((ytdurl, filepath, filename))
            self.txt_queue.addItem(filename)
            self.clear_inputs()

        # self.update_status(filename, 15, "Downloading...")
        downloader = ytd_crawler.Downloader()
        if self.rdb_mp3.isChecked():
            downloader.download_to_mp3(ytdurl)
            # self.update_status(filename, 95, "Renaming...")
            for file in os.listdir(filepath):
                if "kbps" in file:
                    os.chdir(filepath)
                    os.rename(file, filename)
                    break
            
        # self.update_status(filename, 0, "")
        # self.btn_addtoqueue.setEnabled(True)
        
        
    
    def file_isDuplicated(self, ytdurl, filepath, filename):
        global files
        temp_file = os.path.join(filepath, filename)
        for url, path, file in files:
            if ytdurl == url:
                self.message_show_ytdurl_exists(url)
                return True
            if temp_file == os.path.join(path, file):
                self.message_show_filename_exists(filepath, filename)
                return True
        if filename in os.listdir(filepath):
            self.message_show_filename_exists(filepath, filename)
            return True
        return False

    def message_show_filename_exists(self, filepath, filename):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("File name duplication warning")
        msg.setText(f"File {os.path.join(filepath, filename)} already exists either in download queue or in file path.")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setInformativeText("Please rename the file name or check its extension name.")
        msg.exec_()

    def clear_inputs(self):
        self.txt_ytdurl.setText("")
        self.txt_filename.setText("")

    def message_show_ytdurl_exists(self, ytdurl):
        global files
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Youtube URL duplication warning")
        msg.setText(f"URL {ytdurl} is already in queue.")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setInformativeText("Please proceed with another download.")
        msg.exec_()

    def btn_deletequeue_click(self):
        global files
        currentRow = self.txt_queue.currentRow()
        if currentRow != -1:
            files.pop(currentRow)
        self.txt_queue.takeItem(currentRow)

    def btn_push_click(self, dir):
        global files
        currentRow = self.txt_queue.currentRow()
        if dir == -1 and currentRow > 0:
            files.insert(currentRow + dir, files.pop(currentRow))
        elif dir == 1 and currentRow < len(files) - 1:
            files.insert(currentRow + dir, files.pop(currentRow))
        currentItem = self.txt_queue.takeItem(currentRow)
        self.txt_queue.insertItem(currentRow + dir, currentItem)
        self.txt_queue.setCurrentItem(currentItem)

    def update_status(self, filename, progress, info):
        self.pgb_downloadstatus.setValue(progress)
        if progress == 0:
            self.lbl_downloadstatus.setText("Queue is empty")
        else:
            self.lbl_downloadstatus.setText(f"Downloading {filename}: {info}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win_main = QtWidgets.QMainWindow()
    ui = Ui_win_main()
    ui.setupUi(win_main)
    win_main.show()
    sys.exit(app.exec_())

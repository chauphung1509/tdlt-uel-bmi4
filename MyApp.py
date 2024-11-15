from PyQt5.QtWidgets import QApplication, QMainWindow

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEx()
myui.setupUi(mainwindow)
myui.setupSignalAndSlot()
myui.showWindow()
app.exec()
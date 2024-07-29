import sys
import struct
from PyQt5 import QtCore, QtGui, QtWidgets
from array import array
import traceback
import re

class OPTIONAL_DEVICE: 
    def __init__(self):
        self.ECGCable = [0] * 3
        self.bluetooth = 0
        self.spo2 = 0
        self.nibp = 0
        self.etco2 = 0
        self.energySelectionPaddle = 0
        self.pacer = 0
        self.temp = 0
        self.Version = 0
        self.reserved = [0] * 8

def read_config_bin(file_path):
    config_data = OPTIONAL_DEVICE()
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()
            binary_data_size= len(binary_data)
            
            struct_format = "<3B 8B 8B"
            expected_size = struct.calcsize(struct_format) 
            
            if binary_data_size < expected_size:
                print("Binary data size is less than expected. Padding with zeros.")
                binary_data += b'\x00' * (expected_size - binary_data_size)
            elif binary_data_size > expected_size:
                print("Binary data size is greater than expected. Truncating.")
                binary_data = binary_data[:expected_size]
                
            unpacked_data = struct.unpack(struct_format, binary_data)
            
            config_data.ECGCable = list(unpacked_data[0:3]) #3B
            config_data.bluetooth = unpacked_data[3]
            config_data.spo2 = unpacked_data[4]
            config_data.nibp = unpacked_data[5]
            config_data.etco2 = unpacked_data[6]
            config_data.energySelectionPaddle = unpacked_data[7]
            config_data.pacer = unpacked_data[8]
            config_data.temp = unpacked_data[9]
            config_data.Version = unpacked_data[10]
            config_data.reserved = list(unpacked_data[11:19]) #8B
            
    except Exception as e:
        print(f"config_data: {config_data}")
        print(f"Error reading binary file: {e}")
    
    return config_data

def get_config_values(config_data):
    # Helper function to get the variable names and their integer values
    config_values = []
    for name in dir(config_data):
        if not name.startswith("__") and not callable(getattr(config_data, name)):
            value = getattr(config_data, name)
            config_values.append((name, value))
    return config_values

def pack_config_data(config_data):
    packed_data = struct.pack(
        "<3B 8B 8B",
        *config_data.ECGCable,
        config_data.bluetooth,
        config_data.spo2,
        config_data.nibp, 
        config_data.etco2, 
        config_data.energySelectionPaddle, 
        config_data.pacer, 
        config_data.temp, 
        config_data.Version, 
        *config_data.reserved 
    )
    
    return packed_data

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 800, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Filed", "Value"])
        self.pushButtonA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonA.setGeometry(QtCore.QRect(240, 20, 120, 30))
        self.pushButtonA.setObjectName("pushButtonA")
        self.pushButtonB=QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonB.setGeometry(QtCore.QRect(380,20,120,30))
        self.pushButtonB.setObjectName("pushButtonB")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OPTION"))
        self.pushButtonA.setText(_translate("MainWindow", "Read OPTION"))
        self.pushButtonB.setText(_translate("MainWindow", "Write"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config_data = None

        # Connect button A to the read_binary function
        self.ui.pushButtonA.clicked.connect(self.read_binary)
        self.ui.pushButtonB.clicked.connect(self.write_binary)
        self.ui.tableWidget.cellChanged.connect(self.update_config_data)

    def read_binary(self):
        # Open a file dialog to select the binary file
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setNameFilter("Binary Files (*.bin)")
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)

        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.config_data = read_config_bin(selected_file)
            
            # Define the variable names in the desired order
            variable_order = [
                "ECGCable",
                "bluetooth",
                "spo2",
                "nibp",
                "etco2",
                "energySelectionPaddle",
                "pacer",
                "temp",
                "Version",
                "reserved"
            ]
            
            config_values = get_config_values(self.config_data)

            # Display the values in the table widget
            self.ui.tableWidget.setRowCount(len(variable_order))
            for row, filed in enumerate(variable_order):
                value=next((value for name, value in config_values if name==filed),None)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(filed))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(value)))
    
    def update_config_data(self,row,column):
        item=self.ui.tableWidget.item(row,column)
        field_name=self.ui.tableWidget.item(row,0).text()#filed_name is syserrorcode
        
        if not hasattr(self.config_data, field_name):
            return
        
        try:
            if hasattr(self.config_data,field_name):#syserrorcode in check
                attr_value=getattr(self.config_data,field_name)
               
                if isinstance(attr_value, list):#attr_value type check, is it list?
                    arr_value=item.text().strip("[]").split(",")    #parsing
                    arr_parse=[int(val) for val in arr_value]
                    setattr(self.config_data,field_name,arr_parse)
                    print(f"Updated list {field_name} to {arr_parse}")
                    
                elif isinstance(attr_value, bytes): #and attr_value.typecode=='H':
                    print(f"item.text(): {item.text()}")
                    #arr_value = item.text().strip("[]").split(",")    #parsing
                    arr_value = item.text().replace("array('H', [","").replace("])","").split(",")    #parsing
                    print(f"arr_value:{arr_value}")
                    arr_parse = array('H', [int(val) for val in arr_value])
                    print(f"arr_parse:{arr_parse}")
                    setattr(self.config_data, field_name, arr_parse)
                    print(f"Updated array {field_name} to {arr_parse}")
                
                else:
                    value=int(item.text())
                    setattr(self.config_data,field_name,value)
                    print(f"Updated int {field_name} to {value}")
                    
        except ValueError:
            print(f"Invalid value in cell ({row}, {column}): {item.text()}")
        except Exception as e:
            print(f"An error occurred while updating {field_name}: {e}")  
    
    def write_binary(self):
        if self.config_data is not None:
            file_dialog=QtWidgets.QFileDialog(self)
            file_dialog.setNameFilter("Binary Files (*.bin)")
            file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            
            if file_dialog.exec_():
                selected_file=file_dialog.selectedFiles()[0]
                try:
                    binary_data=pack_config_data(self.config_data)
                    print("Option Data:", self.config_data)
                    print("Packed Binary Data:", binary_data)
                    with open(selected_file,"wb") as file:
                        #binary_data=pack_config_data(self.config_dat a)
                        file.write(binary_data)
                    QtWidgets.QMessageBox.information(self,"Success","OPTION.BIN File Saved")
                except Exception as e:
                    traceback.print_exc()
                    QtWidgets.QMessageBox.critical(self,"Warning",f"Failed to save the file :{e}")
        else:
            QtWidgets.QMessageBox.warning(self,"Warning","No data to save")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
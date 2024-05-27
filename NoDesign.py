import sys
import struct
from PyQt5 import QtCore, QtGui, QtWidgets


class FuncStorageConf: #Strut of C to Class of Python
    def __init__(self):
        self.ulSysErrCode = 0
        self.ulImpUpperLimit = 0
        self.ulImpLowerLimit = 0
        self.ulSelfTestCnt = 0
        self.ulBTDuration = 0 #5I
        self.ulImpLevel = [0] * 15 #15I
        self.ulMSTCnt = 0 #1I
        self.ulSTCounter = [0] * 3 # 3I int
        self.ubAEDCPR_TimeDelay = 0
        self.usMONITOR_HR_High_Limits = 0
        self.usMONITOR_HR_Low_Limits = 0                                                                                                                                                                                                 
        self.usMONITOR_Pulse_High_Limits = 0 
        self.usMONITOR_Pulse_Low_Limits = 0
        self.usMONITOR_AlarmPauseTime = 0
        self.ubPRINTER_ManualModeDuration = 0
        self.uNIBP_SysHighLimits = 0
        self.uNIBP_SysLowLimits = 0
        self.uNIBP_DiaHighLimits = 0
        self.uNIBP_DiaLowLimits = 0
        self.uNIBP_MapHighLimits = 0
        self.uNIBP_MapLowLimits = 0 
        self.usNIBP_Adult_Init=0
        self.usNIBP_Pedi_Init=0
        self.usNIBP_Neo_Init=0 #16H
        self.ubSerialNumber = bytes(12) #12B
        self.STLastDate = bytes(8) #8B
        self.SystemDataVersion = bytes(8) #8B
        self.ubAEDAnalyeOnOff = 0 #65
        self.ubAEDCPR_OnOff = 0
        self.ubAEDCPR_Ratio = 0
        self.ubPACERMode = 0
        self.ubPACERCurrent = 0
        self.ubPACERRate = 0
        self.ubMONITOR_HR_Alarm_OnOff = 0
        self.ubMONITOR_Pulse_Alarm_OnOff = 0
        self.ubMONITOR_SpO2_Alarm_OnOff = 0
        self.ubMONITOR_VF_VT_OnOff = 0
        self.ubMONITOR_SpO2_High_Limits = 0
        self.ubMONITOR_SpO2_Low_Limits = 0
        self.ubMONITOR_AsystoleOnOff=0
        self.ubPRINTER_AutoModeOnOff=0
        self.ubECG_1ch_Lead=0
        self.ubECG_2ch_Lead=0
        self.ubECG_1ch_Gain=0
        self.ubECG_2ch_Gain=0#
        self.ubManyLanguage=0
        self.ubAltLanguage=0
        self.ubLCDDisplayFilterRange=0
        self.ubPrinterFilterRange=0
        self.ubACFilterRange=0
        self.ubDEVICE_VoiceRecOnOff=0
        self.ubDEVICE_VolumeLevel=0
        self.ubDEVICE_QRSOnOff=0
        self.ubAlarmVolumeLevel=0 #27B
        self.reserved=bytes(4) #4B
        self.uNIBP_Mode=0
        self.uNIBP_AutoDuration=0
        self.uNIBP_AlarmOnOff=0
        self.uNIBP_AlarmTarget=0
        self.ubMONITOR_EtCO2_Alarm_OnOff=0
        self.ubMONITOR_EtCO2_High_Limits=0
        self.ubMONITOR_EtCO2_Low_Limits=0
        self.ubMONITOR_AwRR_Alarm_OnOff=0
        self.ubMONITOR_AwRR_High_Limits=0
        self.ubMONITOR_AwRR_Low_Limits=0
        self.ubCO2Unit=0 
        self.ubMONITOR_NoBreath_Time=0 #12B
        self.ubEtCO2MAC=bytes(12) #12B
        self.ubEtCO2NAME=bytes(12) #12B
        self.ubCO2Scale=0
        self.ubCO2SweepSpeed=0
        self.ubPRINTER_PrintSectors=0
        self.ubEtCO2VolHighLimits=0
        self.ubEtCO2VolLowLimits=0
        self.ubECG_1ch_Sweep=0
        self.ubECG_2ch_Sweep=0
        self.ubTemperature_Unit=0
        self.ubEtCO2_PerVolO2=0
        self.ubEtCO2_PerVolN2O=0 #10B
        self.reserved2=bytes(10) #16B
        
def read_config_bin(file_path): 
    # Create an instance of FuncStorageConf to hold the data
    config_data = FuncStorageConf()

    try:
        with open(file_path, "rb") as file:
            # Read the binary data from the file
            binary_data = file.read()

            # Unpack the binary data according to the FUNC_STORAGE_CONF structure
            unpacked_data=struct.unpack("<5I 15I 1I 3I 16H 12B 8B 8B 27B 4B 12B 12B 12B 10B 10B", binary_data) 
    
            # Assign the unpacked data to the corresponding fields in config_data
            config_data.ulSysErrCode = unpacked_data[0]
            config_data.ulImpUpperLimit = unpacked_data[1]
            config_data.ulImpLowerLimit = unpacked_data[2]
            config_data.ulSelfTestCnt = unpacked_data[3]
            config_data.ulBTDuration = unpacked_data[4]
            config_data.ulImpLevel = list(unpacked_data[5:20])
            config_data.ulMSTCnt = unpacked_data[20]
            config_data.ulSTCounter = list(unpacked_data[21:24]) #unsigned int (0~23)
            config_data.ubAEDCPR_TimeDelay = unpacked_data[24]
            config_data.usMONITOR_HR_High_Limits = unpacked_data[25]
            config_data.usMONITOR_HR_Low_Limits = unpacked_data[26]
            config_data.usMONITOR_Pulse_High_Limits = unpacked_data[27]
            config_data.usMONITOR_Pulse_Low_Limits = unpacked_data[28]
            config_data.usMONITOR_AlarmPauseTime = unpacked_data[29]
            config_data.ubPRINTER_ManualModeDuration = unpacked_data[30]
            config_data.uNIBP_SysHighLimits = unpacked_data[31]
            config_data.uNIBP_SysLowLimits = unpacked_data[32]
            config_data.uNIBP_DiaHighLimits = unpacked_data[33]
            config_data.uNIBP_DiaLowLimits = unpacked_data[34]
            config_data.uNIBP_MapHighLimits = unpacked_data[35]
            config_data.uNIBP_MapLowLimits = unpacked_data[36] #unsigned short(24~36)
            config_data.usNIBP_Adult_Init=unpacked_data[37]
            config_data.usNIBP_Pedi_Init=unpacked_data[38]
            config_data.usNIBP_Neo_Init=unpacked_data[39]
            config_data.ubSerialNumber = bytes(unpacked_data[40:52])
            config_data.STLastDate = bytes(unpacked_data[52:60])
            config_data.SystemDataVersion = bytes(unpacked_data[60:68])
            config_data.ubAEDAnalyeOnOff = unpacked_data[68]
            config_data.ubAEDCPR_OnOff = unpacked_data[69]
            config_data.ubAEDCPR_Ratio = unpacked_data[70]
            config_data.ubPACERMode=unpacked_data[71]
            config_data.ubPACERCurrent=unpacked_data[72]
            config_data.ubPACERRate=unpacked_data[73]
            config_data.ubMONITOR_HR_Alarm_OnOff=unpacked_data[74]
            config_data.ubMONITOR_Pulse_Alarm_OnOff=unpacked_data[75]
            config_data.ubMONITOR_SpO2_Alarm_OnOff=unpacked_data[76]
            config_data.ubMONITOR_VF_VT_OnOff=unpacked_data[77]
            config_data.ubMONITOR_SpO2_High_Limits=unpacked_data[78]
            config_data.ubMONITOR_SpO2_Low_Limits=unpacked_data[79]
            config_data.ubMONITOR_AsystoleOnOff=unpacked_data[80]
            config_data.ubPRINTER_AutoModeOnOff=unpacked_data[81]
            config_data.ubECG_1ch_Lead=unpacked_data[82]
            config_data.ubECG_2ch_Lead=unpacked_data[83]
            config_data.ubECG_1ch_Gain=unpacked_data[84]
            config_data.ubECG_2ch_Gain=unpacked_data[85]
            config_data.ubManyLanguage=unpacked_data[86]
            config_data.ubAltLanguage=unpacked_data[87]
            config_data.ubLCDDisplayFilterRange=unpacked_data[88]
            config_data.ubPrinterFilterRange=unpacked_data[89]
            config_data.ubACFilterRange=unpacked_data[90]
            config_data.ubDEVICE_VoiceRecOnOff=unpacked_data[91]
            config_data.ubDEVICE_VolumeLevel=unpacked_data[92]
            config_data.ubDEVICE_QRSOnOff=unpacked_data[93]
            config_data.ubAlarmVolumeLevel=unpacked_data[94]
            config_data.reserved=bytes(unpacked_data[95:99])
            config_data.uNIBP_Mode=unpacked_data[99]
            config_data.uNIBP_AutoDuration=unpacked_data[100]
            config_data.uNIBP_AlarmOnOff=unpacked_data[101]
            config_data.uNIBP_AlarmTarget=unpacked_data[102]
            config_data.ubMONITOR_EtCO2_Alarm_OnOff=unpacked_data[103]
            config_data.ubMONITOR_EtCO2_High_Limits=unpacked_data[104]
            config_data.ubMONITOR_EtCO2_Low_Limits=unpacked_data[105]
            config_data.ubMONITOR_AwRR_Alarm_OnOff=unpacked_data[106]
            config_data.ubMONITOR_AwRR_High_Limits=unpacked_data[107]
            config_data.ubMONITOR_AwRR_Low_Limits=unpacked_data[108]
            config_data.ubCO2Unit=unpacked_data[109]
            config_data.ubMONITOR_NoBreath_Time=unpacked_data[110]
            config_data.ubEtCO2MAC=bytes(unpacked_data[111:123])
            config_data.ubEtCO2NAME=bytes(unpacked_data[123:135])
            config_data.ubCO2Scale=unpacked_data[135]
            config_data.ubCO2SweepSpeed=unpacked_data[136]
            config_data.ubPRINTER_PrintSectors=unpacked_data[137]
            config_data.ubEtCO2VolHighLimits=unpacked_data[138]
            config_data.ubEtCO2VolLowLimits=unpacked_data[139]
            config_data.ubECG_1ch_Sweep=unpacked_data[140]
            config_data.ubECG_2ch_Sweep=unpacked_data[141]
            config_data.ubTemperature_Unit=unpacked_data[142]
            config_data.ubEtCO2_PerVolO2=unpacked_data[143]
            config_data.ubEtCO2_PerVolN2O=unpacked_data[144]
            config_data.reserved2=bytes(unpacked_data[145:155])
            
            
            # Continue assigning the remaining fields...

    except Exception as e:
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
    # Pack the values from the config_data object into binary format
    packed_data = struct.pack(
        "<5I 15I 1I 3I 16H 12B 8B 8B 27B 4B 12B 12B 12B 10B 10B",
        
        config_data.ulSysErrCode,
        config_data.ulImpUpperLimit,
        config_data.ulImpLowerLimit,
        config_data.ulSelfTestCnt,
        config_data.ulBTDuration,
        *config_data.ulImpLevel,
        config_data.ulMSTCnt,
        *config_data.ulSTCounter,
        config_data.ubAEDCPR_TimeDelay,
        config_data.usMONITOR_HR_High_Limits,
        config_data.usMONITOR_HR_Low_Limits,
        config_data.usMONITOR_Pulse_High_Limits,
        config_data.usMONITOR_Pulse_Low_Limits,
        config_data.usMONITOR_AlarmPauseTime,
        config_data.ubPRINTER_ManualModeDuration,
        config_data.uNIBP_SysHighLimits,
        config_data.uNIBP_SysLowLimits,
        config_data.uNIBP_DiaHighLimits,
        config_data.uNIBP_DiaLowLimits,
        config_data.uNIBP_MapHighLimits,
        config_data.uNIBP_MapLowLimits,
        config_data.usNIBP_Adult_Init,
        config_data. usNIBP_Pedi_Init,
        config_data.usNIBP_Neo_Init,
        *config_data.ubSerialNumber,
        *config_data.STLastDate,
        *config_data.SystemDataVersion,
        config_data.ubAEDAnalyeOnOff,
        config_data.ubAEDCPR_OnOff,
        config_data.ubAEDCPR_Ratio,
        config_data.ubPACERMode,
        config_data.ubPACERCurrent,
        config_data.ubPACERRate,
        config_data.ubMONITOR_HR_Alarm_OnOff,
        config_data.ubMONITOR_Pulse_Alarm_OnOff,
        config_data.ubMONITOR_SpO2_Alarm_OnOff,
        config_data.ubMONITOR_VF_VT_OnOff,
        config_data.ubMONITOR_SpO2_High_Limits,
        config_data.ubMONITOR_SpO2_Low_Limits,
        config_data.ubMONITOR_AsystoleOnOff,
        config_data.ubPRINTER_AutoModeOnOff,
        config_data.ubECG_1ch_Lead,
        config_data.ubECG_2ch_Lead,
        config_data.ubECG_1ch_Gain,
        config_data.ubECG_2ch_Gain,
        config_data.ubManyLanguage,
        config_data.ubAltLanguage,
        config_data.ubLCDDisplayFilterRange,
        config_data.ubPrinterFilterRange,
        config_data.ubACFilterRange,
        config_data.ubDEVICE_VoiceRecOnOff,
        config_data.ubDEVICE_VolumeLevel,
        config_data.ubDEVICE_QRSOnOff,
        config_data.ubAlarmVolumeLevel,
        *config_data.reserved,
        config_data.uNIBP_Mode,
        config_data.uNIBP_AutoDuration,
        config_data.uNIBP_AlarmOnOff,
        config_data.uNIBP_AlarmTarget,
        config_data.ubMONITOR_EtCO2_Alarm_OnOff,
        config_data.ubMONITOR_EtCO2_High_Limits,
        config_data.ubMONITOR_EtCO2_Low_Limits,
        config_data.ubMONITOR_AwRR_Alarm_OnOff,
        config_data.ubMONITOR_AwRR_High_Limits,
        config_data.ubMONITOR_AwRR_Low_Limits,
        config_data.ubCO2Unit,
        config_data.ubMONITOR_NoBreath_Time,
        *config_data.ubEtCO2MAC,
        *config_data.ubEtCO2NAME,
        config_data.ubCO2Scale,
        config_data.ubCO2SweepSpeed,
        config_data.ubPRINTER_PrintSectors,
        config_data.ubEtCO2VolHighLimits,
        config_data.ubEtCO2VolLowLimits,
        config_data.ubECG_1ch_Sweep,
        config_data.ubECG_2ch_Sweep,
        config_data.ubTemperature_Unit,
        config_data.ubEtCO2_PerVolO2,
        config_data.ubEtCO2_PerVolN2O,
        *config_data.reserved2
    )
    
   
    return packed_data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Test"))
        self.pushButtonA.setText(_translate("MainWindow", "Read CONFIG"))
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
                "ulSysErrCode", "ulImpUpperLimit", "ulImpLowerLimit", "ulSelfTestCnt", "ulBTDuration",
                "ulImpLevel", "ulMSTCnt", "ulSTCounter", "ubAEDCPR_TimeDelay", "usMONITOR_HR_High_Limits",
                "usMONITOR_HR_Low_Limits", "usMONITOR_Pulse_High_Limits", "usMONITOR_Pulse_Low_Limits",
               "usMONITOR_AlarmPauseTime", "ubPRINTER_ManualModeDuration", "uNIBP_SysHighLimits",
                "uNIBP_SysLowLimits", "uNIBP_DiaHighLimits", "uNIBP_DiaLowLimits", "uNIBP_MapHighLimits",
                "uNIBP_MapLowLimits","usNIBP_Adult_Init","usNIBP_Pedi_Init","usNIBP_Neo_Init",
                "ubSerialNumber","STLastDate","SystemDataVersion","ubAEDAnalyeOnOff",
                "ubAEDCPR_OnOff","ubAEDCPR_Ratio","ubPACERMode","ubPACERCurrent","ubPACERRate",
                "ubMONITOR_HR_Alarm_OnOff","ubMONITOR_Pulse_Alarm_OnOff","ubMONITOR_SpO2_Alarm_OnOff","ubMONITOR_VF_VT_OnOff","ubMONITOR_SpO2_High_Limits",
                "ubMONITOR_SpO2_Low_Limits","ubMONITOR_AsystoleOnOff","ubPRINTER_AutoModeOnOff","ubECG_1ch_Lead","ubECG_2ch_Lead",
                "ubECG_1ch_Gain","ubECG_2ch_Gain","ubManyLanguage","ubAltLanguage","ubLCDDisplayFilterRange",
                "ubPrinterFilterRange","ubACFilterRange","ubDEVICE_VoiceRecOnOff","ubDEVICE_VolumeLevel","ubDEVICE_QRSOnOff",
                "ubAlarmVolumeLevel","reserved","uNIBP_Mode","uNIBP_AutoDuration","uNIBP_AlarmOnOff",
                "uNIBP_AlarmTarget","ubMONITOR_EtCO2_Alarm_OnOff","ubMONITOR_EtCO2_High_Limits","ubMONITOR_EtCO2_Low_Limits","ubMONITOR_AwRR_Alarm_OnOff",
                "ubMONITOR_AwRR_High_Limits","ubMONITOR_AwRR_Low_Limits","ubCO2Unit","ubMONITOR_NoBreath_Time","ubEtCO2MAC",
                "ubEtCO2NAME","ubCO2Scale","ubCO2SweepSpeed","ubPRINTER_PrintSectors","ubEtCO2VolHighLimits",
                "ubEtCO2VolLowLimits","ubECG_1ch_Sweep","ubECG_2ch_Sweep","ubTemperature_Unit","ubEtCO2_PerVolO2",
                "ubEtCO2_PerVolN2O","reserved2"
            ]

            # Get the variable names and their integer values
            config_values = get_config_values(self.config_data)

            # Display the values in the table widget
            self.ui.tableWidget.setRowCount(len(variable_order))
            for row, filed in enumerate(variable_order):
                value=next((value for name, value in config_values if name==filed),None)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(filed))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(value)))
    
    def update_config_data(self,row,column):
        item=self.ui.tableWidget.item(row,column)
        filed_name=self.ui.tableWidget.item(row,0).text()#filed_name is syserrorcode
        
        try:
            if hasattr(self.config_data,filed_name):#syserrorcode in check
                attr_value=getattr(self.config_data,filed_name)#attr_value=config_data.syserrorcode
                
                if isinstance(attr_value, list):#attr_value type check, is it list?
                    arr_value=item.text().strip("[]").split(",")#parsing
                    arr_parse=[int(val) for val in arr_value]
                    setattr(self.config_data,filed_name,arr_parse)
                    print(f"Updated {filed_name} to {arr_parse}")
                else:
                    value=int(item.text())
                    setattr(self.config_data,filed_name,value)
                    print(f"Updated {filed_name} to {value}")
        
        except ValueError:
            print(f"Invalid value in cell : {item.text()}")
            pass
            
    '''def update_config_data(self, row, column):
        item=self.ui.tableWidget.item(row,column)
        #header_item=self.ui.tableWidget.horizontalHeaderItem(column)
        header_item=self.ui.tableWidget.item(row,0).text()
        if header_item is None:
            return
        value_name=header_item
        if value_name not in dir(self.config_data):
            return
        try:
            if value_name=="ulImpLevel" or value_name=="ulSTCounter":
                values=[int(x) for x in item.text().split()]
                setattr(self.config_data,value_name,values)
            else:
                value=int(item.text())
                setattr(self.config_data,value_name,value)
            print(f"Updated {value_name} to {getattr(self.config_data,value_name)}")
        except ValueError:
            print(f"Invalid value in cell: {item.text()}")
            pass'''
    
    
                
    
    def write_binary(self):
        if self.config_data is not None:
            file_dialog=QtWidgets.QFileDialog(self)
            file_dialog.setNameFilter("Binary Files (*.bin)")
            file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            
            if file_dialog.exec_():
                selected_file=file_dialog.selectedFiles()[0]
                try:
                    binary_data=pack_config_data(self.config_data)
                    print("Config Data:", self.config_data)
                    print("Packed Binary Data:", binary_data)
                    with open(selected_file,"wb") as file:
                        #binary_data=pack_config_data(self.config_data)
                        file.write(binary_data)
                    QtWidgets.QMessageBox.information(self,"Success","CONFIG.BIN File Saved")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self,"Warning",f"Failed to save the file :{e}")
        else:
            QtWidgets.QMessageBox.warning(self,"Warning","No data to save")
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    #config_data = read_config_bin("config.bin")

    # Print the data from the config_data object
     #print(f"ulSysErrCode: {config_data.ulSysErrCode}")
     #print(f"ulImpUpperLimit: {config_data.ulImpUpperLimit}")
     #print(f"ulImpLowerLimit: {config_data.ulImpLowerLimit}")
    # ... (print the rest of the fields)
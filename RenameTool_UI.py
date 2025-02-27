import maya.cmds as cm
from PySide6 import QtCore, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
from PySide6.QtGui import QFont
import RenameTool
import sys


def main_Window_UI():
    main_Window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_Window_ptr), QtWidgets.QWidget)


class renameTool(QtWidgets.QDialog):
    dlg_instance = None

    @classmethod
    def show_dialog(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = renameTool()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    def __init__(self, parent=main_Window_UI()):
        super(renameTool, self).__init__(parent)

        self.setWindowTitle("Rename Tool v1.0")
        self.setFixedSize(300, 700)

        # For macOS, it make the window a tool to keep it on top of maya
        if sys.platform == "darwin":
            self.setWindowFlag(Qtcore.Qt.tool, True)

        # Applica lo stile CSS
        self.apply_styles()

        self.create_widget()
        self.create_layout()
        self.create_connection()

    def apply_styles(self):
        """ Applica lo stile CSS alla UI """
        self.setStyleSheet("""

            QDialog {
                background-color: #3C3C3C;
                color: white;
            }  
            QGroupBox {
                background-color: #3C3C3C;
                font-weight: bold;

            }

            QPushButton {
                background-color: #555;

                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #777;

            }
            QLineEdit, QSpinBox {
                background-color: #444;
                color: white;
                border: 1px solid #666;
                border-radius: 5px;
                padding: 3px;    

            }
            QRadioButton {
                color: lightgray;   
            }
        """)

    def create_widget(self):
        """ GB = QGroupBox / LE = QLineEdit / FL = QFormLayout / SB = QSpinBox / BTN = QPushButton

        """
        # Rename

        # Font
        self.font_01 = QFont()

        # LineEDIT / SpinBox / BTN  Settings + FormLayout creation
        self.rename_LE = QtWidgets.QLineEdit()
        self.rename_LE.setFixedHeight(30)
        self.rename_LE.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.rename_FL_01 = QtWidgets.QFormLayout()

        self.rename_SB = QtWidgets.QSpinBox()
        self.rename_SB.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.rename_SB.setFixedWidth(30)
        self.rename_SB.setFixedHeight(30)
        self.rename_SB.setValue(1)
        self.rename_SB.setMinimum(0)
        self.rename_SB.setMaximum(10)

        self.rename_BTN = QtWidgets.QPushButton("Rename")
        self.rename_BTN.setFixedHeight(25)
        self.rename_BTN.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.rename_FL_02 = QtWidgets.QFormLayout()

        # Suffix

        # LineEdit + BTN settings
        self.suff_LE = QtWidgets.QLineEdit()
        self.suff_LE.setFixedHeight(30)
        self.suff_BTN = QtWidgets.QPushButton("Add Suffix")
        self.suff_BTN.setFixedWidth(155)
        self.suff_BTN.setFixedHeight(25)

        # RadioButton settings
        self.suff_RB_01 = QtWidgets.QRadioButton("None")
        self.suff_RB_01.setProperty("suffix", "")
        self.suff_RB_01.setChecked(True)
        self.suff_RB_02 = QtWidgets.QRadioButton("_grp")
        self.suff_RB_02.setProperty("suffix", "_grp")
        self.suff_RB_03 = QtWidgets.QRadioButton("_geo")
        self.suff_RB_03.setProperty("suffix", "_geo")
        self.suff_RB_04 = QtWidgets.QRadioButton("_ctrl")
        self.suff_RB_04.setProperty("suffix", "_ctrl")

        self.suff_RB_05 = QtWidgets.QRadioButton("_jnt")
        self.suff_RB_05.setProperty("suffix", "_jnt")
        self.suff_RB_06 = QtWidgets.QRadioButton("_ik")
        self.suff_RB_06.setProperty("suffix", "_ik")
        self.suff_RB_07 = QtWidgets.QRadioButton("_fk")
        self.suff_RB_07.setProperty("suffix", "_fk")
        self.suff_RB_08 = QtWidgets.QRadioButton("_offset")
        self.suff_RB_08.setProperty("suffix", "_offset")

        self.suff_RB_09 = QtWidgets.QRadioButton("LineEdit First")
        self.suff_RB_09.setChecked(True)
        self.suff_RB_10 = QtWidgets.QRadioButton("Preset First")

        # Creating buttonGroups
        self.group_RB_01 = QtWidgets.QButtonGroup()
        self.group_RB_01.addButton(self.suff_RB_01)
        self.group_RB_01.addButton(self.suff_RB_02)
        self.group_RB_01.addButton(self.suff_RB_03)
        self.group_RB_01.addButton(self.suff_RB_04)
        self.group_RB_01.addButton(self.suff_RB_05)
        self.group_RB_01.addButton(self.suff_RB_06)
        self.group_RB_01.addButton(self.suff_RB_07)
        self.group_RB_01.addButton(self.suff_RB_08)

        self.group_RB_02 = QtWidgets.QButtonGroup()
        self.group_RB_02.addButton(self.suff_RB_09)
        self.group_RB_02.addButton(self.suff_RB_10)

        # Prefix

        # LineEdit + BTN Settings
        self.pref_LE = QtWidgets.QLineEdit()
        self.pref_LE.setFixedHeight(30)
        self.pref_BTN = QtWidgets.QPushButton("Add Prefix")
        self.pref_BTN.setFixedWidth(155)
        self.pref_BTN.setFixedHeight(25)

        # RadioButton Settings
        self.pref_RB_01 = QtWidgets.QRadioButton("None")
        self.pref_RB_01.setChecked(True)
        self.pref_RB_01.setProperty("prefix", "")

        self.pref_RB_02 = QtWidgets.QRadioButton("L_")
        self.pref_RB_02.setProperty("prefix", "L_")

        self.pref_RB_03 = QtWidgets.QRadioButton("R_")
        self.pref_RB_03.setProperty("prefix", "R_")
        self.pref_RB_04 = QtWidgets.QRadioButton("C_")
        self.pref_RB_04.setProperty("prefix", "C_")
        self.pref_RB_05 = QtWidgets.QRadioButton("ik_")
        self.pref_RB_05.setProperty("prefix", "ik_")
        self.pref_RB_06 = QtWidgets.QRadioButton("fk_")
        self.pref_RB_06.setProperty("prefix", "fk_")
        self.pref_RB_07 = QtWidgets.QRadioButton("jnt_")
        self.pref_RB_07.setProperty("prefix", "jnt_")
        self.pref_RB_08 = QtWidgets.QRadioButton("ctrl_")
        self.pref_RB_08.setProperty("prefix", "ctrl_")

        self.pref_RB_09 = QtWidgets.QRadioButton("LineEdit First")
        self.pref_RB_09.setChecked(True)
        self.pref_RB_10 = QtWidgets.QRadioButton("Preset First")

        # Creating buttonGroups
        self.group_RB_03 = QtWidgets.QButtonGroup()
        self.group_RB_03.addButton(self.pref_RB_01)
        self.group_RB_03.addButton(self.pref_RB_02)
        self.group_RB_03.addButton(self.pref_RB_03)
        self.group_RB_03.addButton(self.pref_RB_04)
        self.group_RB_03.addButton(self.pref_RB_05)
        self.group_RB_03.addButton(self.pref_RB_06)
        self.group_RB_03.addButton(self.pref_RB_07)
        self.group_RB_03.addButton(self.pref_RB_08)

        self.group_RB_04 = QtWidgets.QButtonGroup()
        self.group_RB_04.addButton(self.pref_RB_09)
        self.group_RB_04.addButton(self.pref_RB_10)

        # Remove Characters

        # Remove Characters BTN + SB settings
        self.rmv_GB = QtWidgets.QGroupBox("Remove Characters")

        self.rmv_FL = QtWidgets.QFormLayout()
        self.rmv_SB = QtWidgets.QSpinBox()
        self.rmv_SB.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.rmv_SB.setFixedWidth(30)
        self.rmv_SB.setFixedHeight(30)
        self.rmv_SB.setValue(1)
        self.rmv_SB.setMinimum(1)
        self.rmv_SB.setMaximum(10)

        self.rmv_BTN_01 = QtWidgets.QPushButton("First Character")
        self.rmv_BTN_01.setFixedWidth(155)
        self.rmv_BTN_01.setFixedHeight(25)
        self.rmv_BTN_02 = QtWidgets.QPushButton("Last Character")
        self.rmv_BTN_02.setFixedWidth(155)
        self.rmv_BTN_02.setFixedHeight(25)

        self.rmv_LBL = QtWidgets.QLabel("Remove 'X'\nCharacter")

        # Select & Replace

        # Select & Replace GroupBox
        self.slcRpl_GB = QtWidgets.QGroupBox("Select & Replace")

        # Select & Replace layouts
        self.slcRpl_VB = QtWidgets.QVBoxLayout()
        self.slcRpl_HB_01 = QtWidgets.QHBoxLayout()
        self.slcRpl_HB_02 = QtWidgets.QHBoxLayout()

        self.slcRpl_FL_01 = QtWidgets.QFormLayout()
        self.slcRpl_FL_02 = QtWidgets.QFormLayout()

        # Select & Replace BTN + RB + LE
        self.slcRpl_BTN_01 = QtWidgets.QPushButton("S")
        self.slcRpl_BTN_01.setFixedWidth(40)
        self.slcRpl_BTN_01.setFixedHeight(25)
        self.slcRpl_BTN_02 = QtWidgets.QPushButton("R")
        self.slcRpl_BTN_02.setFixedWidth(40)
        self.slcRpl_BTN_02.setFixedHeight(25)
        self.slcRpl_LE_01 = QtWidgets.QLineEdit()
        self.slcRpl_LE_02 = QtWidgets.QLineEdit()

    def create_layout(self):

        # Rename
        self.rename_VB = QtWidgets.QVBoxLayout()
        self.rename_HB_01 = QtWidgets.QHBoxLayout()

        self.rename_GB = QtWidgets.QGroupBox("Rename")

        self.rename_FL_01.addRow("Rename Selected", self.rename_LE)
        self.rename_HB_01.addLayout(self.rename_FL_01)

        self.rename_HB_02 = QtWidgets.QHBoxLayout()
        self.rename_HB_02.addWidget(self.rename_SB)
        self.rename_HB_02.addWidget(self.rename_BTN)
        self.rename_FL_02.addRow("Padding", self.rename_HB_02)

        self.rename_VB.addLayout(self.rename_HB_01)
        self.rename_VB.addLayout(self.rename_FL_02)

        self.rename_GB.setLayout(self.rename_VB)

        # Font Rename

        # "Rename" text in groupBox
        self.rename_GB.setStyleSheet(f"QGroupBox {{ font-size: 15px; }}")

        # "Rename Selected" text in FormLayout_01
        label_01 = self.rename_FL_01.itemAt(0, QtWidgets.QFormLayout.LabelRole).widget()
        label_01.setStyleSheet("font-size: 14px")

        # "Padding" write in FormLayout_02
        label_02 = self.rename_FL_02.itemAt(0, QtWidgets.QFormLayout.LabelRole).widget()
        label_02.setStyleSheet("font-size: 14px")

        # Font size in: number in spinbox / "Rename" text in BTN / Text inside LineEdit
        self.rename_SB.setStyleSheet("QSpinBox { font-size: 14px; }")
        self.rename_BTN.setStyleSheet("font-size: 14px")
        self.rename_LE.setStyleSheet("font-size: 11pt")

        # Suffix

        # create Layouts
        self.suff_VB_01 = QtWidgets.QVBoxLayout()
        self.suff_VB_02 = QtWidgets.QVBoxLayout()
        self.suff_VB_03 = QtWidgets.QVBoxLayout()
        self.suff_HB_01 = QtWidgets.QHBoxLayout()
        self.suff_HB_02 = QtWidgets.QHBoxLayout()
        self.suff_HB_03 = QtWidgets.QHBoxLayout()

        self.suff_GB = QtWidgets.QGroupBox("Suffix")

        # VB_01 LineEDIT + BTN / VB_02 RB "Preset/LineEdit First"
        self.suff_VB_01.addWidget(self.suff_LE)
        self.suff_VB_01.addWidget(self.suff_BTN)
        self.suff_VB_02.addWidget(self.suff_RB_09)
        self.suff_VB_02.addWidget(self.suff_RB_10)

        # HB_02 HB_03 RB Preset
        self.suff_HB_02.addWidget(self.suff_RB_01)
        self.suff_HB_02.addWidget(self.suff_RB_02)
        self.suff_HB_02.addWidget(self.suff_RB_03)
        self.suff_HB_02.addWidget(self.suff_RB_04)

        self.suff_HB_03.addWidget(self.suff_RB_05)
        self.suff_HB_03.addWidget(self.suff_RB_06)
        self.suff_HB_03.addWidget(self.suff_RB_07)
        self.suff_HB_03.addWidget(self.suff_RB_08)

        # addLayout
        self.suff_HB_01.addLayout(self.suff_VB_02)
        self.suff_HB_01.addLayout(self.suff_VB_01)

        self.suff_VB_03.addLayout(self.suff_HB_01)
        self.suff_VB_03.addLayout(self.suff_HB_02)
        self.suff_VB_03.addLayout(self.suff_HB_03)

        # suffix GroupBox
        self.suff_GB.setLayout(self.suff_VB_03)

        # Font Suffix

        # font size in: "Suffix" text in GroupBox / "add Suffix" BTN / text inside LineEdit
        self.suff_GB.setStyleSheet(f"QGroupBox {{ font-size: 15px; }}")
        self.suff_BTN.setStyleSheet("font-size: 14px;")
        self.suff_LE.setStyleSheet("font-size: 11pt;")

        # Prefix

        # GroupBox
        self.pref_GB = QtWidgets.QGroupBox("Prefix")

        # Prefix Layouts
        self.pref_VB_01 = QtWidgets.QVBoxLayout()
        self.pref_VB_02 = QtWidgets.QVBoxLayout()
        self.pref_VB_03 = QtWidgets.QVBoxLayout()
        self.pref_VB_04 = QtWidgets.QVBoxLayout()
        self.pref_HB_01 = QtWidgets.QHBoxLayout()
        self.pref_HB_02 = QtWidgets.QHBoxLayout()
        self.pref_HB_03 = QtWidgets.QHBoxLayout()

        self.pref_VB_01.addWidget(self.pref_RB_09)
        self.pref_VB_01.addWidget(self.pref_RB_10)

        self.pref_VB_02.addWidget(self.pref_LE)
        self.pref_VB_02.addWidget(self.pref_BTN)

        self.pref_HB_02.addWidget(self.pref_RB_01)
        self.pref_HB_02.addWidget(self.pref_RB_02)
        self.pref_HB_02.addWidget(self.pref_RB_03)
        self.pref_HB_02.addWidget(self.pref_RB_04)

        self.pref_HB_03.addWidget(self.pref_RB_05)
        self.pref_HB_03.addWidget(self.pref_RB_06)
        self.pref_HB_03.addWidget(self.pref_RB_07)
        self.pref_HB_03.addWidget(self.pref_RB_08)

        self.pref_HB_01.addLayout(self.pref_VB_01)
        self.pref_HB_01.addLayout(self.pref_VB_02)

        self.pref_VB_03.addLayout(self.pref_HB_02)
        self.pref_VB_03.addLayout(self.pref_HB_03)

        self.pref_VB_04.addLayout(self.pref_HB_01)
        self.pref_VB_04.addLayout(self.pref_VB_03)

        self.pref_GB.setLayout(self.pref_VB_04)

        # Font Prefix
        self.pref_GB.setStyleSheet(f"QGroupBox {{ font-size: 15px; }}")
        self.pref_BTN.setStyleSheet("font-size: 14px;")
        self.pref_LE.setStyleSheet("font-size: 11pt;")

        # Remove Characters

        # Remove Layouts
        self.rmv_HB_01 = QtWidgets.QHBoxLayout()
        self.rmv_HB_02 = QtWidgets.QHBoxLayout()
        self.rmv_VB_01 = QtWidgets.QVBoxLayout()
        self.rmv_VB_02 = QtWidgets.QVBoxLayout()

        self.rmv_HB_01.addWidget(self.rmv_LBL)
        self.rmv_HB_01.addWidget(self.rmv_SB)
        self.rmv_HB_01.addStretch()

        self.rmv_VB_01.addWidget(self.rmv_BTN_01)
        self.rmv_VB_01.addWidget(self.rmv_BTN_02)
        self.rmv_HB_02.addLayout(self.rmv_HB_01)
        self.rmv_HB_02.addLayout(self.rmv_VB_01)
        self.rmv_HB_02.addLayout(self.rmv_VB_01)

        self.rmv_GB.setLayout(self.rmv_HB_02)

        # Font Characters
        self.rmv_GB.setStyleSheet(f"QGroupBox {{ font-size: 15px; }}")
        self.rmv_BTN_01.setStyleSheet("font-size: 13px;")
        self.rmv_BTN_02.setStyleSheet("font-size: 13px;")
        self.rmv_LBL.setStyleSheet("font-size: 12px;")
        self.rmv_SB.setStyleSheet("QSpinBox { font-size: 14px; }")

        # Select & Replace

        # Select & Replace Layouts

        self.slcRpl_FL_01.addRow("Select   ", self.slcRpl_LE_01)
        self.slcRpl_FL_02.addRow("Replace", self.slcRpl_LE_02)

        self.slcRpl_HB_01.addLayout(self.slcRpl_FL_01)
        self.slcRpl_HB_01.addWidget(self.slcRpl_BTN_01)
        self.slcRpl_HB_02.addLayout(self.slcRpl_FL_02)
        self.slcRpl_HB_02.addWidget(self.slcRpl_BTN_02)

        self.slcRpl_VB.addLayout(self.slcRpl_HB_01)
        self.slcRpl_VB.addLayout(self.slcRpl_HB_02)

        # Select & Replace GB
        self.slcRpl_GB.setLayout(self.slcRpl_VB)

        # Select & Replace Font

        self.slcRpl_GB.setStyleSheet(f"QGroupBox {{font-size: 15px;}}")

        label_03 = self.slcRpl_FL_01.itemAt(0, QtWidgets.QFormLayout.LabelRole).widget()
        label_03.setStyleSheet("font-size: 14px")

        label_04 = self.slcRpl_FL_02.itemAt(0, QtWidgets.QFormLayout.LabelRole).widget()
        label_04.setStyleSheet("font-size: 14px")

        self.slcRpl_BTN_01.setStyleSheet("font-size: 14px")
        self.slcRpl_BTN_02.setStyleSheet("font-size: 14px")

        self.slcRpl_LE_01.setStyleSheet("font-size: 11pt")
        self.slcRpl_LE_02.setStyleSheet("font-size: 11pt")

        # Main Layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.rename_GB)

        main_layout.addWidget(self.suff_GB)

        main_layout.addWidget(self.pref_GB)

        main_layout.addWidget(self.rmv_GB)

        main_layout.addWidget(self.slcRpl_GB)
        main_layout.addStretch()

    def create_connection(self):
        self.rename_BTN.clicked.connect(self.rename_action)
        self.suff_BTN.clicked.connect(self.suffix_action)
        self.pref_BTN.clicked.connect(self.prefix_action)
        self.rmv_BTN_01.clicked.connect(self.remove_action)
        self.rmv_BTN_02.clicked.connect(self.remove_action)
        self.slcRpl_BTN_01.clicked.connect(self.slc_Action)
        self.slcRpl_BTN_02.clicked.connect(self.Rpl_Action)

    def rename_action(self):
        padding_num = self.rename_SB.value()
        text = self.rename_LE.text()
        RenameTool.rename_selected_meshes(text, padding_num)

    def suffix_action(self):

        lineFirst = self.suff_RB_09.isChecked()
        text = self.suff_LE.text()

        selected_RB = self.group_RB_01.checkedButton()
        if self.suff_RB_01.isChecked() and text == "":
            cm.warning("Type a valid suffix or select a preset")
            return

        if selected_RB:
            selected_suffix = selected_RB.property("suffix")
            RenameTool.add_suffix(selected_suffix, text, lineFirst)

    def prefix_action(self):
        lineFirst = self.pref_RB_09.isChecked()
        text = self.pref_LE.text()

        selected_RB = self.group_RB_03.checkedButton()
        if self.pref_RB_01.isChecked() and text == "":
            cm.warning("Type a valid Prefix or select a preset")
            return

        if selected_RB:
            selected_prefix = selected_RB.property("prefix")
            RenameTool.add_prefix(selected_prefix, text, lineFirst)

    def remove_action(self):
        sender = self.sender()
        first_chr = True
        remove_chr_num = self.rmv_SB.value()

        if not sender == self.rmv_BTN_01:
            first_chr = False

        RenameTool.remove_characters(remove_chr_num, first_chr)

    def slc_Action(self):

        selected_text = self.slcRpl_LE_01.text()
        RenameTool.slc_text(selected_text)

    def Rpl_Action(self):

        select_text = self.slcRpl_LE_01.text()
        replace_text = self.slcRpl_LE_02.text()
        RenameTool.Rpl_text(select_text, replace_text)


if __name__ == "__main__":

    try:
        rename_tool_dialog.close()
        rename_tool_dialog.deleteLater()
    except:
        pass

    rename_tool_dialog = renameTool()
    rename_tool_dialog.show()


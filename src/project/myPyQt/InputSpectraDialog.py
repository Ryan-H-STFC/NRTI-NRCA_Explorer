from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QVBoxLayout
)
from project.myPyQt.ExtendedComboBox import ExtendedComboBox


class InputSpectraDialog(QDialog):

    def __init__(self, parent=None, styleSheet: str = None) -> None:
        super(InputSpectraDialog, self).__init__(parent)
        self.setObjectName('inputWindow')
        if styleSheet is None:
            self.setStyleSheet("""
            *{
                font-family: 'Roboto Mono';
                font-size: 10pt;
                font-weight: 400;
            }
            #inputWindow{
                color: #FFF;
                background-color: #393939;
            }
            #inputWindow QLabel{
                color: #FFF;
            }
            """)

        self.mainLayout = QVBoxLayout()
        self.inputForm = QFormLayout()

        self.inputForm.setObjectName('inputForm')

        self.spectras = ExtendedComboBox()

        self.buttonBox = QDialogButtonBox()

        self.mainLayout.addWidget(self.spectras)
        self.mainLayout.addWidget(self.buttonBox)
        self.setUpdatesEnabled(True)

        self.motionEvent = None
        self.buttonPressEvent = None
        self.tof = None
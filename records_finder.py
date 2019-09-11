#! source /Users/cqoverly/Envs/pyqt5/bin/activate python3
from PyQt5 import QtPrintSupport, QtGui

from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout, QWidget, QApplication, QLabel, QDateEdit, QFormLayout, QDialog, QLineEdit, QTableWidgetItem, QAbstractItemView, QDialog, QTextEdit, QFrame, QFileDialog

import os
import logging

import search_logic as sl


logging.basicConfig(level=os.environ.get('LOGLEVEL', 'DEBUG'))
log = logging.getLogger('main_logger')
log.info("STARTING APPLICATION")

class MainWindow(QMainWindow):
    '''
        Main Window Docs
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.windowTitle = 'Sales Tracker'
        self.resize(700, 500)
        main_frame = MainManager()
        self.setCentralWidget(main_frame)
        
        self.show()
        log.info('MainWindow initialized')

    # def resizeEvent(self, event): # Only needed to find window size parameters
    #     log.info(f'WINDOW RESIZED: {self.size()}')
    #     return super().resizeEvent(event)



class MainManager(QWidget):
    '''
        MainManager Docs
    '''



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.search_numbers = []
        self.report = 'NONE'

        # Create a main container
        # container_layout = QHBoxLayout()

        # Set up section to enter student numbers to search for.
        student_entry_layout = QVBoxLayout()
        numbers_label = QLabel('Student numbers for search:')
        self.entry_textbox = QTextEdit()
        self.entry_textbox.setMaximumWidth(200)
        self.entry_textbox.setFontPointSize(10)
        number_enter_button = QPushButton('Enter Numbers')
        number_enter_button.setFixedWidth(150)
        number_enter_button.clicked.connect(self.enter_numbers)

        student_entry_layout.addWidget(numbers_label)
        student_entry_layout.addWidget(self.entry_textbox)
        student_entry_layout.addWidget(number_enter_button)


        # Layout area to act as container for report selection and search
        # numbers
        report_layout = QVBoxLayout()

        # Set up section to select a report to search
        search_layout = QVBoxLayout()
        self.search_label = QLabel(self.report)
        self.recs_to_search = QLabel('')
        self.recs_found = QLabel('')
        search_button = QPushButton('Select Report')
        search_button.clicked.connect(self.get_report)
        search_button.setMaximumWidth(200)
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.recs_to_search)
        search_layout.addWidget(self.recs_found)
        search_layout.addWidget(search_button)

        # Set up section to display 


        # Set up start search button / reset search button layout
        start_reset_buttons_layout = QHBoxLayout()
        self.start_button = QPushButton('Start Search', enabled=False)
        self.start_button.setMaximumWidth(200)
        self.start_button.clicked.connect(self.run_search)
        start_reset_buttons_layout.addWidget(self.start_button)
        reset_button = QPushButton('Reset Search')
        reset_button.setMaximumWidth(150)
        reset_button.clicked.connect(self.reset_search)
        start_reset_buttons_layout.addWidget(reset_button)

        report_layout.addLayout(search_layout)
        report_layout.addLayout(start_reset_buttons_layout)

        layout_frame = QHBoxLayout()
        layout_frame.addLayout(student_entry_layout)
        layout_frame.addLayout(report_layout)
        # layout_frame.addLayout(entries_layout)
        self.setLayout(layout_frame)

        log.info('main_manager initialized.')

    def enter_numbers(self):
        text = self.entry_textbox.toPlainText()
        self.entry_textbox.setText(text)
        print(text)
        self.search_numbers = [n for n in text.split()]
        # print(self.search_numbers)
        if self.report != 'NONE':
            self.start_button.setEnabled(True)

    def get_report(self):
        print("Find Report")
        self.report = QFileDialog.getOpenFileName(self,
            "Open CSV", os.environ['HOME'], "CSV Files (*.csv)")[0] 
        print(self.report)
        self.search_label.setText(self.report)
        self.search_label.update()
        self.start_button.setEnabled(True)

    def run_search(self):
        number_of_found = sl.finder_main(self.search_numbers, self.report)
        self.recs_to_search.setText(f'Searched for {len(self.search_numbers)} students')
        self.recs_found.setText(f'Found {number_of_found} matching records.')
        


    def reset_search(self):
        self.search_numbers = []
        self.report = 'NONE'
        self.entry_textbox.clear()
        self.search_label.setText(self.report)
        self.start_button.setEnabled(False)
        self.recs_to_search.setText('')
        self.recs_to_search.setText('')




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
import sys
import requests
import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox, QTextEdit, QCheckBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fsociety DDoS GUI")
        self.setGeometry(200, 200, 600, 700)  # Tambah tinggi agar layout lebih proporsional

        self.setStyleSheet("background-color: black; color: white;")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Tambahkan spacer agar gambar lebih ke tengah
        layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tambahkan Gambar Latar Belakang di tengah
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.load_image("https://a.top4top.io/p_3347i1gqq1.jpeg")
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Spacer di bawah gambar agar tidak terlalu dekat dengan teks
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.log_output)

        self.url_label = QLabel("Target URL:")
        layout.addWidget(self.url_label)
        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.requests_label = QLabel("Number of Requests:")
        layout.addWidget(self.requests_label)
        self.requests_input = QLineEdit()
        layout.addWidget(self.requests_input)

        self.stealth_mode = QCheckBox("Enable Stealth Mode")
        layout.addWidget(self.stealth_mode)

        self.use_proxy = QCheckBox("Enable Proxy (Auto Fetch)")
        layout.addWidget(self.use_proxy)

        self.start_button = QPushButton("Start Attack")
        self.start_button.setStyleSheet("background-color: red; color: white;")
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Attack")
        self.stop_button.setStyleSheet("background-color: grey; color: white;")
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)

        # Tambahkan spacer di bawah tombol agar GUI lebih seimbang
        layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        central_widget.setLayout(layout)

    def load_image(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(response.content).getvalue())
            scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
        except Exception as e:
            print(f"Error loading image: {e}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

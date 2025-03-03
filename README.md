🌍 [English](README_ENGLISH.md) | 🇮🇩 [Bahasa Indonesia](README.md)
---
# Fsociety DDoS GUI DAN NON GUI ( Termux )

Fsociety DDoS GUI adalah aplikasi untuk melakukan serangan DDoS (Distributed Denial of Service) sederhana menggunakan PyQt5 sebagai antarmuka grafis (GUI) dan Requests untuk mengirim permintaan HTTP ke target. Aplikasi ini memungkinkan pengguna untuk mengkonfigurasi jumlah permintaan, mode stealth, serta penggunaan proxy, dan menampilkan log serangan di GUI.

## DEVELOPER : PYSCODES
-------------------------
## SCREENSHOOT   
![2025-03-02_04-38](https://github.com/user-attachments/assets/7f16ac9e-2f46-4977-9ec2-faa4e9de809f) ,![2025-03-04_03-49](https://github.com/user-attachments/assets/4cb58720-109e-4944-a5b9-b24cc45fc403)



## Fitur 🚀

- **Serangan DDoS**: Mengirim permintaan HTTP ke URL target secara berulang 🌐.
- **Stealth Mode**: Menggunakan header `User-Agent` yang berbeda untuk mengurangi deteksi 🕵️‍♂️.
- **Proxy**: Opsi untuk menggunakan proxy secara otomatis 🌍.
- **Log Serangan**: Menampilkan status serangan, termasuk jumlah request yang berhasil atau gagal, di GUI 📜.

## Prasyarat ⚙️

Aplikasi ini mendukung berbagai sistem operasi dan memerlukan beberapa dependensi Python yang perlu diinstal terlebih dahulu.

### Dukungan Sistem Operasi 💻

- **Windows**: Aplikasi ini sepenuhnya mendukung Windows 10/11.
- **Linux**: Aplikasi ini dapat dijalankan di distribusi Linux seperti Ubuntu, Kali Linux, dan lainnya.
- **macOS**: Aplikasi ini dapat dijalankan pada macOS dengan Python 3.x.
-- **termux** ( pakai yang non gui )
### Dependensi yang Dibutuhkan 📦

- **Python 3.x**: Pastikan Python versi 3 sudah terinstal di sistem Anda.
- **PyQt5**: Digunakan untuk antarmuka grafis.
- **Requests**: Digunakan untuk mengirim permintaan HTTP.

## Cara Penginstalan 🔧

### Di Windows 🖥️

1. **Instal Python**:
   Unduh dan pasang Python 3.x dari [situs resmi Python](https://www.python.org/downloads/) 🐍.
   
2. **Clone repositori**:
   Buka Command Prompt dan jalankan perintah berikut:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   
   ```bash
   python Fsociety-Ddos.py
   ```

### Di Linux 🐧

1. **Instal Python**:
   
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Clone repositori**:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   
   ```bash
   python3 Fsociety-Ddos.py
   ```

### Di macOS 🍏

1. **Instal Python**:
   
   ```bash
   brew install python
   ```

2. **Clone repositori**:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   
   ```bash
   python3 Fsociety-Ddos.py
   ```

----------------
## REQUEST TEST 
![2025-03-02_04-28](https://github.com/user-attachments/assets/c8bc32d5-a35e-4708-94ba-94807d32efdd)

## Penggunaan 🛠️

1. Masukkan URL target pada kolom **Target URL** 🌐.
2. Masukkan jumlah permintaan yang ingin dikirim pada kolom **Number of Requests** 👖.
3. Pilih **Enable Stealth Mode** untuk menggunakan mode stealth 🕶️.
4. Pilih **Enable Proxy (Auto Fetch)** jika ingin menggunakan proxy secara otomatis 🌍.
5. Klik **Start Attack** untuk memulai serangan 🚀.
6. Klik **Stop Attack** untuk menghentikan serangan ✋.

## Pengembangan 💡

Jika Anda ingin mengembangkan aplikasi ini lebih lanjut, Anda bisa melakukan fork dan pull request. Beberapa ide untuk pengembangan lebih lanjut:
- Menambahkan fitur untuk bypass Cloudflare dan proteksi lainnya 🔒.
- Menambahkan sistem logging untuk menyimpan hasil serangan ke file 🗂️.
- Menambahkan opsi untuk memilih jenis serangan (misalnya, HTTP GET atau POST) ⚔️.

## Lisensi 📝

Aplikasi ini dilisensikan di bawah lisensi MIT - lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

## **Kontak** 📞

Jika Anda mengalami masalah atau membutuhkan bantuan, Anda bisa menghubungi kami melalui:

- **Email**: [pyscodes@mail2tor.com](mailto:pyscodes@mail2tor.com)
- **GitHub Issues**: [Laporan Masalah atau Bug](https://github.com/username/fsociety-ddos-gui/issues)
- **Instagram**: [@pyscodesl](https://instagram.com/pyscodes)

Kami siap membantu Anda! ✨


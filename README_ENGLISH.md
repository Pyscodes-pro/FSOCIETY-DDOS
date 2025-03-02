# Fsociety DDoS GUI

Fsociety DDoS GUI is an application for performing simple Distributed Denial of Service (DDoS) attacks using PyQt5 as a graphical user interface (GUI) and Requests to send HTTP requests to the target. This application allows users to configure the number of requests, stealth mode, proxy usage, and display attack logs in the GUI.

## DEVELOPER: PYSCODES

## Features 🚀

- **DDoS Attack**: Sends HTTP requests to the target URL repeatedly 🌐.
- **Stealth Mode**: Uses different `User-Agent` headers to reduce detection 🕵️‍♂️.
- **Proxy**: Option to use proxies automatically 🌍.
- **Attack Logs**: Displays attack status, including successful or failed request counts, in the GUI 📜.

## Prerequisites ⚙️

This application supports multiple operating systems and requires some Python dependencies to be installed first.

### Supported Operating Systems 💻

- **Windows**: Fully supports Windows 10/11.
- **Linux**: Can run on Linux distributions such as Ubuntu, Kali Linux, and others.
- **macOS**: Runs on macOS with Python 3.x.

### Required Dependencies 📦

- **Python 3.x**: Ensure Python version 3 is installed on your system.
- **PyQt5**: Used for the graphical interface.
- **Requests**: Used to send HTTP requests.

## Installation Guide 🔧

### On Windows 🖥️

1. **Install Python**:
   Download and install Python 3.x from [Python Official Website](https://www.python.org/downloads/) 🐍.
   
2. **Clone the repository**:
   Open Command Prompt and run the following commands:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Install dependencies**:
   
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the application**:
   
   ```bash
   python Fsociety-Ddos.py
   ```

### On Linux 🐧

1. **Install Python**:
   
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Clone the repository**:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Install dependencies**:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the application**:
   
   ```bash
   python3 Fsociety-Ddos.py
   ```

### On macOS 🍏

1. **Install Python**:
   
   ```bash
   brew install python
   ```

2. **Clone the repository**:
   
   ```bash
   git clone https://github.com/username/fsociety-ddos-gui.git
   cd fsociety-ddos-gui
   ```

3. **Install dependencies**:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the application**:
   
   ```bash
   python3 Fsociety-Ddos.py
   ```

## Usage 🛠️

1. Enter the target URL in the **Target URL** field 🌍.
2. Enter the number of requests to be sent in the **Number of Requests** field 🔢.
3. Select **Enable Stealth Mode** to activate stealth mode 🕶️.
4. Select **Enable Proxy (Auto Fetch)** if you want to use a proxy automatically 🌍.
5. Click **Start Attack** to start the attack 🚀.
6. Click **Stop Attack** to stop the attack ✋.

## Development 💡

If you want to further develop this application, you can fork and submit pull requests. Some ideas for further development:
- Adding features to bypass Cloudflare and other protections 🔒.
- Implementing a logging system to store attack results in a file 🗂️.
- Adding options to choose attack types (e.g., HTTP GET or POST) ⚔️.

## License 📝

This application is licensed under the MIT license - see the [LICENSE](LICENSE) file for more details.

## **Contact** 📞

If you encounter issues or need assistance, you can contact us through:

- **Email**: [pyscodes@mail2tor.com](mailto:pyscodes@mail2tor.com)
- **GitHub Issues**: [Report Issues or Bugs](https://github.com/username/fsociety-ddos-gui/issues)
- **Instagram**: [@pyscodesl](https://instagram.com/pyscodes)

We are ready to help you! ✨

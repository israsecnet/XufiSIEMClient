# XufiSIEMClient

XufiSIEMClient is a Python application that is meant to serve as a custom log extractor, an EDR agent, provide the capability for incident response functions and remote administration. These clients can be configured with [this](https://github.com/israsecnet/CRMSIEMSERVER) custom server.

## Features

- Collects various system logs
- Sends logs to an API server using JSON format
- Easy to configure and integrate into existing systems
- Remote administration capabilities
- Set up Canary Files (Ransomware Protection)
- Schedule file scans
- Detect registry changes

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/israsecnet/XufiSIEMClient.git
   ```
3. Navigate to the project directory:
  ```
  cd XufiSIEMClient
  ```
3. Install Dependencies
  ```
  pip install -r requirements.txt 
  ``` 
4. Run setup.py and configure settings
  ```
   python3 setup.py
  ```
5. Verify installation
   Reboot the device and verify health check pings are being sent to server.

## Contact

If you have any questions or need assistance, feel free to [contact me](mailto:raizn@proton.me).

---

Enjoy using XufiClient!

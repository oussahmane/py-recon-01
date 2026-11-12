
# PY-RECON-01

**Basic TCP Port Scanner**

My first practical cybersecurity project, developed using Python on Kali Linux.

A lightweight TCP port scanner designed to identify open ports on a target host and display their associated service names.

## Features

- TCP port scanning
- Custom target IP address
- Configurable port range (currently set in source code)
- Open port detection
- Basic service name lookup
- Connection timeout handling
- Keyboard interruption handling

## Technologies

- Python 3
- Socket
- Datetime
- Kali Linux

## Requirements

- Python 3.x
- Linux, Windows, or macOS

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/oussahmane/py-recon-01.git
```

Navigate to the project directory:

```bash
cd py-recon-01
```

## Usage

Run the scanner:

```bash
python scanner.py
```

Enter the target IP address when prompted.

The current version scans TCP ports 11430–11440.

## Example Output

```text
TARGET: 127.0.0.1
PORT RANGE: 11430-11440

[+] Port 11434 OPEN | Service: Unknown

SCAN COMPLETED
Open ports found: 1
```

## Project Structure

```text
py-recon-01/
├── scanner.py
├── README.md
└── .gitignore
```

## Learning Objectives

- Understanding TCP connections
- Learning socket programming in Python
- Understanding port scanning
- Identifying open network services
- Practicing basic network reconnaissance

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

Only scan systems that you own or have explicit permission to test.

## Author

**Oussama Abderrahmane**

GitHub: [@oussahmane](https://github.com/oussahmane)

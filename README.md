
# PY-RECON-01

## PyRecon – Python TCP Port Scanner

PyRecon is a lightweight TCP port scanner developed in Python for network reconnaissance and authorized security testing.

The project started as a basic socket programming exercise and evolved into a multithreaded scanner capable of scanning the complete TCP port range (1–65535).

## Current Version

**v1.2.0**

## Features

- Full TCP port scanning (1–65535)
- Custom port ranges
- Individual port selection
- Multithreaded scanning
- Configurable connection timeout
- Configurable concurrent workers
- Open port detection
- Conventional TCP service name lookup
- Scan progress indicator
- Scan duration reporting
- Input validation and error handling
- IPv4 target and hostname support

## Technologies

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Argparse
- IP Address Validation

## Requirements

- Python 3.9+
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

### Display help

```bash
python scanner.py --help
```

### Scan all TCP ports

```bash
python scanner.py -t 127.0.0.1
```

### Scan a specific port range

```bash
python scanner.py -t 127.0.0.1 -p 1-1024
```

### Scan selected ports

```bash
python scanner.py -t 127.0.0.1 -p 22,80,443
```

### Customize timeout

```bash
python scanner.py -t 127.0.0.1 -T 1
```

### Customize concurrent workers

```bash
python scanner.py -t 127.0.0.1 -w 100
```

### Full scan with custom settings

```bash
python scanner.py -t 127.0.0.1 -p 1-65535 -w 100 -T 0.5
```

## Example Output

```text
============================================================
                 PYRECON v1.2.0
                 TCP PORT SCANNER
============================================================
Target       : 127.0.0.1
Ports        : 65535
Workers      : 100
Timeout      : 0.5s
============================================================
Progress: 65535/65535

============================================================
                  SCAN RESULTS
============================================================
[+] 11434   OPEN | Service: Unknown
------------------------------------------------------------
Open ports     : 1
Ports checked  : 65535/65535
Duration       : 3.77 seconds
============================================================
```

## Validation

PyRecon was tested against Nmap using a full TCP scan of localhost.

| Scanner | Open Ports |
|---|---|
| PyRecon v1.2.0 | 11434 |
| Nmap | 11434 |

Both scanners identified the same open TCP port during testing.

## Project Structure

```text
py-recon-01/
├── scanner.py
├── README.md
└── .gitignore
```

## Learning Objectives

- Understanding TCP/IP networking
- Learning Python socket programming
- Understanding TCP port scanning
- Working with concurrent execution
- Handling network connections and timeouts
- Understanding service identification
- Comparing custom security tools with established tools

## Roadmap

- [x] v1.0.0 – Basic TCP port scanner
- [x] v1.1.0 – Full port scanning and multithreading
- [x] v1.2.0 – Improved scanning accuracy and input validation
- [ ] v1.3.0 – Service detection and TCP banner grabbing
- [ ] v1.4.0 – JSON and HTML report generation
- [ ] v2.0.0 – Network reconnaissance features

## Disclaimer

PyRecon is developed for educational purposes and authorized security testing only.

Only scan systems and networks that you own or have explicit permission to test.

The author is not responsible for misuse of this tool.

## Author

**Oussama Abderrahmane**

GitHub: [@oussahmane](https://github.com/oussahmane)

Repository: [py-recon-01](https://github.com/oussahmane/py-recon-01)

---

Developed with Python on Kali Linux.

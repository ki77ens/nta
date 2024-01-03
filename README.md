# Network Traffic Analyzer

This script utilizes Scapy, a powerful packet manipulation library, to capture network packets and log essential packet details such as Ethernet source and destination, IP addresses, and TCP/UDP ports. The logged information helps in analyzing network traffic and diagnosing issues.

## Features

- **Packet Details Logging:** Captures Ethernet, IP, TCP, and UDP packet information.
- **Flexible Interface Specification:** Users can specify the network interface to monitor.
- **Logging to File:** Saves captured packet details in a log file for later analysis.

## Usage

### Prerequisites
- Python 3
- `Scapy` library (Install using `pip install scapy`)

### Running the Script

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ki77ens/nta.git
    ```

2. **Execute the Script:**

    ```bash
    python main.py
    ```

4. **View the Logs:**
    - Once the script starts running, it will capture and log packet details to a file named `pd.log`.

## Why Use This Script?

- **Network Analysis:** Gain insights into network traffic patterns and diagnose potential issues.
- **Troubleshooting:** Helpful for diagnosing connectivity problems or identifying suspicious network activities.
- **Learning & Experimentation:** Understand packet structures and network protocols by examining captured data.

### Note:

- Running this script might require administrative privileges (especially on certain operating systems) due to its nature of capturing network packets.

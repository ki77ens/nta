from scapy.all import sniff, Ether, IP, TCP, UDP
import logging

logger = logging.getLogger("scapy")
logger.setLevel(logging.CRITICAL)
file_handler = logging.FileHandler('pd.log') 
file_handler.setLevel(logging.CRITICAL)  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def packet_callback(packet):
    try:
        eth_src = packet[Ether].src
        eth_dst = packet[Ether].dst
        logger.critical(f"Ethernet Source: {eth_src}, Destination: {eth_dst}")
    except IndexError:
        pass

    try:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        logger.critical(f"IP Source: {ip_src}, Destination: {ip_dst}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            logger.critical(f"TCP Source Port: {src_port}, Destination Port: {dst_port}")
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            logger.critical(f"UDP Source Port: {src_port}, Destination Port: {dst_port}")

        logger.critical(f'Packet Data: {packet}')
        packet_str = packet.show(dump=True)
        logger.critical(f'\n{packet_str}')

    except IndexError:
        pass

sniff(iface='Wi-Fi', prn=packet_callback, count=10)
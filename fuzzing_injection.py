from scapy.all import IP, TCP, fuzz, send, Raw, wrpcap

server_ip = "172.18.0.3"
server_port = 80

fuzzed_packets = []

print("[*] Realizando primera inyección con fuzzing TCP...")


packet1 = IP(dst=server_ip)/fuzz(TCP(dport=server_port))
fuzzed_packets.append(packet1)
send(packet1)
print("[+] Paquete 1 enviado")


malformed_http = Raw(load="GET /" + "A"*1000 + " HTTP/1.1\r\nHost: ServidorN2\r\n\r\n")
packet2 = IP(dst=server_ip)/TCP(dport=server_port, flags="PA")/malformed_http
fuzzed_packets.append(packet2)
send(packet2)
print("[+] Paquete 2 enviado")


pcap_file = "fuzzed_packets.pcap"
wrpcap(pcap_file, fuzzed_packets)
print(f"[+] Paquetes guardados en {pcap_file}")


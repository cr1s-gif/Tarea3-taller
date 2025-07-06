from scapy.all import IP, TCP, Raw, send, wrpcap

server_ip = "172.18.0.3"
server_port = 80
packets = []


pkt1 = IP(dst=server_ip)/TCP(dport=server_port, flags="FUP")
packets.append(pkt1)
send(pkt1)
print("[1] TCP con flags FIN+URG+PSH enviado")


pkt2 = IP(dst=server_ip)/TCP(dport=server_port, seq=4294967295, flags="S") 
packets.append(pkt2)
send(pkt2)
print("[2] TCP con seq inválido enviado")


http_payload = Raw(load="GET / HTTP/1.1\r\nHost: \r\n\r\n") 
pkt3 = IP(dst=server_ip)/TCP(dport=server_port, flags="PA")/http_payload
packets.append(pkt3)
send(pkt3)
print("[3] HTTP con Host inválido enviado")


wrpcap("modificacion_paquetes.pcap", packets)
print("[+] Todos los paquetes guardados en modificacion_paquetes.pcap")

import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(("enp0s3", 0))
	#la tarjeta de red utilizada

ethernet   = b'\x52\x54\x00\x12\x35\x02' # MAC Address Destination
ethernet  += b'\x08\x00\x27\xC4\xEE\x0C' # MAC Address Source
ethernet  += b'\x08\x00'		  # Protocol-Type: IPv4

ip_header  = b'\x45\x00\x00\x1C'	# Version, IHL, Type of service | Total Length
ip_header += b'\xab\xcd\x00\x00'	# Identification | Flags, Fragment Offset	
ip_header += b'\x40\x01\x90\xBD'	# TTL, Protocol | Header Checksum
ip_header += b'\x0A\x00\x02\x0F'	# Source Address
ip_header += b'\x5B\x8E\xD6\xB9'	# Destination Address

icmp_header  = b'\x08\x00\xE5\xCA'	# Type of message, Code | Checksum
icmp_header += b'\x12\x34\x00\x01'	# Identifier | Sequence Number

packet = ethernet + ip_header + icmp_header
s.send(packet)

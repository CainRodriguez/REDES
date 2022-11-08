import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(("enp0s3", 0))
	#la tarjeta de red utilizada

ethernet   = b'\x52\x54\x00\x12\x35\x02' # MAC Address Destination
ethernet  += b'\x08\x00\x27\xC4\xEE\x0C' # MAC Address Source
ethernet  += b'\x08\x00'		  # Protocol-Type: IPv4

ip_header  = b'\x45\x00\x00\x28'	# Version, IHL, Type of service | Total Length
ip_header += b'\xab\xcd\x00\x00'	# Identification | Flags, Fragment Offset	
ip_header += b'\x02\x06\xCE\xAC'	# TTL, Protocol | Header Checksum
ip_header += b'\x0A\x00\x02\x0F'	# Source Address
ip_header += b'\x5B\x8E\xD6\xB9'	# Destination Address

tcp_header   = b'\x30\x39\x00\x50'	# Source Port | Destination Port
tcp_header  += b'\x00\x00\x00\x00'	# Sequence number
tcp_header  += b'\x00\x00\x00\x00'	# Acknowledgement Number
tcp_header  += b'\x50\x02\x71\x10'	# Data Offset, Rserved, Flags | Window Size
tcp_header  += b'\xCF\xF2\x00\x00'	# Checksum | Urgent Pointer

packet = ethernet + ip_header + tcp_header
s.send(packet)

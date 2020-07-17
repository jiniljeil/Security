from socket import *
import os
import struct 

# ipheader Component
# [0] Version + Header Length
# [1] Service Type
# [2] Entire Packet Length 
# [3] Datagram ID
# [4] Flag + Fragment Offset
# [5] TTL (Time to Live)
# [6] Protocol
# [7] Header Checksum
# [8] Source IP Address
# [9] Destination IP Address 

def parse_ipheader(data):
    ipheader = struct.unpack('!BBHHHBBH4s4s', data[:20])
    return ipheader
# ! : order of Network bytes (SIZE -)
# B : unsigned char (SIZE 1)
# H : unsigned short (SIZE 2)
# 4s : char[4] (SIZE 4)

def getDatagram(ipheader): # get the ip datagram size 
    return str(ipheader[2])

def getProtocol(ipheader):
    protocols = {1: 'ICMP', 6: 'TCP' , 17: 'UDP'}
    proto = ipheader[6]
    if proto in protocols:
        return protocols[proto]
    else:
        return 'OHTERS'

def getIP(ipheader):
    send_ip = inet_ntoa(ipheader[8])
    des_ip = inet_ntoa(ipheader[9])
    return send_ip, des_ip

def getIPHeaderLen(ipheader):
    ipheaderlen = ipheader[0] & 0x0F
    ipheaderlen *= 4
    return ipheaderlen # icmp header start section

def getTypeCode(icmp):
    icmpheader = struct.unpack('!BB', icmp[:2])
    icmp_type = icmpheader[0]
    icmp_code = icmpheader[1]
    return icmp_type, icmp_code

def recvData(sock):
    data = ''
    try:
        data = sock.recvfrom(65565)
    except timeout:
        data = ''
    return data[0]


def sniffing(host):
    if os.name == 'nt': # window 
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    
    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    if os.name == 'nt': # window
        sniffer.ioctl(SIO_RCVALL, RCVALL_ON)

    count = 1
    try:
        # if you want to receive the field data, use the unpack() 
        while True:
            data = recvData(sniffer)
            ipheader = parse_ipheader(data[:20])
            datagramSize = getDatagram(ipheader)
            protocol = getProtocol(ipheader)
            send_ip, des_ip = getIP(ipheader)
            ipheaderlen = getIPHeaderLen(ipheader)

            if protocol == 'ICMP':
                offset = ipheaderlen
                icmp_type, icmp_code = getTypeCode(data[offset:])
                print('%s -> %s: ICMP: Type[%d], Code[%d]' %(send_ip, des_ip, icmp_type, icmp_code))

            print('\nSNIFFED [%d] ++++++++++++++++' %count)
            print('Datagram SIZE:\t%s' %str(datagramSize))
            print('Protocol:\t%s' %protocol)
            print('Source IP:\t%s' %send_ip)
            print('Destination IP:\t%s' %des_ip)
            print("%s" %(data[:20])) # 20 bytes (ip header)

            count += 1
    except KeyboardInterrupt:
        if os.name == 'nt':
            sniffer.ioctl(SIO_RCVALL, RCVALL_ON)

    # packet = sniffer.recvfrom(65565)
    # print(packet)

    # if os.name == 'nt': # window
    #     sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)

def main():
    host = gethostbyname(gethostname()) #  # "127.0.0.1"
    print('START SNIFFING at [%s]' %host)
    sniffing(host)

if __name__ == '__main__':
    main()

ip_addr = raw_input("Please Enter the IP address:")
ip_addr_octets = ip_addr.split('.')
#print ip_addr_octets
first_3_octets = ip_addr_octets[0:3]
first_3_octets.append('0')
network_number = '.'.join(first_3_octets)
first_octet_binary = bin(int(first_3_octets[0]))
first_octet_hex = hex(int(first_3_octets[0]))
print '\n\n'
print '%20s %20s %20s' % ('NETWORK_NUMBER' , 'FIRST_OCTET_BINARY' ,'FIRST_OCTET_HEX')
print '%10s %20s %20s' % (network_number,first_octet_binary,first_octet_hex)

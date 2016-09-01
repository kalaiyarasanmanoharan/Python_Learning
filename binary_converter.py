
import sys
print ('you have entered IP address',sys.argv[1])
ip_addr = sys.argv[1]
ip_addr_octets = ip_addr.split('.')
first_octet_bin = bin(int(ip_addr_octets[0]))
second_octet_bin = bin(int(ip_addr_octets[1]))
third_octet_bin = bin(int(ip_addr_octets[2]))
fourth_octet_bin = bin(int(ip_addr_octets[3]))
print '\n\n'
print 'Provided IP address: %s' %ip_addr
print 'converted Binary Results are below\n'
print '%20s %20s %20s %20s' % ('first_octet' , 'second_octet' ,'third_octet','fourth_octet')
print '%20s %20s %20s %20s' % (first_octet_bin,second_octet_bin,third_octet_bin,fourth_octet_bin)

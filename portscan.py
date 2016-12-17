import socket
import sys


# Thes scan() function accepts an IP and port. Then attempts to connect 
# using IPV4, sock_stream. If the ports open it will print open. If there's a socket error
# it will stay silent (socket error usually means the port is closed).
def scan(host,port): 
    isopen=False

    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((host,int(port)))
        sock.close()
 


        
        isopen=True
    except socket.error, e:
        isopen=False
       

    if isopen:
        print '[+] %s:%s - Open' % (host,str(port))


# Get command-line args, saves the host's and port's as a list.
def get_args():
    try:
        host=[sys.argv[1]]
        port=[sys.argv[2]]
    except:
        print '\n Usage :'
        print '       python portscan.py host_range port_range\n\n'
        print '       host_range - 127.0.0.1 - 127.0.0.1-200 (for range)'
        print '       host_range - domain.co.uk\n\n'
        print '       port_range - 443 - 21-80 (for range)\n'
	
        exit()
       
 
    ip_range=False
    ip_format=False
    port_range=False

    # If host is IP and a address range, loop through the subnet and add to list  
    if '-' in host[0] and '/' not in host[0]:
        ip_range=host[0].strip().split('.')[3].split('-')
        ip_format=host[0].strip().split('-')[0]
        ip_format=ip_format.split('.')
        ip_format='%s.%s.%s.***' % (ip_format[0],ip_format[1],ip_format[2])
       
        
        host=[]
        count=int(ip_range[0])
        while count!=int(ip_range[1])+1:
            host=host+[(ip_format.replace('***',str(count)))]
            count+=1

    # If port is an address range, loop through port range and add to list                 
    if '-' in port[0]:
        port_range=port[0].strip().split('-')

    else:
	print '\n[!] Port range not specified, using 0-1000 as default'
        port_range=['0','1000']

    if ',' in port[0]:
	port_range=port[0].strip().split(',')

    port=[]
    count=int(port_range[0])
    while count!=int(port_range[1])+1:
        port=port+[str(count)]
        count+=1
    
    return host,port 
   
    

def main():
    hosts,ports=get_args();
    
    for host in hosts:
        print '\n[+] Scanning %s' % (host)
        for port in ports:
            scan(host,int(port));
            
      
  

main();

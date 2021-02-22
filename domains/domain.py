import socket
import requests

class inet():
	def getip(host):
    
		hostname = socket.gethostbyname(host)
		return hostname
    
	def getports(host, ports, conntype):
    
		if conntype == "tcp":
			sock = socket.socket(socket.AF_INET, SOCK_STREAM)
			for port in range(0, ports):
				hostname = socket.gethostbyname(str(host))
				try:
					sock.connect((str(hostname), port))
					print("Port is open")
				except:
					print("Port is closed or filtered")
                
        
		elif conntype == "udp":
			sock = socket.socket(socket.AF_INET, SOCK_DGRAM)
			for port in range(0, ports):
				hostname = socket.gethostbyname(str(host))
				try:
					sock.connect((str(hostname), port))
					print("Port is open")
				except:
					print("Port is closed or filtered")
                

class vulnscan():
    # OWASP TOP 10
	def xss():
     
		return 0

	def broken_auth():
    	
		return 0	
    
	def sde():
    
		return 0	
    	
	def xxe():
    
		return 0	
    
	def security_misconf():
    
		return 0	
    	
	def inscr_dsrlz():
   
		return 0	
    	
	def ucwkv():
    
		return 0	
    	 
	def ilm():
     
		return 0     

	def sql_i():
	
		return 0
		
	def broken_accs_ctrl():
		
		return 0
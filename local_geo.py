#!/usr/bin/env python3

import sys
import os
import geoip2.database

reader = geoip2.database.Reader('path_to_db') # load db once

def main():
	fd = sys.argv[1]
	
	if not os.path.isfile(fd):
		print("[!] File path {} does not exist. Exiting...".format(fd))
		sys.exit()
	
	with open(fd) as fp:
		for line in fp:
			geo_ip(line)
			
	reader.close() # close db

def geo_ip(line):
	ip = line.strip('\n') # strip newline for valid ip	
	# try and catch... so we can deal with errors
	try:
		response = reader.city(ip)
		print("'{}',{},{}".format(ip,response.country.name,response.city.name)) # print ip, country, and city
	except Exception:
		pass
		
if __name__ == '__main__':
	main()

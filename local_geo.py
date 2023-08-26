#!/usr/bin/env python3

import sys
import os
import geoip2.database

import argparse
import logging
import logging.config

reader = geoip2.database.Reader("path_to_db") # load db once

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", type=str)
	parser.add_argument("-o", "--output", type=str)
	parser.add_argument("-lf", "--logfile", type=str)

	args = parser.parse_args()

	ips_fd = args.input
	output_fd = args.output
	log_fd = args.logfile

	if not log_fd:
		print("Specify the log file")
		parser.print_help()
		sys.exit(1)
	else:
		# Create and configure logger
		logging.basicConfig(filename=log_fd,
                    format='%(asctime)s %(message)s',
                    filemode='w')

	# Creating an object
	logger = logging.getLogger()

	if not ips_fd:
		logger.error("No file with IPs provided")
		print("Error: Check log file")
		parser.print_help()
		sys.exit(1)
	
	if not os.path.isfile(ips_fd):
		logger.critical("[!] File path {} does not exist. Exiting...".format(ips_fd))
		sys.exit(1)
	
	with open(ips_fd) as fp:
		for line in fp:
			geo_ip(line, output_fd, logger)
			
	reader.close() # close db

def geo_ip(line, output_fd, logger):
	ip = line.strip('\n') # strip newline for valid ip	
	# try and catch... so we can deal with errors
	fd = open(output_fd, "a")

	try:
		response = reader.city(ip)
		fd.write("'{}',{},{}\n".format(ip,response.country.name,response.city.name))
	except Exception as error:
		logger.warning("[!] Warning: {}".format(error))
		pass
	fd.close()
		
if __name__ == '__main__':
	main()

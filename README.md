# local_geolocation_ips
A small python script written to take advantage of the maxmind db to get location from ip address.

You can get the db here: https://www.maxmind.com/en/home

and once you create an account or login, just download the db and add the path to the line `reader = geoip2.database.Reader("path_to_db") # load db once`. The db is updated often so you should get into the habit of downloading the db from the site.

Usage:

`usage: local_geo.py [-h] [-i INPUT] [-o OUTPUT] [-lf LOGFILE]`

Example:

`python3 local_geo.py -i <list_of_ips_file> -o <output_file> -lf <log_file>`

Help:

```
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
  -o OUTPUT, --output OUTPUT
  -lf LOGFILE, --logfile LOGFILE
```

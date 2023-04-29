# local_geolocation_ips
A small python script written to take advantage of the maxmind db to get location from ip address.

You can get the db here: https://www.maxmind.com/en/home

and once you create an account or login, just download the db. The db is updated often so you should get into the habit of downloading the db from the site. You then just run the program as: python3 local_geo.py <list_of_ips> and combine this with grep you can narrow down the geo location of ips.

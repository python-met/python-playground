import os
import urllib.request

# define save location. ONLY TESTED W/ LINUX
if os.name == "posix":
    save_dir = '/usr/share'
else:
    save_dir = 'C:\\Program Files\\web-file.py'



# read weather data
# weather data from `darksky.net`
link = "https://api.darksky.net/forecast/c428e6fd3d89c3012007b147625db5d2/37.8267,-122.4233"

with urllib.request.urlopen(link) as url:
    web_contents = url.read()

# print the contents
print(web_contents)

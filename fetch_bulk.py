'''Run this script to initialize the database from tt server.'''

# System
import requests
import json

# Application
import constants
import manage_db

manage_db.create_table()

# URL = "https://tt.safecast.org/devices?template={\"when_captured\":\"\",\"device_urn\":\"\",\"device_sn\":\"\",\"device\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"env_temp\":0.0,\"lnd_7318c\":\"\",\"lnd_7318u\":0.0,\"lnd_7128ec\":\"\",\"pms_pm02_5\":\"\",\"bat_voltage\":\"\",\"dev_temp\":0.0}"
# URL =  "https://tt.safecast.org/devices?template={\"device_urn\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"device_sn\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"device_contact_name\":\"\",\"device_contact_email\":\"\",\"device\":0,\"when_captured\":\"\",\"env_temp\":0.0,\"env_humid\":0.0,\"env_press\":0.0,\"bat_voltage\":0.0,\"lnd_7318c\":0.0,\"lnd_7318u\":0.0,\"lnd_7128ec\":0.0,\"pms_pm02_5\":0.0,\"pms_aqi\":0.0,\"dev_temp\":0.0,\"dev_orientation\":\"\",\"dev_dashboard\":\"\"}"
# URL =  'https://tt.safecast.org/devices?template={"device_urn":"","loc_name":"","loc_country":"","device_sn":"","loc_lat":0.0,"loc_lon":0.0,"device_contact_name":"","device_contact_email":"","device":0,"when_captured":"","env_temp":0.0,"env_humid":0.0,"env_press":0.0,"bat_voltage":0.0,"lnd_7318c":0.0,"lnd_7318u":0.0,"lnd_7128ec":0.0,"pms_pm02_5":0.0,"pms_aqi":0.0,"dev_temp":0.0,"dev_orientation":"","dev_dashboard":""}'
URL = constants.URL

req = requests.get(URL)
print(req.ok)
# with open("stuff.json", "w", enc="utf-8") as outfile:      
    # print(req.json(), file=outfile)
records = req.json()
devices = []
ndevices = 0
# print(json.dumps(records[0]))

for rec in records:
    target = rec['device_urn']
    if not target in devices:
        devices.append(target)
        ndevices += 1
        manage_db.insert_data(rec)

print(f'number devices = {ndevices}')



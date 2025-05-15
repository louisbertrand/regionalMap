import requests
import manage_db

manage_db.create_table()

URL = "https://tt.safecast.org/devices?template={\"when_captured\":\"\",\"device_urn\":\"\",\"device_sn\":\"\",\"device\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"env_temp\":0.0,\"lnd_7318c\":\"\",\"lnd_7318u\":0.0,\"lnd_7128ec\":\"\",\"pms_pm02_5\":\"\",\"bat_voltage\":\"\",\"dev_temp\":0.0}"
req = requests.get(URL)
print(req.ok)
# with open("stuff.json", "w", enc="utf-8") as outfile:      
    # print(req.json(), file=outfile)
json = req.json()
devices = []
ndevices = 0
skipped = []
nskipped = 0
duped = []
print(json[0])

for j in json:
    target = j['device_urn']
    if not target in devices:
        devices.append(target)
        ndevices += 1
    else:
        skipped.append(target)
        nskipped += 1
    if target == 65000:
        duped.append(j)
    manage_db.insert_data(j)

print(devices)
print(skipped)
print(f'number devices = {ndevices}; skipped = {nskipped}')
print(duped)



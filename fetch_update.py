import requests
import manage_db

manage_db.create_table()

URL = "https://tt.safecast.org/devices?template={\"when_captured\":\"\",\"device_urn\":\"\",\"device_sn\":\"\",\"device\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"env_temp\":0.0,\"lnd_7318c\":\"\",\"lnd_7318u\":0.0,\"lnd_7128ec\":\"\",\"pms_pm02_5\":\"\",\"bat_voltage\":\"\",\"dev_temp\":0.0}"
req = requests.get(URL)
if not req.ok:
    print("Error refreshing the database. Exiting...")
    exit(0)
json = req.json()

for j in json:
    nrows = manage_db.update_data(j)
print(f'{nrows} updated.')


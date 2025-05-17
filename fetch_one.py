import requests
import json
# import manage_db

LOOK_FOR = "geigiecast:63209"

# URL = "https://tt.safecast.org/devices?template={\"when_captured\":\"\",\"device_urn\":\"\",\"device_sn\":\"\",\"device\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"env_temp\":0.0,\"lnd_7318c\":\"\",\"lnd_7318u\":0.0,\"lnd_7128ec\":\"\",\"pms_pm02_5\":\"\",\"bat_voltage\":\"\",\"dev_temp\":0.0}"

URL =  "https://tt.safecast.org/devices?template={\"device_urn\":\"\",\"loc_name\":\"\",\"loc_country\":\"\",\"device_sn\":\"\",\"loc_lat\":0.0,\"loc_lon\":0.0,\"device_contact_name\":\"\",\"device_contact_email\":\"\",\"device\":0,\"when_captured\":\"\",\"env_temp\":0.0,\"env_humid\":0.0,\"env_press\":0.0,\"bat_voltage\":0.0,\"lnd_7318c\":0.0,\"lnd_7318u\":0.0,\"pms_pm02_5\":0.0,\"pms_aqi\":0.0,\"dev_temp\":0.0,\"dev_orientation\":\"\",\"dev_dashboard\":\"\"}"

req = requests.get(URL)
if req.ok:
    for j in req.json():
        if j['device_urn'] == LOOK_FOR:
            print(json.dumps(j))


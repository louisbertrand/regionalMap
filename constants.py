"""Constants used by regionalMap application."""

URL =  'https://tt.safecast.org/devices?template={"device_urn":"","loc_name":"","loc_country":"","device_sn":"","loc_lat":0.0,"loc_lon":0.0,"device_contact_name":"","device_contact_email":"","device":0,"when_captured":"","env_temp":0.0,"env_humid":0.0,"env_press":0.0,"bat_voltage":0.0,"lnd_7318c":0.0,"lnd_7318u":0.0,"lnd_7128ec":0.0,"pms_pm02_5":0.0,"pms_aqi":0.0,"dev_temp":0.0,"dev_orientation":"","dev_dashboard":""}'
DB_URN = "measurements.sqlite"  # Local file or remote URN

if __name__ == "__main__":
    print("You must import this file as a module.")

import sqlite3

def create_table():
    sql_create = '''
        -- Create the table if it doesn't exist,
        -- and ensure 'when_captured' allows NULL
        CREATE TABLE IF NOT EXISTS measurements (
            device_urn VARCHAR PRIMARY KEY,
            when_captured TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            bat_voltage FLOAT,
            dev_dashboard VARCHAR,
            dev_orientation VARCHAR,
            dev_temp FLOAT,
            device VARCHAR,
            device_contact_email VARCHAR,
            device_contact_name VARCHAR,
            device_sn VARCHAR,
            env_humid FLOAT,
            env_press FLOAT,
            env_temp FLOAT,
            lnd_7318c FLOAT,
            lnd_7318u FLOAT,
            lnd_7128ec FLOAT,
            loc_country VARCHAR,
            loc_lat FLOAT,
            loc_lon FLOAT,
            loc_name VARCHAR,
            pms_aqi FLOAT,
            pms_pm02_5 FLOAT,
            device_filename VARCHAR
        );
        '''
    with sqlite3.connect("measurements.sqlite") as conn:
        curs = conn.cursor()
        curs.execute(sql_create)
        conn.commit()

def insert_data(rec):
    '''Insert a JSON record into the table.'''
    sql_insert = '''
        -- Insert data ignoring duplicates based on device_urn and when_captured
        INSERT OR IGNORE INTO measurements (
          device_urn,
          when_captured,
            bat_voltage,
            dev_dashboard,
            dev_orientation,
            dev_temp,
            device,
            device_contact_email,
            device_contact_name,
            device_sn,
            env_humid,
            env_press,
            env_temp,
            lnd_7318c,
            lnd_7318u,
            lnd_7128ec,
            loc_country,
            loc_lat,
            loc_lon,
            loc_name,
            pms_aqi,
            pms_pm02_5,
          device_filename
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
    with sqlite3.connect("measurements.sqlite") as conn:
        curs = conn.cursor()
        device_filename = f"{rec['device_urn']}.json"

        curs.execute(sql_insert,
                     (rec['device_urn'],
                        rec['when_captured'],
                        rec['bat_voltage'],
                        rec['dev_dashboard'],
                        rec['dev_orientation'],
                        rec['dev_temp'],
                        rec['device'],
                        rec['device_contact_email'],
                        rec['device_contact_name'],
                        rec['device_sn'],
                        rec['env_humid'],
                        rec['env_press'],
                        rec['env_temp'],
                        rec['lnd_7318c'],
                        rec['lnd_7318u'],
                        rec['lnd_7128ec'],
                        rec['loc_country'],
                        rec['loc_lat'],
                        rec['loc_lon'],
                        rec['loc_name'],
                        rec['pms_aqi'],
                        rec['pms_pm02_5'],
                        device_filename
                    ))
        conn.commit()
    return

def update_data(rec):
    '''Update the table with the latest.'''
    sql_update = '''
        -- Update data if when_captured is newer
        UPDATE measurements SET 
          device_urn = ?,
          when_captured = ?,
            bat_voltage = ?,
            dev_dashboard = ?,
            dev_orientation = ?,
            dev_temp = ?,
            device = ?,
            device_contact_email = ?,
            device_contact_name = ?,
            device_sn = ?,
            env_humid = ?,
            env_press = ?,
            env_temp = ?,
            lnd_7318c = ?,
            lnd_7318u = ?,
            lnd_7128ec = ?,
            loc_country = ?,
            loc_lat = ?,
            loc_lon = ?,
            loc_name = ?,
            pms_aqi = ?,
            pms_pm02_5 = ?
        WHERE device_urn = ? AND timediff(?, when_captured) > 0;
        '''
    with sqlite3.connect("measurements.sqlite") as conn:
        curs = conn.cursor()
        device_filename = f"{rec['device_urn']}.json"

        curs.execute(sql_update,
                    (rec['device_urn'],
                    rec['when_captured'],
                    rec['bat_voltage'],
                    rec['dev_dashboard'],
                    rec['dev_orientation'],
                    rec['dev_temp'],
                    rec['device'],
                    rec['device_contact_email'],
                    rec['device_contact_name'],
                    rec['device_sn'],
                    rec['env_humid'],
                    rec['env_press'],
                    rec['env_temp'],
                    rec['lnd_7318c'],
                    rec['lnd_7318u'],
                    rec['lnd_7128ec'],
                    rec['loc_country'],
                    rec['loc_lat'],
                    rec['loc_lon'],
                    rec['loc_name'],
                    rec['pms_aqi'],
                    rec['pms_pm02_5'],
                    rec['device_urn'], # In WHERE clause
                    rec['when_captured']
                    ))
        nrows = curs.rowcount
        conn.commit()
    return nrows


if __name__ == "__main__":
    create_table()

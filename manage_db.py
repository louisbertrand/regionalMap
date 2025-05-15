import sqlite3

def create_table():
    sql_create = '''
        -- Create the table if it doesn't exist, and ensure 'when_captured' allows NULL
        CREATE TABLE IF NOT EXISTS measurements (
          device_urn VARCHAR PRIMARY KEY,
          when_captured TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          device_sn VARCHAR,
          device VARCHAR,
          loc_name VARCHAR,
          loc_country VARCHAR,
          loc_lat FLOAT,
          loc_lon FLOAT,
          env_temp FLOAT,
          lnd_7318c VARCHAR,
          lnd_7318u FLOAT,
          lnd_7128ec VARCHAR,
          pms_pm02_5 VARCHAR,
          bat_voltage FLOAT,
          dev_temp FLOAT,
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
          device_sn,
          device,
          loc_name,
          loc_country,
          loc_lat,
          loc_lon,
          env_temp,
          lnd_7318c,
          lnd_7318u,
          lnd_7128ec,
          pms_pm02_5,
          bat_voltage,
          dev_temp,
          device_filename
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
    with sqlite3.connect("measurements.sqlite") as conn:
        curs = conn.cursor()
        device_filename = f"{rec['device_urn']}.json"

        curs.execute(sql_insert,
                     (rec['device_urn'],
                        rec['when_captured'],
                        rec['device_sn'],
                        rec['device'],
                        rec['loc_name'],
                        rec['loc_country'],
                        rec['loc_lat'],
                        rec['loc_lon'],
                        rec['env_temp'],
                        rec['lnd_7318c'],
                        rec['lnd_7318u'],
                        rec['lnd_7128ec'],
                        rec['pms_pm02_5'],
                        rec['bat_voltage'],
                        rec['dev_temp'],
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
          loc_lat = ?,
          loc_lon = ?,
          env_temp = ?,
          lnd_7318c = ?,
          lnd_7318u = ?,
          lnd_7128ec = ?,
          pms_pm02_5 = ?,
          bat_voltage = ?,
          dev_temp = ?
        WHERE device_urn = ? AND timediff(?, when_captured) > 0;
        '''
    with sqlite3.connect("measurements.sqlite") as conn:
        curs = conn.cursor()
        device_filename = f"{rec['device_urn']}.json"

        curs.execute(sql_update,
                     (rec['device_urn'],
                        rec['when_captured'],
                        rec['loc_lat'],
                        rec['loc_lon'],
                        rec['env_temp'],
                        rec['lnd_7318c'],
                        rec['lnd_7318u'],
                        rec['lnd_7128ec'],
                        rec['pms_pm02_5'],
                        rec['bat_voltage'],
                        rec['dev_temp'],
                        rec['device_urn'],
                        rec['when_captured']
                    ))
        conn.commit()
    return curs.rowcount


if __name__ == "__main__":
    create_table()

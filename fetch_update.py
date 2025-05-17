'''Function to update the database from tt server. It pulls down all the devices
and updates the table where the timestamp is later than existing.
This function could eventually become the worker in a thread.'''

import requests

import manage_db
import constants

def get_update():
    URL = constants.URL

    req = requests.get(URL)
    if not req.ok:
        print("Error reading the database. Returning...")
        return
    json = req.json()

    for j in json:
        nrows = manage_db.update_data(j)


if __name__ == '__main__':
    get_update()
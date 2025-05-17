SELECT device_urn, when_captured, loc_lat, loc_lon, lnd_7318u
	FROM measurements 
	WHERE device_urn LIKE 'geigiecast%' OR device_urn = 'geigiecast-zen:%'
	ORDER BY when_captured DESC
	LIMIT 20
	;
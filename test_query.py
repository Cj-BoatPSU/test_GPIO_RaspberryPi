from influxdb import InfluxDBClient

def main():
    """Instantiate a connection to the InfluxDB."""
    host = 'localhost'
    port = 8086
    user = 'mydb'
    password = 'cjboat'
    dbname = 'db_version1'
    query = 'SELECT * FROM "temperature" WHERE location = \'sensor1\';'

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Querying data: " + query)
    result = client.query(query)
    
    for point in result.get_points():
        print(point)
    
    print(result)

if __name__ == '__main__':
    main()
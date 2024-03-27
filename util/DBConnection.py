import pyodbc
from util.PropertyUtil import PropertyUtil
class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                connection_string = PropertyUtil.get_property_string()
                DBConnection.connection = pyodbc.connect(connection_string)
                if DBConnection.connection:
                    print("Connected to MSSQL database")
            except pyodbc.Error as e:
                print(f"Error while connecting to MSSQL: {e}")
        return DBConnection.connection

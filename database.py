import sqlite3

class DataBase():
    def __init__(self, DbName):
        self.DbName = DbName
        self.conn = sqlite3.connect(DbName)
        self.cursorObj = self.conn.cursor()

    def get_fields(self, table):
        # Select all data from the specified table
        self.cursorObj.execute(f"SELECT * FROM {table}")
        # Get a list of the fields in the table
        Fields = [field[0] for field in self.cursorObj.description]
        return Fields

    def fetch_all(self, table):
        # Select all data from the specified table
        self.cursorObj.execute(f'select * from {table}')
        # Get all rows returned by the query
        results = self.cursorObj.fetchall()
        return results

    def update_data(self, table, field, data, keyfield, kid):
        """ 
        General update query that will work on the key field of any table 
        
        Args:
            table: The name of the table to update
            field: The field to update
            data: The new value for the field
            keyfield: The key field for the table
            kid: The key field value for the record to update
        """
        # Update the specified field for the record with the given keyfield value
        sql = f"UPDATE {table} SET {field} = ? WHERE {keyfield} =?"
        self.cursorObj.execute(sql,(data, kid))
        self.conn.commit()

    def delete_record(self, attr, table, criteria):
        """
        Delete a record from the specified table
        
        Args:
            attr: The attribute to match against the criteria
            table: The name of the table to delete from
            criteria: The value to match for the specified attribute
        """
        # Delete the record where the specified attribute matches the criteria
        self.cursorObj.execute(f"delete from {table} where \"{attr}\" = ?",(criteria,))
        self.conn.commit()

    def add_record(self, table, values):
        """
        Add a new record to the specified table
        
        Args:
            table: The name of the table to add the record to
            values: The values to add to the new record
        """
        # Get the number of values to add
        count = len(values)
        # Create an insert statement for the new record and execute it
        self.cursorObj.execute(f"insert into {table} values (null,"+",".join(count * "?")+")",(values))
        self.conn.commit()

    def general_sql(self, sql):
        """
        Execute a general SQL statement
        
        Args:
            sql: The SQL statement to execute
        """
        # Execute the specified SQL statement and return the results
        self.cursorObj.execute(sql)
        results = self.cursorObj.fetchall()
        return results

    def getData(self, table, attr, criteria):
        """
        Get data from the specified table that matches the specified criteria
        
        Args:
            table: The name of the table to get data from
            attr: The attribute to match against the criteria
            criteria: The value to match for the specified attribute
        """
        # Select all data from the specified table where the specified attribute matches the criteria
        self.cursorObj.execute(f"SELECT * FROM {table} WHERE {attr} like ?", ("%"+criteria+"%",))
        # Get all rows returned by the query
        results = self.cursorObj.fetchall()
        return results
    
    def AverageData(self, table, field):
        """
        Calculate the average of a specified field in the specified table.
    
        Args:
            table (str): The name of the table to query.
            field (str): The name of the field to calculate the average of.
    
        Returns:
            list of tuples: The query result, which contains a single tuple with the average value.
        """
        self.cursorObj.execute(f"SELECT AVG({field}) FROM {table}")
        result = self.cursorObj.fetchall()
        return result

    def close(self):
        # Close the connection to the SQLite database
        self.conn.close()

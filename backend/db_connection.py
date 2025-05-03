import mysql.connector

global cnx

# create a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dinefoods"
)
def get_order_status(order_id: int):
    #create a cursor object
    cursor = cnx.cursor()

    #write the sql query
    query = ("SELECT status from order_tracking WHERE order_id = %s")

    #execute the query
    cursor.execute(query, (order_id,))

    #fetch the result
    result = cursor.fetchone()

    #close the cursor and connection
    cursor.close()
    cnx.close()

    if result is not None:
        return result[0]
    else:
        return None




from connect_db import conn, cursor


# def deleteData():
#   deleteSQL = f"""
#     DELETE FROM "{'parent'}"
#     WHERE "{'PersonID'}" = "{'2'}"
#     """
#   cursor.execute("PRAGMA foreign_keys = ON")
#   cursor.execute(deleteSQL)
#   conn.commit()


# if __name__ == '__main__':
#   deleteData()

def deleteData(table_name,column_name,personID):
    deleteSQL = f"""
    DELETE FROM "{table_name}"
    WHERE "{column_name}" = "{personID}"
    """
    cursor.execute(deleteSQL)
    conn.commit()
if __name__ == '__main__':
    deleteData()

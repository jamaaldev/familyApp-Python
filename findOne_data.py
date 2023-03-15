from connect_db import cursor


def findOne(table_name, column_name, ParentID):
  findSQL = f"""
    SELECT * FROM "{table_name}"
    WHERE "{column_name}" = "{ParentID}"
    """
  cursor.execute(findSQL)
  data = cursor.fetchall()
  return data

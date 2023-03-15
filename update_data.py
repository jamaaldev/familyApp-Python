from connect_db import conn, cursor


def updateParent(
  column_name,
  parentID,
  personID,
):
  print('Updated Parent Data')
  updateSQL = f"""
    UPDATE parent
    SET "{column_name}" = "{parentID}" 
    WHERE "PersonID" = "{personID}"
    """
  cursor.execute(updateSQL)
  conn.commit()


def updateChildren(
  column_name,
  parentID,
  childID,
):
  print('Updated Child Data')
  updateSQL = f"""
    UPDATE children
    SET "{column_name}" = "{parentID}" 
    WHERE "ChildID" = "{childID}"
    """
  cursor.execute(updateSQL)
  conn.commit()

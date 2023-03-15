from connect_db import cursor


def readParent():
  readSQL = """ SELECT * FROM parent """
  cursor.execute(readSQL)
  data = cursor.fetchall()
  if data != []:
    return data
  else:
    return 'No Data'


def readChildren():
  readSQL = """ SELECT * FROM children """
  cursor.execute(readSQL)
  data = cursor.fetchall()
  if data != []:
    return data
  else:
    return 'No Data'

if __name__ == "__main__":
  print('parent list :', readParent())
  print('children list :', readChildren())

from connect_db import conn, cursor
from read_data import readParent
from update_data import updateParent, updateChildren
from findOne_data import findOne


def add():
  ParentID = input('Enter Your Passport ID or driver-license ID Ex AB12345: ')
  finded = []
  if ParentID != '':
    findedPerson = findOne('parent', 'FatherID', ParentID)
    if findedPerson != []:
      finded = findedPerson
  if ParentID != '':
    findedPerson = findOne('parent', 'MotherID', ParentID)
    if findedPerson != []:
      finded = findedPerson
  if ParentID != '':
    findedPerson = findOne('parent', 'CarerID', ParentID)
    if findedPerson != []:
      finded = findedPerson
  searchPerson = ''   
  if finded == []:
    searchPerson = input('Do you Want To Search By PersonID Yes Or No : ').lower()
  if searchPerson == 'yes' and finded == []:
    PersonID = input('Enter Your Person ID Ex 1,2,123: ')
    findedPerson = findOne('parent', 'PersonID', PersonID)
    if findedPerson != []:
      finded = findedPerson

  print('findedPerson:', finded)
  if finded != []:
    hasKids = input(
        'Enter yes or no if you have child to Register yes or no : ').lower()
    if hasKids == 'yes':
      relationship = input(
          'Enter relationship with the child, Ex: Father,Mother,Carer : ').lower(
      )
      column_name = relationship
      childID = input('Enter Child Passport ID or birth certificate number: ')

      if column_name == 'father':
        column_name = "FatherID"
      if column_name == 'mother':
        column_name = "MotherID"
      if column_name == 'carer':
        column_name = "CarerID"
      findedChild= findOne('children', 'ChildID', childID)
      
      if findedChild != []:
        # parentID = input(
        #   'ParentID: Enter Your Passport ID or driver-license ID: ')
        personId = [ person[0] for person in finded]
        print("📢[insert_data.py:46]: ", personId[0])

        updateParent(column_name,ParentID,personId[0])
        updateChildren(column_name, ParentID, childID)
      else:
       if hasKids == 'yes':

        if relationship == 'father':
          insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}","{ParentID}",NULL,NULL)
                  """
          cursor.execute(insertSQL)
          conn.commit()
        if relationship == 'mother':
          insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,"{ParentID}",NULL)
                  """
          cursor.execute(insertSQL)
          conn.commit()
        if relationship == 'carer':
          insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,NULL,"{parentID}")
                  """
          cursor.execute(insertSQL)
          conn.commit()
      # child()
    else:
      # insertSQL = f"""
      #         INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",Null,NULL,NULL)
      #         """
      # cursor.execute(insertSQL)
      # conn.commit()

      print('Good Day')
      print("""
                    Welcome To My Small App Family 
                    ------------------------------
    | --> This Application Base On Python Intagrated Database SQLite3 <-- |
    ---------------------------------------------------------------

    You Have Views Option To Choose Ex: 1,2,3,4

    1. : ReadData for Parent
    2. : ReadData for Children
    3. : InsertData To Add New Person
    4. : DeleteData By PersonID
    5. : Exit


    """)

  else:

    firstName = input('Enter your First Name: ')
    lastName = input('Enter your Last Name: ')
    age = input('Enter your Age: ')
    hasKids = input(
        'Enter yes or no if you have child to Register yes or no : ').lower()

    # insertSQL = f"""
    # INSERT INTO parent VALUES(NULL,{firstName},{lastName},{age},{'father'},{"mother"},{'carer'})
    # """
    if hasKids == 'yes':
      relationship = input(
          'Enter relationship with the child, Ex: Father,Mother,Carer : ').lower(
      )
      
      if relationship == 'father':
        insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}","{ParentID}",NULL,NULL)
                  """
        cursor.execute(insertSQL)
        conn.commit()
      if relationship == 'mother':
        insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,"{ParentID}",NULL)
                  """
        cursor.execute(insertSQL)
        conn.commit()
      if relationship == 'carer':
        insertSQL = f"""
                  INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,NULL,"{ParentID}")
                  """
        cursor.execute(insertSQL)
        conn.commit()
      child()
    else:
      insertSQL = f"""
              INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",Null,NULL,NULL)
              """
      cursor.execute(insertSQL)
      conn.commit()


def child():
  print('parent-list:', readParent())
  childID = input('Enter Child Passport ID or birth certificate number: ')
  # first check if the child already exist in the database
  # by checking passport id or birth certificate number
  findedPerson = findOne('children', 'ChildID', childID)
  print('findPerson:', findedPerson)
  relationship = input(
      'Enter relationship with the child, Ex: Father,Mother,Carer : ')
  print('relation:', relationship)
  if findedPerson != []:
    column_name = relationship
    if column_name == 'father':
      column_name = "FatherID"
    if column_name == 'mother':
      column_name = "MotherID"
    if column_name == 'carer':
      column_name = "CarerID"
    parentID = input('ParentID: Enter Your Passport ID or driver-license ID: ')
    updateChildren(column_name, parentID, childID)
  else:
    firstName = input('Enter child First Name: ')
    lastName = input('Enter child Last Name: ')
    age = input('Enter child Age: ')
    # insertSQL = f"""
    #     INSERT INTO children VALUES(NULL,"{firstName}","{lastName}","{age}","{childID}","{'father'}","{'mother'}","{'carer'}")
    #     """
    parentList = ['father', 'mother', 'carer']
    print('relation', relationship, 'parent', parentList)
    if relationship in parentList:
      parentID = input(
          'ParentID: Enter Your Passport ID or driver-license ID: ')
      print('relationship', relationship)
      if parentID != '':
        insertSQL = f"""
                    INSERT INTO children VALUES(NULL,"{firstName}","{lastName}","{age}","{childID}","{parentID}",NULL,NULL)
                    """
        cursor.execute(insertSQL)
        conn.commit()


if __name__ == '__main__':
  add()

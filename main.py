from insert_data import add
from delete_data import deleteData
from read_data import readChildren, readParent
from create_table import createTable
# : UpdateParent To Update Existing Person Base Of PersonID and ParentID


def menuIU():
  return """
                  Welcome To My Small App Family
                  ------------------------------
  | --> This Application Base On Python Intagrated Database SQLite3 <-- |
  ---------------------------------------------------------------

  You Have Views Option To Choose Ex: 1,2,3,4

  1. : ReadData for Parent
  2. : ReadData for Children
  3. : InsertData To Add New Person
  4. : DeleteData Parent By PersonID
  5. : Exit


  """


if __name__ == '__main__':
  print(menuIU())
loop = True
while loop:

  choose = input('Please Choose a Option: ')
  if '1' == choose:
    print('ParentList:', readParent())
  if '2' == choose:
    print('ChildrenList:', readChildren())
  if '3' == choose:
    print('Option 3 is Insert Query') 
    add()
  if '4' == choose:
      print('Option 4 is Delete Query')
      table_name = input(
          'Enter Table Name, Ex: parent,children : ').lower(
      )
  
      # if table_name != '' and table_name != 'children' :
      #     relationship = input(
      #     'Enter relationship with the child, Ex: Father,Mother,Carer : ').lower(
      # )
      personID = input(
          'Enter PersonID To Delete : ').lower(
      )
      # table_name = table_name
      # if column_name == 'father':
      #   column_name = "FatherID"
      # if column_name == 'mother':
      #   column_name = "MotherID"
      # if column_name == 'carer':
      #   column_name = "CarerID"
      # if table_name == 'children':
      #   column_name = "ChildID"
      deleteData(table_name,'PersonID',personID)
      print('One Person Has Been Deleted From DataBase ')
  if '5' == choose:
    loop = False
    print('Please Come Back Soon')
# createTable()
# parent()

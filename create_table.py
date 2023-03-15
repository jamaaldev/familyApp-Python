from connect_db import cursor


def createTable():

  table_parent = """
  CREATE TABLE parent(
  "PersonID" INTEGER PRIMARY KEY AUTOINCREMENT,
  "FirstName" varchar(20)  NOT NULL,
  "LastName" varchar(20)  NOT NULL,
  "Age" int,
  "FatherID" varchar(50) UNIQUE,
  "MotherID" varchar(50) UNIQUE,
  "CarerID" varchar(50) UNIQUE
  );
  """
  table_children = """
  CREATE TABLE children(
  "PersonID" INTEGER PRIMARY KEY AUTOINCREMENT,
  "FirstName" varchar(20)  NOT NULL,
  "LastName" varchar(20)  NOT NULL,
  "Age" int,
  "ChildID" varchar(50) NOT NULL UNIQUE,
  "FatherID" varchar(50),
  "MotherID" varchar(50),
  "CarerID" varchar(50),
  FOREIGN KEY ("MotherID") REFERENCES parent("MotherID"),
  FOREIGN KEY ("FatherID") REFERENCES parent("FatherID"),
  FOREIGN KEY ("CarerID") REFERENCES parent("CarerID")
  );
  """
  # cursor.execute("DROP TABLE children")
  # cursor.execute("DROP TABLE parent")

  cursor.execute(table_parent)
  cursor.execute(table_children)
if __name__ == "__main__":
  createTable()
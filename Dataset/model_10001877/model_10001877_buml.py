####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Patron_Actor = Class(name="Patron_Actor")
Librarian_Actor = Class(name="Librarian_Actor")
Reserve_Book_UseCase = Class(name="Reserve_Book_UseCase")
Check_Out_Book_UseCase = Class(name="Check_Out_Book_UseCase")
Check_In_Book_UseCase = Class(name="Check_In_Book_UseCase")
Mail_2_Week_Reminders_UseCase = Class(name="Mail_2_Week_Reminders_UseCase")
Acquisition_of_Books_UseCase = Class(name="Acquisition_of_Books_UseCase")
Retirement_of_Books_UseCase = Class(name="Retirement_of_Books_UseCase")
Patron = Class(name="Patron")
Librarian = Class(name="Librarian")
Book = Class(name="Book")
Library = Class(name="Library")
Book_Actor = Class(name="Book_Actor")
Retired_UseCase = Class(name="Retired_UseCase")
Acquired_UseCase = Class(name="Acquired_UseCase")
Checked_In_UseCase = Class(name="Checked_In_UseCase")
Checked_Out_UseCase = Class(name="Checked_Out_UseCase")

# Patron_Actor class attributes and methods

# Librarian_Actor class attributes and methods

# Reserve_Book_UseCase class attributes and methods

# Check_Out_Book_UseCase class attributes and methods

# Check_In_Book_UseCase class attributes and methods

# Mail_2_Week_Reminders_UseCase class attributes and methods

# Acquisition_of_Books_UseCase class attributes and methods

# Retirement_of_Books_UseCase class attributes and methods

# Patron class attributes and methods
Patron_id: Property = Property(name="id", type=IntegerType)
Patron_name: Property = Property(name="name", type=StringType)
Patron_status: Property = Property(name="status", type=StringType)
Patron_address: Property = Property(name="address", type=StringType)
Patron_num_books_checked_out: Property = Property(name="num_books_checked_out", type=IntegerType)
Patron.attributes={Patron_status, Patron_id, Patron_num_books_checked_out, Patron_address, Patron_name}

# Librarian class attributes and methods
Librarian_id: Property = Property(name="id", type=IntegerType)
Librarian_name: Property = Property(name="name", type=StringType)
Librarian.attributes={Librarian_id, Librarian_name}

# Book class attributes and methods
Book_id: Property = Property(name="id", type=IntegerType)
Book_author: Property = Property(name="author", type=StringType)
Book_title: Property = Property(name="title", type=StringType)
Book_status: Property = Property(name="status", type=StringType)
Book_creation_date: Property = Property(name="creation_date", type=StringType)
Book.attributes={Book_author, Book_status, Book_title, Book_id, Book_creation_date}

# Library class attributes and methods
Library_id: Property = Property(name="id", type=IntegerType)
Library_librarian_id: Property = Property(name="librarian_id", type=IntegerType)
Library.attributes={Library_librarian_id, Library_id}

# Book_Actor class attributes and methods

# Retired_UseCase class attributes and methods

# Acquired_UseCase class attributes and methods

# Checked_In_UseCase class attributes and methods

# Checked_Out_UseCase class attributes and methods

# Relationships
Acquisition_of_Books_Librarian: BinaryAssociation = BinaryAssociation(
    name="Acquisition_of_Books_Librarian",
    ends={
        Property(name="librarian14", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="acquisition_of_Books15", type=Acquisition_of_Books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Retirement_of_Books_Librarian: BinaryAssociation = BinaryAssociation(
    name="Retirement_of_Books_Librarian",
    ends={
        Property(name="librarian16", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="retirement_of_Books17", type=Retirement_of_Books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Book",
    ends={
        Property(name="book18", type=Book, multiplicity=Multiplicity(0, 9999)),
        Property(name="patron19", type=Patron, multiplicity=Multiplicity(0, 1))
    }
)
Library_Librarian: BinaryAssociation = BinaryAssociation(
    name="Library_Librarian",
    ends={
        Property(name="librarian20", type=Librarian, multiplicity=Multiplicity(0, 1)),
        Property(name="library21", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Book",
    ends={
        Property(name="book22", type=Book, multiplicity=Multiplicity(0, 9999)),
        Property(name="librarian23", type=Librarian, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Librarian: BinaryAssociation = BinaryAssociation(
    name="Patron_Librarian",
    ends={
        Property(name="librarian24", type=Librarian, multiplicity=Multiplicity(0, 1)),
        Property(name="patron25", type=Patron, multiplicity=Multiplicity(0, 9999))
    }
)
Library_Patron: BinaryAssociation = BinaryAssociation(
    name="Library_Patron",
    ends={
        Property(name="patron26", type=Patron, multiplicity=Multiplicity(0, 9999)),
        Property(name="library27", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
Book_Retired: BinaryAssociation = BinaryAssociation(
    name="Book_Retired",
    ends={
        Property(name="retired28", type=Retired_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="book29", type=Book_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Book_Acquired: BinaryAssociation = BinaryAssociation(
    name="Book_Acquired",
    ends={
        Property(name="acquired30", type=Acquired_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="book31", type=Book_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Book_Check_In: BinaryAssociation = BinaryAssociation(
    name="Book_Check_In",
    ends={
        Property(name="check_In32", type=Checked_In_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="book33", type=Book_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Book_Check_Out: BinaryAssociation = BinaryAssociation(
    name="Book_Check_Out",
    ends={
        Property(name="check_Out34", type=Checked_Out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="book35", type=Book_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Check_Out_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Check_Out_Book",
    ends={
        Property(name="check_Out_Book0", type=Check_Out_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron1", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_In_Book_Patron: BinaryAssociation = BinaryAssociation(
    name="Check_In_Book_Patron",
    ends={
        Property(name="patron2", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_In_Book3", type=Check_In_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Reserve_Book_Patron: BinaryAssociation = BinaryAssociation(
    name="Reserve_Book_Patron",
    ends={
        Property(name="patron4", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reserve_Book5", type=Reserve_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_Out_Book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Check_Out_Book_Librarian",
    ends={
        Property(name="librarian6", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Out_Book7", type=Check_Out_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_In_Book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Check_In_Book_Librarian",
    ends={
        Property(name="librarian8", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_In_Book9", type=Check_In_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Reserve_Book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Reserve_Book_Librarian",
    ends={
        Property(name="librarian10", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reserve_Book11", type=Reserve_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Mail_2_Week_Reminders_Librarian: BinaryAssociation = BinaryAssociation(
    name="Mail_2_Week_Reminders_Librarian",
    ends={
        Property(name="librarian12", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mail_2_Week_Reminders13", type=Mail_2_Week_Reminders_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_b32rMMEKEeeEXb8Dudo6PQ",
    types={Patron_Actor, Librarian_Actor, Reserve_Book_UseCase, Check_Out_Book_UseCase, Check_In_Book_UseCase, Mail_2_Week_Reminders_UseCase, Acquisition_of_Books_UseCase, Retirement_of_Books_UseCase, Patron, Librarian, Book, Library, Book_Actor, Retired_UseCase, Acquired_UseCase, Checked_In_UseCase, Checked_Out_UseCase},
    associations={Acquisition_of_Books_Librarian, Retirement_of_Books_Librarian, Patron_Book, Library_Librarian, Librarian_Book, Patron_Librarian, Library_Patron, Book_Retired, Book_Acquired, Book_Check_In, Book_Check_Out, Patron_Check_Out_Book, Check_In_Book_Patron, Reserve_Book_Patron, Check_Out_Book_Librarian, Check_In_Book_Librarian, Reserve_Book_Librarian, Mail_2_Week_Reminders_Librarian},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
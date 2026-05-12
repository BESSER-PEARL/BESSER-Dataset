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
Librarian_Actor = Class(name="Librarian_Actor")
Check_In_UseCase = Class(name="Check_In_UseCase")
Check_out_UseCase = Class(name="Check_out_UseCase")
Reminder_System_UseCase = Class(name="Reminder_System_UseCase")
Patron_Actor = Class(name="Patron_Actor")
Reserve_UseCase = Class(name="Reserve_UseCase")
Fine_Calculation_UseCase = Class(name="Fine_Calculation_UseCase")
Book_UseCase = Class(name="Book_UseCase")
CD_UseCase = Class(name="CD_UseCase")
Software_UseCase = Class(name="Software_UseCase")
Video_UseCase = Class(name="Video_UseCase")
Library_Inventory_UseCase = Class(name="Library_Inventory_UseCase")
Search_UseCase = Class(name="Search_UseCase")
User_Status_UseCase = Class(name="User_Status_UseCase")
Add_New_Inventory_UseCase = Class(name="Add_New_Inventory_UseCase")
Retire_Old_Inventory_UseCase = Class(name="Retire_Old_Inventory_UseCase")
Due_Date_UseCase = Class(name="Due_Date_UseCase")
Renew_UseCase = Class(name="Renew_UseCase")
Magazine_Management__System_UseCase = Class(name="Magazine_Management__System_UseCase")
Patron = Class(name="Patron")

# Librarian_Actor class attributes and methods

# Check_In_UseCase class attributes and methods

# Check_out_UseCase class attributes and methods

# Reminder_System_UseCase class attributes and methods

# Patron_Actor class attributes and methods

# Reserve_UseCase class attributes and methods

# Fine_Calculation_UseCase class attributes and methods

# Book_UseCase class attributes and methods

# CD_UseCase class attributes and methods

# Software_UseCase class attributes and methods

# Video_UseCase class attributes and methods

# Library_Inventory_UseCase class attributes and methods

# Search_UseCase class attributes and methods

# User_Status_UseCase class attributes and methods

# Add_New_Inventory_UseCase class attributes and methods

# Retire_Old_Inventory_UseCase class attributes and methods

# Due_Date_UseCase class attributes and methods

# Renew_UseCase class attributes and methods

# Magazine_Management__System_UseCase class attributes and methods

# Patron class attributes and methods

# Relationships
Librarian_Reminder_needs_to_be_mailed: BinaryAssociation = BinaryAssociation(
    name="Librarian_Reminder_needs_to_be_mailed",
    ends={
        Property(name="reminder_needs_to_be_mailed0", type=Reminder_System_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian1", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Late_reminder_Patron: BinaryAssociation = BinaryAssociation(
    name="Late_reminder_Patron",
    ends={
        Property(name="patron2", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="late_reminder3", type=Reminder_System_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_in_book_Patron: BinaryAssociation = BinaryAssociation(
    name="Check_in_book_Patron",
    ends={
        Property(name="patron4", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_in_book5", type=Check_In_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_out_book_Patron: BinaryAssociation = BinaryAssociation(
    name="Check_out_book_Patron",
    ends={
        Property(name="patron6", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_out_book7", type=Check_out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Reserve_Patron: BinaryAssociation = BinaryAssociation(
    name="Reserve_Patron",
    ends={
        Property(name="patron8", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reserve9", type=Reserve_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fine_Calculation_Librarian: BinaryAssociation = BinaryAssociation(
    name="Fine_Calculation_Librarian",
    ends={
        Property(name="librarian10", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fine_Calculation11", type=Due_Date_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fine_Calculation_Late_reminder: BinaryAssociation = BinaryAssociation(
    name="Fine_Calculation_Late_reminder",
    ends={
        Property(name="late_reminder12", type=Reminder_System_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fine_Calculation13", type=Fine_Calculation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fine_Calculation_Book: BinaryAssociation = BinaryAssociation(
    name="Fine_Calculation_Book",
    ends={
        Property(name="book14", type=User_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fine_Calculation15", type=Due_Date_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Resource_Book: BinaryAssociation = BinaryAssociation(
    name="Library_Resource_Book",
    ends={
        Property(name="book16", type=Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Resource17", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Resource_CD: BinaryAssociation = BinaryAssociation(
    name="Library_Resource_CD",
    ends={
        Property(name="cD18", type=CD_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Resource19", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Resource_Software: BinaryAssociation = BinaryAssociation(
    name="Library_Resource_Software",
    ends={
        Property(name="software20", type=Software_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Resource21", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Resource_Video: BinaryAssociation = BinaryAssociation(
    name="Library_Resource_Video",
    ends={
        Property(name="video22", type=Video_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Resource23", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_out_Library_Resource: BinaryAssociation = BinaryAssociation(
    name="Check_out_Library_Resource",
    ends={
        Property(name="library_Resource24", type=User_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="check_out25", type=Check_out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Due_Date_Fine_Calculation: BinaryAssociation = BinaryAssociation(
    name="Due_Date_Fine_Calculation",
    ends={
        Property(name="fine_Calculation44", type=Fine_Calculation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="due_Date45", type=Due_Date_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Renew_Patron: BinaryAssociation = BinaryAssociation(
    name="Renew_Patron",
    ends={
        Property(name="patron46", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="renew47", type=Renew_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Renew_User_Status: BinaryAssociation = BinaryAssociation(
    name="Renew_User_Status",
    ends={
        Property(name="user_Status48", type=User_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="renew49", type=Renew_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Search: BinaryAssociation = BinaryAssociation(
    name="Patron_Search",
    ends={
        Property(name="search50", type=Search_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron51", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Inventory_Magazine_Management: BinaryAssociation = BinaryAssociation(
    name="Library_Inventory_Magazine_Management",
    ends={
        Property(name="magazine_Management52", type=Magazine_Management__System_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Inventory53", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Magazine_Management__System: BinaryAssociation = BinaryAssociation(
    name="Librarian_Magazine_Management__System",
    ends={
        Property(name="magazine_Management__System54", type=Magazine_Management__System_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian55", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Fine_Calculation: BinaryAssociation = BinaryAssociation(
    name="Librarian_Fine_Calculation",
    ends={
        Property(name="fine_Calculation56", type=Fine_Calculation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian57", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_In_Library_Resource: BinaryAssociation = BinaryAssociation(
    name="Check_In_Library_Resource",
    ends={
        Property(name="library_Resource26", type=User_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="check_In27", type=Check_In_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Reserve_Search: BinaryAssociation = BinaryAssociation(
    name="Reserve_Search",
    ends={
        Property(name="search28", type=Search_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="reserve29", type=Reserve_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Search_Library_Inventory: BinaryAssociation = BinaryAssociation(
    name="Search_Library_Inventory",
    ends={
        Property(name="library_Inventory30", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="search31", type=Search_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_Status_Library_Inventory: BinaryAssociation = BinaryAssociation(
    name="User_Status_Library_Inventory",
    ends={
        Property(name="library_Inventory32", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user_Status33", type=User_Status_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Add_New_Inventory: BinaryAssociation = BinaryAssociation(
    name="Librarian_Add_New_Inventory",
    ends={
        Property(name="add_New_Inventory34", type=Add_New_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian35", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Add_New_Inventory_Library_Inventory: BinaryAssociation = BinaryAssociation(
    name="Add_New_Inventory_Library_Inventory",
    ends={
        Property(name="library_Inventory36", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="add_New_Inventory37", type=Add_New_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Retire_Old_Inventory: BinaryAssociation = BinaryAssociation(
    name="Librarian_Retire_Old_Inventory",
    ends={
        Property(name="retire_Old_Inventory38", type=Retire_Old_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian39", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Retire_Old_Inventory_Library_Inventory: BinaryAssociation = BinaryAssociation(
    name="Retire_Old_Inventory_Library_Inventory",
    ends={
        Property(name="library_Inventory40", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="retire_Old_Inventory41", type=Retire_Old_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Inventory_Due_Date: BinaryAssociation = BinaryAssociation(
    name="Library_Inventory_Due_Date",
    ends={
        Property(name="due_Date42", type=Due_Date_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_Inventory43", type=Library_Inventory_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JX9gcDt0Eei384rcaJKdxw",
    types={Librarian_Actor, Check_In_UseCase, Check_out_UseCase, Reminder_System_UseCase, Patron_Actor, Reserve_UseCase, Fine_Calculation_UseCase, Book_UseCase, CD_UseCase, Software_UseCase, Video_UseCase, Library_Inventory_UseCase, Search_UseCase, User_Status_UseCase, Add_New_Inventory_UseCase, Retire_Old_Inventory_UseCase, Due_Date_UseCase, Renew_UseCase, Magazine_Management__System_UseCase, Patron},
    associations={Librarian_Reminder_needs_to_be_mailed, Late_reminder_Patron, Check_in_book_Patron, Check_out_book_Patron, Reserve_Patron, Fine_Calculation_Librarian, Fine_Calculation_Late_reminder, Fine_Calculation_Book, Library_Resource_Book, Library_Resource_CD, Library_Resource_Software, Library_Resource_Video, Check_out_Library_Resource, Due_Date_Fine_Calculation, Renew_Patron, Renew_User_Status, Patron_Search, Library_Inventory_Magazine_Management, Librarian_Magazine_Management__System, Librarian_Fine_Calculation, Check_In_Library_Resource, Reserve_Search, Search_Library_Inventory, User_Status_Library_Inventory, Librarian_Add_New_Inventory, Add_New_Inventory_Library_Inventory, Librarian_Retire_Old_Inventory, Retire_Old_Inventory_Library_Inventory, Library_Inventory_Due_Date},
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
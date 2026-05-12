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
User_Actor = Class(name="User_Actor")
Library_Management_System_Component = Class(name="Library_Management_System_Component", is_abstract=True)
T = Class(name="T")
Books_Database_Actor = Class(name="Books_Database_Actor")
User_Database_Actor = Class(name="User_Database_Actor")
Librarian_Actor = Class(name="Librarian_Actor")
Organise_Book_details_external = Class(name="Organise_Book_details_external")
Search_for_Books_external = Class(name="Search_for_Books_external")
Issue_Book_external = Class(name="Issue_Book_external")
Pay_Fine_external = Class(name="Pay_Fine_external")
Requests_for_Book_Borrow_external = Class(name="Requests_for_Book_Borrow_external")
Return_Book_external = Class(name="Return_Book_external")
Register_Member_external = Class(name="Register_Member_external")
Validation_external = Class(name="Validation_external")

# User_Actor class attributes and methods

# Library_Management_System_Component class attributes and methods

# T class attributes and methods

# Books_Database_Actor class attributes and methods

# User_Database_Actor class attributes and methods

# Librarian_Actor class attributes and methods

# Organise_Book_details_external class attributes and methods

# Search_for_Books_external class attributes and methods

# Issue_Book_external class attributes and methods

# Pay_Fine_external class attributes and methods

# Requests_for_Book_Borrow_external class attributes and methods

# Return_Book_external class attributes and methods

# Register_Member_external class attributes and methods

# Validation_external class attributes and methods

# Relationships
Organise_Book_details_Books_Database: BinaryAssociation = BinaryAssociation(
    name="Organise_Book_details_Books_Database",
    ends={
        Property(name="books_Database0", type=Books_Database_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="organise_Book_details1", type=Organise_Book_details_external, multiplicity=Multiplicity(0, 1))
    }
)
Search_for_Books_Books_Database: BinaryAssociation = BinaryAssociation(
    name="Search_for_Books_Books_Database",
    ends={
        Property(name="books_Database2", type=Books_Database_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="search_for_Books3", type=Search_for_Books_external, multiplicity=Multiplicity(0, 1))
    }
)
Issue_Book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Issue_Book_Librarian",
    ends={
        Property(name="librarian4", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="issue_Book5", type=Issue_Book_external, multiplicity=Multiplicity(0, 1))
    }
)
Pay_Fine_Librarian: BinaryAssociation = BinaryAssociation(
    name="Pay_Fine_Librarian",
    ends={
        Property(name="librarian6", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pay_Fine7", type=Pay_Fine_external, multiplicity=Multiplicity(0, 1))
    }
)
User_Search_for_Books: BinaryAssociation = BinaryAssociation(
    name="User_Search_for_Books",
    ends={
        Property(name="search_for_Books8", type=Search_for_Books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Requests_for_Book_Borrow: BinaryAssociation = BinaryAssociation(
    name="User_Requests_for_Book_Borrow",
    ends={
        Property(name="requests_for_Book_Borrow10", type=Requests_for_Book_Borrow_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Return_Book: BinaryAssociation = BinaryAssociation(
    name="User_Return_Book",
    ends={
        Property(name="return_Book12", type=Return_Book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Database_Register_Member: BinaryAssociation = BinaryAssociation(
    name="User_Database_Register_Member",
    ends={
        Property(name="register_Member14", type=Register_Member_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user_Database15", type=User_Database_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Database_Validation: BinaryAssociation = BinaryAssociation(
    name="User_Database_Validation",
    ends={
        Property(name="validation16", type=Validation_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user_Database17", type=User_Database_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_rjr_ELGtEee6S77dw3LIvQ",
    types={User_Actor, Library_Management_System_Component, T, Books_Database_Actor, User_Database_Actor, Librarian_Actor, Organise_Book_details_external, Search_for_Books_external, Issue_Book_external, Pay_Fine_external, Requests_for_Book_Borrow_external, Return_Book_external, Register_Member_external, Validation_external},
    associations={Organise_Book_details_Books_Database, Search_for_Books_Books_Database, Issue_Book_Librarian, Pay_Fine_Librarian, User_Search_for_Books, User_Requests_for_Book_Borrow, User_Return_Book, User_Database_Register_Member, User_Database_Validation},
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
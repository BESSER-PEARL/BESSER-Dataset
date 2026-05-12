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
Library_Management_System_Component = Class(name="Library_Management_System_Component")
Patron_Actor = Class(name="Patron_Actor")
Library_Staff_Actor = Class(name="Library_Staff_Actor")
librarymanagementsystem_Library = Class(name="librarymanagementsystem_Library")
Send_Book_external = Class(name="Send_Book_external")
Return_Book_external = Class(name="Return_Book_external")
Database_external = Class(name="Database_external")
Checkout_Book_external = Class(name="Checkout_Book_external")
Search_for_Books_external = Class(name="Search_for_Books_external")

# Library_Management_System_Component class attributes and methods

# Patron_Actor class attributes and methods

# Library_Staff_Actor class attributes and methods

# librarymanagementsystem_Library class attributes and methods
librarymanagementsystem_Library_books: Property = Property(name="books", type=StringType)
librarymanagementsystem_Library_CDs: Property = Property(name="CDs", type=StringType)
librarymanagementsystem_Library_software: Property = Property(name="software", type=StringType)
librarymanagementsystem_Library_videos: Property = Property(name="videos", type=StringType)
librarymanagementsystem_Library_fine: Property = Property(name="fine", type=StringType)
librarymanagementsystem_Library_maxFine: Property = Property(name="maxFine", type=StringType)
librarymanagementsystem_Library_computers: Property = Property(name="computers", type=IntegerType)
librarymanagementsystem_Library.attributes={librarymanagementsystem_Library_fine, librarymanagementsystem_Library_software, librarymanagementsystem_Library_CDs, librarymanagementsystem_Library_maxFine, librarymanagementsystem_Library_computers, librarymanagementsystem_Library_books, librarymanagementsystem_Library_videos}

# Send_Book_external class attributes and methods

# Return_Book_external class attributes and methods

# Database_external class attributes and methods

# Checkout_Book_external class attributes and methods

# Search_for_Books_external class attributes and methods

# Relationships
Send_Book_Library_Staff: BinaryAssociation = BinaryAssociation(
    name="Send_Book_Library_Staff",
    ends={
        Property(name="library_Staff0", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="send_Book1", type=Send_Book_external, multiplicity=Multiplicity(0, 1))
    }
)
Return_Book_Library_Staff: BinaryAssociation = BinaryAssociation(
    name="Return_Book_Library_Staff",
    ends={
        Property(name="library_Staff2", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="return_Book3", type=Return_Book_external, multiplicity=Multiplicity(0, 1))
    }
)
Database_Library_Staff: BinaryAssociation = BinaryAssociation(
    name="Database_Library_Staff",
    ends={
        Property(name="library_Staff4", type=Library_Staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="database5", type=Database_external, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Checkout_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Checkout_Book",
    ends={
        Property(name="checkout_Book6", type=Checkout_Book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron7", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Return_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Return_Book",
    ends={
        Property(name="return_Book8", type=Return_Book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron9", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Search_for_Books: BinaryAssociation = BinaryAssociation(
    name="Patron_Search_for_Books",
    ends={
        Property(name="search_for_Books10", type=Search_for_Books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron11", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_SPqNUK8AEee6S77dw3LIvQ",
    types={Library_Management_System_Component, Patron_Actor, Library_Staff_Actor, librarymanagementsystem_Library, Send_Book_external, Return_Book_external, Database_external, Checkout_Book_external, Search_for_Books_external},
    associations={Send_Book_Library_Staff, Return_Book_Library_Staff, Database_Library_Staff, Patron_Checkout_Book, Patron_Return_Book, Patron_Search_for_Books},
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
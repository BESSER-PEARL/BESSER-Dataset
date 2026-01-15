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
library_Library = Class(name="library::Library")
library_Book = Class(name="library::Book")
library_User = Class(name="library::User")
library_BorrowedItem = Class(name="library::BorrowedItem")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Book class attributes and methods
library_Book_name: Property = Property(name="name", type=StringType)
library_Book_author: Property = Property(name="author", type=StringType)
library_Book.attributes={library_Book_name, library_Book_author}

# library_User class attributes and methods
library_User_name: Property = Property(name="name", type=StringType)
library_User.attributes={library_User_name}

# library_BorrowedItem class attributes and methods
library_BorrowedItem_borrowDate: Property = Property(name="borrowDate", type=DateType)
library_BorrowedItem_lastReturnDate: Property = Property(name="lastReturnDate", type=DateType)
library_BorrowedItem.attributes={library_BorrowedItem_borrowDate, library_BorrowedItem_lastReturnDate}

# Relationships
borrowedItems4: BinaryAssociation = BinaryAssociation(
    name="borrowedItems4",
    ends={
        Property(name="user", type=library_BorrowedItem, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="BorrowedItem", type=library_User, multiplicity=Multiplicity(1, 1))
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="Library6", type=library_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
item7: BinaryAssociation = BinaryAssociation(
    name="item7",
    ends={
        Property(name="library_Book", type=library_BorrowedItem, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BorrowedItem", type=library_Book, multiplicity=Multiplicity(1, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users1: BinaryAssociation = BinaryAssociation(
    name="users1",
    ends={
        Property(name="User", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library2", type=library_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library3: BinaryAssociation = BinaryAssociation(
    name="library3",
    ends={
        Property(name="Library", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
user8: BinaryAssociation = BinaryAssociation(
    name="user8",
    ends={
        Property(name="User9", type=library_BorrowedItem, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowedItems", type=library_User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Book, library_User, library_BorrowedItem},
    associations={borrowedItems4, library5, item7, books0, users1, library3, user8},
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
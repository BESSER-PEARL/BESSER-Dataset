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
library3Simplified_BookInfo = Class(name="library3Simplified::BookInfo")
library3Simplified_Book = Class(name="library3Simplified::Book")
library3Simplified_Customer = Class(name="library3Simplified::Customer")
library3Simplified_Library = Class(name="library3Simplified::Library")

# library3Simplified_BookInfo class attributes and methods

# library3Simplified_Book class attributes and methods
library3Simplified_Book_pages: Property = Property(name="pages", type=IntegerType)
library3Simplified_Book_dimension: Property = Property(name="dimension", type=StringType)
library3Simplified_Book_download: Property = Property(name="download", type=StringType)
library3Simplified_Book_isbn: Property = Property(name="isbn", type=StringType)
library3Simplified_Book_name: Property = Property(name="name", type=StringType)
library3Simplified_Book_title: Property = Property(name="title", type=StringType)
library3Simplified_Book_author: Property = Property(name="author", type=StringType)
library3Simplified_Book.attributes={library3Simplified_Book_title, library3Simplified_Book_download, library3Simplified_Book_name, library3Simplified_Book_dimension, library3Simplified_Book_pages, library3Simplified_Book_author, library3Simplified_Book_isbn}

# library3Simplified_Customer class attributes and methods
library3Simplified_Customer_firstName: Property = Property(name="firstName", type=StringType)
library3Simplified_Customer_lastName: Property = Property(name="lastName", type=StringType)
library3Simplified_Customer_borrowedBookSince: Property = Property(name="borrowedBookSince", type=StringType)
library3Simplified_Customer.attributes={library3Simplified_Customer_borrowedBookSince, library3Simplified_Customer_firstName, library3Simplified_Customer_lastName}

# library3Simplified_Library class attributes and methods

# Relationships
bookInfo0: BinaryAssociation = BinaryAssociation(
    name="bookInfo0",
    ends={
        Property(name="library3Simplified_BookInfo", type=library3Simplified_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library3Simplified_Book", type=library3Simplified_BookInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
borrowedBookId1: BinaryAssociation = BinaryAssociation(
    name="borrowedBookId1",
    ends={
        Property(name="library3Simplified_Book2", type=library3Simplified_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="library3Simplified_Customer", type=library3Simplified_Book, multiplicity=Multiplicity(0, 1))
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="library3Simplified_Book4", type=library3Simplified_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library3Simplified_Library", type=library3Simplified_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers5: BinaryAssociation = BinaryAssociation(
    name="customers5",
    ends={
        Property(name="library3Simplified_Customer7", type=library3Simplified_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library3Simplified_Library6", type=library3Simplified_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library3Simplified",
    types={library3Simplified_BookInfo, library3Simplified_Book, library3Simplified_Customer, library3Simplified_Library},
    associations={bookInfo0, borrowedBookId1, books3, customers5},
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
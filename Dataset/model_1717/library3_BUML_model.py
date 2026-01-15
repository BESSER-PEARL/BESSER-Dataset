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
Library3_BookInfoType = Class(name="Library3::BookInfoType")
Library3_BookType = Class(name="Library3::BookType")
Library3_CustomerType = Class(name="Library3::CustomerType")
Library3_DocumentRoot = Class(name="Library3::DocumentRoot")
Library3_EStringToStringMapEntry = Class(name="Library3::EStringToStringMapEntry")
Library3_LibraryType = Class(name="Library3::LibraryType")

# Library3_BookInfoType class attributes and methods
Library3_BookInfoType_any: Property = Property(name="any", type=StringType)
Library3_BookInfoType.attributes={Library3_BookInfoType_any}

# Library3_BookType class attributes and methods
Library3_BookType_name: Property = Property(name="name", type=StringType)
Library3_BookType_title: Property = Property(name="title", type=StringType)
Library3_BookType_author: Property = Property(name="author", type=StringType)
Library3_BookType_pages: Property = Property(name="pages", type=StringType)
Library3_BookType_isbn: Property = Property(name="isbn", type=StringType)
Library3_BookType.attributes={Library3_BookType_name, Library3_BookType_pages, Library3_BookType_title, Library3_BookType_author, Library3_BookType_isbn}

# Library3_CustomerType class attributes and methods
Library3_CustomerType_firstName: Property = Property(name="firstName", type=StringType)
Library3_CustomerType_lastName: Property = Property(name="lastName", type=StringType)
Library3_CustomerType_borrowedBookId: Property = Property(name="borrowedBookId", type=StringType)
Library3_CustomerType.attributes={Library3_CustomerType_borrowedBookId, Library3_CustomerType_lastName, Library3_CustomerType_firstName}

# Library3_DocumentRoot class attributes and methods
Library3_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Library3_DocumentRoot.attributes={Library3_DocumentRoot_mixed}

# Library3_EStringToStringMapEntry class attributes and methods

# Library3_LibraryType class attributes and methods

# Relationships
bookInfo0: BinaryAssociation = BinaryAssociation(
    name="bookInfo0",
    ends={
        Property(name="Library3_BookInfoType", type=Library3_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Library3_BookType", type=Library3_BookInfoType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="Library3_DocumentRoot", type=Library3_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Library3_EStringToStringMapEntry", type=Library3_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="Library3_EStringToStringMapEntry4", type=Library3_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Library3_DocumentRoot3", type=Library3_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer10: BinaryAssociation = BinaryAssociation(
    name="customer10",
    ends={
        Property(name="Library3_CustomerType", type=Library3_LibraryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Library3_LibraryType11", type=Library3_CustomerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="Library3_LibraryType", type=Library3_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Library3_DocumentRoot6", type=Library3_LibraryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="Library3_BookType9", type=Library3_LibraryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Library3_LibraryType8", type=Library3_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Library3",
    types={Library3_BookInfoType, Library3_BookType, Library3_CustomerType, Library3_DocumentRoot, Library3_EStringToStringMapEntry, Library3_LibraryType},
    associations={bookInfo0, xMLNSPrefixMap1, xSISchemaLocation2, customer10, library5, book7},
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
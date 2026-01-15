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
library3_BookInfoType = Class(name="library3::BookInfoType")
library3_BookType = Class(name="library3::BookType")
library3_CustomerType = Class(name="library3::CustomerType")
library3_DocumentRoot = Class(name="library3::DocumentRoot")
library3_EStringToStringMapEntry = Class(name="library3::EStringToStringMapEntry")
library3_LibraryType = Class(name="library3::LibraryType")

# library3_BookInfoType class attributes and methods
library3_BookInfoType_any: Property = Property(name="any", type=StringType)
library3_BookInfoType.attributes={library3_BookInfoType_any}

# library3_BookType class attributes and methods
library3_BookType_title: Property = Property(name="title", type=StringType)
library3_BookType_author: Property = Property(name="author", type=StringType)
library3_BookType_name: Property = Property(name="name", type=StringType)
library3_BookType_isbn: Property = Property(name="isbn", type=StringType)
library3_BookType_pages: Property = Property(name="pages", type=StringType)
library3_BookType_dimension: Property = Property(name="dimension", type=StringType)
library3_BookType_download: Property = Property(name="download", type=StringType)
library3_BookType.attributes={library3_BookType_download, library3_BookType_author, library3_BookType_name, library3_BookType_isbn, library3_BookType_title, library3_BookType_pages, library3_BookType_dimension}

# library3_CustomerType class attributes and methods
library3_CustomerType_firstName: Property = Property(name="firstName", type=StringType)
library3_CustomerType_lastName: Property = Property(name="lastName", type=StringType)
library3_CustomerType_borrowedBookId: Property = Property(name="borrowedBookId", type=StringType)
library3_CustomerType_borrowedBookSince: Property = Property(name="borrowedBookSince", type=StringType)
library3_CustomerType.attributes={library3_CustomerType_firstName, library3_CustomerType_borrowedBookSince, library3_CustomerType_borrowedBookId, library3_CustomerType_lastName}

# library3_DocumentRoot class attributes and methods
library3_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
library3_DocumentRoot.attributes={library3_DocumentRoot_mixed}

# library3_EStringToStringMapEntry class attributes and methods

# library3_LibraryType class attributes and methods

# Relationships
bookInfo0: BinaryAssociation = BinaryAssociation(
    name="bookInfo0",
    ends={
        Property(name="library3_BookInfoType", type=library3_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_BookType", type=library3_BookInfoType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="library3_BookType9", type=library3_LibraryType, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_LibraryType8", type=library3_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="library3_EStringToStringMapEntry", type=library3_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_DocumentRoot", type=library3_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="library3_EStringToStringMapEntry4", type=library3_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_DocumentRoot3", type=library3_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="library3_LibraryType", type=library3_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_DocumentRoot6", type=library3_LibraryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer10: BinaryAssociation = BinaryAssociation(
    name="customer10",
    ends={
        Property(name="library3_CustomerType", type=library3_LibraryType, multiplicity=Multiplicity(1, 1)),
        Property(name="library3_LibraryType11", type=library3_CustomerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library3",
    types={library3_BookInfoType, library3_BookType, library3_CustomerType, library3_DocumentRoot, library3_EStringToStringMapEntry, library3_LibraryType},
    associations={bookInfo0, book7, xMLNSPrefixMap1, xSISchemaLocation2, library5, customer10},
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
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

# Enumerations
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biography")
    }
)

# Classes
eavlibrary_Writer = Class(name="eavlibrary::Writer")
eavlibrary_City = Class(name="eavlibrary::City")
eavlibrary_Book = Class(name="eavlibrary::Book")
eavlibrary_Library = Class(name="eavlibrary::Library")

# eavlibrary_Writer class attributes and methods
eavlibrary_Writer_name: Property = Property(name="name", type=StringType)
eavlibrary_Writer.attributes={eavlibrary_Writer_name}

# eavlibrary_City class attributes and methods
eavlibrary_City_name: Property = Property(name="name", type=StringType)
eavlibrary_City.attributes={eavlibrary_City_name}

# eavlibrary_Book class attributes and methods
eavlibrary_Book_test: Property = Property(name="test", type=StringType)
eavlibrary_Book_title: Property = Property(name="title", type=StringType)
eavlibrary_Book_pages: Property = Property(name="pages", type=StringType)
eavlibrary_Book_category: Property = Property(name="category", type=StringType)
eavlibrary_Book.attributes={eavlibrary_Book_category, eavlibrary_Book_pages, eavlibrary_Book_test, eavlibrary_Book_title}

# eavlibrary_Library class attributes and methods
eavlibrary_Library_name: Property = Property(name="name", type=StringType)
eavlibrary_Library.attributes={eavlibrary_Library_name}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=eavlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=eavlibrary_Writer, multiplicity=Multiplicity(1, 1))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=eavlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=eavlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
city5: BinaryAssociation = BinaryAssociation(
    name="city5",
    ends={
        Property(name="eavlibrary_City", type=eavlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="eavlibrary_Writer6", type=eavlibrary_City, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="eavlibrary_Writer", type=eavlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eavlibrary_Library", type=eavlibrary_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="eavlibrary_Book", type=eavlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eavlibrary_Library3", type=eavlibrary_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="eavlibrary",
    types={eavlibrary_Writer, eavlibrary_City, eavlibrary_Book, eavlibrary_Library, BookCategory},
    associations={author0, books4, city5, writers1, books2},
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
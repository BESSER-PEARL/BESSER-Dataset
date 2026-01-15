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
eavlibrary_Book = Class(name="eavlibrary::Book")
eavlibrary_City = Class(name="eavlibrary::City")
eavlibrary_Library = Class(name="eavlibrary::Library")
eavlibrary_Writer = Class(name="eavlibrary::Writer")
eavlibrary_Pen = Class(name="eavlibrary::Pen")

# eavlibrary_Book class attributes and methods
eavlibrary_Book_title: Property = Property(name="title", type=StringType)
eavlibrary_Book_pages: Property = Property(name="pages", type=StringType)
eavlibrary_Book_category: Property = Property(name="category", type=StringType)
eavlibrary_Book_test: Property = Property(name="test", type=StringType)
eavlibrary_Book.attributes={eavlibrary_Book_test, eavlibrary_Book_pages, eavlibrary_Book_category, eavlibrary_Book_title}

# eavlibrary_City class attributes and methods
eavlibrary_City_name: Property = Property(name="name", type=StringType)
eavlibrary_City.attributes={eavlibrary_City_name}

# eavlibrary_Library class attributes and methods
eavlibrary_Library_name: Property = Property(name="name", type=StringType)
eavlibrary_Library.attributes={eavlibrary_Library_name}

# eavlibrary_Writer class attributes and methods
eavlibrary_Writer_name: Property = Property(name="name", type=StringType)
eavlibrary_Writer_image: Property = Property(name="image", type=StringType)
eavlibrary_Writer_abstract: Property = Property(name="abstract", type=StringType)
eavlibrary_Writer.attributes={eavlibrary_Writer_name, eavlibrary_Writer_image, eavlibrary_Writer_abstract}

# eavlibrary_Pen class attributes and methods
eavlibrary_Pen_name: Property = Property(name="name", type=StringType)
eavlibrary_Pen.attributes={eavlibrary_Pen_name}

# Relationships
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
pens7: BinaryAssociation = BinaryAssociation(
    name="pens7",
    ends={
        Property(name="eavlibrary_Pen", type=eavlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="eavlibrary_Writer8", type=eavlibrary_Pen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="eavlibrary",
    types={eavlibrary_Book, eavlibrary_City, eavlibrary_Library, eavlibrary_Writer, eavlibrary_Pen, BookCategory},
    associations={writers1, books2, author0, books4, city5, pens7},
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
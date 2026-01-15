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
libraryExample_Writer = Class(name="libraryExample::Writer")
libraryExample_Library = Class(name="libraryExample::Library")
libraryExample_SchoolLibrary = Class(name="libraryExample::SchoolLibrary")
Library = Class(name="Library")
libraryExample_Asset = Class(name="libraryExample::Asset")
libraryExample_Book = Class(name="libraryExample::Book")
libraryExample_SchoolBook = Class(name="libraryExample::SchoolBook")
Book = Class(name="Book")
Asset = Class(name="Asset")

# libraryExample_Writer class attributes and methods
libraryExample_Writer_name: Property = Property(name="name", type=StringType)
libraryExample_Writer_lastname: Property = Property(name="lastname", type=StringType)
libraryExample_Writer.attributes={libraryExample_Writer_name, libraryExample_Writer_lastname}

# libraryExample_Library class attributes and methods
libraryExample_Library_name: Property = Property(name="name", type=StringType)
libraryExample_Library.attributes={libraryExample_Library_name}

# libraryExample_SchoolLibrary class attributes and methods
libraryExample_SchoolLibrary_location: Property = Property(name="location", type=StringType)
libraryExample_SchoolLibrary.attributes={libraryExample_SchoolLibrary_location}

# Library class attributes and methods

# libraryExample_Asset class attributes and methods
libraryExample_Asset_value: Property = Property(name="value", type=FloatType)
libraryExample_Asset.attributes={libraryExample_Asset_value}

# libraryExample_Book class attributes and methods
libraryExample_Book_title: Property = Property(name="title", type=StringType)
libraryExample_Book_pages: Property = Property(name="pages", type=IntegerType)
libraryExample_Book_category: Property = Property(name="category", type=StringType)
libraryExample_Book.attributes={libraryExample_Book_title, libraryExample_Book_category, libraryExample_Book_pages}

# libraryExample_SchoolBook class attributes and methods

# Book class attributes and methods

# Asset class attributes and methods

# Relationships
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="libraryExample_Writer", type=libraryExample_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryExample_Library2", type=libraryExample_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writer3: BinaryAssociation = BinaryAssociation(
    name="writer3",
    ends={
        Property(name="Writer", type=libraryExample_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=libraryExample_Writer, multiplicity=Multiplicity(1, 1))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=libraryExample_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writer", type=libraryExample_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="libraryExample_Book", type=libraryExample_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryExample_Library", type=libraryExample_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_libraryExample_SchoolLibrary_Library = Generalization(general=Library, specific=libraryExample_SchoolLibrary)
gen_libraryExample_SchoolBook_Book = Generalization(general=Book, specific=libraryExample_SchoolBook)
gen_libraryExample_SchoolBook_Asset = Generalization(general=Asset, specific=libraryExample_SchoolBook)

# Domain Model
domain_model = DomainModel(
    name="libraryExample",
    types={libraryExample_Writer, libraryExample_Library, libraryExample_SchoolLibrary, Library, libraryExample_Asset, libraryExample_Book, libraryExample_SchoolBook, Book, Asset, BookCategory},
    associations={writers1, writer3, books4, books0},
    generalizations={gen_libraryExample_SchoolLibrary_Library, gen_libraryExample_SchoolBook_Book, gen_libraryExample_SchoolBook_Asset},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
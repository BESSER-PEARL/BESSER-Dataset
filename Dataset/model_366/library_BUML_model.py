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
            EnumerationLiteral(name="SciFi"),
			EnumerationLiteral(name="Biography"),
			EnumerationLiteral(name="GeneralFiction"),
			EnumerationLiteral(name="NonFiction")
    }
)

# Classes
lib_Library = Class(name="lib::Library")
lib_Writer = Class(name="lib::Writer")
lib_Book = Class(name="lib::Book")
lib_LibSys = Class(name="lib::LibSys")

# lib_Library class attributes and methods
lib_Library_name: Property = Property(name="name", type=StringType)
lib_Library_location: Property = Property(name="location", type=StringType)
lib_Library.attributes={lib_Library_location, lib_Library_name}

# lib_Writer class attributes and methods
lib_Writer_name: Property = Property(name="name", type=StringType)
lib_Writer.attributes={lib_Writer_name}

# lib_Book class attributes and methods
lib_Book_title: Property = Property(name="title", type=StringType)
lib_Book_pages: Property = Property(name="pages", type=IntegerType)
lib_Book_category: Property = Property(name="category", type=StringType)
lib_Book.attributes={lib_Book_title, lib_Book_pages, lib_Book_category}

# lib_LibSys class attributes and methods

# Relationships
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="lib_Book", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_Library2", type=lib_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="lib_Writer", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_Library", type=lib_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author3: BinaryAssociation = BinaryAssociation(
    name="author3",
    ends={
        Property(name="lib_Writer5", type=lib_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_Book4", type=lib_Writer, multiplicity=Multiplicity(1, 1))
    }
)
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="lib_Library7", type=lib_LibSys, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_LibSys", type=lib_Library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="lib",
    types={lib_Library, lib_Writer, lib_Book, lib_LibSys, BookCategory},
    associations={books1, writers0, author3, library6},
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
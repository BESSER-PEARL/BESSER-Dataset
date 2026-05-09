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
lazy_Writer = Class(name="lazy_Writer")
lazy_Library = Class(name="lazy_Library")
lazy_Book = Class(name="lazy_Book")

# lazy_Writer class attributes and methods
lazy_Writer_name: Property = Property(name="name", type=StringType)
lazy_Writer.attributes={lazy_Writer_name}

# lazy_Library class attributes and methods
lazy_Library_name: Property = Property(name="name", type=StringType)
lazy_Library.attributes={lazy_Library_name}

# lazy_Book class attributes and methods
lazy_Book_title: Property = Property(name="title", type=StringType)
lazy_Book_pages: Property = Property(name="pages", type=StringType)
lazy_Book_category: Property = Property(name="category", type=StringType)
lazy_Book.attributes={lazy_Book_category, lazy_Book_title, lazy_Book_pages}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=lazy_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=lazy_Writer, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="lazy_Writer", type=lazy_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lazy_Library", type=lazy_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="lazy_Book", type=lazy_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lazy_Library3", type=lazy_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=lazy_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=lazy_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lazy",
    types={lazy_Writer, lazy_Library, lazy_Book, BookCategory},
    associations={author0, writers1, books2, books4},
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
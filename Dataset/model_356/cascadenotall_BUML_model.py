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
cascadenotall_Book = Class(name="cascadenotall::Book")
cascadenotall_Writer = Class(name="cascadenotall::Writer")
cascadenotall_Library = Class(name="cascadenotall::Library")

# cascadenotall_Book class attributes and methods
cascadenotall_Book_title: Property = Property(name="title", type=StringType)
cascadenotall_Book_pages: Property = Property(name="pages", type=StringType)
cascadenotall_Book_category: Property = Property(name="category", type=StringType)
cascadenotall_Book.attributes={cascadenotall_Book_category, cascadenotall_Book_title, cascadenotall_Book_pages}

# cascadenotall_Writer class attributes and methods
cascadenotall_Writer_name: Property = Property(name="name", type=StringType)
cascadenotall_Writer.attributes={cascadenotall_Writer_name}

# cascadenotall_Library class attributes and methods
cascadenotall_Library_name: Property = Property(name="name", type=StringType)
cascadenotall_Library.attributes={cascadenotall_Library_name}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=cascadenotall_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=cascadenotall_Writer, multiplicity=Multiplicity(1, 1))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=cascadenotall_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=cascadenotall_Book, multiplicity=Multiplicity(0, 9999))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="cascadenotall_Writer", type=cascadenotall_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="cascadenotall_Library", type=cascadenotall_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="cascadenotall_Book", type=cascadenotall_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="cascadenotall_Library3", type=cascadenotall_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="cascadenotall",
    types={cascadenotall_Book, cascadenotall_Writer, cascadenotall_Library, BookCategory},
    associations={author0, books4, writers1, books2},
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
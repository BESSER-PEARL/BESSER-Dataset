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
Book_Book = Class(name="Book::Book")
Book_Chapter = Class(name="Book::Chapter")
Book_Summary = Class(name="Book::Summary")
Book_Library = Class(name="Book::Library")

# Book_Book class attributes and methods
Book_Book_title: Property = Property(name="title", type=StringType)
Book_Book.attributes={Book_Book_title}

# Book_Chapter class attributes and methods
Book_Chapter_title: Property = Property(name="title", type=StringType)
Book_Chapter_nbPages: Property = Property(name="nbPages", type=IntegerType)
Book_Chapter_author: Property = Property(name="author", type=StringType)
Book_Chapter.attributes={Book_Chapter_nbPages, Book_Chapter_author, Book_Chapter_title}

# Book_Summary class attributes and methods
Book_Summary_content: Property = Property(name="content", type=StringType)
Book_Summary_nbWords: Property = Property(name="nbWords", type=IntegerType)
Book_Summary.attributes={Book_Summary_content, Book_Summary_nbWords}

# Book_Library class attributes and methods

# Relationships
chapters0: BinaryAssociation = BinaryAssociation(
    name="chapters0",
    ends={
        Property(name="Book_Chapter", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Book", type=Book_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digest1: BinaryAssociation = BinaryAssociation(
    name="digest1",
    ends={
        Property(name="Book_Summary", type=Book_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Chapter2", type=Book_Summary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="Book_Book4", type=Book_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Library", type=Book_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Book",
    types={Book_Book, Book_Chapter, Book_Summary, Book_Library},
    associations={chapters0, digest1, books3},
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
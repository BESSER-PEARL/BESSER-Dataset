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
library_Library = Class(name="library::Library")
library_Book = Class(name="library::Book")
library_Writer = Class(name="library::Writer")
library_Member = Class(name="library::Member")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book.attributes={library_Book_pages, library_Book_title}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Member class attributes and methods
library_Member_name: Property = Property(name="name", type=StringType)
library_Member_id: Property = Property(name="id", type=IntegerType)
library_Member.attributes={library_Member_id, library_Member_name}

# Relationships
author5: BinaryAssociation = BinaryAssociation(
    name="author5",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(0, 1))
    }
)
books6: BinaryAssociation = BinaryAssociation(
    name="books6",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
borrowedBooks7: BinaryAssociation = BinaryAssociation(
    name="borrowedBooks7",
    ends={
        Property(name="library_Book9", type=library_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Member8", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="library_Member", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Book, library_Writer, library_Member},
    associations={author5, books6, borrowedBooks7, books0, writers1, members3},
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
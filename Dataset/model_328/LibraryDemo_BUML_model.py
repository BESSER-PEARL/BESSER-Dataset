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
Category: Enumeration = Enumeration(
    name="Category",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="POETRY"),
			EnumerationLiteral(name="SCIENCE"),
			EnumerationLiteral(name="FICTION")
    }
)

# Classes
Library_Writer = Class(name="Library_Writer")
Library_Library = Class(name="Library_Library")
Library_Book = Class(name="Library_Book")

# Library_Writer class attributes and methods
Library_Writer_id: Property = Property(name="id", type=IntegerType)
Library_Writer_name: Property = Property(name="name", type=StringType)
Library_Writer.attributes={Library_Writer_id, Library_Writer_name}

# Library_Library class attributes and methods
Library_Library_name: Property = Property(name="name", type=StringType)
Library_Library_id: Property = Property(name="id", type=IntegerType)
Library_Library.attributes={Library_Library_id, Library_Library_name}

# Library_Book class attributes and methods
Library_Book_pages: Property = Property(name="pages", type=IntegerType)
Library_Book_category: Property = Property(name="category", type=StringType)
Library_Book_blurb: Property = Property(name="blurb", type=StringType)
Library_Book_title: Property = Property(name="title", type=StringType)
Library_Book.attributes={Library_Book_blurb, Library_Book_pages, Library_Book_title, Library_Book_category}

# Relationships
writer0: BinaryAssociation = BinaryAssociation(
    name="writer0",
    ends={
        Property(name="Writer", type=Library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=Library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
library1: BinaryAssociation = BinaryAssociation(
    name="library1",
    ends={
        Property(name="Library", type=Library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books2", type=Library_Library, multiplicity=Multiplicity(1, 1))
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="Book", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books7: BinaryAssociation = BinaryAssociation(
    name="books7",
    ends={
        Property(name="Book8", type=Library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writer", type=Library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
library9: BinaryAssociation = BinaryAssociation(
    name="library9",
    ends={
        Property(name="Library10", type=Library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=Library_Library, multiplicity=Multiplicity(1, 1))
    }
)
writers4: BinaryAssociation = BinaryAssociation(
    name="writers4",
    ends={
        Property(name="Writer6", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library5", type=Library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Writer, Library_Library, Library_Book, Category},
    associations={writer0, library1, books3, books7, library9, writers4},
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
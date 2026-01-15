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
elements_Writer = Class(name="elements::Writer")
elements_Book = Class(name="elements::Book")

# elements_Writer class attributes and methods
elements_Writer_name: Property = Property(name="name", type=StringType)
elements_Writer.attributes={elements_Writer_name}

# elements_Book class attributes and methods
elements_Book_category: Property = Property(name="category", type=StringType)
elements_Book_title: Property = Property(name="title", type=StringType)
elements_Book_pages: Property = Property(name="pages", type=StringType)
elements_Book.attributes={elements_Book_pages, elements_Book_category, elements_Book_title}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=elements_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=elements_Writer, multiplicity=Multiplicity(1, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="Book", type=elements_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=elements_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="elements",
    types={elements_Writer, elements_Book, BookCategory},
    associations={author0, books1},
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
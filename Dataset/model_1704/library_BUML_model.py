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
Library_Writer = Class(name="Library::Writer")
Library_Book = Class(name="Library::Book")

# Library_Writer class attributes and methods
Library_Writer_name: Property = Property(name="name", type=StringType)
Library_Writer.attributes={Library_Writer_name}

# Library_Book class attributes and methods
Library_Book_title: Property = Property(name="title", type=StringType)
Library_Book_pages: Property = Property(name="pages", type=IntegerType)
Library_Book.attributes={Library_Book_pages, Library_Book_title}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Library_Writer", type=Library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Book", type=Library_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Writer, Library_Book},
    associations={author0},
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
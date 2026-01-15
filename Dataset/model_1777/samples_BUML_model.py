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
samples_Author = Class(name="samples::Author")
samples_Book = Class(name="samples::Book")

# samples_Author class attributes and methods
samples_Author_name: Property = Property(name="name", type=StringType)
samples_Author.attributes={samples_Author_name}

# samples_Book class attributes and methods
samples_Book_title: Property = Property(name="title", type=StringType)
samples_Book.attributes={samples_Book_title}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="samples_Book", type=samples_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="samples_Author", type=samples_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="samples_Author3", type=samples_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="samples_Book2", type=samples_Author, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="samples",
    types={samples_Author, samples_Book},
    associations={books0, author1},
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
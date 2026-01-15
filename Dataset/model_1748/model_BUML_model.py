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
model_Library = Class(name="model::Library")
model_Book = Class(name="model::Book")
model_Author = Class(name="model::Author")

# model_Library class attributes and methods

# model_Book class attributes and methods
model_Book_title: Property = Property(name="title", type=StringType)
model_Book.attributes={model_Book_title}

# model_Author class attributes and methods
model_Author_firstName: Property = Property(name="firstName", type=StringType)
model_Author_lastName: Property = Property(name="lastName", type=StringType)
model_Author.attributes={model_Author_firstName, model_Author_lastName}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="model_Book", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="model_Author", type=model_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Book2", type=model_Author, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Library, model_Book, model_Author},
    associations={books0, authors1},
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
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
resourceunload_Book = Class(name="resourceunload::Book")
resourceunload_Library = Class(name="resourceunload::Library")

# resourceunload_Book class attributes and methods
resourceunload_Book_title: Property = Property(name="title", type=StringType)
resourceunload_Book.attributes={resourceunload_Book_title}

# resourceunload_Library class attributes and methods
resourceunload_Library_name: Property = Property(name="name", type=StringType)
resourceunload_Library.attributes={resourceunload_Library_name}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="resourceunload_Book", type=resourceunload_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceunload_Library", type=resourceunload_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="resourceunload",
    types={resourceunload_Book, resourceunload_Library},
    associations={books0},
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
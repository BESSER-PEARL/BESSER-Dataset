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
example_Folder = Class(name="example::Folder")

# example_Folder class attributes and methods
example_Folder_name: Property = Property(name="name", type=StringType)
example_Folder.attributes={example_Folder_name}

# Relationships
subFolder1: BinaryAssociation = BinaryAssociation(
    name="subFolder1",
    ends={
        Property(name="example_Folder", type=example_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="example_Folder0", type=example_Folder, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_Folder},
    associations={subFolder1},
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
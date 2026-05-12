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
Web_User = Class(name="Web_User", is_abstract=True)
Memory_Interface = Class(name="Memory_Interface")

# Web_User class attributes and methods

# Memory_Interface class attributes and methods

# Relationships
Processor_Memory: BinaryAssociation = BinaryAssociation(
    name="Processor_Memory",
    ends={
        Property(name="processor0", type=Web_User, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory1", type=Memory_Interface, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b2434540_f730_4070_9917_19d3ea72234a",
    types={Web_User, Memory_Interface},
    associations={Processor_Memory},
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
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
typeA_BlockA = Class(name="typeA::BlockA")
typeA_PortA = Class(name="typeA::PortA")

# typeA_BlockA class attributes and methods

# typeA_PortA class attributes and methods
typeA_PortA_name: Property = Property(name="name", type=StringType)
typeA_PortA.attributes={typeA_PortA_name}

# Relationships
inputPorts0: BinaryAssociation = BinaryAssociation(
    name="inputPorts0",
    ends={
        Property(name="typeA_PortA", type=typeA_BlockA, multiplicity=Multiplicity(1, 1)),
        Property(name="typeA_BlockA", type=typeA_PortA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts1: BinaryAssociation = BinaryAssociation(
    name="outputPorts1",
    ends={
        Property(name="typeA_PortA3", type=typeA_BlockA, multiplicity=Multiplicity(1, 1)),
        Property(name="typeA_BlockA2", type=typeA_PortA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="typeA",
    types={typeA_BlockA, typeA_PortA},
    associations={inputPorts0, outputPorts1},
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
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
TypeA_BlockA = Class(name="TypeA::BlockA")
TypeA_PortA = Class(name="TypeA::PortA")

# TypeA_BlockA class attributes and methods

# TypeA_PortA class attributes and methods
TypeA_PortA_name: Property = Property(name="name", type=StringType)
TypeA_PortA.attributes={TypeA_PortA_name}

# Relationships
inputPorts0: BinaryAssociation = BinaryAssociation(
    name="inputPorts0",
    ends={
        Property(name="TypeA_PortA", type=TypeA_BlockA, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_BlockA", type=TypeA_PortA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts1: BinaryAssociation = BinaryAssociation(
    name="outputPorts1",
    ends={
        Property(name="TypeA_PortA3", type=TypeA_BlockA, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_BlockA2", type=TypeA_PortA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeA",
    types={TypeA_BlockA, TypeA_PortA},
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
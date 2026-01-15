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
TypeB_PortB = Class(name="TypeB::PortB", is_abstract=True)
PortB = Class(name="PortB")
TypeB_BlockB = Class(name="TypeB::BlockB")
TypeB_InPortB = Class(name="TypeB::InPortB")
TypeB_OutPortB = Class(name="TypeB::OutPortB")

# TypeB_PortB class attributes and methods
TypeB_PortB_name: Property = Property(name="name", type=StringType)
TypeB_PortB.attributes={TypeB_PortB_name}

# PortB class attributes and methods

# TypeB_BlockB class attributes and methods

# TypeB_InPortB class attributes and methods

# TypeB_OutPortB class attributes and methods

# Relationships
inputPorts0: BinaryAssociation = BinaryAssociation(
    name="inputPorts0",
    ends={
        Property(name="TypeB_InPortB", type=TypeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_BlockB", type=TypeB_InPortB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts1: BinaryAssociation = BinaryAssociation(
    name="outputPorts1",
    ends={
        Property(name="TypeB_OutPortB", type=TypeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_BlockB2", type=TypeB_OutPortB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TypeB_InPortB_PortB = Generalization(general=PortB, specific=TypeB_InPortB)
gen_TypeB_OutPortB_PortB = Generalization(general=PortB, specific=TypeB_OutPortB)

# Domain Model
domain_model = DomainModel(
    name="TypeB",
    types={TypeB_PortB, PortB, TypeB_BlockB, TypeB_InPortB, TypeB_OutPortB},
    associations={inputPorts0, outputPorts1},
    generalizations={gen_TypeB_InPortB_PortB, gen_TypeB_OutPortB_PortB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
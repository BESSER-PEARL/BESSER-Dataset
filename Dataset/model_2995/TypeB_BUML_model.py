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
typeB_BlockB = Class(name="typeB::BlockB")
typeB_InPortB = Class(name="typeB::InPortB")
typeB_OutPortB = Class(name="typeB::OutPortB")
typeB_PortB = Class(name="typeB::PortB", is_abstract=True)
PortB = Class(name="PortB")

# typeB_BlockB class attributes and methods

# typeB_InPortB class attributes and methods

# typeB_OutPortB class attributes and methods

# typeB_PortB class attributes and methods
typeB_PortB_id: Property = Property(name="id", type=IntegerType)
typeB_PortB.attributes={typeB_PortB_id}

# PortB class attributes and methods

# Relationships
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="typeB_BlockB5", type=typeB_OutPortB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_OutPortB4", type=typeB_BlockB, multiplicity=Multiplicity(1, 1))
    }
)
inputPorts0: BinaryAssociation = BinaryAssociation(
    name="inputPorts0",
    ends={
        Property(name="typeB_InPortB", type=typeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_BlockB", type=typeB_InPortB, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputPorts1: BinaryAssociation = BinaryAssociation(
    name="outputPorts1",
    ends={
        Property(name="typeB_OutPortB", type=typeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_BlockB2", type=typeB_OutPortB, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_typeB_OutPortB_PortB = Generalization(general=PortB, specific=typeB_OutPortB)
gen_typeB_InPortB_PortB = Generalization(general=PortB, specific=typeB_InPortB)

# Domain Model
domain_model = DomainModel(
    name="typeB",
    types={typeB_BlockB, typeB_InPortB, typeB_OutPortB, typeB_PortB, PortB},
    associations={block3, inputPorts0, outputPorts1},
    generalizations={gen_typeB_OutPortB_PortB, gen_typeB_InPortB_PortB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
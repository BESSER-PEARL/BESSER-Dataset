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
typeB_InPortB = Class(name="typeB::InPortB")
typeB_OutPortB = Class(name="typeB::OutPortB")
typeB_PortB = Class(name="typeB::PortB", is_abstract=True)
PortB = Class(name="PortB")
typeB_BlockB = Class(name="typeB::BlockB")

# typeB_InPortB class attributes and methods

# typeB_OutPortB class attributes and methods

# typeB_PortB class attributes and methods
typeB_PortB_name: Property = Property(name="name", type=StringType)
typeB_PortB.attributes={typeB_PortB_name}

# PortB class attributes and methods

# typeB_BlockB class attributes and methods

# Relationships
inputPorts0: BinaryAssociation = BinaryAssociation(
    name="inputPorts0",
    ends={
        Property(name="typeB_InPortB", type=typeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_BlockB", type=typeB_InPortB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts1: BinaryAssociation = BinaryAssociation(
    name="outputPorts1",
    ends={
        Property(name="typeB_OutPortB", type=typeB_BlockB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_BlockB2", type=typeB_OutPortB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_typeB_InPortB_PortB = Generalization(general=PortB, specific=typeB_InPortB)
gen_typeB_OutPortB_PortB = Generalization(general=PortB, specific=typeB_OutPortB)

# Domain Model
domain_model = DomainModel(
    name="typeB",
    types={typeB_InPortB, typeB_OutPortB, typeB_PortB, PortB, typeB_BlockB},
    associations={inputPorts0, outputPorts1},
    generalizations={gen_typeB_InPortB_PortB, gen_typeB_OutPortB_PortB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
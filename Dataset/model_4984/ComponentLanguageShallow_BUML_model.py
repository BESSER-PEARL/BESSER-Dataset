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
ComponentLanguageShallow_Port = Class(name="ComponentLanguageShallow::Port")
ComponentLanguageShallow_Connector = Class(name="ComponentLanguageShallow::Connector")
ComponentLanguageShallow_InPort = Class(name="ComponentLanguageShallow::InPort")
Port = Class(name="Port")
ComponentLanguageShallow_OutPort = Class(name="ComponentLanguageShallow::OutPort")
ComponentLanguageShallow_Component = Class(name="ComponentLanguageShallow::Component")

# ComponentLanguageShallow_Port class attributes and methods

# ComponentLanguageShallow_Connector class attributes and methods

# ComponentLanguageShallow_InPort class attributes and methods

# Port class attributes and methods

# ComponentLanguageShallow_OutPort class attributes and methods

# ComponentLanguageShallow_Component class attributes and methods

# Relationships
ports0: BinaryAssociation = BinaryAssociation(
    name="ports0",
    ends={
        Property(name="ComponentLanguageShallow_Port", type=ComponentLanguageShallow_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageShallow_Component", type=ComponentLanguageShallow_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in1: BinaryAssociation = BinaryAssociation(
    name="in1",
    ends={
        Property(name="ComponentLanguageShallow_Port2", type=ComponentLanguageShallow_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageShallow_Connector", type=ComponentLanguageShallow_Port, multiplicity=Multiplicity(0, 9999))
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="ComponentLanguageShallow_Port5", type=ComponentLanguageShallow_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageShallow_Connector4", type=ComponentLanguageShallow_Port, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ComponentLanguageShallow_InPort_Port = Generalization(general=Port, specific=ComponentLanguageShallow_InPort)
gen_ComponentLanguageShallow_OutPort_Port = Generalization(general=Port, specific=ComponentLanguageShallow_OutPort)

# Domain Model
domain_model = DomainModel(
    name="ComponentLanguageShallow",
    types={ComponentLanguageShallow_Port, ComponentLanguageShallow_Connector, ComponentLanguageShallow_InPort, Port, ComponentLanguageShallow_OutPort, ComponentLanguageShallow_Component},
    associations={ports0, in1, out3},
    generalizations={gen_ComponentLanguageShallow_InPort_Port, gen_ComponentLanguageShallow_OutPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
ComponentLanguageDeep_Component = Class(name="ComponentLanguageDeep::Component")
ComponentLanguageDeep_Port = Class(name="ComponentLanguageDeep::Port", is_abstract=True)
ComponentLanguageDeep_InPort = Class(name="ComponentLanguageDeep::InPort")
Port = Class(name="Port")
ComponentLanguageDeep_OutPort = Class(name="ComponentLanguageDeep::OutPort")
ComponentLanguageDeep_InPortInstance = Class(name="ComponentLanguageDeep::InPortInstance")
PortInstance = Class(name="PortInstance")
ComponentLanguageDeep_OutPortInstance = Class(name="ComponentLanguageDeep::OutPortInstance")
ComponentLanguageDeep_ComponentInstance = Class(name="ComponentLanguageDeep::ComponentInstance")
ComponentLanguageDeep_Connector = Class(name="ComponentLanguageDeep::Connector")
ComponentLanguageDeep_PortInstance = Class(name="ComponentLanguageDeep::PortInstance")
ComponentLanguageDeep_ConnectorInstance = Class(name="ComponentLanguageDeep::ConnectorInstance")

# ComponentLanguageDeep_Component class attributes and methods

# ComponentLanguageDeep_Port class attributes and methods

# ComponentLanguageDeep_InPort class attributes and methods

# Port class attributes and methods

# ComponentLanguageDeep_OutPort class attributes and methods

# ComponentLanguageDeep_InPortInstance class attributes and methods

# PortInstance class attributes and methods

# ComponentLanguageDeep_OutPortInstance class attributes and methods

# ComponentLanguageDeep_ComponentInstance class attributes and methods

# ComponentLanguageDeep_Connector class attributes and methods

# ComponentLanguageDeep_PortInstance class attributes and methods

# ComponentLanguageDeep_ConnectorInstance class attributes and methods

# Relationships
ports0: BinaryAssociation = BinaryAssociation(
    name="ports0",
    ends={
        Property(name="ComponentLanguageDeep_Port", type=ComponentLanguageDeep_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_Component", type=ComponentLanguageDeep_Port, multiplicity=Multiplicity(0, 9999))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="ComponentLanguageDeep_InPort", type=ComponentLanguageDeep_InPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_InPortInstance", type=ComponentLanguageDeep_InPort, multiplicity=Multiplicity(0, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="ComponentLanguageDeep_OutPort", type=ComponentLanguageDeep_OutPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_OutPortInstance", type=ComponentLanguageDeep_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
in1: BinaryAssociation = BinaryAssociation(
    name="in1",
    ends={
        Property(name="ComponentLanguageDeep_Port2", type=ComponentLanguageDeep_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_Connector", type=ComponentLanguageDeep_Port, multiplicity=Multiplicity(0, 9999))
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="ComponentLanguageDeep_Port5", type=ComponentLanguageDeep_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_Connector4", type=ComponentLanguageDeep_Port, multiplicity=Multiplicity(0, 9999))
    }
)
in12: BinaryAssociation = BinaryAssociation(
    name="in12",
    ends={
        Property(name="ComponentLanguageDeep_PortInstance13", type=ComponentLanguageDeep_ConnectorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_ConnectorInstance", type=ComponentLanguageDeep_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
out14: BinaryAssociation = BinaryAssociation(
    name="out14",
    ends={
        Property(name="ComponentLanguageDeep_PortInstance16", type=ComponentLanguageDeep_ConnectorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_ConnectorInstance15", type=ComponentLanguageDeep_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="ComponentLanguageDeep_Connector19", type=ComponentLanguageDeep_ConnectorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_ConnectorInstance18", type=ComponentLanguageDeep_Connector, multiplicity=Multiplicity(0, 1))
    }
)
ports8: BinaryAssociation = BinaryAssociation(
    name="ports8",
    ends={
        Property(name="ComponentLanguageDeep_PortInstance", type=ComponentLanguageDeep_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_ComponentInstance", type=ComponentLanguageDeep_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="ComponentLanguageDeep_Component11", type=ComponentLanguageDeep_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentLanguageDeep_ComponentInstance10", type=ComponentLanguageDeep_Component, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ComponentLanguageDeep_InPort_Port = Generalization(general=Port, specific=ComponentLanguageDeep_InPort)
gen_ComponentLanguageDeep_OutPort_Port = Generalization(general=Port, specific=ComponentLanguageDeep_OutPort)
gen_ComponentLanguageDeep_InPortInstance_PortInstance = Generalization(general=PortInstance, specific=ComponentLanguageDeep_InPortInstance)
gen_ComponentLanguageDeep_OutPortInstance_PortInstance = Generalization(general=PortInstance, specific=ComponentLanguageDeep_OutPortInstance)

# Domain Model
domain_model = DomainModel(
    name="ComponentLanguageDeep",
    types={ComponentLanguageDeep_Component, ComponentLanguageDeep_Port, ComponentLanguageDeep_InPort, Port, ComponentLanguageDeep_OutPort, ComponentLanguageDeep_InPortInstance, PortInstance, ComponentLanguageDeep_OutPortInstance, ComponentLanguageDeep_ComponentInstance, ComponentLanguageDeep_Connector, ComponentLanguageDeep_PortInstance, ComponentLanguageDeep_ConnectorInstance},
    associations={ports0, type6, type7, in1, out3, in12, out14, type17, ports8, type9},
    generalizations={gen_ComponentLanguageDeep_InPort_Port, gen_ComponentLanguageDeep_OutPort_Port, gen_ComponentLanguageDeep_InPortInstance_PortInstance, gen_ComponentLanguageDeep_OutPortInstance_PortInstance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
WT_WTComponents = Class(name="WT::WTComponents")
WT_Subsystem = Class(name="WT::Subsystem")
DocumentElt = Class(name="DocumentElt")
WT_Architecture = Class(name="WT::Architecture")
WT_ControlSubsystem = Class(name="WT::ControlSubsystem")
WT_Component = Class(name="WT::Component")
WT_Connector = Class(name="WT::Connector")
WT_InPort = Class(name="WT::InPort")
WT_OutPort = Class(name="WT::OutPort")
WT_StateMachine = Class(name="WT::StateMachine")
WT_Vertex = Class(name="WT::Vertex", is_abstract=True)
WT_Edge = Class(name="WT::Edge")
WT_InitialState = Class(name="WT::InitialState")
Vertex = Class(name="Vertex")
WT_SimpleState = Class(name="WT::SimpleState")
WT_Port = Class(name="WT::Port", is_abstract=True)
Port = Class(name="Port")
WT_DocumentElt = Class(name="WT::DocumentElt", is_abstract=True)

# WT_WTComponents class attributes and methods
WT_WTComponents_name: Property = Property(name="name", type=StringType)
WT_WTComponents.attributes={WT_WTComponents_name}

# WT_Subsystem class attributes and methods
WT_Subsystem_name: Property = Property(name="name", type=StringType)
WT_Subsystem.attributes={WT_Subsystem_name}

# DocumentElt class attributes and methods

# WT_Architecture class attributes and methods
WT_Architecture_name: Property = Property(name="name", type=StringType)
WT_Architecture.attributes={WT_Architecture_name}

# WT_ControlSubsystem class attributes and methods
WT_ControlSubsystem_name: Property = Property(name="name", type=StringType)
WT_ControlSubsystem.attributes={WT_ControlSubsystem_name}

# WT_Component class attributes and methods
WT_Component_label: Property = Property(name="label", type=StringType)
WT_Component.attributes={WT_Component_label}

# WT_Connector class attributes and methods

# WT_InPort class attributes and methods

# WT_OutPort class attributes and methods

# WT_StateMachine class attributes and methods
WT_StateMachine_isPublic: Property = Property(name="isPublic", type=BooleanType)
WT_StateMachine_name: Property = Property(name="name", type=StringType)
WT_StateMachine.attributes={WT_StateMachine_name, WT_StateMachine_isPublic}

# WT_Vertex class attributes and methods

# WT_Edge class attributes and methods

# WT_InitialState class attributes and methods

# Vertex class attributes and methods

# WT_SimpleState class attributes and methods

# WT_Port class attributes and methods
WT_Port_label: Property = Property(name="label", type=StringType)
WT_Port_isPublic: Property = Property(name="isPublic", type=BooleanType)
WT_Port.attributes={WT_Port_isPublic, WT_Port_label}

# Port class attributes and methods

# WT_DocumentElt class attributes and methods
WT_DocumentElt_name: Property = Property(name="name", type=StringType)
WT_DocumentElt_description: Property = Property(name="description", type=StringType)
WT_DocumentElt.attributes={WT_DocumentElt_description, WT_DocumentElt_name}

# Relationships
subsystems0: BinaryAssociation = BinaryAssociation(
    name="subsystems0",
    ends={
        Property(name="WT_Subsystem", type=WT_WTComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_WTComponents", type=WT_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing22: BinaryAssociation = BinaryAssociation(
    name="outgoing22",
    ends={
        Property(name="Edge", type=WT_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=WT_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming23: BinaryAssociation = BinaryAssociation(
    name="incoming23",
    ends={
        Property(name="Edge24", type=WT_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=WT_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
subsystems2: BinaryAssociation = BinaryAssociation(
    name="subsystems2",
    ends={
        Property(name="WT_Subsystem3", type=WT_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Subsystem1", type=WT_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ensembles4: BinaryAssociation = BinaryAssociation(
    name="ensembles4",
    ends={
        Property(name="WT_Architecture", type=WT_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Subsystem5", type=WT_Architecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
beh6: BinaryAssociation = BinaryAssociation(
    name="beh6",
    ends={
        Property(name="WT_ControlSubsystem", type=WT_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Subsystem7", type=WT_ControlSubsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="WT_Component", type=WT_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Architecture9", type=WT_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors10: BinaryAssociation = BinaryAssociation(
    name="connectors10",
    ends={
        Property(name="WT_Connector", type=WT_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Architecture11", type=WT_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPort12: BinaryAssociation = BinaryAssociation(
    name="inPort12",
    ends={
        Property(name="WT_InPort", type=WT_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Connector13", type=WT_InPort, multiplicity=Multiplicity(0, 1))
    }
)
outPort14: BinaryAssociation = BinaryAssociation(
    name="outPort14",
    ends={
        Property(name="WT_OutPort", type=WT_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Connector15", type=WT_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
states16: BinaryAssociation = BinaryAssociation(
    name="states16",
    ends={
        Property(name="WT_StateMachine", type=WT_ControlSubsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_ControlSubsystem17", type=WT_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states18: BinaryAssociation = BinaryAssociation(
    name="states18",
    ends={
        Property(name="WT_Vertex", type=WT_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_StateMachine19", type=WT_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions20: BinaryAssociation = BinaryAssociation(
    name="transitions20",
    ends={
        Property(name="WT_Edge", type=WT_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_StateMachine21", type=WT_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="Vertex", type=WT_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=WT_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="Vertex27", type=WT_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=WT_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
ports28: BinaryAssociation = BinaryAssociation(
    name="ports28",
    ends={
        Property(name="WT_Port", type=WT_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Component29", type=WT_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states30: BinaryAssociation = BinaryAssociation(
    name="states30",
    ends={
        Property(name="WT_StateMachine32", type=WT_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Component31", type=WT_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_WT_Vertex_DocumentElt = Generalization(general=DocumentElt, specific=WT_Vertex)
gen_WT_Edge_DocumentElt = Generalization(general=DocumentElt, specific=WT_Edge)
gen_WT_InitialState_Vertex = Generalization(general=Vertex, specific=WT_InitialState)
gen_WT_SimpleState_Vertex = Generalization(general=Vertex, specific=WT_SimpleState)
gen_WT_InPort_Port = Generalization(general=Port, specific=WT_InPort)
gen_WT_OutPort_Port = Generalization(general=Port, specific=WT_OutPort)

# Domain Model
domain_model = DomainModel(
    name="WT",
    types={WT_WTComponents, WT_Subsystem, DocumentElt, WT_Architecture, WT_ControlSubsystem, WT_Component, WT_Connector, WT_InPort, WT_OutPort, WT_StateMachine, WT_Vertex, WT_Edge, WT_InitialState, Vertex, WT_SimpleState, WT_Port, Port, WT_DocumentElt},
    associations={subsystems0, outgoing22, incoming23, subsystems2, ensembles4, beh6, elements8, connectors10, inPort12, outPort14, states16, states18, transitions20, source25, target26, ports28, states30},
    generalizations={gen_WT_Vertex_DocumentElt, gen_WT_Edge_DocumentElt, gen_WT_InitialState_Vertex, gen_WT_SimpleState_Vertex, gen_WT_InPort_Port, gen_WT_OutPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
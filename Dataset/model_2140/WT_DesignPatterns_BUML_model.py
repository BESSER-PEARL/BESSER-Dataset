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
WT_Component = Class(name="WT::Component")
WT_StateMachine = Class(name="WT::StateMachine")
WT_Architecture = Class(name="WT::Architecture")
WT_ControlSubsystem = Class(name="WT::ControlSubsystem")
WT_InitialState = Class(name="WT::InitialState")
Vertex = Class(name="Vertex")
WT_SimpleState = Class(name="WT::SimpleState")
WT_Port = Class(name="WT::Port", is_abstract=True)
WT_Vertex = Class(name="WT::Vertex", is_abstract=True)
WT_Edge = Class(name="WT::Edge")
DocumentElt = Class(name="DocumentElt")
WT_InPort = Class(name="WT::InPort")
Port = Class(name="Port")
WT_OutPort = Class(name="WT::OutPort")
WT_DocumentElt = Class(name="WT::DocumentElt", is_abstract=True)

# WT_WTComponents class attributes and methods
WT_WTComponents_name: Property = Property(name="name", type=StringType)
WT_WTComponents.attributes={WT_WTComponents_name}

# WT_Subsystem class attributes and methods
WT_Subsystem_name: Property = Property(name="name", type=StringType)
WT_Subsystem.attributes={WT_Subsystem_name}

# WT_Component class attributes and methods
WT_Component_label: Property = Property(name="label", type=StringType)
WT_Component.attributes={WT_Component_label}

# WT_StateMachine class attributes and methods
WT_StateMachine_name: Property = Property(name="name", type=StringType)
WT_StateMachine.attributes={WT_StateMachine_name}

# WT_Architecture class attributes and methods
WT_Architecture_name: Property = Property(name="name", type=StringType)
WT_Architecture.attributes={WT_Architecture_name}

# WT_ControlSubsystem class attributes and methods
WT_ControlSubsystem_name: Property = Property(name="name", type=StringType)
WT_ControlSubsystem.attributes={WT_ControlSubsystem_name}

# WT_InitialState class attributes and methods

# Vertex class attributes and methods

# WT_SimpleState class attributes and methods

# WT_Port class attributes and methods
WT_Port_label: Property = Property(name="label", type=StringType)
WT_Port.attributes={WT_Port_label}

# WT_Vertex class attributes and methods

# WT_Edge class attributes and methods

# DocumentElt class attributes and methods

# WT_InPort class attributes and methods

# Port class attributes and methods

# WT_OutPort class attributes and methods

# WT_DocumentElt class attributes and methods
WT_DocumentElt_name: Property = Property(name="name", type=StringType)
WT_DocumentElt_description: Property = Property(name="description", type=StringType)
WT_DocumentElt.attributes={WT_DocumentElt_name, WT_DocumentElt_description}

# Relationships
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="WT_Component", type=WT_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Architecture9", type=WT_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states10: BinaryAssociation = BinaryAssociation(
    name="states10",
    ends={
        Property(name="WT_StateMachine", type=WT_ControlSubsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_ControlSubsystem11", type=WT_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subsystems0: BinaryAssociation = BinaryAssociation(
    name="subsystems0",
    ends={
        Property(name="WT_Subsystem", type=WT_WTComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_WTComponents", type=WT_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="Vertex", type=WT_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=WT_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="Vertex21", type=WT_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=WT_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
ports22: BinaryAssociation = BinaryAssociation(
    name="ports22",
    ends={
        Property(name="WT_Port", type=WT_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Component23", type=WT_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="WT_Vertex", type=WT_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_StateMachine13", type=WT_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions14: BinaryAssociation = BinaryAssociation(
    name="transitions14",
    ends={
        Property(name="WT_Edge", type=WT_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_StateMachine15", type=WT_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing16: BinaryAssociation = BinaryAssociation(
    name="outgoing16",
    ends={
        Property(name="Edge", type=WT_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=WT_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming17: BinaryAssociation = BinaryAssociation(
    name="incoming17",
    ends={
        Property(name="Edge18", type=WT_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=WT_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
states24: BinaryAssociation = BinaryAssociation(
    name="states24",
    ends={
        Property(name="WT_StateMachine26", type=WT_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="WT_Component25", type=WT_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_WT_InitialState_Vertex = Generalization(general=Vertex, specific=WT_InitialState)
gen_WT_SimpleState_Vertex = Generalization(general=Vertex, specific=WT_SimpleState)
gen_WT_Vertex_DocumentElt = Generalization(general=DocumentElt, specific=WT_Vertex)
gen_WT_Edge_DocumentElt = Generalization(general=DocumentElt, specific=WT_Edge)
gen_WT_InPort_Port = Generalization(general=Port, specific=WT_InPort)
gen_WT_OutPort_Port = Generalization(general=Port, specific=WT_OutPort)

# Domain Model
domain_model = DomainModel(
    name="WT",
    types={WT_WTComponents, WT_Subsystem, WT_Component, WT_StateMachine, WT_Architecture, WT_ControlSubsystem, WT_InitialState, Vertex, WT_SimpleState, WT_Port, WT_Vertex, WT_Edge, DocumentElt, WT_InPort, Port, WT_OutPort, WT_DocumentElt},
    associations={elements8, states10, subsystems0, subsystems2, ensembles4, beh6, source19, target20, ports22, states12, transitions14, outgoing16, incoming17, states24},
    generalizations={gen_WT_InitialState_Vertex, gen_WT_SimpleState_Vertex, gen_WT_Vertex_DocumentElt, gen_WT_Edge_DocumentElt, gen_WT_InPort_Port, gen_WT_OutPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
dslComponent_StateMachine = Class(name="dslComponent::StateMachine")
dslComponent_Vertex = Class(name="dslComponent::Vertex", is_abstract=True)
dslComponent_Edge = Class(name="dslComponent::Edge")
DocumElt = Class(name="DocumElt")
dslComponent_WTComponents = Class(name="dslComponent::WTComponents")
dslComponent_Subsystem = Class(name="dslComponent::Subsystem")
dslComponent_ControlSubsystem = Class(name="dslComponent::ControlSubsystem")
dslComponent_Component = Class(name="dslComponent::Component")
dslComponent_Port = Class(name="dslComponent::Port", is_abstract=True)
dslComponent_SimpleState = Class(name="dslComponent::SimpleState")
Vertex = Class(name="Vertex")
dslComponent_InitialState = Class(name="dslComponent::InitialState")
dslComponent_DocumElt = Class(name="dslComponent::DocumElt", is_abstract=True)
dslComponent_InPort = Class(name="dslComponent::InPort")
Port = Class(name="Port")
dslComponent_OutPort = Class(name="dslComponent::OutPort")

# dslComponent_StateMachine class attributes and methods
dslComponent_StateMachine_name: Property = Property(name="name", type=StringType)
dslComponent_StateMachine.attributes={dslComponent_StateMachine_name}

# dslComponent_Vertex class attributes and methods

# dslComponent_Edge class attributes and methods

# DocumElt class attributes and methods

# dslComponent_WTComponents class attributes and methods
dslComponent_WTComponents_id: Property = Property(name="id", type=StringType)
dslComponent_WTComponents_author: Property = Property(name="author", type=StringType)
dslComponent_WTComponents.attributes={dslComponent_WTComponents_id, dslComponent_WTComponents_author}

# dslComponent_Subsystem class attributes and methods
dslComponent_Subsystem_name: Property = Property(name="name", type=StringType)
dslComponent_Subsystem_description: Property = Property(name="description", type=StringType)
dslComponent_Subsystem.attributes={dslComponent_Subsystem_description, dslComponent_Subsystem_name}

# dslComponent_ControlSubsystem class attributes and methods
dslComponent_ControlSubsystem_name: Property = Property(name="name", type=StringType)
dslComponent_ControlSubsystem.attributes={dslComponent_ControlSubsystem_name}

# dslComponent_Component class attributes and methods
dslComponent_Component_id: Property = Property(name="id", type=StringType)
dslComponent_Component_name: Property = Property(name="name", type=StringType)
dslComponent_Component.attributes={dslComponent_Component_name, dslComponent_Component_id}

# dslComponent_Port class attributes and methods
dslComponent_Port_name: Property = Property(name="name", type=StringType)
dslComponent_Port.attributes={dslComponent_Port_name}

# dslComponent_SimpleState class attributes and methods

# Vertex class attributes and methods

# dslComponent_InitialState class attributes and methods

# dslComponent_DocumElt class attributes and methods
dslComponent_DocumElt_name: Property = Property(name="name", type=StringType)
dslComponent_DocumElt_desc: Property = Property(name="desc", type=StringType)
dslComponent_DocumElt.attributes={dslComponent_DocumElt_name, dslComponent_DocumElt_desc}

# dslComponent_InPort class attributes and methods

# Port class attributes and methods

# dslComponent_OutPort class attributes and methods

# Relationships
machines10: BinaryAssociation = BinaryAssociation(
    name="machines10",
    ends={
        Property(name="dslComponent_StateMachine", type=dslComponent_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_Component11", type=dslComponent_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="dslComponent_Vertex", type=dslComponent_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_StateMachine13", type=dslComponent_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions14: BinaryAssociation = BinaryAssociation(
    name="transitions14",
    ends={
        Property(name="dslComponent_Edge", type=dslComponent_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_StateMachine15", type=dslComponent_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing16: BinaryAssociation = BinaryAssociation(
    name="outgoing16",
    ends={
        Property(name="Edge", type=dslComponent_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=dslComponent_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming17: BinaryAssociation = BinaryAssociation(
    name="incoming17",
    ends={
        Property(name="Edge18", type=dslComponent_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=dslComponent_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
subsystems0: BinaryAssociation = BinaryAssociation(
    name="subsystems0",
    ends={
        Property(name="dslComponent_Subsystem", type=dslComponent_WTComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_WTComponents", type=dslComponent_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
beh1: BinaryAssociation = BinaryAssociation(
    name="beh1",
    ends={
        Property(name="dslComponent_ControlSubsystem", type=dslComponent_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_Subsystem2", type=dslComponent_ControlSubsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components3: BinaryAssociation = BinaryAssociation(
    name="components3",
    ends={
        Property(name="dslComponent_Component", type=dslComponent_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_Subsystem4", type=dslComponent_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subsystems6: BinaryAssociation = BinaryAssociation(
    name="subsystems6",
    ends={
        Property(name="dslComponent_Subsystem7", type=dslComponent_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_Subsystem5", type=dslComponent_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports8: BinaryAssociation = BinaryAssociation(
    name="ports8",
    ends={
        Property(name="dslComponent_Port", type=dslComponent_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_Component9", type=dslComponent_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="Vertex", type=dslComponent_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=dslComponent_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="Vertex21", type=dslComponent_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=dslComponent_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
machines22: BinaryAssociation = BinaryAssociation(
    name="machines22",
    ends={
        Property(name="dslComponent_StateMachine24", type=dslComponent_ControlSubsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dslComponent_ControlSubsystem23", type=dslComponent_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dslComponent_Vertex_DocumElt = Generalization(general=DocumElt, specific=dslComponent_Vertex)
gen_dslComponent_Edge_DocumElt = Generalization(general=DocumElt, specific=dslComponent_Edge)
gen_dslComponent_SimpleState_Vertex = Generalization(general=Vertex, specific=dslComponent_SimpleState)
gen_dslComponent_InitialState_Vertex = Generalization(general=Vertex, specific=dslComponent_InitialState)
gen_dslComponent_InPort_Port = Generalization(general=Port, specific=dslComponent_InPort)
gen_dslComponent_OutPort_Port = Generalization(general=Port, specific=dslComponent_OutPort)

# Domain Model
domain_model = DomainModel(
    name="dslComponent",
    types={dslComponent_StateMachine, dslComponent_Vertex, dslComponent_Edge, DocumElt, dslComponent_WTComponents, dslComponent_Subsystem, dslComponent_ControlSubsystem, dslComponent_Component, dslComponent_Port, dslComponent_SimpleState, Vertex, dslComponent_InitialState, dslComponent_DocumElt, dslComponent_InPort, Port, dslComponent_OutPort},
    associations={machines10, states12, transitions14, outgoing16, incoming17, subsystems0, beh1, components3, subsystems6, ports8, source19, target20, machines22},
    generalizations={gen_dslComponent_Vertex_DocumElt, gen_dslComponent_Edge_DocumElt, gen_dslComponent_SimpleState_Vertex, gen_dslComponent_InitialState_Vertex, gen_dslComponent_InPort_Port, gen_dslComponent_OutPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
df_Unit = Class(name="df::Unit")
Attributable = Class(name="Attributable")
df_Var = Class(name="df::Var")
df_Type = Class(name="df::Type")
df_Instance = Class(name="df::Instance")
Adaptable = Class(name="Adaptable")
df_Argument = Class(name="df::Argument")
df_EObject = Class(name="df::EObject")
df_Entity = Class(name="df::Entity")
df_Procedure = Class(name="df::Procedure")
df_Port = Class(name="df::Port")
Vertex = Class(name="Vertex")
df_Actor = Class(name="df::Actor")
df_Action = Class(name="df::Action")
df_FSM = Class(name="df::FSM")
df_MoC = Class(name="df::MoC")
df_Vertex = Class(name="df::Vertex")
df_Network = Class(name="df::Network")
Graph = Class(name="Graph")
df_Pattern = Class(name="df::Pattern")
df_Connection = Class(name="df::Connection")
Edge = Class(name="Edge")
df_State = Class(name="df::State")
df_PortToEIntegerObjectMapEntry = Class(name="df::PortToEIntegerObjectMapEntry")
df_PortToVarMapEntry = Class(name="df::PortToVarMapEntry")
df_VarToPortMapEntry = Class(name="df::VarToPortMapEntry")
df_Tag = Class(name="df::Tag")
df_Expression = Class(name="df::Expression")
df_Transition = Class(name="df::Transition")

# df_Unit class attributes and methods
df_Unit_fileName: Property = Property(name="fileName", type=StringType)
df_Unit_lineNumber: Property = Property(name="lineNumber", type=IntegerType)
df_Unit_name: Property = Property(name="name", type=StringType)
df_Unit.attributes={df_Unit_fileName, df_Unit_name, df_Unit_lineNumber}

# Attributable class attributes and methods

# df_Var class attributes and methods

# df_Type class attributes and methods

# df_Instance class attributes and methods
df_Instance_name: Property = Property(name="name", type=StringType)
df_Instance.attributes={df_Instance_name}

# Adaptable class attributes and methods

# df_Argument class attributes and methods

# df_EObject class attributes and methods

# df_Entity class attributes and methods
df_Entity_incomingPortMap: Property = Property(name="incomingPortMap", type=StringType)
df_Entity_name: Property = Property(name="name", type=StringType)
df_Entity_outgoingPortMap: Property = Property(name="outgoingPortMap", type=StringType)
df_Entity.attributes={df_Entity_outgoingPortMap, df_Entity_name, df_Entity_incomingPortMap}

# df_Procedure class attributes and methods

# df_Port class attributes and methods
df_Port_numTokensProduced: Property = Property(name="numTokensProduced", type=IntegerType)
df_Port_name: Property = Property(name="name", type=StringType)
df_Port_numTokensConsumed: Property = Property(name="numTokensConsumed", type=IntegerType)
df_Port.attributes={df_Port_numTokensConsumed, df_Port_numTokensProduced, df_Port_name}

# Vertex class attributes and methods

# df_Actor class attributes and methods
df_Actor_fileName: Property = Property(name="fileName", type=StringType)
df_Actor_native: Property = Property(name="native", type=BooleanType)
df_Actor_name: Property = Property(name="name", type=StringType)
df_Actor_lineNumber: Property = Property(name="lineNumber", type=IntegerType)
df_Actor.attributes={df_Actor_native, df_Actor_fileName, df_Actor_lineNumber, df_Actor_name}

# df_Action class attributes and methods

# df_FSM class attributes and methods

# df_MoC class attributes and methods

# df_Vertex class attributes and methods

# df_Network class attributes and methods
df_Network_fileName: Property = Property(name="fileName", type=StringType)
df_Network_name: Property = Property(name="name", type=StringType)
df_Network.attributes={df_Network_fileName, df_Network_name}

# Graph class attributes and methods

# df_Pattern class attributes and methods

# df_Connection class attributes and methods

# Edge class attributes and methods

# df_State class attributes and methods

# df_PortToEIntegerObjectMapEntry class attributes and methods
df_PortToEIntegerObjectMapEntry_value: Property = Property(name="value", type=StringType)
df_PortToEIntegerObjectMapEntry.attributes={df_PortToEIntegerObjectMapEntry_value}

# df_PortToVarMapEntry class attributes and methods

# df_VarToPortMapEntry class attributes and methods

# df_Tag class attributes and methods
df_Tag_identifiers: Property = Property(name="identifiers", type=StringType)
df_Tag.attributes={df_Tag_identifiers}

# df_Expression class attributes and methods

# df_Transition class attributes and methods

# Relationships
constants0: BinaryAssociation = BinaryAssociation(
    name="constants0",
    ends={
        Property(name="df_Var", type=df_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Unit", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="df_Type", type=df_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Port", type=df_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments4: BinaryAssociation = BinaryAssociation(
    name="arguments4",
    ends={
        Property(name="df_Argument", type=df_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Instance", type=df_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity5: BinaryAssociation = BinaryAssociation(
    name="entity5",
    ends={
        Property(name="df_EObject", type=df_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Instance6", type=df_EObject, multiplicity=Multiplicity(0, 1))
    }
)
inputs7: BinaryAssociation = BinaryAssociation(
    name="inputs7",
    ends={
        Property(name="df_Port8", type=df_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Entity", type=df_Port, multiplicity=Multiplicity(0, 9999))
    }
)
procedures1: BinaryAssociation = BinaryAssociation(
    name="procedures1",
    ends={
        Property(name="df_Procedure", type=df_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Unit2", type=df_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters12: BinaryAssociation = BinaryAssociation(
    name="parameters12",
    ends={
        Property(name="df_Entity13", type=df_Var, multiplicity=Multiplicity(0, 9999)),
        Property(name="df_Var14", type=df_Entity, multiplicity=Multiplicity(1, 1))
    }
)
actions15: BinaryAssociation = BinaryAssociation(
    name="actions15",
    ends={
        Property(name="df_Action", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor", type=df_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsOutsideFsm16: BinaryAssociation = BinaryAssociation(
    name="actionsOutsideFsm16",
    ends={
        Property(name="df_Action18", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor17", type=df_Action, multiplicity=Multiplicity(0, 9999))
    }
)
fsm19: BinaryAssociation = BinaryAssociation(
    name="fsm19",
    ends={
        Property(name="df_FSM", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor20", type=df_FSM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs9: BinaryAssociation = BinaryAssociation(
    name="outputs9",
    ends={
        Property(name="df_Port11", type=df_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Entity10", type=df_Port, multiplicity=Multiplicity(0, 9999))
    }
)
moC27: BinaryAssociation = BinaryAssociation(
    name="moC27",
    ends={
        Property(name="df_MoC", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor28", type=df_MoC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs29: BinaryAssociation = BinaryAssociation(
    name="outputs29",
    ends={
        Property(name="df_Port31", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor30", type=df_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters32: BinaryAssociation = BinaryAssociation(
    name="parameters32",
    ends={
        Property(name="df_Var34", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor33", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procs35: BinaryAssociation = BinaryAssociation(
    name="procs35",
    ends={
        Property(name="df_Procedure37", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor36", type=df_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializes21: BinaryAssociation = BinaryAssociation(
    name="initializes21",
    ends={
        Property(name="df_Action23", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor22", type=df_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs24: BinaryAssociation = BinaryAssociation(
    name="inputs24",
    ends={
        Property(name="df_Port26", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor25", type=df_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children41: BinaryAssociation = BinaryAssociation(
    name="children41",
    ends={
        Property(name="df_Vertex", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network", type=df_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
inputs42: BinaryAssociation = BinaryAssociation(
    name="inputs42",
    ends={
        Property(name="df_Port44", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network43", type=df_Port, multiplicity=Multiplicity(0, 9999))
    }
)
moC45: BinaryAssociation = BinaryAssociation(
    name="moC45",
    ends={
        Property(name="df_MoC47", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network46", type=df_MoC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs48: BinaryAssociation = BinaryAssociation(
    name="outputs48",
    ends={
        Property(name="df_Port50", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network49", type=df_Port, multiplicity=Multiplicity(0, 9999))
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="df_Var53", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network52", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateVars38: BinaryAssociation = BinaryAssociation(
    name="stateVars38",
    ends={
        Property(name="df_Var40", type=df_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Actor39", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourcePort57: BinaryAssociation = BinaryAssociation(
    name="sourcePort57",
    ends={
        Property(name="df_Port58", type=df_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Connection", type=df_Port, multiplicity=Multiplicity(0, 1))
    }
)
targetPort59: BinaryAssociation = BinaryAssociation(
    name="targetPort59",
    ends={
        Property(name="df_Port61", type=df_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Connection60", type=df_Port, multiplicity=Multiplicity(0, 1))
    }
)
body62: BinaryAssociation = BinaryAssociation(
    name="body62",
    ends={
        Property(name="df_Procedure64", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action63", type=df_Procedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputPattern65: BinaryAssociation = BinaryAssociation(
    name="inputPattern65",
    ends={
        Property(name="df_Pattern", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action66", type=df_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputPattern67: BinaryAssociation = BinaryAssociation(
    name="outputPattern67",
    ends={
        Property(name="df_Pattern69", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action68", type=df_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables54: BinaryAssociation = BinaryAssociation(
    name="variables54",
    ends={
        Property(name="df_Var56", type=df_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Network55", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState78: BinaryAssociation = BinaryAssociation(
    name="initialState78",
    ends={
        Property(name="df_State", type=df_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="df_FSM79", type=df_State, multiplicity=Multiplicity(0, 1))
    }
)
numTokensMap80: BinaryAssociation = BinaryAssociation(
    name="numTokensMap80",
    ends={
        Property(name="df_PortToEIntegerObjectMapEntry", type=df_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Pattern81", type=df_PortToEIntegerObjectMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports82: BinaryAssociation = BinaryAssociation(
    name="ports82",
    ends={
        Property(name="df_Port84", type=df_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Pattern83", type=df_Port, multiplicity=Multiplicity(0, 9999))
    }
)
portToVarMap85: BinaryAssociation = BinaryAssociation(
    name="portToVarMap85",
    ends={
        Property(name="df_PortToVarMapEntry", type=df_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Pattern86", type=df_PortToVarMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables87: BinaryAssociation = BinaryAssociation(
    name="variables87",
    ends={
        Property(name="df_Var89", type=df_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Pattern88", type=df_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varToPortMap90: BinaryAssociation = BinaryAssociation(
    name="varToPortMap90",
    ends={
        Property(name="df_VarToPortMapEntry", type=df_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Pattern91", type=df_VarToPortMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
peekPattern70: BinaryAssociation = BinaryAssociation(
    name="peekPattern70",
    ends={
        Property(name="df_Pattern72", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action71", type=df_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scheduler73: BinaryAssociation = BinaryAssociation(
    name="scheduler73",
    ends={
        Property(name="df_Procedure75", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action74", type=df_Procedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag76: BinaryAssociation = BinaryAssociation(
    name="tag76",
    ends={
        Property(name="df_Tag", type=df_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Action77", type=df_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key97: BinaryAssociation = BinaryAssociation(
    name="key97",
    ends={
        Property(name="df_Port99", type=df_PortToVarMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="df_PortToVarMapEntry98", type=df_Port, multiplicity=Multiplicity(0, 1))
    }
)
value100: BinaryAssociation = BinaryAssociation(
    name="value100",
    ends={
        Property(name="df_Var102", type=df_PortToVarMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="df_PortToVarMapEntry101", type=df_Var, multiplicity=Multiplicity(0, 1))
    }
)
key103: BinaryAssociation = BinaryAssociation(
    name="key103",
    ends={
        Property(name="df_Var105", type=df_VarToPortMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="df_VarToPortMapEntry104", type=df_Var, multiplicity=Multiplicity(0, 1))
    }
)
value106: BinaryAssociation = BinaryAssociation(
    name="value106",
    ends={
        Property(name="df_Port108", type=df_VarToPortMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="df_VarToPortMapEntry107", type=df_Port, multiplicity=Multiplicity(0, 1))
    }
)
value109: BinaryAssociation = BinaryAssociation(
    name="value109",
    ends={
        Property(name="df_Expression", type=df_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Argument110", type=df_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable111: BinaryAssociation = BinaryAssociation(
    name="variable111",
    ends={
        Property(name="df_Var113", type=df_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Argument112", type=df_Var, multiplicity=Multiplicity(0, 1))
    }
)
actions92: BinaryAssociation = BinaryAssociation(
    name="actions92",
    ends={
        Property(name="df_Action93", type=df_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="df_Transition", type=df_Action, multiplicity=Multiplicity(0, 9999))
    }
)
key94: BinaryAssociation = BinaryAssociation(
    name="key94",
    ends={
        Property(name="df_Port96", type=df_PortToEIntegerObjectMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="df_PortToEIntegerObjectMapEntry95", type=df_Port, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_df_Unit_Attributable = Generalization(general=Attributable, specific=df_Unit)
gen_df_Instance_Vertex = Generalization(general=Vertex, specific=df_Instance)
gen_df_Instance_Adaptable = Generalization(general=Adaptable, specific=df_Instance)
gen_df_Entity_Attributable = Generalization(general=Attributable, specific=df_Entity)
gen_df_Entity_Adaptable = Generalization(general=Adaptable, specific=df_Entity)
gen_df_Port_Vertex = Generalization(general=Vertex, specific=df_Port)
gen_df_Actor_Vertex = Generalization(general=Vertex, specific=df_Actor)
gen_df_Actor_Adaptable = Generalization(general=Adaptable, specific=df_Actor)
gen_df_Network_Graph = Generalization(general=Graph, specific=df_Network)
gen_df_Network_Adaptable = Generalization(general=Adaptable, specific=df_Network)
gen_df_Action_Attributable = Generalization(general=Attributable, specific=df_Action)
gen_df_Connection_Edge = Generalization(general=Edge, specific=df_Connection)
gen_df_FSM_Graph = Generalization(general=Graph, specific=df_FSM)
gen_df_State_Vertex = Generalization(general=Vertex, specific=df_State)
gen_df_Transition_Edge = Generalization(general=Edge, specific=df_Transition)

# Domain Model
domain_model = DomainModel(
    name="df",
    types={df_Unit, Attributable, df_Var, df_Type, df_Instance, Adaptable, df_Argument, df_EObject, df_Entity, df_Procedure, df_Port, Vertex, df_Actor, df_Action, df_FSM, df_MoC, df_Vertex, df_Network, Graph, df_Pattern, df_Connection, Edge, df_State, df_PortToEIntegerObjectMapEntry, df_PortToVarMapEntry, df_VarToPortMapEntry, df_Tag, df_Expression, df_Transition},
    associations={constants0, type3, arguments4, entity5, inputs7, procedures1, parameters12, actions15, actionsOutsideFsm16, fsm19, outputs9, moC27, outputs29, parameters32, procs35, initializes21, inputs24, children41, inputs42, moC45, outputs48, parameters51, stateVars38, sourcePort57, targetPort59, body62, inputPattern65, outputPattern67, variables54, initialState78, numTokensMap80, ports82, portToVarMap85, variables87, varToPortMap90, peekPattern70, scheduler73, tag76, key97, value100, key103, value106, value109, variable111, actions92, key94},
    generalizations={gen_df_Unit_Attributable, gen_df_Instance_Vertex, gen_df_Instance_Adaptable, gen_df_Entity_Attributable, gen_df_Entity_Adaptable, gen_df_Port_Vertex, gen_df_Actor_Vertex, gen_df_Actor_Adaptable, gen_df_Network_Graph, gen_df_Network_Adaptable, gen_df_Action_Attributable, gen_df_Connection_Edge, gen_df_FSM_Graph, gen_df_State_Vertex, gen_df_Transition_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
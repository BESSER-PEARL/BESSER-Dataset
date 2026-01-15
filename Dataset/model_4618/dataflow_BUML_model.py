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
Attributable = Class(name="Attributable")
dataflow_Actor = Class(name="dataflow::Actor")
dataflow_ActorClass = Class(name="dataflow::ActorClass")
dataflow_Buffer = Class(name="dataflow::Buffer")
dataflow_Port = Class(name="dataflow::Port")
dataflow_SharedVariable = Class(name="dataflow::SharedVariable")
dataflow_Version = Class(name="dataflow::Version")
dataflow_Network = Class(name="dataflow::Network")
dataflow_Variable = Class(name="dataflow::Variable")
dataflow_Action = Class(name="dataflow::Action")
dataflow_Procedure = Class(name="dataflow::Procedure")
dataflow_Guard = Class(name="dataflow::Guard")
dataflow_Type = Class(name="dataflow::Type", is_abstract=True)
dataflow_TypeUint = Class(name="dataflow::TypeUint")
Type = Class(name="Type")
dataflow_TypeInt = Class(name="dataflow::TypeInt")
Variable = Class(name="Variable")
dataflow_TypeDouble = Class(name="dataflow::TypeDouble")
dataflow_TypeUndefined = Class(name="dataflow::TypeUndefined")
dataflow_TypeString = Class(name="dataflow::TypeString")
dataflow_TypeList = Class(name="dataflow::TypeList")
dataflow_TypeBoolean = Class(name="dataflow::TypeBoolean")

# Attributable class attributes and methods

# dataflow_Actor class attributes and methods
dataflow_Actor_name: Property = Property(name="name", type=StringType)
dataflow_Actor_m_getAction: Method = Method(name="getAction", parameters={Parameter(name='name')}, type=StringType)
dataflow_Actor_m_getInputPort: Method = Method(name="getInputPort", parameters={Parameter(name='name')}, type=StringType)
dataflow_Actor_m_getOutputPort: Method = Method(name="getOutputPort", parameters={Parameter(name='name')}, type=StringType)
dataflow_Actor_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='name')}, type=StringType)
dataflow_Actor_m_getProcedure: Method = Method(name="getProcedure", parameters={Parameter(name='name')}, type=StringType)
dataflow_Actor_m_getSharedVariable: Method = Method(name="getSharedVariable", parameters={Parameter(name='tag')}, type=StringType)
dataflow_Actor.attributes={dataflow_Actor_name}
dataflow_Actor.methods={dataflow_Actor_m_getProcedure, dataflow_Actor_m_getVariable, dataflow_Actor_m_getInputPort, dataflow_Actor_m_getSharedVariable, dataflow_Actor_m_getAction, dataflow_Actor_m_getOutputPort}

# dataflow_ActorClass class attributes and methods
dataflow_ActorClass_sourceCode: Property = Property(name="sourceCode", type=StringType)
dataflow_ActorClass_name: Property = Property(name="name", type=StringType)
dataflow_ActorClass_sourceFile: Property = Property(name="sourceFile", type=StringType)
dataflow_ActorClass_nameSpace: Property = Property(name="nameSpace", type=StringType)
dataflow_ActorClass.attributes={dataflow_ActorClass_nameSpace, dataflow_ActorClass_sourceFile, dataflow_ActorClass_name, dataflow_ActorClass_sourceCode}

# dataflow_Buffer class attributes and methods

# dataflow_Port class attributes and methods
dataflow_Port_name: Property = Property(name="name", type=StringType)
dataflow_Port.attributes={dataflow_Port_name}

# dataflow_SharedVariable class attributes and methods
dataflow_SharedVariable_tag: Property = Property(name="tag", type=StringType)
dataflow_SharedVariable.attributes={dataflow_SharedVariable_tag}

# dataflow_Version class attributes and methods

# dataflow_Network class attributes and methods
dataflow_Network_name: Property = Property(name="name", type=StringType)
dataflow_Network_sourceFile: Property = Property(name="sourceFile", type=StringType)
dataflow_Network_project: Property = Property(name="project", type=StringType)
dataflow_Network_m_getActor: Method = Method(name="getActor", parameters={Parameter(name='name')}, type=StringType)
dataflow_Network_m_getActorClass: Method = Method(name="getActorClass", parameters={Parameter(name='name')}, type=StringType)
dataflow_Network_m_getInputPort: Method = Method(name="getInputPort", parameters={Parameter(name='name')}, type=StringType)
dataflow_Network_m_getOutputPort: Method = Method(name="getOutputPort", parameters={Parameter(name='name')}, type=StringType)
dataflow_Network_m_getSharedVariables: Method = Method(name="getSharedVariables", parameters={Parameter(name='tag')}, type=StringType)
dataflow_Network.attributes={dataflow_Network_sourceFile, dataflow_Network_name, dataflow_Network_project}
dataflow_Network.methods={dataflow_Network_m_getOutputPort, dataflow_Network_m_getInputPort, dataflow_Network_m_getActor, dataflow_Network_m_getActorClass, dataflow_Network_m_getSharedVariables}

# dataflow_Variable class attributes and methods
dataflow_Variable_name: Property = Property(name="name", type=StringType)
dataflow_Variable_shared: Property = Property(name="shared", type=BooleanType)
dataflow_Variable.attributes={dataflow_Variable_shared, dataflow_Variable_name}

# dataflow_Action class attributes and methods
dataflow_Action_name: Property = Property(name="name", type=StringType)
dataflow_Action_m_getGuard: Method = Method(name="getGuard", parameters={Parameter(name='tag')}, type=StringType)
dataflow_Action.attributes={dataflow_Action_name}
dataflow_Action.methods={dataflow_Action_m_getGuard}

# dataflow_Procedure class attributes and methods
dataflow_Procedure_name: Property = Property(name="name", type=StringType)
dataflow_Procedure.attributes={dataflow_Procedure_name}

# dataflow_Guard class attributes and methods
dataflow_Guard_tag: Property = Property(name="tag", type=StringType)
dataflow_Guard.attributes={dataflow_Guard_tag}

# dataflow_Type class attributes and methods
dataflow_Type_etype: Property = Property(name="etype", type=StringType)
dataflow_Type_bits: Property = Property(name="bits", type=IntegerType)
dataflow_Type.attributes={dataflow_Type_bits, dataflow_Type_etype}

# dataflow_TypeUint class attributes and methods
dataflow_TypeUint_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeUint.attributes={dataflow_TypeUint_size}

# Type class attributes and methods

# dataflow_TypeInt class attributes and methods
dataflow_TypeInt_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeInt.attributes={dataflow_TypeInt_size}

# Variable class attributes and methods

# dataflow_TypeDouble class attributes and methods
dataflow_TypeDouble_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeDouble.attributes={dataflow_TypeDouble_size}

# dataflow_TypeUndefined class attributes and methods
dataflow_TypeUndefined_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeUndefined.attributes={dataflow_TypeUndefined_size}

# dataflow_TypeString class attributes and methods
dataflow_TypeString_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeString.attributes={dataflow_TypeString_size}

# dataflow_TypeList class attributes and methods
dataflow_TypeList_elements: Property = Property(name="elements", type=IntegerType)
dataflow_TypeList.attributes={dataflow_TypeList_elements}

# dataflow_TypeBoolean class attributes and methods
dataflow_TypeBoolean_size: Property = Property(name="size", type=IntegerType)
dataflow_TypeBoolean.attributes={dataflow_TypeBoolean_size}

# Relationships
actors0: BinaryAssociation = BinaryAssociation(
    name="actors0",
    ends={
        Property(name="dataflow_Actor", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network", type=dataflow_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClasses1: BinaryAssociation = BinaryAssociation(
    name="actorClasses1",
    ends={
        Property(name="dataflow_ActorClass", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network2", type=dataflow_ActorClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buffers3: BinaryAssociation = BinaryAssociation(
    name="buffers3",
    ends={
        Property(name="dataflow_Buffer", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network4", type=dataflow_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts5: BinaryAssociation = BinaryAssociation(
    name="inputPorts5",
    ends={
        Property(name="dataflow_Port", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network6", type=dataflow_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts7: BinaryAssociation = BinaryAssociation(
    name="outputPorts7",
    ends={
        Property(name="dataflow_Port9", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network8", type=dataflow_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sharedVariables10: BinaryAssociation = BinaryAssociation(
    name="sharedVariables10",
    ends={
        Property(name="dataflow_SharedVariable", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network11", type=dataflow_SharedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
version12: BinaryAssociation = BinaryAssociation(
    name="version12",
    ends={
        Property(name="dataflow_Version", type=dataflow_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Network13", type=dataflow_Version, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="dataflow_ActorClass19", type=dataflow_Network, multiplicity=Multiplicity(0, 1)),
        Property(name="dataflow_Network20", type=dataflow_ActorClass, multiplicity=Multiplicity(1, 1))
    }
)
inputPorts21: BinaryAssociation = BinaryAssociation(
    name="inputPorts21",
    ends={
        Property(name="dataflow_Port23", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor22", type=dataflow_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts24: BinaryAssociation = BinaryAssociation(
    name="outputPorts24",
    ends={
        Property(name="dataflow_Port26", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor25", type=dataflow_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables27: BinaryAssociation = BinaryAssociation(
    name="variables27",
    ends={
        Property(name="dataflow_Variable", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor28", type=dataflow_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClass29: BinaryAssociation = BinaryAssociation(
    name="actorClass29",
    ends={
        Property(name="ActorClass", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=dataflow_ActorClass, multiplicity=Multiplicity(1, 1))
    }
)
actions30: BinaryAssociation = BinaryAssociation(
    name="actions30",
    ends={
        Property(name="dataflow_Action", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor31", type=dataflow_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures32: BinaryAssociation = BinaryAssociation(
    name="procedures32",
    ends={
        Property(name="dataflow_Procedure", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor33", type=dataflow_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner34: BinaryAssociation = BinaryAssociation(
    name="owner34",
    ends={
        Property(name="dataflow_Network36", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor35", type=dataflow_Network, multiplicity=Multiplicity(0, 1))
    }
)
buffers37: BinaryAssociation = BinaryAssociation(
    name="buffers37",
    ends={
        Property(name="dataflow_Buffer39", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor38", type=dataflow_Buffer, multiplicity=Multiplicity(0, 9999))
    }
)
actors14: BinaryAssociation = BinaryAssociation(
    name="actors14",
    ends={
        Property(name="Actor", type=dataflow_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="actorClass", type=dataflow_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
version15: BinaryAssociation = BinaryAssociation(
    name="version15",
    ends={
        Property(name="dataflow_Version17", type=dataflow_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_ActorClass16", type=dataflow_Version, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successors50: BinaryAssociation = BinaryAssociation(
    name="successors50",
    ends={
        Property(name="dataflow_Actor51", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor49", type=dataflow_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
inputPorts52: BinaryAssociation = BinaryAssociation(
    name="inputPorts52",
    ends={
        Property(name="Port", type=dataflow_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="readers", type=dataflow_Port, multiplicity=Multiplicity(0, 9999))
    }
)
outputPorts53: BinaryAssociation = BinaryAssociation(
    name="outputPorts53",
    ends={
        Property(name="Port54", type=dataflow_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=dataflow_Port, multiplicity=Multiplicity(0, 9999))
    }
)
guards55: BinaryAssociation = BinaryAssociation(
    name="guards55",
    ends={
        Property(name="dataflow_Guard", type=dataflow_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Action56", type=dataflow_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner57: BinaryAssociation = BinaryAssociation(
    name="owner57",
    ends={
        Property(name="dataflow_Actor59", type=dataflow_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Action58", type=dataflow_Actor, multiplicity=Multiplicity(0, 1))
    }
)
variables60: BinaryAssociation = BinaryAssociation(
    name="variables60",
    ends={
        Property(name="dataflow_Variable62", type=dataflow_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Procedure61", type=dataflow_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
owner63: BinaryAssociation = BinaryAssociation(
    name="owner63",
    ends={
        Property(name="dataflow_Actor65", type=dataflow_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Procedure64", type=dataflow_Actor, multiplicity=Multiplicity(0, 1))
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="dataflow_Type", type=dataflow_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Variable67", type=dataflow_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owner68: BinaryAssociation = BinaryAssociation(
    name="owner68",
    ends={
        Property(name="dataflow_Actor70", type=dataflow_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Variable69", type=dataflow_Actor, multiplicity=Multiplicity(0, 1))
    }
)
incomingBuffers40: BinaryAssociation = BinaryAssociation(
    name="incomingBuffers40",
    ends={
        Property(name="dataflow_Buffer42", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor41", type=dataflow_Buffer, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingBuffers43: BinaryAssociation = BinaryAssociation(
    name="outgoingBuffers43",
    ends={
        Property(name="dataflow_Buffer45", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor44", type=dataflow_Buffer, multiplicity=Multiplicity(0, 9999))
    }
)
predecessors47: BinaryAssociation = BinaryAssociation(
    name="predecessors47",
    ends={
        Property(name="dataflow_Actor48", type=dataflow_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Actor46", type=dataflow_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
input74: BinaryAssociation = BinaryAssociation(
    name="input74",
    ends={
        Property(name="Buffer", type=dataflow_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=dataflow_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
outputs75: BinaryAssociation = BinaryAssociation(
    name="outputs75",
    ends={
        Property(name="Buffer76", type=dataflow_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=dataflow_Buffer, multiplicity=Multiplicity(0, 9999))
    }
)
owner77: BinaryAssociation = BinaryAssociation(
    name="owner77",
    ends={
        Property(name="dataflow_Actor79", type=dataflow_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Port78", type=dataflow_Actor, multiplicity=Multiplicity(0, 1))
    }
)
source80: BinaryAssociation = BinaryAssociation(
    name="source80",
    ends={
        Property(name="Port81", type=dataflow_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="outputs", type=dataflow_Port, multiplicity=Multiplicity(1, 1))
    }
)
target82: BinaryAssociation = BinaryAssociation(
    name="target82",
    ends={
        Property(name="Port83", type=dataflow_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="input", type=dataflow_Port, multiplicity=Multiplicity(1, 1))
    }
)
type84: BinaryAssociation = BinaryAssociation(
    name="type84",
    ends={
        Property(name="dataflow_Type86", type=dataflow_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Buffer85", type=dataflow_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owner87: BinaryAssociation = BinaryAssociation(
    name="owner87",
    ends={
        Property(name="dataflow_Network89", type=dataflow_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Buffer88", type=dataflow_Network, multiplicity=Multiplicity(0, 1))
    }
)
owner90: BinaryAssociation = BinaryAssociation(
    name="owner90",
    ends={
        Property(name="dataflow_Action92", type=dataflow_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_Guard91", type=dataflow_Action, multiplicity=Multiplicity(0, 1))
    }
)
writers71: BinaryAssociation = BinaryAssociation(
    name="writers71",
    ends={
        Property(name="Action", type=dataflow_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="outputPorts", type=dataflow_Action, multiplicity=Multiplicity(0, 9999))
    }
)
readers72: BinaryAssociation = BinaryAssociation(
    name="readers72",
    ends={
        Property(name="Action73", type=dataflow_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="inputPorts", type=dataflow_Action, multiplicity=Multiplicity(0, 9999))
    }
)
listType93: BinaryAssociation = BinaryAssociation(
    name="listType93",
    ends={
        Property(name="dataflow_Type94", type=dataflow_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflow_TypeList", type=dataflow_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dataflow_Network_Attributable = Generalization(general=Attributable, specific=dataflow_Network)
gen_dataflow_Actor_Attributable = Generalization(general=Attributable, specific=dataflow_Actor)
gen_dataflow_ActorClass_Attributable = Generalization(general=Attributable, specific=dataflow_ActorClass)
gen_dataflow_Action_Attributable = Generalization(general=Attributable, specific=dataflow_Action)
gen_dataflow_Procedure_Attributable = Generalization(general=Attributable, specific=dataflow_Procedure)
gen_dataflow_Variable_Attributable = Generalization(general=Attributable, specific=dataflow_Variable)
gen_dataflow_Buffer_Attributable = Generalization(general=Attributable, specific=dataflow_Buffer)
gen_dataflow_Guard_Attributable = Generalization(general=Attributable, specific=dataflow_Guard)
gen_dataflow_TypeUint_Type = Generalization(general=Type, specific=dataflow_TypeUint)
gen_dataflow_TypeInt_Type = Generalization(general=Type, specific=dataflow_TypeInt)
gen_dataflow_SharedVariable_Variable = Generalization(general=Variable, specific=dataflow_SharedVariable)
gen_dataflow_Port_Attributable = Generalization(general=Attributable, specific=dataflow_Port)
gen_dataflow_TypeDouble_Type = Generalization(general=Type, specific=dataflow_TypeDouble)
gen_dataflow_TypeUndefined_Type = Generalization(general=Type, specific=dataflow_TypeUndefined)
gen_dataflow_TypeString_Type = Generalization(general=Type, specific=dataflow_TypeString)
gen_dataflow_TypeList_Type = Generalization(general=Type, specific=dataflow_TypeList)
gen_dataflow_TypeBoolean_Type = Generalization(general=Type, specific=dataflow_TypeBoolean)

# Domain Model
domain_model = DomainModel(
    name="dataflow",
    types={Attributable, dataflow_Actor, dataflow_ActorClass, dataflow_Buffer, dataflow_Port, dataflow_SharedVariable, dataflow_Version, dataflow_Network, dataflow_Variable, dataflow_Action, dataflow_Procedure, dataflow_Guard, dataflow_Type, dataflow_TypeUint, Type, dataflow_TypeInt, Variable, dataflow_TypeDouble, dataflow_TypeUndefined, dataflow_TypeString, dataflow_TypeList, dataflow_TypeBoolean},
    associations={actors0, actorClasses1, buffers3, inputPorts5, outputPorts7, sharedVariables10, version12, owner18, inputPorts21, outputPorts24, variables27, actorClass29, actions30, procedures32, owner34, buffers37, actors14, version15, successors50, inputPorts52, outputPorts53, guards55, owner57, variables60, owner63, type66, owner68, incomingBuffers40, outgoingBuffers43, predecessors47, input74, outputs75, owner77, source80, target82, type84, owner87, owner90, writers71, readers72, listType93},
    generalizations={gen_dataflow_Network_Attributable, gen_dataflow_Actor_Attributable, gen_dataflow_ActorClass_Attributable, gen_dataflow_Action_Attributable, gen_dataflow_Procedure_Attributable, gen_dataflow_Variable_Attributable, gen_dataflow_Buffer_Attributable, gen_dataflow_Guard_Attributable, gen_dataflow_TypeUint_Type, gen_dataflow_TypeInt_Type, gen_dataflow_SharedVariable_Variable, gen_dataflow_Port_Attributable, gen_dataflow_TypeDouble_Type, gen_dataflow_TypeUndefined_Type, gen_dataflow_TypeString_Type, gen_dataflow_TypeList_Type, gen_dataflow_TypeBoolean_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
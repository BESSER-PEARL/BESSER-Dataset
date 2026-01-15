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
td1_State = Class(name="td1::State")
td1_Transition = Class(name="td1::Transition")
td1_Process = Class(name="td1::Process")
td1_Variable = Class(name="td1::Variable")
td1_Port = Class(name="td1::Port")
td1_Trigger = Class(name="td1::Trigger")
td1_Guard = Class(name="td1::Guard")
td1_Action = Class(name="td1::Action")
td1_Program = Class(name="td1::Program")
td1_DataType = Class(name="td1::DataType")
td1_Component = Class(name="td1::Component")

# td1_State class attributes and methods
td1_State_Name: Property = Property(name="Name", type=StringType)
td1_State.attributes={td1_State_Name}

# td1_Transition class attributes and methods
td1_Transition_Name: Property = Property(name="Name", type=StringType)
td1_Transition.attributes={td1_Transition_Name}

# td1_Process class attributes and methods
td1_Process_Name: Property = Property(name="Name", type=StringType)
td1_Process_StateSize: Property = Property(name="StateSize", type=IntegerType)
td1_Process_VarSize: Property = Property(name="VarSize", type=IntegerType)
td1_Process.attributes={td1_Process_Name, td1_Process_VarSize, td1_Process_StateSize}

# td1_Variable class attributes and methods
td1_Variable_Name: Property = Property(name="Name", type=StringType)
td1_Variable_initVal: Property = Property(name="initVal", type=StringType)
td1_Variable.attributes={td1_Variable_initVal, td1_Variable_Name}

# td1_Port class attributes and methods
td1_Port_Name: Property = Property(name="Name", type=StringType)
td1_Port.attributes={td1_Port_Name}

# td1_Trigger class attributes and methods
td1_Trigger_Name: Property = Property(name="Name", type=StringType)
td1_Trigger_Body: Property = Property(name="Body", type=StringType)
td1_Trigger_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
td1_Trigger_ArgSize: Property = Property(name="ArgSize", type=IntegerType)
td1_Trigger.attributes={td1_Trigger_Name, td1_Trigger_codeFiacre, td1_Trigger_Body, td1_Trigger_ArgSize}

# td1_Guard class attributes and methods
td1_Guard_Name: Property = Property(name="Name", type=StringType)
td1_Guard_Body: Property = Property(name="Body", type=StringType)
td1_Guard_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
td1_Guard.attributes={td1_Guard_Body, td1_Guard_codeFiacre, td1_Guard_Name}

# td1_Action class attributes and methods
td1_Action_Name: Property = Property(name="Name", type=StringType)
td1_Action_Body: Property = Property(name="Body", type=StringType)
td1_Action_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
td1_Action.attributes={td1_Action_Name, td1_Action_codeFiacre, td1_Action_Body}

# td1_Program class attributes and methods
td1_Program_Name: Property = Property(name="Name", type=StringType)
td1_Program_ComponentSize: Property = Property(name="ComponentSize", type=IntegerType)
td1_Program.attributes={td1_Program_ComponentSize, td1_Program_Name}

# td1_DataType class attributes and methods
td1_DataType_Name: Property = Property(name="Name", type=StringType)
td1_DataType.attributes={td1_DataType_Name}

# td1_Component class attributes and methods
td1_Component_Name: Property = Property(name="Name", type=StringType)
td1_Component_ProcessSize: Property = Property(name="ProcessSize", type=IntegerType)
td1_Component_VarSize: Property = Property(name="VarSize", type=IntegerType)
td1_Component.attributes={td1_Component_VarSize, td1_Component_ProcessSize, td1_Component_Name}

# Relationships
outTransitions0: BinaryAssociation = BinaryAssociation(
    name="outTransitions0",
    ends={
        Property(name="Transition", type=td1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=td1_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
inTransitions1: BinaryAssociation = BinaryAssociation(
    name="inTransitions1",
    ends={
        Property(name="Transition2", type=td1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=td1_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
process3: BinaryAssociation = BinaryAssociation(
    name="process3",
    ends={
        Property(name="Process", type=td1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="initState", type=td1_Process, multiplicity=Multiplicity(1, 1))
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="td1_Transition", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Process", type=td1_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="Variable", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="processes", type=td1_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="td1_State", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Process7", type=td1_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initState8: BinaryAssociation = BinaryAssociation(
    name="initState8",
    ends={
        Property(name="State", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=td1_State, multiplicity=Multiplicity(1, 1))
    }
)
outPorts9: BinaryAssociation = BinaryAssociation(
    name="outPorts9",
    ends={
        Property(name="td1_Port", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Process10", type=td1_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alluniqueTriggers11: BinaryAssociation = BinaryAssociation(
    name="alluniqueTriggers11",
    ends={
        Property(name="td1_Trigger", type=td1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Process12", type=td1_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="State14", type=td1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=td1_State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="State16", type=td1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=td1_State, multiplicity=Multiplicity(1, 1))
    }
)
guard17: BinaryAssociation = BinaryAssociation(
    name="guard17",
    ends={
        Property(name="td1_Guard", type=td1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Transition18", type=td1_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger19: BinaryAssociation = BinaryAssociation(
    name="trigger19",
    ends={
        Property(name="td1_Trigger21", type=td1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Transition20", type=td1_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action22: BinaryAssociation = BinaryAssociation(
    name="action22",
    ends={
        Property(name="td1_Action", type=td1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Transition23", type=td1_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables31: BinaryAssociation = BinaryAssociation(
    name="variables31",
    ends={
        Property(name="Variable32", type=td1_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=td1_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
ports33: BinaryAssociation = BinaryAssociation(
    name="ports33",
    ends={
        Property(name="td1_Port35", type=td1_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Component34", type=td1_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components36: BinaryAssociation = BinaryAssociation(
    name="components36",
    ends={
        Property(name="td1_Component37", type=td1_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Program", type=td1_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable38: BinaryAssociation = BinaryAssociation(
    name="variable38",
    ends={
        Property(name="td1_Variable40", type=td1_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Program39", type=td1_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes41: BinaryAssociation = BinaryAssociation(
    name="processes41",
    ends={
        Property(name="td1_Process43", type=td1_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Program42", type=td1_Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
datatype24: BinaryAssociation = BinaryAssociation(
    name="datatype24",
    ends={
        Property(name="td1_DataType", type=td1_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Variable", type=td1_DataType, multiplicity=Multiplicity(1, 1))
    }
)
processes25: BinaryAssociation = BinaryAssociation(
    name="processes25",
    ends={
        Property(name="Process26", type=td1_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=td1_Process, multiplicity=Multiplicity(0, 9999))
    }
)
components27: BinaryAssociation = BinaryAssociation(
    name="components27",
    ends={
        Property(name="Component", type=td1_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables28", type=td1_Component, multiplicity=Multiplicity(0, 9999))
    }
)
instances29: BinaryAssociation = BinaryAssociation(
    name="instances29",
    ends={
        Property(name="td1_Process30", type=td1_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Component", type=td1_Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
datatypes44: BinaryAssociation = BinaryAssociation(
    name="datatypes44",
    ends={
        Property(name="td1_DataType46", type=td1_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Program45", type=td1_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments47: BinaryAssociation = BinaryAssociation(
    name="arguments47",
    ends={
        Property(name="td1_Variable49", type=td1_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Trigger48", type=td1_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components50: BinaryAssociation = BinaryAssociation(
    name="components50",
    ends={
        Property(name="td1_Component52", type=td1_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="td1_Port51", type=td1_Component, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="td1",
    types={td1_State, td1_Transition, td1_Process, td1_Variable, td1_Port, td1_Trigger, td1_Guard, td1_Action, td1_Program, td1_DataType, td1_Component},
    associations={outTransitions0, inTransitions1, process3, transitions4, variables5, states6, initState8, outPorts9, alluniqueTriggers11, source13, target15, guard17, trigger19, action22, variables31, ports33, components36, variable38, processes41, datatype24, processes25, components27, instances29, datatypes44, arguments47, components50},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
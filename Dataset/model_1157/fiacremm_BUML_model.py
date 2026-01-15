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
fiacremm_State = Class(name="fiacremm::State")
EModelElement = Class(name="EModelElement")
fiacremm_Transition = Class(name="fiacremm::Transition")
fiacremm_Process = Class(name="fiacremm::Process")
fiacremm_Port = Class(name="fiacremm::Port")
fiacremm_Trigger = Class(name="fiacremm::Trigger")
fiacremm_Guard = Class(name="fiacremm::Guard")
fiacremm_Action = Class(name="fiacremm::Action")
fiacremm_DataType = Class(name="fiacremm::DataType")
fiacremm_Variable = Class(name="fiacremm::Variable")
fiacremm_Component = Class(name="fiacremm::Component")
fiacremm_Program = Class(name="fiacremm::Program")

# fiacremm_State class attributes and methods
fiacremm_State_Name: Property = Property(name="Name", type=StringType)
fiacremm_State.attributes={fiacremm_State_Name}

# EModelElement class attributes and methods

# fiacremm_Transition class attributes and methods
fiacremm_Transition_Name: Property = Property(name="Name", type=StringType)
fiacremm_Transition.attributes={fiacremm_Transition_Name}

# fiacremm_Process class attributes and methods
fiacremm_Process_StateSize: Property = Property(name="StateSize", type=IntegerType)
fiacremm_Process_VarSize: Property = Property(name="VarSize", type=IntegerType)
fiacremm_Process_Name: Property = Property(name="Name", type=StringType)
fiacremm_Process.attributes={fiacremm_Process_StateSize, fiacremm_Process_Name, fiacremm_Process_VarSize}

# fiacremm_Port class attributes and methods
fiacremm_Port_Name: Property = Property(name="Name", type=StringType)
fiacremm_Port.attributes={fiacremm_Port_Name}

# fiacremm_Trigger class attributes and methods
fiacremm_Trigger_Name: Property = Property(name="Name", type=StringType)
fiacremm_Trigger_Body: Property = Property(name="Body", type=StringType)
fiacremm_Trigger_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
fiacremm_Trigger_ArgSize: Property = Property(name="ArgSize", type=IntegerType)
fiacremm_Trigger.attributes={fiacremm_Trigger_Body, fiacremm_Trigger_codeFiacre, fiacremm_Trigger_Name, fiacremm_Trigger_ArgSize}

# fiacremm_Guard class attributes and methods
fiacremm_Guard_Name: Property = Property(name="Name", type=StringType)
fiacremm_Guard_Body: Property = Property(name="Body", type=StringType)
fiacremm_Guard_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
fiacremm_Guard.attributes={fiacremm_Guard_Name, fiacremm_Guard_codeFiacre, fiacremm_Guard_Body}

# fiacremm_Action class attributes and methods
fiacremm_Action_Name: Property = Property(name="Name", type=StringType)
fiacremm_Action_Body: Property = Property(name="Body", type=StringType)
fiacremm_Action_codeFiacre: Property = Property(name="codeFiacre", type=StringType)
fiacremm_Action.attributes={fiacremm_Action_Name, fiacremm_Action_Body, fiacremm_Action_codeFiacre}

# fiacremm_DataType class attributes and methods
fiacremm_DataType_Name: Property = Property(name="Name", type=StringType)
fiacremm_DataType.attributes={fiacremm_DataType_Name}

# fiacremm_Variable class attributes and methods
fiacremm_Variable_initVal: Property = Property(name="initVal", type=StringType)
fiacremm_Variable_Name: Property = Property(name="Name", type=StringType)
fiacremm_Variable.attributes={fiacremm_Variable_Name, fiacremm_Variable_initVal}

# fiacremm_Component class attributes and methods
fiacremm_Component_Name: Property = Property(name="Name", type=StringType)
fiacremm_Component_ProcessSize: Property = Property(name="ProcessSize", type=IntegerType)
fiacremm_Component_VarSize: Property = Property(name="VarSize", type=IntegerType)
fiacremm_Component.attributes={fiacremm_Component_VarSize, fiacremm_Component_Name, fiacremm_Component_ProcessSize}

# fiacremm_Program class attributes and methods
fiacremm_Program_Name: Property = Property(name="Name", type=StringType)
fiacremm_Program_ComponentSize: Property = Property(name="ComponentSize", type=IntegerType)
fiacremm_Program.attributes={fiacremm_Program_Name, fiacremm_Program_ComponentSize}

# Relationships
outTransitions0: BinaryAssociation = BinaryAssociation(
    name="outTransitions0",
    ends={
        Property(name="Transition", type=fiacremm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fiacremm_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
inTransitions1: BinaryAssociation = BinaryAssociation(
    name="inTransitions1",
    ends={
        Property(name="Transition2", type=fiacremm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fiacremm_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
process3: BinaryAssociation = BinaryAssociation(
    name="process3",
    ends={
        Property(name="Process", type=fiacremm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="initState", type=fiacremm_Process, multiplicity=Multiplicity(1, 1))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="fiacremm_State", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Process7", type=fiacremm_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initState8: BinaryAssociation = BinaryAssociation(
    name="initState8",
    ends={
        Property(name="State", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=fiacremm_State, multiplicity=Multiplicity(1, 1))
    }
)
outPorts9: BinaryAssociation = BinaryAssociation(
    name="outPorts9",
    ends={
        Property(name="fiacremm_Port", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Process10", type=fiacremm_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alluniqueTriggers11: BinaryAssociation = BinaryAssociation(
    name="alluniqueTriggers11",
    ends={
        Property(name="fiacremm_Trigger", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Process12", type=fiacremm_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="State14", type=fiacremm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=fiacremm_State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="State16", type=fiacremm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=fiacremm_State, multiplicity=Multiplicity(1, 1))
    }
)
guard17: BinaryAssociation = BinaryAssociation(
    name="guard17",
    ends={
        Property(name="fiacremm_Guard", type=fiacremm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Transition18", type=fiacremm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger19: BinaryAssociation = BinaryAssociation(
    name="trigger19",
    ends={
        Property(name="fiacremm_Trigger21", type=fiacremm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Transition20", type=fiacremm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action22: BinaryAssociation = BinaryAssociation(
    name="action22",
    ends={
        Property(name="fiacremm_Action", type=fiacremm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Transition23", type=fiacremm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="fiacremm_Transition", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Process", type=fiacremm_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="Variable", type=fiacremm_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="processes", type=fiacremm_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
components27: BinaryAssociation = BinaryAssociation(
    name="components27",
    ends={
        Property(name="Component", type=fiacremm_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables28", type=fiacremm_Component, multiplicity=Multiplicity(0, 9999))
    }
)
instances29: BinaryAssociation = BinaryAssociation(
    name="instances29",
    ends={
        Property(name="fiacremm_Process30", type=fiacremm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Component", type=fiacremm_Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables31: BinaryAssociation = BinaryAssociation(
    name="variables31",
    ends={
        Property(name="Variable32", type=fiacremm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=fiacremm_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
ports33: BinaryAssociation = BinaryAssociation(
    name="ports33",
    ends={
        Property(name="fiacremm_Port35", type=fiacremm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Component34", type=fiacremm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components36: BinaryAssociation = BinaryAssociation(
    name="components36",
    ends={
        Property(name="fiacremm_Component37", type=fiacremm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Program", type=fiacremm_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable38: BinaryAssociation = BinaryAssociation(
    name="variable38",
    ends={
        Property(name="fiacremm_Variable40", type=fiacremm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Program39", type=fiacremm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes41: BinaryAssociation = BinaryAssociation(
    name="processes41",
    ends={
        Property(name="fiacremm_Process43", type=fiacremm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Program42", type=fiacremm_Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
datatype24: BinaryAssociation = BinaryAssociation(
    name="datatype24",
    ends={
        Property(name="fiacremm_DataType", type=fiacremm_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Variable", type=fiacremm_DataType, multiplicity=Multiplicity(1, 1))
    }
)
processes25: BinaryAssociation = BinaryAssociation(
    name="processes25",
    ends={
        Property(name="Process26", type=fiacremm_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=fiacremm_Process, multiplicity=Multiplicity(0, 9999))
    }
)
arguments47: BinaryAssociation = BinaryAssociation(
    name="arguments47",
    ends={
        Property(name="fiacremm_Variable49", type=fiacremm_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Trigger48", type=fiacremm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components50: BinaryAssociation = BinaryAssociation(
    name="components50",
    ends={
        Property(name="fiacremm_Component52", type=fiacremm_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Port51", type=fiacremm_Component, multiplicity=Multiplicity(0, 9999))
    }
)
datatypes44: BinaryAssociation = BinaryAssociation(
    name="datatypes44",
    ends={
        Property(name="fiacremm_DataType46", type=fiacremm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacremm_Program45", type=fiacremm_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fiacremm_State_EModelElement = Generalization(general=EModelElement, specific=fiacremm_State)
gen_fiacremm_Transition_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Transition)
gen_fiacremm_DataType_EModelElement = Generalization(general=EModelElement, specific=fiacremm_DataType)
gen_fiacremm_Process_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Process)
gen_fiacremm_Component_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Component)
gen_fiacremm_Program_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Program)
gen_fiacremm_Variable_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Variable)
gen_fiacremm_Action_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Action)
gen_fiacremm_Port_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Port)
gen_fiacremm_Guard_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Guard)
gen_fiacremm_Trigger_EModelElement = Generalization(general=EModelElement, specific=fiacremm_Trigger)

# Domain Model
domain_model = DomainModel(
    name="fiacremm",
    types={fiacremm_State, EModelElement, fiacremm_Transition, fiacremm_Process, fiacremm_Port, fiacremm_Trigger, fiacremm_Guard, fiacremm_Action, fiacremm_DataType, fiacremm_Variable, fiacremm_Component, fiacremm_Program},
    associations={outTransitions0, inTransitions1, process3, states6, initState8, outPorts9, alluniqueTriggers11, source13, target15, guard17, trigger19, action22, transitions4, variables5, components27, instances29, variables31, ports33, components36, variable38, processes41, datatype24, processes25, arguments47, components50, datatypes44},
    generalizations={gen_fiacremm_State_EModelElement, gen_fiacremm_Transition_EModelElement, gen_fiacremm_DataType_EModelElement, gen_fiacremm_Process_EModelElement, gen_fiacremm_Component_EModelElement, gen_fiacremm_Program_EModelElement, gen_fiacremm_Variable_EModelElement, gen_fiacremm_Action_EModelElement, gen_fiacremm_Port_EModelElement, gen_fiacremm_Guard_EModelElement, gen_fiacremm_Trigger_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
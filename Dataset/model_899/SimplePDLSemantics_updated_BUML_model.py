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

# Enumerations
WorkSequenceType: Enumeration = Enumeration(
    name="WorkSequenceType",
    literals={
            EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="startToFinish"),
			EnumerationLiteral(name="finishToFinish")
    }
)

ExecutionState: Enumeration = Enumeration(
    name="ExecutionState",
    literals={
            EnumerationLiteral(name="notStarted"),
			EnumerationLiteral(name="running"),
			EnumerationLiteral(name="finished")
    }
)

TimeState: Enumeration = Enumeration(
    name="TimeState",
    literals={
            EnumerationLiteral(name="tooEarly"),
			EnumerationLiteral(name="inTime"),
			EnumerationLiteral(name="tooLate")
    }
)

# Classes
SimplePDLSemantics_DDMMSimplePDL_Process = Class(name="SimplePDLSemantics::DDMMSimplePDL::Process")
ProcessElement = Class(name="ProcessElement")
WorkDefinition = Class(name="WorkDefinition")
SimplePDLSemantics_DDMMSimplePDL_WorkDefinition = Class(name="SimplePDLSemantics::DDMMSimplePDL::WorkDefinition")
WorkSequence = Class(name="WorkSequence")
Process = Class(name="Process")
SimplePDLSemantics_DDMMSimplePDL_WorkSequence = Class(name="SimplePDLSemantics::DDMMSimplePDL::WorkSequence")
SimplePDLSemantics_DDMMSimplePDL_ProcessElement = Class(name="SimplePDLSemantics::DDMMSimplePDL::ProcessElement", is_abstract=True)
SimplePDLSemantics_EDMMSimplePDL_Event = Class(name="SimplePDLSemantics::EDMMSimplePDL::Event", is_abstract=True)
SPDLSimEvent = Class(name="SPDLSimEvent")
SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent = Class(name="SimplePDLSemantics::EDMMSimplePDL::WorkDefinitionEvent", is_abstract=True)
Event = Class(name="Event")
SimplePDLSemantics_EDMMSimplePDL_StartWD = Class(name="SimplePDLSemantics::EDMMSimplePDL::StartWD")
WorkDefinitionEvent = Class(name="WorkDefinitionEvent")
SimplePDLSemantics_EDMMSimplePDL_FinishWD = Class(name="SimplePDLSemantics::EDMMSimplePDL::FinishWD")
SimplePDLSemantics_DDMMSimplePDL_Guidance = Class(name="SimplePDLSemantics::DDMMSimplePDL::Guidance")
SimplePDLSemantics_TM3SimplePDL_SPDLScenario = Class(name="SimplePDLSemantics::TM3SimplePDL::SPDLScenario")
SPDLTrace = Class(name="SPDLTrace")
SimplePDLSemantics_TM3SimplePDL_SPDLTrace = Class(name="SimplePDLSemantics::TM3SimplePDL::SPDLTrace")
SPDLScenario = Class(name="SPDLScenario")
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent = Class(name="SimplePDLSemantics::TM3SimplePDL::SPDLSimEvent")
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition = Class(name="SimplePDLSemantics::SDMMSimplePDL::DynamicWorkDefinition")

# SimplePDLSemantics_DDMMSimplePDL_Process class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_Process_name: Property = Property(name="name", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_Process.attributes={SimplePDLSemantics_DDMMSimplePDL_Process_name}

# ProcessElement class attributes and methods

# WorkDefinition class attributes and methods

# SimplePDLSemantics_DDMMSimplePDL_WorkDefinition class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_name: Property = Property(name="name", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_WorkDefinition.attributes={SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_name}

# WorkSequence class attributes and methods

# Process class attributes and methods

# SimplePDLSemantics_DDMMSimplePDL_WorkSequence class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_WorkSequence.attributes={SimplePDLSemantics_DDMMSimplePDL_WorkSequence_linkType}

# SimplePDLSemantics_DDMMSimplePDL_ProcessElement class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_Event class attributes and methods

# SPDLSimEvent class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent class attributes and methods

# Event class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_StartWD class attributes and methods

# WorkDefinitionEvent class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_FinishWD class attributes and methods

# SimplePDLSemantics_DDMMSimplePDL_Guidance class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_Guidance_text: Property = Property(name="text", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_Guidance.attributes={SimplePDLSemantics_DDMMSimplePDL_Guidance_text}

# SimplePDLSemantics_TM3SimplePDL_SPDLScenario class attributes and methods

# SPDLTrace class attributes and methods

# SimplePDLSemantics_TM3SimplePDL_SPDLTrace class attributes and methods

# SPDLScenario class attributes and methods

# SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent class attributes and methods
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_internal: Property = Property(name="internal", type=BooleanType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_date: Property = Property(name="date", type=IntegerType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_name: Property = Property(name="name", type=StringType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent.attributes={SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_name, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_date, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_internal}

# SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition class attributes and methods
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_time: Property = Property(name="time", type=StringType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_timeElapsed: Property = Property(name="timeElapsed", type=FloatType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_state: Property = Property(name="state", type=StringType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition.attributes={SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_timeElapsed, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_time, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_state}

# Relationships
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="DDMMSimplePDL2", type=SimplePDLSemantics_DDMMSimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="WorkDefinition", type=WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
linksToPredecessors3: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors3",
    ends={
        Property(name="DDMMSimplePDL4", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="WorkSequence", type=WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors5: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors5",
    ends={
        Property(name="DDMMSimplePDL7", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="WorkSequence6", type=WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
process8: BinaryAssociation = BinaryAssociation(
    name="process8",
    ends={
        Property(name="DDMMSimplePDL9", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="Process", type=Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor10: BinaryAssociation = BinaryAssociation(
    name="predecessor10",
    ends={
        Property(name="DDMMSimplePDL12", type=SimplePDLSemantics_DDMMSimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="WorkDefinition11", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor13: BinaryAssociation = BinaryAssociation(
    name="successor13",
    ends={
        Property(name="DDMMSimplePDL15", type=SimplePDLSemantics_DDMMSimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="WorkDefinition14", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="DDMMSimplePDL", type=SimplePDLSemantics_DDMMSimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessElement", type=ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element19: BinaryAssociation = BinaryAssociation(
    name="element19",
    ends={
        Property(name="ProcessElement20", type=SimplePDLSemantics_DDMMSimplePDL_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_DDMMSimplePDL_Guidance", type=ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
workdefinition21: BinaryAssociation = BinaryAssociation(
    name="workdefinition21",
    ends={
        Property(name="WorkDefinition22", type=SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parent16: BinaryAssociation = BinaryAssociation(
    name="parent16",
    ends={
        Property(name="DDMMSimplePDL18", type=SimplePDLSemantics_DDMMSimplePDL_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Process17", type=Process, multiplicity=Multiplicity(1, 1))
    }
)
traces23: BinaryAssociation = BinaryAssociation(
    name="traces23",
    ends={
        Property(name="TM3SimplePDL", type=SimplePDLSemantics_TM3SimplePDL_SPDLScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SPDLTrace", type=SPDLTrace, multiplicity=Multiplicity(0, 9999))
    }
)
simEvents24: BinaryAssociation = BinaryAssociation(
    name="simEvents24",
    ends={
        Property(name="SPDLSimEvent", type=SimplePDLSemantics_TM3SimplePDL_SPDLScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_TM3SimplePDL_SPDLScenario", type=SPDLSimEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario25: BinaryAssociation = BinaryAssociation(
    name="scenario25",
    ends={
        Property(name="TM3SimplePDL26", type=SimplePDLSemantics_TM3SimplePDL_SPDLTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="SPDLScenario", type=SPDLScenario, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition)
gen_SimplePDLSemantics_DDMMSimplePDL_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_WorkSequence)
gen_SimplePDLSemantics_EDMMSimplePDL_Event_SPDLSimEvent = Generalization(general=SPDLSimEvent, specific=SimplePDLSemantics_EDMMSimplePDL_Event)
gen_SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent_Event = Generalization(general=Event, specific=SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent)
gen_SimplePDLSemantics_EDMMSimplePDL_StartWD_WorkDefinitionEvent = Generalization(general=WorkDefinitionEvent, specific=SimplePDLSemantics_EDMMSimplePDL_StartWD)
gen_SimplePDLSemantics_EDMMSimplePDL_FinishWD_WorkDefinitionEvent = Generalization(general=WorkDefinitionEvent, specific=SimplePDLSemantics_EDMMSimplePDL_FinishWD)
gen_SimplePDLSemantics_DDMMSimplePDL_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_Guidance)
gen_SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_WorkDefinition = Generalization(general=WorkDefinition, specific=SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition)

# Domain Model
domain_model = DomainModel(
    name="SimplePDLSemantics",
    types={SimplePDLSemantics_DDMMSimplePDL_Process, ProcessElement, WorkDefinition, SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, WorkSequence, Process, SimplePDLSemantics_DDMMSimplePDL_WorkSequence, SimplePDLSemantics_DDMMSimplePDL_ProcessElement, SimplePDLSemantics_EDMMSimplePDL_Event, SPDLSimEvent, SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent, Event, SimplePDLSemantics_EDMMSimplePDL_StartWD, WorkDefinitionEvent, SimplePDLSemantics_EDMMSimplePDL_FinishWD, SimplePDLSemantics_DDMMSimplePDL_Guidance, SimplePDLSemantics_TM3SimplePDL_SPDLScenario, SPDLTrace, SimplePDLSemantics_TM3SimplePDL_SPDLTrace, SPDLScenario, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition, WorkSequenceType, ExecutionState, TimeState},
    associations={from1, linksToPredecessors3, linksToSuccessors5, process8, predecessor10, successor13, processElements0, element19, workdefinition21, parent16, traces23, simEvents24, scenario25},
    generalizations={gen_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_ProcessElement, gen_SimplePDLSemantics_DDMMSimplePDL_WorkSequence_ProcessElement, gen_SimplePDLSemantics_EDMMSimplePDL_Event_SPDLSimEvent, gen_SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent_Event, gen_SimplePDLSemantics_EDMMSimplePDL_StartWD_WorkDefinitionEvent, gen_SimplePDLSemantics_EDMMSimplePDL_FinishWD_WorkDefinitionEvent, gen_SimplePDLSemantics_DDMMSimplePDL_Guidance_ProcessElement, gen_SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_WorkDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
SimplePDLSemantics_DDMMSimplePDL_Process = Class(name="SimplePDLSemantics_DDMMSimplePDL_Process")
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition = Class(name="SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition")
ProcessElement = Class(name="ProcessElement")
SimplePDLSemantics_TM3SimplePDL_SPDLScenario = Class(name="SimplePDLSemantics_TM3SimplePDL_SPDLScenario")
WorkDefinition = Class(name="WorkDefinition")
SimplePDLSemantics_DDMMSimplePDL_WorkDefinition = Class(name="SimplePDLSemantics_DDMMSimplePDL_WorkDefinition")
WorkSequence = Class(name="WorkSequence")
Process = Class(name="Process")
SimplePDLSemantics_DDMMSimplePDL_WorkSequence = Class(name="SimplePDLSemantics_DDMMSimplePDL_WorkSequence")
SimplePDLSemantics_DDMMSimplePDL_ProcessElement = Class(name="SimplePDLSemantics_DDMMSimplePDL_ProcessElement", is_abstract=True)
SimplePDLSemantics_DDMMSimplePDL_Guidance = Class(name="SimplePDLSemantics_DDMMSimplePDL_Guidance")
SimplePDLSemantics_EDMMSimplePDL_Event = Class(name="SimplePDLSemantics_EDMMSimplePDL_Event", is_abstract=True)
SPDLSimEvent = Class(name="SPDLSimEvent")
SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent = Class(name="SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent", is_abstract=True)
Event = Class(name="Event")
SimplePDLSemantics_EDMMSimplePDL_StartWD = Class(name="SimplePDLSemantics_EDMMSimplePDL_StartWD")
WorkDefinitionEvent = Class(name="WorkDefinitionEvent")
SimplePDLSemantics_EDMMSimplePDL_FinishWD = Class(name="SimplePDLSemantics_EDMMSimplePDL_FinishWD")
SPDLTrace = Class(name="SPDLTrace")
SimplePDLSemantics_TM3SimplePDL_SPDLTrace = Class(name="SimplePDLSemantics_TM3SimplePDL_SPDLTrace")
SPDLScenario = Class(name="SPDLScenario")
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent = Class(name="SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent")

# SimplePDLSemantics_DDMMSimplePDL_Process class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_Process_name: Property = Property(name="name", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_Process.attributes={SimplePDLSemantics_DDMMSimplePDL_Process_name}

# SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition class attributes and methods
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_state: Property = Property(name="state", type=StringType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_time: Property = Property(name="time", type=StringType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_timeElapsed: Property = Property(name="timeElapsed", type=FloatType)
SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition.attributes={SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_time, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_state, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_timeElapsed}

# ProcessElement class attributes and methods

# SimplePDLSemantics_TM3SimplePDL_SPDLScenario class attributes and methods

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

# SimplePDLSemantics_DDMMSimplePDL_Guidance class attributes and methods
SimplePDLSemantics_DDMMSimplePDL_Guidance_text: Property = Property(name="text", type=StringType)
SimplePDLSemantics_DDMMSimplePDL_Guidance.attributes={SimplePDLSemantics_DDMMSimplePDL_Guidance_text}

# SimplePDLSemantics_EDMMSimplePDL_Event class attributes and methods

# SPDLSimEvent class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent class attributes and methods

# Event class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_StartWD class attributes and methods

# WorkDefinitionEvent class attributes and methods

# SimplePDLSemantics_EDMMSimplePDL_FinishWD class attributes and methods

# SPDLTrace class attributes and methods

# SimplePDLSemantics_TM3SimplePDL_SPDLTrace class attributes and methods

# SPDLScenario class attributes and methods

# SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent class attributes and methods
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_internal: Property = Property(name="internal", type=BooleanType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_date: Property = Property(name="date", type=IntegerType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_name: Property = Property(name="name", type=StringType)
SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent.attributes={SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_internal, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_date, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent_name}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="ProcessElement", type=SimplePDLSemantics_DDMMSimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_1: BinaryAssociation = BinaryAssociation(
    name="from_1",
    ends={
        Property(name="WorkDefinition", type=SimplePDLSemantics_DDMMSimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
linksToPredecessors2: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors2",
    ends={
        Property(name="WorkSequence", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="WorkSequence4", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
process5: BinaryAssociation = BinaryAssociation(
    name="process5",
    ends={
        Property(name="Process", type=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor6: BinaryAssociation = BinaryAssociation(
    name="predecessor6",
    ends={
        Property(name="WorkDefinition7", type=SimplePDLSemantics_DDMMSimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor8: BinaryAssociation = BinaryAssociation(
    name="successor8",
    ends={
        Property(name="WorkDefinition9", type=SimplePDLSemantics_DDMMSimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parent10: BinaryAssociation = BinaryAssociation(
    name="parent10",
    ends={
        Property(name="Process11", type=SimplePDLSemantics_DDMMSimplePDL_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="processElements", type=Process, multiplicity=Multiplicity(1, 1))
    }
)
element12: BinaryAssociation = BinaryAssociation(
    name="element12",
    ends={
        Property(name="ProcessElement13", type=SimplePDLSemantics_DDMMSimplePDL_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_DDMMSimplePDL_Guidance", type=ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
workdefinition14: BinaryAssociation = BinaryAssociation(
    name="workdefinition14",
    ends={
        Property(name="WorkDefinition15", type=SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent", type=WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
traces16: BinaryAssociation = BinaryAssociation(
    name="traces16",
    ends={
        Property(name="SPDLTrace", type=SimplePDLSemantics_TM3SimplePDL_SPDLScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenario", type=SPDLTrace, multiplicity=Multiplicity(0, 9999))
    }
)
simEvents17: BinaryAssociation = BinaryAssociation(
    name="simEvents17",
    ends={
        Property(name="SPDLSimEvent", type=SimplePDLSemantics_TM3SimplePDL_SPDLScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDLSemantics_TM3SimplePDL_SPDLScenario", type=SPDLSimEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario18: BinaryAssociation = BinaryAssociation(
    name="scenario18",
    ends={
        Property(name="SPDLScenario", type=SimplePDLSemantics_TM3SimplePDL_SPDLTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces", type=SPDLScenario, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_WorkDefinition = Generalization(general=WorkDefinition, specific=SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition)
gen_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_WorkDefinition)
gen_SimplePDLSemantics_DDMMSimplePDL_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_WorkSequence)
gen_SimplePDLSemantics_DDMMSimplePDL_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDLSemantics_DDMMSimplePDL_Guidance)
gen_SimplePDLSemantics_EDMMSimplePDL_Event_SPDLSimEvent = Generalization(general=SPDLSimEvent, specific=SimplePDLSemantics_EDMMSimplePDL_Event)
gen_SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent_Event = Generalization(general=Event, specific=SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent)
gen_SimplePDLSemantics_EDMMSimplePDL_StartWD_WorkDefinitionEvent = Generalization(general=WorkDefinitionEvent, specific=SimplePDLSemantics_EDMMSimplePDL_StartWD)
gen_SimplePDLSemantics_EDMMSimplePDL_FinishWD_WorkDefinitionEvent = Generalization(general=WorkDefinitionEvent, specific=SimplePDLSemantics_EDMMSimplePDL_FinishWD)

# Domain Model
domain_model = DomainModel(
    name="SimplePDLSemantics",
    types={SimplePDLSemantics_DDMMSimplePDL_Process, SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition, ProcessElement, SimplePDLSemantics_TM3SimplePDL_SPDLScenario, WorkDefinition, SimplePDLSemantics_DDMMSimplePDL_WorkDefinition, WorkSequence, Process, SimplePDLSemantics_DDMMSimplePDL_WorkSequence, SimplePDLSemantics_DDMMSimplePDL_ProcessElement, SimplePDLSemantics_DDMMSimplePDL_Guidance, SimplePDLSemantics_EDMMSimplePDL_Event, SPDLSimEvent, SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent, Event, SimplePDLSemantics_EDMMSimplePDL_StartWD, WorkDefinitionEvent, SimplePDLSemantics_EDMMSimplePDL_FinishWD, SPDLTrace, SimplePDLSemantics_TM3SimplePDL_SPDLTrace, SPDLScenario, SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent, WorkSequenceType, ExecutionState, TimeState},
    associations={processElements0, from_1, linksToPredecessors2, linksToSuccessors3, process5, predecessor6, successor8, parent10, element12, workdefinition14, traces16, simEvents17, scenario18},
    generalizations={gen_SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition_WorkDefinition, gen_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition_ProcessElement, gen_SimplePDLSemantics_DDMMSimplePDL_WorkSequence_ProcessElement, gen_SimplePDLSemantics_DDMMSimplePDL_Guidance_ProcessElement, gen_SimplePDLSemantics_EDMMSimplePDL_Event_SPDLSimEvent, gen_SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent_Event, gen_SimplePDLSemantics_EDMMSimplePDL_StartWD_WorkDefinitionEvent, gen_SimplePDLSemantics_EDMMSimplePDL_FinishWD_WorkDefinitionEvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
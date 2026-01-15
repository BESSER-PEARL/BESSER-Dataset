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

# Classes
SimplePDL_WorkSequence = Class(name="SimplePDL::WorkSequence")
SimplePDL_Resource = Class(name="SimplePDL::Resource")
SimplePDL_Process = Class(name="SimplePDL::Process")
SimplePDL_ProcessElement = Class(name="SimplePDL::ProcessElement")
SimplePDL_Guidance = Class(name="SimplePDL::Guidance")
SimplePDL_WorkDefinition = Class(name="SimplePDL::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
SimplePDL_ResourceType = Class(name="SimplePDL::ResourceType")

# SimplePDL_WorkSequence class attributes and methods
SimplePDL_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
SimplePDL_WorkSequence.attributes={SimplePDL_WorkSequence_linkType}

# SimplePDL_Resource class attributes and methods
SimplePDL_Resource_occurrences: Property = Property(name="occurrences", type=IntegerType)
SimplePDL_Resource.attributes={SimplePDL_Resource_occurrences}

# SimplePDL_Process class attributes and methods
SimplePDL_Process_name: Property = Property(name="name", type=StringType)
SimplePDL_Process_minTime: Property = Property(name="minTime", type=IntegerType)
SimplePDL_Process_maxTime: Property = Property(name="maxTime", type=IntegerType)
SimplePDL_Process.attributes={SimplePDL_Process_name, SimplePDL_Process_maxTime, SimplePDL_Process_minTime}

# SimplePDL_ProcessElement class attributes and methods

# SimplePDL_Guidance class attributes and methods
SimplePDL_Guidance_text: Property = Property(name="text", type=StringType)
SimplePDL_Guidance.attributes={SimplePDL_Guidance_text}

# SimplePDL_WorkDefinition class attributes and methods
SimplePDL_WorkDefinition_name: Property = Property(name="name", type=StringType)
SimplePDL_WorkDefinition_minTime: Property = Property(name="minTime", type=IntegerType)
SimplePDL_WorkDefinition_maxTime: Property = Property(name="maxTime", type=IntegerType)
SimplePDL_WorkDefinition.attributes={SimplePDL_WorkDefinition_maxTime, SimplePDL_WorkDefinition_minTime, SimplePDL_WorkDefinition_name}

# ProcessElement class attributes and methods

# SimplePDL_ResourceType class attributes and methods
SimplePDL_ResourceType_name: Property = Property(name="name", type=StringType)
SimplePDL_ResourceType_occurrences: Property = Property(name="occurrences", type=IntegerType)
SimplePDL_ResourceType.attributes={SimplePDL_ResourceType_occurrences, SimplePDL_ResourceType_name}

# Relationships
linksToPredecessors3: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors3",
    ends={
        Property(name="WorkSequence", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=SimplePDL_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors4: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors4",
    ends={
        Property(name="WorkSequence5", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=SimplePDL_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
neededResources6: BinaryAssociation = BinaryAssociation(
    name="neededResources6",
    ends={
        Property(name="Resource", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workDefinition", type=SimplePDL_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="SimplePDL_ProcessElement", type=SimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDL_Process", type=SimplePDL_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guidanceGFX1: BinaryAssociation = BinaryAssociation(
    name="guidanceGFX1",
    ends={
        Property(name="SimplePDL_Guidance", type=SimplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDL_Process2", type=SimplePDL_Guidance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="ProcessElement", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=SimplePDL_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor8: BinaryAssociation = BinaryAssociation(
    name="predecessor8",
    ends={
        Property(name="WorkDefinition", type=SimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor9: BinaryAssociation = BinaryAssociation(
    name="successor9",
    ends={
        Property(name="WorkDefinition10", type=SimplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
guides11: BinaryAssociation = BinaryAssociation(
    name="guides11",
    ends={
        Property(name="SimplePDL_Guidance13", type=SimplePDL_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDL_ProcessElement12", type=SimplePDL_Guidance, multiplicity=Multiplicity(0, 9999))
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="WorkDefinition15", type=SimplePDL_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
workDefinition16: BinaryAssociation = BinaryAssociation(
    name="workDefinition16",
    ends={
        Property(name="WorkDefinition17", type=SimplePDL_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="neededResources", type=SimplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="SimplePDL_ResourceType", type=SimplePDL_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePDL_Resource", type=SimplePDL_ResourceType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimplePDL_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDL_WorkDefinition)
gen_SimplePDL_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDL_WorkSequence)
gen_SimplePDL_ResourceType_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDL_ResourceType)
gen_SimplePDL_Resource_ProcessElement = Generalization(general=ProcessElement, specific=SimplePDL_Resource)

# Domain Model
domain_model = DomainModel(
    name="SimplePDL",
    types={SimplePDL_WorkSequence, SimplePDL_Resource, SimplePDL_Process, SimplePDL_ProcessElement, SimplePDL_Guidance, SimplePDL_WorkDefinition, ProcessElement, SimplePDL_ResourceType, WorkSequenceType},
    associations={linksToPredecessors3, linksToSuccessors4, neededResources6, processElements0, guidanceGFX1, child7, predecessor8, successor9, guides11, parent14, workDefinition16, type18},
    generalizations={gen_SimplePDL_WorkDefinition_ProcessElement, gen_SimplePDL_WorkSequence_ProcessElement, gen_SimplePDL_ResourceType_ProcessElement, gen_SimplePDL_Resource_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
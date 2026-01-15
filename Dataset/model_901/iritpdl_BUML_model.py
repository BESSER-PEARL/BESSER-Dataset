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
iritpdl_ProcessElement = Class(name="iritpdl::ProcessElement")
iritpdl_Guidance = Class(name="iritpdl::Guidance")
iritpdl_ResourceType = Class(name="iritpdl::ResourceType")
iritpdl_WorkDefinition = Class(name="iritpdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
iritpdl_WorkSequence = Class(name="iritpdl::WorkSequence")
iritpdl_Process = Class(name="iritpdl::Process")
iritpdl_Resource = Class(name="iritpdl::Resource")
iritpdl_ResourceConf = Class(name="iritpdl::ResourceConf")

# iritpdl_ProcessElement class attributes and methods

# iritpdl_Guidance class attributes and methods
iritpdl_Guidance_text: Property = Property(name="text", type=StringType)
iritpdl_Guidance.attributes={iritpdl_Guidance_text}

# iritpdl_ResourceType class attributes and methods
iritpdl_ResourceType_name: Property = Property(name="name", type=StringType)
iritpdl_ResourceType_occurrences: Property = Property(name="occurrences", type=IntegerType)
iritpdl_ResourceType.attributes={iritpdl_ResourceType_occurrences, iritpdl_ResourceType_name}

# iritpdl_WorkDefinition class attributes and methods
iritpdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
iritpdl_WorkDefinition_minTime: Property = Property(name="minTime", type=IntegerType)
iritpdl_WorkDefinition_maxTime: Property = Property(name="maxTime", type=IntegerType)
iritpdl_WorkDefinition.attributes={iritpdl_WorkDefinition_maxTime, iritpdl_WorkDefinition_minTime, iritpdl_WorkDefinition_name}

# ProcessElement class attributes and methods

# iritpdl_WorkSequence class attributes and methods
iritpdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
iritpdl_WorkSequence.attributes={iritpdl_WorkSequence_linkType}

# iritpdl_Process class attributes and methods
iritpdl_Process_name: Property = Property(name="name", type=StringType)
iritpdl_Process_minTime: Property = Property(name="minTime", type=IntegerType)
iritpdl_Process_maxTime: Property = Property(name="maxTime", type=IntegerType)
iritpdl_Process.attributes={iritpdl_Process_name, iritpdl_Process_minTime, iritpdl_Process_maxTime}

# iritpdl_Resource class attributes and methods
iritpdl_Resource_occurrences: Property = Property(name="occurrences", type=IntegerType)
iritpdl_Resource.attributes={iritpdl_Resource_occurrences}

# iritpdl_ResourceConf class attributes and methods
iritpdl_ResourceConf_name: Property = Property(name="name", type=StringType)
iritpdl_ResourceConf.attributes={iritpdl_ResourceConf_name}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="iritpdl_ProcessElement", type=iritpdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="iritpdl_Process", type=iritpdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guidanceGFX1: BinaryAssociation = BinaryAssociation(
    name="guidanceGFX1",
    ends={
        Property(name="iritpdl_Guidance", type=iritpdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="iritpdl_Process2", type=iritpdl_Guidance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="iritpdl_ResourceType", type=iritpdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="iritpdl_Process4", type=iritpdl_ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToPredecessors5: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors5",
    ends={
        Property(name="WorkSequence", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=iritpdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="iritpdl_ResourceType19", type=iritpdl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="iritpdl_Resource", type=iritpdl_ResourceType, multiplicity=Multiplicity(1, 1))
    }
)
resourceConf20: BinaryAssociation = BinaryAssociation(
    name="resourceConf20",
    ends={
        Property(name="ResourceConf21", type=iritpdl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="neededResources", type=iritpdl_ResourceConf, multiplicity=Multiplicity(1, 1))
    }
)
workDefinition22: BinaryAssociation = BinaryAssociation(
    name="workDefinition22",
    ends={
        Property(name="WorkDefinition23", type=iritpdl_ResourceConf, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceConf", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
neededResources24: BinaryAssociation = BinaryAssociation(
    name="neededResources24",
    ends={
        Property(name="Resource", type=iritpdl_ResourceConf, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceConf25", type=iritpdl_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors6: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors6",
    ends={
        Property(name="WorkSequence7", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=iritpdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
resourceConf8: BinaryAssociation = BinaryAssociation(
    name="resourceConf8",
    ends={
        Property(name="ResourceConf", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workDefinition", type=iritpdl_ResourceConf, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="ProcessElement", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=iritpdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor10: BinaryAssociation = BinaryAssociation(
    name="predecessor10",
    ends={
        Property(name="WorkDefinition", type=iritpdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor11: BinaryAssociation = BinaryAssociation(
    name="successor11",
    ends={
        Property(name="WorkDefinition12", type=iritpdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
guides13: BinaryAssociation = BinaryAssociation(
    name="guides13",
    ends={
        Property(name="iritpdl_Guidance15", type=iritpdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="iritpdl_ProcessElement14", type=iritpdl_Guidance, multiplicity=Multiplicity(0, 9999))
    }
)
parent16: BinaryAssociation = BinaryAssociation(
    name="parent16",
    ends={
        Property(name="WorkDefinition17", type=iritpdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=iritpdl_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iritpdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=iritpdl_WorkDefinition)
gen_iritpdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=iritpdl_WorkSequence)

# Domain Model
domain_model = DomainModel(
    name="iritpdl",
    types={iritpdl_ProcessElement, iritpdl_Guidance, iritpdl_ResourceType, iritpdl_WorkDefinition, ProcessElement, iritpdl_WorkSequence, iritpdl_Process, iritpdl_Resource, iritpdl_ResourceConf, WorkSequenceType},
    associations={processElements0, guidanceGFX1, resources3, linksToPredecessors5, type18, resourceConf20, workDefinition22, neededResources24, linksToSuccessors6, resourceConf8, children9, predecessor10, successor11, guides13, parent16},
    generalizations={gen_iritpdl_WorkDefinition_ProcessElement, gen_iritpdl_WorkSequence_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
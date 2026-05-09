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
simplepdl_Process = Class(name="simplepdl_Process")
simplepdl_ProcessElement = Class(name="simplepdl_ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl_WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl_WorkSequence")
simplepdl_UseResources = Class(name="simplepdl_UseResources")
simplepdl_Guidance = Class(name="simplepdl_Guidance")
simplepdl_Resource = Class(name="simplepdl_Resource")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_UseResources class attributes and methods
simplepdl_UseResources_weight: Property = Property(name="weight", type=IntegerType)
simplepdl_UseResources.attributes={simplepdl_UseResources_weight}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_Resource class attributes and methods
simplepdl_Resource_quantity: Property = Property(name="quantity", type=StringType)
simplepdl_Resource_name: Property = Property(name="name", type=StringType)
simplepdl_Resource.attributes={simplepdl_Resource_name, simplepdl_Resource_quantity}

# Relationships
linksToSuccessors5: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors5",
    ends={
        Property(name="WorkSequence6", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process1: BinaryAssociation = BinaryAssociation(
    name="process1",
    ends={
        Property(name="simplepdl_Process3", type=simplepdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_ProcessElement2", type=simplepdl_Process, multiplicity=Multiplicity(1, 1))
    }
)
linksToPredecessors4: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors4",
    ends={
        Property(name="WorkSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
uses7: BinaryAssociation = BinaryAssociation(
    name="uses7",
    ends={
        Property(name="simplepdl_UseResources", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_WorkDefinition", type=simplepdl_UseResources, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predecessor8: BinaryAssociation = BinaryAssociation(
    name="predecessor8",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor9: BinaryAssociation = BinaryAssociation(
    name="successor9",
    ends={
        Property(name="WorkDefinition10", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
element11: BinaryAssociation = BinaryAssociation(
    name="element11",
    ends={
        Property(name="simplepdl_ProcessElement12", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
usedResource13: BinaryAssociation = BinaryAssociation(
    name="usedResource13",
    ends={
        Property(name="simplepdl_Resource", type=simplepdl_UseResources, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_UseResources14", type=simplepdl_Resource, multiplicity=Multiplicity(1, 1))
    }
)
associatedWD15: BinaryAssociation = BinaryAssociation(
    name="associatedWD15",
    ends={
        Property(name="simplepdl_WorkDefinition17", type=simplepdl_UseResources, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_UseResources16", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_Resource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Resource)
gen_simplepdl_UseResources_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_UseResources)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_UseResources, simplepdl_Guidance, simplepdl_Resource, WorkSequenceType},
    associations={linksToSuccessors5, processElements0, process1, linksToPredecessors4, uses7, predecessor8, successor9, element11, usedResource13, associatedWD15},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_Resource_ProcessElement, gen_simplepdl_UseResources_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
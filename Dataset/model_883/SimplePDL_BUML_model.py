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
simplepdl_Process = Class(name="simplepdl::Process")
simplepdl_RessourceSequence = Class(name="simplepdl::RessourceSequence")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Ressource = Class(name="simplepdl::Ressource")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_RessourceSequence class attributes and methods
simplepdl_RessourceSequence_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_RessourceSequence.attributes={simplepdl_RessourceSequence_quantity}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_Ressource_name: Property = Property(name="name", type=StringType)
simplepdl_Ressource.attributes={simplepdl_Ressource_quantity, simplepdl_Ressource_name}

# Relationships
linksToSuccessors5: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors5",
    ends={
        Property(name="WorkSequence6", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
ressourcesequence7: BinaryAssociation = BinaryAssociation(
    name="ressourcesequence7",
    ends={
        Property(name="RessourceSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workdefinition", type=simplepdl_RessourceSequence, multiplicity=Multiplicity(0, 9999))
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
ressource13: BinaryAssociation = BinaryAssociation(
    name="ressource13",
    ends={
        Property(name="simplepdl_Ressource", type=simplepdl_RessourceSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_RessourceSequence", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1))
    }
)
workdefinition14: BinaryAssociation = BinaryAssociation(
    name="workdefinition14",
    ends={
        Property(name="WorkDefinition15", type=simplepdl_RessourceSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="ressourcesequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_Ressource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Ressource)
gen_simplepdl_RessourceSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceSequence)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_RessourceSequence, simplepdl_Guidance, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_Ressource, WorkSequenceType},
    associations={linksToSuccessors5, ressourcesequence7, predecessor8, successor9, element11, processElements0, process1, linksToPredecessors4, ressource13, workdefinition14},
    generalizations={gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_Ressource_ProcessElement, gen_simplepdl_RessourceSequence_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
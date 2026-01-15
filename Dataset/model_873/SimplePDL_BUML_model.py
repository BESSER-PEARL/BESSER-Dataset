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
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_Process = Class(name="simplepdl::Process")
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_Ressource = Class(name="simplepdl::Ressource")
simplepdl_RessourceLink = Class(name="simplepdl::RessourceLink")

# simplepdl_ProcessElement class attributes and methods

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_WorkDefinition_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name, simplepdl_WorkDefinition_max_time, simplepdl_WorkDefinition_min_time}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_name: Property = Property(name="name", type=StringType)
simplepdl_Ressource_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_Ressource.attributes={simplepdl_Ressource_quantity, simplepdl_Ressource_name}

# simplepdl_RessourceLink class attributes and methods
simplepdl_RessourceLink_weight: Property = Property(name="weight", type=IntegerType)
simplepdl_RessourceLink.attributes={simplepdl_RessourceLink_weight}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ressource10: BinaryAssociation = BinaryAssociation(
    name="ressource10",
    ends={
        Property(name="simplepdl_Ressource", type=simplepdl_RessourceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_RessourceLink11", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1))
    }
)
linksToPredecessors1: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors1",
    ends={
        Property(name="WorkSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors2: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors2",
    ends={
        Property(name="WorkSequence3", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor4: BinaryAssociation = BinaryAssociation(
    name="predecessor4",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor5: BinaryAssociation = BinaryAssociation(
    name="successor5",
    ends={
        Property(name="WorkDefinition6", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="simplepdl_ProcessElement8", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
workDef9: BinaryAssociation = BinaryAssociation(
    name="workDef9",
    ends={
        Property(name="simplepdl_WorkDefinition", type=simplepdl_RessourceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_RessourceLink", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_Ressource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Ressource)
gen_simplepdl_RessourceLink_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceLink)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_ProcessElement, simplepdl_Process, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_Guidance, simplepdl_Ressource, simplepdl_RessourceLink, WorkSequenceType},
    associations={processElements0, ressource10, linksToPredecessors1, linksToSuccessors2, predecessor4, successor5, element7, workDef9},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_Ressource_ProcessElement, gen_simplepdl_RessourceLink_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
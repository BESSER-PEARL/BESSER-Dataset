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
simplepdl_Guidance = Class(name="simplepdl_Guidance")
simplepdl_Process = Class(name="simplepdl_Process")
simplepdl_ProcessElement = Class(name="simplepdl_ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl_WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl_WorkSequence")
simplepdl_RessourceConso = Class(name="simplepdl_RessourceConso")
simplepdl_Ressource = Class(name="simplepdl_Ressource")

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

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

# simplepdl_RessourceConso class attributes and methods
simplepdl_RessourceConso_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_RessourceConso.attributes={simplepdl_RessourceConso_quantity}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_type: Property = Property(name="type", type=StringType)
simplepdl_Ressource_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_Ressource.attributes={simplepdl_Ressource_type, simplepdl_Ressource_quantity}

# Relationships
successor6: BinaryAssociation = BinaryAssociation(
    name="successor6",
    ends={
        Property(name="WorkDefinition7", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
process8: BinaryAssociation = BinaryAssociation(
    name="process8",
    ends={
        Property(name="simplepdl_Process10", type=simplepdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_ProcessElement9", type=simplepdl_Process, multiplicity=Multiplicity(0, 1))
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
ressourcecons4: BinaryAssociation = BinaryAssociation(
    name="ressourcecons4",
    ends={
        Property(name="RessourceConso", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workdefinition", type=simplepdl_RessourceConso, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor5: BinaryAssociation = BinaryAssociation(
    name="predecessor5",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
workdefinition13: BinaryAssociation = BinaryAssociation(
    name="workdefinition13",
    ends={
        Property(name="WorkDefinition14", type=simplepdl_RessourceConso, multiplicity=Multiplicity(1, 1)),
        Property(name="ressourcecons", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
ressource15: BinaryAssociation = BinaryAssociation(
    name="ressource15",
    ends={
        Property(name="simplepdl_Ressource", type=simplepdl_RessourceConso, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_RessourceConso", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Ressource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Ressource)
gen_simplepdl_RessourceConso_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceConso)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Guidance, simplepdl_Process, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_RessourceConso, simplepdl_Ressource, WorkSequenceType},
    associations={successor6, process8, element11, processElements0, linksToPredecessors1, linksToSuccessors2, ressourcecons4, predecessor5, workdefinition13, ressource15},
    generalizations={gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Ressource_ProcessElement, gen_simplepdl_RessourceConso_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
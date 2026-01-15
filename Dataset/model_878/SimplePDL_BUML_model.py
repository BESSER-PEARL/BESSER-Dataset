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
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_RessourceDefinition = Class(name="simplepdl::RessourceDefinition")
simplepdl_RessourceInstance = Class(name="simplepdl::RessourceInstance")
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_RessourceConfig = Class(name="simplepdl::RessourceConfig")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_Process_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_Process.attributes={simplepdl_Process_min_time, simplepdl_Process_name, simplepdl_Process_max_time}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_RessourceDefinition class attributes and methods
simplepdl_RessourceDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_RessourceDefinition_number: Property = Property(name="number", type=IntegerType)
simplepdl_RessourceDefinition.attributes={simplepdl_RessourceDefinition_number, simplepdl_RessourceDefinition_name}

# simplepdl_RessourceInstance class attributes and methods
simplepdl_RessourceInstance_instances: Property = Property(name="instances", type=IntegerType)
simplepdl_RessourceInstance.attributes={simplepdl_RessourceInstance_instances}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_WorkDefinition_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_max_time, simplepdl_WorkDefinition_name, simplepdl_WorkDefinition_min_time}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_RessourceConfig class attributes and methods
simplepdl_RessourceConfig_name: Property = Property(name="name", type=StringType)
simplepdl_RessourceConfig.attributes={simplepdl_RessourceConfig_name}

# Relationships
element8: BinaryAssociation = BinaryAssociation(
    name="element8",
    ends={
        Property(name="simplepdl_ProcessElement9", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="simplepdl_RessourceDefinition", type=simplepdl_RessourceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_RessourceInstance", type=simplepdl_RessourceDefinition, multiplicity=Multiplicity(1, 1))
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
linksToRessources4: BinaryAssociation = BinaryAssociation(
    name="linksToRessources4",
    ends={
        Property(name="RessourceConfig", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=simplepdl_RessourceConfig, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor5: BinaryAssociation = BinaryAssociation(
    name="predecessor5",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor6: BinaryAssociation = BinaryAssociation(
    name="successor6",
    ends={
        Property(name="WorkDefinition7", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
config11: BinaryAssociation = BinaryAssociation(
    name="config11",
    ends={
        Property(name="RessourceConfig12", type=simplepdl_RessourceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ressources", type=simplepdl_RessourceConfig, multiplicity=Multiplicity(1, 1))
    }
)
activity13: BinaryAssociation = BinaryAssociation(
    name="activity13",
    ends={
        Property(name="WorkDefinition14", type=simplepdl_RessourceConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToRessources", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
ressources15: BinaryAssociation = BinaryAssociation(
    name="ressources15",
    ends={
        Property(name="RessourceInstance", type=simplepdl_RessourceConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="config", type=simplepdl_RessourceInstance, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_RessourceDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceDefinition)
gen_simplepdl_RessourceInstance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceInstance)
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_RessourceConfig_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RessourceConfig)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_Guidance, simplepdl_RessourceDefinition, simplepdl_RessourceInstance, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_RessourceConfig, WorkSequenceType},
    associations={element8, type10, processElements0, linksToPredecessors1, linksToSuccessors2, linksToRessources4, predecessor5, successor6, config11, activity13, ressources15},
    generalizations={gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_RessourceDefinition_ProcessElement, gen_simplepdl_RessourceInstance_ProcessElement, gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_RessourceConfig_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
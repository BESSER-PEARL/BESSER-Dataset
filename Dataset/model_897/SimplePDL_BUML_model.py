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
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement")
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# ProcessElement class attributes and methods

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="simplepdl_ProcessElement8", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
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

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_Guidance, simplepdl_WorkSequence, WorkSequenceType},
    associations={processElements0, predecessor4, successor5, elements7, linksToPredecessors1, linksToSuccessors2},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
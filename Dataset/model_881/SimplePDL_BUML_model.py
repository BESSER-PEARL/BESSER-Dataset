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
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Process = Class(name="simplepdl::Process")
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_Allocation = Class(name="simplepdl::Allocation")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_Ressource = Class(name="simplepdl::Ressource")

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_Allocation class attributes and methods
simplepdl_Allocation_count: Property = Property(name="count", type=IntegerType)
simplepdl_Allocation.attributes={simplepdl_Allocation_count}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_count: Property = Property(name="count", type=IntegerType)
simplepdl_Ressource_name: Property = Property(name="name", type=StringType)
simplepdl_Ressource.attributes={simplepdl_Ressource_count, simplepdl_Ressource_name}

# Relationships
allocations10: BinaryAssociation = BinaryAssociation(
    name="allocations10",
    ends={
        Property(name="Allocation11", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1)),
        Property(name="ressource", type=simplepdl_Allocation, multiplicity=Multiplicity(0, 9999))
    }
)
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workDefinition12: BinaryAssociation = BinaryAssociation(
    name="workDefinition12",
    ends={
        Property(name="WorkDefinition13", type=simplepdl_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocations", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
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
allocations4: BinaryAssociation = BinaryAssociation(
    name="allocations4",
    ends={
        Property(name="Allocation", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workDefinition", type=simplepdl_Allocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
process8: BinaryAssociation = BinaryAssociation(
    name="process8",
    ends={
        Property(name="Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="processElements", type=simplepdl_Process, multiplicity=Multiplicity(1, 1))
    }
)
processElements9: BinaryAssociation = BinaryAssociation(
    name="processElements9",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
ressource14: BinaryAssociation = BinaryAssociation(
    name="ressource14",
    ends={
        Property(name="Ressource", type=simplepdl_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocations15", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_Ressource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Ressource)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_Process, simplepdl_ProcessElement, simplepdl_Allocation, simplepdl_Guidance, simplepdl_Ressource, WorkSequenceType},
    associations={allocations10, processElements0, workDefinition12, linksToPredecessors1, linksToSuccessors2, allocations4, predecessor5, successor6, process8, processElements9, ressource14},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_Ressource_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
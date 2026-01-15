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
simplepdl_ProcessElements = Class(name="simplepdl::ProcessElements")
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElements = Class(name="ProcessElements")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Allocation = Class(name="simplepdl::Allocation")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_Ressource = Class(name="simplepdl::Ressource")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_ProcessElements class attributes and methods

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# ProcessElements class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# simplepdl_Allocation class attributes and methods
simplepdl_Allocation_count: Property = Property(name="count", type=IntegerType)
simplepdl_Allocation.attributes={simplepdl_Allocation_count}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_name: Property = Property(name="name", type=StringType)
simplepdl_Ressource_count: Property = Property(name="count", type=IntegerType)
simplepdl_Ressource.attributes={simplepdl_Ressource_name, simplepdl_Ressource_count}

# Relationships
predecessor5: BinaryAssociation = BinaryAssociation(
    name="predecessor5",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
processelement0: BinaryAssociation = BinaryAssociation(
    name="processelement0",
    ends={
        Property(name="simplepdl_ProcessElements", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_ProcessElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
allocation4: BinaryAssociation = BinaryAssociation(
    name="allocation4",
    ends={
        Property(name="simplepdl_Allocation", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_WorkDefinition", type=simplepdl_Allocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor6: BinaryAssociation = BinaryAssociation(
    name="successor6",
    ends={
        Property(name="WorkDefinition7", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
processelement8: BinaryAssociation = BinaryAssociation(
    name="processelement8",
    ends={
        Property(name="simplepdl_ProcessElements9", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElements, multiplicity=Multiplicity(0, 1))
    }
)
ressource10: BinaryAssociation = BinaryAssociation(
    name="ressource10",
    ends={
        Property(name="simplepdl_Ressource", type=simplepdl_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Allocation11", type=simplepdl_Ressource, multiplicity=Multiplicity(0, 1))
    }
)
workdefinition12: BinaryAssociation = BinaryAssociation(
    name="workdefinition12",
    ends={
        Property(name="simplepdl_WorkDefinition14", type=simplepdl_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Allocation13", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElements = Generalization(general=ProcessElements, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElements = Generalization(general=ProcessElements, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElements = Generalization(general=ProcessElements, specific=simplepdl_Guidance)
gen_simplepdl_Ressource_ProcessElements = Generalization(general=ProcessElements, specific=simplepdl_Ressource)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_ProcessElements, simplepdl_WorkDefinition, ProcessElements, simplepdl_WorkSequence, simplepdl_Allocation, simplepdl_Guidance, simplepdl_Ressource, WorkSequenceType},
    associations={predecessor5, processelement0, linksToPredecessors1, linksToSuccessors2, allocation4, successor6, processelement8, ressource10, workdefinition12},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElements, gen_simplepdl_WorkSequence_ProcessElements, gen_simplepdl_Guidance_ProcessElements, gen_simplepdl_Ressource_ProcessElements},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
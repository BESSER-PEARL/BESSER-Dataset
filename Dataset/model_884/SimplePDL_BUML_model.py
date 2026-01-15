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
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_NeedSet = Class(name="simplepdl::NeedSet")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_Ressource = Class(name="simplepdl::Ressource")
simplepdl_Need = Class(name="simplepdl::Need")

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

# simplepdl_NeedSet class attributes and methods
simplepdl_NeedSet_name: Property = Property(name="name", type=StringType)
simplepdl_NeedSet.attributes={simplepdl_NeedSet_name}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# simplepdl_Ressource class attributes and methods
simplepdl_Ressource_name: Property = Property(name="name", type=StringType)
simplepdl_Ressource_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_Ressource.attributes={simplepdl_Ressource_name, simplepdl_Ressource_quantity}

# simplepdl_Need class attributes and methods
simplepdl_Need_quantity: Property = Property(name="quantity", type=IntegerType)
simplepdl_Need.attributes={simplepdl_Need_quantity}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process1: BinaryAssociation = BinaryAssociation(
    name="process1",
    ends={
        Property(name="Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="processElements", type=simplepdl_Process, multiplicity=Multiplicity(1, 1))
    }
)
linksToPredecessors2: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors2",
    ends={
        Property(name="WorkSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="WorkSequence4", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
needSets5: BinaryAssociation = BinaryAssociation(
    name="needSets5",
    ends={
        Property(name="NeedSet", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="wd", type=simplepdl_NeedSet, multiplicity=Multiplicity(0, 9999))
    }
)
successor7: BinaryAssociation = BinaryAssociation(
    name="successor7",
    ends={
        Property(name="WorkDefinition8", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
element9: BinaryAssociation = BinaryAssociation(
    name="element9",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
ressource10: BinaryAssociation = BinaryAssociation(
    name="ressource10",
    ends={
        Property(name="simplepdl_Ressource", type=simplepdl_Need, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Need", type=simplepdl_Ressource, multiplicity=Multiplicity(1, 1))
    }
)
predecessor6: BinaryAssociation = BinaryAssociation(
    name="predecessor6",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
needSet11: BinaryAssociation = BinaryAssociation(
    name="needSet11",
    ends={
        Property(name="NeedSet12", type=simplepdl_Need, multiplicity=Multiplicity(1, 1)),
        Property(name="needs", type=simplepdl_NeedSet, multiplicity=Multiplicity(1, 1))
    }
)
needs13: BinaryAssociation = BinaryAssociation(
    name="needs13",
    ends={
        Property(name="Need", type=simplepdl_NeedSet, multiplicity=Multiplicity(1, 1)),
        Property(name="needSet", type=simplepdl_Need, multiplicity=Multiplicity(1, 9999))
    }
)
wd14: BinaryAssociation = BinaryAssociation(
    name="wd14",
    ends={
        Property(name="WorkDefinition15", type=simplepdl_NeedSet, multiplicity=Multiplicity(1, 1)),
        Property(name="needSets", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_Ressource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Ressource)
gen_simplepdl_Need_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Need)
gen_simplepdl_NeedSet_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_NeedSet)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_NeedSet, simplepdl_Guidance, simplepdl_Ressource, simplepdl_Need, WorkSequenceType},
    associations={processElements0, process1, linksToPredecessors2, linksToSuccessors3, needSets5, successor7, element9, ressource10, predecessor6, needSet11, needs13, wd14},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_Ressource_ProcessElement, gen_simplepdl_Need_ProcessElement, gen_simplepdl_NeedSet_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
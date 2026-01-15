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
simplepdl_Guidance = Class(name="simplepdl::Guidance")
simplepdl_Process = Class(name="simplepdl::Process")
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_RequeteDeRessource = Class(name="simplepdl::RequeteDeRessource")
simplepdl_Resources = Class(name="simplepdl::Resources")
simplepdl_GuidanceLink = Class(name="simplepdl::GuidanceLink")

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

# simplepdl_RequeteDeRessource class attributes and methods
simplepdl_RequeteDeRessource_quantite: Property = Property(name="quantite", type=IntegerType)
simplepdl_RequeteDeRessource.attributes={simplepdl_RequeteDeRessource_quantite}

# simplepdl_Resources class attributes and methods
simplepdl_Resources_quantite: Property = Property(name="quantite", type=IntegerType)
simplepdl_Resources_name: Property = Property(name="name", type=StringType)
simplepdl_Resources.attributes={simplepdl_Resources_quantite, simplepdl_Resources_name}

# simplepdl_GuidanceLink class attributes and methods

# Relationships
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
linktoresource4: BinaryAssociation = BinaryAssociation(
    name="linktoresource4",
    ends={
        Property(name="RequeteDeRessource", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workdefinition", type=simplepdl_RequeteDeRessource, multiplicity=Multiplicity(0, 9999))
    }
)
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="simplepdl_ProcessElement9", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
linktoresource10: BinaryAssociation = BinaryAssociation(
    name="linktoresource10",
    ends={
        Property(name="RequeteDeRessource11", type=simplepdl_Resources, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=simplepdl_RequeteDeRessource, multiplicity=Multiplicity(0, 9999))
    }
)
resources12: BinaryAssociation = BinaryAssociation(
    name="resources12",
    ends={
        Property(name="Resources", type=simplepdl_RequeteDeRessource, multiplicity=Multiplicity(1, 1)),
        Property(name="linktoresource", type=simplepdl_Resources, multiplicity=Multiplicity(1, 1))
    }
)
workdefinition13: BinaryAssociation = BinaryAssociation(
    name="workdefinition13",
    ends={
        Property(name="WorkDefinition15", type=simplepdl_RequeteDeRessource, multiplicity=Multiplicity(1, 1)),
        Property(name="linktoresource14", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
guidance16: BinaryAssociation = BinaryAssociation(
    name="guidance16",
    ends={
        Property(name="simplepdl_Guidance17", type=simplepdl_GuidanceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_GuidanceLink", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1))
    }
)
workdefinition18: BinaryAssociation = BinaryAssociation(
    name="workdefinition18",
    ends={
        Property(name="simplepdl_WorkDefinition", type=simplepdl_GuidanceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_GuidanceLink19", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Resources_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Resources)
gen_simplepdl_RequeteDeRessource_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_RequeteDeRessource)
gen_simplepdl_GuidanceLink_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_GuidanceLink)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Guidance, simplepdl_Process, simplepdl_ProcessElement, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_RequeteDeRessource, simplepdl_Resources, simplepdl_GuidanceLink, WorkSequenceType},
    associations={predecessor5, successor6, processElements0, linksToPredecessors1, linksToSuccessors2, linktoresource4, elements8, linktoresource10, resources12, workdefinition13, guidance16, workdefinition18},
    generalizations={gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Resources_ProcessElement, gen_simplepdl_RequeteDeRessource_ProcessElement, gen_simplepdl_GuidanceLink_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
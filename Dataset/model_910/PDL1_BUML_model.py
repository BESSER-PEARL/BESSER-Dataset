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
            EnumerationLiteral(name="start2start"),
			EnumerationLiteral(name="finish2start"),
			EnumerationLiteral(name="start2finish"),
			EnumerationLiteral(name="finish2finish")
    }
)

# Classes
pDL1_Process = Class(name="pDL1::Process")
pDL1_ProcessElement = Class(name="pDL1::ProcessElement")
pDL1_WorkDefinition = Class(name="pDL1::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
pDL1_WorkSequence = Class(name="pDL1::WorkSequence")
pDL1_Guidance = Class(name="pDL1::Guidance")

# pDL1_Process class attributes and methods
pDL1_Process_name: Property = Property(name="name", type=StringType)
pDL1_Process.attributes={pDL1_Process_name}

# pDL1_ProcessElement class attributes and methods

# pDL1_WorkDefinition class attributes and methods
pDL1_WorkDefinition_name: Property = Property(name="name", type=StringType)
pDL1_WorkDefinition.attributes={pDL1_WorkDefinition_name}

# ProcessElement class attributes and methods

# pDL1_WorkSequence class attributes and methods
pDL1_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
pDL1_WorkSequence.attributes={pDL1_WorkSequence_linkType}

# pDL1_Guidance class attributes and methods
pDL1_Guidance_texte: Property = Property(name="texte", type=StringType)
pDL1_Guidance.attributes={pDL1_Guidance_texte}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="pDL1_ProcessElement", type=pDL1_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL1_Process", type=pDL1_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor1: BinaryAssociation = BinaryAssociation(
    name="predecessor1",
    ends={
        Property(name="pDL1_WorkDefinition", type=pDL1_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL1_WorkSequence", type=pDL1_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
successor2: BinaryAssociation = BinaryAssociation(
    name="successor2",
    ends={
        Property(name="pDL1_WorkDefinition4", type=pDL1_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL1_WorkSequence3", type=pDL1_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pDL1_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=pDL1_WorkDefinition)
gen_pDL1_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=pDL1_WorkSequence)
gen_pDL1_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=pDL1_Guidance)

# Domain Model
domain_model = DomainModel(
    name="pDL1",
    types={pDL1_Process, pDL1_ProcessElement, pDL1_WorkDefinition, ProcessElement, pDL1_WorkSequence, pDL1_Guidance, WorkSequenceType},
    associations={processElements0, predecessor1, successor2},
    generalizations={gen_pDL1_WorkDefinition_ProcessElement, gen_pDL1_WorkSequence_ProcessElement, gen_pDL1_Guidance_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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

# Classes
pDL2_Process = Class(name="pDL2::Process")
pDL2_ProcessElement = Class(name="pDL2::ProcessElement")
pDL2_WorkDefinition = Class(name="pDL2::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
pDL2_DependanceStart = Class(name="pDL2::DependanceStart")
pDL2_DependanceFinish = Class(name="pDL2::DependanceFinish")
pDL2_WorkSequenceKindStart = Class(name="pDL2::WorkSequenceKindStart")
pDL2_Guidance = Class(name="pDL2::Guidance")
pDL2_WorkSequenceKindFinish = Class(name="pDL2::WorkSequenceKindFinish")

# pDL2_Process class attributes and methods
pDL2_Process_name: Property = Property(name="name", type=StringType)
pDL2_Process.attributes={pDL2_Process_name}

# pDL2_ProcessElement class attributes and methods

# pDL2_WorkDefinition class attributes and methods
pDL2_WorkDefinition_name: Property = Property(name="name", type=StringType)
pDL2_WorkDefinition.attributes={pDL2_WorkDefinition_name}

# ProcessElement class attributes and methods

# pDL2_DependanceStart class attributes and methods

# pDL2_DependanceFinish class attributes and methods

# pDL2_WorkSequenceKindStart class attributes and methods
pDL2_WorkSequenceKindStart_Started2Start: Property = Property(name="Started2Start", type=StringType)
pDL2_WorkSequenceKindStart_Started2Finish: Property = Property(name="Started2Finish", type=StringType)
pDL2_WorkSequenceKindStart.attributes={pDL2_WorkSequenceKindStart_Started2Finish, pDL2_WorkSequenceKindStart_Started2Start}

# pDL2_Guidance class attributes and methods
pDL2_Guidance_text: Property = Property(name="text", type=StringType)
pDL2_Guidance.attributes={pDL2_Guidance_text}

# pDL2_WorkSequenceKindFinish class attributes and methods
pDL2_WorkSequenceKindFinish_Finished2Start: Property = Property(name="Finished2Start", type=StringType)
pDL2_WorkSequenceKindFinish_Finished2Finish: Property = Property(name="Finished2Finish", type=StringType)
pDL2_WorkSequenceKindFinish.attributes={pDL2_WorkSequenceKindFinish_Finished2Finish, pDL2_WorkSequenceKindFinish_Finished2Start}

# Relationships
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="pDL2_ProcessElement", type=pDL2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_Process", type=pDL2_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToPredecessors1: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors1",
    ends={
        Property(name="pDL2_DependanceStart", type=pDL2_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_WorkDefinition", type=pDL2_DependanceStart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors2: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors2",
    ends={
        Property(name="pDL2_DependanceFinish", type=pDL2_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_WorkDefinition3", type=pDL2_DependanceFinish, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor4: BinaryAssociation = BinaryAssociation(
    name="predecessor4",
    ends={
        Property(name="pDL2_WorkDefinition6", type=pDL2_DependanceStart, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_DependanceStart5", type=pDL2_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
link7: BinaryAssociation = BinaryAssociation(
    name="link7",
    ends={
        Property(name="pDL2_WorkSequenceKindStart", type=pDL2_DependanceStart, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_DependanceStart8", type=pDL2_WorkSequenceKindStart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor9: BinaryAssociation = BinaryAssociation(
    name="predecessor9",
    ends={
        Property(name="pDL2_WorkDefinition11", type=pDL2_DependanceFinish, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_DependanceFinish10", type=pDL2_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
link12: BinaryAssociation = BinaryAssociation(
    name="link12",
    ends={
        Property(name="pDL2_WorkSequenceKindFinish", type=pDL2_DependanceFinish, multiplicity=Multiplicity(1, 1)),
        Property(name="pDL2_DependanceFinish13", type=pDL2_WorkSequenceKindFinish, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pDL2_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=pDL2_WorkDefinition)
gen_pDL2_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=pDL2_Guidance)

# Domain Model
domain_model = DomainModel(
    name="pDL2",
    types={pDL2_Process, pDL2_ProcessElement, pDL2_WorkDefinition, ProcessElement, pDL2_DependanceStart, pDL2_DependanceFinish, pDL2_WorkSequenceKindStart, pDL2_Guidance, pDL2_WorkSequenceKindFinish},
    associations={processElements0, linksToPredecessors1, linksToSuccessors2, predecessor4, link7, predecessor9, link12},
    generalizations={gen_pDL2_WorkDefinition_ProcessElement, gen_pDL2_Guidance_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
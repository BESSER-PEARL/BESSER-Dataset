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
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process.attributes={simplepdl_Process_name}

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name}

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType}

# Relationships
linksToSuccessors4: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors4",
    ends={
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999)),
        Property(name="WorkSequence5", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
predecessor6: BinaryAssociation = BinaryAssociation(
    name="predecessor6",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor7: BinaryAssociation = BinaryAssociation(
    name="successor7",
    ends={
        Property(name="WorkDefinition8", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
activities0: BinaryAssociation = BinaryAssociation(
    name="activities0",
    ends={
        Property(name="simplepdl_WorkDefinition", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
workSequences1: BinaryAssociation = BinaryAssociation(
    name="workSequences1",
    ends={
        Property(name="simplepdl_WorkSequence", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process2", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToPredecessors3: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors3",
    ends={
        Property(name="WorkSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_WorkDefinition, simplepdl_WorkSequence, WorkSequenceType},
    associations={linksToSuccessors4, predecessor6, successor7, activities0, workSequences1, linksToPredecessors3},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
WorkSequenceKind: Enumeration = Enumeration(
    name="WorkSequenceKind",
    literals={
            EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish")
    }
)

# Classes
spem_Process = Class(name="spem::Process")
spem_Activity = Class(name="spem::Activity")
spem_WorkSequence = Class(name="spem::WorkSequence")

# spem_Process class attributes and methods

# spem_Activity class attributes and methods
spem_Activity_name: Property = Property(name="name", type=StringType)
spem_Activity_durationmin: Property = Property(name="durationmin", type=IntegerType)
spem_Activity_durationmax: Property = Property(name="durationmax", type=IntegerType)
spem_Activity.attributes={spem_Activity_name, spem_Activity_durationmin, spem_Activity_durationmax}

# spem_WorkSequence class attributes and methods
spem_WorkSequence_kind: Property = Property(name="kind", type=StringType)
spem_WorkSequence.attributes={spem_WorkSequence_kind}

# Relationships
workSquences1: BinaryAssociation = BinaryAssociation(
    name="workSquences1",
    ends={
        Property(name="process2", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="WorkSequence", type=spem_Process, multiplicity=Multiplicity(1, 1))
    }
)
linkToSuccessor3: BinaryAssociation = BinaryAssociation(
    name="linkToSuccessor3",
    ends={
        Property(name="WorkSequence4", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linkToPredecessor5: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor5",
    ends={
        Property(name="WorkSequence6", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
process7: BinaryAssociation = BinaryAssociation(
    name="process7",
    ends={
        Property(name="Process", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities", type=spem_Process, multiplicity=Multiplicity(1, 1))
    }
)
successor8: BinaryAssociation = BinaryAssociation(
    name="successor8",
    ends={
        Property(name="Activity9", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToPredecessor", type=spem_Activity, multiplicity=Multiplicity(1, 1))
    }
)
activities0: BinaryAssociation = BinaryAssociation(
    name="activities0",
    ends={
        Property(name="Activity", type=spem_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=spem_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor10: BinaryAssociation = BinaryAssociation(
    name="predecessor10",
    ends={
        Property(name="Activity11", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToSuccessor", type=spem_Activity, multiplicity=Multiplicity(1, 1))
    }
)
process12: BinaryAssociation = BinaryAssociation(
    name="process12",
    ends={
        Property(name="Process13", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="workSquences", type=spem_Process, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="spem",
    types={spem_Process, spem_Activity, spem_WorkSequence, WorkSequenceKind},
    associations={workSquences1, linkToSuccessor3, linkToPredecessor5, process7, successor8, activities0, predecessor10, process12},
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
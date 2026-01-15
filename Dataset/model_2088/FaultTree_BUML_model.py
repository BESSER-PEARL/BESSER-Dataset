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
EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="Basic"),
			EnumerationLiteral(name="External"),
			EnumerationLiteral(name="Intermediate"),
			EnumerationLiteral(name="Undeveloped")
    }
)

LogicOperation: Enumeration = Enumeration(
    name="LogicOperation",
    literals={
            EnumerationLiteral(name="Or"),
			EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Xor"),
			EnumerationLiteral(name="PriorityAnd"),
			EnumerationLiteral(name="kOf"),
			EnumerationLiteral(name="kOrmore"),
			EnumerationLiteral(name="kOrless")
    }
)

FaultTreeType: Enumeration = Enumeration(
    name="FaultTreeType",
    literals={
            EnumerationLiteral(name="FaultTree"),
			EnumerationLiteral(name="FaultTrace"),
			EnumerationLiteral(name="MinimalCutSet"),
			EnumerationLiteral(name="CompositeParts")
    }
)

# Classes
FaultTree_Event = Class(name="FaultTree::Event")
FaultTree_EObject = Class(name="FaultTree::EObject")
FaultTree_FaultTree = Class(name="FaultTree::FaultTree")

# FaultTree_Event class attributes and methods
FaultTree_Event_name: Property = Property(name="name", type=StringType)
FaultTree_Event_message: Property = Property(name="message", type=StringType)
FaultTree_Event_k: Property = Property(name="k", type=IntegerType)
FaultTree_Event_assignedProbability: Property = Property(name="assignedProbability", type=StringType)
FaultTree_Event_computedProbability: Property = Property(name="computedProbability", type=StringType)
FaultTree_Event_referenceCount: Property = Property(name="referenceCount", type=IntegerType)
FaultTree_Event_type: Property = Property(name="type", type=StringType)
FaultTree_Event_subEventLogic: Property = Property(name="subEventLogic", type=StringType)
FaultTree_Event_scale: Property = Property(name="scale", type=StringType)
FaultTree_Event_m_getProbability: Method = Method(name="getProbability", parameters={}, type=StringType)
FaultTree_Event.attributes={FaultTree_Event_type, FaultTree_Event_computedProbability, FaultTree_Event_assignedProbability, FaultTree_Event_message, FaultTree_Event_subEventLogic, FaultTree_Event_referenceCount, FaultTree_Event_scale, FaultTree_Event_k, FaultTree_Event_name}
FaultTree_Event.methods={FaultTree_Event_m_getProbability}

# FaultTree_EObject class attributes and methods

# FaultTree_FaultTree class attributes and methods
FaultTree_FaultTree_name: Property = Property(name="name", type=StringType)
FaultTree_FaultTree_message: Property = Property(name="message", type=StringType)
FaultTree_FaultTree_faultTreeType: Property = Property(name="faultTreeType", type=StringType)
FaultTree_FaultTree.attributes={FaultTree_FaultTree_message, FaultTree_FaultTree_faultTreeType, FaultTree_FaultTree_name}

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="FaultTree_Event", type=FaultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_FaultTree", type=FaultTree_Event, multiplicity=Multiplicity(0, 1))
    }
)
events3: BinaryAssociation = BinaryAssociation(
    name="events3",
    ends={
        Property(name="FaultTree_Event5", type=FaultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_FaultTree4", type=FaultTree_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instanceRoot1: BinaryAssociation = BinaryAssociation(
    name="instanceRoot1",
    ends={
        Property(name="FaultTree_EObject", type=FaultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_FaultTree2", type=FaultTree_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subEvents7: BinaryAssociation = BinaryAssociation(
    name="subEvents7",
    ends={
        Property(name="FaultTree_Event6", type=FaultTree_Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="FaultTree_Event8", type=FaultTree_Event, multiplicity=Multiplicity(1, 1))
    }
)
relatedInstanceObject9: BinaryAssociation = BinaryAssociation(
    name="relatedInstanceObject9",
    ends={
        Property(name="FaultTree_EObject11", type=FaultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_Event10", type=FaultTree_EObject, multiplicity=Multiplicity(0, 1))
    }
)
relatedErrorType12: BinaryAssociation = BinaryAssociation(
    name="relatedErrorType12",
    ends={
        Property(name="FaultTree_EObject14", type=FaultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_Event13", type=FaultTree_EObject, multiplicity=Multiplicity(0, 1))
    }
)
relatedEMV2Object15: BinaryAssociation = BinaryAssociation(
    name="relatedEMV2Object15",
    ends={
        Property(name="FaultTree_EObject17", type=FaultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="FaultTree_Event16", type=FaultTree_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="FaultTree",
    types={FaultTree_Event, FaultTree_EObject, FaultTree_FaultTree, EventType, LogicOperation, FaultTreeType},
    associations={root0, events3, instanceRoot1, subEvents7, relatedInstanceObject9, relatedErrorType12, relatedEMV2Object15},
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
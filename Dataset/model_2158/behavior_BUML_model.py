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
behavior_UseCaseRepository = Class(name="behavior::UseCaseRepository")
behavior_SessionRepository = Class(name="behavior::SessionRepository")
behavior_Session = Class(name="behavior::Session")
behavior_ObservedUseCaseExecution = Class(name="behavior::ObservedUseCaseExecution")
AbstractUseCaseExecution = Class(name="AbstractUseCaseExecution")
behavior_AbstractUseCaseExecution = Class(name="behavior::AbstractUseCaseExecution", is_abstract=True)
behavior_AbstractBehaviorModelGraph = Class(name="behavior::AbstractBehaviorModelGraph", is_abstract=True)
behavior_Vertex = Class(name="behavior::Vertex")
behavior_UseCase = Class(name="behavior::UseCase")
behavior_Transition = Class(name="behavior::Transition")
behavior_BehaviorModelAbsolute = Class(name="behavior::BehaviorModelAbsolute")
AbstractBehaviorModelGraph = Class(name="AbstractBehaviorModelGraph")
behavior_BehaviorModelRelative = Class(name="behavior::BehaviorModelRelative")
behavior_BehaviorMix = Class(name="behavior::BehaviorMix")
behavior_BehaviorMixEntry = Class(name="behavior::BehaviorMixEntry")

# behavior_UseCaseRepository class attributes and methods

# behavior_SessionRepository class attributes and methods

# behavior_Session class attributes and methods
behavior_Session_id: Property = Property(name="id", type=StringType)
behavior_Session_startTime: Property = Property(name="startTime", type=StringType)
behavior_Session_endTime: Property = Property(name="endTime", type=StringType)
behavior_Session_transactionType: Property = Property(name="transactionType", type=StringType)
behavior_Session.attributes={behavior_Session_startTime, behavior_Session_endTime, behavior_Session_id, behavior_Session_transactionType}

# behavior_ObservedUseCaseExecution class attributes and methods
behavior_ObservedUseCaseExecution_startTime: Property = Property(name="startTime", type=StringType)
behavior_ObservedUseCaseExecution_endTime: Property = Property(name="endTime", type=StringType)
behavior_ObservedUseCaseExecution.attributes={behavior_ObservedUseCaseExecution_startTime, behavior_ObservedUseCaseExecution_endTime}

# AbstractUseCaseExecution class attributes and methods

# behavior_AbstractUseCaseExecution class attributes and methods

# behavior_AbstractBehaviorModelGraph class attributes and methods
behavior_AbstractBehaviorModelGraph_transactionType: Property = Property(name="transactionType", type=StringType)
behavior_AbstractBehaviorModelGraph.attributes={behavior_AbstractBehaviorModelGraph_transactionType}

# behavior_Vertex class attributes and methods

# behavior_UseCase class attributes and methods
behavior_UseCase_name: Property = Property(name="name", type=StringType)
behavior_UseCase_id: Property = Property(name="id", type=StringType)
behavior_UseCase.attributes={behavior_UseCase_id, behavior_UseCase_name}

# behavior_Transition class attributes and methods
behavior_Transition_value: Property = Property(name="value", type=FloatType)
behavior_Transition_timeDiffs: Property = Property(name="timeDiffs", type=StringType)
behavior_Transition_thinkTimeParams: Property = Property(name="thinkTimeParams", type=StringType)
behavior_Transition.attributes={behavior_Transition_thinkTimeParams, behavior_Transition_value, behavior_Transition_timeDiffs}

# behavior_BehaviorModelAbsolute class attributes and methods

# AbstractBehaviorModelGraph class attributes and methods

# behavior_BehaviorModelRelative class attributes and methods

# behavior_BehaviorMix class attributes and methods

# behavior_BehaviorMixEntry class attributes and methods
behavior_BehaviorMixEntry_behaviorModelName: Property = Property(name="behaviorModelName", type=StringType)
behavior_BehaviorMixEntry_relativeFrequency: Property = Property(name="relativeFrequency", type=FloatType)
behavior_BehaviorMixEntry.attributes={behavior_BehaviorMixEntry_relativeFrequency, behavior_BehaviorMixEntry_behaviorModelName}

# Relationships
useCases0: BinaryAssociation = BinaryAssociation(
    name="useCases0",
    ends={
        Property(name="behavior_UseCase", type=behavior_UseCaseRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_UseCaseRepository", type=behavior_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions1: BinaryAssociation = BinaryAssociation(
    name="sessions1",
    ends={
        Property(name="behavior_Session", type=behavior_SessionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_SessionRepository", type=behavior_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observedUseCaseExecutions2: BinaryAssociation = BinaryAssociation(
    name="observedUseCaseExecutions2",
    ends={
        Property(name="behavior_ObservedUseCaseExecution", type=behavior_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Session3", type=behavior_ObservedUseCaseExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase4: BinaryAssociation = BinaryAssociation(
    name="useCase4",
    ends={
        Property(name="behavior_UseCase5", type=behavior_AbstractUseCaseExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_AbstractUseCaseExecution", type=behavior_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
vertices6: BinaryAssociation = BinaryAssociation(
    name="vertices6",
    ends={
        Property(name="behavior_Vertex", type=behavior_AbstractBehaviorModelGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_AbstractBehaviorModelGraph", type=behavior_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorModel16: BinaryAssociation = BinaryAssociation(
    name="behaviorModel16",
    ends={
        Property(name="behavior_BehaviorModelRelative", type=behavior_BehaviorMixEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_BehaviorMixEntry17", type=behavior_BehaviorModelRelative, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions7: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions7",
    ends={
        Property(name="behavior_Transition", type=behavior_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Vertex8", type=behavior_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetVertex9: BinaryAssociation = BinaryAssociation(
    name="targetVertex9",
    ends={
        Property(name="behavior_Vertex11", type=behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Transition10", type=behavior_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
sourceVertex12: BinaryAssociation = BinaryAssociation(
    name="sourceVertex12",
    ends={
        Property(name="behavior_Vertex14", type=behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Transition13", type=behavior_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
entries15: BinaryAssociation = BinaryAssociation(
    name="entries15",
    ends={
        Property(name="behavior_BehaviorMixEntry", type=behavior_BehaviorMix, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_BehaviorMix", type=behavior_BehaviorMixEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_behavior_ObservedUseCaseExecution_AbstractUseCaseExecution = Generalization(general=AbstractUseCaseExecution, specific=behavior_ObservedUseCaseExecution)
gen_behavior_Vertex_AbstractUseCaseExecution = Generalization(general=AbstractUseCaseExecution, specific=behavior_Vertex)
gen_behavior_BehaviorModelAbsolute_AbstractBehaviorModelGraph = Generalization(general=AbstractBehaviorModelGraph, specific=behavior_BehaviorModelAbsolute)
gen_behavior_BehaviorModelRelative_AbstractBehaviorModelGraph = Generalization(general=AbstractBehaviorModelGraph, specific=behavior_BehaviorModelRelative)

# Domain Model
domain_model = DomainModel(
    name="behavior",
    types={behavior_UseCaseRepository, behavior_SessionRepository, behavior_Session, behavior_ObservedUseCaseExecution, AbstractUseCaseExecution, behavior_AbstractUseCaseExecution, behavior_AbstractBehaviorModelGraph, behavior_Vertex, behavior_UseCase, behavior_Transition, behavior_BehaviorModelAbsolute, AbstractBehaviorModelGraph, behavior_BehaviorModelRelative, behavior_BehaviorMix, behavior_BehaviorMixEntry},
    associations={useCases0, sessions1, observedUseCaseExecutions2, useCase4, vertices6, behaviorModel16, outgoingTransitions7, targetVertex9, sourceVertex12, entries15},
    generalizations={gen_behavior_ObservedUseCaseExecution_AbstractUseCaseExecution, gen_behavior_Vertex_AbstractUseCaseExecution, gen_behavior_BehaviorModelAbsolute_AbstractBehaviorModelGraph, gen_behavior_BehaviorModelRelative_AbstractBehaviorModelGraph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
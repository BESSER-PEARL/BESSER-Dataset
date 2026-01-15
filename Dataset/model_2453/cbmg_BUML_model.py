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
cbmg_State = Class(name="cbmg::State")
cbmg_Transition = Class(name="cbmg::Transition")
cbmg_RequestParameter = Class(name="cbmg::RequestParameter")

# cbmg_State class attributes and methods
cbmg_State_port: Property = Property(name="port", type=IntegerType)
cbmg_State_localName: Property = Property(name="localName", type=StringType)
cbmg_State_isStartState: Property = Property(name="isStartState", type=BooleanType)
cbmg_State_isEndState: Property = Property(name="isEndState", type=BooleanType)
cbmg_State_requestURL: Property = Property(name="requestURL", type=StringType)
cbmg_State_localAddr: Property = Property(name="localAddr", type=StringType)
cbmg_State.attributes={cbmg_State_isEndState, cbmg_State_localAddr, cbmg_State_localName, cbmg_State_isStartState, cbmg_State_requestURL, cbmg_State_port}

# cbmg_Transition class attributes and methods
cbmg_Transition_method: Property = Property(name="method", type=StringType)
cbmg_Transition_probability: Property = Property(name="probability", type=FloatType)
cbmg_Transition_thinkTime: Property = Property(name="thinkTime", type=FloatType)
cbmg_Transition_nbrOfTransitions: Property = Property(name="nbrOfTransitions", type=IntegerType)
cbmg_Transition_accept: Property = Property(name="accept", type=StringType)
cbmg_Transition_condition: Property = Property(name="condition", type=StringType)
cbmg_Transition.attributes={cbmg_Transition_accept, cbmg_Transition_condition, cbmg_Transition_nbrOfTransitions, cbmg_Transition_probability, cbmg_Transition_method, cbmg_Transition_thinkTime}

# cbmg_RequestParameter class attributes and methods
cbmg_RequestParameter_parameterName: Property = Property(name="parameterName", type=StringType)
cbmg_RequestParameter_parameterValue: Property = Property(name="parameterValue", type=StringType)
cbmg_RequestParameter.attributes={cbmg_RequestParameter_parameterName, cbmg_RequestParameter_parameterValue}

# Relationships
outgoingTransitions0: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions0",
    ends={
        Property(name="cbmg_Transition", type=cbmg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_State", type=cbmg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
sourceState4: BinaryAssociation = BinaryAssociation(
    name="sourceState4",
    ends={
        Property(name="cbmg_State6", type=cbmg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_Transition5", type=cbmg_State, multiplicity=Multiplicity(1, 1))
    }
)
targetState7: BinaryAssociation = BinaryAssociation(
    name="targetState7",
    ends={
        Property(name="cbmg_State9", type=cbmg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_Transition8", type=cbmg_State, multiplicity=Multiplicity(1, 1))
    }
)
requestParameter_transition10: BinaryAssociation = BinaryAssociation(
    name="requestParameter_transition10",
    ends={
        Property(name="cbmg_RequestParameter", type=cbmg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_Transition11", type=cbmg_RequestParameter, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions1: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions1",
    ends={
        Property(name="cbmg_Transition3", type=cbmg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_State2", type=cbmg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transition_RequestParameter12: BinaryAssociation = BinaryAssociation(
    name="transition_RequestParameter12",
    ends={
        Property(name="cbmg_Transition14", type=cbmg_RequestParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cbmg_RequestParameter13", type=cbmg_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="cbmg",
    types={cbmg_State, cbmg_Transition, cbmg_RequestParameter},
    associations={outgoingTransitions0, sourceState4, targetState7, requestParameter_transition10, incomingTransitions1, transition_RequestParameter12},
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
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
myDsl_Statemachine = Class(name="myDsl_Statemachine")
myDsl_Event = Class(name="myDsl_Event")
myDsl_Service = Class(name="myDsl_Service")
myDsl_JvmTypeReference = Class(name="myDsl_JvmTypeReference")
myDsl_XExpression = Class(name="myDsl_XExpression")
myDsl_Transition = Class(name="myDsl_Transition")
myDsl_State = Class(name="myDsl_State")

# myDsl_Statemachine class attributes and methods

# myDsl_Event class attributes and methods
myDsl_Event_resetEvent: Property = Property(name="resetEvent", type=BooleanType)
myDsl_Event_name: Property = Property(name="name", type=StringType)
myDsl_Event.attributes={myDsl_Event_resetEvent, myDsl_Event_name}

# myDsl_Service class attributes and methods
myDsl_Service_name: Property = Property(name="name", type=StringType)
myDsl_Service.attributes={myDsl_Service_name}

# myDsl_JvmTypeReference class attributes and methods

# myDsl_XExpression class attributes and methods

# myDsl_Transition class attributes and methods

# myDsl_State class attributes and methods
myDsl_State_name: Property = Property(name="name", type=StringType)
myDsl_State.attributes={myDsl_State_name}

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="myDsl_Event", type=myDsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statemachine", type=myDsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services1: BinaryAssociation = BinaryAssociation(
    name="services1",
    ends={
        Property(name="myDsl_Service", type=myDsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statemachine2", type=myDsl_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="myDsl_JvmTypeReference", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service6", type=myDsl_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action7: BinaryAssociation = BinaryAssociation(
    name="action7",
    ends={
        Property(name="myDsl_XExpression", type=myDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_State8", type=myDsl_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="myDsl_Transition", type=myDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_State10", type=myDsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="myDsl_State", type=myDsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statemachine4", type=myDsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event11: BinaryAssociation = BinaryAssociation(
    name="event11",
    ends={
        Property(name="myDsl_Transition12", type=myDsl_Event, multiplicity=Multiplicity(0, 1)),
        Property(name="myDsl_Event13", type=myDsl_Transition, multiplicity=Multiplicity(1, 1))
    }
)
state14: BinaryAssociation = BinaryAssociation(
    name="state14",
    ends={
        Property(name="myDsl_State16", type=myDsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Transition15", type=myDsl_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Statemachine, myDsl_Event, myDsl_Service, myDsl_JvmTypeReference, myDsl_XExpression, myDsl_Transition, myDsl_State},
    associations={events0, services1, type5, action7, transitions9, states3, event11, state14},
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
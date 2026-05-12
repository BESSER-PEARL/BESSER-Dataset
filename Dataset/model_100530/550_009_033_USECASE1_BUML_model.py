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
USECASE1_Task = Class(name="USECASE1_Task")
Service = Class(name="Service")
USECASE1_User = Class(name="USECASE1_User")
USECASE1_UseCase = Class(name="USECASE1_UseCase")
Context = Class(name="Context")
UseCase = Class(name="UseCase")
Actor = Class(name="Actor")
USECASE1_Actor = Class(name="USECASE1_Actor")
Goal = Class(name="Goal")
User = Class(name="User")
USECASE1_Goal = Class(name="USECASE1_Goal")
PreCondition = Class(name="PreCondition")
PostCondition = Class(name="PostCondition")
USECASE1_Service = Class(name="USECASE1_Service")
Task = Class(name="Task")
USECASE1_Scenario = Class(name="USECASE1_Scenario")
USECASE1_Action = Class(name="USECASE1_Action")
USECASE1_Context = Class(name="USECASE1_Context")
USECASE1_Responce = Class(name="USECASE1_Responce")
Parameter_ = Class(name="Parameter")
USECASE1_Stimilus = Class(name="USECASE1_Stimilus")
USECASE1_PreCondition = Class(name="USECASE1_PreCondition")
USECASE1_PostCondition = Class(name="USECASE1_PostCondition")
USECASE1_Episode = Class(name="USECASE1_Episode")
Event = Class(name="Event")
USECASE1_Event = Class(name="USECASE1_Event")
Episode = Class(name="Episode")
USECASE1_Parameter = Class(name="USECASE1_Parameter")
Stimilus = Class(name="Stimilus")
Responce = Class(name="Responce")

# USECASE1_Task class attributes and methods

# Service class attributes and methods

# USECASE1_User class attributes and methods

# USECASE1_UseCase class attributes and methods

# Context class attributes and methods

# UseCase class attributes and methods

# Actor class attributes and methods

# USECASE1_Actor class attributes and methods

# Goal class attributes and methods

# User class attributes and methods

# USECASE1_Goal class attributes and methods

# PreCondition class attributes and methods

# PostCondition class attributes and methods

# USECASE1_Service class attributes and methods

# Task class attributes and methods

# USECASE1_Scenario class attributes and methods

# USECASE1_Action class attributes and methods

# USECASE1_Context class attributes and methods

# USECASE1_Responce class attributes and methods

# Parameter class attributes and methods

# USECASE1_Stimilus class attributes and methods

# USECASE1_PreCondition class attributes and methods

# USECASE1_PostCondition class attributes and methods

# USECASE1_Episode class attributes and methods

# Event class attributes and methods

# USECASE1_Event class attributes and methods

# Episode class attributes and methods

# USECASE1_Parameter class attributes and methods

# Stimilus class attributes and methods

# Responce class attributes and methods

# Relationships
service0: BinaryAssociation = BinaryAssociation(
    name="service0",
    ends={
        Property(name="Service", type=USECASE1_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="task", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)
actor12: BinaryAssociation = BinaryAssociation(
    name="actor12",
    ends={
        Property(name="Actor14", type=USECASE1_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal13", type=Actor, multiplicity=Multiplicity(1, 9999))
    }
)
context15: BinaryAssociation = BinaryAssociation(
    name="context15",
    ends={
        Property(name="Context", type=USECASE1_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
service16: BinaryAssociation = BinaryAssociation(
    name="service16",
    ends={
        Property(name="Service18", type=USECASE1_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase17", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
useCase1: BinaryAssociation = BinaryAssociation(
    name="useCase1",
    ends={
        Property(name="UseCase", type=USECASE1_User, multiplicity=Multiplicity(1, 1)),
        Property(name="user", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
actor2: BinaryAssociation = BinaryAssociation(
    name="actor2",
    ends={
        Property(name="Actor", type=USECASE1_User, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=Actor, multiplicity=Multiplicity(0, 9999))
    }
)
useCase4: BinaryAssociation = BinaryAssociation(
    name="useCase4",
    ends={
        Property(name="UseCase5", type=USECASE1_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
goal6: BinaryAssociation = BinaryAssociation(
    name="goal6",
    ends={
        Property(name="Goal", type=USECASE1_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor7", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
user8: BinaryAssociation = BinaryAssociation(
    name="user8",
    ends={
        Property(name="User", type=USECASE1_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor9", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
service10: BinaryAssociation = BinaryAssociation(
    name="service10",
    ends={
        Property(name="Service11", type=USECASE1_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)
preCondition32: BinaryAssociation = BinaryAssociation(
    name="preCondition32",
    ends={
        Property(name="PreCondition", type=USECASE1_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=PreCondition, multiplicity=Multiplicity(1, 9999))
    }
)
postCondition33: BinaryAssociation = BinaryAssociation(
    name="postCondition33",
    ends={
        Property(name="PostCondition", type=USECASE1_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="context34", type=PostCondition, multiplicity=Multiplicity(1, 9999))
    }
)
useCase35: BinaryAssociation = BinaryAssociation(
    name="useCase35",
    ends={
        Property(name="UseCase37", type=USECASE1_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="context36", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
user19: BinaryAssociation = BinaryAssociation(
    name="user19",
    ends={
        Property(name="User21", type=USECASE1_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase20", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
actor22: BinaryAssociation = BinaryAssociation(
    name="actor22",
    ends={
        Property(name="Actor24", type=USECASE1_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase23", type=Actor, multiplicity=Multiplicity(0, 9999))
    }
)
useCase25: BinaryAssociation = BinaryAssociation(
    name="useCase25",
    ends={
        Property(name="UseCase26", type=USECASE1_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
goal27: BinaryAssociation = BinaryAssociation(
    name="goal27",
    ends={
        Property(name="Goal29", type=USECASE1_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service28", type=Goal, multiplicity=Multiplicity(1, 9999))
    }
)
task30: BinaryAssociation = BinaryAssociation(
    name="task30",
    ends={
        Property(name="Task", type=USECASE1_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service31", type=Task, multiplicity=Multiplicity(1, 9999))
    }
)
parameter44: BinaryAssociation = BinaryAssociation(
    name="parameter44",
    ends={
        Property(name="Parameter", type=USECASE1_Responce, multiplicity=Multiplicity(1, 1)),
        Property(name="responce", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter45: BinaryAssociation = BinaryAssociation(
    name="parameter45",
    ends={
        Property(name="Parameter46", type=USECASE1_Stimilus, multiplicity=Multiplicity(1, 1)),
        Property(name="stimilus", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context38: BinaryAssociation = BinaryAssociation(
    name="context38",
    ends={
        Property(name="Context39", type=USECASE1_PreCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="preCondition", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
context40: BinaryAssociation = BinaryAssociation(
    name="context40",
    ends={
        Property(name="Context41", type=USECASE1_PostCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="postCondition", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
event42: BinaryAssociation = BinaryAssociation(
    name="event42",
    ends={
        Property(name="Event", type=USECASE1_Episode, multiplicity=Multiplicity(1, 1)),
        Property(name="episode", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
episode43: BinaryAssociation = BinaryAssociation(
    name="episode43",
    ends={
        Property(name="Episode", type=USECASE1_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="event", type=Episode, multiplicity=Multiplicity(1, 9999))
    }
)
stimilus47: BinaryAssociation = BinaryAssociation(
    name="stimilus47",
    ends={
        Property(name="Stimilus", type=USECASE1_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=Stimilus, multiplicity=Multiplicity(1, 9999))
    }
)
responce48: BinaryAssociation = BinaryAssociation(
    name="responce48",
    ends={
        Property(name="Responce", type=USECASE1_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter49", type=Responce, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_USECASE1_Action_Event = Generalization(general=Event, specific=USECASE1_Action)
gen_USECASE1_Responce_Event = Generalization(general=Event, specific=USECASE1_Responce)
gen_USECASE1_Stimilus_Event = Generalization(general=Event, specific=USECASE1_Stimilus)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={USECASE1_Task, Service, USECASE1_User, USECASE1_UseCase, Context, UseCase, Actor, USECASE1_Actor, Goal, User, USECASE1_Goal, PreCondition, PostCondition, USECASE1_Service, Task, USECASE1_Scenario, USECASE1_Action, USECASE1_Context, USECASE1_Responce, Parameter_, USECASE1_Stimilus, USECASE1_PreCondition, USECASE1_PostCondition, USECASE1_Episode, Event, USECASE1_Event, Episode, USECASE1_Parameter, Stimilus, Responce},
    associations={service0, actor12, context15, service16, useCase1, actor2, useCase4, goal6, user8, service10, preCondition32, postCondition33, useCase35, user19, actor22, useCase25, goal27, task30, parameter44, parameter45, context38, context40, event42, episode43, stimilus47, responce48},
    generalizations={gen_USECASE1_Action_Event, gen_USECASE1_Responce_Event, gen_USECASE1_Stimilus_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
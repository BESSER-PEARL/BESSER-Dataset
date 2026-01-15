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
DurationUnit: Enumeration = Enumeration(
    name="DurationUnit",
    literals={
            EnumerationLiteral(name="MILLISECONDS"),
			EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MINUTES")
    }
)

Intensity: Enumeration = Enumeration(
    name="Intensity",
    literals={
            EnumerationLiteral(name="C"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="E")
    }
)

# Classes
roc_Movement = Class(name="roc::Movement")
roc_Motion = Class(name="roc::Motion")
roc_Action = Class(name="roc::Action")
roc_Speed = Class(name="roc::Speed")
roc_Program = Class(name="roc::Program")
roc_FullDirectedAction = Class(name="roc::FullDirectedAction")
roc_Direction = Class(name="roc::Direction")
roc_EObject = Class(name="roc::EObject")
roc_CompleteAction = Class(name="roc::CompleteAction")
roc_SingleAction = Class(name="roc::SingleAction")
roc_DirectedAction = Class(name="roc::DirectedAction")
roc_LeftRightDirectedAction = Class(name="roc::LeftRightDirectedAction")
roc_LeftRightDirection = Class(name="roc::LeftRightDirection")

# roc_Movement class attributes and methods

# roc_Motion class attributes and methods
roc_Motion_duration: Property = Property(name="duration", type=StringType)
roc_Motion_durationUnit: Property = Property(name="durationUnit", type=StringType)
roc_Motion.attributes={roc_Motion_durationUnit, roc_Motion_duration}

# roc_Action class attributes and methods
roc_Action_intensity: Property = Property(name="intensity", type=StringType)
roc_Action.attributes={roc_Action_intensity}

# roc_Speed class attributes and methods
roc_Speed_SLOWEST: Property = Property(name="SLOWEST", type=StringType)
roc_Speed_SLOW: Property = Property(name="SLOW", type=StringType)
roc_Speed_NORMAL: Property = Property(name="NORMAL", type=StringType)
roc_Speed_FAST: Property = Property(name="FAST", type=StringType)
roc_Speed_FULL: Property = Property(name="FULL", type=StringType)
roc_Speed.attributes={roc_Speed_FULL, roc_Speed_SLOW, roc_Speed_NORMAL, roc_Speed_SLOWEST, roc_Speed_FAST}

# roc_Program class attributes and methods

# roc_FullDirectedAction class attributes and methods
roc_FullDirectedAction_turnHead: Property = Property(name="turnHead", type=StringType)
roc_FullDirectedAction_turnEyes: Property = Property(name="turnEyes", type=StringType)
roc_FullDirectedAction.attributes={roc_FullDirectedAction_turnHead, roc_FullDirectedAction_turnEyes}

# roc_Direction class attributes and methods
roc_Direction_UP: Property = Property(name="UP", type=StringType)
roc_Direction_DOWN: Property = Property(name="DOWN", type=StringType)
roc_Direction_LEFT: Property = Property(name="LEFT", type=StringType)
roc_Direction_RIGHT: Property = Property(name="RIGHT", type=StringType)
roc_Direction.attributes={roc_Direction_LEFT, roc_Direction_RIGHT, roc_Direction_UP, roc_Direction_DOWN}

# roc_EObject class attributes and methods

# roc_CompleteAction class attributes and methods
roc_CompleteAction_actionName: Property = Property(name="actionName", type=StringType)
roc_CompleteAction.attributes={roc_CompleteAction_actionName}

# roc_SingleAction class attributes and methods
roc_SingleAction_actionName: Property = Property(name="actionName", type=StringType)
roc_SingleAction.attributes={roc_SingleAction_actionName}

# roc_DirectedAction class attributes and methods

# roc_LeftRightDirectedAction class attributes and methods
roc_LeftRightDirectedAction_tiltHead: Property = Property(name="tiltHead", type=StringType)
roc_LeftRightDirectedAction.attributes={roc_LeftRightDirectedAction_tiltHead}

# roc_LeftRightDirection class attributes and methods
roc_LeftRightDirection_right: Property = Property(name="right", type=StringType)
roc_LeftRightDirection_left: Property = Property(name="left", type=StringType)
roc_LeftRightDirection.attributes={roc_LeftRightDirection_left, roc_LeftRightDirection_right}

# Relationships
movements0: BinaryAssociation = BinaryAssociation(
    name="movements0",
    ends={
        Property(name="roc_Movement", type=roc_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_Program", type=roc_Movement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
motions1: BinaryAssociation = BinaryAssociation(
    name="motions1",
    ends={
        Property(name="roc_Motion", type=roc_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_Movement2", type=roc_Motion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action3: BinaryAssociation = BinaryAssociation(
    name="action3",
    ends={
        Property(name="roc_Action", type=roc_Motion, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_Motion4", type=roc_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
speed5: BinaryAssociation = BinaryAssociation(
    name="speed5",
    ends={
        Property(name="roc_Speed", type=roc_Motion, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_Motion6", type=roc_Speed, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionHolder7: BinaryAssociation = BinaryAssociation(
    name="actionHolder7",
    ends={
        Property(name="roc_EObject", type=roc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_Action8", type=roc_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionName9: BinaryAssociation = BinaryAssociation(
    name="actionName9",
    ends={
        Property(name="roc_EObject10", type=roc_DirectedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_DirectedAction", type=roc_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direction11: BinaryAssociation = BinaryAssociation(
    name="direction11",
    ends={
        Property(name="roc_EObject13", type=roc_DirectedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roc_DirectedAction12", type=roc_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="roc",
    types={roc_Movement, roc_Motion, roc_Action, roc_Speed, roc_Program, roc_FullDirectedAction, roc_Direction, roc_EObject, roc_CompleteAction, roc_SingleAction, roc_DirectedAction, roc_LeftRightDirectedAction, roc_LeftRightDirection, DurationUnit, Intensity},
    associations={movements0, motions1, action3, speed5, actionHolder7, actionName9, direction11},
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
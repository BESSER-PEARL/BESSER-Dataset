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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="FORWARD"),
			EnumerationLiteral(name="BACKWARD")
    }
)

# Classes
dSL_ConditionList = Class(name="dSL_ConditionList")
dSL_Specification = Class(name="dSL_Specification")
dSL_Rule = Class(name="dSL_Rule")
dSL_Action = Class(name="dSL_Action")
dSL_ActionList = Class(name="dSL_ActionList")
dSL_Condition = Class(name="dSL_Condition")
dSL_Distance = Class(name="dSL_Distance")
dSL_Angle = Class(name="dSL_Angle")

# dSL_ConditionList class attributes and methods

# dSL_Specification class attributes and methods

# dSL_Rule class attributes and methods

# dSL_Action class attributes and methods
dSL_Action_showLakes: Property = Property(name="showLakes", type=BooleanType)
dSL_Action_driveDirection: Property = Property(name="driveDirection", type=BooleanType)
dSL_Action_direction: Property = Property(name="direction", type=StringType)
dSL_Action_driveDistance: Property = Property(name="driveDistance", type=BooleanType)
dSL_Action_steer: Property = Property(name="steer", type=BooleanType)
dSL_Action_probeLake: Property = Property(name="probeLake", type=BooleanType)
dSL_Action_blinkLights: Property = Property(name="blinkLights", type=BooleanType)
dSL_Action.attributes={dSL_Action_showLakes, dSL_Action_steer, dSL_Action_direction, dSL_Action_probeLake, dSL_Action_driveDistance, dSL_Action_blinkLights, dSL_Action_driveDirection}

# dSL_ActionList class attributes and methods

# dSL_Condition class attributes and methods
dSL_Condition_not_: Property = Property(name="not_", type=BooleanType)
dSL_Condition_allLakes: Property = Property(name="allLakes", type=BooleanType)
dSL_Condition_collision: Property = Property(name="collision", type=BooleanType)
dSL_Condition_atLake: Property = Property(name="atLake", type=BooleanType)
dSL_Condition_isProbed: Property = Property(name="isProbed", type=BooleanType)
dSL_Condition.attributes={dSL_Condition_collision, dSL_Condition_isProbed, dSL_Condition_allLakes, dSL_Condition_atLake, dSL_Condition_not_}

# dSL_Distance class attributes and methods
dSL_Distance_value: Property = Property(name="value", type=IntegerType)
dSL_Distance.attributes={dSL_Distance_value}

# dSL_Angle class attributes and methods
dSL_Angle_value: Property = Property(name="value", type=IntegerType)
dSL_Angle_away: Property = Property(name="away", type=BooleanType)
dSL_Angle.attributes={dSL_Angle_away, dSL_Angle_value}

# Relationships
rule0: BinaryAssociation = BinaryAssociation(
    name="rule0",
    ends={
        Property(name="dSL_Rule", type=dSL_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Specification", type=dSL_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionList1: BinaryAssociation = BinaryAssociation(
    name="conditionList1",
    ends={
        Property(name="dSL_ConditionList", type=dSL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Rule2", type=dSL_ConditionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions12: BinaryAssociation = BinaryAssociation(
    name="actions12",
    ends={
        Property(name="dSL_Action", type=dSL_ActionList, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ActionList13", type=dSL_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionList3: BinaryAssociation = BinaryAssociation(
    name="actionList3",
    ends={
        Property(name="dSL_ActionList", type=dSL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Rule4", type=dSL_ActionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions5: BinaryAssociation = BinaryAssociation(
    name="conditions5",
    ends={
        Property(name="dSL_Condition", type=dSL_ConditionList, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ConditionList6", type=dSL_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="dSL_Condition9", type=dSL_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Condition7", type=dSL_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance10: BinaryAssociation = BinaryAssociation(
    name="distance10",
    ends={
        Property(name="dSL_Distance", type=dSL_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Condition11", type=dSL_Distance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance14: BinaryAssociation = BinaryAssociation(
    name="distance14",
    ends={
        Property(name="dSL_Distance16", type=dSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Action15", type=dSL_Distance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle17: BinaryAssociation = BinaryAssociation(
    name="angle17",
    ends={
        Property(name="dSL_Angle", type=dSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Action18", type=dSL_Angle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="dSL",
    types={dSL_ConditionList, dSL_Specification, dSL_Rule, dSL_Action, dSL_ActionList, dSL_Condition, dSL_Distance, dSL_Angle, Direction},
    associations={rule0, conditionList1, actions12, actionList3, conditions5, condition8, distance10, distance14, angle17},
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
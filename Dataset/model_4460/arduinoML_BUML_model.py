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
Signal: Enumeration = Enumeration(
    name="Signal",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="LOW")
    }
)

Comparator: Enumeration = Enumeration(
    name="Comparator",
    literals={
            EnumerationLiteral(name="sup"),
			EnumerationLiteral(name="inf"),
			EnumerationLiteral(name="equ"),
			EnumerationLiteral(name="esup"),
			EnumerationLiteral(name="einf")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="analog"),
			EnumerationLiteral(name="digital")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
arduinoML_Brick = Class(name="arduinoML::Brick", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduinoML_Actuator = Class(name="arduinoML::Actuator")
Brick = Class(name="Brick")
arduinoML_Sensor = Class(name="arduinoML::Sensor")
arduinoML_BaseCondition = Class(name="arduinoML::BaseCondition")
arduinoML_App = Class(name="arduinoML::App")
arduinoML_State = Class(name="arduinoML::State")
arduinoML_Action = Class(name="arduinoML::Action")
arduinoML_Transition = Class(name="arduinoML::Transition")
arduinoML_SinkError = Class(name="arduinoML::SinkError")
arduinoML_BooleanCondition = Class(name="arduinoML::BooleanCondition")
arduinoML_NamedElement = Class(name="arduinoML::NamedElement", is_abstract=True)
arduinoML_Condition = Class(name="arduinoML::Condition", is_abstract=True)
Condition = Class(name="Condition")

# arduinoML_Brick class attributes and methods
arduinoML_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoML_Brick_type: Property = Property(name="type", type=StringType)
arduinoML_Brick.attributes={arduinoML_Brick_type, arduinoML_Brick_pin}

# NamedElement class attributes and methods

# arduinoML_Actuator class attributes and methods

# Brick class attributes and methods

# arduinoML_Sensor class attributes and methods

# arduinoML_BaseCondition class attributes and methods

# arduinoML_App class attributes and methods

# arduinoML_State class attributes and methods

# arduinoML_Action class attributes and methods
arduinoML_Action_analogvalue: Property = Property(name="analogvalue", type=IntegerType)
arduinoML_Action_value: Property = Property(name="value", type=StringType)
arduinoML_Action.attributes={arduinoML_Action_value, arduinoML_Action_analogvalue}

# arduinoML_Transition class attributes and methods

# arduinoML_SinkError class attributes and methods
arduinoML_SinkError_value: Property = Property(name="value", type=IntegerType)
arduinoML_SinkError.attributes={arduinoML_SinkError_value}

# arduinoML_BooleanCondition class attributes and methods
arduinoML_BooleanCondition_operator: Property = Property(name="operator", type=StringType)
arduinoML_BooleanCondition.attributes={arduinoML_BooleanCondition_operator}

# arduinoML_NamedElement class attributes and methods
arduinoML_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoML_NamedElement.attributes={arduinoML_NamedElement_name}

# arduinoML_Condition class attributes and methods
arduinoML_Condition_value: Property = Property(name="value", type=StringType)
arduinoML_Condition_analogvalue: Property = Property(name="analogvalue", type=IntegerType)
arduinoML_Condition_comparator: Property = Property(name="comparator", type=StringType)
arduinoML_Condition.attributes={arduinoML_Condition_analogvalue, arduinoML_Condition_value, arduinoML_Condition_comparator}

# Condition class attributes and methods

# Relationships
next13: BinaryAssociation = BinaryAssociation(
    name="next13",
    ends={
        Property(name="arduinoML_State14", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
state15: BinaryAssociation = BinaryAssociation(
    name="state15",
    ends={
        Property(name="State", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
basecondition16: BinaryAssociation = BinaryAssociation(
    name="basecondition16",
    ends={
        Property(name="arduinoML_BaseCondition", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition17", type=arduinoML_BaseCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bricks0: BinaryAssociation = BinaryAssociation(
    name="bricks0",
    ends={
        Property(name="arduinoML_Brick", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App", type=arduinoML_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="arduinoML_State", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App2", type=arduinoML_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="arduinoML_State5", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App4", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoML_Action", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_State7", type=arduinoML_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="Transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=arduinoML_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
errors9: BinaryAssociation = BinaryAssociation(
    name="errors9",
    ends={
        Property(name="SinkError", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state10", type=arduinoML_SinkError, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuator11: BinaryAssociation = BinaryAssociation(
    name="actuator11",
    ends={
        Property(name="arduinoML_Actuator", type=arduinoML_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Action12", type=arduinoML_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
booleancondition18: BinaryAssociation = BinaryAssociation(
    name="booleancondition18",
    ends={
        Property(name="arduinoML_BooleanCondition", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition19", type=arduinoML_BooleanCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensor20: BinaryAssociation = BinaryAssociation(
    name="sensor20",
    ends={
        Property(name="arduinoML_Sensor", type=arduinoML_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Condition", type=arduinoML_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
basecondition21: BinaryAssociation = BinaryAssociation(
    name="basecondition21",
    ends={
        Property(name="arduinoML_BaseCondition22", type=arduinoML_SinkError, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_SinkError", type=arduinoML_BaseCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
booleancondition23: BinaryAssociation = BinaryAssociation(
    name="booleancondition23",
    ends={
        Property(name="arduinoML_BooleanCondition25", type=arduinoML_SinkError, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_SinkError24", type=arduinoML_BooleanCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state26: BinaryAssociation = BinaryAssociation(
    name="state26",
    ends={
        Property(name="State27", type=arduinoML_SinkError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduinoML_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Brick)
gen_arduinoML_Actuator_Brick = Generalization(general=Brick, specific=arduinoML_Actuator)
gen_arduinoML_Sensor_Brick = Generalization(general=Brick, specific=arduinoML_Sensor)
gen_arduinoML_App_NamedElement = Generalization(general=NamedElement, specific=arduinoML_App)
gen_arduinoML_State_NamedElement = Generalization(general=NamedElement, specific=arduinoML_State)
gen_arduinoML_BaseCondition_Condition = Generalization(general=Condition, specific=arduinoML_BaseCondition)
gen_arduinoML_BooleanCondition_Condition = Generalization(general=Condition, specific=arduinoML_BooleanCondition)

# Domain Model
domain_model = DomainModel(
    name="arduinoML",
    types={arduinoML_Brick, NamedElement, arduinoML_Actuator, Brick, arduinoML_Sensor, arduinoML_BaseCondition, arduinoML_App, arduinoML_State, arduinoML_Action, arduinoML_Transition, arduinoML_SinkError, arduinoML_BooleanCondition, arduinoML_NamedElement, arduinoML_Condition, Condition, Signal, Comparator, Type, Operator},
    associations={next13, state15, basecondition16, bricks0, states1, initial3, actions6, transitions8, errors9, actuator11, booleancondition18, sensor20, basecondition21, booleancondition23, state26},
    generalizations={gen_arduinoML_Brick_NamedElement, gen_arduinoML_Actuator_Brick, gen_arduinoML_Sensor_Brick, gen_arduinoML_App_NamedElement, gen_arduinoML_State_NamedElement, gen_arduinoML_BaseCondition_Condition, gen_arduinoML_BooleanCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
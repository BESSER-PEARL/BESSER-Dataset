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
SIGNAL: Enumeration = Enumeration(
    name="SIGNAL",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="LOW")
    }
)

OPERATOR: Enumeration = Enumeration(
    name="OPERATOR",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or")
    }
)

COMPARATOR: Enumeration = Enumeration(
    name="COMPARATOR",
    literals={
            EnumerationLiteral(name="SUPERIOR"),
			EnumerationLiteral(name="INFERIOR"),
			EnumerationLiteral(name="EQUAL")
    }
)

# Classes
arduinoml_NamedElement = Class(name="arduinoml::NamedElement", is_abstract=True)
arduinoml_App = Class(name="arduinoml::App")
NamedElement = Class(name="NamedElement")
arduinoml_State = Class(name="arduinoml::State")
arduinoml_Brick = Class(name="arduinoml::Brick")
arduinoml_Action = Class(name="arduinoml::Action", is_abstract=True)
arduinoml_Transition = Class(name="arduinoml::Transition")
arduinoml_Actuator = Class(name="arduinoml::Actuator", is_abstract=True)
arduinoml_MultipleElementCondition = Class(name="arduinoml::MultipleElementCondition")
arduinoml_Sensor = Class(name="arduinoml::Sensor", is_abstract=True)
Brick = Class(name="Brick")
arduinoml_Condition = Class(name="arduinoml::Condition", is_abstract=True)
arduinoml_SingleElementCondition = Class(name="arduinoml::SingleElementCondition")
Condition = Class(name="Condition")
arduinoml_BinarySensor = Class(name="arduinoml::BinarySensor")
arduinoml_ValueElementCondition = Class(name="arduinoml::ValueElementCondition")
arduinoml_AnalogSensor = Class(name="arduinoml::AnalogSensor")
Sensor = Class(name="Sensor")
arduinoml_AnalogActuator = Class(name="arduinoml::AnalogActuator")
Actuator = Class(name="Actuator")
arduinoml_BinaryActuator = Class(name="arduinoml::BinaryActuator")
arduinoml_AnalogAction = Class(name="arduinoml::AnalogAction")
Action = Class(name="Action")
arduinoml_BinaryAction = Class(name="arduinoml::BinaryAction")

# arduinoml_NamedElement class attributes and methods
arduinoml_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoml_NamedElement.attributes={arduinoml_NamedElement_name}

# arduinoml_App class attributes and methods

# NamedElement class attributes and methods

# arduinoml_State class attributes and methods

# arduinoml_Brick class attributes and methods
arduinoml_Brick_pin: Property = Property(name="pin", type=StringType)
arduinoml_Brick.attributes={arduinoml_Brick_pin}

# arduinoml_Action class attributes and methods

# arduinoml_Transition class attributes and methods

# arduinoml_Actuator class attributes and methods

# arduinoml_MultipleElementCondition class attributes and methods
arduinoml_MultipleElementCondition_operators: Property = Property(name="operators", type=StringType)
arduinoml_MultipleElementCondition.attributes={arduinoml_MultipleElementCondition_operators}

# arduinoml_Sensor class attributes and methods

# Brick class attributes and methods

# arduinoml_Condition class attributes and methods

# arduinoml_SingleElementCondition class attributes and methods
arduinoml_SingleElementCondition_value: Property = Property(name="value", type=StringType)
arduinoml_SingleElementCondition.attributes={arduinoml_SingleElementCondition_value}

# Condition class attributes and methods

# arduinoml_BinarySensor class attributes and methods

# arduinoml_ValueElementCondition class attributes and methods
arduinoml_ValueElementCondition_value: Property = Property(name="value", type=FloatType)
arduinoml_ValueElementCondition_comparator: Property = Property(name="comparator", type=StringType)
arduinoml_ValueElementCondition.attributes={arduinoml_ValueElementCondition_comparator, arduinoml_ValueElementCondition_value}

# arduinoml_AnalogSensor class attributes and methods

# Sensor class attributes and methods

# arduinoml_AnalogActuator class attributes and methods

# Actuator class attributes and methods

# arduinoml_BinaryActuator class attributes and methods

# arduinoml_AnalogAction class attributes and methods
arduinoml_AnalogAction_actionValue: Property = Property(name="actionValue", type=IntegerType)
arduinoml_AnalogAction.attributes={arduinoml_AnalogAction_actionValue}

# Action class attributes and methods

# arduinoml_BinaryAction class attributes and methods
arduinoml_BinaryAction_actionValue: Property = Property(name="actionValue", type=StringType)
arduinoml_BinaryAction.attributes={arduinoml_BinaryAction_actionValue}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="arduinoml_State", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App", type=arduinoml_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bricks1: BinaryAssociation = BinaryAssociation(
    name="bricks1",
    ends={
        Property(name="arduinoml_Brick", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App2", type=arduinoml_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="arduinoml_State5", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App4", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoml_Action", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State7", type=arduinoml_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="arduinoml_Transition", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State9", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actuator10: BinaryAssociation = BinaryAssociation(
    name="actuator10",
    ends={
        Property(name="arduinoml_Actuator", type=arduinoml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Action11", type=arduinoml_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
next12: BinaryAssociation = BinaryAssociation(
    name="next12",
    ends={
        Property(name="arduinoml_State14", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition13", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="arduinoml_MultipleElementCondition", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition16", type=arduinoml_MultipleElementCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sensor17: BinaryAssociation = BinaryAssociation(
    name="sensor17",
    ends={
        Property(name="arduinoml_BinarySensor", type=arduinoml_SingleElementCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_SingleElementCondition", type=arduinoml_BinarySensor, multiplicity=Multiplicity(1, 1))
    }
)
sensor20: BinaryAssociation = BinaryAssociation(
    name="sensor20",
    ends={
        Property(name="arduinoml_AnalogSensor", type=arduinoml_ValueElementCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_ValueElementCondition", type=arduinoml_AnalogSensor, multiplicity=Multiplicity(1, 1))
    }
)
conditions18: BinaryAssociation = BinaryAssociation(
    name="conditions18",
    ends={
        Property(name="arduinoml_Condition", type=arduinoml_MultipleElementCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_MultipleElementCondition19", type=arduinoml_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_arduinoml_App_NamedElement = Generalization(general=NamedElement, specific=arduinoml_App)
gen_arduinoml_State_NamedElement = Generalization(general=NamedElement, specific=arduinoml_State)
gen_arduinoml_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Brick)
gen_arduinoml_Sensor_Brick = Generalization(general=Brick, specific=arduinoml_Sensor)
gen_arduinoml_Actuator_Brick = Generalization(general=Brick, specific=arduinoml_Actuator)
gen_arduinoml_SingleElementCondition_Condition = Generalization(general=Condition, specific=arduinoml_SingleElementCondition)
gen_arduinoml_MultipleElementCondition_Condition = Generalization(general=Condition, specific=arduinoml_MultipleElementCondition)
gen_arduinoml_ValueElementCondition_Condition = Generalization(general=Condition, specific=arduinoml_ValueElementCondition)
gen_arduinoml_BinarySensor_Sensor = Generalization(general=Sensor, specific=arduinoml_BinarySensor)
gen_arduinoml_AnalogSensor_Sensor = Generalization(general=Sensor, specific=arduinoml_AnalogSensor)
gen_arduinoml_AnalogActuator_Actuator = Generalization(general=Actuator, specific=arduinoml_AnalogActuator)
gen_arduinoml_BinaryActuator_Actuator = Generalization(general=Actuator, specific=arduinoml_BinaryActuator)
gen_arduinoml_AnalogAction_Action = Generalization(general=Action, specific=arduinoml_AnalogAction)
gen_arduinoml_BinaryAction_Action = Generalization(general=Action, specific=arduinoml_BinaryAction)

# Domain Model
domain_model = DomainModel(
    name="arduinoml",
    types={arduinoml_NamedElement, arduinoml_App, NamedElement, arduinoml_State, arduinoml_Brick, arduinoml_Action, arduinoml_Transition, arduinoml_Actuator, arduinoml_MultipleElementCondition, arduinoml_Sensor, Brick, arduinoml_Condition, arduinoml_SingleElementCondition, Condition, arduinoml_BinarySensor, arduinoml_ValueElementCondition, arduinoml_AnalogSensor, Sensor, arduinoml_AnalogActuator, Actuator, arduinoml_BinaryActuator, arduinoml_AnalogAction, Action, arduinoml_BinaryAction, SIGNAL, OPERATOR, COMPARATOR},
    associations={states0, bricks1, initial3, actions6, transition8, actuator10, next12, condition15, sensor17, sensor20, conditions18},
    generalizations={gen_arduinoml_App_NamedElement, gen_arduinoml_State_NamedElement, gen_arduinoml_Brick_NamedElement, gen_arduinoml_Sensor_Brick, gen_arduinoml_Actuator_Brick, gen_arduinoml_SingleElementCondition_Condition, gen_arduinoml_MultipleElementCondition_Condition, gen_arduinoml_ValueElementCondition_Condition, gen_arduinoml_BinarySensor_Sensor, gen_arduinoml_AnalogSensor_Sensor, gen_arduinoml_AnalogActuator_Actuator, gen_arduinoml_BinaryActuator_Actuator, gen_arduinoml_AnalogAction_Action, gen_arduinoml_BinaryAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
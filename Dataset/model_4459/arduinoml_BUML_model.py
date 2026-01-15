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
OPERATOR: Enumeration = Enumeration(
    name="OPERATOR",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

COMPARATOR: Enumeration = Enumeration(
    name="COMPARATOR",
    literals={
            EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NON_EQUALS"),
			EnumerationLiteral(name="SUPERIOR"),
			EnumerationLiteral(name="INFERIOR"),
			EnumerationLiteral(name="SUPERIOR_OR_EQUALS"),
			EnumerationLiteral(name="INFERIOR_OR_EQUALS")
    }
)

BrickType: Enumeration = Enumeration(
    name="BrickType",
    literals={
            EnumerationLiteral(name="DIGITAL"),
			EnumerationLiteral(name="ANALOGICAL")
    }
)

# Classes
arduinoml_State = Class(name="arduinoml::State")
arduinoml_Condition = Class(name="arduinoml::Condition", is_abstract=True)
arduinoml_Transition = Class(name="arduinoml::Transition")
arduinoml_Sensor = Class(name="arduinoml::Sensor")
Brick = Class(name="Brick")
arduinoml_Actuator = Class(name="arduinoml::Actuator")
arduinoml_NamedElement = Class(name="arduinoml::NamedElement", is_abstract=True)
arduinoml_App = Class(name="arduinoml::App")
NamedElement = Class(name="NamedElement")
arduinoml_Brick = Class(name="arduinoml::Brick", is_abstract=True)
arduinoml_SimpleCondition = Class(name="arduinoml::SimpleCondition")
Condition = Class(name="Condition")
arduinoml_Action = Class(name="arduinoml::Action")
arduinoml_MultipleCondition = Class(name="arduinoml::MultipleCondition")

# arduinoml_State class attributes and methods

# arduinoml_Condition class attributes and methods

# arduinoml_Transition class attributes and methods

# arduinoml_Sensor class attributes and methods

# Brick class attributes and methods

# arduinoml_Actuator class attributes and methods

# arduinoml_NamedElement class attributes and methods
arduinoml_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoml_NamedElement.attributes={arduinoml_NamedElement_name}

# arduinoml_App class attributes and methods

# NamedElement class attributes and methods

# arduinoml_Brick class attributes and methods
arduinoml_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoml_Brick_type: Property = Property(name="type", type=StringType)
arduinoml_Brick.attributes={arduinoml_Brick_pin, arduinoml_Brick_type}

# arduinoml_SimpleCondition class attributes and methods
arduinoml_SimpleCondition_value: Property = Property(name="value", type=StringType)
arduinoml_SimpleCondition_comparator: Property = Property(name="comparator", type=StringType)
arduinoml_SimpleCondition.attributes={arduinoml_SimpleCondition_value, arduinoml_SimpleCondition_comparator}

# Condition class attributes and methods

# arduinoml_Action class attributes and methods
arduinoml_Action_value: Property = Property(name="value", type=StringType)
arduinoml_Action.attributes={arduinoml_Action_value}

# arduinoml_MultipleCondition class attributes and methods
arduinoml_MultipleCondition_operators: Property = Property(name="operators", type=StringType)
arduinoml_MultipleCondition.attributes={arduinoml_MultipleCondition_operators}

# Relationships
bricks0: BinaryAssociation = BinaryAssociation(
    name="bricks0",
    ends={
        Property(name="arduinoml_Brick", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App", type=arduinoml_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="arduinoml_State", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App2", type=arduinoml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions3: BinaryAssociation = BinaryAssociation(
    name="conditions3",
    ends={
        Property(name="arduinoml_Condition", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App4", type=arduinoml_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="arduinoml_Transition", type=arduinoml_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_App6", type=arduinoml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuator21: BinaryAssociation = BinaryAssociation(
    name="actuator21",
    ends={
        Property(name="arduinoml_Actuator", type=arduinoml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Action22", type=arduinoml_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
sensor23: BinaryAssociation = BinaryAssociation(
    name="sensor23",
    ends={
        Property(name="arduinoml_Sensor", type=arduinoml_SimpleCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_SimpleCondition", type=arduinoml_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
next7: BinaryAssociation = BinaryAssociation(
    name="next7",
    ends={
        Property(name="arduinoml_State9", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition8", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="arduinoml_Condition12", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition11", type=arduinoml_Condition, multiplicity=Multiplicity(1, 1))
    }
)
previous13: BinaryAssociation = BinaryAssociation(
    name="previous13",
    ends={
        Property(name="arduinoml_State15", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition14", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
actions16: BinaryAssociation = BinaryAssociation(
    name="actions16",
    ends={
        Property(name="arduinoml_Action", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State17", type=arduinoml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions18: BinaryAssociation = BinaryAssociation(
    name="transitions18",
    ends={
        Property(name="arduinoml_Transition20", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State19", type=arduinoml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
conditions24: BinaryAssociation = BinaryAssociation(
    name="conditions24",
    ends={
        Property(name="arduinoml_SimpleCondition25", type=arduinoml_MultipleCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_MultipleCondition", type=arduinoml_SimpleCondition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_arduinoml_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Brick)
gen_arduinoml_Sensor_Brick = Generalization(general=Brick, specific=arduinoml_Sensor)
gen_arduinoml_Actuator_Brick = Generalization(general=Brick, specific=arduinoml_Actuator)
gen_arduinoml_App_NamedElement = Generalization(general=NamedElement, specific=arduinoml_App)
gen_arduinoml_Action_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Action)
gen_arduinoml_SimpleCondition_Condition = Generalization(general=Condition, specific=arduinoml_SimpleCondition)
gen_arduinoml_State_NamedElement = Generalization(general=NamedElement, specific=arduinoml_State)
gen_arduinoml_Condition_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Condition)
gen_arduinoml_MultipleCondition_Condition = Generalization(general=Condition, specific=arduinoml_MultipleCondition)

# Domain Model
domain_model = DomainModel(
    name="arduinoml",
    types={arduinoml_State, arduinoml_Condition, arduinoml_Transition, arduinoml_Sensor, Brick, arduinoml_Actuator, arduinoml_NamedElement, arduinoml_App, NamedElement, arduinoml_Brick, arduinoml_SimpleCondition, Condition, arduinoml_Action, arduinoml_MultipleCondition, OPERATOR, COMPARATOR, BrickType},
    associations={bricks0, states1, conditions3, transitions5, actuator21, sensor23, next7, condition10, previous13, actions16, transitions18, conditions24},
    generalizations={gen_arduinoml_Brick_NamedElement, gen_arduinoml_Sensor_Brick, gen_arduinoml_Actuator_Brick, gen_arduinoml_App_NamedElement, gen_arduinoml_Action_NamedElement, gen_arduinoml_SimpleCondition_Condition, gen_arduinoml_State_NamedElement, gen_arduinoml_Condition_NamedElement, gen_arduinoml_MultipleCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
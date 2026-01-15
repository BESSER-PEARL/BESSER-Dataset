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
DigitalState: Enumeration = Enumeration(
    name="DigitalState",
    literals={
            EnumerationLiteral(name="OFF"),
			EnumerationLiteral(name="ON")
    }
)

TimeComparison: Enumeration = Enumeration(
    name="TimeComparison",
    literals={
            EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="BEFORE")
    }
)

AnalogComparison: Enumeration = Enumeration(
    name="AnalogComparison",
    literals={
            EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="GREATEREQ"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="LOWEREQ"),
			EnumerationLiteral(name="LOWER")
    }
)

# Classes
arduinoml_AMLState = Class(name="arduinoml::AMLState")
NamedElement = Class(name="NamedElement")
arduinoml_Transition = Class(name="arduinoml::Transition")
arduinoml_Action = Class(name="arduinoml::Action", is_abstract=True)
arduinoml_DigitalSensor = Class(name="arduinoml::DigitalSensor")
Brick = Class(name="Brick")
arduinoml_DigitalActuator = Class(name="arduinoml::DigitalActuator")
arduinoml_AnalogSensor = Class(name="arduinoml::AnalogSensor")
arduinoml_AMLMachine = Class(name="arduinoml::AMLMachine")
arduinoml_Brick = Class(name="arduinoml::Brick", is_abstract=True)
arduinoml_NamedElement = Class(name="arduinoml::NamedElement", is_abstract=True)
arduinoml_TimeCondition = Class(name="arduinoml::TimeCondition")
arduinoml_AnalogCondition = Class(name="arduinoml::AnalogCondition")
arduinoml_AnalogAction = Class(name="arduinoml::AnalogAction", is_abstract=True)
arduinoml_AnalogActuator = Class(name="arduinoml::AnalogActuator")
arduinoml_Condition = Class(name="arduinoml::Condition", is_abstract=True)
arduinoml_DigitalCondition = Class(name="arduinoml::DigitalCondition")
Condition = Class(name="Condition")
arduinoml_DigitalAction = Class(name="arduinoml::DigitalAction")
Action = Class(name="Action")
arduinoml_AnalogActionValue = Class(name="arduinoml::AnalogActionValue")
AnalogAction = Class(name="AnalogAction")
arduinoml_AnalogActionSensor = Class(name="arduinoml::AnalogActionSensor")

# arduinoml_AMLState class attributes and methods

# NamedElement class attributes and methods

# arduinoml_Transition class attributes and methods

# arduinoml_Action class attributes and methods

# arduinoml_DigitalSensor class attributes and methods

# Brick class attributes and methods

# arduinoml_DigitalActuator class attributes and methods

# arduinoml_AnalogSensor class attributes and methods

# arduinoml_AMLMachine class attributes and methods
arduinoml_AMLMachine_frequency: Property = Property(name="frequency", type=IntegerType)
arduinoml_AMLMachine.attributes={arduinoml_AMLMachine_frequency}

# arduinoml_Brick class attributes and methods
arduinoml_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoml_Brick.attributes={arduinoml_Brick_pin}

# arduinoml_NamedElement class attributes and methods
arduinoml_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoml_NamedElement.attributes={arduinoml_NamedElement_name}

# arduinoml_TimeCondition class attributes and methods
arduinoml_TimeCondition_time: Property = Property(name="time", type=IntegerType)
arduinoml_TimeCondition_tComp: Property = Property(name="tComp", type=StringType)
arduinoml_TimeCondition.attributes={arduinoml_TimeCondition_time, arduinoml_TimeCondition_tComp}

# arduinoml_AnalogCondition class attributes and methods
arduinoml_AnalogCondition_aComp: Property = Property(name="aComp", type=StringType)
arduinoml_AnalogCondition_value: Property = Property(name="value", type=IntegerType)
arduinoml_AnalogCondition.attributes={arduinoml_AnalogCondition_aComp, arduinoml_AnalogCondition_value}

# arduinoml_AnalogAction class attributes and methods

# arduinoml_AnalogActuator class attributes and methods

# arduinoml_Condition class attributes and methods

# arduinoml_DigitalCondition class attributes and methods
arduinoml_DigitalCondition_dState: Property = Property(name="dState", type=StringType)
arduinoml_DigitalCondition.attributes={arduinoml_DigitalCondition_dState}

# Condition class attributes and methods

# arduinoml_DigitalAction class attributes and methods
arduinoml_DigitalAction_dState: Property = Property(name="dState", type=StringType)
arduinoml_DigitalAction.attributes={arduinoml_DigitalAction_dState}

# Action class attributes and methods

# arduinoml_AnalogActionValue class attributes and methods
arduinoml_AnalogActionValue_value: Property = Property(name="value", type=IntegerType)
arduinoml_AnalogActionValue.attributes={arduinoml_AnalogActionValue_value}

# AnalogAction class attributes and methods

# arduinoml_AnalogActionSensor class attributes and methods

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="arduinoml_AMLState", type=arduinoml_AMLMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AMLMachine2", type=arduinoml_AMLState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
start3: BinaryAssociation = BinaryAssociation(
    name="start3",
    ends={
        Property(name="arduinoml_AMLState5", type=arduinoml_AMLMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AMLMachine4", type=arduinoml_AMLState, multiplicity=Multiplicity(1, 1))
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="arduinoml_Transition", type=arduinoml_AMLState, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AMLState7", type=arduinoml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions8: BinaryAssociation = BinaryAssociation(
    name="actions8",
    ends={
        Property(name="arduinoml_Action", type=arduinoml_AMLState, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AMLState9", type=arduinoml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bricks0: BinaryAssociation = BinaryAssociation(
    name="bricks0",
    ends={
        Property(name="arduinoml_Brick", type=arduinoml_AMLMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AMLMachine", type=arduinoml_Brick, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuator16: BinaryAssociation = BinaryAssociation(
    name="actuator16",
    ends={
        Property(name="arduinoml_DigitalActuator", type=arduinoml_DigitalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_DigitalAction", type=arduinoml_DigitalActuator, multiplicity=Multiplicity(1, 1))
    }
)
sensor17: BinaryAssociation = BinaryAssociation(
    name="sensor17",
    ends={
        Property(name="arduinoml_AnalogSensor", type=arduinoml_AnalogCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AnalogCondition", type=arduinoml_AnalogSensor, multiplicity=Multiplicity(1, 1))
    }
)
goto10: BinaryAssociation = BinaryAssociation(
    name="goto10",
    ends={
        Property(name="arduinoml_AMLState12", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition11", type=arduinoml_AMLState, multiplicity=Multiplicity(1, 1))
    }
)
conditions13: BinaryAssociation = BinaryAssociation(
    name="conditions13",
    ends={
        Property(name="arduinoml_Condition", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition14", type=arduinoml_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sensor15: BinaryAssociation = BinaryAssociation(
    name="sensor15",
    ends={
        Property(name="arduinoml_DigitalSensor", type=arduinoml_DigitalCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_DigitalCondition", type=arduinoml_DigitalSensor, multiplicity=Multiplicity(1, 1))
    }
)
actuator18: BinaryAssociation = BinaryAssociation(
    name="actuator18",
    ends={
        Property(name="arduinoml_AnalogActuator", type=arduinoml_AnalogAction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AnalogAction", type=arduinoml_AnalogActuator, multiplicity=Multiplicity(1, 1))
    }
)
sensor19: BinaryAssociation = BinaryAssociation(
    name="sensor19",
    ends={
        Property(name="arduinoml_AnalogSensor20", type=arduinoml_AnalogActionSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_AnalogActionSensor", type=arduinoml_AnalogSensor, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduinoml_AMLState_NamedElement = Generalization(general=NamedElement, specific=arduinoml_AMLState)
gen_arduinoml_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Brick)
gen_arduinoml_DigitalSensor_Brick = Generalization(general=Brick, specific=arduinoml_DigitalSensor)
gen_arduinoml_DigitalActuator_Brick = Generalization(general=Brick, specific=arduinoml_DigitalActuator)
gen_arduinoml_AnalogSensor_Brick = Generalization(general=Brick, specific=arduinoml_AnalogSensor)
gen_arduinoml_TimeCondition_Condition = Generalization(general=Condition, specific=arduinoml_TimeCondition)
gen_arduinoml_AnalogCondition_Condition = Generalization(general=Condition, specific=arduinoml_AnalogCondition)
gen_arduinoml_AnalogAction_Action = Generalization(general=Action, specific=arduinoml_AnalogAction)
gen_arduinoml_AnalogActuator_Brick = Generalization(general=Brick, specific=arduinoml_AnalogActuator)
gen_arduinoml_DigitalCondition_Condition = Generalization(general=Condition, specific=arduinoml_DigitalCondition)
gen_arduinoml_DigitalAction_Action = Generalization(general=Action, specific=arduinoml_DigitalAction)
gen_arduinoml_AnalogActionValue_AnalogAction = Generalization(general=AnalogAction, specific=arduinoml_AnalogActionValue)
gen_arduinoml_AnalogActionSensor_AnalogAction = Generalization(general=AnalogAction, specific=arduinoml_AnalogActionSensor)

# Domain Model
domain_model = DomainModel(
    name="arduinoml",
    types={arduinoml_AMLState, NamedElement, arduinoml_Transition, arduinoml_Action, arduinoml_DigitalSensor, Brick, arduinoml_DigitalActuator, arduinoml_AnalogSensor, arduinoml_AMLMachine, arduinoml_Brick, arduinoml_NamedElement, arduinoml_TimeCondition, arduinoml_AnalogCondition, arduinoml_AnalogAction, arduinoml_AnalogActuator, arduinoml_Condition, arduinoml_DigitalCondition, Condition, arduinoml_DigitalAction, Action, arduinoml_AnalogActionValue, AnalogAction, arduinoml_AnalogActionSensor, DigitalState, TimeComparison, AnalogComparison},
    associations={states1, start3, transitions6, actions8, bricks0, actuator16, sensor17, goto10, conditions13, sensor15, actuator18, sensor19},
    generalizations={gen_arduinoml_AMLState_NamedElement, gen_arduinoml_Brick_NamedElement, gen_arduinoml_DigitalSensor_Brick, gen_arduinoml_DigitalActuator_Brick, gen_arduinoml_AnalogSensor_Brick, gen_arduinoml_TimeCondition_Condition, gen_arduinoml_AnalogCondition_Condition, gen_arduinoml_AnalogAction_Action, gen_arduinoml_AnalogActuator_Brick, gen_arduinoml_DigitalCondition_Condition, gen_arduinoml_DigitalAction_Action, gen_arduinoml_AnalogActionValue_AnalogAction, gen_arduinoml_AnalogActionSensor_AnalogAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
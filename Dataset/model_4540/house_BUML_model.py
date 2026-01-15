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
Element = Class(name="Element")
House2_Room = Class(name="House2::Room")
House2_ControlRule = Class(name="House2::ControlRule")
House2_Container = Class(name="House2::Container", is_abstract=True)
NamedElement = Class(name="NamedElement")
House2_Element = Class(name="House2::Element", is_abstract=True)
House2_Sensor = Class(name="House2::Sensor", is_abstract=True)
House2_Actor = Class(name="House2::Actor", is_abstract=True)
House2_TemperatureSensor = Class(name="House2::TemperatureSensor")
Sensor = Class(name="Sensor")
House2_TwilightSwitch = Class(name="House2::TwilightSwitch")
House2_Boiler = Class(name="House2::Boiler")
Actor = Class(name="Actor")
House2_RollerBlind = Class(name="House2::RollerBlind")
House2_Condition = Class(name="House2::Condition", is_abstract=True)
House2_Action = Class(name="House2::Action", is_abstract=True)
House2_House = Class(name="House2::House")
Container = Class(name="Container")
House2_Lamp = Class(name="House2::Lamp")
House2_EqualCondition = Class(name="House2::EqualCondition")
House2_RainSensor = Class(name="House2::RainSensor")
House2_BooleanAction = Class(name="House2::BooleanAction")
Action = Class(name="Action")
House2_ValueAction = Class(name="House2::ValueAction")
House2_NamedElement = Class(name="House2::NamedElement", is_abstract=True)
House2_LessThanCondition = Class(name="House2::LessThanCondition")
Condition = Class(name="Condition")
House2_GreaterThanCondition = Class(name="House2::GreaterThanCondition")

# Element class attributes and methods

# House2_Room class attributes and methods

# House2_ControlRule class attributes and methods

# House2_Container class attributes and methods

# NamedElement class attributes and methods

# House2_Element class attributes and methods

# House2_Sensor class attributes and methods

# House2_Actor class attributes and methods

# House2_TemperatureSensor class attributes and methods
House2_TemperatureSensor_temp: Property = Property(name="temp", type=FloatType)
House2_TemperatureSensor.attributes={House2_TemperatureSensor_temp}

# Sensor class attributes and methods

# House2_TwilightSwitch class attributes and methods
House2_TwilightSwitch_active: Property = Property(name="active", type=BooleanType)
House2_TwilightSwitch.attributes={House2_TwilightSwitch_active}

# House2_Boiler class attributes and methods
House2_Boiler_isOn: Property = Property(name="isOn", type=BooleanType)
House2_Boiler.attributes={House2_Boiler_isOn}

# Actor class attributes and methods

# House2_RollerBlind class attributes and methods
House2_RollerBlind_isUp: Property = Property(name="isUp", type=BooleanType)
House2_RollerBlind.attributes={House2_RollerBlind_isUp}

# House2_Condition class attributes and methods

# House2_Action class attributes and methods

# House2_House class attributes and methods

# Container class attributes and methods

# House2_Lamp class attributes and methods
House2_Lamp_isOn: Property = Property(name="isOn", type=BooleanType)
House2_Lamp.attributes={House2_Lamp_isOn}

# House2_EqualCondition class attributes and methods
House2_EqualCondition_boolcond: Property = Property(name="boolcond", type=BooleanType)
House2_EqualCondition_valuecond: Property = Property(name="valuecond", type=FloatType)
House2_EqualCondition.attributes={House2_EqualCondition_boolcond, House2_EqualCondition_valuecond}

# House2_RainSensor class attributes and methods
House2_RainSensor_active: Property = Property(name="active", type=BooleanType)
House2_RainSensor.attributes={House2_RainSensor_active}

# House2_BooleanAction class attributes and methods
House2_BooleanAction_switchTo: Property = Property(name="switchTo", type=BooleanType)
House2_BooleanAction.attributes={House2_BooleanAction_switchTo}

# Action class attributes and methods

# House2_ValueAction class attributes and methods
House2_ValueAction_switchToValue: Property = Property(name="switchToValue", type=FloatType)
House2_ValueAction.attributes={House2_ValueAction_switchToValue}

# House2_NamedElement class attributes and methods
House2_NamedElement_name: Property = Property(name="name", type=StringType)
House2_NamedElement.attributes={House2_NamedElement_name}

# House2_LessThanCondition class attributes and methods
House2_LessThanCondition_threshold: Property = Property(name="threshold", type=FloatType)
House2_LessThanCondition.attributes={House2_LessThanCondition_threshold}

# Condition class attributes and methods

# House2_GreaterThanCondition class attributes and methods
House2_GreaterThanCondition_threshold: Property = Property(name="threshold", type=FloatType)
House2_GreaterThanCondition.attributes={House2_GreaterThanCondition_threshold}

# Relationships
rooms0: BinaryAssociation = BinaryAssociation(
    name="rooms0",
    ends={
        Property(name="House2_Room", type=House2_House, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_House", type=House2_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlRules1: BinaryAssociation = BinaryAssociation(
    name="controlRules1",
    ends={
        Property(name="House2_ControlRule", type=House2_House, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_House2", type=House2_ControlRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="House2_Element", type=House2_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_Container", type=House2_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isLocatedIn4: BinaryAssociation = BinaryAssociation(
    name="isLocatedIn4",
    ends={
        Property(name="House2_Container5", type=House2_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_Sensor", type=House2_Container, multiplicity=Multiplicity(0, 1))
    }
)
isLocatedIn6: BinaryAssociation = BinaryAssociation(
    name="isLocatedIn6",
    ends={
        Property(name="House2_Container7", type=House2_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_Actor", type=House2_Container, multiplicity=Multiplicity(0, 1))
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="House2_Condition", type=House2_ControlRule, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_ControlRule9", type=House2_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action10: BinaryAssociation = BinaryAssociation(
    name="action10",
    ends={
        Property(name="House2_Action", type=House2_ControlRule, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_ControlRule11", type=House2_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actor15: BinaryAssociation = BinaryAssociation(
    name="actor15",
    ends={
        Property(name="House2_Actor17", type=House2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_Action16", type=House2_Actor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensor12: BinaryAssociation = BinaryAssociation(
    name="sensor12",
    ends={
        Property(name="House2_Sensor14", type=House2_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="House2_Condition13", type=House2_Sensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_House2_House_Container = Generalization(general=Container, specific=House2_House)
gen_House2_House_Element = Generalization(general=Element, specific=House2_House)
gen_House2_Room_Container = Generalization(general=Container, specific=House2_Room)
gen_House2_Container_NamedElement = Generalization(general=NamedElement, specific=House2_Container)
gen_House2_Element_NamedElement = Generalization(general=NamedElement, specific=House2_Element)
gen_House2_Sensor_NamedElement = Generalization(general=NamedElement, specific=House2_Sensor)
gen_House2_Actor_NamedElement = Generalization(general=NamedElement, specific=House2_Actor)
gen_House2_TemperatureSensor_Sensor = Generalization(general=Sensor, specific=House2_TemperatureSensor)
gen_House2_TwilightSwitch_Sensor = Generalization(general=Sensor, specific=House2_TwilightSwitch)
gen_House2_Boiler_Actor = Generalization(general=Actor, specific=House2_Boiler)
gen_House2_RollerBlind_Actor = Generalization(general=Actor, specific=House2_RollerBlind)
gen_House2_Lamp_Actor = Generalization(general=Actor, specific=House2_Lamp)
gen_House2_EqualCondition_Condition = Generalization(general=Condition, specific=House2_EqualCondition)
gen_House2_RainSensor_Sensor = Generalization(general=Sensor, specific=House2_RainSensor)
gen_House2_BooleanAction_Action = Generalization(general=Action, specific=House2_BooleanAction)
gen_House2_ValueAction_Action = Generalization(general=Action, specific=House2_ValueAction)
gen_House2_LessThanCondition_Condition = Generalization(general=Condition, specific=House2_LessThanCondition)
gen_House2_GreaterThanCondition_Condition = Generalization(general=Condition, specific=House2_GreaterThanCondition)

# Domain Model
domain_model = DomainModel(
    name="House2",
    types={Element, House2_Room, House2_ControlRule, House2_Container, NamedElement, House2_Element, House2_Sensor, House2_Actor, House2_TemperatureSensor, Sensor, House2_TwilightSwitch, House2_Boiler, Actor, House2_RollerBlind, House2_Condition, House2_Action, House2_House, Container, House2_Lamp, House2_EqualCondition, House2_RainSensor, House2_BooleanAction, Action, House2_ValueAction, House2_NamedElement, House2_LessThanCondition, Condition, House2_GreaterThanCondition},
    associations={rooms0, controlRules1, elements3, isLocatedIn4, isLocatedIn6, condition8, action10, actor15, sensor12},
    generalizations={gen_House2_House_Container, gen_House2_House_Element, gen_House2_Room_Container, gen_House2_Container_NamedElement, gen_House2_Element_NamedElement, gen_House2_Sensor_NamedElement, gen_House2_Actor_NamedElement, gen_House2_TemperatureSensor_Sensor, gen_House2_TwilightSwitch_Sensor, gen_House2_Boiler_Actor, gen_House2_RollerBlind_Actor, gen_House2_Lamp_Actor, gen_House2_EqualCondition_Condition, gen_House2_RainSensor_Sensor, gen_House2_BooleanAction_Action, gen_House2_ValueAction_Action, gen_House2_LessThanCondition_Condition, gen_House2_GreaterThanCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
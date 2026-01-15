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
Comparator: Enumeration = Enumeration(
    name="Comparator",
    literals={
            EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LE")
    }
)

# Classes
majordomo_Majordomo = Class(name="majordomo::Majordomo")
majordomo_House = Class(name="majordomo::House")
majordomo_Room = Class(name="majordomo::Room")
majordomo_Program = Class(name="majordomo::Program")
Extendable = Class(name="Extendable")
majordomo_Extendable = Class(name="majordomo::Extendable", is_abstract=True)
majordomo_Sensor = Class(name="majordomo::Sensor", is_abstract=True)
majordomo_Actor = Class(name="majordomo::Actor", is_abstract=True)
majordomo_LightSensor = Class(name="majordomo::LightSensor")
HouseMountable = Class(name="HouseMountable")
RoomMountable = Class(name="RoomMountable")
FloatSensor = Class(name="FloatSensor")
majordomo_TemperatureSensor = Class(name="majordomo::TemperatureSensor")
majordomo_RainSensor = Class(name="majordomo::RainSensor")
BooleanSensor = Class(name="BooleanSensor")
majordomo_SwitchSensor = Class(name="majordomo::SwitchSensor")
majordomo_NumberSensor = Class(name="majordomo::NumberSensor")
majordomo_ClockSensor = Class(name="majordomo::ClockSensor")
majordomo_LampActor = Class(name="majordomo::LampActor")
FloatActor = Class(name="FloatActor")
majordomo_RollerActor = Class(name="majordomo::RollerActor")
BooleanActor = Class(name="BooleanActor")
majordomo_RoofWindowActor = Class(name="majordomo::RoofWindowActor")
majordomo_BoilerActor = Class(name="majordomo::BoilerActor")
majordomo_RadiatorActor = Class(name="majordomo::RadiatorActor")
majordomo_RoomMountable = Class(name="majordomo::RoomMountable", is_abstract=True)
majordomo_HouseMountable = Class(name="majordomo::HouseMountable", is_abstract=True)
majordomo_BooleanSensor = Class(name="majordomo::BooleanSensor", is_abstract=True)
Sensor = Class(name="Sensor")
Extension = Class(name="Extension")
majordomo_Rule = Class(name="majordomo::Rule")
majordomo_Statement = Class(name="majordomo::Statement", is_abstract=True)
majordomo_Action = Class(name="majordomo::Action", is_abstract=True)
majordomo_Extension = Class(name="majordomo::Extension", is_abstract=True)
majordomo_BooleanAction = Class(name="majordomo::BooleanAction")
majordomo_CoffeeActor = Class(name="majordomo::CoffeeActor")
majordomo_BinaryOperation = Class(name="majordomo::BinaryOperation", is_abstract=True)
Statement = Class(name="Statement")
majordomo_NotOperation = Class(name="majordomo::NotOperation")
majordomo_CompareOperation = Class(name="majordomo::CompareOperation")
majordomo_ValueExpression = Class(name="majordomo::ValueExpression", is_abstract=True)
majordomo_FloatSensor = Class(name="majordomo::FloatSensor", is_abstract=True)
majordomo_BooleanActor = Class(name="majordomo::BooleanActor", is_abstract=True)
Actor = Class(name="Actor")
majordomo_FloatActor = Class(name="majordomo::FloatActor", is_abstract=True)
majordomo_FloatAction = Class(name="majordomo::FloatAction")
Action = Class(name="Action")
majordomo_PreparedActionSet = Class(name="majordomo::PreparedActionSet")
majordomo_ActionSetReference = Class(name="majordomo::ActionSetReference")
majordomo_BinaryAndOperation = Class(name="majordomo::BinaryAndOperation")
BinaryOperation = Class(name="BinaryOperation")
majordomo_BinaryOrOperation = Class(name="majordomo::BinaryOrOperation")
majordomo_BooleanSensorStatement = Class(name="majordomo::BooleanSensorStatement")
majordomo_ConstantValue = Class(name="majordomo::ConstantValue")
ValueExpression = Class(name="ValueExpression")
majordomo_SensorValue = Class(name="majordomo::SensorValue")
majordomo_StatementReference = Class(name="majordomo::StatementReference")
majordomo_PreparedStatement = Class(name="majordomo::PreparedStatement")
majordomo_PreparedValue = Class(name="majordomo::PreparedValue")
majordomo_ValueReference = Class(name="majordomo::ValueReference")

# majordomo_Majordomo class attributes and methods
majordomo_Majordomo_name: Property = Property(name="name", type=StringType)
majordomo_Majordomo.attributes={majordomo_Majordomo_name}

# majordomo_House class attributes and methods

# majordomo_Room class attributes and methods
majordomo_Room_name: Property = Property(name="name", type=StringType)
majordomo_Room.attributes={majordomo_Room_name}

# majordomo_Program class attributes and methods

# Extendable class attributes and methods

# majordomo_Extendable class attributes and methods

# majordomo_Sensor class attributes and methods

# majordomo_Actor class attributes and methods

# majordomo_LightSensor class attributes and methods

# HouseMountable class attributes and methods

# RoomMountable class attributes and methods

# FloatSensor class attributes and methods

# majordomo_TemperatureSensor class attributes and methods

# majordomo_RainSensor class attributes and methods

# BooleanSensor class attributes and methods

# majordomo_SwitchSensor class attributes and methods

# majordomo_NumberSensor class attributes and methods

# majordomo_ClockSensor class attributes and methods

# majordomo_LampActor class attributes and methods

# FloatActor class attributes and methods

# majordomo_RollerActor class attributes and methods

# BooleanActor class attributes and methods

# majordomo_RoofWindowActor class attributes and methods

# majordomo_BoilerActor class attributes and methods

# majordomo_RadiatorActor class attributes and methods

# majordomo_RoomMountable class attributes and methods

# majordomo_HouseMountable class attributes and methods

# majordomo_BooleanSensor class attributes and methods
majordomo_BooleanSensor_m_getValue: Method = Method(name="getValue", parameters={}, type=BooleanType)
majordomo_BooleanSensor.methods={majordomo_BooleanSensor_m_getValue}

# Sensor class attributes and methods

# Extension class attributes and methods

# majordomo_Rule class attributes and methods

# majordomo_Statement class attributes and methods

# majordomo_Action class attributes and methods

# majordomo_Extension class attributes and methods
majordomo_Extension_name: Property = Property(name="name", type=StringType)
majordomo_Extension.attributes={majordomo_Extension_name}

# majordomo_BooleanAction class attributes and methods
majordomo_BooleanAction_value: Property = Property(name="value", type=BooleanType)
majordomo_BooleanAction.attributes={majordomo_BooleanAction_value}

# majordomo_CoffeeActor class attributes and methods

# majordomo_BinaryOperation class attributes and methods

# Statement class attributes and methods

# majordomo_NotOperation class attributes and methods

# majordomo_CompareOperation class attributes and methods
majordomo_CompareOperation_comparator: Property = Property(name="comparator", type=StringType)
majordomo_CompareOperation.attributes={majordomo_CompareOperation_comparator}

# majordomo_ValueExpression class attributes and methods

# majordomo_FloatSensor class attributes and methods
majordomo_FloatSensor_m_getValue: Method = Method(name="getValue", parameters={}, type=FloatType)
majordomo_FloatSensor.methods={majordomo_FloatSensor_m_getValue}

# majordomo_BooleanActor class attributes and methods
majordomo_BooleanActor_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='value')})
majordomo_BooleanActor.methods={majordomo_BooleanActor_m_setValue}

# Actor class attributes and methods

# majordomo_FloatActor class attributes and methods
majordomo_FloatActor_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='value')})
majordomo_FloatActor.methods={majordomo_FloatActor_m_setValue}

# majordomo_FloatAction class attributes and methods
majordomo_FloatAction_value: Property = Property(name="value", type=FloatType)
majordomo_FloatAction.attributes={majordomo_FloatAction_value}

# Action class attributes and methods

# majordomo_PreparedActionSet class attributes and methods
majordomo_PreparedActionSet_name: Property = Property(name="name", type=StringType)
majordomo_PreparedActionSet.attributes={majordomo_PreparedActionSet_name}

# majordomo_ActionSetReference class attributes and methods

# majordomo_BinaryAndOperation class attributes and methods

# BinaryOperation class attributes and methods

# majordomo_BinaryOrOperation class attributes and methods

# majordomo_BooleanSensorStatement class attributes and methods

# majordomo_ConstantValue class attributes and methods
majordomo_ConstantValue_value: Property = Property(name="value", type=FloatType)
majordomo_ConstantValue.attributes={majordomo_ConstantValue_value}

# ValueExpression class attributes and methods

# majordomo_SensorValue class attributes and methods

# majordomo_StatementReference class attributes and methods

# majordomo_PreparedStatement class attributes and methods
majordomo_PreparedStatement_name: Property = Property(name="name", type=StringType)
majordomo_PreparedStatement.attributes={majordomo_PreparedStatement_name}

# majordomo_PreparedValue class attributes and methods
majordomo_PreparedValue_name: Property = Property(name="name", type=StringType)
majordomo_PreparedValue.attributes={majordomo_PreparedValue_name}

# majordomo_ValueReference class attributes and methods

# Relationships
house0: BinaryAssociation = BinaryAssociation(
    name="house0",
    ends={
        Property(name="majordomo_House", type=majordomo_Majordomo, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Majordomo", type=majordomo_House, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rooms1: BinaryAssociation = BinaryAssociation(
    name="rooms1",
    ends={
        Property(name="majordomo_Room", type=majordomo_Majordomo, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Majordomo2", type=majordomo_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program3: BinaryAssociation = BinaryAssociation(
    name="program3",
    ends={
        Property(name="majordomo_Program", type=majordomo_Majordomo, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Majordomo4", type=majordomo_Program, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sensors5: BinaryAssociation = BinaryAssociation(
    name="sensors5",
    ends={
        Property(name="Sensor", type=majordomo_Extendable, multiplicity=Multiplicity(1, 1)),
        Property(name="ctx", type=majordomo_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors6: BinaryAssociation = BinaryAssociation(
    name="actors6",
    ends={
        Property(name="Actor", type=majordomo_Extendable, multiplicity=Multiplicity(1, 1)),
        Property(name="ctx7", type=majordomo_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctx8: BinaryAssociation = BinaryAssociation(
    name="ctx8",
    ends={
        Property(name="Extendable", type=majordomo_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="sensors", type=majordomo_Extendable, multiplicity=Multiplicity(1, 1))
    }
)
ctx9: BinaryAssociation = BinaryAssociation(
    name="ctx9",
    ends={
        Property(name="Extendable10", type=majordomo_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=majordomo_Extendable, multiplicity=Multiplicity(1, 1))
    }
)
statement11: BinaryAssociation = BinaryAssociation(
    name="statement11",
    ends={
        Property(name="majordomo_Statement", type=majordomo_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Rule", type=majordomo_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions12: BinaryAssociation = BinaryAssociation(
    name="actions12",
    ends={
        Property(name="majordomo_Action", type=majordomo_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Rule13", type=majordomo_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actor15: BinaryAssociation = BinaryAssociation(
    name="actor15",
    ends={
        Property(name="majordomo_BooleanActor", type=majordomo_BooleanAction, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_BooleanAction", type=majordomo_BooleanActor, multiplicity=Multiplicity(1, 1))
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="majordomo_Statement17", type=majordomo_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_BinaryOperation", type=majordomo_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="majordomo_Statement20", type=majordomo_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_BinaryOperation19", type=majordomo_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement21: BinaryAssociation = BinaryAssociation(
    name="statement21",
    ends={
        Property(name="majordomo_Statement22", type=majordomo_NotOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_NotOperation", type=majordomo_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="majordomo_ValueExpression", type=majordomo_CompareOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_CompareOperation", type=majordomo_ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right24: BinaryAssociation = BinaryAssociation(
    name="right24",
    ends={
        Property(name="majordomo_ValueExpression26", type=majordomo_CompareOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_CompareOperation25", type=majordomo_ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actor14: BinaryAssociation = BinaryAssociation(
    name="actor14",
    ends={
        Property(name="majordomo_FloatActor", type=majordomo_FloatAction, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_FloatAction", type=majordomo_FloatActor, multiplicity=Multiplicity(1, 1))
    }
)
preparedStatements32: BinaryAssociation = BinaryAssociation(
    name="preparedStatements32",
    ends={
        Property(name="PreparedStatement", type=majordomo_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ctx33", type=majordomo_PreparedStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preparedActionSets34: BinaryAssociation = BinaryAssociation(
    name="preparedActionSets34",
    ends={
        Property(name="PreparedActionSet", type=majordomo_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ctx35", type=majordomo_PreparedActionSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules36: BinaryAssociation = BinaryAssociation(
    name="rules36",
    ends={
        Property(name="majordomo_Rule38", type=majordomo_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_Program37", type=majordomo_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctx39: BinaryAssociation = BinaryAssociation(
    name="ctx39",
    ends={
        Property(name="Program", type=majordomo_PreparedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="preparedStatements", type=majordomo_Program, multiplicity=Multiplicity(1, 1))
    }
)
statement40: BinaryAssociation = BinaryAssociation(
    name="statement40",
    ends={
        Property(name="majordomo_Statement42", type=majordomo_PreparedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_PreparedStatement41", type=majordomo_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ctx43: BinaryAssociation = BinaryAssociation(
    name="ctx43",
    ends={
        Property(name="Program44", type=majordomo_PreparedActionSet, multiplicity=Multiplicity(1, 1)),
        Property(name="preparedActionSets", type=majordomo_Program, multiplicity=Multiplicity(1, 1))
    }
)
actions45: BinaryAssociation = BinaryAssociation(
    name="actions45",
    ends={
        Property(name="majordomo_Action46", type=majordomo_PreparedActionSet, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_PreparedActionSet", type=majordomo_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ref47: BinaryAssociation = BinaryAssociation(
    name="ref47",
    ends={
        Property(name="majordomo_PreparedActionSet48", type=majordomo_ActionSetReference, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_ActionSetReference", type=majordomo_PreparedActionSet, multiplicity=Multiplicity(1, 1))
    }
)
sensor27: BinaryAssociation = BinaryAssociation(
    name="sensor27",
    ends={
        Property(name="majordomo_BooleanSensor", type=majordomo_BooleanSensorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_BooleanSensorStatement", type=majordomo_BooleanSensor, multiplicity=Multiplicity(1, 1))
    }
)
sensor28: BinaryAssociation = BinaryAssociation(
    name="sensor28",
    ends={
        Property(name="majordomo_FloatSensor", type=majordomo_SensorValue, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_SensorValue", type=majordomo_FloatSensor, multiplicity=Multiplicity(1, 1))
    }
)
ref29: BinaryAssociation = BinaryAssociation(
    name="ref29",
    ends={
        Property(name="majordomo_PreparedStatement", type=majordomo_StatementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_StatementReference", type=majordomo_PreparedStatement, multiplicity=Multiplicity(1, 1))
    }
)
constants30: BinaryAssociation = BinaryAssociation(
    name="constants30",
    ends={
        Property(name="PreparedValue", type=majordomo_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ctx31", type=majordomo_PreparedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctx49: BinaryAssociation = BinaryAssociation(
    name="ctx49",
    ends={
        Property(name="Program50", type=majordomo_PreparedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=majordomo_Program, multiplicity=Multiplicity(1, 1))
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="majordomo_ValueExpression52", type=majordomo_PreparedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_PreparedValue", type=majordomo_ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref53: BinaryAssociation = BinaryAssociation(
    name="ref53",
    ends={
        Property(name="majordomo_PreparedValue54", type=majordomo_ValueReference, multiplicity=Multiplicity(1, 1)),
        Property(name="majordomo_ValueReference", type=majordomo_PreparedValue, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_majordomo_House_Extendable = Generalization(general=Extendable, specific=majordomo_House)
gen_majordomo_LightSensor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_LightSensor)
gen_majordomo_LightSensor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_LightSensor)
gen_majordomo_LightSensor_FloatSensor = Generalization(general=FloatSensor, specific=majordomo_LightSensor)
gen_majordomo_TemperatureSensor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_TemperatureSensor)
gen_majordomo_TemperatureSensor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_TemperatureSensor)
gen_majordomo_TemperatureSensor_FloatSensor = Generalization(general=FloatSensor, specific=majordomo_TemperatureSensor)
gen_majordomo_RainSensor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_RainSensor)
gen_majordomo_RainSensor_BooleanSensor = Generalization(general=BooleanSensor, specific=majordomo_RainSensor)
gen_majordomo_SwitchSensor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_SwitchSensor)
gen_majordomo_SwitchSensor_BooleanSensor = Generalization(general=BooleanSensor, specific=majordomo_SwitchSensor)
gen_majordomo_NumberSensor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_NumberSensor)
gen_majordomo_NumberSensor_FloatSensor = Generalization(general=FloatSensor, specific=majordomo_NumberSensor)
gen_majordomo_ClockSensor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_ClockSensor)
gen_majordomo_ClockSensor_FloatSensor = Generalization(general=FloatSensor, specific=majordomo_ClockSensor)
gen_majordomo_LampActor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_LampActor)
gen_majordomo_LampActor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_LampActor)
gen_majordomo_LampActor_FloatActor = Generalization(general=FloatActor, specific=majordomo_LampActor)
gen_majordomo_RollerActor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_RollerActor)
gen_majordomo_RollerActor_BooleanActor = Generalization(general=BooleanActor, specific=majordomo_RollerActor)
gen_majordomo_RoofWindowActor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_RoofWindowActor)
gen_majordomo_RoofWindowActor_BooleanActor = Generalization(general=BooleanActor, specific=majordomo_RoofWindowActor)
gen_majordomo_BoilerActor_HouseMountable = Generalization(general=HouseMountable, specific=majordomo_BoilerActor)
gen_majordomo_BoilerActor_BooleanActor = Generalization(general=BooleanActor, specific=majordomo_BoilerActor)
gen_majordomo_RadiatorActor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_RadiatorActor)
gen_majordomo_RadiatorActor_BooleanActor = Generalization(general=BooleanActor, specific=majordomo_RadiatorActor)
gen_majordomo_BooleanSensor_Sensor = Generalization(general=Sensor, specific=majordomo_BooleanSensor)
gen_majordomo_Room_Extendable = Generalization(general=Extendable, specific=majordomo_Room)
gen_majordomo_Sensor_Extension = Generalization(general=Extension, specific=majordomo_Sensor)
gen_majordomo_Actor_Extension = Generalization(general=Extension, specific=majordomo_Actor)
gen_majordomo_BooleanAction_Action = Generalization(general=Action, specific=majordomo_BooleanAction)
gen_majordomo_CoffeeActor_RoomMountable = Generalization(general=RoomMountable, specific=majordomo_CoffeeActor)
gen_majordomo_CoffeeActor_BooleanActor = Generalization(general=BooleanActor, specific=majordomo_CoffeeActor)
gen_majordomo_BinaryOperation_Statement = Generalization(general=Statement, specific=majordomo_BinaryOperation)
gen_majordomo_NotOperation_Statement = Generalization(general=Statement, specific=majordomo_NotOperation)
gen_majordomo_CompareOperation_Statement = Generalization(general=Statement, specific=majordomo_CompareOperation)
gen_majordomo_FloatSensor_Sensor = Generalization(general=Sensor, specific=majordomo_FloatSensor)
gen_majordomo_BooleanActor_Actor = Generalization(general=Actor, specific=majordomo_BooleanActor)
gen_majordomo_FloatActor_Actor = Generalization(general=Actor, specific=majordomo_FloatActor)
gen_majordomo_FloatAction_Action = Generalization(general=Action, specific=majordomo_FloatAction)
gen_majordomo_ActionSetReference_Action = Generalization(general=Action, specific=majordomo_ActionSetReference)
gen_majordomo_BinaryAndOperation_BinaryOperation = Generalization(general=BinaryOperation, specific=majordomo_BinaryAndOperation)
gen_majordomo_BinaryOrOperation_BinaryOperation = Generalization(general=BinaryOperation, specific=majordomo_BinaryOrOperation)
gen_majordomo_BooleanSensorStatement_Statement = Generalization(general=Statement, specific=majordomo_BooleanSensorStatement)
gen_majordomo_ConstantValue_ValueExpression = Generalization(general=ValueExpression, specific=majordomo_ConstantValue)
gen_majordomo_SensorValue_ValueExpression = Generalization(general=ValueExpression, specific=majordomo_SensorValue)
gen_majordomo_StatementReference_Statement = Generalization(general=Statement, specific=majordomo_StatementReference)
gen_majordomo_ValueReference_ValueExpression = Generalization(general=ValueExpression, specific=majordomo_ValueReference)

# Domain Model
domain_model = DomainModel(
    name="majordomo",
    types={majordomo_Majordomo, majordomo_House, majordomo_Room, majordomo_Program, Extendable, majordomo_Extendable, majordomo_Sensor, majordomo_Actor, majordomo_LightSensor, HouseMountable, RoomMountable, FloatSensor, majordomo_TemperatureSensor, majordomo_RainSensor, BooleanSensor, majordomo_SwitchSensor, majordomo_NumberSensor, majordomo_ClockSensor, majordomo_LampActor, FloatActor, majordomo_RollerActor, BooleanActor, majordomo_RoofWindowActor, majordomo_BoilerActor, majordomo_RadiatorActor, majordomo_RoomMountable, majordomo_HouseMountable, majordomo_BooleanSensor, Sensor, Extension, majordomo_Rule, majordomo_Statement, majordomo_Action, majordomo_Extension, majordomo_BooleanAction, majordomo_CoffeeActor, majordomo_BinaryOperation, Statement, majordomo_NotOperation, majordomo_CompareOperation, majordomo_ValueExpression, majordomo_FloatSensor, majordomo_BooleanActor, Actor, majordomo_FloatActor, majordomo_FloatAction, Action, majordomo_PreparedActionSet, majordomo_ActionSetReference, majordomo_BinaryAndOperation, BinaryOperation, majordomo_BinaryOrOperation, majordomo_BooleanSensorStatement, majordomo_ConstantValue, ValueExpression, majordomo_SensorValue, majordomo_StatementReference, majordomo_PreparedStatement, majordomo_PreparedValue, majordomo_ValueReference, Comparator},
    associations={house0, rooms1, program3, sensors5, actors6, ctx8, ctx9, statement11, actions12, actor15, left16, right18, statement21, left23, right24, actor14, preparedStatements32, preparedActionSets34, rules36, ctx39, statement40, ctx43, actions45, ref47, sensor27, sensor28, ref29, constants30, ctx49, value51, ref53},
    generalizations={gen_majordomo_House_Extendable, gen_majordomo_LightSensor_HouseMountable, gen_majordomo_LightSensor_RoomMountable, gen_majordomo_LightSensor_FloatSensor, gen_majordomo_TemperatureSensor_HouseMountable, gen_majordomo_TemperatureSensor_RoomMountable, gen_majordomo_TemperatureSensor_FloatSensor, gen_majordomo_RainSensor_HouseMountable, gen_majordomo_RainSensor_BooleanSensor, gen_majordomo_SwitchSensor_RoomMountable, gen_majordomo_SwitchSensor_BooleanSensor, gen_majordomo_NumberSensor_RoomMountable, gen_majordomo_NumberSensor_FloatSensor, gen_majordomo_ClockSensor_HouseMountable, gen_majordomo_ClockSensor_FloatSensor, gen_majordomo_LampActor_HouseMountable, gen_majordomo_LampActor_RoomMountable, gen_majordomo_LampActor_FloatActor, gen_majordomo_RollerActor_RoomMountable, gen_majordomo_RollerActor_BooleanActor, gen_majordomo_RoofWindowActor_RoomMountable, gen_majordomo_RoofWindowActor_BooleanActor, gen_majordomo_BoilerActor_HouseMountable, gen_majordomo_BoilerActor_BooleanActor, gen_majordomo_RadiatorActor_RoomMountable, gen_majordomo_RadiatorActor_BooleanActor, gen_majordomo_BooleanSensor_Sensor, gen_majordomo_Room_Extendable, gen_majordomo_Sensor_Extension, gen_majordomo_Actor_Extension, gen_majordomo_BooleanAction_Action, gen_majordomo_CoffeeActor_RoomMountable, gen_majordomo_CoffeeActor_BooleanActor, gen_majordomo_BinaryOperation_Statement, gen_majordomo_NotOperation_Statement, gen_majordomo_CompareOperation_Statement, gen_majordomo_FloatSensor_Sensor, gen_majordomo_BooleanActor_Actor, gen_majordomo_FloatActor_Actor, gen_majordomo_FloatAction_Action, gen_majordomo_ActionSetReference_Action, gen_majordomo_BinaryAndOperation_BinaryOperation, gen_majordomo_BinaryOrOperation_BinaryOperation, gen_majordomo_BooleanSensorStatement_Statement, gen_majordomo_ConstantValue_ValueExpression, gen_majordomo_SensorValue_ValueExpression, gen_majordomo_StatementReference_Statement, gen_majordomo_ValueReference_ValueExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
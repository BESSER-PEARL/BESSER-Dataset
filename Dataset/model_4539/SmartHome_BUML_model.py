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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="superior"),
			EnumerationLiteral(name="inferior"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="different")
    }
)

# Classes
SmartHome_Light = Class(name="SmartHome_Light")
SmartHome_PhysicalContext = Class(name="SmartHome_PhysicalContext")
SmartHome_Shutter = Class(name="SmartHome_Shutter")
SmartHome_Rule = Class(name="SmartHome_Rule")
SmartHome_Clock = Class(name="SmartHome_Clock")
SmartHome_Home = Class(name="SmartHome_Home")
SmartHome_Sensor = Class(name="SmartHome_Sensor", is_abstract=True)
IotComponent = Class(name="IotComponent")
SmartHome_Activator = Class(name="SmartHome_Activator", is_abstract=True)
SmartHome_NamedElement = Class(name="SmartHome_NamedElement", is_abstract=True)
Sensor = Class(name="Sensor")
Activator = Class(name="Activator")
SmartHome_Room = Class(name="SmartHome_Room")
NamedElement = Class(name="NamedElement")
SmartHome_LightSensor = Class(name="SmartHome_LightSensor")
SmartHome_RuleComposant = Class(name="SmartHome_RuleComposant")
SmartHome_Value = Class(name="SmartHome_Value", is_abstract=True)
SmartHome_DigitValue = Class(name="SmartHome_DigitValue")
Value = Class(name="Value")
SmartHome_AnalValue = Class(name="SmartHome_AnalValue")
SmartHome_IotComponent = Class(name="SmartHome_IotComponent", is_abstract=True)

# SmartHome_Light class attributes and methods
SmartHome_Light_stateInit: Property = Property(name="stateInit", type=BooleanType)
SmartHome_Light_intensity: Property = Property(name="intensity", type=FloatType)
SmartHome_Light.attributes={SmartHome_Light_stateInit, SmartHome_Light_intensity}

# SmartHome_PhysicalContext class attributes and methods
SmartHome_PhysicalContext_lightIn: Property = Property(name="lightIn", type=FloatType)
SmartHome_PhysicalContext_lightOut: Property = Property(name="lightOut", type=FloatType)
SmartHome_PhysicalContext.attributes={SmartHome_PhysicalContext_lightIn, SmartHome_PhysicalContext_lightOut}

# SmartHome_Shutter class attributes and methods
SmartHome_Shutter_stateInit: Property = Property(name="stateInit", type=BooleanType)
SmartHome_Shutter.attributes={SmartHome_Shutter_stateInit}

# SmartHome_Rule class attributes and methods

# SmartHome_Clock class attributes and methods

# SmartHome_Home class attributes and methods
SmartHome_Home_startDay: Property = Property(name="startDay", type=FloatType)
SmartHome_Home_speed: Property = Property(name="speed", type=FloatType)
SmartHome_Home.attributes={SmartHome_Home_speed, SmartHome_Home_startDay}

# SmartHome_Sensor class attributes and methods

# IotComponent class attributes and methods

# SmartHome_Activator class attributes and methods
SmartHome_Activator_m_activate: Method = Method(name="activate", parameters={}, type=StringType)
SmartHome_Activator.methods={SmartHome_Activator_m_activate}

# SmartHome_NamedElement class attributes and methods
SmartHome_NamedElement_name: Property = Property(name="name", type=StringType)
SmartHome_NamedElement.attributes={SmartHome_NamedElement_name}

# Sensor class attributes and methods

# Activator class attributes and methods

# SmartHome_Room class attributes and methods

# NamedElement class attributes and methods

# SmartHome_LightSensor class attributes and methods

# SmartHome_RuleComposant class attributes and methods
SmartHome_RuleComposant_operator: Property = Property(name="operator", type=StringType)
SmartHome_RuleComposant.attributes={SmartHome_RuleComposant_operator}

# SmartHome_Value class attributes and methods

# SmartHome_DigitValue class attributes and methods
SmartHome_DigitValue_value: Property = Property(name="value", type=FloatType)
SmartHome_DigitValue.attributes={SmartHome_DigitValue_value}

# Value class attributes and methods

# SmartHome_AnalValue class attributes and methods
SmartHome_AnalValue_value: Property = Property(name="value", type=BooleanType)
SmartHome_AnalValue.attributes={SmartHome_AnalValue_value}

# SmartHome_IotComponent class attributes and methods

# Relationships
light1: BinaryAssociation = BinaryAssociation(
    name="light1",
    ends={
        Property(name="SmartHome_Light", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room2", type=SmartHome_Light, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalcontext3: BinaryAssociation = BinaryAssociation(
    name="physicalcontext3",
    ends={
        Property(name="SmartHome_PhysicalContext", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room4", type=SmartHome_PhysicalContext, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shutters5: BinaryAssociation = BinaryAssociation(
    name="shutters5",
    ends={
        Property(name="SmartHome_Shutter", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room6", type=SmartHome_Shutter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules7: BinaryAssociation = BinaryAssociation(
    name="rules7",
    ends={
        Property(name="SmartHome_Rule", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room8", type=SmartHome_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock9: BinaryAssociation = BinaryAssociation(
    name="clock9",
    ends={
        Property(name="SmartHome_Clock", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room10", type=SmartHome_Clock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
room11: BinaryAssociation = BinaryAssociation(
    name="room11",
    ends={
        Property(name="SmartHome_Room12", type=SmartHome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Home", type=SmartHome_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules13: BinaryAssociation = BinaryAssociation(
    name="rules13",
    ends={
        Property(name="SmartHome_Rule15", type=SmartHome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Home14", type=SmartHome_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lightsensor0: BinaryAssociation = BinaryAssociation(
    name="lightsensor0",
    ends={
        Property(name="SmartHome_LightSensor", type=SmartHome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Room", type=SmartHome_LightSensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rulecondition16: BinaryAssociation = BinaryAssociation(
    name="rulecondition16",
    ends={
        Property(name="SmartHome_RuleComposant", type=SmartHome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Rule17", type=SmartHome_RuleComposant, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ruleconsequence18: BinaryAssociation = BinaryAssociation(
    name="ruleconsequence18",
    ends={
        Property(name="SmartHome_RuleComposant20", type=SmartHome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_Rule19", type=SmartHome_RuleComposant, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="SmartHome_Value", type=SmartHome_RuleComposant, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_RuleComposant22", type=SmartHome_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iotcomponent23: BinaryAssociation = BinaryAssociation(
    name="iotcomponent23",
    ends={
        Property(name="SmartHome_IotComponent", type=SmartHome_RuleComposant, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHome_RuleComposant24", type=SmartHome_IotComponent, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SmartHome_Home_NamedElement = Generalization(general=NamedElement, specific=SmartHome_Home)
gen_SmartHome_Sensor_IotComponent = Generalization(general=IotComponent, specific=SmartHome_Sensor)
gen_SmartHome_Activator_IotComponent = Generalization(general=IotComponent, specific=SmartHome_Activator)
gen_SmartHome_LightSensor_Sensor = Generalization(general=Sensor, specific=SmartHome_LightSensor)
gen_SmartHome_Light_Activator = Generalization(general=Activator, specific=SmartHome_Light)
gen_SmartHome_PhysicalContext_NamedElement = Generalization(general=NamedElement, specific=SmartHome_PhysicalContext)
gen_SmartHome_Room_NamedElement = Generalization(general=NamedElement, specific=SmartHome_Room)
gen_SmartHome_Rule_NamedElement = Generalization(general=NamedElement, specific=SmartHome_Rule)
gen_SmartHome_DigitValue_Value = Generalization(general=Value, specific=SmartHome_DigitValue)
gen_SmartHome_AnalValue_Value = Generalization(general=Value, specific=SmartHome_AnalValue)
gen_SmartHome_IotComponent_NamedElement = Generalization(general=NamedElement, specific=SmartHome_IotComponent)
gen_SmartHome_Clock_Sensor = Generalization(general=Sensor, specific=SmartHome_Clock)
gen_SmartHome_Shutter_Activator = Generalization(general=Activator, specific=SmartHome_Shutter)

# Domain Model
domain_model = DomainModel(
    name="SmartHome",
    types={SmartHome_Light, SmartHome_PhysicalContext, SmartHome_Shutter, SmartHome_Rule, SmartHome_Clock, SmartHome_Home, SmartHome_Sensor, IotComponent, SmartHome_Activator, SmartHome_NamedElement, Sensor, Activator, SmartHome_Room, NamedElement, SmartHome_LightSensor, SmartHome_RuleComposant, SmartHome_Value, SmartHome_DigitValue, Value, SmartHome_AnalValue, SmartHome_IotComponent, Operator},
    associations={light1, physicalcontext3, shutters5, rules7, clock9, room11, rules13, lightsensor0, rulecondition16, ruleconsequence18, value21, iotcomponent23},
    generalizations={gen_SmartHome_Home_NamedElement, gen_SmartHome_Sensor_IotComponent, gen_SmartHome_Activator_IotComponent, gen_SmartHome_LightSensor_Sensor, gen_SmartHome_Light_Activator, gen_SmartHome_PhysicalContext_NamedElement, gen_SmartHome_Room_NamedElement, gen_SmartHome_Rule_NamedElement, gen_SmartHome_DigitValue_Value, gen_SmartHome_AnalValue_Value, gen_SmartHome_IotComponent_NamedElement, gen_SmartHome_Clock_Sensor, gen_SmartHome_Shutter_Activator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
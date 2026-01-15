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
SmartHouse_House = Class(name="SmartHouse::House")
SmartHouse_Room = Class(name="SmartHouse::Room")
SmartHouse_Person = Class(name="SmartHouse::Person")
SmartHouse_WaterHeater = Class(name="SmartHouse::WaterHeater")
SmartHouse_EV = Class(name="SmartHouse::EV")
SmartHouse_Gate = Class(name="SmartHouse::Gate")
SmartHouse_Security = Class(name="SmartHouse::Security")
SmartHouse_Window = Class(name="SmartHouse::Window")
SmartHouse_Heating = Class(name="SmartHouse::Heating")
SmartHouse_Light = Class(name="SmartHouse::Light")
SmartHouse_AirConditioner = Class(name="SmartHouse::AirConditioner")
SmartHouse_Sensor = Class(name="SmartHouse::Sensor")
SmartHouse_Projector = Class(name="SmartHouse::Projector")
SmartHouse_Cooker = Class(name="SmartHouse::Cooker")
SmartHouse_WashingMachine = Class(name="SmartHouse::WashingMachine")
SmartHouse_CoffeeMaker = Class(name="SmartHouse::CoffeeMaker")

# SmartHouse_House class attributes and methods
SmartHouse_House_name: Property = Property(name="name", type=StringType)
SmartHouse_House_eprice: Property = Property(name="eprice", type=StringType)
SmartHouse_House_time: Property = Property(name="time", type=StringType)
SmartHouse_House_outtemp: Property = Property(name="outtemp", type=StringType)
SmartHouse_House.attributes={SmartHouse_House_outtemp, SmartHouse_House_name, SmartHouse_House_time, SmartHouse_House_eprice}

# SmartHouse_Room class attributes and methods
SmartHouse_Room_temp: Property = Property(name="temp", type=FloatType)
SmartHouse_Room_bright: Property = Property(name="bright", type=StringType)
SmartHouse_Room_air: Property = Property(name="air", type=IntegerType)
SmartHouse_Room_name: Property = Property(name="name", type=StringType)
SmartHouse_Room.attributes={SmartHouse_Room_name, SmartHouse_Room_air, SmartHouse_Room_temp, SmartHouse_Room_bright}

# SmartHouse_Person class attributes and methods
SmartHouse_Person_name: Property = Property(name="name", type=StringType)
SmartHouse_Person.attributes={SmartHouse_Person_name}

# SmartHouse_WaterHeater class attributes and methods
SmartHouse_WaterHeater_temp: Property = Property(name="temp", type=StringType)
SmartHouse_WaterHeater_on: Property = Property(name="on", type=BooleanType)
SmartHouse_WaterHeater_boost: Property = Property(name="boost", type=BooleanType)
SmartHouse_WaterHeater.attributes={SmartHouse_WaterHeater_boost, SmartHouse_WaterHeater_temp, SmartHouse_WaterHeater_on}

# SmartHouse_EV class attributes and methods
SmartHouse_EV_name: Property = Property(name="name", type=StringType)
SmartHouse_EV_pluged: Property = Property(name="pluged", type=BooleanType)
SmartHouse_EV_level: Property = Property(name="level", type=StringType)
SmartHouse_EV_charging: Property = Property(name="charging", type=BooleanType)
SmartHouse_EV.attributes={SmartHouse_EV_pluged, SmartHouse_EV_name, SmartHouse_EV_charging, SmartHouse_EV_level}

# SmartHouse_Gate class attributes and methods
SmartHouse_Gate_outlocked: Property = Property(name="outlocked", type=BooleanType)
SmartHouse_Gate.attributes={SmartHouse_Gate_outlocked}

# SmartHouse_Security class attributes and methods
SmartHouse_Security_on: Property = Property(name="on", type=BooleanType)
SmartHouse_Security.attributes={SmartHouse_Security_on}

# SmartHouse_Window class attributes and methods
SmartHouse_Window_curtainOn: Property = Property(name="curtainOn", type=BooleanType)
SmartHouse_Window_opened: Property = Property(name="opened", type=BooleanType)
SmartHouse_Window_name: Property = Property(name="name", type=StringType)
SmartHouse_Window.attributes={SmartHouse_Window_opened, SmartHouse_Window_curtainOn, SmartHouse_Window_name}

# SmartHouse_Heating class attributes and methods
SmartHouse_Heating_name: Property = Property(name="name", type=StringType)
SmartHouse_Heating_level: Property = Property(name="level", type=IntegerType)
SmartHouse_Heating.attributes={SmartHouse_Heating_level, SmartHouse_Heating_name}

# SmartHouse_Light class attributes and methods
SmartHouse_Light_level: Property = Property(name="level", type=StringType)
SmartHouse_Light.attributes={SmartHouse_Light_level}

# SmartHouse_AirConditioner class attributes and methods
SmartHouse_AirConditioner_level: Property = Property(name="level", type=StringType)
SmartHouse_AirConditioner_freshAir: Property = Property(name="freshAir", type=BooleanType)
SmartHouse_AirConditioner.attributes={SmartHouse_AirConditioner_level, SmartHouse_AirConditioner_freshAir}

# SmartHouse_Sensor class attributes and methods
SmartHouse_Sensor_temp: Property = Property(name="temp", type=BooleanType)
SmartHouse_Sensor_air: Property = Property(name="air", type=BooleanType)
SmartHouse_Sensor_brightness: Property = Property(name="brightness", type=BooleanType)
SmartHouse_Sensor_battery: Property = Property(name="battery", type=StringType)
SmartHouse_Sensor_circle: Property = Property(name="circle", type=StringType)
SmartHouse_Sensor.attributes={SmartHouse_Sensor_battery, SmartHouse_Sensor_circle, SmartHouse_Sensor_air, SmartHouse_Sensor_temp, SmartHouse_Sensor_brightness}

# SmartHouse_Projector class attributes and methods
SmartHouse_Projector_on: Property = Property(name="on", type=BooleanType)
SmartHouse_Projector_brightness: Property = Property(name="brightness", type=StringType)
SmartHouse_Projector_volume: Property = Property(name="volume", type=StringType)
SmartHouse_Projector.attributes={SmartHouse_Projector_volume, SmartHouse_Projector_on, SmartHouse_Projector_brightness}

# SmartHouse_Cooker class attributes and methods
SmartHouse_Cooker_on: Property = Property(name="on", type=BooleanType)
SmartHouse_Cooker.attributes={SmartHouse_Cooker_on}

# SmartHouse_WashingMachine class attributes and methods
SmartHouse_WashingMachine_loaded: Property = Property(name="loaded", type=BooleanType)
SmartHouse_WashingMachine_on: Property = Property(name="on", type=BooleanType)
SmartHouse_WashingMachine.attributes={SmartHouse_WashingMachine_on, SmartHouse_WashingMachine_loaded}

# SmartHouse_CoffeeMaker class attributes and methods
SmartHouse_CoffeeMaker_loaded: Property = Property(name="loaded", type=BooleanType)
SmartHouse_CoffeeMaker_on: Property = Property(name="on", type=BooleanType)
SmartHouse_CoffeeMaker_warming: Property = Property(name="warming", type=BooleanType)
SmartHouse_CoffeeMaker.attributes={SmartHouse_CoffeeMaker_loaded, SmartHouse_CoffeeMaker_on, SmartHouse_CoffeeMaker_warming}

# Relationships
house10: BinaryAssociation = BinaryAssociation(
    name="house10",
    ends={
        Property(name="gate", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="House", type=SmartHouse_Gate, multiplicity=Multiplicity(1, 1))
    }
)
house11: BinaryAssociation = BinaryAssociation(
    name="house11",
    ends={
        Property(name="House12", type=SmartHouse_Security, multiplicity=Multiplicity(1, 1)),
        Property(name="sec", type=SmartHouse_House, multiplicity=Multiplicity(1, 1))
    }
)
room0: BinaryAssociation = BinaryAssociation(
    name="room0",
    ends={
        Property(name="Room", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="house", type=SmartHouse_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member1: BinaryAssociation = BinaryAssociation(
    name="member1",
    ends={
        Property(name="SmartHouse_Person", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_House", type=SmartHouse_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wh2: BinaryAssociation = BinaryAssociation(
    name="wh2",
    ends={
        Property(name="WaterHeater", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="house3", type=SmartHouse_WaterHeater, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ev4: BinaryAssociation = BinaryAssociation(
    name="ev4",
    ends={
        Property(name="EV", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="house5", type=SmartHouse_EV, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gate6: BinaryAssociation = BinaryAssociation(
    name="gate6",
    ends={
        Property(name="Gate", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="house7", type=SmartHouse_Gate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sec8: BinaryAssociation = BinaryAssociation(
    name="sec8",
    ends={
        Property(name="Security", type=SmartHouse_House, multiplicity=Multiplicity(1, 1)),
        Property(name="house9", type=SmartHouse_Security, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
house17: BinaryAssociation = BinaryAssociation(
    name="house17",
    ends={
        Property(name="House18", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room", type=SmartHouse_House, multiplicity=Multiplicity(0, 1))
    }
)
window19: BinaryAssociation = BinaryAssociation(
    name="window19",
    ends={
        Property(name="SmartHouse_Window", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room", type=SmartHouse_Window, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heating20: BinaryAssociation = BinaryAssociation(
    name="heating20",
    ends={
        Property(name="SmartHouse_Heating", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room21", type=SmartHouse_Heating, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
light22: BinaryAssociation = BinaryAssociation(
    name="light22",
    ends={
        Property(name="SmartHouse_Light", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room23", type=SmartHouse_Light, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ac24: BinaryAssociation = BinaryAssociation(
    name="ac24",
    ends={
        Property(name="AirConditioner", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room25", type=SmartHouse_AirConditioner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
house13: BinaryAssociation = BinaryAssociation(
    name="house13",
    ends={
        Property(name="House14", type=SmartHouse_WaterHeater, multiplicity=Multiplicity(1, 1)),
        Property(name="wh", type=SmartHouse_House, multiplicity=Multiplicity(1, 1))
    }
)
house15: BinaryAssociation = BinaryAssociation(
    name="house15",
    ends={
        Property(name="House16", type=SmartHouse_EV, multiplicity=Multiplicity(1, 1)),
        Property(name="ev", type=SmartHouse_House, multiplicity=Multiplicity(1, 1))
    }
)
room39: BinaryAssociation = BinaryAssociation(
    name="room39",
    ends={
        Property(name="Room40", type=SmartHouse_AirConditioner, multiplicity=Multiplicity(1, 1)),
        Property(name="ac", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1))
    }
)
occupied26: BinaryAssociation = BinaryAssociation(
    name="occupied26",
    ends={
        Property(name="SmartHouse_Person28", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room27", type=SmartHouse_Person, multiplicity=Multiplicity(0, 9999))
    }
)
sensor29: BinaryAssociation = BinaryAssociation(
    name="sensor29",
    ends={
        Property(name="SmartHouse_Sensor", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room30", type=SmartHouse_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projector31: BinaryAssociation = BinaryAssociation(
    name="projector31",
    ends={
        Property(name="Projector", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room32", type=SmartHouse_Projector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cooker33: BinaryAssociation = BinaryAssociation(
    name="cooker33",
    ends={
        Property(name="SmartHouse_Cooker", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="SmartHouse_Room34", type=SmartHouse_Cooker, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wm35: BinaryAssociation = BinaryAssociation(
    name="wm35",
    ends={
        Property(name="WashingMachine", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room36", type=SmartHouse_WashingMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cm37: BinaryAssociation = BinaryAssociation(
    name="cm37",
    ends={
        Property(name="CoffeeMaker", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room38", type=SmartHouse_CoffeeMaker, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
room41: BinaryAssociation = BinaryAssociation(
    name="room41",
    ends={
        Property(name="Room42", type=SmartHouse_Projector, multiplicity=Multiplicity(1, 1)),
        Property(name="projector", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1))
    }
)
room43: BinaryAssociation = BinaryAssociation(
    name="room43",
    ends={
        Property(name="Room44", type=SmartHouse_WashingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="wm", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1))
    }
)
room45: BinaryAssociation = BinaryAssociation(
    name="room45",
    ends={
        Property(name="Room46", type=SmartHouse_CoffeeMaker, multiplicity=Multiplicity(1, 1)),
        Property(name="cm", type=SmartHouse_Room, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="SmartHouse",
    types={SmartHouse_House, SmartHouse_Room, SmartHouse_Person, SmartHouse_WaterHeater, SmartHouse_EV, SmartHouse_Gate, SmartHouse_Security, SmartHouse_Window, SmartHouse_Heating, SmartHouse_Light, SmartHouse_AirConditioner, SmartHouse_Sensor, SmartHouse_Projector, SmartHouse_Cooker, SmartHouse_WashingMachine, SmartHouse_CoffeeMaker},
    associations={house10, house11, room0, member1, wh2, ev4, gate6, sec8, house17, window19, heating20, light22, ac24, house13, house15, room39, occupied26, sensor29, projector31, cooker33, wm35, cm37, room41, room43, room45},
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
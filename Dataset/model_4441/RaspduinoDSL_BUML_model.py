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
raspduinoDSL_Model = Class(name="raspduinoDSL::Model")
raspduinoDSL_AbstractDevice = Class(name="raspduinoDSL::AbstractDevice")
raspduinoDSL_EventHandler = Class(name="raspduinoDSL::EventHandler")
raspduinoDSL_SensorListener = Class(name="raspduinoDSL::SensorListener")
raspduinoDSL_Timer = Class(name="raspduinoDSL::Timer")
raspduinoDSL_Sensor = Class(name="raspduinoDSL::Sensor")
AbstractDevice = Class(name="AbstractDevice")
raspduinoDSL_Actuator = Class(name="raspduinoDSL::Actuator")
raspduinoDSL_ChangeActuator = Class(name="raspduinoDSL::ChangeActuator")

# raspduinoDSL_Model class attributes and methods
raspduinoDSL_Model_name: Property = Property(name="name", type=StringType)
raspduinoDSL_Model_hardware: Property = Property(name="hardware", type=StringType)
raspduinoDSL_Model.attributes={raspduinoDSL_Model_hardware, raspduinoDSL_Model_name}

# raspduinoDSL_AbstractDevice class attributes and methods
raspduinoDSL_AbstractDevice_name: Property = Property(name="name", type=StringType)
raspduinoDSL_AbstractDevice_pin: Property = Property(name="pin", type=StringType)
raspduinoDSL_AbstractDevice.attributes={raspduinoDSL_AbstractDevice_name, raspduinoDSL_AbstractDevice_pin}

# raspduinoDSL_EventHandler class attributes and methods
raspduinoDSL_EventHandler_name: Property = Property(name="name", type=StringType)
raspduinoDSL_EventHandler.attributes={raspduinoDSL_EventHandler_name}

# raspduinoDSL_SensorListener class attributes and methods
raspduinoDSL_SensorListener_type: Property = Property(name="type", type=StringType)
raspduinoDSL_SensorListener_l: Property = Property(name="l", type=IntegerType)
raspduinoDSL_SensorListener_h: Property = Property(name="h", type=IntegerType)
raspduinoDSL_SensorListener.attributes={raspduinoDSL_SensorListener_l, raspduinoDSL_SensorListener_type, raspduinoDSL_SensorListener_h}

# raspduinoDSL_Timer class attributes and methods
raspduinoDSL_Timer_repeattype: Property = Property(name="repeattype", type=StringType)
raspduinoDSL_Timer_secs: Property = Property(name="secs", type=IntegerType)
raspduinoDSL_Timer_hours: Property = Property(name="hours", type=IntegerType)
raspduinoDSL_Timer_minutes: Property = Property(name="minutes", type=IntegerType)
raspduinoDSL_Timer.attributes={raspduinoDSL_Timer_secs, raspduinoDSL_Timer_minutes, raspduinoDSL_Timer_hours, raspduinoDSL_Timer_repeattype}

# raspduinoDSL_Sensor class attributes and methods

# AbstractDevice class attributes and methods

# raspduinoDSL_Actuator class attributes and methods

# raspduinoDSL_ChangeActuator class attributes and methods
raspduinoDSL_ChangeActuator_ActuatorState: Property = Property(name="ActuatorState", type=StringType)
raspduinoDSL_ChangeActuator.attributes={raspduinoDSL_ChangeActuator_ActuatorState}

# Relationships
devices0: BinaryAssociation = BinaryAssociation(
    name="devices0",
    ends={
        Property(name="raspduinoDSL_AbstractDevice", type=raspduinoDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_Model", type=raspduinoDSL_AbstractDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventHandlers1: BinaryAssociation = BinaryAssociation(
    name="eventHandlers1",
    ends={
        Property(name="raspduinoDSL_EventHandler", type=raspduinoDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_Model2", type=raspduinoDSL_EventHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorListeners3: BinaryAssociation = BinaryAssociation(
    name="sensorListeners3",
    ends={
        Property(name="raspduinoDSL_SensorListener", type=raspduinoDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_Model4", type=raspduinoDSL_SensorListener, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers5: BinaryAssociation = BinaryAssociation(
    name="timers5",
    ends={
        Property(name="raspduinoDSL_Timer", type=raspduinoDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_Model6", type=raspduinoDSL_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeActuators7: BinaryAssociation = BinaryAssociation(
    name="changeActuators7",
    ends={
        Property(name="raspduinoDSL_ChangeActuator", type=raspduinoDSL_EventHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_EventHandler8", type=raspduinoDSL_ChangeActuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventHandler16: BinaryAssociation = BinaryAssociation(
    name="eventHandler16",
    ends={
        Property(name="raspduinoDSL_EventHandler18", type=raspduinoDSL_Timer, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_Timer17", type=raspduinoDSL_EventHandler, multiplicity=Multiplicity(0, 1))
    }
)
actuator9: BinaryAssociation = BinaryAssociation(
    name="actuator9",
    ends={
        Property(name="raspduinoDSL_Actuator", type=raspduinoDSL_ChangeActuator, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_ChangeActuator10", type=raspduinoDSL_Actuator, multiplicity=Multiplicity(0, 1))
    }
)
sensor11: BinaryAssociation = BinaryAssociation(
    name="sensor11",
    ends={
        Property(name="raspduinoDSL_Sensor", type=raspduinoDSL_SensorListener, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_SensorListener12", type=raspduinoDSL_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
eventHandler13: BinaryAssociation = BinaryAssociation(
    name="eventHandler13",
    ends={
        Property(name="raspduinoDSL_EventHandler15", type=raspduinoDSL_SensorListener, multiplicity=Multiplicity(1, 1)),
        Property(name="raspduinoDSL_SensorListener14", type=raspduinoDSL_EventHandler, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_raspduinoDSL_Sensor_AbstractDevice = Generalization(general=AbstractDevice, specific=raspduinoDSL_Sensor)
gen_raspduinoDSL_Actuator_AbstractDevice = Generalization(general=AbstractDevice, specific=raspduinoDSL_Actuator)

# Domain Model
domain_model = DomainModel(
    name="raspduinoDSL",
    types={raspduinoDSL_Model, raspduinoDSL_AbstractDevice, raspduinoDSL_EventHandler, raspduinoDSL_SensorListener, raspduinoDSL_Timer, raspduinoDSL_Sensor, AbstractDevice, raspduinoDSL_Actuator, raspduinoDSL_ChangeActuator},
    associations={devices0, eventHandlers1, sensorListeners3, timers5, changeActuators7, eventHandler16, actuator9, sensor11, eventHandler13},
    generalizations={gen_raspduinoDSL_Sensor_AbstractDevice, gen_raspduinoDSL_Actuator_AbstractDevice},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
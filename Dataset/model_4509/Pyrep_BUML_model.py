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
PyDslRep_IP = Class(name="PyDslRep::IP")
PyDslRep_Robot = Class(name="PyDslRep::Robot")
PyDslRep_Model = Class(name="PyDslRep::Model")
PyDslRep_Entity = Class(name="PyDslRep::Entity")
PyDslRep_Environment = Class(name="PyDslRep::Environment")
Entity = Class(name="Entity")
PyDslRep_MoveCollection = Class(name="PyDslRep::MoveCollection")
PyDslRep_Wheel = Class(name="PyDslRep::Wheel")
PyDslRep_AbstractDataMove = Class(name="PyDslRep::AbstractDataMove")
PyDslRep_AbstractMove = Class(name="PyDslRep::AbstractMove")
AbstractDataMove = Class(name="AbstractDataMove")
PyDslRep_DataMove = Class(name="PyDslRep::DataMove")
PyDslRep_AbstractCrossMove = Class(name="PyDslRep::AbstractCrossMove")
PyDslRep_Move = Class(name="PyDslRep::Move")
DataMove = Class(name="DataMove")
PyDslRep_Turn = Class(name="PyDslRep::Turn")
PyDslRep_Sensor = Class(name="PyDslRep::Sensor")
PyDslRep_TypeSensor = Class(name="PyDslRep::TypeSensor")

# PyDslRep_IP class attributes and methods
PyDslRep_IP_name: Property = Property(name="name", type=StringType)
PyDslRep_IP_ip: Property = Property(name="ip", type=StringType)
PyDslRep_IP.attributes={PyDslRep_IP_name, PyDslRep_IP_ip}

# PyDslRep_Robot class attributes and methods
PyDslRep_Robot_name: Property = Property(name="name", type=StringType)
PyDslRep_Robot_port: Property = Property(name="port", type=IntegerType)
PyDslRep_Robot.attributes={PyDslRep_Robot_name, PyDslRep_Robot_port}

# PyDslRep_Model class attributes and methods

# PyDslRep_Entity class attributes and methods

# PyDslRep_Environment class attributes and methods
PyDslRep_Environment_name: Property = Property(name="name", type=StringType)
PyDslRep_Environment.attributes={PyDslRep_Environment_name}

# Entity class attributes and methods

# PyDslRep_MoveCollection class attributes and methods
PyDslRep_MoveCollection_concurrent: Property = Property(name="concurrent", type=BooleanType)
PyDslRep_MoveCollection_name: Property = Property(name="name", type=StringType)
PyDslRep_MoveCollection.attributes={PyDslRep_MoveCollection_name, PyDslRep_MoveCollection_concurrent}

# PyDslRep_Wheel class attributes and methods
PyDslRep_Wheel_name: Property = Property(name="name", type=StringType)
PyDslRep_Wheel_radius: Property = Property(name="radius", type=StringType)
PyDslRep_Wheel.attributes={PyDslRep_Wheel_name, PyDslRep_Wheel_radius}

# PyDslRep_AbstractDataMove class attributes and methods

# PyDslRep_AbstractMove class attributes and methods

# AbstractDataMove class attributes and methods

# PyDslRep_DataMove class attributes and methods
PyDslRep_DataMove_name: Property = Property(name="name", type=BooleanType)
PyDslRep_DataMove_type: Property = Property(name="type", type=StringType)
PyDslRep_DataMove_velocity: Property = Property(name="velocity", type=StringType)
PyDslRep_DataMove.attributes={PyDslRep_DataMove_name, PyDslRep_DataMove_type, PyDslRep_DataMove_velocity}

# PyDslRep_AbstractCrossMove class attributes and methods

# PyDslRep_Move class attributes and methods
PyDslRep_Move_distance: Property = Property(name="distance", type=StringType)
PyDslRep_Move.attributes={PyDslRep_Move_distance}

# DataMove class attributes and methods

# PyDslRep_Turn class attributes and methods

# PyDslRep_Sensor class attributes and methods
PyDslRep_Sensor_name: Property = Property(name="name", type=StringType)
PyDslRep_Sensor.attributes={PyDslRep_Sensor_name}

# PyDslRep_TypeSensor class attributes and methods
PyDslRep_TypeSensor_typeName: Property = Property(name="typeName", type=StringType)
PyDslRep_TypeSensor.attributes={PyDslRep_TypeSensor_typeName}

# Relationships
ip1: BinaryAssociation = BinaryAssociation(
    name="ip1",
    ends={
        Property(name="PyDslRep_IP", type=PyDslRep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Environment", type=PyDslRep_IP, multiplicity=Multiplicity(0, 1))
    }
)
robots2: BinaryAssociation = BinaryAssociation(
    name="robots2",
    ends={
        Property(name="PyDslRep_Robot", type=PyDslRep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Environment3", type=PyDslRep_Robot, multiplicity=Multiplicity(0, 9999))
    }
)
environment0: BinaryAssociation = BinaryAssociation(
    name="environment0",
    ends={
        Property(name="PyDslRep_Entity", type=PyDslRep_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Model", type=PyDslRep_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moves4: BinaryAssociation = BinaryAssociation(
    name="moves4",
    ends={
        Property(name="PyDslRep_MoveCollection", type=PyDslRep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Environment5", type=PyDslRep_MoveCollection, multiplicity=Multiplicity(0, 9999))
    }
)
wheels6: BinaryAssociation = BinaryAssociation(
    name="wheels6",
    ends={
        Property(name="PyDslRep_Wheel", type=PyDslRep_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Robot7", type=PyDslRep_Wheel, multiplicity=Multiplicity(0, 9999))
    }
)
robot8: BinaryAssociation = BinaryAssociation(
    name="robot8",
    ends={
        Property(name="PyDslRep_Robot10", type=PyDslRep_MoveCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_MoveCollection9", type=PyDslRep_Robot, multiplicity=Multiplicity(0, 1))
    }
)
moves11: BinaryAssociation = BinaryAssociation(
    name="moves11",
    ends={
        Property(name="PyDslRep_AbstractDataMove", type=PyDslRep_MoveCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_MoveCollection12", type=PyDslRep_AbstractDataMove, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeM13: BinaryAssociation = BinaryAssociation(
    name="typeM13",
    ends={
        Property(name="PyDslRep_DataMove", type=PyDslRep_AbstractMove, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_AbstractMove", type=PyDslRep_DataMove, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeM14: BinaryAssociation = BinaryAssociation(
    name="typeM14",
    ends={
        Property(name="PyDslRep_DataMove15", type=PyDslRep_AbstractCrossMove, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_AbstractCrossMove", type=PyDslRep_DataMove, multiplicity=Multiplicity(0, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="PyDslRep_TypeSensor", type=PyDslRep_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="PyDslRep_Sensor", type=PyDslRep_TypeSensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_PyDslRep_Environment_Entity = Generalization(general=Entity, specific=PyDslRep_Environment)
gen_PyDslRep_Robot_Entity = Generalization(general=Entity, specific=PyDslRep_Robot)
gen_PyDslRep_IP_Entity = Generalization(general=Entity, specific=PyDslRep_IP)
gen_PyDslRep_Wheel_Entity = Generalization(general=Entity, specific=PyDslRep_Wheel)
gen_PyDslRep_MoveCollection_Entity = Generalization(general=Entity, specific=PyDslRep_MoveCollection)
gen_PyDslRep_AbstractMove_AbstractDataMove = Generalization(general=AbstractDataMove, specific=PyDslRep_AbstractMove)
gen_PyDslRep_AbstractCrossMove_AbstractDataMove = Generalization(general=AbstractDataMove, specific=PyDslRep_AbstractCrossMove)
gen_PyDslRep_DataMove_Entity = Generalization(general=Entity, specific=PyDslRep_DataMove)
gen_PyDslRep_Move_DataMove = Generalization(general=DataMove, specific=PyDslRep_Move)
gen_PyDslRep_Turn_DataMove = Generalization(general=DataMove, specific=PyDslRep_Turn)
gen_PyDslRep_Sensor_Entity = Generalization(general=Entity, specific=PyDslRep_Sensor)
gen_PyDslRep_TypeSensor_Entity = Generalization(general=Entity, specific=PyDslRep_TypeSensor)

# Domain Model
domain_model = DomainModel(
    name="PyDslRep",
    types={PyDslRep_IP, PyDslRep_Robot, PyDslRep_Model, PyDslRep_Entity, PyDslRep_Environment, Entity, PyDslRep_MoveCollection, PyDslRep_Wheel, PyDslRep_AbstractDataMove, PyDslRep_AbstractMove, AbstractDataMove, PyDslRep_DataMove, PyDslRep_AbstractCrossMove, PyDslRep_Move, DataMove, PyDslRep_Turn, PyDslRep_Sensor, PyDslRep_TypeSensor},
    associations={ip1, robots2, environment0, moves4, wheels6, robot8, moves11, typeM13, typeM14, type16},
    generalizations={gen_PyDslRep_Environment_Entity, gen_PyDslRep_Robot_Entity, gen_PyDslRep_IP_Entity, gen_PyDslRep_Wheel_Entity, gen_PyDslRep_MoveCollection_Entity, gen_PyDslRep_AbstractMove_AbstractDataMove, gen_PyDslRep_AbstractCrossMove_AbstractDataMove, gen_PyDslRep_DataMove_Entity, gen_PyDslRep_Move_DataMove, gen_PyDslRep_Turn_DataMove, gen_PyDslRep_Sensor_Entity, gen_PyDslRep_TypeSensor_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
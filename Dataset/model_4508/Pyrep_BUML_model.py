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
pyrep_Model = Class(name="pyrep::Model")
pyrep_Entity = Class(name="pyrep::Entity")
pyrep_Environment = Class(name="pyrep::Environment")
Entity = Class(name="Entity")
pyrep_IP = Class(name="pyrep::IP")
pyrep_Robot = Class(name="pyrep::Robot")
pyrep_MoveCollection = Class(name="pyrep::MoveCollection")
AbstractDataMove = Class(name="AbstractDataMove")
pyrep_DataMove = Class(name="pyrep::DataMove")
pyrep_AbstractCrossMove = Class(name="pyrep::AbstractCrossMove")
pyrep_Move = Class(name="pyrep::Move")
DataMove = Class(name="DataMove")
pyrep_Turn = Class(name="pyrep::Turn")
pyrep_Sensor = Class(name="pyrep::Sensor")
pyrep_TypeSensor = Class(name="pyrep::TypeSensor")
pyrep_Wheel = Class(name="pyrep::Wheel")
pyrep_AbstractDataMove = Class(name="pyrep::AbstractDataMove")
pyrep_AbstractMove = Class(name="pyrep::AbstractMove")

# pyrep_Model class attributes and methods

# pyrep_Entity class attributes and methods

# pyrep_Environment class attributes and methods
pyrep_Environment_name: Property = Property(name="name", type=StringType)
pyrep_Environment.attributes={pyrep_Environment_name}

# Entity class attributes and methods

# pyrep_IP class attributes and methods
pyrep_IP_name: Property = Property(name="name", type=StringType)
pyrep_IP_ip: Property = Property(name="ip", type=StringType)
pyrep_IP.attributes={pyrep_IP_name, pyrep_IP_ip}

# pyrep_Robot class attributes and methods
pyrep_Robot_name: Property = Property(name="name", type=StringType)
pyrep_Robot_port: Property = Property(name="port", type=IntegerType)
pyrep_Robot.attributes={pyrep_Robot_port, pyrep_Robot_name}

# pyrep_MoveCollection class attributes and methods
pyrep_MoveCollection_concurrent: Property = Property(name="concurrent", type=BooleanType)
pyrep_MoveCollection_name: Property = Property(name="name", type=StringType)
pyrep_MoveCollection.attributes={pyrep_MoveCollection_name, pyrep_MoveCollection_concurrent}

# AbstractDataMove class attributes and methods

# pyrep_DataMove class attributes and methods
pyrep_DataMove_name: Property = Property(name="name", type=BooleanType)
pyrep_DataMove_type: Property = Property(name="type", type=StringType)
pyrep_DataMove_velocity: Property = Property(name="velocity", type=StringType)
pyrep_DataMove.attributes={pyrep_DataMove_type, pyrep_DataMove_name, pyrep_DataMove_velocity}

# pyrep_AbstractCrossMove class attributes and methods

# pyrep_Move class attributes and methods
pyrep_Move_distance: Property = Property(name="distance", type=StringType)
pyrep_Move.attributes={pyrep_Move_distance}

# DataMove class attributes and methods

# pyrep_Turn class attributes and methods

# pyrep_Sensor class attributes and methods
pyrep_Sensor_name: Property = Property(name="name", type=StringType)
pyrep_Sensor.attributes={pyrep_Sensor_name}

# pyrep_TypeSensor class attributes and methods
pyrep_TypeSensor_typeName: Property = Property(name="typeName", type=StringType)
pyrep_TypeSensor.attributes={pyrep_TypeSensor_typeName}

# pyrep_Wheel class attributes and methods
pyrep_Wheel_name: Property = Property(name="name", type=StringType)
pyrep_Wheel_radius: Property = Property(name="radius", type=StringType)
pyrep_Wheel.attributes={pyrep_Wheel_radius, pyrep_Wheel_name}

# pyrep_AbstractDataMove class attributes and methods

# pyrep_AbstractMove class attributes and methods

# Relationships
environment0: BinaryAssociation = BinaryAssociation(
    name="environment0",
    ends={
        Property(name="pyrep_Entity", type=pyrep_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Model", type=pyrep_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ip1: BinaryAssociation = BinaryAssociation(
    name="ip1",
    ends={
        Property(name="pyrep_IP", type=pyrep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Environment", type=pyrep_IP, multiplicity=Multiplicity(0, 1))
    }
)
robots2: BinaryAssociation = BinaryAssociation(
    name="robots2",
    ends={
        Property(name="pyrep_Robot", type=pyrep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Environment3", type=pyrep_Robot, multiplicity=Multiplicity(0, 9999))
    }
)
moves4: BinaryAssociation = BinaryAssociation(
    name="moves4",
    ends={
        Property(name="pyrep_MoveCollection", type=pyrep_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Environment5", type=pyrep_MoveCollection, multiplicity=Multiplicity(0, 9999))
    }
)
typeM13: BinaryAssociation = BinaryAssociation(
    name="typeM13",
    ends={
        Property(name="pyrep_DataMove", type=pyrep_AbstractMove, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_AbstractMove", type=pyrep_DataMove, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeM14: BinaryAssociation = BinaryAssociation(
    name="typeM14",
    ends={
        Property(name="pyrep_DataMove15", type=pyrep_AbstractCrossMove, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_AbstractCrossMove", type=pyrep_DataMove, multiplicity=Multiplicity(0, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="pyrep_TypeSensor", type=pyrep_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Sensor", type=pyrep_TypeSensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wheels6: BinaryAssociation = BinaryAssociation(
    name="wheels6",
    ends={
        Property(name="pyrep_Wheel", type=pyrep_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_Robot7", type=pyrep_Wheel, multiplicity=Multiplicity(0, 9999))
    }
)
robot8: BinaryAssociation = BinaryAssociation(
    name="robot8",
    ends={
        Property(name="pyrep_Robot10", type=pyrep_MoveCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_MoveCollection9", type=pyrep_Robot, multiplicity=Multiplicity(0, 1))
    }
)
moves11: BinaryAssociation = BinaryAssociation(
    name="moves11",
    ends={
        Property(name="pyrep_AbstractDataMove", type=pyrep_MoveCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="pyrep_MoveCollection12", type=pyrep_AbstractDataMove, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pyrep_Environment_Entity = Generalization(general=Entity, specific=pyrep_Environment)
gen_pyrep_AbstractMove_AbstractDataMove = Generalization(general=AbstractDataMove, specific=pyrep_AbstractMove)
gen_pyrep_AbstractCrossMove_AbstractDataMove = Generalization(general=AbstractDataMove, specific=pyrep_AbstractCrossMove)
gen_pyrep_DataMove_Entity = Generalization(general=Entity, specific=pyrep_DataMove)
gen_pyrep_Move_DataMove = Generalization(general=DataMove, specific=pyrep_Move)
gen_pyrep_Turn_DataMove = Generalization(general=DataMove, specific=pyrep_Turn)
gen_pyrep_Sensor_Entity = Generalization(general=Entity, specific=pyrep_Sensor)
gen_pyrep_TypeSensor_Entity = Generalization(general=Entity, specific=pyrep_TypeSensor)
gen_pyrep_Robot_Entity = Generalization(general=Entity, specific=pyrep_Robot)
gen_pyrep_IP_Entity = Generalization(general=Entity, specific=pyrep_IP)
gen_pyrep_Wheel_Entity = Generalization(general=Entity, specific=pyrep_Wheel)
gen_pyrep_MoveCollection_Entity = Generalization(general=Entity, specific=pyrep_MoveCollection)

# Domain Model
domain_model = DomainModel(
    name="pyrep",
    types={pyrep_Model, pyrep_Entity, pyrep_Environment, Entity, pyrep_IP, pyrep_Robot, pyrep_MoveCollection, AbstractDataMove, pyrep_DataMove, pyrep_AbstractCrossMove, pyrep_Move, DataMove, pyrep_Turn, pyrep_Sensor, pyrep_TypeSensor, pyrep_Wheel, pyrep_AbstractDataMove, pyrep_AbstractMove},
    associations={environment0, ip1, robots2, moves4, typeM13, typeM14, type16, wheels6, robot8, moves11},
    generalizations={gen_pyrep_Environment_Entity, gen_pyrep_AbstractMove_AbstractDataMove, gen_pyrep_AbstractCrossMove_AbstractDataMove, gen_pyrep_DataMove_Entity, gen_pyrep_Move_DataMove, gen_pyrep_Turn_DataMove, gen_pyrep_Sensor_Entity, gen_pyrep_TypeSensor_Entity, gen_pyrep_Robot_Entity, gen_pyrep_IP_Entity, gen_pyrep_Wheel_Entity, gen_pyrep_MoveCollection_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
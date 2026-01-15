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
iot_Board = Class(name="iot::Board")
iot_Arduino = Class(name="iot::Arduino")
iot_Motor = Class(name="iot::Motor")

# iot_Board class attributes and methods

# iot_Arduino class attributes and methods
iot_Arduino_model: Property = Property(name="model", type=StringType)
iot_Arduino_pins: Property = Property(name="pins", type=IntegerType)
iot_Arduino_m_setup: Method = Method(name="setup", parameters={})
iot_Arduino_m_loop: Method = Method(name="loop", parameters={})
iot_Arduino.attributes={iot_Arduino_model, iot_Arduino_pins}
iot_Arduino.methods={iot_Arduino_m_setup, iot_Arduino_m_loop}

# iot_Motor class attributes and methods
iot_Motor_degrees: Property = Property(name="degrees", type=StringType)
iot_Motor_pins: Property = Property(name="pins", type=IntegerType)
iot_Motor_name: Property = Property(name="name", type=StringType)
iot_Motor_library: Property = Property(name="library", type=StringType)
iot_Motor_m_turn: Method = Method(name="turn", parameters={})
iot_Motor.attributes={iot_Motor_pins, iot_Motor_library, iot_Motor_degrees, iot_Motor_name}
iot_Motor.methods={iot_Motor_m_turn}

# Relationships
Arduino0: BinaryAssociation = BinaryAssociation(
    name="Arduino0",
    ends={
        Property(name="iot_Arduino", type=iot_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Board", type=iot_Arduino, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Motor1: BinaryAssociation = BinaryAssociation(
    name="Motor1",
    ends={
        Property(name="iot_Motor", type=iot_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Board2", type=iot_Motor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conector3: BinaryAssociation = BinaryAssociation(
    name="conector3",
    ends={
        Property(name="iot_Motor5", type=iot_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Arduino4", type=iot_Motor, multiplicity=Multiplicity(0, 9999))
    }
)
conectorMotorMotor7: BinaryAssociation = BinaryAssociation(
    name="conectorMotorMotor7",
    ends={
        Property(name="iot_Motor8", type=iot_Motor, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Motor6", type=iot_Motor, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="iot",
    types={iot_Board, iot_Arduino, iot_Motor},
    associations={Arduino0, Motor1, conector3, conectorMotorMotor7},
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
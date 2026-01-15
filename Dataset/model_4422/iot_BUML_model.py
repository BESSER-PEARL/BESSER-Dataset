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
BoardType: Enumeration = Enumeration(
    name="BoardType",
    literals={
            EnumerationLiteral(name="RaspberryPi"),
			EnumerationLiteral(name="Arduino"),
			EnumerationLiteral(name="BeagleBoard")
    }
)

# Classes
iot_IotOperationDef = Class(name="iot::IotOperationDef", is_abstract=True)
iot_HWComp = Class(name="iot::HWComp", is_abstract=True)
iot_Sensor = Class(name="iot::Sensor")
HWComp = Class(name="HWComp")
iot_Actuator = Class(name="iot::Actuator")
iot_System = Class(name="iot::System")
iot_Board = Class(name="iot::Board")
iot_Sketch = Class(name="iot::Sketch")
iot_IotActivity = Class(name="iot::IotActivity", is_abstract=True)

# iot_IotOperationDef class attributes and methods

# iot_HWComp class attributes and methods
iot_HWComp_name: Property = Property(name="name", type=StringType)
iot_HWComp.attributes={iot_HWComp_name}

# iot_Sensor class attributes and methods

# HWComp class attributes and methods

# iot_Actuator class attributes and methods

# iot_System class attributes and methods
iot_System_name: Property = Property(name="name", type=StringType)
iot_System.attributes={iot_System_name}

# iot_Board class attributes and methods
iot_Board_name: Property = Property(name="name", type=StringType)
iot_Board_type: Property = Property(name="type", type=StringType)
iot_Board.attributes={iot_Board_type, iot_Board_name}

# iot_Sketch class attributes and methods

# iot_IotActivity class attributes and methods

# Relationships
components7: BinaryAssociation = BinaryAssociation(
    name="components7",
    ends={
        Property(name="iot_HWComp9", type=iot_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Board8", type=iot_HWComp, multiplicity=Multiplicity(0, 9999))
    }
)
services0: BinaryAssociation = BinaryAssociation(
    name="services0",
    ends={
        Property(name="iot_IotOperationDef", type=iot_HWComp, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_HWComp", type=iot_IotOperationDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components1: BinaryAssociation = BinaryAssociation(
    name="components1",
    ends={
        Property(name="iot_HWComp2", type=iot_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_System", type=iot_HWComp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards3: BinaryAssociation = BinaryAssociation(
    name="boards3",
    ends={
        Property(name="iot_Board", type=iot_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_System4", type=iot_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketch5: BinaryAssociation = BinaryAssociation(
    name="sketch5",
    ends={
        Property(name="iot_Sketch", type=iot_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_System6", type=iot_Sketch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity10: BinaryAssociation = BinaryAssociation(
    name="activity10",
    ends={
        Property(name="iot_IotActivity", type=iot_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Sketch11", type=iot_IotActivity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_iot_Sensor_HWComp = Generalization(general=HWComp, specific=iot_Sensor)
gen_iot_Actuator_HWComp = Generalization(general=HWComp, specific=iot_Actuator)

# Domain Model
domain_model = DomainModel(
    name="iot",
    types={iot_IotOperationDef, iot_HWComp, iot_Sensor, HWComp, iot_Actuator, iot_System, iot_Board, iot_Sketch, iot_IotActivity, BoardType},
    associations={components7, services0, components1, boards3, sketch5, activity10},
    generalizations={gen_iot_Sensor_HWComp, gen_iot_Actuator_HWComp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
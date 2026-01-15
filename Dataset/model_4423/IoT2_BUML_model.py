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
iot2_System = Class(name="iot2::System")
iot2_Activity = Class(name="iot2::Activity")
iot2_OperationDef = Class(name="iot2::OperationDef")
iot2_Sensor = Class(name="iot2::Sensor")
HWComponent = Class(name="HWComponent")
iot2_Actuator = Class(name="iot2::Actuator")
iot2_HWComponent = Class(name="iot2::HWComponent", is_abstract=True)
iot2_Board = Class(name="iot2::Board")
iot2_Sketch = Class(name="iot2::Sketch")

# iot2_System class attributes and methods
iot2_System_name: Property = Property(name="name", type=StringType)
iot2_System.attributes={iot2_System_name}

# iot2_Activity class attributes and methods

# iot2_OperationDef class attributes and methods

# iot2_Sensor class attributes and methods

# HWComponent class attributes and methods

# iot2_Actuator class attributes and methods

# iot2_HWComponent class attributes and methods
iot2_HWComponent_name: Property = Property(name="name", type=StringType)
iot2_HWComponent.attributes={iot2_HWComponent_name}

# iot2_Board class attributes and methods
iot2_Board_name: Property = Property(name="name", type=StringType)
iot2_Board_type: Property = Property(name="type", type=StringType)
iot2_Board.attributes={iot2_Board_type, iot2_Board_name}

# iot2_Sketch class attributes and methods

# Relationships
components5: BinaryAssociation = BinaryAssociation(
    name="components5",
    ends={
        Property(name="iot2_HWComponent7", type=iot2_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Board6", type=iot2_HWComponent, multiplicity=Multiplicity(0, 9999))
    }
)
activity8: BinaryAssociation = BinaryAssociation(
    name="activity8",
    ends={
        Property(name="iot2_Activity", type=iot2_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Sketch9", type=iot2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services10: BinaryAssociation = BinaryAssociation(
    name="services10",
    ends={
        Property(name="iot2_OperationDef", type=iot2_HWComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_HWComponent11", type=iot2_OperationDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="iot2_HWComponent", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System", type=iot2_HWComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards1: BinaryAssociation = BinaryAssociation(
    name="boards1",
    ends={
        Property(name="iot2_Board", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System2", type=iot2_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketch3: BinaryAssociation = BinaryAssociation(
    name="sketch3",
    ends={
        Property(name="iot2_Sketch", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System4", type=iot2_Sketch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_iot2_Sensor_HWComponent = Generalization(general=HWComponent, specific=iot2_Sensor)
gen_iot2_Actuator_HWComponent = Generalization(general=HWComponent, specific=iot2_Actuator)

# Domain Model
domain_model = DomainModel(
    name="iot2",
    types={iot2_System, iot2_Activity, iot2_OperationDef, iot2_Sensor, HWComponent, iot2_Actuator, iot2_HWComponent, iot2_Board, iot2_Sketch, BoardType},
    associations={components5, activity8, services10, components0, boards1, sketch3},
    generalizations={gen_iot2_Sensor_HWComponent, gen_iot2_Actuator_HWComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
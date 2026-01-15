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
surveillance_GunShot = Class(name="surveillance::GunShot")
surveillance_MovingObject = Class(name="surveillance::MovingObject", is_abstract=True)
surveillance_Drone = Class(name="surveillance::Drone")
MovingObject = Class(name="MovingObject")
surveillance_UnidentifiedObject = Class(name="surveillance::UnidentifiedObject")
ProbableElement = Class(name="ProbableElement")
surveillance_Coordinate = Class(name="surveillance::Coordinate")
surveillance_ProbableElement = Class(name="surveillance::ProbableElement", is_abstract=True)
surveillance_Clock = Class(name="surveillance::Clock")

# surveillance_GunShot class attributes and methods
surveillance_GunShot_angle: Property = Property(name="angle", type=FloatType)
surveillance_GunShot_hitsTarget: Property = Property(name="hitsTarget", type=BooleanType)
surveillance_GunShot.attributes={surveillance_GunShot_hitsTarget, surveillance_GunShot_angle}

# surveillance_MovingObject class attributes and methods
surveillance_MovingObject_width: Property = Property(name="width", type=FloatType)
surveillance_MovingObject_angle: Property = Property(name="angle", type=FloatType)
surveillance_MovingObject_speed: Property = Property(name="speed", type=FloatType)
surveillance_MovingObject_m_move: Method = Method(name="move", parameters={Parameter(name='seconds')})
surveillance_MovingObject.attributes={surveillance_MovingObject_angle, surveillance_MovingObject_width, surveillance_MovingObject_speed}
surveillance_MovingObject.methods={surveillance_MovingObject_m_move}

# surveillance_Drone class attributes and methods

# MovingObject class attributes and methods

# surveillance_UnidentifiedObject class attributes and methods

# ProbableElement class attributes and methods

# surveillance_Coordinate class attributes and methods
surveillance_Coordinate_x: Property = Property(name="x", type=FloatType)
surveillance_Coordinate_y: Property = Property(name="y", type=FloatType)
surveillance_Coordinate_m_distance: Method = Method(name="distance", parameters={Parameter(name='other')}, type=FloatType)
surveillance_Coordinate.attributes={surveillance_Coordinate_y, surveillance_Coordinate_x}
surveillance_Coordinate.methods={surveillance_Coordinate_m_distance}

# surveillance_ProbableElement class attributes and methods
surveillance_ProbableElement_confidence: Property = Property(name="confidence", type=FloatType)
surveillance_ProbableElement.attributes={surveillance_ProbableElement_confidence}

# surveillance_Clock class attributes and methods
surveillance_Clock_now: Property = Property(name="now", type=IntegerType)
surveillance_Clock.attributes={surveillance_Clock_now}

# Relationships
shot0: BinaryAssociation = BinaryAssociation(
    name="shot0",
    ends={
        Property(name="GunShot", type=surveillance_Coordinate, multiplicity=Multiplicity(1, 1)),
        Property(name="shootingPosition", type=surveillance_GunShot, multiplicity=Multiplicity(0, 1))
    }
)
object1: BinaryAssociation = BinaryAssociation(
    name="object1",
    ends={
        Property(name="MovingObject", type=surveillance_Coordinate, multiplicity=Multiplicity(1, 1)),
        Property(name="currentPosition", type=surveillance_MovingObject, multiplicity=Multiplicity(1, 1))
    }
)
currentPosition2: BinaryAssociation = BinaryAssociation(
    name="currentPosition2",
    ends={
        Property(name="Coordinate", type=surveillance_MovingObject, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=surveillance_Coordinate, multiplicity=Multiplicity(0, 1))
    }
)
shot3: BinaryAssociation = BinaryAssociation(
    name="shot3",
    ends={
        Property(name="GunShot4", type=surveillance_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone", type=surveillance_GunShot, multiplicity=Multiplicity(0, 9999))
    }
)
shot5: BinaryAssociation = BinaryAssociation(
    name="shot5",
    ends={
        Property(name="GunShot6", type=surveillance_UnidentifiedObject, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=surveillance_GunShot, multiplicity=Multiplicity(0, 9999))
    }
)
shootingPosition7: BinaryAssociation = BinaryAssociation(
    name="shootingPosition7",
    ends={
        Property(name="Coordinate8", type=surveillance_GunShot, multiplicity=Multiplicity(1, 1)),
        Property(name="shot", type=surveillance_Coordinate, multiplicity=Multiplicity(1, 1))
    }
)
drone9: BinaryAssociation = BinaryAssociation(
    name="drone9",
    ends={
        Property(name="Drone", type=surveillance_GunShot, multiplicity=Multiplicity(1, 1)),
        Property(name="shot10", type=surveillance_Drone, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="UnidentifiedObject", type=surveillance_GunShot, multiplicity=Multiplicity(1, 1)),
        Property(name="shot12", type=surveillance_UnidentifiedObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_surveillance_Drone_MovingObject = Generalization(general=MovingObject, specific=surveillance_Drone)
gen_surveillance_UnidentifiedObject_MovingObject = Generalization(general=MovingObject, specific=surveillance_UnidentifiedObject)
gen_surveillance_UnidentifiedObject_ProbableElement = Generalization(general=ProbableElement, specific=surveillance_UnidentifiedObject)
gen_surveillance_GunShot_ProbableElement = Generalization(general=ProbableElement, specific=surveillance_GunShot)

# Domain Model
domain_model = DomainModel(
    name="surveillance",
    types={surveillance_GunShot, surveillance_MovingObject, surveillance_Drone, MovingObject, surveillance_UnidentifiedObject, ProbableElement, surveillance_Coordinate, surveillance_ProbableElement, surveillance_Clock},
    associations={shot0, object1, currentPosition2, shot3, shot5, shootingPosition7, drone9, target11},
    generalizations={gen_surveillance_Drone_MovingObject, gen_surveillance_UnidentifiedObject_MovingObject, gen_surveillance_UnidentifiedObject_ProbableElement, gen_surveillance_GunShot_ProbableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
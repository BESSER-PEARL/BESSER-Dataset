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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="yellow")
    }
)

# Classes
roverDSL_Robot = Class(name="roverDSL::Robot")
roverDSL_Mission = Class(name="roverDSL::Mission")
roverDSL_Colors = Class(name="roverDSL::Colors")
roverDSL_DetectBottle = Class(name="roverDSL::DetectBottle")

# roverDSL_Robot class attributes and methods
roverDSL_Robot_defaultSpeed: Property = Property(name="defaultSpeed", type=IntegerType)
roverDSL_Robot_slowSpeed: Property = Property(name="slowSpeed", type=IntegerType)
roverDSL_Robot_minAngle: Property = Property(name="minAngle", type=IntegerType)
roverDSL_Robot_maxAngle: Property = Property(name="maxAngle", type=IntegerType)
roverDSL_Robot.attributes={roverDSL_Robot_defaultSpeed, roverDSL_Robot_minAngle, roverDSL_Robot_maxAngle, roverDSL_Robot_slowSpeed}

# roverDSL_Mission class attributes and methods
roverDSL_Mission_id: Property = Property(name="id", type=StringType)
roverDSL_Mission.attributes={roverDSL_Mission_id}

# roverDSL_Colors class attributes and methods
roverDSL_Colors_color: Property = Property(name="color", type=StringType)
roverDSL_Colors.attributes={roverDSL_Colors_color}

# roverDSL_DetectBottle class attributes and methods
roverDSL_DetectBottle_maxDistance: Property = Property(name="maxDistance", type=IntegerType)
roverDSL_DetectBottle.attributes={roverDSL_DetectBottle_maxDistance}

# Relationships
mission0: BinaryAssociation = BinaryAssociation(
    name="mission0",
    ends={
        Property(name="roverDSL_Mission", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot", type=roverDSL_Mission, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
find1: BinaryAssociation = BinaryAssociation(
    name="find1",
    ends={
        Property(name="roverDSL_Colors", type=roverDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Mission2", type=roverDSL_Colors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottle3: BinaryAssociation = BinaryAssociation(
    name="bottle3",
    ends={
        Property(name="roverDSL_DetectBottle", type=roverDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Mission4", type=roverDSL_DetectBottle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
avoid5: BinaryAssociation = BinaryAssociation(
    name="avoid5",
    ends={
        Property(name="roverDSL_Colors7", type=roverDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Mission6", type=roverDSL_Colors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="roverDSL",
    types={roverDSL_Robot, roverDSL_Mission, roverDSL_Colors, roverDSL_DetectBottle, Color},
    associations={mission0, find1, bottle3, avoid5},
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
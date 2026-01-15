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
platoon_Platoon = Class(name="platoon::Platoon")
platoon_PlatoonVehicle = Class(name="platoon::PlatoonVehicle")
platoon_JoinPlatoonCoord = Class(name="platoon::JoinPlatoonCoord")
platoon_Vehicle = Class(name="platoon::Vehicle", is_abstract=True)
platoon_JoiningVehicle = Class(name="platoon::JoiningVehicle")
Vehicle = Class(name="Vehicle")
platoon_FrontGap = Class(name="platoon::FrontGap")
platoon_JoiningPosition = Class(name="platoon::JoiningPosition")
platoon_PlatooningSystem = Class(name="platoon::PlatooningSystem")

# platoon_Platoon class attributes and methods
platoon_Platoon_length: Property = Property(name="length", type=IntegerType)
platoon_Platoon_desiredGapSize: Property = Property(name="desiredGapSize", type=IntegerType)
platoon_Platoon.attributes={platoon_Platoon_length, platoon_Platoon_desiredGapSize}

# platoon_PlatoonVehicle class attributes and methods
platoon_PlatoonVehicle_position: Property = Property(name="position", type=IntegerType)
platoon_PlatoonVehicle.attributes={platoon_PlatoonVehicle_position}

# platoon_JoinPlatoonCoord class attributes and methods

# platoon_Vehicle class attributes and methods
platoon_Vehicle_id: Property = Property(name="id", type=IntegerType)
platoon_Vehicle.attributes={platoon_Vehicle_id}

# platoon_JoiningVehicle class attributes and methods

# Vehicle class attributes and methods

# platoon_FrontGap class attributes and methods
platoon_FrontGap_actualGapSize: Property = Property(name="actualGapSize", type=IntegerType)
platoon_FrontGap.attributes={platoon_FrontGap_actualGapSize}

# platoon_JoiningPosition class attributes and methods

# platoon_PlatooningSystem class attributes and methods

# Relationships
leader0: BinaryAssociation = BinaryAssociation(
    name="leader0",
    ends={
        Property(name="platoon_PlatoonVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
follower1: BinaryAssociation = BinaryAssociation(
    name="follower1",
    ends={
        Property(name="platoon_PlatoonVehicle3", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon2", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
follows5: BinaryAssociation = BinaryAssociation(
    name="follows5",
    ends={
        Property(name="platoon_Platoon6", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon4", type=platoon_Platoon, multiplicity=Multiplicity(0, 1))
    }
)
joinplatoonCord7: BinaryAssociation = BinaryAssociation(
    name="joinplatoonCord7",
    ends={
        Property(name="platoon_JoinPlatoonCoord", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon8", type=platoon_JoinPlatoonCoord, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members9: BinaryAssociation = BinaryAssociation(
    name="members9",
    ends={
        Property(name="PlatoonVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 9999))
    }
)
joinCord15: BinaryAssociation = BinaryAssociation(
    name="joinCord15",
    ends={
        Property(name="platoon_JoinPlatoonCoord17", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Vehicle16", type=platoon_JoinPlatoonCoord, multiplicity=Multiplicity(0, 1))
    }
)
cordManager18: BinaryAssociation = BinaryAssociation(
    name="cordManager18",
    ends={
        Property(name="platoon_Vehicle20", type=platoon_JoinPlatoonCoord, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_JoinPlatoonCoord19", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
gapMaker21: BinaryAssociation = BinaryAssociation(
    name="gapMaker21",
    ends={
        Property(name="platoon_Vehicle23", type=platoon_JoinPlatoonCoord, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_JoinPlatoonCoord22", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
joiningVehicle24: BinaryAssociation = BinaryAssociation(
    name="joiningVehicle24",
    ends={
        Property(name="platoon_Vehicle26", type=platoon_JoinPlatoonCoord, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_JoinPlatoonCoord25", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
insertsIn27: BinaryAssociation = BinaryAssociation(
    name="insertsIn27",
    ends={
        Property(name="platoon_FrontGap", type=platoon_JoiningVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_JoiningVehicle", type=platoon_FrontGap, multiplicity=Multiplicity(0, 1))
    }
)
wantsToJoin28: BinaryAssociation = BinaryAssociation(
    name="wantsToJoin28",
    ends={
        Property(name="PlatoonVehicle29", type=platoon_JoiningVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="joiningRequest", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(0, 1))
    }
)
locatedIn30: BinaryAssociation = BinaryAssociation(
    name="locatedIn30",
    ends={
        Property(name="platoon_JoiningPosition", type=platoon_JoiningVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_JoiningVehicle31", type=platoon_JoiningPosition, multiplicity=Multiplicity(0, 1))
    }
)
forms32: BinaryAssociation = BinaryAssociation(
    name="forms32",
    ends={
        Property(name="platoon_FrontGap34", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_PlatoonVehicle33", type=platoon_FrontGap, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
marks35: BinaryAssociation = BinaryAssociation(
    name="marks35",
    ends={
        Property(name="platoon_JoiningPosition37", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_PlatoonVehicle36", type=platoon_JoiningPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joiningRequest38: BinaryAssociation = BinaryAssociation(
    name="joiningRequest38",
    ends={
        Property(name="JoiningVehicle", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="wantsToJoin", type=platoon_JoiningVehicle, multiplicity=Multiplicity(0, 1))
    }
)
platoon39: BinaryAssociation = BinaryAssociation(
    name="platoon39",
    ends={
        Property(name="Platoon", type=platoon_PlatoonVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=platoon_Platoon, multiplicity=Multiplicity(0, 1))
    }
)
vehicles40: BinaryAssociation = BinaryAssociation(
    name="vehicles40",
    ends={
        Property(name="platoon_Vehicle41", type=platoon_PlatooningSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_PlatooningSystem", type=platoon_Vehicle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platoon42: BinaryAssociation = BinaryAssociation(
    name="platoon42",
    ends={
        Property(name="platoon_Platoon44", type=platoon_PlatooningSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_PlatooningSystem43", type=platoon_Platoon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
follows11: BinaryAssociation = BinaryAssociation(
    name="follows11",
    ends={
        Property(name="platoon_Vehicle", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Vehicle10", type=platoon_Vehicle, multiplicity=Multiplicity(0, 1))
    }
)
isAwareOf13: BinaryAssociation = BinaryAssociation(
    name="isAwareOf13",
    ends={
        Property(name="platoon_Vehicle14", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Vehicle12", type=platoon_Vehicle, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_platoon_JoiningVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_JoiningVehicle)
gen_platoon_PlatoonVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_PlatoonVehicle)

# Domain Model
domain_model = DomainModel(
    name="platoon",
    types={platoon_Platoon, platoon_PlatoonVehicle, platoon_JoinPlatoonCoord, platoon_Vehicle, platoon_JoiningVehicle, Vehicle, platoon_FrontGap, platoon_JoiningPosition, platoon_PlatooningSystem},
    associations={leader0, follower1, follows5, joinplatoonCord7, members9, joinCord15, cordManager18, gapMaker21, joiningVehicle24, insertsIn27, wantsToJoin28, locatedIn30, forms32, marks35, joiningRequest38, platoon39, vehicles40, platoon42, follows11, isAwareOf13},
    generalizations={gen_platoon_JoiningVehicle_Vehicle, gen_platoon_PlatoonVehicle_Vehicle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
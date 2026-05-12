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
Train = Class(name="Train")
T = Class(name="T")
FreightTrain = Class(name="FreightTrain")
PassengerTrain = Class(name="PassengerTrain")
EngineCar = Class(name="EngineCar")
PassengerCar = Class(name="PassengerCar")
ContainerCar = Class(name="ContainerCar")
Maglev = Class(name="Maglev")
ElectricTrain = Class(name="ElectricTrain")
MaglevCar = Class(name="MaglevCar")

# Train class attributes and methods
Train_milesPerHour: Property = Property(name="milesPerHour", type=FloatType)
Train_totalCars: Property = Property(name="totalCars", type=IntegerType)
Train.attributes={Train_milesPerHour, Train_totalCars}

# T class attributes and methods

# FreightTrain class attributes and methods
FreightTrain_containerTrain: Property = Property(name="containerTrain", type=BooleanType)
FreightTrain.attributes={FreightTrain_containerTrain}

# PassengerTrain class attributes and methods

# EngineCar class attributes and methods
EngineCar_MAXSPEED: Property = Property(name="MAXSPEED", type=FloatType)
EngineCar.attributes={EngineCar_MAXSPEED}

# PassengerCar class attributes and methods
PassengerCar_NUMSEATS: Property = Property(name="NUMSEATS", type=IntegerType)
PassengerCar_numSeatsOccupied: Property = Property(name="numSeatsOccupied", type=IntegerType)
PassengerCar.attributes={PassengerCar_numSeatsOccupied, PassengerCar_NUMSEATS}

# ContainerCar class attributes and methods
ContainerCar_cubicFeet: Property = Property(name="cubicFeet", type=FloatType)
ContainerCar_climateControlled: Property = Property(name="climateControlled", type=BooleanType)
ContainerCar_temp: Property = Property(name="temp", type=FloatType)
ContainerCar.attributes={ContainerCar_climateControlled, ContainerCar_cubicFeet, ContainerCar_temp}

# Maglev class attributes and methods
Maglev_MAXSPEED: Property = Property(name="MAXSPEED", type=FloatType)
Maglev.attributes={Maglev_MAXSPEED}

# ElectricTrain class attributes and methods
ElectricTrain_MAXSPEED: Property = Property(name="MAXSPEED", type=FloatType)
ElectricTrain.attributes={ElectricTrain_MAXSPEED}

# MaglevCar class attributes and methods
MaglevCar_numSeatsOccupied: Property = Property(name="numSeatsOccupied", type=IntegerType)
MaglevCar_NUMSEATS: Property = Property(name="NUMSEATS", type=IntegerType)
MaglevCar.attributes={MaglevCar_numSeatsOccupied, MaglevCar_NUMSEATS}

# Relationships
Train_freightTrain: BinaryAssociation = BinaryAssociation(
    name="Train_freightTrain",
    ends={
        Property(name="freightTrain0", type=FreightTrain, multiplicity=Multiplicity(0, 1)),
        Property(name="train1", type=Train, multiplicity=Multiplicity(0, 1))
    }
)
Train_passengerTrain: BinaryAssociation = BinaryAssociation(
    name="Train_passengerTrain",
    ends={
        Property(name="passengerTrain2", type=PassengerTrain, multiplicity=Multiplicity(0, 1)),
        Property(name="train3", type=Train, multiplicity=Multiplicity(0, 1))
    }
)
ContainerCar_FreightTrain: BinaryAssociation = BinaryAssociation(
    name="ContainerCar_FreightTrain",
    ends={
        Property(name="freightTrain4", type=FreightTrain, multiplicity=Multiplicity(0, 1)),
        Property(name="containerCar5", type=ContainerCar, multiplicity=Multiplicity(0, 1))
    }
)
PassengerTrain_Maglev: BinaryAssociation = BinaryAssociation(
    name="PassengerTrain_Maglev",
    ends={
        Property(name="maglev6", type=Maglev, multiplicity=Multiplicity(0, 1)),
        Property(name="passengerTrain7", type=PassengerTrain, multiplicity=Multiplicity(0, 1))
    }
)
PassengerTrain_ElectricTrain: BinaryAssociation = BinaryAssociation(
    name="PassengerTrain_ElectricTrain",
    ends={
        Property(name="electricTrain8", type=ElectricTrain, multiplicity=Multiplicity(0, 1)),
        Property(name="passengerTrain9", type=PassengerTrain, multiplicity=Multiplicity(0, 1))
    }
)
ElectricTrain_EngineCar: BinaryAssociation = BinaryAssociation(
    name="ElectricTrain_EngineCar",
    ends={
        Property(name="engineCar10", type=EngineCar, multiplicity=Multiplicity(0, 1)),
        Property(name="electricTrain11", type=ElectricTrain, multiplicity=Multiplicity(0, 1))
    }
)
ElectricTrain_PassengerCar: BinaryAssociation = BinaryAssociation(
    name="ElectricTrain_PassengerCar",
    ends={
        Property(name="passengerCar12", type=PassengerCar, multiplicity=Multiplicity(0, 1)),
        Property(name="electricTrain13", type=ElectricTrain, multiplicity=Multiplicity(0, 1))
    }
)
Maglev_MaglevCar: BinaryAssociation = BinaryAssociation(
    name="Maglev_MaglevCar",
    ends={
        Property(name="maglevCar14", type=MaglevCar, multiplicity=Multiplicity(0, 1)),
        Property(name="maglev15", type=Maglev, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="efd0ceff_408d_41dd_8220_45b05141d1dc",
    types={Train, T, FreightTrain, PassengerTrain, EngineCar, PassengerCar, ContainerCar, Maglev, ElectricTrain, MaglevCar},
    associations={Train_freightTrain, Train_passengerTrain, ContainerCar_FreightTrain, PassengerTrain_Maglev, PassengerTrain_ElectricTrain, ElectricTrain_EngineCar, ElectricTrain_PassengerCar, Maglev_MaglevCar},
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
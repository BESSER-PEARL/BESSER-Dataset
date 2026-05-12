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
spotType: Enumeration = Enumeration(
    name="spotType",
    literals={
            
    }
)

vehicleStatus: Enumeration = Enumeration(
    name="vehicleStatus",
    literals={
            
    }
)

spotStatus: Enumeration = Enumeration(
    name="spotStatus",
    literals={
            
    }
)

# Classes
spotRestriction = Class(name="spotRestriction")
AbstractVehicle = Class(name="AbstractVehicle", is_abstract=True)
Bus = Class(name="Bus")
Car = Class(name="Car")
MotorCycle = Class(name="MotorCycle")
VehicleInterface_Interface = Class(name="VehicleInterface_Interface")
ParkingLot = Class(name="ParkingLot")
Spot = Class(name="Spot")
Parking_Record = Class(name="Parking_Record")

# spotRestriction class attributes and methods
spotRestriction_spotType: Property = Property(name="spotType", type=spotType)
spotRestriction_size: Property = Property(name="size", type=IntegerType)
spotRestriction.attributes={spotRestriction_size, spotRestriction_spotType}

# AbstractVehicle class attributes and methods
AbstractVehicle_type: Property = Property(name="type", type=StringType)
AbstractVehicle_licensePlate: Property = Property(name="licensePlate", type=StringType)
AbstractVehicle_restrictions: Property = Property(name="restrictions", type=spotRestriction)
AbstractVehicle.attributes={AbstractVehicle_licensePlate, AbstractVehicle_type, AbstractVehicle_restrictions}

# Bus class attributes and methods

# Car class attributes and methods

# MotorCycle class attributes and methods

# VehicleInterface_Interface class attributes and methods

# ParkingLot class attributes and methods
ParkingLot_maxSize: Property = Property(name="maxSize", type=IntegerType)
ParkingLot_hourlyPrice: Property = Property(name="hourlyPrice", type=IntegerType)
ParkingLot.attributes={ParkingLot_hourlyPrice, ParkingLot_maxSize}

# Spot class attributes and methods
Spot_spotType: Property = Property(name="spotType", type=spotType)
Spot_level: Property = Property(name="level", type=IntegerType)
Spot_section: Property = Property(name="section", type=StringType)
Spot_spotNumber: Property = Property(name="spotNumber", type=IntegerType)
Spot_status: Property = Property(name="status", type=spotStatus)
Spot_covered: Property = Property(name="covered", type=BooleanType)
Spot_isDisabledSpot: Property = Property(name="isDisabledSpot", type=BooleanType)
Spot_isValet: Property = Property(name="isValet", type=BooleanType)
Spot.attributes={Spot_spotType, Spot_spotNumber, Spot_covered, Spot_status, Spot_isDisabledSpot, Spot_isValet, Spot_section, Spot_level}

# Parking_Record class attributes and methods
Parking_Record_spot: Property = Property(name="spot", type=Spot)
Parking_Record_vehicleLicensePlate: Property = Property(name="vehicleLicensePlate", type=StringType)
Parking_Record_vehicleModel: Property = Property(name="vehicleModel", type=StringType)
Parking_Record_vehicleColor: Property = Property(name="vehicleColor", type=StringType)
Parking_Record_ownerName: Property = Property(name="ownerName", type=StringType)
Parking_Record_ownerPhone: Property = Property(name="ownerPhone", type=StringType)
Parking_Record_parkTime: Property = Property(name="parkTime", type=StringType)
Parking_Record_releaseTime: Property = Property(name="releaseTime", type=StringType)
Parking_Record_hourlyRate: Property = Property(name="hourlyRate", type=IntegerType)
Parking_Record_totalCost: Property = Property(name="totalCost", type=IntegerType)
Parking_Record.attributes={Parking_Record_hourlyRate, Parking_Record_releaseTime, Parking_Record_vehicleModel, Parking_Record_ownerPhone, Parking_Record_vehicleColor, Parking_Record_parkTime, Parking_Record_ownerName, Parking_Record_spot, Parking_Record_vehicleLicensePlate, Parking_Record_totalCost}

# Relationships
spot_ParkingLot: BinaryAssociation = BinaryAssociation(
    name="spot_ParkingLot",
    ends={
        Property(name="parkingLot0", type=ParkingLot, multiplicity=Multiplicity(1, 1)),
        Property(name="spot1", type=Spot, multiplicity=Multiplicity(1, 9999))
    }
)
ParkingLot_Parking_Record: BinaryAssociation = BinaryAssociation(
    name="ParkingLot_Parking_Record",
    ends={
        Property(name="parking_Record2", type=Parking_Record, multiplicity=Multiplicity(0, 9999)),
        Property(name="parkingLot3", type=ParkingLot, multiplicity=Multiplicity(1, 1))
    }
)
Spot_Parking_Record: BinaryAssociation = BinaryAssociation(
    name="Spot_Parking_Record",
    ends={
        Property(name="parking_Record4", type=Parking_Record, multiplicity=Multiplicity(0, 9999)),
        Property(name="spot25", type=Spot, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_B6w2sL5PEeedTfUoC_GfaA",
    types={spotRestriction, AbstractVehicle, Bus, Car, MotorCycle, VehicleInterface_Interface, ParkingLot, Spot, Parking_Record, spotType, vehicleStatus, spotStatus},
    associations={spot_ParkingLot, ParkingLot_Parking_Record, Spot_Parking_Record},
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
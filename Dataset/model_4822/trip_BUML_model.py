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
trip_Person = Class(name="trip::Person")
trip_Car = Class(name="trip::Car")
Vehicle = Class(name="Vehicle")
trip_TripModel = Class(name="trip::TripModel")
trip_NamedElement = Class(name="trip::NamedElement", is_abstract=True)
trip_Van = Class(name="trip::Van")
trip_Trip = Class(name="trip::Trip")
NamedElement = Class(name="NamedElement")
trip_Vehicle = Class(name="trip::Vehicle", is_abstract=True)

# trip_Person class attributes and methods

# trip_Car class attributes and methods

# Vehicle class attributes and methods

# trip_TripModel class attributes and methods

# trip_NamedElement class attributes and methods
trip_NamedElement_name: Property = Property(name="name", type=StringType)
trip_NamedElement.attributes={trip_NamedElement_name}

# trip_Van class attributes and methods

# trip_Trip class attributes and methods

# NamedElement class attributes and methods

# trip_Vehicle class attributes and methods
trip_Vehicle_nrOfSeats: Property = Property(name="nrOfSeats", type=IntegerType)
trip_Vehicle.attributes={trip_Vehicle_nrOfSeats}

# Relationships
vehicle0: BinaryAssociation = BinaryAssociation(
    name="vehicle0",
    ends={
        Property(name="trip_Trip", type=trip_Vehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_Vehicle", type=trip_Trip, multiplicity=Multiplicity(1, 1))
    }
)
passengers1: BinaryAssociation = BinaryAssociation(
    name="passengers1",
    ends={
        Property(name="Person", type=trip_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trips", type=trip_Person, multiplicity=Multiplicity(0, 9999))
    }
)
driver2: BinaryAssociation = BinaryAssociation(
    name="driver2",
    ends={
        Property(name="trip_Person", type=trip_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_Trip3", type=trip_Person, multiplicity=Multiplicity(1, 1))
    }
)
trips4: BinaryAssociation = BinaryAssociation(
    name="trips4",
    ends={
        Property(name="Trip", type=trip_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="passengers", type=trip_Trip, multiplicity=Multiplicity(0, 9999))
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="trip_NamedElement", type=trip_TripModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_TripModel", type=trip_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trip_Vehicle_NamedElement = Generalization(general=NamedElement, specific=trip_Vehicle)
gen_trip_Person_NamedElement = Generalization(general=NamedElement, specific=trip_Person)
gen_trip_Car_Vehicle = Generalization(general=Vehicle, specific=trip_Car)
gen_trip_TripModel_NamedElement = Generalization(general=NamedElement, specific=trip_TripModel)
gen_trip_Van_Vehicle = Generalization(general=Vehicle, specific=trip_Van)
gen_trip_Trip_NamedElement = Generalization(general=NamedElement, specific=trip_Trip)

# Domain Model
domain_model = DomainModel(
    name="trip",
    types={trip_Person, trip_Car, Vehicle, trip_TripModel, trip_NamedElement, trip_Van, trip_Trip, NamedElement, trip_Vehicle},
    associations={vehicle0, passengers1, driver2, trips4, elements5},
    generalizations={gen_trip_Vehicle_NamedElement, gen_trip_Person_NamedElement, gen_trip_Car_Vehicle, gen_trip_TripModel_NamedElement, gen_trip_Van_Vehicle, gen_trip_Trip_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
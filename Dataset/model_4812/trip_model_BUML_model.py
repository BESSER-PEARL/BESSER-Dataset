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
trip_model_Service = Class(name="trip::model::Service")
trip_model_OtherService = Class(name="trip::model::OtherService")
Service = Class(name="Service")
trip_model_location = Class(name="trip::model::location")
trip_model_TravelService = Class(name="trip::model::TravelService")
trip_model_Trip = Class(name="trip::model::Trip")
trip_model_TripModel = Class(name="trip::model::TripModel")

# trip_model_Service class attributes and methods
trip_model_Service_Cost: Property = Property(name="Cost", type=FloatType)
trip_model_Service_Duration: Property = Property(name="Duration", type=IntegerType)
trip_model_Service_Rating: Property = Property(name="Rating", type=IntegerType)
trip_model_Service_name: Property = Property(name="name", type=StringType)
trip_model_Service_Type: Property = Property(name="Type", type=StringType)
trip_model_Service.attributes={trip_model_Service_name, trip_model_Service_Rating, trip_model_Service_Type, trip_model_Service_Cost, trip_model_Service_Duration}

# trip_model_OtherService class attributes and methods

# Service class attributes and methods

# trip_model_location class attributes and methods
trip_model_location_name: Property = Property(name="name", type=StringType)
trip_model_location.attributes={trip_model_location_name}

# trip_model_TravelService class attributes and methods

# trip_model_Trip class attributes and methods
trip_model_Trip_End: Property = Property(name="End", type=DateType)
trip_model_Trip_name: Property = Property(name="name", type=StringType)
trip_model_Trip_Start: Property = Property(name="Start", type=DateType)
trip_model_Trip.attributes={trip_model_Trip_End, trip_model_Trip_name, trip_model_Trip_Start}

# trip_model_TripModel class attributes and methods

# Relationships
location0: BinaryAssociation = BinaryAssociation(
    name="location0",
    ends={
        Property(name="trip_model_location", type=trip_model_OtherService, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_OtherService", type=trip_model_location, multiplicity=Multiplicity(1, 1))
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="trip_model_location2", type=trip_model_TravelService, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_TravelService", type=trip_model_location, multiplicity=Multiplicity(1, 1))
    }
)
destination3: BinaryAssociation = BinaryAssociation(
    name="destination3",
    ends={
        Property(name="trip_model_location5", type=trip_model_TravelService, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_TravelService4", type=trip_model_location, multiplicity=Multiplicity(1, 1))
    }
)
service6: BinaryAssociation = BinaryAssociation(
    name="service6",
    ends={
        Property(name="trip_model_Service", type=trip_model_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_Trip", type=trip_model_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="trip_model_location9", type=trip_model_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_Trip8", type=trip_model_location, multiplicity=Multiplicity(1, 1))
    }
)
destination10: BinaryAssociation = BinaryAssociation(
    name="destination10",
    ends={
        Property(name="trip_model_location12", type=trip_model_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_Trip11", type=trip_model_location, multiplicity=Multiplicity(1, 1))
    }
)
trip13: BinaryAssociation = BinaryAssociation(
    name="trip13",
    ends={
        Property(name="trip_model_Trip14", type=trip_model_TripModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_TripModel", type=trip_model_Trip, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location15: BinaryAssociation = BinaryAssociation(
    name="location15",
    ends={
        Property(name="trip_model_location17", type=trip_model_TripModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trip_model_TripModel16", type=trip_model_location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trip_model_OtherService_Service = Generalization(general=Service, specific=trip_model_OtherService)
gen_trip_model_TravelService_Service = Generalization(general=Service, specific=trip_model_TravelService)

# Domain Model
domain_model = DomainModel(
    name="trip_model",
    types={trip_model_Service, trip_model_OtherService, Service, trip_model_location, trip_model_TravelService, trip_model_Trip, trip_model_TripModel},
    associations={location0, source1, destination3, service6, source7, destination10, trip13, location15},
    generalizations={gen_trip_model_OtherService_Service, gen_trip_model_TravelService_Service},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
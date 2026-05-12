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
Service = Class(name="Service")
TrainStats = Class(name="TrainStats")
ServiceTypeFactory = Class(name="ServiceTypeFactory")
ServiceType_Interface = Class(name="ServiceType_Interface")
Commutator = Class(name="Commutator")
InterCity = Class(name="InterCity")
Sleeper = Class(name="Sleeper")
Coach = Class(name="Coach")
TrainBuilder_Interface = Class(name="TrainBuilder_Interface")
Route = Class(name="Route")
Engine = Class(name="Engine")
Train = Class(name="Train")

# Service class attributes and methods
Service_type: Property = Property(name="type", type=ServiceType_Interface)
Service_arrivalDateTime: Property = Property(name="arrivalDateTime", type=StringType)
Service_departureDateTime: Property = Property(name="departureDateTime", type=StringType)
Service_serviceName: Property = Property(name="serviceName", type=StringType)
Service_serviceId: Property = Property(name="serviceId", type=IntegerType)
Service.attributes={Service_type, Service_serviceName, Service_departureDateTime, Service_arrivalDateTime, Service_serviceId}

# TrainStats class attributes and methods
TrainStats_trainService: Property = Property(name="trainService", type=StringType)
TrainStats_fuelAvg: Property = Property(name="fuelAvg", type=StringType)
TrainStats_passengerCount: Property = Property(name="passengerCount", type=IntegerType)
TrainStats_tempAvg: Property = Property(name="tempAvg", type=StringType)
TrainStats_humidityAvg: Property = Property(name="humidityAvg", type=StringType)
TrainStats.attributes={TrainStats_tempAvg, TrainStats_trainService, TrainStats_fuelAvg, TrainStats_humidityAvg, TrainStats_passengerCount}

# ServiceTypeFactory class attributes and methods
ServiceTypeFactory_type: Property = Property(name="type", type=StringType)
ServiceTypeFactory_getServiceType: Property = Property(name="getServiceType", type=ServiceType_Interface)
ServiceTypeFactory.attributes={ServiceTypeFactory_type, ServiceTypeFactory_getServiceType}

# ServiceType_Interface class attributes and methods

# Commutator class attributes and methods
Commutator_builder: Property = Property(name="builder", type=TrainBuilder_Interface)
Commutator_commutatorTrain: Property = Property(name="commutatorTrain", type=StringType)
Commutator.attributes={Commutator_commutatorTrain, Commutator_builder}

# InterCity class attributes and methods
InterCity_builder: Property = Property(name="builder", type=TrainBuilder_Interface)
InterCity_interCityTrain: Property = Property(name="interCityTrain", type=StringType)
InterCity.attributes={InterCity_builder, InterCity_interCityTrain}

# Sleeper class attributes and methods
Sleeper_builder: Property = Property(name="builder", type=TrainBuilder_Interface)
Sleeper_sleeperTrain: Property = Property(name="sleeperTrain", type=StringType)
Sleeper.attributes={Sleeper_builder, Sleeper_sleeperTrain}

# Coach class attributes and methods
Coach_capacity: Property = Property(name="capacity", type=IntegerType)
Coach_totalPassengers: Property = Property(name="totalPassengers", type=IntegerType)
Coach_temprature: Property = Property(name="temprature", type=StringType)
Coach_humidity: Property = Property(name="humidity", type=StringType)
Coach_coachType: Property = Property(name="coachType", type=StringType)
Coach.attributes={Coach_capacity, Coach_humidity, Coach_temprature, Coach_coachType, Coach_totalPassengers}

# TrainBuilder_Interface class attributes and methods

# Route class attributes and methods
Route_destination: Property = Property(name="destination", type=StringType)
Route_source: Property = Property(name="source", type=StringType)
Route_stops: Property = Property(name="stops", type=StringType)
Route_routeId: Property = Property(name="routeId", type=IntegerType)
Route.attributes={Route_stops, Route_source, Route_destination, Route_routeId}

# Engine class attributes and methods
Engine_horsePower: Property = Property(name="horsePower", type=StringType)
Engine_fuelAvg: Property = Property(name="fuelAvg", type=StringType)
Engine.attributes={Engine_fuelAvg, Engine_horsePower}

# Train class attributes and methods
Train_myEngine: Property = Property(name="myEngine", type=StringType)
Train_myCoach: Property = Property(name="myCoach", type=StringType)
Train.attributes={Train_myEngine, Train_myCoach}

# Relationships
Service_Route: BinaryAssociation = BinaryAssociation(
    name="Service_Route",
    ends={
        Property(name="route10", type=Route, multiplicity=Multiplicity(1, 1)),
        Property(name="service11", type=Service, multiplicity=Multiplicity(1, 1))
    }
)
TrainStats_Service: BinaryAssociation = BinaryAssociation(
    name="TrainStats_Service",
    ends={
        Property(name="service12", type=Service, multiplicity=Multiplicity(1, 1)),
        Property(name="trainStats13", type=TrainStats, multiplicity=Multiplicity(1, 1))
    }
)
InterCity_TrainBuilder2: BinaryAssociation = BinaryAssociation(
    name="InterCity_TrainBuilder2",
    ends={
        Property(name="trainBuilder14", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="interCity15", type=InterCity, multiplicity=Multiplicity(1, 1))
    }
)
Sleeper_TrainBuilder2: BinaryAssociation = BinaryAssociation(
    name="Sleeper_TrainBuilder2",
    ends={
        Property(name="trainBuilder16", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="sleeper17", type=Sleeper, multiplicity=Multiplicity(1, 1))
    }
)
Commutator_TrainBuilder2: BinaryAssociation = BinaryAssociation(
    name="Commutator_TrainBuilder2",
    ends={
        Property(name="trainBuilder18", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="commutator19", type=Commutator, multiplicity=Multiplicity(1, 1))
    }
)
Service_ServiceTypeFactory: BinaryAssociation = BinaryAssociation(
    name="Service_ServiceTypeFactory",
    ends={
        Property(name="serviceTypeFactory0", type=ServiceTypeFactory, multiplicity=Multiplicity(1, 9999)),
        Property(name="service1", type=Service, multiplicity=Multiplicity(1, 1))
    }
)
ServiceTypeFactory_ServiceType: BinaryAssociation = BinaryAssociation(
    name="ServiceTypeFactory_ServiceType",
    ends={
        Property(name="serviceType2", type=ServiceType_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="serviceTypeFactory3", type=ServiceTypeFactory, multiplicity=Multiplicity(1, 1))
    }
)
Sleeper_TrainBuilder: BinaryAssociation = BinaryAssociation(
    name="Sleeper_TrainBuilder",
    ends={
        Property(name="trainBuilder4", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="sleeper5", type=Sleeper, multiplicity=Multiplicity(1, 1))
    }
)
InterCity_TrainBuilder: BinaryAssociation = BinaryAssociation(
    name="InterCity_TrainBuilder",
    ends={
        Property(name="trainBuilder6", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interCity7", type=InterCity, multiplicity=Multiplicity(1, 1))
    }
)
Commutator_TrainBuilder: BinaryAssociation = BinaryAssociation(
    name="Commutator_TrainBuilder",
    ends={
        Property(name="trainBuilder8", type=TrainBuilder_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="commutator9", type=Commutator, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d8913117_b4b2_4319_9035_5868a9e846c7",
    types={Service, TrainStats, ServiceTypeFactory, ServiceType_Interface, Commutator, InterCity, Sleeper, Coach, TrainBuilder_Interface, Route, Engine, Train},
    associations={Service_Route, TrainStats_Service, InterCity_TrainBuilder2, Sleeper_TrainBuilder2, Commutator_TrainBuilder2, Service_ServiceTypeFactory, ServiceTypeFactory_ServiceType, Sleeper_TrainBuilder, InterCity_TrainBuilder, Commutator_TrainBuilder},
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
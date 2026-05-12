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
CargoTrain = Class(name="CargoTrain")
PassengerTrain = Class(name="PassengerTrain")
FirstClass = Class(name="FirstClass")
Coach = Class(name="Coach")

# Train class attributes and methods
Train_Power: Property = Property(name="Power", type=StringType)
Train_Manufacturer: Property = Property(name="Manufacturer", type=StringType)
Train_Cars: Property = Property(name="Cars", type=StringType)
Train_Operator: Property = Property(name="Operator", type=StringType)
Train.attributes={Train_Cars, Train_Manufacturer, Train_Power, Train_Operator}

# CargoTrain class attributes and methods
CargoTrain_Origin: Property = Property(name="Origin", type=StringType)
CargoTrain_Stops: Property = Property(name="Stops", type=StringType)
CargoTrain_Containers: Property = Property(name="Containers", type=StringType)
CargoTrain.attributes={CargoTrain_Stops, CargoTrain_Origin, CargoTrain_Containers}

# PassengerTrain class attributes and methods
PassengerTrain_Origin: Property = Property(name="Origin", type=StringType)
PassengerTrain_Stops: Property = Property(name="Stops", type=StringType)
PassengerTrain_numberOfPassengers: Property = Property(name="numberOfPassengers", type=IntegerType)
PassengerTrain.attributes={PassengerTrain_Stops, PassengerTrain_Origin, PassengerTrain_numberOfPassengers}

# FirstClass class attributes and methods
FirstClass_numberOfSeats: Property = Property(name="numberOfSeats", type=IntegerType)
FirstClass_seatsFilled: Property = Property(name="seatsFilled", type=IntegerType)
FirstClass.attributes={FirstClass_numberOfSeats, FirstClass_seatsFilled}

# Coach class attributes and methods
Coach_numberOfSeats: Property = Property(name="numberOfSeats", type=IntegerType)
Coach_seatsFilled: Property = Property(name="seatsFilled", type=IntegerType)
Coach.attributes={Coach_numberOfSeats, Coach_seatsFilled}

# Domain Model
domain_model = DomainModel(
    name="_QDtykIiSEeeveJPbhFhy_g",
    types={Train, CargoTrain, PassengerTrain, FirstClass, Coach},
    associations={},
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
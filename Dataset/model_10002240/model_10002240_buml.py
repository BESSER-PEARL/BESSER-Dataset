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
Car = Class(name="Car")
Vehicle = Class(name="Vehicle")
Boat = Class(name="Boat")
Airplane = Class(name="Airplane")
Car1 = Class(name="Car1")
Train = Class(name="Train")

# Car class attributes and methods
Car_model: Property = Property(name="model", type=StringType)
Car_engine: Property = Property(name="engine", type=StringType)
Car_wheels: Property = Property(name="wheels", type=StringType)
Car_doors: Property = Property(name="doors", type=IntegerType)
Car_width: Property = Property(name="width", type=IntegerType)
Car_length: Property = Property(name="length", type=IntegerType)
Car_height: Property = Property(name="height", type=IntegerType)
Car.attributes={Car_length, Car_wheels, Car_engine, Car_width, Car_doors, Car_height, Car_model}

# Vehicle class attributes and methods
Vehicle_brand: Property = Property(name="brand", type=StringType)
Vehicle_price: Property = Property(name="price", type=StringType)
Vehicle_engine: Property = Property(name="engine", type=StringType)
Vehicle.attributes={Vehicle_brand, Vehicle_price, Vehicle_engine}

# Boat class attributes and methods
Boat_maxCarryingWeight: Property = Property(name="maxCarryingWeight", type=IntegerType)
Boat.attributes={Boat_maxCarryingWeight}

# Airplane class attributes and methods
Airplane_maxCarryingWeight: Property = Property(name="maxCarryingWeight", type=IntegerType)
Airplane_maxAttitude: Property = Property(name="maxAttitude", type=IntegerType)
Airplane.attributes={Airplane_maxCarryingWeight, Airplane_maxAttitude}

# Car1 class attributes and methods
Car1_doors: Property = Property(name="doors", type=IntegerType)
Car1_helmSide: Property = Property(name="helmSide", type=StringType)
Car1.attributes={Car1_doors, Car1_helmSide}

# Train class attributes and methods
Train_trucks: Property = Property(name="trucks", type=IntegerType)
Train_type: Property = Property(name="type", type=StringType)
Train.attributes={Train_trucks, Train_type}

# Domain Model
domain_model = DomainModel(
    name="_yk3doPQDEeiy0d_yUThzLQ",
    types={Car, Vehicle, Boat, Airplane, Car1, Train},
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
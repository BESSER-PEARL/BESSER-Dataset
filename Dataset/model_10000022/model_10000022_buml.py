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
Book = Class(name="Book")
Car = Class(name="Car")
Car1 = Class(name="Car1")
Engine = Class(name="Engine")
Wheel = Class(name="Wheel")
Manufacturer = Class(name="Manufacturer")
BankAccount = Class(name="BankAccount")

# Book class attributes and methods
Book_name: Property = Property(name="name", type=StringType)
Book_autor: Property = Property(name="autor", type=StringType)
Book_realese_date: Property = Property(name="realese_date", type=StringType)
Book_pages: Property = Property(name="pages", type=IntegerType)
Book.attributes={Book_realese_date, Book_pages, Book_autor, Book_name}

# Car class attributes and methods
Car_model: Property = Property(name="model", type=StringType)
Car_engine: Property = Property(name="engine", type=StringType)
Car_wheels: Property = Property(name="wheels", type=StringType)
Car_doors: Property = Property(name="doors", type=IntegerType)
Car_width: Property = Property(name="width", type=IntegerType)
Car_length: Property = Property(name="length", type=IntegerType)
Car_height: Property = Property(name="height", type=IntegerType)
Car.attributes={Car_doors, Car_wheels, Car_engine, Car_width, Car_length, Car_model, Car_height}

# Car1 class attributes and methods
Car1_model: Property = Property(name="model", type=StringType)
Car1_engine: Property = Property(name="engine", type=StringType)
Car1_wheels: Property = Property(name="wheels", type=StringType)
Car1_doors: Property = Property(name="doors", type=IntegerType)
Car1_width: Property = Property(name="width", type=IntegerType)
Car1_length: Property = Property(name="length", type=IntegerType)
Car1_height: Property = Property(name="height", type=IntegerType)
Car1.attributes={Car1_width, Car1_doors, Car1_wheels, Car1_length, Car1_height, Car1_model, Car1_engine}

# Engine class attributes and methods
Engine_manufacturer: Property = Property(name="manufacturer", type=StringType)
Engine_volume: Property = Property(name="volume", type=IntegerType)
Engine_power: Property = Property(name="power", type=IntegerType)
Engine_rpm: Property = Property(name="rpm", type=IntegerType)
Engine_weight: Property = Property(name="weight", type=IntegerType)
Engine.attributes={Engine_weight, Engine_power, Engine_manufacturer, Engine_rpm, Engine_volume}

# Wheel class attributes and methods
Wheel_manufacturer: Property = Property(name="manufacturer", type=Manufacturer)
Wheel_width: Property = Property(name="width", type=IntegerType)
Wheel_diameter: Property = Property(name="diameter", type=IntegerType)
Wheel.attributes={Wheel_manufacturer, Wheel_width, Wheel_diameter}

# Manufacturer class attributes and methods
Manufacturer_brand: Property = Property(name="brand", type=StringType)
Manufacturer_location: Property = Property(name="location", type=StringType)
Manufacturer.attributes={Manufacturer_location, Manufacturer_brand}

# BankAccount class attributes and methods
BankAccount_owner: Property = Property(name="owner", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=StringType)
BankAccount.attributes={BankAccount_owner, BankAccount_balance}

# Relationships
Car_Engine: BinaryAssociation = BinaryAssociation(
    name="Car_Engine",
    ends={
        Property(name="engine0", type=Engine, multiplicity=Multiplicity(0, 1)),
        Property(name="car1", type=Car1, multiplicity=Multiplicity(0, 1))
    }
)
Car_Wheel: BinaryAssociation = BinaryAssociation(
    name="Car_Wheel",
    ends={
        Property(name="wheel2", type=Wheel, multiplicity=Multiplicity(0, 1)),
        Property(name="car3", type=Car1, multiplicity=Multiplicity(0, 1))
    }
)
Engine_Manufacturer: BinaryAssociation = BinaryAssociation(
    name="Engine_Manufacturer",
    ends={
        Property(name="manufacturer4", type=Manufacturer, multiplicity=Multiplicity(0, 1)),
        Property(name="engine5", type=Engine, multiplicity=Multiplicity(0, 1))
    }
)
Wheel_Manufacturer: BinaryAssociation = BinaryAssociation(
    name="Wheel_Manufacturer",
    ends={
        Property(name="manufacturer6", type=Manufacturer, multiplicity=Multiplicity(0, 1)),
        Property(name="wheel7", type=Wheel, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_03fb9697_ec09_4168_bb93_86efdd808f92",
    types={Book, Car, Car1, Engine, Wheel, Manufacturer, BankAccount},
    associations={Car_Engine, Car_Wheel, Engine_Manufacturer, Wheel_Manufacturer},
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
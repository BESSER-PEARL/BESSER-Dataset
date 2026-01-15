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
restaurant_Restaurant = Class(name="restaurant::Restaurant")
restaurant_Menu = Class(name="restaurant::Menu")
restaurant_Table = Class(name="restaurant::Table")
restaurant_Waiter = Class(name="restaurant::Waiter")
restaurant_Booking = Class(name="restaurant::Booking")

# restaurant_Restaurant class attributes and methods

# restaurant_Menu class attributes and methods

# restaurant_Table class attributes and methods

# restaurant_Waiter class attributes and methods

# restaurant_Booking class attributes and methods

# Relationships
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="restaurant_Table", type=restaurant_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="restaurant_Restaurant2", type=restaurant_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waiters3: BinaryAssociation = BinaryAssociation(
    name="waiters3",
    ends={
        Property(name="restaurant_Waiter", type=restaurant_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="restaurant_Restaurant4", type=restaurant_Waiter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookings5: BinaryAssociation = BinaryAssociation(
    name="bookings5",
    ends={
        Property(name="restaurant_Booking", type=restaurant_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="restaurant_Restaurant6", type=restaurant_Booking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menus0: BinaryAssociation = BinaryAssociation(
    name="menus0",
    ends={
        Property(name="restaurant_Menu", type=restaurant_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="restaurant_Restaurant", type=restaurant_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="restaurant",
    types={restaurant_Restaurant, restaurant_Menu, restaurant_Table, restaurant_Waiter, restaurant_Booking},
    associations={tables1, waiters3, bookings5, menus0},
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
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
Customer = Class(name="Customer")
Order = Class(name="Order")
GPSLocation = Class(name="GPSLocation")
Pizza = Class(name="Pizza")
Toppings = Class(name="Toppings")
Sides = Class(name="Sides")
Address = Class(name="Address")
Base = Class(name="Base")
MealDeal = Class(name="MealDeal")

# Customer class attributes and methods
Customer_customerID: Property = Property(name="customerID", type=IntegerType)
Customer_customerName: Property = Property(name="customerName", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Customer.attributes={Customer_phoneNumber, Customer_customerName, Customer_customerID}

# Order class attributes and methods
Order_orderID: Property = Property(name="orderID", type=IntegerType)
Order_date: Property = Property(name="date", type=StringType)
Order_time: Property = Property(name="time", type=IntegerType)
Order_orderNotes: Property = Property(name="orderNotes", type=StringType)
Order_creditCardDetails: Property = Property(name="creditCardDetails", type=StringType)
Order.attributes={Order_date, Order_orderID, Order_orderNotes, Order_time, Order_creditCardDetails}

# GPSLocation class attributes and methods
GPSLocation_GPS: Property = Property(name="GPS", type=StringType)
GPSLocation.attributes={GPSLocation_GPS}

# Pizza class attributes and methods
Pizza_price: Property = Property(name="price", type=FloatType)
Pizza_isVegetarian: Property = Property(name="isVegetarian", type=BooleanType)
Pizza.attributes={Pizza_price, Pizza_isVegetarian}

# Toppings class attributes and methods
Toppings_isVegetarian: Property = Property(name="isVegetarian", type=BooleanType)
Toppings_name: Property = Property(name="name", type=StringType)
Toppings.attributes={Toppings_isVegetarian, Toppings_name}

# Sides class attributes and methods
Sides_isVegetarian: Property = Property(name="isVegetarian", type=BooleanType)
Sides_name: Property = Property(name="name", type=StringType)
Sides_price: Property = Property(name="price", type=FloatType)
Sides.attributes={Sides_name, Sides_price, Sides_isVegetarian}

# Address class attributes and methods
Address_Line1: Property = Property(name="Line1", type=StringType)
Address_Line_2: Property = Property(name="Line_2", type=StringType)
Address_City: Property = Property(name="City", type=StringType)
Address_County: Property = Property(name="County", type=StringType)
Address.attributes={Address_County, Address_Line_2, Address_Line1, Address_City}

# Base class attributes and methods
Base_name: Property = Property(name="name", type=StringType)
Base_isVegetarian: Property = Property(name="isVegetarian", type=BooleanType)
Base.attributes={Base_name, Base_isVegetarian}

# MealDeal class attributes and methods
MealDeal_name: Property = Property(name="name", type=StringType)
MealDeal_description: Property = Property(name="description", type=StringType)
MealDeal_price: Property = Property(name="price", type=FloatType)
MealDeal_isVegetarian: Property = Property(name="isVegetarian", type=BooleanType)
MealDeal.attributes={MealDeal_isVegetarian, MealDeal_description, MealDeal_name, MealDeal_price}

# Relationships
Pizza_Base: BinaryAssociation = BinaryAssociation(
    name="Pizza_Base",
    ends={
        Property(name="base0", type=Base, multiplicity=Multiplicity(1, 1)),
        Property(name="pizza1", type=Pizza, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Pizza: BinaryAssociation = BinaryAssociation(
    name="Order_Pizza",
    ends={
        Property(name="pizza2", type=Pizza, multiplicity=Multiplicity(0, 9999)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_GPS_Location: BinaryAssociation = BinaryAssociation(
    name="Order_GPS_Location",
    ends={
        Property(name="GPS_Location4", type=GPSLocation, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Pizza_Toppings: BinaryAssociation = BinaryAssociation(
    name="Pizza_Toppings",
    ends={
        Property(name="toppings6", type=Toppings, multiplicity=Multiplicity(0, 9999)),
        Property(name="pizza7", type=Pizza, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Order_Customer",
    ends={
        Property(name="customer8", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Sides: BinaryAssociation = BinaryAssociation(
    name="Order_Sides",
    ends={
        Property(name="sides10", type=Sides, multiplicity=Multiplicity(0, 9999)),
        Property(name="order11", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Address: BinaryAssociation = BinaryAssociation(
    name="Customer_Address",
    ends={
        Property(name="address12", type=Address, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer13", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
MealDeal_Sides: BinaryAssociation = BinaryAssociation(
    name="MealDeal_Sides",
    ends={
        Property(name="sides14", type=Sides, multiplicity=Multiplicity(0, 9999)),
        Property(name="mealDeal15", type=MealDeal, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Address: BinaryAssociation = BinaryAssociation(
    name="Order_Address",
    ends={
        Property(name="order21", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="address20", type=Address, multiplicity=Multiplicity(0, 1))
    }
)
MealDeal_Pizza: BinaryAssociation = BinaryAssociation(
    name="MealDeal_Pizza",
    ends={
        Property(name="pizza16", type=Pizza, multiplicity=Multiplicity(0, 9999)),
        Property(name="mealDeal17", type=MealDeal, multiplicity=Multiplicity(0, 9999))
    }
)
Order_MealDeal: BinaryAssociation = BinaryAssociation(
    name="Order_MealDeal",
    ends={
        Property(name="mealDeal18", type=MealDeal, multiplicity=Multiplicity(0, 9999)),
        Property(name="order19", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="efaf5fe3_64bf_49fa_999e_101b5c79cffe",
    types={Customer, Order, GPSLocation, Pizza, Toppings, Sides, Address, Base, MealDeal},
    associations={Pizza_Base, Order_Pizza, Order_GPS_Location, Pizza_Toppings, Order_Customer, Order_Sides, Customer_Address, MealDeal_Sides, Order_Address, MealDeal_Pizza, Order_MealDeal},
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
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
Costomer = Class(name="Costomer")
Shipment = Class(name="Shipment")
MyClass = Class(name="MyClass")
Express = Class(name="Express")
Normal = Class(name="Normal")
Order = Class(name="Order")
Item = Class(name="Item")
Cahs = Class(name="Cahs")
CreditCard = Class(name="CreditCard")
Payment = Class(name="Payment")
Shipmment_UseCase = Class(name="Shipmment_UseCase")
Client_1_UseCase = Class(name="Client_1_UseCase")
Client_2_UseCase = Class(name="Client_2_UseCase")
Client_4_UseCase = Class(name="Client_4_UseCase")
Client_3_UseCase = Class(name="Client_3_UseCase")
Internet_____________________network_UseCase = Class(name="Internet_____________________network_UseCase")
Shipment_server_Component = Class(name="Shipment_server_Component")
Order_server_Component = Class(name="Order_server_Component")
customer_Actor = Class(name="customer_Actor")
Company_Actor = Class(name="Company_Actor")
Shipping_UseCase = Class(name="Shipping_UseCase")
Point_system_UseCase = Class(name="Point_system_UseCase")
Pay_UseCase = Class(name="Pay_UseCase")
Cancel_UseCase = Class(name="Cancel_UseCase")
Get_dedcuted_percent_UseCase = Class(name="Get_dedcuted_percent_UseCase")
Se_price_UseCase = Class(name="Se_price_UseCase")
Set_period_of_ship_UseCase = Class(name="Set_period_of_ship_UseCase")
set_deducted_percent_UseCase = Class(name="set_deducted_percent_UseCase")
Normal_UseCase = Class(name="Normal_UseCase")
express_UseCase = Class(name="express_UseCase")
Cash_UseCase = Class(name="Cash_UseCase")
Credit_card_UseCase = Class(name="Credit_card_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
Actor_Actor = Class(name="Actor_Actor")
mysubject_Component = Class(name="mysubject_Component")

# Costomer class attributes and methods
Costomer_Name: Property = Property(name="Name", type=StringType)
Costomer_Email: Property = Property(name="Email", type=StringType)
Costomer_mobileNumber: Property = Property(name="mobileNumber", type=IntegerType)
Costomer_ID: Property = Property(name="ID", type=IntegerType)
Costomer_Address: Property = Property(name="Address", type=StringType)
Costomer.attributes={Costomer_mobileNumber, Costomer_Name, Costomer_ID, Costomer_Address, Costomer_Email}

# Shipment class attributes and methods
Shipment_Date: Property = Property(name="Date", type=DateType)
Shipment_Forbidden_to_ship: Property = Property(name="Forbidden_to_ship", type=StringType)
Shipment_SippingType: Property = Property(name="SippingType", type=StringType)
Shipment_pireodofShip: Property = Property(name="pireodofShip", type=IntegerType)
Shipment.attributes={Shipment_pireodofShip, Shipment_Date, Shipment_Forbidden_to_ship, Shipment_SippingType}

# MyClass class attributes and methods

# Express class attributes and methods

# Normal class attributes and methods

# Order class attributes and methods
Order_orderSirealNumber: Property = Property(name="orderSirealNumber", type=IntegerType)
Order.attributes={Order_orderSirealNumber}

# Item class attributes and methods
Item_Quantity: Property = Property(name="Quantity", type=IntegerType)
Item_price: Property = Property(name="price", type=IntegerType)
Item_ItemID: Property = Property(name="ItemID", type=IntegerType)
Item.attributes={Item_ItemID, Item_price, Item_Quantity}

# Cahs class attributes and methods

# CreditCard class attributes and methods
CreditCard_CCNumber: Property = Property(name="CCNumber", type=IntegerType)
CreditCard.attributes={CreditCard_CCNumber}

# Payment class attributes and methods
Payment_Amuant: Property = Property(name="Amuant", type=IntegerType)
Payment.attributes={Payment_Amuant}

# Shipmment_UseCase class attributes and methods

# Client_1_UseCase class attributes and methods

# Client_2_UseCase class attributes and methods

# Client_4_UseCase class attributes and methods

# Client_3_UseCase class attributes and methods

# Internet_____________________network_UseCase class attributes and methods

# Shipment_server_Component class attributes and methods

# Order_server_Component class attributes and methods

# customer_Actor class attributes and methods

# Company_Actor class attributes and methods

# Shipping_UseCase class attributes and methods

# Point_system_UseCase class attributes and methods

# Pay_UseCase class attributes and methods

# Cancel_UseCase class attributes and methods

# Get_dedcuted_percent_UseCase class attributes and methods

# Se_price_UseCase class attributes and methods

# Set_period_of_ship_UseCase class attributes and methods

# set_deducted_percent_UseCase class attributes and methods

# Normal_UseCase class attributes and methods

# express_UseCase class attributes and methods

# Cash_UseCase class attributes and methods

# Credit_card_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# Actor_Actor class attributes and methods

# mysubject_Component class attributes and methods

# Relationships
Order_Costomer: BinaryAssociation = BinaryAssociation(
    name="Order_Costomer",
    ends={
        Property(name="Order_Costomer_00", type=Costomer, multiplicity=Multiplicity(1, 1)),
        Property(name="ship_to1", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Costomer_Shipment: BinaryAssociation = BinaryAssociation(
    name="Costomer_Shipment",
    ends={
        Property(name="Costomer_Shipment_02", type=Shipment, multiplicity=Multiplicity(1, 9999)),
        Property(name="has_shippment3", type=Costomer, multiplicity=Multiplicity(0, 9999))
    }
)
Item_Order: BinaryAssociation = BinaryAssociation(
    name="Item_Order",
    ends={
        Property(name="Item_Order_04", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="Item_Order_15", type=Item, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="Order_Payment_06", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="Order_Payment_17", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Client_1_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Client_1_Internet_network",
    ends={
        Property(name="internet_network8", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client_19", type=Client_1_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Client_2_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Client_2_Internet_network",
    ends={
        Property(name="internet_network10", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client_211", type=Client_2_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Shipment_server_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Shipment_server_Internet_network",
    ends={
        Property(name="internet_network18", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shipment_server19", type=Shipment_server_Component, multiplicity=Multiplicity(0, 1))
    }
)
Company_Set_period_of_ship: BinaryAssociation = BinaryAssociation(
    name="Company_Set_period_of_ship",
    ends={
        Property(name="set_period_of_ship20", type=Set_period_of_ship_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="company21", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Company_Se_price: BinaryAssociation = BinaryAssociation(
    name="Company_Se_price",
    ends={
        Property(name="se_price22", type=Se_price_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="company23", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Company_set_deducted_percent: BinaryAssociation = BinaryAssociation(
    name="Company_set_deducted_percent",
    ends={
        Property(name="set_deducted_percent24", type=set_deducted_percent_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="company25", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_Point_system: BinaryAssociation = BinaryAssociation(
    name="customer_Point_system",
    ends={
        Property(name="point_system26", type=Point_system_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer27", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_Pay: BinaryAssociation = BinaryAssociation(
    name="customer_Pay",
    ends={
        Property(name="pay28", type=Pay_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer29", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_Cancel: BinaryAssociation = BinaryAssociation(
    name="customer_Cancel",
    ends={
        Property(name="cancel30", type=Cancel_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer31", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_Get_dedcuted_percent: BinaryAssociation = BinaryAssociation(
    name="customer_Get_dedcuted_percent",
    ends={
        Property(name="get_dedcuted_percent32", type=Get_dedcuted_percent_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer33", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Company_Shipping: BinaryAssociation = BinaryAssociation(
    name="Company_Shipping",
    ends={
        Property(name="shipping34", type=Shipping_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="company35", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_Shipping: BinaryAssociation = BinaryAssociation(
    name="customer_Shipping",
    ends={
        Property(name="shipping36", type=Shipping_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer37", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_3_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Client_3_Internet_network",
    ends={
        Property(name="internet_network12", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client_313", type=Client_3_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Client_4_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Client_4_Internet_network",
    ends={
        Property(name="internet_network14", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client_415", type=Client_4_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_server_Internet_network: BinaryAssociation = BinaryAssociation(
    name="Order_server_Internet_network",
    ends={
        Property(name="internet_network16", type=Internet_____________________network_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="order_server17", type=Order_server_Component, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bcc086a9_3482_4f44_8856_1a04bbfd074c",
    types={Costomer, Shipment, MyClass, Express, Normal, Order, Item, Cahs, CreditCard, Payment, Shipmment_UseCase, Client_1_UseCase, Client_2_UseCase, Client_4_UseCase, Client_3_UseCase, Internet_____________________network_UseCase, Shipment_server_Component, Order_server_Component, customer_Actor, Company_Actor, Shipping_UseCase, Point_system_UseCase, Pay_UseCase, Cancel_UseCase, Get_dedcuted_percent_UseCase, Se_price_UseCase, Set_period_of_ship_UseCase, set_deducted_percent_UseCase, Normal_UseCase, express_UseCase, Cash_UseCase, Credit_card_UseCase, UseCase_UseCase, UseCase2_UseCase, Actor_Actor, mysubject_Component},
    associations={Order_Costomer, Costomer_Shipment, Item_Order, Order_Payment, Client_1_Internet_network, Client_2_Internet_network, Shipment_server_Internet_network, Company_Set_period_of_ship, Company_Se_price, Company_set_deducted_percent, customer_Point_system, customer_Pay, customer_Cancel, customer_Get_dedcuted_percent, Company_Shipping, customer_Shipping, Client_3_Internet_network, Client_4_Internet_network, Order_server_Internet_network},
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
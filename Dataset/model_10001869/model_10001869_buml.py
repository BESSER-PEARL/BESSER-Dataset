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
Interface_Interface = Class(name="Interface_Interface")
StoringStrategy_Interface = Class(name="StoringStrategy_Interface")
Class1 = Class(name="Class1")
SoftwareType = Class(name="SoftwareType")
Actor_Actor = Class(name="Actor_Actor")
Custumor_Actor = Class(name="Custumor_Actor")
Customer_Actor = Class(name="Customer_Actor")
Subject_Actor = Class(name="Subject_Actor")
Observer = Class(name="Observer")
ObserverA = Class(name="ObserverA")
ObserverB = Class(name="ObserverB")
Stratrgy_Interface = Class(name="Stratrgy_Interface")
Strategy_Interface = Class(name="Strategy_Interface")
StrategyA = Class(name="StrategyA")
Obs_Actor = Class(name="Obs_Actor")
Observer1 = Class(name="Observer1")
Observer_Actor = Class(name="Observer_Actor")
Subject = Class(name="Subject")
Strategy = Class(name="Strategy")
PaymentStrategy_Interface = Class(name="PaymentStrategy_Interface")
CheckOrCard = Class(name="CheckOrCard")
Check = Class(name="Check")
Card = Class(name="Card")
ShoppingCartExample_ShoppingCart = Class(name="ShoppingCartExample_ShoppingCart")
ShoppingCartExample_Order = Class(name="ShoppingCartExample_Order")
ShoppingCartExample_LineItem = Class(name="ShoppingCartExample_LineItem")
ShoppingCartExample_Account = Class(name="ShoppingCartExample_Account")
ShoppingCartExample_Customer = Class(name="ShoppingCartExample_Customer")
StoringStrategy = Class(name="StoringStrategy")

# Interface_Interface class attributes and methods

# StoringStrategy_Interface class attributes and methods

# Class1 class attributes and methods

# SoftwareType class attributes and methods

# Actor_Actor class attributes and methods

# Custumor_Actor class attributes and methods

# Customer_Actor class attributes and methods

# Subject_Actor class attributes and methods

# Observer class attributes and methods

# ObserverA class attributes and methods

# ObserverB class attributes and methods

# Stratrgy_Interface class attributes and methods

# Strategy_Interface class attributes and methods

# StrategyA class attributes and methods

# Obs_Actor class attributes and methods

# Observer1 class attributes and methods

# Observer_Actor class attributes and methods

# Subject class attributes and methods

# Strategy class attributes and methods

# PaymentStrategy_Interface class attributes and methods

# CheckOrCard class attributes and methods

# Check class attributes and methods

# Card class attributes and methods

# ShoppingCartExample_ShoppingCart class attributes and methods
ShoppingCartExample_ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCartExample_ShoppingCart.attributes={ShoppingCartExample_ShoppingCart_creationDate}

# ShoppingCartExample_Order class attributes and methods
ShoppingCartExample_Order_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Order.attributes={ShoppingCartExample_Order_id}

# ShoppingCartExample_LineItem class attributes and methods
ShoppingCartExample_LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCartExample_LineItem_price: Property = Property(name="price", type=IntegerType)
ShoppingCartExample_LineItem.attributes={ShoppingCartExample_LineItem_price, ShoppingCartExample_LineItem_quantity}

# ShoppingCartExample_Account class attributes and methods
ShoppingCartExample_Account_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Account.attributes={ShoppingCartExample_Account_id}

# ShoppingCartExample_Customer class attributes and methods

# StoringStrategy class attributes and methods

# Relationships
Order_Line: BinaryAssociation = BinaryAssociation(
    name="Order_Line",
    ends={
        Property(name="items0", type=ShoppingCartExample_LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order1", type=ShoppingCartExample_Order, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_Order: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Order",
    ends={
        Property(name="order2", type=ShoppingCartExample_Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="c3", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Account_Customer",
    ends={
        Property(name="customer6", type=ShoppingCartExample_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_aiUTcN87EemZHaiox11UDg",
    types={Interface_Interface, StoringStrategy_Interface, Class1, SoftwareType, Actor_Actor, Custumor_Actor, Customer_Actor, Subject_Actor, Observer, ObserverA, ObserverB, Stratrgy_Interface, Strategy_Interface, StrategyA, Obs_Actor, Observer1, Observer_Actor, Subject, Strategy, PaymentStrategy_Interface, CheckOrCard, Check, Card, ShoppingCartExample_ShoppingCart, ShoppingCartExample_Order, ShoppingCartExample_LineItem, ShoppingCartExample_Account, ShoppingCartExample_Customer, StoringStrategy},
    associations={Order_Line, ShoppingCart_Order, Account_ShoppingCart, Account_Customer},
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
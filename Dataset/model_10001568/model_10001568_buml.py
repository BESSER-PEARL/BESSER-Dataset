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
Product = Class(name="Product")
Shopping_cart = Class(name="Shopping_cart")
Stock = Class(name="Stock")
Order = Class(name="Order")
User = Class(name="User")
Person = Class(name="Person")

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_price: Property = Property(name="price", type=IntegerType)
Product_quantity: Property = Property(name="quantity", type=IntegerType)
Product.attributes={Product_description, Product_name, Product_quantity, Product_price, Product_ProductID}

# Shopping_cart class attributes and methods
Shopping_cart_Products: Property = Property(name="Products", type=StringType)
Shopping_cart.attributes={Shopping_cart_Products}

# Stock class attributes and methods
Stock_Items: Property = Property(name="Items", type=StringType)
Stock.attributes={Stock_Items}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_Date: Property = Property(name="Date", type=StringType)
Order_Customer: Property = Property(name="Customer", type=Person)
Order_items: Property = Property(name="items", type=Shopping_cart)
Order.attributes={Order_Customer, Order_items, Order_OrderID, Order_Date}

# User class attributes and methods
User_UserID: Property = Property(name="UserID", type=IntegerType)
User_UserName: Property = Property(name="UserName", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User.attributes={User_Password, User_UserName, User_UserID}

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_Surname: Property = Property(name="Surname", type=StringType)
Person_Email: Property = Property(name="Email", type=StringType)
Person_Address: Property = Property(name="Address", type=StringType)
Person.attributes={Person_Email, Person_Surname, Person_Address, Person_Name}

# Relationships
Order_Client: BinaryAssociation = BinaryAssociation(
    name="Order_Client",
    ends={
        Property(name="person0", type=Person, multiplicity=Multiplicity(1, 1)),
        Property(name="order1", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Order_Shopping_cart",
    ends={
        Property(name="shopping_cart2", type=Shopping_cart, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Stock_Product: BinaryAssociation = BinaryAssociation(
    name="Stock_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="stock5", type=Stock, multiplicity=Multiplicity(0, 9999))
    }
)
Shopping_cart_Product: BinaryAssociation = BinaryAssociation(
    name="Shopping_cart_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_cart7", type=Shopping_cart, multiplicity=Multiplicity(1, 1))
    }
)
User_Person: BinaryAssociation = BinaryAssociation(
    name="User_Person",
    ends={
        Property(name="person8", type=Person, multiplicity=Multiplicity(1, 1)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GFXlUOGCEee1VcqWCkiVQg",
    types={Product, Shopping_cart, Stock, Order, User, Person},
    associations={Order_Client, Order_Shopping_cart, Stock_Product, Shopping_cart_Product, User_Person},
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
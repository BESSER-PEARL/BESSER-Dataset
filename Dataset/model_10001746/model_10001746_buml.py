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
User = Class(name="User")
ClientAccount = Class(name="ClientAccount")
Double_Interface = Class(name="Double_Interface")
Order = Class(name="Order")
Shopping_Cart = Class(name="Shopping_Cart")

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_ProductName: Property = Property(name="ProductName", type=StringType)
Product_ProductType: Property = Property(name="ProductType", type=StringType)
Product_ProductPrice: Property = Property(name="ProductPrice", type=FloatType)
Product_ProductDescription: Property = Property(name="ProductDescription", type=StringType)
Product_ProductImage: Property = Property(name="ProductImage", type=StringType)
Product.attributes={Product_ProductType, Product_ProductImage, Product_ProductDescription, Product_ProductID, Product_ProductName, Product_ProductPrice}

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_Surname: Property = Property(name="Surname", type=StringType)
User_Age: Property = Property(name="Age", type=IntegerType)
User_Email: Property = Property(name="Email", type=StringType)
User_HomeAddress: Property = Property(name="HomeAddress", type=StringType)
User.attributes={User_Email, User_Age, User_Name, User_HomeAddress, User_Surname}

# ClientAccount class attributes and methods
ClientAccount_Password: Property = Property(name="Password", type=StringType)
ClientAccount.attributes={ClientAccount_Password}

# Double_Interface class attributes and methods

# Order class attributes and methods
Order_OrderNumber: Property = Property(name="OrderNumber", type=IntegerType)
Order_Date: Property = Property(name="Date", type=StringType)
Order_CustomerName: Property = Property(name="CustomerName", type=User)
Order_Products: Property = Property(name="Products", type=Shopping_Cart)
Order_PaymentMethod: Property = Property(name="PaymentMethod", type=StringType)
Order_HomeAddress: Property = Property(name="HomeAddress", type=User)
Order.attributes={Order_OrderNumber, Order_PaymentMethod, Order_Date, Order_Products, Order_HomeAddress, Order_CustomerName}

# Shopping_Cart class attributes and methods
Shopping_Cart_ProductPurchased: Property = Property(name="ProductPurchased", type=StringType)
Shopping_Cart.attributes={Shopping_Cart_ProductPurchased}

# Relationships
ClientAccount_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="ClientAccount_Shopping_Cart",
    ends={
        Property(name="ClientAccount_Shopping_Cart_00", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="ClientAccount_Shopping_Cart_11", type=ClientAccount, multiplicity=Multiplicity(1, 1))
    }
)
Order_ClientAccount: BinaryAssociation = BinaryAssociation(
    name="Order_ClientAccount",
    ends={
        Property(name="clientAccount2", type=ClientAccount, multiplicity=Multiplicity(1, 9999)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Shopping_Cart_Product: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Cart5", type=Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)
Order_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Order_Shopping_Cart",
    ends={
        Property(name="shopping_Cart6", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Sbhw8OCWEeeAyLDAJ12_fg",
    types={Product, User, ClientAccount, Double_Interface, Order, Shopping_Cart},
    associations={ClientAccount_Shopping_Cart, Order_ClientAccount, Shopping_Cart_Product, Order_Shopping_Cart},
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
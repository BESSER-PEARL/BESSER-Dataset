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
ShoppingCart = Class(name="ShoppingCart")
WebUser = Class(name="WebUser")
Order = Class(name="Order")
Product_View = Class(name="Product_View")
Product = Class(name="Product")

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser.attributes={WebUser_password, WebUser_login}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_Address: Property = Property(name="Address", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_status, Order_ordered, Order_Address, Order_number, Order_total}

# Product_View class attributes and methods
Product_View_quantity: Property = Property(name="quantity", type=IntegerType)
Product_View_price: Property = Property(name="price", type=FloatType)
Product_View.attributes={Product_View_quantity, Product_View_price}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# Relationships
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items2", type=Product_View, multiplicity=Multiplicity(1, 1)),
        Property(name="sc3", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems4", type=Product_View, multiplicity=Multiplicity(0, 9999)),
        Property(name="product5", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items6", type=Product_View, multiplicity=Multiplicity(1, 9999)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c89234a8_22fe_4d8c_abaa_48ee91b4fc46",
    types={ShoppingCart, WebUser, Order, Product_View, Product},
    associations={WebUser_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem},
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
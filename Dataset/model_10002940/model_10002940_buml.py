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

# Enumerations
OrderStatus: Enumeration = Enumeration(
    name="OrderStatus",
    literals={
            
    }
)

# Classes
ShoppingCart = Class(name="ShoppingCart")
Item = Class(name="Item")
Product = Class(name="Product")
Account = Class(name="Account")
Payment = Class(name="Payment")
Order = Class(name="Order")
Customer = Class(name="Customer")

# ShoppingCart class attributes and methods
ShoppingCart_id: Property = Property(name="id", type=IntegerType)
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate, ShoppingCart_id}

# Item class attributes and methods
Item_quantity: Property = Property(name="quantity", type=IntegerType)
Item_price: Property = Property(name="price", type=FloatType)
Item_id: Property = Property(name="id", type=IntegerType)
Item.attributes={Item_id, Item_price, Item_quantity}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_id: Property = Property(name="id", type=IntegerType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_description, Product_name, Product_id}

# Account class attributes and methods
Account_id: Property = Property(name="id", type=IntegerType)
Account_openDate: Property = Property(name="openDate", type=DateType)
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account.attributes={Account_openDate, Account_id, Account_billingAddress}

# Payment class attributes and methods
Payment_id: Property = Property(name="id", type=IntegerType)
Payment_total: Property = Property(name="total", type=IntegerType)
Payment_comments: Property = Property(name="comments", type=StringType)
Payment.attributes={Payment_comments, Payment_id, Payment_total}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=IntegerType)
Order_shippingAddress: Property = Property(name="shippingAddress", type=StringType)
Order_finalTotal: Property = Property(name="finalTotal", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_shippingAddress, Order_status, Order_id, Order_finalTotal}

# Customer class attributes and methods
Customer_firstname: Property = Property(name="firstname", type=StringType)
Customer_lastname: Property = Property(name="lastname", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer_id: Property = Property(name="id", type=IntegerType)
Customer_login: Property = Property(name="login", type=StringType)
Customer_password: Property = Property(name="password", type=StringType)
Customer_isBan: Property = Property(name="isBan", type=BooleanType)
Customer.attributes={Customer_lastname, Customer_isBan, Customer_password, Customer_login, Customer_firstname, Customer_id, Customer_emailAddress}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="c0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="cart1", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account3", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="accnt4", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingcart5", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="acc6", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="payment7", type=Payment, multiplicity=Multiplicity(0, 9999))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="payment8", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="shoppingcart10", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="item11", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="item12", type=Item, multiplicity=Multiplicity(1, 9999)),
        Property(name="product13", type=Product, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ebfb6f11_a148_4828_bf9d_ad25c4781c59",
    types={ShoppingCart, Item, Product, Account, Payment, Order, Customer, OrderStatus},
    associations={association2, association3, association4, association5, association6, association7, association8},
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
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
OnlineShopping = Class(name="OnlineShopping")
RetailStore = Class(name="RetailStore")
CustomerInfo = Class(name="CustomerInfo")
Order = Class(name="Order")
Items = Class(name="Items")
ShippingCart = Class(name="ShippingCart")
payment = Class(name="payment")
Clothes = Class(name="Clothes")
Electronic = Class(name="Electronic")
Address = Class(name="Address")
Shopping_Interface = Class(name="Shopping_Interface")

# OnlineShopping class attributes and methods

# RetailStore class attributes and methods

# CustomerInfo class attributes and methods
CustomerInfo_Cname: Property = Property(name="Cname", type=StringType)
CustomerInfo_Cid: Property = Property(name="Cid", type=IntegerType)
CustomerInfo_password: Property = Property(name="password", type=StringType)
CustomerInfo_shippingaddress: Property = Property(name="shippingaddress", type=StringType)
CustomerInfo_billingaddress: Property = Property(name="billingaddress", type=StringType)
CustomerInfo.attributes={CustomerInfo_shippingaddress, CustomerInfo_billingaddress, CustomerInfo_Cname, CustomerInfo_Cid, CustomerInfo_password}

# Order class attributes and methods
Order_Orderid: Property = Property(name="Orderid", type=IntegerType)
Order_datecreated: Property = Property(name="datecreated", type=IntegerType)
Order_shippinddate: Property = Property(name="shippinddate", type=IntegerType)
Order_customername: Property = Property(name="customername", type=StringType)
Order_customerid: Property = Property(name="customerid", type=IntegerType)
Order_statues: Property = Property(name="statues", type=StringType)
Order_shippingid: Property = Property(name="shippingid", type=IntegerType)
Order.attributes={Order_Orderid, Order_customername, Order_shippingid, Order_shippinddate, Order_statues, Order_datecreated, Order_customerid}

# Items class attributes and methods
Items_itemid: Property = Property(name="itemid", type=IntegerType)
Items.attributes={Items_itemid}

# ShippingCart class attributes and methods
ShippingCart_productID: Property = Property(name="productID", type=IntegerType)
ShippingCart_cartID: Property = Property(name="cartID", type=IntegerType)
ShippingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShippingCart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
ShippingCart.attributes={ShippingCart_quantity, ShippingCart_dateAdded, ShippingCart_cartID, ShippingCart_productID}

# payment class attributes and methods
payment_cardID: Property = Property(name="cardID", type=IntegerType)
payment_amount: Property = Property(name="amount", type=IntegerType)
payment.attributes={payment_amount, payment_cardID}

# Clothes class attributes and methods
Clothes_typeofclothe: Property = Property(name="typeofclothe", type=StringType)
Clothes_color: Property = Property(name="color", type=StringType)
Clothes.attributes={Clothes_color, Clothes_typeofclothe}

# Electronic class attributes and methods
Electronic_brand: Property = Property(name="brand", type=StringType)
Electronic.attributes={Electronic_brand}

# Address class attributes and methods
Address_street: Property = Property(name="street", type=StringType)
Address_city: Property = Property(name="city", type=StringType)
Address_state: Property = Property(name="state", type=StringType)
Address_country: Property = Property(name="country", type=StringType)
Address_postalcode: Property = Property(name="postalcode", type=StringType)
Address.attributes={Address_street, Address_state, Address_postalcode, Address_country, Address_city}

# Shopping_Interface class attributes and methods

# Relationships
OnlineShopping_Items: BinaryAssociation = BinaryAssociation(
    name="OnlineShopping_Items",
    ends={
        Property(name="items0", type=Items, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShopping1", type=OnlineShopping, multiplicity=Multiplicity(0, 1))
    }
)
OnlineShopping_Order: BinaryAssociation = BinaryAssociation(
    name="OnlineShopping_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShopping3", type=OnlineShopping, multiplicity=Multiplicity(0, 1))
    }
)
OnlineShopping_CustomerInfo: BinaryAssociation = BinaryAssociation(
    name="OnlineShopping_CustomerInfo",
    ends={
        Property(name="customerInfo4", type=CustomerInfo, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShopping5", type=OnlineShopping, multiplicity=Multiplicity(0, 1))
    }
)
CustomerInfo_ShippingCart: BinaryAssociation = BinaryAssociation(
    name="CustomerInfo_ShippingCart",
    ends={
        Property(name="shippingCart6", type=ShippingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="customerInfo7", type=CustomerInfo, multiplicity=Multiplicity(0, 1))
    }
)
Order_payment: BinaryAssociation = BinaryAssociation(
    name="Order_payment",
    ends={
        Property(name="payment8", type=payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
CustomerInfo_Address: BinaryAssociation = BinaryAssociation(
    name="CustomerInfo_Address",
    ends={
        Property(name="address10", type=Address, multiplicity=Multiplicity(0, 1)),
        Property(name="customerInfo11", type=CustomerInfo, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ac8360ac_2f13_449d_9387_7503efbd3922",
    types={OnlineShopping, RetailStore, CustomerInfo, Order, Items, ShippingCart, payment, Clothes, Electronic, Address, Shopping_Interface},
    associations={OnlineShopping_Items, OnlineShopping_Order, OnlineShopping_CustomerInfo, CustomerInfo_ShippingCart, Order_payment, CustomerInfo_Address},
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
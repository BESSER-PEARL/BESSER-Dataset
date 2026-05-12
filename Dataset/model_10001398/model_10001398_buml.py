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
user = Class(name="user")
coustomer = Class(name="coustomer")
ShoppingCart = Class(name="ShoppingCart")
cartitem = Class(name="cartitem")
product = Class(name="product")
orderDetail = Class(name="orderDetail")
order = Class(name="order")
shippinginfo = Class(name="shippinginfo")

# user class attributes and methods
user_UserId: Property = Property(name="UserId", type=IntegerType)
user_email: Property = Property(name="email", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user_loginstatus: Property = Property(name="loginstatus", type=StringType)
user.attributes={user_UserId, user_password, user_loginstatus, user_email}

# coustomer class attributes and methods
coustomer_customerId: Property = Property(name="customerId", type=IntegerType)
coustomer_name: Property = Property(name="name", type=StringType)
coustomer_address: Property = Property(name="address", type=StringType)
coustomer_email: Property = Property(name="email", type=StringType)
coustomer_phoneno: Property = Property(name="phoneno", type=IntegerType)
coustomer_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
coustomer.attributes={coustomer_shippinginfo, coustomer_name, coustomer_customerId, coustomer_address, coustomer_email, coustomer_phoneno}

# ShoppingCart class attributes and methods
ShoppingCart_cartId: Property = Property(name="cartId", type=IntegerType)
ShoppingCart_productId: Property = Property(name="productId", type=IntegerType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_productId, ShoppingCart_dateAdded, ShoppingCart_quantity, ShoppingCart_cartId}

# cartitem class attributes and methods
cartitem_productId: Property = Property(name="productId", type=IntegerType)
cartitem_quantity: Property = Property(name="quantity", type=IntegerType)
cartitem_unitcost: Property = Property(name="unitcost", type=FloatType)
cartitem_subtotal: Property = Property(name="subtotal", type=FloatType)
cartitem.attributes={cartitem_quantity, cartitem_unitcost, cartitem_productId, cartitem_subtotal}

# product class attributes and methods
product_productId: Property = Property(name="productId", type=IntegerType)
product_name: Property = Property(name="name", type=StringType)
product_description: Property = Property(name="description", type=StringType)
product_price: Property = Property(name="price", type=IntegerType)
product_image: Property = Property(name="image", type=StringType)
product.attributes={product_description, product_image, product_productId, product_price, product_name}

# orderDetail class attributes and methods
orderDetail_orderId: Property = Property(name="orderId", type=IntegerType)
orderDetail_productid: Property = Property(name="productid", type=IntegerType)
orderDetail_productname: Property = Property(name="productname", type=StringType)
orderDetail_quantity: Property = Property(name="quantity", type=IntegerType)
orderDetail_unitcost: Property = Property(name="unitcost", type=FloatType)
orderDetail_subtotall: Property = Property(name="subtotall", type=FloatType)
orderDetail.attributes={orderDetail_productid, orderDetail_quantity, orderDetail_productname, orderDetail_orderId, orderDetail_unitcost, orderDetail_subtotall}

# order class attributes and methods
order_orderId: Property = Property(name="orderId", type=IntegerType)
order_datecreated: Property = Property(name="datecreated", type=StringType)
order_name: Property = Property(name="name", type=StringType)
order_customerid: Property = Property(name="customerid", type=IntegerType)
order_shippingid: Property = Property(name="shippingid", type=StringType)
order.attributes={order_orderId, order_shippingid, order_datecreated, order_name, order_customerid}

# shippinginfo class attributes and methods
shippinginfo_shippingId: Property = Property(name="shippingId", type=IntegerType)
shippinginfo_shippingcost: Property = Property(name="shippingcost", type=IntegerType)
shippinginfo.attributes={shippinginfo_shippingcost, shippinginfo_shippingId}

# Relationships
ShoppingCart_coustomer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_coustomer",
    ends={
        Property(name="ShoppingCart_coustomer_00", type=coustomer, multiplicity=Multiplicity(1, 1)),
        Property(name="ShoppingCart_coustomer_11", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_cartitem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_cartitem",
    ends={
        Property(name="ShoppingCart_cartitem_02", type=cartitem, multiplicity=Multiplicity(0, 1)),
        Property(name="ShoppingCart_cartitem_13", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
cartitem_ProLocal: BinaryAssociation = BinaryAssociation(
    name="cartitem_ProLocal",
    ends={
        Property(name="cartitem_ProLocal_04", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="cartitem_ProLocal_15", type=cartitem, multiplicity=Multiplicity(0, 1))
    }
)
orderDetail_ProLocal: BinaryAssociation = BinaryAssociation(
    name="orderDetail_ProLocal",
    ends={
        Property(name="orderDetail_ProLocal_06", type=product, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetail_ProLocal_17", type=orderDetail, multiplicity=Multiplicity(1, 9999))
    }
)
coustomer_order: BinaryAssociation = BinaryAssociation(
    name="coustomer_order",
    ends={
        Property(name="coustomer_order_08", type=order, multiplicity=Multiplicity(1, 9999)),
        Property(name="coustomer_order_19", type=coustomer, multiplicity=Multiplicity(1, 1))
    }
)
order_orderDetail: BinaryAssociation = BinaryAssociation(
    name="order_orderDetail",
    ends={
        Property(name="order_orderDetail_010", type=orderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="order_orderDetail_111", type=order, multiplicity=Multiplicity(1, 1))
    }
)
order_shippinginfo: BinaryAssociation = BinaryAssociation(
    name="order_shippinginfo",
    ends={
        Property(name="order_shippinginfo_012", type=shippinginfo, multiplicity=Multiplicity(1, 1)),
        Property(name="order_shippinginfo_113", type=order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4PUEUH9LEeqjCeBtMxTJVQ",
    types={user, coustomer, ShoppingCart, cartitem, product, orderDetail, order, shippinginfo},
    associations={ShoppingCart_coustomer, ShoppingCart_cartitem, cartitem_ProLocal, orderDetail_ProLocal, coustomer_order, order_orderDetail, order_shippinginfo},
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
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
login_status: Enumeration = Enumeration(
    name="login_status",
    literals={
            
    }
)

# Classes
Login = Class(name="Login")
User = Class(name="User")
ShoppingCart = Class(name="ShoppingCart")
cartitem = Class(name="cartitem")
product = Class(name="product")
orderDetail = Class(name="orderDetail")
order = Class(name="order")
shippinginfo = Class(name="shippinginfo")
Payment = Class(name="Payment")

# Login class attributes and methods
Login_UserId: Property = Property(name="UserId", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_login_status: Property = Property(name="login_status", type=StringType)
Login.attributes={Login_password, Login_UserId, Login_login_status}

# User class attributes and methods
User_User_name: Property = Property(name="User_name", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_phone_no: Property = Property(name="phone_no", type=IntegerType)
User_Card_info: Property = Property(name="Card_info", type=StringType)
User_shipping_info: Property = Property(name="shipping_info", type=StringType)
User.attributes={User_phone_no, User_email, User_shipping_info, User_Card_info, User_User_name, User_address}

# ShoppingCart class attributes and methods
ShoppingCart_cartId: Property = Property(name="cartId", type=IntegerType)
ShoppingCart_productId: Property = Property(name="productId", type=IntegerType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_dateAdded, ShoppingCart_cartId, ShoppingCart_productId, ShoppingCart_quantity}

# cartitem class attributes and methods
cartitem_name: Property = Property(name="name", type=StringType)
cartitem_product: Property = Property(name="product", type=IntegerType)
cartitem_quantity: Property = Property(name="quantity", type=IntegerType)
cartitem_unitcost: Property = Property(name="unitcost", type=FloatType)
cartitem_subtotal: Property = Property(name="subtotal", type=FloatType)
cartitem.attributes={cartitem_product, cartitem_subtotal, cartitem_name, cartitem_quantity, cartitem_unitcost}

# product class attributes and methods
product_productid: Property = Property(name="productid", type=IntegerType)
product_productname: Property = Property(name="productname", type=StringType)
product_price: Property = Property(name="price", type=IntegerType)
product_imagefilename: Property = Property(name="imagefilename", type=StringType)
product.attributes={product_productname, product_price, product_imagefilename, product_productid}

# orderDetail class attributes and methods
orderDetail_orderId: Property = Property(name="orderId", type=IntegerType)
orderDetail_productid: Property = Property(name="productid", type=IntegerType)
orderDetail_productname: Property = Property(name="productname", type=StringType)
orderDetail_quantity: Property = Property(name="quantity", type=IntegerType)
orderDetail_unitcost: Property = Property(name="unitcost", type=FloatType)
orderDetail_subtotall: Property = Property(name="subtotall", type=FloatType)
orderDetail.attributes={orderDetail_orderId, orderDetail_subtotall, orderDetail_unitcost, orderDetail_productname, orderDetail_productid, orderDetail_quantity}

# order class attributes and methods
order_shipping_date: Property = Property(name="shipping_date", type=DateType)
order_c_name: Property = Property(name="c_name", type=StringType)
order_status: Property = Property(name="status", type=StringType)
order_shippingid: Property = Property(name="shippingid", type=StringType)
order_order_ID: Property = Property(name="order_ID", type=IntegerType)
order_date_created: Property = Property(name="date_created", type=DateType)
order.attributes={order_shipping_date, order_shippingid, order_order_ID, order_status, order_date_created, order_c_name}

# shippinginfo class attributes and methods
shippinginfo_shipping_id: Property = Property(name="shipping_id", type=StringType)
shippinginfo_shipping_type: Property = Property(name="shipping_type", type=StringType)
shippinginfo_shipping_cost: Property = Property(name="shipping_cost", type=IntegerType)
shippinginfo_shipping_Address: Property = Property(name="shipping_Address", type=StringType)
shippinginfo_shipping_date: Property = Property(name="shipping_date", type=DateType)
shippinginfo.attributes={shippinginfo_shipping_Address, shippinginfo_shipping_type, shippinginfo_shipping_date, shippinginfo_shipping_id, shippinginfo_shipping_cost}

# Payment class attributes and methods
Payment_Payment_id: Property = Property(name="Payment_id", type=StringType)
Payment_Payment_type: Property = Property(name="Payment_type", type=StringType)
Payment_Payment_method: Property = Property(name="Payment_method", type=IntegerType)
Payment.attributes={Payment_Payment_id, Payment_Payment_method, Payment_Payment_type}

# Relationships
ShoppingCart_coustomer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_coustomer",
    ends={
        Property(name="ShoppingCart_coustomer_00", type=User, multiplicity=Multiplicity(1, 1)),
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
coustomer_order: BinaryAssociation = BinaryAssociation(
    name="coustomer_order",
    ends={
        Property(name="coustomer_order_04", type=order, multiplicity=Multiplicity(1, 9999)),
        Property(name="coustomer_order_15", type=User, multiplicity=Multiplicity(1, 1))
    }
)
order_orderDetail: BinaryAssociation = BinaryAssociation(
    name="order_orderDetail",
    ends={
        Property(name="order_orderDetail_06", type=orderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="order_orderDetail_17", type=order, multiplicity=Multiplicity(1, 1))
    }
)
order_shippinginfo: BinaryAssociation = BinaryAssociation(
    name="order_shippinginfo",
    ends={
        Property(name="order_shippinginfo_08", type=shippinginfo, multiplicity=Multiplicity(1, 1)),
        Property(name="order_shippinginfo_19", type=order, multiplicity=Multiplicity(1, 1))
    }
)
order_Payment: BinaryAssociation = BinaryAssociation(
    name="order_Payment",
    ends={
        Property(name="payment10", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order11", type=order, multiplicity=Multiplicity(0, 1))
    }
)
cartitem_product: BinaryAssociation = BinaryAssociation(
    name="cartitem_product",
    ends={
        Property(name="product212", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="cartitem13", type=cartitem, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5sV_IOacEemBQOlXnGuUXA",
    types={Login, User, ShoppingCart, cartitem, product, orderDetail, order, shippinginfo, Payment, login_status},
    associations={ShoppingCart_coustomer, ShoppingCart_cartitem, coustomer_order, order_orderDetail, order_shippinginfo, order_Payment, cartitem_product},
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
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
Models_ShippingType: Enumeration = Enumeration(
    name="Models_ShippingType",
    literals={
            
    }
)

Models_ShoppingCartStatus: Enumeration = Enumeration(
    name="Models_ShoppingCartStatus",
    literals={
            
    }
)

Models_OrderStatus: Enumeration = Enumeration(
    name="Models_OrderStatus",
    literals={
            
    }
)

# Classes
dao_ProductDao_Interface = Class(name="dao_ProductDao_Interface")
dao_CustomerDao_Interface = Class(name="dao_CustomerDao_Interface")
dao_LineItemDao_Interface = Class(name="dao_LineItemDao_Interface")
dao_ShippingInfoDao_Interface = Class(name="dao_ShippingInfoDao_Interface")
dao_CartItemDao_Interface = Class(name="dao_CartItemDao_Interface")
dao_OrderDao_Interface = Class(name="dao_OrderDao_Interface")
dao_ShoppingCartDao_Interface = Class(name="dao_ShoppingCartDao_Interface")
Models_ShoppingCart = Class(name="Models_ShoppingCart")
Models_Customer = Class(name="Models_Customer")
Models_LineItem = Class(name="Models_LineItem")
Models_Order = Class(name="Models_Order")
Models_User = Class(name="Models_User")
Models_LoginLog = Class(name="Models_LoginLog")
Models_Product = Class(name="Models_Product")
Models_cartItem = Class(name="Models_cartItem")
Models_ShippingInfo = Class(name="Models_ShippingInfo")
Controllers_ShoppingCartController = Class(name="Controllers_ShoppingCartController")
Controllers_OrderController = Class(name="Controllers_OrderController")
Controllers_ProductController = Class(name="Controllers_ProductController")

# dao_ProductDao_Interface class attributes and methods

# dao_CustomerDao_Interface class attributes and methods

# dao_LineItemDao_Interface class attributes and methods

# dao_ShippingInfoDao_Interface class attributes and methods

# dao_CartItemDao_Interface class attributes and methods

# dao_OrderDao_Interface class attributes and methods

# dao_ShoppingCartDao_Interface class attributes and methods

# Models_ShoppingCart class attributes and methods
Models_ShoppingCart_cartId: Property = Property(name="cartId", type=IntegerType)
Models_ShoppingCart_customerId: Property = Property(name="customerId", type=IntegerType)
Models_ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
Models_ShoppingCart_status: Property = Property(name="status", type=IntegerType)
Models_ShoppingCart_deleted: Property = Property(name="deleted", type=BooleanType)
Models_ShoppingCart.attributes={Models_ShoppingCart_status, Models_ShoppingCart_cartId, Models_ShoppingCart_dateAdded, Models_ShoppingCart_customerId, Models_ShoppingCart_deleted}

# Models_Customer class attributes and methods
Models_Customer_coustomername: Property = Property(name="coustomername", type=StringType)
Models_Customer_address: Property = Property(name="address", type=StringType)
Models_Customer_phoneno: Property = Property(name="phoneno", type=IntegerType)
Models_Customer_creditcardinfo: Property = Property(name="creditcardinfo", type=StringType)
Models_Customer_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
Models_Customer_deleted: Property = Property(name="deleted", type=BooleanType)
Models_Customer.attributes={Models_Customer_address, Models_Customer_phoneno, Models_Customer_creditcardinfo, Models_Customer_shippinginfo, Models_Customer_deleted, Models_Customer_coustomername}

# Models_LineItem class attributes and methods
Models_LineItem_orderId: Property = Property(name="orderId", type=IntegerType)
Models_LineItem_productid: Property = Property(name="productid", type=IntegerType)
Models_LineItem_productname: Property = Property(name="productname", type=StringType)
Models_LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
Models_LineItem_unitcost: Property = Property(name="unitcost", type=FloatType)
Models_LineItem_subtotal: Property = Property(name="subtotal", type=FloatType)
Models_LineItem.attributes={Models_LineItem_productid, Models_LineItem_subtotal, Models_LineItem_unitcost, Models_LineItem_productname, Models_LineItem_orderId, Models_LineItem_quantity}

# Models_Order class attributes and methods
Models_Order_orderID: Property = Property(name="orderID", type=IntegerType)
Models_Order_dateCreated: Property = Property(name="dateCreated", type=DateType)
Models_Order_dateShipped: Property = Property(name="dateShipped", type=StringType)
Models_Order_customerid: Property = Property(name="customerid", type=IntegerType)
Models_Order_status: Property = Property(name="status", type=StringType)
Models_Order_shippingInfoId: Property = Property(name="shippingInfoId", type=IntegerType)
Models_Order.attributes={Models_Order_orderID, Models_Order_shippingInfoId, Models_Order_dateShipped, Models_Order_status, Models_Order_dateCreated, Models_Order_customerid}

# Models_User class attributes and methods
Models_User_UserId: Property = Property(name="UserId", type=StringType)
Models_User_password: Property = Property(name="password", type=StringType)
Models_User_email: Property = Property(name="email", type=StringType)
Models_User.attributes={Models_User_email, Models_User_UserId, Models_User_password}

# Models_LoginLog class attributes and methods
Models_LoginLog_id: Property = Property(name="id", type=IntegerType)
Models_LoginLog_user_id: Property = Property(name="user_id", type=IntegerType)
Models_LoginLog_isLogin: Property = Property(name="isLogin", type=BooleanType)
Models_LoginLog_lastLoginDate: Property = Property(name="lastLoginDate", type=DateType)
Models_LoginLog.attributes={Models_LoginLog_lastLoginDate, Models_LoginLog_isLogin, Models_LoginLog_id, Models_LoginLog_user_id}

# Models_Product class attributes and methods
Models_Product_productid: Property = Property(name="productid", type=IntegerType)
Models_Product_productname: Property = Property(name="productname", type=StringType)
Models_Product_price: Property = Property(name="price", type=FloatType)
Models_Product_imagefilename: Property = Property(name="imagefilename", type=StringType)
Models_Product_quantity: Property = Property(name="quantity", type=IntegerType)
Models_Product.attributes={Models_Product_quantity, Models_Product_imagefilename, Models_Product_productname, Models_Product_price, Models_Product_productid}

# Models_cartItem class attributes and methods
Models_cartItem_name: Property = Property(name="name", type=StringType)
Models_cartItem_cartId: Property = Property(name="cartId", type=IntegerType)
Models_cartItem_quantity: Property = Property(name="quantity", type=IntegerType)
Models_cartItem_unitcost: Property = Property(name="unitcost", type=FloatType)
Models_cartItem_subtotal: Property = Property(name="subtotal", type=FloatType)
Models_cartItem_deleted: Property = Property(name="deleted", type=BooleanType)
Models_cartItem.attributes={Models_cartItem_subtotal, Models_cartItem_cartId, Models_cartItem_unitcost, Models_cartItem_name, Models_cartItem_deleted, Models_cartItem_quantity}

# Models_ShippingInfo class attributes and methods
Models_ShippingInfo_shippingid: Property = Property(name="shippingid", type=IntegerType)
Models_ShippingInfo_shippingtype: Property = Property(name="shippingtype", type=StringType)
Models_ShippingInfo_shippingcost: Property = Property(name="shippingcost", type=IntegerType)
Models_ShippingInfo_shippingregionid: Property = Property(name="shippingregionid", type=IntegerType)
Models_ShippingInfo.attributes={Models_ShippingInfo_shippingcost, Models_ShippingInfo_shippingid, Models_ShippingInfo_shippingregionid, Models_ShippingInfo_shippingtype}

# Controllers_ShoppingCartController class attributes and methods

# Controllers_OrderController class attributes and methods

# Controllers_ProductController class attributes and methods

# Relationships
coustomer_order: BinaryAssociation = BinaryAssociation(
    name="coustomer_order",
    ends={
        Property(name="coustomer_order_012", type=Models_Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="coustomer_order_113", type=Models_Customer, multiplicity=Multiplicity(1, 1))
    }
)
order_orderDetail: BinaryAssociation = BinaryAssociation(
    name="order_orderDetail",
    ends={
        Property(name="order_orderDetail_014", type=Models_LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order_orderDetail_115", type=Models_Order, multiplicity=Multiplicity(1, 1))
    }
)
LoginLog_user: BinaryAssociation = BinaryAssociation(
    name="LoginLog_user",
    ends={
        Property(name="user16", type=Models_User, multiplicity=Multiplicity(0, 1)),
        Property(name="loginLog17", type=Models_LoginLog, multiplicity=Multiplicity(0, 1))
    }
)
orderDetail_ProLocal: BinaryAssociation = BinaryAssociation(
    name="orderDetail_ProLocal",
    ends={
        Property(name="orderDetail_ProLocal_018", type=Models_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetail_ProLocal_119", type=Models_LineItem, multiplicity=Multiplicity(1, 1))
    }
)
ShippingInfo_shippingInfo: BinaryAssociation = BinaryAssociation(
    name="ShippingInfo_shippingInfo",
    ends={
        Property(name="shippingInfo0", type=Models_ShippingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="shippingInfo1", type=dao_ShippingInfoDao_Interface, multiplicity=Multiplicity(1, 1))
    }
)
OrderDao_Order: BinaryAssociation = BinaryAssociation(
    name="OrderDao_Order",
    ends={
        Property(name="order2", type=Models_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDao3", type=dao_OrderDao_Interface, multiplicity=Multiplicity(1, 1))
    }
)
CartItemDao_cartItem: BinaryAssociation = BinaryAssociation(
    name="CartItemDao_cartItem",
    ends={
        Property(name="cartItem4", type=Models_cartItem, multiplicity=Multiplicity(1, 1)),
        Property(name="cartItemDao5", type=dao_CartItemDao_Interface, multiplicity=Multiplicity(1, 1))
    }
)
product_LineItemDao: BinaryAssociation = BinaryAssociation(
    name="product_LineItemDao",
    ends={
        Property(name="lineItemDao6", type=dao_LineItemDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="LineItem7", type=Models_LineItem, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_ShoppingCartDao: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_ShoppingCartDao",
    ends={
        Property(name="shoppingCartDao8", type=dao_ShoppingCartDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingCart9", type=Models_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_coustomer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_coustomer",
    ends={
        Property(name="ShoppingCart_coustomer_010", type=Models_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="ShoppingCart_coustomer_111", type=Models_ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_cartitem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_cartitem",
    ends={
        Property(name="ShoppingCart_cartitem_020", type=Models_cartItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="ShoppingCart_cartitem_121", type=Models_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
cartitem_ProLocal: BinaryAssociation = BinaryAssociation(
    name="cartitem_ProLocal",
    ends={
        Property(name="cartitem_ProLocal_022", type=Models_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="cartitem_ProLocal_123", type=Models_cartItem, multiplicity=Multiplicity(1, 9999))
    }
)
order_shippinginfo: BinaryAssociation = BinaryAssociation(
    name="order_shippinginfo",
    ends={
        Property(name="order_shippinginfo_024", type=Models_ShippingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="order_shippinginfo_125", type=Models_Order, multiplicity=Multiplicity(1, 1))
    }
)
product_ProductDao: BinaryAssociation = BinaryAssociation(
    name="product_ProductDao",
    ends={
        Property(name="productDao26", type=dao_ProductDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="product27", type=Models_Product, multiplicity=Multiplicity(1, 1))
    }
)
Customer_CustomerDao: BinaryAssociation = BinaryAssociation(
    name="Customer_CustomerDao",
    ends={
        Property(name="customerDao28", type=dao_CustomerDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="customer29", type=Models_Customer, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCartController_CartItemDao: BinaryAssociation = BinaryAssociation(
    name="ShoppingCartController_CartItemDao",
    ends={
        Property(name="cartItemDao30", type=dao_CartItemDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingCartController31", type=Controllers_ShoppingCartController, multiplicity=Multiplicity(1, 1))
    }
)
OrderController_OrderDao: BinaryAssociation = BinaryAssociation(
    name="OrderController_OrderDao",
    ends={
        Property(name="orderDao32", type=dao_OrderDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="orderController33", type=Controllers_OrderController, multiplicity=Multiplicity(1, 1))
    }
)
ProductController_ProductDao: BinaryAssociation = BinaryAssociation(
    name="ProductController_ProductDao",
    ends={
        Property(name="productDao34", type=dao_ProductDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="productController35", type=Controllers_ProductController, multiplicity=Multiplicity(1, 1))
    }
)
ProductController_ShoppingCartDao: BinaryAssociation = BinaryAssociation(
    name="ProductController_ShoppingCartDao",
    ends={
        Property(name="shoppingCartDao36", type=dao_ShoppingCartDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="productController37", type=Controllers_ProductController, multiplicity=Multiplicity(1, 1))
    }
)
OrderController_LineItemDao: BinaryAssociation = BinaryAssociation(
    name="OrderController_LineItemDao",
    ends={
        Property(name="lineItemDao38", type=dao_LineItemDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="orderController39", type=Controllers_OrderController, multiplicity=Multiplicity(1, 1))
    }
)
OrderController_ShippingInfoDao: BinaryAssociation = BinaryAssociation(
    name="OrderController_ShippingInfoDao",
    ends={
        Property(name="shippingInfoDao40", type=dao_ShippingInfoDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="orderController41", type=Controllers_OrderController, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCartController_OrderDao: BinaryAssociation = BinaryAssociation(
    name="ShoppingCartController_OrderDao",
    ends={
        Property(name="orderDao42", type=dao_OrderDao_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCartController43", type=Controllers_ShoppingCartController, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCartController_ShoppingCartDao: BinaryAssociation = BinaryAssociation(
    name="ShoppingCartController_ShoppingCartDao",
    ends={
        Property(name="shoppingCartDao44", type=dao_ShoppingCartDao_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingCartController45", type=Controllers_ShoppingCartController, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_86a0dcf9_1e0a_4418_97b3_657ea22699d8",
    types={dao_ProductDao_Interface, dao_CustomerDao_Interface, dao_LineItemDao_Interface, dao_ShippingInfoDao_Interface, dao_CartItemDao_Interface, dao_OrderDao_Interface, dao_ShoppingCartDao_Interface, Models_ShoppingCart, Models_Customer, Models_LineItem, Models_Order, Models_User, Models_LoginLog, Models_Product, Models_cartItem, Models_ShippingInfo, Controllers_ShoppingCartController, Controllers_OrderController, Controllers_ProductController, Models_ShippingType, Models_ShoppingCartStatus, Models_OrderStatus},
    associations={coustomer_order, order_orderDetail, LoginLog_user, orderDetail_ProLocal, ShippingInfo_shippingInfo, OrderDao_Order, CartItemDao_cartItem, product_LineItemDao, ShoppingCart_ShoppingCartDao, ShoppingCart_coustomer, ShoppingCart_cartitem, cartitem_ProLocal, order_shippinginfo, product_ProductDao, Customer_CustomerDao, ShoppingCartController_CartItemDao, OrderController_OrderDao, ProductController_ProductDao, ProductController_ShoppingCartDao, OrderController_LineItemDao, OrderController_ShippingInfoDao, ShoppingCartController_OrderDao, ShoppingCartController_ShoppingCartDao},
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
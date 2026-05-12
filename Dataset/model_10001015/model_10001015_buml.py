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
Guest = Class(name="Guest")
Customer = Class(name="Customer")
Product = Class(name="Product")
List_Product_ = Class(name="List_Product_")
Order = Class(name="Order")
WishList = Class(name="WishList")
ProductListHelper = Class(name="ProductListHelper")
ShippingInfo = Class(name="ShippingInfo")
Seller = Class(name="Seller")
PaymentFactory = Class(name="PaymentFactory")
DebitCardPayment = Class(name="DebitCardPayment")
CreditCardPayment = Class(name="CreditCardPayment")
Payment_Interface = Class(name="Payment_Interface")
Ornaments = Class(name="Ornaments")
Electronics = Class(name="Electronics")
Appliances = Class(name="Appliances")
Cart = Class(name="Cart")
User = Class(name="User")

# Guest class attributes and methods

# Customer class attributes and methods
Customer_user_name: Property = Property(name="user_name", type=StringType)
Customer_firstName: Property = Property(name="firstName", type=StringType)
Customer_lastName: Property = Property(name="lastName", type=StringType)
Customer_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Customer_address: Property = Property(name="address", type=StringType)
Customer.attributes={Customer_firstName, Customer_address, Customer_user_name, Customer_phoneNo, Customer_lastName}

# Product class attributes and methods
Product_productId: Property = Property(name="productId", type=IntegerType)
Product_productName: Property = Property(name="productName", type=StringType)
Product_price: Property = Property(name="price", type=IntegerType)
Product_image: Property = Property(name="image", type=StringType)
Product_sellerInfo: Property = Property(name="sellerInfo", type=Seller)
Product_description: Property = Property(name="description", type=StringType)
Product_rating: Property = Property(name="rating", type=IntegerType)
Product.attributes={Product_productId, Product_image, Product_productName, Product_price, Product_description, Product_sellerInfo, Product_rating}

# List_Product_ class attributes and methods

# Order class attributes and methods
Order_orderId: Property = Property(name="orderId", type=IntegerType)
Order_orderedOn: Property = Property(name="orderedOn", type=StringType)
Order_status: Property = Property(name="status", type=StringType)
Order_shippingId: Property = Property(name="shippingId", type=IntegerType)
Order_noOfItem: Property = Property(name="noOfItem", type=IntegerType)
Order_orderTotalAmount: Property = Property(name="orderTotalAmount", type=IntegerType)
Order_deliveryDate: Property = Property(name="deliveryDate", type=IntegerType)
Order_items: Property = Property(name="items", type=List_Product_)
Order.attributes={Order_shippingId, Order_status, Order_deliveryDate, Order_orderId, Order_orderTotalAmount, Order_items, Order_noOfItem, Order_orderedOn}

# WishList class attributes and methods

# ProductListHelper class attributes and methods

# ShippingInfo class attributes and methods
ShippingInfo_deliveryAddress: Property = Property(name="deliveryAddress", type=StringType)
ShippingInfo_deliveryType: Property = Property(name="deliveryType", type=StringType)
ShippingInfo_estimatedDeliveryDate: Property = Property(name="estimatedDeliveryDate", type=StringType)
ShippingInfo_shippingCharges: Property = Property(name="shippingCharges", type=IntegerType)
ShippingInfo.attributes={ShippingInfo_deliveryType, ShippingInfo_shippingCharges, ShippingInfo_estimatedDeliveryDate, ShippingInfo_deliveryAddress}

# Seller class attributes and methods
Seller_name: Property = Property(name="name", type=StringType)
Seller_sellerId: Property = Property(name="sellerId", type=StringType)
Seller_rating: Property = Property(name="rating", type=StringType)
Seller.attributes={Seller_rating, Seller_sellerId, Seller_name}

# PaymentFactory class attributes and methods

# DebitCardPayment class attributes and methods

# CreditCardPayment class attributes and methods

# Payment_Interface class attributes and methods

# Ornaments class attributes and methods
Ornaments_Name: Property = Property(name="Name", type=StringType)
Ornaments.attributes={Ornaments_Name}

# Electronics class attributes and methods

# Appliances class attributes and methods

# Cart class attributes and methods

# User class attributes and methods
User_userId: Property = Property(name="userId", type=IntegerType)
User.attributes={User_userId}

# Relationships
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Order_ShippingInfo: BinaryAssociation = BinaryAssociation(
    name="Order_ShippingInfo",
    ends={
        Property(name="shippingInfo2", type=ShippingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
User_Product: BinaryAssociation = BinaryAssociation(
    name="User_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Product_Seller: BinaryAssociation = BinaryAssociation(
    name="Product_Seller",
    ends={
        Property(name="seller6", type=Seller, multiplicity=Multiplicity(1, 1)),
        Property(name="product7", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_Order: BinaryAssociation = BinaryAssociation(
    name="Product_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="product9", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Cart",
    ends={
        Property(name="cart10", type=Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_WishList: BinaryAssociation = BinaryAssociation(
    name="Customer_WishList",
    ends={
        Property(name="wishList12", type=WishList, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Cart_ProductListHelper: BinaryAssociation = BinaryAssociation(
    name="Cart_ProductListHelper",
    ends={
        Property(name="productListHelper14", type=ProductListHelper, multiplicity=Multiplicity(0, 1)),
        Property(name="cart15", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
WishList_ProductListHelper: BinaryAssociation = BinaryAssociation(
    name="WishList_ProductListHelper",
    ends={
        Property(name="productListHelper16", type=ProductListHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="wishList17", type=WishList, multiplicity=Multiplicity(0, 1))
    }
)
Product_WishList: BinaryAssociation = BinaryAssociation(
    name="Product_WishList",
    ends={
        Property(name="wishList18", type=WishList, multiplicity=Multiplicity(1, 1)),
        Property(name="product19", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_Cart: BinaryAssociation = BinaryAssociation(
    name="Product_Cart",
    ends={
        Property(name="cart20", type=Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="product21", type=Product, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7b2c1540_0556_4a82_8fda_f789e73d6d1e",
    types={Guest, Customer, Product, List_Product_, Order, WishList, ProductListHelper, ShippingInfo, Seller, PaymentFactory, DebitCardPayment, CreditCardPayment, Payment_Interface, Ornaments, Electronics, Appliances, Cart, User},
    associations={Customer_Order, Order_ShippingInfo, User_Product, Product_Seller, Product_Order, Customer_Cart, Customer_WishList, Cart_ProductListHelper, WishList_ProductListHelper, Product_WishList, Product_Cart},
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
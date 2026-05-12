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
mobile_Interface = Class(name="mobile_Interface")
shiporder_Interface = Class(name="shiporder_Interface")
pickuppoint_Interface = Class(name="pickuppoint_Interface")
customeraddress_Interface = Class(name="customeraddress_Interface")
promotions = Class(name="promotions")
payment_Interface = Class(name="payment_Interface")
billdesk_Interface = Class(name="billdesk_Interface")
Credit_DebitCard = Class(name="Credit_DebitCard")
gpay_Interface = Class(name="gpay_Interface")
Class_ = Class(name="Class")
paylater_Interface = Class(name="paylater_Interface")
EmailNotification = Class(name="EmailNotification")
PushNotification = Class(name="PushNotification")
Credit_DebitCard1 = Class(name="Credit_DebitCard1")
Gpay = Class(name="Gpay")
PayLater = Class(name="PayLater")
Category = Class(name="Category")
Class1 = Class(name="Class1")
Class2 = Class(name="Class2")
Offer_Interface = Class(name="Offer_Interface")
ProductDiscount = Class(name="ProductDiscount")
TimeBasedDiscount = Class(name="TimeBasedDiscount")
Price = Class(name="Price")
Item = Class(name="Item")
OrderService = Class(name="OrderService")
Payment = Class(name="Payment")
Payment_Interface = Class(name="Payment_Interface")
CreditCardPayment = Class(name="CreditCardPayment")
PayLater1 = Class(name="PayLater1")
ShippingType_Interface = Class(name="ShippingType_Interface")
Vendor = Class(name="Vendor")
ShoppingCart = Class(name="ShoppingCart")
Address = Class(name="Address")
Notify_Interface = Class(name="Notify_Interface")
SMS = Class(name="SMS")
email = Class(name="email")
User = Class(name="User")
SessionManager = Class(name="SessionManager")
Customer = Class(name="Customer")
Administrator = Class(name="Administrator")
Department = Class(name="Department")
searchFacade = Class(name="searchFacade")
Order = Class(name="Order")
Shipping = Class(name="Shipping")
OrderDetail = Class(name="OrderDetail")
Product = Class(name="Product")
keywordSet = Class(name="keywordSet")
cartItem = Class(name="cartItem")
notify_Interface = Class(name="notify_Interface")
email_Interface = Class(name="email_Interface")

# mobile_Interface class attributes and methods

# shiporder_Interface class attributes and methods

# pickuppoint_Interface class attributes and methods

# customeraddress_Interface class attributes and methods

# promotions class attributes and methods
promotions_promotionCode: Property = Property(name="promotionCode", type=StringType)
promotions_startDate: Property = Property(name="startDate", type=IntegerType)
promotions_endDate: Property = Property(name="endDate", type=IntegerType)
promotions.attributes={promotions_startDate, promotions_promotionCode, promotions_endDate}

# payment_Interface class attributes and methods

# billdesk_Interface class attributes and methods

# Credit_DebitCard class attributes and methods

# gpay_Interface class attributes and methods

# Class class attributes and methods

# paylater_Interface class attributes and methods

# EmailNotification class attributes and methods

# PushNotification class attributes and methods

# Credit_DebitCard1 class attributes and methods

# Gpay class attributes and methods

# PayLater class attributes and methods

# Category class attributes and methods
Category_description: Property = Property(name="description", type=StringType)
Category_categoryID: Property = Property(name="categoryID", type=IntegerType)
Category_categoryName: Property = Property(name="categoryName", type=StringType)
Category_departmentId: Property = Property(name="departmentId", type=IntegerType)
Category.attributes={Category_categoryName, Category_departmentId, Category_categoryID, Category_description}

# Class1 class attributes and methods

# Class2 class attributes and methods

# Offer_Interface class attributes and methods

# ProductDiscount class attributes and methods

# TimeBasedDiscount class attributes and methods

# Price class attributes and methods
Price_ActualPrice: Property = Property(name="ActualPrice", type=StringType)
Price.attributes={Price_ActualPrice}

# Item class attributes and methods
Item_Name: Property = Property(name="Name", type=StringType)
Item_Quantity: Property = Property(name="Quantity", type=IntegerType)
Item_attribute: Property = Property(name="attribute", type=StringType)
Item.attributes={Item_attribute, Item_Quantity, Item_Name}

# OrderService class attributes and methods
OrderService_attribute: Property = Property(name="attribute", type=StringType)
OrderService.attributes={OrderService_attribute}

# Payment class attributes and methods

# Payment_Interface class attributes and methods

# CreditCardPayment class attributes and methods
CreditCardPayment_CardType: Property = Property(name="CardType", type=StringType)
CreditCardPayment_CardNumber: Property = Property(name="CardNumber", type=IntegerType)
CreditCardPayment.attributes={CreditCardPayment_CardType, CreditCardPayment_CardNumber}

# PayLater1 class attributes and methods
PayLater1_UserID: Property = Property(name="UserID", type=StringType)
PayLater1.attributes={PayLater1_UserID}

# ShippingType_Interface class attributes and methods

# Vendor class attributes and methods
Vendor_attribute: Property = Property(name="attribute", type=StringType)
Vendor_attribute2: Property = Property(name="attribute2", type=StringType)
Vendor.attributes={Vendor_attribute2, Vendor_attribute}

# ShoppingCart class attributes and methods
ShoppingCart_Item: Property = Property(name="Item", type=StringType)
ShoppingCart_GetTotalPrice: Property = Property(name="GetTotalPrice", type=StringType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_dateAdded, ShoppingCart_Item, ShoppingCart_GetTotalPrice, ShoppingCart_quantity}

# Address class attributes and methods
Address_Street: Property = Property(name="Street", type=StringType)
Address_City: Property = Property(name="City", type=StringType)
Address_State: Property = Property(name="State", type=StringType)
Address_ZipCode: Property = Property(name="ZipCode", type=StringType)
Address_Country: Property = Property(name="Country", type=StringType)
Address_Type: Property = Property(name="Type", type=StringType)
Address.attributes={Address_State, Address_ZipCode, Address_City, Address_Country, Address_Street, Address_Type}

# Notify_Interface class attributes and methods

# SMS class attributes and methods
SMS_MobileNo: Property = Property(name="MobileNo", type=IntegerType)
SMS.attributes={SMS_MobileNo}

# email class attributes and methods
email_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
email.attributes={email_EmailAddress}

# User class attributes and methods
User_userId: Property = Property(name="userId", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User.attributes={User_userId, User_loginStatus, User_password}

# SessionManager class attributes and methods
SessionManager_userid: Property = Property(name="userid", type=StringType)
SessionManager_departmentName: Property = Property(name="departmentName", type=StringType)
SessionManager.attributes={SessionManager_userid, SessionManager_departmentName}

# Customer class attributes and methods
Customer_customerName: Property = Property(name="customerName", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_phoneno: Property = Property(name="phoneno", type=IntegerType)
Customer_creditcardinfo: Property = Property(name="creditcardinfo", type=StringType)
Customer_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
Customer_newsLettersub: Property = Property(name="newsLettersub", type=BooleanType)
Customer_surveys: Property = Property(name="surveys", type=BooleanType)
Customer.attributes={Customer_creditcardinfo, Customer_surveys, Customer_address, Customer_email, Customer_newsLettersub, Customer_customerName, Customer_shippinginfo, Customer_phoneno}

# Administrator class attributes and methods
Administrator_adminName: Property = Property(name="adminName", type=StringType)
Administrator_email: Property = Property(name="email", type=StringType)
Administrator.attributes={Administrator_email, Administrator_adminName}

# Department class attributes and methods
Department_departmentID: Property = Property(name="departmentID", type=IntegerType)
Department_departmentName: Property = Property(name="departmentName", type=StringType)
Department_description: Property = Property(name="description", type=StringType)
Department.attributes={Department_departmentID, Department_departmentName, Department_description}

# searchFacade class attributes and methods

# Order class attributes and methods
Order_OrderId: Property = Property(name="OrderId", type=IntegerType)
Order_Item: Property = Property(name="Item", type=StringType)
Order_dateCreated: Property = Property(name="dateCreated", type=StringType)
Order_dateShipped: Property = Property(name="dateShipped", type=StringType)
Order_customerName: Property = Property(name="customerName", type=StringType)
Order_status: Property = Property(name="status", type=StringType)
Order_customerId: Property = Property(name="customerId", type=StringType)
Order_ShippingAddress: Property = Property(name="ShippingAddress", type=StringType)
Order_BillingAddress: Property = Property(name="BillingAddress", type=StringType)
Order_OrderStatus: Property = Property(name="OrderStatus", type=StringType)
Order_Payment: Property = Property(name="Payment", type=StringType)
Order.attributes={Order_dateShipped, Order_status, Order_OrderStatus, Order_customerId, Order_BillingAddress, Order_dateCreated, Order_Item, Order_OrderId, Order_ShippingAddress, Order_customerName, Order_Payment}

# Shipping class attributes and methods
Shipping_shippingId: Property = Property(name="shippingId", type=IntegerType)
Shipping_shippingType: Property = Property(name="shippingType", type=StringType)
Shipping_shippingAddress: Property = Property(name="shippingAddress", type=StringType)
Shipping__attr: Property = Property(name="_attr", type=IntegerType)
Shipping_ShippingType: Property = Property(name="ShippingType", type=StringType)
Shipping.attributes={Shipping_shippingAddress, Shipping_shippingType, Shipping__attr, Shipping_shippingId, Shipping_ShippingType}

# OrderDetail class attributes and methods
OrderDetail_orderId: Property = Property(name="orderId", type=IntegerType)
OrderDetail_productId: Property = Property(name="productId", type=IntegerType)
OrderDetail_productName: Property = Property(name="productName", type=StringType)
OrderDetail_quantity: Property = Property(name="quantity", type=IntegerType)
OrderDetail_unitCost: Property = Property(name="unitCost", type=StringType)
OrderDetail_subTotal: Property = Property(name="subTotal", type=StringType)
OrderDetail.attributes={OrderDetail_subTotal, OrderDetail_orderId, OrderDetail_productId, OrderDetail_quantity, OrderDetail_productName, OrderDetail_unitCost}

# Product class attributes and methods
Product_productId: Property = Property(name="productId", type=IntegerType)
Product_Name: Property = Property(name="Name", type=StringType)
Product_SKU: Property = Property(name="SKU", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_attribute5: Property = Property(name="attribute5", type=StringType)
Product_attribute6: Property = Property(name="attribute6", type=StringType)
Product_attribute7: Property = Property(name="attribute7", type=StringType)
Product_Price: Property = Property(name="Price", type=StringType)
Product_reviews: Property = Property(name="reviews", type=StringType)
Product.attributes={Product_Name, Product_reviews, Product_attribute7, Product_attribute6, Product_productId, Product_attribute5, Product_description, Product_SKU, Product_Price}

# keywordSet class attributes and methods
keywordSet_keyword: Property = Property(name="keyword", type=StringType)
keywordSet.attributes={keywordSet_keyword}

# cartItem class attributes and methods
cartItem_name: Property = Property(name="name", type=StringType)
cartItem_productId: Property = Property(name="productId", type=IntegerType)
cartItem_quantity: Property = Property(name="quantity", type=IntegerType)
cartItem_unitCost: Property = Property(name="unitCost", type=StringType)
cartItem_subtotal: Property = Property(name="subtotal", type=StringType)
cartItem.attributes={cartItem_subtotal, cartItem_unitCost, cartItem_quantity, cartItem_productId, cartItem_name}

# notify_Interface class attributes and methods

# email_Interface class attributes and methods

# Relationships
SessionManager_User: BinaryAssociation = BinaryAssociation(
    name="SessionManager_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="sessionManager1", type=SessionManager, multiplicity=Multiplicity(0, 1))
    }
)
Cart_Cart: BinaryAssociation = BinaryAssociation(
    name="Cart_Cart",
    ends={
        Property(name="cart2", type=cartItem, multiplicity=Multiplicity(0, 1)),
        Property(name="cart3", type=cartItem, multiplicity=Multiplicity(0, 1))
    }
)
Genre_Genre: BinaryAssociation = BinaryAssociation(
    name="Genre_Genre",
    ends={
        Property(name="genre4", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="genre5", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Genre_Product: BinaryAssociation = BinaryAssociation(
    name="Genre_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="genre7", type=Category, multiplicity=Multiplicity(0, 1))
    }
)
SessionManager_Genre: BinaryAssociation = BinaryAssociation(
    name="SessionManager_Genre",
    ends={
        Property(name="genre8", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="sessionManager9", type=SessionManager, multiplicity=Multiplicity(0, 1))
    }
)
Order_Shippinginfo: BinaryAssociation = BinaryAssociation(
    name="Order_Shippinginfo",
    ends={
        Property(name="Order_Shippinginfo_010", type=Shipping, multiplicity=Multiplicity(0, 1)),
        Property(name="Order_Shippinginfo_111", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_OrderDetail: BinaryAssociation = BinaryAssociation(
    name="Order_OrderDetail",
    ends={
        Property(name="orderDetail12", type=OrderDetail, multiplicity=Multiplicity(0, 1)),
        Property(name="order13", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Order: BinaryAssociation = BinaryAssociation(
    name="Administrator_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Product_OrderDetail: BinaryAssociation = BinaryAssociation(
    name="Product_OrderDetail",
    ends={
        Property(name="orderDetail18", type=OrderDetail, multiplicity=Multiplicity(0, 1)),
        Property(name="product19", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_cartItem: BinaryAssociation = BinaryAssociation(
    name="Product_cartItem",
    ends={
        Property(name="cartItem20", type=cartItem, multiplicity=Multiplicity(0, 1)),
        Property(name="product21", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
searchFacade_keywordSet: BinaryAssociation = BinaryAssociation(
    name="searchFacade_keywordSet",
    ends={
        Property(name="keywordSet22", type=keywordSet, multiplicity=Multiplicity(0, 1)),
        Property(name="searchFacade23", type=searchFacade, multiplicity=Multiplicity(0, 1))
    }
)
keywordSet_Product: BinaryAssociation = BinaryAssociation(
    name="keywordSet_Product",
    ends={
        Property(name="product24", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="keywordSet25", type=keywordSet, multiplicity=Multiplicity(0, 1))
    }
)
notify_email: BinaryAssociation = BinaryAssociation(
    name="notify_email",
    ends={
        Property(name="email226", type=email_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="notify27", type=notify_Interface, multiplicity=Multiplicity(0, 1))
    }
)
notify_mobile: BinaryAssociation = BinaryAssociation(
    name="notify_mobile",
    ends={
        Property(name="mobile228", type=mobile_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="notify29", type=notify_Interface, multiplicity=Multiplicity(0, 1))
    }
)
shiporder_pickuppoint: BinaryAssociation = BinaryAssociation(
    name="shiporder_pickuppoint",
    ends={
        Property(name="pickuppoint30", type=pickuppoint_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="shiporder31", type=shiporder_Interface, multiplicity=Multiplicity(0, 1))
    }
)
PayLater_payment: BinaryAssociation = BinaryAssociation(
    name="PayLater_payment",
    ends={
        Property(name="payment50", type=payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="payLater51", type=PayLater, multiplicity=Multiplicity(0, 1))
    }
)
Department_Department: BinaryAssociation = BinaryAssociation(
    name="Department_Department",
    ends={
        Property(name="department52", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="department53", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Category: BinaryAssociation = BinaryAssociation(
    name="Department_Category",
    ends={
        Property(name="category54", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="department55", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Price_Price: BinaryAssociation = BinaryAssociation(
    name="Price_Price",
    ends={
        Property(name="price56", type=Price, multiplicity=Multiplicity(0, 1)),
        Property(name="price57", type=Price, multiplicity=Multiplicity(0, 1))
    }
)
Product_Offer: BinaryAssociation = BinaryAssociation(
    name="Product_Offer",
    ends={
        Property(name="offer58", type=Offer_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="product59", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_Price: BinaryAssociation = BinaryAssociation(
    name="Product_Price",
    ends={
        Property(name="price60", type=Price, multiplicity=Multiplicity(0, 1)),
        Property(name="product61", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Item_Product: BinaryAssociation = BinaryAssociation(
    name="Item_Product",
    ends={
        Property(name="product62", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="item63", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
OrderService_Order: BinaryAssociation = BinaryAssociation(
    name="OrderService_Order",
    ends={
        Property(name="order64", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="orderService65", type=OrderService, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment66", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order67", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment2: BinaryAssociation = BinaryAssociation(
    name="Order_Payment2",
    ends={
        Property(name="payment68", type=Payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="order69", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
ShippingType_ShippingType: BinaryAssociation = BinaryAssociation(
    name="ShippingType_ShippingType",
    ends={
        Property(name="shippingType70", type=ShippingType_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="shippingType71", type=ShippingType_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Shipping_ShippingType: BinaryAssociation = BinaryAssociation(
    name="Shipping_ShippingType",
    ends={
        Property(name="shippingType272", type=ShippingType_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="shipping73", type=Shipping, multiplicity=Multiplicity(0, 1))
    }
)
Order_Shipping: BinaryAssociation = BinaryAssociation(
    name="Order_Shipping",
    ends={
        Property(name="shipping74", type=Shipping, multiplicity=Multiplicity(0, 1)),
        Property(name="order75", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Item_Order: BinaryAssociation = BinaryAssociation(
    name="Item_Order",
    ends={
        Property(name="order76", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="item77", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_Item: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Item",
    ends={
        Property(name="item78", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart79", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
Order_Address: BinaryAssociation = BinaryAssociation(
    name="Order_Address",
    ends={
        Property(name="address80", type=Address, multiplicity=Multiplicity(0, 1)),
        Property(name="order81", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
OrderService_Notify: BinaryAssociation = BinaryAssociation(
    name="OrderService_Notify",
    ends={
        Property(name="notify82", type=Notify_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="orderService83", type=OrderService, multiplicity=Multiplicity(0, 1))
    }
)
shiporder_customeraddress: BinaryAssociation = BinaryAssociation(
    name="shiporder_customeraddress",
    ends={
        Property(name="customeraddress32", type=customeraddress_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="shiporder33", type=shiporder_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Customer_promotions: BinaryAssociation = BinaryAssociation(
    name="Customer_promotions",
    ends={
        Property(name="promotions34", type=promotions, multiplicity=Multiplicity(0, 1)),
        Property(name="customer35", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
billdesk_payment: BinaryAssociation = BinaryAssociation(
    name="billdesk_payment",
    ends={
        Property(name="payment36", type=payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="billdesk37", type=billdesk_Interface, multiplicity=Multiplicity(0, 1))
    }
)
payment_gpay: BinaryAssociation = BinaryAssociation(
    name="payment_gpay",
    ends={
        Property(name="gpay38", type=gpay_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="payment39", type=payment_Interface, multiplicity=Multiplicity(0, 1))
    }
)
payment_paylater: BinaryAssociation = BinaryAssociation(
    name="payment_paylater",
    ends={
        Property(name="paylater40", type=paylater_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="payment41", type=payment_Interface, multiplicity=Multiplicity(0, 1))
    }
)
EmailNotification_notify: BinaryAssociation = BinaryAssociation(
    name="EmailNotification_notify",
    ends={
        Property(name="notify42", type=notify_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="emailNotification43", type=EmailNotification, multiplicity=Multiplicity(0, 1))
    }
)
PushNotification_notify: BinaryAssociation = BinaryAssociation(
    name="PushNotification_notify",
    ends={
        Property(name="notify44", type=notify_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="pushNotification45", type=PushNotification, multiplicity=Multiplicity(0, 1))
    }
)
Credit_DebitCard_payment: BinaryAssociation = BinaryAssociation(
    name="Credit_DebitCard_payment",
    ends={
        Property(name="payment46", type=payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="credit_DebitCard47", type=Credit_DebitCard1, multiplicity=Multiplicity(0, 1))
    }
)
Gpay_payment: BinaryAssociation = BinaryAssociation(
    name="Gpay_payment",
    ends={
        Property(name="payment48", type=payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="gpay49", type=Gpay, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_XP20kPO9EemTHo7LQdQL6Q",
    types={mobile_Interface, shiporder_Interface, pickuppoint_Interface, customeraddress_Interface, promotions, payment_Interface, billdesk_Interface, Credit_DebitCard, gpay_Interface, Class_, paylater_Interface, EmailNotification, PushNotification, Credit_DebitCard1, Gpay, PayLater, Category, Class1, Class2, Offer_Interface, ProductDiscount, TimeBasedDiscount, Price, Item, OrderService, Payment, Payment_Interface, CreditCardPayment, PayLater1, ShippingType_Interface, Vendor, ShoppingCart, Address, Notify_Interface, SMS, email, User, SessionManager, Customer, Administrator, Department, searchFacade, Order, Shipping, OrderDetail, Product, keywordSet, cartItem, notify_Interface, email_Interface},
    associations={SessionManager_User, Cart_Cart, Genre_Genre, Genre_Product, SessionManager_Genre, Order_Shippinginfo, Order_OrderDetail, Customer_Order, Administrator_Order, Product_OrderDetail, Product_cartItem, searchFacade_keywordSet, keywordSet_Product, notify_email, notify_mobile, shiporder_pickuppoint, PayLater_payment, Department_Department, Department_Category, Price_Price, Product_Offer, Product_Price, Item_Product, OrderService_Order, Order_Payment, Order_Payment2, ShippingType_ShippingType, Shipping_ShippingType, Order_Shipping, Item_Order, ShoppingCart_Item, Order_Address, OrderService_Notify, shiporder_customeraddress, Customer_promotions, billdesk_payment, payment_gpay, payment_paylater, EmailNotification_notify, PushNotification_notify, Credit_DebitCard_payment, Gpay_payment},
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
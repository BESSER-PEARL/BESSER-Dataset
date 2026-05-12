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
Admin = Class(name="Admin")
Shopping_Cart = Class(name="Shopping_Cart")
Search = Class(name="Search")
BookSet = Class(name="BookSet")
Order = Class(name="Order")
Bookstore_Shop = Class(name="Bookstore_Shop")
Payment = Class(name="Payment")
User = Class(name="User")
Customer = Class(name="Customer")

# Admin class attributes and methods
Admin_adminId: Property = Property(name="adminId", type=IntegerType)
Admin_adminPassword: Property = Property(name="adminPassword", type=StringType)
Admin_adminName: Property = Property(name="adminName", type=StringType)
Admin_adminRmail: Property = Property(name="adminRmail", type=StringType)
Admin.attributes={Admin_adminPassword, Admin_adminId, Admin_adminName, Admin_adminRmail}

# Shopping_Cart class attributes and methods
Shopping_Cart_orderId: Property = Property(name="orderId", type=IntegerType)
Shopping_Cart_price: Property = Property(name="price", type=StringType)
Shopping_Cart_customerId: Property = Property(name="customerId", type=Customer)
Shopping_Cart.attributes={Shopping_Cart_customerId, Shopping_Cart_price, Shopping_Cart_orderId}

# Search class attributes and methods
Search_bookTitle: Property = Property(name="bookTitle", type=StringType)
Search_authorName: Property = Property(name="authorName", type=StringType)
Search_priceLimit: Property = Property(name="priceLimit", type=StringType)
Search.attributes={Search_priceLimit, Search_authorName, Search_bookTitle}

# BookSet class attributes and methods
BookSet_bookIsbn: Property = Property(name="bookIsbn", type=IntegerType)
BookSet_bookTitle: Property = Property(name="bookTitle", type=StringType)
BookSet.attributes={BookSet_bookTitle, BookSet_bookIsbn}

# Order class attributes and methods
Order_orderId: Property = Property(name="orderId", type=IntegerType)
Order_price: Property = Property(name="price", type=StringType)
Order_customerId: Property = Property(name="customerId", type=IntegerType)
Order_NumberOfBooks: Property = Property(name="NumberOfBooks", type=IntegerType)
Order.attributes={Order_customerId, Order_price, Order_orderId, Order_NumberOfBooks}

# Bookstore_Shop class attributes and methods
Bookstore_Shop_User: Property = Property(name="User", type=User)
Bookstore_Shop_Admin: Property = Property(name="Admin", type=Admin)
Bookstore_Shop.attributes={Bookstore_Shop_User, Bookstore_Shop_Admin}

# Payment class attributes and methods
Payment_paymentId: Property = Property(name="paymentId", type=IntegerType)
Payment_paymentTotal: Property = Property(name="paymentTotal", type=StringType)
Payment.attributes={Payment_paymentTotal, Payment_paymentId}

# User class attributes and methods
User_userId: Property = Property(name="userId", type=IntegerType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_userId}

# Customer class attributes and methods
Customer_customerId: Property = Property(name="customerId", type=IntegerType)
Customer_customerName: Property = Property(name="customerName", type=StringType)
Customer_customerAddress: Property = Property(name="customerAddress", type=StringType)
Customer_customerPhone: Property = Property(name="customerPhone", type=IntegerType)
Customer_customerPaymentInfo: Property = Property(name="customerPaymentInfo", type=StringType)
Customer.attributes={Customer_customerPaymentInfo, Customer_customerId, Customer_customerAddress, Customer_customerName, Customer_customerPhone}

# Relationships
User_Customer: BinaryAssociation = BinaryAssociation(
    name="User_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Admin: BinaryAssociation = BinaryAssociation(
    name="User_Admin",
    ends={
        Property(name="admin2", type=Admin, multiplicity=Multiplicity(0, 10)),
        Property(name="_addUserAsMember3", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="Customer_Shopping_Cart_04", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="addBookToCart5", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Search: BinaryAssociation = BinaryAssociation(
    name="Customer_Search",
    ends={
        Property(name="search6", type=Search, multiplicity=Multiplicity(0, 9999)),
        Property(name="searchBook7", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Search_BookSet: BinaryAssociation = BinaryAssociation(
    name="Search_BookSet",
    ends={
        Property(name="bookSet8", type=BookSet, multiplicity=Multiplicity(0, 1)),
        Property(name="search9", type=Search, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_OrderBook: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_OrderBook",
    ends={
        Property(name="orderBook10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="orderIsUndatedToCart11", type=Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
OrderBook_Admin: BinaryAssociation = BinaryAssociation(
    name="OrderBook_Admin",
    ends={
        Property(name="addBook12", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="orderBook13", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="adce6cef_b3d2_4a14_84ea_977e39592181",
    types={Admin, Shopping_Cart, Search, BookSet, Order, Bookstore_Shop, Payment, User, Customer},
    associations={User_Customer, User_Admin, Customer_Shopping_Cart, Customer_Search, Search_BookSet, Shopping_Cart_OrderBook, OrderBook_Admin},
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
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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Class21 = Class(name="Class21")
Orders = Class(name="Orders")
OrderDetails = Class(name="OrderDetails")
ShoppingCart = Class(name="ShoppingCart")
inter = Class(name="inter")
Product = Class(name="Product")
Statistics = Class(name="Statistics")
Component_Component = Class(name="Component_Component")
Checkout_UseCase = Class(name="Checkout_UseCase")
Customer_Actor = Class(name="Customer_Actor")
Shopping_System_Login_UseCase = Class(name="Shopping_System_Login_UseCase")
Shopping_System_Registration_UseCase = Class(name="Shopping_System_Registration_UseCase")
Shopping_System_Search_Product_UseCase = Class(name="Shopping_System_Search_Product_UseCase")
Shopping_System_Manage_ShopCart_UseCase = Class(name="Shopping_System_Manage_ShopCart_UseCase")
Shopping_System_Manage_Order_UseCase = Class(name="Shopping_System_Manage_Order_UseCase")
Shopping_System_Payment_UseCase = Class(name="Shopping_System_Payment_UseCase")
Shopping_System_Manage_Catalog_UseCase = Class(name="Shopping_System_Manage_Catalog_UseCase")
Shopping_System_Manage_Bills_UseCase = Class(name="Shopping_System_Manage_Bills_UseCase")
Shopping_System_Manage_Settings_UseCase = Class(name="Shopping_System_Manage_Settings_UseCase")
Employee_Actor = Class(name="Employee_Actor")
Manager_Actor = Class(name="Manager_Actor")
Bank_System_Actor = Class(name="Bank_System_Actor")
Category = Class(name="Category")
_Interface = Class(name="_Interface")
Producer = Class(name="Producer")
SubCategory = Class(name="SubCategory")
Customer = Class(name="Customer")
Class_ = Class(name="Class")
Administrator = Class(name="Administrator")
User = Class(name="User")
Class1 = Class(name="Class1")
Class2 = Class(name="Class2")

# Class21 class attributes and methods

# Orders class attributes and methods
Orders_u_id: Property = Property(name="u_id", type=IntegerType)
Orders_dateCreated: Property = Property(name="dateCreated", type=StringType)
Orders_dateShipped: Property = Property(name="dateShipped", type=StringType)
Orders_customer_id: Property = Property(name="customer_id", type=IntegerType)
Orders_status: Property = Property(name="status", type=IntegerType)
Orders.attributes={Orders_status, Orders_customer_id, Orders_dateShipped, Orders_u_id, Orders_dateCreated}

# OrderDetails class attributes and methods
OrderDetails_order_id: Property = Property(name="order_id", type=IntegerType)
OrderDetails_product_id: Property = Property(name="product_id", type=IntegerType)
OrderDetails_product_name: Property = Property(name="product_name", type=StringType)
OrderDetails_quantity: Property = Property(name="quantity", type=IntegerType)
OrderDetails.attributes={OrderDetails_product_id, OrderDetails_order_id, OrderDetails_product_name, OrderDetails_quantity}

# ShoppingCart class attributes and methods
ShoppingCart_cart_id: Property = Property(name="cart_id", type=IntegerType)
ShoppingCart_product_id: Property = Property(name="product_id", type=IntegerType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_product_id, ShoppingCart_quantity, ShoppingCart_cart_id}

# inter class attributes and methods

# Product class attributes and methods
Product_u_id: Property = Property(name="u_id", type=IntegerType)
Product_stock: Property = Property(name="stock", type=IntegerType)
Product_price: Property = Property(name="price", type=StringType)
Product.attributes={Product_u_id, Product_price, Product_stock}

# Statistics class attributes and methods
Statistics_customer_id: Property = Property(name="customer_id", type=IntegerType)
Statistics_click_homepage: Property = Property(name="click_homepage", type=IntegerType)
Statistics_click_homeCat: Property = Property(name="click_homeCat", type=IntegerType)
Statistics_click_subCat: Property = Property(name="click_subCat", type=IntegerType)
Statistics_item_id: Property = Property(name="item_id", type=IntegerType)
Statistics_clicks: Property = Property(name="clicks", type=IntegerType)
Statistics.attributes={Statistics_click_homepage, Statistics_click_homeCat, Statistics_item_id, Statistics_clicks, Statistics_customer_id, Statistics_click_subCat}

# Component_Component class attributes and methods

# Checkout_UseCase class attributes and methods

# Customer_Actor class attributes and methods

# Shopping_System_Login_UseCase class attributes and methods

# Shopping_System_Registration_UseCase class attributes and methods

# Shopping_System_Search_Product_UseCase class attributes and methods

# Shopping_System_Manage_ShopCart_UseCase class attributes and methods

# Shopping_System_Manage_Order_UseCase class attributes and methods

# Shopping_System_Payment_UseCase class attributes and methods

# Shopping_System_Manage_Catalog_UseCase class attributes and methods

# Shopping_System_Manage_Bills_UseCase class attributes and methods

# Shopping_System_Manage_Settings_UseCase class attributes and methods

# Employee_Actor class attributes and methods

# Manager_Actor class attributes and methods

# Bank_System_Actor class attributes and methods

# Category class attributes and methods
Category_u_id: Property = Property(name="u_id", type=IntegerType)
Category_name: Property = Property(name="name", type=StringType)
Category_sequence_id: Property = Property(name="sequence_id", type=IntegerType)
Category.attributes={Category_u_id, Category_sequence_id, Category_name}

# _Interface class attributes and methods

# Producer class attributes and methods
Producer_u_id: Property = Property(name="u_id", type=IntegerType)
Producer_name: Property = Property(name="name", type=StringType)
Producer_country: Property = Property(name="country", type=StringType)
Producer.attributes={Producer_name, Producer_u_id, Producer_country}

# SubCategory class attributes and methods
SubCategory_id: Property = Property(name="id", type=IntegerType)
SubCategory_name: Property = Property(name="name", type=StringType)
SubCategory_cat_id: Property = Property(name="cat_id", type=IntegerType)
SubCategory.attributes={SubCategory_cat_id, SubCategory_name, SubCategory_id}

# Customer class attributes and methods
Customer_u_id: Property = Property(name="u_id", type=IntegerType)
Customer_name: Property = Property(name="name", type=StringType)
Customer_surname: Property = Property(name="surname", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_e_mail: Property = Property(name="e_mail", type=StringType)
Customer.attributes={Customer_name, Customer_address, Customer_surname, Customer_u_id, Customer_e_mail}

# Class class attributes and methods

# Administrator class attributes and methods
Administrator_u_id: Property = Property(name="u_id", type=IntegerType)
Administrator_username: Property = Property(name="username", type=StringType)
Administrator_e_mail: Property = Property(name="e_mail", type=StringType)
Administrator_phone: Property = Property(name="phone", type=StringType)
Administrator.attributes={Administrator_e_mail, Administrator_phone, Administrator_username, Administrator_u_id}

# User class attributes and methods
User_u_id: Property = Property(name="u_id", type=IntegerType)
User_name: Property = Property(name="name", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_e_mail: Property = Property(name="e_mail", type=StringType)
User_phone: Property = Property(name="phone", type=StringType)
User.attributes={User_u_id, User_e_mail, User_phone, User_name, User_password}

# Class1 class attributes and methods

# Class2 class attributes and methods

# Relationships
Category_Category: BinaryAssociation = BinaryAssociation(
    name="Category_Category",
    ends={
        Property(name="category0", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="category1", type=Category, multiplicity=Multiplicity(0, 1))
    }
)
SubCategory_Category: BinaryAssociation = BinaryAssociation(
    name="SubCategory_Category",
    ends={
        Property(name="category2", type=Category, multiplicity=Multiplicity(0, 9999)),
        Property(name="subCategory3", type=SubCategory, multiplicity=Multiplicity(1, 1))
    }
)
Category_Category2: BinaryAssociation = BinaryAssociation(
    name="Category_Category2",
    ends={
        Property(name="category22", type=Category, multiplicity=Multiplicity(0, 9999)),
        Property(name="category23", type=Category, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Bank_System: BinaryAssociation = BinaryAssociation(
    name="Payment_Bank_System",
    ends={
        Property(name="bank_System24", type=Bank_System_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="payment25", type=Shopping_System_Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Login: BinaryAssociation = BinaryAssociation(
    name="Actor_Login",
    ends={
        Property(name="login26", type=Shopping_System_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor27", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Registration: BinaryAssociation = BinaryAssociation(
    name="Actor_Registration",
    ends={
        Property(name="registration28", type=Shopping_System_Registration_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor29", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Search_Product: BinaryAssociation = BinaryAssociation(
    name="Actor_Search_Product",
    ends={
        Property(name="search_Product30", type=Shopping_System_Search_Product_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor31", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Manage_ShopCart: BinaryAssociation = BinaryAssociation(
    name="Actor_Manage_ShopCart",
    ends={
        Property(name="manage_ShopCart32", type=Shopping_System_Manage_ShopCart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor33", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Manage_Order: BinaryAssociation = BinaryAssociation(
    name="Actor_Manage_Order",
    ends={
        Property(name="manage_Order34", type=Shopping_System_Manage_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor35", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Payment: BinaryAssociation = BinaryAssociation(
    name="Actor_Payment",
    ends={
        Property(name="payment36", type=Shopping_System_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor37", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Employee: BinaryAssociation = BinaryAssociation(
    name="Employee_Employee",
    ends={
        Property(name="employee38", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="employee39", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Sales_Report: BinaryAssociation = BinaryAssociation(
    name="Employee_Sales_Report",
    ends={
        Property(name="sales_Report40", type=Shopping_System_Manage_Bills_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee41", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Manage_Order: BinaryAssociation = BinaryAssociation(
    name="Employee_Manage_Order",
    ends={
        Property(name="manage_Order42", type=Shopping_System_Manage_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee43", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login44", type=Shopping_System_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee45", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Login: BinaryAssociation = BinaryAssociation(
    name="Manager_Login",
    ends={
        Property(name="login46", type=Shopping_System_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager47", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Manage_Catalog: BinaryAssociation = BinaryAssociation(
    name="Manager_Manage_Catalog",
    ends={
        Property(name="manage_Catalog48", type=Shopping_System_Manage_Catalog_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager49", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Manage_Settings: BinaryAssociation = BinaryAssociation(
    name="Manager_Manage_Settings",
    ends={
        Property(name="manage_Settings50", type=Shopping_System_Manage_Settings_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager51", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
SubCategory_SubCategory: BinaryAssociation = BinaryAssociation(
    name="SubCategory_SubCategory",
    ends={
        Property(name="subCategory4", type=SubCategory, multiplicity=Multiplicity(0, 1)),
        Property(name="subCategory5", type=SubCategory, multiplicity=Multiplicity(0, 1))
    }
)
SubCategory_Category2: BinaryAssociation = BinaryAssociation(
    name="SubCategory_Category2",
    ends={
        Property(name="category6", type=Category, multiplicity=Multiplicity(1, 1)),
        Property(name="subCategory7", type=SubCategory, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="orders8", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer9", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Orders_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Orders_OrderDetails",
    ends={
        Property(name="orderDetails10", type=OrderDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="orders11", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_Customer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Customer",
    ends={
        Property(name="customer12", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart13", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="shoppingCart14", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="customer15", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Product_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Product_OrderDetails",
    ends={
        Property(name="orderDetails16", type=OrderDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="product17", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
Producer_Product: BinaryAssociation = BinaryAssociation(
    name="Producer_Product",
    ends={
        Property(name="product18", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="producer19", type=Producer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Statistics: BinaryAssociation = BinaryAssociation(
    name="Customer_Statistics",
    ends={
        Property(name="statistics20", type=Statistics, multiplicity=Multiplicity(1, 1)),
        Property(name="customer21", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5xzzkIRdEemg3PWSmqBV3A",
    types={Class21, Orders, OrderDetails, ShoppingCart, inter, Product, Statistics, Component_Component, Checkout_UseCase, Customer_Actor, Shopping_System_Login_UseCase, Shopping_System_Registration_UseCase, Shopping_System_Search_Product_UseCase, Shopping_System_Manage_ShopCart_UseCase, Shopping_System_Manage_Order_UseCase, Shopping_System_Payment_UseCase, Shopping_System_Manage_Catalog_UseCase, Shopping_System_Manage_Bills_UseCase, Shopping_System_Manage_Settings_UseCase, Employee_Actor, Manager_Actor, Bank_System_Actor, Category, _Interface, Producer, SubCategory, Customer, Class_, Administrator, User, Class1, Class2, Enumeration_},
    associations={Category_Category, SubCategory_Category, Category_Category2, Payment_Bank_System, Actor_Login, Actor_Registration, Actor_Search_Product, Actor_Manage_ShopCart, Actor_Manage_Order, Actor_Payment, Employee_Employee, Employee_Sales_Report, Employee_Manage_Order, Employee_Login, Manager_Login, Manager_Manage_Catalog, Manager_Manage_Settings, SubCategory_SubCategory, SubCategory_Category2, Customer_Orders, Orders_OrderDetails, ShoppingCart_Customer, Customer_ShoppingCart, Product_OrderDetails, Producer_Product, Customer_Statistics},
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
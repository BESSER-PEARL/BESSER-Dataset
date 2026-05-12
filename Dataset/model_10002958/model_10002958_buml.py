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
user_name_UseCase = Class(name="user_name_UseCase")
User_Actor = Class(name="User_Actor")
Login_UseCase = Class(name="Login_UseCase")
View_product_UseCase = Class(name="View_product_UseCase")
Password_UseCase = Class(name="Password_UseCase")
Update_product_UseCase = Class(name="Update_product_UseCase")
Buy_product_UseCase = Class(name="Buy_product_UseCase")
Key_generate_UseCase = Class(name="Key_generate_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Comment_UseCase = Class(name="Comment_UseCase")
Analyzing_UseCase = Class(name="Analyzing_UseCase")
Customer = Class(name="Customer")
Account = Class(name="Account")
Payment = Class(name="Payment")
Login = Class(name="Login")
Cart = Class(name="Cart")
order = Class(name="order")

# user_name_UseCase class attributes and methods

# User_Actor class attributes and methods

# Login_UseCase class attributes and methods

# View_product_UseCase class attributes and methods

# Password_UseCase class attributes and methods

# Update_product_UseCase class attributes and methods

# Buy_product_UseCase class attributes and methods

# Key_generate_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Comment_UseCase class attributes and methods

# Analyzing_UseCase class attributes and methods

# Customer class attributes and methods
Customer_login_id_: Property = Property(name="login_id_", type=StringType)
Customer_Address_: Property = Property(name="Address_", type=StringType)
Customer_Phone_: Property = Property(name="Phone_", type=IntegerType)
Customer.attributes={Customer_login_id_, Customer_Address_, Customer_Phone_}

# Account class attributes and methods
Account_Branch_: Property = Property(name="Branch_", type=StringType)
Account_Phone_no_: Property = Property(name="Phone_no_", type=IntegerType)
Account_Acc_no_: Property = Property(name="Acc_no_", type=IntegerType)
Account.attributes={Account_Phone_no_, Account_Acc_no_, Account_Branch_}

# Payment class attributes and methods
Payment_Transaction_id_: Property = Property(name="Transaction_id_", type=IntegerType)
Payment_Amount_paid_: Property = Property(name="Amount_paid_", type=IntegerType)
Payment_Acc_No_: Property = Property(name="Acc_No_", type=IntegerType)
Payment.attributes={Payment_Amount_paid_, Payment_Acc_No_, Payment_Transaction_id_}

# Login class attributes and methods
Login_login_id_: Property = Property(name="login_id_", type=StringType)
Login_password_: Property = Property(name="password_", type=StringType)
Login.attributes={Login_password_, Login_login_id_}

# Cart class attributes and methods
Cart_Buy_: Property = Property(name="Buy_", type=IntegerType)
Cart_No_of_items_: Property = Property(name="No_of_items_", type=IntegerType)
Cart_Delete_: Property = Property(name="Delete_", type=StringType)
Cart.attributes={Cart_No_of_items_, Cart_Delete_, Cart_Buy_}

# order class attributes and methods
order_no_of_items_: Property = Property(name="no_of_items_", type=IntegerType)
order_amount__: Property = Property(name="amount__", type=IntegerType)
order_order_status_: Property = Property(name="order_status_", type=StringType)
order.attributes={order_no_of_items_, order_order_status_, order_amount__}

# Relationships
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login0", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_product: BinaryAssociation = BinaryAssociation(
    name="User_View_product",
    ends={
        Property(name="view_product2", type=View_product_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Buy_product: BinaryAssociation = BinaryAssociation(
    name="User_Buy_product",
    ends={
        Property(name="buy_product4", type=Buy_product_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Key_generate: BinaryAssociation = BinaryAssociation(
    name="User_Key_generate",
    ends={
        Property(name="key_generate6", type=Key_generate_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Login: BinaryAssociation = BinaryAssociation(
    name="Admin_Login",
    ends={
        Property(name="login8", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Update_product_Admin: BinaryAssociation = BinaryAssociation(
    name="Update_product_Admin",
    ends={
        Property(name="admin10", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_product11", type=Update_product_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Key_generate_Admin: BinaryAssociation = BinaryAssociation(
    name="Key_generate_Admin",
    ends={
        Property(name="admin12", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="key_generate13", type=Key_generate_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_product_Admin: BinaryAssociation = BinaryAssociation(
    name="View_product_Admin",
    ends={
        Property(name="admin14", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_product15", type=View_product_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Login_Customer: BinaryAssociation = BinaryAssociation(
    name="Login_Customer",
    ends={
        Property(name="customer16", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="login17", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Cart_order: BinaryAssociation = BinaryAssociation(
    name="Cart_order",
    ends={
        Property(name="order18", type=order, multiplicity=Multiplicity(0, 1)),
        Property(name="cart19", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
Account_order: BinaryAssociation = BinaryAssociation(
    name="Account_order",
    ends={
        Property(name="order20", type=order, multiplicity=Multiplicity(0, 1)),
        Property(name="account21", type=Account, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ef906059_9e09_4003_bc38_73028f54ac9c",
    types={user_name_UseCase, User_Actor, Login_UseCase, View_product_UseCase, Password_UseCase, Update_product_UseCase, Buy_product_UseCase, Key_generate_UseCase, Admin_Actor, Comment_UseCase, Analyzing_UseCase, Customer, Account, Payment, Login, Cart, order},
    associations={User_Login, User_View_product, User_Buy_product, User_Key_generate, Admin_Login, Update_product_Admin, Key_generate_Admin, View_product_Admin, Login_Customer, Cart_order, Account_order},
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
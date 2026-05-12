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
Customer_Actor = Class(name="Customer_Actor")
Sign_up_UseCase = Class(name="Sign_up_UseCase")
Log_in_UseCase = Class(name="Log_in_UseCase")
Search_Book_UseCase = Class(name="Search_Book_UseCase")
Add_book__to_cart_UseCase = Class(name="Add_book__to_cart_UseCase")
Make_Payment_UseCase = Class(name="Make_Payment_UseCase")
Logout_UseCase = Class(name="Logout_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Add_Book_UseCase = Class(name="Add_Book_UseCase")
Edit_Book_UseCase = Class(name="Edit_Book_UseCase")
Confirm_Payment_UseCase = Class(name="Confirm_Payment_UseCase")
Bank_Mobile_Money_Agent_Actor = Class(name="Bank_Mobile_Money_Agent_Actor")
Administrator = Class(name="Administrator")
Book = Class(name="Book")
Customer = Class(name="Customer")
Category = Class(name="Category")

# Customer_Actor class attributes and methods

# Sign_up_UseCase class attributes and methods

# Log_in_UseCase class attributes and methods

# Search_Book_UseCase class attributes and methods

# Add_book__to_cart_UseCase class attributes and methods

# Make_Payment_UseCase class attributes and methods

# Logout_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Add_Book_UseCase class attributes and methods

# Edit_Book_UseCase class attributes and methods

# Confirm_Payment_UseCase class attributes and methods

# Bank_Mobile_Money_Agent_Actor class attributes and methods

# Administrator class attributes and methods
Administrator_adminID: Property = Property(name="adminID", type=IntegerType)
Administrator_name: Property = Property(name="name", type=StringType)
Administrator_email: Property = Property(name="email", type=StringType)
Administrator.attributes={Administrator_adminID, Administrator_name, Administrator_email}

# Book class attributes and methods
Book_bookID: Property = Property(name="bookID", type=IntegerType)
Book_title: Property = Property(name="title", type=StringType)
Book_category: Property = Property(name="category", type=Customer)
Book_price: Property = Property(name="price", type=IntegerType)
Book_description: Property = Property(name="description", type=StringType)
Book_author: Property = Property(name="author", type=StringType)
Book.attributes={Book_bookID, Book_author, Book_title, Book_description, Book_price, Book_category}

# Customer class attributes and methods
Customer_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Customer_username: Property = Property(name="username", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_username, Customer_CustomerID, Customer_email}

# Category class attributes and methods
Category_categoryID: Property = Property(name="categoryID", type=IntegerType)
Category_categoryName: Property = Property(name="categoryName", type=StringType)
Category.attributes={Category_categoryName, Category_categoryID}

# Relationships
Logout_Logout: BinaryAssociation = BinaryAssociation(
    name="Logout_Logout",
    ends={
        Property(name="logout0", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="logout1", type=Logout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Logout: BinaryAssociation = BinaryAssociation(
    name="Customer_Logout",
    ends={
        Property(name="logout2", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Sign_up: BinaryAssociation = BinaryAssociation(
    name="Customer_Sign_up",
    ends={
        Property(name="sign_up4", type=Sign_up_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Log_in: BinaryAssociation = BinaryAssociation(
    name="Customer_Log_in",
    ends={
        Property(name="log_in6", type=Log_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Add_book__to_cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Add_book__to_cart",
    ends={
        Property(name="add_book__to_cart8", type=Add_book__to_cart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Make_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Make_Payment",
    ends={
        Property(name="make_Payment10", type=Make_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Search_Book: BinaryAssociation = BinaryAssociation(
    name="Customer_Search_Book",
    ends={
        Property(name="search_Book12", type=Search_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Edit_Book: BinaryAssociation = BinaryAssociation(
    name="Administrator_Edit_Book",
    ends={
        Property(name="edit_Book14", type=Edit_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Add_Book: BinaryAssociation = BinaryAssociation(
    name="Administrator_Add_Book",
    ends={
        Property(name="add_Book16", type=Add_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Confirm_Payment: BinaryAssociation = BinaryAssociation(
    name="Administrator_Confirm_Payment",
    ends={
        Property(name="confirm_Payment18", type=Confirm_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator19", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Mobile_Money_Agent_Confirm_Payment: BinaryAssociation = BinaryAssociation(
    name="Bank_Mobile_Money_Agent_Confirm_Payment",
    ends={
        Property(name="confirm_Payment20", type=Confirm_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank_Mobile_Money_Agent21", type=Bank_Mobile_Money_Agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Book: BinaryAssociation = BinaryAssociation(
    name="Administrator_Book",
    ends={
        Property(name="book22", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator23", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Category_Category: BinaryAssociation = BinaryAssociation(
    name="Category_Category",
    ends={
        Property(name="category26", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="category27", type=Category, multiplicity=Multiplicity(0, 1))
    }
)
Category_Book: BinaryAssociation = BinaryAssociation(
    name="Category_Book",
    ends={
        Property(name="book28", type=Book, multiplicity=Multiplicity(1, 9999)),
        Property(name="category29", type=Category, multiplicity=Multiplicity(1, 9999))
    }
)
Administrator_Administrator: BinaryAssociation = BinaryAssociation(
    name="Administrator_Administrator",
    ends={
        Property(name="administrator30", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator31", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Customer: BinaryAssociation = BinaryAssociation(
    name="Administrator_Customer",
    ends={
        Property(name="customer32", type=Customer, multiplicity=Multiplicity(1, 9999)),
        Property(name="administrator33", type=Administrator, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Book: BinaryAssociation = BinaryAssociation(
    name="Customer_Book",
    ends={
        Property(name="book34", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="customer35", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer",
    ends={
        Property(name="customer36", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="customer37", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Book2: BinaryAssociation = BinaryAssociation(
    name="Customer_Book2",
    ends={
        Property(name="book38", type=Book, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer39", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Administrator_Book2: BinaryAssociation = BinaryAssociation(
    name="Administrator_Book2",
    ends={
        Property(name="book24", type=Book, multiplicity=Multiplicity(1, 9999)),
        Property(name="administrator25", type=Administrator, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7rJioEE9EeqonN_RS9oRzw",
    types={Customer_Actor, Sign_up_UseCase, Log_in_UseCase, Search_Book_UseCase, Add_book__to_cart_UseCase, Make_Payment_UseCase, Logout_UseCase, Administrator_Actor, Add_Book_UseCase, Edit_Book_UseCase, Confirm_Payment_UseCase, Bank_Mobile_Money_Agent_Actor, Administrator, Book, Customer, Category},
    associations={Logout_Logout, Customer_Logout, Customer_Sign_up, Customer_Log_in, Customer_Add_book__to_cart, Customer_Make_Payment, Customer_Search_Book, Administrator_Edit_Book, Administrator_Add_Book, Administrator_Confirm_Payment, Bank_Mobile_Money_Agent_Confirm_Payment, Administrator_Book, Category_Category, Category_Book, Administrator_Administrator, Administrator_Customer, Customer_Book, Customer_Customer, Customer_Book2, Administrator_Book2},
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
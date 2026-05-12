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
Librarian_Actor = Class(name="Librarian_Actor")
Log_in_UseCase = Class(name="Log_in_UseCase")
Add_Book_UseCase = Class(name="Add_Book_UseCase")
Delete_Book_UseCase = Class(name="Delete_Book_UseCase")
User_Maintenance_UseCase = Class(name="User_Maintenance_UseCase")
Person_Actor = Class(name="Person_Actor")
View_Books_UseCase = Class(name="View_Books_UseCase")
Borrow_Book_UseCase = Class(name="Borrow_Book_UseCase")
Capatcha_UseCase = Class(name="Capatcha_UseCase")
Enter__Username_UseCase = Class(name="Enter__Username_UseCase")
Enter_Password_UseCase = Class(name="Enter_Password_UseCase")
Recieving_Book_UseCase = Class(name="Recieving_Book_UseCase")
Guest_Actor = Class(name="Guest_Actor")
ID_Authentication_Server_Actor = Class(name="ID_Authentication_Server_Actor")
Viewing_Books_UseCase = Class(name="Viewing_Books_UseCase")
List_view__UseCase = Class(name="List_view__UseCase")
Searching_UseCase = Class(name="Searching_UseCase")
Suggestion_UseCase = Class(name="Suggestion_UseCase")
Add_to_Borrow_basket_UseCase = Class(name="Add_to_Borrow_basket_UseCase")
User_Actor = Class(name="User_Actor")
ID_Authentication_Server_UseCase = Class(name="ID_Authentication_Server_UseCase")
Billing_UseCase = Class(name="Billing_UseCase")
PayPal_UseCase = Class(name="PayPal_UseCase")
Credit_Card_UseCase = Class(name="Credit_Card_UseCase")
Debit_Card_UseCase = Class(name="Debit_Card_UseCase")
Cash_UseCase = Class(name="Cash_UseCase")
Payment_System_UseCase = Class(name="Payment_System_UseCase")
_UseCase = Class(name="_UseCase")
Bank_Server_Side_Authentication_UseCase = Class(name="Bank_Server_Side_Authentication_UseCase")
Payment_UseCase = Class(name="Payment_UseCase")
PayPal_UseCase1 = Class(name="PayPal_UseCase1")
Credit_Card_UseCase1 = Class(name="Credit_Card_UseCase1")
Payment_Authentecation_System_Actor = Class(name="Payment_Authentecation_System_Actor")
PayPal_Authentication_Service_Actor = Class(name="PayPal_Authentication_Service_Actor")
Credit_Card_Authentication_Service_Actor = Class(name="Credit_Card_Authentication_Service_Actor")
Bank_Accounting_Actor = Class(name="Bank_Accounting_Actor")
Book_Maintenance__UseCase = Class(name="Book_Maintenance__UseCase")
Remove_Member_UseCase = Class(name="Remove_Member_UseCase")
Add_Member_UseCase = Class(name="Add_Member_UseCase")
Registration__UseCase = Class(name="Registration__UseCase")
Authentication_UseCase = Class(name="Authentication_UseCase")
Generating_Membership_Card_UseCase = Class(name="Generating_Membership_Card_UseCase")
Book = Class(name="Book")
Person = Class(name="Person")
Guest = Class(name="Guest")
Librarian = Class(name="Librarian")
User = Class(name="User")
BookBorrow = Class(name="BookBorrow")
Library = Class(name="Library")
Billing_UseCase1 = Class(name="Billing_UseCase1")
Book_Delivery__UseCase = Class(name="Book_Delivery__UseCase")

# Librarian_Actor class attributes and methods

# Log_in_UseCase class attributes and methods

# Add_Book_UseCase class attributes and methods

# Delete_Book_UseCase class attributes and methods

# User_Maintenance_UseCase class attributes and methods

# Person_Actor class attributes and methods

# View_Books_UseCase class attributes and methods

# Borrow_Book_UseCase class attributes and methods

# Capatcha_UseCase class attributes and methods

# Enter__Username_UseCase class attributes and methods

# Enter_Password_UseCase class attributes and methods

# Recieving_Book_UseCase class attributes and methods

# Guest_Actor class attributes and methods

# ID_Authentication_Server_Actor class attributes and methods

# Viewing_Books_UseCase class attributes and methods

# List_view__UseCase class attributes and methods

# Searching_UseCase class attributes and methods

# Suggestion_UseCase class attributes and methods

# Add_to_Borrow_basket_UseCase class attributes and methods

# User_Actor class attributes and methods

# ID_Authentication_Server_UseCase class attributes and methods

# Billing_UseCase class attributes and methods

# PayPal_UseCase class attributes and methods

# Credit_Card_UseCase class attributes and methods

# Debit_Card_UseCase class attributes and methods

# Cash_UseCase class attributes and methods

# Payment_System_UseCase class attributes and methods

# _UseCase class attributes and methods

# Bank_Server_Side_Authentication_UseCase class attributes and methods

# Payment_UseCase class attributes and methods

# PayPal_UseCase1 class attributes and methods

# Credit_Card_UseCase1 class attributes and methods

# Payment_Authentecation_System_Actor class attributes and methods

# PayPal_Authentication_Service_Actor class attributes and methods

# Credit_Card_Authentication_Service_Actor class attributes and methods

# Bank_Accounting_Actor class attributes and methods

# Book_Maintenance__UseCase class attributes and methods

# Remove_Member_UseCase class attributes and methods

# Add_Member_UseCase class attributes and methods

# Registration__UseCase class attributes and methods

# Authentication_UseCase class attributes and methods

# Generating_Membership_Card_UseCase class attributes and methods

# Book class attributes and methods
Book_BookID: Property = Property(name="BookID", type=IntegerType)
Book_BookName: Property = Property(name="BookName", type=StringType)
Book_PubName: Property = Property(name="PubName", type=StringType)
Book_Price: Property = Property(name="Price", type=IntegerType)
Book_LibraryID: Property = Property(name="LibraryID", type=IntegerType)
Book.attributes={Book_LibraryID, Book_Price, Book_BookName, Book_BookID, Book_PubName}

# Person class attributes and methods
Person_PersonID: Property = Property(name="PersonID", type=IntegerType)
Person_PersonName: Property = Property(name="PersonName", type=StringType)
Person_BirthDay: Property = Property(name="BirthDay", type=StringType)
Person_LibraryID: Property = Property(name="LibraryID", type=IntegerType)
Person.attributes={Person_PersonID, Person_PersonName, Person_BirthDay, Person_LibraryID}

# Guest class attributes and methods
Guest_GuestID: Property = Property(name="GuestID", type=IntegerType)
Guest.attributes={Guest_GuestID}

# Librarian class attributes and methods
Librarian_LibID: Property = Property(name="LibID", type=IntegerType)
Librarian_Department: Property = Property(name="Department", type=StringType)
Librarian.attributes={Librarian_LibID, Librarian_Department}

# User class attributes and methods
User_UserCode: Property = Property(name="UserCode", type=IntegerType)
User_attribute: Property = Property(name="attribute", type=StringType)
User_Active: Property = Property(name="Active", type=BooleanType)
User_RegistrationDate: Property = Property(name="RegistrationDate", type=StringType)
User_Mail: Property = Property(name="Mail", type=StringType)
User_Address: Property = Property(name="Address", type=StringType)
User_Phone: Property = Property(name="Phone", type=IntegerType)
User.attributes={User_Mail, User_Address, User_RegistrationDate, User_UserCode, User_attribute, User_Phone, User_Active}

# BookBorrow class attributes and methods
BookBorrow_BorrowID: Property = Property(name="BorrowID", type=IntegerType)
BookBorrow_InDate: Property = Property(name="InDate", type=StringType)
BookBorrow_OutDate: Property = Property(name="OutDate", type=StringType)
BookBorrow_BookID: Property = Property(name="BookID", type=IntegerType)
BookBorrow_UserCode: Property = Property(name="UserCode", type=Enter__Username_UseCase)
BookBorrow.attributes={BookBorrow_UserCode, BookBorrow_OutDate, BookBorrow_BorrowID, BookBorrow_InDate, BookBorrow_BookID}

# Library class attributes and methods
Library_LibraryID: Property = Property(name="LibraryID", type=IntegerType)
Library_Address: Property = Property(name="Address", type=StringType)
Library.attributes={Library_LibraryID, Library_Address}

# Billing_UseCase1 class attributes and methods

# Book_Delivery__UseCase class attributes and methods

# Relationships
Payment_Authentecation_System_Credit_Card: BinaryAssociation = BinaryAssociation(
    name="Payment_Authentecation_System_Credit_Card",
    ends={
        Property(name="credit_Card16", type=Credit_Card_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_Authentecation_System17", type=Payment_Authentecation_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
PayPal_Authentication_Service_PayPal: BinaryAssociation = BinaryAssociation(
    name="PayPal_Authentication_Service_PayPal",
    ends={
        Property(name="payPal18", type=PayPal_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="payPal_Authentication_Service19", type=PayPal_Authentication_Service_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Credit_Card_Authentication_Service_Credit_Card: BinaryAssociation = BinaryAssociation(
    name="Credit_Card_Authentication_Service_Credit_Card",
    ends={
        Property(name="credit_Card20", type=Credit_Card_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="credit_Card_Authentication_Service21", type=Credit_Card_Authentication_Service_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Accounting_Bank_Server_Side_Authentication: BinaryAssociation = BinaryAssociation(
    name="Bank_Accounting_Bank_Server_Side_Authentication",
    ends={
        Property(name="bank_Server_Side_Authentication22", type=Bank_Server_Side_Authentication_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank_Accounting23", type=Bank_Accounting_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Book_Maintenance: BinaryAssociation = BinaryAssociation(
    name="Librarian_Book_Maintenance",
    ends={
        Property(name="book_Maintenance24", type=Book_Maintenance__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian25", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
ID_Authentication_Server_Authentication: BinaryAssociation = BinaryAssociation(
    name="ID_Authentication_Server_Authentication",
    ends={
        Property(name="authentication26", type=Authentication_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iD_Authentication_Server27", type=ID_Authentication_Server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Book_BookBorrow: BinaryAssociation = BinaryAssociation(
    name="Book_BookBorrow",
    ends={
        Property(name="bookBorrow28", type=BookBorrow, multiplicity=Multiplicity(1, 9999)),
        Property(name="book29", type=Book, multiplicity=Multiplicity(1, 9999))
    }
)
BookBorrow_User: BinaryAssociation = BinaryAssociation(
    name="BookBorrow_User",
    ends={
        Property(name="user30", type=User, multiplicity=Multiplicity(1, 9999)),
        Property(name="bookBorrow31", type=BookBorrow, multiplicity=Multiplicity(1, 9999))
    }
)
Book_Library: BinaryAssociation = BinaryAssociation(
    name="Book_Library",
    ends={
        Property(name="library32", type=Library, multiplicity=Multiplicity(1, 9999)),
        Property(name="book33", type=Book, multiplicity=Multiplicity(1, 9999))
    }
)
Library_Person: BinaryAssociation = BinaryAssociation(
    name="Library_Person",
    ends={
        Property(name="person34", type=Person, multiplicity=Multiplicity(1, 9999)),
        Property(name="library35", type=Library, multiplicity=Multiplicity(1, 9999))
    }
)
Registered_User_Log_in: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Log_in",
    ends={
        Property(name="log_in36", type=Log_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User37", type=Person_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Person_View_Books: BinaryAssociation = BinaryAssociation(
    name="Person_View_Books",
    ends={
        Property(name="view_Books38", type=View_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="person39", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Person_Borrow_Book: BinaryAssociation = BinaryAssociation(
    name="Person_Borrow_Book",
    ends={
        Property(name="borrow_Book40", type=Borrow_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="person41", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Guest_View_Books: BinaryAssociation = BinaryAssociation(
    name="Guest_View_Books",
    ends={
        Property(name="view_Books42", type=View_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest43", type=Guest_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Add_Book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Add_Book",
    ends={
        Property(name="add_Book0", type=Add_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian1", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Delete_Book: BinaryAssociation = BinaryAssociation(
    name="Librarian_Delete_Book",
    ends={
        Property(name="delete_Book2", type=Delete_Book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian3", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Add_User: BinaryAssociation = BinaryAssociation(
    name="Librarian_Add_User",
    ends={
        Property(name="add_User4", type=User_Maintenance_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian5", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Borrow_Book_Authentication_Server: BinaryAssociation = BinaryAssociation(
    name="Borrow_Book_Authentication_Server",
    ends={
        Property(name="authentication_Server6", type=ID_Authentication_Server_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="borrow_Book7", type=Borrow_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_Books_Authentication_Server: BinaryAssociation = BinaryAssociation(
    name="View_Books_Authentication_Server",
    ends={
        Property(name="authentication_Server8", type=ID_Authentication_Server_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_Books9", type=View_Books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ID_Authentication_Server_Log_in: BinaryAssociation = BinaryAssociation(
    name="ID_Authentication_Server_Log_in",
    ends={
        Property(name="log_in10", type=Log_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iD_Authentication_Server11", type=ID_Authentication_Server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payment_System_Payment_Authentecation_System: BinaryAssociation = BinaryAssociation(
    name="Payment_System_Payment_Authentecation_System",
    ends={
        Property(name="payment_Authentecation_System12", type=_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_System13", type=Payment_System_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Authentecation_System_PayPal: BinaryAssociation = BinaryAssociation(
    name="Payment_Authentecation_System_PayPal",
    ends={
        Property(name="payPal14", type=PayPal_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_Authentecation_System15", type=Payment_Authentecation_System_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_RcxFYIniEemopIBfncy06w",
    types={Librarian_Actor, Log_in_UseCase, Add_Book_UseCase, Delete_Book_UseCase, User_Maintenance_UseCase, Person_Actor, View_Books_UseCase, Borrow_Book_UseCase, Capatcha_UseCase, Enter__Username_UseCase, Enter_Password_UseCase, Recieving_Book_UseCase, Guest_Actor, ID_Authentication_Server_Actor, Viewing_Books_UseCase, List_view__UseCase, Searching_UseCase, Suggestion_UseCase, Add_to_Borrow_basket_UseCase, User_Actor, ID_Authentication_Server_UseCase, Billing_UseCase, PayPal_UseCase, Credit_Card_UseCase, Debit_Card_UseCase, Cash_UseCase, Payment_System_UseCase, _UseCase, Bank_Server_Side_Authentication_UseCase, Payment_UseCase, PayPal_UseCase1, Credit_Card_UseCase1, Payment_Authentecation_System_Actor, PayPal_Authentication_Service_Actor, Credit_Card_Authentication_Service_Actor, Bank_Accounting_Actor, Book_Maintenance__UseCase, Remove_Member_UseCase, Add_Member_UseCase, Registration__UseCase, Authentication_UseCase, Generating_Membership_Card_UseCase, Book, Person, Guest, Librarian, User, BookBorrow, Library, Billing_UseCase1, Book_Delivery__UseCase},
    associations={Payment_Authentecation_System_Credit_Card, PayPal_Authentication_Service_PayPal, Credit_Card_Authentication_Service_Credit_Card, Bank_Accounting_Bank_Server_Side_Authentication, Librarian_Book_Maintenance, ID_Authentication_Server_Authentication, Book_BookBorrow, BookBorrow_User, Book_Library, Library_Person, Registered_User_Log_in, Person_View_Books, Person_Borrow_Book, Guest_View_Books, Librarian_Add_Book, Librarian_Delete_Book, Librarian_Add_User, Borrow_Book_Authentication_Server, View_Books_Authentication_Server, ID_Authentication_Server_Log_in, Payment_System_Payment_Authentecation_System, Payment_Authentecation_System_PayPal},
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
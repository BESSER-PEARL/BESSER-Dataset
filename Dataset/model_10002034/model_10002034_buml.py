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
User = Class(name="User")
SessionManager = Class(name="SessionManager")
Customer = Class(name="Customer")
BooksOrder = Class(name="BooksOrder")
Book = Class(name="Book")
Administrator = Class(name="Administrator")
BookSet = Class(name="BookSet")
Search = Class(name="Search")
AdvSearch = Class(name="AdvSearch")
Category = Class(name="Category")
ShoppingCart = Class(name="ShoppingCart")

# User class attributes and methods
User_userID: Property = Property(name="userID", type=IntegerType)
User_password: Property = Property(name="password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User.attributes={User_userID, User_password, User_loginStatus}

# SessionManager class attributes and methods
SessionManager_userID: Property = Property(name="userID", type=IntegerType)
SessionManager_categoryName: Property = Property(name="categoryName", type=StringType)
SessionManager.attributes={SessionManager_categoryName, SessionManager_userID}

# Customer class attributes and methods
Customer_email: Property = Property(name="email", type=StringType)
Customer_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Customer_CCinfo: Property = Property(name="CCinfo", type=StringType)
Customer_customerID: Property = Property(name="customerID", type=StringType)
Customer_password: Property = Property(name="password", type=StringType)
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer.attributes={Customer_address, Customer_email, Customer_name, Customer_password, Customer_customerID, Customer_CCinfo, Customer_phoneNo}

# BooksOrder class attributes and methods
BooksOrder_orderID: Property = Property(name="orderID", type=IntegerType)
BooksOrder_price: Property = Property(name="price", type=StringType)
BooksOrder_customerID: Property = Property(name="customerID", type=IntegerType)
BooksOrder_quantity: Property = Property(name="quantity", type=IntegerType)
BooksOrder.attributes={BooksOrder_quantity, BooksOrder_orderID, BooksOrder_price, BooksOrder_customerID}

# Book class attributes and methods
Book_bookID: Property = Property(name="bookID", type=IntegerType)
Book_bookName: Property = Property(name="bookName", type=StringType)
Book_price: Property = Property(name="price", type=StringType)
Book_rating: Property = Property(name="rating", type=IntegerType)
Book_authorName: Property = Property(name="authorName", type=StringType)
Book_imageURL: Property = Property(name="imageURL", type=StringType)
Book_notes: Property = Property(name="notes", type=StringType)
Book_productURL: Property = Property(name="productURL", type=StringType)
Book_categoryID: Property = Property(name="categoryID", type=IntegerType)
Book.attributes={Book_notes, Book_rating, Book_price, Book_categoryID, Book_bookName, Book_bookID, Book_imageURL, Book_productURL, Book_authorName}

# Administrator class attributes and methods
Administrator_adminID: Property = Property(name="adminID", type=IntegerType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator_name: Property = Property(name="name", type=StringType)
Administrator_email: Property = Property(name="email", type=StringType)
Administrator_phoneNo: Property = Property(name="phoneNo", type=StringType)
Administrator.attributes={Administrator_name, Administrator_adminID, Administrator_phoneNo, Administrator_email, Administrator_password}

# BookSet class attributes and methods
BookSet_bookID: Property = Property(name="bookID", type=IntegerType)
BookSet_bookName: Property = Property(name="bookName", type=StringType)
BookSet.attributes={BookSet_bookID, BookSet_bookName}

# Search class attributes and methods
Search_bookTitle: Property = Property(name="bookTitle", type=StringType)
Search_categoryID: Property = Property(name="categoryID", type=StringType)
Search.attributes={Search_bookTitle, Search_categoryID}

# AdvSearch class attributes and methods
AdvSearch_bookTitle: Property = Property(name="bookTitle", type=StringType)
AdvSearch_categoryID: Property = Property(name="categoryID", type=StringType)
AdvSearch_bookAuthor: Property = Property(name="bookAuthor", type=StringType)
AdvSearch_bookLowCost: Property = Property(name="bookLowCost", type=StringType)
AdvSearch_bookHighCost: Property = Property(name="bookHighCost", type=StringType)
AdvSearch.attributes={AdvSearch_bookLowCost, AdvSearch_categoryID, AdvSearch_bookAuthor, AdvSearch_bookHighCost, AdvSearch_bookTitle}

# Category class attributes and methods
Category_categoryID: Property = Property(name="categoryID", type=IntegerType)
Category_categoryName: Property = Property(name="categoryName", type=StringType)
Category.attributes={Category_categoryID, Category_categoryName}

# ShoppingCart class attributes and methods
ShoppingCart_price: Property = Property(name="price", type=StringType)
ShoppingCart_orderID: Property = Property(name="orderID", type=IntegerType)
ShoppingCart_customerID: Property = Property(name="customerID", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_customerID, ShoppingCart_price, ShoppingCart_orderID}

# Relationships
User_User: BinaryAssociation = BinaryAssociation(
    name="User_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 1))
    }
)
SessionManager_User: BinaryAssociation = BinaryAssociation(
    name="SessionManager_User",
    ends={
        Property(name="user2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="sessionManager3", type=SessionManager, multiplicity=Multiplicity(0, 1))
    }
)
Customer_BooksOrder: BinaryAssociation = BinaryAssociation(
    name="Customer_BooksOrder",
    ends={
        Property(name="booksOrder4", type=BooksOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
BooksOrder_Book: BinaryAssociation = BinaryAssociation(
    name="BooksOrder_Book",
    ends={
        Property(name="book6", type=Book, multiplicity=Multiplicity(1, 9999)),
        Property(name="booksOrder7", type=BooksOrder, multiplicity=Multiplicity(1, 1))
    }
)
BooksOrder_Administrator: BinaryAssociation = BinaryAssociation(
    name="BooksOrder_Administrator",
    ends={
        Property(name="administrator8", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="booksOrder9", type=BooksOrder, multiplicity=Multiplicity(0, 9999))
    }
)
BookSet_Search: BinaryAssociation = BinaryAssociation(
    name="BookSet_Search",
    ends={
        Property(name="search10", type=Search, multiplicity=Multiplicity(0, 9999)),
        Property(name="bookSet11", type=BookSet, multiplicity=Multiplicity(0, 9999))
    }
)
BookSet_AdvSearch: BinaryAssociation = BinaryAssociation(
    name="BookSet_AdvSearch",
    ends={
        Property(name="advSearch12", type=AdvSearch, multiplicity=Multiplicity(0, 9999)),
        Property(name="bookSet13", type=BookSet, multiplicity=Multiplicity(0, 9999))
    }
)
SessionManager_Category: BinaryAssociation = BinaryAssociation(
    name="SessionManager_Category",
    ends={
        Property(name="category14", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="sessionManager15", type=SessionManager, multiplicity=Multiplicity(1, 1))
    }
)
Category_Book: BinaryAssociation = BinaryAssociation(
    name="Category_Book",
    ends={
        Property(name="book16", type=Book, multiplicity=Multiplicity(1, 1)),
        Property(name="category17", type=Category, multiplicity=Multiplicity(1, 9999))
    }
)
ShoppingCart_BooksOrder: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_BooksOrder",
    ends={
        Property(name="booksOrder18", type=BooksOrder, multiplicity=Multiplicity(1, 9999)),
        Property(name="shoppingCart19", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="shoppingCart20", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="customer21", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_klGBkZgOEemt1PHp7arfQg",
    types={User, SessionManager, Customer, BooksOrder, Book, Administrator, BookSet, Search, AdvSearch, Category, ShoppingCart},
    associations={User_User, SessionManager_User, Customer_BooksOrder, BooksOrder_Book, BooksOrder_Administrator, BookSet_Search, BookSet_AdvSearch, SessionManager_Category, Category_Book, ShoppingCart_BooksOrder, Customer_ShoppingCart},
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
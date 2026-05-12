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
CardInfo = Class(name="CardInfo")
Retailer = Class(name="Retailer")
User = Class(name="User")
Retailer_Cart = Class(name="Retailer_Cart")
Farmer = Class(name="Farmer")
AccountInfo = Class(name="AccountInfo")
Administrator = Class(name="Administrator")
rating___review = Class(name="rating___review")
Order = Class(name="Order")
Farmer_produces = Class(name="Farmer_produces")
Products = Class(name="Products")

# CardInfo class attributes and methods
CardInfo_ID: Property = Property(name="ID", type=IntegerType)
CardInfo_name: Property = Property(name="name", type=StringType)
CardInfo_number: Property = Property(name="number", type=IntegerType)
CardInfo_expiryDate: Property = Property(name="expiryDate", type=DateType)
CardInfo_CVV: Property = Property(name="CVV", type=IntegerType)
CardInfo_billingAddress: Property = Property(name="billingAddress", type=StringType)
CardInfo.attributes={CardInfo_number, CardInfo_ID, CardInfo_expiryDate, CardInfo_billingAddress, CardInfo_CVV, CardInfo_name}

# Retailer class attributes and methods
Retailer_userId: Property = Property(name="userId", type=IntegerType)
Retailer_name: Property = Property(name="name", type=StringType)
Retailer_emailId: Property = Property(name="emailId", type=StringType)
Retailer_address: Property = Property(name="address", type=StringType)
Retailer_phone: Property = Property(name="phone", type=IntegerType)
Retailer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Retailer_CardInfo: Property = Property(name="CardInfo", type=IntegerType)
Retailer_Photo: Property = Property(name="Photo", type=StringType)
Retailer.attributes={Retailer_name, Retailer_Photo, Retailer_dateOfBirth, Retailer_CardInfo, Retailer_userId, Retailer_phone, Retailer_emailId, Retailer_address}

# User class attributes and methods
User_Id: Property = Property(name="Id", type=IntegerType)
User_userName: Property = Property(name="userName", type=StringType)
User_userType: Property = Property(name="userType", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_userType, User_userName, User_password, User_Id}

# Retailer_Cart class attributes and methods
Retailer_Cart_userID: Property = Property(name="userID", type=IntegerType)
Retailer_Cart_product: Property = Property(name="product", type=Products)
Retailer_Cart_quantity___product: Property = Property(name="quantity___product", type=FloatType)
Retailer_Cart.attributes={Retailer_Cart_quantity___product, Retailer_Cart_product, Retailer_Cart_userID}

# Farmer class attributes and methods
Farmer_userId: Property = Property(name="userId", type=IntegerType)
Farmer_name: Property = Property(name="name", type=StringType)
Farmer_emailId: Property = Property(name="emailId", type=StringType)
Farmer_address: Property = Property(name="address", type=StringType)
Farmer_phone: Property = Property(name="phone", type=IntegerType)
Farmer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Farmer_type: Property = Property(name="type", type=StringType)
Farmer_accountInfoID: Property = Property(name="accountInfoID", type=IntegerType)
Farmer_CardInfo: Property = Property(name="CardInfo", type=StringType)
Farmer.attributes={Farmer_type, Farmer_dateOfBirth, Farmer_CardInfo, Farmer_address, Farmer_name, Farmer_emailId, Farmer_userId, Farmer_phone, Farmer_accountInfoID}

# AccountInfo class attributes and methods
AccountInfo_name: Property = Property(name="name", type=StringType)
AccountInfo_bankName: Property = Property(name="bankName", type=StringType)
AccountInfo_bankBranch: Property = Property(name="bankBranch", type=StringType)
AccountInfo_accountNumber: Property = Property(name="accountNumber", type=IntegerType)
AccountInfo_routingNumber: Property = Property(name="routingNumber", type=IntegerType)
AccountInfo_ID: Property = Property(name="ID", type=IntegerType)
AccountInfo.attributes={AccountInfo_routingNumber, AccountInfo_name, AccountInfo_bankName, AccountInfo_ID, AccountInfo_accountNumber, AccountInfo_bankBranch}

# Administrator class attributes and methods
Administrator_userId: Property = Property(name="userId", type=IntegerType)
Administrator_name: Property = Property(name="name", type=StringType)
Administrator_emailId: Property = Property(name="emailId", type=StringType)
Administrator_address: Property = Property(name="address", type=StringType)
Administrator_phone: Property = Property(name="phone", type=IntegerType)
Administrator_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Administrator_adminType: Property = Property(name="adminType", type=StringType)
Administrator.attributes={Administrator_dateOfBirth, Administrator_adminType, Administrator_emailId, Administrator_address, Administrator_name, Administrator_phone, Administrator_userId}

# rating___review class attributes and methods
rating___review_ID: Property = Property(name="ID", type=IntegerType)
rating___review_name: Property = Property(name="name", type=StringType)
rating___review_rating: Property = Property(name="rating", type=IntegerType)
rating___review_reviews: Property = Property(name="reviews", type=StringType)
rating___review_retailerID: Property = Property(name="retailerID", type=StringType)
rating___review_inventoryID: Property = Property(name="inventoryID", type=StringType)
rating___review.attributes={rating___review_rating, rating___review_inventoryID, rating___review_reviews, rating___review_name, rating___review_ID, rating___review_retailerID}

# Order class attributes and methods
Order_transactionID: Property = Property(name="transactionID", type=IntegerType)
Order_purchaseDate: Property = Property(name="purchaseDate", type=DateType)
Order_cardDetails: Property = Property(name="cardDetails", type=StringType)
Order_productDetails: Property = Property(name="productDetails", type=StringType)
Order.attributes={Order_transactionID, Order_productDetails, Order_purchaseDate, Order_cardDetails}

# Farmer_produces class attributes and methods
Farmer_produces_ID: Property = Property(name="ID", type=IntegerType)
Farmer_produces_farmerID: Property = Property(name="farmerID", type=IntegerType)
Farmer_produces_productList: Property = Property(name="productList", type=StringType)
Farmer_produces.attributes={Farmer_produces_productList, Farmer_produces_ID, Farmer_produces_farmerID}

# Products class attributes and methods
Products_name: Property = Property(name="name", type=StringType)
Products_ID: Property = Property(name="ID", type=IntegerType)
Products_selling_price: Property = Property(name="selling_price", type=FloatType)
Products_description: Property = Property(name="description", type=StringType)
Products_discount: Property = Property(name="discount", type=IntegerType)
Products_rating: Property = Property(name="rating", type=IntegerType)
Products_reviews: Property = Property(name="reviews", type=StringType)
Products_farmerID: Property = Property(name="farmerID", type=StringType)
Products_inventoryID: Property = Property(name="inventoryID", type=StringType)
Products.attributes={Products_inventoryID, Products_discount, Products_description, Products_selling_price, Products_rating, Products_farmerID, Products_reviews, Products_ID, Products_name}

# Relationships
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=Retailer_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="customer1", type=Retailer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_CardInfo: BinaryAssociation = BinaryAssociation(
    name="Customer_CardInfo",
    ends={
        Property(name="cardInfo2", type=CardInfo, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Retailer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order4", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Retailer, multiplicity=Multiplicity(0, 1))
    }
)
Seller_AccountInfo: BinaryAssociation = BinaryAssociation(
    name="Seller_AccountInfo",
    ends={
        Property(name="accountInfo6", type=AccountInfo, multiplicity=Multiplicity(0, 1)),
        Property(name="seller7", type=Farmer, multiplicity=Multiplicity(0, 1))
    }
)
Product_Farmer_Farmer: BinaryAssociation = BinaryAssociation(
    name="Product_Farmer_Farmer",
    ends={
        Property(name="farmer8", type=Farmer, multiplicity=Multiplicity(0, 1)),
        Property(name="product_Farmer9", type=Products, multiplicity=Multiplicity(0, 1))
    }
)
Order_Farmer: BinaryAssociation = BinaryAssociation(
    name="Order_Farmer",
    ends={
        Property(name="farmer10", type=Farmer, multiplicity=Multiplicity(0, 1)),
        Property(name="order11", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_679a7c49_2d55_4bdc_bb6b_f00597a42ccb",
    types={CardInfo, Retailer, User, Retailer_Cart, Farmer, AccountInfo, Administrator, rating___review, Order, Farmer_produces, Products},
    associations={Customer_ShoppingCart, Customer_CardInfo, Customer_Order, Seller_AccountInfo, Product_Farmer_Farmer, Order_Farmer},
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
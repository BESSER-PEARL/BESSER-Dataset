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
BankAccount = Class(name="BankAccount")
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")
ClassG = Class(name="ClassG")
ClassJ = Class(name="ClassJ")
ClassH = Class(name="ClassH")
ClassK = Class(name="ClassK")
ClassL = Class(name="ClassL")
ClassM = Class(name="ClassM")
ClassN = Class(name="ClassN")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
Admin = Class(name="Admin")
ProductDetail = Class(name="ProductDetail")
_unnamed = Class(name="_unnamed")
ProductShow2 = Class(name="ProductShow2")
Class_ = Class(name="Class")
Shoe = Class(name="Shoe")
ProductShow = Class(name="ProductShow")
User_abstract_ = Class(name="User_abstract_")
Customer = Class(name="Customer")
Database = Class(name="Database")
DBController = Class(name="DBController")

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_balance, BankAccount_ownerName}

# ClassA class attributes and methods
ClassA_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassA_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassA_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassA_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassA.attributes={ClassA_privateAttribute, ClassA_protectedAttribute, ClassA_publicAttribute, ClassA_packageAttribute}

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_privateAttribute, ClassC_protectedAttribute, ClassC_packageAttribute, ClassC_publicAttribute}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# ClassG class attributes and methods

# ClassJ class attributes and methods

# ClassH class attributes and methods

# ClassK class attributes and methods

# ClassL class attributes and methods

# ClassM class attributes and methods

# ClassN class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# Admin class attributes and methods

# ProductDetail class attributes and methods
ProductDetail_productId: Property = Property(name="productId", type=StringType)
ProductDetail_productName: Property = Property(name="productName", type=StringType)
ProductDetail_category: Property = Property(name="category", type=StringType)
ProductDetail_brand: Property = Property(name="brand", type=StringType)
ProductDetail_sex: Property = Property(name="sex", type=IntegerType)
ProductDetail_priceCost: Property = Property(name="priceCost", type=FloatType)
ProductDetail.attributes={ProductDetail_category, ProductDetail_productId, ProductDetail_priceCost, ProductDetail_brand, ProductDetail_sex, ProductDetail_productName}

# _unnamed class attributes and methods

# ProductShow2 class attributes and methods
ProductShow2_productId: Property = Property(name="productId", type=StringType)
ProductShow2_productName: Property = Property(name="productName", type=StringType)
ProductShow2_category: Property = Property(name="category", type=StringType)
ProductShow2_brand: Property = Property(name="brand", type=StringType)
ProductShow2_sex: Property = Property(name="sex", type=IntegerType)
ProductShow2_priceCost: Property = Property(name="priceCost", type=FloatType)
ProductShow2.attributes={ProductShow2_productId, ProductShow2_sex, ProductShow2_category, ProductShow2_brand, ProductShow2_productName, ProductShow2_priceCost}

# Class class attributes and methods

# Shoe class attributes and methods
Shoe_productId: Property = Property(name="productId", type=StringType)
Shoe_productName: Property = Property(name="productName", type=StringType)
Shoe_category: Property = Property(name="category", type=StringType)
Shoe_brand: Property = Property(name="brand", type=StringType)
Shoe_brand2: Property = Property(name="brand2", type=StringType)
Shoe_size: Property = Property(name="size", type=IntegerType)
Shoe_sex: Property = Property(name="sex", type=IntegerType)
Shoe_priceCost: Property = Property(name="priceCost", type=FloatType)
Shoe_description: Property = Property(name="description", type=StringType)
Shoe_color: Property = Property(name="color", type=StringType)
Shoe.attributes={Shoe_color, Shoe_description, Shoe_sex, Shoe_priceCost, Shoe_brand2, Shoe_productName, Shoe_brand, Shoe_size, Shoe_category, Shoe_productId}

# ProductShow class attributes and methods
ProductShow_productId: Property = Property(name="productId", type=StringType)
ProductShow_productName: Property = Property(name="productName", type=StringType)
ProductShow_category: Property = Property(name="category", type=StringType)
ProductShow_brand: Property = Property(name="brand", type=StringType)
ProductShow_sex: Property = Property(name="sex", type=IntegerType)
ProductShow_priceSale: Property = Property(name="priceSale", type=FloatType)
ProductShow_image: Property = Property(name="image", type=StringType)
ProductShow.attributes={ProductShow_sex, ProductShow_productId, ProductShow_category, ProductShow_priceSale, ProductShow_image, ProductShow_brand, ProductShow_productName}

# User_abstract_ class attributes and methods
User_abstract__name: Property = Property(name="name", type=StringType)
User_abstract__password: Property = Property(name="password", type=StringType)
User_abstract__email: Property = Property(name="email", type=StringType)
User_abstract__userId: Property = Property(name="userId", type=StringType)
User_abstract_.attributes={User_abstract__email, User_abstract__userId, User_abstract__name, User_abstract__password}

# Customer class attributes and methods
Customer_phonenumber: Property = Property(name="phonenumber", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_creditCardInfo: Property = Property(name="creditCardInfo", type=StringType)
Customer_attribute: Property = Property(name="attribute", type=StringType)
Customer.attributes={Customer_creditCardInfo, Customer_phonenumber, Customer_attribute, Customer_address}

# Database class attributes and methods
Database_instance: Property = Property(name="instance", type=Database)
Database_url: Property = Property(name="url", type=StringType)
Database_username: Property = Property(name="username", type=StringType)
Database_password: Property = Property(name="password", type=StringType)
Database.attributes={Database_instance, Database_username, Database_url, Database_password}

# DBController class attributes and methods
DBController_CustomerLogin: Property = Property(name="CustomerLogin", type=User_abstract_)
DBController.attributes={DBController_CustomerLogin}

# Relationships
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=ClassE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=ClassD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopy",
    ends={
        Property(name="classG2", type=ClassG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=ClassF, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopyCopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopyCopy",
    ends={
        Property(name="classG4", type=ClassJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=ClassH, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hbadYGUuEeqK2M3E1LfZ7Q",
    types={BankAccount, ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassJ, ClassH, ClassK, ClassL, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, Admin, ProductDetail, _unnamed, ProductShow2, Class_, Shoe, ProductShow, User_abstract_, Customer, Database, DBController, Enumeration_},
    associations={ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy},
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
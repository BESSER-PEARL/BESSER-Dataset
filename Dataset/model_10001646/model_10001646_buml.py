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
_LoginCredential = Class(name="_LoginCredential")
_User = Class(name="_User")
_ProductRating = Class(name="_ProductRating")
_Product = Class(name="_Product")
_ProductType = Class(name="_ProductType")
_OrderDetail = Class(name="_OrderDetail")
_PaymentInfo = Class(name="_PaymentInfo")
_UserType = Class(name="_UserType")

# _LoginCredential class attributes and methods
_LoginCredential__loginid: Property = Property(name="_loginid", type=StringType)
_LoginCredential__password: Property = Property(name="_password", type=StringType)
_LoginCredential.attributes={_LoginCredential__loginid, _LoginCredential__password}

# _User class attributes and methods
_User__username: Property = Property(name="_username", type=StringType)
_User__address: Property = Property(name="_address", type=StringType)
_User__phone: Property = Property(name="_phone", type=IntegerType)
_User__email: Property = Property(name="_email", type=StringType)
_User__usertypeid: Property = Property(name="_usertypeid", type=IntegerType)
_User__logincredentialsid: Property = Property(name="_logincredentialsid", type=IntegerType)
_User.attributes={_User__username, _User__email, _User__phone, _User__address, _User__usertypeid, _User__logincredentialsid}

# _ProductRating class attributes and methods
_ProductRating__rating: Property = Property(name="_rating", type=IntegerType)
_ProductRating__userid: Property = Property(name="_userid", type=IntegerType)
_ProductRating__productid: Property = Property(name="_productid", type=IntegerType)
_ProductRating.attributes={_ProductRating__productid, _ProductRating__userid, _ProductRating__rating}

# _Product class attributes and methods
_Product__name: Property = Property(name="_name", type=StringType)
_Product__modelno: Property = Property(name="_modelno", type=StringType)
_Product__description: Property = Property(name="_description", type=StringType)
_Product__stock: Property = Property(name="_stock", type=IntegerType)
_Product__price: Property = Property(name="_price", type=IntegerType)
_Product__producttypeid: Property = Property(name="_producttypeid", type=IntegerType)
_Product.attributes={_Product__stock, _Product__price, _Product__description, _Product__modelno, _Product__producttypeid, _Product__name}

# _ProductType class attributes and methods
_ProductType__type: Property = Property(name="_type", type=StringType)
_ProductType.attributes={_ProductType__type}

# _OrderDetail class attributes and methods
_OrderDetail__productid: Property = Property(name="_productid", type=IntegerType)
_OrderDetail__quantity: Property = Property(name="_quantity", type=IntegerType)
_OrderDetail__orderdate: Property = Property(name="_orderdate", type=DateType)
_OrderDetail__totalamount: Property = Property(name="_totalamount", type=IntegerType)
_OrderDetail__userid: Property = Property(name="_userid", type=IntegerType)
_OrderDetail.attributes={_OrderDetail__productid, _OrderDetail__userid, _OrderDetail__orderdate, _OrderDetail__totalamount, _OrderDetail__quantity}

# _PaymentInfo class attributes and methods
_PaymentInfo__cardno: Property = Property(name="_cardno", type=IntegerType)
_PaymentInfo__cvv: Property = Property(name="_cvv", type=IntegerType)
_PaymentInfo__expirydate: Property = Property(name="_expirydate", type=DateType)
_PaymentInfo__cardname: Property = Property(name="_cardname", type=StringType)
_PaymentInfo__userid: Property = Property(name="_userid", type=IntegerType)
_PaymentInfo.attributes={_PaymentInfo__userid, _PaymentInfo__expirydate, _PaymentInfo__cardname, _PaymentInfo__cvv, _PaymentInfo__cardno}

# _UserType class attributes and methods
_UserType__userrole: Property = Property(name="_userrole", type=StringType)
_UserType.attributes={_UserType__userrole}

# Relationships
Ratings_Customer: BinaryAssociation = BinaryAssociation(
    name="Ratings_Customer",
    ends={
        Property(name="_rated_by2", type=_User, multiplicity=Multiplicity(0, 9999)),
        Property(name="_rates3", type=_ProductRating, multiplicity=Multiplicity(1, 1))
    }
)
ProductType_Product: BinaryAssociation = BinaryAssociation(
    name="ProductType_Product",
    ends={
        Property(name="_has_products4", type=_Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="_type_of5", type=_ProductType, multiplicity=Multiplicity(1, 1))
    }
)
_Customer__PaymentInfo: BinaryAssociation = BinaryAssociation(
    name="_Customer__PaymentInfo",
    ends={
        Property(name="_has6", type=_PaymentInfo, multiplicity=Multiplicity(1, 9999)),
        Property(name="_belongs_to7", type=_User, multiplicity=Multiplicity(1, 1))
    }
)
_Product__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Product__OrderDetails",
    ends={
        Property(name="_is_in8", type=_OrderDetail, multiplicity=Multiplicity(0, 9999)),
        Property(name="_contains9", type=_Product, multiplicity=Multiplicity(0, 9999))
    }
)
_Customer__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Customer__OrderDetails",
    ends={
        Property(name="_orders10", type=_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="_ordered_by11", type=_User, multiplicity=Multiplicity(1, 1))
    }
)
_UserType__Customer: BinaryAssociation = BinaryAssociation(
    name="_UserType__Customer",
    ends={
        Property(name="_has12", type=_User, multiplicity=Multiplicity(0, 9999)),
        Property(name="_belongs_to13", type=_UserType, multiplicity=Multiplicity(1, 1))
    }
)
_ProductRating__Product: BinaryAssociation = BinaryAssociation(
    name="_ProductRating__Product",
    ends={
        Property(name="_is_for14", type=_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="_has_rating15", type=_ProductRating, multiplicity=Multiplicity(0, 9999))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="_for0", type=_User, multiplicity=Multiplicity(1, 1)),
        Property(name="_logs_in_with1", type=_LoginCredential, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_LYCGQEakEeqonN_RS9oRzw",
    types={_LoginCredential, _User, _ProductRating, _Product, _ProductType, _OrderDetail, _PaymentInfo, _UserType},
    associations={Ratings_Customer, ProductType_Product, _Customer__PaymentInfo, _Product__OrderDetails, _Customer__OrderDetails, _UserType__Customer, _ProductRating__Product, WebUser_Customer},
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
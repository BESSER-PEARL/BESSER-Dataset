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
Card = Class(name="Card")
Transaction = Class(name="Transaction")
_Fee = Class(name="_Fee")
_TransactionType = Class(name="_TransactionType")
_OrderDetail = Class(name="_OrderDetail")
_PaymentInfo = Class(name="_PaymentInfo")

# _LoginCredential class attributes and methods
_LoginCredential__loginid: Property = Property(name="_loginid", type=StringType)
_LoginCredential__password: Property = Property(name="_password", type=StringType)
_LoginCredential.attributes={_LoginCredential__password, _LoginCredential__loginid}

# Card class attributes and methods
Card__username: Property = Property(name="_username", type=StringType)
Card__address: Property = Property(name="_address", type=StringType)
Card__phone: Property = Property(name="_phone", type=IntegerType)
Card__email: Property = Property(name="_email", type=StringType)
Card__usertypeid: Property = Property(name="_usertypeid", type=IntegerType)
Card__logincredentialsid: Property = Property(name="_logincredentialsid", type=IntegerType)
Card.attributes={Card__logincredentialsid, Card__address, Card__email, Card__phone, Card__username, Card__usertypeid}

# Transaction class attributes and methods
Transaction_shipmentNumber: Property = Property(name="shipmentNumber", type=IntegerType)
Transaction_orderId: Property = Property(name="orderId", type=IntegerType)
Transaction.attributes={Transaction_shipmentNumber, Transaction_orderId}

# _Fee class attributes and methods
_Fee__name: Property = Property(name="_name", type=StringType)
_Fee__description: Property = Property(name="_description", type=StringType)
_Fee__stock: Property = Property(name="_stock", type=IntegerType)
_Fee__price: Property = Property(name="_price", type=IntegerType)
_Fee__producttypeid: Property = Property(name="_producttypeid", type=IntegerType)
_Fee.attributes={_Fee__price, _Fee__stock, _Fee__producttypeid, _Fee__name, _Fee__description}

# _TransactionType class attributes and methods
_TransactionType__type: Property = Property(name="_type", type=StringType)
_TransactionType.attributes={_TransactionType__type}

# _OrderDetail class attributes and methods
_OrderDetail__productid: Property = Property(name="_productid", type=IntegerType)
_OrderDetail__quantity: Property = Property(name="_quantity", type=IntegerType)
_OrderDetail__orderdate: Property = Property(name="_orderdate", type=DateType)
_OrderDetail__totalamount: Property = Property(name="_totalamount", type=IntegerType)
_OrderDetail__userid: Property = Property(name="_userid", type=IntegerType)
_OrderDetail_OrderId: Property = Property(name="OrderId", type=IntegerType)
_OrderDetail_paymentInfoId: Property = Property(name="paymentInfoId", type=IntegerType)
_OrderDetail.attributes={_OrderDetail_OrderId, _OrderDetail__userid, _OrderDetail__orderdate, _OrderDetail__productid, _OrderDetail__quantity, _OrderDetail__totalamount, _OrderDetail_paymentInfoId}

# _PaymentInfo class attributes and methods
_PaymentInfo__cardno: Property = Property(name="_cardno", type=IntegerType)
_PaymentInfo__cvv: Property = Property(name="_cvv", type=IntegerType)
_PaymentInfo__expirydate: Property = Property(name="_expirydate", type=DateType)
_PaymentInfo__cardname: Property = Property(name="_cardname", type=StringType)
_PaymentInfo__userid: Property = Property(name="_userid", type=IntegerType)
_PaymentInfo_paymentId: Property = Property(name="paymentId", type=IntegerType)
_PaymentInfo.attributes={_PaymentInfo_paymentId, _PaymentInfo__expirydate, _PaymentInfo__cardname, _PaymentInfo__cvv, _PaymentInfo__userid, _PaymentInfo__cardno}

# Relationships
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="_for0", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="_logs_in_with1", type=_LoginCredential, multiplicity=Multiplicity(1, 1))
    }
)
Ratings_Customer: BinaryAssociation = BinaryAssociation(
    name="Ratings_Customer",
    ends={
        Property(name="_Delivers2", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="_ships3", type=Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
ProductType_Product: BinaryAssociation = BinaryAssociation(
    name="ProductType_Product",
    ends={
        Property(name="_has_products4", type=_Fee, multiplicity=Multiplicity(0, 9999)),
        Property(name="_type_of5", type=_TransactionType, multiplicity=Multiplicity(1, 1))
    }
)
_Product__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Product__OrderDetails",
    ends={
        Property(name="_is_in6", type=_OrderDetail, multiplicity=Multiplicity(0, 9999)),
        Property(name="_contains7", type=_Fee, multiplicity=Multiplicity(0, 9999))
    }
)
_Customer__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Customer__OrderDetails",
    ends={
        Property(name="_orders8", type=_OrderDetail, multiplicity=Multiplicity(1, 9999)),
        Property(name="receives9", type=Card, multiplicity=Multiplicity(1, 1))
    }
)
_PaymentInfo__OrderDetail: BinaryAssociation = BinaryAssociation(
    name="_PaymentInfo__OrderDetail",
    ends={
        Property(name="_OrderDetail10", type=_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="_PaymentInfo11", type=_PaymentInfo, multiplicity=Multiplicity(1, 1))
    }
)
Farmer__ProductType: BinaryAssociation = BinaryAssociation(
    name="Farmer__ProductType",
    ends={
        Property(name="_Add_Product_Type12", type=_TransactionType, multiplicity=Multiplicity(0, 9999)),
        Property(name="farmer13", type=Card, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vQ6JAPcOEemUnaCK8fYTPQ",
    types={_LoginCredential, Card, Transaction, _Fee, _TransactionType, _OrderDetail, _PaymentInfo},
    associations={WebUser_Customer, Ratings_Customer, ProductType_Product, _Product__OrderDetails, _Customer__OrderDetails, _PaymentInfo__OrderDetail, Farmer__ProductType},
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
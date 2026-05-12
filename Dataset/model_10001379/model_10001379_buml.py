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
Farmer = Class(name="Farmer")
_Shipment = Class(name="_Shipment")
_Product = Class(name="_Product")
_ProductType = Class(name="_ProductType")
_OrderDetail = Class(name="_OrderDetail")
_PaymentInfo = Class(name="_PaymentInfo")

# _LoginCredential class attributes and methods
_LoginCredential__loginid: Property = Property(name="_loginid", type=StringType)
_LoginCredential__password: Property = Property(name="_password", type=StringType)
_LoginCredential.attributes={_LoginCredential__password, _LoginCredential__loginid}

# Farmer class attributes and methods
Farmer__username: Property = Property(name="_username", type=StringType)
Farmer__address: Property = Property(name="_address", type=StringType)
Farmer__phone: Property = Property(name="_phone", type=IntegerType)
Farmer__email: Property = Property(name="_email", type=StringType)
Farmer__usertypeid: Property = Property(name="_usertypeid", type=IntegerType)
Farmer__logincredentialsid: Property = Property(name="_logincredentialsid", type=IntegerType)
Farmer.attributes={Farmer__usertypeid, Farmer__phone, Farmer__address, Farmer__logincredentialsid, Farmer__email, Farmer__username}

# _Shipment class attributes and methods
_Shipment_shipmentNumber: Property = Property(name="shipmentNumber", type=IntegerType)
_Shipment_orderId: Property = Property(name="orderId", type=IntegerType)
_Shipment.attributes={_Shipment_orderId, _Shipment_shipmentNumber}

# _Product class attributes and methods
_Product__name: Property = Property(name="_name", type=StringType)
_Product__description: Property = Property(name="_description", type=StringType)
_Product__stock: Property = Property(name="_stock", type=IntegerType)
_Product__price: Property = Property(name="_price", type=IntegerType)
_Product__producttypeid: Property = Property(name="_producttypeid", type=IntegerType)
_Product.attributes={_Product__name, _Product__price, _Product__stock, _Product__description, _Product__producttypeid}

# _ProductType class attributes and methods
_ProductType__type: Property = Property(name="_type", type=StringType)
_ProductType.attributes={_ProductType__type}

# _OrderDetail class attributes and methods
_OrderDetail__productid: Property = Property(name="_productid", type=IntegerType)
_OrderDetail__quantity: Property = Property(name="_quantity", type=IntegerType)
_OrderDetail__orderdate: Property = Property(name="_orderdate", type=DateType)
_OrderDetail__totalamount: Property = Property(name="_totalamount", type=IntegerType)
_OrderDetail__userid: Property = Property(name="_userid", type=IntegerType)
_OrderDetail_OrderId: Property = Property(name="OrderId", type=IntegerType)
_OrderDetail_paymentInfoId: Property = Property(name="paymentInfoId", type=IntegerType)
_OrderDetail.attributes={_OrderDetail__userid, _OrderDetail__totalamount, _OrderDetail__quantity, _OrderDetail__productid, _OrderDetail__orderdate, _OrderDetail_paymentInfoId, _OrderDetail_OrderId}

# _PaymentInfo class attributes and methods
_PaymentInfo__cardno: Property = Property(name="_cardno", type=IntegerType)
_PaymentInfo__cvv: Property = Property(name="_cvv", type=IntegerType)
_PaymentInfo__expirydate: Property = Property(name="_expirydate", type=DateType)
_PaymentInfo__cardname: Property = Property(name="_cardname", type=StringType)
_PaymentInfo__userid: Property = Property(name="_userid", type=IntegerType)
_PaymentInfo_paymentId: Property = Property(name="paymentId", type=IntegerType)
_PaymentInfo.attributes={_PaymentInfo__cardname, _PaymentInfo__expirydate, _PaymentInfo_paymentId, _PaymentInfo__cardno, _PaymentInfo__userid, _PaymentInfo__cvv}

# Relationships
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="_for0", type=Farmer, multiplicity=Multiplicity(1, 1)),
        Property(name="_logs_in_with1", type=_LoginCredential, multiplicity=Multiplicity(1, 1))
    }
)
Ratings_Customer: BinaryAssociation = BinaryAssociation(
    name="Ratings_Customer",
    ends={
        Property(name="_Delivers2", type=Farmer, multiplicity=Multiplicity(1, 1)),
        Property(name="_ships3", type=_Shipment, multiplicity=Multiplicity(0, 9999))
    }
)
ProductType_Product: BinaryAssociation = BinaryAssociation(
    name="ProductType_Product",
    ends={
        Property(name="_has_products4", type=_Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="_type_of5", type=_ProductType, multiplicity=Multiplicity(1, 1))
    }
)
_Product__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Product__OrderDetails",
    ends={
        Property(name="_is_in6", type=_OrderDetail, multiplicity=Multiplicity(0, 9999)),
        Property(name="_contains7", type=_Product, multiplicity=Multiplicity(0, 9999))
    }
)
_Customer__OrderDetails: BinaryAssociation = BinaryAssociation(
    name="_Customer__OrderDetails",
    ends={
        Property(name="_orders8", type=_OrderDetail, multiplicity=Multiplicity(1, 9999)),
        Property(name="receives9", type=Farmer, multiplicity=Multiplicity(1, 1))
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
        Property(name="_Add_Product_Type12", type=_ProductType, multiplicity=Multiplicity(0, 9999)),
        Property(name="farmer13", type=Farmer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3HAuoPXGEemEXt2Xl4w_3Q",
    types={_LoginCredential, Farmer, _Shipment, _Product, _ProductType, _OrderDetail, _PaymentInfo},
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
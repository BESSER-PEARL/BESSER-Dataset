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
Bill_Details: Enumeration = Enumeration(
    name="Bill_Details",
    literals={
            
    }
)

Booking_Status: Enumeration = Enumeration(
    name="Booking_Status",
    literals={
            
    }
)

# Classes
Booking_Entity = Class(name="Booking_Entity")
Payment = Class(name="Payment")
PostStay_Entity = Class(name="PostStay_Entity")
CheckIn_Entity = Class(name="CheckIn_Entity")
User_Entity = Class(name="User_Entity")
StayIn_Entity = Class(name="StayIn_Entity")
CheckOut_Entity = Class(name="CheckOut_Entity")
FeedBack = Class(name="FeedBack")

# Booking_Entity class attributes and methods
Booking_Entity_address: Property = Property(name="address", type=StringType)
Booking_Entity_phone: Property = Property(name="phone", type=StringType)
Booking_Entity_email: Property = Property(name="email", type=StringType)
Booking_Entity_CheckInDate: Property = Property(name="CheckInDate", type=DateType)
Booking_Entity_NoOfDays: Property = Property(name="NoOfDays", type=IntegerType)
Booking_Entity.attributes={Booking_Entity_phone, Booking_Entity_address, Booking_Entity_CheckInDate, Booking_Entity_NoOfDays, Booking_Entity_email}

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_total, Payment_details, Payment_paidDate}

# PostStay_Entity class attributes and methods
PostStay_Entity_ThanksMessage: Property = Property(name="ThanksMessage", type=StringType)
PostStay_Entity_DiscountPoints: Property = Property(name="DiscountPoints", type=StringType)
PostStay_Entity_PromotionPoints: Property = Property(name="PromotionPoints", type=StringType)
PostStay_Entity.attributes={PostStay_Entity_DiscountPoints, PostStay_Entity_PromotionPoints, PostStay_Entity_ThanksMessage}

# CheckIn_Entity class attributes and methods
CheckIn_Entity_PickUpAddress: Property = Property(name="PickUpAddress", type=StringType)
CheckIn_Entity_paymentMode: Property = Property(name="paymentMode", type=StringType)
CheckIn_Entity_CheckInStatus: Property = Property(name="CheckInStatus", type=StringType)
CheckIn_Entity_QRCode: Property = Property(name="QRCode", type=StringType)
CheckIn_Entity_MobileKey: Property = Property(name="MobileKey", type=StringType)
CheckIn_Entity.attributes={CheckIn_Entity_paymentMode, CheckIn_Entity_CheckInStatus, CheckIn_Entity_MobileKey, CheckIn_Entity_PickUpAddress, CheckIn_Entity_QRCode}

# User_Entity class attributes and methods
User_Entity_login: Property = Property(name="login", type=StringType)
User_Entity_password: Property = Property(name="password", type=StringType)
User_Entity_City: Property = Property(name="City", type=StringType)
User_Entity_Email: Property = Property(name="Email", type=StringType)
User_Entity.attributes={User_Entity_login, User_Entity_password, User_Entity_City, User_Entity_Email}

# StayIn_Entity class attributes and methods
StayIn_Entity_EntertainMentList: Property = Property(name="EntertainMentList", type=StringType)
StayIn_Entity_oodList: Property = Property(name="oodList", type=StringType)
StayIn_Entity_InPremisesList: Property = Property(name="InPremisesList", type=StringType)
StayIn_Entity_promotionsList: Property = Property(name="promotionsList", type=StringType)
StayIn_Entity_placeOfInterest: Property = Property(name="placeOfInterest", type=FloatType)
StayIn_Entity_status: Property = Property(name="status", type=Booking_Status)
StayIn_Entity.attributes={StayIn_Entity_InPremisesList, StayIn_Entity_oodList, StayIn_Entity_EntertainMentList, StayIn_Entity_placeOfInterest, StayIn_Entity_status, StayIn_Entity_promotionsList}

# CheckOut_Entity class attributes and methods
CheckOut_Entity_ItemisedBillDetails: Property = Property(name="ItemisedBillDetails", type=Bill_Details)
CheckOut_Entity_price: Property = Property(name="price", type=FloatType)
CheckOut_Entity.attributes={CheckOut_Entity_ItemisedBillDetails, CheckOut_Entity_price}

# FeedBack class attributes and methods
FeedBack_Rating: Property = Property(name="Rating", type=StringType)
FeedBack_FeedBackMessage: Property = Property(name="FeedBackMessage", type=StringType)
FeedBack.attributes={FeedBack_Rating, FeedBack_FeedBackMessage}

# Relationships
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="Start_Resedentz2", type=PostStay_Entity, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=User_Entity, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="Booking4", type=Booking_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser5", type=User_Entity, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="undefined6", type=PostStay_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="undefined7", type=CheckIn_Entity, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="undefined8", type=CheckOut_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="sc9", type=PostStay_Entity, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="Items10", type=CheckOut_Entity, multiplicity=Multiplicity(0, 9999)),
        Property(name="Feed_Back11", type=FeedBack, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items12", type=CheckOut_Entity, multiplicity=Multiplicity(1, 9999)),
        Property(name="order13", type=StayIn_Entity, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order14", type=StayIn_Entity, multiplicity=Multiplicity(0, 9999)),
        Property(name="undefined15", type=CheckIn_Entity, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order16", type=StayIn_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="payment17", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=CheckOut_Entity, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c96d076f_6a61_4cf9_9288_a9d661d79147",
    types={Booking_Entity, Payment, PostStay_Entity, CheckIn_Entity, User_Entity, StayIn_Entity, CheckOut_Entity, FeedBack, Bill_Details, Booking_Status},
    associations={WebUser_ShoppingCart, WebUser_Customer, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order, Account_Payment},
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
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
TrackOrder = Class(name="TrackOrder")
Store = Class(name="Store")
void_Interface = Class(name="void_Interface")
ReviewOrder = Class(name="ReviewOrder")
OrderHistory = Class(name="OrderHistory")
ConfirmOrder = Class(name="ConfirmOrder")
Categories = Class(name="Categories")
PlaceOrder = Class(name="PlaceOrder")
UserRegisteration = Class(name="UserRegisteration")
Login = Class(name="Login")
CartItems = Class(name="CartItems")
CompanyAddItem = Class(name="CompanyAddItem")
CompanyAddRider = Class(name="CompanyAddRider")
phon = Class(name="phon")
CompanyAssignRider = Class(name="CompanyAssignRider")
CompanyOrderHistory = Class(name="CompanyOrderHistory")
CompanyTrackOrder = Class(name="CompanyTrackOrder")
Order = Class(name="Order")
RiderStatusUpdate = Class(name="RiderStatusUpdate")

# TrackOrder class attributes and methods
TrackOrder_OrderTime_Date: Property = Property(name="OrderTime_Date", type=StringType)
TrackOrder_OrderTrack: Property = Property(name="OrderTrack", type=StringType)
TrackOrder.attributes={TrackOrder_OrderTime_Date, TrackOrder_OrderTrack}

# Store class attributes and methods
Store_Name: Property = Property(name="Name", type=StringType)
Store.attributes={Store_Name}

# void_Interface class attributes and methods

# ReviewOrder class attributes and methods
ReviewOrder_OrderTime_Date: Property = Property(name="OrderTime_Date", type=StringType)
ReviewOrder_RiderName: Property = Property(name="RiderName", type=StringType)
ReviewOrder_Review: Property = Property(name="Review", type=StringType)
ReviewOrder.attributes={ReviewOrder_Review, ReviewOrder_OrderTime_Date, ReviewOrder_RiderName}

# OrderHistory class attributes and methods
OrderHistory_OrderReview: Property = Property(name="OrderReview", type=StringType)
OrderHistory_OrderStatus: Property = Property(name="OrderStatus", type=StringType)
OrderHistory_OrderDate_Time: Property = Property(name="OrderDate_Time", type=StringType)
OrderHistory_OrderRider: Property = Property(name="OrderRider", type=StringType)
OrderHistory.attributes={OrderHistory_OrderReview, OrderHistory_OrderStatus, OrderHistory_OrderDate_Time, OrderHistory_OrderRider}

# ConfirmOrder class attributes and methods
ConfirmOrder_OrderName: Property = Property(name="OrderName", type=StringType)
ConfirmOrder_OrderPrice: Property = Property(name="OrderPrice", type=StringType)
ConfirmOrder_Quantity: Property = Property(name="Quantity", type=StringType)
ConfirmOrder_StoreName: Property = Property(name="StoreName", type=StringType)
ConfirmOrder.attributes={ConfirmOrder_StoreName, ConfirmOrder_Quantity, ConfirmOrder_OrderName, ConfirmOrder_OrderPrice}

# Categories class attributes and methods
Categories_Categories: Property = Property(name="Categories", type=StringType)
Categories.attributes={Categories_Categories}

# PlaceOrder class attributes and methods
PlaceOrder_Name: Property = Property(name="Name", type=StringType)
PlaceOrder_Price: Property = Property(name="Price", type=StringType)
PlaceOrder.attributes={PlaceOrder_Price, PlaceOrder_Name}

# UserRegisteration class attributes and methods
UserRegisteration_FirstName: Property = Property(name="FirstName", type=StringType)
UserRegisteration_LastName: Property = Property(name="LastName", type=StringType)
UserRegisteration_UserName: Property = Property(name="UserName", type=StringType)
UserRegisteration_Email: Property = Property(name="Email", type=StringType)
UserRegisteration_Password: Property = Property(name="Password", type=StringType)
UserRegisteration_Address: Property = Property(name="Address", type=StringType)
UserRegisteration_Phone: Property = Property(name="Phone", type=StringType)
UserRegisteration.attributes={UserRegisteration_FirstName, UserRegisteration_Password, UserRegisteration_UserName, UserRegisteration_Address, UserRegisteration_Email, UserRegisteration_LastName, UserRegisteration_Phone}

# Login class attributes and methods
Login_Email: Property = Property(name="Email", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Email, Login_Password}

# CartItems class attributes and methods
CartItems_Name: Property = Property(name="Name", type=StringType)
CartItems_Price: Property = Property(name="Price", type=StringType)
CartItems.attributes={CartItems_Price, CartItems_Name}

# CompanyAddItem class attributes and methods
CompanyAddItem_Name: Property = Property(name="Name", type=StringType)
CompanyAddItem_Price: Property = Property(name="Price", type=StringType)
CompanyAddItem_Description: Property = Property(name="Description", type=StringType)
CompanyAddItem_Category: Property = Property(name="Category", type=StringType)
CompanyAddItem.attributes={CompanyAddItem_Price, CompanyAddItem_Category, CompanyAddItem_Description, CompanyAddItem_Name}

# CompanyAddRider class attributes and methods
CompanyAddRider_Name: Property = Property(name="Name", type=StringType)
CompanyAddRider_UserName: Property = Property(name="UserName", type=StringType)
CompanyAddRider_Email: Property = Property(name="Email", type=StringType)
CompanyAddRider_Password: Property = Property(name="Password", type=StringType)
CompanyAddRider_Address: Property = Property(name="Address", type=StringType)
CompanyAddRider_Phone: Property = Property(name="Phone", type=StringType)
CompanyAddRider_CNIC: Property = Property(name="CNIC", type=IntegerType)
CompanyAddRider.attributes={CompanyAddRider_Password, CompanyAddRider_UserName, CompanyAddRider_Address, CompanyAddRider_Phone, CompanyAddRider_Email, CompanyAddRider_CNIC, CompanyAddRider_Name}

# phon class attributes and methods

# CompanyAssignRider class attributes and methods
CompanyAssignRider_CustomerName: Property = Property(name="CustomerName", type=StringType)
CompanyAssignRider_OrderDate_Time: Property = Property(name="OrderDate_Time", type=StringType)
CompanyAssignRider_OrderRider: Property = Property(name="OrderRider", type=StringType)
CompanyAssignRider.attributes={CompanyAssignRider_OrderDate_Time, CompanyAssignRider_OrderRider, CompanyAssignRider_CustomerName}

# CompanyOrderHistory class attributes and methods
CompanyOrderHistory_CustomerName: Property = Property(name="CustomerName", type=StringType)
CompanyOrderHistory_OrderDate_Time: Property = Property(name="OrderDate_Time", type=StringType)
CompanyOrderHistory_OrderReview: Property = Property(name="OrderReview", type=StringType)
CompanyOrderHistory_OrderRider: Property = Property(name="OrderRider", type=StringType)
CompanyOrderHistory.attributes={CompanyOrderHistory_CustomerName, CompanyOrderHistory_OrderDate_Time, CompanyOrderHistory_OrderReview, CompanyOrderHistory_OrderRider}

# CompanyTrackOrder class attributes and methods
CompanyTrackOrder_CustomerName: Property = Property(name="CustomerName", type=StringType)
CompanyTrackOrder_OrderDate_Time: Property = Property(name="OrderDate_Time", type=StringType)
CompanyTrackOrder_OrderRider: Property = Property(name="OrderRider", type=StringType)
CompanyTrackOrder_OrderStatus: Property = Property(name="OrderStatus", type=StringType)
CompanyTrackOrder.attributes={CompanyTrackOrder_OrderDate_Time, CompanyTrackOrder_OrderStatus, CompanyTrackOrder_OrderRider, CompanyTrackOrder_CustomerName}

# Order class attributes and methods
Order_OrderTime_Date: Property = Property(name="OrderTime_Date", type=StringType)
Order_OrderStatus: Property = Property(name="OrderStatus", type=StringType)
Order_OrderReview: Property = Property(name="OrderReview", type=StringType)
Order_OrderPrice: Property = Property(name="OrderPrice", type=StringType)
Order_OrderRider: Property = Property(name="OrderRider", type=StringType)
Order.attributes={Order_OrderReview, Order_OrderTime_Date, Order_OrderRider, Order_OrderPrice, Order_OrderStatus}

# RiderStatusUpdate class attributes and methods
RiderStatusUpdate_OrderDate_Time: Property = Property(name="OrderDate_Time", type=StringType)
RiderStatusUpdate_CustomerName: Property = Property(name="CustomerName", type=StringType)
RiderStatusUpdate_ItemList: Property = Property(name="ItemList", type=StringType)
RiderStatusUpdate.attributes={RiderStatusUpdate_OrderDate_Time, RiderStatusUpdate_ItemList, RiderStatusUpdate_CustomerName}

# Domain Model
domain_model = DomainModel(
    name="_0Es5sHLsEem42bdoMoG80w",
    types={TrackOrder, Store, void_Interface, ReviewOrder, OrderHistory, ConfirmOrder, Categories, PlaceOrder, UserRegisteration, Login, CartItems, CompanyAddItem, CompanyAddRider, phon, CompanyAssignRider, CompanyOrderHistory, CompanyTrackOrder, Order, RiderStatusUpdate},
    associations={},
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
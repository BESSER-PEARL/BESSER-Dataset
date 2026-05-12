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
Products = Class(name="Products")
Collection = Class(name="Collection")
Type = Class(name="Type")
Gallery = Class(name="Gallery")
Banner = Class(name="Banner")
Color = Class(name="Color")
Size = Class(name="Size")
Inventory = Class(name="Inventory")
Cart = Class(name="Cart")
DetailCart = Class(name="DetailCart")
Orders = Class(name="Orders")
DetailOrder = Class(name="DetailOrder")
Admin = Class(name="Admin")

# User class attributes and methods
User_ID: Property = Property(name="ID", type=IntegerType)
User_UserName: Property = Property(name="UserName", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_Email: Property = Property(name="Email", type=StringType)
User_Phone: Property = Property(name="Phone", type=IntegerType)
User_Point: Property = Property(name="Point", type=IntegerType)
User_UserInfo: Property = Property(name="UserInfo", type=StringType)
User.attributes={User_UserInfo, User_UserName, User_Email, User_Point, User_Password, User_ID, User_Phone}

# Products class attributes and methods
Products_ProductID: Property = Property(name="ProductID", type=IntegerType)
Products_TypeID: Property = Property(name="TypeID", type=IntegerType)
Products_CollectionID: Property = Property(name="CollectionID", type=IntegerType)
Products_ProductInfo: Property = Property(name="ProductInfo", type=StringType)
Products_InStock: Property = Property(name="InStock", type=IntegerType)
Products_Index: Property = Property(name="Index", type=IntegerType)
Products_DateCreate: Property = Property(name="DateCreate", type=StringType)
Products_TypeID1: Property = Property(name="TypeID1", type=IntegerType)
Products.attributes={Products_TypeID1, Products_CollectionID, Products_ProductID, Products_Index, Products_DateCreate, Products_TypeID, Products_InStock, Products_ProductInfo}

# Collection class attributes and methods
Collection_CollectionID: Property = Property(name="CollectionID", type=IntegerType)
Collection_CollectionName: Property = Property(name="CollectionName", type=StringType)
Collection.attributes={Collection_CollectionID, Collection_CollectionName}

# Type class attributes and methods
Type_TypeID: Property = Property(name="TypeID", type=IntegerType)
Type_TypeName: Property = Property(name="TypeName", type=StringType)
Type.attributes={Type_TypeID, Type_TypeName}

# Gallery class attributes and methods
Gallery_GalleryID: Property = Property(name="GalleryID", type=IntegerType)
Gallery_ProductID: Property = Property(name="ProductID", type=IntegerType)
Gallery_GalleryName: Property = Property(name="GalleryName", type=StringType)
Gallery_Image: Property = Property(name="Image", type=StringType)
Gallery_DateCreate: Property = Property(name="DateCreate", type=StringType)
Gallery.attributes={Gallery_DateCreate, Gallery_GalleryName, Gallery_GalleryID, Gallery_Image, Gallery_ProductID}

# Banner class attributes and methods
Banner_Image: Property = Property(name="Image", type=StringType)
Banner_BannerID: Property = Property(name="BannerID", type=IntegerType)
Banner_BannerInfo: Property = Property(name="BannerInfo", type=StringType)
Banner_DateStart: Property = Property(name="DateStart", type=StringType)
Banner_DateEnd: Property = Property(name="DateEnd", type=StringType)
Banner_IsShow: Property = Property(name="IsShow", type=IntegerType)
Banner.attributes={Banner_DateEnd, Banner_Image, Banner_IsShow, Banner_BannerInfo, Banner_DateStart, Banner_BannerID}

# Color class attributes and methods
Color_ColorID: Property = Property(name="ColorID", type=StringType)
Color_ColorName: Property = Property(name="ColorName", type=StringType)
Color.attributes={Color_ColorID, Color_ColorName}

# Size class attributes and methods
Size_SizeID: Property = Property(name="SizeID", type=IntegerType)
Size_SizeName: Property = Property(name="SizeName", type=StringType)
Size.attributes={Size_SizeID, Size_SizeName}

# Inventory class attributes and methods
Inventory_ProductID: Property = Property(name="ProductID", type=IntegerType)
Inventory_ColorID: Property = Property(name="ColorID", type=IntegerType)
Inventory_SizeID: Property = Property(name="SizeID", type=IntegerType)
Inventory_InStock: Property = Property(name="InStock", type=IntegerType)
Inventory.attributes={Inventory_InStock, Inventory_ColorID, Inventory_ProductID, Inventory_SizeID}

# Cart class attributes and methods
Cart_CartID: Property = Property(name="CartID", type=IntegerType)
Cart_CartInfo: Property = Property(name="CartInfo", type=StringType)
Cart.attributes={Cart_CartInfo, Cart_CartID}

# DetailCart class attributes and methods
DetailCart_DetailCartID: Property = Property(name="DetailCartID", type=IntegerType)
DetailCart_CartID: Property = Property(name="CartID", type=IntegerType)
DetailCart_ProductID: Property = Property(name="ProductID", type=IntegerType)
DetailCart_DetailCartInfo: Property = Property(name="DetailCartInfo", type=StringType)
DetailCart.attributes={DetailCart_ProductID, DetailCart_CartID, DetailCart_DetailCartID, DetailCart_DetailCartInfo}

# Orders class attributes and methods
Orders_OrderID: Property = Property(name="OrderID", type=IntegerType)
Orders_UserID: Property = Property(name="UserID", type=IntegerType)
Orders_OrderInfo: Property = Property(name="OrderInfo", type=StringType)
Orders_DeliInfo: Property = Property(name="DeliInfo", type=StringType)
Orders.attributes={Orders_OrderID, Orders_UserID, Orders_OrderInfo, Orders_DeliInfo}

# DetailOrder class attributes and methods
DetailOrder_DetailOrderID: Property = Property(name="DetailOrderID", type=IntegerType)
DetailOrder_OrderID: Property = Property(name="OrderID", type=IntegerType)
DetailOrder_ProductID: Property = Property(name="ProductID", type=IntegerType)
DetailOrder_DetailOrderInfo: Property = Property(name="DetailOrderInfo", type=StringType)
DetailOrder.attributes={DetailOrder_DetailOrderID, DetailOrder_ProductID, DetailOrder_OrderID, DetailOrder_DetailOrderInfo}

# Admin class attributes and methods
Admin_ID: Property = Property(name="ID", type=IntegerType)
Admin_UserName: Property = Property(name="UserName", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin_AdminInfo: Property = Property(name="AdminInfo", type=StringType)
Admin.attributes={Admin_Password, Admin_AdminInfo, Admin_ID, Admin_UserName}

# Relationships
Size_Inventory: BinaryAssociation = BinaryAssociation(
    name="Size_Inventory",
    ends={
        Property(name="inventory0", type=Inventory, multiplicity=Multiplicity(0, 9999)),
        Property(name="size1", type=Size, multiplicity=Multiplicity(0, 9999))
    }
)
Color_Inventory: BinaryAssociation = BinaryAssociation(
    name="Color_Inventory",
    ends={
        Property(name="inventory2", type=Inventory, multiplicity=Multiplicity(0, 9999)),
        Property(name="color3", type=Color, multiplicity=Multiplicity(0, 9999))
    }
)
Products_Inventory: BinaryAssociation = BinaryAssociation(
    name="Products_Inventory",
    ends={
        Property(name="inventory4", type=Inventory, multiplicity=Multiplicity(0, 9999)),
        Property(name="products5", type=Products, multiplicity=Multiplicity(0, 9999))
    }
)
Collection_Products: BinaryAssociation = BinaryAssociation(
    name="Collection_Products",
    ends={
        Property(name="products6", type=Products, multiplicity=Multiplicity(0, 9999)),
        Property(name="collection7", type=Collection, multiplicity=Multiplicity(1, 1))
    }
)
Type_Products: BinaryAssociation = BinaryAssociation(
    name="Type_Products",
    ends={
        Property(name="products8", type=Products, multiplicity=Multiplicity(0, 9999)),
        Property(name="type9", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
Gallery_Products: BinaryAssociation = BinaryAssociation(
    name="Gallery_Products",
    ends={
        Property(name="products10", type=Products, multiplicity=Multiplicity(1, 1)),
        Property(name="gallery11", type=Gallery, multiplicity=Multiplicity(0, 9999))
    }
)
DetailOrder_Products: BinaryAssociation = BinaryAssociation(
    name="DetailOrder_Products",
    ends={
        Property(name="products12", type=Products, multiplicity=Multiplicity(0, 9999)),
        Property(name="detailOrder13", type=DetailOrder, multiplicity=Multiplicity(1, 1))
    }
)
Products_DetailCart: BinaryAssociation = BinaryAssociation(
    name="Products_DetailCart",
    ends={
        Property(name="detailCart14", type=DetailCart, multiplicity=Multiplicity(1, 1)),
        Property(name="products15", type=Products, multiplicity=Multiplicity(0, 9999))
    }
)
DetailOrder_Orders: BinaryAssociation = BinaryAssociation(
    name="DetailOrder_Orders",
    ends={
        Property(name="orders16", type=Orders, multiplicity=Multiplicity(1, 1)),
        Property(name="detailOrder17", type=DetailOrder, multiplicity=Multiplicity(0, 9999))
    }
)
DetailCart_Cart: BinaryAssociation = BinaryAssociation(
    name="DetailCart_Cart",
    ends={
        Property(name="cart18", type=Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="detailCart19", type=DetailCart, multiplicity=Multiplicity(0, 9999))
    }
)
Orders_User: BinaryAssociation = BinaryAssociation(
    name="Orders_User",
    ends={
        Property(name="user20", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="orders21", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
Cart_User: BinaryAssociation = BinaryAssociation(
    name="Cart_User",
    ends={
        Property(name="user22", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="cart23", type=Cart, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vLApoK4CEemHYc7DDM2g2A",
    types={User, Products, Collection, Type, Gallery, Banner, Color, Size, Inventory, Cart, DetailCart, Orders, DetailOrder, Admin},
    associations={Size_Inventory, Color_Inventory, Products_Inventory, Collection_Products, Type_Products, Gallery_Products, DetailOrder_Products, Products_DetailCart, DetailOrder_Orders, DetailCart_Cart, Orders_User, Cart_User},
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
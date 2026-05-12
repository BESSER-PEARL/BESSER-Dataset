from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin:

    def __init__(self, ID: int, UserName: str, Password: str, AdminInfo: str):
        self.ID = ID
        self.UserName = UserName
        self.Password = Password
        self.AdminInfo = AdminInfo
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def AdminInfo(self):
        return self.__AdminInfo
    @AdminInfo.setter
    def AdminInfo(self, AdminInfo: str):
        self.__AdminInfo = AdminInfo

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName



class DetailOrder:

    def __init__(self, DetailOrderID: int, OrderID: int, ProductID: int, DetailOrderInfo: str, products12: set["Products"] = None, orders16: "Orders" = None):
        self.DetailOrderID = DetailOrderID
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.DetailOrderInfo = DetailOrderInfo
        self.products12 = products12 if products12 is not None else set()
        self.orders16 = orders16
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def DetailOrderInfo(self):
        return self.__DetailOrderInfo
    @DetailOrderInfo.setter
    def DetailOrderInfo(self, DetailOrderInfo: str):
        self.__DetailOrderInfo = DetailOrderInfo

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def DetailOrderID(self):
        return self.__DetailOrderID
    @DetailOrderID.setter
    def DetailOrderID(self, DetailOrderID: int):
        self.__DetailOrderID = DetailOrderID

    @property
    def products12(self):
        return self.__products12
    @products12.setter
    def products12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DetailOrder__products12", None)
        self.__products12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "detailOrder13"):
                    opp_val = getattr(item, "detailOrder13", None)
                    
                    if opp_val == self:
                        setattr(item, "detailOrder13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "detailOrder13"):
                    opp_val = getattr(item, "detailOrder13", None)
                    
                    setattr(item, "detailOrder13", self)
                    

    @property
    def orders16(self):
        return self.__orders16
    @orders16.setter
    def orders16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DetailOrder__orders16", None)
        self.__orders16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detailOrder17"):
                opp_val = getattr(old_value, "detailOrder17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detailOrder17"):
                opp_val = getattr(value, "detailOrder17", None)
                if opp_val is None:
                    setattr(value, "detailOrder17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Orders:

    def __init__(self, OrderID: int, UserID: int, OrderInfo: str, DeliInfo: str, detailOrder17: set["DetailOrder"] = None, user20: "User" = None):
        self.OrderID = OrderID
        self.UserID = UserID
        self.OrderInfo = OrderInfo
        self.DeliInfo = DeliInfo
        self.detailOrder17 = detailOrder17 if detailOrder17 is not None else set()
        self.user20 = user20
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def OrderInfo(self):
        return self.__OrderInfo
    @OrderInfo.setter
    def OrderInfo(self, OrderInfo: str):
        self.__OrderInfo = OrderInfo

    @property
    def DeliInfo(self):
        return self.__DeliInfo
    @DeliInfo.setter
    def DeliInfo(self, DeliInfo: str):
        self.__DeliInfo = DeliInfo

    @property
    def detailOrder17(self):
        return self.__detailOrder17
    @detailOrder17.setter
    def detailOrder17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__detailOrder17", None)
        self.__detailOrder17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orders16"):
                    opp_val = getattr(item, "orders16", None)
                    
                    if opp_val == self:
                        setattr(item, "orders16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orders16"):
                    opp_val = getattr(item, "orders16", None)
                    
                    setattr(item, "orders16", self)
                    

    @property
    def user20(self):
        return self.__user20
    @user20.setter
    def user20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__user20", None)
        self.__user20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders21"):
                opp_val = getattr(old_value, "orders21", None)
                if opp_val == self:
                    setattr(old_value, "orders21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders21"):
                opp_val = getattr(value, "orders21", None)
                setattr(value, "orders21", self)



class DetailCart:

    def __init__(self, DetailCartID: int, CartID: int, ProductID: int, DetailCartInfo: str, products15: set["Products"] = None, cart18: "Cart" = None):
        self.DetailCartID = DetailCartID
        self.CartID = CartID
        self.ProductID = ProductID
        self.DetailCartInfo = DetailCartInfo
        self.products15 = products15 if products15 is not None else set()
        self.cart18 = cart18
        
        pass
    @property
    def DetailCartInfo(self):
        return self.__DetailCartInfo
    @DetailCartInfo.setter
    def DetailCartInfo(self, DetailCartInfo: str):
        self.__DetailCartInfo = DetailCartInfo

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def DetailCartID(self):
        return self.__DetailCartID
    @DetailCartID.setter
    def DetailCartID(self, DetailCartID: int):
        self.__DetailCartID = DetailCartID

    @property
    def CartID(self):
        return self.__CartID
    @CartID.setter
    def CartID(self, CartID: int):
        self.__CartID = CartID

    @property
    def products15(self):
        return self.__products15
    @products15.setter
    def products15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DetailCart__products15", None)
        self.__products15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "detailCart14"):
                    opp_val = getattr(item, "detailCart14", None)
                    
                    if opp_val == self:
                        setattr(item, "detailCart14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "detailCart14"):
                    opp_val = getattr(item, "detailCart14", None)
                    
                    setattr(item, "detailCart14", self)
                    

    @property
    def cart18(self):
        return self.__cart18
    @cart18.setter
    def cart18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DetailCart__cart18", None)
        self.__cart18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detailCart19"):
                opp_val = getattr(old_value, "detailCart19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detailCart19"):
                opp_val = getattr(value, "detailCart19", None)
                if opp_val is None:
                    setattr(value, "detailCart19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cart:

    def __init__(self, CartID: int, CartInfo: str, detailCart19: set["DetailCart"] = None, user22: "User" = None):
        self.CartID = CartID
        self.CartInfo = CartInfo
        self.detailCart19 = detailCart19 if detailCart19 is not None else set()
        self.user22 = user22
        
        pass
    @property
    def CartID(self):
        return self.__CartID
    @CartID.setter
    def CartID(self, CartID: int):
        self.__CartID = CartID

    @property
    def CartInfo(self):
        return self.__CartInfo
    @CartInfo.setter
    def CartInfo(self, CartInfo: str):
        self.__CartInfo = CartInfo

    @property
    def user22(self):
        return self.__user22
    @user22.setter
    def user22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__user22", None)
        self.__user22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart23"):
                opp_val = getattr(old_value, "cart23", None)
                if opp_val == self:
                    setattr(old_value, "cart23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart23"):
                opp_val = getattr(value, "cart23", None)
                setattr(value, "cart23", self)

    @property
    def detailCart19(self):
        return self.__detailCart19
    @detailCart19.setter
    def detailCart19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__detailCart19", None)
        self.__detailCart19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cart18"):
                    opp_val = getattr(item, "cart18", None)
                    
                    if opp_val == self:
                        setattr(item, "cart18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cart18"):
                    opp_val = getattr(item, "cart18", None)
                    
                    setattr(item, "cart18", self)
                    



class Inventory:

    def __init__(self, ProductID: int, ColorID: int, SizeID: int, InStock: int, size1: set["Size"] = None, color3: set["Color"] = None, products5: set["Products"] = None):
        self.ProductID = ProductID
        self.ColorID = ColorID
        self.SizeID = SizeID
        self.InStock = InStock
        self.size1 = size1 if size1 is not None else set()
        self.color3 = color3 if color3 is not None else set()
        self.products5 = products5 if products5 is not None else set()
        
        pass
    @property
    def InStock(self):
        return self.__InStock
    @InStock.setter
    def InStock(self, InStock: int):
        self.__InStock = InStock

    @property
    def SizeID(self):
        return self.__SizeID
    @SizeID.setter
    def SizeID(self, SizeID: int):
        self.__SizeID = SizeID

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def ColorID(self):
        return self.__ColorID
    @ColorID.setter
    def ColorID(self, ColorID: int):
        self.__ColorID = ColorID

    @property
    def products5(self):
        return self.__products5
    @products5.setter
    def products5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__products5", None)
        self.__products5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory4"):
                    opp_val = getattr(item, "inventory4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory4"):
                    opp_val = getattr(item, "inventory4", None)
                    
                    if opp_val is None:
                        setattr(item, "inventory4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def color3(self):
        return self.__color3
    @color3.setter
    def color3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__color3", None)
        self.__color3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory2"):
                    opp_val = getattr(item, "inventory2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory2"):
                    opp_val = getattr(item, "inventory2", None)
                    
                    if opp_val is None:
                        setattr(item, "inventory2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def size1(self):
        return self.__size1
    @size1.setter
    def size1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__size1", None)
        self.__size1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory0"):
                    opp_val = getattr(item, "inventory0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory0"):
                    opp_val = getattr(item, "inventory0", None)
                    
                    if opp_val is None:
                        setattr(item, "inventory0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Size:

    def __init__(self, SizeID: int, SizeName: str, inventory0: set["Inventory"] = None):
        self.SizeID = SizeID
        self.SizeName = SizeName
        self.inventory0 = inventory0 if inventory0 is not None else set()
        
        pass
    @property
    def SizeID(self):
        return self.__SizeID
    @SizeID.setter
    def SizeID(self, SizeID: int):
        self.__SizeID = SizeID

    @property
    def SizeName(self):
        return self.__SizeName
    @SizeName.setter
    def SizeName(self, SizeName: str):
        self.__SizeName = SizeName

    @property
    def inventory0(self):
        return self.__inventory0
    @inventory0.setter
    def inventory0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Size__inventory0", None)
        self.__inventory0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "size1"):
                    opp_val = getattr(item, "size1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "size1"):
                    opp_val = getattr(item, "size1", None)
                    
                    if opp_val is None:
                        setattr(item, "size1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Color:

    def __init__(self, ColorID: str, ColorName: str, inventory2: set["Inventory"] = None):
        self.ColorID = ColorID
        self.ColorName = ColorName
        self.inventory2 = inventory2 if inventory2 is not None else set()
        
        pass
    @property
    def ColorID(self):
        return self.__ColorID
    @ColorID.setter
    def ColorID(self, ColorID: str):
        self.__ColorID = ColorID

    @property
    def ColorName(self):
        return self.__ColorName
    @ColorName.setter
    def ColorName(self, ColorName: str):
        self.__ColorName = ColorName

    @property
    def inventory2(self):
        return self.__inventory2
    @inventory2.setter
    def inventory2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Color__inventory2", None)
        self.__inventory2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "color3"):
                    opp_val = getattr(item, "color3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "color3"):
                    opp_val = getattr(item, "color3", None)
                    
                    if opp_val is None:
                        setattr(item, "color3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Banner:

    def __init__(self, Image: str, BannerID: int, BannerInfo: str, DateStart: str, DateEnd: str, IsShow: int):
        self.Image = Image
        self.BannerID = BannerID
        self.BannerInfo = BannerInfo
        self.DateStart = DateStart
        self.DateEnd = DateEnd
        self.IsShow = IsShow
        
        pass
    @property
    def Image(self):
        return self.__Image
    @Image.setter
    def Image(self, Image: str):
        self.__Image = Image

    @property
    def IsShow(self):
        return self.__IsShow
    @IsShow.setter
    def IsShow(self, IsShow: int):
        self.__IsShow = IsShow

    @property
    def DateEnd(self):
        return self.__DateEnd
    @DateEnd.setter
    def DateEnd(self, DateEnd: str):
        self.__DateEnd = DateEnd

    @property
    def BannerID(self):
        return self.__BannerID
    @BannerID.setter
    def BannerID(self, BannerID: int):
        self.__BannerID = BannerID

    @property
    def DateStart(self):
        return self.__DateStart
    @DateStart.setter
    def DateStart(self, DateStart: str):
        self.__DateStart = DateStart

    @property
    def BannerInfo(self):
        return self.__BannerInfo
    @BannerInfo.setter
    def BannerInfo(self, BannerInfo: str):
        self.__BannerInfo = BannerInfo



class Gallery:

    def __init__(self, GalleryID: int, ProductID: int, GalleryName: str, Image: str, DateCreate: str, products10: "Products" = None):
        self.GalleryID = GalleryID
        self.ProductID = ProductID
        self.GalleryName = GalleryName
        self.Image = Image
        self.DateCreate = DateCreate
        self.products10 = products10
        
        pass
    @property
    def GalleryID(self):
        return self.__GalleryID
    @GalleryID.setter
    def GalleryID(self, GalleryID: int):
        self.__GalleryID = GalleryID

    @property
    def DateCreate(self):
        return self.__DateCreate
    @DateCreate.setter
    def DateCreate(self, DateCreate: str):
        self.__DateCreate = DateCreate

    @property
    def Image(self):
        return self.__Image
    @Image.setter
    def Image(self, Image: str):
        self.__Image = Image

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def GalleryName(self):
        return self.__GalleryName
    @GalleryName.setter
    def GalleryName(self, GalleryName: str):
        self.__GalleryName = GalleryName

    @property
    def products10(self):
        return self.__products10
    @products10.setter
    def products10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gallery__products10", None)
        self.__products10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gallery11"):
                opp_val = getattr(old_value, "gallery11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gallery11"):
                opp_val = getattr(value, "gallery11", None)
                if opp_val is None:
                    setattr(value, "gallery11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Type:

    def __init__(self, TypeID: int, TypeName: str, products8: set["Products"] = None):
        self.TypeID = TypeID
        self.TypeName = TypeName
        self.products8 = products8 if products8 is not None else set()
        
        pass
    @property
    def TypeName(self):
        return self.__TypeName
    @TypeName.setter
    def TypeName(self, TypeName: str):
        self.__TypeName = TypeName

    @property
    def TypeID(self):
        return self.__TypeID
    @TypeID.setter
    def TypeID(self, TypeID: int):
        self.__TypeID = TypeID

    @property
    def products8(self):
        return self.__products8
    @products8.setter
    def products8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Type__products8", None)
        self.__products8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type9"):
                    opp_val = getattr(item, "type9", None)
                    
                    if opp_val == self:
                        setattr(item, "type9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type9"):
                    opp_val = getattr(item, "type9", None)
                    
                    setattr(item, "type9", self)
                    



class Collection:

    def __init__(self, CollectionID: int, CollectionName: str, products6: set["Products"] = None):
        self.CollectionID = CollectionID
        self.CollectionName = CollectionName
        self.products6 = products6 if products6 is not None else set()
        
        pass
    @property
    def CollectionID(self):
        return self.__CollectionID
    @CollectionID.setter
    def CollectionID(self, CollectionID: int):
        self.__CollectionID = CollectionID

    @property
    def CollectionName(self):
        return self.__CollectionName
    @CollectionName.setter
    def CollectionName(self, CollectionName: str):
        self.__CollectionName = CollectionName

    @property
    def products6(self):
        return self.__products6
    @products6.setter
    def products6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Collection__products6", None)
        self.__products6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection7"):
                    opp_val = getattr(item, "collection7", None)
                    
                    if opp_val == self:
                        setattr(item, "collection7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection7"):
                    opp_val = getattr(item, "collection7", None)
                    
                    setattr(item, "collection7", self)
                    



class Products:

    def __init__(self, ProductID: int, TypeID: int, CollectionID: int, ProductInfo: str, InStock: int, Index: int, DateCreate: str, TypeID1: int, inventory4: set["Inventory"] = None, collection7: "Collection" = None, type9: "Type" = None, gallery11: set["Gallery"] = None, detailOrder13: "DetailOrder" = None, detailCart14: "DetailCart" = None):
        self.ProductID = ProductID
        self.TypeID = TypeID
        self.CollectionID = CollectionID
        self.ProductInfo = ProductInfo
        self.InStock = InStock
        self.Index = Index
        self.DateCreate = DateCreate
        self.TypeID1 = TypeID1
        self.inventory4 = inventory4 if inventory4 is not None else set()
        self.collection7 = collection7
        self.type9 = type9
        self.gallery11 = gallery11 if gallery11 is not None else set()
        self.detailOrder13 = detailOrder13
        self.detailCart14 = detailCart14
        
        pass
    @property
    def TypeID1(self):
        return self.__TypeID1
    @TypeID1.setter
    def TypeID1(self, TypeID1: int):
        self.__TypeID1 = TypeID1

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def Index(self):
        return self.__Index
    @Index.setter
    def Index(self, Index: int):
        self.__Index = Index

    @property
    def DateCreate(self):
        return self.__DateCreate
    @DateCreate.setter
    def DateCreate(self, DateCreate: str):
        self.__DateCreate = DateCreate

    @property
    def InStock(self):
        return self.__InStock
    @InStock.setter
    def InStock(self, InStock: int):
        self.__InStock = InStock

    @property
    def TypeID(self):
        return self.__TypeID
    @TypeID.setter
    def TypeID(self, TypeID: int):
        self.__TypeID = TypeID

    @property
    def CollectionID(self):
        return self.__CollectionID
    @CollectionID.setter
    def CollectionID(self, CollectionID: int):
        self.__CollectionID = CollectionID

    @property
    def ProductInfo(self):
        return self.__ProductInfo
    @ProductInfo.setter
    def ProductInfo(self, ProductInfo: str):
        self.__ProductInfo = ProductInfo

    @property
    def inventory4(self):
        return self.__inventory4
    @inventory4.setter
    def inventory4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__inventory4", None)
        self.__inventory4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products5"):
                    opp_val = getattr(item, "products5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products5"):
                    opp_val = getattr(item, "products5", None)
                    
                    if opp_val is None:
                        setattr(item, "products5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def detailOrder13(self):
        return self.__detailOrder13
    @detailOrder13.setter
    def detailOrder13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__detailOrder13", None)
        self.__detailOrder13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products12"):
                opp_val = getattr(old_value, "products12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products12"):
                opp_val = getattr(value, "products12", None)
                if opp_val is None:
                    setattr(value, "products12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def type9(self):
        return self.__type9
    @type9.setter
    def type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__type9", None)
        self.__type9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products8"):
                opp_val = getattr(old_value, "products8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products8"):
                opp_val = getattr(value, "products8", None)
                if opp_val is None:
                    setattr(value, "products8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def collection7(self):
        return self.__collection7
    @collection7.setter
    def collection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__collection7", None)
        self.__collection7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products6"):
                opp_val = getattr(old_value, "products6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products6"):
                opp_val = getattr(value, "products6", None)
                if opp_val is None:
                    setattr(value, "products6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gallery11(self):
        return self.__gallery11
    @gallery11.setter
    def gallery11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__gallery11", None)
        self.__gallery11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products10"):
                    opp_val = getattr(item, "products10", None)
                    
                    if opp_val == self:
                        setattr(item, "products10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products10"):
                    opp_val = getattr(item, "products10", None)
                    
                    setattr(item, "products10", self)
                    

    @property
    def detailCart14(self):
        return self.__detailCart14
    @detailCart14.setter
    def detailCart14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__detailCart14", None)
        self.__detailCart14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products15"):
                opp_val = getattr(old_value, "products15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products15"):
                opp_val = getattr(value, "products15", None)
                if opp_val is None:
                    setattr(value, "products15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, ID: int, UserName: str, Password: str, Email: str, Phone: int, Point: int, UserInfo: str, orders21: "Orders" = None, cart23: "Cart" = None):
        self.ID = ID
        self.UserName = UserName
        self.Password = Password
        self.Email = Email
        self.Phone = Phone
        self.Point = Point
        self.UserInfo = UserInfo
        self.orders21 = orders21
        self.cart23 = cart23
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Point(self):
        return self.__Point
    @Point.setter
    def Point(self, Point: int):
        self.__Point = Point

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserInfo(self):
        return self.__UserInfo
    @UserInfo.setter
    def UserInfo(self, UserInfo: str):
        self.__UserInfo = UserInfo

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def orders21(self):
        return self.__orders21
    @orders21.setter
    def orders21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__orders21", None)
        self.__orders21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user20"):
                opp_val = getattr(old_value, "user20", None)
                if opp_val == self:
                    setattr(old_value, "user20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user20"):
                opp_val = getattr(value, "user20", None)
                setattr(value, "user20", self)

    @property
    def cart23(self):
        return self.__cart23
    @cart23.setter
    def cart23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__cart23", None)
        self.__cart23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user22"):
                opp_val = getattr(old_value, "user22", None)
                if opp_val == self:
                    setattr(old_value, "user22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user22"):
                opp_val = getattr(value, "user22", None)
                setattr(value, "user22", self)


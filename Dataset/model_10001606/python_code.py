from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class SubCategory:

    def __init__(self, Name: str, RusName: str, CategoryId: str, category10: "Category" = None, item12: "Item" = None):
        self.Name = Name
        self.RusName = RusName
        self.CategoryId = CategoryId
        self.category10 = category10
        self.item12 = item12
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def RusName(self):
        return self.__RusName
    @RusName.setter
    def RusName(self, RusName: str):
        self.__RusName = RusName

    @property
    def CategoryId(self):
        return self.__CategoryId
    @CategoryId.setter
    def CategoryId(self, CategoryId: str):
        self.__CategoryId = CategoryId

    @property
    def item12(self):
        return self.__item12
    @item12.setter
    def item12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__item12", None)
        self.__item12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategory13"):
                opp_val = getattr(old_value, "subCategory13", None)
                if opp_val == self:
                    setattr(old_value, "subCategory13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategory13"):
                opp_val = getattr(value, "subCategory13", None)
                setattr(value, "subCategory13", self)

    @property
    def category10(self):
        return self.__category10
    @category10.setter
    def category10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__category10", None)
        self.__category10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategory11"):
                opp_val = getattr(old_value, "subCategory11", None)
                if opp_val == self:
                    setattr(old_value, "subCategory11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategory11"):
                opp_val = getattr(value, "subCategory11", None)
                setattr(value, "subCategory11", self)



class OrderItem:

    def __init__(self, Name: str, Price: str, Amount: int, ItemId: str, OrderId: str, order8: "Order" = None):
        self.Name = Name
        self.Price = Price
        self.Amount = Amount
        self.ItemId = ItemId
        self.OrderId = OrderId
        self.order8 = order8
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: str):
        self.__OrderId = OrderId

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def ItemId(self):
        return self.__ItemId
    @ItemId.setter
    def ItemId(self, ItemId: str):
        self.__ItemId = ItemId

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem9"):
                opp_val = getattr(old_value, "orderItem9", None)
                if opp_val == self:
                    setattr(old_value, "orderItem9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem9"):
                opp_val = getattr(value, "orderItem9", None)
                setattr(value, "orderItem9", self)



class FavoriteItem:

    def __init__(self, UserId: str, ItemId: str, item1: "Item" = None, user2: "User" = None):
        self.UserId = UserId
        self.ItemId = ItemId
        self.item1 = item1
        self.user2 = user2
        
        pass
    @property
    def ItemId(self):
        return self.__ItemId
    @ItemId.setter
    def ItemId(self, ItemId: str):
        self.__ItemId = ItemId

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: str):
        self.__UserId = UserId

    @property
    def user2(self):
        return self.__user2
    @user2.setter
    def user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FavoriteItem__user2", None)
        self.__user2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "favoriteItem3"):
                opp_val = getattr(old_value, "favoriteItem3", None)
                if opp_val == self:
                    setattr(old_value, "favoriteItem3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "favoriteItem3"):
                opp_val = getattr(value, "favoriteItem3", None)
                setattr(value, "favoriteItem3", self)

    @property
    def item1(self):
        return self.__item1
    @item1.setter
    def item1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FavoriteItem__item1", None)
        self.__item1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "favoriteItem0"):
                opp_val = getattr(old_value, "favoriteItem0", None)
                if opp_val == self:
                    setattr(old_value, "favoriteItem0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "favoriteItem0"):
                opp_val = getattr(value, "favoriteItem0", None)
                setattr(value, "favoriteItem0", self)



class CouponCode:

    def __init__(self, ExpiryDate: str, Code: str, Discount: int, UserId: str, order5: "Order" = None, user6: "User" = None):
        self.ExpiryDate = ExpiryDate
        self.Code = Code
        self.Discount = Discount
        self.UserId = UserId
        self.order5 = order5
        self.user6 = user6
        
        pass
    @property
    def ExpiryDate(self):
        return self.__ExpiryDate
    @ExpiryDate.setter
    def ExpiryDate(self, ExpiryDate: str):
        self.__ExpiryDate = ExpiryDate

    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: int):
        self.__Discount = Discount

    @property
    def Code(self):
        return self.__Code
    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: str):
        self.__UserId = UserId

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CouponCode__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "couponCode7"):
                opp_val = getattr(old_value, "couponCode7", None)
                if opp_val == self:
                    setattr(old_value, "couponCode7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "couponCode7"):
                opp_val = getattr(value, "couponCode7", None)
                setattr(value, "couponCode7", self)

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CouponCode__order5", None)
        self.__order5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "couponCode4"):
                opp_val = getattr(old_value, "couponCode4", None)
                if opp_val == self:
                    setattr(old_value, "couponCode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "couponCode4"):
                opp_val = getattr(value, "couponCode4", None)
                setattr(value, "couponCode4", self)



class Category:

    def __init__(self, Name: str, RusName: str, subCategory11: "SubCategory" = None, item14: "Item" = None):
        self.Name = Name
        self.RusName = RusName
        self.subCategory11 = subCategory11
        self.item14 = item14
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def RusName(self):
        return self.__RusName
    @RusName.setter
    def RusName(self, RusName: str):
        self.__RusName = RusName

    @property
    def subCategory11(self):
        return self.__subCategory11
    @subCategory11.setter
    def subCategory11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__subCategory11", None)
        self.__subCategory11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category10"):
                opp_val = getattr(old_value, "category10", None)
                if opp_val == self:
                    setattr(old_value, "category10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category10"):
                opp_val = getattr(value, "category10", None)
                setattr(value, "category10", self)

    @property
    def item14(self):
        return self.__item14
    @item14.setter
    def item14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__item14", None)
        self.__item14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category15"):
                opp_val = getattr(old_value, "category15", None)
                if opp_val == self:
                    setattr(old_value, "category15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category15"):
                opp_val = getattr(value, "category15", None)
                setattr(value, "category15", self)



class Item:

    def __init__(self, Name: str, Description: str, Color: str, Brand: str, Discount: str, Price: str, PreviewImagePath: str, MinPreviewImagePath: str, ImagePath1: str, ImagePath2: str, ImagePath3: str, Status: int, Size: str, Amount: int, Sex: int, CategoryId: str, SubCategoryId: str, favoriteItem0: "FavoriteItem" = None, subCategory13: "SubCategory" = None, category15: "Category" = None):
        self.Name = Name
        self.Description = Description
        self.Color = Color
        self.Brand = Brand
        self.Discount = Discount
        self.Price = Price
        self.PreviewImagePath = PreviewImagePath
        self.MinPreviewImagePath = MinPreviewImagePath
        self.ImagePath1 = ImagePath1
        self.ImagePath2 = ImagePath2
        self.ImagePath3 = ImagePath3
        self.Status = Status
        self.Size = Size
        self.Amount = Amount
        self.Sex = Sex
        self.CategoryId = CategoryId
        self.SubCategoryId = SubCategoryId
        self.favoriteItem0 = favoriteItem0
        self.subCategory13 = subCategory13
        self.category15 = category15
        
        pass
    @property
    def MinPreviewImagePath(self):
        return self.__MinPreviewImagePath
    @MinPreviewImagePath.setter
    def MinPreviewImagePath(self, MinPreviewImagePath: str):
        self.__MinPreviewImagePath = MinPreviewImagePath

    @property
    def SubCategoryId(self):
        return self.__SubCategoryId
    @SubCategoryId.setter
    def SubCategoryId(self, SubCategoryId: str):
        self.__SubCategoryId = SubCategoryId

    @property
    def CategoryId(self):
        return self.__CategoryId
    @CategoryId.setter
    def CategoryId(self, CategoryId: str):
        self.__CategoryId = CategoryId

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Brand(self):
        return self.__Brand
    @Brand.setter
    def Brand(self, Brand: str):
        self.__Brand = Brand

    @property
    def PreviewImagePath(self):
        return self.__PreviewImagePath
    @PreviewImagePath.setter
    def PreviewImagePath(self, PreviewImagePath: str):
        self.__PreviewImagePath = PreviewImagePath

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: int):
        self.__Sex = Sex

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: int):
        self.__Status = Status

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ImagePath3(self):
        return self.__ImagePath3
    @ImagePath3.setter
    def ImagePath3(self, ImagePath3: str):
        self.__ImagePath3 = ImagePath3

    @property
    def ImagePath1(self):
        return self.__ImagePath1
    @ImagePath1.setter
    def ImagePath1(self, ImagePath1: str):
        self.__ImagePath1 = ImagePath1

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def Color(self):
        return self.__Color
    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: str):
        self.__Discount = Discount

    @property
    def ImagePath2(self):
        return self.__ImagePath2
    @ImagePath2.setter
    def ImagePath2(self, ImagePath2: str):
        self.__ImagePath2 = ImagePath2

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def favoriteItem0(self):
        return self.__favoriteItem0
    @favoriteItem0.setter
    def favoriteItem0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__favoriteItem0", None)
        self.__favoriteItem0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item1"):
                opp_val = getattr(old_value, "item1", None)
                if opp_val == self:
                    setattr(old_value, "item1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item1"):
                opp_val = getattr(value, "item1", None)
                setattr(value, "item1", self)

    @property
    def category15(self):
        return self.__category15
    @category15.setter
    def category15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__category15", None)
        self.__category15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item14"):
                opp_val = getattr(old_value, "item14", None)
                if opp_val == self:
                    setattr(old_value, "item14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item14"):
                opp_val = getattr(value, "item14", None)
                setattr(value, "item14", self)

    @property
    def subCategory13(self):
        return self.__subCategory13
    @subCategory13.setter
    def subCategory13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__subCategory13", None)
        self.__subCategory13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item12"):
                opp_val = getattr(old_value, "item12", None)
                if opp_val == self:
                    setattr(old_value, "item12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item12"):
                opp_val = getattr(value, "item12", None)
                setattr(value, "item12", self)



class Order:

    def __init__(self, Name: str, PhoneNumber: str, Email: str, Comment: str, Address: str, TotalPrice: str, Status: int, CodeId: str, UserId: str, couponCode4: "CouponCode" = None, orderItem9: "OrderItem" = None):
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Comment = Comment
        self.Address = Address
        self.TotalPrice = TotalPrice
        self.Status = Status
        self.CodeId = CodeId
        self.UserId = UserId
        self.couponCode4 = couponCode4
        self.orderItem9 = orderItem9
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Comment(self):
        return self.__Comment
    @Comment.setter
    def Comment(self, Comment: str):
        self.__Comment = Comment

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def TotalPrice(self):
        return self.__TotalPrice
    @TotalPrice.setter
    def TotalPrice(self, TotalPrice: str):
        self.__TotalPrice = TotalPrice

    @property
    def CodeId(self):
        return self.__CodeId
    @CodeId.setter
    def CodeId(self, CodeId: str):
        self.__CodeId = CodeId

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: int):
        self.__Status = Status

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: str):
        self.__UserId = UserId

    @property
    def orderItem9(self):
        return self.__orderItem9
    @orderItem9.setter
    def orderItem9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderItem9", None)
        self.__orderItem9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order8"):
                opp_val = getattr(old_value, "order8", None)
                if opp_val == self:
                    setattr(old_value, "order8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order8"):
                opp_val = getattr(value, "order8", None)
                setattr(value, "order8", self)

    @property
    def couponCode4(self):
        return self.__couponCode4
    @couponCode4.setter
    def couponCode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__couponCode4", None)
        self.__couponCode4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if opp_val == self:
                    setattr(old_value, "order5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                setattr(value, "order5", self)



class User:

    def __init__(self, Login: str, Password: str, Email: str, FirstName: str, LastName: str, Role: int, PhoneNumber: str, favoriteItem3: "FavoriteItem" = None, couponCode7: "CouponCode" = None):
        self.Login = Login
        self.Password = Password
        self.Email = Email
        self.FirstName = FirstName
        self.LastName = LastName
        self.Role = Role
        self.PhoneNumber = PhoneNumber
        self.favoriteItem3 = favoriteItem3
        self.couponCode7 = couponCode7
        
        pass
    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self, Login: str):
        self.__Login = Login

    @property
    def Role(self):
        return self.__Role
    @Role.setter
    def Role(self, Role: int):
        self.__Role = Role

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def couponCode7(self):
        return self.__couponCode7
    @couponCode7.setter
    def couponCode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__couponCode7", None)
        self.__couponCode7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user6"):
                opp_val = getattr(old_value, "user6", None)
                if opp_val == self:
                    setattr(old_value, "user6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user6"):
                opp_val = getattr(value, "user6", None)
                setattr(value, "user6", self)

    @property
    def favoriteItem3(self):
        return self.__favoriteItem3
    @favoriteItem3.setter
    def favoriteItem3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__favoriteItem3", None)
        self.__favoriteItem3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user2"):
                opp_val = getattr(old_value, "user2", None)
                if opp_val == self:
                    setattr(old_value, "user2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user2"):
                opp_val = getattr(value, "user2", None)
                setattr(value, "user2", self)



class BaseEntity:

    def __init__(self, Id: str, Active: bool, CreatedBy: str, CreatedDate: str, UpdatedBy: str, UpdatedDate: str):
        self.Id = Id
        self.Active = Active
        self.CreatedBy = CreatedBy
        self.CreatedDate = CreatedDate
        self.UpdatedBy = UpdatedBy
        self.UpdatedDate = UpdatedDate
        
        pass
    @property
    def UpdatedDate(self):
        return self.__UpdatedDate
    @UpdatedDate.setter
    def UpdatedDate(self, UpdatedDate: str):
        self.__UpdatedDate = UpdatedDate

    @property
    def CreatedBy(self):
        return self.__CreatedBy
    @CreatedBy.setter
    def CreatedBy(self, CreatedBy: str):
        self.__CreatedBy = CreatedBy

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Active(self):
        return self.__Active
    @Active.setter
    def Active(self, Active: bool):
        self.__Active = Active

    @property
    def CreatedDate(self):
        return self.__CreatedDate
    @CreatedDate.setter
    def CreatedDate(self, CreatedDate: str):
        self.__CreatedDate = CreatedDate

    @property
    def UpdatedBy(self):
        return self.__UpdatedBy
    @UpdatedBy.setter
    def UpdatedBy(self, UpdatedBy: str):
        self.__UpdatedBy = UpdatedBy


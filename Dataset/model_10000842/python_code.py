from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Products:

    def __init__(self, name: str, ID: int, selling_price: float, description: str, discount: int, rating: int, reviews: str, farmerID: str, inventoryID: str, farmer8: "Farmer" = None):
        self.name = name
        self.ID = ID
        self.selling_price = selling_price
        self.description = description
        self.discount = discount
        self.rating = rating
        self.reviews = reviews
        self.farmerID = farmerID
        self.inventoryID = inventoryID
        self.farmer8 = farmer8
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selling_price(self):
        return self.__selling_price
    @selling_price.setter
    def selling_price(self, selling_price: float):
        self.__selling_price = selling_price

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def farmerID(self):
        return self.__farmerID
    @farmerID.setter
    def farmerID(self, farmerID: str):
        self.__farmerID = farmerID

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: str):
        self.__reviews = reviews

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def inventoryID(self):
        return self.__inventoryID
    @inventoryID.setter
    def inventoryID(self, inventoryID: str):
        self.__inventoryID = inventoryID

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: int):
        self.__discount = discount

    @property
    def farmer8(self):
        return self.__farmer8
    @farmer8.setter
    def farmer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__farmer8", None)
        self.__farmer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_Farmer9"):
                opp_val = getattr(old_value, "product_Farmer9", None)
                if opp_val == self:
                    setattr(old_value, "product_Farmer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_Farmer9"):
                opp_val = getattr(value, "product_Farmer9", None)
                setattr(value, "product_Farmer9", self)



class Farmer_produces:

    def __init__(self, ID: int, farmerID: int, productList: str):
        self.ID = ID
        self.farmerID = farmerID
        self.productList = productList
        
        pass
    @property
    def farmerID(self):
        return self.__farmerID
    @farmerID.setter
    def farmerID(self, farmerID: int):
        self.__farmerID = farmerID

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def productList(self):
        return self.__productList
    @productList.setter
    def productList(self, productList: str):
        self.__productList = productList



class Order:

    def __init__(self, transactionID: int, purchaseDate: date, cardDetails: str, productDetails: str, customer5: "Retailer" = None, farmer10: "Farmer" = None):
        self.transactionID = transactionID
        self.purchaseDate = purchaseDate
        self.cardDetails = cardDetails
        self.productDetails = productDetails
        self.customer5 = customer5
        self.farmer10 = farmer10
        
        pass
    @property
    def productDetails(self):
        return self.__productDetails
    @productDetails.setter
    def productDetails(self, productDetails: str):
        self.__productDetails = productDetails

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: int):
        self.__transactionID = transactionID

    @property
    def purchaseDate(self):
        return self.__purchaseDate
    @purchaseDate.setter
    def purchaseDate(self, purchaseDate: date):
        self.__purchaseDate = purchaseDate

    @property
    def cardDetails(self):
        return self.__cardDetails
    @cardDetails.setter
    def cardDetails(self, cardDetails: str):
        self.__cardDetails = cardDetails

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order4"):
                opp_val = getattr(old_value, "order4", None)
                if opp_val == self:
                    setattr(old_value, "order4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order4"):
                opp_val = getattr(value, "order4", None)
                setattr(value, "order4", self)

    @property
    def farmer10(self):
        return self.__farmer10
    @farmer10.setter
    def farmer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__farmer10", None)
        self.__farmer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order11"):
                opp_val = getattr(old_value, "order11", None)
                if opp_val == self:
                    setattr(old_value, "order11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order11"):
                opp_val = getattr(value, "order11", None)
                setattr(value, "order11", self)



class rating___review:

    def __init__(self, ID: int, name: str, rating: int, reviews: str, retailerID: str, inventoryID: str):
        self.ID = ID
        self.name = name
        self.rating = rating
        self.reviews = reviews
        self.retailerID = retailerID
        self.inventoryID = inventoryID
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inventoryID(self):
        return self.__inventoryID
    @inventoryID.setter
    def inventoryID(self, inventoryID: str):
        self.__inventoryID = inventoryID

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: str):
        self.__reviews = reviews

    @property
    def retailerID(self):
        return self.__retailerID
    @retailerID.setter
    def retailerID(self, retailerID: str):
        self.__retailerID = retailerID



class Administrator:

    def __init__(self, userId: int, name: str, emailId: str, address: str, phone: int, dateOfBirth: date, adminType: str):
        self.userId = userId
        self.name = name
        self.emailId = emailId
        self.address = address
        self.phone = phone
        self.dateOfBirth = dateOfBirth
        self.adminType = adminType
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def adminType(self):
        return self.__adminType
    @adminType.setter
    def adminType(self, adminType: str):
        self.__adminType = adminType

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emailId(self):
        return self.__emailId
    @emailId.setter
    def emailId(self, emailId: str):
        self.__emailId = emailId

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone



class AccountInfo:

    def __init__(self, name: str, bankName: str, bankBranch: str, accountNumber: int, routingNumber: int, ID: int, seller7: "Farmer" = None):
        self.name = name
        self.bankName = bankName
        self.bankBranch = bankBranch
        self.accountNumber = accountNumber
        self.routingNumber = routingNumber
        self.ID = ID
        self.seller7 = seller7
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def bankBranch(self):
        return self.__bankBranch
    @bankBranch.setter
    def bankBranch(self, bankBranch: str):
        self.__bankBranch = bankBranch

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def routingNumber(self):
        return self.__routingNumber
    @routingNumber.setter
    def routingNumber(self, routingNumber: int):
        self.__routingNumber = routingNumber

    @property
    def bankName(self):
        return self.__bankName
    @bankName.setter
    def bankName(self, bankName: str):
        self.__bankName = bankName

    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: int):
        self.__accountNumber = accountNumber

    @property
    def seller7(self):
        return self.__seller7
    @seller7.setter
    def seller7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AccountInfo__seller7", None)
        self.__seller7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accountInfo6"):
                opp_val = getattr(old_value, "accountInfo6", None)
                if opp_val == self:
                    setattr(old_value, "accountInfo6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accountInfo6"):
                opp_val = getattr(value, "accountInfo6", None)
                setattr(value, "accountInfo6", self)



class Farmer:

    def __init__(self, userId: int, name: str, emailId: str, address: str, phone: int, dateOfBirth: date, type: str, accountInfoID: int, CardInfo: str, accountInfo6: "AccountInfo" = None, product_Farmer9: "Products" = None, order11: "Order" = None):
        self.userId = userId
        self.name = name
        self.emailId = emailId
        self.address = address
        self.phone = phone
        self.dateOfBirth = dateOfBirth
        self.type = type
        self.accountInfoID = accountInfoID
        self.CardInfo = CardInfo
        self.accountInfo6 = accountInfo6
        self.product_Farmer9 = product_Farmer9
        self.order11 = order11
        
        pass
    @property
    def CardInfo(self):
        return self.__CardInfo
    @CardInfo.setter
    def CardInfo(self, CardInfo: str):
        self.__CardInfo = CardInfo

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def emailId(self):
        return self.__emailId
    @emailId.setter
    def emailId(self, emailId: str):
        self.__emailId = emailId

    @property
    def accountInfoID(self):
        return self.__accountInfoID
    @accountInfoID.setter
    def accountInfoID(self, accountInfoID: int):
        self.__accountInfoID = accountInfoID

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accountInfo6(self):
        return self.__accountInfo6
    @accountInfo6.setter
    def accountInfo6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Farmer__accountInfo6", None)
        self.__accountInfo6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seller7"):
                opp_val = getattr(old_value, "seller7", None)
                if opp_val == self:
                    setattr(old_value, "seller7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seller7"):
                opp_val = getattr(value, "seller7", None)
                setattr(value, "seller7", self)

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Farmer__order11", None)
        self.__order11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farmer10"):
                opp_val = getattr(old_value, "farmer10", None)
                if opp_val == self:
                    setattr(old_value, "farmer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farmer10"):
                opp_val = getattr(value, "farmer10", None)
                setattr(value, "farmer10", self)

    @property
    def product_Farmer9(self):
        return self.__product_Farmer9
    @product_Farmer9.setter
    def product_Farmer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Farmer__product_Farmer9", None)
        self.__product_Farmer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farmer8"):
                opp_val = getattr(old_value, "farmer8", None)
                if opp_val == self:
                    setattr(old_value, "farmer8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farmer8"):
                opp_val = getattr(value, "farmer8", None)
                setattr(value, "farmer8", self)



class Retailer_Cart:

    def __init__(self, userID: int, product: Products, quantity___product: float, customer1: "Retailer" = None):
        self.userID = userID
        self.product = product
        self.quantity___product = quantity___product
        self.customer1 = customer1
        
        pass
    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product: Products):
        self.__product = product

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def quantity___product(self):
        return self.__quantity___product
    @quantity___product.setter
    def quantity___product(self, quantity___product: float):
        self.__quantity___product = quantity___product

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Retailer_Cart__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                setattr(value, "shoppingCart0", self)



class User:

    def __init__(self, Id: int, userName: str, userType: str, password: str):
        self.Id = Id
        self.userName = userName
        self.userType = userType
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userType(self):
        return self.__userType
    @userType.setter
    def userType(self, userType: str):
        self.__userType = userType

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id



class Retailer:

    def __init__(self, userId: int, name: str, emailId: str, address: str, phone: int, dateOfBirth: date, CardInfo: int, Photo: str, shoppingCart0: "Retailer_Cart" = None, cardInfo2: "CardInfo" = None, order4: "Order" = None):
        self.userId = userId
        self.name = name
        self.emailId = emailId
        self.address = address
        self.phone = phone
        self.dateOfBirth = dateOfBirth
        self.CardInfo = CardInfo
        self.Photo = Photo
        self.shoppingCart0 = shoppingCart0
        self.cardInfo2 = cardInfo2
        self.order4 = order4
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def CardInfo(self):
        return self.__CardInfo
    @CardInfo.setter
    def CardInfo(self, CardInfo: int):
        self.__CardInfo = CardInfo

    @property
    def Photo(self):
        return self.__Photo
    @Photo.setter
    def Photo(self, Photo: str):
        self.__Photo = Photo

    @property
    def emailId(self):
        return self.__emailId
    @emailId.setter
    def emailId(self, emailId: str):
        self.__emailId = emailId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def cardInfo2(self):
        return self.__cardInfo2
    @cardInfo2.setter
    def cardInfo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Retailer__cardInfo2", None)
        self.__cardInfo2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)

    @property
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Retailer__shoppingCart0", None)
        self.__shoppingCart0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if opp_val == self:
                    setattr(old_value, "customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                setattr(value, "customer1", self)

    @property
    def order4(self):
        return self.__order4
    @order4.setter
    def order4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Retailer__order4", None)
        self.__order4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)



class CardInfo:

    def __init__(self, ID: int, name: str, number: int, expiryDate: date, CVV: int, billingAddress: str, customer3: "Retailer" = None):
        self.ID = ID
        self.name = name
        self.number = number
        self.expiryDate = expiryDate
        self.CVV = CVV
        self.billingAddress = billingAddress
        self.customer3 = customer3
        
        pass
    @property
    def CVV(self):
        return self.__CVV
    @CVV.setter
    def CVV(self, CVV: int):
        self.__CVV = CVV

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def expiryDate(self):
        return self.__expiryDate
    @expiryDate.setter
    def expiryDate(self, expiryDate: date):
        self.__expiryDate = expiryDate

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardInfo__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardInfo2"):
                opp_val = getattr(old_value, "cardInfo2", None)
                if opp_val == self:
                    setattr(old_value, "cardInfo2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardInfo2"):
                opp_val = getattr(value, "cardInfo2", None)
                setattr(value, "cardInfo2", self)


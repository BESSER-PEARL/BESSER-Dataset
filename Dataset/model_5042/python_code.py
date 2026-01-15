from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class nocollectionowner_Customer:

    def __init__(self, surname: str, familyName: str, telephoneNr: str, address: str, hotel: str, comments: str, nocollectionowner_Customer: "nocollectionowner_Order" = None):
        self.surname = surname
        self.familyName = familyName
        self.telephoneNr = telephoneNr
        self.address = address
        self.hotel = hotel
        self.comments = comments
        self.nocollectionowner_Customer = nocollectionowner_Customer
        
    @property
    def familyName(self) -> str:
        return self.__familyName

    @familyName.setter
    def familyName(self, familyName: str):
        self.__familyName = familyName

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def hotel(self) -> str:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: str):
        self.__hotel = hotel

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def telephoneNr(self) -> str:
        return self.__telephoneNr

    @telephoneNr.setter
    def telephoneNr(self, telephoneNr: str):
        self.__telephoneNr = telephoneNr

    @property
    def nocollectionowner_Customer(self):
        return self.__nocollectionowner_Customer

    @nocollectionowner_Customer.setter
    def nocollectionowner_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Customer__nocollectionowner_Customer", None)
        self.__nocollectionowner_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_Order"):
                opp_val = getattr(old_value, "nocollectionowner_Order", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_Order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_Order"):
                opp_val = getattr(value, "nocollectionowner_Order", None)
                setattr(value, "nocollectionowner_Order", self)

class nocollectionowner_PriceCategory:

    def __init__(self, name: str, prices: float, nocollectionowner_PriceCategory: "nocollectionowner_Product" = None):
        self.name = name
        self.prices = prices
        self.nocollectionowner_PriceCategory = nocollectionowner_PriceCategory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prices(self) -> float:
        return self.__prices

    @prices.setter
    def prices(self, prices: float):
        self.__prices = prices

    @property
    def nocollectionowner_PriceCategory(self):
        return self.__nocollectionowner_PriceCategory

    @nocollectionowner_PriceCategory.setter
    def nocollectionowner_PriceCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_PriceCategory__nocollectionowner_PriceCategory", None)
        self.__nocollectionowner_PriceCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_Product"):
                opp_val = getattr(old_value, "nocollectionowner_Product", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_Product"):
                opp_val = getattr(value, "nocollectionowner_Product", None)
                setattr(value, "nocollectionowner_Product", self)

class nocollectionowner_ProductCategory:

    def __init__(self, name: str, productCategory: set["nocollectionowner_Product"] = None, ProductCategory5: "nocollectionowner_ProductCategory" = None, parent: set["nocollectionowner_ProductCategory"] = None, ProductCategory8: "nocollectionowner_ProductCategory" = None, subCategorys: "nocollectionowner_ProductCategory" = None, ProductCategory: "nocollectionowner_Product" = None):
        self.name = name
        self.productCategory = productCategory if productCategory is not None else set()
        self.ProductCategory5 = ProductCategory5
        self.parent = parent if parent is not None else set()
        self.ProductCategory8 = ProductCategory8
        self.subCategorys = subCategorys
        self.ProductCategory = ProductCategory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ProductCategory8(self):
        return self.__ProductCategory8

    @ProductCategory8.setter
    def ProductCategory8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__ProductCategory8", None)
        self.__ProductCategory8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategorys"):
                opp_val = getattr(old_value, "subCategorys", None)
                if opp_val == self:
                    setattr(old_value, "subCategorys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategorys"):
                opp_val = getattr(value, "subCategorys", None)
                setattr(value, "subCategorys", self)

    @property
    def ProductCategory(self):
        return self.__ProductCategory

    @ProductCategory.setter
    def ProductCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__ProductCategory", None)
        self.__ProductCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products"):
                opp_val = getattr(old_value, "products", None)
                if opp_val == self:
                    setattr(old_value, "products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products"):
                opp_val = getattr(value, "products", None)
                setattr(value, "products", self)

    @property
    def productCategory(self):
        return self.__productCategory

    @productCategory.setter
    def productCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__productCategory", None)
        self.__productCategory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    if opp_val == self:
                        setattr(item, "Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    setattr(item, "Product", self)
                    

    @property
    def ProductCategory5(self):
        return self.__ProductCategory5

    @ProductCategory5.setter
    def ProductCategory5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__ProductCategory5", None)
        self.__ProductCategory5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProductCategory5"):
                    opp_val = getattr(item, "ProductCategory5", None)
                    
                    if opp_val == self:
                        setattr(item, "ProductCategory5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProductCategory5"):
                    opp_val = getattr(item, "ProductCategory5", None)
                    
                    setattr(item, "ProductCategory5", self)
                    

    @property
    def subCategorys(self):
        return self.__subCategorys

    @subCategorys.setter
    def subCategorys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_ProductCategory__subCategorys", None)
        self.__subCategorys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProductCategory8"):
                opp_val = getattr(old_value, "ProductCategory8", None)
                if opp_val == self:
                    setattr(old_value, "ProductCategory8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProductCategory8"):
                opp_val = getattr(value, "ProductCategory8", None)
                setattr(value, "ProductCategory8", self)

class nocollectionowner_Product:

    def __init__(self, name: str, number: str, description: str, Product: "nocollectionowner_ProductCategory" = None, products: "nocollectionowner_ProductCategory" = None, nocollectionowner_Product: "nocollectionowner_PriceCategory" = None, nocollectionowner_Product13: "nocollectionowner_Transaction" = None):
        self.name = name
        self.number = number
        self.description = description
        self.Product = Product
        self.products = products
        self.nocollectionowner_Product = nocollectionowner_Product
        self.nocollectionowner_Product13 = nocollectionowner_Product13
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Product__Product", None)
        self.__Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "productCategory"):
                opp_val = getattr(old_value, "productCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "productCategory"):
                opp_val = getattr(value, "productCategory", None)
                if opp_val is None:
                    setattr(value, "productCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Product__products", None)
        self.__products = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProductCategory"):
                opp_val = getattr(old_value, "ProductCategory", None)
                if opp_val == self:
                    setattr(old_value, "ProductCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProductCategory"):
                opp_val = getattr(value, "ProductCategory", None)
                setattr(value, "ProductCategory", self)

    @property
    def nocollectionowner_Product(self):
        return self.__nocollectionowner_Product

    @nocollectionowner_Product.setter
    def nocollectionowner_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Product__nocollectionowner_Product", None)
        self.__nocollectionowner_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_PriceCategory"):
                opp_val = getattr(old_value, "nocollectionowner_PriceCategory", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_PriceCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_PriceCategory"):
                opp_val = getattr(value, "nocollectionowner_PriceCategory", None)
                setattr(value, "nocollectionowner_PriceCategory", self)

    @property
    def nocollectionowner_Product13(self):
        return self.__nocollectionowner_Product13

    @nocollectionowner_Product13.setter
    def nocollectionowner_Product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Product__nocollectionowner_Product13", None)
        self.__nocollectionowner_Product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_Transaction"):
                opp_val = getattr(old_value, "nocollectionowner_Transaction", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_Transaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_Transaction"):
                opp_val = getattr(value, "nocollectionowner_Transaction", None)
                setattr(value, "nocollectionowner_Transaction", self)

class nocollectionowner_Transaction:

    def __init__(self, number: str, startDate: date, endDate: date, price: float, paidDate: date, Transaction: "nocollectionowner_Order" = None, transactions: "nocollectionowner_Order" = None, nocollectionowner_Transaction: "nocollectionowner_Product" = None):
        self.number = number
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.paidDate = paidDate
        self.Transaction = Transaction
        self.transactions = transactions
        self.nocollectionowner_Transaction = nocollectionowner_Transaction
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def paidDate(self) -> date:
        return self.__paidDate

    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Transaction__transactions", None)
        self.__transactions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order"):
                opp_val = getattr(old_value, "Order", None)
                if opp_val == self:
                    setattr(old_value, "Order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order"):
                opp_val = getattr(value, "Order", None)
                setattr(value, "Order", self)

    @property
    def nocollectionowner_Transaction(self):
        return self.__nocollectionowner_Transaction

    @nocollectionowner_Transaction.setter
    def nocollectionowner_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Transaction__nocollectionowner_Transaction", None)
        self.__nocollectionowner_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_Product13"):
                opp_val = getattr(old_value, "nocollectionowner_Product13", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_Product13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_Product13"):
                opp_val = getattr(value, "nocollectionowner_Product13", None)
                setattr(value, "nocollectionowner_Product13", self)

    @property
    def Transaction(self):
        return self.__Transaction

    @Transaction.setter
    def Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Transaction__Transaction", None)
        self.__Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order"):
                opp_val = getattr(old_value, "order", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order"):
                opp_val = getattr(value, "order", None)
                if opp_val is None:
                    setattr(value, "order", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nocollectionowner_Order:

    def __init__(self, number: str, comments: str, order: set["nocollectionowner_Transaction"] = None, nocollectionowner_Order: "nocollectionowner_Customer" = None, Order: "nocollectionowner_Transaction" = None):
        self.number = number
        self.comments = comments
        self.order = order if order is not None else set()
        self.nocollectionowner_Order = nocollectionowner_Order
        self.Order = Order
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def nocollectionowner_Order(self):
        return self.__nocollectionowner_Order

    @nocollectionowner_Order.setter
    def nocollectionowner_Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Order__nocollectionowner_Order", None)
        self.__nocollectionowner_Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nocollectionowner_Customer"):
                opp_val = getattr(old_value, "nocollectionowner_Customer", None)
                if opp_val == self:
                    setattr(old_value, "nocollectionowner_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nocollectionowner_Customer"):
                opp_val = getattr(value, "nocollectionowner_Customer", None)
                setattr(value, "nocollectionowner_Customer", self)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Order__order", None)
        self.__order = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    setattr(item, "Transaction", self)
                    

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nocollectionowner_Order__Order", None)
        self.__Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions"):
                opp_val = getattr(old_value, "transactions", None)
                if opp_val == self:
                    setattr(old_value, "transactions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions"):
                opp_val = getattr(value, "transactions", None)
                setattr(value, "transactions", self)

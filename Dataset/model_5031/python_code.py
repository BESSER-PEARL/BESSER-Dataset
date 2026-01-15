from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class shop_Transaction:

    def __init__(self, number: str, startDate: date, endDate: date, price: float, paidDate: date, Transaction: "shop_Order" = None, transactions: "shop_Order" = None, shop_Transaction: "shop_Product" = None):
        self.number = number
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.paidDate = paidDate
        self.Transaction = Transaction
        self.transactions = transactions
        self.shop_Transaction = shop_Transaction
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def paidDate(self) -> date:
        return self.__paidDate

    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

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
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Transaction__transactions", None)
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
    def shop_Transaction(self):
        return self.__shop_Transaction

    @shop_Transaction.setter
    def shop_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Transaction__shop_Transaction", None)
        self.__shop_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Product13"):
                opp_val = getattr(old_value, "shop_Product13", None)
                if opp_val == self:
                    setattr(old_value, "shop_Product13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Product13"):
                opp_val = getattr(value, "shop_Product13", None)
                setattr(value, "shop_Product13", self)

    @property
    def Transaction(self):
        return self.__Transaction

    @Transaction.setter
    def Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Transaction__Transaction", None)
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

class shop_Order:

    def __init__(self, number: str, comments: str, order: set["shop_Transaction"] = None, shop_Order: "shop_Customer" = None, Order: "shop_Transaction" = None):
        self.number = number
        self.comments = comments
        self.order = order if order is not None else set()
        self.shop_Order = shop_Order
        self.Order = Order
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def shop_Order(self):
        return self.__shop_Order

    @shop_Order.setter
    def shop_Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Order__shop_Order", None)
        self.__shop_Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Customer"):
                opp_val = getattr(old_value, "shop_Customer", None)
                if opp_val == self:
                    setattr(old_value, "shop_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Customer"):
                opp_val = getattr(value, "shop_Customer", None)
                setattr(value, "shop_Customer", self)

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Order__Order", None)
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

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Order__order", None)
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
                    

class shop_Customer:

    def __init__(self, hotel: str, comments: str, surname: str, familyName: str, telephoneNr: str, address: str, shop_Customer: "shop_Order" = None):
        self.hotel = hotel
        self.comments = comments
        self.surname = surname
        self.familyName = familyName
        self.telephoneNr = telephoneNr
        self.address = address
        self.shop_Customer = shop_Customer
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def telephoneNr(self) -> str:
        return self.__telephoneNr

    @telephoneNr.setter
    def telephoneNr(self, telephoneNr: str):
        self.__telephoneNr = telephoneNr

    @property
    def hotel(self) -> str:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: str):
        self.__hotel = hotel

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def familyName(self) -> str:
        return self.__familyName

    @familyName.setter
    def familyName(self, familyName: str):
        self.__familyName = familyName

    @property
    def shop_Customer(self):
        return self.__shop_Customer

    @shop_Customer.setter
    def shop_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Customer__shop_Customer", None)
        self.__shop_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Order"):
                opp_val = getattr(old_value, "shop_Order", None)
                if opp_val == self:
                    setattr(old_value, "shop_Order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Order"):
                opp_val = getattr(value, "shop_Order", None)
                setattr(value, "shop_Order", self)

class shop_PriceCategory:

    def __init__(self, name: str, prices: float, shop_PriceCategory: "shop_Product" = None):
        self.name = name
        self.prices = prices
        self.shop_PriceCategory = shop_PriceCategory
        
    @property
    def prices(self) -> float:
        return self.__prices

    @prices.setter
    def prices(self, prices: float):
        self.__prices = prices

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shop_PriceCategory(self):
        return self.__shop_PriceCategory

    @shop_PriceCategory.setter
    def shop_PriceCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_PriceCategory__shop_PriceCategory", None)
        self.__shop_PriceCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Product"):
                opp_val = getattr(old_value, "shop_Product", None)
                if opp_val == self:
                    setattr(old_value, "shop_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Product"):
                opp_val = getattr(value, "shop_Product", None)
                setattr(value, "shop_Product", self)

class shop_ProductCategory:

    def __init__(self, name: str, productCategory: set["shop_Product"] = None, ProductCategory: "shop_Product" = None, ProductCategory5: "shop_ProductCategory" = None, parent: set["shop_ProductCategory"] = None, ProductCategory8: "shop_ProductCategory" = None, subCategorys: "shop_ProductCategory" = None):
        self.name = name
        self.productCategory = productCategory if productCategory is not None else set()
        self.ProductCategory = ProductCategory
        self.ProductCategory5 = ProductCategory5
        self.parent = parent if parent is not None else set()
        self.ProductCategory8 = ProductCategory8
        self.subCategorys = subCategorys
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__parent", None)
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
    def ProductCategory5(self):
        return self.__ProductCategory5

    @ProductCategory5.setter
    def ProductCategory5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__ProductCategory5", None)
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
    def subCategorys(self):
        return self.__subCategorys

    @subCategorys.setter
    def subCategorys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__subCategorys", None)
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

    @property
    def productCategory(self):
        return self.__productCategory

    @productCategory.setter
    def productCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__productCategory", None)
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
    def ProductCategory(self):
        return self.__ProductCategory

    @ProductCategory.setter
    def ProductCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__ProductCategory", None)
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
    def ProductCategory8(self):
        return self.__ProductCategory8

    @ProductCategory8.setter
    def ProductCategory8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_ProductCategory__ProductCategory8", None)
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

class shop_Product:

    def __init__(self, name: str, number: str, description: str, Product: "shop_ProductCategory" = None, products: "shop_ProductCategory" = None, shop_Product: "shop_PriceCategory" = None, shop_Product13: "shop_Transaction" = None):
        self.name = name
        self.number = number
        self.description = description
        self.Product = Product
        self.products = products
        self.shop_Product = shop_Product
        self.shop_Product13 = shop_Product13
        
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
    def shop_Product13(self):
        return self.__shop_Product13

    @shop_Product13.setter
    def shop_Product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Product__shop_Product13", None)
        self.__shop_Product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Transaction"):
                opp_val = getattr(old_value, "shop_Transaction", None)
                if opp_val == self:
                    setattr(old_value, "shop_Transaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Transaction"):
                opp_val = getattr(value, "shop_Transaction", None)
                setattr(value, "shop_Transaction", self)

    @property
    def shop_Product(self):
        return self.__shop_Product

    @shop_Product.setter
    def shop_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Product__shop_Product", None)
        self.__shop_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_PriceCategory"):
                opp_val = getattr(old_value, "shop_PriceCategory", None)
                if opp_val == self:
                    setattr(old_value, "shop_PriceCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_PriceCategory"):
                opp_val = getattr(value, "shop_PriceCategory", None)
                setattr(value, "shop_PriceCategory", self)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Product__products", None)
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
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Product__Product", None)
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

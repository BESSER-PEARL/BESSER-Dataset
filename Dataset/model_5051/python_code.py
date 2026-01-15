from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class eShop_Product:

    def __init__(self, price: int, stock: int, Product: "eShop_SaleLine" = None, product: set["eShop_SaleLine"] = None):
        self.price = price
        self.stock = stock
        self.Product = Product
        self.product = product if product is not None else set()
        
    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Product__Product", None)
        self.__Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salesLines"):
                opp_val = getattr(old_value, "salesLines", None)
                if opp_val == self:
                    setattr(old_value, "salesLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salesLines"):
                opp_val = getattr(value, "salesLines", None)
                setattr(value, "salesLines", self)

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Product__product", None)
        self.__product = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SaleLine11"):
                    opp_val = getattr(item, "SaleLine11", None)
                    
                    if opp_val == self:
                        setattr(item, "SaleLine11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SaleLine11"):
                    opp_val = getattr(item, "SaleLine11", None)
                    
                    setattr(item, "SaleLine11", self)
                    

class eShop_SaleLine:

    def __init__(self, quantity: int, SaleLine: "eShop_Sale" = None, lines: "eShop_Sale" = None, salesLines: "eShop_Product" = None, SaleLine11: "eShop_Product" = None):
        self.quantity = quantity
        self.SaleLine = SaleLine
        self.lines = lines
        self.salesLines = salesLines
        self.SaleLine11 = SaleLine11
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def SaleLine11(self):
        return self.__SaleLine11

    @SaleLine11.setter
    def SaleLine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_SaleLine__SaleLine11", None)
        self.__SaleLine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product"):
                opp_val = getattr(old_value, "product", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product"):
                opp_val = getattr(value, "product", None)
                if opp_val is None:
                    setattr(value, "product", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_SaleLine__lines", None)
        self.__lines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sale8"):
                opp_val = getattr(old_value, "Sale8", None)
                if opp_val == self:
                    setattr(old_value, "Sale8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sale8"):
                opp_val = getattr(value, "Sale8", None)
                setattr(value, "Sale8", self)

    @property
    def SaleLine(self):
        return self.__SaleLine

    @SaleLine.setter
    def SaleLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_SaleLine__SaleLine", None)
        self.__SaleLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale6"):
                opp_val = getattr(old_value, "sale6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale6"):
                opp_val = getattr(value, "sale6", None)
                if opp_val is None:
                    setattr(value, "sale6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def salesLines(self):
        return self.__salesLines

    @salesLines.setter
    def salesLines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_SaleLine__salesLines", None)
        self.__salesLines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product"):
                opp_val = getattr(old_value, "Product", None)
                if opp_val == self:
                    setattr(old_value, "Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product"):
                opp_val = getattr(value, "Product", None)
                setattr(value, "Product", self)

class eShop_Sale:

    def __init__(self, id: int, paid: bool, amount: int, Sale: "eShop_Customer" = None, sale: "eShop_Customer" = None, sale6: set["eShop_SaleLine"] = None, Sale8: "eShop_SaleLine" = None):
        self.id = id
        self.paid = paid
        self.amount = amount
        self.Sale = Sale
        self.sale = sale
        self.sale6 = sale6 if sale6 is not None else set()
        self.Sale8 = Sale8
        
    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def paid(self) -> bool:
        return self.__paid

    @paid.setter
    def paid(self, paid: bool):
        self.__paid = paid

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Sale8(self):
        return self.__Sale8

    @Sale8.setter
    def Sale8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Sale__Sale8", None)
        self.__Sale8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lines"):
                opp_val = getattr(old_value, "lines", None)
                if opp_val == self:
                    setattr(old_value, "lines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lines"):
                opp_val = getattr(value, "lines", None)
                setattr(value, "lines", self)

    @property
    def Sale(self):
        return self.__Sale

    @Sale.setter
    def Sale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Sale__Sale", None)
        self.__Sale = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaser"):
                opp_val = getattr(old_value, "purchaser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaser"):
                opp_val = getattr(value, "purchaser", None)
                if opp_val is None:
                    setattr(value, "purchaser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sale6(self):
        return self.__sale6

    @sale6.setter
    def sale6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Sale__sale6", None)
        self.__sale6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SaleLine"):
                    opp_val = getattr(item, "SaleLine", None)
                    
                    if opp_val == self:
                        setattr(item, "SaleLine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SaleLine"):
                    opp_val = getattr(item, "SaleLine", None)
                    
                    setattr(item, "SaleLine", self)
                    

    @property
    def sale(self):
        return self.__sale

    @sale.setter
    def sale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Sale__sale", None)
        self.__sale = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer4"):
                opp_val = getattr(old_value, "Customer4", None)
                if opp_val == self:
                    setattr(old_value, "Customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer4"):
                opp_val = getattr(value, "Customer4", None)
                setattr(value, "Customer4", self)

    def addSaleLine(self, p: str, quantity: int) -> str:
        # TODO: Implement addSaleLine method
        pass

class eShop_Portal:

    def __init__(self, name: str, url: str, portal: set["eShop_Customer"] = None, Portal: "eShop_Customer" = None):
        self.name = name
        self.url = url
        self.portal = portal if portal is not None else set()
        self.Portal = Portal
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Portal(self):
        return self.__Portal

    @Portal.setter
    def Portal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Portal__Portal", None)
        self.__Portal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers"):
                opp_val = getattr(old_value, "customers", None)
                if opp_val == self:
                    setattr(old_value, "customers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers"):
                opp_val = getattr(value, "customers", None)
                setattr(value, "customers", self)

    @property
    def portal(self):
        return self.__portal

    @portal.setter
    def portal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Portal__portal", None)
        self.__portal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    setattr(item, "Customer", self)
                    

    def removeGoldCategory(self, c: Customer):
        # TODO: Implement removeGoldCategory method
        pass

class eShop_Customer:

    def __init__(self, name: int, Customer: "eShop_Portal" = None, customers: "eShop_Portal" = None, purchaser: set["eShop_Sale"] = None, Customer4: "eShop_Sale" = None):
        self.name = name
        self.Customer = Customer
        self.customers = customers
        self.purchaser = purchaser if purchaser is not None else set()
        self.Customer4 = Customer4
        
    @property
    def name(self) -> int:
        return self.__name

    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "portal"):
                opp_val = getattr(old_value, "portal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "portal"):
                opp_val = getattr(value, "portal", None)
                if opp_val is None:
                    setattr(value, "portal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def purchaser(self):
        return self.__purchaser

    @purchaser.setter
    def purchaser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Customer__purchaser", None)
        self.__purchaser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sale"):
                    opp_val = getattr(item, "Sale", None)
                    
                    if opp_val == self:
                        setattr(item, "Sale", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sale"):
                    opp_val = getattr(item, "Sale", None)
                    
                    setattr(item, "Sale", self)
                    

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Customer__customers", None)
        self.__customers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Portal"):
                opp_val = getattr(old_value, "Portal", None)
                if opp_val == self:
                    setattr(old_value, "Portal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Portal"):
                opp_val = getattr(value, "Portal", None)
                setattr(value, "Portal", self)

    @property
    def Customer4(self):
        return self.__Customer4

    @Customer4.setter
    def Customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eShop_Customer__Customer4", None)
        self.__Customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale"):
                opp_val = getattr(old_value, "sale", None)
                if opp_val == self:
                    setattr(old_value, "sale", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale"):
                opp_val = getattr(value, "sale", None)
                setattr(value, "sale", self)

    def newCustomer(self, p: str, name: int) -> str:
        # TODO: Implement newCustomer method
        pass

class Customer:

    pass
class eShop_GoldCustomer(Customer):

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class amazoninformational_Invoice:

    pass
class amazoninformational_Shipment:

    pass
class amazoninformational_Product:

    def __init__(self, onHand: int, amazoninformational_Product9: "amazoninformational_Package" = None, amazoninformational_Product: "amazoninformational_Order" = None):
        self.onHand = onHand
        self.amazoninformational_Product9 = amazoninformational_Product9
        self.amazoninformational_Product = amazoninformational_Product
        
    @property
    def onHand(self) -> int:
        return self.__onHand

    @onHand.setter
    def onHand(self, onHand: int):
        self.__onHand = onHand

    @property
    def amazoninformational_Product9(self):
        return self.__amazoninformational_Product9

    @amazoninformational_Product9.setter
    def amazoninformational_Product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Product__amazoninformational_Product9", None)
        self.__amazoninformational_Product9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Package"):
                opp_val = getattr(old_value, "amazoninformational_Package", None)
                if opp_val == self:
                    setattr(old_value, "amazoninformational_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Package"):
                opp_val = getattr(value, "amazoninformational_Package", None)
                setattr(value, "amazoninformational_Package", self)

    @property
    def amazoninformational_Product(self):
        return self.__amazoninformational_Product

    @amazoninformational_Product.setter
    def amazoninformational_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Product__amazoninformational_Product", None)
        self.__amazoninformational_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Order"):
                opp_val = getattr(old_value, "amazoninformational_Order", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Order"):
                opp_val = getattr(value, "amazoninformational_Order", None)
                if opp_val is None:
                    setattr(value, "amazoninformational_Order", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class amazoninformational_Order:

    def __init__(self, status: str, totalAmount: float, order3: "amazoninformational_Invoice" = None, order5: set["amazoninformational_Package"] = None, amazoninformational_Order7: "amazoninformational_Customer" = None, Order: "amazoninformational_Package" = None, Order14: "amazoninformational_Shipment" = None, Order16: "amazoninformational_Invoice" = None, amazoninformational_Order: set["amazoninformational_Product"] = None, order: "amazoninformational_Shipment" = None):
        self.status = status
        self.totalAmount = totalAmount
        self.order3 = order3
        self.order5 = order5 if order5 is not None else set()
        self.amazoninformational_Order7 = amazoninformational_Order7
        self.Order = Order
        self.Order14 = Order14
        self.Order16 = Order16
        self.amazoninformational_Order = amazoninformational_Order if amazoninformational_Order is not None else set()
        self.order = order
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def totalAmount(self) -> float:
        return self.__totalAmount

    @totalAmount.setter
    def totalAmount(self, totalAmount: float):
        self.__totalAmount = totalAmount

    @property
    def order3(self):
        return self.__order3

    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__order3", None)
        self.__order3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Invoice"):
                opp_val = getattr(old_value, "Invoice", None)
                if opp_val == self:
                    setattr(old_value, "Invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Invoice"):
                opp_val = getattr(value, "Invoice", None)
                setattr(value, "Invoice", self)

    @property
    def Order16(self):
        return self.__Order16

    @Order16.setter
    def Order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__Order16", None)
        self.__Order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoice"):
                opp_val = getattr(old_value, "invoice", None)
                if opp_val == self:
                    setattr(old_value, "invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoice"):
                opp_val = getattr(value, "invoice", None)
                setattr(value, "invoice", self)

    @property
    def Order14(self):
        return self.__Order14

    @Order14.setter
    def Order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__Order14", None)
        self.__Order14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shipment"):
                opp_val = getattr(old_value, "shipment", None)
                if opp_val == self:
                    setattr(old_value, "shipment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shipment"):
                opp_val = getattr(value, "shipment", None)
                setattr(value, "shipment", self)

    @property
    def amazoninformational_Order7(self):
        return self.__amazoninformational_Order7

    @amazoninformational_Order7.setter
    def amazoninformational_Order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__amazoninformational_Order7", None)
        self.__amazoninformational_Order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Customer"):
                opp_val = getattr(old_value, "amazoninformational_Customer", None)
                if opp_val == self:
                    setattr(old_value, "amazoninformational_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Customer"):
                opp_val = getattr(value, "amazoninformational_Customer", None)
                setattr(value, "amazoninformational_Customer", self)

    @property
    def order5(self):
        return self.__order5

    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__order5", None)
        self.__order5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__Order", None)
        self.__Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packages"):
                opp_val = getattr(old_value, "packages", None)
                if opp_val == self:
                    setattr(old_value, "packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packages"):
                opp_val = getattr(value, "packages", None)
                setattr(value, "packages", self)

    @property
    def amazoninformational_Order(self):
        return self.__amazoninformational_Order

    @amazoninformational_Order.setter
    def amazoninformational_Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__amazoninformational_Order", None)
        self.__amazoninformational_Order = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amazoninformational_Product"):
                    opp_val = getattr(item, "amazoninformational_Product", None)
                    
                    if opp_val == self:
                        setattr(item, "amazoninformational_Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amazoninformational_Product"):
                    opp_val = getattr(item, "amazoninformational_Product", None)
                    
                    setattr(item, "amazoninformational_Product", self)
                    

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Order__order", None)
        self.__order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shipment"):
                opp_val = getattr(old_value, "Shipment", None)
                if opp_val == self:
                    setattr(old_value, "Shipment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shipment"):
                opp_val = getattr(value, "Shipment", None)
                setattr(value, "Shipment", self)

class amazoninformational_Payment:

    pass
class amazoninformational_Customer:

    def __init__(self, inGoodStanding: bool, creditLimit: float, consummedCredit: float, address: str, isVIP: bool, amazoninformational_Customer: "amazoninformational_Order" = None):
        self.inGoodStanding = inGoodStanding
        self.creditLimit = creditLimit
        self.consummedCredit = consummedCredit
        self.address = address
        self.isVIP = isVIP
        self.amazoninformational_Customer = amazoninformational_Customer
        
    @property
    def creditLimit(self) -> float:
        return self.__creditLimit

    @creditLimit.setter
    def creditLimit(self, creditLimit: float):
        self.__creditLimit = creditLimit

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def consummedCredit(self) -> float:
        return self.__consummedCredit

    @consummedCredit.setter
    def consummedCredit(self, consummedCredit: float):
        self.__consummedCredit = consummedCredit

    @property
    def isVIP(self) -> bool:
        return self.__isVIP

    @isVIP.setter
    def isVIP(self, isVIP: bool):
        self.__isVIP = isVIP

    @property
    def inGoodStanding(self) -> bool:
        return self.__inGoodStanding

    @inGoodStanding.setter
    def inGoodStanding(self, inGoodStanding: bool):
        self.__inGoodStanding = inGoodStanding

    @property
    def amazoninformational_Customer(self):
        return self.__amazoninformational_Customer

    @amazoninformational_Customer.setter
    def amazoninformational_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Customer__amazoninformational_Customer", None)
        self.__amazoninformational_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Order7"):
                opp_val = getattr(old_value, "amazoninformational_Order7", None)
                if opp_val == self:
                    setattr(old_value, "amazoninformational_Order7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Order7"):
                opp_val = getattr(value, "amazoninformational_Order7", None)
                setattr(value, "amazoninformational_Order7", self)

class amazoninformational_Package:

    def __init__(self, location: str, Package: "amazoninformational_Order" = None, amazoninformational_Package: "amazoninformational_Product" = None, packages: "amazoninformational_Order" = None, amazoninformational_Package12: "amazoninformational_Shipment" = None):
        self.location = location
        self.Package = Package
        self.amazoninformational_Package = amazoninformational_Package
        self.packages = packages
        self.amazoninformational_Package12 = amazoninformational_Package12
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Package__packages", None)
        self.__packages = value
        
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
    def amazoninformational_Package(self):
        return self.__amazoninformational_Package

    @amazoninformational_Package.setter
    def amazoninformational_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Package__amazoninformational_Package", None)
        self.__amazoninformational_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Product9"):
                opp_val = getattr(old_value, "amazoninformational_Product9", None)
                if opp_val == self:
                    setattr(old_value, "amazoninformational_Product9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Product9"):
                opp_val = getattr(value, "amazoninformational_Product9", None)
                setattr(value, "amazoninformational_Product9", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                if opp_val is None:
                    setattr(value, "order5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amazoninformational_Package12(self):
        return self.__amazoninformational_Package12

    @amazoninformational_Package12.setter
    def amazoninformational_Package12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Package__amazoninformational_Package12", None)
        self.__amazoninformational_Package12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Shipment"):
                opp_val = getattr(old_value, "amazoninformational_Shipment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Shipment"):
                opp_val = getattr(value, "amazoninformational_Shipment", None)
                if opp_val is None:
                    setattr(value, "amazoninformational_Shipment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

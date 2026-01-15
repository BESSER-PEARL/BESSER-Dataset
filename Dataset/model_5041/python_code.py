from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VoucherType(Enum):
    RECEIPTVOUCHER = "RECEIPTVOUCHER"
    EXPENDITURE = "EXPENDITURE"
class BillingType(Enum):
    INVOICE = "INVOICE"
    LETTER = "LETTER"
    OFFER = "OFFER"
    ORDER = "ORDER"
    CONFIRMATION = "CONFIRMATION"
    DELIVERY = "DELIVERY"
    CREDIT = "CREDIT"
    DUNNING = "DUNNING"
    PROFORMA = "PROFORMA"
    NONE = "NONE"
class ReliabilityType(Enum):
    NONE = "NONE"
    POOR = "POOR"
    MEDIUM = "MEDIUM"
    GOOD = "GOOD"
class ShippingVatType(Enum):
    SHIPPINGVATFIX = "SHIPPINGVATFIX"
    SHIPPINGVATGROSS = "SHIPPINGVATGROSS"
    SHIPPINGVATNET = "SHIPPINGVATNET"
class ContactType(Enum):
    BILLING = "BILLING"
    DELIVERY = "DELIVERY"
class ItemType(Enum):
    POSITION = "POSITION"
    FREETEXT = "FREETEXT"
    DELIVERY_PART = "DELIVERY_PART"
    SUBTOTAL = "SUBTOTAL"


############################################
# Definition of Classes
############################################

class IDescribableEntity:

    pass
class Document:

    pass
class model_Credit(Document):

    pass
class model_Dunning(Document):

    def __init__(self, dunningLevel: str):
        self.dunningLevel = dunningLevel
        
    @property
    def dunningLevel(self) -> str:
        return self.__dunningLevel

    @dunningLevel.setter
    def dunningLevel(self, dunningLevel: str):
        self.__dunningLevel = dunningLevel

class model_Proforma(Document):

    pass
class model_Delivery(Document):

    pass
class model_Order(Document):

    pass
class model_Letter(Document):

    pass
class model_Confirmation(Document):

    pass
class model_Offer(Document):

    pass
class model_Product(IDescribableEntity):

    def __init__(self, webshopId: str, weight: str, block1: str, block2: str, block3: str, block4: str, block5: str, picture: str, itemNumber: str, price1: str, price2: str, price3: str, price4: str, price5: str, quantity: str, quantityUnit: str, sellingUnit: str, gtin: str, costPrice: str, cdf01: str, cdf02: str, cdf03: str, model_Product: "model_DocumentItem" = None, model_Product52: "model_ProductCategory" = None, model_Product54: set["model_ProductOptions"] = None, model_Product56: "model_VAT" = None, model_Product59: set["model_ProductBlockPrice"] = None):
        self.webshopId = webshopId
        self.weight = weight
        self.block1 = block1
        self.block2 = block2
        self.block3 = block3
        self.block4 = block4
        self.block5 = block5
        self.picture = picture
        self.itemNumber = itemNumber
        self.price1 = price1
        self.price2 = price2
        self.price3 = price3
        self.price4 = price4
        self.price5 = price5
        self.quantity = quantity
        self.quantityUnit = quantityUnit
        self.sellingUnit = sellingUnit
        self.gtin = gtin
        self.costPrice = costPrice
        self.cdf01 = cdf01
        self.cdf02 = cdf02
        self.cdf03 = cdf03
        self.model_Product = model_Product
        self.model_Product52 = model_Product52
        self.model_Product54 = model_Product54 if model_Product54 is not None else set()
        self.model_Product56 = model_Product56
        self.model_Product59 = model_Product59 if model_Product59 is not None else set()
        
    @property
    def cdf03(self) -> str:
        return self.__cdf03

    @cdf03.setter
    def cdf03(self, cdf03: str):
        self.__cdf03 = cdf03

    @property
    def itemNumber(self) -> str:
        return self.__itemNumber

    @itemNumber.setter
    def itemNumber(self, itemNumber: str):
        self.__itemNumber = itemNumber

    @property
    def price2(self) -> str:
        return self.__price2

    @price2.setter
    def price2(self, price2: str):
        self.__price2 = price2

    @property
    def block2(self) -> str:
        return self.__block2

    @block2.setter
    def block2(self, block2: str):
        self.__block2 = block2

    @property
    def block1(self) -> str:
        return self.__block1

    @block1.setter
    def block1(self, block1: str):
        self.__block1 = block1

    @property
    def quantityUnit(self) -> str:
        return self.__quantityUnit

    @quantityUnit.setter
    def quantityUnit(self, quantityUnit: str):
        self.__quantityUnit = quantityUnit

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def costPrice(self) -> str:
        return self.__costPrice

    @costPrice.setter
    def costPrice(self, costPrice: str):
        self.__costPrice = costPrice

    @property
    def block3(self) -> str:
        return self.__block3

    @block3.setter
    def block3(self, block3: str):
        self.__block3 = block3

    @property
    def webshopId(self) -> str:
        return self.__webshopId

    @webshopId.setter
    def webshopId(self, webshopId: str):
        self.__webshopId = webshopId

    @property
    def price3(self) -> str:
        return self.__price3

    @price3.setter
    def price3(self, price3: str):
        self.__price3 = price3

    @property
    def price5(self) -> str:
        return self.__price5

    @price5.setter
    def price5(self, price5: str):
        self.__price5 = price5

    @property
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def gtin(self) -> str:
        return self.__gtin

    @gtin.setter
    def gtin(self, gtin: str):
        self.__gtin = gtin

    @property
    def cdf02(self) -> str:
        return self.__cdf02

    @cdf02.setter
    def cdf02(self, cdf02: str):
        self.__cdf02 = cdf02

    @property
    def block5(self) -> str:
        return self.__block5

    @block5.setter
    def block5(self, block5: str):
        self.__block5 = block5

    @property
    def cdf01(self) -> str:
        return self.__cdf01

    @cdf01.setter
    def cdf01(self, cdf01: str):
        self.__cdf01 = cdf01

    @property
    def sellingUnit(self) -> str:
        return self.__sellingUnit

    @sellingUnit.setter
    def sellingUnit(self, sellingUnit: str):
        self.__sellingUnit = sellingUnit

    @property
    def price1(self) -> str:
        return self.__price1

    @price1.setter
    def price1(self, price1: str):
        self.__price1 = price1

    @property
    def block4(self) -> str:
        return self.__block4

    @block4.setter
    def block4(self, block4: str):
        self.__block4 = block4

    @property
    def price4(self) -> str:
        return self.__price4

    @price4.setter
    def price4(self, price4: str):
        self.__price4 = price4

    @property
    def model_Product54(self):
        return self.__model_Product54

    @model_Product54.setter
    def model_Product54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Product__model_Product54", None)
        self.__model_Product54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ProductOptions"):
                    opp_val = getattr(item, "model_ProductOptions", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ProductOptions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ProductOptions"):
                    opp_val = getattr(item, "model_ProductOptions", None)
                    
                    setattr(item, "model_ProductOptions", self)
                    

    @property
    def model_Product59(self):
        return self.__model_Product59

    @model_Product59.setter
    def model_Product59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Product__model_Product59", None)
        self.__model_Product59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ProductBlockPrice"):
                    opp_val = getattr(item, "model_ProductBlockPrice", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ProductBlockPrice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ProductBlockPrice"):
                    opp_val = getattr(item, "model_ProductBlockPrice", None)
                    
                    setattr(item, "model_ProductBlockPrice", self)
                    

    @property
    def model_Product56(self):
        return self.__model_Product56

    @model_Product56.setter
    def model_Product56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Product__model_Product56", None)
        self.__model_Product56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VAT57"):
                opp_val = getattr(old_value, "model_VAT57", None)
                if opp_val == self:
                    setattr(old_value, "model_VAT57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VAT57"):
                opp_val = getattr(value, "model_VAT57", None)
                setattr(value, "model_VAT57", self)

    @property
    def model_Product52(self):
        return self.__model_Product52

    @model_Product52.setter
    def model_Product52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Product__model_Product52", None)
        self.__model_Product52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ProductCategory"):
                opp_val = getattr(old_value, "model_ProductCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_ProductCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ProductCategory"):
                opp_val = getattr(value, "model_ProductCategory", None)
                setattr(value, "model_ProductCategory", self)

    @property
    def model_Product(self):
        return self.__model_Product

    @model_Product.setter
    def model_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Product__model_Product", None)
        self.__model_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DocumentItem34"):
                opp_val = getattr(old_value, "model_DocumentItem34", None)
                if opp_val == self:
                    setattr(old_value, "model_DocumentItem34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DocumentItem34"):
                opp_val = getattr(value, "model_DocumentItem34", None)
                setattr(value, "model_DocumentItem34", self)

class model_Shipping(IDescribableEntity):

    def __init__(self, autoVat: str, shippingValue: str, code: str, model_Shipping: "model_Document" = None, model_Shipping61: "model_VAT" = None, model_Shipping64: "model_ShippingCategory" = None):
        self.autoVat = autoVat
        self.shippingValue = shippingValue
        self.code = code
        self.model_Shipping = model_Shipping
        self.model_Shipping61 = model_Shipping61
        self.model_Shipping64 = model_Shipping64
        
    @property
    def shippingValue(self) -> str:
        return self.__shippingValue

    @shippingValue.setter
    def shippingValue(self, shippingValue: str):
        self.__shippingValue = shippingValue

    @property
    def autoVat(self) -> str:
        return self.__autoVat

    @autoVat.setter
    def autoVat(self, autoVat: str):
        self.__autoVat = autoVat

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def model_Shipping(self):
        return self.__model_Shipping

    @model_Shipping.setter
    def model_Shipping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Shipping__model_Shipping", None)
        self.__model_Shipping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document29"):
                opp_val = getattr(old_value, "model_Document29", None)
                if opp_val == self:
                    setattr(old_value, "model_Document29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document29"):
                opp_val = getattr(value, "model_Document29", None)
                setattr(value, "model_Document29", self)

    @property
    def model_Shipping61(self):
        return self.__model_Shipping61

    @model_Shipping61.setter
    def model_Shipping61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Shipping__model_Shipping61", None)
        self.__model_Shipping61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VAT62"):
                opp_val = getattr(old_value, "model_VAT62", None)
                if opp_val == self:
                    setattr(old_value, "model_VAT62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VAT62"):
                opp_val = getattr(value, "model_VAT62", None)
                setattr(value, "model_VAT62", self)

    @property
    def model_Shipping64(self):
        return self.__model_Shipping64

    @model_Shipping64.setter
    def model_Shipping64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Shipping__model_Shipping64", None)
        self.__model_Shipping64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ShippingCategory"):
                opp_val = getattr(old_value, "model_ShippingCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_ShippingCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ShippingCategory"):
                opp_val = getattr(value, "model_ShippingCategory", None)
                setattr(value, "model_ShippingCategory", self)

class model_Invoice(Document):

    pass
class Contact:

    pass
class model_Debitor(Contact):

    pass
class model_Creditor(Contact):

    pass
class AbstractCategory:

    pass
class model_TextCategory(AbstractCategory):

    pass
class model_VATCategory(AbstractCategory):

    pass
class model_ProductCategory(AbstractCategory):

    pass
class model_ContactCategory(AbstractCategory):

    pass
class model_ShippingCategory(AbstractCategory):

    pass
class model_ItemListTypeCategory(AbstractCategory):

    pass
class model_VoucherCategory(AbstractCategory):

    pass
class IEntity:

    pass
class model_ProductBlockPrice(IEntity):

    def __init__(self, block: str, price: str, model_ProductBlockPrice: "model_Product" = None):
        self.block = block
        self.price = price
        self.model_ProductBlockPrice = model_ProductBlockPrice
        
    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def model_ProductBlockPrice(self):
        return self.__model_ProductBlockPrice

    @model_ProductBlockPrice.setter
    def model_ProductBlockPrice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ProductBlockPrice__model_ProductBlockPrice", None)
        self.__model_ProductBlockPrice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Product59"):
                opp_val = getattr(old_value, "model_Product59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Product59"):
                opp_val = getattr(value, "model_Product59", None)
                if opp_val is None:
                    setattr(value, "model_Product59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_ItemAccountType(IEntity):

    def __init__(self, value: str, model_ItemAccountType47: "model_ItemListTypeCategory" = None, model_ItemAccountType: "model_VoucherItem" = None):
        self.value = value
        self.model_ItemAccountType47 = model_ItemAccountType47
        self.model_ItemAccountType = model_ItemAccountType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_ItemAccountType47(self):
        return self.__model_ItemAccountType47

    @model_ItemAccountType47.setter
    def model_ItemAccountType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ItemAccountType__model_ItemAccountType47", None)
        self.__model_ItemAccountType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ItemListTypeCategory"):
                opp_val = getattr(old_value, "model_ItemListTypeCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_ItemListTypeCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ItemListTypeCategory"):
                opp_val = getattr(value, "model_ItemListTypeCategory", None)
                setattr(value, "model_ItemListTypeCategory", self)

    @property
    def model_ItemAccountType(self):
        return self.__model_ItemAccountType

    @model_ItemAccountType.setter
    def model_ItemAccountType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ItemAccountType__model_ItemAccountType", None)
        self.__model_ItemAccountType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VoucherItem42"):
                opp_val = getattr(old_value, "model_VoucherItem42", None)
                if opp_val == self:
                    setattr(old_value, "model_VoucherItem42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VoucherItem42"):
                opp_val = getattr(value, "model_VoucherItem42", None)
                setattr(value, "model_VoucherItem42", self)

class model_BankAccount(IEntity):

    def __init__(self, accountHolder: str, bankCode: str, bankName: str, bic: str, iban: str, model_BankAccount: "model_Contact" = None):
        self.accountHolder = accountHolder
        self.bankCode = bankCode
        self.bankName = bankName
        self.bic = bic
        self.iban = iban
        self.model_BankAccount = model_BankAccount
        
    @property
    def iban(self) -> str:
        return self.__iban

    @iban.setter
    def iban(self, iban: str):
        self.__iban = iban

    @property
    def accountHolder(self) -> str:
        return self.__accountHolder

    @accountHolder.setter
    def accountHolder(self, accountHolder: str):
        self.__accountHolder = accountHolder

    @property
    def bankName(self) -> str:
        return self.__bankName

    @bankName.setter
    def bankName(self, bankName: str):
        self.__bankName = bankName

    @property
    def bankCode(self) -> str:
        return self.__bankCode

    @bankCode.setter
    def bankCode(self, bankCode: str):
        self.__bankCode = bankCode

    @property
    def bic(self) -> str:
        return self.__bic

    @bic.setter
    def bic(self, bic: str):
        self.__bic = bic

    @property
    def model_BankAccount(self):
        return self.__model_BankAccount

    @model_BankAccount.setter
    def model_BankAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BankAccount__model_BankAccount", None)
        self.__model_BankAccount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact11"):
                opp_val = getattr(old_value, "model_Contact11", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact11"):
                opp_val = getattr(value, "model_Contact11", None)
                setattr(value, "model_Contact11", self)

class model_VoucherItem(IEntity):

    def __init__(self, price: str, posNr: str, itemVoucherType: str, model_VoucherItem: "model_Voucher" = None, model_VoucherItem42: "model_ItemAccountType" = None, model_VoucherItem44: "model_VAT" = None):
        self.price = price
        self.posNr = posNr
        self.itemVoucherType = itemVoucherType
        self.model_VoucherItem = model_VoucherItem
        self.model_VoucherItem42 = model_VoucherItem42
        self.model_VoucherItem44 = model_VoucherItem44
        
    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def posNr(self) -> str:
        return self.__posNr

    @posNr.setter
    def posNr(self, posNr: str):
        self.__posNr = posNr

    @property
    def itemVoucherType(self) -> str:
        return self.__itemVoucherType

    @itemVoucherType.setter
    def itemVoucherType(self, itemVoucherType: str):
        self.__itemVoucherType = itemVoucherType

    @property
    def model_VoucherItem(self):
        return self.__model_VoucherItem

    @model_VoucherItem.setter
    def model_VoucherItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VoucherItem__model_VoucherItem", None)
        self.__model_VoucherItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Voucher40"):
                opp_val = getattr(old_value, "model_Voucher40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Voucher40"):
                opp_val = getattr(value, "model_Voucher40", None)
                if opp_val is None:
                    setattr(value, "model_Voucher40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_VoucherItem44(self):
        return self.__model_VoucherItem44

    @model_VoucherItem44.setter
    def model_VoucherItem44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VoucherItem__model_VoucherItem44", None)
        self.__model_VoucherItem44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VAT45"):
                opp_val = getattr(old_value, "model_VAT45", None)
                if opp_val == self:
                    setattr(old_value, "model_VAT45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VAT45"):
                opp_val = getattr(value, "model_VAT45", None)
                setattr(value, "model_VAT45", self)

    @property
    def model_VoucherItem42(self):
        return self.__model_VoucherItem42

    @model_VoucherItem42.setter
    def model_VoucherItem42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VoucherItem__model_VoucherItem42", None)
        self.__model_VoucherItem42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ItemAccountType"):
                opp_val = getattr(old_value, "model_ItemAccountType", None)
                if opp_val == self:
                    setattr(old_value, "model_ItemAccountType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ItemAccountType"):
                opp_val = getattr(value, "model_ItemAccountType", None)
                setattr(value, "model_ItemAccountType", self)

class model_CEFACTCode(IEntity):

    def __init__(self, abbreviation_de: str, abbreviation_en: str, code: str, target: str, name_de: str):
        self.abbreviation_de = abbreviation_de
        self.abbreviation_en = abbreviation_en
        self.code = code
        self.target = target
        self.name_de = name_de
        
    @property
    def abbreviation_en(self) -> str:
        return self.__abbreviation_en

    @abbreviation_en.setter
    def abbreviation_en(self, abbreviation_en: str):
        self.__abbreviation_en = abbreviation_en

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def abbreviation_de(self) -> str:
        return self.__abbreviation_de

    @abbreviation_de.setter
    def abbreviation_de(self, abbreviation_de: str):
        self.__abbreviation_de = abbreviation_de

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name_de(self) -> str:
        return self.__name_de

    @name_de.setter
    def name_de(self, name_de: str):
        self.__name_de = name_de

class model_User(IEntity):

    def __init__(self, password: str, userName: str, model_User: "model_Tenant" = None, model_User68: set["model_Role"] = None):
        self.password = password
        self.userName = userName
        self.model_User = model_User
        self.model_User68 = model_User68 if model_User68 is not None else set()
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def model_User68(self):
        return self.__model_User68

    @model_User68.setter
    def model_User68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User68", None)
        self.__model_User68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Role"):
                    opp_val = getattr(item, "model_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Role"):
                    opp_val = getattr(item, "model_Role", None)
                    
                    setattr(item, "model_Role", self)
                    

    @property
    def model_User(self):
        return self.__model_User

    @model_User.setter
    def model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User", None)
        self.__model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Tenant"):
                opp_val = getattr(old_value, "model_Tenant", None)
                if opp_val == self:
                    setattr(old_value, "model_Tenant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Tenant"):
                opp_val = getattr(value, "model_Tenant", None)
                setattr(value, "model_Tenant", self)

class model_Tenant(IEntity):

    pass
class model_Address(IEntity):

    def __init__(self, street: str, cityAddon: str, city: str, zip: str, countryCode: str, manualAddress: str, model_Address: "model_Contact" = None):
        self.street = street
        self.cityAddon = cityAddon
        self.city = city
        self.zip = zip
        self.countryCode = countryCode
        self.manualAddress = manualAddress
        self.model_Address = model_Address
        
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def manualAddress(self) -> str:
        return self.__manualAddress

    @manualAddress.setter
    def manualAddress(self, manualAddress: str):
        self.__manualAddress = manualAddress

    @property
    def cityAddon(self) -> str:
        return self.__cityAddon

    @cityAddon.setter
    def cityAddon(self, cityAddon: str):
        self.__cityAddon = cityAddon

    @property
    def countryCode(self) -> str:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode

    @property
    def model_Address(self):
        return self.__model_Address

    @model_Address.setter
    def model_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Address__model_Address", None)
        self.__model_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact"):
                opp_val = getattr(old_value, "model_Contact", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact"):
                opp_val = getattr(value, "model_Contact", None)
                setattr(value, "model_Contact", self)

class model_TextModule(IEntity):

    def __init__(self, text: str, model_TextModule: "model_TextCategory" = None):
        self.text = text
        self.model_TextModule = model_TextModule
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def model_TextModule(self):
        return self.__model_TextModule

    @model_TextModule.setter
    def model_TextModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TextModule__model_TextModule", None)
        self.__model_TextModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TextCategory"):
                opp_val = getattr(old_value, "model_TextCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_TextCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TextCategory"):
                opp_val = getattr(value, "model_TextCategory", None)
                setattr(value, "model_TextCategory", self)

class model_DocumentItem(IEntity):

    def __init__(self, gtin: str, noVat: str, itemRebate: str, itemNumber: str, quantity: str, originQuantity: str, weight: str, tara: str, description: str, optional: str, picture: str, price: str, quantityUnit: str, posNr: str, itemType: str, vestingPeriodStart: date, vestingPeriodEnd: date, model_DocumentItem: "model_Document" = None, model_DocumentItem34: "model_Product" = None, model_DocumentItem36: "model_VAT" = None):
        self.gtin = gtin
        self.noVat = noVat
        self.itemRebate = itemRebate
        self.itemNumber = itemNumber
        self.quantity = quantity
        self.originQuantity = originQuantity
        self.weight = weight
        self.tara = tara
        self.description = description
        self.optional = optional
        self.picture = picture
        self.price = price
        self.quantityUnit = quantityUnit
        self.posNr = posNr
        self.itemType = itemType
        self.vestingPeriodStart = vestingPeriodStart
        self.vestingPeriodEnd = vestingPeriodEnd
        self.model_DocumentItem = model_DocumentItem
        self.model_DocumentItem34 = model_DocumentItem34
        self.model_DocumentItem36 = model_DocumentItem36
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def vestingPeriodStart(self) -> date:
        return self.__vestingPeriodStart

    @vestingPeriodStart.setter
    def vestingPeriodStart(self, vestingPeriodStart: date):
        self.__vestingPeriodStart = vestingPeriodStart

    @property
    def itemRebate(self) -> str:
        return self.__itemRebate

    @itemRebate.setter
    def itemRebate(self, itemRebate: str):
        self.__itemRebate = itemRebate

    @property
    def originQuantity(self) -> str:
        return self.__originQuantity

    @originQuantity.setter
    def originQuantity(self, originQuantity: str):
        self.__originQuantity = originQuantity

    @property
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def tara(self) -> str:
        return self.__tara

    @tara.setter
    def tara(self, tara: str):
        self.__tara = tara

    @property
    def itemType(self) -> str:
        return self.__itemType

    @itemType.setter
    def itemType(self, itemType: str):
        self.__itemType = itemType

    @property
    def noVat(self) -> str:
        return self.__noVat

    @noVat.setter
    def noVat(self, noVat: str):
        self.__noVat = noVat

    @property
    def quantityUnit(self) -> str:
        return self.__quantityUnit

    @quantityUnit.setter
    def quantityUnit(self, quantityUnit: str):
        self.__quantityUnit = quantityUnit

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def itemNumber(self) -> str:
        return self.__itemNumber

    @itemNumber.setter
    def itemNumber(self, itemNumber: str):
        self.__itemNumber = itemNumber

    @property
    def gtin(self) -> str:
        return self.__gtin

    @gtin.setter
    def gtin(self, gtin: str):
        self.__gtin = gtin

    @property
    def vestingPeriodEnd(self) -> date:
        return self.__vestingPeriodEnd

    @vestingPeriodEnd.setter
    def vestingPeriodEnd(self, vestingPeriodEnd: date):
        self.__vestingPeriodEnd = vestingPeriodEnd

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def posNr(self) -> str:
        return self.__posNr

    @posNr.setter
    def posNr(self, posNr: str):
        self.__posNr = posNr

    @property
    def model_DocumentItem34(self):
        return self.__model_DocumentItem34

    @model_DocumentItem34.setter
    def model_DocumentItem34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DocumentItem__model_DocumentItem34", None)
        self.__model_DocumentItem34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Product"):
                opp_val = getattr(old_value, "model_Product", None)
                if opp_val == self:
                    setattr(old_value, "model_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Product"):
                opp_val = getattr(value, "model_Product", None)
                setattr(value, "model_Product", self)

    @property
    def model_DocumentItem(self):
        return self.__model_DocumentItem

    @model_DocumentItem.setter
    def model_DocumentItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DocumentItem__model_DocumentItem", None)
        self.__model_DocumentItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document22"):
                opp_val = getattr(old_value, "model_Document22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document22"):
                opp_val = getattr(value, "model_Document22", None)
                if opp_val is None:
                    setattr(value, "model_Document22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DocumentItem36(self):
        return self.__model_DocumentItem36

    @model_DocumentItem36.setter
    def model_DocumentItem36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DocumentItem__model_DocumentItem36", None)
        self.__model_DocumentItem36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VAT37"):
                opp_val = getattr(old_value, "model_VAT37", None)
                if opp_val == self:
                    setattr(old_value, "model_VAT37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VAT37"):
                opp_val = getattr(value, "model_VAT37", None)
                setattr(value, "model_VAT37", self)

class model_Role(IEntity):

    pass
class model_AbstractCategory(IEntity):

    pass
class model_VAT(IEntity):

    def __init__(self, description: str, taxValue: str, salesEqualizationTax: str, model_VAT: "model_Document" = None, model_VAT37: "model_DocumentItem" = None, model_VAT45: "model_VoucherItem" = None, model_VAT57: "model_Product" = None, model_VAT62: "model_Shipping" = None, model_VAT70: "model_VATCategory" = None):
        self.description = description
        self.taxValue = taxValue
        self.salesEqualizationTax = salesEqualizationTax
        self.model_VAT = model_VAT
        self.model_VAT37 = model_VAT37
        self.model_VAT45 = model_VAT45
        self.model_VAT57 = model_VAT57
        self.model_VAT62 = model_VAT62
        self.model_VAT70 = model_VAT70
        
    @property
    def salesEqualizationTax(self) -> str:
        return self.__salesEqualizationTax

    @salesEqualizationTax.setter
    def salesEqualizationTax(self, salesEqualizationTax: str):
        self.__salesEqualizationTax = salesEqualizationTax

    @property
    def taxValue(self) -> str:
        return self.__taxValue

    @taxValue.setter
    def taxValue(self, taxValue: str):
        self.__taxValue = taxValue

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def model_VAT70(self):
        return self.__model_VAT70

    @model_VAT70.setter
    def model_VAT70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT70", None)
        self.__model_VAT70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VATCategory"):
                opp_val = getattr(old_value, "model_VATCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_VATCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VATCategory"):
                opp_val = getattr(value, "model_VATCategory", None)
                setattr(value, "model_VATCategory", self)

    @property
    def model_VAT37(self):
        return self.__model_VAT37

    @model_VAT37.setter
    def model_VAT37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT37", None)
        self.__model_VAT37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DocumentItem36"):
                opp_val = getattr(old_value, "model_DocumentItem36", None)
                if opp_val == self:
                    setattr(old_value, "model_DocumentItem36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DocumentItem36"):
                opp_val = getattr(value, "model_DocumentItem36", None)
                setattr(value, "model_DocumentItem36", self)

    @property
    def model_VAT45(self):
        return self.__model_VAT45

    @model_VAT45.setter
    def model_VAT45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT45", None)
        self.__model_VAT45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VoucherItem44"):
                opp_val = getattr(old_value, "model_VoucherItem44", None)
                if opp_val == self:
                    setattr(old_value, "model_VoucherItem44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VoucherItem44"):
                opp_val = getattr(value, "model_VoucherItem44", None)
                setattr(value, "model_VoucherItem44", self)

    @property
    def model_VAT(self):
        return self.__model_VAT

    @model_VAT.setter
    def model_VAT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT", None)
        self.__model_VAT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document24"):
                opp_val = getattr(old_value, "model_Document24", None)
                if opp_val == self:
                    setattr(old_value, "model_Document24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document24"):
                opp_val = getattr(value, "model_Document24", None)
                setattr(value, "model_Document24", self)

    @property
    def model_VAT57(self):
        return self.__model_VAT57

    @model_VAT57.setter
    def model_VAT57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT57", None)
        self.__model_VAT57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Product56"):
                opp_val = getattr(old_value, "model_Product56", None)
                if opp_val == self:
                    setattr(old_value, "model_Product56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Product56"):
                opp_val = getattr(value, "model_Product56", None)
                setattr(value, "model_Product56", self)

    @property
    def model_VAT62(self):
        return self.__model_VAT62

    @model_VAT62.setter
    def model_VAT62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VAT__model_VAT62", None)
        self.__model_VAT62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Shipping61"):
                opp_val = getattr(old_value, "model_Shipping61", None)
                if opp_val == self:
                    setattr(old_value, "model_Shipping61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Shipping61"):
                opp_val = getattr(value, "model_Shipping61", None)
                setattr(value, "model_Shipping61", self)

class model_IndividualDocumentInfo(IEntity):

    def __init__(self, shippingValue: str, paymentName: str, paymentText: str, paymentDescription: str, shippingName: str, shippingAutoVat: str, shippingDescription: str, shippingVatDescription: str, shippingVatValue: str, noVatName: str, noVatDescription: str, model_IndividualDocumentInfo: "model_Document" = None):
        self.shippingValue = shippingValue
        self.paymentName = paymentName
        self.paymentText = paymentText
        self.paymentDescription = paymentDescription
        self.shippingName = shippingName
        self.shippingAutoVat = shippingAutoVat
        self.shippingDescription = shippingDescription
        self.shippingVatDescription = shippingVatDescription
        self.shippingVatValue = shippingVatValue
        self.noVatName = noVatName
        self.noVatDescription = noVatDescription
        self.model_IndividualDocumentInfo = model_IndividualDocumentInfo
        
    @property
    def shippingAutoVat(self) -> str:
        return self.__shippingAutoVat

    @shippingAutoVat.setter
    def shippingAutoVat(self, shippingAutoVat: str):
        self.__shippingAutoVat = shippingAutoVat

    @property
    def paymentText(self) -> str:
        return self.__paymentText

    @paymentText.setter
    def paymentText(self, paymentText: str):
        self.__paymentText = paymentText

    @property
    def noVatName(self) -> str:
        return self.__noVatName

    @noVatName.setter
    def noVatName(self, noVatName: str):
        self.__noVatName = noVatName

    @property
    def shippingValue(self) -> str:
        return self.__shippingValue

    @shippingValue.setter
    def shippingValue(self, shippingValue: str):
        self.__shippingValue = shippingValue

    @property
    def paymentDescription(self) -> str:
        return self.__paymentDescription

    @paymentDescription.setter
    def paymentDescription(self, paymentDescription: str):
        self.__paymentDescription = paymentDescription

    @property
    def shippingVatValue(self) -> str:
        return self.__shippingVatValue

    @shippingVatValue.setter
    def shippingVatValue(self, shippingVatValue: str):
        self.__shippingVatValue = shippingVatValue

    @property
    def shippingName(self) -> str:
        return self.__shippingName

    @shippingName.setter
    def shippingName(self, shippingName: str):
        self.__shippingName = shippingName

    @property
    def shippingDescription(self) -> str:
        return self.__shippingDescription

    @shippingDescription.setter
    def shippingDescription(self, shippingDescription: str):
        self.__shippingDescription = shippingDescription

    @property
    def noVatDescription(self) -> str:
        return self.__noVatDescription

    @noVatDescription.setter
    def noVatDescription(self, noVatDescription: str):
        self.__noVatDescription = noVatDescription

    @property
    def paymentName(self) -> str:
        return self.__paymentName

    @paymentName.setter
    def paymentName(self, paymentName: str):
        self.__paymentName = paymentName

    @property
    def shippingVatDescription(self) -> str:
        return self.__shippingVatDescription

    @shippingVatDescription.setter
    def shippingVatDescription(self, shippingVatDescription: str):
        self.__shippingVatDescription = shippingVatDescription

    @property
    def model_IndividualDocumentInfo(self):
        return self.__model_IndividualDocumentInfo

    @model_IndividualDocumentInfo.setter
    def model_IndividualDocumentInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IndividualDocumentInfo__model_IndividualDocumentInfo", None)
        self.__model_IndividualDocumentInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document"):
                opp_val = getattr(old_value, "model_Document", None)
                if opp_val == self:
                    setattr(old_value, "model_Document", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document"):
                opp_val = getattr(value, "model_Document", None)
                setattr(value, "model_Document", self)

class model_WebshopStateMapping(IEntity):

    def __init__(self, webshopState: str, fakturamaOrderState: str, model_WebshopStateMapping: "model_WebShop" = None):
        self.webshopState = webshopState
        self.fakturamaOrderState = fakturamaOrderState
        self.model_WebshopStateMapping = model_WebshopStateMapping
        
    @property
    def webshopState(self) -> str:
        return self.__webshopState

    @webshopState.setter
    def webshopState(self, webshopState: str):
        self.__webshopState = webshopState

    @property
    def fakturamaOrderState(self) -> str:
        return self.__fakturamaOrderState

    @fakturamaOrderState.setter
    def fakturamaOrderState(self, fakturamaOrderState: str):
        self.__fakturamaOrderState = fakturamaOrderState

    @property
    def model_WebshopStateMapping(self):
        return self.__model_WebshopStateMapping

    @model_WebshopStateMapping.setter
    def model_WebshopStateMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WebshopStateMapping__model_WebshopStateMapping", None)
        self.__model_WebshopStateMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_WebShop"):
                opp_val = getattr(old_value, "model_WebShop", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_WebShop"):
                opp_val = getattr(value, "model_WebShop", None)
                if opp_val is None:
                    setattr(value, "model_WebShop", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_WebShop(IEntity):

    def __init__(self, webshopVendor: str, webshopVersion: str, model_WebShop: set["model_WebshopStateMapping"] = None):
        self.webshopVendor = webshopVendor
        self.webshopVersion = webshopVersion
        self.model_WebShop = model_WebShop if model_WebShop is not None else set()
        
    @property
    def webshopVersion(self) -> str:
        return self.__webshopVersion

    @webshopVersion.setter
    def webshopVersion(self, webshopVersion: str):
        self.__webshopVersion = webshopVersion

    @property
    def webshopVendor(self) -> str:
        return self.__webshopVendor

    @webshopVendor.setter
    def webshopVendor(self, webshopVendor: str):
        self.__webshopVendor = webshopVendor

    @property
    def model_WebShop(self):
        return self.__model_WebShop

    @model_WebShop.setter
    def model_WebShop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WebShop__model_WebShop", None)
        self.__model_WebShop = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_WebshopStateMapping"):
                    opp_val = getattr(item, "model_WebshopStateMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "model_WebshopStateMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_WebshopStateMapping"):
                    opp_val = getattr(item, "model_WebshopStateMapping", None)
                    
                    setattr(item, "model_WebshopStateMapping", self)
                    

class model_UserProperty(IEntity):

    def __init__(self, value: str, user: str, default: str, global: str):
        self.value = value
        self.user = user
        self.default = default
        self.global = global
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

class model_Voucher(IEntity):

    def __init__(self, voucherDate: date, discounted: str, doNotBook: str, documentNumber: str, voucherNumber: str, paidValue: str, totalValue: str, voucherType: str, model_Voucher: "model_VoucherCategory" = None, model_Voucher40: set["model_VoucherItem"] = None):
        self.voucherDate = voucherDate
        self.discounted = discounted
        self.doNotBook = doNotBook
        self.documentNumber = documentNumber
        self.voucherNumber = voucherNumber
        self.paidValue = paidValue
        self.totalValue = totalValue
        self.voucherType = voucherType
        self.model_Voucher = model_Voucher
        self.model_Voucher40 = model_Voucher40 if model_Voucher40 is not None else set()
        
    @property
    def totalValue(self) -> str:
        return self.__totalValue

    @totalValue.setter
    def totalValue(self, totalValue: str):
        self.__totalValue = totalValue

    @property
    def discounted(self) -> str:
        return self.__discounted

    @discounted.setter
    def discounted(self, discounted: str):
        self.__discounted = discounted

    @property
    def voucherDate(self) -> date:
        return self.__voucherDate

    @voucherDate.setter
    def voucherDate(self, voucherDate: date):
        self.__voucherDate = voucherDate

    @property
    def voucherNumber(self) -> str:
        return self.__voucherNumber

    @voucherNumber.setter
    def voucherNumber(self, voucherNumber: str):
        self.__voucherNumber = voucherNumber

    @property
    def paidValue(self) -> str:
        return self.__paidValue

    @paidValue.setter
    def paidValue(self, paidValue: str):
        self.__paidValue = paidValue

    @property
    def documentNumber(self) -> str:
        return self.__documentNumber

    @documentNumber.setter
    def documentNumber(self, documentNumber: str):
        self.__documentNumber = documentNumber

    @property
    def doNotBook(self) -> str:
        return self.__doNotBook

    @doNotBook.setter
    def doNotBook(self, doNotBook: str):
        self.__doNotBook = doNotBook

    @property
    def voucherType(self) -> str:
        return self.__voucherType

    @voucherType.setter
    def voucherType(self, voucherType: str):
        self.__voucherType = voucherType

    @property
    def model_Voucher40(self):
        return self.__model_Voucher40

    @model_Voucher40.setter
    def model_Voucher40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Voucher__model_Voucher40", None)
        self.__model_Voucher40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_VoucherItem"):
                    opp_val = getattr(item, "model_VoucherItem", None)
                    
                    if opp_val == self:
                        setattr(item, "model_VoucherItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_VoucherItem"):
                    opp_val = getattr(item, "model_VoucherItem", None)
                    
                    setattr(item, "model_VoucherItem", self)
                    

    @property
    def model_Voucher(self):
        return self.__model_Voucher

    @model_Voucher.setter
    def model_Voucher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Voucher__model_Voucher", None)
        self.__model_Voucher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VoucherCategory"):
                opp_val = getattr(old_value, "model_VoucherCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_VoucherCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VoucherCategory"):
                opp_val = getattr(value, "model_VoucherCategory", None)
                setattr(value, "model_VoucherCategory", self)

class model_Contact(IEntity):

    def __init__(self, mandateReference: str, customerNumber: str, title: str, firstName: str, gender: str, company: str, birthday: date, email: str, mobile: str, phone: str, fax: str, discount: str, note: str, reliability: str, useNetGross: str, vatNumber: str, vatNumberValid: str, website: str, webshopName: str, supplierNumber: str, gln: str, contactType: str, useSalesEqualizationTax: str, model_Contact: "model_Address" = None, model_Contact5: "model_Contact" = None, model_Contact3: "model_Contact" = None, model_Contact7: "model_ContactCategory" = None, model_Contact9: "model_Payment" = None, model_Contact11: "model_BankAccount" = None, model_Contact15: "model_Document" = None, model_Contact18: "model_Document" = None):
        self.mandateReference = mandateReference
        self.customerNumber = customerNumber
        self.title = title
        self.firstName = firstName
        self.gender = gender
        self.company = company
        self.birthday = birthday
        self.email = email
        self.mobile = mobile
        self.phone = phone
        self.fax = fax
        self.discount = discount
        self.note = note
        self.reliability = reliability
        self.useNetGross = useNetGross
        self.vatNumber = vatNumber
        self.vatNumberValid = vatNumberValid
        self.website = website
        self.webshopName = webshopName
        self.supplierNumber = supplierNumber
        self.gln = gln
        self.contactType = contactType
        self.useSalesEqualizationTax = useSalesEqualizationTax
        self.model_Contact = model_Contact
        self.model_Contact5 = model_Contact5
        self.model_Contact3 = model_Contact3
        self.model_Contact7 = model_Contact7
        self.model_Contact9 = model_Contact9
        self.model_Contact11 = model_Contact11
        self.model_Contact15 = model_Contact15
        self.model_Contact18 = model_Contact18
        
    @property
    def contactType(self) -> str:
        return self.__contactType

    @contactType.setter
    def contactType(self, contactType: str):
        self.__contactType = contactType

    @property
    def supplierNumber(self) -> str:
        return self.__supplierNumber

    @supplierNumber.setter
    def supplierNumber(self, supplierNumber: str):
        self.__supplierNumber = supplierNumber

    @property
    def reliability(self) -> str:
        return self.__reliability

    @reliability.setter
    def reliability(self, reliability: str):
        self.__reliability = reliability

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def discount(self) -> str:
        return self.__discount

    @discount.setter
    def discount(self, discount: str):
        self.__discount = discount

    @property
    def webshopName(self) -> str:
        return self.__webshopName

    @webshopName.setter
    def webshopName(self, webshopName: str):
        self.__webshopName = webshopName

    @property
    def useNetGross(self) -> str:
        return self.__useNetGross

    @useNetGross.setter
    def useNetGross(self, useNetGross: str):
        self.__useNetGross = useNetGross

    @property
    def mandateReference(self) -> str:
        return self.__mandateReference

    @mandateReference.setter
    def mandateReference(self, mandateReference: str):
        self.__mandateReference = mandateReference

    @property
    def gln(self) -> str:
        return self.__gln

    @gln.setter
    def gln(self, gln: str):
        self.__gln = gln

    @property
    def birthday(self) -> date:
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: date):
        self.__birthday = birthday

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def vatNumber(self) -> str:
        return self.__vatNumber

    @vatNumber.setter
    def vatNumber(self, vatNumber: str):
        self.__vatNumber = vatNumber

    @property
    def customerNumber(self) -> str:
        return self.__customerNumber

    @customerNumber.setter
    def customerNumber(self, customerNumber: str):
        self.__customerNumber = customerNumber

    @property
    def mobile(self) -> str:
        return self.__mobile

    @mobile.setter
    def mobile(self, mobile: str):
        self.__mobile = mobile

    @property
    def useSalesEqualizationTax(self) -> str:
        return self.__useSalesEqualizationTax

    @useSalesEqualizationTax.setter
    def useSalesEqualizationTax(self, useSalesEqualizationTax: str):
        self.__useSalesEqualizationTax = useSalesEqualizationTax

    @property
    def company(self) -> str:
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def vatNumberValid(self) -> str:
        return self.__vatNumberValid

    @vatNumberValid.setter
    def vatNumberValid(self, vatNumberValid: str):
        self.__vatNumberValid = vatNumberValid

    @property
    def fax(self) -> str:
        return self.__fax

    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def model_Contact18(self):
        return self.__model_Contact18

    @model_Contact18.setter
    def model_Contact18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact18", None)
        self.__model_Contact18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document17"):
                opp_val = getattr(old_value, "model_Document17", None)
                if opp_val == self:
                    setattr(old_value, "model_Document17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document17"):
                opp_val = getattr(value, "model_Document17", None)
                setattr(value, "model_Document17", self)

    @property
    def model_Contact(self):
        return self.__model_Contact

    @model_Contact.setter
    def model_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact", None)
        self.__model_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Address"):
                opp_val = getattr(old_value, "model_Address", None)
                if opp_val == self:
                    setattr(old_value, "model_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Address"):
                opp_val = getattr(value, "model_Address", None)
                setattr(value, "model_Address", self)

    @property
    def model_Contact9(self):
        return self.__model_Contact9

    @model_Contact9.setter
    def model_Contact9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact9", None)
        self.__model_Contact9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Payment"):
                opp_val = getattr(old_value, "model_Payment", None)
                if opp_val == self:
                    setattr(old_value, "model_Payment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Payment"):
                opp_val = getattr(value, "model_Payment", None)
                setattr(value, "model_Payment", self)

    @property
    def model_Contact3(self):
        return self.__model_Contact3

    @model_Contact3.setter
    def model_Contact3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact3", None)
        self.__model_Contact3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact5"):
                opp_val = getattr(old_value, "model_Contact5", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact5"):
                opp_val = getattr(value, "model_Contact5", None)
                setattr(value, "model_Contact5", self)

    @property
    def model_Contact15(self):
        return self.__model_Contact15

    @model_Contact15.setter
    def model_Contact15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact15", None)
        self.__model_Contact15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document14"):
                opp_val = getattr(old_value, "model_Document14", None)
                if opp_val == self:
                    setattr(old_value, "model_Document14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document14"):
                opp_val = getattr(value, "model_Document14", None)
                setattr(value, "model_Document14", self)

    @property
    def model_Contact5(self):
        return self.__model_Contact5

    @model_Contact5.setter
    def model_Contact5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact5", None)
        self.__model_Contact5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact3"):
                opp_val = getattr(old_value, "model_Contact3", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact3"):
                opp_val = getattr(value, "model_Contact3", None)
                setattr(value, "model_Contact3", self)

    @property
    def model_Contact11(self):
        return self.__model_Contact11

    @model_Contact11.setter
    def model_Contact11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact11", None)
        self.__model_Contact11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BankAccount"):
                opp_val = getattr(old_value, "model_BankAccount", None)
                if opp_val == self:
                    setattr(old_value, "model_BankAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BankAccount"):
                opp_val = getattr(value, "model_BankAccount", None)
                setattr(value, "model_BankAccount", self)

    @property
    def model_Contact7(self):
        return self.__model_Contact7

    @model_Contact7.setter
    def model_Contact7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Contact__model_Contact7", None)
        self.__model_Contact7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ContactCategory"):
                opp_val = getattr(old_value, "model_ContactCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_ContactCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ContactCategory"):
                opp_val = getattr(value, "model_ContactCategory", None)
                setattr(value, "model_ContactCategory", self)

class model_Payment(IEntity):

    def __init__(self, description: str, discountDays: str, discountValue: str, netDays: str, paidText: str, unpaidText: str, depositText: str, code: str, model_Payment: "model_Contact" = None, model_Payment27: "model_Document" = None, model_Payment49: "model_VoucherCategory" = None):
        self.description = description
        self.discountDays = discountDays
        self.discountValue = discountValue
        self.netDays = netDays
        self.paidText = paidText
        self.unpaidText = unpaidText
        self.depositText = depositText
        self.code = code
        self.model_Payment = model_Payment
        self.model_Payment27 = model_Payment27
        self.model_Payment49 = model_Payment49
        
    @property
    def unpaidText(self) -> str:
        return self.__unpaidText

    @unpaidText.setter
    def unpaidText(self, unpaidText: str):
        self.__unpaidText = unpaidText

    @property
    def depositText(self) -> str:
        return self.__depositText

    @depositText.setter
    def depositText(self, depositText: str):
        self.__depositText = depositText

    @property
    def paidText(self) -> str:
        return self.__paidText

    @paidText.setter
    def paidText(self, paidText: str):
        self.__paidText = paidText

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def netDays(self) -> str:
        return self.__netDays

    @netDays.setter
    def netDays(self, netDays: str):
        self.__netDays = netDays

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def discountDays(self) -> str:
        return self.__discountDays

    @discountDays.setter
    def discountDays(self, discountDays: str):
        self.__discountDays = discountDays

    @property
    def discountValue(self) -> str:
        return self.__discountValue

    @discountValue.setter
    def discountValue(self, discountValue: str):
        self.__discountValue = discountValue

    @property
    def model_Payment(self):
        return self.__model_Payment

    @model_Payment.setter
    def model_Payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Payment__model_Payment", None)
        self.__model_Payment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact9"):
                opp_val = getattr(old_value, "model_Contact9", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact9"):
                opp_val = getattr(value, "model_Contact9", None)
                setattr(value, "model_Contact9", self)

    @property
    def model_Payment49(self):
        return self.__model_Payment49

    @model_Payment49.setter
    def model_Payment49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Payment__model_Payment49", None)
        self.__model_Payment49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VoucherCategory50"):
                opp_val = getattr(old_value, "model_VoucherCategory50", None)
                if opp_val == self:
                    setattr(old_value, "model_VoucherCategory50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VoucherCategory50"):
                opp_val = getattr(value, "model_VoucherCategory50", None)
                setattr(value, "model_VoucherCategory50", self)

    @property
    def model_Payment27(self):
        return self.__model_Payment27

    @model_Payment27.setter
    def model_Payment27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Payment__model_Payment27", None)
        self.__model_Payment27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document26"):
                opp_val = getattr(old_value, "model_Document26", None)
                if opp_val == self:
                    setattr(old_value, "model_Document26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document26"):
                opp_val = getattr(value, "model_Document26", None)
                setattr(value, "model_Document26", self)

class model_Document(IEntity):

    def __init__(self, odtPath: str, addressFirstLine: str, billingType: str, consultant: str, customerRef: str, deposit: str, documentDate: date, dueDays: str, itemsRebate: str, message: str, message2: str, message3: str, netGross: str, orderDate: date, paidValue: str, paid: str, payDate: date, pdfPath: str, printed: str, printTemplate: str, progress: str, serviceDate: date, shippingAutoVat: str, shippingValue: str, totalValue: str, transactionId: str, webshopDate: date, webshopId: str, vestingPeriodStart: date, vestingPeriodEnd: date, model_Document: "model_IndividualDocumentInfo" = None, model_Document14: "model_Contact" = None, model_Document17: "model_Contact" = None, model_Document20: "model_Invoice" = None, model_Document22: set["model_DocumentItem"] = None, model_Document24: "model_VAT" = None, model_Document26: "model_Payment" = None, model_Document29: "model_Shipping" = None, model_Document32: "model_Document" = None, model_Document30: "model_Document" = None):
        self.odtPath = odtPath
        self.addressFirstLine = addressFirstLine
        self.billingType = billingType
        self.consultant = consultant
        self.customerRef = customerRef
        self.deposit = deposit
        self.documentDate = documentDate
        self.dueDays = dueDays
        self.itemsRebate = itemsRebate
        self.message = message
        self.message2 = message2
        self.message3 = message3
        self.netGross = netGross
        self.orderDate = orderDate
        self.paidValue = paidValue
        self.paid = paid
        self.payDate = payDate
        self.pdfPath = pdfPath
        self.printed = printed
        self.printTemplate = printTemplate
        self.progress = progress
        self.serviceDate = serviceDate
        self.shippingAutoVat = shippingAutoVat
        self.shippingValue = shippingValue
        self.totalValue = totalValue
        self.transactionId = transactionId
        self.webshopDate = webshopDate
        self.webshopId = webshopId
        self.vestingPeriodStart = vestingPeriodStart
        self.vestingPeriodEnd = vestingPeriodEnd
        self.model_Document = model_Document
        self.model_Document14 = model_Document14
        self.model_Document17 = model_Document17
        self.model_Document20 = model_Document20
        self.model_Document22 = model_Document22 if model_Document22 is not None else set()
        self.model_Document24 = model_Document24
        self.model_Document26 = model_Document26
        self.model_Document29 = model_Document29
        self.model_Document32 = model_Document32
        self.model_Document30 = model_Document30
        
    @property
    def addressFirstLine(self) -> str:
        return self.__addressFirstLine

    @addressFirstLine.setter
    def addressFirstLine(self, addressFirstLine: str):
        self.__addressFirstLine = addressFirstLine

    @property
    def message2(self) -> str:
        return self.__message2

    @message2.setter
    def message2(self, message2: str):
        self.__message2 = message2

    @property
    def dueDays(self) -> str:
        return self.__dueDays

    @dueDays.setter
    def dueDays(self, dueDays: str):
        self.__dueDays = dueDays

    @property
    def totalValue(self) -> str:
        return self.__totalValue

    @totalValue.setter
    def totalValue(self, totalValue: str):
        self.__totalValue = totalValue

    @property
    def deposit(self) -> str:
        return self.__deposit

    @deposit.setter
    def deposit(self, deposit: str):
        self.__deposit = deposit

    @property
    def printed(self) -> str:
        return self.__printed

    @printed.setter
    def printed(self, printed: str):
        self.__printed = printed

    @property
    def serviceDate(self) -> date:
        return self.__serviceDate

    @serviceDate.setter
    def serviceDate(self, serviceDate: date):
        self.__serviceDate = serviceDate

    @property
    def paid(self) -> str:
        return self.__paid

    @paid.setter
    def paid(self, paid: str):
        self.__paid = paid

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def printTemplate(self) -> str:
        return self.__printTemplate

    @printTemplate.setter
    def printTemplate(self, printTemplate: str):
        self.__printTemplate = printTemplate

    @property
    def documentDate(self) -> date:
        return self.__documentDate

    @documentDate.setter
    def documentDate(self, documentDate: date):
        self.__documentDate = documentDate

    @property
    def shippingAutoVat(self) -> str:
        return self.__shippingAutoVat

    @shippingAutoVat.setter
    def shippingAutoVat(self, shippingAutoVat: str):
        self.__shippingAutoVat = shippingAutoVat

    @property
    def customerRef(self) -> str:
        return self.__customerRef

    @customerRef.setter
    def customerRef(self, customerRef: str):
        self.__customerRef = customerRef

    @property
    def pdfPath(self) -> str:
        return self.__pdfPath

    @pdfPath.setter
    def pdfPath(self, pdfPath: str):
        self.__pdfPath = pdfPath

    @property
    def orderDate(self) -> date:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: date):
        self.__orderDate = orderDate

    @property
    def odtPath(self) -> str:
        return self.__odtPath

    @odtPath.setter
    def odtPath(self, odtPath: str):
        self.__odtPath = odtPath

    @property
    def billingType(self) -> str:
        return self.__billingType

    @billingType.setter
    def billingType(self, billingType: str):
        self.__billingType = billingType

    @property
    def transactionId(self) -> str:
        return self.__transactionId

    @transactionId.setter
    def transactionId(self, transactionId: str):
        self.__transactionId = transactionId

    @property
    def payDate(self) -> date:
        return self.__payDate

    @payDate.setter
    def payDate(self, payDate: date):
        self.__payDate = payDate

    @property
    def itemsRebate(self) -> str:
        return self.__itemsRebate

    @itemsRebate.setter
    def itemsRebate(self, itemsRebate: str):
        self.__itemsRebate = itemsRebate

    @property
    def paidValue(self) -> str:
        return self.__paidValue

    @paidValue.setter
    def paidValue(self, paidValue: str):
        self.__paidValue = paidValue

    @property
    def netGross(self) -> str:
        return self.__netGross

    @netGross.setter
    def netGross(self, netGross: str):
        self.__netGross = netGross

    @property
    def vestingPeriodEnd(self) -> date:
        return self.__vestingPeriodEnd

    @vestingPeriodEnd.setter
    def vestingPeriodEnd(self, vestingPeriodEnd: date):
        self.__vestingPeriodEnd = vestingPeriodEnd

    @property
    def message3(self) -> str:
        return self.__message3

    @message3.setter
    def message3(self, message3: str):
        self.__message3 = message3

    @property
    def vestingPeriodStart(self) -> date:
        return self.__vestingPeriodStart

    @vestingPeriodStart.setter
    def vestingPeriodStart(self, vestingPeriodStart: date):
        self.__vestingPeriodStart = vestingPeriodStart

    @property
    def progress(self) -> str:
        return self.__progress

    @progress.setter
    def progress(self, progress: str):
        self.__progress = progress

    @property
    def webshopId(self) -> str:
        return self.__webshopId

    @webshopId.setter
    def webshopId(self, webshopId: str):
        self.__webshopId = webshopId

    @property
    def shippingValue(self) -> str:
        return self.__shippingValue

    @shippingValue.setter
    def shippingValue(self, shippingValue: str):
        self.__shippingValue = shippingValue

    @property
    def webshopDate(self) -> date:
        return self.__webshopDate

    @webshopDate.setter
    def webshopDate(self, webshopDate: date):
        self.__webshopDate = webshopDate

    @property
    def consultant(self) -> str:
        return self.__consultant

    @consultant.setter
    def consultant(self, consultant: str):
        self.__consultant = consultant

    @property
    def model_Document30(self):
        return self.__model_Document30

    @model_Document30.setter
    def model_Document30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document30", None)
        self.__model_Document30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document32"):
                opp_val = getattr(old_value, "model_Document32", None)
                if opp_val == self:
                    setattr(old_value, "model_Document32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document32"):
                opp_val = getattr(value, "model_Document32", None)
                setattr(value, "model_Document32", self)

    @property
    def model_Document(self):
        return self.__model_Document

    @model_Document.setter
    def model_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document", None)
        self.__model_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IndividualDocumentInfo"):
                opp_val = getattr(old_value, "model_IndividualDocumentInfo", None)
                if opp_val == self:
                    setattr(old_value, "model_IndividualDocumentInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IndividualDocumentInfo"):
                opp_val = getattr(value, "model_IndividualDocumentInfo", None)
                setattr(value, "model_IndividualDocumentInfo", self)

    @property
    def model_Document22(self):
        return self.__model_Document22

    @model_Document22.setter
    def model_Document22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document22", None)
        self.__model_Document22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DocumentItem"):
                    opp_val = getattr(item, "model_DocumentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DocumentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DocumentItem"):
                    opp_val = getattr(item, "model_DocumentItem", None)
                    
                    setattr(item, "model_DocumentItem", self)
                    

    @property
    def model_Document29(self):
        return self.__model_Document29

    @model_Document29.setter
    def model_Document29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document29", None)
        self.__model_Document29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Shipping"):
                opp_val = getattr(old_value, "model_Shipping", None)
                if opp_val == self:
                    setattr(old_value, "model_Shipping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Shipping"):
                opp_val = getattr(value, "model_Shipping", None)
                setattr(value, "model_Shipping", self)

    @property
    def model_Document20(self):
        return self.__model_Document20

    @model_Document20.setter
    def model_Document20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document20", None)
        self.__model_Document20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Invoice"):
                opp_val = getattr(old_value, "model_Invoice", None)
                if opp_val == self:
                    setattr(old_value, "model_Invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Invoice"):
                opp_val = getattr(value, "model_Invoice", None)
                setattr(value, "model_Invoice", self)

    @property
    def model_Document14(self):
        return self.__model_Document14

    @model_Document14.setter
    def model_Document14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document14", None)
        self.__model_Document14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact15"):
                opp_val = getattr(old_value, "model_Contact15", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact15"):
                opp_val = getattr(value, "model_Contact15", None)
                setattr(value, "model_Contact15", self)

    @property
    def model_Document26(self):
        return self.__model_Document26

    @model_Document26.setter
    def model_Document26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document26", None)
        self.__model_Document26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Payment27"):
                opp_val = getattr(old_value, "model_Payment27", None)
                if opp_val == self:
                    setattr(old_value, "model_Payment27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Payment27"):
                opp_val = getattr(value, "model_Payment27", None)
                setattr(value, "model_Payment27", self)

    @property
    def model_Document17(self):
        return self.__model_Document17

    @model_Document17.setter
    def model_Document17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document17", None)
        self.__model_Document17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Contact18"):
                opp_val = getattr(old_value, "model_Contact18", None)
                if opp_val == self:
                    setattr(old_value, "model_Contact18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Contact18"):
                opp_val = getattr(value, "model_Contact18", None)
                setattr(value, "model_Contact18", self)

    @property
    def model_Document32(self):
        return self.__model_Document32

    @model_Document32.setter
    def model_Document32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document32", None)
        self.__model_Document32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Document30"):
                opp_val = getattr(old_value, "model_Document30", None)
                if opp_val == self:
                    setattr(old_value, "model_Document30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Document30"):
                opp_val = getattr(value, "model_Document30", None)
                setattr(value, "model_Document30", self)

    @property
    def model_Document24(self):
        return self.__model_Document24

    @model_Document24.setter
    def model_Document24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Document__model_Document24", None)
        self.__model_Document24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VAT"):
                opp_val = getattr(old_value, "model_VAT", None)
                if opp_val == self:
                    setattr(old_value, "model_VAT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VAT"):
                opp_val = getattr(value, "model_VAT", None)
                setattr(value, "model_VAT", self)

class model_ProductOptions(IEntity):

    def __init__(self, attributeValue: str, sequenceNumber: str, model_ProductOptions: "model_Product" = None):
        self.attributeValue = attributeValue
        self.sequenceNumber = sequenceNumber
        self.model_ProductOptions = model_ProductOptions
        
    @property
    def attributeValue(self) -> str:
        return self.__attributeValue

    @attributeValue.setter
    def attributeValue(self, attributeValue: str):
        self.__attributeValue = attributeValue

    @property
    def sequenceNumber(self) -> str:
        return self.__sequenceNumber

    @sequenceNumber.setter
    def sequenceNumber(self, sequenceNumber: str):
        self.__sequenceNumber = sequenceNumber

    @property
    def model_ProductOptions(self):
        return self.__model_ProductOptions

    @model_ProductOptions.setter
    def model_ProductOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ProductOptions__model_ProductOptions", None)
        self.__model_ProductOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Product54"):
                opp_val = getattr(old_value, "model_Product54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Product54"):
                opp_val = getattr(value, "model_Product54", None)
                if opp_val is None:
                    setattr(value, "model_Product54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_IDescribableEntity(IEntity):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class model_IEntity(ABC):

    def __init__(self, name: str, dateAdded: date, modifiedBy: str, modified: date, id: str, deleted: str, validFrom: date, validTo: date):
        self.name = name
        self.dateAdded = dateAdded
        self.modifiedBy = modifiedBy
        self.modified = modified
        self.id = id
        self.deleted = deleted
        self.validFrom = validFrom
        self.validTo = validTo
        
    @property
    def validTo(self) -> date:
        return self.__validTo

    @validTo.setter
    def validTo(self, validTo: date):
        self.__validTo = validTo

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def deleted(self) -> str:
        return self.__deleted

    @deleted.setter
    def deleted(self, deleted: str):
        self.__deleted = deleted

    @property
    def validFrom(self) -> date:
        return self.__validFrom

    @validFrom.setter
    def validFrom(self, validFrom: date):
        self.__validFrom = validFrom

    @property
    def modified(self) -> date:
        return self.__modified

    @modified.setter
    def modified(self, modified: date):
        self.__modified = modified

    @property
    def dateAdded(self) -> date:
        return self.__dateAdded

    @dateAdded.setter
    def dateAdded(self, dateAdded: date):
        self.__dateAdded = dateAdded

    @property
    def modifiedBy(self) -> str:
        return self.__modifiedBy

    @modifiedBy.setter
    def modifiedBy(self, modifiedBy: str):
        self.__modifiedBy = modifiedBy

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    def isSameAs(self) -> str:
        # TODO: Implement isSameAs method
        pass

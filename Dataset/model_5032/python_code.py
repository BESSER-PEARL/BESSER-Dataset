from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CanadaProvinces(Enum):
    NB = "NB"
    NL = "NL"
    NT = "NT"
    UNKNOWN = "UNKNOWN"
    AB = "AB"
    BC = "BC"
    MB = "MB"
class USStates(Enum):
    UNKNOWN = "UNKNOWN"
    AL = "AL"
    AK = "AK"
    AS = "AS"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"


############################################
# Definition of Classes
############################################

class customers_CustomersDB:

    def __init__(self, comment: str, customers_CustomersDB: set["customers_Customer"] = None):
        self.comment = comment
        self.customers_CustomersDB = customers_CustomersDB if customers_CustomersDB is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def customers_CustomersDB(self):
        return self.__customers_CustomersDB

    @customers_CustomersDB.setter
    def customers_CustomersDB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_CustomersDB__customers_CustomersDB", None)
        self.__customers_CustomersDB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customers_Customer4"):
                    opp_val = getattr(item, "customers_Customer4", None)
                    
                    if opp_val == self:
                        setattr(item, "customers_Customer4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customers_Customer4"):
                    opp_val = getattr(item, "customers_Customer4", None)
                    
                    setattr(item, "customers_Customer4", self)
                    

class Address:

    pass
class customers_CanadaAddress(Address):

    def __init__(self, province: str):
        self.province = province
        
    @property
    def province(self) -> str:
        return self.__province

    @province.setter
    def province(self, province: str):
        self.__province = province

class customers_USAddress(Address):

    def __init__(self, state: str):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class customers_Address:

    def __init__(self, street: str, town: str, zipCode: str, customers_Address: "customers_Customer" = None):
        self.street = street
        self.town = town
        self.zipCode = zipCode
        self.customers_Address = customers_Address
        
    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def town(self) -> str:
        return self.__town

    @town.setter
    def town(self, town: str):
        self.__town = town

    @property
    def customers_Address(self):
        return self.__customers_Address

    @customers_Address.setter
    def customers_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_Address__customers_Address", None)
        self.__customers_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers_Customer"):
                opp_val = getattr(old_value, "customers_Customer", None)
                if opp_val == self:
                    setattr(old_value, "customers_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers_Customer"):
                opp_val = getattr(value, "customers_Customer", None)
                setattr(value, "customers_Customer", self)

class customers_CreditCard:

    def __init__(self, ccNumber: str, expiresDate: date, type: str, CreditCard: "customers_Customer" = None, creditCard: "customers_Customer" = None):
        self.ccNumber = ccNumber
        self.expiresDate = expiresDate
        self.type = type
        self.CreditCard = CreditCard
        self.creditCard = creditCard
        
    @property
    def ccNumber(self) -> str:
        return self.__ccNumber

    @ccNumber.setter
    def ccNumber(self, ccNumber: str):
        self.__ccNumber = ccNumber

    @property
    def expiresDate(self) -> date:
        return self.__expiresDate

    @expiresDate.setter
    def expiresDate(self, expiresDate: date):
        self.__expiresDate = expiresDate

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def CreditCard(self):
        return self.__CreditCard

    @CreditCard.setter
    def CreditCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_CreditCard__CreditCard", None)
        self.__CreditCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "holder"):
                opp_val = getattr(old_value, "holder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "holder"):
                opp_val = getattr(value, "holder", None)
                if opp_val is None:
                    setattr(value, "holder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def creditCard(self):
        return self.__creditCard

    @creditCard.setter
    def creditCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_CreditCard__creditCard", None)
        self.__creditCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

class customers_Customer:

    def __init__(self, firstName: str, lastName: str, comment: str, dateOfBirth: date, holder: set["customers_CreditCard"] = None, customers_Customer: "customers_Address" = None, Customer: "customers_CreditCard" = None, customers_Customer4: "customers_CustomersDB" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.comment = comment
        self.dateOfBirth = dateOfBirth
        self.holder = holder if holder is not None else set()
        self.customers_Customer = customers_Customer
        self.Customer = Customer
        self.customers_Customer4 = customers_Customer4
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_Customer__holder", None)
        self.__holder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreditCard"):
                    opp_val = getattr(item, "CreditCard", None)
                    
                    if opp_val == self:
                        setattr(item, "CreditCard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreditCard"):
                    opp_val = getattr(item, "CreditCard", None)
                    
                    setattr(item, "CreditCard", self)
                    

    @property
    def customers_Customer(self):
        return self.__customers_Customer

    @customers_Customer.setter
    def customers_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_Customer__customers_Customer", None)
        self.__customers_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers_Address"):
                opp_val = getattr(old_value, "customers_Address", None)
                if opp_val == self:
                    setattr(old_value, "customers_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers_Address"):
                opp_val = getattr(value, "customers_Address", None)
                setattr(value, "customers_Address", self)

    @property
    def customers_Customer4(self):
        return self.__customers_Customer4

    @customers_Customer4.setter
    def customers_Customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_Customer__customers_Customer4", None)
        self.__customers_Customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers_CustomersDB"):
                opp_val = getattr(old_value, "customers_CustomersDB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers_CustomersDB"):
                opp_val = getattr(value, "customers_CustomersDB", None)
                if opp_val is None:
                    setattr(value, "customers_CustomersDB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customers_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "creditCard"):
                opp_val = getattr(old_value, "creditCard", None)
                if opp_val == self:
                    setattr(old_value, "creditCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "creditCard"):
                opp_val = getattr(value, "creditCard", None)
                setattr(value, "creditCard", self)

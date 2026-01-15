from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


############################################
# Definition of Classes
############################################

class test_ConfigurationModel:

    pass
class test_AddressModel:

    def __init__(self, zipCode: str, validFrom: date, validTo: date, differentPostAddress: bool, street: str, houseNumber: str, test_AddressModel: "test_TestModel" = None):
        self.zipCode = zipCode
        self.validFrom = validFrom
        self.validTo = validTo
        self.differentPostAddress = differentPostAddress
        self.street = street
        self.houseNumber = houseNumber
        self.test_AddressModel = test_AddressModel
        
    @property
    def validFrom(self) -> date:
        return self.__validFrom

    @validFrom.setter
    def validFrom(self, validFrom: date):
        self.__validFrom = validFrom

    @property
    def houseNumber(self) -> str:
        return self.__houseNumber

    @houseNumber.setter
    def houseNumber(self, houseNumber: str):
        self.__houseNumber = houseNumber

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
    def validTo(self) -> date:
        return self.__validTo

    @validTo.setter
    def validTo(self, validTo: date):
        self.__validTo = validTo

    @property
    def differentPostAddress(self) -> bool:
        return self.__differentPostAddress

    @differentPostAddress.setter
    def differentPostAddress(self, differentPostAddress: bool):
        self.__differentPostAddress = differentPostAddress

    @property
    def test_AddressModel(self):
        return self.__test_AddressModel

    @test_AddressModel.setter
    def test_AddressModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_AddressModel__test_AddressModel", None)
        self.__test_AddressModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestModel"):
                opp_val = getattr(old_value, "test_TestModel", None)
                if opp_val == self:
                    setattr(old_value, "test_TestModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestModel"):
                opp_val = getattr(value, "test_TestModel", None)
                setattr(value, "test_TestModel", self)

class test_TestModel:

    def __init__(self, gender: str, name: str, birthDate: date, overdrawAccount: str, childCount: str, age: int, accountBalance: str, isSelectable: str, test_TestModel: "test_AddressModel" = None, test_TestModel2: "test_ConfigurationModel" = None, test_TestModel5: "test_ConfigurationModel" = None):
        self.gender = gender
        self.name = name
        self.birthDate = birthDate
        self.overdrawAccount = overdrawAccount
        self.childCount = childCount
        self.age = age
        self.accountBalance = accountBalance
        self.isSelectable = isSelectable
        self.test_TestModel = test_TestModel
        self.test_TestModel2 = test_TestModel2
        self.test_TestModel5 = test_TestModel5
        
    @property
    def accountBalance(self) -> str:
        return self.__accountBalance

    @accountBalance.setter
    def accountBalance(self, accountBalance: str):
        self.__accountBalance = accountBalance

    @property
    def isSelectable(self) -> str:
        return self.__isSelectable

    @isSelectable.setter
    def isSelectable(self, isSelectable: str):
        self.__isSelectable = isSelectable

    @property
    def childCount(self) -> str:
        return self.__childCount

    @childCount.setter
    def childCount(self, childCount: str):
        self.__childCount = childCount

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def overdrawAccount(self) -> str:
        return self.__overdrawAccount

    @overdrawAccount.setter
    def overdrawAccount(self, overdrawAccount: str):
        self.__overdrawAccount = overdrawAccount

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def birthDate(self) -> date:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate

    @property
    def test_TestModel(self):
        return self.__test_TestModel

    @test_TestModel.setter
    def test_TestModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestModel__test_TestModel", None)
        self.__test_TestModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_AddressModel"):
                opp_val = getattr(old_value, "test_AddressModel", None)
                if opp_val == self:
                    setattr(old_value, "test_AddressModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_AddressModel"):
                opp_val = getattr(value, "test_AddressModel", None)
                setattr(value, "test_AddressModel", self)

    @property
    def test_TestModel2(self):
        return self.__test_TestModel2

    @test_TestModel2.setter
    def test_TestModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestModel__test_TestModel2", None)
        self.__test_TestModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_ConfigurationModel"):
                opp_val = getattr(old_value, "test_ConfigurationModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_ConfigurationModel"):
                opp_val = getattr(value, "test_ConfigurationModel", None)
                if opp_val is None:
                    setattr(value, "test_ConfigurationModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_TestModel5(self):
        return self.__test_TestModel5

    @test_TestModel5.setter
    def test_TestModel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestModel__test_TestModel5", None)
        self.__test_TestModel5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_ConfigurationModel4"):
                opp_val = getattr(old_value, "test_ConfigurationModel4", None)
                if opp_val == self:
                    setattr(old_value, "test_ConfigurationModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_ConfigurationModel4"):
                opp_val = getattr(value, "test_ConfigurationModel4", None)
                setattr(value, "test_ConfigurationModel4", self)

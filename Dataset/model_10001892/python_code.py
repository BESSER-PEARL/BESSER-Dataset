from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Admin_Actor:

    pass


class View_AttackNews_UseCase:

    pass


class ExecuteAttack_UseCase:

    pass


class View_AttackHistory_UseCase:

    pass


class Edit_Profile_UseCase:

    pass


class View_Profile_UseCase:

    pass


class View_Home_UseCase:

    pass


class Authenticate_UseCase:

    pass


class Register_UseCase:

    pass


class User_Actor:

    pass





class View_Profile_UseCase1:

    pass


class View_Home_UseCase1:

    pass


class Authenticate_UseCase1:

    pass


class View_AttackNews_UseCase1:

    pass


class View_AttackHistory_UseCase1:

    pass


class Edit_Profile_UseCase1:

    pass


class StartParam:

    def __init__(self, type: str, value: str, attackHistory12: set["AttackHistory"] = None):
        self.type = type
        self.value = value
        self.attackHistory12 = attackHistory12 if attackHistory12 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def attackHistory12(self):
        return self.__attackHistory12
    @attackHistory12.setter
    def attackHistory12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StartParam__attackHistory12", None)
        self.__attackHistory12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "startParam13"):
                    opp_val = getattr(item, "startParam13", None)
                    
                    if opp_val == self:
                        setattr(item, "startParam13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "startParam13"):
                    opp_val = getattr(item, "startParam13", None)
                    
                    setattr(item, "startParam13", self)
                    



class Result:

    def __init__(self, value: str, attackHistory14: set["AttackHistory"] = None):
        self.value = value
        self.attackHistory14 = attackHistory14 if attackHistory14 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def attackHistory14(self):
        return self.__attackHistory14
    @attackHistory14.setter
    def attackHistory14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Result__attackHistory14", None)
        self.__attackHistory14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "result15"):
                    opp_val = getattr(item, "result15", None)
                    
                    if opp_val == self:
                        setattr(item, "result15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "result15"):
                    opp_val = getattr(item, "result15", None)
                    
                    setattr(item, "result15", self)
                    



class Attack:

    def __init__(self, name: str, requiredTokens: int, attackHistory10: set["AttackHistory"] = None):
        self.name = name
        self.requiredTokens = requiredTokens
        self.attackHistory10 = attackHistory10 if attackHistory10 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def requiredTokens(self):
        return self.__requiredTokens
    @requiredTokens.setter
    def requiredTokens(self, requiredTokens: int):
        self.__requiredTokens = requiredTokens

    @property
    def attackHistory10(self):
        return self.__attackHistory10
    @attackHistory10.setter
    def attackHistory10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attack__attackHistory10", None)
        self.__attackHistory10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attack11"):
                    opp_val = getattr(item, "attack11", None)
                    
                    if opp_val == self:
                        setattr(item, "attack11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attack11"):
                    opp_val = getattr(item, "attack11", None)
                    
                    setattr(item, "attack11", self)
                    



class AttackHistory:

    def __init__(self, auto: bool, target: str, date: int, attack11: "Attack" = None, startParam13: "StartParam" = None, result15: "Result" = None, user17: "User" = None):
        self.auto = auto
        self.target = target
        self.date = date
        self.attack11 = attack11
        self.startParam13 = startParam13
        self.result15 = result15
        self.user17 = user17
        
        pass
    @property
    def auto(self):
        return self.__auto
    @auto.setter
    def auto(self, auto: bool):
        self.__auto = auto

    @property
    def target(self):
        return self.__target
    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def startParam13(self):
        return self.__startParam13
    @startParam13.setter
    def startParam13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AttackHistory__startParam13", None)
        self.__startParam13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackHistory12"):
                opp_val = getattr(old_value, "attackHistory12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackHistory12"):
                opp_val = getattr(value, "attackHistory12", None)
                if opp_val is None:
                    setattr(value, "attackHistory12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def result15(self):
        return self.__result15
    @result15.setter
    def result15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AttackHistory__result15", None)
        self.__result15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackHistory14"):
                opp_val = getattr(old_value, "attackHistory14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackHistory14"):
                opp_val = getattr(value, "attackHistory14", None)
                if opp_val is None:
                    setattr(value, "attackHistory14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attack11(self):
        return self.__attack11
    @attack11.setter
    def attack11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AttackHistory__attack11", None)
        self.__attack11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackHistory10"):
                opp_val = getattr(old_value, "attackHistory10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackHistory10"):
                opp_val = getattr(value, "attackHistory10", None)
                if opp_val is None:
                    setattr(value, "attackHistory10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user17(self):
        return self.__user17
    @user17.setter
    def user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AttackHistory__user17", None)
        self.__user17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackHistory16"):
                opp_val = getattr(old_value, "attackHistory16", None)
                if opp_val == self:
                    setattr(old_value, "attackHistory16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackHistory16"):
                opp_val = getattr(value, "attackHistory16", None)
                setattr(value, "attackHistory16", self)



class Location:

    def __init__(self, streetAddress: str, postalCode: int, city: str, stateProvince: str, user3: "User" = None, country8: "Country" = None):
        self.streetAddress = streetAddress
        self.postalCode = postalCode
        self.city = city
        self.stateProvince = stateProvince
        self.user3 = user3
        self.country8 = country8
        
        pass
    @property
    def stateProvince(self):
        return self.__stateProvince
    @stateProvince.setter
    def stateProvince(self, stateProvince: str):
        self.__stateProvince = stateProvince

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def streetAddress(self):
        return self.__streetAddress
    @streetAddress.setter
    def streetAddress(self, streetAddress: str):
        self.__streetAddress = streetAddress

    @property
    def postalCode(self):
        return self.__postalCode
    @postalCode.setter
    def postalCode(self, postalCode: int):
        self.__postalCode = postalCode

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Location__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location2"):
                opp_val = getattr(old_value, "location2", None)
                if opp_val == self:
                    setattr(old_value, "location2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location2"):
                opp_val = getattr(value, "location2", None)
                setattr(value, "location2", self)

    @property
    def country8(self):
        return self.__country8
    @country8.setter
    def country8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Location__country8", None)
        self.__country8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location9"):
                opp_val = getattr(old_value, "location9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location9"):
                opp_val = getattr(value, "location9", None)
                if opp_val is None:
                    setattr(value, "location9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Country:

    def __init__(self, countryName: str, location9: set["Location"] = None):
        self.countryName = countryName
        self.location9 = location9 if location9 is not None else set()
        
        pass
    @property
    def countryName(self):
        return self.__countryName
    @countryName.setter
    def countryName(self, countryName: str):
        self.__countryName = countryName

    @property
    def location9(self):
        return self.__location9
    @location9.setter
    def location9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Country__location9", None)
        self.__location9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "country8"):
                    opp_val = getattr(item, "country8", None)
                    
                    if opp_val == self:
                        setattr(item, "country8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "country8"):
                    opp_val = getattr(item, "country8", None)
                    
                    setattr(item, "country8", self)
                    



class Balance:

    def __init__(self, tokens: int, account7: "Account" = None):
        self.tokens = tokens
        self.account7 = account7
        
        pass
    @property
    def tokens(self):
        return self.__tokens
    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Balance__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "balance6"):
                opp_val = getattr(old_value, "balance6", None)
                if opp_val == self:
                    setattr(old_value, "balance6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "balance6"):
                opp_val = getattr(value, "balance6", None)
                setattr(value, "balance6", self)



class Account:

    def __init__(self, login: str, password: int, creationDate: int, user5: "User" = None, balance6: "Balance" = None):
        self.login = login
        self.password = password
        self.creationDate = creationDate
        self.user5 = user5
        self.balance6 = balance6
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: int):
        self.__creationDate = creationDate

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def balance6(self):
        return self.__balance6
    @balance6.setter
    def balance6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__balance6", None)
        self.__balance6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)



class Role:

    def __init__(self, type: str, user1: set["User"] = None):
        self.type = type
        self.user1 = user1 if user1 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__user1", None)
        self.__user1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "role0"):
                    opp_val = getattr(item, "role0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "role0"):
                    opp_val = getattr(item, "role0", None)
                    
                    if opp_val is None:
                        setattr(item, "role0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, lName: str, birthDate: int, email: str, phoneNumber: int, cin: str, fName: str, role0: set["Role"] = None, location2: "Location" = None, account4: "Account" = None, attackHistory16: "AttackHistory" = None):
        self.lName = lName
        self.birthDate = birthDate
        self.email = email
        self.phoneNumber = phoneNumber
        self.cin = cin
        self.fName = fName
        self.role0 = role0 if role0 is not None else set()
        self.location2 = location2
        self.account4 = account4
        self.attackHistory16 = attackHistory16
        
        pass
    @property
    def fName(self):
        return self.__fName
    @fName.setter
    def fName(self, fName: str):
        self.__fName = fName

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self, cin: str):
        self.__cin = cin

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def birthDate(self):
        return self.__birthDate
    @birthDate.setter
    def birthDate(self, birthDate: int):
        self.__birthDate = birthDate

    @property
    def lName(self):
        return self.__lName
    @lName.setter
    def lName(self, lName: str):
        self.__lName = lName

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user5"):
                opp_val = getattr(old_value, "user5", None)
                if opp_val == self:
                    setattr(old_value, "user5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user5"):
                opp_val = getattr(value, "user5", None)
                setattr(value, "user5", self)

    @property
    def attackHistory16(self):
        return self.__attackHistory16
    @attackHistory16.setter
    def attackHistory16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__attackHistory16", None)
        self.__attackHistory16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user17"):
                opp_val = getattr(old_value, "user17", None)
                if opp_val == self:
                    setattr(old_value, "user17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user17"):
                opp_val = getattr(value, "user17", None)
                setattr(value, "user17", self)

    @property
    def location2(self):
        return self.__location2
    @location2.setter
    def location2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__location2", None)
        self.__location2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user3"):
                opp_val = getattr(old_value, "user3", None)
                if opp_val == self:
                    setattr(old_value, "user3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user3"):
                opp_val = getattr(value, "user3", None)
                setattr(value, "user3", self)

    @property
    def role0(self):
        return self.__role0
    @role0.setter
    def role0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__role0", None)
        self.__role0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    if opp_val is None:
                        setattr(item, "user1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    


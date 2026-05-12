from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class virtualtour_TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class ClientType:

    pass


class client_ClientAccount:

    def __init__(self, clientNo: str, type: ClientType, client0: "Client" = None, transactions2: set["virtualtour_Transaction"] = None):
        self.clientNo = clientNo
        self.type = type
        self.client0 = client0
        self.transactions2 = transactions2 if transactions2 is not None else set()
        
        pass
    @property
    def clientNo(self):
        return self.__clientNo
    @clientNo.setter
    def clientNo(self, clientNo: str):
        self.__clientNo = clientNo

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: ClientType):
        self.__type = type

    @property
    def client0(self):
        return self.__client0
    @client0.setter
    def client0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_client_ClientAccount__client0", None)
        self.__client0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                if opp_val is None:
                    setattr(value, "a1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transactions2(self):
        return self.__transactions2
    @transactions2.setter
    def transactions2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_client_ClientAccount__transactions2", None)
        self.__transactions2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    if opp_val == self:
                        setattr(item, "account3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    setattr(item, "account3", self)
                    



class client_Realtor:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class client_HomeOwner:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class virtualtour_ArchiveVirtual:

    pass


class virtualtour_LinkVirtual:

    pass


class virtualtour_TakePicture:

    pass


class virtualtour_UploadPicture:

    pass


class virtualtour_UploadFloorplan:

    pass


class virtualtour_Transaction:

    def __init__(self, id: int, type: virtualtour_TransactionType, transactionTime: date, account3: "client_ClientAccount" = None, linkVirtual7: "virtualtour_LinkVirtual" = None, archiveVirtual9: "virtualtour_ArchiveVirtual" = None):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.account3 = account3
        self.linkVirtual7 = linkVirtual7
        self.archiveVirtual9 = archiveVirtual9
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: virtualtour_TransactionType):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def linkVirtual7(self):
        return self.__linkVirtual7
    @linkVirtual7.setter
    def linkVirtual7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_virtualtour_Transaction__linkVirtual7", None)
        self.__linkVirtual7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction6"):
                opp_val = getattr(old_value, "transaction6", None)
                if opp_val == self:
                    setattr(old_value, "transaction6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction6"):
                opp_val = getattr(value, "transaction6", None)
                setattr(value, "transaction6", self)

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_virtualtour_Transaction__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions2"):
                opp_val = getattr(old_value, "transactions2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions2"):
                opp_val = getattr(value, "transactions2", None)
                if opp_val is None:
                    setattr(value, "transactions2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archiveVirtual9(self):
        return self.__archiveVirtual9
    @archiveVirtual9.setter
    def archiveVirtual9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_virtualtour_Transaction__archiveVirtual9", None)
        self.__archiveVirtual9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction8"):
                opp_val = getattr(old_value, "transaction8", None)
                if opp_val == self:
                    setattr(old_value, "transaction8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction8"):
                opp_val = getattr(value, "transaction8", None)
                setattr(value, "transaction8", self)



class Login:

    def __init__(self, username: str, securityAnswer: str, password: str, securityQuestion: str, lastLoginTime: date, client5: "Client" = None):
        self.username = username
        self.securityAnswer = securityAnswer
        self.password = password
        self.securityQuestion = securityQuestion
        self.lastLoginTime = lastLoginTime
        self.client5 = client5
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: date):
        self.__lastLoginTime = lastLoginTime

    @property
    def securityQuestion(self):
        return self.__securityQuestion
    @securityQuestion.setter
    def securityQuestion(self, securityQuestion: str):
        self.__securityQuestion = securityQuestion

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def securityAnswer(self):
        return self.__securityAnswer
    @securityAnswer.setter
    def securityAnswer(self, securityAnswer: str):
        self.__securityAnswer = securityAnswer

    @property
    def client5(self):
        return self.__client5
    @client5.setter
    def client5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__client5", None)
        self.__client5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)



class Client:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str, a1: set["client_ClientAccount"] = None, login4: "Login" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.a1 = a1 if a1 is not None else set()
        self.login4 = login4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__a1", None)
        self.__a1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "client0"):
                    opp_val = getattr(item, "client0", None)
                    
                    if opp_val == self:
                        setattr(item, "client0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "client0"):
                    opp_val = getattr(item, "client0", None)
                    
                    setattr(item, "client0", self)
                    

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client5"):
                opp_val = getattr(old_value, "client5", None)
                if opp_val == self:
                    setattr(old_value, "client5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client5"):
                opp_val = getattr(value, "client5", None)
                setattr(value, "client5", self)


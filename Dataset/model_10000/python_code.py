from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardType(Enum):
    pass

############################################
# Definition of Classes
############################################

class bank_Manager:

    def __init__(self, name: str, bank_Manager: "bank_Bank" = None, Manager: "bank_Client" = None, manager: set["bank_Client"] = None):
        self.name = name
        self.bank_Manager = bank_Manager
        self.Manager = Manager
        self.manager = manager if manager is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Manager(self):
        return self.__Manager

    @Manager.setter
    def Manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Manager__Manager", None)
        self.__Manager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clients"):
                opp_val = getattr(old_value, "clients", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clients"):
                opp_val = getattr(value, "clients", None)
                if opp_val is None:
                    setattr(value, "clients", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Manager__manager", None)
        self.__manager = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Client"):
                    opp_val = getattr(item, "Client", None)
                    
                    if opp_val == self:
                        setattr(item, "Client", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Client"):
                    opp_val = getattr(item, "Client", None)
                    
                    setattr(item, "Client", self)
                    

    @property
    def bank_Manager(self):
        return self.__bank_Manager

    @bank_Manager.setter
    def bank_Manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Manager__bank_Manager", None)
        self.__bank_Manager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Bank"):
                opp_val = getattr(old_value, "bank_Bank", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Bank"):
                opp_val = getattr(value, "bank_Bank", None)
                if opp_val is None:
                    setattr(value, "bank_Bank", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bank_Bank:

    pass
class bank_Card:

    def __init__(self, number: str, type: str, bank_Card: "bank_Account" = None):
        self.number = number
        self.type = type
        self.bank_Card = bank_Card
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def bank_Card(self):
        return self.__bank_Card

    @bank_Card.setter
    def bank_Card(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Card__bank_Card", None)
        self.__bank_Card = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Account14"):
                opp_val = getattr(old_value, "bank_Account14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Account14"):
                opp_val = getattr(value, "bank_Account14", None)
                if opp_val is None:
                    setattr(value, "bank_Account14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bank_Client:

    def __init__(self, name: str, capacity: int, bank_Client: "bank_Bank" = None, clients: set["bank_Manager"] = None, owners: set["bank_Account"] = None, bank_Client9: "bank_Client" = None, bank_Client7: set["bank_Client"] = None, Client: "bank_Manager" = None, Client12: "bank_Account" = None):
        self.name = name
        self.capacity = capacity
        self.bank_Client = bank_Client
        self.clients = clients if clients is not None else set()
        self.owners = owners if owners is not None else set()
        self.bank_Client9 = bank_Client9
        self.bank_Client7 = bank_Client7 if bank_Client7 is not None else set()
        self.Client = Client
        self.Client12 = Client12
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity


    @property
    def bank_Client7(self):
        return self.__bank_Client7

    @bank_Client7.setter
    def bank_Client7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__bank_Client7", None)
        self.__bank_Client7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank_Client9"):
                    opp_val = getattr(item, "bank_Client9", None)
                    
                    if opp_val == self:
                        setattr(item, "bank_Client9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank_Client9"):
                    opp_val = getattr(item, "bank_Client9", None)
                    
                    setattr(item, "bank_Client9", self)
                    

    @property
    def bank_Client(self):
        return self.__bank_Client

    @bank_Client.setter
    def bank_Client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__bank_Client", None)
        self.__bank_Client = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Bank4"):
                opp_val = getattr(old_value, "bank_Bank4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Bank4"):
                opp_val = getattr(value, "bank_Bank4", None)
                if opp_val is None:
                    setattr(value, "bank_Bank4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__owners", None)
        self.__owners = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    if opp_val == self:
                        setattr(item, "Account", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    setattr(item, "Account", self)
                    

    @property
    def clients(self):
        return self.__clients

    @clients.setter
    def clients(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__clients", None)
        self.__clients = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Manager"):
                    opp_val = getattr(item, "Manager", None)
                    
                    if opp_val == self:
                        setattr(item, "Manager", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Manager"):
                    opp_val = getattr(item, "Manager", None)
                    
                    setattr(item, "Manager", self)
                    

    @property
    def Client12(self):
        return self.__Client12

    @Client12.setter
    def Client12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__Client12", None)
        self.__Client12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts"):
                opp_val = getattr(old_value, "accounts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts"):
                opp_val = getattr(value, "accounts", None)
                if opp_val is None:
                    setattr(value, "accounts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__Client", None)
        self.__Client = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                if opp_val is None:
                    setattr(value, "manager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_Client9(self):
        return self.__bank_Client9

    @bank_Client9.setter
    def bank_Client9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Client__bank_Client9", None)
        self.__bank_Client9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Client7"):
                opp_val = getattr(old_value, "bank_Client7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Client7"):
                opp_val = getattr(value, "bank_Client7", None)
                if opp_val is None:
                    setattr(value, "bank_Client7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bank_Account:

    def __init__(self, credit: float, overdraft: float, bank_Account: "bank_Bank" = None, Account: "bank_Client" = None, accounts: set["bank_Client"] = None, bank_Account14: set["bank_Card"] = None):
        self.credit = credit
        self.overdraft = overdraft
        self.bank_Account = bank_Account
        self.Account = Account
        self.accounts = accounts if accounts is not None else set()
        self.bank_Account14 = bank_Account14 if bank_Account14 is not None else set()
        
        pass
    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit


    @property
    def overdraft(self):
        return self.__overdraft

    @overdraft.setter
    def overdraft(self, overdraft: float):
        self.__overdraft = overdraft


    @property
    def bank_Account(self):
        return self.__bank_Account

    @bank_Account.setter
    def bank_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__bank_Account", None)
        self.__bank_Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Bank2"):
                opp_val = getattr(old_value, "bank_Bank2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Bank2"):
                opp_val = getattr(value, "bank_Bank2", None)
                if opp_val is None:
                    setattr(value, "bank_Bank2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_Account14(self):
        return self.__bank_Account14

    @bank_Account14.setter
    def bank_Account14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__bank_Account14", None)
        self.__bank_Account14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank_Card"):
                    opp_val = getattr(item, "bank_Card", None)
                    
                    if opp_val == self:
                        setattr(item, "bank_Card", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank_Card"):
                    opp_val = getattr(item, "bank_Card", None)
                    
                    setattr(item, "bank_Card", self)
                    

    @property
    def Account(self):
        return self.__Account

    @Account.setter
    def Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__Account", None)
        self.__Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owners"):
                opp_val = getattr(old_value, "owners", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owners"):
                opp_val = getattr(value, "owners", None)
                if opp_val is None:
                    setattr(value, "owners", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__accounts", None)
        self.__accounts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Client12"):
                    opp_val = getattr(item, "Client12", None)
                    
                    if opp_val == self:
                        setattr(item, "Client12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Client12"):
                    opp_val = getattr(item, "Client12", None)
                    
                    setattr(item, "Client12", self)
                    

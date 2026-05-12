from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RoyalAndLoyal_LoyaltyProgram:

    def __init__(self, programs3: set["RoyalAndLoyal_Customer"] = None, LoyaltyProgram: "RoyalAndLoyal_ServiceLevel" = None, RoyalAndLoyal_LoyaltyProgram: "RoyalAndLoyal_Container_RandL" = None, LoyaltyProgram20: "RoyalAndLoyal_Customer" = None, LoyaltyProgram31: "RoyalAndLoyal_ProgramPartner" = None, programs: set["RoyalAndLoyal_ProgramPartner"] = None, program: set["RoyalAndLoyal_ServiceLevel"] = None):
        self.programs3 = programs3 if programs3 is not None else set()
        self.LoyaltyProgram = LoyaltyProgram
        self.RoyalAndLoyal_LoyaltyProgram = RoyalAndLoyal_LoyaltyProgram
        self.LoyaltyProgram20 = LoyaltyProgram20
        self.LoyaltyProgram31 = LoyaltyProgram31
        self.programs = programs if programs is not None else set()
        self.program = program if program is not None else set()
        
        pass
    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__program", None)
        self.__program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceLevel"):
                    opp_val = getattr(item, "ServiceLevel", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceLevel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceLevel"):
                    opp_val = getattr(item, "ServiceLevel", None)
                    
                    setattr(item, "ServiceLevel", self)
                    

    @property
    def RoyalAndLoyal_LoyaltyProgram(self):
        return self.__RoyalAndLoyal_LoyaltyProgram

    @RoyalAndLoyal_LoyaltyProgram.setter
    def RoyalAndLoyal_LoyaltyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__RoyalAndLoyal_LoyaltyProgram", None)
        self.__RoyalAndLoyal_LoyaltyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL13"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL13"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL13", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LoyaltyProgram(self):
        return self.__LoyaltyProgram

    @LoyaltyProgram.setter
    def LoyaltyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram", None)
        self.__LoyaltyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "levels"):
                opp_val = getattr(old_value, "levels", None)
                if opp_val == self:
                    setattr(old_value, "levels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "levels"):
                opp_val = getattr(value, "levels", None)
                setattr(value, "levels", self)

    @property
    def programs3(self):
        return self.__programs3

    @programs3.setter
    def programs3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__programs3", None)
        self.__programs3 = value if value is not None else set()
        
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
                    

    @property
    def LoyaltyProgram31(self):
        return self.__LoyaltyProgram31

    @LoyaltyProgram31.setter
    def LoyaltyProgram31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram31", None)
        self.__LoyaltyProgram31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partners"):
                opp_val = getattr(old_value, "partners", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partners"):
                opp_val = getattr(value, "partners", None)
                if opp_val is None:
                    setattr(value, "partners", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LoyaltyProgram20(self):
        return self.__LoyaltyProgram20

    @LoyaltyProgram20.setter
    def LoyaltyProgram20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram20", None)
        self.__LoyaltyProgram20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participants"):
                opp_val = getattr(old_value, "participants", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participants"):
                opp_val = getattr(value, "participants", None)
                if opp_val is None:
                    setattr(value, "participants", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__programs", None)
        self.__programs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgramPartner"):
                    opp_val = getattr(item, "ProgramPartner", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgramPartner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgramPartner"):
                    opp_val = getattr(item, "ProgramPartner", None)
                    
                    setattr(item, "ProgramPartner", self)
                    

    def enroll(self, RoyalAndLoyal_c):
        # TODO: Implement enroll method
        pass

    def addService(self, RoyalAndLoyal_s, RoyalAndLoyal_l, RoyalAndLoyal_p):
        # TODO: Implement addService method
        pass

class RoyalAndLoyal_CustomerCard:

    def __init__(self, valid: bool, RoyalAndLoyal_CustomerCard: "RoyalAndLoyal_Container_RandL" = None, CustomerCard: "RoyalAndLoyal_Customer" = None, cards: "RoyalAndLoyal_Customer" = None, RoyalAndLoyal_CustomerCard23: "RoyalAndLoyal_ServiceLevel" = None):
        self.valid = valid
        self.RoyalAndLoyal_CustomerCard = RoyalAndLoyal_CustomerCard
        self.CustomerCard = CustomerCard
        self.cards = cards
        self.RoyalAndLoyal_CustomerCard23 = RoyalAndLoyal_CustomerCard23
        
        pass
    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, valid: bool):
        self.__valid = valid


    @property
    def RoyalAndLoyal_CustomerCard23(self):
        return self.__RoyalAndLoyal_CustomerCard23

    @RoyalAndLoyal_CustomerCard23.setter
    def RoyalAndLoyal_CustomerCard23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard23", None)
        self.__RoyalAndLoyal_CustomerCard23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_ServiceLevel24"):
                opp_val = getattr(old_value, "RoyalAndLoyal_ServiceLevel24", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_ServiceLevel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_ServiceLevel24"):
                opp_val = getattr(value, "RoyalAndLoyal_ServiceLevel24", None)
                setattr(value, "RoyalAndLoyal_ServiceLevel24", self)

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__cards", None)
        self.__cards = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer26"):
                opp_val = getattr(old_value, "Customer26", None)
                if opp_val == self:
                    setattr(old_value, "Customer26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer26"):
                opp_val = getattr(value, "Customer26", None)
                setattr(value, "Customer26", self)

    @property
    def RoyalAndLoyal_CustomerCard(self):
        return self.__RoyalAndLoyal_CustomerCard

    @RoyalAndLoyal_CustomerCard.setter
    def RoyalAndLoyal_CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard", None)
        self.__RoyalAndLoyal_CustomerCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL8"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL8"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL8", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CustomerCard(self):
        return self.__CustomerCard

    @CustomerCard.setter
    def CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__CustomerCard", None)
        self.__CustomerCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RoyalAndLoyal_Container_RandL:

    pass
class RoyalAndLoyal_Customer:

    pass
class RoyalAndLoyal_ServiceLevel:

    pass
class RoyalAndLoyal_ProgramPartner:

    def __init__(self, numberOfCustomers: int, RoyalAndLoyal_ProgramPartner: "RoyalAndLoyal_Container_RandL" = None, RoyalAndLoyal_ProgramPartner28: set["RoyalAndLoyal_Service"] = None, partners: set["RoyalAndLoyal_LoyaltyProgram"] = None, ProgramPartner: "RoyalAndLoyal_LoyaltyProgram" = None):
        self.numberOfCustomers = numberOfCustomers
        self.RoyalAndLoyal_ProgramPartner = RoyalAndLoyal_ProgramPartner
        self.RoyalAndLoyal_ProgramPartner28 = RoyalAndLoyal_ProgramPartner28 if RoyalAndLoyal_ProgramPartner28 is not None else set()
        self.partners = partners if partners is not None else set()
        self.ProgramPartner = ProgramPartner
        
        pass
    @property
    def numberOfCustomers(self):
        return self.__numberOfCustomers

    @numberOfCustomers.setter
    def numberOfCustomers(self, numberOfCustomers: int):
        self.__numberOfCustomers = numberOfCustomers


    @property
    def ProgramPartner(self):
        return self.__ProgramPartner

    @ProgramPartner.setter
    def ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__ProgramPartner", None)
        self.__ProgramPartner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programs"):
                opp_val = getattr(old_value, "programs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programs"):
                opp_val = getattr(value, "programs", None)
                if opp_val is None:
                    setattr(value, "programs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoyalAndLoyal_ProgramPartner(self):
        return self.__RoyalAndLoyal_ProgramPartner

    @RoyalAndLoyal_ProgramPartner.setter
    def RoyalAndLoyal_ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__RoyalAndLoyal_ProgramPartner", None)
        self.__RoyalAndLoyal_ProgramPartner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL18"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL18"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL18", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def partners(self):
        return self.__partners

    @partners.setter
    def partners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__partners", None)
        self.__partners = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LoyaltyProgram31"):
                    opp_val = getattr(item, "LoyaltyProgram31", None)
                    
                    if opp_val == self:
                        setattr(item, "LoyaltyProgram31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LoyaltyProgram31"):
                    opp_val = getattr(item, "LoyaltyProgram31", None)
                    
                    setattr(item, "LoyaltyProgram31", self)
                    

    @property
    def RoyalAndLoyal_ProgramPartner28(self):
        return self.__RoyalAndLoyal_ProgramPartner28

    @RoyalAndLoyal_ProgramPartner28.setter
    def RoyalAndLoyal_ProgramPartner28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__RoyalAndLoyal_ProgramPartner28", None)
        self.__RoyalAndLoyal_ProgramPartner28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoyalAndLoyal_Service29"):
                    opp_val = getattr(item, "RoyalAndLoyal_Service29", None)
                    
                    if opp_val == self:
                        setattr(item, "RoyalAndLoyal_Service29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoyalAndLoyal_Service29"):
                    opp_val = getattr(item, "RoyalAndLoyal_Service29", None)
                    
                    setattr(item, "RoyalAndLoyal_Service29", self)
                    

class RoyalAndLoyal_Service:

    pass
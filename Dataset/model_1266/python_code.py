from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FamilyMModel_Member:

    def __init__(self, firstName: str, relation: str, FamilyMModel_Member: "FamilyMModel_Family" = None):
        self.firstName = firstName
        self.relation = relation
        self.FamilyMModel_Member = FamilyMModel_Member
        
    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def FamilyMModel_Member(self):
        return self.__FamilyMModel_Member

    @FamilyMModel_Member.setter
    def FamilyMModel_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyMModel_Member__FamilyMModel_Member", None)
        self.__FamilyMModel_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyMModel_Family"):
                opp_val = getattr(old_value, "FamilyMModel_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyMModel_Family"):
                opp_val = getattr(value, "FamilyMModel_Family", None)
                if opp_val is None:
                    setattr(value, "FamilyMModel_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FamilyMModel_Family:

    def __init__(self, lastName: str, FamilyMModel_Family: set["FamilyMModel_Member"] = None):
        self.lastName = lastName
        self.FamilyMModel_Family = FamilyMModel_Family if FamilyMModel_Family is not None else set()
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def FamilyMModel_Family(self):
        return self.__FamilyMModel_Family

    @FamilyMModel_Family.setter
    def FamilyMModel_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyMModel_Family__FamilyMModel_Family", None)
        self.__FamilyMModel_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyMModel_Member"):
                    opp_val = getattr(item, "FamilyMModel_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyMModel_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyMModel_Member"):
                    opp_val = getattr(item, "FamilyMModel_Member", None)
                    
                    setattr(item, "FamilyMModel_Member", self)
                    

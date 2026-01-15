from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class geneology_Member:

    def __init__(self, name: str, female: bool, members: "geneology_Family" = None, Member: "geneology_Family" = None):
        self.name = name
        self.female = female
        self.members = members
        self.Member = Member
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def female(self) -> bool:
        return self.__female

    @female.setter
    def female(self, female: bool):
        self.__female = female

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                if opp_val is None:
                    setattr(value, "family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Member__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family4"):
                opp_val = getattr(old_value, "Family4", None)
                if opp_val == self:
                    setattr(old_value, "Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family4"):
                opp_val = getattr(value, "Family4", None)
                setattr(value, "Family4", self)

class geneology_Family:

    def __init__(self, name: str, Family: "geneology_Geneology" = None, families: "geneology_Geneology" = None, Family4: "geneology_Member" = None, family: set["geneology_Member"] = None):
        self.name = name
        self.Family = Family
        self.families = families
        self.Family4 = Family4
        self.family = family if family is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geneology"):
                opp_val = getattr(old_value, "Geneology", None)
                if opp_val == self:
                    setattr(old_value, "Geneology", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geneology"):
                opp_val = getattr(value, "Geneology", None)
                setattr(value, "Geneology", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geneology"):
                opp_val = getattr(old_value, "geneology", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geneology"):
                opp_val = getattr(value, "geneology", None)
                if opp_val is None:
                    setattr(value, "geneology", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Family__family", None)
        self.__family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    @property
    def Family4(self):
        return self.__Family4

    @Family4.setter
    def Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geneology_Family__Family4", None)
        self.__Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

class geneology_Geneology:

    pass
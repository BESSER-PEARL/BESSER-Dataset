from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class family_Family:

    def __init__(self, lastName: str, Family2: "family_Member" = None, Family4: "family_Member" = None, Family6: "family_Member" = None, familyFather: "family_Member" = None, familyMother: "family_Member" = None, familySon: set["family_Member"] = None, familyDaughter: set["family_Member"] = None, Family: "family_Member" = None):
        self.lastName = lastName
        self.Family2 = Family2
        self.Family4 = Family4
        self.Family6 = Family6
        self.familyFather = familyFather
        self.familyMother = familyMother
        self.familySon = familySon if familySon is not None else set()
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        self.Family = Family
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Family6(self):
        return self.__Family6

    @Family6.setter
    def Family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__Family6", None)
        self.__Family6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daughter"):
                opp_val = getattr(old_value, "daughter", None)
                if opp_val == self:
                    setattr(old_value, "daughter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daughter"):
                opp_val = getattr(value, "daughter", None)
                setattr(value, "daughter", self)

    @property
    def familySon(self):
        return self.__familySon

    @familySon.setter
    def familySon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__familySon", None)
        self.__familySon = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member11"):
                    opp_val = getattr(item, "Member11", None)
                    
                    if opp_val == self:
                        setattr(item, "Member11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member11"):
                    opp_val = getattr(item, "Member11", None)
                    
                    setattr(item, "Member11", self)
                    

    @property
    def Family4(self):
        return self.__Family4

    @Family4.setter
    def Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__Family4", None)
        self.__Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "son"):
                opp_val = getattr(old_value, "son", None)
                if opp_val == self:
                    setattr(old_value, "son", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "son"):
                opp_val = getattr(value, "son", None)
                setattr(value, "son", self)

    @property
    def familyDaughter(self):
        return self.__familyDaughter

    @familyDaughter.setter
    def familyDaughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__familyDaughter", None)
        self.__familyDaughter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member13"):
                    opp_val = getattr(item, "Member13", None)
                    
                    if opp_val == self:
                        setattr(item, "Member13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member13"):
                    opp_val = getattr(item, "Member13", None)
                    
                    setattr(item, "Member13", self)
                    

    @property
    def familyMother(self):
        return self.__familyMother

    @familyMother.setter
    def familyMother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__familyMother", None)
        self.__familyMother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member9"):
                opp_val = getattr(old_value, "Member9", None)
                if opp_val == self:
                    setattr(old_value, "Member9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member9"):
                opp_val = getattr(value, "Member9", None)
                setattr(value, "Member9", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "father"):
                opp_val = getattr(old_value, "father", None)
                if opp_val == self:
                    setattr(old_value, "father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "father"):
                opp_val = getattr(value, "father", None)
                setattr(value, "father", self)

    @property
    def familyFather(self):
        return self.__familyFather

    @familyFather.setter
    def familyFather(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__familyFather", None)
        self.__familyFather = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member"):
                opp_val = getattr(old_value, "Member", None)
                if opp_val == self:
                    setattr(old_value, "Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member"):
                opp_val = getattr(value, "Member", None)
                setattr(value, "Member", self)

    @property
    def Family2(self):
        return self.__Family2

    @Family2.setter
    def Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__Family2", None)
        self.__Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mother"):
                opp_val = getattr(old_value, "mother", None)
                if opp_val == self:
                    setattr(old_value, "mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mother"):
                opp_val = getattr(value, "mother", None)
                setattr(value, "mother", self)

class family_Member(ABC):

    def __init__(self, name: str, mother: "family_Family" = None, son: "family_Family" = None, daughter: "family_Family" = None, Member: "family_Family" = None, Member9: "family_Family" = None, Member11: "family_Family" = None, Member13: "family_Family" = None, father: "family_Family" = None):
        self.name = name
        self.mother = mother
        self.son = son
        self.daughter = daughter
        self.Member = Member
        self.Member9 = Member9
        self.Member11 = Member11
        self.Member13 = Member13
        self.father = father
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def son(self):
        return self.__son

    @son.setter
    def son(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__son", None)
        self.__son = value
        
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

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family2"):
                opp_val = getattr(old_value, "Family2", None)
                if opp_val == self:
                    setattr(old_value, "Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family2"):
                opp_val = getattr(value, "Family2", None)
                setattr(value, "Family2", self)

    @property
    def Member11(self):
        return self.__Member11

    @Member11.setter
    def Member11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__Member11", None)
        self.__Member11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familySon"):
                opp_val = getattr(old_value, "familySon", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familySon"):
                opp_val = getattr(value, "familySon", None)
                if opp_val is None:
                    setattr(value, "familySon", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__father", None)
        self.__father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family"):
                opp_val = getattr(old_value, "Family", None)
                if opp_val == self:
                    setattr(old_value, "Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family"):
                opp_val = getattr(value, "Family", None)
                setattr(value, "Family", self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familyFather"):
                opp_val = getattr(old_value, "familyFather", None)
                if opp_val == self:
                    setattr(old_value, "familyFather", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familyFather"):
                opp_val = getattr(value, "familyFather", None)
                setattr(value, "familyFather", self)

    @property
    def Member13(self):
        return self.__Member13

    @Member13.setter
    def Member13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__Member13", None)
        self.__Member13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familyDaughter"):
                opp_val = getattr(old_value, "familyDaughter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familyDaughter"):
                opp_val = getattr(value, "familyDaughter", None)
                if opp_val is None:
                    setattr(value, "familyDaughter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Member9(self):
        return self.__Member9

    @Member9.setter
    def Member9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__Member9", None)
        self.__Member9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familyMother"):
                opp_val = getattr(old_value, "familyMother", None)
                if opp_val == self:
                    setattr(old_value, "familyMother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familyMother"):
                opp_val = getattr(value, "familyMother", None)
                setattr(value, "familyMother", self)

    @property
    def daughter(self):
        return self.__daughter

    @daughter.setter
    def daughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Member__daughter", None)
        self.__daughter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family6"):
                opp_val = getattr(old_value, "Family6", None)
                if opp_val == self:
                    setattr(old_value, "Family6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family6"):
                opp_val = getattr(value, "Family6", None)
                setattr(value, "Family6", self)

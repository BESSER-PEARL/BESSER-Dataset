from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Families_Member:

    def __init__(self, firstName: str, Member: "Families_Family" = None, Member2: "Families_Family" = None, Member4: "Families_Family" = None, Member6: "Families_Family" = None, father: "Families_Family" = None, mother: "Families_Family" = None, sons: "Families_Family" = None, daughters: "Families_Family" = None):
        self.firstName = firstName
        self.Member = Member
        self.Member2 = Member2
        self.Member4 = Member4
        self.Member6 = Member6
        self.father = father
        self.mother = mother
        self.sons = sons
        self.daughters = daughters
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__daughters", None)
        self.__daughters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family13"):
                opp_val = getattr(old_value, "Family13", None)
                if opp_val == self:
                    setattr(old_value, "Family13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family13"):
                opp_val = getattr(value, "Family13", None)
                setattr(value, "Family13", self)

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family9"):
                opp_val = getattr(old_value, "Family9", None)
                if opp_val == self:
                    setattr(old_value, "Family9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family9"):
                opp_val = getattr(value, "Family9", None)
                setattr(value, "Family9", self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Member", None)
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
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__father", None)
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
    def Member2(self):
        return self.__Member2

    @Member2.setter
    def Member2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Member2", None)
        self.__Member2 = value
        
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
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__sons", None)
        self.__sons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family11"):
                opp_val = getattr(old_value, "Family11", None)
                if opp_val == self:
                    setattr(old_value, "Family11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family11"):
                opp_val = getattr(value, "Family11", None)
                setattr(value, "Family11", self)

    @property
    def Member6(self):
        return self.__Member6

    @Member6.setter
    def Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Member6", None)
        self.__Member6 = value
        
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
    def Member4(self):
        return self.__Member4

    @Member4.setter
    def Member4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Member4", None)
        self.__Member4 = value
        
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

class Families_Family:

    def __init__(self, lastName: str, familyFather: "Families_Member" = None, familyMother: "Families_Member" = None, familySon: set["Families_Member"] = None, familyDaughter: set["Families_Member"] = None, Family: "Families_Member" = None, Family9: "Families_Member" = None, Family11: "Families_Member" = None, Family13: "Families_Member" = None):
        self.lastName = lastName
        self.familyFather = familyFather
        self.familyMother = familyMother
        self.familySon = familySon if familySon is not None else set()
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        self.Family = Family
        self.Family9 = Family9
        self.Family11 = Family11
        self.Family13 = Family13
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def familyFather(self):
        return self.__familyFather

    @familyFather.setter
    def familyFather(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyFather", None)
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
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family", None)
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
    def familyDaughter(self):
        return self.__familyDaughter

    @familyDaughter.setter
    def familyDaughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyDaughter", None)
        self.__familyDaughter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member6"):
                    opp_val = getattr(item, "Member6", None)
                    
                    if opp_val == self:
                        setattr(item, "Member6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member6"):
                    opp_val = getattr(item, "Member6", None)
                    
                    setattr(item, "Member6", self)
                    

    @property
    def familyMother(self):
        return self.__familyMother

    @familyMother.setter
    def familyMother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyMother", None)
        self.__familyMother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member2"):
                opp_val = getattr(old_value, "Member2", None)
                if opp_val == self:
                    setattr(old_value, "Member2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member2"):
                opp_val = getattr(value, "Member2", None)
                setattr(value, "Member2", self)

    @property
    def familySon(self):
        return self.__familySon

    @familySon.setter
    def familySon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familySon", None)
        self.__familySon = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member4"):
                    opp_val = getattr(item, "Member4", None)
                    
                    if opp_val == self:
                        setattr(item, "Member4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member4"):
                    opp_val = getattr(item, "Member4", None)
                    
                    setattr(item, "Member4", self)
                    

    @property
    def Family13(self):
        return self.__Family13

    @Family13.setter
    def Family13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family13", None)
        self.__Family13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daughters"):
                opp_val = getattr(old_value, "daughters", None)
                if opp_val == self:
                    setattr(old_value, "daughters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daughters"):
                opp_val = getattr(value, "daughters", None)
                setattr(value, "daughters", self)

    @property
    def Family11(self):
        return self.__Family11

    @Family11.setter
    def Family11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family11", None)
        self.__Family11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sons"):
                opp_val = getattr(old_value, "sons", None)
                if opp_val == self:
                    setattr(old_value, "sons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sons"):
                opp_val = getattr(value, "sons", None)
                setattr(value, "sons", self)

    @property
    def Family9(self):
        return self.__Family9

    @Family9.setter
    def Family9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family9", None)
        self.__Family9 = value
        
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

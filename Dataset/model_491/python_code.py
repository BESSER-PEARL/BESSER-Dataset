from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Member:

    pass
class Families_Family:

    def __init__(self, lastName: str, familyFather: "Member" = None, familyMother: "Member" = None, familySon: set["Member"] = None, familyDaughter: set["Member"] = None):
        self.lastName = lastName
        self.familyFather = familyFather
        self.familyMother = familyMother
        self.familySon = familySon if familySon is not None else set()
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


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

class Families_MemberMale(Member):

    def __init__(self, test: str, Member6: "Families_Family" = None, Member2: "Families_Family" = None, Member: "Families_Family" = None, Member4: "Families_Family" = None):
        self.test = test
        
        pass
    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, test: str):
        self.__test = test


class Family:

    pass
class Families_Member:

    def __init__(self, firstName: str, mother: "Family" = None, sons: "Family" = None, daughters: "Family" = None, father: "Family" = None):
        self.firstName = firstName
        self.mother = mother
        self.sons = sons
        self.daughters = daughters
        self.father = father
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


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

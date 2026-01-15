from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class families_Member:

    def __init__(self, firstName: str, Member: "families_Family" = None, Member3: "families_Family" = None, sons: "families_Family" = None, daughters: "families_Family" = None, father: "families_Family" = None, mother: "families_Family" = None, Member5: "families_Family" = None, Member7: "families_Family" = None):
        self.firstName = firstName
        self.Member = Member
        self.Member3 = Member3
        self.sons = sons
        self.daughters = daughters
        self.father = father
        self.mother = mother
        self.Member5 = Member5
        self.Member7 = Member7
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__sons", None)
        self.__sons = value
        
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
    def Member7(self):
        return self.__Member7

    @Member7.setter
    def Member7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member7", None)
        self.__Member7 = value
        
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
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__daughters", None)
        self.__daughters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family10"):
                opp_val = getattr(old_value, "Family10", None)
                if opp_val == self:
                    setattr(old_value, "Family10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family10"):
                opp_val = getattr(value, "Family10", None)
                setattr(value, "Family10", self)

    @property
    def Member3(self):
        return self.__Member3

    @Member3.setter
    def Member3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member3", None)
        self.__Member3 = value
        
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
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member", None)
        self.__Member = value
        
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
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family14"):
                opp_val = getattr(old_value, "Family14", None)
                if opp_val == self:
                    setattr(old_value, "Family14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family14"):
                opp_val = getattr(value, "Family14", None)
                setattr(value, "Family14", self)

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__father", None)
        self.__father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family12"):
                opp_val = getattr(old_value, "Family12", None)
                if opp_val == self:
                    setattr(old_value, "Family12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family12"):
                opp_val = getattr(value, "Family12", None)
                setattr(value, "Family12", self)

    @property
    def Member5(self):
        return self.__Member5

    @Member5.setter
    def Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member5", None)
        self.__Member5 = value
        
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

class families_Family:

    def __init__(self, lastName: str, families_Family: "families_FamilyRegister" = None, familySon: set["families_Member"] = None, familyDaughter: set["families_Member"] = None, Family: "families_Member" = None, Family10: "families_Member" = None, Family12: "families_Member" = None, Family14: "families_Member" = None, familyFather: "families_Member" = None, familyMother: "families_Member" = None):
        self.lastName = lastName
        self.families_Family = families_Family
        self.familySon = familySon if familySon is not None else set()
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        self.Family = Family
        self.Family10 = Family10
        self.Family12 = Family12
        self.Family14 = Family14
        self.familyFather = familyFather
        self.familyMother = familyMother
        
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
        old_value = getattr(self, f"_families_Family__familyFather", None)
        self.__familyFather = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member5"):
                opp_val = getattr(old_value, "Member5", None)
                if opp_val == self:
                    setattr(old_value, "Member5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member5"):
                opp_val = getattr(value, "Member5", None)
                setattr(value, "Member5", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family", None)
        self.__Family = value
        
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
    def Family10(self):
        return self.__Family10

    @Family10.setter
    def Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family10", None)
        self.__Family10 = value
        
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
    def Family14(self):
        return self.__Family14

    @Family14.setter
    def Family14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family14", None)
        self.__Family14 = value
        
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

    @property
    def familySon(self):
        return self.__familySon

    @familySon.setter
    def familySon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__familySon", None)
        self.__familySon = value if value is not None else set()
        
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
    def familyMother(self):
        return self.__familyMother

    @familyMother.setter
    def familyMother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__familyMother", None)
        self.__familyMother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member7"):
                opp_val = getattr(old_value, "Member7", None)
                if opp_val == self:
                    setattr(old_value, "Member7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member7"):
                opp_val = getattr(value, "Member7", None)
                setattr(value, "Member7", self)

    @property
    def families_Family(self):
        return self.__families_Family

    @families_Family.setter
    def families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family", None)
        self.__families_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_FamilyRegister"):
                opp_val = getattr(old_value, "families_FamilyRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_FamilyRegister"):
                opp_val = getattr(value, "families_FamilyRegister", None)
                if opp_val is None:
                    setattr(value, "families_FamilyRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def familyDaughter(self):
        return self.__familyDaughter

    @familyDaughter.setter
    def familyDaughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__familyDaughter", None)
        self.__familyDaughter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member3"):
                    opp_val = getattr(item, "Member3", None)
                    
                    if opp_val == self:
                        setattr(item, "Member3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member3"):
                    opp_val = getattr(item, "Member3", None)
                    
                    setattr(item, "Member3", self)
                    

    @property
    def Family12(self):
        return self.__Family12

    @Family12.setter
    def Family12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family12", None)
        self.__Family12 = value
        
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

class families_FamilyRegister:

    def __init__(self, id: str, families_FamilyRegister: set["families_Family"] = None):
        self.id = id
        self.families_FamilyRegister = families_FamilyRegister if families_FamilyRegister is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def families_FamilyRegister(self):
        return self.__families_FamilyRegister

    @families_FamilyRegister.setter
    def families_FamilyRegister(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_FamilyRegister__families_FamilyRegister", None)
        self.__families_FamilyRegister = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Family"):
                    opp_val = getattr(item, "families_Family", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Family", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Family"):
                    opp_val = getattr(item, "families_Family", None)
                    
                    setattr(item, "families_Family", self)
                    

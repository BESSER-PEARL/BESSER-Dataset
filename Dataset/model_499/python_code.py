from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class families_Member:

    def __init__(self, firstName: str, age: int, Member4: "families_Family" = None, Member6: "families_Family" = None, father: "families_Family" = None, mother: "families_Family" = None, sons: "families_Family" = None, daughters: "families_Family" = None, members: "families_FamilyModel" = None, Member: "families_Family" = None, Member2: "families_Family" = None, Member21: "families_FamilyModel" = None):
        self.firstName = firstName
        self.age = age
        self.Member4 = Member4
        self.Member6 = Member6
        self.father = father
        self.mother = mother
        self.sons = sons
        self.daughters = daughters
        self.members = members
        self.Member = Member
        self.Member2 = Member2
        self.Member21 = Member21
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

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
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member", None)
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
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__daughters", None)
        self.__daughters = value
        
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
    def Member2(self):
        return self.__Member2

    @Member2.setter
    def Member2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member2", None)
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
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__father", None)
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
    def Member21(self):
        return self.__Member21

    @Member21.setter
    def Member21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member21", None)
        self.__Member21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model20"):
                opp_val = getattr(old_value, "model20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model20"):
                opp_val = getattr(value, "model20", None)
                if opp_val is None:
                    setattr(value, "model20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Member6(self):
        return self.__Member6

    @Member6.setter
    def Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__Member6", None)
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
        old_value = getattr(self, f"_families_Member__Member4", None)
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

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyModel16"):
                opp_val = getattr(old_value, "FamilyModel16", None)
                if opp_val == self:
                    setattr(old_value, "FamilyModel16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyModel16"):
                opp_val = getattr(value, "FamilyModel16", None)
                setattr(value, "FamilyModel16", self)

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
            if hasattr(old_value, "Family12"):
                opp_val = getattr(old_value, "Family12", None)
                if opp_val == self:
                    setattr(old_value, "Family12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family12"):
                opp_val = getattr(value, "Family12", None)
                setattr(value, "Family12", self)

class families_Family:

    def __init__(self, lastName: str, street: str, town: str, familySon: set["families_Member"] = None, familyDaughter: set["families_Member"] = None, families: "families_FamilyModel" = None, Family: "families_Member" = None, Family10: "families_Member" = None, Family12: "families_Member" = None, Family14: "families_Member" = None, Family18: "families_FamilyModel" = None, familyFather: "families_Member" = None, familyMother: "families_Member" = None):
        self.lastName = lastName
        self.street = street
        self.town = town
        self.familySon = familySon if familySon is not None else set()
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        self.families = families
        self.Family = Family
        self.Family10 = Family10
        self.Family12 = Family12
        self.Family14 = Family14
        self.Family18 = Family18
        self.familyFather = familyFather
        self.familyMother = familyMother
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def town(self) -> str:
        return self.__town

    @town.setter
    def town(self, town: str):
        self.__town = town

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
    def Family10(self):
        return self.__Family10

    @Family10.setter
    def Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family10", None)
        self.__Family10 = value
        
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
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyModel"):
                opp_val = getattr(old_value, "FamilyModel", None)
                if opp_val == self:
                    setattr(old_value, "FamilyModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyModel"):
                opp_val = getattr(value, "FamilyModel", None)
                setattr(value, "FamilyModel", self)

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
        old_value = getattr(self, f"_families_Family__familyMother", None)
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
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family", None)
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
    def Family18(self):
        return self.__Family18

    @Family18.setter
    def Family18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family18", None)
        self.__Family18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
        old_value = getattr(self, f"_families_Family__familyDaughter", None)
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
                    

class families_FamilyModel:

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Families_FamilyMember:

    def __init__(self, name: str, FamilyMember: "Families_Family" = None, FamilyMember5: "Families_Family" = None, FamilyMember7: "Families_Family" = None, father: "Families_Family" = None, mother: "Families_Family" = None, sons: "Families_Family" = None, daughters: "Families_Family" = None, FamilyMember3: "Families_Family" = None):
        self.name = name
        self.FamilyMember = FamilyMember
        self.FamilyMember5 = FamilyMember5
        self.FamilyMember7 = FamilyMember7
        self.father = father
        self.mother = mother
        self.sons = sons
        self.daughters = daughters
        self.FamilyMember3 = FamilyMember3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FamilyMember7(self):
        return self.__FamilyMember7

    @FamilyMember7.setter
    def FamilyMember7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__FamilyMember7", None)
        self.__FamilyMember7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daughtersInverse"):
                opp_val = getattr(old_value, "daughtersInverse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daughtersInverse"):
                opp_val = getattr(value, "daughtersInverse", None)
                if opp_val is None:
                    setattr(value, "daughtersInverse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FamilyMember5(self):
        return self.__FamilyMember5

    @FamilyMember5.setter
    def FamilyMember5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__FamilyMember5", None)
        self.__FamilyMember5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sonsInverse"):
                opp_val = getattr(old_value, "sonsInverse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sonsInverse"):
                opp_val = getattr(value, "sonsInverse", None)
                if opp_val is None:
                    setattr(value, "sonsInverse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__father", None)
        self.__father = value
        
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
    def FamilyMember3(self):
        return self.__FamilyMember3

    @FamilyMember3.setter
    def FamilyMember3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__FamilyMember3", None)
        self.__FamilyMember3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "motherInverse"):
                opp_val = getattr(old_value, "motherInverse", None)
                if opp_val == self:
                    setattr(old_value, "motherInverse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "motherInverse"):
                opp_val = getattr(value, "motherInverse", None)
                setattr(value, "motherInverse", self)

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__mother", None)
        self.__mother = value
        
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
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__daughters", None)
        self.__daughters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family16"):
                opp_val = getattr(old_value, "Family16", None)
                if opp_val == self:
                    setattr(old_value, "Family16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family16"):
                opp_val = getattr(value, "Family16", None)
                setattr(value, "Family16", self)

    @property
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__sons", None)
        self.__sons = value
        
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
    def FamilyMember(self):
        return self.__FamilyMember

    @FamilyMember.setter
    def FamilyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__FamilyMember", None)
        self.__FamilyMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fatherInverse"):
                opp_val = getattr(old_value, "fatherInverse", None)
                if opp_val == self:
                    setattr(old_value, "fatherInverse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fatherInverse"):
                opp_val = getattr(value, "fatherInverse", None)
                setattr(value, "fatherInverse", self)

class Families_Family:

    def __init__(self, name: str, Family: "Families_FamilyRegister" = None, sonsInverse: set["Families_FamilyMember"] = None, daughtersInverse: set["Families_FamilyMember"] = None, families: "Families_FamilyRegister" = None, Family10: "Families_FamilyMember" = None, Family12: "Families_FamilyMember" = None, Family14: "Families_FamilyMember" = None, Family16: "Families_FamilyMember" = None, fatherInverse: "Families_FamilyMember" = None, motherInverse: "Families_FamilyMember" = None):
        self.name = name
        self.Family = Family
        self.sonsInverse = sonsInverse if sonsInverse is not None else set()
        self.daughtersInverse = daughtersInverse if daughtersInverse is not None else set()
        self.families = families
        self.Family10 = Family10
        self.Family12 = Family12
        self.Family14 = Family14
        self.Family16 = Family16
        self.fatherInverse = fatherInverse
        self.motherInverse = motherInverse
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def motherInverse(self):
        return self.__motherInverse

    @motherInverse.setter
    def motherInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__motherInverse", None)
        self.__motherInverse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyMember3"):
                opp_val = getattr(old_value, "FamilyMember3", None)
                if opp_val == self:
                    setattr(old_value, "FamilyMember3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyMember3"):
                opp_val = getattr(value, "FamilyMember3", None)
                setattr(value, "FamilyMember3", self)

    @property
    def Family16(self):
        return self.__Family16

    @Family16.setter
    def Family16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family16", None)
        self.__Family16 = value
        
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
        old_value = getattr(self, f"_Families_Family__Family14", None)
        self.__Family14 = value
        
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
    def sonsInverse(self):
        return self.__sonsInverse

    @sonsInverse.setter
    def sonsInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__sonsInverse", None)
        self.__sonsInverse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyMember5"):
                    opp_val = getattr(item, "FamilyMember5", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyMember5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyMember5"):
                    opp_val = getattr(item, "FamilyMember5", None)
                    
                    setattr(item, "FamilyMember5", self)
                    

    @property
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister"):
                opp_val = getattr(old_value, "FamilyRegister", None)
                if opp_val == self:
                    setattr(old_value, "FamilyRegister", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister"):
                opp_val = getattr(value, "FamilyRegister", None)
                setattr(value, "FamilyRegister", self)

    @property
    def fatherInverse(self):
        return self.__fatherInverse

    @fatherInverse.setter
    def fatherInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__fatherInverse", None)
        self.__fatherInverse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyMember"):
                opp_val = getattr(old_value, "FamilyMember", None)
                if opp_val == self:
                    setattr(old_value, "FamilyMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyMember"):
                opp_val = getattr(value, "FamilyMember", None)
                setattr(value, "FamilyMember", self)

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
            if hasattr(old_value, "familiesInverse"):
                opp_val = getattr(old_value, "familiesInverse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familiesInverse"):
                opp_val = getattr(value, "familiesInverse", None)
                if opp_val is None:
                    setattr(value, "familiesInverse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Family12(self):
        return self.__Family12

    @Family12.setter
    def Family12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family12", None)
        self.__Family12 = value
        
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
    def daughtersInverse(self):
        return self.__daughtersInverse

    @daughtersInverse.setter
    def daughtersInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__daughtersInverse", None)
        self.__daughtersInverse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyMember7"):
                    opp_val = getattr(item, "FamilyMember7", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyMember7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyMember7"):
                    opp_val = getattr(item, "FamilyMember7", None)
                    
                    setattr(item, "FamilyMember7", self)
                    

    @property
    def Family10(self):
        return self.__Family10

    @Family10.setter
    def Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family10", None)
        self.__Family10 = value
        
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

class Families_FamilyRegister:

    pass
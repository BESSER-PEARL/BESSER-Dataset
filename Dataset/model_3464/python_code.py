from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class featureModel_Proposition:

    def __init__(self, nameA: str, nameRest: str, featureModel_Proposition: "featureModel_PropFormula" = None, featureModel_Proposition13: "featureModel_PropFormula" = None):
        self.nameA = nameA
        self.nameRest = nameRest
        self.featureModel_Proposition = featureModel_Proposition
        self.featureModel_Proposition13 = featureModel_Proposition13
        
    @property
    def nameA(self) -> str:
        return self.__nameA

    @nameA.setter
    def nameA(self, nameA: str):
        self.__nameA = nameA

    @property
    def nameRest(self) -> str:
        return self.__nameRest

    @nameRest.setter
    def nameRest(self, nameRest: str):
        self.__nameRest = nameRest

    @property
    def featureModel_Proposition(self):
        return self.__featureModel_Proposition

    @featureModel_Proposition.setter
    def featureModel_Proposition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Proposition__featureModel_Proposition", None)
        self.__featureModel_Proposition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_PropFormula10"):
                opp_val = getattr(old_value, "featureModel_PropFormula10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_PropFormula10"):
                opp_val = getattr(value, "featureModel_PropFormula10", None)
                if opp_val is None:
                    setattr(value, "featureModel_PropFormula10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Proposition13(self):
        return self.__featureModel_Proposition13

    @featureModel_Proposition13.setter
    def featureModel_Proposition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Proposition__featureModel_Proposition13", None)
        self.__featureModel_Proposition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_PropFormula12"):
                opp_val = getattr(old_value, "featureModel_PropFormula12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_PropFormula12"):
                opp_val = getattr(value, "featureModel_PropFormula12", None)
                if opp_val is None:
                    setattr(value, "featureModel_PropFormula12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Constraint:

    pass
class featureModel_ExcludeConstraint(Constraint):

    pass
class featureModel_ImplyConstraint(Constraint):

    pass
class featureModel_Constraint:

    def __init__(self, nameA: str, nameB: str, featureModel_Constraint: "featureModel_Constraints" = None):
        self.nameA = nameA
        self.nameB = nameB
        self.featureModel_Constraint = featureModel_Constraint
        
    @property
    def nameB(self) -> str:
        return self.__nameB

    @nameB.setter
    def nameB(self, nameB: str):
        self.__nameB = nameB

    @property
    def nameA(self) -> str:
        return self.__nameA

    @nameA.setter
    def nameA(self, nameA: str):
        self.__nameA = nameA

    @property
    def featureModel_Constraint(self):
        return self.__featureModel_Constraint

    @featureModel_Constraint.setter
    def featureModel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Constraint__featureModel_Constraint", None)
        self.__featureModel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Constraints8"):
                opp_val = getattr(old_value, "featureModel_Constraints8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Constraints8"):
                opp_val = getattr(value, "featureModel_Constraints8", None)
                if opp_val is None:
                    setattr(value, "featureModel_Constraints8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featureModel_Group:

    pass
class Group:

    pass
class featureModel_PropFormula:

    pass
class featureModel_Constraints:

    pass
class featureModel_Feature(Group):

    def __init__(self, name: str, featureModel_Feature: "featureModel_FeatureModel" = None, featureModel_Feature6: set["featureModel_Group"] = None):
        self.name = name
        self.featureModel_Feature = featureModel_Feature
        self.featureModel_Feature6 = featureModel_Feature6 if featureModel_Feature6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureModel_Feature(self):
        return self.__featureModel_Feature

    @featureModel_Feature.setter
    def featureModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature", None)
        self.__featureModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_FeatureModel"):
                opp_val = getattr(old_value, "featureModel_FeatureModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_FeatureModel"):
                opp_val = getattr(value, "featureModel_FeatureModel", None)
                if opp_val is None:
                    setattr(value, "featureModel_FeatureModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature6(self):
        return self.__featureModel_Feature6

    @featureModel_Feature6.setter
    def featureModel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature6", None)
        self.__featureModel_Feature6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Group"):
                    opp_val = getattr(item, "featureModel_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Group"):
                    opp_val = getattr(item, "featureModel_Group", None)
                    
                    setattr(item, "featureModel_Group", self)
                    

class featureModel_FeatureModel:

    pass
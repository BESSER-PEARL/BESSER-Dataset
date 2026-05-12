from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RequirementSet:

    pass
class reqSpec_GlobalRequirementSet(RequirementSet):

    pass
class reqSpec_SystemRequirementSet(RequirementSet):

    pass
class ReqPredicate:

    pass
class reqSpec_Predicate(ReqPredicate):

    pass
class reqSpec_InformalPredicate(ReqPredicate):

    def __init__(self, description: str):
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class reqSpec_AVariableReference:

    pass
class reqSpec_DesiredValue:

    def __init__(self, upto: bool, reqSpec_DesiredValue: "reqSpec_ValuePredicate" = None, reqSpec_DesiredValue107: "reqSpec_AVariableReference" = None, reqSpec_DesiredValue109: "reqSpec_PropertyExpression" = None):
        self.upto = upto
        self.reqSpec_DesiredValue = reqSpec_DesiredValue
        self.reqSpec_DesiredValue107 = reqSpec_DesiredValue107
        self.reqSpec_DesiredValue109 = reqSpec_DesiredValue109
        
        pass
    @property
    def upto(self):
        return self.__upto

    @upto.setter
    def upto(self, upto: bool):
        self.__upto = upto


    @property
    def reqSpec_DesiredValue109(self):
        return self.__reqSpec_DesiredValue109

    @reqSpec_DesiredValue109.setter
    def reqSpec_DesiredValue109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_DesiredValue__reqSpec_DesiredValue109", None)
        self.__reqSpec_DesiredValue109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_PropertyExpression110"):
                opp_val = getattr(old_value, "reqSpec_PropertyExpression110", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_PropertyExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_PropertyExpression110"):
                opp_val = getattr(value, "reqSpec_PropertyExpression110", None)
                setattr(value, "reqSpec_PropertyExpression110", self)

    @property
    def reqSpec_DesiredValue107(self):
        return self.__reqSpec_DesiredValue107

    @reqSpec_DesiredValue107.setter
    def reqSpec_DesiredValue107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_DesiredValue__reqSpec_DesiredValue107", None)
        self.__reqSpec_DesiredValue107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_AVariableReference"):
                opp_val = getattr(old_value, "reqSpec_AVariableReference", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_AVariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_AVariableReference"):
                opp_val = getattr(value, "reqSpec_AVariableReference", None)
                setattr(value, "reqSpec_AVariableReference", self)

    @property
    def reqSpec_DesiredValue(self):
        return self.__reqSpec_DesiredValue

    @reqSpec_DesiredValue.setter
    def reqSpec_DesiredValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_DesiredValue__reqSpec_DesiredValue", None)
        self.__reqSpec_DesiredValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ValuePredicate105"):
                opp_val = getattr(old_value, "reqSpec_ValuePredicate105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ValuePredicate105"):
                opp_val = getattr(value, "reqSpec_ValuePredicate105", None)
                if opp_val is None:
                    setattr(value, "reqSpec_ValuePredicate105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reqSpec_ValuePredicate(ReqPredicate):

    pass
class reqSpec_PropertyExpression:

    pass
class reqSpec_ErrorBehaviorState:

    pass
class reqSpec_Mode:

    pass
class reqSpec_IncludeGlobalRequirement:

    def __init__(self, componentCategory: str, self1: bool, reqSpec_IncludeGlobalRequirement: "reqSpec_EObject" = None, reqSpec_IncludeGlobalRequirement115: "reqSpec_SystemRequirementSet" = None):
        self.componentCategory = componentCategory
        self.self1 = self1
        self.reqSpec_IncludeGlobalRequirement = reqSpec_IncludeGlobalRequirement
        self.reqSpec_IncludeGlobalRequirement115 = reqSpec_IncludeGlobalRequirement115
        
        pass
    @property
    def componentCategory(self):
        return self.__componentCategory

    @componentCategory.setter
    def componentCategory(self, componentCategory: str):
        self.__componentCategory = componentCategory


    @property
    def self1(self):
        return self.__self1

    @self1.setter
    def self1(self, self1: bool):
        self.__self1 = self1


    @property
    def reqSpec_IncludeGlobalRequirement115(self):
        return self.__reqSpec_IncludeGlobalRequirement115

    @reqSpec_IncludeGlobalRequirement115.setter
    def reqSpec_IncludeGlobalRequirement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_IncludeGlobalRequirement__reqSpec_IncludeGlobalRequirement115", None)
        self.__reqSpec_IncludeGlobalRequirement115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_SystemRequirementSet114"):
                opp_val = getattr(old_value, "reqSpec_SystemRequirementSet114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_SystemRequirementSet114"):
                opp_val = getattr(value, "reqSpec_SystemRequirementSet114", None)
                if opp_val is None:
                    setattr(value, "reqSpec_SystemRequirementSet114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_IncludeGlobalRequirement(self):
        return self.__reqSpec_IncludeGlobalRequirement

    @reqSpec_IncludeGlobalRequirement.setter
    def reqSpec_IncludeGlobalRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_IncludeGlobalRequirement__reqSpec_IncludeGlobalRequirement", None)
        self.__reqSpec_IncludeGlobalRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_EObject93"):
                opp_val = getattr(old_value, "reqSpec_EObject93", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_EObject93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_EObject93"):
                opp_val = getattr(value, "reqSpec_EObject93", None)
                setattr(value, "reqSpec_EObject93", self)

class reqSpec_ReqPredicate:

    pass
class reqSpec_Stakeholder:

    pass
class ContractualElement:

    pass
class reqSpec_DocumentSection:

    def __init__(self, label: str, title: str, reqSpec_DocumentSection: "reqSpec_Description" = None, reqSpec_DocumentSection45: set["reqSpec_EObject"] = None):
        self.label = label
        self.title = title
        self.reqSpec_DocumentSection = reqSpec_DocumentSection
        self.reqSpec_DocumentSection45 = reqSpec_DocumentSection45 if reqSpec_DocumentSection45 is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def reqSpec_DocumentSection(self):
        return self.__reqSpec_DocumentSection

    @reqSpec_DocumentSection.setter
    def reqSpec_DocumentSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_DocumentSection__reqSpec_DocumentSection", None)
        self.__reqSpec_DocumentSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Description43"):
                opp_val = getattr(old_value, "reqSpec_Description43", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Description43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Description43"):
                opp_val = getattr(value, "reqSpec_Description43", None)
                setattr(value, "reqSpec_Description43", self)

    @property
    def reqSpec_DocumentSection45(self):
        return self.__reqSpec_DocumentSection45

    @reqSpec_DocumentSection45.setter
    def reqSpec_DocumentSection45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_DocumentSection__reqSpec_DocumentSection45", None)
        self.__reqSpec_DocumentSection45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_EObject46"):
                    opp_val = getattr(item, "reqSpec_EObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_EObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_EObject46"):
                    opp_val = getattr(item, "reqSpec_EObject46", None)
                    
                    setattr(item, "reqSpec_EObject46", self)
                    

class reqSpec_Requirement(ContractualElement):

    def __init__(self, exceptionText: str, componentCategory: str, connections: bool, reqSpec_Requirement77: set["reqSpec_Requirement"] = None, reqSpec_Requirement57: "reqSpec_RequirementSet" = None, reqSpec_Requirement87: set["reqSpec_Stakeholder"] = None, reqSpec_Requirement91: "reqSpec_Requirement" = None, reqSpec_Requirement89: set["reqSpec_Requirement"] = None, reqSpec_Requirement: "reqSpec_ContractualElement" = None, reqSpec_Requirement70: set["reqSpec_AVariableDeclaration"] = None, reqSpec_Requirement73: "reqSpec_ReqPredicate" = None, reqSpec_Requirement75: "reqSpec_EObject" = None, reqSpec_Requirement79: "reqSpec_Requirement" = None, reqSpec_Requirement82: "reqSpec_Requirement" = None, reqSpec_Requirement80: set["reqSpec_Requirement"] = None, reqSpec_Requirement85: "reqSpec_Requirement" = None, reqSpec_Requirement83: "reqSpec_Requirement" = None):
        self.exceptionText = exceptionText
        self.componentCategory = componentCategory
        self.connections = connections
        self.reqSpec_Requirement77 = reqSpec_Requirement77 if reqSpec_Requirement77 is not None else set()
        self.reqSpec_Requirement57 = reqSpec_Requirement57
        self.reqSpec_Requirement87 = reqSpec_Requirement87 if reqSpec_Requirement87 is not None else set()
        self.reqSpec_Requirement91 = reqSpec_Requirement91
        self.reqSpec_Requirement89 = reqSpec_Requirement89 if reqSpec_Requirement89 is not None else set()
        self.reqSpec_Requirement = reqSpec_Requirement
        self.reqSpec_Requirement70 = reqSpec_Requirement70 if reqSpec_Requirement70 is not None else set()
        self.reqSpec_Requirement73 = reqSpec_Requirement73
        self.reqSpec_Requirement75 = reqSpec_Requirement75
        self.reqSpec_Requirement79 = reqSpec_Requirement79
        self.reqSpec_Requirement82 = reqSpec_Requirement82
        self.reqSpec_Requirement80 = reqSpec_Requirement80 if reqSpec_Requirement80 is not None else set()
        self.reqSpec_Requirement85 = reqSpec_Requirement85
        self.reqSpec_Requirement83 = reqSpec_Requirement83
        
        pass
    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, connections: bool):
        self.__connections = connections


    @property
    def componentCategory(self):
        return self.__componentCategory

    @componentCategory.setter
    def componentCategory(self, componentCategory: str):
        self.__componentCategory = componentCategory


    @property
    def exceptionText(self):
        return self.__exceptionText

    @exceptionText.setter
    def exceptionText(self, exceptionText: str):
        self.__exceptionText = exceptionText


    @property
    def reqSpec_Requirement87(self):
        return self.__reqSpec_Requirement87

    @reqSpec_Requirement87.setter
    def reqSpec_Requirement87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement87", None)
        self.__reqSpec_Requirement87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Stakeholder88"):
                    opp_val = getattr(item, "reqSpec_Stakeholder88", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Stakeholder88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Stakeholder88"):
                    opp_val = getattr(item, "reqSpec_Stakeholder88", None)
                    
                    setattr(item, "reqSpec_Stakeholder88", self)
                    

    @property
    def reqSpec_Requirement77(self):
        return self.__reqSpec_Requirement77

    @reqSpec_Requirement77.setter
    def reqSpec_Requirement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement77", None)
        self.__reqSpec_Requirement77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Requirement79"):
                    opp_val = getattr(item, "reqSpec_Requirement79", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Requirement79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Requirement79"):
                    opp_val = getattr(item, "reqSpec_Requirement79", None)
                    
                    setattr(item, "reqSpec_Requirement79", self)
                    

    @property
    def reqSpec_Requirement73(self):
        return self.__reqSpec_Requirement73

    @reqSpec_Requirement73.setter
    def reqSpec_Requirement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement73", None)
        self.__reqSpec_Requirement73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ReqPredicate"):
                opp_val = getattr(old_value, "reqSpec_ReqPredicate", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_ReqPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ReqPredicate"):
                opp_val = getattr(value, "reqSpec_ReqPredicate", None)
                setattr(value, "reqSpec_ReqPredicate", self)

    @property
    def reqSpec_Requirement82(self):
        return self.__reqSpec_Requirement82

    @reqSpec_Requirement82.setter
    def reqSpec_Requirement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement82", None)
        self.__reqSpec_Requirement82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Requirement80"):
                opp_val = getattr(old_value, "reqSpec_Requirement80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Requirement80"):
                opp_val = getattr(value, "reqSpec_Requirement80", None)
                if opp_val is None:
                    setattr(value, "reqSpec_Requirement80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_Requirement85(self):
        return self.__reqSpec_Requirement85

    @reqSpec_Requirement85.setter
    def reqSpec_Requirement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement85", None)
        self.__reqSpec_Requirement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Requirement83"):
                opp_val = getattr(old_value, "reqSpec_Requirement83", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Requirement83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Requirement83"):
                opp_val = getattr(value, "reqSpec_Requirement83", None)
                setattr(value, "reqSpec_Requirement83", self)

    @property
    def reqSpec_Requirement70(self):
        return self.__reqSpec_Requirement70

    @reqSpec_Requirement70.setter
    def reqSpec_Requirement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement70", None)
        self.__reqSpec_Requirement70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_AVariableDeclaration71"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration71", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_AVariableDeclaration71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_AVariableDeclaration71"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration71", None)
                    
                    setattr(item, "reqSpec_AVariableDeclaration71", self)
                    

    @property
    def reqSpec_Requirement80(self):
        return self.__reqSpec_Requirement80

    @reqSpec_Requirement80.setter
    def reqSpec_Requirement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement80", None)
        self.__reqSpec_Requirement80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Requirement82"):
                    opp_val = getattr(item, "reqSpec_Requirement82", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Requirement82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Requirement82"):
                    opp_val = getattr(item, "reqSpec_Requirement82", None)
                    
                    setattr(item, "reqSpec_Requirement82", self)
                    

    @property
    def reqSpec_Requirement75(self):
        return self.__reqSpec_Requirement75

    @reqSpec_Requirement75.setter
    def reqSpec_Requirement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement75", None)
        self.__reqSpec_Requirement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_EObject76"):
                opp_val = getattr(old_value, "reqSpec_EObject76", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_EObject76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_EObject76"):
                opp_val = getattr(value, "reqSpec_EObject76", None)
                setattr(value, "reqSpec_EObject76", self)

    @property
    def reqSpec_Requirement(self):
        return self.__reqSpec_Requirement

    @reqSpec_Requirement.setter
    def reqSpec_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement", None)
        self.__reqSpec_Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ContractualElement19"):
                opp_val = getattr(old_value, "reqSpec_ContractualElement19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ContractualElement19"):
                opp_val = getattr(value, "reqSpec_ContractualElement19", None)
                if opp_val is None:
                    setattr(value, "reqSpec_ContractualElement19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_Requirement79(self):
        return self.__reqSpec_Requirement79

    @reqSpec_Requirement79.setter
    def reqSpec_Requirement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement79", None)
        self.__reqSpec_Requirement79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Requirement77"):
                opp_val = getattr(old_value, "reqSpec_Requirement77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Requirement77"):
                opp_val = getattr(value, "reqSpec_Requirement77", None)
                if opp_val is None:
                    setattr(value, "reqSpec_Requirement77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_Requirement57(self):
        return self.__reqSpec_Requirement57

    @reqSpec_Requirement57.setter
    def reqSpec_Requirement57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement57", None)
        self.__reqSpec_Requirement57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_RequirementSet56"):
                opp_val = getattr(old_value, "reqSpec_RequirementSet56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_RequirementSet56"):
                opp_val = getattr(value, "reqSpec_RequirementSet56", None)
                if opp_val is None:
                    setattr(value, "reqSpec_RequirementSet56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_Requirement91(self):
        return self.__reqSpec_Requirement91

    @reqSpec_Requirement91.setter
    def reqSpec_Requirement91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement91", None)
        self.__reqSpec_Requirement91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Requirement89"):
                opp_val = getattr(old_value, "reqSpec_Requirement89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Requirement89"):
                opp_val = getattr(value, "reqSpec_Requirement89", None)
                if opp_val is None:
                    setattr(value, "reqSpec_Requirement89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_Requirement89(self):
        return self.__reqSpec_Requirement89

    @reqSpec_Requirement89.setter
    def reqSpec_Requirement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement89", None)
        self.__reqSpec_Requirement89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Requirement91"):
                    opp_val = getattr(item, "reqSpec_Requirement91", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Requirement91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Requirement91"):
                    opp_val = getattr(item, "reqSpec_Requirement91", None)
                    
                    setattr(item, "reqSpec_Requirement91", self)
                    

    @property
    def reqSpec_Requirement83(self):
        return self.__reqSpec_Requirement83

    @reqSpec_Requirement83.setter
    def reqSpec_Requirement83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_Requirement__reqSpec_Requirement83", None)
        self.__reqSpec_Requirement83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Requirement85"):
                opp_val = getattr(old_value, "reqSpec_Requirement85", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Requirement85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Requirement85"):
                opp_val = getattr(value, "reqSpec_Requirement85", None)
                setattr(value, "reqSpec_Requirement85", self)

class reqSpec_Uncertainty:

    pass
class ReqRoot:

    pass
class reqSpec_ReqDocument(ReqRoot):

    pass
class reqSpec_RequirementSet(ReqRoot):

    pass
class reqSpec_StakeholderGoals(ReqRoot):

    def __init__(self, componentCategory: str, reqSpec_StakeholderGoals35: set["reqSpec_AVariableDeclaration"] = None, reqSpec_StakeholderGoals38: set["reqSpec_Goal"] = None, reqSpec_StakeholderGoals: "reqSpec_ComponentClassifier" = None, reqSpec_StakeholderGoals32: set["reqSpec_GlobalConstants"] = None):
        self.componentCategory = componentCategory
        self.reqSpec_StakeholderGoals35 = reqSpec_StakeholderGoals35 if reqSpec_StakeholderGoals35 is not None else set()
        self.reqSpec_StakeholderGoals38 = reqSpec_StakeholderGoals38 if reqSpec_StakeholderGoals38 is not None else set()
        self.reqSpec_StakeholderGoals = reqSpec_StakeholderGoals
        self.reqSpec_StakeholderGoals32 = reqSpec_StakeholderGoals32 if reqSpec_StakeholderGoals32 is not None else set()
        
        pass
    @property
    def componentCategory(self):
        return self.__componentCategory

    @componentCategory.setter
    def componentCategory(self, componentCategory: str):
        self.__componentCategory = componentCategory


    @property
    def reqSpec_StakeholderGoals32(self):
        return self.__reqSpec_StakeholderGoals32

    @reqSpec_StakeholderGoals32.setter
    def reqSpec_StakeholderGoals32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_StakeholderGoals__reqSpec_StakeholderGoals32", None)
        self.__reqSpec_StakeholderGoals32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_GlobalConstants33"):
                    opp_val = getattr(item, "reqSpec_GlobalConstants33", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_GlobalConstants33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_GlobalConstants33"):
                    opp_val = getattr(item, "reqSpec_GlobalConstants33", None)
                    
                    setattr(item, "reqSpec_GlobalConstants33", self)
                    

    @property
    def reqSpec_StakeholderGoals(self):
        return self.__reqSpec_StakeholderGoals

    @reqSpec_StakeholderGoals.setter
    def reqSpec_StakeholderGoals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_StakeholderGoals__reqSpec_StakeholderGoals", None)
        self.__reqSpec_StakeholderGoals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ComponentClassifier30"):
                opp_val = getattr(old_value, "reqSpec_ComponentClassifier30", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_ComponentClassifier30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ComponentClassifier30"):
                opp_val = getattr(value, "reqSpec_ComponentClassifier30", None)
                setattr(value, "reqSpec_ComponentClassifier30", self)

    @property
    def reqSpec_StakeholderGoals35(self):
        return self.__reqSpec_StakeholderGoals35

    @reqSpec_StakeholderGoals35.setter
    def reqSpec_StakeholderGoals35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_StakeholderGoals__reqSpec_StakeholderGoals35", None)
        self.__reqSpec_StakeholderGoals35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_AVariableDeclaration36"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration36", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_AVariableDeclaration36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_AVariableDeclaration36"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration36", None)
                    
                    setattr(item, "reqSpec_AVariableDeclaration36", self)
                    

    @property
    def reqSpec_StakeholderGoals38(self):
        return self.__reqSpec_StakeholderGoals38

    @reqSpec_StakeholderGoals38.setter
    def reqSpec_StakeholderGoals38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_StakeholderGoals__reqSpec_StakeholderGoals38", None)
        self.__reqSpec_StakeholderGoals38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Goal39"):
                    opp_val = getattr(item, "reqSpec_Goal39", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Goal39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Goal39"):
                    opp_val = getattr(item, "reqSpec_Goal39", None)
                    
                    setattr(item, "reqSpec_Goal39", self)
                    

class reqSpec_ReqRoot:

    def __init__(self, name: str, title: str, issues: str, reqSpec_ReqRoot60: "reqSpec_RequirementSet" = None, reqSpec_ReqRoot: "reqSpec_Description" = None, reqSpec_ReqRoot27: set["reqSpec_ExternalDocument"] = None):
        self.name = name
        self.title = title
        self.issues = issues
        self.reqSpec_ReqRoot60 = reqSpec_ReqRoot60
        self.reqSpec_ReqRoot = reqSpec_ReqRoot
        self.reqSpec_ReqRoot27 = reqSpec_ReqRoot27 if reqSpec_ReqRoot27 is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def issues(self):
        return self.__issues

    @issues.setter
    def issues(self, issues: str):
        self.__issues = issues


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def reqSpec_ReqRoot60(self):
        return self.__reqSpec_ReqRoot60

    @reqSpec_ReqRoot60.setter
    def reqSpec_ReqRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ReqRoot__reqSpec_ReqRoot60", None)
        self.__reqSpec_ReqRoot60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_RequirementSet59"):
                opp_val = getattr(old_value, "reqSpec_RequirementSet59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_RequirementSet59"):
                opp_val = getattr(value, "reqSpec_RequirementSet59", None)
                if opp_val is None:
                    setattr(value, "reqSpec_RequirementSet59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_ReqRoot27(self):
        return self.__reqSpec_ReqRoot27

    @reqSpec_ReqRoot27.setter
    def reqSpec_ReqRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ReqRoot__reqSpec_ReqRoot27", None)
        self.__reqSpec_ReqRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_ExternalDocument28"):
                    opp_val = getattr(item, "reqSpec_ExternalDocument28", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_ExternalDocument28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_ExternalDocument28"):
                    opp_val = getattr(item, "reqSpec_ExternalDocument28", None)
                    
                    setattr(item, "reqSpec_ExternalDocument28", self)
                    

    @property
    def reqSpec_ReqRoot(self):
        return self.__reqSpec_ReqRoot

    @reqSpec_ReqRoot.setter
    def reqSpec_ReqRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ReqRoot__reqSpec_ReqRoot", None)
        self.__reqSpec_ReqRoot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Description25"):
                opp_val = getattr(old_value, "reqSpec_Description25", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Description25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Description25"):
                opp_val = getattr(value, "reqSpec_Description25", None)
                setattr(value, "reqSpec_Description25", self)

class reqSpec_Goal(ContractualElement):

    pass
class reqSpec_ExternalDocument:

    def __init__(self, docReference: str, docFragment: str, reqSpec_ExternalDocument: "reqSpec_ContractualElement" = None, reqSpec_ExternalDocument28: "reqSpec_ReqRoot" = None):
        self.docReference = docReference
        self.docFragment = docFragment
        self.reqSpec_ExternalDocument = reqSpec_ExternalDocument
        self.reqSpec_ExternalDocument28 = reqSpec_ExternalDocument28
        
        pass
    @property
    def docFragment(self):
        return self.__docFragment

    @docFragment.setter
    def docFragment(self, docFragment: str):
        self.__docFragment = docFragment


    @property
    def docReference(self):
        return self.__docReference

    @docReference.setter
    def docReference(self, docReference: str):
        self.__docReference = docReference


    @property
    def reqSpec_ExternalDocument(self):
        return self.__reqSpec_ExternalDocument

    @reqSpec_ExternalDocument.setter
    def reqSpec_ExternalDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ExternalDocument__reqSpec_ExternalDocument", None)
        self.__reqSpec_ExternalDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ContractualElement21"):
                opp_val = getattr(old_value, "reqSpec_ContractualElement21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ContractualElement21"):
                opp_val = getattr(value, "reqSpec_ContractualElement21", None)
                if opp_val is None:
                    setattr(value, "reqSpec_ContractualElement21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_ExternalDocument28(self):
        return self.__reqSpec_ExternalDocument28

    @reqSpec_ExternalDocument28.setter
    def reqSpec_ExternalDocument28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ExternalDocument__reqSpec_ExternalDocument28", None)
        self.__reqSpec_ExternalDocument28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ReqRoot27"):
                opp_val = getattr(old_value, "reqSpec_ReqRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ReqRoot27"):
                opp_val = getattr(value, "reqSpec_ReqRoot27", None)
                if opp_val is None:
                    setattr(value, "reqSpec_ReqRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reqSpec_ContractualElement:

    def __init__(self, name: str, title: str, targetDescription: str, dropped: bool, dropRationale: str, issues: str, reqSpec_ContractualElement: "reqSpec_ComponentClassifier" = None, reqSpec_ContractualElement4: "reqSpec_NamedElement" = None, reqSpec_ContractualElement6: set["reqSpec_Category"] = None, reqSpec_ContractualElement8: "reqSpec_Description" = None, reqSpec_ContractualElement10: set["reqSpec_AVariableDeclaration"] = None, reqSpec_ContractualElement13: "reqSpec_WhenCondition" = None, reqSpec_ContractualElement15: "reqSpec_Rationale" = None, reqSpec_ContractualElement21: set["reqSpec_ExternalDocument"] = None, reqSpec_ContractualElement23: set["reqSpec_Goal"] = None, reqSpec_ContractualElement17: "reqSpec_Uncertainty" = None, reqSpec_ContractualElement19: set["reqSpec_Requirement"] = None):
        self.name = name
        self.title = title
        self.targetDescription = targetDescription
        self.dropped = dropped
        self.dropRationale = dropRationale
        self.issues = issues
        self.reqSpec_ContractualElement = reqSpec_ContractualElement
        self.reqSpec_ContractualElement4 = reqSpec_ContractualElement4
        self.reqSpec_ContractualElement6 = reqSpec_ContractualElement6 if reqSpec_ContractualElement6 is not None else set()
        self.reqSpec_ContractualElement8 = reqSpec_ContractualElement8
        self.reqSpec_ContractualElement10 = reqSpec_ContractualElement10 if reqSpec_ContractualElement10 is not None else set()
        self.reqSpec_ContractualElement13 = reqSpec_ContractualElement13
        self.reqSpec_ContractualElement15 = reqSpec_ContractualElement15
        self.reqSpec_ContractualElement21 = reqSpec_ContractualElement21 if reqSpec_ContractualElement21 is not None else set()
        self.reqSpec_ContractualElement23 = reqSpec_ContractualElement23 if reqSpec_ContractualElement23 is not None else set()
        self.reqSpec_ContractualElement17 = reqSpec_ContractualElement17
        self.reqSpec_ContractualElement19 = reqSpec_ContractualElement19 if reqSpec_ContractualElement19 is not None else set()
        
        pass
    @property
    def dropped(self):
        return self.__dropped

    @dropped.setter
    def dropped(self, dropped: bool):
        self.__dropped = dropped


    @property
    def dropRationale(self):
        return self.__dropRationale

    @dropRationale.setter
    def dropRationale(self, dropRationale: str):
        self.__dropRationale = dropRationale


    @property
    def targetDescription(self):
        return self.__targetDescription

    @targetDescription.setter
    def targetDescription(self, targetDescription: str):
        self.__targetDescription = targetDescription


    @property
    def issues(self):
        return self.__issues

    @issues.setter
    def issues(self, issues: str):
        self.__issues = issues


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def reqSpec_ContractualElement(self):
        return self.__reqSpec_ContractualElement

    @reqSpec_ContractualElement.setter
    def reqSpec_ContractualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement", None)
        self.__reqSpec_ContractualElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_ComponentClassifier"):
                opp_val = getattr(old_value, "reqSpec_ComponentClassifier", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_ComponentClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_ComponentClassifier"):
                opp_val = getattr(value, "reqSpec_ComponentClassifier", None)
                setattr(value, "reqSpec_ComponentClassifier", self)

    @property
    def reqSpec_ContractualElement4(self):
        return self.__reqSpec_ContractualElement4

    @reqSpec_ContractualElement4.setter
    def reqSpec_ContractualElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement4", None)
        self.__reqSpec_ContractualElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_NamedElement"):
                opp_val = getattr(old_value, "reqSpec_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_NamedElement"):
                opp_val = getattr(value, "reqSpec_NamedElement", None)
                setattr(value, "reqSpec_NamedElement", self)

    @property
    def reqSpec_ContractualElement8(self):
        return self.__reqSpec_ContractualElement8

    @reqSpec_ContractualElement8.setter
    def reqSpec_ContractualElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement8", None)
        self.__reqSpec_ContractualElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Description"):
                opp_val = getattr(old_value, "reqSpec_Description", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Description"):
                opp_val = getattr(value, "reqSpec_Description", None)
                setattr(value, "reqSpec_Description", self)

    @property
    def reqSpec_ContractualElement13(self):
        return self.__reqSpec_ContractualElement13

    @reqSpec_ContractualElement13.setter
    def reqSpec_ContractualElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement13", None)
        self.__reqSpec_ContractualElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_WhenCondition"):
                opp_val = getattr(old_value, "reqSpec_WhenCondition", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_WhenCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_WhenCondition"):
                opp_val = getattr(value, "reqSpec_WhenCondition", None)
                setattr(value, "reqSpec_WhenCondition", self)

    @property
    def reqSpec_ContractualElement10(self):
        return self.__reqSpec_ContractualElement10

    @reqSpec_ContractualElement10.setter
    def reqSpec_ContractualElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement10", None)
        self.__reqSpec_ContractualElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_AVariableDeclaration11"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration11", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_AVariableDeclaration11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_AVariableDeclaration11"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration11", None)
                    
                    setattr(item, "reqSpec_AVariableDeclaration11", self)
                    

    @property
    def reqSpec_ContractualElement17(self):
        return self.__reqSpec_ContractualElement17

    @reqSpec_ContractualElement17.setter
    def reqSpec_ContractualElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement17", None)
        self.__reqSpec_ContractualElement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Uncertainty"):
                opp_val = getattr(old_value, "reqSpec_Uncertainty", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Uncertainty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Uncertainty"):
                opp_val = getattr(value, "reqSpec_Uncertainty", None)
                setattr(value, "reqSpec_Uncertainty", self)

    @property
    def reqSpec_ContractualElement19(self):
        return self.__reqSpec_ContractualElement19

    @reqSpec_ContractualElement19.setter
    def reqSpec_ContractualElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement19", None)
        self.__reqSpec_ContractualElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Requirement"):
                    opp_val = getattr(item, "reqSpec_Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Requirement"):
                    opp_val = getattr(item, "reqSpec_Requirement", None)
                    
                    setattr(item, "reqSpec_Requirement", self)
                    

    @property
    def reqSpec_ContractualElement6(self):
        return self.__reqSpec_ContractualElement6

    @reqSpec_ContractualElement6.setter
    def reqSpec_ContractualElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement6", None)
        self.__reqSpec_ContractualElement6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Category"):
                    opp_val = getattr(item, "reqSpec_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Category"):
                    opp_val = getattr(item, "reqSpec_Category", None)
                    
                    setattr(item, "reqSpec_Category", self)
                    

    @property
    def reqSpec_ContractualElement15(self):
        return self.__reqSpec_ContractualElement15

    @reqSpec_ContractualElement15.setter
    def reqSpec_ContractualElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement15", None)
        self.__reqSpec_ContractualElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_Rationale"):
                opp_val = getattr(old_value, "reqSpec_Rationale", None)
                if opp_val == self:
                    setattr(old_value, "reqSpec_Rationale", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_Rationale"):
                opp_val = getattr(value, "reqSpec_Rationale", None)
                setattr(value, "reqSpec_Rationale", self)

    @property
    def reqSpec_ContractualElement23(self):
        return self.__reqSpec_ContractualElement23

    @reqSpec_ContractualElement23.setter
    def reqSpec_ContractualElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement23", None)
        self.__reqSpec_ContractualElement23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_Goal"):
                    opp_val = getattr(item, "reqSpec_Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_Goal"):
                    opp_val = getattr(item, "reqSpec_Goal", None)
                    
                    setattr(item, "reqSpec_Goal", self)
                    

    @property
    def reqSpec_ContractualElement21(self):
        return self.__reqSpec_ContractualElement21

    @reqSpec_ContractualElement21.setter
    def reqSpec_ContractualElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_ContractualElement__reqSpec_ContractualElement21", None)
        self.__reqSpec_ContractualElement21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_ExternalDocument"):
                    opp_val = getattr(item, "reqSpec_ExternalDocument", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_ExternalDocument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_ExternalDocument"):
                    opp_val = getattr(item, "reqSpec_ExternalDocument", None)
                    
                    setattr(item, "reqSpec_ExternalDocument", self)
                    

class reqSpec_AVariableDeclaration:

    pass
class reqSpec_Rationale:

    pass
class reqSpec_WhenCondition:

    pass
class reqSpec_Description:

    pass
class reqSpec_Category:

    pass
class reqSpec_NamedElement:

    pass
class reqSpec_ComponentClassifier:

    pass
class reqSpec_GlobalConstants:

    def __init__(self, name: str, reqSpec_GlobalConstants: set["reqSpec_AVariableDeclaration"] = None, reqSpec_GlobalConstants48: "reqSpec_RequirementSet" = None, reqSpec_GlobalConstants33: "reqSpec_StakeholderGoals" = None):
        self.name = name
        self.reqSpec_GlobalConstants = reqSpec_GlobalConstants if reqSpec_GlobalConstants is not None else set()
        self.reqSpec_GlobalConstants48 = reqSpec_GlobalConstants48
        self.reqSpec_GlobalConstants33 = reqSpec_GlobalConstants33
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def reqSpec_GlobalConstants48(self):
        return self.__reqSpec_GlobalConstants48

    @reqSpec_GlobalConstants48.setter
    def reqSpec_GlobalConstants48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_GlobalConstants__reqSpec_GlobalConstants48", None)
        self.__reqSpec_GlobalConstants48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_RequirementSet"):
                opp_val = getattr(old_value, "reqSpec_RequirementSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_RequirementSet"):
                opp_val = getattr(value, "reqSpec_RequirementSet", None)
                if opp_val is None:
                    setattr(value, "reqSpec_RequirementSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_GlobalConstants33(self):
        return self.__reqSpec_GlobalConstants33

    @reqSpec_GlobalConstants33.setter
    def reqSpec_GlobalConstants33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_GlobalConstants__reqSpec_GlobalConstants33", None)
        self.__reqSpec_GlobalConstants33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqSpec_StakeholderGoals32"):
                opp_val = getattr(old_value, "reqSpec_StakeholderGoals32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqSpec_StakeholderGoals32"):
                opp_val = getattr(value, "reqSpec_StakeholderGoals32", None)
                if opp_val is None:
                    setattr(value, "reqSpec_StakeholderGoals32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqSpec_GlobalConstants(self):
        return self.__reqSpec_GlobalConstants

    @reqSpec_GlobalConstants.setter
    def reqSpec_GlobalConstants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqSpec_GlobalConstants__reqSpec_GlobalConstants", None)
        self.__reqSpec_GlobalConstants = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reqSpec_AVariableDeclaration"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "reqSpec_AVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reqSpec_AVariableDeclaration"):
                    opp_val = getattr(item, "reqSpec_AVariableDeclaration", None)
                    
                    setattr(item, "reqSpec_AVariableDeclaration", self)
                    

class reqSpec_EObject:

    pass
class reqSpec_ReqSpec:

    pass
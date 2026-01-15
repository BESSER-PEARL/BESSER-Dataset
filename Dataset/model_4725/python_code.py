from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableKind(Enum):
    logicalVar = "logicalVar"
    locationVar = "locationVar"
    ruleVar = "ruleVar"


############################################
# Definition of Classes
############################################

class ComplexDomain:

    pass
class asmeta_domains_RealDomain(ComplexDomain):

    pass
class AbstractTd:

    pass
class asmeta_domains_AgentDomain(AbstractTd):

    pass
class asmeta_domains_ReserveDomain(AbstractTd):

    pass
class StructuredTd:

    pass
class asmeta_domains_BagDomain(StructuredTd):

    pass
class asmeta_domains_RuleDomain(StructuredTd):

    def __init__(self, domains: str):
        self.domains = domains
        
    @property
    def domains(self) -> str:
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains

class asmeta_domains_SequenceDomain(StructuredTd):

    pass
class TypeDomain:

    pass
class asmeta_domains_AbstractTd(TypeDomain):

    def __init__(self, isDynamic: str):
        self.isDynamic = isDynamic
        
    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

class asmeta_domains_AnyDomain(TypeDomain):

    pass
class asmeta_domains_BasicTd(TypeDomain):

    pass
class asmeta_domains_StructuredTd(TypeDomain):

    pass
class Domain:

    pass
class asmeta_domains_TypeDomain(Domain):

    pass
class BasicTd:

    pass
class asmeta_domains_StringDomain(BasicTd):

    pass
class asmeta_domains_ComplexDomain(BasicTd):

    pass
class asmeta_domains_CharDomain(BasicTd):

    pass
class asmeta_domains_BooleanDomain(BasicTd):

    pass
class asmeta_domains_UndefDomain(BasicTd):

    pass
class IntegerDomain:

    pass
class asmeta_domains_NaturalDomain(IntegerDomain):

    pass
class domains_TypeDomain:

    pass
class asmeta_domains_ConcreteDomain(Domain):

    def __init__(self, isDynamic: str, DomainInitialization309: set["DomainInitialization"] = None, DomainDefinition312: "DomainDefinition" = None, asmeta_domains_ConcreteDomain: "domains_TypeDomain" = None):
        self.isDynamic = isDynamic
        self.DomainInitialization309 = DomainInitialization309 if DomainInitialization309 is not None else set()
        self.DomainDefinition312 = DomainDefinition312
        self.asmeta_domains_ConcreteDomain = asmeta_domains_ConcreteDomain
        
    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def DomainDefinition312(self):
        return self.__DomainDefinition312

    @DomainDefinition312.setter
    def DomainDefinition312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__DomainDefinition312", None)
        self.__DomainDefinition312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure313"):
                opp_val = getattr(old_value, "structure313", None)
                if opp_val == self:
                    setattr(old_value, "structure313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure313"):
                opp_val = getattr(value, "structure313", None)
                setattr(value, "structure313", self)

    @property
    def asmeta_domains_ConcreteDomain(self):
        return self.__asmeta_domains_ConcreteDomain

    @asmeta_domains_ConcreteDomain.setter
    def asmeta_domains_ConcreteDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__asmeta_domains_ConcreteDomain", None)
        self.__asmeta_domains_ConcreteDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_TypeDomain"):
                opp_val = getattr(old_value, "domains_TypeDomain", None)
                if opp_val == self:
                    setattr(old_value, "domains_TypeDomain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_TypeDomain"):
                opp_val = getattr(value, "domains_TypeDomain", None)
                setattr(value, "domains_TypeDomain", self)

    @property
    def DomainInitialization309(self):
        return self.__DomainInitialization309

    @DomainInitialization309.setter
    def DomainInitialization309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__DomainInitialization309", None)
        self.__DomainInitialization309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure310"):
                    opp_val = getattr(item, "structure310", None)
                    
                    if opp_val == self:
                        setattr(item, "structure310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure310"):
                    opp_val = getattr(item, "structure310", None)
                    
                    setattr(item, "structure310", self)
                    

class asmeta_domains_EnumElement:

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class domains_EnumElement:

    pass
class asmeta_domains_EnumTd(TypeDomain):

    pass
class RealDomain:

    pass
class asmeta_domains_IntegerDomain(RealDomain):

    pass
class asmeta_domains_MapDomain(StructuredTd):

    pass
class asmeta_domains_PowersetDomain(StructuredTd):

    pass
class asmeta_domains_ProductDomain(StructuredTd):

    def __init__(self, domains: str):
        self.domains = domains
        
    @property
    def domains(self) -> str:
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains

class TemporalProperty:

    pass
class asmeta_definitions_LtlSpec(TemporalProperty):

    pass
class asmeta_definitions_CtlSpec(TemporalProperty):

    pass
class BasicFunction:

    pass
class asmeta_definitions_StaticFunction(BasicFunction):

    pass
class asmeta_definitions_DynamicFunction(BasicFunction):

    pass
class Invariant:

    pass
class Classifier:

    pass
class asmeta_definitions_FairnessConstraint(Classifier):

    pass
class asmeta_definitions_InvarConstraint(Classifier):

    pass
class asmeta_definitions_Function(Classifier):

    def __init__(self, arity: str, Invariant276: set["Invariant"] = None, Signature279: "Signature" = None, asmeta_definitions_Function: "domains_Domain" = None, asmeta_definitions_Function270: "domains_Domain" = None, FunctionDefinition273: "FunctionDefinition" = None):
        self.arity = arity
        self.Invariant276 = Invariant276 if Invariant276 is not None else set()
        self.Signature279 = Signature279
        self.asmeta_definitions_Function = asmeta_definitions_Function
        self.asmeta_definitions_Function270 = asmeta_definitions_Function270
        self.FunctionDefinition273 = FunctionDefinition273
        
    @property
    def arity(self) -> str:
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity

    @property
    def asmeta_definitions_Function(self):
        return self.__asmeta_definitions_Function

    @asmeta_definitions_Function.setter
    def asmeta_definitions_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__asmeta_definitions_Function", None)
        self.__asmeta_definitions_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_Domain268"):
                opp_val = getattr(old_value, "domains_Domain268", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain268"):
                opp_val = getattr(value, "domains_Domain268", None)
                setattr(value, "domains_Domain268", self)

    @property
    def FunctionDefinition273(self):
        return self.__FunctionDefinition273

    @FunctionDefinition273.setter
    def FunctionDefinition273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__FunctionDefinition273", None)
        self.__FunctionDefinition273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure274"):
                opp_val = getattr(old_value, "structure274", None)
                if opp_val == self:
                    setattr(old_value, "structure274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure274"):
                opp_val = getattr(value, "structure274", None)
                setattr(value, "structure274", self)

    @property
    def asmeta_definitions_Function270(self):
        return self.__asmeta_definitions_Function270

    @asmeta_definitions_Function270.setter
    def asmeta_definitions_Function270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__asmeta_definitions_Function270", None)
        self.__asmeta_definitions_Function270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_Domain271"):
                opp_val = getattr(old_value, "domains_Domain271", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain271"):
                opp_val = getattr(value, "domains_Domain271", None)
                setattr(value, "domains_Domain271", self)

    @property
    def Invariant276(self):
        return self.__Invariant276

    @Invariant276.setter
    def Invariant276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__Invariant276", None)
        self.__Invariant276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "definitions277"):
                    opp_val = getattr(item, "definitions277", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions277"):
                    opp_val = getattr(item, "definitions277", None)
                    
                    setattr(item, "definitions277", self)
                    

    @property
    def Signature279(self):
        return self.__Signature279

    @Signature279.setter
    def Signature279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__Signature279", None)
        self.__Signature279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure280"):
                opp_val = getattr(old_value, "structure280", None)
                if opp_val == self:
                    setattr(old_value, "structure280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure280"):
                opp_val = getattr(value, "structure280", None)
                setattr(value, "structure280", self)

class asmeta_domains_Domain(Classifier):

    def __init__(self, Invariant303: set["Invariant"] = None, Signature306: "Signature" = None):
        self.Invariant303 = Invariant303 if Invariant303 is not None else set()
        self.Signature306 = Signature306
        
    @property
    def Invariant303(self):
        return self.__Invariant303

    @Invariant303.setter
    def Invariant303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__Invariant303", None)
        self.__Invariant303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "definitions304"):
                    opp_val = getattr(item, "definitions304", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions304"):
                    opp_val = getattr(item, "definitions304", None)
                    
                    setattr(item, "definitions304", self)
                    

    @property
    def Signature306(self):
        return self.__Signature306

    @Signature306.setter
    def Signature306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__Signature306", None)
        self.__Signature306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure307"):
                opp_val = getattr(old_value, "structure307", None)
                if opp_val == self:
                    setattr(old_value, "structure307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure307"):
                opp_val = getattr(value, "structure307", None)
                setattr(value, "structure307", self)

    def compatible(self):
        # TODO: Implement compatible method
        pass

class asmeta_definitions_Property(Classifier):

    pass
class asmeta_definitions_RuleDeclaration(Classifier):

    def __init__(self, arity: str, asmeta_definitions_RuleDeclaration: set["basicterms_VariableTerm"] = None, Invariant: set["Invariant"] = None, asmeta_definitions_RuleDeclaration248: "basictransitionrules_Rule" = None, Body251: "Body" = None):
        self.arity = arity
        self.asmeta_definitions_RuleDeclaration = asmeta_definitions_RuleDeclaration if asmeta_definitions_RuleDeclaration is not None else set()
        self.Invariant = Invariant if Invariant is not None else set()
        self.asmeta_definitions_RuleDeclaration248 = asmeta_definitions_RuleDeclaration248
        self.Body251 = Body251
        
    @property
    def arity(self) -> str:
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity

    @property
    def Invariant(self):
        return self.__Invariant

    @Invariant.setter
    def Invariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__Invariant", None)
        self.__Invariant = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "definitions246"):
                    opp_val = getattr(item, "definitions246", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions246"):
                    opp_val = getattr(item, "definitions246", None)
                    
                    setattr(item, "definitions246", self)
                    

    @property
    def Body251(self):
        return self.__Body251

    @Body251.setter
    def Body251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__Body251", None)
        self.__Body251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure252"):
                opp_val = getattr(old_value, "structure252", None)
                if opp_val == self:
                    setattr(old_value, "structure252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure252"):
                opp_val = getattr(value, "structure252", None)
                setattr(value, "structure252", self)

    @property
    def asmeta_definitions_RuleDeclaration(self):
        return self.__asmeta_definitions_RuleDeclaration

    @asmeta_definitions_RuleDeclaration.setter
    def asmeta_definitions_RuleDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__asmeta_definitions_RuleDeclaration", None)
        self.__asmeta_definitions_RuleDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm244"):
                    opp_val = getattr(item, "basicterms_VariableTerm244", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm244"):
                    opp_val = getattr(item, "basicterms_VariableTerm244", None)
                    
                    setattr(item, "basicterms_VariableTerm244", self)
                    

    @property
    def asmeta_definitions_RuleDeclaration248(self):
        return self.__asmeta_definitions_RuleDeclaration248

    @asmeta_definitions_RuleDeclaration248.setter
    def asmeta_definitions_RuleDeclaration248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__asmeta_definitions_RuleDeclaration248", None)
        self.__asmeta_definitions_RuleDeclaration248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule249"):
                opp_val = getattr(old_value, "basictransitionrules_Rule249", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule249"):
                opp_val = getattr(value, "basictransitionrules_Rule249", None)
                setattr(value, "basictransitionrules_Rule249", self)

class BasicRule:

    pass
class asmeta_basictransitionrules_MacroCallRule(BasicRule):

    def __init__(self, parameters: str, asmeta_basictransitionrules_MacroCallRule: "basictransitionrules_MacroDeclaration" = None):
        self.parameters = parameters
        self.asmeta_basictransitionrules_MacroCallRule = asmeta_basictransitionrules_MacroCallRule
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def asmeta_basictransitionrules_MacroCallRule(self):
        return self.__asmeta_basictransitionrules_MacroCallRule

    @asmeta_basictransitionrules_MacroCallRule.setter
    def asmeta_basictransitionrules_MacroCallRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_MacroCallRule__asmeta_basictransitionrules_MacroCallRule", None)
        self.__asmeta_basictransitionrules_MacroCallRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_MacroDeclaration205"):
                opp_val = getattr(old_value, "basictransitionrules_MacroDeclaration205", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_MacroDeclaration205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_MacroDeclaration205"):
                opp_val = getattr(value, "basictransitionrules_MacroDeclaration205", None)
                setattr(value, "basictransitionrules_MacroDeclaration205", self)

class asmeta_basictransitionrules_UpdateRule(BasicRule):

    pass
class asmeta_basictransitionrules_SkipRule(BasicRule):

    pass
class asmeta_basictransitionrules_ChooseRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ChooseRule: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule196: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule199: "basicterms_Term" = None, asmeta_basictransitionrules_ChooseRule202: set["basicterms_VariableTerm"] = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ChooseRule = asmeta_basictransitionrules_ChooseRule
        self.asmeta_basictransitionrules_ChooseRule196 = asmeta_basictransitionrules_ChooseRule196
        self.asmeta_basictransitionrules_ChooseRule199 = asmeta_basictransitionrules_ChooseRule199
        self.asmeta_basictransitionrules_ChooseRule202 = asmeta_basictransitionrules_ChooseRule202 if asmeta_basictransitionrules_ChooseRule202 is not None else set()
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def asmeta_basictransitionrules_ChooseRule199(self):
        return self.__asmeta_basictransitionrules_ChooseRule199

    @asmeta_basictransitionrules_ChooseRule199.setter
    def asmeta_basictransitionrules_ChooseRule199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule199", None)
        self.__asmeta_basictransitionrules_ChooseRule199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term200"):
                opp_val = getattr(old_value, "basicterms_Term200", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term200"):
                opp_val = getattr(value, "basicterms_Term200", None)
                setattr(value, "basicterms_Term200", self)

    @property
    def asmeta_basictransitionrules_ChooseRule196(self):
        return self.__asmeta_basictransitionrules_ChooseRule196

    @asmeta_basictransitionrules_ChooseRule196.setter
    def asmeta_basictransitionrules_ChooseRule196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule196", None)
        self.__asmeta_basictransitionrules_ChooseRule196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule197"):
                opp_val = getattr(old_value, "basictransitionrules_Rule197", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule197"):
                opp_val = getattr(value, "basictransitionrules_Rule197", None)
                setattr(value, "basictransitionrules_Rule197", self)

    @property
    def asmeta_basictransitionrules_ChooseRule(self):
        return self.__asmeta_basictransitionrules_ChooseRule

    @asmeta_basictransitionrules_ChooseRule.setter
    def asmeta_basictransitionrules_ChooseRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule", None)
        self.__asmeta_basictransitionrules_ChooseRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule194"):
                opp_val = getattr(old_value, "basictransitionrules_Rule194", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule194"):
                opp_val = getattr(value, "basictransitionrules_Rule194", None)
                setattr(value, "basictransitionrules_Rule194", self)

    @property
    def asmeta_basictransitionrules_ChooseRule202(self):
        return self.__asmeta_basictransitionrules_ChooseRule202

    @asmeta_basictransitionrules_ChooseRule202.setter
    def asmeta_basictransitionrules_ChooseRule202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule202", None)
        self.__asmeta_basictransitionrules_ChooseRule202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm203"):
                    opp_val = getattr(item, "basicterms_VariableTerm203", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm203"):
                    opp_val = getattr(item, "basicterms_VariableTerm203", None)
                    
                    setattr(item, "basicterms_VariableTerm203", self)
                    

class asmeta_basictransitionrules_ExtendRule(BasicRule):

    pass
class asmeta_basictransitionrules_LetRule(BasicRule):

    pass
class asmeta_basictransitionrules_ForallRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ForallRule: set["basicterms_VariableTerm"] = None, asmeta_basictransitionrules_ForallRule217: "basicterms_Term" = None, asmeta_basictransitionrules_ForallRule220: "basictransitionrules_Rule" = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ForallRule = asmeta_basictransitionrules_ForallRule if asmeta_basictransitionrules_ForallRule is not None else set()
        self.asmeta_basictransitionrules_ForallRule217 = asmeta_basictransitionrules_ForallRule217
        self.asmeta_basictransitionrules_ForallRule220 = asmeta_basictransitionrules_ForallRule220
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def asmeta_basictransitionrules_ForallRule220(self):
        return self.__asmeta_basictransitionrules_ForallRule220

    @asmeta_basictransitionrules_ForallRule220.setter
    def asmeta_basictransitionrules_ForallRule220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule220", None)
        self.__asmeta_basictransitionrules_ForallRule220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule221"):
                opp_val = getattr(old_value, "basictransitionrules_Rule221", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule221"):
                opp_val = getattr(value, "basictransitionrules_Rule221", None)
                setattr(value, "basictransitionrules_Rule221", self)

    @property
    def asmeta_basictransitionrules_ForallRule217(self):
        return self.__asmeta_basictransitionrules_ForallRule217

    @asmeta_basictransitionrules_ForallRule217.setter
    def asmeta_basictransitionrules_ForallRule217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule217", None)
        self.__asmeta_basictransitionrules_ForallRule217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term218"):
                opp_val = getattr(old_value, "basicterms_Term218", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term218"):
                opp_val = getattr(value, "basicterms_Term218", None)
                setattr(value, "basicterms_Term218", self)

    @property
    def asmeta_basictransitionrules_ForallRule(self):
        return self.__asmeta_basictransitionrules_ForallRule

    @asmeta_basictransitionrules_ForallRule.setter
    def asmeta_basictransitionrules_ForallRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule", None)
        self.__asmeta_basictransitionrules_ForallRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm215"):
                    opp_val = getattr(item, "basicterms_VariableTerm215", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm215"):
                    opp_val = getattr(item, "basicterms_VariableTerm215", None)
                    
                    setattr(item, "basicterms_VariableTerm215", self)
                    

class asmeta_basictransitionrules_ConditionalRule(BasicRule):

    pass
class asmeta_basictransitionrules_BlockRule(BasicRule):

    def __init__(self, rules: str):
        self.rules = rules
        
    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

class TurboDerivedRule:

    pass
class asmeta_derivedtransitionrules_RecursiveWhileRule(TurboDerivedRule):

    pass
class asmeta_basictransitionrules_Rule(ABC):

    pass
class DerivedRule:

    pass
class asmeta_derivedtransitionrules_TurboDerivedRule(DerivedRule):

    pass
class asmeta_derivedtransitionrules_BasicDerivedRule(DerivedRule):

    pass
class BasicDerivedRule:

    pass
class asmeta_derivedtransitionrules_CaseRule(BasicDerivedRule):

    def __init__(self, caseBranches: str, asmeta_derivedtransitionrules_CaseRule: "basicterms_Term" = None, asmeta_derivedtransitionrules_CaseRule185: set["basicterms_Term"] = None, asmeta_derivedtransitionrules_CaseRule188: "basictransitionrules_Rule" = None):
        self.caseBranches = caseBranches
        self.asmeta_derivedtransitionrules_CaseRule = asmeta_derivedtransitionrules_CaseRule
        self.asmeta_derivedtransitionrules_CaseRule185 = asmeta_derivedtransitionrules_CaseRule185 if asmeta_derivedtransitionrules_CaseRule185 is not None else set()
        self.asmeta_derivedtransitionrules_CaseRule188 = asmeta_derivedtransitionrules_CaseRule188
        
    @property
    def caseBranches(self) -> str:
        return self.__caseBranches

    @caseBranches.setter
    def caseBranches(self, caseBranches: str):
        self.__caseBranches = caseBranches

    @property
    def asmeta_derivedtransitionrules_CaseRule188(self):
        return self.__asmeta_derivedtransitionrules_CaseRule188

    @asmeta_derivedtransitionrules_CaseRule188.setter
    def asmeta_derivedtransitionrules_CaseRule188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule188", None)
        self.__asmeta_derivedtransitionrules_CaseRule188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule189"):
                opp_val = getattr(old_value, "basictransitionrules_Rule189", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule189"):
                opp_val = getattr(value, "basictransitionrules_Rule189", None)
                setattr(value, "basictransitionrules_Rule189", self)

    @property
    def asmeta_derivedtransitionrules_CaseRule185(self):
        return self.__asmeta_derivedtransitionrules_CaseRule185

    @asmeta_derivedtransitionrules_CaseRule185.setter
    def asmeta_derivedtransitionrules_CaseRule185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule185", None)
        self.__asmeta_derivedtransitionrules_CaseRule185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_Term186"):
                    opp_val = getattr(item, "basicterms_Term186", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_Term186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_Term186"):
                    opp_val = getattr(item, "basicterms_Term186", None)
                    
                    setattr(item, "basicterms_Term186", self)
                    

    @property
    def asmeta_derivedtransitionrules_CaseRule(self):
        return self.__asmeta_derivedtransitionrules_CaseRule

    @asmeta_derivedtransitionrules_CaseRule.setter
    def asmeta_derivedtransitionrules_CaseRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule", None)
        self.__asmeta_derivedtransitionrules_CaseRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term183"):
                opp_val = getattr(old_value, "basicterms_Term183", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term183"):
                opp_val = getattr(value, "basicterms_Term183", None)
                setattr(value, "basicterms_Term183", self)

class asmeta_derivedtransitionrules_IterativeWhileRule(TurboDerivedRule):

    pass
class Body:

    pass
class ExportClause:

    pass
class Signature:

    pass
class turbotransitionrules_TurboCallRule:

    pass
class turbotransitionrules_TurboDeclaration:

    pass
class LocalFunction:

    pass
class basictransitionrules_Rule:

    pass
class TurboRule:

    pass
class asmeta_turbotransitionrules_IterateRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TurboCallRule(TurboRule):

    def __init__(self, parameters: str, asmeta_turbotransitionrules_TurboCallRule: "turbotransitionrules_TurboDeclaration" = None):
        self.parameters = parameters
        self.asmeta_turbotransitionrules_TurboCallRule = asmeta_turbotransitionrules_TurboCallRule
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def asmeta_turbotransitionrules_TurboCallRule(self):
        return self.__asmeta_turbotransitionrules_TurboCallRule

    @asmeta_turbotransitionrules_TurboCallRule.setter
    def asmeta_turbotransitionrules_TurboCallRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_turbotransitionrules_TurboCallRule__asmeta_turbotransitionrules_TurboCallRule", None)
        self.__asmeta_turbotransitionrules_TurboCallRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turbotransitionrules_TurboDeclaration"):
                opp_val = getattr(old_value, "turbotransitionrules_TurboDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "turbotransitionrules_TurboDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turbotransitionrules_TurboDeclaration"):
                opp_val = getattr(value, "turbotransitionrules_TurboDeclaration", None)
                setattr(value, "turbotransitionrules_TurboDeclaration", self)

class asmeta_turbotransitionrules_TryCatchRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TurboReturnRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TurboLocalStateRule(TurboRule):

    pass
class asmeta_turbotransitionrules_SeqRule(TurboRule):

    def __init__(self, rules: str):
        self.rules = rules
        
    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

class Rule:

    pass
class asmeta_basictransitionrules_TermAsRule(Rule):

    def __init__(self, parameters: str, basicterms191: "basicterms_Term" = None):
        self.parameters = parameters
        self.basicterms191 = basicterms191
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def basicterms191(self):
        return self.__basicterms191

    @basicterms191.setter
    def basicterms191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_TermAsRule__basicterms191", None)
        self.__basicterms191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "terms192"):
                opp_val = getattr(old_value, "terms192", None)
                if opp_val == self:
                    setattr(old_value, "terms192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "terms192"):
                opp_val = getattr(value, "terms192", None)
                setattr(value, "terms192", self)

class asmeta_derivedtransitionrules_DerivedRule(Rule):

    pass
class asmeta_basictransitionrules_BasicRule(Rule):

    pass
class asmeta_turbotransitionrules_TurboRule(Rule):

    pass
class basictransitionrules_MacroDeclaration:

    pass
class asmeta_structure_ImportClause:

    def __init__(self, moduleName: str, asmeta_structure_ImportClause102: set["Function"] = None, asmeta_structure_ImportClause105: set["RuleDeclaration"] = None, asmeta_structure_ImportClause: set["domains_Domain"] = None):
        self.moduleName = moduleName
        self.asmeta_structure_ImportClause102 = asmeta_structure_ImportClause102 if asmeta_structure_ImportClause102 is not None else set()
        self.asmeta_structure_ImportClause105 = asmeta_structure_ImportClause105 if asmeta_structure_ImportClause105 is not None else set()
        self.asmeta_structure_ImportClause = asmeta_structure_ImportClause if asmeta_structure_ImportClause is not None else set()
        
    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def asmeta_structure_ImportClause102(self):
        return self.__asmeta_structure_ImportClause102

    @asmeta_structure_ImportClause102.setter
    def asmeta_structure_ImportClause102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause102", None)
        self.__asmeta_structure_ImportClause102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function103"):
                    opp_val = getattr(item, "Function103", None)
                    
                    if opp_val == self:
                        setattr(item, "Function103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function103"):
                    opp_val = getattr(item, "Function103", None)
                    
                    setattr(item, "Function103", self)
                    

    @property
    def asmeta_structure_ImportClause105(self):
        return self.__asmeta_structure_ImportClause105

    @asmeta_structure_ImportClause105.setter
    def asmeta_structure_ImportClause105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause105", None)
        self.__asmeta_structure_ImportClause105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleDeclaration106"):
                    opp_val = getattr(item, "RuleDeclaration106", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleDeclaration106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleDeclaration106"):
                    opp_val = getattr(item, "RuleDeclaration106", None)
                    
                    setattr(item, "RuleDeclaration106", self)
                    

    @property
    def asmeta_structure_ImportClause(self):
        return self.__asmeta_structure_ImportClause

    @asmeta_structure_ImportClause.setter
    def asmeta_structure_ImportClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause", None)
        self.__asmeta_structure_ImportClause = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domains_Domain100"):
                    opp_val = getattr(item, "domains_Domain100", None)
                    
                    if opp_val == self:
                        setattr(item, "domains_Domain100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domains_Domain100"):
                    opp_val = getattr(item, "domains_Domain100", None)
                    
                    setattr(item, "domains_Domain100", self)
                    

class asmeta_structure_ExportClause:

    pass
class domains_StructuredTd:

    pass
class Header:

    pass
class ImportClause:

    pass
class asmeta_structure_Header:

    pass
class AgentInitialization:

    pass
class FunctionInitialization:

    pass
class DomainInitialization:

    pass
class NamedElement:

    pass
class asmeta_definitions_Classifier(NamedElement):

    pass
class asmeta_structure_Asm(NamedElement):

    def __init__(self, isAsynchr: str, Header145: "Header" = None, asmeta_structure_Asm148: "basictransitionrules_MacroDeclaration" = None, asmeta_structure_Asm: set["Initialization"] = None, Initialization140: "Initialization" = None, Body: "Body" = None):
        self.isAsynchr = isAsynchr
        self.Header145 = Header145
        self.asmeta_structure_Asm148 = asmeta_structure_Asm148
        self.asmeta_structure_Asm = asmeta_structure_Asm if asmeta_structure_Asm is not None else set()
        self.Initialization140 = Initialization140
        self.Body = Body
        
    @property
    def isAsynchr(self) -> str:
        return self.__isAsynchr

    @isAsynchr.setter
    def isAsynchr(self, isAsynchr: str):
        self.__isAsynchr = isAsynchr

    @property
    def asmeta_structure_Asm(self):
        return self.__asmeta_structure_Asm

    @asmeta_structure_Asm.setter
    def asmeta_structure_Asm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asmeta_structure_Asm", None)
        self.__asmeta_structure_Asm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Initialization138"):
                    opp_val = getattr(item, "Initialization138", None)
                    
                    if opp_val == self:
                        setattr(item, "Initialization138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Initialization138"):
                    opp_val = getattr(item, "Initialization138", None)
                    
                    setattr(item, "Initialization138", self)
                    

    @property
    def Initialization140(self):
        return self.__Initialization140

    @Initialization140.setter
    def Initialization140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__Initialization140", None)
        self.__Initialization140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure141"):
                opp_val = getattr(old_value, "structure141", None)
                if opp_val == self:
                    setattr(old_value, "structure141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure141"):
                opp_val = getattr(value, "structure141", None)
                setattr(value, "structure141", self)

    @property
    def asmeta_structure_Asm148(self):
        return self.__asmeta_structure_Asm148

    @asmeta_structure_Asm148.setter
    def asmeta_structure_Asm148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asmeta_structure_Asm148", None)
        self.__asmeta_structure_Asm148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_MacroDeclaration"):
                opp_val = getattr(old_value, "basictransitionrules_MacroDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_MacroDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_MacroDeclaration"):
                opp_val = getattr(value, "basictransitionrules_MacroDeclaration", None)
                setattr(value, "basictransitionrules_MacroDeclaration", self)

    @property
    def Header145(self):
        return self.__Header145

    @Header145.setter
    def Header145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__Header145", None)
        self.__Header145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure146"):
                opp_val = getattr(old_value, "structure146", None)
                if opp_val == self:
                    setattr(old_value, "structure146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure146"):
                opp_val = getattr(value, "structure146", None)
                setattr(value, "structure146", self)

    @property
    def Body(self):
        return self.__Body

    @Body.setter
    def Body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__Body", None)
        self.__Body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure143"):
                opp_val = getattr(old_value, "structure143", None)
                if opp_val == self:
                    setattr(old_value, "structure143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure143"):
                opp_val = getattr(value, "structure143", None)
                setattr(value, "structure143", self)

class asmeta_structure_Initialization(NamedElement):

    pass
class asmeta_structure_DomainDefinition:

    pass
class asmeta_structure_FunctionDefinition:

    pass
class Property:

    pass
class asmeta_definitions_Invariant(Property):

    pass
class asmeta_definitions_TemporalProperty(Property):

    pass
class FunctionDefinition:

    pass
class asmeta_structure_Body:

    pass
class Initialization:

    pass
class basictransitionrules_MacroCallRule:

    pass
class asmeta_structure_AgentInitialization:

    pass
class asmeta_structure_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class asmeta_structure_Signature:

    pass
class domains_ConcreteDomain:

    pass
class asmeta_structure_DomainInitialization:

    pass
class DynamicFunction:

    pass
class asmeta_definitions_MonitoredFunction(DynamicFunction):

    pass
class asmeta_definitions_ControlledFunction(DynamicFunction):

    pass
class asmeta_definitions_SharedFunction(DynamicFunction):

    pass
class asmeta_definitions_OutFunction(DynamicFunction):

    pass
class asmeta_definitions_LocalFunction(DynamicFunction):

    pass
class asmeta_structure_FunctionInitialization:

    pass
class InvarConstraint:

    pass
class FairnessConstraint:

    pass
class asmeta_definitions_CompassionConstraint(FairnessConstraint):

    pass
class asmeta_definitions_JusticeConstraint(FairnessConstraint):

    pass
class Asm:

    pass
class DomainDefinition:

    pass
class furtherterms_FiniteQuantificationTerm:

    pass
class BasicTerm:

    pass
class asmeta_basicterms_VariableTerm(BasicTerm):

    def __init__(self, name: str, kind: str, furtherterms: "furtherterms_FiniteQuantificationTerm" = None):
        self.name = name
        self.kind = kind
        self.furtherterms = furtherterms
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def furtherterms(self):
        return self.__furtherterms

    @furtherterms.setter
    def furtherterms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basicterms_VariableTerm__furtherterms", None)
        self.__furtherterms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "terms37"):
                opp_val = getattr(old_value, "terms37", None)
                if opp_val == self:
                    setattr(old_value, "terms37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "terms37"):
                opp_val = getattr(value, "terms37", None)
                setattr(value, "terms37", self)

class basictransitionrules_TermAsRule:

    pass
class domains_Domain:

    pass
class asmeta_basicterms_Term(ABC):

    def __init__(self, asmeta_basicterms_Term: "domains_Domain" = None, basictransitionrules: set["basictransitionrules_TermAsRule"] = None):
        self.asmeta_basicterms_Term = asmeta_basicterms_Term
        self.basictransitionrules = basictransitionrules if basictransitionrules is not None else set()
        
    @property
    def basictransitionrules(self):
        return self.__basictransitionrules

    @basictransitionrules.setter
    def basictransitionrules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basicterms_Term__basictransitionrules", None)
        self.__basictransitionrules = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transitionrules"):
                    opp_val = getattr(item, "transitionrules", None)
                    
                    if opp_val == self:
                        setattr(item, "transitionrules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transitionrules"):
                    opp_val = getattr(item, "transitionrules", None)
                    
                    setattr(item, "transitionrules", self)
                    

    @property
    def asmeta_basicterms_Term(self):
        return self.__asmeta_basicterms_Term

    @asmeta_basicterms_Term.setter
    def asmeta_basicterms_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basicterms_Term__asmeta_basicterms_Term", None)
        self.__asmeta_basicterms_Term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_Domain"):
                opp_val = getattr(old_value, "domains_Domain", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain"):
                opp_val = getattr(value, "domains_Domain", None)
                setattr(value, "domains_Domain", self)

    def compatible(self):
        # TODO: Implement compatible method
        pass

class asmeta_basicterms_ConstantTerm(BasicTerm):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class Term:

    pass
class asmeta_basicterms_BasicTerm(Term):

    pass
class asmeta_basicterms_ExtendedTerm(Term):

    pass
class Function:

    pass
class asmeta_definitions_BasicFunction(Function):

    pass
class asmeta_definitions_DerivedFunction(Function):

    pass
class asmeta_basicterms_FunctionTerm(BasicTerm):

    pass
class FunctionTerm:

    pass
class asmeta_basicterms_LocationTerm(FunctionTerm):

    pass
class RuleDeclaration:

    pass
class asmeta_basictransitionrules_MacroDeclaration(RuleDeclaration):

    pass
class asmeta_turbotransitionrules_TurboDeclaration(RuleDeclaration):

    pass
class FiniteQuantificationTerm:

    pass
class asmeta_furtherterms_ExistTerm(FiniteQuantificationTerm):

    pass
class asmeta_furtherterms_ExistUniqueTerm(FiniteQuantificationTerm):

    pass
class asmeta_furtherterms_ForallTerm(FiniteQuantificationTerm):

    pass
class basicterms_Term:

    pass
class basicterms_VariableTerm:

    pass
class VariableBindingTerm:

    pass
class asmeta_furtherterms_FiniteQuantificationTerm(VariableBindingTerm):

    def __init__(self, ranges: str, basicterms: set["basicterms_VariableTerm"] = None, asmeta_furtherterms_FiniteQuantificationTerm: "basicterms_Term" = None):
        self.ranges = ranges
        self.basicterms = basicterms if basicterms is not None else set()
        self.asmeta_furtherterms_FiniteQuantificationTerm = asmeta_furtherterms_FiniteQuantificationTerm
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def basicterms(self):
        return self.__basicterms

    @basicterms.setter
    def basicterms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_FiniteQuantificationTerm__basicterms", None)
        self.__basicterms = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "terms"):
                    opp_val = getattr(item, "terms", None)
                    
                    if opp_val == self:
                        setattr(item, "terms", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "terms"):
                    opp_val = getattr(item, "terms", None)
                    
                    setattr(item, "terms", self)
                    

    @property
    def asmeta_furtherterms_FiniteQuantificationTerm(self):
        return self.__asmeta_furtherterms_FiniteQuantificationTerm

    @asmeta_furtherterms_FiniteQuantificationTerm.setter
    def asmeta_furtherterms_FiniteQuantificationTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_FiniteQuantificationTerm__asmeta_furtherterms_FiniteQuantificationTerm", None)
        self.__asmeta_furtherterms_FiniteQuantificationTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term9"):
                opp_val = getattr(old_value, "basicterms_Term9", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term9"):
                opp_val = getattr(value, "basicterms_Term9", None)
                setattr(value, "basicterms_Term9", self)

class asmeta_furtherterms_ComprehensionTerm(VariableBindingTerm):

    def __init__(self, ranges: str, asmeta_furtherterms_ComprehensionTerm: set["basicterms_VariableTerm"] = None, asmeta_furtherterms_ComprehensionTerm21: "basicterms_Term" = None, asmeta_furtherterms_ComprehensionTerm24: "basicterms_Term" = None):
        self.ranges = ranges
        self.asmeta_furtherterms_ComprehensionTerm = asmeta_furtherterms_ComprehensionTerm if asmeta_furtherterms_ComprehensionTerm is not None else set()
        self.asmeta_furtherterms_ComprehensionTerm21 = asmeta_furtherterms_ComprehensionTerm21
        self.asmeta_furtherterms_ComprehensionTerm24 = asmeta_furtherterms_ComprehensionTerm24
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def asmeta_furtherterms_ComprehensionTerm24(self):
        return self.__asmeta_furtherterms_ComprehensionTerm24

    @asmeta_furtherterms_ComprehensionTerm24.setter
    def asmeta_furtherterms_ComprehensionTerm24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_ComprehensionTerm__asmeta_furtherterms_ComprehensionTerm24", None)
        self.__asmeta_furtherterms_ComprehensionTerm24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term25"):
                opp_val = getattr(old_value, "basicterms_Term25", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term25"):
                opp_val = getattr(value, "basicterms_Term25", None)
                setattr(value, "basicterms_Term25", self)

    @property
    def asmeta_furtherterms_ComprehensionTerm21(self):
        return self.__asmeta_furtherterms_ComprehensionTerm21

    @asmeta_furtherterms_ComprehensionTerm21.setter
    def asmeta_furtherterms_ComprehensionTerm21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_ComprehensionTerm__asmeta_furtherterms_ComprehensionTerm21", None)
        self.__asmeta_furtherterms_ComprehensionTerm21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term22"):
                opp_val = getattr(old_value, "basicterms_Term22", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term22"):
                opp_val = getattr(value, "basicterms_Term22", None)
                setattr(value, "basicterms_Term22", self)

    @property
    def asmeta_furtherterms_ComprehensionTerm(self):
        return self.__asmeta_furtherterms_ComprehensionTerm

    @asmeta_furtherterms_ComprehensionTerm.setter
    def asmeta_furtherterms_ComprehensionTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_ComprehensionTerm__asmeta_furtherterms_ComprehensionTerm", None)
        self.__asmeta_furtherterms_ComprehensionTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm19"):
                    opp_val = getattr(item, "basicterms_VariableTerm19", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm19"):
                    opp_val = getattr(item, "basicterms_VariableTerm19", None)
                    
                    setattr(item, "basicterms_VariableTerm19", self)
                    

class asmeta_furtherterms_LetTerm(VariableBindingTerm):

    pass
class basicterms_TupleTerm:

    pass
class CollectionTerm:

    pass
class asmeta_furtherterms_MapTerm(CollectionTerm):

    pass
class asmeta_basicterms_SetTerm(CollectionTerm):

    pass
class asmeta_furtherterms_BagTerm(CollectionTerm):

    pass
class asmeta_furtherterms_SequenceTerm(CollectionTerm):

    def __init__(self, terms: str):
        self.terms = terms
        
    @property
    def terms(self) -> str:
        return self.__terms

    @terms.setter
    def terms(self, terms: str):
        self.__terms = terms

class ComprehensionTerm:

    pass
class asmeta_furtherterms_BagCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_MapCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_SequenceCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_SetCt(ComprehensionTerm):

    pass
class ExtendedTerm:

    pass
class asmeta_furtherterms_CaseTerm(ExtendedTerm):

    def __init__(self, resultTerms: str, asmeta_furtherterms_CaseTerm: set["basicterms_Term"] = None, asmeta_furtherterms_CaseTerm29: "basicterms_Term" = None, asmeta_furtherterms_CaseTerm32: "basicterms_Term" = None):
        self.resultTerms = resultTerms
        self.asmeta_furtherterms_CaseTerm = asmeta_furtherterms_CaseTerm if asmeta_furtherterms_CaseTerm is not None else set()
        self.asmeta_furtherterms_CaseTerm29 = asmeta_furtherterms_CaseTerm29
        self.asmeta_furtherterms_CaseTerm32 = asmeta_furtherterms_CaseTerm32
        
    @property
    def resultTerms(self) -> str:
        return self.__resultTerms

    @resultTerms.setter
    def resultTerms(self, resultTerms: str):
        self.__resultTerms = resultTerms

    @property
    def asmeta_furtherterms_CaseTerm32(self):
        return self.__asmeta_furtherterms_CaseTerm32

    @asmeta_furtherterms_CaseTerm32.setter
    def asmeta_furtherterms_CaseTerm32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_CaseTerm__asmeta_furtherterms_CaseTerm32", None)
        self.__asmeta_furtherterms_CaseTerm32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term33"):
                opp_val = getattr(old_value, "basicterms_Term33", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term33"):
                opp_val = getattr(value, "basicterms_Term33", None)
                setattr(value, "basicterms_Term33", self)

    @property
    def asmeta_furtherterms_CaseTerm(self):
        return self.__asmeta_furtherterms_CaseTerm

    @asmeta_furtherterms_CaseTerm.setter
    def asmeta_furtherterms_CaseTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_CaseTerm__asmeta_furtherterms_CaseTerm", None)
        self.__asmeta_furtherterms_CaseTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_Term27"):
                    opp_val = getattr(item, "basicterms_Term27", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_Term27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_Term27"):
                    opp_val = getattr(item, "basicterms_Term27", None)
                    
                    setattr(item, "basicterms_Term27", self)
                    

    @property
    def asmeta_furtherterms_CaseTerm29(self):
        return self.__asmeta_furtherterms_CaseTerm29

    @asmeta_furtherterms_CaseTerm29.setter
    def asmeta_furtherterms_CaseTerm29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_CaseTerm__asmeta_furtherterms_CaseTerm29", None)
        self.__asmeta_furtherterms_CaseTerm29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term30"):
                opp_val = getattr(old_value, "basicterms_Term30", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term30"):
                opp_val = getattr(value, "basicterms_Term30", None)
                setattr(value, "basicterms_Term30", self)

class asmeta_basicterms_CollectionTerm(ExtendedTerm):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class asmeta_basicterms_DomainTerm(ExtendedTerm):

    pass
class asmeta_basicterms_TupleTerm(ExtendedTerm):

    def __init__(self, terms: str, arity: str):
        self.terms = terms
        self.arity = arity
        
    @property
    def arity(self) -> str:
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity

    @property
    def terms(self) -> str:
        return self.__terms

    @terms.setter
    def terms(self, terms: str):
        self.__terms = terms

class asmeta_basicterms_RuleAsTerm(ExtendedTerm):

    pass
class asmeta_furtherterms_ConditionalTerm(ExtendedTerm):

    pass
class asmeta_furtherterms_VariableBindingTerm(ExtendedTerm):

    pass
class ConstantTerm:

    pass
class asmeta_furtherterms_StringTerm(ConstantTerm):

    pass
class asmeta_furtherterms_NaturalTerm(ConstantTerm):

    pass
class asmeta_basicterms_UndefTerm(ConstantTerm):

    pass
class asmeta_furtherterms_RealTerm(ConstantTerm):

    pass
class asmeta_furtherterms_EnumTerm(ConstantTerm):

    pass
class asmeta_basicterms_BooleanTerm(ConstantTerm):

    pass
class asmeta_furtherterms_ComplexTerm(ConstantTerm):

    pass
class asmeta_furtherterms_CharTerm(ConstantTerm):

    pass
class asmeta_furtherterms_IntegerTerm(ConstantTerm):

    pass
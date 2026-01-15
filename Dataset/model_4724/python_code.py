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

class domains_TypeDomain:

    pass
class RealDomain:

    pass
class asmeta_domains_IntegerDomain(RealDomain):

    pass
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
class asmeta_domains_BasicTd(TypeDomain):

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

class asmeta_domains_EnumTd(TypeDomain):

    pass
class asmeta_domains_AnyDomain(TypeDomain):

    pass
class asmeta_domains_StructuredTd(TypeDomain):

    pass
class Domain:

    pass
class asmeta_domains_ConcreteDomain(Domain):

    def __init__(self, isDynamic: str, DomainInitialization294: set["DomainInitialization"] = None, DomainDefinition297: "DomainDefinition" = None, asmeta_domains_ConcreteDomain: "domains_TypeDomain" = None):
        self.isDynamic = isDynamic
        self.DomainInitialization294 = DomainInitialization294 if DomainInitialization294 is not None else set()
        self.DomainDefinition297 = DomainDefinition297
        self.asmeta_domains_ConcreteDomain = asmeta_domains_ConcreteDomain
        
    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def DomainDefinition297(self):
        return self.__DomainDefinition297

    @DomainDefinition297.setter
    def DomainDefinition297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__DomainDefinition297", None)
        self.__DomainDefinition297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure298"):
                opp_val = getattr(old_value, "structure298", None)
                if opp_val == self:
                    setattr(old_value, "structure298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure298"):
                opp_val = getattr(value, "structure298", None)
                setattr(value, "structure298", self)

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
    def DomainInitialization294(self):
        return self.__DomainInitialization294

    @DomainInitialization294.setter
    def DomainInitialization294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__DomainInitialization294", None)
        self.__DomainInitialization294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure295"):
                    opp_val = getattr(item, "structure295", None)
                    
                    if opp_val == self:
                        setattr(item, "structure295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure295"):
                    opp_val = getattr(item, "structure295", None)
                    
                    setattr(item, "structure295", self)
                    

class asmeta_domains_TypeDomain(Domain):

    pass
class BasicTd:

    pass
class asmeta_domains_ComplexDomain(BasicTd):

    pass
class asmeta_domains_CharDomain(BasicTd):

    pass
class asmeta_domains_StringDomain(BasicTd):

    pass
class asmeta_domains_BooleanDomain(BasicTd):

    pass
class asmeta_domains_UndefDomain(BasicTd):

    pass
class IntegerDomain:

    pass
class asmeta_domains_NaturalDomain(IntegerDomain):

    pass
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
class asmeta_definitions_Function(Classifier):

    def __init__(self, arity: str, asmeta_definitions_Function: "domains_Domain" = None, asmeta_definitions_Function266: "domains_Domain" = None, FunctionDefinition269: "FunctionDefinition" = None, Invariant272: set["Invariant"] = None, Signature275: "Signature" = None):
        self.arity = arity
        self.asmeta_definitions_Function = asmeta_definitions_Function
        self.asmeta_definitions_Function266 = asmeta_definitions_Function266
        self.FunctionDefinition269 = FunctionDefinition269
        self.Invariant272 = Invariant272 if Invariant272 is not None else set()
        self.Signature275 = Signature275
        
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
            if hasattr(old_value, "domains_Domain264"):
                opp_val = getattr(old_value, "domains_Domain264", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain264"):
                opp_val = getattr(value, "domains_Domain264", None)
                setattr(value, "domains_Domain264", self)

    @property
    def FunctionDefinition269(self):
        return self.__FunctionDefinition269

    @FunctionDefinition269.setter
    def FunctionDefinition269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__FunctionDefinition269", None)
        self.__FunctionDefinition269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure270"):
                opp_val = getattr(old_value, "structure270", None)
                if opp_val == self:
                    setattr(old_value, "structure270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure270"):
                opp_val = getattr(value, "structure270", None)
                setattr(value, "structure270", self)

    @property
    def asmeta_definitions_Function266(self):
        return self.__asmeta_definitions_Function266

    @asmeta_definitions_Function266.setter
    def asmeta_definitions_Function266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__asmeta_definitions_Function266", None)
        self.__asmeta_definitions_Function266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_Domain267"):
                opp_val = getattr(old_value, "domains_Domain267", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain267"):
                opp_val = getattr(value, "domains_Domain267", None)
                setattr(value, "domains_Domain267", self)

    @property
    def Signature275(self):
        return self.__Signature275

    @Signature275.setter
    def Signature275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__Signature275", None)
        self.__Signature275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure276"):
                opp_val = getattr(old_value, "structure276", None)
                if opp_val == self:
                    setattr(old_value, "structure276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure276"):
                opp_val = getattr(value, "structure276", None)
                setattr(value, "structure276", self)

    @property
    def Invariant272(self):
        return self.__Invariant272

    @Invariant272.setter
    def Invariant272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__Invariant272", None)
        self.__Invariant272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "definitions273"):
                    opp_val = getattr(item, "definitions273", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions273"):
                    opp_val = getattr(item, "definitions273", None)
                    
                    setattr(item, "definitions273", self)
                    

class asmeta_domains_Domain(Classifier):

    def __init__(self, Invariant288: set["Invariant"] = None, Signature291: "Signature" = None):
        self.Invariant288 = Invariant288 if Invariant288 is not None else set()
        self.Signature291 = Signature291
        
    @property
    def Invariant288(self):
        return self.__Invariant288

    @Invariant288.setter
    def Invariant288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__Invariant288", None)
        self.__Invariant288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "definitions289"):
                    opp_val = getattr(item, "definitions289", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions289"):
                    opp_val = getattr(item, "definitions289", None)
                    
                    setattr(item, "definitions289", self)
                    

    @property
    def Signature291(self):
        return self.__Signature291

    @Signature291.setter
    def Signature291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__Signature291", None)
        self.__Signature291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure292"):
                opp_val = getattr(old_value, "structure292", None)
                if opp_val == self:
                    setattr(old_value, "structure292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure292"):
                opp_val = getattr(value, "structure292", None)
                setattr(value, "structure292", self)

    def compatible(self):
        # TODO: Implement compatible method
        pass

class asmeta_definitions_Property(Classifier):

    pass
class asmeta_definitions_RuleDeclaration(Classifier):

    def __init__(self, arity: str, asmeta_definitions_RuleDeclaration: set["basicterms_VariableTerm"] = None, Invariant: set["Invariant"] = None, asmeta_definitions_RuleDeclaration244: "basictransitionrules_Rule" = None, Body247: "Body" = None):
        self.arity = arity
        self.asmeta_definitions_RuleDeclaration = asmeta_definitions_RuleDeclaration if asmeta_definitions_RuleDeclaration is not None else set()
        self.Invariant = Invariant if Invariant is not None else set()
        self.asmeta_definitions_RuleDeclaration244 = asmeta_definitions_RuleDeclaration244
        self.Body247 = Body247
        
    @property
    def arity(self) -> str:
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity

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
                if hasattr(item, "basicterms_VariableTerm240"):
                    opp_val = getattr(item, "basicterms_VariableTerm240", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm240"):
                    opp_val = getattr(item, "basicterms_VariableTerm240", None)
                    
                    setattr(item, "basicterms_VariableTerm240", self)
                    

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
                if hasattr(item, "definitions242"):
                    opp_val = getattr(item, "definitions242", None)
                    
                    if opp_val == self:
                        setattr(item, "definitions242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "definitions242"):
                    opp_val = getattr(item, "definitions242", None)
                    
                    setattr(item, "definitions242", self)
                    

    @property
    def Body247(self):
        return self.__Body247

    @Body247.setter
    def Body247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__Body247", None)
        self.__Body247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure248"):
                opp_val = getattr(old_value, "structure248", None)
                if opp_val == self:
                    setattr(old_value, "structure248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure248"):
                opp_val = getattr(value, "structure248", None)
                setattr(value, "structure248", self)

    @property
    def asmeta_definitions_RuleDeclaration244(self):
        return self.__asmeta_definitions_RuleDeclaration244

    @asmeta_definitions_RuleDeclaration244.setter
    def asmeta_definitions_RuleDeclaration244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__asmeta_definitions_RuleDeclaration244", None)
        self.__asmeta_definitions_RuleDeclaration244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule245"):
                opp_val = getattr(old_value, "basictransitionrules_Rule245", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule245"):
                opp_val = getattr(value, "basictransitionrules_Rule245", None)
                setattr(value, "basictransitionrules_Rule245", self)

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
            if hasattr(old_value, "basictransitionrules_MacroDeclaration201"):
                opp_val = getattr(old_value, "basictransitionrules_MacroDeclaration201", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_MacroDeclaration201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_MacroDeclaration201"):
                opp_val = getattr(value, "basictransitionrules_MacroDeclaration201", None)
                setattr(value, "basictransitionrules_MacroDeclaration201", self)

class asmeta_basictransitionrules_SkipRule(BasicRule):

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

class asmeta_basictransitionrules_UpdateRule(BasicRule):

    pass
class asmeta_basictransitionrules_ExtendRule(BasicRule):

    pass
class asmeta_basictransitionrules_LetRule(BasicRule):

    pass
class asmeta_basictransitionrules_ConditionalRule(BasicRule):

    pass
class asmeta_basictransitionrules_ChooseRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ChooseRule: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule192: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule195: "basicterms_Term" = None, asmeta_basictransitionrules_ChooseRule198: set["basicterms_VariableTerm"] = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ChooseRule = asmeta_basictransitionrules_ChooseRule
        self.asmeta_basictransitionrules_ChooseRule192 = asmeta_basictransitionrules_ChooseRule192
        self.asmeta_basictransitionrules_ChooseRule195 = asmeta_basictransitionrules_ChooseRule195
        self.asmeta_basictransitionrules_ChooseRule198 = asmeta_basictransitionrules_ChooseRule198 if asmeta_basictransitionrules_ChooseRule198 is not None else set()
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def asmeta_basictransitionrules_ChooseRule195(self):
        return self.__asmeta_basictransitionrules_ChooseRule195

    @asmeta_basictransitionrules_ChooseRule195.setter
    def asmeta_basictransitionrules_ChooseRule195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule195", None)
        self.__asmeta_basictransitionrules_ChooseRule195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term196"):
                opp_val = getattr(old_value, "basicterms_Term196", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term196"):
                opp_val = getattr(value, "basicterms_Term196", None)
                setattr(value, "basicterms_Term196", self)

    @property
    def asmeta_basictransitionrules_ChooseRule192(self):
        return self.__asmeta_basictransitionrules_ChooseRule192

    @asmeta_basictransitionrules_ChooseRule192.setter
    def asmeta_basictransitionrules_ChooseRule192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule192", None)
        self.__asmeta_basictransitionrules_ChooseRule192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule193"):
                opp_val = getattr(old_value, "basictransitionrules_Rule193", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule193"):
                opp_val = getattr(value, "basictransitionrules_Rule193", None)
                setattr(value, "basictransitionrules_Rule193", self)

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
            if hasattr(old_value, "basictransitionrules_Rule190"):
                opp_val = getattr(old_value, "basictransitionrules_Rule190", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule190"):
                opp_val = getattr(value, "basictransitionrules_Rule190", None)
                setattr(value, "basictransitionrules_Rule190", self)

    @property
    def asmeta_basictransitionrules_ChooseRule198(self):
        return self.__asmeta_basictransitionrules_ChooseRule198

    @asmeta_basictransitionrules_ChooseRule198.setter
    def asmeta_basictransitionrules_ChooseRule198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule198", None)
        self.__asmeta_basictransitionrules_ChooseRule198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm199"):
                    opp_val = getattr(item, "basicterms_VariableTerm199", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm199"):
                    opp_val = getattr(item, "basicterms_VariableTerm199", None)
                    
                    setattr(item, "basicterms_VariableTerm199", self)
                    

class asmeta_basictransitionrules_Rule(ABC):

    pass
class asmeta_basictransitionrules_ForallRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ForallRule: set["basicterms_VariableTerm"] = None, asmeta_basictransitionrules_ForallRule213: "basicterms_Term" = None, asmeta_basictransitionrules_ForallRule216: "basictransitionrules_Rule" = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ForallRule = asmeta_basictransitionrules_ForallRule if asmeta_basictransitionrules_ForallRule is not None else set()
        self.asmeta_basictransitionrules_ForallRule213 = asmeta_basictransitionrules_ForallRule213
        self.asmeta_basictransitionrules_ForallRule216 = asmeta_basictransitionrules_ForallRule216
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def asmeta_basictransitionrules_ForallRule216(self):
        return self.__asmeta_basictransitionrules_ForallRule216

    @asmeta_basictransitionrules_ForallRule216.setter
    def asmeta_basictransitionrules_ForallRule216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule216", None)
        self.__asmeta_basictransitionrules_ForallRule216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule217"):
                opp_val = getattr(old_value, "basictransitionrules_Rule217", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule217"):
                opp_val = getattr(value, "basictransitionrules_Rule217", None)
                setattr(value, "basictransitionrules_Rule217", self)

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
                if hasattr(item, "basicterms_VariableTerm211"):
                    opp_val = getattr(item, "basicterms_VariableTerm211", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm211"):
                    opp_val = getattr(item, "basicterms_VariableTerm211", None)
                    
                    setattr(item, "basicterms_VariableTerm211", self)
                    

    @property
    def asmeta_basictransitionrules_ForallRule213(self):
        return self.__asmeta_basictransitionrules_ForallRule213

    @asmeta_basictransitionrules_ForallRule213.setter
    def asmeta_basictransitionrules_ForallRule213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule213", None)
        self.__asmeta_basictransitionrules_ForallRule213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term214"):
                opp_val = getattr(old_value, "basicterms_Term214", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term214"):
                opp_val = getattr(value, "basicterms_Term214", None)
                setattr(value, "basicterms_Term214", self)

class BasicDerivedRule:

    pass
class asmeta_derivedtransitionrules_CaseRule(BasicDerivedRule):

    def __init__(self, caseBranches: str, asmeta_derivedtransitionrules_CaseRule184: "basictransitionrules_Rule" = None, asmeta_derivedtransitionrules_CaseRule: "basicterms_Term" = None, asmeta_derivedtransitionrules_CaseRule181: set["basicterms_Term"] = None):
        self.caseBranches = caseBranches
        self.asmeta_derivedtransitionrules_CaseRule184 = asmeta_derivedtransitionrules_CaseRule184
        self.asmeta_derivedtransitionrules_CaseRule = asmeta_derivedtransitionrules_CaseRule
        self.asmeta_derivedtransitionrules_CaseRule181 = asmeta_derivedtransitionrules_CaseRule181 if asmeta_derivedtransitionrules_CaseRule181 is not None else set()
        
    @property
    def caseBranches(self) -> str:
        return self.__caseBranches

    @caseBranches.setter
    def caseBranches(self, caseBranches: str):
        self.__caseBranches = caseBranches

    @property
    def asmeta_derivedtransitionrules_CaseRule181(self):
        return self.__asmeta_derivedtransitionrules_CaseRule181

    @asmeta_derivedtransitionrules_CaseRule181.setter
    def asmeta_derivedtransitionrules_CaseRule181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule181", None)
        self.__asmeta_derivedtransitionrules_CaseRule181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_Term182"):
                    opp_val = getattr(item, "basicterms_Term182", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_Term182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_Term182"):
                    opp_val = getattr(item, "basicterms_Term182", None)
                    
                    setattr(item, "basicterms_Term182", self)
                    

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
            if hasattr(old_value, "basicterms_Term179"):
                opp_val = getattr(old_value, "basicterms_Term179", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term179"):
                opp_val = getattr(value, "basicterms_Term179", None)
                setattr(value, "basicterms_Term179", self)

    @property
    def asmeta_derivedtransitionrules_CaseRule184(self):
        return self.__asmeta_derivedtransitionrules_CaseRule184

    @asmeta_derivedtransitionrules_CaseRule184.setter
    def asmeta_derivedtransitionrules_CaseRule184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule184", None)
        self.__asmeta_derivedtransitionrules_CaseRule184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule185"):
                opp_val = getattr(old_value, "basictransitionrules_Rule185", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule185"):
                opp_val = getattr(value, "basictransitionrules_Rule185", None)
                setattr(value, "basictransitionrules_Rule185", self)

class TurboDerivedRule:

    pass
class asmeta_derivedtransitionrules_IterativeWhileRule(TurboDerivedRule):

    pass
class asmeta_derivedtransitionrules_RecursiveWhileRule(TurboDerivedRule):

    pass
class DerivedRule:

    pass
class asmeta_derivedtransitionrules_TurboDerivedRule(DerivedRule):

    pass
class asmeta_derivedtransitionrules_BasicDerivedRule(DerivedRule):

    pass
class turbotransitionrules_TurboCallRule:

    pass
class basictransitionrules_Rule:

    pass
class TurboRule:

    pass
class asmeta_turbotransitionrules_TryCatchRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TurboLocalStateRule(TurboRule):

    pass
class asmeta_turbotransitionrules_IterateRule(TurboRule):

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

    def __init__(self, parameters: str, basicterms187: "basicterms_Term" = None):
        self.parameters = parameters
        self.basicterms187 = basicterms187
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def basicterms187(self):
        return self.__basicterms187

    @basicterms187.setter
    def basicterms187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_TermAsRule__basicterms187", None)
        self.__basicterms187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "terms188"):
                opp_val = getattr(old_value, "terms188", None)
                if opp_val == self:
                    setattr(old_value, "terms188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "terms188"):
                opp_val = getattr(value, "terms188", None)
                setattr(value, "terms188", self)

class asmeta_derivedtransitionrules_DerivedRule(Rule):

    pass
class asmeta_basictransitionrules_BasicRule(Rule):

    pass
class asmeta_turbotransitionrules_TurboRule(Rule):

    pass
class basictransitionrules_MacroDeclaration:

    pass
class Body:

    pass
class ExportClause:

    pass
class Signature:

    pass
class ImportClause:

    pass
class asmeta_structure_Header:

    pass
class asmeta_turbotransitionrules_TurboReturnRule(TurboRule):

    pass
class turbotransitionrules_TurboDeclaration:

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

class LocalFunction:

    pass
class asmeta_structure_DomainDefinition:

    pass
class asmeta_structure_FunctionDefinition:

    pass
class asmeta_structure_ImportClause:

    def __init__(self, moduleName: str, asmeta_structure_ImportClause: set["domains_Domain"] = None, asmeta_structure_ImportClause98: set["Function"] = None, asmeta_structure_ImportClause101: set["RuleDeclaration"] = None):
        self.moduleName = moduleName
        self.asmeta_structure_ImportClause = asmeta_structure_ImportClause if asmeta_structure_ImportClause is not None else set()
        self.asmeta_structure_ImportClause98 = asmeta_structure_ImportClause98 if asmeta_structure_ImportClause98 is not None else set()
        self.asmeta_structure_ImportClause101 = asmeta_structure_ImportClause101 if asmeta_structure_ImportClause101 is not None else set()
        
    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def asmeta_structure_ImportClause101(self):
        return self.__asmeta_structure_ImportClause101

    @asmeta_structure_ImportClause101.setter
    def asmeta_structure_ImportClause101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause101", None)
        self.__asmeta_structure_ImportClause101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleDeclaration102"):
                    opp_val = getattr(item, "RuleDeclaration102", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleDeclaration102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleDeclaration102"):
                    opp_val = getattr(item, "RuleDeclaration102", None)
                    
                    setattr(item, "RuleDeclaration102", self)
                    

    @property
    def asmeta_structure_ImportClause98(self):
        return self.__asmeta_structure_ImportClause98

    @asmeta_structure_ImportClause98.setter
    def asmeta_structure_ImportClause98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause98", None)
        self.__asmeta_structure_ImportClause98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function99"):
                    opp_val = getattr(item, "Function99", None)
                    
                    if opp_val == self:
                        setattr(item, "Function99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function99"):
                    opp_val = getattr(item, "Function99", None)
                    
                    setattr(item, "Function99", self)
                    

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
                if hasattr(item, "domains_Domain96"):
                    opp_val = getattr(item, "domains_Domain96", None)
                    
                    if opp_val == self:
                        setattr(item, "domains_Domain96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domains_Domain96"):
                    opp_val = getattr(item, "domains_Domain96", None)
                    
                    setattr(item, "domains_Domain96", self)
                    

class asmeta_structure_ExportClause:

    pass
class domains_StructuredTd:

    pass
class Header:

    pass
class asmeta_structure_Signature:

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

    def __init__(self, isAsynchr: str, asmeta_structure_Asm: set["Initialization"] = None, Initialization136: "Initialization" = None, Body: "Body" = None, Header141: "Header" = None, asmeta_structure_Asm144: "basictransitionrules_MacroDeclaration" = None):
        self.isAsynchr = isAsynchr
        self.asmeta_structure_Asm = asmeta_structure_Asm if asmeta_structure_Asm is not None else set()
        self.Initialization136 = Initialization136
        self.Body = Body
        self.Header141 = Header141
        self.asmeta_structure_Asm144 = asmeta_structure_Asm144
        
    @property
    def isAsynchr(self) -> str:
        return self.__isAsynchr

    @isAsynchr.setter
    def isAsynchr(self, isAsynchr: str):
        self.__isAsynchr = isAsynchr

    @property
    def asmeta_structure_Asm144(self):
        return self.__asmeta_structure_Asm144

    @asmeta_structure_Asm144.setter
    def asmeta_structure_Asm144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asmeta_structure_Asm144", None)
        self.__asmeta_structure_Asm144 = value
        
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
    def Header141(self):
        return self.__Header141

    @Header141.setter
    def Header141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__Header141", None)
        self.__Header141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure142"):
                opp_val = getattr(old_value, "structure142", None)
                if opp_val == self:
                    setattr(old_value, "structure142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure142"):
                opp_val = getattr(value, "structure142", None)
                setattr(value, "structure142", self)

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
                if hasattr(item, "Initialization134"):
                    opp_val = getattr(item, "Initialization134", None)
                    
                    if opp_val == self:
                        setattr(item, "Initialization134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Initialization134"):
                    opp_val = getattr(item, "Initialization134", None)
                    
                    setattr(item, "Initialization134", self)
                    

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
            if hasattr(old_value, "structure139"):
                opp_val = getattr(old_value, "structure139", None)
                if opp_val == self:
                    setattr(old_value, "structure139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure139"):
                opp_val = getattr(value, "structure139", None)
                setattr(value, "structure139", self)

    @property
    def Initialization136(self):
        return self.__Initialization136

    @Initialization136.setter
    def Initialization136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__Initialization136", None)
        self.__Initialization136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure137"):
                opp_val = getattr(old_value, "structure137", None)
                if opp_val == self:
                    setattr(old_value, "structure137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure137"):
                opp_val = getattr(value, "structure137", None)
                setattr(value, "structure137", self)

class asmeta_structure_Initialization(NamedElement):

    pass
class asmeta_structure_FunctionInitialization:

    pass
class Asm:

    pass
class DomainDefinition:

    pass
class Property:

    pass
class asmeta_definitions_Invariant(Property):

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

class domains_ConcreteDomain:

    pass
class Term:

    pass
class asmeta_basicterms_BasicTerm(Term):

    pass
class asmeta_basicterms_ExtendedTerm(Term):

    pass
class asmeta_structure_DomainInitialization:

    pass
class FunctionTerm:

    pass
class asmeta_basicterms_LocationTerm(FunctionTerm):

    pass
class DynamicFunction:

    pass
class asmeta_definitions_OutFunction(DynamicFunction):

    pass
class asmeta_definitions_LocalFunction(DynamicFunction):

    pass
class asmeta_definitions_SharedFunction(DynamicFunction):

    pass
class asmeta_definitions_ControlledFunction(DynamicFunction):

    pass
class asmeta_definitions_MonitoredFunction(DynamicFunction):

    pass
class RuleDeclaration:

    pass
class asmeta_turbotransitionrules_TurboDeclaration(RuleDeclaration):

    pass
class asmeta_basictransitionrules_MacroDeclaration(RuleDeclaration):

    pass
class furtherterms_FiniteQuantificationTerm:

    pass
class BasicTerm:

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

class asmeta_basicterms_VariableTerm(BasicTerm):

    def __init__(self, name: str, kind: str, furtherterms: "furtherterms_FiniteQuantificationTerm" = None):
        self.name = name
        self.kind = kind
        self.furtherterms = furtherterms
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class Function:

    pass
class asmeta_definitions_DerivedFunction(Function):

    pass
class asmeta_definitions_BasicFunction(Function):

    pass
class asmeta_basicterms_FunctionTerm(BasicTerm):

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
class ComprehensionTerm:

    pass
class asmeta_furtherterms_BagCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_SetCt(ComprehensionTerm):

    pass
class ExtendedTerm:

    pass
class asmeta_basicterms_DomainTerm(ExtendedTerm):

    pass
class asmeta_furtherterms_ConditionalTerm(ExtendedTerm):

    pass
class asmeta_basicterms_CollectionTerm(ExtendedTerm):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class asmeta_basicterms_RuleAsTerm(ExtendedTerm):

    pass
class asmeta_basicterms_TupleTerm(ExtendedTerm):

    def __init__(self, arity: str, terms: str):
        self.arity = arity
        self.terms = terms
        
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
                    

class asmeta_furtherterms_VariableBindingTerm(ExtendedTerm):

    pass
class ConstantTerm:

    pass
class asmeta_basicterms_UndefTerm(ConstantTerm):

    pass
class asmeta_furtherterms_ComplexTerm(ConstantTerm):

    pass
class asmeta_furtherterms_NaturalTerm(ConstantTerm):

    pass
class asmeta_basicterms_BooleanTerm(ConstantTerm):

    pass
class asmeta_furtherterms_StringTerm(ConstantTerm):

    pass
class asmeta_furtherterms_EnumTerm(ConstantTerm):

    pass
class asmeta_furtherterms_CharTerm(ConstantTerm):

    pass
class asmeta_furtherterms_IntegerTerm(ConstantTerm):

    pass
class VariableBindingTerm:

    pass
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
                    

class asmeta_furtherterms_LetTerm(VariableBindingTerm):

    pass
class asmeta_furtherterms_MapCt(ComprehensionTerm):

    pass
class basicterms_TupleTerm:

    pass
class asmeta_furtherterms_RealTerm(ConstantTerm):

    pass
class asmeta_furtherterms_SequenceCt(ComprehensionTerm):

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

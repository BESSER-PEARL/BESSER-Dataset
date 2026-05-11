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
class domains_TypeDomain:

    pass
class asmeta_domains_EnumElement:

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class domains_EnumElement:

    pass
class RealDomain:

    pass
class asmeta_domains_IntegerDomain(RealDomain):

    pass
class TemporalProperty:

    pass
class asmeta_definitions_LtlSpec(TemporalProperty):

    pass
class asmeta_definitions_CtlSpec(TemporalProperty):

    pass
class StructuredTd:

    pass
class asmeta_domains_BagDomain(StructuredTd):

    pass
class asmeta_domains_RuleDomain(StructuredTd):

    def __init__(self, domains: str):
        self.domains = domains
        
        pass
    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains


class asmeta_domains_PowersetDomain(StructuredTd):

    pass
class asmeta_domains_ProductDomain(StructuredTd):

    def __init__(self, domains: str):
        self.domains = domains
        
        pass
    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains


class asmeta_domains_MapDomain(StructuredTd):

    pass
class asmeta_domains_SequenceDomain(StructuredTd):

    pass
class TypeDomain:

    pass
class asmeta_domains_EnumTd(TypeDomain):

    pass
class asmeta_domains_AnyDomain(TypeDomain):

    pass
class asmeta_domains_BasicTd(TypeDomain):

    pass
class asmeta_domains_AbstractTd(TypeDomain):

    def __init__(self, isDynamic: str):
        self.isDynamic = isDynamic
        
        pass
    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


class asmeta_domains_StructuredTd(TypeDomain):

    pass
class Domain:

    pass
class asmeta_domains_ConcreteDomain(Domain):

    def __init__(self, isDynamic: str, initializedDomain: set["DomainInitialization"] = None, definedDomain: "DomainDefinition" = None, asmeta_domains_ConcreteDomain: "domains_TypeDomain" = None):
        self.isDynamic = isDynamic
        self.initializedDomain = initializedDomain if initializedDomain is not None else set()
        self.definedDomain = definedDomain
        self.asmeta_domains_ConcreteDomain = asmeta_domains_ConcreteDomain
        
        pass
    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


    @property
    def initializedDomain(self):
        return self.__initializedDomain

    @initializedDomain.setter
    def initializedDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__initializedDomain", None)
        self.__initializedDomain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainInitialization286"):
                    opp_val = getattr(item, "DomainInitialization286", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainInitialization286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainInitialization286"):
                    opp_val = getattr(item, "DomainInitialization286", None)
                    
                    setattr(item, "DomainInitialization286", self)
                    

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
    def definedDomain(self):
        return self.__definedDomain

    @definedDomain.setter
    def definedDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_ConcreteDomain__definedDomain", None)
        self.__definedDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainDefinition288"):
                opp_val = getattr(old_value, "DomainDefinition288", None)
                if opp_val == self:
                    setattr(old_value, "DomainDefinition288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainDefinition288"):
                opp_val = getattr(value, "DomainDefinition288", None)
                setattr(value, "DomainDefinition288", self)

class asmeta_domains_TypeDomain(Domain):

    pass
class BasicTd:

    pass
class asmeta_domains_ComplexDomain(BasicTd):

    pass
class asmeta_domains_BooleanDomain(BasicTd):

    pass
class asmeta_domains_CharDomain(BasicTd):

    pass
class asmeta_domains_StringDomain(BasicTd):

    pass
class asmeta_domains_UndefDomain(BasicTd):

    pass
class IntegerDomain:

    pass
class asmeta_domains_NaturalDomain(IntegerDomain):

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
class asmeta_definitions_Property(Classifier):

    pass
class asmeta_definitions_InvarConstraint(Classifier):

    pass
class asmeta_definitions_FairnessConstraint(Classifier):

    pass
class asmeta_definitions_Function(Classifier):

    def __init__(self, arity: str, asmeta_definitions_Function: "domains_Domain" = None, asmeta_definitions_Function252: "domains_Domain" = None, definedFunction: "FunctionDefinition" = None, constrainedFunction: set["Invariant"] = None, function: "Signature" = None):
        self.arity = arity
        self.asmeta_definitions_Function = asmeta_definitions_Function
        self.asmeta_definitions_Function252 = asmeta_definitions_Function252
        self.definedFunction = definedFunction
        self.constrainedFunction = constrainedFunction if constrainedFunction is not None else set()
        self.function = function
        
        pass
    @property
    def arity(self):
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity


    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__function", None)
        self.__function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature259"):
                opp_val = getattr(old_value, "Signature259", None)
                if opp_val == self:
                    setattr(old_value, "Signature259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature259"):
                opp_val = getattr(value, "Signature259", None)
                setattr(value, "Signature259", self)

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
            if hasattr(old_value, "domains_Domain250"):
                opp_val = getattr(old_value, "domains_Domain250", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain250"):
                opp_val = getattr(value, "domains_Domain250", None)
                setattr(value, "domains_Domain250", self)

    @property
    def asmeta_definitions_Function252(self):
        return self.__asmeta_definitions_Function252

    @asmeta_definitions_Function252.setter
    def asmeta_definitions_Function252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__asmeta_definitions_Function252", None)
        self.__asmeta_definitions_Function252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains_Domain253"):
                opp_val = getattr(old_value, "domains_Domain253", None)
                if opp_val == self:
                    setattr(old_value, "domains_Domain253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains_Domain253"):
                opp_val = getattr(value, "domains_Domain253", None)
                setattr(value, "domains_Domain253", self)

    @property
    def definedFunction(self):
        return self.__definedFunction

    @definedFunction.setter
    def definedFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__definedFunction", None)
        self.__definedFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FunctionDefinition255"):
                opp_val = getattr(old_value, "FunctionDefinition255", None)
                if opp_val == self:
                    setattr(old_value, "FunctionDefinition255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FunctionDefinition255"):
                opp_val = getattr(value, "FunctionDefinition255", None)
                setattr(value, "FunctionDefinition255", self)

    @property
    def constrainedFunction(self):
        return self.__constrainedFunction

    @constrainedFunction.setter
    def constrainedFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_Function__constrainedFunction", None)
        self.__constrainedFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invariant257"):
                    opp_val = getattr(item, "Invariant257", None)
                    
                    if opp_val == self:
                        setattr(item, "Invariant257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invariant257"):
                    opp_val = getattr(item, "Invariant257", None)
                    
                    setattr(item, "Invariant257", self)
                    

class asmeta_domains_Domain(Classifier):

    def __init__(self, constrainedDomain: set["Invariant"] = None, domain: "Signature" = None):
        self.constrainedDomain = constrainedDomain if constrainedDomain is not None else set()
        self.domain = domain
        
        pass
    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__domain", None)
        self.__domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature284"):
                opp_val = getattr(old_value, "Signature284", None)
                if opp_val == self:
                    setattr(old_value, "Signature284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature284"):
                opp_val = getattr(value, "Signature284", None)
                setattr(value, "Signature284", self)

    @property
    def constrainedDomain(self):
        return self.__constrainedDomain

    @constrainedDomain.setter
    def constrainedDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_domains_Domain__constrainedDomain", None)
        self.__constrainedDomain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invariant282"):
                    opp_val = getattr(item, "Invariant282", None)
                    
                    if opp_val == self:
                        setattr(item, "Invariant282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invariant282"):
                    opp_val = getattr(item, "Invariant282", None)
                    
                    setattr(item, "Invariant282", self)
                    

    def compatible(self):
        # TODO: Implement compatible method
        pass

class asmeta_definitions_RuleDeclaration(Classifier):

    def __init__(self, arity: str, asmeta_definitions_RuleDeclaration: set["basicterms_VariableTerm"] = None, constrainedRule: set["Invariant"] = None, asmeta_definitions_RuleDeclaration233: "basictransitionrules_Rule" = None, ruleDeclaration: "Body" = None):
        self.arity = arity
        self.asmeta_definitions_RuleDeclaration = asmeta_definitions_RuleDeclaration if asmeta_definitions_RuleDeclaration is not None else set()
        self.constrainedRule = constrainedRule if constrainedRule is not None else set()
        self.asmeta_definitions_RuleDeclaration233 = asmeta_definitions_RuleDeclaration233
        self.ruleDeclaration = ruleDeclaration
        
        pass
    @property
    def arity(self):
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity


    @property
    def asmeta_definitions_RuleDeclaration233(self):
        return self.__asmeta_definitions_RuleDeclaration233

    @asmeta_definitions_RuleDeclaration233.setter
    def asmeta_definitions_RuleDeclaration233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__asmeta_definitions_RuleDeclaration233", None)
        self.__asmeta_definitions_RuleDeclaration233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule234"):
                opp_val = getattr(old_value, "basictransitionrules_Rule234", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule234"):
                opp_val = getattr(value, "basictransitionrules_Rule234", None)
                setattr(value, "basictransitionrules_Rule234", self)

    @property
    def constrainedRule(self):
        return self.__constrainedRule

    @constrainedRule.setter
    def constrainedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__constrainedRule", None)
        self.__constrainedRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invariant"):
                    opp_val = getattr(item, "Invariant", None)
                    
                    if opp_val == self:
                        setattr(item, "Invariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invariant"):
                    opp_val = getattr(item, "Invariant", None)
                    
                    setattr(item, "Invariant", self)
                    

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
                if hasattr(item, "basicterms_VariableTerm230"):
                    opp_val = getattr(item, "basicterms_VariableTerm230", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm230"):
                    opp_val = getattr(item, "basicterms_VariableTerm230", None)
                    
                    setattr(item, "basicterms_VariableTerm230", self)
                    

    @property
    def ruleDeclaration(self):
        return self.__ruleDeclaration

    @ruleDeclaration.setter
    def ruleDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_definitions_RuleDeclaration__ruleDeclaration", None)
        self.__ruleDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Body236"):
                opp_val = getattr(old_value, "Body236", None)
                if opp_val == self:
                    setattr(old_value, "Body236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Body236"):
                opp_val = getattr(value, "Body236", None)
                setattr(value, "Body236", self)

class BasicRule:

    pass
class asmeta_basictransitionrules_LetRule(BasicRule):

    pass
class asmeta_basictransitionrules_SkipRule(BasicRule):

    pass
class asmeta_basictransitionrules_ExtendRule(BasicRule):

    pass
class asmeta_basictransitionrules_MacroCallRule(BasicRule):

    def __init__(self, parameters: str, asmeta_basictransitionrules_MacroCallRule: "basictransitionrules_MacroDeclaration" = None):
        self.parameters = parameters
        self.asmeta_basictransitionrules_MacroCallRule = asmeta_basictransitionrules_MacroCallRule
        
        pass
    @property
    def parameters(self):
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
            if hasattr(old_value, "basictransitionrules_MacroDeclaration191"):
                opp_val = getattr(old_value, "basictransitionrules_MacroDeclaration191", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_MacroDeclaration191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_MacroDeclaration191"):
                opp_val = getattr(value, "basictransitionrules_MacroDeclaration191", None)
                setattr(value, "basictransitionrules_MacroDeclaration191", self)

class asmeta_basictransitionrules_ForallRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ForallRule206: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ForallRule: set["basicterms_VariableTerm"] = None, asmeta_basictransitionrules_ForallRule203: "basicterms_Term" = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ForallRule206 = asmeta_basictransitionrules_ForallRule206
        self.asmeta_basictransitionrules_ForallRule = asmeta_basictransitionrules_ForallRule if asmeta_basictransitionrules_ForallRule is not None else set()
        self.asmeta_basictransitionrules_ForallRule203 = asmeta_basictransitionrules_ForallRule203
        
        pass
    @property
    def ranges(self):
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges


    @property
    def asmeta_basictransitionrules_ForallRule206(self):
        return self.__asmeta_basictransitionrules_ForallRule206

    @asmeta_basictransitionrules_ForallRule206.setter
    def asmeta_basictransitionrules_ForallRule206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule206", None)
        self.__asmeta_basictransitionrules_ForallRule206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule207"):
                opp_val = getattr(old_value, "basictransitionrules_Rule207", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule207"):
                opp_val = getattr(value, "basictransitionrules_Rule207", None)
                setattr(value, "basictransitionrules_Rule207", self)

    @property
    def asmeta_basictransitionrules_ForallRule203(self):
        return self.__asmeta_basictransitionrules_ForallRule203

    @asmeta_basictransitionrules_ForallRule203.setter
    def asmeta_basictransitionrules_ForallRule203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ForallRule__asmeta_basictransitionrules_ForallRule203", None)
        self.__asmeta_basictransitionrules_ForallRule203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term204"):
                opp_val = getattr(old_value, "basicterms_Term204", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term204"):
                opp_val = getattr(value, "basicterms_Term204", None)
                setattr(value, "basicterms_Term204", self)

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
                if hasattr(item, "basicterms_VariableTerm201"):
                    opp_val = getattr(item, "basicterms_VariableTerm201", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm201"):
                    opp_val = getattr(item, "basicterms_VariableTerm201", None)
                    
                    setattr(item, "basicterms_VariableTerm201", self)
                    

class asmeta_basictransitionrules_UpdateRule(BasicRule):

    pass
class asmeta_basictransitionrules_ConditionalRule(BasicRule):

    pass
class asmeta_basictransitionrules_BlockRule(BasicRule):

    def __init__(self, rules: str):
        self.rules = rules
        
        pass
    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


class asmeta_basictransitionrules_ChooseRule(BasicRule):

    def __init__(self, ranges: str, asmeta_basictransitionrules_ChooseRule188: set["basicterms_VariableTerm"] = None, asmeta_basictransitionrules_ChooseRule: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule182: "basictransitionrules_Rule" = None, asmeta_basictransitionrules_ChooseRule185: "basicterms_Term" = None):
        self.ranges = ranges
        self.asmeta_basictransitionrules_ChooseRule188 = asmeta_basictransitionrules_ChooseRule188 if asmeta_basictransitionrules_ChooseRule188 is not None else set()
        self.asmeta_basictransitionrules_ChooseRule = asmeta_basictransitionrules_ChooseRule
        self.asmeta_basictransitionrules_ChooseRule182 = asmeta_basictransitionrules_ChooseRule182
        self.asmeta_basictransitionrules_ChooseRule185 = asmeta_basictransitionrules_ChooseRule185
        
        pass
    @property
    def ranges(self):
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges


    @property
    def asmeta_basictransitionrules_ChooseRule182(self):
        return self.__asmeta_basictransitionrules_ChooseRule182

    @asmeta_basictransitionrules_ChooseRule182.setter
    def asmeta_basictransitionrules_ChooseRule182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule182", None)
        self.__asmeta_basictransitionrules_ChooseRule182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule183"):
                opp_val = getattr(old_value, "basictransitionrules_Rule183", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule183"):
                opp_val = getattr(value, "basictransitionrules_Rule183", None)
                setattr(value, "basictransitionrules_Rule183", self)

    @property
    def asmeta_basictransitionrules_ChooseRule188(self):
        return self.__asmeta_basictransitionrules_ChooseRule188

    @asmeta_basictransitionrules_ChooseRule188.setter
    def asmeta_basictransitionrules_ChooseRule188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule188", None)
        self.__asmeta_basictransitionrules_ChooseRule188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_VariableTerm189"):
                    opp_val = getattr(item, "basicterms_VariableTerm189", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_VariableTerm189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_VariableTerm189"):
                    opp_val = getattr(item, "basicterms_VariableTerm189", None)
                    
                    setattr(item, "basicterms_VariableTerm189", self)
                    

    @property
    def asmeta_basictransitionrules_ChooseRule185(self):
        return self.__asmeta_basictransitionrules_ChooseRule185

    @asmeta_basictransitionrules_ChooseRule185.setter
    def asmeta_basictransitionrules_ChooseRule185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_ChooseRule__asmeta_basictransitionrules_ChooseRule185", None)
        self.__asmeta_basictransitionrules_ChooseRule185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicterms_Term186"):
                opp_val = getattr(old_value, "basicterms_Term186", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term186"):
                opp_val = getattr(value, "basicterms_Term186", None)
                setattr(value, "basicterms_Term186", self)

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
            if hasattr(old_value, "basictransitionrules_Rule180"):
                opp_val = getattr(old_value, "basictransitionrules_Rule180", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule180"):
                opp_val = getattr(value, "basictransitionrules_Rule180", None)
                setattr(value, "basictransitionrules_Rule180", self)

class asmeta_basictransitionrules_Rule(ABC):

    pass
class TurboDerivedRule:

    pass
class asmeta_derivedtransitionrules_RecursiveWhileRule(TurboDerivedRule):

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

    def __init__(self, caseBranches: str, asmeta_derivedtransitionrules_CaseRule: "basicterms_Term" = None, asmeta_derivedtransitionrules_CaseRule173: set["basicterms_Term"] = None, asmeta_derivedtransitionrules_CaseRule176: "basictransitionrules_Rule" = None):
        self.caseBranches = caseBranches
        self.asmeta_derivedtransitionrules_CaseRule = asmeta_derivedtransitionrules_CaseRule
        self.asmeta_derivedtransitionrules_CaseRule173 = asmeta_derivedtransitionrules_CaseRule173 if asmeta_derivedtransitionrules_CaseRule173 is not None else set()
        self.asmeta_derivedtransitionrules_CaseRule176 = asmeta_derivedtransitionrules_CaseRule176
        
        pass
    @property
    def caseBranches(self):
        return self.__caseBranches

    @caseBranches.setter
    def caseBranches(self, caseBranches: str):
        self.__caseBranches = caseBranches


    @property
    def asmeta_derivedtransitionrules_CaseRule176(self):
        return self.__asmeta_derivedtransitionrules_CaseRule176

    @asmeta_derivedtransitionrules_CaseRule176.setter
    def asmeta_derivedtransitionrules_CaseRule176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule176", None)
        self.__asmeta_derivedtransitionrules_CaseRule176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basictransitionrules_Rule177"):
                opp_val = getattr(old_value, "basictransitionrules_Rule177", None)
                if opp_val == self:
                    setattr(old_value, "basictransitionrules_Rule177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basictransitionrules_Rule177"):
                opp_val = getattr(value, "basictransitionrules_Rule177", None)
                setattr(value, "basictransitionrules_Rule177", self)

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
            if hasattr(old_value, "basicterms_Term171"):
                opp_val = getattr(old_value, "basicterms_Term171", None)
                if opp_val == self:
                    setattr(old_value, "basicterms_Term171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicterms_Term171"):
                opp_val = getattr(value, "basicterms_Term171", None)
                setattr(value, "basicterms_Term171", self)

    @property
    def asmeta_derivedtransitionrules_CaseRule173(self):
        return self.__asmeta_derivedtransitionrules_CaseRule173

    @asmeta_derivedtransitionrules_CaseRule173.setter
    def asmeta_derivedtransitionrules_CaseRule173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_derivedtransitionrules_CaseRule__asmeta_derivedtransitionrules_CaseRule173", None)
        self.__asmeta_derivedtransitionrules_CaseRule173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicterms_Term174"):
                    opp_val = getattr(item, "basicterms_Term174", None)
                    
                    if opp_val == self:
                        setattr(item, "basicterms_Term174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicterms_Term174"):
                    opp_val = getattr(item, "basicterms_Term174", None)
                    
                    setattr(item, "basicterms_Term174", self)
                    

class asmeta_derivedtransitionrules_IterativeWhileRule(TurboDerivedRule):

    pass
class Rule:

    pass
class asmeta_derivedtransitionrules_DerivedRule(Rule):

    pass
class asmeta_basictransitionrules_TermAsRule(Rule):

    def __init__(self, parameters: str, termAsRule: "basicterms_Term" = None):
        self.parameters = parameters
        self.termAsRule = termAsRule
        
        pass
    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


    @property
    def termAsRule(self):
        return self.__termAsRule

    @termAsRule.setter
    def termAsRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basictransitionrules_TermAsRule__termAsRule", None)
        self.__termAsRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term"):
                opp_val = getattr(old_value, "Term", None)
                if opp_val == self:
                    setattr(old_value, "Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term"):
                opp_val = getattr(value, "Term", None)
                setattr(value, "Term", self)

class asmeta_basictransitionrules_BasicRule(Rule):

    pass
class asmeta_turbotransitionrules_TurboRule(Rule):

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
class asmeta_turbotransitionrules_TurboCallRule(TurboRule):

    def __init__(self, parameters: str, asmeta_turbotransitionrules_TurboCallRule: "turbotransitionrules_TurboDeclaration" = None):
        self.parameters = parameters
        self.asmeta_turbotransitionrules_TurboCallRule = asmeta_turbotransitionrules_TurboCallRule
        
        pass
    @property
    def parameters(self):
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

class asmeta_turbotransitionrules_TurboLocalStateRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TurboReturnRule(TurboRule):

    pass
class asmeta_turbotransitionrules_IterateRule(TurboRule):

    pass
class asmeta_turbotransitionrules_TryCatchRule(TurboRule):

    pass
class asmeta_turbotransitionrules_SeqRule(TurboRule):

    def __init__(self, rules: str):
        self.rules = rules
        
        pass
    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


class asmeta_structure_DomainDefinition:

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
class AgentInitialization:

    pass
class FunctionInitialization:

    pass
class DomainInitialization:

    pass
class NamedElement:

    pass
class asmeta_structure_Asm(NamedElement):

    def __init__(self, isAsynchr: str, asmeta_structure_Asm: set["Initialization"] = None, asm: "Initialization" = None, asm131: "Body" = None, asm133: "Header" = None, asmeta_structure_Asm136: "basictransitionrules_MacroDeclaration" = None):
        self.isAsynchr = isAsynchr
        self.asmeta_structure_Asm = asmeta_structure_Asm if asmeta_structure_Asm is not None else set()
        self.asm = asm
        self.asm131 = asm131
        self.asm133 = asm133
        self.asmeta_structure_Asm136 = asmeta_structure_Asm136
        
        pass
    @property
    def isAsynchr(self):
        return self.__isAsynchr

    @isAsynchr.setter
    def isAsynchr(self, isAsynchr: str):
        self.__isAsynchr = isAsynchr


    @property
    def asm(self):
        return self.__asm

    @asm.setter
    def asm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asm", None)
        self.__asm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Initialization129"):
                opp_val = getattr(old_value, "Initialization129", None)
                if opp_val == self:
                    setattr(old_value, "Initialization129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Initialization129"):
                opp_val = getattr(value, "Initialization129", None)
                setattr(value, "Initialization129", self)

    @property
    def asmeta_structure_Asm136(self):
        return self.__asmeta_structure_Asm136

    @asmeta_structure_Asm136.setter
    def asmeta_structure_Asm136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asmeta_structure_Asm136", None)
        self.__asmeta_structure_Asm136 = value
        
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
    def asm131(self):
        return self.__asm131

    @asm131.setter
    def asm131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asm131", None)
        self.__asm131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Body"):
                opp_val = getattr(old_value, "Body", None)
                if opp_val == self:
                    setattr(old_value, "Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Body"):
                opp_val = getattr(value, "Body", None)
                setattr(value, "Body", self)

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
                if hasattr(item, "Initialization127"):
                    opp_val = getattr(item, "Initialization127", None)
                    
                    if opp_val == self:
                        setattr(item, "Initialization127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Initialization127"):
                    opp_val = getattr(item, "Initialization127", None)
                    
                    setattr(item, "Initialization127", self)
                    

    @property
    def asm133(self):
        return self.__asm133

    @asm133.setter
    def asm133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_Asm__asm133", None)
        self.__asm133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Header134"):
                opp_val = getattr(old_value, "Header134", None)
                if opp_val == self:
                    setattr(old_value, "Header134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Header134"):
                opp_val = getattr(value, "Header134", None)
                setattr(value, "Header134", self)

class asmeta_definitions_Classifier(NamedElement):

    pass
class asmeta_structure_Initialization(NamedElement):

    pass
class domains_ConcreteDomain:

    pass
class asmeta_structure_DomainInitialization:

    pass
class asmeta_structure_FunctionDefinition:

    pass
class asmeta_structure_ImportClause:

    def __init__(self, moduleName: str, asmeta_structure_ImportClause98: set["RuleDeclaration"] = None, asmeta_structure_ImportClause: set["domains_Domain"] = None, asmeta_structure_ImportClause95: set["Function"] = None):
        self.moduleName = moduleName
        self.asmeta_structure_ImportClause98 = asmeta_structure_ImportClause98 if asmeta_structure_ImportClause98 is not None else set()
        self.asmeta_structure_ImportClause = asmeta_structure_ImportClause if asmeta_structure_ImportClause is not None else set()
        self.asmeta_structure_ImportClause95 = asmeta_structure_ImportClause95 if asmeta_structure_ImportClause95 is not None else set()
        
        pass
    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


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
                if hasattr(item, "RuleDeclaration99"):
                    opp_val = getattr(item, "RuleDeclaration99", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleDeclaration99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleDeclaration99"):
                    opp_val = getattr(item, "RuleDeclaration99", None)
                    
                    setattr(item, "RuleDeclaration99", self)
                    

    @property
    def asmeta_structure_ImportClause95(self):
        return self.__asmeta_structure_ImportClause95

    @asmeta_structure_ImportClause95.setter
    def asmeta_structure_ImportClause95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_structure_ImportClause__asmeta_structure_ImportClause95", None)
        self.__asmeta_structure_ImportClause95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function96"):
                    opp_val = getattr(item, "Function96", None)
                    
                    if opp_val == self:
                        setattr(item, "Function96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function96"):
                    opp_val = getattr(item, "Function96", None)
                    
                    setattr(item, "Function96", self)
                    

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
                if hasattr(item, "domains_Domain93"):
                    opp_val = getattr(item, "domains_Domain93", None)
                    
                    if opp_val == self:
                        setattr(item, "domains_Domain93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domains_Domain93"):
                    opp_val = getattr(item, "domains_Domain93", None)
                    
                    setattr(item, "domains_Domain93", self)
                    

class asmeta_structure_ExportClause:

    pass
class domains_StructuredTd:

    pass
class Header:

    pass
class asmeta_structure_Signature:

    pass
class basictransitionrules_MacroCallRule:

    pass
class asmeta_structure_AgentInitialization:

    pass
class asmeta_structure_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class DynamicFunction:

    pass
class asmeta_definitions_ControlledFunction(DynamicFunction):

    pass
class asmeta_definitions_MonitoredFunction(DynamicFunction):

    pass
class asmeta_definitions_SharedFunction(DynamicFunction):

    pass
class asmeta_definitions_LocalFunction(DynamicFunction):

    pass
class asmeta_definitions_OutFunction(DynamicFunction):

    pass
class asmeta_structure_FunctionInitialization:

    pass
class InvarConstraint:

    pass
class FairnessConstraint:

    pass
class asmeta_definitions_JusticeConstraint(FairnessConstraint):

    pass
class asmeta_definitions_CompassionConstraint(FairnessConstraint):

    pass
class Asm:

    pass
class DomainDefinition:

    pass
class Property:

    pass
class asmeta_definitions_TemporalProperty(Property):

    pass
class asmeta_definitions_Invariant(Property):

    pass
class FunctionDefinition:

    pass
class asmeta_structure_Body:

    pass
class Initialization:

    pass
class RuleDeclaration:

    pass
class asmeta_turbotransitionrules_TurboDeclaration(RuleDeclaration):

    pass
class asmeta_basictransitionrules_MacroDeclaration(RuleDeclaration):

    pass
class basictransitionrules_TermAsRule:

    pass
class domains_Domain:

    pass
class asmeta_basicterms_Term(ABC):

    def __init__(self, asmeta_basicterms_Term: "domains_Domain" = None, term: set["basictransitionrules_TermAsRule"] = None):
        self.asmeta_basicterms_Term = asmeta_basicterms_Term
        self.term = term if term is not None else set()
        
        pass
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

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basicterms_Term__term", None)
        self.__term = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TermAsRule"):
                    opp_val = getattr(item, "TermAsRule", None)
                    
                    if opp_val == self:
                        setattr(item, "TermAsRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TermAsRule"):
                    opp_val = getattr(item, "TermAsRule", None)
                    
                    setattr(item, "TermAsRule", self)
                    

    def compatible(self):
        # TODO: Implement compatible method
        pass

class Term:

    pass
class asmeta_basicterms_BasicTerm(Term):

    pass
class asmeta_basicterms_ExtendedTerm(Term):

    pass
class Function:

    pass
class asmeta_definitions_DerivedFunction(Function):

    pass
class asmeta_definitions_BasicFunction(Function):

    pass
class FunctionTerm:

    pass
class asmeta_basicterms_LocationTerm(FunctionTerm):

    pass
class furtherterms_FiniteQuantificationTerm:

    pass
class BasicTerm:

    pass
class asmeta_basicterms_ConstantTerm(BasicTerm):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class asmeta_basicterms_FunctionTerm(BasicTerm):

    pass
class asmeta_basicterms_VariableTerm(BasicTerm):

    def __init__(self, name: str, kind: str, variable: "furtherterms_FiniteQuantificationTerm" = None):
        self.name = name
        self.kind = kind
        self.variable = variable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_basicterms_VariableTerm__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteQuantificationTerm"):
                opp_val = getattr(old_value, "FiniteQuantificationTerm", None)
                if opp_val == self:
                    setattr(old_value, "FiniteQuantificationTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteQuantificationTerm"):
                opp_val = getattr(value, "FiniteQuantificationTerm", None)
                setattr(value, "FiniteQuantificationTerm", self)

class CollectionTerm:

    pass
class asmeta_furtherterms_BagTerm(CollectionTerm):

    pass
class asmeta_basicterms_SetTerm(CollectionTerm):

    pass
class asmeta_furtherterms_MapTerm(CollectionTerm):

    pass
class asmeta_furtherterms_SequenceTerm(CollectionTerm):

    def __init__(self, terms: str):
        self.terms = terms
        
        pass
    @property
    def terms(self):
        return self.__terms

    @terms.setter
    def terms(self, terms: str):
        self.__terms = terms


class ComprehensionTerm:

    pass
class asmeta_furtherterms_SequenceCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_BagCt(ComprehensionTerm):

    pass
class asmeta_furtherterms_SetCt(ComprehensionTerm):

    pass
class ExtendedTerm:

    pass
class asmeta_basicterms_RuleAsTerm(ExtendedTerm):

    pass
class asmeta_basicterms_DomainTerm(ExtendedTerm):

    pass
class asmeta_basicterms_CollectionTerm(ExtendedTerm):

    def __init__(self, size: str):
        self.size = size
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


class asmeta_furtherterms_CaseTerm(ExtendedTerm):

    def __init__(self, resultTerms: str, asmeta_furtherterms_CaseTerm: set["basicterms_Term"] = None, asmeta_furtherterms_CaseTerm29: "basicterms_Term" = None, asmeta_furtherterms_CaseTerm32: "basicterms_Term" = None):
        self.resultTerms = resultTerms
        self.asmeta_furtherterms_CaseTerm = asmeta_furtherterms_CaseTerm if asmeta_furtherterms_CaseTerm is not None else set()
        self.asmeta_furtherterms_CaseTerm29 = asmeta_furtherterms_CaseTerm29
        self.asmeta_furtherterms_CaseTerm32 = asmeta_furtherterms_CaseTerm32
        
        pass
    @property
    def resultTerms(self):
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

class asmeta_basicterms_TupleTerm(ExtendedTerm):

    def __init__(self, arity: str, terms: str):
        self.arity = arity
        self.terms = terms
        
        pass
    @property
    def terms(self):
        return self.__terms

    @terms.setter
    def terms(self, terms: str):
        self.__terms = terms


    @property
    def arity(self):
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity


class asmeta_furtherterms_VariableBindingTerm(ExtendedTerm):

    pass
class asmeta_furtherterms_ConditionalTerm(ExtendedTerm):

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
class asmeta_furtherterms_ComprehensionTerm(VariableBindingTerm):

    def __init__(self, ranges: str, asmeta_furtherterms_ComprehensionTerm: set["basicterms_VariableTerm"] = None, asmeta_furtherterms_ComprehensionTerm21: "basicterms_Term" = None, asmeta_furtherterms_ComprehensionTerm24: "basicterms_Term" = None):
        self.ranges = ranges
        self.asmeta_furtherterms_ComprehensionTerm = asmeta_furtherterms_ComprehensionTerm if asmeta_furtherterms_ComprehensionTerm is not None else set()
        self.asmeta_furtherterms_ComprehensionTerm21 = asmeta_furtherterms_ComprehensionTerm21
        self.asmeta_furtherterms_ComprehensionTerm24 = asmeta_furtherterms_ComprehensionTerm24
        
        pass
    @property
    def ranges(self):
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
                    

class asmeta_furtherterms_FiniteQuantificationTerm(VariableBindingTerm):

    def __init__(self, ranges: str, finiteQuantificationTerm: set["basicterms_VariableTerm"] = None, asmeta_furtherterms_FiniteQuantificationTerm: "basicterms_Term" = None):
        self.ranges = ranges
        self.finiteQuantificationTerm = finiteQuantificationTerm if finiteQuantificationTerm is not None else set()
        self.asmeta_furtherterms_FiniteQuantificationTerm = asmeta_furtherterms_FiniteQuantificationTerm
        
        pass
    @property
    def ranges(self):
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
    def finiteQuantificationTerm(self):
        return self.__finiteQuantificationTerm

    @finiteQuantificationTerm.setter
    def finiteQuantificationTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asmeta_furtherterms_FiniteQuantificationTerm__finiteQuantificationTerm", None)
        self.__finiteQuantificationTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableTerm"):
                    opp_val = getattr(item, "VariableTerm", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableTerm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableTerm"):
                    opp_val = getattr(item, "VariableTerm", None)
                    
                    setattr(item, "VariableTerm", self)
                    

class asmeta_furtherterms_LetTerm(VariableBindingTerm):

    pass
class asmeta_furtherterms_MapCt(ComprehensionTerm):

    pass
class basicterms_TupleTerm:

    pass
class ConstantTerm:

    pass
class asmeta_furtherterms_EnumTerm(ConstantTerm):

    pass
class asmeta_basicterms_BooleanTerm(ConstantTerm):

    pass
class asmeta_furtherterms_StringTerm(ConstantTerm):

    pass
class asmeta_furtherterms_NaturalTerm(ConstantTerm):

    pass
class asmeta_furtherterms_CharTerm(ConstantTerm):

    pass
class asmeta_furtherterms_ComplexTerm(ConstantTerm):

    pass
class asmeta_furtherterms_RealTerm(ConstantTerm):

    pass
class asmeta_basicterms_UndefTerm(ConstantTerm):

    pass
class asmeta_furtherterms_IntegerTerm(ConstantTerm):

    pass
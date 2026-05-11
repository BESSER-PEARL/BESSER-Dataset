####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
VariableKind: Enumeration = Enumeration(
    name="VariableKind",
    literals={
            EnumerationLiteral(name="logicalVar"),
			EnumerationLiteral(name="locationVar"),
			EnumerationLiteral(name="ruleVar")
    }
)

# Classes
asmeta_furtherterms_IntegerTerm = Class(name="asmeta_furtherterms_IntegerTerm")
ConstantTerm = Class(name="ConstantTerm")
asmeta_furtherterms_NaturalTerm = Class(name="asmeta_furtherterms_NaturalTerm")
asmeta_furtherterms_VariableBindingTerm = Class(name="asmeta_furtherterms_VariableBindingTerm", is_abstract=True)
ExtendedTerm = Class(name="ExtendedTerm")
asmeta_furtherterms_StringTerm = Class(name="asmeta_furtherterms_StringTerm")
asmeta_furtherterms_SetCt = Class(name="asmeta_furtherterms_SetCt")
ComprehensionTerm = Class(name="ComprehensionTerm")
asmeta_furtherterms_SequenceTerm = Class(name="asmeta_furtherterms_SequenceTerm")
CollectionTerm = Class(name="CollectionTerm")
asmeta_furtherterms_RealTerm = Class(name="asmeta_furtherterms_RealTerm")
asmeta_furtherterms_MapTerm = Class(name="asmeta_furtherterms_MapTerm")
basicterms_TupleTerm = Class(name="basicterms_TupleTerm")
asmeta_furtherterms_MapCt = Class(name="asmeta_furtherterms_MapCt")
asmeta_furtherterms_LetTerm = Class(name="asmeta_furtherterms_LetTerm")
VariableBindingTerm = Class(name="VariableBindingTerm")
basicterms_VariableTerm = Class(name="basicterms_VariableTerm")
basicterms_Term = Class(name="basicterms_Term")
asmeta_furtherterms_ForallTerm = Class(name="asmeta_furtherterms_ForallTerm")
FiniteQuantificationTerm = Class(name="FiniteQuantificationTerm")
asmeta_furtherterms_FiniteQuantificationTerm = Class(name="asmeta_furtherterms_FiniteQuantificationTerm", is_abstract=True)
asmeta_furtherterms_ExistUniqueTerm = Class(name="asmeta_furtherterms_ExistUniqueTerm")
asmeta_furtherterms_ExistTerm = Class(name="asmeta_furtherterms_ExistTerm")
asmeta_furtherterms_EnumTerm = Class(name="asmeta_furtherterms_EnumTerm")
asmeta_furtherterms_ConditionalTerm = Class(name="asmeta_furtherterms_ConditionalTerm")
asmeta_furtherterms_ComprehensionTerm = Class(name="asmeta_furtherterms_ComprehensionTerm", is_abstract=True)
asmeta_furtherterms_SequenceCt = Class(name="asmeta_furtherterms_SequenceCt")
asmeta_furtherterms_ComplexTerm = Class(name="asmeta_furtherterms_ComplexTerm")
asmeta_furtherterms_CharTerm = Class(name="asmeta_furtherterms_CharTerm")
asmeta_furtherterms_CaseTerm = Class(name="asmeta_furtherterms_CaseTerm")
asmeta_furtherterms_BagTerm = Class(name="asmeta_furtherterms_BagTerm")
asmeta_furtherterms_BagCt = Class(name="asmeta_furtherterms_BagCt")
asmeta_basicterms_VariableTerm = Class(name="asmeta_basicterms_VariableTerm")
BasicTerm = Class(name="BasicTerm")
furtherterms_FiniteQuantificationTerm = Class(name="furtherterms_FiniteQuantificationTerm")
asmeta_basicterms_UndefTerm = Class(name="asmeta_basicterms_UndefTerm")
asmeta_basicterms_TupleTerm = Class(name="asmeta_basicterms_TupleTerm")
asmeta_basicterms_SetTerm = Class(name="asmeta_basicterms_SetTerm")
asmeta_basicterms_RuleAsTerm = Class(name="asmeta_basicterms_RuleAsTerm")
RuleDeclaration = Class(name="RuleDeclaration")
asmeta_basicterms_LocationTerm = Class(name="asmeta_basicterms_LocationTerm")
FunctionTerm = Class(name="FunctionTerm")
asmeta_basicterms_FunctionTerm = Class(name="asmeta_basicterms_FunctionTerm")
Function = Class(name="Function")
asmeta_basicterms_ExtendedTerm = Class(name="asmeta_basicterms_ExtendedTerm", is_abstract=True)
Term = Class(name="Term")
asmeta_basicterms_DomainTerm = Class(name="asmeta_basicterms_DomainTerm")
asmeta_basicterms_ConstantTerm = Class(name="asmeta_basicterms_ConstantTerm", is_abstract=True)
asmeta_basicterms_CollectionTerm = Class(name="asmeta_basicterms_CollectionTerm", is_abstract=True)
asmeta_basicterms_BooleanTerm = Class(name="asmeta_basicterms_BooleanTerm")
asmeta_basicterms_BasicTerm = Class(name="asmeta_basicterms_BasicTerm", is_abstract=True)
asmeta_basicterms_Term = Class(name="asmeta_basicterms_Term", is_abstract=True)
domains_Domain = Class(name="domains_Domain")
basictransitionrules_TermAsRule = Class(name="basictransitionrules_TermAsRule")
asmeta_structure_NamedElement = Class(name="asmeta_structure_NamedElement", is_abstract=True)
asmeta_structure_AgentInitialization = Class(name="asmeta_structure_AgentInitialization")
basictransitionrules_MacroCallRule = Class(name="basictransitionrules_MacroCallRule")
Initialization = Class(name="Initialization")
asmeta_structure_Body = Class(name="asmeta_structure_Body")
FunctionDefinition = Class(name="FunctionDefinition")
Property_ = Class(name="Property")
DomainDefinition = Class(name="DomainDefinition")
Asm = Class(name="Asm")
asmeta_structure_FunctionInitialization = Class(name="asmeta_structure_FunctionInitialization")
DynamicFunction = Class(name="DynamicFunction")
asmeta_structure_DomainInitialization = Class(name="asmeta_structure_DomainInitialization")
domains_ConcreteDomain = Class(name="domains_ConcreteDomain")
asmeta_structure_Signature = Class(name="asmeta_structure_Signature")
Header = Class(name="Header")
domains_StructuredTd = Class(name="domains_StructuredTd")
asmeta_structure_ExportClause = Class(name="asmeta_structure_ExportClause")
asmeta_structure_ImportClause = Class(name="asmeta_structure_ImportClause")
asmeta_structure_FunctionDefinition = Class(name="asmeta_structure_FunctionDefinition")
asmeta_structure_DomainDefinition = Class(name="asmeta_structure_DomainDefinition")
asmeta_structure_Initialization = Class(name="asmeta_structure_Initialization")
NamedElement = Class(name="NamedElement")
DomainInitialization = Class(name="DomainInitialization")
FunctionInitialization = Class(name="FunctionInitialization")
AgentInitialization = Class(name="AgentInitialization")
asmeta_structure_Header = Class(name="asmeta_structure_Header")
ImportClause = Class(name="ImportClause")
Signature = Class(name="Signature")
ExportClause = Class(name="ExportClause")
asmeta_structure_Asm = Class(name="asmeta_structure_Asm")
Body = Class(name="Body")
basictransitionrules_MacroDeclaration = Class(name="basictransitionrules_MacroDeclaration")
asmeta_turbotransitionrules_TurboRule = Class(name="asmeta_turbotransitionrules_TurboRule", is_abstract=True)
Rule = Class(name="Rule")
asmeta_turbotransitionrules_TurboDeclaration = Class(name="asmeta_turbotransitionrules_TurboDeclaration")
asmeta_turbotransitionrules_SeqRule = Class(name="asmeta_turbotransitionrules_SeqRule")
TurboRule = Class(name="TurboRule")
asmeta_turbotransitionrules_TurboLocalStateRule = Class(name="asmeta_turbotransitionrules_TurboLocalStateRule")
basictransitionrules_Rule = Class(name="basictransitionrules_Rule")
LocalFunction = Class(name="LocalFunction")
asmeta_turbotransitionrules_TurboCallRule = Class(name="asmeta_turbotransitionrules_TurboCallRule")
turbotransitionrules_TurboDeclaration = Class(name="turbotransitionrules_TurboDeclaration")
asmeta_turbotransitionrules_TurboReturnRule = Class(name="asmeta_turbotransitionrules_TurboReturnRule")
turbotransitionrules_TurboCallRule = Class(name="turbotransitionrules_TurboCallRule")
asmeta_turbotransitionrules_TryCatchRule = Class(name="asmeta_turbotransitionrules_TryCatchRule")
asmeta_turbotransitionrules_IterateRule = Class(name="asmeta_turbotransitionrules_IterateRule")
asmeta_derivedtransitionrules_RecursiveWhileRule = Class(name="asmeta_derivedtransitionrules_RecursiveWhileRule")
TurboDerivedRule = Class(name="TurboDerivedRule")
asmeta_derivedtransitionrules_IterativeWhileRule = Class(name="asmeta_derivedtransitionrules_IterativeWhileRule")
asmeta_derivedtransitionrules_DerivedRule = Class(name="asmeta_derivedtransitionrules_DerivedRule", is_abstract=True)
asmeta_derivedtransitionrules_CaseRule = Class(name="asmeta_derivedtransitionrules_CaseRule")
BasicDerivedRule = Class(name="BasicDerivedRule")
asmeta_derivedtransitionrules_BasicDerivedRule = Class(name="asmeta_derivedtransitionrules_BasicDerivedRule", is_abstract=True)
DerivedRule = Class(name="DerivedRule")
asmeta_derivedtransitionrules_TurboDerivedRule = Class(name="asmeta_derivedtransitionrules_TurboDerivedRule", is_abstract=True)
asmeta_basictransitionrules_TermAsRule = Class(name="asmeta_basictransitionrules_TermAsRule")
asmeta_basictransitionrules_BasicRule = Class(name="asmeta_basictransitionrules_BasicRule", is_abstract=True)
asmeta_basictransitionrules_Rule = Class(name="asmeta_basictransitionrules_Rule", is_abstract=True)
asmeta_basictransitionrules_ChooseRule = Class(name="asmeta_basictransitionrules_ChooseRule")
BasicRule = Class(name="BasicRule")
asmeta_basictransitionrules_MacroCallRule = Class(name="asmeta_basictransitionrules_MacroCallRule")
asmeta_basictransitionrules_BlockRule = Class(name="asmeta_basictransitionrules_BlockRule")
asmeta_basictransitionrules_ConditionalRule = Class(name="asmeta_basictransitionrules_ConditionalRule")
asmeta_basictransitionrules_ForallRule = Class(name="asmeta_basictransitionrules_ForallRule")
asmeta_basictransitionrules_LetRule = Class(name="asmeta_basictransitionrules_LetRule")
asmeta_basictransitionrules_ExtendRule = Class(name="asmeta_basictransitionrules_ExtendRule")
asmeta_basictransitionrules_UpdateRule = Class(name="asmeta_basictransitionrules_UpdateRule")
asmeta_basictransitionrules_SkipRule = Class(name="asmeta_basictransitionrules_SkipRule")
asmeta_basictransitionrules_MacroDeclaration = Class(name="asmeta_basictransitionrules_MacroDeclaration")
asmeta_definitions_RuleDeclaration = Class(name="asmeta_definitions_RuleDeclaration", is_abstract=True)
Classifier = Class(name="Classifier")
Invariant = Class(name="Invariant")
asmeta_definitions_LocalFunction = Class(name="asmeta_definitions_LocalFunction")
asmeta_definitions_ControlledFunction = Class(name="asmeta_definitions_ControlledFunction")
asmeta_definitions_SharedFunction = Class(name="asmeta_definitions_SharedFunction")
asmeta_definitions_MonitoredFunction = Class(name="asmeta_definitions_MonitoredFunction")
asmeta_definitions_OutFunction = Class(name="asmeta_definitions_OutFunction")
asmeta_definitions_DynamicFunction = Class(name="asmeta_definitions_DynamicFunction", is_abstract=True)
BasicFunction = Class(name="BasicFunction")
asmeta_definitions_StaticFunction = Class(name="asmeta_definitions_StaticFunction")
asmeta_definitions_DerivedFunction = Class(name="asmeta_definitions_DerivedFunction")
asmeta_definitions_BasicFunction = Class(name="asmeta_definitions_BasicFunction", is_abstract=True)
asmeta_definitions_Invariant = Class(name="asmeta_definitions_Invariant")
asmeta_definitions_Function = Class(name="asmeta_definitions_Function", is_abstract=True)
asmeta_definitions_Classifier = Class(name="asmeta_definitions_Classifier", is_abstract=True)
asmeta_definitions_Property = Class(name="asmeta_definitions_Property")
asmeta_domains_NaturalDomain = Class(name="asmeta_domains_NaturalDomain")
IntegerDomain = Class(name="IntegerDomain")
asmeta_domains_UndefDomain = Class(name="asmeta_domains_UndefDomain")
BasicTd = Class(name="BasicTd")
asmeta_domains_TypeDomain = Class(name="asmeta_domains_TypeDomain", is_abstract=True)
Domain = Class(name="Domain")
asmeta_domains_StructuredTd = Class(name="asmeta_domains_StructuredTd", is_abstract=True)
TypeDomain = Class(name="TypeDomain")
asmeta_domains_StringDomain = Class(name="asmeta_domains_StringDomain")
asmeta_domains_SequenceDomain = Class(name="asmeta_domains_SequenceDomain")
StructuredTd = Class(name="StructuredTd")
asmeta_domains_RuleDomain = Class(name="asmeta_domains_RuleDomain")
asmeta_domains_ReserveDomain = Class(name="asmeta_domains_ReserveDomain")
AbstractTd = Class(name="AbstractTd")
asmeta_domains_RealDomain = Class(name="asmeta_domains_RealDomain")
ComplexDomain = Class(name="ComplexDomain")
asmeta_domains_ProductDomain = Class(name="asmeta_domains_ProductDomain")
asmeta_domains_PowersetDomain = Class(name="asmeta_domains_PowersetDomain")
asmeta_domains_MapDomain = Class(name="asmeta_domains_MapDomain")
asmeta_domains_IntegerDomain = Class(name="asmeta_domains_IntegerDomain")
RealDomain = Class(name="RealDomain")
asmeta_domains_EnumTd = Class(name="asmeta_domains_EnumTd")
domains_EnumElement = Class(name="domains_EnumElement")
asmeta_domains_EnumElement = Class(name="asmeta_domains_EnumElement")
asmeta_domains_Domain = Class(name="asmeta_domains_Domain", is_abstract=True)
asmeta_domains_ConcreteDomain = Class(name="asmeta_domains_ConcreteDomain")
domains_TypeDomain = Class(name="domains_TypeDomain")
asmeta_domains_ComplexDomain = Class(name="asmeta_domains_ComplexDomain")
asmeta_domains_CharDomain = Class(name="asmeta_domains_CharDomain")
asmeta_domains_BooleanDomain = Class(name="asmeta_domains_BooleanDomain")
asmeta_domains_BasicTd = Class(name="asmeta_domains_BasicTd", is_abstract=True)
asmeta_domains_BagDomain = Class(name="asmeta_domains_BagDomain")
asmeta_domains_AnyDomain = Class(name="asmeta_domains_AnyDomain")
asmeta_domains_AgentDomain = Class(name="asmeta_domains_AgentDomain")
asmeta_domains_AbstractTd = Class(name="asmeta_domains_AbstractTd")

# asmeta_furtherterms_IntegerTerm class attributes and methods

# ConstantTerm class attributes and methods

# asmeta_furtherterms_NaturalTerm class attributes and methods

# asmeta_furtherterms_VariableBindingTerm class attributes and methods

# ExtendedTerm class attributes and methods

# asmeta_furtherterms_StringTerm class attributes and methods

# asmeta_furtherterms_SetCt class attributes and methods

# ComprehensionTerm class attributes and methods

# asmeta_furtherterms_SequenceTerm class attributes and methods
asmeta_furtherterms_SequenceTerm_terms: Property = Property(name="terms", type=StringType)
asmeta_furtherterms_SequenceTerm.attributes={asmeta_furtherterms_SequenceTerm_terms}

# CollectionTerm class attributes and methods

# asmeta_furtherterms_RealTerm class attributes and methods

# asmeta_furtherterms_MapTerm class attributes and methods

# basicterms_TupleTerm class attributes and methods

# asmeta_furtherterms_MapCt class attributes and methods

# asmeta_furtherterms_LetTerm class attributes and methods

# VariableBindingTerm class attributes and methods

# basicterms_VariableTerm class attributes and methods

# basicterms_Term class attributes and methods

# asmeta_furtherterms_ForallTerm class attributes and methods

# FiniteQuantificationTerm class attributes and methods

# asmeta_furtherterms_FiniteQuantificationTerm class attributes and methods
asmeta_furtherterms_FiniteQuantificationTerm_ranges: Property = Property(name="ranges", type=StringType)
asmeta_furtherterms_FiniteQuantificationTerm.attributes={asmeta_furtherterms_FiniteQuantificationTerm_ranges}

# asmeta_furtherterms_ExistUniqueTerm class attributes and methods

# asmeta_furtherterms_ExistTerm class attributes and methods

# asmeta_furtherterms_EnumTerm class attributes and methods

# asmeta_furtherterms_ConditionalTerm class attributes and methods

# asmeta_furtherterms_ComprehensionTerm class attributes and methods
asmeta_furtherterms_ComprehensionTerm_ranges: Property = Property(name="ranges", type=StringType)
asmeta_furtherterms_ComprehensionTerm.attributes={asmeta_furtherterms_ComprehensionTerm_ranges}

# asmeta_furtherterms_SequenceCt class attributes and methods

# asmeta_furtherterms_ComplexTerm class attributes and methods

# asmeta_furtherterms_CharTerm class attributes and methods

# asmeta_furtherterms_CaseTerm class attributes and methods
asmeta_furtherterms_CaseTerm_resultTerms: Property = Property(name="resultTerms", type=StringType)
asmeta_furtherterms_CaseTerm.attributes={asmeta_furtherterms_CaseTerm_resultTerms}

# asmeta_furtherterms_BagTerm class attributes and methods

# asmeta_furtherterms_BagCt class attributes and methods

# asmeta_basicterms_VariableTerm class attributes and methods
asmeta_basicterms_VariableTerm_name: Property = Property(name="name", type=StringType)
asmeta_basicterms_VariableTerm_kind: Property = Property(name="kind", type=StringType)
asmeta_basicterms_VariableTerm.attributes={asmeta_basicterms_VariableTerm_kind, asmeta_basicterms_VariableTerm_name}

# BasicTerm class attributes and methods

# furtherterms_FiniteQuantificationTerm class attributes and methods

# asmeta_basicterms_UndefTerm class attributes and methods

# asmeta_basicterms_TupleTerm class attributes and methods
asmeta_basicterms_TupleTerm_arity: Property = Property(name="arity", type=StringType)
asmeta_basicterms_TupleTerm_terms: Property = Property(name="terms", type=StringType)
asmeta_basicterms_TupleTerm.attributes={asmeta_basicterms_TupleTerm_terms, asmeta_basicterms_TupleTerm_arity}

# asmeta_basicterms_SetTerm class attributes and methods

# asmeta_basicterms_RuleAsTerm class attributes and methods

# RuleDeclaration class attributes and methods

# asmeta_basicterms_LocationTerm class attributes and methods

# FunctionTerm class attributes and methods

# asmeta_basicterms_FunctionTerm class attributes and methods

# Function class attributes and methods

# asmeta_basicterms_ExtendedTerm class attributes and methods

# Term class attributes and methods

# asmeta_basicterms_DomainTerm class attributes and methods

# asmeta_basicterms_ConstantTerm class attributes and methods
asmeta_basicterms_ConstantTerm_symbol: Property = Property(name="symbol", type=StringType)
asmeta_basicterms_ConstantTerm.attributes={asmeta_basicterms_ConstantTerm_symbol}

# asmeta_basicterms_CollectionTerm class attributes and methods
asmeta_basicterms_CollectionTerm_size: Property = Property(name="size", type=StringType)
asmeta_basicterms_CollectionTerm.attributes={asmeta_basicterms_CollectionTerm_size}

# asmeta_basicterms_BooleanTerm class attributes and methods

# asmeta_basicterms_BasicTerm class attributes and methods

# asmeta_basicterms_Term class attributes and methods
asmeta_basicterms_Term_m_compatible: Method = Method(name="compatible", parameters={})
asmeta_basicterms_Term.methods={asmeta_basicterms_Term_m_compatible}

# domains_Domain class attributes and methods

# basictransitionrules_TermAsRule class attributes and methods

# asmeta_structure_NamedElement class attributes and methods
asmeta_structure_NamedElement_name: Property = Property(name="name", type=StringType)
asmeta_structure_NamedElement.attributes={asmeta_structure_NamedElement_name}

# asmeta_structure_AgentInitialization class attributes and methods

# basictransitionrules_MacroCallRule class attributes and methods

# Initialization class attributes and methods

# asmeta_structure_Body class attributes and methods

# FunctionDefinition class attributes and methods

# Property class attributes and methods

# DomainDefinition class attributes and methods

# Asm class attributes and methods

# asmeta_structure_FunctionInitialization class attributes and methods

# DynamicFunction class attributes and methods

# asmeta_structure_DomainInitialization class attributes and methods

# domains_ConcreteDomain class attributes and methods

# asmeta_structure_Signature class attributes and methods

# Header class attributes and methods

# domains_StructuredTd class attributes and methods

# asmeta_structure_ExportClause class attributes and methods

# asmeta_structure_ImportClause class attributes and methods
asmeta_structure_ImportClause_moduleName: Property = Property(name="moduleName", type=StringType)
asmeta_structure_ImportClause.attributes={asmeta_structure_ImportClause_moduleName}

# asmeta_structure_FunctionDefinition class attributes and methods

# asmeta_structure_DomainDefinition class attributes and methods

# asmeta_structure_Initialization class attributes and methods

# NamedElement class attributes and methods

# DomainInitialization class attributes and methods

# FunctionInitialization class attributes and methods

# AgentInitialization class attributes and methods

# asmeta_structure_Header class attributes and methods

# ImportClause class attributes and methods

# Signature class attributes and methods

# ExportClause class attributes and methods

# asmeta_structure_Asm class attributes and methods
asmeta_structure_Asm_isAsynchr: Property = Property(name="isAsynchr", type=StringType)
asmeta_structure_Asm.attributes={asmeta_structure_Asm_isAsynchr}

# Body class attributes and methods

# basictransitionrules_MacroDeclaration class attributes and methods

# asmeta_turbotransitionrules_TurboRule class attributes and methods

# Rule class attributes and methods

# asmeta_turbotransitionrules_TurboDeclaration class attributes and methods

# asmeta_turbotransitionrules_SeqRule class attributes and methods
asmeta_turbotransitionrules_SeqRule_rules: Property = Property(name="rules", type=StringType)
asmeta_turbotransitionrules_SeqRule.attributes={asmeta_turbotransitionrules_SeqRule_rules}

# TurboRule class attributes and methods

# asmeta_turbotransitionrules_TurboLocalStateRule class attributes and methods

# basictransitionrules_Rule class attributes and methods

# LocalFunction class attributes and methods

# asmeta_turbotransitionrules_TurboCallRule class attributes and methods
asmeta_turbotransitionrules_TurboCallRule_parameters: Property = Property(name="parameters", type=StringType)
asmeta_turbotransitionrules_TurboCallRule.attributes={asmeta_turbotransitionrules_TurboCallRule_parameters}

# turbotransitionrules_TurboDeclaration class attributes and methods

# asmeta_turbotransitionrules_TurboReturnRule class attributes and methods

# turbotransitionrules_TurboCallRule class attributes and methods

# asmeta_turbotransitionrules_TryCatchRule class attributes and methods

# asmeta_turbotransitionrules_IterateRule class attributes and methods

# asmeta_derivedtransitionrules_RecursiveWhileRule class attributes and methods

# TurboDerivedRule class attributes and methods

# asmeta_derivedtransitionrules_IterativeWhileRule class attributes and methods

# asmeta_derivedtransitionrules_DerivedRule class attributes and methods

# asmeta_derivedtransitionrules_CaseRule class attributes and methods
asmeta_derivedtransitionrules_CaseRule_caseBranches: Property = Property(name="caseBranches", type=StringType)
asmeta_derivedtransitionrules_CaseRule.attributes={asmeta_derivedtransitionrules_CaseRule_caseBranches}

# BasicDerivedRule class attributes and methods

# asmeta_derivedtransitionrules_BasicDerivedRule class attributes and methods

# DerivedRule class attributes and methods

# asmeta_derivedtransitionrules_TurboDerivedRule class attributes and methods

# asmeta_basictransitionrules_TermAsRule class attributes and methods
asmeta_basictransitionrules_TermAsRule_parameters: Property = Property(name="parameters", type=StringType)
asmeta_basictransitionrules_TermAsRule.attributes={asmeta_basictransitionrules_TermAsRule_parameters}

# asmeta_basictransitionrules_BasicRule class attributes and methods

# asmeta_basictransitionrules_Rule class attributes and methods

# asmeta_basictransitionrules_ChooseRule class attributes and methods
asmeta_basictransitionrules_ChooseRule_ranges: Property = Property(name="ranges", type=StringType)
asmeta_basictransitionrules_ChooseRule.attributes={asmeta_basictransitionrules_ChooseRule_ranges}

# BasicRule class attributes and methods

# asmeta_basictransitionrules_MacroCallRule class attributes and methods
asmeta_basictransitionrules_MacroCallRule_parameters: Property = Property(name="parameters", type=StringType)
asmeta_basictransitionrules_MacroCallRule.attributes={asmeta_basictransitionrules_MacroCallRule_parameters}

# asmeta_basictransitionrules_BlockRule class attributes and methods
asmeta_basictransitionrules_BlockRule_rules: Property = Property(name="rules", type=StringType)
asmeta_basictransitionrules_BlockRule.attributes={asmeta_basictransitionrules_BlockRule_rules}

# asmeta_basictransitionrules_ConditionalRule class attributes and methods

# asmeta_basictransitionrules_ForallRule class attributes and methods
asmeta_basictransitionrules_ForallRule_ranges: Property = Property(name="ranges", type=StringType)
asmeta_basictransitionrules_ForallRule.attributes={asmeta_basictransitionrules_ForallRule_ranges}

# asmeta_basictransitionrules_LetRule class attributes and methods

# asmeta_basictransitionrules_ExtendRule class attributes and methods

# asmeta_basictransitionrules_UpdateRule class attributes and methods

# asmeta_basictransitionrules_SkipRule class attributes and methods

# asmeta_basictransitionrules_MacroDeclaration class attributes and methods

# asmeta_definitions_RuleDeclaration class attributes and methods
asmeta_definitions_RuleDeclaration_arity: Property = Property(name="arity", type=StringType)
asmeta_definitions_RuleDeclaration.attributes={asmeta_definitions_RuleDeclaration_arity}

# Classifier class attributes and methods

# Invariant class attributes and methods

# asmeta_definitions_LocalFunction class attributes and methods

# asmeta_definitions_ControlledFunction class attributes and methods

# asmeta_definitions_SharedFunction class attributes and methods

# asmeta_definitions_MonitoredFunction class attributes and methods

# asmeta_definitions_OutFunction class attributes and methods

# asmeta_definitions_DynamicFunction class attributes and methods

# BasicFunction class attributes and methods

# asmeta_definitions_StaticFunction class attributes and methods

# asmeta_definitions_DerivedFunction class attributes and methods

# asmeta_definitions_BasicFunction class attributes and methods

# asmeta_definitions_Invariant class attributes and methods

# asmeta_definitions_Function class attributes and methods
asmeta_definitions_Function_arity: Property = Property(name="arity", type=StringType)
asmeta_definitions_Function.attributes={asmeta_definitions_Function_arity}

# asmeta_definitions_Classifier class attributes and methods

# asmeta_definitions_Property class attributes and methods

# asmeta_domains_NaturalDomain class attributes and methods

# IntegerDomain class attributes and methods

# asmeta_domains_UndefDomain class attributes and methods

# BasicTd class attributes and methods

# asmeta_domains_TypeDomain class attributes and methods

# Domain class attributes and methods

# asmeta_domains_StructuredTd class attributes and methods

# TypeDomain class attributes and methods

# asmeta_domains_StringDomain class attributes and methods

# asmeta_domains_SequenceDomain class attributes and methods

# StructuredTd class attributes and methods

# asmeta_domains_RuleDomain class attributes and methods
asmeta_domains_RuleDomain_domains: Property = Property(name="domains", type=StringType)
asmeta_domains_RuleDomain.attributes={asmeta_domains_RuleDomain_domains}

# asmeta_domains_ReserveDomain class attributes and methods

# AbstractTd class attributes and methods

# asmeta_domains_RealDomain class attributes and methods

# ComplexDomain class attributes and methods

# asmeta_domains_ProductDomain class attributes and methods
asmeta_domains_ProductDomain_domains: Property = Property(name="domains", type=StringType)
asmeta_domains_ProductDomain.attributes={asmeta_domains_ProductDomain_domains}

# asmeta_domains_PowersetDomain class attributes and methods

# asmeta_domains_MapDomain class attributes and methods

# asmeta_domains_IntegerDomain class attributes and methods

# RealDomain class attributes and methods

# asmeta_domains_EnumTd class attributes and methods

# domains_EnumElement class attributes and methods

# asmeta_domains_EnumElement class attributes and methods
asmeta_domains_EnumElement_symbol: Property = Property(name="symbol", type=StringType)
asmeta_domains_EnumElement.attributes={asmeta_domains_EnumElement_symbol}

# asmeta_domains_Domain class attributes and methods
asmeta_domains_Domain_m_compatible: Method = Method(name="compatible", parameters={})
asmeta_domains_Domain.methods={asmeta_domains_Domain_m_compatible}

# asmeta_domains_ConcreteDomain class attributes and methods
asmeta_domains_ConcreteDomain_isDynamic: Property = Property(name="isDynamic", type=StringType)
asmeta_domains_ConcreteDomain.attributes={asmeta_domains_ConcreteDomain_isDynamic}

# domains_TypeDomain class attributes and methods

# asmeta_domains_ComplexDomain class attributes and methods

# asmeta_domains_CharDomain class attributes and methods

# asmeta_domains_BooleanDomain class attributes and methods

# asmeta_domains_BasicTd class attributes and methods

# asmeta_domains_BagDomain class attributes and methods

# asmeta_domains_AnyDomain class attributes and methods

# asmeta_domains_AgentDomain class attributes and methods

# asmeta_domains_AbstractTd class attributes and methods
asmeta_domains_AbstractTd_isDynamic: Property = Property(name="isDynamic", type=StringType)
asmeta_domains_AbstractTd.attributes={asmeta_domains_AbstractTd_isDynamic}

# Relationships
pair0: BinaryAssociation = BinaryAssociation(
    name="pair0",
    ends={
        Property(name="basicterms_TupleTerm", type=asmeta_furtherterms_MapTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_MapTerm", type=basicterms_TupleTerm, multiplicity=Multiplicity(0, 9999))
    }
)
variable1: BinaryAssociation = BinaryAssociation(
    name="variable1",
    ends={
        Property(name="basicterms_VariableTerm", type=asmeta_furtherterms_LetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_LetTerm", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assignmentTerm2: BinaryAssociation = BinaryAssociation(
    name="assignmentTerm2",
    ends={
        Property(name="basicterms_Term", type=asmeta_furtherterms_LetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_LetTerm3", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="basicterms_Term6", type=asmeta_furtherterms_LetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_LetTerm5", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
variable7: BinaryAssociation = BinaryAssociation(
    name="variable7",
    ends={
        Property(name="VariableTerm", type=asmeta_furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="finiteQuantificationTerm", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
guard8: BinaryAssociation = BinaryAssociation(
    name="guard8",
    ends={
        Property(name="basicterms_Term9", type=asmeta_furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_FiniteQuantificationTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
elseTerm10: BinaryAssociation = BinaryAssociation(
    name="elseTerm10",
    ends={
        Property(name="basicterms_Term11", type=asmeta_furtherterms_ConditionalTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ConditionalTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
guard12: BinaryAssociation = BinaryAssociation(
    name="guard12",
    ends={
        Property(name="basicterms_Term14", type=asmeta_furtherterms_ConditionalTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ConditionalTerm13", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
thenTerm15: BinaryAssociation = BinaryAssociation(
    name="thenTerm15",
    ends={
        Property(name="basicterms_Term17", type=asmeta_furtherterms_ConditionalTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ConditionalTerm16", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
variable18: BinaryAssociation = BinaryAssociation(
    name="variable18",
    ends={
        Property(name="basicterms_VariableTerm19", type=asmeta_furtherterms_ComprehensionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ComprehensionTerm", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
guard20: BinaryAssociation = BinaryAssociation(
    name="guard20",
    ends={
        Property(name="basicterms_Term22", type=asmeta_furtherterms_ComprehensionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ComprehensionTerm21", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
comparingTerm26: BinaryAssociation = BinaryAssociation(
    name="comparingTerm26",
    ends={
        Property(name="basicterms_Term27", type=asmeta_furtherterms_CaseTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_CaseTerm", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
comparedTerm28: BinaryAssociation = BinaryAssociation(
    name="comparedTerm28",
    ends={
        Property(name="basicterms_Term30", type=asmeta_furtherterms_CaseTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_CaseTerm29", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
otherwiseTerm31: BinaryAssociation = BinaryAssociation(
    name="otherwiseTerm31",
    ends={
        Property(name="basicterms_Term33", type=asmeta_furtherterms_CaseTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_CaseTerm32", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
term34: BinaryAssociation = BinaryAssociation(
    name="term34",
    ends={
        Property(name="basicterms_Term35", type=asmeta_furtherterms_BagTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_BagTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 9999))
    }
)
finiteQuantificationTerm36: BinaryAssociation = BinaryAssociation(
    name="finiteQuantificationTerm36",
    ends={
        Property(name="FiniteQuantificationTerm", type=asmeta_basicterms_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(0, 1))
    }
)
term37: BinaryAssociation = BinaryAssociation(
    name="term37",
    ends={
        Property(name="basicterms_Term38", type=asmeta_basicterms_SetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_SetTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 9999))
    }
)
rule39: BinaryAssociation = BinaryAssociation(
    name="rule39",
    ends={
        Property(name="RuleDeclaration", type=asmeta_basicterms_RuleAsTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_RuleAsTerm", type=RuleDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
term23: BinaryAssociation = BinaryAssociation(
    name="term23",
    ends={
        Property(name="basicterms_Term25", type=asmeta_furtherterms_ComprehensionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ComprehensionTerm24", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
arguments40: BinaryAssociation = BinaryAssociation(
    name="arguments40",
    ends={
        Property(name="basicterms_TupleTerm41", type=asmeta_basicterms_FunctionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_FunctionTerm", type=basicterms_TupleTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function42: BinaryAssociation = BinaryAssociation(
    name="function42",
    ends={
        Property(name="Function", type=asmeta_basicterms_FunctionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_FunctionTerm43", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
domain44: BinaryAssociation = BinaryAssociation(
    name="domain44",
    ends={
        Property(name="domains_Domain", type=asmeta_basicterms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_Term", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
termAsRule45: BinaryAssociation = BinaryAssociation(
    name="termAsRule45",
    ends={
        Property(name="TermAsRule", type=asmeta_basicterms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="term", type=basictransitionrules_TermAsRule, multiplicity=Multiplicity(0, 9999))
    }
)
program46: BinaryAssociation = BinaryAssociation(
    name="program46",
    ends={
        Property(name="basictransitionrules_MacroCallRule", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_AgentInitialization", type=basictransitionrules_MacroCallRule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain47: BinaryAssociation = BinaryAssociation(
    name="domain47",
    ends={
        Property(name="domains_Domain49", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_AgentInitialization48", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
initialState50: BinaryAssociation = BinaryAssociation(
    name="initialState50",
    ends={
        Property(name="Initialization", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="agentInitialization", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
functionDefinition51: BinaryAssociation = BinaryAssociation(
    name="functionDefinition51",
    ends={
        Property(name="FunctionDefinition", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body", type=FunctionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property52: BinaryAssociation = BinaryAssociation(
    name="property52",
    ends={
        Property(name="Property", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body53", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainDefinition54: BinaryAssociation = BinaryAssociation(
    name="domainDefinition54",
    ends={
        Property(name="DomainDefinition", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body55", type=DomainDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruleDeclaration56: BinaryAssociation = BinaryAssociation(
    name="ruleDeclaration56",
    ends={
        Property(name="RuleDeclaration57", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmBody", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
asm58: BinaryAssociation = BinaryAssociation(
    name="asm58",
    ends={
        Property(name="Asm", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="bodySection", type=Asm, multiplicity=Multiplicity(0, 1))
    }
)
initialState59: BinaryAssociation = BinaryAssociation(
    name="initialState59",
    ends={
        Property(name="Initialization60", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="functionInitialization", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="basicterms_Term62", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
initializedFunction63: BinaryAssociation = BinaryAssociation(
    name="initializedFunction63",
    ends={
        Property(name="DynamicFunction", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="initialization", type=DynamicFunction, multiplicity=Multiplicity(1, 1))
    }
)
variable64: BinaryAssociation = BinaryAssociation(
    name="variable64",
    ends={
        Property(name="basicterms_VariableTerm66", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization65", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedDomain67: BinaryAssociation = BinaryAssociation(
    name="initializedDomain67",
    ends={
        Property(name="ConcreteDomain", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="initialization68", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
body69: BinaryAssociation = BinaryAssociation(
    name="body69",
    ends={
        Property(name="basicterms_Term70", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialState71: BinaryAssociation = BinaryAssociation(
    name="initialState71",
    ends={
        Property(name="Initialization72", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="domainInitialization", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
domain73: BinaryAssociation = BinaryAssociation(
    name="domain73",
    ends={
        Property(name="Domain", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=domains_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function74: BinaryAssociation = BinaryAssociation(
    name="function74",
    ends={
        Property(name="Function76", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature75", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headerSection77: BinaryAssociation = BinaryAssociation(
    name="headerSection77",
    ends={
        Property(name="Header", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature78", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
structuredDomain79: BinaryAssociation = BinaryAssociation(
    name="structuredDomain79",
    ends={
        Property(name="domains_StructuredTd", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Signature", type=domains_StructuredTd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportedFunction80: BinaryAssociation = BinaryAssociation(
    name="exportedFunction80",
    ends={
        Property(name="Function81", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
exportedDomain82: BinaryAssociation = BinaryAssociation(
    name="exportedDomain82",
    ends={
        Property(name="domains_Domain84", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause83", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
exportedRule85: BinaryAssociation = BinaryAssociation(
    name="exportedRule85",
    ends={
        Property(name="RuleDeclaration87", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause86", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
importedDomain88: BinaryAssociation = BinaryAssociation(
    name="importedDomain88",
    ends={
        Property(name="domains_Domain89", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
importedFunction90: BinaryAssociation = BinaryAssociation(
    name="importedFunction90",
    ends={
        Property(name="Function92", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause91", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
initialState122: BinaryAssociation = BinaryAssociation(
    name="initialState122",
    ends={
        Property(name="Initialization123", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm", type=Initialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body96: BinaryAssociation = BinaryAssociation(
    name="body96",
    ends={
        Property(name="basicterms_Term97", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable98: BinaryAssociation = BinaryAssociation(
    name="variable98",
    ends={
        Property(name="basicterms_VariableTerm100", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition99", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999))
    }
)
definedFunction101: BinaryAssociation = BinaryAssociation(
    name="definedFunction101",
    ends={
        Property(name="Function102", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
body103: BinaryAssociation = BinaryAssociation(
    name="body103",
    ends={
        Property(name="basicterms_Term104", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definedDomain105: BinaryAssociation = BinaryAssociation(
    name="definedDomain105",
    ends={
        Property(name="ConcreteDomain107", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition106", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
domainInitialization108: BinaryAssociation = BinaryAssociation(
    name="domainInitialization108",
    ends={
        Property(name="DomainInitialization", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="initialState", type=DomainInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionInitialization109: BinaryAssociation = BinaryAssociation(
    name="functionInitialization109",
    ends={
        Property(name="FunctionInitialization", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="initialState110", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agentInitialization111: BinaryAssociation = BinaryAssociation(
    name="agentInitialization111",
    ends={
        Property(name="AgentInitialization", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="initialState112", type=AgentInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
asm113: BinaryAssociation = BinaryAssociation(
    name="asm113",
    ends={
        Property(name="Asm114", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultInitialState", type=Asm, multiplicity=Multiplicity(1, 1))
    }
)
importClause115: BinaryAssociation = BinaryAssociation(
    name="importClause115",
    ends={
        Property(name="ImportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header", type=ImportClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature116: BinaryAssociation = BinaryAssociation(
    name="signature116",
    ends={
        Property(name="Signature", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="headerSection", type=Signature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exportClause117: BinaryAssociation = BinaryAssociation(
    name="exportClause117",
    ends={
        Property(name="ExportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header118", type=ExportClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asm119: BinaryAssociation = BinaryAssociation(
    name="asm119",
    ends={
        Property(name="Asm121", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="headerSection120", type=Asm, multiplicity=Multiplicity(0, 1))
    }
)
importedRule93: BinaryAssociation = BinaryAssociation(
    name="importedRule93",
    ends={
        Property(name="RuleDeclaration95", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause94", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
defaultInitialState124: BinaryAssociation = BinaryAssociation(
    name="defaultInitialState124",
    ends={
        Property(name="Initialization125", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asm", type=Initialization, multiplicity=Multiplicity(0, 1))
    }
)
bodySection126: BinaryAssociation = BinaryAssociation(
    name="bodySection126",
    ends={
        Property(name="Body", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asm127", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headerSection128: BinaryAssociation = BinaryAssociation(
    name="headerSection128",
    ends={
        Property(name="Header130", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asm129", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainrule131: BinaryAssociation = BinaryAssociation(
    name="mainrule131",
    ends={
        Property(name="basictransitionrules_MacroDeclaration", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm132", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
resultType133: BinaryAssociation = BinaryAssociation(
    name="resultType133",
    ends={
        Property(name="domains_Domain134", type=asmeta_turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboDeclaration", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
init135: BinaryAssociation = BinaryAssociation(
    name="init135",
    ends={
        Property(name="basictransitionrules_Rule", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body136: BinaryAssociation = BinaryAssociation(
    name="body136",
    ends={
        Property(name="basictransitionrules_Rule138", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule137", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localFunction139: BinaryAssociation = BinaryAssociation(
    name="localFunction139",
    ends={
        Property(name="LocalFunction", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule140", type=LocalFunction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
calledRule141: BinaryAssociation = BinaryAssociation(
    name="calledRule141",
    ends={
        Property(name="turbotransitionrules_TurboDeclaration", type=asmeta_turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboCallRule", type=turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
location142: BinaryAssociation = BinaryAssociation(
    name="location142",
    ends={
        Property(name="basicterms_Term143", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
updateRule144: BinaryAssociation = BinaryAssociation(
    name="updateRule144",
    ends={
        Property(name="turbotransitionrules_TurboCallRule", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule145", type=turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1))
    }
)
location146: BinaryAssociation = BinaryAssociation(
    name="location146",
    ends={
        Property(name="basicterms_Term147", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
catchRule148: BinaryAssociation = BinaryAssociation(
    name="catchRule148",
    ends={
        Property(name="basictransitionrules_Rule150", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule149", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryRule151: BinaryAssociation = BinaryAssociation(
    name="tryRule151",
    ends={
        Property(name="basictransitionrules_Rule153", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule152", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule154: BinaryAssociation = BinaryAssociation(
    name="rule154",
    ends={
        Property(name="basictransitionrules_Rule155", type=asmeta_turbotransitionrules_IterateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_IterateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard158: BinaryAssociation = BinaryAssociation(
    name="guard158",
    ends={
        Property(name="basicterms_Term160", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule159", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
guard161: BinaryAssociation = BinaryAssociation(
    name="guard161",
    ends={
        Property(name="basicterms_Term162", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
rule163: BinaryAssociation = BinaryAssociation(
    name="rule163",
    ends={
        Property(name="basictransitionrules_Rule165", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule164", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term166: BinaryAssociation = BinaryAssociation(
    name="term166",
    ends={
        Property(name="basicterms_Term167", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
caseTerm168: BinaryAssociation = BinaryAssociation(
    name="caseTerm168",
    ends={
        Property(name="basicterms_Term170", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule169", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
otherwiseBranch171: BinaryAssociation = BinaryAssociation(
    name="otherwiseBranch171",
    ends={
        Property(name="basictransitionrules_Rule173", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule172", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term174: BinaryAssociation = BinaryAssociation(
    name="term174",
    ends={
        Property(name="Term", type=asmeta_basictransitionrules_TermAsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="termAsRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
ifnone175: BinaryAssociation = BinaryAssociation(
    name="ifnone175",
    ends={
        Property(name="basictransitionrules_Rule176", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doRule177: BinaryAssociation = BinaryAssociation(
    name="doRule177",
    ends={
        Property(name="basictransitionrules_Rule179", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule178", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard180: BinaryAssociation = BinaryAssociation(
    name="guard180",
    ends={
        Property(name="basicterms_Term182", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule181", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
rule156: BinaryAssociation = BinaryAssociation(
    name="rule156",
    ends={
        Property(name="basictransitionrules_Rule157", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable183: BinaryAssociation = BinaryAssociation(
    name="variable183",
    ends={
        Property(name="basicterms_VariableTerm185", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule184", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
calledMacro186: BinaryAssociation = BinaryAssociation(
    name="calledMacro186",
    ends={
        Property(name="basictransitionrules_MacroDeclaration187", type=asmeta_basictransitionrules_MacroCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_MacroCallRule", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
guard188: BinaryAssociation = BinaryAssociation(
    name="guard188",
    ends={
        Property(name="basicterms_Term189", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
elseRule190: BinaryAssociation = BinaryAssociation(
    name="elseRule190",
    ends={
        Property(name="basictransitionrules_Rule192", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule191", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenRule193: BinaryAssociation = BinaryAssociation(
    name="thenRule193",
    ends={
        Property(name="basictransitionrules_Rule195", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule194", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable196: BinaryAssociation = BinaryAssociation(
    name="variable196",
    ends={
        Property(name="basicterms_VariableTerm197", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
guard198: BinaryAssociation = BinaryAssociation(
    name="guard198",
    ends={
        Property(name="basicterms_Term200", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule199", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
doRule201: BinaryAssociation = BinaryAssociation(
    name="doRule201",
    ends={
        Property(name="basictransitionrules_Rule203", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule202", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inRule204: BinaryAssociation = BinaryAssociation(
    name="inRule204",
    ends={
        Property(name="basictransitionrules_Rule205", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression206: BinaryAssociation = BinaryAssociation(
    name="initExpression206",
    ends={
        Property(name="basicterms_Term208", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule207", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
variable209: BinaryAssociation = BinaryAssociation(
    name="variable209",
    ends={
        Property(name="basicterms_VariableTerm211", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule210", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
extendedDomain212: BinaryAssociation = BinaryAssociation(
    name="extendedDomain212",
    ends={
        Property(name="domains_Domain213", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
boundVar214: BinaryAssociation = BinaryAssociation(
    name="boundVar214",
    ends={
        Property(name="basicterms_VariableTerm216", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule215", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
doRule217: BinaryAssociation = BinaryAssociation(
    name="doRule217",
    ends={
        Property(name="basictransitionrules_Rule219", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule218", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updatingTerm220: BinaryAssociation = BinaryAssociation(
    name="updatingTerm220",
    ends={
        Property(name="basicterms_Term221", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
location222: BinaryAssociation = BinaryAssociation(
    name="location222",
    ends={
        Property(name="basicterms_Term224", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule223", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
variable225: BinaryAssociation = BinaryAssociation(
    name="variable225",
    ends={
        Property(name="asmeta_definitions_RuleDeclaration", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999)),
        Property(name="basicterms_VariableTerm226", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
constraint227: BinaryAssociation = BinaryAssociation(
    name="constraint227",
    ends={
        Property(name="Invariant", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedRule", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
ruleBody228: BinaryAssociation = BinaryAssociation(
    name="ruleBody228",
    ends={
        Property(name="basictransitionrules_Rule230", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_RuleDeclaration229", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1))
    }
)
asmBody231: BinaryAssociation = BinaryAssociation(
    name="asmBody231",
    ends={
        Property(name="Body232", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ruleDeclaration", type=Body, multiplicity=Multiplicity(1, 1))
    }
)
initialization233: BinaryAssociation = BinaryAssociation(
    name="initialization233",
    ends={
        Property(name="FunctionInitialization234", type=asmeta_definitions_DynamicFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedFunction", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedDomain235: BinaryAssociation = BinaryAssociation(
    name="constrainedDomain235",
    ends={
        Property(name="Domain236", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
body237: BinaryAssociation = BinaryAssociation(
    name="body237",
    ends={
        Property(name="basicterms_Term238", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Invariant", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedRule239: BinaryAssociation = BinaryAssociation(
    name="constrainedRule239",
    ends={
        Property(name="RuleDeclaration241", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint240", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedFunction242: BinaryAssociation = BinaryAssociation(
    name="constrainedFunction242",
    ends={
        Property(name="Function244", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint243", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
domain245: BinaryAssociation = BinaryAssociation(
    name="domain245",
    ends={
        Property(name="domains_Domain246", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
codomain247: BinaryAssociation = BinaryAssociation(
    name="codomain247",
    ends={
        Property(name="domains_Domain249", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function248", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
definition250: BinaryAssociation = BinaryAssociation(
    name="definition250",
    ends={
        Property(name="FunctionDefinition251", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="definedFunction", type=FunctionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
constraint252: BinaryAssociation = BinaryAssociation(
    name="constraint252",
    ends={
        Property(name="Invariant253", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedFunction", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
domain256: BinaryAssociation = BinaryAssociation(
    name="domain256",
    ends={
        Property(name="domains_Domain257", type=asmeta_domains_SequenceDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_SequenceDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
baseDomain258: BinaryAssociation = BinaryAssociation(
    name="baseDomain258",
    ends={
        Property(name="domains_Domain259", type=asmeta_domains_PowersetDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_PowersetDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
sourceDomain260: BinaryAssociation = BinaryAssociation(
    name="sourceDomain260",
    ends={
        Property(name="domains_Domain261", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
targetDomain262: BinaryAssociation = BinaryAssociation(
    name="targetDomain262",
    ends={
        Property(name="domains_Domain264", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain263", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
signature254: BinaryAssociation = BinaryAssociation(
    name="signature254",
    ends={
        Property(name="Signature255", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="function", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
element265: BinaryAssociation = BinaryAssociation(
    name="element265",
    ends={
        Property(name="domains_EnumElement", type=asmeta_domains_EnumTd, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_EnumTd", type=domains_EnumElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraint266: BinaryAssociation = BinaryAssociation(
    name="constraint266",
    ends={
        Property(name="Invariant267", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedDomain", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
signature268: BinaryAssociation = BinaryAssociation(
    name="signature268",
    ends={
        Property(name="Signature269", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
initialization270: BinaryAssociation = BinaryAssociation(
    name="initialization270",
    ends={
        Property(name="DomainInitialization271", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedDomain", type=DomainInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
definition272: BinaryAssociation = BinaryAssociation(
    name="definition272",
    ends={
        Property(name="DomainDefinition273", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="definedDomain", type=DomainDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeDomain274: BinaryAssociation = BinaryAssociation(
    name="typeDomain274",
    ends={
        Property(name="domains_TypeDomain", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_ConcreteDomain", type=domains_TypeDomain, multiplicity=Multiplicity(1, 1))
    }
)
domain275: BinaryAssociation = BinaryAssociation(
    name="domain275",
    ends={
        Property(name="domains_Domain276", type=asmeta_domains_BagDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_BagDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_asmeta_furtherterms_IntegerTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_IntegerTerm)
gen_asmeta_furtherterms_NaturalTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_NaturalTerm)
gen_asmeta_furtherterms_VariableBindingTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_VariableBindingTerm)
gen_asmeta_furtherterms_StringTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_StringTerm)
gen_asmeta_furtherterms_SetCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_SetCt)
gen_asmeta_furtherterms_SequenceTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_SequenceTerm)
gen_asmeta_furtherterms_RealTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_RealTerm)
gen_asmeta_furtherterms_MapTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_MapTerm)
gen_asmeta_furtherterms_MapCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_MapCt)
gen_asmeta_furtherterms_LetTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_LetTerm)
gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ForallTerm)
gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_FiniteQuantificationTerm)
gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistUniqueTerm)
gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistTerm)
gen_asmeta_furtherterms_EnumTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_EnumTerm)
gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_ConditionalTerm)
gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_ComprehensionTerm)
gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_SequenceCt)
gen_asmeta_furtherterms_ComplexTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_ComplexTerm)
gen_asmeta_furtherterms_CharTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_CharTerm)
gen_asmeta_furtherterms_CaseTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_CaseTerm)
gen_asmeta_furtherterms_BagTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_BagTerm)
gen_asmeta_furtherterms_BagCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_BagCt)
gen_asmeta_basicterms_VariableTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_VariableTerm)
gen_asmeta_basicterms_UndefTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_basicterms_UndefTerm)
gen_asmeta_basicterms_TupleTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_TupleTerm)
gen_asmeta_basicterms_SetTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_basicterms_SetTerm)
gen_asmeta_basicterms_RuleAsTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_RuleAsTerm)
gen_asmeta_basicterms_LocationTerm_FunctionTerm = Generalization(general=FunctionTerm, specific=asmeta_basicterms_LocationTerm)
gen_asmeta_basicterms_FunctionTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_FunctionTerm)
gen_asmeta_basicterms_ExtendedTerm_Term = Generalization(general=Term, specific=asmeta_basicterms_ExtendedTerm)
gen_asmeta_basicterms_DomainTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_DomainTerm)
gen_asmeta_basicterms_ConstantTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_ConstantTerm)
gen_asmeta_basicterms_CollectionTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_CollectionTerm)
gen_asmeta_basicterms_BooleanTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_basicterms_BooleanTerm)
gen_asmeta_basicterms_BasicTerm_Term = Generalization(general=Term, specific=asmeta_basicterms_BasicTerm)
gen_asmeta_structure_Initialization_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Initialization)
gen_asmeta_structure_Asm_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Asm)
gen_asmeta_turbotransitionrules_TurboRule_Rule = Generalization(general=Rule, specific=asmeta_turbotransitionrules_TurboRule)
gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration = Generalization(general=RuleDeclaration, specific=asmeta_turbotransitionrules_TurboDeclaration)
gen_asmeta_turbotransitionrules_SeqRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_SeqRule)
gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboLocalStateRule)
gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboCallRule)
gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboReturnRule)
gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TryCatchRule)
gen_asmeta_turbotransitionrules_IterateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_IterateRule)
gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_RecursiveWhileRule)
gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_IterativeWhileRule)
gen_asmeta_derivedtransitionrules_DerivedRule_Rule = Generalization(general=Rule, specific=asmeta_derivedtransitionrules_DerivedRule)
gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule = Generalization(general=BasicDerivedRule, specific=asmeta_derivedtransitionrules_CaseRule)
gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_BasicDerivedRule)
gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_TurboDerivedRule)
gen_asmeta_basictransitionrules_TermAsRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_TermAsRule)
gen_asmeta_basictransitionrules_BasicRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_BasicRule)
gen_asmeta_basictransitionrules_ChooseRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ChooseRule)
gen_asmeta_basictransitionrules_MacroCallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_MacroCallRule)
gen_asmeta_basictransitionrules_BlockRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_BlockRule)
gen_asmeta_basictransitionrules_ConditionalRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ConditionalRule)
gen_asmeta_basictransitionrules_ForallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ForallRule)
gen_asmeta_basictransitionrules_LetRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_LetRule)
gen_asmeta_basictransitionrules_ExtendRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ExtendRule)
gen_asmeta_basictransitionrules_UpdateRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_UpdateRule)
gen_asmeta_basictransitionrules_SkipRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_SkipRule)
gen_asmeta_basictransitionrules_MacroDeclaration_RuleDeclaration = Generalization(general=RuleDeclaration, specific=asmeta_basictransitionrules_MacroDeclaration)
gen_asmeta_definitions_RuleDeclaration_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_RuleDeclaration)
gen_asmeta_definitions_LocalFunction_DynamicFunction = Generalization(general=DynamicFunction, specific=asmeta_definitions_LocalFunction)
gen_asmeta_definitions_ControlledFunction_DynamicFunction = Generalization(general=DynamicFunction, specific=asmeta_definitions_ControlledFunction)
gen_asmeta_definitions_SharedFunction_DynamicFunction = Generalization(general=DynamicFunction, specific=asmeta_definitions_SharedFunction)
gen_asmeta_definitions_MonitoredFunction_DynamicFunction = Generalization(general=DynamicFunction, specific=asmeta_definitions_MonitoredFunction)
gen_asmeta_definitions_OutFunction_DynamicFunction = Generalization(general=DynamicFunction, specific=asmeta_definitions_OutFunction)
gen_asmeta_definitions_DynamicFunction_BasicFunction = Generalization(general=BasicFunction, specific=asmeta_definitions_DynamicFunction)
gen_asmeta_definitions_StaticFunction_BasicFunction = Generalization(general=BasicFunction, specific=asmeta_definitions_StaticFunction)
gen_asmeta_definitions_DerivedFunction_Function = Generalization(general=Function, specific=asmeta_definitions_DerivedFunction)
gen_asmeta_definitions_BasicFunction_Function = Generalization(general=Function, specific=asmeta_definitions_BasicFunction)
gen_asmeta_definitions_Invariant_Property = Generalization(general=Property_, specific=asmeta_definitions_Invariant)
gen_asmeta_definitions_Function_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_Function)
gen_asmeta_definitions_Classifier_NamedElement = Generalization(general=NamedElement, specific=asmeta_definitions_Classifier)
gen_asmeta_definitions_Property_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_Property)
gen_asmeta_domains_NaturalDomain_IntegerDomain = Generalization(general=IntegerDomain, specific=asmeta_domains_NaturalDomain)
gen_asmeta_domains_UndefDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_UndefDomain)
gen_asmeta_domains_TypeDomain_Domain = Generalization(general=Domain, specific=asmeta_domains_TypeDomain)
gen_asmeta_domains_StructuredTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_StructuredTd)
gen_asmeta_domains_StringDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_StringDomain)
gen_asmeta_domains_SequenceDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_SequenceDomain)
gen_asmeta_domains_RuleDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_RuleDomain)
gen_asmeta_domains_ReserveDomain_AbstractTd = Generalization(general=AbstractTd, specific=asmeta_domains_ReserveDomain)
gen_asmeta_domains_RealDomain_ComplexDomain = Generalization(general=ComplexDomain, specific=asmeta_domains_RealDomain)
gen_asmeta_domains_ProductDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_ProductDomain)
gen_asmeta_domains_PowersetDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_PowersetDomain)
gen_asmeta_domains_MapDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_MapDomain)
gen_asmeta_domains_EnumTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_EnumTd)
gen_asmeta_domains_Domain_Classifier = Generalization(general=Classifier, specific=asmeta_domains_Domain)
gen_asmeta_domains_ConcreteDomain_Domain = Generalization(general=Domain, specific=asmeta_domains_ConcreteDomain)
gen_asmeta_domains_ComplexDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_ComplexDomain)
gen_asmeta_domains_CharDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_CharDomain)
gen_asmeta_domains_BooleanDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_BooleanDomain)
gen_asmeta_domains_BasicTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_BasicTd)
gen_asmeta_domains_BagDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_BagDomain)
gen_asmeta_domains_AnyDomain_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_AnyDomain)
gen_asmeta_domains_AgentDomain_AbstractTd = Generalization(general=AbstractTd, specific=asmeta_domains_AgentDomain)
gen_asmeta_domains_AbstractTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_AbstractTd)
gen_asmeta_domains_IntegerDomain_RealDomain = Generalization(general=RealDomain, specific=asmeta_domains_IntegerDomain)

# Domain Model
domain_model = DomainModel(
    name="asmeta",
    types={asmeta_furtherterms_IntegerTerm, ConstantTerm, asmeta_furtherterms_NaturalTerm, asmeta_furtherterms_VariableBindingTerm, ExtendedTerm, asmeta_furtherterms_StringTerm, asmeta_furtherterms_SetCt, ComprehensionTerm, asmeta_furtherterms_SequenceTerm, CollectionTerm, asmeta_furtherterms_RealTerm, asmeta_furtherterms_MapTerm, basicterms_TupleTerm, asmeta_furtherterms_MapCt, asmeta_furtherterms_LetTerm, VariableBindingTerm, basicterms_VariableTerm, basicterms_Term, asmeta_furtherterms_ForallTerm, FiniteQuantificationTerm, asmeta_furtherterms_FiniteQuantificationTerm, asmeta_furtherterms_ExistUniqueTerm, asmeta_furtherterms_ExistTerm, asmeta_furtherterms_EnumTerm, asmeta_furtherterms_ConditionalTerm, asmeta_furtherterms_ComprehensionTerm, asmeta_furtherterms_SequenceCt, asmeta_furtherterms_ComplexTerm, asmeta_furtherterms_CharTerm, asmeta_furtherterms_CaseTerm, asmeta_furtherterms_BagTerm, asmeta_furtherterms_BagCt, asmeta_basicterms_VariableTerm, BasicTerm, furtherterms_FiniteQuantificationTerm, asmeta_basicterms_UndefTerm, asmeta_basicterms_TupleTerm, asmeta_basicterms_SetTerm, asmeta_basicterms_RuleAsTerm, RuleDeclaration, asmeta_basicterms_LocationTerm, FunctionTerm, asmeta_basicterms_FunctionTerm, Function, asmeta_basicterms_ExtendedTerm, Term, asmeta_basicterms_DomainTerm, asmeta_basicterms_ConstantTerm, asmeta_basicterms_CollectionTerm, asmeta_basicterms_BooleanTerm, asmeta_basicterms_BasicTerm, asmeta_basicterms_Term, domains_Domain, basictransitionrules_TermAsRule, asmeta_structure_NamedElement, asmeta_structure_AgentInitialization, basictransitionrules_MacroCallRule, Initialization, asmeta_structure_Body, FunctionDefinition, Property_, DomainDefinition, Asm, asmeta_structure_FunctionInitialization, DynamicFunction, asmeta_structure_DomainInitialization, domains_ConcreteDomain, asmeta_structure_Signature, Header, domains_StructuredTd, asmeta_structure_ExportClause, asmeta_structure_ImportClause, asmeta_structure_FunctionDefinition, asmeta_structure_DomainDefinition, asmeta_structure_Initialization, NamedElement, DomainInitialization, FunctionInitialization, AgentInitialization, asmeta_structure_Header, ImportClause, Signature, ExportClause, asmeta_structure_Asm, Body, basictransitionrules_MacroDeclaration, asmeta_turbotransitionrules_TurboRule, Rule, asmeta_turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_SeqRule, TurboRule, asmeta_turbotransitionrules_TurboLocalStateRule, basictransitionrules_Rule, LocalFunction, asmeta_turbotransitionrules_TurboCallRule, turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_TurboReturnRule, turbotransitionrules_TurboCallRule, asmeta_turbotransitionrules_TryCatchRule, asmeta_turbotransitionrules_IterateRule, asmeta_derivedtransitionrules_RecursiveWhileRule, TurboDerivedRule, asmeta_derivedtransitionrules_IterativeWhileRule, asmeta_derivedtransitionrules_DerivedRule, asmeta_derivedtransitionrules_CaseRule, BasicDerivedRule, asmeta_derivedtransitionrules_BasicDerivedRule, DerivedRule, asmeta_derivedtransitionrules_TurboDerivedRule, asmeta_basictransitionrules_TermAsRule, asmeta_basictransitionrules_BasicRule, asmeta_basictransitionrules_Rule, asmeta_basictransitionrules_ChooseRule, BasicRule, asmeta_basictransitionrules_MacroCallRule, asmeta_basictransitionrules_BlockRule, asmeta_basictransitionrules_ConditionalRule, asmeta_basictransitionrules_ForallRule, asmeta_basictransitionrules_LetRule, asmeta_basictransitionrules_ExtendRule, asmeta_basictransitionrules_UpdateRule, asmeta_basictransitionrules_SkipRule, asmeta_basictransitionrules_MacroDeclaration, asmeta_definitions_RuleDeclaration, Classifier, Invariant, asmeta_definitions_LocalFunction, asmeta_definitions_ControlledFunction, asmeta_definitions_SharedFunction, asmeta_definitions_MonitoredFunction, asmeta_definitions_OutFunction, asmeta_definitions_DynamicFunction, BasicFunction, asmeta_definitions_StaticFunction, asmeta_definitions_DerivedFunction, asmeta_definitions_BasicFunction, asmeta_definitions_Invariant, asmeta_definitions_Function, asmeta_definitions_Classifier, asmeta_definitions_Property, asmeta_domains_NaturalDomain, IntegerDomain, asmeta_domains_UndefDomain, BasicTd, asmeta_domains_TypeDomain, Domain, asmeta_domains_StructuredTd, TypeDomain, asmeta_domains_StringDomain, asmeta_domains_SequenceDomain, StructuredTd, asmeta_domains_RuleDomain, asmeta_domains_ReserveDomain, AbstractTd, asmeta_domains_RealDomain, ComplexDomain, asmeta_domains_ProductDomain, asmeta_domains_PowersetDomain, asmeta_domains_MapDomain, asmeta_domains_IntegerDomain, RealDomain, asmeta_domains_EnumTd, domains_EnumElement, asmeta_domains_EnumElement, asmeta_domains_Domain, asmeta_domains_ConcreteDomain, domains_TypeDomain, asmeta_domains_ComplexDomain, asmeta_domains_CharDomain, asmeta_domains_BooleanDomain, asmeta_domains_BasicTd, asmeta_domains_BagDomain, asmeta_domains_AnyDomain, asmeta_domains_AgentDomain, asmeta_domains_AbstractTd, VariableKind},
    associations={pair0, variable1, assignmentTerm2, body4, variable7, guard8, elseTerm10, guard12, thenTerm15, variable18, guard20, comparingTerm26, comparedTerm28, otherwiseTerm31, term34, finiteQuantificationTerm36, term37, rule39, term23, arguments40, function42, domain44, termAsRule45, program46, domain47, initialState50, functionDefinition51, property52, domainDefinition54, ruleDeclaration56, asm58, initialState59, body61, initializedFunction63, variable64, initializedDomain67, body69, initialState71, domain73, function74, headerSection77, structuredDomain79, exportedFunction80, exportedDomain82, exportedRule85, importedDomain88, importedFunction90, initialState122, body96, variable98, definedFunction101, body103, definedDomain105, domainInitialization108, functionInitialization109, agentInitialization111, asm113, importClause115, signature116, exportClause117, asm119, importedRule93, defaultInitialState124, bodySection126, headerSection128, mainrule131, resultType133, init135, body136, localFunction139, calledRule141, location142, updateRule144, location146, catchRule148, tryRule151, rule154, guard158, guard161, rule163, term166, caseTerm168, otherwiseBranch171, term174, ifnone175, doRule177, guard180, rule156, variable183, calledMacro186, guard188, elseRule190, thenRule193, variable196, guard198, doRule201, inRule204, initExpression206, variable209, extendedDomain212, boundVar214, doRule217, updatingTerm220, location222, variable225, constraint227, ruleBody228, asmBody231, initialization233, constrainedDomain235, body237, constrainedRule239, constrainedFunction242, domain245, codomain247, definition250, constraint252, domain256, baseDomain258, sourceDomain260, targetDomain262, signature254, element265, constraint266, signature268, initialization270, definition272, typeDomain274, domain275},
    generalizations={gen_asmeta_furtherterms_IntegerTerm_ConstantTerm, gen_asmeta_furtherterms_NaturalTerm_ConstantTerm, gen_asmeta_furtherterms_VariableBindingTerm_ExtendedTerm, gen_asmeta_furtherterms_StringTerm_ConstantTerm, gen_asmeta_furtherterms_SetCt_ComprehensionTerm, gen_asmeta_furtherterms_SequenceTerm_CollectionTerm, gen_asmeta_furtherterms_RealTerm_ConstantTerm, gen_asmeta_furtherterms_MapTerm_CollectionTerm, gen_asmeta_furtherterms_MapCt_ComprehensionTerm, gen_asmeta_furtherterms_LetTerm_VariableBindingTerm, gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm, gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_EnumTerm_ConstantTerm, gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm, gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm, gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm, gen_asmeta_furtherterms_ComplexTerm_ConstantTerm, gen_asmeta_furtherterms_CharTerm_ConstantTerm, gen_asmeta_furtherterms_CaseTerm_ExtendedTerm, gen_asmeta_furtherterms_BagTerm_CollectionTerm, gen_asmeta_furtherterms_BagCt_ComprehensionTerm, gen_asmeta_basicterms_VariableTerm_BasicTerm, gen_asmeta_basicterms_UndefTerm_ConstantTerm, gen_asmeta_basicterms_TupleTerm_ExtendedTerm, gen_asmeta_basicterms_SetTerm_CollectionTerm, gen_asmeta_basicterms_RuleAsTerm_ExtendedTerm, gen_asmeta_basicterms_LocationTerm_FunctionTerm, gen_asmeta_basicterms_FunctionTerm_BasicTerm, gen_asmeta_basicterms_ExtendedTerm_Term, gen_asmeta_basicterms_DomainTerm_ExtendedTerm, gen_asmeta_basicterms_ConstantTerm_BasicTerm, gen_asmeta_basicterms_CollectionTerm_ExtendedTerm, gen_asmeta_basicterms_BooleanTerm_ConstantTerm, gen_asmeta_basicterms_BasicTerm_Term, gen_asmeta_structure_Initialization_NamedElement, gen_asmeta_structure_Asm_NamedElement, gen_asmeta_turbotransitionrules_TurboRule_Rule, gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration, gen_asmeta_turbotransitionrules_SeqRule_TurboRule, gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule, gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule, gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule, gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule, gen_asmeta_turbotransitionrules_IterateRule_TurboRule, gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule, gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule, gen_asmeta_derivedtransitionrules_DerivedRule_Rule, gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule, gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule, gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule, gen_asmeta_basictransitionrules_TermAsRule_Rule, gen_asmeta_basictransitionrules_BasicRule_Rule, gen_asmeta_basictransitionrules_ChooseRule_BasicRule, gen_asmeta_basictransitionrules_MacroCallRule_BasicRule, gen_asmeta_basictransitionrules_BlockRule_BasicRule, gen_asmeta_basictransitionrules_ConditionalRule_BasicRule, gen_asmeta_basictransitionrules_ForallRule_BasicRule, gen_asmeta_basictransitionrules_LetRule_BasicRule, gen_asmeta_basictransitionrules_ExtendRule_BasicRule, gen_asmeta_basictransitionrules_UpdateRule_BasicRule, gen_asmeta_basictransitionrules_SkipRule_BasicRule, gen_asmeta_basictransitionrules_MacroDeclaration_RuleDeclaration, gen_asmeta_definitions_RuleDeclaration_Classifier, gen_asmeta_definitions_LocalFunction_DynamicFunction, gen_asmeta_definitions_ControlledFunction_DynamicFunction, gen_asmeta_definitions_SharedFunction_DynamicFunction, gen_asmeta_definitions_MonitoredFunction_DynamicFunction, gen_asmeta_definitions_OutFunction_DynamicFunction, gen_asmeta_definitions_DynamicFunction_BasicFunction, gen_asmeta_definitions_StaticFunction_BasicFunction, gen_asmeta_definitions_DerivedFunction_Function, gen_asmeta_definitions_BasicFunction_Function, gen_asmeta_definitions_Invariant_Property, gen_asmeta_definitions_Function_Classifier, gen_asmeta_definitions_Classifier_NamedElement, gen_asmeta_definitions_Property_Classifier, gen_asmeta_domains_NaturalDomain_IntegerDomain, gen_asmeta_domains_UndefDomain_BasicTd, gen_asmeta_domains_TypeDomain_Domain, gen_asmeta_domains_StructuredTd_TypeDomain, gen_asmeta_domains_StringDomain_BasicTd, gen_asmeta_domains_SequenceDomain_StructuredTd, gen_asmeta_domains_RuleDomain_StructuredTd, gen_asmeta_domains_ReserveDomain_AbstractTd, gen_asmeta_domains_RealDomain_ComplexDomain, gen_asmeta_domains_ProductDomain_StructuredTd, gen_asmeta_domains_PowersetDomain_StructuredTd, gen_asmeta_domains_MapDomain_StructuredTd, gen_asmeta_domains_EnumTd_TypeDomain, gen_asmeta_domains_Domain_Classifier, gen_asmeta_domains_ConcreteDomain_Domain, gen_asmeta_domains_ComplexDomain_BasicTd, gen_asmeta_domains_CharDomain_BasicTd, gen_asmeta_domains_BooleanDomain_BasicTd, gen_asmeta_domains_BasicTd_TypeDomain, gen_asmeta_domains_BagDomain_StructuredTd, gen_asmeta_domains_AnyDomain_TypeDomain, gen_asmeta_domains_AgentDomain_AbstractTd, gen_asmeta_domains_AbstractTd_TypeDomain, gen_asmeta_domains_IntegerDomain_RealDomain},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
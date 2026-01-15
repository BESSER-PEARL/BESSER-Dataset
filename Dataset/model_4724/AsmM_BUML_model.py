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
asmeta_furtherterms_SequenceTerm = Class(name="asmeta::furtherterms::SequenceTerm")
CollectionTerm = Class(name="CollectionTerm")
asmeta_furtherterms_SequenceCt = Class(name="asmeta::furtherterms::SequenceCt")
asmeta_furtherterms_RealTerm = Class(name="asmeta::furtherterms::RealTerm")
asmeta_furtherterms_MapTerm = Class(name="asmeta::furtherterms::MapTerm")
basicterms_TupleTerm = Class(name="basicterms::TupleTerm")
asmeta_furtherterms_MapCt = Class(name="asmeta::furtherterms::MapCt")
asmeta_furtherterms_LetTerm = Class(name="asmeta::furtherterms::LetTerm")
VariableBindingTerm = Class(name="VariableBindingTerm")
asmeta_furtherterms_IntegerTerm = Class(name="asmeta::furtherterms::IntegerTerm")
ConstantTerm = Class(name="ConstantTerm")
asmeta_furtherterms_NaturalTerm = Class(name="asmeta::furtherterms::NaturalTerm")
asmeta_furtherterms_VariableBindingTerm = Class(name="asmeta::furtherterms::VariableBindingTerm", is_abstract=True)
ExtendedTerm = Class(name="ExtendedTerm")
asmeta_furtherterms_StringTerm = Class(name="asmeta::furtherterms::StringTerm")
asmeta_furtherterms_SetCt = Class(name="asmeta::furtherterms::SetCt")
ComprehensionTerm = Class(name="ComprehensionTerm")
asmeta_furtherterms_CharTerm = Class(name="asmeta::furtherterms::CharTerm")
asmeta_furtherterms_CaseTerm = Class(name="asmeta::furtherterms::CaseTerm")
asmeta_furtherterms_BagTerm = Class(name="asmeta::furtherterms::BagTerm")
basicterms_VariableTerm = Class(name="basicterms::VariableTerm")
basicterms_Term = Class(name="basicterms::Term")
asmeta_furtherterms_ForallTerm = Class(name="asmeta::furtherterms::ForallTerm")
FiniteQuantificationTerm = Class(name="FiniteQuantificationTerm")
asmeta_furtherterms_FiniteQuantificationTerm = Class(name="asmeta::furtherterms::FiniteQuantificationTerm", is_abstract=True)
asmeta_furtherterms_ExistUniqueTerm = Class(name="asmeta::furtherterms::ExistUniqueTerm")
asmeta_furtherterms_ExistTerm = Class(name="asmeta::furtherterms::ExistTerm")
asmeta_furtherterms_EnumTerm = Class(name="asmeta::furtherterms::EnumTerm")
asmeta_furtherterms_ConditionalTerm = Class(name="asmeta::furtherterms::ConditionalTerm")
asmeta_furtherterms_ComprehensionTerm = Class(name="asmeta::furtherterms::ComprehensionTerm", is_abstract=True)
asmeta_furtherterms_ComplexTerm = Class(name="asmeta::furtherterms::ComplexTerm")
asmeta_basicterms_FunctionTerm = Class(name="asmeta::basicterms::FunctionTerm")
Function = Class(name="Function")
asmeta_furtherterms_BagCt = Class(name="asmeta::furtherterms::BagCt")
asmeta_basicterms_VariableTerm = Class(name="asmeta::basicterms::VariableTerm")
BasicTerm = Class(name="BasicTerm")
furtherterms_FiniteQuantificationTerm = Class(name="furtherterms::FiniteQuantificationTerm")
asmeta_basicterms_UndefTerm = Class(name="asmeta::basicterms::UndefTerm")
asmeta_basicterms_TupleTerm = Class(name="asmeta::basicterms::TupleTerm")
asmeta_basicterms_SetTerm = Class(name="asmeta::basicterms::SetTerm")
asmeta_basicterms_RuleAsTerm = Class(name="asmeta::basicterms::RuleAsTerm")
RuleDeclaration = Class(name="RuleDeclaration")
DynamicFunction = Class(name="DynamicFunction")
asmeta_basicterms_LocationTerm = Class(name="asmeta::basicterms::LocationTerm")
FunctionTerm = Class(name="FunctionTerm")
asmeta_structure_DomainInitialization = Class(name="asmeta::structure::DomainInitialization")
asmeta_basicterms_ExtendedTerm = Class(name="asmeta::basicterms::ExtendedTerm", is_abstract=True)
Term = Class(name="Term")
domains_ConcreteDomain = Class(name="domains::ConcreteDomain")
asmeta_basicterms_DomainTerm = Class(name="asmeta::basicterms::DomainTerm")
asmeta_basicterms_ConstantTerm = Class(name="asmeta::basicterms::ConstantTerm", is_abstract=True)
asmeta_basicterms_CollectionTerm = Class(name="asmeta::basicterms::CollectionTerm", is_abstract=True)
asmeta_basicterms_BooleanTerm = Class(name="asmeta::basicterms::BooleanTerm")
asmeta_basicterms_BasicTerm = Class(name="asmeta::basicterms::BasicTerm", is_abstract=True)
asmeta_basicterms_Term = Class(name="asmeta::basicterms::Term", is_abstract=True)
domains_Domain = Class(name="domains::Domain")
basictransitionrules_TermAsRule = Class(name="basictransitionrules::TermAsRule")
asmeta_structure_NamedElement = Class(name="asmeta::structure::NamedElement", is_abstract=True)
asmeta_structure_AgentInitialization = Class(name="asmeta::structure::AgentInitialization")
basictransitionrules_MacroCallRule = Class(name="basictransitionrules::MacroCallRule")
Initialization = Class(name="Initialization")
asmeta_structure_Body = Class(name="asmeta::structure::Body")
FunctionDefinition = Class(name="FunctionDefinition")
Property_ = Class(name="Property")
DomainDefinition = Class(name="DomainDefinition")
Asm = Class(name="Asm")
asmeta_structure_FunctionInitialization = Class(name="asmeta::structure::FunctionInitialization")
asmeta_structure_Initialization = Class(name="asmeta::structure::Initialization")
NamedElement = Class(name="NamedElement")
DomainInitialization = Class(name="DomainInitialization")
FunctionInitialization = Class(name="FunctionInitialization")
AgentInitialization = Class(name="AgentInitialization")
asmeta_structure_Signature = Class(name="asmeta::structure::Signature")
Header = Class(name="Header")
domains_StructuredTd = Class(name="domains::StructuredTd")
asmeta_structure_ExportClause = Class(name="asmeta::structure::ExportClause")
asmeta_structure_ImportClause = Class(name="asmeta::structure::ImportClause")
asmeta_structure_FunctionDefinition = Class(name="asmeta::structure::FunctionDefinition")
asmeta_structure_DomainDefinition = Class(name="asmeta::structure::DomainDefinition")
LocalFunction = Class(name="LocalFunction")
asmeta_turbotransitionrules_TurboCallRule = Class(name="asmeta::turbotransitionrules::TurboCallRule")
turbotransitionrules_TurboDeclaration = Class(name="turbotransitionrules::TurboDeclaration")
asmeta_turbotransitionrules_TurboReturnRule = Class(name="asmeta::turbotransitionrules::TurboReturnRule")
asmeta_structure_Header = Class(name="asmeta::structure::Header")
ImportClause = Class(name="ImportClause")
Signature = Class(name="Signature")
ExportClause = Class(name="ExportClause")
asmeta_structure_Asm = Class(name="asmeta::structure::Asm")
Body = Class(name="Body")
basictransitionrules_MacroDeclaration = Class(name="basictransitionrules::MacroDeclaration")
asmeta_turbotransitionrules_TurboRule = Class(name="asmeta::turbotransitionrules::TurboRule", is_abstract=True)
Rule = Class(name="Rule")
asmeta_turbotransitionrules_TurboDeclaration = Class(name="asmeta::turbotransitionrules::TurboDeclaration")
asmeta_turbotransitionrules_SeqRule = Class(name="asmeta::turbotransitionrules::SeqRule")
TurboRule = Class(name="TurboRule")
asmeta_turbotransitionrules_TurboLocalStateRule = Class(name="asmeta::turbotransitionrules::TurboLocalStateRule")
basictransitionrules_Rule = Class(name="basictransitionrules::Rule")
asmeta_turbotransitionrules_IterateRule = Class(name="asmeta::turbotransitionrules::IterateRule")
turbotransitionrules_TurboCallRule = Class(name="turbotransitionrules::TurboCallRule")
asmeta_turbotransitionrules_TryCatchRule = Class(name="asmeta::turbotransitionrules::TryCatchRule")
asmeta_derivedtransitionrules_BasicDerivedRule = Class(name="asmeta::derivedtransitionrules::BasicDerivedRule", is_abstract=True)
DerivedRule = Class(name="DerivedRule")
asmeta_derivedtransitionrules_TurboDerivedRule = Class(name="asmeta::derivedtransitionrules::TurboDerivedRule", is_abstract=True)
asmeta_derivedtransitionrules_RecursiveWhileRule = Class(name="asmeta::derivedtransitionrules::RecursiveWhileRule")
TurboDerivedRule = Class(name="TurboDerivedRule")
asmeta_derivedtransitionrules_IterativeWhileRule = Class(name="asmeta::derivedtransitionrules::IterativeWhileRule")
asmeta_derivedtransitionrules_DerivedRule = Class(name="asmeta::derivedtransitionrules::DerivedRule", is_abstract=True)
asmeta_derivedtransitionrules_CaseRule = Class(name="asmeta::derivedtransitionrules::CaseRule")
BasicDerivedRule = Class(name="BasicDerivedRule")
asmeta_basictransitionrules_ForallRule = Class(name="asmeta::basictransitionrules::ForallRule")
asmeta_basictransitionrules_TermAsRule = Class(name="asmeta::basictransitionrules::TermAsRule")
asmeta_basictransitionrules_BasicRule = Class(name="asmeta::basictransitionrules::BasicRule", is_abstract=True)
asmeta_basictransitionrules_Rule = Class(name="asmeta::basictransitionrules::Rule", is_abstract=True)
asmeta_basictransitionrules_ChooseRule = Class(name="asmeta::basictransitionrules::ChooseRule")
BasicRule = Class(name="BasicRule")
asmeta_basictransitionrules_MacroCallRule = Class(name="asmeta::basictransitionrules::MacroCallRule")
asmeta_basictransitionrules_BlockRule = Class(name="asmeta::basictransitionrules::BlockRule")
asmeta_basictransitionrules_ConditionalRule = Class(name="asmeta::basictransitionrules::ConditionalRule")
asmeta_basictransitionrules_MacroDeclaration = Class(name="asmeta::basictransitionrules::MacroDeclaration")
asmeta_definitions_RuleDeclaration = Class(name="asmeta::definitions::RuleDeclaration", is_abstract=True)
Classifier = Class(name="Classifier")
asmeta_basictransitionrules_LetRule = Class(name="asmeta::basictransitionrules::LetRule")
asmeta_basictransitionrules_ExtendRule = Class(name="asmeta::basictransitionrules::ExtendRule")
asmeta_basictransitionrules_UpdateRule = Class(name="asmeta::basictransitionrules::UpdateRule")
asmeta_basictransitionrules_SkipRule = Class(name="asmeta::basictransitionrules::SkipRule")
Invariant = Class(name="Invariant")
asmeta_definitions_LocalFunction = Class(name="asmeta::definitions::LocalFunction")
asmeta_definitions_ControlledFunction = Class(name="asmeta::definitions::ControlledFunction")
asmeta_definitions_SharedFunction = Class(name="asmeta::definitions::SharedFunction")
asmeta_definitions_MonitoredFunction = Class(name="asmeta::definitions::MonitoredFunction")
asmeta_definitions_OutFunction = Class(name="asmeta::definitions::OutFunction")
asmeta_definitions_DynamicFunction = Class(name="asmeta::definitions::DynamicFunction", is_abstract=True)
BasicFunction = Class(name="BasicFunction")
asmeta_definitions_StaticFunction = Class(name="asmeta::definitions::StaticFunction")
asmeta_definitions_DerivedFunction = Class(name="asmeta::definitions::DerivedFunction")
asmeta_definitions_BasicFunction = Class(name="asmeta::definitions::BasicFunction", is_abstract=True)
asmeta_definitions_Invariant = Class(name="asmeta::definitions::Invariant")
asmeta_definitions_Function = Class(name="asmeta::definitions::Function", is_abstract=True)
domains_EnumElement = Class(name="domains::EnumElement")
asmeta_domains_EnumElement = Class(name="asmeta::domains::EnumElement")
asmeta_domains_Domain = Class(name="asmeta::domains::Domain", is_abstract=True)
asmeta_definitions_Classifier = Class(name="asmeta::definitions::Classifier", is_abstract=True)
asmeta_definitions_Property = Class(name="asmeta::definitions::Property")
asmeta_domains_NaturalDomain = Class(name="asmeta::domains::NaturalDomain")
IntegerDomain = Class(name="IntegerDomain")
asmeta_domains_UndefDomain = Class(name="asmeta::domains::UndefDomain")
BasicTd = Class(name="BasicTd")
asmeta_domains_TypeDomain = Class(name="asmeta::domains::TypeDomain", is_abstract=True)
Domain = Class(name="Domain")
asmeta_domains_StructuredTd = Class(name="asmeta::domains::StructuredTd", is_abstract=True)
TypeDomain = Class(name="TypeDomain")
asmeta_domains_StringDomain = Class(name="asmeta::domains::StringDomain")
asmeta_domains_SequenceDomain = Class(name="asmeta::domains::SequenceDomain")
StructuredTd = Class(name="StructuredTd")
asmeta_domains_RuleDomain = Class(name="asmeta::domains::RuleDomain")
asmeta_domains_ReserveDomain = Class(name="asmeta::domains::ReserveDomain")
AbstractTd = Class(name="AbstractTd")
asmeta_domains_RealDomain = Class(name="asmeta::domains::RealDomain")
ComplexDomain = Class(name="ComplexDomain")
asmeta_domains_ProductDomain = Class(name="asmeta::domains::ProductDomain")
asmeta_domains_PowersetDomain = Class(name="asmeta::domains::PowersetDomain")
asmeta_domains_MapDomain = Class(name="asmeta::domains::MapDomain")
asmeta_domains_IntegerDomain = Class(name="asmeta::domains::IntegerDomain")
RealDomain = Class(name="RealDomain")
asmeta_domains_EnumTd = Class(name="asmeta::domains::EnumTd")
asmeta_domains_ConcreteDomain = Class(name="asmeta::domains::ConcreteDomain")
domains_TypeDomain = Class(name="domains::TypeDomain")
asmeta_domains_ComplexDomain = Class(name="asmeta::domains::ComplexDomain")
asmeta_domains_CharDomain = Class(name="asmeta::domains::CharDomain")
asmeta_domains_BooleanDomain = Class(name="asmeta::domains::BooleanDomain")
asmeta_domains_BasicTd = Class(name="asmeta::domains::BasicTd", is_abstract=True)
asmeta_domains_BagDomain = Class(name="asmeta::domains::BagDomain")
asmeta_domains_AnyDomain = Class(name="asmeta::domains::AnyDomain")
asmeta_domains_AgentDomain = Class(name="asmeta::domains::AgentDomain")
asmeta_domains_AbstractTd = Class(name="asmeta::domains::AbstractTd")

# asmeta_furtherterms_SequenceTerm class attributes and methods
asmeta_furtherterms_SequenceTerm_terms: Property = Property(name="terms", type=StringType)
asmeta_furtherterms_SequenceTerm.attributes={asmeta_furtherterms_SequenceTerm_terms}

# CollectionTerm class attributes and methods

# asmeta_furtherterms_SequenceCt class attributes and methods

# asmeta_furtherterms_RealTerm class attributes and methods

# asmeta_furtherterms_MapTerm class attributes and methods

# basicterms_TupleTerm class attributes and methods

# asmeta_furtherterms_MapCt class attributes and methods

# asmeta_furtherterms_LetTerm class attributes and methods

# VariableBindingTerm class attributes and methods

# asmeta_furtherterms_IntegerTerm class attributes and methods

# ConstantTerm class attributes and methods

# asmeta_furtherterms_NaturalTerm class attributes and methods

# asmeta_furtherterms_VariableBindingTerm class attributes and methods

# ExtendedTerm class attributes and methods

# asmeta_furtherterms_StringTerm class attributes and methods

# asmeta_furtherterms_SetCt class attributes and methods

# ComprehensionTerm class attributes and methods

# asmeta_furtherterms_CharTerm class attributes and methods

# asmeta_furtherterms_CaseTerm class attributes and methods
asmeta_furtherterms_CaseTerm_resultTerms: Property = Property(name="resultTerms", type=StringType)
asmeta_furtherterms_CaseTerm.attributes={asmeta_furtherterms_CaseTerm_resultTerms}

# asmeta_furtherterms_BagTerm class attributes and methods

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

# asmeta_furtherterms_ComplexTerm class attributes and methods

# asmeta_basicterms_FunctionTerm class attributes and methods

# Function class attributes and methods

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
asmeta_basicterms_TupleTerm.attributes={asmeta_basicterms_TupleTerm_arity, asmeta_basicterms_TupleTerm_terms}

# asmeta_basicterms_SetTerm class attributes and methods

# asmeta_basicterms_RuleAsTerm class attributes and methods

# RuleDeclaration class attributes and methods

# DynamicFunction class attributes and methods

# asmeta_basicterms_LocationTerm class attributes and methods

# FunctionTerm class attributes and methods

# asmeta_structure_DomainInitialization class attributes and methods

# asmeta_basicterms_ExtendedTerm class attributes and methods

# Term class attributes and methods

# domains_ConcreteDomain class attributes and methods

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

# asmeta_structure_Initialization class attributes and methods

# NamedElement class attributes and methods

# DomainInitialization class attributes and methods

# FunctionInitialization class attributes and methods

# AgentInitialization class attributes and methods

# asmeta_structure_Signature class attributes and methods

# Header class attributes and methods

# domains_StructuredTd class attributes and methods

# asmeta_structure_ExportClause class attributes and methods

# asmeta_structure_ImportClause class attributes and methods
asmeta_structure_ImportClause_moduleName: Property = Property(name="moduleName", type=StringType)
asmeta_structure_ImportClause.attributes={asmeta_structure_ImportClause_moduleName}

# asmeta_structure_FunctionDefinition class attributes and methods

# asmeta_structure_DomainDefinition class attributes and methods

# LocalFunction class attributes and methods

# asmeta_turbotransitionrules_TurboCallRule class attributes and methods
asmeta_turbotransitionrules_TurboCallRule_parameters: Property = Property(name="parameters", type=StringType)
asmeta_turbotransitionrules_TurboCallRule.attributes={asmeta_turbotransitionrules_TurboCallRule_parameters}

# turbotransitionrules_TurboDeclaration class attributes and methods

# asmeta_turbotransitionrules_TurboReturnRule class attributes and methods

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

# asmeta_turbotransitionrules_IterateRule class attributes and methods

# turbotransitionrules_TurboCallRule class attributes and methods

# asmeta_turbotransitionrules_TryCatchRule class attributes and methods

# asmeta_derivedtransitionrules_BasicDerivedRule class attributes and methods

# DerivedRule class attributes and methods

# asmeta_derivedtransitionrules_TurboDerivedRule class attributes and methods

# asmeta_derivedtransitionrules_RecursiveWhileRule class attributes and methods

# TurboDerivedRule class attributes and methods

# asmeta_derivedtransitionrules_IterativeWhileRule class attributes and methods

# asmeta_derivedtransitionrules_DerivedRule class attributes and methods

# asmeta_derivedtransitionrules_CaseRule class attributes and methods
asmeta_derivedtransitionrules_CaseRule_caseBranches: Property = Property(name="caseBranches", type=StringType)
asmeta_derivedtransitionrules_CaseRule.attributes={asmeta_derivedtransitionrules_CaseRule_caseBranches}

# BasicDerivedRule class attributes and methods

# asmeta_basictransitionrules_ForallRule class attributes and methods
asmeta_basictransitionrules_ForallRule_ranges: Property = Property(name="ranges", type=StringType)
asmeta_basictransitionrules_ForallRule.attributes={asmeta_basictransitionrules_ForallRule_ranges}

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

# asmeta_basictransitionrules_MacroDeclaration class attributes and methods

# asmeta_definitions_RuleDeclaration class attributes and methods
asmeta_definitions_RuleDeclaration_arity: Property = Property(name="arity", type=StringType)
asmeta_definitions_RuleDeclaration.attributes={asmeta_definitions_RuleDeclaration_arity}

# Classifier class attributes and methods

# asmeta_basictransitionrules_LetRule class attributes and methods

# asmeta_basictransitionrules_ExtendRule class attributes and methods

# asmeta_basictransitionrules_UpdateRule class attributes and methods

# asmeta_basictransitionrules_SkipRule class attributes and methods

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

# domains_EnumElement class attributes and methods

# asmeta_domains_EnumElement class attributes and methods
asmeta_domains_EnumElement_symbol: Property = Property(name="symbol", type=StringType)
asmeta_domains_EnumElement.attributes={asmeta_domains_EnumElement_symbol}

# asmeta_domains_Domain class attributes and methods
asmeta_domains_Domain_m_compatible: Method = Method(name="compatible", parameters={})
asmeta_domains_Domain.methods={asmeta_domains_Domain_m_compatible}

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
        Property(name="terms", type=asmeta_furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="basicterms", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
term23: BinaryAssociation = BinaryAssociation(
    name="term23",
    ends={
        Property(name="basicterms_Term25", type=asmeta_furtherterms_ComprehensionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_furtherterms_ComprehensionTerm24", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
arguments41: BinaryAssociation = BinaryAssociation(
    name="arguments41",
    ends={
        Property(name="basicterms_TupleTerm42", type=asmeta_basicterms_FunctionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_FunctionTerm", type=basicterms_TupleTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function43: BinaryAssociation = BinaryAssociation(
    name="function43",
    ends={
        Property(name="Function", type=asmeta_basicterms_FunctionTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_FunctionTerm44", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
finiteQuantificationTerm36: BinaryAssociation = BinaryAssociation(
    name="finiteQuantificationTerm36",
    ends={
        Property(name="terms37", type=asmeta_basicterms_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="furtherterms", type=furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(0, 1))
    }
)
term38: BinaryAssociation = BinaryAssociation(
    name="term38",
    ends={
        Property(name="basicterms_Term39", type=asmeta_basicterms_SetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_SetTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 9999))
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="basicterms_Term65", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
rule40: BinaryAssociation = BinaryAssociation(
    name="rule40",
    ends={
        Property(name="RuleDeclaration", type=asmeta_basicterms_RuleAsTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_RuleAsTerm", type=RuleDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
initializedFunction66: BinaryAssociation = BinaryAssociation(
    name="initializedFunction66",
    ends={
        Property(name="definitions67", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="DynamicFunction", type=DynamicFunction, multiplicity=Multiplicity(1, 1))
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="basicterms_VariableTerm70", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization69", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedDomain71: BinaryAssociation = BinaryAssociation(
    name="initializedDomain71",
    ends={
        Property(name="definitions72", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
body73: BinaryAssociation = BinaryAssociation(
    name="body73",
    ends={
        Property(name="basicterms_Term74", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain45: BinaryAssociation = BinaryAssociation(
    name="domain45",
    ends={
        Property(name="domains_Domain", type=asmeta_basicterms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_Term", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
termAsRule46: BinaryAssociation = BinaryAssociation(
    name="termAsRule46",
    ends={
        Property(name="transitionrules", type=asmeta_basicterms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="basictransitionrules", type=basictransitionrules_TermAsRule, multiplicity=Multiplicity(0, 9999))
    }
)
program47: BinaryAssociation = BinaryAssociation(
    name="program47",
    ends={
        Property(name="basictransitionrules_MacroCallRule", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_AgentInitialization", type=basictransitionrules_MacroCallRule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain48: BinaryAssociation = BinaryAssociation(
    name="domain48",
    ends={
        Property(name="domains_Domain50", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_AgentInitialization49", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
initialState51: BinaryAssociation = BinaryAssociation(
    name="initialState51",
    ends={
        Property(name="structure", type=asmeta_structure_AgentInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
functionDefinition52: BinaryAssociation = BinaryAssociation(
    name="functionDefinition52",
    ends={
        Property(name="FunctionDefinition", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body", type=FunctionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property53: BinaryAssociation = BinaryAssociation(
    name="property53",
    ends={
        Property(name="Property", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body54", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainDefinition55: BinaryAssociation = BinaryAssociation(
    name="domainDefinition55",
    ends={
        Property(name="DomainDefinition", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body56", type=DomainDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruleDeclaration57: BinaryAssociation = BinaryAssociation(
    name="ruleDeclaration57",
    ends={
        Property(name="definitions", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleDeclaration58", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
asm59: BinaryAssociation = BinaryAssociation(
    name="asm59",
    ends={
        Property(name="structure60", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="Asm", type=Asm, multiplicity=Multiplicity(0, 1))
    }
)
initialState61: BinaryAssociation = BinaryAssociation(
    name="initialState61",
    ends={
        Property(name="structure63", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization62", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
body111: BinaryAssociation = BinaryAssociation(
    name="body111",
    ends={
        Property(name="basicterms_Term112", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definedDomain113: BinaryAssociation = BinaryAssociation(
    name="definedDomain113",
    ends={
        Property(name="definitions115", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="domains114", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
domainInitialization116: BinaryAssociation = BinaryAssociation(
    name="domainInitialization116",
    ends={
        Property(name="structure117", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainInitialization", type=DomainInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionInitialization118: BinaryAssociation = BinaryAssociation(
    name="functionInitialization118",
    ends={
        Property(name="structure119", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionInitialization", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agentInitialization120: BinaryAssociation = BinaryAssociation(
    name="agentInitialization120",
    ends={
        Property(name="structure121", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="AgentInitialization", type=AgentInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState75: BinaryAssociation = BinaryAssociation(
    name="initialState75",
    ends={
        Property(name="structure77", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization76", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
domain78: BinaryAssociation = BinaryAssociation(
    name="domain78",
    ends={
        Property(name="definitions80", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="domains79", type=domains_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function81: BinaryAssociation = BinaryAssociation(
    name="function81",
    ends={
        Property(name="definitions83", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Function82", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headerSection84: BinaryAssociation = BinaryAssociation(
    name="headerSection84",
    ends={
        Property(name="structure85", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
structuredDomain86: BinaryAssociation = BinaryAssociation(
    name="structuredDomain86",
    ends={
        Property(name="domains_StructuredTd", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Signature", type=domains_StructuredTd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportedFunction87: BinaryAssociation = BinaryAssociation(
    name="exportedFunction87",
    ends={
        Property(name="Function88", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
exportedDomain89: BinaryAssociation = BinaryAssociation(
    name="exportedDomain89",
    ends={
        Property(name="domains_Domain91", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause90", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
exportedRule92: BinaryAssociation = BinaryAssociation(
    name="exportedRule92",
    ends={
        Property(name="RuleDeclaration94", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause93", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
importedDomain95: BinaryAssociation = BinaryAssociation(
    name="importedDomain95",
    ends={
        Property(name="domains_Domain96", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
importedFunction97: BinaryAssociation = BinaryAssociation(
    name="importedFunction97",
    ends={
        Property(name="Function99", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause98", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
importedRule100: BinaryAssociation = BinaryAssociation(
    name="importedRule100",
    ends={
        Property(name="RuleDeclaration102", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause101", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
body103: BinaryAssociation = BinaryAssociation(
    name="body103",
    ends={
        Property(name="basicterms_Term104", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable105: BinaryAssociation = BinaryAssociation(
    name="variable105",
    ends={
        Property(name="basicterms_VariableTerm107", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition106", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999))
    }
)
definedFunction108: BinaryAssociation = BinaryAssociation(
    name="definedFunction108",
    ends={
        Property(name="definitions110", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="Function109", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
init147: BinaryAssociation = BinaryAssociation(
    name="init147",
    ends={
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="basictransitionrules_Rule", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1))
    }
)
body148: BinaryAssociation = BinaryAssociation(
    name="body148",
    ends={
        Property(name="basictransitionrules_Rule150", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule149", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localFunction151: BinaryAssociation = BinaryAssociation(
    name="localFunction151",
    ends={
        Property(name="LocalFunction", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule152", type=LocalFunction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
calledRule153: BinaryAssociation = BinaryAssociation(
    name="calledRule153",
    ends={
        Property(name="turbotransitionrules_TurboDeclaration", type=asmeta_turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboCallRule", type=turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
location154: BinaryAssociation = BinaryAssociation(
    name="location154",
    ends={
        Property(name="basicterms_Term155", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
asm122: BinaryAssociation = BinaryAssociation(
    name="asm122",
    ends={
        Property(name="structure124", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Asm123", type=Asm, multiplicity=Multiplicity(1, 1))
    }
)
importClause125: BinaryAssociation = BinaryAssociation(
    name="importClause125",
    ends={
        Property(name="ImportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header", type=ImportClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature126: BinaryAssociation = BinaryAssociation(
    name="signature126",
    ends={
        Property(name="structure127", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature", type=Signature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exportClause128: BinaryAssociation = BinaryAssociation(
    name="exportClause128",
    ends={
        Property(name="ExportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header129", type=ExportClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asm130: BinaryAssociation = BinaryAssociation(
    name="asm130",
    ends={
        Property(name="structure132", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Asm131", type=Asm, multiplicity=Multiplicity(0, 1))
    }
)
initialState133: BinaryAssociation = BinaryAssociation(
    name="initialState133",
    ends={
        Property(name="Initialization134", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm", type=Initialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultInitialState135: BinaryAssociation = BinaryAssociation(
    name="defaultInitialState135",
    ends={
        Property(name="structure137", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization136", type=Initialization, multiplicity=Multiplicity(0, 1))
    }
)
bodySection138: BinaryAssociation = BinaryAssociation(
    name="bodySection138",
    ends={
        Property(name="structure139", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Body", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headerSection140: BinaryAssociation = BinaryAssociation(
    name="headerSection140",
    ends={
        Property(name="structure142", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Header141", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainrule143: BinaryAssociation = BinaryAssociation(
    name="mainrule143",
    ends={
        Property(name="basictransitionrules_MacroDeclaration", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm144", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
resultType145: BinaryAssociation = BinaryAssociation(
    name="resultType145",
    ends={
        Property(name="domains_Domain146", type=asmeta_turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboDeclaration", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
location158: BinaryAssociation = BinaryAssociation(
    name="location158",
    ends={
        Property(name="basicterms_Term159", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
catchRule160: BinaryAssociation = BinaryAssociation(
    name="catchRule160",
    ends={
        Property(name="basictransitionrules_Rule162", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule161", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryRule163: BinaryAssociation = BinaryAssociation(
    name="tryRule163",
    ends={
        Property(name="basictransitionrules_Rule165", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule164", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule166: BinaryAssociation = BinaryAssociation(
    name="rule166",
    ends={
        Property(name="basictransitionrules_Rule167", type=asmeta_turbotransitionrules_IterateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_IterateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updateRule156: BinaryAssociation = BinaryAssociation(
    name="updateRule156",
    ends={
        Property(name="turbotransitionrules_TurboCallRule", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule157", type=turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1))
    }
)
otherwiseBranch183: BinaryAssociation = BinaryAssociation(
    name="otherwiseBranch183",
    ends={
        Property(name="basictransitionrules_Rule185", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule184", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule168: BinaryAssociation = BinaryAssociation(
    name="rule168",
    ends={
        Property(name="basictransitionrules_Rule169", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard170: BinaryAssociation = BinaryAssociation(
    name="guard170",
    ends={
        Property(name="basicterms_Term172", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule171", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
guard173: BinaryAssociation = BinaryAssociation(
    name="guard173",
    ends={
        Property(name="basicterms_Term174", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
rule175: BinaryAssociation = BinaryAssociation(
    name="rule175",
    ends={
        Property(name="basictransitionrules_Rule177", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule176", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term178: BinaryAssociation = BinaryAssociation(
    name="term178",
    ends={
        Property(name="basicterms_Term179", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
elseRule204: BinaryAssociation = BinaryAssociation(
    name="elseRule204",
    ends={
        Property(name="basictransitionrules_Rule206", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule205", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseTerm180: BinaryAssociation = BinaryAssociation(
    name="caseTerm180",
    ends={
        Property(name="basicterms_Term182", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule181", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
thenRule207: BinaryAssociation = BinaryAssociation(
    name="thenRule207",
    ends={
        Property(name="basictransitionrules_Rule209", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule208", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term186: BinaryAssociation = BinaryAssociation(
    name="term186",
    ends={
        Property(name="terms188", type=asmeta_basictransitionrules_TermAsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="basicterms187", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
ifnone189: BinaryAssociation = BinaryAssociation(
    name="ifnone189",
    ends={
        Property(name="basictransitionrules_Rule190", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doRule191: BinaryAssociation = BinaryAssociation(
    name="doRule191",
    ends={
        Property(name="basictransitionrules_Rule193", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule192", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard194: BinaryAssociation = BinaryAssociation(
    name="guard194",
    ends={
        Property(name="basicterms_Term196", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule195", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
variable197: BinaryAssociation = BinaryAssociation(
    name="variable197",
    ends={
        Property(name="basicterms_VariableTerm199", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule198", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
calledMacro200: BinaryAssociation = BinaryAssociation(
    name="calledMacro200",
    ends={
        Property(name="basictransitionrules_MacroDeclaration201", type=asmeta_basictransitionrules_MacroCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_MacroCallRule", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
guard202: BinaryAssociation = BinaryAssociation(
    name="guard202",
    ends={
        Property(name="basicterms_Term203", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
variable239: BinaryAssociation = BinaryAssociation(
    name="variable239",
    ends={
        Property(name="basicterms_VariableTerm240", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_RuleDeclaration", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999))
    }
)
variable210: BinaryAssociation = BinaryAssociation(
    name="variable210",
    ends={
        Property(name="basicterms_VariableTerm211", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
guard212: BinaryAssociation = BinaryAssociation(
    name="guard212",
    ends={
        Property(name="basicterms_Term214", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule213", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
doRule215: BinaryAssociation = BinaryAssociation(
    name="doRule215",
    ends={
        Property(name="basictransitionrules_Rule217", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule216", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inRule218: BinaryAssociation = BinaryAssociation(
    name="inRule218",
    ends={
        Property(name="basictransitionrules_Rule219", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression220: BinaryAssociation = BinaryAssociation(
    name="initExpression220",
    ends={
        Property(name="basicterms_Term222", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule221", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
variable223: BinaryAssociation = BinaryAssociation(
    name="variable223",
    ends={
        Property(name="basicterms_VariableTerm225", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule224", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
extendedDomain226: BinaryAssociation = BinaryAssociation(
    name="extendedDomain226",
    ends={
        Property(name="domains_Domain227", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
boundVar228: BinaryAssociation = BinaryAssociation(
    name="boundVar228",
    ends={
        Property(name="basicterms_VariableTerm230", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule229", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
doRule231: BinaryAssociation = BinaryAssociation(
    name="doRule231",
    ends={
        Property(name="basictransitionrules_Rule233", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule232", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updatingTerm234: BinaryAssociation = BinaryAssociation(
    name="updatingTerm234",
    ends={
        Property(name="basicterms_Term235", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
location236: BinaryAssociation = BinaryAssociation(
    name="location236",
    ends={
        Property(name="basicterms_Term238", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule237", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
domain263: BinaryAssociation = BinaryAssociation(
    name="domain263",
    ends={
        Property(name="domains_Domain264", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
codomain265: BinaryAssociation = BinaryAssociation(
    name="codomain265",
    ends={
        Property(name="domains_Domain267", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function266", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
definition268: BinaryAssociation = BinaryAssociation(
    name="definition268",
    ends={
        Property(name="structure270", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionDefinition269", type=FunctionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
constraint241: BinaryAssociation = BinaryAssociation(
    name="constraint241",
    ends={
        Property(name="definitions242", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
ruleBody243: BinaryAssociation = BinaryAssociation(
    name="ruleBody243",
    ends={
        Property(name="basictransitionrules_Rule245", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_RuleDeclaration244", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1))
    }
)
asmBody246: BinaryAssociation = BinaryAssociation(
    name="asmBody246",
    ends={
        Property(name="structure248", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Body247", type=Body, multiplicity=Multiplicity(1, 1))
    }
)
initialization249: BinaryAssociation = BinaryAssociation(
    name="initialization249",
    ends={
        Property(name="structure251", type=asmeta_definitions_DynamicFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionInitialization250", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedDomain252: BinaryAssociation = BinaryAssociation(
    name="constrainedDomain252",
    ends={
        Property(name="definitions254", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="domains253", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
body255: BinaryAssociation = BinaryAssociation(
    name="body255",
    ends={
        Property(name="basicterms_Term256", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Invariant", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedRule257: BinaryAssociation = BinaryAssociation(
    name="constrainedRule257",
    ends={
        Property(name="definitions259", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleDeclaration258", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedFunction260: BinaryAssociation = BinaryAssociation(
    name="constrainedFunction260",
    ends={
        Property(name="definitions262", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="Function261", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
element286: BinaryAssociation = BinaryAssociation(
    name="element286",
    ends={
        Property(name="domains_EnumElement", type=asmeta_domains_EnumTd, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_EnumTd", type=domains_EnumElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraint271: BinaryAssociation = BinaryAssociation(
    name="constraint271",
    ends={
        Property(name="definitions273", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant272", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
signature274: BinaryAssociation = BinaryAssociation(
    name="signature274",
    ends={
        Property(name="structure276", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature275", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
domain277: BinaryAssociation = BinaryAssociation(
    name="domain277",
    ends={
        Property(name="domains_Domain278", type=asmeta_domains_SequenceDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_SequenceDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
baseDomain279: BinaryAssociation = BinaryAssociation(
    name="baseDomain279",
    ends={
        Property(name="domains_Domain280", type=asmeta_domains_PowersetDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_PowersetDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
sourceDomain281: BinaryAssociation = BinaryAssociation(
    name="sourceDomain281",
    ends={
        Property(name="domains_Domain282", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
targetDomain283: BinaryAssociation = BinaryAssociation(
    name="targetDomain283",
    ends={
        Property(name="domains_Domain285", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain284", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
constraint287: BinaryAssociation = BinaryAssociation(
    name="constraint287",
    ends={
        Property(name="definitions289", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant288", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
signature290: BinaryAssociation = BinaryAssociation(
    name="signature290",
    ends={
        Property(name="structure292", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature291", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
initialization293: BinaryAssociation = BinaryAssociation(
    name="initialization293",
    ends={
        Property(name="structure295", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainInitialization294", type=DomainInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
definition296: BinaryAssociation = BinaryAssociation(
    name="definition296",
    ends={
        Property(name="structure298", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainDefinition297", type=DomainDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeDomain299: BinaryAssociation = BinaryAssociation(
    name="typeDomain299",
    ends={
        Property(name="domains_TypeDomain", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_ConcreteDomain", type=domains_TypeDomain, multiplicity=Multiplicity(1, 1))
    }
)
domain300: BinaryAssociation = BinaryAssociation(
    name="domain300",
    ends={
        Property(name="domains_Domain301", type=asmeta_domains_BagDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_BagDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_asmeta_furtherterms_SequenceTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_SequenceTerm)
gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_SequenceCt)
gen_asmeta_furtherterms_RealTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_RealTerm)
gen_asmeta_furtherterms_MapTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_MapTerm)
gen_asmeta_furtherterms_MapCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_MapCt)
gen_asmeta_furtherterms_LetTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_LetTerm)
gen_asmeta_furtherterms_IntegerTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_IntegerTerm)
gen_asmeta_furtherterms_NaturalTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_NaturalTerm)
gen_asmeta_furtherterms_VariableBindingTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_VariableBindingTerm)
gen_asmeta_furtherterms_StringTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_StringTerm)
gen_asmeta_furtherterms_SetCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_SetCt)
gen_asmeta_furtherterms_ComplexTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_ComplexTerm)
gen_asmeta_furtherterms_CharTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_CharTerm)
gen_asmeta_furtherterms_CaseTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_CaseTerm)
gen_asmeta_furtherterms_BagTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_BagTerm)
gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ForallTerm)
gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_FiniteQuantificationTerm)
gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistUniqueTerm)
gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistTerm)
gen_asmeta_furtherterms_EnumTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_EnumTerm)
gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_ConditionalTerm)
gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_ComprehensionTerm)
gen_asmeta_basicterms_FunctionTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_FunctionTerm)
gen_asmeta_furtherterms_BagCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_BagCt)
gen_asmeta_basicterms_VariableTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_VariableTerm)
gen_asmeta_basicterms_UndefTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_basicterms_UndefTerm)
gen_asmeta_basicterms_TupleTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_TupleTerm)
gen_asmeta_basicterms_SetTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_basicterms_SetTerm)
gen_asmeta_basicterms_RuleAsTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_RuleAsTerm)
gen_asmeta_basicterms_LocationTerm_FunctionTerm = Generalization(general=FunctionTerm, specific=asmeta_basicterms_LocationTerm)
gen_asmeta_basicterms_ExtendedTerm_Term = Generalization(general=Term, specific=asmeta_basicterms_ExtendedTerm)
gen_asmeta_basicterms_DomainTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_DomainTerm)
gen_asmeta_basicterms_ConstantTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_ConstantTerm)
gen_asmeta_basicterms_CollectionTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_CollectionTerm)
gen_asmeta_basicterms_BooleanTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_basicterms_BooleanTerm)
gen_asmeta_basicterms_BasicTerm_Term = Generalization(general=Term, specific=asmeta_basicterms_BasicTerm)
gen_asmeta_structure_Initialization_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Initialization)
gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboCallRule)
gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboReturnRule)
gen_asmeta_structure_Asm_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Asm)
gen_asmeta_turbotransitionrules_TurboRule_Rule = Generalization(general=Rule, specific=asmeta_turbotransitionrules_TurboRule)
gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration = Generalization(general=RuleDeclaration, specific=asmeta_turbotransitionrules_TurboDeclaration)
gen_asmeta_turbotransitionrules_SeqRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_SeqRule)
gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboLocalStateRule)
gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TryCatchRule)
gen_asmeta_turbotransitionrules_IterateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_IterateRule)
gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_BasicDerivedRule)
gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_TurboDerivedRule)
gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_RecursiveWhileRule)
gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_IterativeWhileRule)
gen_asmeta_derivedtransitionrules_DerivedRule_Rule = Generalization(general=Rule, specific=asmeta_derivedtransitionrules_DerivedRule)
gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule = Generalization(general=BasicDerivedRule, specific=asmeta_derivedtransitionrules_CaseRule)
gen_asmeta_basictransitionrules_ForallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ForallRule)
gen_asmeta_basictransitionrules_TermAsRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_TermAsRule)
gen_asmeta_basictransitionrules_BasicRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_BasicRule)
gen_asmeta_basictransitionrules_ChooseRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ChooseRule)
gen_asmeta_basictransitionrules_MacroCallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_MacroCallRule)
gen_asmeta_basictransitionrules_BlockRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_BlockRule)
gen_asmeta_basictransitionrules_ConditionalRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ConditionalRule)
gen_asmeta_basictransitionrules_SkipRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_SkipRule)
gen_asmeta_basictransitionrules_MacroDeclaration_RuleDeclaration = Generalization(general=RuleDeclaration, specific=asmeta_basictransitionrules_MacroDeclaration)
gen_asmeta_definitions_RuleDeclaration_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_RuleDeclaration)
gen_asmeta_basictransitionrules_LetRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_LetRule)
gen_asmeta_basictransitionrules_ExtendRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ExtendRule)
gen_asmeta_basictransitionrules_UpdateRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_UpdateRule)
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
gen_asmeta_domains_Domain_Classifier = Generalization(general=Classifier, specific=asmeta_domains_Domain)
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
gen_asmeta_domains_IntegerDomain_RealDomain = Generalization(general=RealDomain, specific=asmeta_domains_IntegerDomain)
gen_asmeta_domains_EnumTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_EnumTd)
gen_asmeta_domains_ConcreteDomain_Domain = Generalization(general=Domain, specific=asmeta_domains_ConcreteDomain)
gen_asmeta_domains_ComplexDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_ComplexDomain)
gen_asmeta_domains_CharDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_CharDomain)
gen_asmeta_domains_BooleanDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_BooleanDomain)
gen_asmeta_domains_BasicTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_BasicTd)
gen_asmeta_domains_BagDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_BagDomain)
gen_asmeta_domains_AnyDomain_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_AnyDomain)
gen_asmeta_domains_AgentDomain_AbstractTd = Generalization(general=AbstractTd, specific=asmeta_domains_AgentDomain)
gen_asmeta_domains_AbstractTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_AbstractTd)

# Domain Model
domain_model = DomainModel(
    name="asmeta",
    types={asmeta_furtherterms_SequenceTerm, CollectionTerm, asmeta_furtherterms_SequenceCt, asmeta_furtherterms_RealTerm, asmeta_furtherterms_MapTerm, basicterms_TupleTerm, asmeta_furtherterms_MapCt, asmeta_furtherterms_LetTerm, VariableBindingTerm, asmeta_furtherterms_IntegerTerm, ConstantTerm, asmeta_furtherterms_NaturalTerm, asmeta_furtherterms_VariableBindingTerm, ExtendedTerm, asmeta_furtherterms_StringTerm, asmeta_furtherterms_SetCt, ComprehensionTerm, asmeta_furtherterms_CharTerm, asmeta_furtherterms_CaseTerm, asmeta_furtherterms_BagTerm, basicterms_VariableTerm, basicterms_Term, asmeta_furtherterms_ForallTerm, FiniteQuantificationTerm, asmeta_furtherterms_FiniteQuantificationTerm, asmeta_furtherterms_ExistUniqueTerm, asmeta_furtherterms_ExistTerm, asmeta_furtherterms_EnumTerm, asmeta_furtherterms_ConditionalTerm, asmeta_furtherterms_ComprehensionTerm, asmeta_furtherterms_ComplexTerm, asmeta_basicterms_FunctionTerm, Function, asmeta_furtherterms_BagCt, asmeta_basicterms_VariableTerm, BasicTerm, furtherterms_FiniteQuantificationTerm, asmeta_basicterms_UndefTerm, asmeta_basicterms_TupleTerm, asmeta_basicterms_SetTerm, asmeta_basicterms_RuleAsTerm, RuleDeclaration, DynamicFunction, asmeta_basicterms_LocationTerm, FunctionTerm, asmeta_structure_DomainInitialization, asmeta_basicterms_ExtendedTerm, Term, domains_ConcreteDomain, asmeta_basicterms_DomainTerm, asmeta_basicterms_ConstantTerm, asmeta_basicterms_CollectionTerm, asmeta_basicterms_BooleanTerm, asmeta_basicterms_BasicTerm, asmeta_basicterms_Term, domains_Domain, basictransitionrules_TermAsRule, asmeta_structure_NamedElement, asmeta_structure_AgentInitialization, basictransitionrules_MacroCallRule, Initialization, asmeta_structure_Body, FunctionDefinition, Property_, DomainDefinition, Asm, asmeta_structure_FunctionInitialization, asmeta_structure_Initialization, NamedElement, DomainInitialization, FunctionInitialization, AgentInitialization, asmeta_structure_Signature, Header, domains_StructuredTd, asmeta_structure_ExportClause, asmeta_structure_ImportClause, asmeta_structure_FunctionDefinition, asmeta_structure_DomainDefinition, LocalFunction, asmeta_turbotransitionrules_TurboCallRule, turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_TurboReturnRule, asmeta_structure_Header, ImportClause, Signature, ExportClause, asmeta_structure_Asm, Body, basictransitionrules_MacroDeclaration, asmeta_turbotransitionrules_TurboRule, Rule, asmeta_turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_SeqRule, TurboRule, asmeta_turbotransitionrules_TurboLocalStateRule, basictransitionrules_Rule, asmeta_turbotransitionrules_IterateRule, turbotransitionrules_TurboCallRule, asmeta_turbotransitionrules_TryCatchRule, asmeta_derivedtransitionrules_BasicDerivedRule, DerivedRule, asmeta_derivedtransitionrules_TurboDerivedRule, asmeta_derivedtransitionrules_RecursiveWhileRule, TurboDerivedRule, asmeta_derivedtransitionrules_IterativeWhileRule, asmeta_derivedtransitionrules_DerivedRule, asmeta_derivedtransitionrules_CaseRule, BasicDerivedRule, asmeta_basictransitionrules_ForallRule, asmeta_basictransitionrules_TermAsRule, asmeta_basictransitionrules_BasicRule, asmeta_basictransitionrules_Rule, asmeta_basictransitionrules_ChooseRule, BasicRule, asmeta_basictransitionrules_MacroCallRule, asmeta_basictransitionrules_BlockRule, asmeta_basictransitionrules_ConditionalRule, asmeta_basictransitionrules_MacroDeclaration, asmeta_definitions_RuleDeclaration, Classifier, asmeta_basictransitionrules_LetRule, asmeta_basictransitionrules_ExtendRule, asmeta_basictransitionrules_UpdateRule, asmeta_basictransitionrules_SkipRule, Invariant, asmeta_definitions_LocalFunction, asmeta_definitions_ControlledFunction, asmeta_definitions_SharedFunction, asmeta_definitions_MonitoredFunction, asmeta_definitions_OutFunction, asmeta_definitions_DynamicFunction, BasicFunction, asmeta_definitions_StaticFunction, asmeta_definitions_DerivedFunction, asmeta_definitions_BasicFunction, asmeta_definitions_Invariant, asmeta_definitions_Function, domains_EnumElement, asmeta_domains_EnumElement, asmeta_domains_Domain, asmeta_definitions_Classifier, asmeta_definitions_Property, asmeta_domains_NaturalDomain, IntegerDomain, asmeta_domains_UndefDomain, BasicTd, asmeta_domains_TypeDomain, Domain, asmeta_domains_StructuredTd, TypeDomain, asmeta_domains_StringDomain, asmeta_domains_SequenceDomain, StructuredTd, asmeta_domains_RuleDomain, asmeta_domains_ReserveDomain, AbstractTd, asmeta_domains_RealDomain, ComplexDomain, asmeta_domains_ProductDomain, asmeta_domains_PowersetDomain, asmeta_domains_MapDomain, asmeta_domains_IntegerDomain, RealDomain, asmeta_domains_EnumTd, asmeta_domains_ConcreteDomain, domains_TypeDomain, asmeta_domains_ComplexDomain, asmeta_domains_CharDomain, asmeta_domains_BooleanDomain, asmeta_domains_BasicTd, asmeta_domains_BagDomain, asmeta_domains_AnyDomain, asmeta_domains_AgentDomain, asmeta_domains_AbstractTd, VariableKind},
    associations={pair0, comparingTerm26, comparedTerm28, otherwiseTerm31, term34, variable1, assignmentTerm2, body4, variable7, guard8, elseTerm10, guard12, thenTerm15, variable18, guard20, term23, arguments41, function43, finiteQuantificationTerm36, term38, body64, rule40, initializedFunction66, variable68, initializedDomain71, body73, domain45, termAsRule46, program47, domain48, initialState51, functionDefinition52, property53, domainDefinition55, ruleDeclaration57, asm59, initialState61, body111, definedDomain113, domainInitialization116, functionInitialization118, agentInitialization120, initialState75, domain78, function81, headerSection84, structuredDomain86, exportedFunction87, exportedDomain89, exportedRule92, importedDomain95, importedFunction97, importedRule100, body103, variable105, definedFunction108, init147, body148, localFunction151, calledRule153, location154, asm122, importClause125, signature126, exportClause128, asm130, initialState133, defaultInitialState135, bodySection138, headerSection140, mainrule143, resultType145, location158, catchRule160, tryRule163, rule166, updateRule156, otherwiseBranch183, rule168, guard170, guard173, rule175, term178, elseRule204, caseTerm180, thenRule207, term186, ifnone189, doRule191, guard194, variable197, calledMacro200, guard202, variable239, variable210, guard212, doRule215, inRule218, initExpression220, variable223, extendedDomain226, boundVar228, doRule231, updatingTerm234, location236, domain263, codomain265, definition268, constraint241, ruleBody243, asmBody246, initialization249, constrainedDomain252, body255, constrainedRule257, constrainedFunction260, element286, constraint271, signature274, domain277, baseDomain279, sourceDomain281, targetDomain283, constraint287, signature290, initialization293, definition296, typeDomain299, domain300},
    generalizations={gen_asmeta_furtherterms_SequenceTerm_CollectionTerm, gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm, gen_asmeta_furtherterms_RealTerm_ConstantTerm, gen_asmeta_furtherterms_MapTerm_CollectionTerm, gen_asmeta_furtherterms_MapCt_ComprehensionTerm, gen_asmeta_furtherterms_LetTerm_VariableBindingTerm, gen_asmeta_furtherterms_IntegerTerm_ConstantTerm, gen_asmeta_furtherterms_NaturalTerm_ConstantTerm, gen_asmeta_furtherterms_VariableBindingTerm_ExtendedTerm, gen_asmeta_furtherterms_StringTerm_ConstantTerm, gen_asmeta_furtherterms_SetCt_ComprehensionTerm, gen_asmeta_furtherterms_ComplexTerm_ConstantTerm, gen_asmeta_furtherterms_CharTerm_ConstantTerm, gen_asmeta_furtherterms_CaseTerm_ExtendedTerm, gen_asmeta_furtherterms_BagTerm_CollectionTerm, gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm, gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_EnumTerm_ConstantTerm, gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm, gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm, gen_asmeta_basicterms_FunctionTerm_BasicTerm, gen_asmeta_furtherterms_BagCt_ComprehensionTerm, gen_asmeta_basicterms_VariableTerm_BasicTerm, gen_asmeta_basicterms_UndefTerm_ConstantTerm, gen_asmeta_basicterms_TupleTerm_ExtendedTerm, gen_asmeta_basicterms_SetTerm_CollectionTerm, gen_asmeta_basicterms_RuleAsTerm_ExtendedTerm, gen_asmeta_basicterms_LocationTerm_FunctionTerm, gen_asmeta_basicterms_ExtendedTerm_Term, gen_asmeta_basicterms_DomainTerm_ExtendedTerm, gen_asmeta_basicterms_ConstantTerm_BasicTerm, gen_asmeta_basicterms_CollectionTerm_ExtendedTerm, gen_asmeta_basicterms_BooleanTerm_ConstantTerm, gen_asmeta_basicterms_BasicTerm_Term, gen_asmeta_structure_Initialization_NamedElement, gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule, gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule, gen_asmeta_structure_Asm_NamedElement, gen_asmeta_turbotransitionrules_TurboRule_Rule, gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration, gen_asmeta_turbotransitionrules_SeqRule_TurboRule, gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule, gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule, gen_asmeta_turbotransitionrules_IterateRule_TurboRule, gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule, gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule, gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule, gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule, gen_asmeta_derivedtransitionrules_DerivedRule_Rule, gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule, gen_asmeta_basictransitionrules_ForallRule_BasicRule, gen_asmeta_basictransitionrules_TermAsRule_Rule, gen_asmeta_basictransitionrules_BasicRule_Rule, gen_asmeta_basictransitionrules_ChooseRule_BasicRule, gen_asmeta_basictransitionrules_MacroCallRule_BasicRule, gen_asmeta_basictransitionrules_BlockRule_BasicRule, gen_asmeta_basictransitionrules_ConditionalRule_BasicRule, gen_asmeta_basictransitionrules_SkipRule_BasicRule, gen_asmeta_basictransitionrules_MacroDeclaration_RuleDeclaration, gen_asmeta_definitions_RuleDeclaration_Classifier, gen_asmeta_basictransitionrules_LetRule_BasicRule, gen_asmeta_basictransitionrules_ExtendRule_BasicRule, gen_asmeta_basictransitionrules_UpdateRule_BasicRule, gen_asmeta_definitions_LocalFunction_DynamicFunction, gen_asmeta_definitions_ControlledFunction_DynamicFunction, gen_asmeta_definitions_SharedFunction_DynamicFunction, gen_asmeta_definitions_MonitoredFunction_DynamicFunction, gen_asmeta_definitions_OutFunction_DynamicFunction, gen_asmeta_definitions_DynamicFunction_BasicFunction, gen_asmeta_definitions_StaticFunction_BasicFunction, gen_asmeta_definitions_DerivedFunction_Function, gen_asmeta_definitions_BasicFunction_Function, gen_asmeta_definitions_Invariant_Property, gen_asmeta_definitions_Function_Classifier, gen_asmeta_domains_Domain_Classifier, gen_asmeta_definitions_Classifier_NamedElement, gen_asmeta_definitions_Property_Classifier, gen_asmeta_domains_NaturalDomain_IntegerDomain, gen_asmeta_domains_UndefDomain_BasicTd, gen_asmeta_domains_TypeDomain_Domain, gen_asmeta_domains_StructuredTd_TypeDomain, gen_asmeta_domains_StringDomain_BasicTd, gen_asmeta_domains_SequenceDomain_StructuredTd, gen_asmeta_domains_RuleDomain_StructuredTd, gen_asmeta_domains_ReserveDomain_AbstractTd, gen_asmeta_domains_RealDomain_ComplexDomain, gen_asmeta_domains_ProductDomain_StructuredTd, gen_asmeta_domains_PowersetDomain_StructuredTd, gen_asmeta_domains_MapDomain_StructuredTd, gen_asmeta_domains_IntegerDomain_RealDomain, gen_asmeta_domains_EnumTd_TypeDomain, gen_asmeta_domains_ConcreteDomain_Domain, gen_asmeta_domains_ComplexDomain_BasicTd, gen_asmeta_domains_CharDomain_BasicTd, gen_asmeta_domains_BooleanDomain_BasicTd, gen_asmeta_domains_BasicTd_TypeDomain, gen_asmeta_domains_BagDomain_StructuredTd, gen_asmeta_domains_AnyDomain_TypeDomain, gen_asmeta_domains_AgentDomain_AbstractTd, gen_asmeta_domains_AbstractTd_TypeDomain},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
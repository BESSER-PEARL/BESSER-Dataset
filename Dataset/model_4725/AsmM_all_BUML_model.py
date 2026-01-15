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
asmeta_furtherterms_IntegerTerm = Class(name="asmeta::furtherterms::IntegerTerm")
ConstantTerm = Class(name="ConstantTerm")
asmeta_furtherterms_NaturalTerm = Class(name="asmeta::furtherterms::NaturalTerm")
asmeta_furtherterms_VariableBindingTerm = Class(name="asmeta::furtherterms::VariableBindingTerm", is_abstract=True)
ExtendedTerm = Class(name="ExtendedTerm")
asmeta_furtherterms_StringTerm = Class(name="asmeta::furtherterms::StringTerm")
asmeta_furtherterms_SetCt = Class(name="asmeta::furtherterms::SetCt")
ComprehensionTerm = Class(name="ComprehensionTerm")
asmeta_furtherterms_SequenceTerm = Class(name="asmeta::furtherterms::SequenceTerm")
CollectionTerm = Class(name="CollectionTerm")
asmeta_furtherterms_SequenceCt = Class(name="asmeta::furtherterms::SequenceCt")
asmeta_furtherterms_RealTerm = Class(name="asmeta::furtherterms::RealTerm")
asmeta_furtherterms_MapTerm = Class(name="asmeta::furtherterms::MapTerm")
basicterms_TupleTerm = Class(name="basicterms::TupleTerm")
asmeta_furtherterms_MapCt = Class(name="asmeta::furtherterms::MapCt")
asmeta_furtherterms_LetTerm = Class(name="asmeta::furtherterms::LetTerm")
VariableBindingTerm = Class(name="VariableBindingTerm")
basicterms_VariableTerm = Class(name="basicterms::VariableTerm")
basicterms_Term = Class(name="basicterms::Term")
asmeta_furtherterms_ForallTerm = Class(name="asmeta::furtherterms::ForallTerm")
FiniteQuantificationTerm = Class(name="FiniteQuantificationTerm")
asmeta_furtherterms_ComprehensionTerm = Class(name="asmeta::furtherterms::ComprehensionTerm", is_abstract=True)
asmeta_furtherterms_ComplexTerm = Class(name="asmeta::furtherterms::ComplexTerm")
asmeta_furtherterms_CharTerm = Class(name="asmeta::furtherterms::CharTerm")
asmeta_furtherterms_CaseTerm = Class(name="asmeta::furtherterms::CaseTerm")
asmeta_furtherterms_FiniteQuantificationTerm = Class(name="asmeta::furtherterms::FiniteQuantificationTerm", is_abstract=True)
asmeta_furtherterms_ExistUniqueTerm = Class(name="asmeta::furtherterms::ExistUniqueTerm")
asmeta_furtherterms_ExistTerm = Class(name="asmeta::furtherterms::ExistTerm")
asmeta_furtherterms_EnumTerm = Class(name="asmeta::furtherterms::EnumTerm")
asmeta_furtherterms_ConditionalTerm = Class(name="asmeta::furtherterms::ConditionalTerm")
asmeta_basicterms_SetTerm = Class(name="asmeta::basicterms::SetTerm")
asmeta_basicterms_RuleAsTerm = Class(name="asmeta::basicterms::RuleAsTerm")
RuleDeclaration = Class(name="RuleDeclaration")
asmeta_basicterms_LocationTerm = Class(name="asmeta::basicterms::LocationTerm")
FunctionTerm = Class(name="FunctionTerm")
asmeta_basicterms_FunctionTerm = Class(name="asmeta::basicterms::FunctionTerm")
Function = Class(name="Function")
asmeta_basicterms_ExtendedTerm = Class(name="asmeta::basicterms::ExtendedTerm", is_abstract=True)
Term = Class(name="Term")
asmeta_basicterms_DomainTerm = Class(name="asmeta::basicterms::DomainTerm")
asmeta_basicterms_ConstantTerm = Class(name="asmeta::basicterms::ConstantTerm", is_abstract=True)
asmeta_basicterms_CollectionTerm = Class(name="asmeta::basicterms::CollectionTerm", is_abstract=True)
asmeta_basicterms_BooleanTerm = Class(name="asmeta::basicterms::BooleanTerm")
asmeta_basicterms_BasicTerm = Class(name="asmeta::basicterms::BasicTerm", is_abstract=True)
asmeta_basicterms_Term = Class(name="asmeta::basicterms::Term", is_abstract=True)
domains_Domain = Class(name="domains::Domain")
basictransitionrules_TermAsRule = Class(name="basictransitionrules::TermAsRule")
asmeta_furtherterms_BagTerm = Class(name="asmeta::furtherterms::BagTerm")
asmeta_furtherterms_BagCt = Class(name="asmeta::furtherterms::BagCt")
asmeta_basicterms_VariableTerm = Class(name="asmeta::basicterms::VariableTerm")
BasicTerm = Class(name="BasicTerm")
furtherterms_FiniteQuantificationTerm = Class(name="furtherterms::FiniteQuantificationTerm")
asmeta_basicterms_UndefTerm = Class(name="asmeta::basicterms::UndefTerm")
asmeta_basicterms_TupleTerm = Class(name="asmeta::basicterms::TupleTerm")
DomainDefinition = Class(name="DomainDefinition")
Asm = Class(name="Asm")
FairnessConstraint = Class(name="FairnessConstraint")
InvarConstraint = Class(name="InvarConstraint")
asmeta_structure_FunctionInitialization = Class(name="asmeta::structure::FunctionInitialization")
DynamicFunction = Class(name="DynamicFunction")
asmeta_structure_DomainInitialization = Class(name="asmeta::structure::DomainInitialization")
domains_ConcreteDomain = Class(name="domains::ConcreteDomain")
asmeta_structure_Signature = Class(name="asmeta::structure::Signature")
asmeta_structure_NamedElement = Class(name="asmeta::structure::NamedElement", is_abstract=True)
asmeta_structure_AgentInitialization = Class(name="asmeta::structure::AgentInitialization")
basictransitionrules_MacroCallRule = Class(name="basictransitionrules::MacroCallRule")
Initialization = Class(name="Initialization")
asmeta_structure_Body = Class(name="asmeta::structure::Body")
FunctionDefinition = Class(name="FunctionDefinition")
Property_ = Class(name="Property")
asmeta_structure_FunctionDefinition = Class(name="asmeta::structure::FunctionDefinition")
asmeta_structure_DomainDefinition = Class(name="asmeta::structure::DomainDefinition")
asmeta_structure_Initialization = Class(name="asmeta::structure::Initialization")
NamedElement = Class(name="NamedElement")
DomainInitialization = Class(name="DomainInitialization")
FunctionInitialization = Class(name="FunctionInitialization")
AgentInitialization = Class(name="AgentInitialization")
asmeta_structure_Header = Class(name="asmeta::structure::Header")
ImportClause = Class(name="ImportClause")
Header = Class(name="Header")
domains_StructuredTd = Class(name="domains::StructuredTd")
asmeta_structure_ExportClause = Class(name="asmeta::structure::ExportClause")
asmeta_structure_ImportClause = Class(name="asmeta::structure::ImportClause")
basictransitionrules_MacroDeclaration = Class(name="basictransitionrules::MacroDeclaration")
asmeta_turbotransitionrules_TurboRule = Class(name="asmeta::turbotransitionrules::TurboRule", is_abstract=True)
Rule = Class(name="Rule")
asmeta_turbotransitionrules_TurboDeclaration = Class(name="asmeta::turbotransitionrules::TurboDeclaration")
asmeta_turbotransitionrules_SeqRule = Class(name="asmeta::turbotransitionrules::SeqRule")
TurboRule = Class(name="TurboRule")
asmeta_turbotransitionrules_TurboLocalStateRule = Class(name="asmeta::turbotransitionrules::TurboLocalStateRule")
basictransitionrules_Rule = Class(name="basictransitionrules::Rule")
LocalFunction = Class(name="LocalFunction")
asmeta_turbotransitionrules_TurboCallRule = Class(name="asmeta::turbotransitionrules::TurboCallRule")
turbotransitionrules_TurboDeclaration = Class(name="turbotransitionrules::TurboDeclaration")
asmeta_turbotransitionrules_TurboReturnRule = Class(name="asmeta::turbotransitionrules::TurboReturnRule")
turbotransitionrules_TurboCallRule = Class(name="turbotransitionrules::TurboCallRule")
Signature = Class(name="Signature")
ExportClause = Class(name="ExportClause")
asmeta_structure_Asm = Class(name="asmeta::structure::Asm")
Body = Class(name="Body")
asmeta_derivedtransitionrules_IterativeWhileRule = Class(name="asmeta::derivedtransitionrules::IterativeWhileRule")
asmeta_derivedtransitionrules_DerivedRule = Class(name="asmeta::derivedtransitionrules::DerivedRule", is_abstract=True)
asmeta_derivedtransitionrules_CaseRule = Class(name="asmeta::derivedtransitionrules::CaseRule")
BasicDerivedRule = Class(name="BasicDerivedRule")
asmeta_derivedtransitionrules_BasicDerivedRule = Class(name="asmeta::derivedtransitionrules::BasicDerivedRule", is_abstract=True)
DerivedRule = Class(name="DerivedRule")
asmeta_derivedtransitionrules_TurboDerivedRule = Class(name="asmeta::derivedtransitionrules::TurboDerivedRule", is_abstract=True)
asmeta_basictransitionrules_TermAsRule = Class(name="asmeta::basictransitionrules::TermAsRule")
asmeta_basictransitionrules_BasicRule = Class(name="asmeta::basictransitionrules::BasicRule", is_abstract=True)
asmeta_basictransitionrules_Rule = Class(name="asmeta::basictransitionrules::Rule", is_abstract=True)
asmeta_turbotransitionrules_TryCatchRule = Class(name="asmeta::turbotransitionrules::TryCatchRule")
asmeta_turbotransitionrules_IterateRule = Class(name="asmeta::turbotransitionrules::IterateRule")
asmeta_derivedtransitionrules_RecursiveWhileRule = Class(name="asmeta::derivedtransitionrules::RecursiveWhileRule")
TurboDerivedRule = Class(name="TurboDerivedRule")
asmeta_basictransitionrules_BlockRule = Class(name="asmeta::basictransitionrules::BlockRule")
asmeta_basictransitionrules_ConditionalRule = Class(name="asmeta::basictransitionrules::ConditionalRule")
asmeta_basictransitionrules_ForallRule = Class(name="asmeta::basictransitionrules::ForallRule")
asmeta_basictransitionrules_LetRule = Class(name="asmeta::basictransitionrules::LetRule")
asmeta_basictransitionrules_ExtendRule = Class(name="asmeta::basictransitionrules::ExtendRule")
asmeta_basictransitionrules_ChooseRule = Class(name="asmeta::basictransitionrules::ChooseRule")
BasicRule = Class(name="BasicRule")
asmeta_basictransitionrules_MacroCallRule = Class(name="asmeta::basictransitionrules::MacroCallRule")
asmeta_basictransitionrules_MacroDeclaration = Class(name="asmeta::basictransitionrules::MacroDeclaration")
asmeta_definitions_RuleDeclaration = Class(name="asmeta::definitions::RuleDeclaration", is_abstract=True)
Classifier = Class(name="Classifier")
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
asmeta_basictransitionrules_UpdateRule = Class(name="asmeta::basictransitionrules::UpdateRule")
asmeta_basictransitionrules_SkipRule = Class(name="asmeta::basictransitionrules::SkipRule")
asmeta_definitions_Classifier = Class(name="asmeta::definitions::Classifier", is_abstract=True)
asmeta_definitions_Property = Class(name="asmeta::definitions::Property")
asmeta_definitions_TemporalProperty = Class(name="asmeta::definitions::TemporalProperty", is_abstract=True)
asmeta_definitions_CtlSpec = Class(name="asmeta::definitions::CtlSpec")
TemporalProperty = Class(name="TemporalProperty")
asmeta_definitions_LtlSpec = Class(name="asmeta::definitions::LtlSpec")
asmeta_definitions_InvarConstraint = Class(name="asmeta::definitions::InvarConstraint")
asmeta_definitions_FairnessConstraint = Class(name="asmeta::definitions::FairnessConstraint", is_abstract=True)
asmeta_definitions_JusticeConstraint = Class(name="asmeta::definitions::JusticeConstraint")
asmeta_definitions_CompassionConstraint = Class(name="asmeta::definitions::CompassionConstraint")
asmeta_definitions_Function = Class(name="asmeta::definitions::Function", is_abstract=True)
asmeta_domains_ProductDomain = Class(name="asmeta::domains::ProductDomain")
asmeta_domains_PowersetDomain = Class(name="asmeta::domains::PowersetDomain")
asmeta_domains_MapDomain = Class(name="asmeta::domains::MapDomain")
asmeta_domains_IntegerDomain = Class(name="asmeta::domains::IntegerDomain")
RealDomain = Class(name="RealDomain")
asmeta_domains_EnumTd = Class(name="asmeta::domains::EnumTd")
domains_EnumElement = Class(name="domains::EnumElement")
asmeta_domains_EnumElement = Class(name="asmeta::domains::EnumElement")
asmeta_domains_Domain = Class(name="asmeta::domains::Domain", is_abstract=True)
asmeta_domains_ConcreteDomain = Class(name="asmeta::domains::ConcreteDomain")
domains_TypeDomain = Class(name="domains::TypeDomain")
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
asmeta_domains_ComplexDomain = Class(name="asmeta::domains::ComplexDomain")
asmeta_domains_CharDomain = Class(name="asmeta::domains::CharDomain")
asmeta_domains_BooleanDomain = Class(name="asmeta::domains::BooleanDomain")
asmeta_domains_BasicTd = Class(name="asmeta::domains::BasicTd", is_abstract=True)
asmeta_domains_BagDomain = Class(name="asmeta::domains::BagDomain")
asmeta_domains_AnyDomain = Class(name="asmeta::domains::AnyDomain")
asmeta_domains_AgentDomain = Class(name="asmeta::domains::AgentDomain")
asmeta_domains_AbstractTd = Class(name="asmeta::domains::AbstractTd")

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

# asmeta_furtherterms_SequenceCt class attributes and methods

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

# asmeta_furtherterms_ComprehensionTerm class attributes and methods
asmeta_furtherterms_ComprehensionTerm_ranges: Property = Property(name="ranges", type=StringType)
asmeta_furtherterms_ComprehensionTerm.attributes={asmeta_furtherterms_ComprehensionTerm_ranges}

# asmeta_furtherterms_ComplexTerm class attributes and methods

# asmeta_furtherterms_CharTerm class attributes and methods

# asmeta_furtherterms_CaseTerm class attributes and methods
asmeta_furtherterms_CaseTerm_resultTerms: Property = Property(name="resultTerms", type=StringType)
asmeta_furtherterms_CaseTerm.attributes={asmeta_furtherterms_CaseTerm_resultTerms}

# asmeta_furtherterms_FiniteQuantificationTerm class attributes and methods
asmeta_furtherterms_FiniteQuantificationTerm_ranges: Property = Property(name="ranges", type=StringType)
asmeta_furtherterms_FiniteQuantificationTerm.attributes={asmeta_furtherterms_FiniteQuantificationTerm_ranges}

# asmeta_furtherterms_ExistUniqueTerm class attributes and methods

# asmeta_furtherterms_ExistTerm class attributes and methods

# asmeta_furtherterms_EnumTerm class attributes and methods

# asmeta_furtherterms_ConditionalTerm class attributes and methods

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

# asmeta_furtherterms_BagTerm class attributes and methods

# asmeta_furtherterms_BagCt class attributes and methods

# asmeta_basicterms_VariableTerm class attributes and methods
asmeta_basicterms_VariableTerm_name: Property = Property(name="name", type=StringType)
asmeta_basicterms_VariableTerm_kind: Property = Property(name="kind", type=StringType)
asmeta_basicterms_VariableTerm.attributes={asmeta_basicterms_VariableTerm_name, asmeta_basicterms_VariableTerm_kind}

# BasicTerm class attributes and methods

# furtherterms_FiniteQuantificationTerm class attributes and methods

# asmeta_basicterms_UndefTerm class attributes and methods

# asmeta_basicterms_TupleTerm class attributes and methods
asmeta_basicterms_TupleTerm_terms: Property = Property(name="terms", type=StringType)
asmeta_basicterms_TupleTerm_arity: Property = Property(name="arity", type=StringType)
asmeta_basicterms_TupleTerm.attributes={asmeta_basicterms_TupleTerm_arity, asmeta_basicterms_TupleTerm_terms}

# DomainDefinition class attributes and methods

# Asm class attributes and methods

# FairnessConstraint class attributes and methods

# InvarConstraint class attributes and methods

# asmeta_structure_FunctionInitialization class attributes and methods

# DynamicFunction class attributes and methods

# asmeta_structure_DomainInitialization class attributes and methods

# domains_ConcreteDomain class attributes and methods

# asmeta_structure_Signature class attributes and methods

# asmeta_structure_NamedElement class attributes and methods
asmeta_structure_NamedElement_name: Property = Property(name="name", type=StringType)
asmeta_structure_NamedElement.attributes={asmeta_structure_NamedElement_name}

# asmeta_structure_AgentInitialization class attributes and methods

# basictransitionrules_MacroCallRule class attributes and methods

# Initialization class attributes and methods

# asmeta_structure_Body class attributes and methods

# FunctionDefinition class attributes and methods

# Property class attributes and methods

# asmeta_structure_FunctionDefinition class attributes and methods

# asmeta_structure_DomainDefinition class attributes and methods

# asmeta_structure_Initialization class attributes and methods

# NamedElement class attributes and methods

# DomainInitialization class attributes and methods

# FunctionInitialization class attributes and methods

# AgentInitialization class attributes and methods

# asmeta_structure_Header class attributes and methods

# ImportClause class attributes and methods

# Header class attributes and methods

# domains_StructuredTd class attributes and methods

# asmeta_structure_ExportClause class attributes and methods

# asmeta_structure_ImportClause class attributes and methods
asmeta_structure_ImportClause_moduleName: Property = Property(name="moduleName", type=StringType)
asmeta_structure_ImportClause.attributes={asmeta_structure_ImportClause_moduleName}

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

# Signature class attributes and methods

# ExportClause class attributes and methods

# asmeta_structure_Asm class attributes and methods
asmeta_structure_Asm_isAsynchr: Property = Property(name="isAsynchr", type=StringType)
asmeta_structure_Asm.attributes={asmeta_structure_Asm_isAsynchr}

# Body class attributes and methods

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

# asmeta_turbotransitionrules_TryCatchRule class attributes and methods

# asmeta_turbotransitionrules_IterateRule class attributes and methods

# asmeta_derivedtransitionrules_RecursiveWhileRule class attributes and methods

# TurboDerivedRule class attributes and methods

# asmeta_basictransitionrules_BlockRule class attributes and methods
asmeta_basictransitionrules_BlockRule_rules: Property = Property(name="rules", type=StringType)
asmeta_basictransitionrules_BlockRule.attributes={asmeta_basictransitionrules_BlockRule_rules}

# asmeta_basictransitionrules_ConditionalRule class attributes and methods

# asmeta_basictransitionrules_ForallRule class attributes and methods
asmeta_basictransitionrules_ForallRule_ranges: Property = Property(name="ranges", type=StringType)
asmeta_basictransitionrules_ForallRule.attributes={asmeta_basictransitionrules_ForallRule_ranges}

# asmeta_basictransitionrules_LetRule class attributes and methods

# asmeta_basictransitionrules_ExtendRule class attributes and methods

# asmeta_basictransitionrules_ChooseRule class attributes and methods
asmeta_basictransitionrules_ChooseRule_ranges: Property = Property(name="ranges", type=StringType)
asmeta_basictransitionrules_ChooseRule.attributes={asmeta_basictransitionrules_ChooseRule_ranges}

# BasicRule class attributes and methods

# asmeta_basictransitionrules_MacroCallRule class attributes and methods
asmeta_basictransitionrules_MacroCallRule_parameters: Property = Property(name="parameters", type=StringType)
asmeta_basictransitionrules_MacroCallRule.attributes={asmeta_basictransitionrules_MacroCallRule_parameters}

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

# asmeta_basictransitionrules_UpdateRule class attributes and methods

# asmeta_basictransitionrules_SkipRule class attributes and methods

# asmeta_definitions_Classifier class attributes and methods

# asmeta_definitions_Property class attributes and methods

# asmeta_definitions_TemporalProperty class attributes and methods

# asmeta_definitions_CtlSpec class attributes and methods

# TemporalProperty class attributes and methods

# asmeta_definitions_LtlSpec class attributes and methods

# asmeta_definitions_InvarConstraint class attributes and methods

# asmeta_definitions_FairnessConstraint class attributes and methods

# asmeta_definitions_JusticeConstraint class attributes and methods

# asmeta_definitions_CompassionConstraint class attributes and methods

# asmeta_definitions_Function class attributes and methods
asmeta_definitions_Function_arity: Property = Property(name="arity", type=StringType)
asmeta_definitions_Function.attributes={asmeta_definitions_Function_arity}

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
term38: BinaryAssociation = BinaryAssociation(
    name="term38",
    ends={
        Property(name="basicterms_Term39", type=asmeta_basicterms_SetTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_SetTerm", type=basicterms_Term, multiplicity=Multiplicity(0, 9999))
    }
)
rule40: BinaryAssociation = BinaryAssociation(
    name="rule40",
    ends={
        Property(name="RuleDeclaration", type=asmeta_basicterms_RuleAsTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basicterms_RuleAsTerm", type=RuleDeclaration, multiplicity=Multiplicity(1, 1))
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
        Property(name="terms37", type=asmeta_basicterms_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="furtherterms", type=furtherterms_FiniteQuantificationTerm, multiplicity=Multiplicity(0, 1))
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
fairnessConstraint61: BinaryAssociation = BinaryAssociation(
    name="fairnessConstraint61",
    ends={
        Property(name="FairnessConstraint", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body62", type=FairnessConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariantConstraint63: BinaryAssociation = BinaryAssociation(
    name="invariantConstraint63",
    ends={
        Property(name="InvarConstraint", type=asmeta_structure_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Body64", type=InvarConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState65: BinaryAssociation = BinaryAssociation(
    name="initialState65",
    ends={
        Property(name="structure67", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization66", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
body68: BinaryAssociation = BinaryAssociation(
    name="body68",
    ends={
        Property(name="basicterms_Term69", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
initializedFunction70: BinaryAssociation = BinaryAssociation(
    name="initializedFunction70",
    ends={
        Property(name="definitions71", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="DynamicFunction", type=DynamicFunction, multiplicity=Multiplicity(1, 1))
    }
)
variable72: BinaryAssociation = BinaryAssociation(
    name="variable72",
    ends={
        Property(name="basicterms_VariableTerm74", type=asmeta_structure_FunctionInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionInitialization73", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedDomain75: BinaryAssociation = BinaryAssociation(
    name="initializedDomain75",
    ends={
        Property(name="definitions76", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
body77: BinaryAssociation = BinaryAssociation(
    name="body77",
    ends={
        Property(name="basicterms_Term78", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainInitialization", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialState79: BinaryAssociation = BinaryAssociation(
    name="initialState79",
    ends={
        Property(name="structure81", type=asmeta_structure_DomainInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization80", type=Initialization, multiplicity=Multiplicity(1, 1))
    }
)
domain82: BinaryAssociation = BinaryAssociation(
    name="domain82",
    ends={
        Property(name="definitions84", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="domains83", type=domains_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
importedFunction101: BinaryAssociation = BinaryAssociation(
    name="importedFunction101",
    ends={
        Property(name="Function103", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause102", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
importedRule104: BinaryAssociation = BinaryAssociation(
    name="importedRule104",
    ends={
        Property(name="RuleDeclaration106", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause105", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
body107: BinaryAssociation = BinaryAssociation(
    name="body107",
    ends={
        Property(name="basicterms_Term108", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable109: BinaryAssociation = BinaryAssociation(
    name="variable109",
    ends={
        Property(name="basicterms_VariableTerm111", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_FunctionDefinition110", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999))
    }
)
definedFunction112: BinaryAssociation = BinaryAssociation(
    name="definedFunction112",
    ends={
        Property(name="definitions114", type=asmeta_structure_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="Function113", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
body115: BinaryAssociation = BinaryAssociation(
    name="body115",
    ends={
        Property(name="basicterms_Term116", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_DomainDefinition", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definedDomain117: BinaryAssociation = BinaryAssociation(
    name="definedDomain117",
    ends={
        Property(name="definitions119", type=asmeta_structure_DomainDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="domains118", type=domains_ConcreteDomain, multiplicity=Multiplicity(1, 1))
    }
)
domainInitialization120: BinaryAssociation = BinaryAssociation(
    name="domainInitialization120",
    ends={
        Property(name="structure121", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainInitialization", type=DomainInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionInitialization122: BinaryAssociation = BinaryAssociation(
    name="functionInitialization122",
    ends={
        Property(name="structure123", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionInitialization", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agentInitialization124: BinaryAssociation = BinaryAssociation(
    name="agentInitialization124",
    ends={
        Property(name="structure125", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="AgentInitialization", type=AgentInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
asm126: BinaryAssociation = BinaryAssociation(
    name="asm126",
    ends={
        Property(name="structure128", type=asmeta_structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Asm127", type=Asm, multiplicity=Multiplicity(1, 1))
    }
)
importClause129: BinaryAssociation = BinaryAssociation(
    name="importClause129",
    ends={
        Property(name="ImportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header", type=ImportClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function85: BinaryAssociation = BinaryAssociation(
    name="function85",
    ends={
        Property(name="definitions87", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Function86", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headerSection88: BinaryAssociation = BinaryAssociation(
    name="headerSection88",
    ends={
        Property(name="structure89", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
structuredDomain90: BinaryAssociation = BinaryAssociation(
    name="structuredDomain90",
    ends={
        Property(name="domains_StructuredTd", type=asmeta_structure_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Signature", type=domains_StructuredTd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportedFunction91: BinaryAssociation = BinaryAssociation(
    name="exportedFunction91",
    ends={
        Property(name="Function92", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
exportedDomain93: BinaryAssociation = BinaryAssociation(
    name="exportedDomain93",
    ends={
        Property(name="domains_Domain95", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause94", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
exportedRule96: BinaryAssociation = BinaryAssociation(
    name="exportedRule96",
    ends={
        Property(name="RuleDeclaration98", type=asmeta_structure_ExportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ExportClause97", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
importedDomain99: BinaryAssociation = BinaryAssociation(
    name="importedDomain99",
    ends={
        Property(name="domains_Domain100", type=asmeta_structure_ImportClause, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_ImportClause", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
headerSection144: BinaryAssociation = BinaryAssociation(
    name="headerSection144",
    ends={
        Property(name="structure146", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Header145", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainrule147: BinaryAssociation = BinaryAssociation(
    name="mainrule147",
    ends={
        Property(name="basictransitionrules_MacroDeclaration", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm148", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
resultType149: BinaryAssociation = BinaryAssociation(
    name="resultType149",
    ends={
        Property(name="domains_Domain150", type=asmeta_turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboDeclaration", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
init151: BinaryAssociation = BinaryAssociation(
    name="init151",
    ends={
        Property(name="basictransitionrules_Rule", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body152: BinaryAssociation = BinaryAssociation(
    name="body152",
    ends={
        Property(name="basictransitionrules_Rule154", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule153", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localFunction155: BinaryAssociation = BinaryAssociation(
    name="localFunction155",
    ends={
        Property(name="LocalFunction", type=asmeta_turbotransitionrules_TurboLocalStateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboLocalStateRule156", type=LocalFunction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
calledRule157: BinaryAssociation = BinaryAssociation(
    name="calledRule157",
    ends={
        Property(name="turbotransitionrules_TurboDeclaration", type=asmeta_turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboCallRule", type=turbotransitionrules_TurboDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
location158: BinaryAssociation = BinaryAssociation(
    name="location158",
    ends={
        Property(name="basicterms_Term159", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
signature130: BinaryAssociation = BinaryAssociation(
    name="signature130",
    ends={
        Property(name="structure131", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature", type=Signature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exportClause132: BinaryAssociation = BinaryAssociation(
    name="exportClause132",
    ends={
        Property(name="ExportClause", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Header133", type=ExportClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asm134: BinaryAssociation = BinaryAssociation(
    name="asm134",
    ends={
        Property(name="structure136", type=asmeta_structure_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Asm135", type=Asm, multiplicity=Multiplicity(0, 1))
    }
)
initialState137: BinaryAssociation = BinaryAssociation(
    name="initialState137",
    ends={
        Property(name="Initialization138", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_structure_Asm", type=Initialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultInitialState139: BinaryAssociation = BinaryAssociation(
    name="defaultInitialState139",
    ends={
        Property(name="structure141", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Initialization140", type=Initialization, multiplicity=Multiplicity(0, 1))
    }
)
bodySection142: BinaryAssociation = BinaryAssociation(
    name="bodySection142",
    ends={
        Property(name="structure143", type=asmeta_structure_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="Body", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule172: BinaryAssociation = BinaryAssociation(
    name="rule172",
    ends={
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="basictransitionrules_Rule173", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1))
    }
)
guard174: BinaryAssociation = BinaryAssociation(
    name="guard174",
    ends={
        Property(name="basicterms_Term176", type=asmeta_derivedtransitionrules_RecursiveWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_RecursiveWhileRule175", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
guard177: BinaryAssociation = BinaryAssociation(
    name="guard177",
    ends={
        Property(name="basicterms_Term178", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
rule179: BinaryAssociation = BinaryAssociation(
    name="rule179",
    ends={
        Property(name="basictransitionrules_Rule181", type=asmeta_derivedtransitionrules_IterativeWhileRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_IterativeWhileRule180", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term182: BinaryAssociation = BinaryAssociation(
    name="term182",
    ends={
        Property(name="basicterms_Term183", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
caseTerm184: BinaryAssociation = BinaryAssociation(
    name="caseTerm184",
    ends={
        Property(name="basicterms_Term186", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule185", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
otherwiseBranch187: BinaryAssociation = BinaryAssociation(
    name="otherwiseBranch187",
    ends={
        Property(name="basictransitionrules_Rule189", type=asmeta_derivedtransitionrules_CaseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_derivedtransitionrules_CaseRule188", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term190: BinaryAssociation = BinaryAssociation(
    name="term190",
    ends={
        Property(name="terms192", type=asmeta_basictransitionrules_TermAsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="basicterms191", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
updateRule160: BinaryAssociation = BinaryAssociation(
    name="updateRule160",
    ends={
        Property(name="turbotransitionrules_TurboCallRule", type=asmeta_turbotransitionrules_TurboReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TurboReturnRule161", type=turbotransitionrules_TurboCallRule, multiplicity=Multiplicity(1, 1))
    }
)
location162: BinaryAssociation = BinaryAssociation(
    name="location162",
    ends={
        Property(name="basicterms_Term163", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
catchRule164: BinaryAssociation = BinaryAssociation(
    name="catchRule164",
    ends={
        Property(name="basictransitionrules_Rule166", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule165", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryRule167: BinaryAssociation = BinaryAssociation(
    name="tryRule167",
    ends={
        Property(name="basictransitionrules_Rule169", type=asmeta_turbotransitionrules_TryCatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_TryCatchRule168", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule170: BinaryAssociation = BinaryAssociation(
    name="rule170",
    ends={
        Property(name="basictransitionrules_Rule171", type=asmeta_turbotransitionrules_IterateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_turbotransitionrules_IterateRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard206: BinaryAssociation = BinaryAssociation(
    name="guard206",
    ends={
        Property(name="basicterms_Term207", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
elseRule208: BinaryAssociation = BinaryAssociation(
    name="elseRule208",
    ends={
        Property(name="basictransitionrules_Rule210", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule209", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenRule211: BinaryAssociation = BinaryAssociation(
    name="thenRule211",
    ends={
        Property(name="basictransitionrules_Rule213", type=asmeta_basictransitionrules_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ConditionalRule212", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable214: BinaryAssociation = BinaryAssociation(
    name="variable214",
    ends={
        Property(name="basicterms_VariableTerm215", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
guard216: BinaryAssociation = BinaryAssociation(
    name="guard216",
    ends={
        Property(name="basicterms_Term218", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule217", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
doRule219: BinaryAssociation = BinaryAssociation(
    name="doRule219",
    ends={
        Property(name="basictransitionrules_Rule221", type=asmeta_basictransitionrules_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ForallRule220", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inRule222: BinaryAssociation = BinaryAssociation(
    name="inRule222",
    ends={
        Property(name="basictransitionrules_Rule223", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression224: BinaryAssociation = BinaryAssociation(
    name="initExpression224",
    ends={
        Property(name="basicterms_Term226", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule225", type=basicterms_Term, multiplicity=Multiplicity(1, 9999))
    }
)
variable227: BinaryAssociation = BinaryAssociation(
    name="variable227",
    ends={
        Property(name="basicterms_VariableTerm229", type=asmeta_basictransitionrules_LetRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_LetRule228", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
ifnone193: BinaryAssociation = BinaryAssociation(
    name="ifnone193",
    ends={
        Property(name="basictransitionrules_Rule194", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule", type=basictransitionrules_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doRule195: BinaryAssociation = BinaryAssociation(
    name="doRule195",
    ends={
        Property(name="basictransitionrules_Rule197", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule196", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard198: BinaryAssociation = BinaryAssociation(
    name="guard198",
    ends={
        Property(name="basicterms_Term200", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule199", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
variable201: BinaryAssociation = BinaryAssociation(
    name="variable201",
    ends={
        Property(name="basicterms_VariableTerm203", type=asmeta_basictransitionrules_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ChooseRule202", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999))
    }
)
calledMacro204: BinaryAssociation = BinaryAssociation(
    name="calledMacro204",
    ends={
        Property(name="basictransitionrules_MacroDeclaration205", type=asmeta_basictransitionrules_MacroCallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_MacroCallRule", type=basictransitionrules_MacroDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
variable243: BinaryAssociation = BinaryAssociation(
    name="variable243",
    ends={
        Property(name="basicterms_VariableTerm244", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_RuleDeclaration", type=basicterms_VariableTerm, multiplicity=Multiplicity(0, 9999))
    }
)
constraint245: BinaryAssociation = BinaryAssociation(
    name="constraint245",
    ends={
        Property(name="definitions246", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
ruleBody247: BinaryAssociation = BinaryAssociation(
    name="ruleBody247",
    ends={
        Property(name="basictransitionrules_Rule249", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_RuleDeclaration248", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1))
    }
)
asmBody250: BinaryAssociation = BinaryAssociation(
    name="asmBody250",
    ends={
        Property(name="structure252", type=asmeta_definitions_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Body251", type=Body, multiplicity=Multiplicity(1, 1))
    }
)
initialization253: BinaryAssociation = BinaryAssociation(
    name="initialization253",
    ends={
        Property(name="structure255", type=asmeta_definitions_DynamicFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionInitialization254", type=FunctionInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedDomain256: BinaryAssociation = BinaryAssociation(
    name="constrainedDomain256",
    ends={
        Property(name="definitions258", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="domains257", type=domains_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
extendedDomain230: BinaryAssociation = BinaryAssociation(
    name="extendedDomain230",
    ends={
        Property(name="domains_Domain231", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
boundVar232: BinaryAssociation = BinaryAssociation(
    name="boundVar232",
    ends={
        Property(name="basicterms_VariableTerm234", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule233", type=basicterms_VariableTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
doRule235: BinaryAssociation = BinaryAssociation(
    name="doRule235",
    ends={
        Property(name="basictransitionrules_Rule237", type=asmeta_basictransitionrules_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_ExtendRule236", type=basictransitionrules_Rule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updatingTerm238: BinaryAssociation = BinaryAssociation(
    name="updatingTerm238",
    ends={
        Property(name="basicterms_Term239", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule", type=basicterms_Term, multiplicity=Multiplicity(1, 1))
    }
)
location240: BinaryAssociation = BinaryAssociation(
    name="location240",
    ends={
        Property(name="basicterms_Term242", type=asmeta_basictransitionrules_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_basictransitionrules_UpdateRule241", type=basicterms_Term, multiplicity=Multiplicity(0, 1))
    }
)
constraint275: BinaryAssociation = BinaryAssociation(
    name="constraint275",
    ends={
        Property(name="definitions277", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant276", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
signature278: BinaryAssociation = BinaryAssociation(
    name="signature278",
    ends={
        Property(name="structure280", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature279", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
body281: BinaryAssociation = BinaryAssociation(
    name="body281",
    ends={
        Property(name="basicterms_Term282", type=asmeta_definitions_TemporalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_TemporalProperty", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body283: BinaryAssociation = BinaryAssociation(
    name="body283",
    ends={
        Property(name="basicterms_Term284", type=asmeta_definitions_InvarConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_InvarConstraint", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body285: BinaryAssociation = BinaryAssociation(
    name="body285",
    ends={
        Property(name="basicterms_Term286", type=asmeta_definitions_JusticeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_JusticeConstraint", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
p287: BinaryAssociation = BinaryAssociation(
    name="p287",
    ends={
        Property(name="basicterms_Term288", type=asmeta_definitions_CompassionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_CompassionConstraint", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
q289: BinaryAssociation = BinaryAssociation(
    name="q289",
    ends={
        Property(name="basicterms_Term291", type=asmeta_definitions_CompassionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_CompassionConstraint290", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedRule259: BinaryAssociation = BinaryAssociation(
    name="constrainedRule259",
    ends={
        Property(name="definitions261", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleDeclaration260", type=RuleDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedFunction262: BinaryAssociation = BinaryAssociation(
    name="constrainedFunction262",
    ends={
        Property(name="definitions264", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="Function263", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
body265: BinaryAssociation = BinaryAssociation(
    name="body265",
    ends={
        Property(name="basicterms_Term266", type=asmeta_definitions_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Invariant", type=basicterms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain267: BinaryAssociation = BinaryAssociation(
    name="domain267",
    ends={
        Property(name="domains_Domain268", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function", type=domains_Domain, multiplicity=Multiplicity(0, 1))
    }
)
codomain269: BinaryAssociation = BinaryAssociation(
    name="codomain269",
    ends={
        Property(name="domains_Domain271", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_definitions_Function270", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
definition272: BinaryAssociation = BinaryAssociation(
    name="definition272",
    ends={
        Property(name="structure274", type=asmeta_definitions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionDefinition273", type=FunctionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
baseDomain294: BinaryAssociation = BinaryAssociation(
    name="baseDomain294",
    ends={
        Property(name="domains_Domain295", type=asmeta_domains_PowersetDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_PowersetDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
sourceDomain296: BinaryAssociation = BinaryAssociation(
    name="sourceDomain296",
    ends={
        Property(name="domains_Domain297", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
targetDomain298: BinaryAssociation = BinaryAssociation(
    name="targetDomain298",
    ends={
        Property(name="domains_Domain300", type=asmeta_domains_MapDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_MapDomain299", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
element301: BinaryAssociation = BinaryAssociation(
    name="element301",
    ends={
        Property(name="domains_EnumElement", type=asmeta_domains_EnumTd, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_EnumTd", type=domains_EnumElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraint302: BinaryAssociation = BinaryAssociation(
    name="constraint302",
    ends={
        Property(name="definitions304", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Invariant303", type=Invariant, multiplicity=Multiplicity(0, 9999))
    }
)
signature305: BinaryAssociation = BinaryAssociation(
    name="signature305",
    ends={
        Property(name="structure307", type=asmeta_domains_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature306", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
initialization308: BinaryAssociation = BinaryAssociation(
    name="initialization308",
    ends={
        Property(name="structure310", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainInitialization309", type=DomainInitialization, multiplicity=Multiplicity(0, 9999))
    }
)
definition311: BinaryAssociation = BinaryAssociation(
    name="definition311",
    ends={
        Property(name="structure313", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainDefinition312", type=DomainDefinition, multiplicity=Multiplicity(0, 1))
    }
)
domain292: BinaryAssociation = BinaryAssociation(
    name="domain292",
    ends={
        Property(name="domains_Domain293", type=asmeta_domains_SequenceDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_SequenceDomain", type=domains_Domain, multiplicity=Multiplicity(1, 1))
    }
)
typeDomain314: BinaryAssociation = BinaryAssociation(
    name="typeDomain314",
    ends={
        Property(name="domains_TypeDomain", type=asmeta_domains_ConcreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="asmeta_domains_ConcreteDomain", type=domains_TypeDomain, multiplicity=Multiplicity(1, 1))
    }
)
domain315: BinaryAssociation = BinaryAssociation(
    name="domain315",
    ends={
        Property(name="domains_Domain316", type=asmeta_domains_BagDomain, multiplicity=Multiplicity(1, 1)),
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
gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_SequenceCt)
gen_asmeta_furtherterms_RealTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_RealTerm)
gen_asmeta_furtherterms_MapTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_MapTerm)
gen_asmeta_furtherterms_MapCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_MapCt)
gen_asmeta_furtherterms_LetTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_LetTerm)
gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ForallTerm)
gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_ComprehensionTerm)
gen_asmeta_furtherterms_ComplexTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_ComplexTerm)
gen_asmeta_furtherterms_CharTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_CharTerm)
gen_asmeta_furtherterms_CaseTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_CaseTerm)
gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm = Generalization(general=VariableBindingTerm, specific=asmeta_furtherterms_FiniteQuantificationTerm)
gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistUniqueTerm)
gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm = Generalization(general=FiniteQuantificationTerm, specific=asmeta_furtherterms_ExistTerm)
gen_asmeta_furtherterms_EnumTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_furtherterms_EnumTerm)
gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_furtherterms_ConditionalTerm)
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
gen_asmeta_furtherterms_BagTerm_CollectionTerm = Generalization(general=CollectionTerm, specific=asmeta_furtherterms_BagTerm)
gen_asmeta_furtherterms_BagCt_ComprehensionTerm = Generalization(general=ComprehensionTerm, specific=asmeta_furtherterms_BagCt)
gen_asmeta_basicterms_VariableTerm_BasicTerm = Generalization(general=BasicTerm, specific=asmeta_basicterms_VariableTerm)
gen_asmeta_basicterms_UndefTerm_ConstantTerm = Generalization(general=ConstantTerm, specific=asmeta_basicterms_UndefTerm)
gen_asmeta_basicterms_TupleTerm_ExtendedTerm = Generalization(general=ExtendedTerm, specific=asmeta_basicterms_TupleTerm)
gen_asmeta_structure_Initialization_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Initialization)
gen_asmeta_turbotransitionrules_TurboRule_Rule = Generalization(general=Rule, specific=asmeta_turbotransitionrules_TurboRule)
gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration = Generalization(general=RuleDeclaration, specific=asmeta_turbotransitionrules_TurboDeclaration)
gen_asmeta_turbotransitionrules_SeqRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_SeqRule)
gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboLocalStateRule)
gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboCallRule)
gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TurboReturnRule)
gen_asmeta_structure_Asm_NamedElement = Generalization(general=NamedElement, specific=asmeta_structure_Asm)
gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_IterativeWhileRule)
gen_asmeta_derivedtransitionrules_DerivedRule_Rule = Generalization(general=Rule, specific=asmeta_derivedtransitionrules_DerivedRule)
gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule = Generalization(general=BasicDerivedRule, specific=asmeta_derivedtransitionrules_CaseRule)
gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_BasicDerivedRule)
gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule = Generalization(general=DerivedRule, specific=asmeta_derivedtransitionrules_TurboDerivedRule)
gen_asmeta_basictransitionrules_TermAsRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_TermAsRule)
gen_asmeta_basictransitionrules_BasicRule_Rule = Generalization(general=Rule, specific=asmeta_basictransitionrules_BasicRule)
gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_TryCatchRule)
gen_asmeta_turbotransitionrules_IterateRule_TurboRule = Generalization(general=TurboRule, specific=asmeta_turbotransitionrules_IterateRule)
gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule = Generalization(general=TurboDerivedRule, specific=asmeta_derivedtransitionrules_RecursiveWhileRule)
gen_asmeta_basictransitionrules_BlockRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_BlockRule)
gen_asmeta_basictransitionrules_ConditionalRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ConditionalRule)
gen_asmeta_basictransitionrules_ForallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ForallRule)
gen_asmeta_basictransitionrules_LetRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_LetRule)
gen_asmeta_basictransitionrules_ExtendRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ExtendRule)
gen_asmeta_basictransitionrules_ChooseRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_ChooseRule)
gen_asmeta_basictransitionrules_MacroCallRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_MacroCallRule)
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
gen_asmeta_basictransitionrules_UpdateRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_UpdateRule)
gen_asmeta_basictransitionrules_SkipRule_BasicRule = Generalization(general=BasicRule, specific=asmeta_basictransitionrules_SkipRule)
gen_asmeta_definitions_Classifier_NamedElement = Generalization(general=NamedElement, specific=asmeta_definitions_Classifier)
gen_asmeta_definitions_Property_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_Property)
gen_asmeta_definitions_TemporalProperty_Property = Generalization(general=Property_, specific=asmeta_definitions_TemporalProperty)
gen_asmeta_definitions_CtlSpec_TemporalProperty = Generalization(general=TemporalProperty, specific=asmeta_definitions_CtlSpec)
gen_asmeta_definitions_LtlSpec_TemporalProperty = Generalization(general=TemporalProperty, specific=asmeta_definitions_LtlSpec)
gen_asmeta_definitions_InvarConstraint_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_InvarConstraint)
gen_asmeta_definitions_FairnessConstraint_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_FairnessConstraint)
gen_asmeta_definitions_JusticeConstraint_FairnessConstraint = Generalization(general=FairnessConstraint, specific=asmeta_definitions_JusticeConstraint)
gen_asmeta_definitions_CompassionConstraint_FairnessConstraint = Generalization(general=FairnessConstraint, specific=asmeta_definitions_CompassionConstraint)
gen_asmeta_definitions_Function_Classifier = Generalization(general=Classifier, specific=asmeta_definitions_Function)
gen_asmeta_domains_ProductDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_ProductDomain)
gen_asmeta_domains_PowersetDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_PowersetDomain)
gen_asmeta_domains_MapDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_MapDomain)
gen_asmeta_domains_IntegerDomain_RealDomain = Generalization(general=RealDomain, specific=asmeta_domains_IntegerDomain)
gen_asmeta_domains_EnumTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_EnumTd)
gen_asmeta_domains_Domain_Classifier = Generalization(general=Classifier, specific=asmeta_domains_Domain)
gen_asmeta_domains_ConcreteDomain_Domain = Generalization(general=Domain, specific=asmeta_domains_ConcreteDomain)
gen_asmeta_domains_NaturalDomain_IntegerDomain = Generalization(general=IntegerDomain, specific=asmeta_domains_NaturalDomain)
gen_asmeta_domains_UndefDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_UndefDomain)
gen_asmeta_domains_TypeDomain_Domain = Generalization(general=Domain, specific=asmeta_domains_TypeDomain)
gen_asmeta_domains_StructuredTd_TypeDomain = Generalization(general=TypeDomain, specific=asmeta_domains_StructuredTd)
gen_asmeta_domains_StringDomain_BasicTd = Generalization(general=BasicTd, specific=asmeta_domains_StringDomain)
gen_asmeta_domains_SequenceDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_SequenceDomain)
gen_asmeta_domains_RuleDomain_StructuredTd = Generalization(general=StructuredTd, specific=asmeta_domains_RuleDomain)
gen_asmeta_domains_ReserveDomain_AbstractTd = Generalization(general=AbstractTd, specific=asmeta_domains_ReserveDomain)
gen_asmeta_domains_RealDomain_ComplexDomain = Generalization(general=ComplexDomain, specific=asmeta_domains_RealDomain)
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
    types={asmeta_furtherterms_IntegerTerm, ConstantTerm, asmeta_furtherterms_NaturalTerm, asmeta_furtherterms_VariableBindingTerm, ExtendedTerm, asmeta_furtherterms_StringTerm, asmeta_furtherterms_SetCt, ComprehensionTerm, asmeta_furtherterms_SequenceTerm, CollectionTerm, asmeta_furtherterms_SequenceCt, asmeta_furtherterms_RealTerm, asmeta_furtherterms_MapTerm, basicterms_TupleTerm, asmeta_furtherterms_MapCt, asmeta_furtherterms_LetTerm, VariableBindingTerm, basicterms_VariableTerm, basicterms_Term, asmeta_furtherterms_ForallTerm, FiniteQuantificationTerm, asmeta_furtherterms_ComprehensionTerm, asmeta_furtherterms_ComplexTerm, asmeta_furtherterms_CharTerm, asmeta_furtherterms_CaseTerm, asmeta_furtherterms_FiniteQuantificationTerm, asmeta_furtherterms_ExistUniqueTerm, asmeta_furtherterms_ExistTerm, asmeta_furtherterms_EnumTerm, asmeta_furtherterms_ConditionalTerm, asmeta_basicterms_SetTerm, asmeta_basicterms_RuleAsTerm, RuleDeclaration, asmeta_basicterms_LocationTerm, FunctionTerm, asmeta_basicterms_FunctionTerm, Function, asmeta_basicterms_ExtendedTerm, Term, asmeta_basicterms_DomainTerm, asmeta_basicterms_ConstantTerm, asmeta_basicterms_CollectionTerm, asmeta_basicterms_BooleanTerm, asmeta_basicterms_BasicTerm, asmeta_basicterms_Term, domains_Domain, basictransitionrules_TermAsRule, asmeta_furtherterms_BagTerm, asmeta_furtherterms_BagCt, asmeta_basicterms_VariableTerm, BasicTerm, furtherterms_FiniteQuantificationTerm, asmeta_basicterms_UndefTerm, asmeta_basicterms_TupleTerm, DomainDefinition, Asm, FairnessConstraint, InvarConstraint, asmeta_structure_FunctionInitialization, DynamicFunction, asmeta_structure_DomainInitialization, domains_ConcreteDomain, asmeta_structure_Signature, asmeta_structure_NamedElement, asmeta_structure_AgentInitialization, basictransitionrules_MacroCallRule, Initialization, asmeta_structure_Body, FunctionDefinition, Property_, asmeta_structure_FunctionDefinition, asmeta_structure_DomainDefinition, asmeta_structure_Initialization, NamedElement, DomainInitialization, FunctionInitialization, AgentInitialization, asmeta_structure_Header, ImportClause, Header, domains_StructuredTd, asmeta_structure_ExportClause, asmeta_structure_ImportClause, basictransitionrules_MacroDeclaration, asmeta_turbotransitionrules_TurboRule, Rule, asmeta_turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_SeqRule, TurboRule, asmeta_turbotransitionrules_TurboLocalStateRule, basictransitionrules_Rule, LocalFunction, asmeta_turbotransitionrules_TurboCallRule, turbotransitionrules_TurboDeclaration, asmeta_turbotransitionrules_TurboReturnRule, turbotransitionrules_TurboCallRule, Signature, ExportClause, asmeta_structure_Asm, Body, asmeta_derivedtransitionrules_IterativeWhileRule, asmeta_derivedtransitionrules_DerivedRule, asmeta_derivedtransitionrules_CaseRule, BasicDerivedRule, asmeta_derivedtransitionrules_BasicDerivedRule, DerivedRule, asmeta_derivedtransitionrules_TurboDerivedRule, asmeta_basictransitionrules_TermAsRule, asmeta_basictransitionrules_BasicRule, asmeta_basictransitionrules_Rule, asmeta_turbotransitionrules_TryCatchRule, asmeta_turbotransitionrules_IterateRule, asmeta_derivedtransitionrules_RecursiveWhileRule, TurboDerivedRule, asmeta_basictransitionrules_BlockRule, asmeta_basictransitionrules_ConditionalRule, asmeta_basictransitionrules_ForallRule, asmeta_basictransitionrules_LetRule, asmeta_basictransitionrules_ExtendRule, asmeta_basictransitionrules_ChooseRule, BasicRule, asmeta_basictransitionrules_MacroCallRule, asmeta_basictransitionrules_MacroDeclaration, asmeta_definitions_RuleDeclaration, Classifier, Invariant, asmeta_definitions_LocalFunction, asmeta_definitions_ControlledFunction, asmeta_definitions_SharedFunction, asmeta_definitions_MonitoredFunction, asmeta_definitions_OutFunction, asmeta_definitions_DynamicFunction, BasicFunction, asmeta_definitions_StaticFunction, asmeta_definitions_DerivedFunction, asmeta_definitions_BasicFunction, asmeta_definitions_Invariant, asmeta_basictransitionrules_UpdateRule, asmeta_basictransitionrules_SkipRule, asmeta_definitions_Classifier, asmeta_definitions_Property, asmeta_definitions_TemporalProperty, asmeta_definitions_CtlSpec, TemporalProperty, asmeta_definitions_LtlSpec, asmeta_definitions_InvarConstraint, asmeta_definitions_FairnessConstraint, asmeta_definitions_JusticeConstraint, asmeta_definitions_CompassionConstraint, asmeta_definitions_Function, asmeta_domains_ProductDomain, asmeta_domains_PowersetDomain, asmeta_domains_MapDomain, asmeta_domains_IntegerDomain, RealDomain, asmeta_domains_EnumTd, domains_EnumElement, asmeta_domains_EnumElement, asmeta_domains_Domain, asmeta_domains_ConcreteDomain, domains_TypeDomain, asmeta_domains_NaturalDomain, IntegerDomain, asmeta_domains_UndefDomain, BasicTd, asmeta_domains_TypeDomain, Domain, asmeta_domains_StructuredTd, TypeDomain, asmeta_domains_StringDomain, asmeta_domains_SequenceDomain, StructuredTd, asmeta_domains_RuleDomain, asmeta_domains_ReserveDomain, AbstractTd, asmeta_domains_RealDomain, ComplexDomain, asmeta_domains_ComplexDomain, asmeta_domains_CharDomain, asmeta_domains_BooleanDomain, asmeta_domains_BasicTd, asmeta_domains_BagDomain, asmeta_domains_AnyDomain, asmeta_domains_AgentDomain, asmeta_domains_AbstractTd, VariableKind},
    associations={pair0, variable1, assignmentTerm2, body4, guard12, thenTerm15, variable18, guard20, term23, comparingTerm26, comparedTerm28, otherwiseTerm31, variable7, guard8, elseTerm10, term38, rule40, arguments41, function43, domain45, termAsRule46, term34, finiteQuantificationTerm36, domainDefinition55, ruleDeclaration57, asm59, fairnessConstraint61, invariantConstraint63, initialState65, body68, initializedFunction70, variable72, initializedDomain75, body77, initialState79, domain82, program47, domain48, initialState51, functionDefinition52, property53, importedFunction101, importedRule104, body107, variable109, definedFunction112, body115, definedDomain117, domainInitialization120, functionInitialization122, agentInitialization124, asm126, importClause129, function85, headerSection88, structuredDomain90, exportedFunction91, exportedDomain93, exportedRule96, importedDomain99, headerSection144, mainrule147, resultType149, init151, body152, localFunction155, calledRule157, location158, signature130, exportClause132, asm134, initialState137, defaultInitialState139, bodySection142, rule172, guard174, guard177, rule179, term182, caseTerm184, otherwiseBranch187, term190, updateRule160, location162, catchRule164, tryRule167, rule170, guard206, elseRule208, thenRule211, variable214, guard216, doRule219, inRule222, initExpression224, variable227, ifnone193, doRule195, guard198, variable201, calledMacro204, variable243, constraint245, ruleBody247, asmBody250, initialization253, constrainedDomain256, extendedDomain230, boundVar232, doRule235, updatingTerm238, location240, constraint275, signature278, body281, body283, body285, p287, q289, constrainedRule259, constrainedFunction262, body265, domain267, codomain269, definition272, baseDomain294, sourceDomain296, targetDomain298, element301, constraint302, signature305, initialization308, definition311, domain292, typeDomain314, domain315},
    generalizations={gen_asmeta_furtherterms_IntegerTerm_ConstantTerm, gen_asmeta_furtherterms_NaturalTerm_ConstantTerm, gen_asmeta_furtherterms_VariableBindingTerm_ExtendedTerm, gen_asmeta_furtherterms_StringTerm_ConstantTerm, gen_asmeta_furtherterms_SetCt_ComprehensionTerm, gen_asmeta_furtherterms_SequenceTerm_CollectionTerm, gen_asmeta_furtherterms_SequenceCt_ComprehensionTerm, gen_asmeta_furtherterms_RealTerm_ConstantTerm, gen_asmeta_furtherterms_MapTerm_CollectionTerm, gen_asmeta_furtherterms_MapCt_ComprehensionTerm, gen_asmeta_furtherterms_LetTerm_VariableBindingTerm, gen_asmeta_furtherterms_ForallTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_ComprehensionTerm_VariableBindingTerm, gen_asmeta_furtherterms_ComplexTerm_ConstantTerm, gen_asmeta_furtherterms_CharTerm_ConstantTerm, gen_asmeta_furtherterms_CaseTerm_ExtendedTerm, gen_asmeta_furtherterms_FiniteQuantificationTerm_VariableBindingTerm, gen_asmeta_furtherterms_ExistUniqueTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_ExistTerm_FiniteQuantificationTerm, gen_asmeta_furtherterms_EnumTerm_ConstantTerm, gen_asmeta_furtherterms_ConditionalTerm_ExtendedTerm, gen_asmeta_basicterms_SetTerm_CollectionTerm, gen_asmeta_basicterms_RuleAsTerm_ExtendedTerm, gen_asmeta_basicterms_LocationTerm_FunctionTerm, gen_asmeta_basicterms_FunctionTerm_BasicTerm, gen_asmeta_basicterms_ExtendedTerm_Term, gen_asmeta_basicterms_DomainTerm_ExtendedTerm, gen_asmeta_basicterms_ConstantTerm_BasicTerm, gen_asmeta_basicterms_CollectionTerm_ExtendedTerm, gen_asmeta_basicterms_BooleanTerm_ConstantTerm, gen_asmeta_basicterms_BasicTerm_Term, gen_asmeta_furtherterms_BagTerm_CollectionTerm, gen_asmeta_furtherterms_BagCt_ComprehensionTerm, gen_asmeta_basicterms_VariableTerm_BasicTerm, gen_asmeta_basicterms_UndefTerm_ConstantTerm, gen_asmeta_basicterms_TupleTerm_ExtendedTerm, gen_asmeta_structure_Initialization_NamedElement, gen_asmeta_turbotransitionrules_TurboRule_Rule, gen_asmeta_turbotransitionrules_TurboDeclaration_RuleDeclaration, gen_asmeta_turbotransitionrules_SeqRule_TurboRule, gen_asmeta_turbotransitionrules_TurboLocalStateRule_TurboRule, gen_asmeta_turbotransitionrules_TurboCallRule_TurboRule, gen_asmeta_turbotransitionrules_TurboReturnRule_TurboRule, gen_asmeta_structure_Asm_NamedElement, gen_asmeta_derivedtransitionrules_IterativeWhileRule_TurboDerivedRule, gen_asmeta_derivedtransitionrules_DerivedRule_Rule, gen_asmeta_derivedtransitionrules_CaseRule_BasicDerivedRule, gen_asmeta_derivedtransitionrules_BasicDerivedRule_DerivedRule, gen_asmeta_derivedtransitionrules_TurboDerivedRule_DerivedRule, gen_asmeta_basictransitionrules_TermAsRule_Rule, gen_asmeta_basictransitionrules_BasicRule_Rule, gen_asmeta_turbotransitionrules_TryCatchRule_TurboRule, gen_asmeta_turbotransitionrules_IterateRule_TurboRule, gen_asmeta_derivedtransitionrules_RecursiveWhileRule_TurboDerivedRule, gen_asmeta_basictransitionrules_BlockRule_BasicRule, gen_asmeta_basictransitionrules_ConditionalRule_BasicRule, gen_asmeta_basictransitionrules_ForallRule_BasicRule, gen_asmeta_basictransitionrules_LetRule_BasicRule, gen_asmeta_basictransitionrules_ExtendRule_BasicRule, gen_asmeta_basictransitionrules_ChooseRule_BasicRule, gen_asmeta_basictransitionrules_MacroCallRule_BasicRule, gen_asmeta_basictransitionrules_MacroDeclaration_RuleDeclaration, gen_asmeta_definitions_RuleDeclaration_Classifier, gen_asmeta_definitions_LocalFunction_DynamicFunction, gen_asmeta_definitions_ControlledFunction_DynamicFunction, gen_asmeta_definitions_SharedFunction_DynamicFunction, gen_asmeta_definitions_MonitoredFunction_DynamicFunction, gen_asmeta_definitions_OutFunction_DynamicFunction, gen_asmeta_definitions_DynamicFunction_BasicFunction, gen_asmeta_definitions_StaticFunction_BasicFunction, gen_asmeta_definitions_DerivedFunction_Function, gen_asmeta_definitions_BasicFunction_Function, gen_asmeta_definitions_Invariant_Property, gen_asmeta_basictransitionrules_UpdateRule_BasicRule, gen_asmeta_basictransitionrules_SkipRule_BasicRule, gen_asmeta_definitions_Classifier_NamedElement, gen_asmeta_definitions_Property_Classifier, gen_asmeta_definitions_TemporalProperty_Property, gen_asmeta_definitions_CtlSpec_TemporalProperty, gen_asmeta_definitions_LtlSpec_TemporalProperty, gen_asmeta_definitions_InvarConstraint_Classifier, gen_asmeta_definitions_FairnessConstraint_Classifier, gen_asmeta_definitions_JusticeConstraint_FairnessConstraint, gen_asmeta_definitions_CompassionConstraint_FairnessConstraint, gen_asmeta_definitions_Function_Classifier, gen_asmeta_domains_ProductDomain_StructuredTd, gen_asmeta_domains_PowersetDomain_StructuredTd, gen_asmeta_domains_MapDomain_StructuredTd, gen_asmeta_domains_IntegerDomain_RealDomain, gen_asmeta_domains_EnumTd_TypeDomain, gen_asmeta_domains_Domain_Classifier, gen_asmeta_domains_ConcreteDomain_Domain, gen_asmeta_domains_NaturalDomain_IntegerDomain, gen_asmeta_domains_UndefDomain_BasicTd, gen_asmeta_domains_TypeDomain_Domain, gen_asmeta_domains_StructuredTd_TypeDomain, gen_asmeta_domains_StringDomain_BasicTd, gen_asmeta_domains_SequenceDomain_StructuredTd, gen_asmeta_domains_RuleDomain_StructuredTd, gen_asmeta_domains_ReserveDomain_AbstractTd, gen_asmeta_domains_RealDomain_ComplexDomain, gen_asmeta_domains_ComplexDomain_BasicTd, gen_asmeta_domains_CharDomain_BasicTd, gen_asmeta_domains_BooleanDomain_BasicTd, gen_asmeta_domains_BasicTd_TypeDomain, gen_asmeta_domains_BagDomain_StructuredTd, gen_asmeta_domains_AnyDomain_TypeDomain, gen_asmeta_domains_AgentDomain_AbstractTd, gen_asmeta_domains_AbstractTd_TypeDomain},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
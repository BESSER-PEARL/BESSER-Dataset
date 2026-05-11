import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vcml::Statement,
    CharacteristicReference::C,
    vcml::ShortVarReference,
    vcml::ObjectCharacteristicReference,
    Literal,
    vcml::EObject,
    Condition,
    ConstraintRestriction,
    vcml::ConstraintRestrictionFalse,
    vcml::SubpartOfCondition,
    vcml::NegatedConstraintRestrictionLHS,
    vcml::PartOfCondition,
    vcml::PartialKey,
    vcml::FunctionOrTable,
    vcml::Expression,
    ConstraintObject,
    vcml::ConstraintClass,
    vcml::ShortVarDefinition,
    vcml::CharacteristicReference::C,
    vcml::ConstraintRestriction,
    vcml::ConstraintObject,
    vcml::FormattedDocumentationBlock,
    vcml::MultipleLanguageDocumentation::LanguageBlock,
    Documentation,
    vcml::MultipleLanguageDocumentation,
    vcml::SimpleDocumentation,
    vcml::ObjectType,
    vcml::ConstraintMaterial,
    vcml::MultiLanguageDescription,
    Description,
    vcml::MultiLanguageDescriptions,
    vcml::SimpleDescription,
    vcml::Row,
    vcml::VariantTableArgument,
    vcml::VariantFunctionArgument,
    vcml::ValueAssignment,
    vcml::Classification,
    vcml::CharacteristicGroup,
    vcml::ConstraintSource,
    vcml::Condition,
    vcml::ConditionSource,
    vcml::ProcedureSource,
    Dependency,
    vcml::Dependency,
    vcml::NumberListEntry,
    vcml::DateCharacteristicValue,
    vcml::CharacteristicValue,
    vcml::NumericCharacteristicValue,
    vcml::CharacteristicOrValueDependencies,
    vcml::CharacteristicType,
    vcml::Documentation,
    BOMItem,
    vcml::BOMItem::Class,
    vcml::BOMItem::Material,
    vcml::ConfigurationProfileEntry,
    vcml::BOMItem,
    VCObject,
    vcml::Precondition,
    vcml::Procedure,
    vcml::Constraint,
    vcml::ConfigurationProfile,
    vcml::VariantTableContent,
    vcml::Class,
    vcml::VariantTable,
    vcml::InterfaceDesign,
    vcml::VariantFunction,
    vcml::Material,
    vcml::Characteristic,
    vcml::DependencyNet,
    vcml::SelectionCondition,
    vcml::BillOfMaterial,
    vcml::Description,
    CharacteristicType,
    vcml::SymbolicType,
    vcml::DateType,
    vcml::NumericType,
    vcml::VCObject,
    vcml::Option,
    vcml::Import,
    vcml::VcmlModel,
    vcml::BinaryCondition,
    vcml::ConditionalConstraintRestriction,
    List,
    vcml::SymbolList,
    vcml::NumberList,
    vcml::InCondition::P,
    vcml::List,
    vcml::InCondition::C,
    vcml::IsSpecified::P,
    vcml::IsSpecified::C,
    vcml::Comparison,
    vcml::UnaryCondition,
    vcml::SymbolicLiteral,
    NumberListEntry,
    vcml::NumericInterval,
    vcml::NumericLiteral,
    vcml::MDataCharacteristic::P,
    vcml::MDataCharacteristic::C,
    Expression,
    vcml::CountParts,
    vcml::SumParts,
    vcml::FunctionCall,
    vcml::Literal,
    vcml::BinaryExpression,
    vcml::UnaryExpression,
    vcml::TypeOf,
    SetOrDelDefault,
    vcml::DelDefault,
    vcml::SetDefault,
    FunctionOrTable,
    vcml::CharacteristicReference::P,
    SimpleStatement,
    vcml::IsInvisible,
    vcml::Table,
    vcml::Function,
    vcml::SetPricingFactor,
    vcml::SetOrDelDefault,
    vcml::PFunction,
    vcml::Assignment,
    Statement,
    vcml::SimpleStatement,
    vcml::ConditionalStatement,
    vcml::CompoundStatement,
    Status,
    ProcedureLocation,
    Fixing,
    UnaryExpressionOperator,
    OptionType,
    ComparisonOperator,
    FunctionName,
    Language,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vcml::statement_is_not_abstract():
    assert not inspect.isabstract(vcml::Statement)


def test_vcml::statement_constructor_exists():
    assert callable(vcml::Statement.__init__)


def test_vcml::statement_constructor_args():
    sig = inspect.signature(vcml::Statement.__init__)
    params = list(sig.parameters.keys())



def test_characteristicreference::c_is_not_abstract():
    assert not inspect.isabstract(CharacteristicReference::C)


def test_characteristicreference::c_constructor_exists():
    assert callable(CharacteristicReference::C.__init__)


def test_characteristicreference::c_constructor_args():
    sig = inspect.signature(CharacteristicReference::C.__init__)
    params = list(sig.parameters.keys())



def test_vcml::shortvarreference_is_not_abstract():
    assert not inspect.isabstract(vcml::ShortVarReference)


def test_vcml::shortvarreference_constructor_exists():
    assert callable(vcml::ShortVarReference.__init__)


def test_vcml::shortvarreference_constructor_args():
    sig = inspect.signature(vcml::ShortVarReference.__init__)
    params = list(sig.parameters.keys())



def test_vcml::objectcharacteristicreference_is_not_abstract():
    assert not inspect.isabstract(vcml::ObjectCharacteristicReference)


def test_vcml::objectcharacteristicreference_constructor_exists():
    assert callable(vcml::ObjectCharacteristicReference.__init__)


def test_vcml::objectcharacteristicreference_constructor_args():
    sig = inspect.signature(vcml::ObjectCharacteristicReference.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_vcml::eobject_is_not_abstract():
    assert not inspect.isabstract(vcml::EObject)


def test_vcml::eobject_constructor_exists():
    assert callable(vcml::EObject.__init__)


def test_vcml::eobject_constructor_args():
    sig = inspect.signature(vcml::EObject.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_constraintrestriction_is_not_abstract():
    assert not inspect.isabstract(ConstraintRestriction)


def test_constraintrestriction_constructor_exists():
    assert callable(ConstraintRestriction.__init__)


def test_constraintrestriction_constructor_args():
    sig = inspect.signature(ConstraintRestriction.__init__)
    params = list(sig.parameters.keys())



def test_vcml::constraintrestrictionfalse_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintRestrictionFalse)


def test_vcml::constraintrestrictionfalse_constructor_exists():
    assert callable(vcml::ConstraintRestrictionFalse.__init__)


def test_vcml::constraintrestrictionfalse_constructor_args():
    sig = inspect.signature(vcml::ConstraintRestrictionFalse.__init__)
    params = list(sig.parameters.keys())



def test_vcml::subpartofcondition_is_not_abstract():
    assert not inspect.isabstract(vcml::SubpartOfCondition)


def test_vcml::subpartofcondition_constructor_exists():
    assert callable(vcml::SubpartOfCondition.__init__)


def test_vcml::subpartofcondition_constructor_args():
    sig = inspect.signature(vcml::SubpartOfCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml::negatedconstraintrestrictionlhs_is_not_abstract():
    assert not inspect.isabstract(vcml::NegatedConstraintRestrictionLHS)


def test_vcml::negatedconstraintrestrictionlhs_constructor_exists():
    assert callable(vcml::NegatedConstraintRestrictionLHS.__init__)


def test_vcml::negatedconstraintrestrictionlhs_constructor_args():
    sig = inspect.signature(vcml::NegatedConstraintRestrictionLHS.__init__)
    params = list(sig.parameters.keys())



def test_vcml::partofcondition_is_not_abstract():
    assert not inspect.isabstract(vcml::PartOfCondition)


def test_vcml::partofcondition_constructor_exists():
    assert callable(vcml::PartOfCondition.__init__)


def test_vcml::partofcondition_constructor_args():
    sig = inspect.signature(vcml::PartOfCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml::partialkey_is_not_abstract():
    assert not inspect.isabstract(vcml::PartialKey)


def test_vcml::partialkey_constructor_exists():
    assert callable(vcml::PartialKey.__init__)


def test_vcml::partialkey_constructor_args():
    sig = inspect.signature(vcml::PartialKey.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_vcml::partialkey_has_key():
    assert hasattr(vcml::PartialKey, "key")
    descriptor = None
    for klass in vcml::PartialKey.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_vcml::functionortable_is_not_abstract():
    assert not inspect.isabstract(vcml::FunctionOrTable)


def test_vcml::functionortable_constructor_exists():
    assert callable(vcml::FunctionOrTable.__init__)


def test_vcml::functionortable_constructor_args():
    sig = inspect.signature(vcml::FunctionOrTable.__init__)
    params = list(sig.parameters.keys())



def test_vcml::expression_is_not_abstract():
    assert not inspect.isabstract(vcml::Expression)


def test_vcml::expression_constructor_exists():
    assert callable(vcml::Expression.__init__)


def test_vcml::expression_constructor_args():
    sig = inspect.signature(vcml::Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraintobject_is_not_abstract():
    assert not inspect.isabstract(ConstraintObject)


def test_constraintobject_constructor_exists():
    assert callable(ConstraintObject.__init__)


def test_constraintobject_constructor_args():
    sig = inspect.signature(ConstraintObject.__init__)
    params = list(sig.parameters.keys())



def test_vcml::constraintclass_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintClass)


def test_vcml::constraintclass_constructor_exists():
    assert callable(vcml::ConstraintClass.__init__)


def test_vcml::constraintclass_constructor_args():
    sig = inspect.signature(vcml::ConstraintClass.__init__)
    params = list(sig.parameters.keys())



def test_vcml::shortvardefinition_is_not_abstract():
    assert not inspect.isabstract(vcml::ShortVarDefinition)


def test_vcml::shortvardefinition_constructor_exists():
    assert callable(vcml::ShortVarDefinition.__init__)


def test_vcml::shortvardefinition_constructor_args():
    sig = inspect.signature(vcml::ShortVarDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::shortvardefinition_has_name():
    assert hasattr(vcml::ShortVarDefinition, "name")
    descriptor = None
    for klass in vcml::ShortVarDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::characteristicreference::c_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicReference::C)


def test_vcml::characteristicreference::c_constructor_exists():
    assert callable(vcml::CharacteristicReference::C.__init__)


def test_vcml::characteristicreference::c_constructor_args():
    sig = inspect.signature(vcml::CharacteristicReference::C.__init__)
    params = list(sig.parameters.keys())



def test_vcml::constraintrestriction_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintRestriction)


def test_vcml::constraintrestriction_constructor_exists():
    assert callable(vcml::ConstraintRestriction.__init__)


def test_vcml::constraintrestriction_constructor_args():
    sig = inspect.signature(vcml::ConstraintRestriction.__init__)
    params = list(sig.parameters.keys())



def test_vcml::constraintobject_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintObject)


def test_vcml::constraintobject_constructor_exists():
    assert callable(vcml::ConstraintObject.__init__)


def test_vcml::constraintobject_constructor_args():
    sig = inspect.signature(vcml::ConstraintObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::constraintobject_has_name():
    assert hasattr(vcml::ConstraintObject, "name")
    descriptor = None
    for klass in vcml::ConstraintObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::formatteddocumentationblock_is_not_abstract():
    assert not inspect.isabstract(vcml::FormattedDocumentationBlock)


def test_vcml::formatteddocumentationblock_constructor_exists():
    assert callable(vcml::FormattedDocumentationBlock.__init__)


def test_vcml::formatteddocumentationblock_constructor_args():
    sig = inspect.signature(vcml::FormattedDocumentationBlock.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "format" in params, "Missing parameter 'format'"

def test_vcml::formatteddocumentationblock_has_value():
    assert hasattr(vcml::FormattedDocumentationBlock, "value")
    descriptor = None
    for klass in vcml::FormattedDocumentationBlock.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml::formatteddocumentationblock_has_format():
    assert hasattr(vcml::FormattedDocumentationBlock, "format")
    descriptor = None
    for klass in vcml::FormattedDocumentationBlock.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_vcml::multiplelanguagedocumentation::languageblock_is_not_abstract():
    assert not inspect.isabstract(vcml::MultipleLanguageDocumentation::LanguageBlock)


def test_vcml::multiplelanguagedocumentation::languageblock_constructor_exists():
    assert callable(vcml::MultipleLanguageDocumentation::LanguageBlock.__init__)


def test_vcml::multiplelanguagedocumentation::languageblock_constructor_args():
    sig = inspect.signature(vcml::MultipleLanguageDocumentation::LanguageBlock.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_vcml::multiplelanguagedocumentation::languageblock_has_language():
    assert hasattr(vcml::MultipleLanguageDocumentation::LanguageBlock, "language")
    descriptor = None
    for klass in vcml::MultipleLanguageDocumentation::LanguageBlock.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_documentation_is_not_abstract():
    assert not inspect.isabstract(Documentation)


def test_documentation_constructor_exists():
    assert callable(Documentation.__init__)


def test_documentation_constructor_args():
    sig = inspect.signature(Documentation.__init__)
    params = list(sig.parameters.keys())



def test_vcml::multiplelanguagedocumentation_is_not_abstract():
    assert not inspect.isabstract(vcml::MultipleLanguageDocumentation)


def test_vcml::multiplelanguagedocumentation_constructor_exists():
    assert callable(vcml::MultipleLanguageDocumentation.__init__)


def test_vcml::multiplelanguagedocumentation_constructor_args():
    sig = inspect.signature(vcml::MultipleLanguageDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_vcml::simpledocumentation_is_not_abstract():
    assert not inspect.isabstract(vcml::SimpleDocumentation)


def test_vcml::simpledocumentation_constructor_exists():
    assert callable(vcml::SimpleDocumentation.__init__)


def test_vcml::simpledocumentation_constructor_args():
    sig = inspect.signature(vcml::SimpleDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml::simpledocumentation_has_value():
    assert hasattr(vcml::SimpleDocumentation, "value")
    descriptor = None
    for klass in vcml::SimpleDocumentation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml::objecttype_is_not_abstract():
    assert not inspect.isabstract(vcml::ObjectType)


def test_vcml::objecttype_constructor_exists():
    assert callable(vcml::ObjectType.__init__)


def test_vcml::objecttype_constructor_args():
    sig = inspect.signature(vcml::ObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "classType" in params, "Missing parameter 'classType'"

def test_vcml::objecttype_has_type():
    assert hasattr(vcml::ObjectType, "type")
    descriptor = None
    for klass in vcml::ObjectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_vcml::objecttype_has_classType():
    assert hasattr(vcml::ObjectType, "classType")
    descriptor = None
    for klass in vcml::ObjectType.__mro__:
        if "classType" in klass.__dict__:
            descriptor = klass.__dict__["classType"]
            break
    assert isinstance(descriptor, property)



def test_vcml::constraintmaterial_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintMaterial)


def test_vcml::constraintmaterial_constructor_exists():
    assert callable(vcml::ConstraintMaterial.__init__)


def test_vcml::constraintmaterial_constructor_args():
    sig = inspect.signature(vcml::ConstraintMaterial.__init__)
    params = list(sig.parameters.keys())



def test_vcml::multilanguagedescription_is_not_abstract():
    assert not inspect.isabstract(vcml::MultiLanguageDescription)


def test_vcml::multilanguagedescription_constructor_exists():
    assert callable(vcml::MultiLanguageDescription.__init__)


def test_vcml::multilanguagedescription_constructor_args():
    sig = inspect.signature(vcml::MultiLanguageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "language" in params, "Missing parameter 'language'"

def test_vcml::multilanguagedescription_has_value():
    assert hasattr(vcml::MultiLanguageDescription, "value")
    descriptor = None
    for klass in vcml::MultiLanguageDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml::multilanguagedescription_has_language():
    assert hasattr(vcml::MultiLanguageDescription, "language")
    descriptor = None
    for klass in vcml::MultiLanguageDescription.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_description_is_not_abstract():
    assert not inspect.isabstract(Description)


def test_description_constructor_exists():
    assert callable(Description.__init__)


def test_description_constructor_args():
    sig = inspect.signature(Description.__init__)
    params = list(sig.parameters.keys())



def test_vcml::multilanguagedescriptions_is_not_abstract():
    assert not inspect.isabstract(vcml::MultiLanguageDescriptions)


def test_vcml::multilanguagedescriptions_constructor_exists():
    assert callable(vcml::MultiLanguageDescriptions.__init__)


def test_vcml::multilanguagedescriptions_constructor_args():
    sig = inspect.signature(vcml::MultiLanguageDescriptions.__init__)
    params = list(sig.parameters.keys())



def test_vcml::simpledescription_is_not_abstract():
    assert not inspect.isabstract(vcml::SimpleDescription)


def test_vcml::simpledescription_constructor_exists():
    assert callable(vcml::SimpleDescription.__init__)


def test_vcml::simpledescription_constructor_args():
    sig = inspect.signature(vcml::SimpleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml::simpledescription_has_value():
    assert hasattr(vcml::SimpleDescription, "value")
    descriptor = None
    for klass in vcml::SimpleDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml::row_is_not_abstract():
    assert not inspect.isabstract(vcml::Row)


def test_vcml::row_constructor_exists():
    assert callable(vcml::Row.__init__)


def test_vcml::row_constructor_args():
    sig = inspect.signature(vcml::Row.__init__)
    params = list(sig.parameters.keys())



def test_vcml::varianttableargument_is_not_abstract():
    assert not inspect.isabstract(vcml::VariantTableArgument)


def test_vcml::varianttableargument_constructor_exists():
    assert callable(vcml::VariantTableArgument.__init__)


def test_vcml::varianttableargument_constructor_args():
    sig = inspect.signature(vcml::VariantTableArgument.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_vcml::varianttableargument_has_key():
    assert hasattr(vcml::VariantTableArgument, "key")
    descriptor = None
    for klass in vcml::VariantTableArgument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_vcml::variantfunctionargument_is_not_abstract():
    assert not inspect.isabstract(vcml::VariantFunctionArgument)


def test_vcml::variantfunctionargument_constructor_exists():
    assert callable(vcml::VariantFunctionArgument.__init__)


def test_vcml::variantfunctionargument_constructor_args():
    sig = inspect.signature(vcml::VariantFunctionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_vcml::variantfunctionargument_has_in_():
    assert hasattr(vcml::VariantFunctionArgument, "in_")
    descriptor = None
    for klass in vcml::VariantFunctionArgument.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_vcml::valueassignment_is_not_abstract():
    assert not inspect.isabstract(vcml::ValueAssignment)


def test_vcml::valueassignment_constructor_exists():
    assert callable(vcml::ValueAssignment.__init__)


def test_vcml::valueassignment_constructor_args():
    sig = inspect.signature(vcml::ValueAssignment.__init__)
    params = list(sig.parameters.keys())



def test_vcml::classification_is_not_abstract():
    assert not inspect.isabstract(vcml::Classification)


def test_vcml::classification_constructor_exists():
    assert callable(vcml::Classification.__init__)


def test_vcml::classification_constructor_args():
    sig = inspect.signature(vcml::Classification.__init__)
    params = list(sig.parameters.keys())



def test_vcml::characteristicgroup_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicGroup)


def test_vcml::characteristicgroup_constructor_exists():
    assert callable(vcml::CharacteristicGroup.__init__)


def test_vcml::characteristicgroup_constructor_args():
    sig = inspect.signature(vcml::CharacteristicGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::characteristicgroup_has_name():
    assert hasattr(vcml::CharacteristicGroup, "name")
    descriptor = None
    for klass in vcml::CharacteristicGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::constraintsource_is_not_abstract():
    assert not inspect.isabstract(vcml::ConstraintSource)


def test_vcml::constraintsource_constructor_exists():
    assert callable(vcml::ConstraintSource.__init__)


def test_vcml::constraintsource_constructor_args():
    sig = inspect.signature(vcml::ConstraintSource.__init__)
    params = list(sig.parameters.keys())



def test_vcml::condition_is_not_abstract():
    assert not inspect.isabstract(vcml::Condition)


def test_vcml::condition_constructor_exists():
    assert callable(vcml::Condition.__init__)


def test_vcml::condition_constructor_args():
    sig = inspect.signature(vcml::Condition.__init__)
    params = list(sig.parameters.keys())



def test_vcml::conditionsource_is_not_abstract():
    assert not inspect.isabstract(vcml::ConditionSource)


def test_vcml::conditionsource_constructor_exists():
    assert callable(vcml::ConditionSource.__init__)


def test_vcml::conditionsource_constructor_args():
    sig = inspect.signature(vcml::ConditionSource.__init__)
    params = list(sig.parameters.keys())



def test_vcml::proceduresource_is_not_abstract():
    assert not inspect.isabstract(vcml::ProcedureSource)


def test_vcml::proceduresource_constructor_exists():
    assert callable(vcml::ProcedureSource.__init__)


def test_vcml::proceduresource_constructor_args():
    sig = inspect.signature(vcml::ProcedureSource.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_vcml::dependency_is_not_abstract():
    assert not inspect.isabstract(vcml::Dependency)


def test_vcml::dependency_constructor_exists():
    assert callable(vcml::Dependency.__init__)


def test_vcml::dependency_constructor_args():
    sig = inspect.signature(vcml::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_vcml::numberlistentry_is_not_abstract():
    assert not inspect.isabstract(vcml::NumberListEntry)


def test_vcml::numberlistentry_constructor_exists():
    assert callable(vcml::NumberListEntry.__init__)


def test_vcml::numberlistentry_constructor_args():
    sig = inspect.signature(vcml::NumberListEntry.__init__)
    params = list(sig.parameters.keys())



def test_vcml::datecharacteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml::DateCharacteristicValue)


def test_vcml::datecharacteristicvalue_constructor_exists():
    assert callable(vcml::DateCharacteristicValue.__init__)


def test_vcml::datecharacteristicvalue_constructor_args():
    sig = inspect.signature(vcml::DateCharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_vcml::datecharacteristicvalue_has_default():
    assert hasattr(vcml::DateCharacteristicValue, "default")
    descriptor = None
    for klass in vcml::DateCharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_vcml::datecharacteristicvalue_has_from_():
    assert hasattr(vcml::DateCharacteristicValue, "from_")
    descriptor = None
    for klass in vcml::DateCharacteristicValue.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_vcml::datecharacteristicvalue_has_to():
    assert hasattr(vcml::DateCharacteristicValue, "to")
    descriptor = None
    for klass in vcml::DateCharacteristicValue.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_vcml::characteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicValue)


def test_vcml::characteristicvalue_constructor_exists():
    assert callable(vcml::CharacteristicValue.__init__)


def test_vcml::characteristicvalue_constructor_args():
    sig = inspect.signature(vcml::CharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::characteristicvalue_has_default():
    assert hasattr(vcml::CharacteristicValue, "default")
    descriptor = None
    for klass in vcml::CharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristicvalue_has_name():
    assert hasattr(vcml::CharacteristicValue, "name")
    descriptor = None
    for klass in vcml::CharacteristicValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::numericcharacteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml::NumericCharacteristicValue)


def test_vcml::numericcharacteristicvalue_constructor_exists():
    assert callable(vcml::NumericCharacteristicValue.__init__)


def test_vcml::numericcharacteristicvalue_constructor_args():
    sig = inspect.signature(vcml::NumericCharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_vcml::numericcharacteristicvalue_has_default():
    assert hasattr(vcml::NumericCharacteristicValue, "default")
    descriptor = None
    for klass in vcml::NumericCharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_vcml::characteristicorvaluedependencies_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicOrValueDependencies)


def test_vcml::characteristicorvaluedependencies_constructor_exists():
    assert callable(vcml::CharacteristicOrValueDependencies.__init__)


def test_vcml::characteristicorvaluedependencies_constructor_args():
    sig = inspect.signature(vcml::CharacteristicOrValueDependencies.__init__)
    params = list(sig.parameters.keys())



def test_vcml::characteristictype_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicType)


def test_vcml::characteristictype_constructor_exists():
    assert callable(vcml::CharacteristicType.__init__)


def test_vcml::characteristictype_constructor_args():
    sig = inspect.signature(vcml::CharacteristicType.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfChars" in params, "Missing parameter 'numberOfChars'"

def test_vcml::characteristictype_has_numberOfChars():
    assert hasattr(vcml::CharacteristicType, "numberOfChars")
    descriptor = None
    for klass in vcml::CharacteristicType.__mro__:
        if "numberOfChars" in klass.__dict__:
            descriptor = klass.__dict__["numberOfChars"]
            break
    assert isinstance(descriptor, property)



def test_vcml::documentation_is_not_abstract():
    assert not inspect.isabstract(vcml::Documentation)


def test_vcml::documentation_constructor_exists():
    assert callable(vcml::Documentation.__init__)


def test_vcml::documentation_constructor_args():
    sig = inspect.signature(vcml::Documentation.__init__)
    params = list(sig.parameters.keys())



def test_bomitem_is_not_abstract():
    assert not inspect.isabstract(BOMItem)


def test_bomitem_constructor_exists():
    assert callable(BOMItem.__init__)


def test_bomitem_constructor_args():
    sig = inspect.signature(BOMItem.__init__)
    params = list(sig.parameters.keys())



def test_vcml::bomitem::class_is_not_abstract():
    assert not inspect.isabstract(vcml::BOMItem::Class)


def test_vcml::bomitem::class_constructor_exists():
    assert callable(vcml::BOMItem::Class.__init__)


def test_vcml::bomitem::class_constructor_args():
    sig = inspect.signature(vcml::BOMItem::Class.__init__)
    params = list(sig.parameters.keys())



def test_vcml::bomitem::material_is_not_abstract():
    assert not inspect.isabstract(vcml::BOMItem::Material)


def test_vcml::bomitem::material_constructor_exists():
    assert callable(vcml::BOMItem::Material.__init__)


def test_vcml::bomitem::material_constructor_args():
    sig = inspect.signature(vcml::BOMItem::Material.__init__)
    params = list(sig.parameters.keys())



def test_vcml::configurationprofileentry_is_not_abstract():
    assert not inspect.isabstract(vcml::ConfigurationProfileEntry)


def test_vcml::configurationprofileentry_constructor_exists():
    assert callable(vcml::ConfigurationProfileEntry.__init__)


def test_vcml::configurationprofileentry_constructor_args():
    sig = inspect.signature(vcml::ConfigurationProfileEntry.__init__)
    params = list(sig.parameters.keys())
    assert "sequence" in params, "Missing parameter 'sequence'"

def test_vcml::configurationprofileentry_has_sequence():
    assert hasattr(vcml::ConfigurationProfileEntry, "sequence")
    descriptor = None
    for klass in vcml::ConfigurationProfileEntry.__mro__:
        if "sequence" in klass.__dict__:
            descriptor = klass.__dict__["sequence"]
            break
    assert isinstance(descriptor, property)



def test_vcml::bomitem_is_not_abstract():
    assert not inspect.isabstract(vcml::BOMItem)


def test_vcml::bomitem_constructor_exists():
    assert callable(vcml::BOMItem.__init__)


def test_vcml::bomitem_constructor_args():
    sig = inspect.signature(vcml::BOMItem.__init__)
    params = list(sig.parameters.keys())
    assert "itemnumber" in params, "Missing parameter 'itemnumber'"

def test_vcml::bomitem_has_itemnumber():
    assert hasattr(vcml::BOMItem, "itemnumber")
    descriptor = None
    for klass in vcml::BOMItem.__mro__:
        if "itemnumber" in klass.__dict__:
            descriptor = klass.__dict__["itemnumber"]
            break
    assert isinstance(descriptor, property)



def test_vcobject_is_not_abstract():
    assert not inspect.isabstract(VCObject)


def test_vcobject_constructor_exists():
    assert callable(VCObject.__init__)


def test_vcobject_constructor_args():
    sig = inspect.signature(VCObject.__init__)
    params = list(sig.parameters.keys())



def test_vcml::precondition_is_not_abstract():
    assert not inspect.isabstract(vcml::Precondition)


def test_vcml::precondition_constructor_exists():
    assert callable(vcml::Precondition.__init__)


def test_vcml::precondition_constructor_args():
    sig = inspect.signature(vcml::Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml::precondition_has_group():
    assert hasattr(vcml::Precondition, "group")
    descriptor = None
    for klass in vcml::Precondition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml::precondition_has_status():
    assert hasattr(vcml::Precondition, "status")
    descriptor = None
    for klass in vcml::Precondition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml::procedure_is_not_abstract():
    assert not inspect.isabstract(vcml::Procedure)


def test_vcml::procedure_constructor_exists():
    assert callable(vcml::Procedure.__init__)


def test_vcml::procedure_constructor_args():
    sig = inspect.signature(vcml::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml::procedure_has_status():
    assert hasattr(vcml::Procedure, "status")
    descriptor = None
    for klass in vcml::Procedure.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::procedure_has_group():
    assert hasattr(vcml::Procedure, "group")
    descriptor = None
    for klass in vcml::Procedure.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml::constraint_is_not_abstract():
    assert not inspect.isabstract(vcml::Constraint)


def test_vcml::constraint_constructor_exists():
    assert callable(vcml::Constraint.__init__)


def test_vcml::constraint_constructor_args():
    sig = inspect.signature(vcml::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml::constraint_has_status():
    assert hasattr(vcml::Constraint, "status")
    descriptor = None
    for klass in vcml::Constraint.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::constraint_has_group():
    assert hasattr(vcml::Constraint, "group")
    descriptor = None
    for klass in vcml::Constraint.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml::configurationprofile_is_not_abstract():
    assert not inspect.isabstract(vcml::ConfigurationProfile)


def test_vcml::configurationprofile_constructor_exists():
    assert callable(vcml::ConfigurationProfile.__init__)


def test_vcml::configurationprofile_constructor_args():
    sig = inspect.signature(vcml::ConfigurationProfile.__init__)
    params = list(sig.parameters.keys())
    assert "fixing" in params, "Missing parameter 'fixing'"
    assert "status" in params, "Missing parameter 'status'"
    assert "bomapplication" in params, "Missing parameter 'bomapplication'"

def test_vcml::configurationprofile_has_fixing():
    assert hasattr(vcml::ConfigurationProfile, "fixing")
    descriptor = None
    for klass in vcml::ConfigurationProfile.__mro__:
        if "fixing" in klass.__dict__:
            descriptor = klass.__dict__["fixing"]
            break
    assert isinstance(descriptor, property)

def test_vcml::configurationprofile_has_status():
    assert hasattr(vcml::ConfigurationProfile, "status")
    descriptor = None
    for klass in vcml::ConfigurationProfile.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::configurationprofile_has_bomapplication():
    assert hasattr(vcml::ConfigurationProfile, "bomapplication")
    descriptor = None
    for klass in vcml::ConfigurationProfile.__mro__:
        if "bomapplication" in klass.__dict__:
            descriptor = klass.__dict__["bomapplication"]
            break
    assert isinstance(descriptor, property)



def test_vcml::varianttablecontent_is_not_abstract():
    assert not inspect.isabstract(vcml::VariantTableContent)


def test_vcml::varianttablecontent_constructor_exists():
    assert callable(vcml::VariantTableContent.__init__)


def test_vcml::varianttablecontent_constructor_args():
    sig = inspect.signature(vcml::VariantTableContent.__init__)
    params = list(sig.parameters.keys())



def test_vcml::class_is_not_abstract():
    assert not inspect.isabstract(vcml::Class)


def test_vcml::class_constructor_exists():
    assert callable(vcml::Class.__init__)


def test_vcml::class_constructor_args():
    sig = inspect.signature(vcml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml::class_has_group():
    assert hasattr(vcml::Class, "group")
    descriptor = None
    for klass in vcml::Class.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml::class_has_status():
    assert hasattr(vcml::Class, "status")
    descriptor = None
    for klass in vcml::Class.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml::varianttable_is_not_abstract():
    assert not inspect.isabstract(vcml::VariantTable)


def test_vcml::varianttable_constructor_exists():
    assert callable(vcml::VariantTable.__init__)


def test_vcml::varianttable_constructor_args():
    sig = inspect.signature(vcml::VariantTable.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml::varianttable_has_status():
    assert hasattr(vcml::VariantTable, "status")
    descriptor = None
    for klass in vcml::VariantTable.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::varianttable_has_group():
    assert hasattr(vcml::VariantTable, "group")
    descriptor = None
    for klass in vcml::VariantTable.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml::interfacedesign_is_not_abstract():
    assert not inspect.isabstract(vcml::InterfaceDesign)


def test_vcml::interfacedesign_constructor_exists():
    assert callable(vcml::InterfaceDesign.__init__)


def test_vcml::interfacedesign_constructor_args():
    sig = inspect.signature(vcml::InterfaceDesign.__init__)
    params = list(sig.parameters.keys())



def test_vcml::variantfunction_is_not_abstract():
    assert not inspect.isabstract(vcml::VariantFunction)


def test_vcml::variantfunction_constructor_exists():
    assert callable(vcml::VariantFunction.__init__)


def test_vcml::variantfunction_constructor_args():
    sig = inspect.signature(vcml::VariantFunction.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml::variantfunction_has_status():
    assert hasattr(vcml::VariantFunction, "status")
    descriptor = None
    for klass in vcml::VariantFunction.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::variantfunction_has_group():
    assert hasattr(vcml::VariantFunction, "group")
    descriptor = None
    for klass in vcml::VariantFunction.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml::material_is_not_abstract():
    assert not inspect.isabstract(vcml::Material)


def test_vcml::material_constructor_exists():
    assert callable(vcml::Material.__init__)


def test_vcml::material_constructor_args():
    sig = inspect.signature(vcml::Material.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_vcml::material_has_type():
    assert hasattr(vcml::Material, "type")
    descriptor = None
    for klass in vcml::Material.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_vcml::characteristic_is_not_abstract():
    assert not inspect.isabstract(vcml::Characteristic)


def test_vcml::characteristic_constructor_exists():
    assert callable(vcml::Characteristic.__init__)


def test_vcml::characteristic_constructor_args():
    sig = inspect.signature(vcml::Characteristic.__init__)
    params = list(sig.parameters.keys())
    assert "displayAllowedValues" in params, "Missing parameter 'displayAllowedValues'"
    assert "field" in params, "Missing parameter 'field'"
    assert "table" in params, "Missing parameter 'table'"
    assert "additionalValues" in params, "Missing parameter 'additionalValues'"
    assert "noDisplay" in params, "Missing parameter 'noDisplay'"
    assert "multiValue" in params, "Missing parameter 'multiValue'"
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"
    assert "required" in params, "Missing parameter 'required'"
    assert "notReadyForInput" in params, "Missing parameter 'notReadyForInput'"
    assert "restrictable" in params, "Missing parameter 'restrictable'"

def test_vcml::characteristic_has_displayAllowedValues():
    assert hasattr(vcml::Characteristic, "displayAllowedValues")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "displayAllowedValues" in klass.__dict__:
            descriptor = klass.__dict__["displayAllowedValues"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_field():
    assert hasattr(vcml::Characteristic, "field")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_table():
    assert hasattr(vcml::Characteristic, "table")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_additionalValues():
    assert hasattr(vcml::Characteristic, "additionalValues")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "additionalValues" in klass.__dict__:
            descriptor = klass.__dict__["additionalValues"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_noDisplay():
    assert hasattr(vcml::Characteristic, "noDisplay")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "noDisplay" in klass.__dict__:
            descriptor = klass.__dict__["noDisplay"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_multiValue():
    assert hasattr(vcml::Characteristic, "multiValue")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "multiValue" in klass.__dict__:
            descriptor = klass.__dict__["multiValue"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_group():
    assert hasattr(vcml::Characteristic, "group")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_status():
    assert hasattr(vcml::Characteristic, "status")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_required():
    assert hasattr(vcml::Characteristic, "required")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_notReadyForInput():
    assert hasattr(vcml::Characteristic, "notReadyForInput")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "notReadyForInput" in klass.__dict__:
            descriptor = klass.__dict__["notReadyForInput"]
            break
    assert isinstance(descriptor, property)

def test_vcml::characteristic_has_restrictable():
    assert hasattr(vcml::Characteristic, "restrictable")
    descriptor = None
    for klass in vcml::Characteristic.__mro__:
        if "restrictable" in klass.__dict__:
            descriptor = klass.__dict__["restrictable"]
            break
    assert isinstance(descriptor, property)



def test_vcml::dependencynet_is_not_abstract():
    assert not inspect.isabstract(vcml::DependencyNet)


def test_vcml::dependencynet_constructor_exists():
    assert callable(vcml::DependencyNet.__init__)


def test_vcml::dependencynet_constructor_args():
    sig = inspect.signature(vcml::DependencyNet.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml::dependencynet_has_group():
    assert hasattr(vcml::DependencyNet, "group")
    descriptor = None
    for klass in vcml::DependencyNet.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml::dependencynet_has_status():
    assert hasattr(vcml::DependencyNet, "status")
    descriptor = None
    for klass in vcml::DependencyNet.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml::selectioncondition_is_not_abstract():
    assert not inspect.isabstract(vcml::SelectionCondition)


def test_vcml::selectioncondition_constructor_exists():
    assert callable(vcml::SelectionCondition.__init__)


def test_vcml::selectioncondition_constructor_args():
    sig = inspect.signature(vcml::SelectionCondition.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml::selectioncondition_has_status():
    assert hasattr(vcml::SelectionCondition, "status")
    descriptor = None
    for klass in vcml::SelectionCondition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml::selectioncondition_has_group():
    assert hasattr(vcml::SelectionCondition, "group")
    descriptor = None
    for klass in vcml::SelectionCondition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml::billofmaterial_is_not_abstract():
    assert not inspect.isabstract(vcml::BillOfMaterial)


def test_vcml::billofmaterial_constructor_exists():
    assert callable(vcml::BillOfMaterial.__init__)


def test_vcml::billofmaterial_constructor_args():
    sig = inspect.signature(vcml::BillOfMaterial.__init__)
    params = list(sig.parameters.keys())



def test_vcml::description_is_not_abstract():
    assert not inspect.isabstract(vcml::Description)


def test_vcml::description_constructor_exists():
    assert callable(vcml::Description.__init__)


def test_vcml::description_constructor_args():
    sig = inspect.signature(vcml::Description.__init__)
    params = list(sig.parameters.keys())



def test_characteristictype_is_not_abstract():
    assert not inspect.isabstract(CharacteristicType)


def test_characteristictype_constructor_exists():
    assert callable(CharacteristicType.__init__)


def test_characteristictype_constructor_args():
    sig = inspect.signature(CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_vcml::symbolictype_is_not_abstract():
    assert not inspect.isabstract(vcml::SymbolicType)


def test_vcml::symbolictype_constructor_exists():
    assert callable(vcml::SymbolicType.__init__)


def test_vcml::symbolictype_constructor_args():
    sig = inspect.signature(vcml::SymbolicType.__init__)
    params = list(sig.parameters.keys())
    assert "caseSensitive" in params, "Missing parameter 'caseSensitive'"

def test_vcml::symbolictype_has_caseSensitive():
    assert hasattr(vcml::SymbolicType, "caseSensitive")
    descriptor = None
    for klass in vcml::SymbolicType.__mro__:
        if "caseSensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseSensitive"]
            break
    assert isinstance(descriptor, property)



def test_vcml::datetype_is_not_abstract():
    assert not inspect.isabstract(vcml::DateType)


def test_vcml::datetype_constructor_exists():
    assert callable(vcml::DateType.__init__)


def test_vcml::datetype_constructor_args():
    sig = inspect.signature(vcml::DateType.__init__)
    params = list(sig.parameters.keys())
    assert "intervalValuesAllowed" in params, "Missing parameter 'intervalValuesAllowed'"

def test_vcml::datetype_has_intervalValuesAllowed():
    assert hasattr(vcml::DateType, "intervalValuesAllowed")
    descriptor = None
    for klass in vcml::DateType.__mro__:
        if "intervalValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["intervalValuesAllowed"]
            break
    assert isinstance(descriptor, property)



def test_vcml::numerictype_is_not_abstract():
    assert not inspect.isabstract(vcml::NumericType)


def test_vcml::numerictype_constructor_exists():
    assert callable(vcml::NumericType.__init__)


def test_vcml::numerictype_constructor_args():
    sig = inspect.signature(vcml::NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "decimalPlaces" in params, "Missing parameter 'decimalPlaces'"
    assert "intervalValuesAllowed" in params, "Missing parameter 'intervalValuesAllowed'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "negativeValuesAllowed" in params, "Missing parameter 'negativeValuesAllowed'"

def test_vcml::numerictype_has_decimalPlaces():
    assert hasattr(vcml::NumericType, "decimalPlaces")
    descriptor = None
    for klass in vcml::NumericType.__mro__:
        if "decimalPlaces" in klass.__dict__:
            descriptor = klass.__dict__["decimalPlaces"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numerictype_has_intervalValuesAllowed():
    assert hasattr(vcml::NumericType, "intervalValuesAllowed")
    descriptor = None
    for klass in vcml::NumericType.__mro__:
        if "intervalValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["intervalValuesAllowed"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numerictype_has_unit():
    assert hasattr(vcml::NumericType, "unit")
    descriptor = None
    for klass in vcml::NumericType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numerictype_has_negativeValuesAllowed():
    assert hasattr(vcml::NumericType, "negativeValuesAllowed")
    descriptor = None
    for klass in vcml::NumericType.__mro__:
        if "negativeValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["negativeValuesAllowed"]
            break
    assert isinstance(descriptor, property)



def test_vcml::vcobject_is_not_abstract():
    assert not inspect.isabstract(vcml::VCObject)


def test_vcml::vcobject_constructor_exists():
    assert callable(vcml::VCObject.__init__)


def test_vcml::vcobject_constructor_args():
    sig = inspect.signature(vcml::VCObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::vcobject_has_name():
    assert hasattr(vcml::VCObject, "name")
    descriptor = None
    for klass in vcml::VCObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::option_is_not_abstract():
    assert not inspect.isabstract(vcml::Option)


def test_vcml::option_constructor_exists():
    assert callable(vcml::Option.__init__)


def test_vcml::option_constructor_args():
    sig = inspect.signature(vcml::Option.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_vcml::option_has_value():
    assert hasattr(vcml::Option, "value")
    descriptor = None
    for klass in vcml::Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml::option_has_name():
    assert hasattr(vcml::Option, "name")
    descriptor = None
    for klass in vcml::Option.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml::import_is_not_abstract():
    assert not inspect.isabstract(vcml::Import)


def test_vcml::import_constructor_exists():
    assert callable(vcml::Import.__init__)


def test_vcml::import_constructor_args():
    sig = inspect.signature(vcml::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_vcml::import_has_importURI():
    assert hasattr(vcml::Import, "importURI")
    descriptor = None
    for klass in vcml::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_vcml::vcmlmodel_is_not_abstract():
    assert not inspect.isabstract(vcml::VcmlModel)


def test_vcml::vcmlmodel_constructor_exists():
    assert callable(vcml::VcmlModel.__init__)


def test_vcml::vcmlmodel_constructor_args():
    sig = inspect.signature(vcml::VcmlModel.__init__)
    params = list(sig.parameters.keys())



def test_vcml::binarycondition_is_not_abstract():
    assert not inspect.isabstract(vcml::BinaryCondition)


def test_vcml::binarycondition_constructor_exists():
    assert callable(vcml::BinaryCondition.__init__)


def test_vcml::binarycondition_constructor_args():
    sig = inspect.signature(vcml::BinaryCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml::binarycondition_has_operator():
    assert hasattr(vcml::BinaryCondition, "operator")
    descriptor = None
    for klass in vcml::BinaryCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml::conditionalconstraintrestriction_is_not_abstract():
    assert not inspect.isabstract(vcml::ConditionalConstraintRestriction)


def test_vcml::conditionalconstraintrestriction_constructor_exists():
    assert callable(vcml::ConditionalConstraintRestriction.__init__)


def test_vcml::conditionalconstraintrestriction_constructor_args():
    sig = inspect.signature(vcml::ConditionalConstraintRestriction.__init__)
    params = list(sig.parameters.keys())



def test_list_is_not_abstract():
    assert not inspect.isabstract(List)


def test_list_constructor_exists():
    assert callable(List.__init__)


def test_list_constructor_args():
    sig = inspect.signature(List.__init__)
    params = list(sig.parameters.keys())



def test_vcml::symbollist_is_not_abstract():
    assert not inspect.isabstract(vcml::SymbolList)


def test_vcml::symbollist_constructor_exists():
    assert callable(vcml::SymbolList.__init__)


def test_vcml::symbollist_constructor_args():
    sig = inspect.signature(vcml::SymbolList.__init__)
    params = list(sig.parameters.keys())



def test_vcml::numberlist_is_not_abstract():
    assert not inspect.isabstract(vcml::NumberList)


def test_vcml::numberlist_constructor_exists():
    assert callable(vcml::NumberList.__init__)


def test_vcml::numberlist_constructor_args():
    sig = inspect.signature(vcml::NumberList.__init__)
    params = list(sig.parameters.keys())



def test_vcml::incondition::p_is_not_abstract():
    assert not inspect.isabstract(vcml::InCondition::P)


def test_vcml::incondition::p_constructor_exists():
    assert callable(vcml::InCondition::P.__init__)


def test_vcml::incondition::p_constructor_args():
    sig = inspect.signature(vcml::InCondition::P.__init__)
    params = list(sig.parameters.keys())



def test_vcml::list_is_not_abstract():
    assert not inspect.isabstract(vcml::List)


def test_vcml::list_constructor_exists():
    assert callable(vcml::List.__init__)


def test_vcml::list_constructor_args():
    sig = inspect.signature(vcml::List.__init__)
    params = list(sig.parameters.keys())



def test_vcml::incondition::c_is_not_abstract():
    assert not inspect.isabstract(vcml::InCondition::C)


def test_vcml::incondition::c_constructor_exists():
    assert callable(vcml::InCondition::C.__init__)


def test_vcml::incondition::c_constructor_args():
    sig = inspect.signature(vcml::InCondition::C.__init__)
    params = list(sig.parameters.keys())



def test_vcml::isspecified::p_is_not_abstract():
    assert not inspect.isabstract(vcml::IsSpecified::P)


def test_vcml::isspecified::p_constructor_exists():
    assert callable(vcml::IsSpecified::P.__init__)


def test_vcml::isspecified::p_constructor_args():
    sig = inspect.signature(vcml::IsSpecified::P.__init__)
    params = list(sig.parameters.keys())



def test_vcml::isspecified::c_is_not_abstract():
    assert not inspect.isabstract(vcml::IsSpecified::C)


def test_vcml::isspecified::c_constructor_exists():
    assert callable(vcml::IsSpecified::C.__init__)


def test_vcml::isspecified::c_constructor_args():
    sig = inspect.signature(vcml::IsSpecified::C.__init__)
    params = list(sig.parameters.keys())



def test_vcml::comparison_is_not_abstract():
    assert not inspect.isabstract(vcml::Comparison)


def test_vcml::comparison_constructor_exists():
    assert callable(vcml::Comparison.__init__)


def test_vcml::comparison_constructor_args():
    sig = inspect.signature(vcml::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml::comparison_has_operator():
    assert hasattr(vcml::Comparison, "operator")
    descriptor = None
    for klass in vcml::Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml::unarycondition_is_not_abstract():
    assert not inspect.isabstract(vcml::UnaryCondition)


def test_vcml::unarycondition_constructor_exists():
    assert callable(vcml::UnaryCondition.__init__)


def test_vcml::unarycondition_constructor_args():
    sig = inspect.signature(vcml::UnaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml::symbolicliteral_is_not_abstract():
    assert not inspect.isabstract(vcml::SymbolicLiteral)


def test_vcml::symbolicliteral_constructor_exists():
    assert callable(vcml::SymbolicLiteral.__init__)


def test_vcml::symbolicliteral_constructor_args():
    sig = inspect.signature(vcml::SymbolicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml::symbolicliteral_has_value():
    assert hasattr(vcml::SymbolicLiteral, "value")
    descriptor = None
    for klass in vcml::SymbolicLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numberlistentry_is_not_abstract():
    assert not inspect.isabstract(NumberListEntry)


def test_numberlistentry_constructor_exists():
    assert callable(NumberListEntry.__init__)


def test_numberlistentry_constructor_args():
    sig = inspect.signature(NumberListEntry.__init__)
    params = list(sig.parameters.keys())



def test_vcml::numericinterval_is_not_abstract():
    assert not inspect.isabstract(vcml::NumericInterval)


def test_vcml::numericinterval_constructor_exists():
    assert callable(vcml::NumericInterval.__init__)


def test_vcml::numericinterval_constructor_args():
    sig = inspect.signature(vcml::NumericInterval.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBoundOp" in params, "Missing parameter 'lowerBoundOp'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBoundOp" in params, "Missing parameter 'upperBoundOp'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_vcml::numericinterval_has_lowerBoundOp():
    assert hasattr(vcml::NumericInterval, "lowerBoundOp")
    descriptor = None
    for klass in vcml::NumericInterval.__mro__:
        if "lowerBoundOp" in klass.__dict__:
            descriptor = klass.__dict__["lowerBoundOp"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numericinterval_has_lowerBound():
    assert hasattr(vcml::NumericInterval, "lowerBound")
    descriptor = None
    for klass in vcml::NumericInterval.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numericinterval_has_upperBoundOp():
    assert hasattr(vcml::NumericInterval, "upperBoundOp")
    descriptor = None
    for klass in vcml::NumericInterval.__mro__:
        if "upperBoundOp" in klass.__dict__:
            descriptor = klass.__dict__["upperBoundOp"]
            break
    assert isinstance(descriptor, property)

def test_vcml::numericinterval_has_upperBound():
    assert hasattr(vcml::NumericInterval, "upperBound")
    descriptor = None
    for klass in vcml::NumericInterval.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_vcml::numericliteral_is_not_abstract():
    assert not inspect.isabstract(vcml::NumericLiteral)


def test_vcml::numericliteral_constructor_exists():
    assert callable(vcml::NumericLiteral.__init__)


def test_vcml::numericliteral_constructor_args():
    sig = inspect.signature(vcml::NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml::numericliteral_has_value():
    assert hasattr(vcml::NumericLiteral, "value")
    descriptor = None
    for klass in vcml::NumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml::mdatacharacteristic::p_is_not_abstract():
    assert not inspect.isabstract(vcml::MDataCharacteristic::P)


def test_vcml::mdatacharacteristic::p_constructor_exists():
    assert callable(vcml::MDataCharacteristic::P.__init__)


def test_vcml::mdatacharacteristic::p_constructor_args():
    sig = inspect.signature(vcml::MDataCharacteristic::P.__init__)
    params = list(sig.parameters.keys())



def test_vcml::mdatacharacteristic::c_is_not_abstract():
    assert not inspect.isabstract(vcml::MDataCharacteristic::C)


def test_vcml::mdatacharacteristic::c_constructor_exists():
    assert callable(vcml::MDataCharacteristic::C.__init__)


def test_vcml::mdatacharacteristic::c_constructor_args():
    sig = inspect.signature(vcml::MDataCharacteristic::C.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vcml::countparts_is_not_abstract():
    assert not inspect.isabstract(vcml::CountParts)


def test_vcml::countparts_constructor_exists():
    assert callable(vcml::CountParts.__init__)


def test_vcml::countparts_constructor_args():
    sig = inspect.signature(vcml::CountParts.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml::countparts_has_location():
    assert hasattr(vcml::CountParts, "location")
    descriptor = None
    for klass in vcml::CountParts.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml::sumparts_is_not_abstract():
    assert not inspect.isabstract(vcml::SumParts)


def test_vcml::sumparts_constructor_exists():
    assert callable(vcml::SumParts.__init__)


def test_vcml::sumparts_constructor_args():
    sig = inspect.signature(vcml::SumParts.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml::sumparts_has_location():
    assert hasattr(vcml::SumParts, "location")
    descriptor = None
    for klass in vcml::SumParts.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml::functioncall_is_not_abstract():
    assert not inspect.isabstract(vcml::FunctionCall)


def test_vcml::functioncall_constructor_exists():
    assert callable(vcml::FunctionCall.__init__)


def test_vcml::functioncall_constructor_args():
    sig = inspect.signature(vcml::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_vcml::functioncall_has_function():
    assert hasattr(vcml::FunctionCall, "function")
    descriptor = None
    for klass in vcml::FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_vcml::literal_is_not_abstract():
    assert not inspect.isabstract(vcml::Literal)


def test_vcml::literal_constructor_exists():
    assert callable(vcml::Literal.__init__)


def test_vcml::literal_constructor_args():
    sig = inspect.signature(vcml::Literal.__init__)
    params = list(sig.parameters.keys())



def test_vcml::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(vcml::BinaryExpression)


def test_vcml::binaryexpression_constructor_exists():
    assert callable(vcml::BinaryExpression.__init__)


def test_vcml::binaryexpression_constructor_args():
    sig = inspect.signature(vcml::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml::binaryexpression_has_operator():
    assert hasattr(vcml::BinaryExpression, "operator")
    descriptor = None
    for klass in vcml::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(vcml::UnaryExpression)


def test_vcml::unaryexpression_constructor_exists():
    assert callable(vcml::UnaryExpression.__init__)


def test_vcml::unaryexpression_constructor_args():
    sig = inspect.signature(vcml::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml::unaryexpression_has_operator():
    assert hasattr(vcml::UnaryExpression, "operator")
    descriptor = None
    for klass in vcml::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml::typeof_is_not_abstract():
    assert not inspect.isabstract(vcml::TypeOf)


def test_vcml::typeof_constructor_exists():
    assert callable(vcml::TypeOf.__init__)


def test_vcml::typeof_constructor_args():
    sig = inspect.signature(vcml::TypeOf.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml::typeof_has_location():
    assert hasattr(vcml::TypeOf, "location")
    descriptor = None
    for klass in vcml::TypeOf.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_setordeldefault_is_not_abstract():
    assert not inspect.isabstract(SetOrDelDefault)


def test_setordeldefault_constructor_exists():
    assert callable(SetOrDelDefault.__init__)


def test_setordeldefault_constructor_args():
    sig = inspect.signature(SetOrDelDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml::deldefault_is_not_abstract():
    assert not inspect.isabstract(vcml::DelDefault)


def test_vcml::deldefault_constructor_exists():
    assert callable(vcml::DelDefault.__init__)


def test_vcml::deldefault_constructor_args():
    sig = inspect.signature(vcml::DelDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml::setdefault_is_not_abstract():
    assert not inspect.isabstract(vcml::SetDefault)


def test_vcml::setdefault_constructor_exists():
    assert callable(vcml::SetDefault.__init__)


def test_vcml::setdefault_constructor_args():
    sig = inspect.signature(vcml::SetDefault.__init__)
    params = list(sig.parameters.keys())



def test_functionortable_is_not_abstract():
    assert not inspect.isabstract(FunctionOrTable)


def test_functionortable_constructor_exists():
    assert callable(FunctionOrTable.__init__)


def test_functionortable_constructor_args():
    sig = inspect.signature(FunctionOrTable.__init__)
    params = list(sig.parameters.keys())



def test_vcml::characteristicreference::p_is_not_abstract():
    assert not inspect.isabstract(vcml::CharacteristicReference::P)


def test_vcml::characteristicreference::p_constructor_exists():
    assert callable(vcml::CharacteristicReference::P.__init__)


def test_vcml::characteristicreference::p_constructor_args():
    sig = inspect.signature(vcml::CharacteristicReference::P.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml::characteristicreference::p_has_location():
    assert hasattr(vcml::CharacteristicReference::P, "location")
    descriptor = None
    for klass in vcml::CharacteristicReference::P.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml::isinvisible_is_not_abstract():
    assert not inspect.isabstract(vcml::IsInvisible)


def test_vcml::isinvisible_constructor_exists():
    assert callable(vcml::IsInvisible.__init__)


def test_vcml::isinvisible_constructor_args():
    sig = inspect.signature(vcml::IsInvisible.__init__)
    params = list(sig.parameters.keys())



def test_vcml::table_is_not_abstract():
    assert not inspect.isabstract(vcml::Table)


def test_vcml::table_constructor_exists():
    assert callable(vcml::Table.__init__)


def test_vcml::table_constructor_args():
    sig = inspect.signature(vcml::Table.__init__)
    params = list(sig.parameters.keys())



def test_vcml::function_is_not_abstract():
    assert not inspect.isabstract(vcml::Function)


def test_vcml::function_constructor_exists():
    assert callable(vcml::Function.__init__)


def test_vcml::function_constructor_args():
    sig = inspect.signature(vcml::Function.__init__)
    params = list(sig.parameters.keys())



def test_vcml::setpricingfactor_is_not_abstract():
    assert not inspect.isabstract(vcml::SetPricingFactor)


def test_vcml::setpricingfactor_constructor_exists():
    assert callable(vcml::SetPricingFactor.__init__)


def test_vcml::setpricingfactor_constructor_args():
    sig = inspect.signature(vcml::SetPricingFactor.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml::setpricingfactor_has_location():
    assert hasattr(vcml::SetPricingFactor, "location")
    descriptor = None
    for klass in vcml::SetPricingFactor.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml::setordeldefault_is_not_abstract():
    assert not inspect.isabstract(vcml::SetOrDelDefault)


def test_vcml::setordeldefault_constructor_exists():
    assert callable(vcml::SetOrDelDefault.__init__)


def test_vcml::setordeldefault_constructor_args():
    sig = inspect.signature(vcml::SetOrDelDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml::pfunction_is_not_abstract():
    assert not inspect.isabstract(vcml::PFunction)


def test_vcml::pfunction_constructor_exists():
    assert callable(vcml::PFunction.__init__)


def test_vcml::pfunction_constructor_args():
    sig = inspect.signature(vcml::PFunction.__init__)
    params = list(sig.parameters.keys())



def test_vcml::assignment_is_not_abstract():
    assert not inspect.isabstract(vcml::Assignment)


def test_vcml::assignment_constructor_exists():
    assert callable(vcml::Assignment.__init__)


def test_vcml::assignment_constructor_args():
    sig = inspect.signature(vcml::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_vcml::simplestatement_is_not_abstract():
    assert not inspect.isabstract(vcml::SimpleStatement)


def test_vcml::simplestatement_constructor_exists():
    assert callable(vcml::SimpleStatement.__init__)


def test_vcml::simplestatement_constructor_args():
    sig = inspect.signature(vcml::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml::conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(vcml::ConditionalStatement)


def test_vcml::conditionalstatement_constructor_exists():
    assert callable(vcml::ConditionalStatement.__init__)


def test_vcml::conditionalstatement_constructor_args():
    sig = inspect.signature(vcml::ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml::compoundstatement_is_not_abstract():
    assert not inspect.isabstract(vcml::CompoundStatement)


def test_vcml::compoundstatement_constructor_exists():
    assert callable(vcml::CompoundStatement.__init__)


def test_vcml::compoundstatement_constructor_args():
    sig = inspect.signature(vcml::CompoundStatement.__init__)
    params = list(sig.parameters.keys())

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "InPreparation",
        "Released",
        "Locked",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_procedurelocation_exists():
    # Check that the Enumeration exists
    assert ProcedureLocation is not None

def test_procedurelocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureLocation]
    expected_literals = [
        "SELF",
        "ROOT",
        "PARENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureLocation"

def test_fixing_exists():
    # Check that the Enumeration exists
    assert Fixing is not None

def test_fixing_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Fixing]
    expected_literals = [
        "Entry",
        "TopDown",
        "None_",
        "BottomUp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Fixing"

def test_unaryexpressionoperator_exists():
    # Check that the Enumeration exists
    assert UnaryExpressionOperator is not None

def test_unaryexpressionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryExpressionOperator]
    expected_literals = [
        "MINUS",
        "LC",
        "PLUS",
        "UC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryExpressionOperator"

def test_optiontype_exists():
    # Check that the Enumeration exists
    assert OptionType is not None

def test_optiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptionType]
    expected_literals = [
        "KeyDate",
        "ECM",
        "UPS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptionType"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "NE",
        "EQ",
        "LT",
        "GT",
        "GE",
        "LE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_functionname_exists():
    # Check that the Enumeration exists
    assert FunctionName is not None

def test_functionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionName]
    expected_literals = [
        "ARCSIN",
        "FRAC",
        "LOG10",
        "CEIL",
        "ARCTAN",
        "TAN",
        "ABS",
        "TRUNK",
        "SIN",
        "ARCCOS",
        "FLOOR",
        "EXP",
        "SQRT",
        "COS",
        "SIGN",
        "LN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionName"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "SH",
        "HR",
        "ZF",
        "ID",
        "AF",
        "LT",
        "FR",
        "UK",
        "SV",
        "FI",
        "PL",
        "TH",
        "EL",
        "NO",
        "JA",
        "BG",
        "MS",
        "RU",
        "ET",
        "NL",
        "RO",
        "SL",
        "HU",
        "EN",
        "PT",
        "IT",
        "DA",
        "CA",
        "KO",
        "AR",
        "ZH",
        "LV",
        "Z1",
        "IS",
        "CS",
        "TR",
        "SR",
        "ES",
        "SK",
        "HE",
        "DE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
vcml::Statement_strategy = st.builds(
    vcml::Statement,
)
CharacteristicReference::C_strategy = st.builds(
    CharacteristicReference::C,
)
vcml::ShortVarReference_strategy = st.builds(
    vcml::ShortVarReference,
)
vcml::ObjectCharacteristicReference_strategy = st.builds(
    vcml::ObjectCharacteristicReference,
)
Literal_strategy = st.builds(
    Literal,
)
vcml::EObject_strategy = st.builds(
    vcml::EObject,
)
Condition_strategy = st.builds(
    Condition,
)
ConstraintRestriction_strategy = st.builds(
    ConstraintRestriction,
)
vcml::ConstraintRestrictionFalse_strategy = st.builds(
    vcml::ConstraintRestrictionFalse,
)
vcml::SubpartOfCondition_strategy = st.builds(
    vcml::SubpartOfCondition,
)
vcml::NegatedConstraintRestrictionLHS_strategy = st.builds(
    vcml::NegatedConstraintRestrictionLHS,
)
vcml::PartOfCondition_strategy = st.builds(
    vcml::PartOfCondition,
)
vcml::PartialKey_strategy = st.builds(
    vcml::PartialKey,
    key=
        safe_text
)
vcml::FunctionOrTable_strategy = st.builds(
    vcml::FunctionOrTable,
)
vcml::Expression_strategy = st.builds(
    vcml::Expression,
)
ConstraintObject_strategy = st.builds(
    ConstraintObject,
)
vcml::ConstraintClass_strategy = st.builds(
    vcml::ConstraintClass,
)
vcml::ShortVarDefinition_strategy = st.builds(
    vcml::ShortVarDefinition,
    name=
        safe_text
)
vcml::CharacteristicReference::C_strategy = st.builds(
    vcml::CharacteristicReference::C,
)
vcml::ConstraintRestriction_strategy = st.builds(
    vcml::ConstraintRestriction,
)
vcml::ConstraintObject_strategy = st.builds(
    vcml::ConstraintObject,
    name=
        safe_text
)
vcml::FormattedDocumentationBlock_strategy = st.builds(
    vcml::FormattedDocumentationBlock,
    value=
        safe_text,
    format=
        safe_text
)
vcml::MultipleLanguageDocumentation::LanguageBlock_strategy = st.builds(
    vcml::MultipleLanguageDocumentation::LanguageBlock,
    language=
        safe_text
)
Documentation_strategy = st.builds(
    Documentation,
)
vcml::MultipleLanguageDocumentation_strategy = st.builds(
    vcml::MultipleLanguageDocumentation,
)
vcml::SimpleDocumentation_strategy = st.builds(
    vcml::SimpleDocumentation,
    value=
        safe_text
)
vcml::ObjectType_strategy = st.builds(
    vcml::ObjectType,
    type=
        safe_text,
    classType=
        st.integers()
)
vcml::ConstraintMaterial_strategy = st.builds(
    vcml::ConstraintMaterial,
)
vcml::MultiLanguageDescription_strategy = st.builds(
    vcml::MultiLanguageDescription,
    value=
        safe_text,
    language=
        safe_text
)
Description_strategy = st.builds(
    Description,
)
vcml::MultiLanguageDescriptions_strategy = st.builds(
    vcml::MultiLanguageDescriptions,
)
vcml::SimpleDescription_strategy = st.builds(
    vcml::SimpleDescription,
    value=
        safe_text
)
vcml::Row_strategy = st.builds(
    vcml::Row,
)
vcml::VariantTableArgument_strategy = st.builds(
    vcml::VariantTableArgument,
    key=
        st.booleans()
)
vcml::VariantFunctionArgument_strategy = st.builds(
    vcml::VariantFunctionArgument,
    in_=
        st.booleans()
)
vcml::ValueAssignment_strategy = st.builds(
    vcml::ValueAssignment,
)
vcml::Classification_strategy = st.builds(
    vcml::Classification,
)
vcml::CharacteristicGroup_strategy = st.builds(
    vcml::CharacteristicGroup,
    name=
        safe_text
)
vcml::ConstraintSource_strategy = st.builds(
    vcml::ConstraintSource,
)
vcml::Condition_strategy = st.builds(
    vcml::Condition,
)
vcml::ConditionSource_strategy = st.builds(
    vcml::ConditionSource,
)
vcml::ProcedureSource_strategy = st.builds(
    vcml::ProcedureSource,
)
Dependency_strategy = st.builds(
    Dependency,
)
vcml::Dependency_strategy = st.builds(
    vcml::Dependency,
)
vcml::NumberListEntry_strategy = st.builds(
    vcml::NumberListEntry,
)
vcml::DateCharacteristicValue_strategy = st.builds(
    vcml::DateCharacteristicValue,
    default=
        st.booleans(),
    from_=
        safe_text,
    to=
        safe_text
)
vcml::CharacteristicValue_strategy = st.builds(
    vcml::CharacteristicValue,
    default=
        st.booleans(),
    name=
        safe_text
)
vcml::NumericCharacteristicValue_strategy = st.builds(
    vcml::NumericCharacteristicValue,
    default=
        st.booleans()
)
vcml::CharacteristicOrValueDependencies_strategy = st.builds(
    vcml::CharacteristicOrValueDependencies,
)
vcml::CharacteristicType_strategy = st.builds(
    vcml::CharacteristicType,
    numberOfChars=
        st.integers()
)
vcml::Documentation_strategy = st.builds(
    vcml::Documentation,
)
BOMItem_strategy = st.builds(
    BOMItem,
)
vcml::BOMItem::Class_strategy = st.builds(
    vcml::BOMItem::Class,
)
vcml::BOMItem::Material_strategy = st.builds(
    vcml::BOMItem::Material,
)
vcml::ConfigurationProfileEntry_strategy = st.builds(
    vcml::ConfigurationProfileEntry,
    sequence=
        st.integers()
)
vcml::BOMItem_strategy = st.builds(
    vcml::BOMItem,
    itemnumber=
        st.integers()
)
VCObject_strategy = st.builds(
    VCObject,
)
vcml::Precondition_strategy = st.builds(
    vcml::Precondition,
    group=
        safe_text,
    status=
        safe_text
)
vcml::Procedure_strategy = st.builds(
    vcml::Procedure,
    status=
        safe_text,
    group=
        safe_text
)
vcml::Constraint_strategy = st.builds(
    vcml::Constraint,
    status=
        safe_text,
    group=
        safe_text
)
vcml::ConfigurationProfile_strategy = st.builds(
    vcml::ConfigurationProfile,
    fixing=
        safe_text,
    status=
        safe_text,
    bomapplication=
        safe_text
)
vcml::VariantTableContent_strategy = st.builds(
    vcml::VariantTableContent,
)
vcml::Class_strategy = st.builds(
    vcml::Class,
    group=
        safe_text,
    status=
        safe_text
)
vcml::VariantTable_strategy = st.builds(
    vcml::VariantTable,
    status=
        safe_text,
    group=
        safe_text
)
vcml::InterfaceDesign_strategy = st.builds(
    vcml::InterfaceDesign,
)
vcml::VariantFunction_strategy = st.builds(
    vcml::VariantFunction,
    status=
        safe_text,
    group=
        safe_text
)
vcml::Material_strategy = st.builds(
    vcml::Material,
    type=
        safe_text
)
vcml::Characteristic_strategy = st.builds(
    vcml::Characteristic,
    displayAllowedValues=
        st.booleans(),
    field=
        safe_text,
    table=
        safe_text,
    additionalValues=
        st.booleans(),
    noDisplay=
        st.booleans(),
    multiValue=
        st.booleans(),
    group=
        safe_text,
    status=
        safe_text,
    required=
        st.booleans(),
    notReadyForInput=
        st.booleans(),
    restrictable=
        st.booleans()
)
vcml::DependencyNet_strategy = st.builds(
    vcml::DependencyNet,
    group=
        safe_text,
    status=
        safe_text
)
vcml::SelectionCondition_strategy = st.builds(
    vcml::SelectionCondition,
    status=
        safe_text,
    group=
        safe_text
)
vcml::BillOfMaterial_strategy = st.builds(
    vcml::BillOfMaterial,
)
vcml::Description_strategy = st.builds(
    vcml::Description,
)
CharacteristicType_strategy = st.builds(
    CharacteristicType,
)
vcml::SymbolicType_strategy = st.builds(
    vcml::SymbolicType,
    caseSensitive=
        st.booleans()
)
vcml::DateType_strategy = st.builds(
    vcml::DateType,
    intervalValuesAllowed=
        st.booleans()
)
vcml::NumericType_strategy = st.builds(
    vcml::NumericType,
    decimalPlaces=
        st.integers(),
    intervalValuesAllowed=
        st.booleans(),
    unit=
        safe_text,
    negativeValuesAllowed=
        st.booleans()
)
vcml::VCObject_strategy = st.builds(
    vcml::VCObject,
    name=
        safe_text
)
vcml::Option_strategy = st.builds(
    vcml::Option,
    value=
        safe_text,
    name=
        safe_text
)
vcml::Import_strategy = st.builds(
    vcml::Import,
    importURI=
        safe_text
)
vcml::VcmlModel_strategy = st.builds(
    vcml::VcmlModel,
)
vcml::BinaryCondition_strategy = st.builds(
    vcml::BinaryCondition,
    operator=
        safe_text
)
vcml::ConditionalConstraintRestriction_strategy = st.builds(
    vcml::ConditionalConstraintRestriction,
)
List_strategy = st.builds(
    List,
)
vcml::SymbolList_strategy = st.builds(
    vcml::SymbolList,
)
vcml::NumberList_strategy = st.builds(
    vcml::NumberList,
)
vcml::InCondition::P_strategy = st.builds(
    vcml::InCondition::P,
)
vcml::List_strategy = st.builds(
    vcml::List,
)
vcml::InCondition::C_strategy = st.builds(
    vcml::InCondition::C,
)
vcml::IsSpecified::P_strategy = st.builds(
    vcml::IsSpecified::P,
)
vcml::IsSpecified::C_strategy = st.builds(
    vcml::IsSpecified::C,
)
vcml::Comparison_strategy = st.builds(
    vcml::Comparison,
    operator=
        safe_text
)
vcml::UnaryCondition_strategy = st.builds(
    vcml::UnaryCondition,
)
vcml::SymbolicLiteral_strategy = st.builds(
    vcml::SymbolicLiteral,
    value=
        safe_text
)
NumberListEntry_strategy = st.builds(
    NumberListEntry,
)
vcml::NumericInterval_strategy = st.builds(
    vcml::NumericInterval,
    lowerBoundOp=
        safe_text,
    lowerBound=
        safe_text,
    upperBoundOp=
        safe_text,
    upperBound=
        safe_text
)
vcml::NumericLiteral_strategy = st.builds(
    vcml::NumericLiteral,
    value=
        safe_text
)
vcml::MDataCharacteristic::P_strategy = st.builds(
    vcml::MDataCharacteristic::P,
)
vcml::MDataCharacteristic::C_strategy = st.builds(
    vcml::MDataCharacteristic::C,
)
Expression_strategy = st.builds(
    Expression,
)
vcml::CountParts_strategy = st.builds(
    vcml::CountParts,
    location=
        safe_text
)
vcml::SumParts_strategy = st.builds(
    vcml::SumParts,
    location=
        safe_text
)
vcml::FunctionCall_strategy = st.builds(
    vcml::FunctionCall,
    function=
        safe_text
)
vcml::Literal_strategy = st.builds(
    vcml::Literal,
)
vcml::BinaryExpression_strategy = st.builds(
    vcml::BinaryExpression,
    operator=
        safe_text
)
vcml::UnaryExpression_strategy = st.builds(
    vcml::UnaryExpression,
    operator=
        safe_text
)
vcml::TypeOf_strategy = st.builds(
    vcml::TypeOf,
    location=
        safe_text
)
SetOrDelDefault_strategy = st.builds(
    SetOrDelDefault,
)
vcml::DelDefault_strategy = st.builds(
    vcml::DelDefault,
)
vcml::SetDefault_strategy = st.builds(
    vcml::SetDefault,
)
FunctionOrTable_strategy = st.builds(
    FunctionOrTable,
)
vcml::CharacteristicReference::P_strategy = st.builds(
    vcml::CharacteristicReference::P,
    location=
        safe_text
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
vcml::IsInvisible_strategy = st.builds(
    vcml::IsInvisible,
)
vcml::Table_strategy = st.builds(
    vcml::Table,
)
vcml::Function_strategy = st.builds(
    vcml::Function,
)
vcml::SetPricingFactor_strategy = st.builds(
    vcml::SetPricingFactor,
    location=
        safe_text
)
vcml::SetOrDelDefault_strategy = st.builds(
    vcml::SetOrDelDefault,
)
vcml::PFunction_strategy = st.builds(
    vcml::PFunction,
)
vcml::Assignment_strategy = st.builds(
    vcml::Assignment,
)
Statement_strategy = st.builds(
    Statement,
)
vcml::SimpleStatement_strategy = st.builds(
    vcml::SimpleStatement,
)
vcml::ConditionalStatement_strategy = st.builds(
    vcml::ConditionalStatement,
)
vcml::CompoundStatement_strategy = st.builds(
    vcml::CompoundStatement,
)

@given(instance=vcml::Statement_strategy)
@settings(max_examples=50)
def test_vcml::statement_instantiation(instance):
    assert isinstance(instance, vcml::Statement)

@given(instance=CharacteristicReference::C_strategy)
@settings(max_examples=50)
def test_characteristicreference::c_instantiation(instance):
    assert isinstance(instance, CharacteristicReference::C)

@given(instance=vcml::ShortVarReference_strategy)
@settings(max_examples=50)
def test_vcml::shortvarreference_instantiation(instance):
    assert isinstance(instance, vcml::ShortVarReference)

@given(instance=vcml::ObjectCharacteristicReference_strategy)
@settings(max_examples=50)
def test_vcml::objectcharacteristicreference_instantiation(instance):
    assert isinstance(instance, vcml::ObjectCharacteristicReference)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=vcml::EObject_strategy)
@settings(max_examples=50)
def test_vcml::eobject_instantiation(instance):
    assert isinstance(instance, vcml::EObject)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=ConstraintRestriction_strategy)
@settings(max_examples=50)
def test_constraintrestriction_instantiation(instance):
    assert isinstance(instance, ConstraintRestriction)

@given(instance=vcml::ConstraintRestrictionFalse_strategy)
@settings(max_examples=50)
def test_vcml::constraintrestrictionfalse_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintRestrictionFalse)

@given(instance=vcml::SubpartOfCondition_strategy)
@settings(max_examples=50)
def test_vcml::subpartofcondition_instantiation(instance):
    assert isinstance(instance, vcml::SubpartOfCondition)

@given(instance=vcml::NegatedConstraintRestrictionLHS_strategy)
@settings(max_examples=50)
def test_vcml::negatedconstraintrestrictionlhs_instantiation(instance):
    assert isinstance(instance, vcml::NegatedConstraintRestrictionLHS)

@given(instance=vcml::PartOfCondition_strategy)
@settings(max_examples=50)
def test_vcml::partofcondition_instantiation(instance):
    assert isinstance(instance, vcml::PartOfCondition)

@given(instance=vcml::PartialKey_strategy)
@settings(max_examples=50)
def test_vcml::partialkey_instantiation(instance):
    assert isinstance(instance, vcml::PartialKey)

@given(instance=vcml::PartialKey_strategy)
def test_vcml::partialkey_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=vcml::PartialKey_strategy)
def test_vcml::partialkey_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=vcml::FunctionOrTable_strategy)
@settings(max_examples=50)
def test_vcml::functionortable_instantiation(instance):
    assert isinstance(instance, vcml::FunctionOrTable)

@given(instance=vcml::Expression_strategy)
@settings(max_examples=50)
def test_vcml::expression_instantiation(instance):
    assert isinstance(instance, vcml::Expression)

@given(instance=ConstraintObject_strategy)
@settings(max_examples=50)
def test_constraintobject_instantiation(instance):
    assert isinstance(instance, ConstraintObject)

@given(instance=vcml::ConstraintClass_strategy)
@settings(max_examples=50)
def test_vcml::constraintclass_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintClass)

@given(instance=vcml::ShortVarDefinition_strategy)
@settings(max_examples=50)
def test_vcml::shortvardefinition_instantiation(instance):
    assert isinstance(instance, vcml::ShortVarDefinition)

@given(instance=vcml::ShortVarDefinition_strategy)
def test_vcml::shortvardefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::ShortVarDefinition_strategy)
def test_vcml::shortvardefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::CharacteristicReference::C_strategy)
@settings(max_examples=50)
def test_vcml::characteristicreference::c_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicReference::C)

@given(instance=vcml::ConstraintRestriction_strategy)
@settings(max_examples=50)
def test_vcml::constraintrestriction_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintRestriction)

@given(instance=vcml::ConstraintObject_strategy)
@settings(max_examples=50)
def test_vcml::constraintobject_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintObject)

@given(instance=vcml::ConstraintObject_strategy)
def test_vcml::constraintobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::ConstraintObject_strategy)
def test_vcml::constraintobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::FormattedDocumentationBlock_strategy)
@settings(max_examples=50)
def test_vcml::formatteddocumentationblock_instantiation(instance):
    assert isinstance(instance, vcml::FormattedDocumentationBlock)

@given(instance=vcml::FormattedDocumentationBlock_strategy)
def test_vcml::formatteddocumentationblock_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::FormattedDocumentationBlock_strategy)
def test_vcml::formatteddocumentationblock_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::FormattedDocumentationBlock_strategy)
def test_vcml::formatteddocumentationblock_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=vcml::FormattedDocumentationBlock_strategy)
def test_vcml::formatteddocumentationblock_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=vcml::MultipleLanguageDocumentation::LanguageBlock_strategy)
@settings(max_examples=50)
def test_vcml::multiplelanguagedocumentation::languageblock_instantiation(instance):
    assert isinstance(instance, vcml::MultipleLanguageDocumentation::LanguageBlock)

@given(instance=vcml::MultipleLanguageDocumentation::LanguageBlock_strategy)
def test_vcml::multiplelanguagedocumentation::languageblock_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=vcml::MultipleLanguageDocumentation::LanguageBlock_strategy)
def test_vcml::multiplelanguagedocumentation::languageblock_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Documentation_strategy)
@settings(max_examples=50)
def test_documentation_instantiation(instance):
    assert isinstance(instance, Documentation)

@given(instance=vcml::MultipleLanguageDocumentation_strategy)
@settings(max_examples=50)
def test_vcml::multiplelanguagedocumentation_instantiation(instance):
    assert isinstance(instance, vcml::MultipleLanguageDocumentation)

@given(instance=vcml::SimpleDocumentation_strategy)
@settings(max_examples=50)
def test_vcml::simpledocumentation_instantiation(instance):
    assert isinstance(instance, vcml::SimpleDocumentation)

@given(instance=vcml::SimpleDocumentation_strategy)
def test_vcml::simpledocumentation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::SimpleDocumentation_strategy)
def test_vcml::simpledocumentation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::ObjectType_strategy)
@settings(max_examples=50)
def test_vcml::objecttype_instantiation(instance):
    assert isinstance(instance, vcml::ObjectType)

@given(instance=vcml::ObjectType_strategy)
def test_vcml::objecttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=vcml::ObjectType_strategy)
def test_vcml::objecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vcml::ObjectType_strategy)
def test_vcml::objecttype_classType_type(instance):
    assert isinstance(instance.classType, int)


@given(instance=vcml::ObjectType_strategy)
def test_vcml::objecttype_classType_setter(instance):
    original = instance.classType
    instance.classType = original
    assert instance.classType == original

@given(instance=vcml::ConstraintMaterial_strategy)
@settings(max_examples=50)
def test_vcml::constraintmaterial_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintMaterial)

@given(instance=vcml::MultiLanguageDescription_strategy)
@settings(max_examples=50)
def test_vcml::multilanguagedescription_instantiation(instance):
    assert isinstance(instance, vcml::MultiLanguageDescription)

@given(instance=vcml::MultiLanguageDescription_strategy)
def test_vcml::multilanguagedescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::MultiLanguageDescription_strategy)
def test_vcml::multilanguagedescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::MultiLanguageDescription_strategy)
def test_vcml::multilanguagedescription_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=vcml::MultiLanguageDescription_strategy)
def test_vcml::multilanguagedescription_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Description_strategy)
@settings(max_examples=50)
def test_description_instantiation(instance):
    assert isinstance(instance, Description)

@given(instance=vcml::MultiLanguageDescriptions_strategy)
@settings(max_examples=50)
def test_vcml::multilanguagedescriptions_instantiation(instance):
    assert isinstance(instance, vcml::MultiLanguageDescriptions)

@given(instance=vcml::SimpleDescription_strategy)
@settings(max_examples=50)
def test_vcml::simpledescription_instantiation(instance):
    assert isinstance(instance, vcml::SimpleDescription)

@given(instance=vcml::SimpleDescription_strategy)
def test_vcml::simpledescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::SimpleDescription_strategy)
def test_vcml::simpledescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::Row_strategy)
@settings(max_examples=50)
def test_vcml::row_instantiation(instance):
    assert isinstance(instance, vcml::Row)

@given(instance=vcml::VariantTableArgument_strategy)
@settings(max_examples=50)
def test_vcml::varianttableargument_instantiation(instance):
    assert isinstance(instance, vcml::VariantTableArgument)

@given(instance=vcml::VariantTableArgument_strategy)
def test_vcml::varianttableargument_key_type(instance):
    assert isinstance(instance.key, bool)


@given(instance=vcml::VariantTableArgument_strategy)
def test_vcml::varianttableargument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=vcml::VariantFunctionArgument_strategy)
@settings(max_examples=50)
def test_vcml::variantfunctionargument_instantiation(instance):
    assert isinstance(instance, vcml::VariantFunctionArgument)

@given(instance=vcml::VariantFunctionArgument_strategy)
def test_vcml::variantfunctionargument_in__type(instance):
    assert isinstance(instance.in_, bool)


@given(instance=vcml::VariantFunctionArgument_strategy)
def test_vcml::variantfunctionargument_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=vcml::ValueAssignment_strategy)
@settings(max_examples=50)
def test_vcml::valueassignment_instantiation(instance):
    assert isinstance(instance, vcml::ValueAssignment)

@given(instance=vcml::Classification_strategy)
@settings(max_examples=50)
def test_vcml::classification_instantiation(instance):
    assert isinstance(instance, vcml::Classification)

@given(instance=vcml::CharacteristicGroup_strategy)
@settings(max_examples=50)
def test_vcml::characteristicgroup_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicGroup)

@given(instance=vcml::CharacteristicGroup_strategy)
def test_vcml::characteristicgroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::CharacteristicGroup_strategy)
def test_vcml::characteristicgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::ConstraintSource_strategy)
@settings(max_examples=50)
def test_vcml::constraintsource_instantiation(instance):
    assert isinstance(instance, vcml::ConstraintSource)

@given(instance=vcml::Condition_strategy)
@settings(max_examples=50)
def test_vcml::condition_instantiation(instance):
    assert isinstance(instance, vcml::Condition)

@given(instance=vcml::ConditionSource_strategy)
@settings(max_examples=50)
def test_vcml::conditionsource_instantiation(instance):
    assert isinstance(instance, vcml::ConditionSource)

@given(instance=vcml::ProcedureSource_strategy)
@settings(max_examples=50)
def test_vcml::proceduresource_instantiation(instance):
    assert isinstance(instance, vcml::ProcedureSource)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=vcml::Dependency_strategy)
@settings(max_examples=50)
def test_vcml::dependency_instantiation(instance):
    assert isinstance(instance, vcml::Dependency)

@given(instance=vcml::NumberListEntry_strategy)
@settings(max_examples=50)
def test_vcml::numberlistentry_instantiation(instance):
    assert isinstance(instance, vcml::NumberListEntry)

@given(instance=vcml::DateCharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml::datecharacteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml::DateCharacteristicValue)

@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=vcml::DateCharacteristicValue_strategy)
def test_vcml::datecharacteristicvalue_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=vcml::CharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml::characteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicValue)

@given(instance=vcml::CharacteristicValue_strategy)
def test_vcml::characteristicvalue_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=vcml::CharacteristicValue_strategy)
def test_vcml::characteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=vcml::CharacteristicValue_strategy)
def test_vcml::characteristicvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::CharacteristicValue_strategy)
def test_vcml::characteristicvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::NumericCharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml::numericcharacteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml::NumericCharacteristicValue)

@given(instance=vcml::NumericCharacteristicValue_strategy)
def test_vcml::numericcharacteristicvalue_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=vcml::NumericCharacteristicValue_strategy)
def test_vcml::numericcharacteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=vcml::CharacteristicOrValueDependencies_strategy)
@settings(max_examples=50)
def test_vcml::characteristicorvaluedependencies_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicOrValueDependencies)

@given(instance=vcml::CharacteristicType_strategy)
@settings(max_examples=50)
def test_vcml::characteristictype_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicType)

@given(instance=vcml::CharacteristicType_strategy)
def test_vcml::characteristictype_numberOfChars_type(instance):
    assert isinstance(instance.numberOfChars, int)


@given(instance=vcml::CharacteristicType_strategy)
def test_vcml::characteristictype_numberOfChars_setter(instance):
    original = instance.numberOfChars
    instance.numberOfChars = original
    assert instance.numberOfChars == original

@given(instance=vcml::Documentation_strategy)
@settings(max_examples=50)
def test_vcml::documentation_instantiation(instance):
    assert isinstance(instance, vcml::Documentation)

@given(instance=BOMItem_strategy)
@settings(max_examples=50)
def test_bomitem_instantiation(instance):
    assert isinstance(instance, BOMItem)

@given(instance=vcml::BOMItem::Class_strategy)
@settings(max_examples=50)
def test_vcml::bomitem::class_instantiation(instance):
    assert isinstance(instance, vcml::BOMItem::Class)

@given(instance=vcml::BOMItem::Material_strategy)
@settings(max_examples=50)
def test_vcml::bomitem::material_instantiation(instance):
    assert isinstance(instance, vcml::BOMItem::Material)

@given(instance=vcml::ConfigurationProfileEntry_strategy)
@settings(max_examples=50)
def test_vcml::configurationprofileentry_instantiation(instance):
    assert isinstance(instance, vcml::ConfigurationProfileEntry)

@given(instance=vcml::ConfigurationProfileEntry_strategy)
def test_vcml::configurationprofileentry_sequence_type(instance):
    assert isinstance(instance.sequence, int)


@given(instance=vcml::ConfigurationProfileEntry_strategy)
def test_vcml::configurationprofileentry_sequence_setter(instance):
    original = instance.sequence
    instance.sequence = original
    assert instance.sequence == original

@given(instance=vcml::BOMItem_strategy)
@settings(max_examples=50)
def test_vcml::bomitem_instantiation(instance):
    assert isinstance(instance, vcml::BOMItem)

@given(instance=vcml::BOMItem_strategy)
def test_vcml::bomitem_itemnumber_type(instance):
    assert isinstance(instance.itemnumber, int)


@given(instance=vcml::BOMItem_strategy)
def test_vcml::bomitem_itemnumber_setter(instance):
    original = instance.itemnumber
    instance.itemnumber = original
    assert instance.itemnumber == original

@given(instance=VCObject_strategy)
@settings(max_examples=50)
def test_vcobject_instantiation(instance):
    assert isinstance(instance, VCObject)

@given(instance=vcml::Precondition_strategy)
@settings(max_examples=50)
def test_vcml::precondition_instantiation(instance):
    assert isinstance(instance, vcml::Precondition)

@given(instance=vcml::Precondition_strategy)
def test_vcml::precondition_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::Precondition_strategy)
def test_vcml::precondition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::Precondition_strategy)
def test_vcml::precondition_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::Precondition_strategy)
def test_vcml::precondition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::Procedure_strategy)
@settings(max_examples=50)
def test_vcml::procedure_instantiation(instance):
    assert isinstance(instance, vcml::Procedure)

@given(instance=vcml::Procedure_strategy)
def test_vcml::procedure_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::Procedure_strategy)
def test_vcml::procedure_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::Procedure_strategy)
def test_vcml::procedure_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::Procedure_strategy)
def test_vcml::procedure_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::Constraint_strategy)
@settings(max_examples=50)
def test_vcml::constraint_instantiation(instance):
    assert isinstance(instance, vcml::Constraint)

@given(instance=vcml::Constraint_strategy)
def test_vcml::constraint_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::Constraint_strategy)
def test_vcml::constraint_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::Constraint_strategy)
def test_vcml::constraint_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::Constraint_strategy)
def test_vcml::constraint_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::ConfigurationProfile_strategy)
@settings(max_examples=50)
def test_vcml::configurationprofile_instantiation(instance):
    assert isinstance(instance, vcml::ConfigurationProfile)

@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_fixing_type(instance):
    assert isinstance(instance.fixing, str)


@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_fixing_setter(instance):
    original = instance.fixing
    instance.fixing = original
    assert instance.fixing == original

@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_bomapplication_type(instance):
    assert isinstance(instance.bomapplication, str)


@given(instance=vcml::ConfigurationProfile_strategy)
def test_vcml::configurationprofile_bomapplication_setter(instance):
    original = instance.bomapplication
    instance.bomapplication = original
    assert instance.bomapplication == original

@given(instance=vcml::VariantTableContent_strategy)
@settings(max_examples=50)
def test_vcml::varianttablecontent_instantiation(instance):
    assert isinstance(instance, vcml::VariantTableContent)

@given(instance=vcml::Class_strategy)
@settings(max_examples=50)
def test_vcml::class_instantiation(instance):
    assert isinstance(instance, vcml::Class)

@given(instance=vcml::Class_strategy)
def test_vcml::class_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::Class_strategy)
def test_vcml::class_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::Class_strategy)
def test_vcml::class_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::Class_strategy)
def test_vcml::class_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::VariantTable_strategy)
@settings(max_examples=50)
def test_vcml::varianttable_instantiation(instance):
    assert isinstance(instance, vcml::VariantTable)

@given(instance=vcml::VariantTable_strategy)
def test_vcml::varianttable_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::VariantTable_strategy)
def test_vcml::varianttable_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::VariantTable_strategy)
def test_vcml::varianttable_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::VariantTable_strategy)
def test_vcml::varianttable_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::InterfaceDesign_strategy)
@settings(max_examples=50)
def test_vcml::interfacedesign_instantiation(instance):
    assert isinstance(instance, vcml::InterfaceDesign)

@given(instance=vcml::VariantFunction_strategy)
@settings(max_examples=50)
def test_vcml::variantfunction_instantiation(instance):
    assert isinstance(instance, vcml::VariantFunction)

@given(instance=vcml::VariantFunction_strategy)
def test_vcml::variantfunction_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::VariantFunction_strategy)
def test_vcml::variantfunction_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::VariantFunction_strategy)
def test_vcml::variantfunction_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::VariantFunction_strategy)
def test_vcml::variantfunction_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::Material_strategy)
@settings(max_examples=50)
def test_vcml::material_instantiation(instance):
    assert isinstance(instance, vcml::Material)

@given(instance=vcml::Material_strategy)
def test_vcml::material_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=vcml::Material_strategy)
def test_vcml::material_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vcml::Characteristic_strategy)
@settings(max_examples=50)
def test_vcml::characteristic_instantiation(instance):
    assert isinstance(instance, vcml::Characteristic)

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_displayAllowedValues_type(instance):
    assert isinstance(instance.displayAllowedValues, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_displayAllowedValues_setter(instance):
    original = instance.displayAllowedValues
    instance.displayAllowedValues = original
    assert instance.displayAllowedValues == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_table_type(instance):
    assert isinstance(instance.table, str)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_additionalValues_type(instance):
    assert isinstance(instance.additionalValues, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_additionalValues_setter(instance):
    original = instance.additionalValues
    instance.additionalValues = original
    assert instance.additionalValues == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_noDisplay_type(instance):
    assert isinstance(instance.noDisplay, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_noDisplay_setter(instance):
    original = instance.noDisplay
    instance.noDisplay = original
    assert instance.noDisplay == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_multiValue_type(instance):
    assert isinstance(instance.multiValue, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_multiValue_setter(instance):
    original = instance.multiValue
    instance.multiValue = original
    assert instance.multiValue == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_notReadyForInput_type(instance):
    assert isinstance(instance.notReadyForInput, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_notReadyForInput_setter(instance):
    original = instance.notReadyForInput
    instance.notReadyForInput = original
    assert instance.notReadyForInput == original

@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_restrictable_type(instance):
    assert isinstance(instance.restrictable, bool)


@given(instance=vcml::Characteristic_strategy)
def test_vcml::characteristic_restrictable_setter(instance):
    original = instance.restrictable
    instance.restrictable = original
    assert instance.restrictable == original

@given(instance=vcml::DependencyNet_strategy)
@settings(max_examples=50)
def test_vcml::dependencynet_instantiation(instance):
    assert isinstance(instance, vcml::DependencyNet)

@given(instance=vcml::DependencyNet_strategy)
def test_vcml::dependencynet_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::DependencyNet_strategy)
def test_vcml::dependencynet_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::DependencyNet_strategy)
def test_vcml::dependencynet_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::DependencyNet_strategy)
def test_vcml::dependencynet_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::SelectionCondition_strategy)
@settings(max_examples=50)
def test_vcml::selectioncondition_instantiation(instance):
    assert isinstance(instance, vcml::SelectionCondition)

@given(instance=vcml::SelectionCondition_strategy)
def test_vcml::selectioncondition_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=vcml::SelectionCondition_strategy)
def test_vcml::selectioncondition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml::SelectionCondition_strategy)
def test_vcml::selectioncondition_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=vcml::SelectionCondition_strategy)
def test_vcml::selectioncondition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml::BillOfMaterial_strategy)
@settings(max_examples=50)
def test_vcml::billofmaterial_instantiation(instance):
    assert isinstance(instance, vcml::BillOfMaterial)

@given(instance=vcml::Description_strategy)
@settings(max_examples=50)
def test_vcml::description_instantiation(instance):
    assert isinstance(instance, vcml::Description)

@given(instance=CharacteristicType_strategy)
@settings(max_examples=50)
def test_characteristictype_instantiation(instance):
    assert isinstance(instance, CharacteristicType)

@given(instance=vcml::SymbolicType_strategy)
@settings(max_examples=50)
def test_vcml::symbolictype_instantiation(instance):
    assert isinstance(instance, vcml::SymbolicType)

@given(instance=vcml::SymbolicType_strategy)
def test_vcml::symbolictype_caseSensitive_type(instance):
    assert isinstance(instance.caseSensitive, bool)


@given(instance=vcml::SymbolicType_strategy)
def test_vcml::symbolictype_caseSensitive_setter(instance):
    original = instance.caseSensitive
    instance.caseSensitive = original
    assert instance.caseSensitive == original

@given(instance=vcml::DateType_strategy)
@settings(max_examples=50)
def test_vcml::datetype_instantiation(instance):
    assert isinstance(instance, vcml::DateType)

@given(instance=vcml::DateType_strategy)
def test_vcml::datetype_intervalValuesAllowed_type(instance):
    assert isinstance(instance.intervalValuesAllowed, bool)


@given(instance=vcml::DateType_strategy)
def test_vcml::datetype_intervalValuesAllowed_setter(instance):
    original = instance.intervalValuesAllowed
    instance.intervalValuesAllowed = original
    assert instance.intervalValuesAllowed == original

@given(instance=vcml::NumericType_strategy)
@settings(max_examples=50)
def test_vcml::numerictype_instantiation(instance):
    assert isinstance(instance, vcml::NumericType)

@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_decimalPlaces_type(instance):
    assert isinstance(instance.decimalPlaces, int)


@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_decimalPlaces_setter(instance):
    original = instance.decimalPlaces
    instance.decimalPlaces = original
    assert instance.decimalPlaces == original

@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_intervalValuesAllowed_type(instance):
    assert isinstance(instance.intervalValuesAllowed, bool)


@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_intervalValuesAllowed_setter(instance):
    original = instance.intervalValuesAllowed
    instance.intervalValuesAllowed = original
    assert instance.intervalValuesAllowed == original

@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_negativeValuesAllowed_type(instance):
    assert isinstance(instance.negativeValuesAllowed, bool)


@given(instance=vcml::NumericType_strategy)
def test_vcml::numerictype_negativeValuesAllowed_setter(instance):
    original = instance.negativeValuesAllowed
    instance.negativeValuesAllowed = original
    assert instance.negativeValuesAllowed == original

@given(instance=vcml::VCObject_strategy)
@settings(max_examples=50)
def test_vcml::vcobject_instantiation(instance):
    assert isinstance(instance, vcml::VCObject)

@given(instance=vcml::VCObject_strategy)
def test_vcml::vcobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::VCObject_strategy)
def test_vcml::vcobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::Option_strategy)
@settings(max_examples=50)
def test_vcml::option_instantiation(instance):
    assert isinstance(instance, vcml::Option)

@given(instance=vcml::Option_strategy)
def test_vcml::option_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::Option_strategy)
def test_vcml::option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::Option_strategy)
def test_vcml::option_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vcml::Option_strategy)
def test_vcml::option_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml::Import_strategy)
@settings(max_examples=50)
def test_vcml::import_instantiation(instance):
    assert isinstance(instance, vcml::Import)

@given(instance=vcml::Import_strategy)
def test_vcml::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=vcml::Import_strategy)
def test_vcml::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=vcml::VcmlModel_strategy)
@settings(max_examples=50)
def test_vcml::vcmlmodel_instantiation(instance):
    assert isinstance(instance, vcml::VcmlModel)

@given(instance=vcml::BinaryCondition_strategy)
@settings(max_examples=50)
def test_vcml::binarycondition_instantiation(instance):
    assert isinstance(instance, vcml::BinaryCondition)

@given(instance=vcml::BinaryCondition_strategy)
def test_vcml::binarycondition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vcml::BinaryCondition_strategy)
def test_vcml::binarycondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml::ConditionalConstraintRestriction_strategy)
@settings(max_examples=50)
def test_vcml::conditionalconstraintrestriction_instantiation(instance):
    assert isinstance(instance, vcml::ConditionalConstraintRestriction)

@given(instance=List_strategy)
@settings(max_examples=50)
def test_list_instantiation(instance):
    assert isinstance(instance, List)

@given(instance=vcml::SymbolList_strategy)
@settings(max_examples=50)
def test_vcml::symbollist_instantiation(instance):
    assert isinstance(instance, vcml::SymbolList)

@given(instance=vcml::NumberList_strategy)
@settings(max_examples=50)
def test_vcml::numberlist_instantiation(instance):
    assert isinstance(instance, vcml::NumberList)

@given(instance=vcml::InCondition::P_strategy)
@settings(max_examples=50)
def test_vcml::incondition::p_instantiation(instance):
    assert isinstance(instance, vcml::InCondition::P)

@given(instance=vcml::List_strategy)
@settings(max_examples=50)
def test_vcml::list_instantiation(instance):
    assert isinstance(instance, vcml::List)

@given(instance=vcml::InCondition::C_strategy)
@settings(max_examples=50)
def test_vcml::incondition::c_instantiation(instance):
    assert isinstance(instance, vcml::InCondition::C)

@given(instance=vcml::IsSpecified::P_strategy)
@settings(max_examples=50)
def test_vcml::isspecified::p_instantiation(instance):
    assert isinstance(instance, vcml::IsSpecified::P)

@given(instance=vcml::IsSpecified::C_strategy)
@settings(max_examples=50)
def test_vcml::isspecified::c_instantiation(instance):
    assert isinstance(instance, vcml::IsSpecified::C)

@given(instance=vcml::Comparison_strategy)
@settings(max_examples=50)
def test_vcml::comparison_instantiation(instance):
    assert isinstance(instance, vcml::Comparison)

@given(instance=vcml::Comparison_strategy)
def test_vcml::comparison_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vcml::Comparison_strategy)
def test_vcml::comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml::UnaryCondition_strategy)
@settings(max_examples=50)
def test_vcml::unarycondition_instantiation(instance):
    assert isinstance(instance, vcml::UnaryCondition)

@given(instance=vcml::SymbolicLiteral_strategy)
@settings(max_examples=50)
def test_vcml::symbolicliteral_instantiation(instance):
    assert isinstance(instance, vcml::SymbolicLiteral)

@given(instance=vcml::SymbolicLiteral_strategy)
def test_vcml::symbolicliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::SymbolicLiteral_strategy)
def test_vcml::symbolicliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberListEntry_strategy)
@settings(max_examples=50)
def test_numberlistentry_instantiation(instance):
    assert isinstance(instance, NumberListEntry)

@given(instance=vcml::NumericInterval_strategy)
@settings(max_examples=50)
def test_vcml::numericinterval_instantiation(instance):
    assert isinstance(instance, vcml::NumericInterval)

@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_lowerBoundOp_type(instance):
    assert isinstance(instance.lowerBoundOp, str)


@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_lowerBoundOp_setter(instance):
    original = instance.lowerBoundOp
    instance.lowerBoundOp = original
    assert instance.lowerBoundOp == original

@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_upperBoundOp_type(instance):
    assert isinstance(instance.upperBoundOp, str)


@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_upperBoundOp_setter(instance):
    original = instance.upperBoundOp
    instance.upperBoundOp = original
    assert instance.upperBoundOp == original

@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=vcml::NumericInterval_strategy)
def test_vcml::numericinterval_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=vcml::NumericLiteral_strategy)
@settings(max_examples=50)
def test_vcml::numericliteral_instantiation(instance):
    assert isinstance(instance, vcml::NumericLiteral)

@given(instance=vcml::NumericLiteral_strategy)
def test_vcml::numericliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vcml::NumericLiteral_strategy)
def test_vcml::numericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml::MDataCharacteristic::P_strategy)
@settings(max_examples=50)
def test_vcml::mdatacharacteristic::p_instantiation(instance):
    assert isinstance(instance, vcml::MDataCharacteristic::P)

@given(instance=vcml::MDataCharacteristic::C_strategy)
@settings(max_examples=50)
def test_vcml::mdatacharacteristic::c_instantiation(instance):
    assert isinstance(instance, vcml::MDataCharacteristic::C)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vcml::CountParts_strategy)
@settings(max_examples=50)
def test_vcml::countparts_instantiation(instance):
    assert isinstance(instance, vcml::CountParts)

@given(instance=vcml::CountParts_strategy)
def test_vcml::countparts_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=vcml::CountParts_strategy)
def test_vcml::countparts_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml::SumParts_strategy)
@settings(max_examples=50)
def test_vcml::sumparts_instantiation(instance):
    assert isinstance(instance, vcml::SumParts)

@given(instance=vcml::SumParts_strategy)
def test_vcml::sumparts_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=vcml::SumParts_strategy)
def test_vcml::sumparts_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml::FunctionCall_strategy)
@settings(max_examples=50)
def test_vcml::functioncall_instantiation(instance):
    assert isinstance(instance, vcml::FunctionCall)

@given(instance=vcml::FunctionCall_strategy)
def test_vcml::functioncall_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=vcml::FunctionCall_strategy)
def test_vcml::functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=vcml::Literal_strategy)
@settings(max_examples=50)
def test_vcml::literal_instantiation(instance):
    assert isinstance(instance, vcml::Literal)

@given(instance=vcml::BinaryExpression_strategy)
@settings(max_examples=50)
def test_vcml::binaryexpression_instantiation(instance):
    assert isinstance(instance, vcml::BinaryExpression)

@given(instance=vcml::BinaryExpression_strategy)
def test_vcml::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vcml::BinaryExpression_strategy)
def test_vcml::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml::UnaryExpression_strategy)
@settings(max_examples=50)
def test_vcml::unaryexpression_instantiation(instance):
    assert isinstance(instance, vcml::UnaryExpression)

@given(instance=vcml::UnaryExpression_strategy)
def test_vcml::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vcml::UnaryExpression_strategy)
def test_vcml::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml::TypeOf_strategy)
@settings(max_examples=50)
def test_vcml::typeof_instantiation(instance):
    assert isinstance(instance, vcml::TypeOf)

@given(instance=vcml::TypeOf_strategy)
def test_vcml::typeof_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=vcml::TypeOf_strategy)
def test_vcml::typeof_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SetOrDelDefault_strategy)
@settings(max_examples=50)
def test_setordeldefault_instantiation(instance):
    assert isinstance(instance, SetOrDelDefault)

@given(instance=vcml::DelDefault_strategy)
@settings(max_examples=50)
def test_vcml::deldefault_instantiation(instance):
    assert isinstance(instance, vcml::DelDefault)

@given(instance=vcml::SetDefault_strategy)
@settings(max_examples=50)
def test_vcml::setdefault_instantiation(instance):
    assert isinstance(instance, vcml::SetDefault)

@given(instance=FunctionOrTable_strategy)
@settings(max_examples=50)
def test_functionortable_instantiation(instance):
    assert isinstance(instance, FunctionOrTable)

@given(instance=vcml::CharacteristicReference::P_strategy)
@settings(max_examples=50)
def test_vcml::characteristicreference::p_instantiation(instance):
    assert isinstance(instance, vcml::CharacteristicReference::P)

@given(instance=vcml::CharacteristicReference::P_strategy)
def test_vcml::characteristicreference::p_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=vcml::CharacteristicReference::P_strategy)
def test_vcml::characteristicreference::p_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=vcml::IsInvisible_strategy)
@settings(max_examples=50)
def test_vcml::isinvisible_instantiation(instance):
    assert isinstance(instance, vcml::IsInvisible)

@given(instance=vcml::Table_strategy)
@settings(max_examples=50)
def test_vcml::table_instantiation(instance):
    assert isinstance(instance, vcml::Table)

@given(instance=vcml::Function_strategy)
@settings(max_examples=50)
def test_vcml::function_instantiation(instance):
    assert isinstance(instance, vcml::Function)

@given(instance=vcml::SetPricingFactor_strategy)
@settings(max_examples=50)
def test_vcml::setpricingfactor_instantiation(instance):
    assert isinstance(instance, vcml::SetPricingFactor)

@given(instance=vcml::SetPricingFactor_strategy)
def test_vcml::setpricingfactor_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=vcml::SetPricingFactor_strategy)
def test_vcml::setpricingfactor_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml::SetOrDelDefault_strategy)
@settings(max_examples=50)
def test_vcml::setordeldefault_instantiation(instance):
    assert isinstance(instance, vcml::SetOrDelDefault)

@given(instance=vcml::PFunction_strategy)
@settings(max_examples=50)
def test_vcml::pfunction_instantiation(instance):
    assert isinstance(instance, vcml::PFunction)

@given(instance=vcml::Assignment_strategy)
@settings(max_examples=50)
def test_vcml::assignment_instantiation(instance):
    assert isinstance(instance, vcml::Assignment)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=vcml::SimpleStatement_strategy)
@settings(max_examples=50)
def test_vcml::simplestatement_instantiation(instance):
    assert isinstance(instance, vcml::SimpleStatement)

@given(instance=vcml::ConditionalStatement_strategy)
@settings(max_examples=50)
def test_vcml::conditionalstatement_instantiation(instance):
    assert isinstance(instance, vcml::ConditionalStatement)

@given(instance=vcml::CompoundStatement_strategy)
@settings(max_examples=50)
def test_vcml::compoundstatement_instantiation(instance):
    assert isinstance(instance, vcml::CompoundStatement)

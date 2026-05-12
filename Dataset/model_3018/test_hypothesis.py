import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleStatement,
    vcml_Assignment,
    Statement,
    vcml_SimpleStatement,
    vcml_CompoundStatement,
    vcml_Statement,
    CharacteristicReference_C,
    vcml_ShortVarReference,
    vcml_ObjectCharacteristicReference,
    Literal,
    vcml_CharacteristicReference_P,
    vcml_EObject,
    Condition,
    ConstraintRestriction,
    vcml_SubpartOfCondition,
    vcml_ConstraintRestrictionFalse,
    vcml_NegatedConstraintRestrictionLHS,
    vcml_PartOfCondition,
    vcml_PartialKey,
    vcml_FunctionOrTable,
    vcml_Expression,
    ConstraintObject,
    vcml_ConstraintClass,
    vcml_ShortVarDefinition,
    vcml_CharacteristicReference_C,
    vcml_ConstraintRestriction,
    vcml_ConstraintObject,
    vcml_FormattedDocumentationBlock,
    vcml_MultipleLanguageDocumentation_LanguageBlock,
    Documentation,
    vcml_MultipleLanguageDocumentation,
    vcml_SimpleDocumentation,
    vcml_ObjectType,
    vcml_ConstraintMaterial,
    vcml_MultiLanguageDescription,
    Description,
    vcml_MultiLanguageDescriptions,
    vcml_SimpleDescription,
    vcml_Row,
    vcml_VariantTableArgument,
    vcml_VariantFunctionArgument,
    vcml_ValueAssignment,
    vcml_Classification,
    vcml_CharacteristicGroup,
    vcml_ConstraintSource,
    vcml_Condition,
    vcml_ConditionSource,
    vcml_ProcedureSource,
    Dependency,
    vcml_Dependency,
    vcml_NumberListEntry,
    vcml_DateCharacteristicValue,
    vcml_CharacteristicValue,
    vcml_NumericCharacteristicValue,
    vcml_CharacteristicOrValueDependencies,
    vcml_CharacteristicType,
    vcml_Documentation,
    BOMItem,
    vcml_BOMItem_Class,
    vcml_BOMItem_Material,
    vcml_ConfigurationProfileEntry,
    vcml_BOMItem,
    VCObject,
    vcml_VariantTable,
    vcml_Constraint,
    vcml_VariantTableContent,
    vcml_Procedure,
    vcml_InterfaceDesign,
    vcml_DependencyNet,
    vcml_Material,
    vcml_VariantFunction,
    vcml_SelectionCondition,
    vcml_Class,
    vcml_Precondition,
    vcml_Characteristic,
    vcml_ConfigurationProfile,
    vcml_BillOfMaterial,
    vcml_Description,
    CharacteristicType,
    vcml_SymbolicType,
    vcml_DateType,
    vcml_NumericType,
    vcml_VCObject,
    vcml_Option,
    vcml_Import,
    vcml_VcmlModel,
    vcml_BinaryCondition,
    vcml_ConditionalStatement,
    vcml_ConditionalConstraintRestriction,
    List,
    vcml_SymbolList,
    vcml_NumberList,
    vcml_InCondition_P,
    vcml_List,
    vcml_InCondition_C,
    vcml_IsSpecified_P,
    vcml_IsSpecified_C,
    vcml_Comparison,
    vcml_UnaryCondition,
    vcml_SymbolicLiteral,
    NumberListEntry,
    vcml_NumericInterval,
    vcml_NumericLiteral,
    vcml_MDataCharacteristic_P,
    vcml_MDataCharacteristic_C,
    Expression,
    vcml_Literal,
    vcml_FunctionCall,
    vcml_SumParts,
    vcml_BinaryExpression,
    vcml_CountParts,
    vcml_UnaryExpression,
    vcml_TypeOf,
    vcml_SetPricingFactor,
    vcml_IsInvisible,
    SetOrDelDefault,
    vcml_DelDefault,
    vcml_SetDefault,
    vcml_SetOrDelDefault,
    FunctionOrTable,
    vcml_PFunction,
    vcml_Table,
    vcml_Function,
    Status,
    FunctionName,
    Fixing,
    Language,
    ComparisonOperator,
    OptionType,
    ProcedureLocation,
    UnaryExpressionOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml_assignment_is_not_abstract():
    assert not inspect.isabstract(vcml_Assignment)


def test_vcml_assignment_constructor_exists():
    assert callable(vcml_Assignment.__init__)


def test_vcml_assignment_constructor_args():
    sig = inspect.signature(vcml_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_vcml_simplestatement_is_not_abstract():
    assert not inspect.isabstract(vcml_SimpleStatement)


def test_vcml_simplestatement_constructor_exists():
    assert callable(vcml_SimpleStatement.__init__)


def test_vcml_simplestatement_constructor_args():
    sig = inspect.signature(vcml_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml_compoundstatement_is_not_abstract():
    assert not inspect.isabstract(vcml_CompoundStatement)


def test_vcml_compoundstatement_constructor_exists():
    assert callable(vcml_CompoundStatement.__init__)


def test_vcml_compoundstatement_constructor_args():
    sig = inspect.signature(vcml_CompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml_statement_is_not_abstract():
    assert not inspect.isabstract(vcml_Statement)


def test_vcml_statement_constructor_exists():
    assert callable(vcml_Statement.__init__)


def test_vcml_statement_constructor_args():
    sig = inspect.signature(vcml_Statement.__init__)
    params = list(sig.parameters.keys())



def test_characteristicreference_c_is_not_abstract():
    assert not inspect.isabstract(CharacteristicReference_C)


def test_characteristicreference_c_constructor_exists():
    assert callable(CharacteristicReference_C.__init__)


def test_characteristicreference_c_constructor_args():
    sig = inspect.signature(CharacteristicReference_C.__init__)
    params = list(sig.parameters.keys())



def test_vcml_shortvarreference_is_not_abstract():
    assert not inspect.isabstract(vcml_ShortVarReference)


def test_vcml_shortvarreference_constructor_exists():
    assert callable(vcml_ShortVarReference.__init__)


def test_vcml_shortvarreference_constructor_args():
    sig = inspect.signature(vcml_ShortVarReference.__init__)
    params = list(sig.parameters.keys())



def test_vcml_objectcharacteristicreference_is_not_abstract():
    assert not inspect.isabstract(vcml_ObjectCharacteristicReference)


def test_vcml_objectcharacteristicreference_constructor_exists():
    assert callable(vcml_ObjectCharacteristicReference.__init__)


def test_vcml_objectcharacteristicreference_constructor_args():
    sig = inspect.signature(vcml_ObjectCharacteristicReference.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_vcml_characteristicreference_p_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicReference_P)


def test_vcml_characteristicreference_p_constructor_exists():
    assert callable(vcml_CharacteristicReference_P.__init__)


def test_vcml_characteristicreference_p_constructor_args():
    sig = inspect.signature(vcml_CharacteristicReference_P.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml_characteristicreference_p_has_location():
    assert hasattr(vcml_CharacteristicReference_P, "location")
    descriptor = None
    for klass in vcml_CharacteristicReference_P.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml_eobject_is_not_abstract():
    assert not inspect.isabstract(vcml_EObject)


def test_vcml_eobject_constructor_exists():
    assert callable(vcml_EObject.__init__)


def test_vcml_eobject_constructor_args():
    sig = inspect.signature(vcml_EObject.__init__)
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



def test_vcml_subpartofcondition_is_not_abstract():
    assert not inspect.isabstract(vcml_SubpartOfCondition)


def test_vcml_subpartofcondition_constructor_exists():
    assert callable(vcml_SubpartOfCondition.__init__)


def test_vcml_subpartofcondition_constructor_args():
    sig = inspect.signature(vcml_SubpartOfCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml_constraintrestrictionfalse_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintRestrictionFalse)


def test_vcml_constraintrestrictionfalse_constructor_exists():
    assert callable(vcml_ConstraintRestrictionFalse.__init__)


def test_vcml_constraintrestrictionfalse_constructor_args():
    sig = inspect.signature(vcml_ConstraintRestrictionFalse.__init__)
    params = list(sig.parameters.keys())



def test_vcml_negatedconstraintrestrictionlhs_is_not_abstract():
    assert not inspect.isabstract(vcml_NegatedConstraintRestrictionLHS)


def test_vcml_negatedconstraintrestrictionlhs_constructor_exists():
    assert callable(vcml_NegatedConstraintRestrictionLHS.__init__)


def test_vcml_negatedconstraintrestrictionlhs_constructor_args():
    sig = inspect.signature(vcml_NegatedConstraintRestrictionLHS.__init__)
    params = list(sig.parameters.keys())



def test_vcml_partofcondition_is_not_abstract():
    assert not inspect.isabstract(vcml_PartOfCondition)


def test_vcml_partofcondition_constructor_exists():
    assert callable(vcml_PartOfCondition.__init__)


def test_vcml_partofcondition_constructor_args():
    sig = inspect.signature(vcml_PartOfCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml_partialkey_is_not_abstract():
    assert not inspect.isabstract(vcml_PartialKey)


def test_vcml_partialkey_constructor_exists():
    assert callable(vcml_PartialKey.__init__)


def test_vcml_partialkey_constructor_args():
    sig = inspect.signature(vcml_PartialKey.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_vcml_partialkey_has_key():
    assert hasattr(vcml_PartialKey, "key")
    descriptor = None
    for klass in vcml_PartialKey.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_vcml_functionortable_is_not_abstract():
    assert not inspect.isabstract(vcml_FunctionOrTable)


def test_vcml_functionortable_constructor_exists():
    assert callable(vcml_FunctionOrTable.__init__)


def test_vcml_functionortable_constructor_args():
    sig = inspect.signature(vcml_FunctionOrTable.__init__)
    params = list(sig.parameters.keys())



def test_vcml_expression_is_not_abstract():
    assert not inspect.isabstract(vcml_Expression)


def test_vcml_expression_constructor_exists():
    assert callable(vcml_Expression.__init__)


def test_vcml_expression_constructor_args():
    sig = inspect.signature(vcml_Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraintobject_is_not_abstract():
    assert not inspect.isabstract(ConstraintObject)


def test_constraintobject_constructor_exists():
    assert callable(ConstraintObject.__init__)


def test_constraintobject_constructor_args():
    sig = inspect.signature(ConstraintObject.__init__)
    params = list(sig.parameters.keys())



def test_vcml_constraintclass_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintClass)


def test_vcml_constraintclass_constructor_exists():
    assert callable(vcml_ConstraintClass.__init__)


def test_vcml_constraintclass_constructor_args():
    sig = inspect.signature(vcml_ConstraintClass.__init__)
    params = list(sig.parameters.keys())



def test_vcml_shortvardefinition_is_not_abstract():
    assert not inspect.isabstract(vcml_ShortVarDefinition)


def test_vcml_shortvardefinition_constructor_exists():
    assert callable(vcml_ShortVarDefinition.__init__)


def test_vcml_shortvardefinition_constructor_args():
    sig = inspect.signature(vcml_ShortVarDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_shortvardefinition_has_name():
    assert hasattr(vcml_ShortVarDefinition, "name")
    descriptor = None
    for klass in vcml_ShortVarDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_characteristicreference_c_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicReference_C)


def test_vcml_characteristicreference_c_constructor_exists():
    assert callable(vcml_CharacteristicReference_C.__init__)


def test_vcml_characteristicreference_c_constructor_args():
    sig = inspect.signature(vcml_CharacteristicReference_C.__init__)
    params = list(sig.parameters.keys())



def test_vcml_constraintrestriction_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintRestriction)


def test_vcml_constraintrestriction_constructor_exists():
    assert callable(vcml_ConstraintRestriction.__init__)


def test_vcml_constraintrestriction_constructor_args():
    sig = inspect.signature(vcml_ConstraintRestriction.__init__)
    params = list(sig.parameters.keys())



def test_vcml_constraintobject_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintObject)


def test_vcml_constraintobject_constructor_exists():
    assert callable(vcml_ConstraintObject.__init__)


def test_vcml_constraintobject_constructor_args():
    sig = inspect.signature(vcml_ConstraintObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_constraintobject_has_name():
    assert hasattr(vcml_ConstraintObject, "name")
    descriptor = None
    for klass in vcml_ConstraintObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_formatteddocumentationblock_is_not_abstract():
    assert not inspect.isabstract(vcml_FormattedDocumentationBlock)


def test_vcml_formatteddocumentationblock_constructor_exists():
    assert callable(vcml_FormattedDocumentationBlock.__init__)


def test_vcml_formatteddocumentationblock_constructor_args():
    sig = inspect.signature(vcml_FormattedDocumentationBlock.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "format" in params, "Missing parameter 'format'"

def test_vcml_formatteddocumentationblock_has_value():
    assert hasattr(vcml_FormattedDocumentationBlock, "value")
    descriptor = None
    for klass in vcml_FormattedDocumentationBlock.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml_formatteddocumentationblock_has_format():
    assert hasattr(vcml_FormattedDocumentationBlock, "format")
    descriptor = None
    for klass in vcml_FormattedDocumentationBlock.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_vcml_multiplelanguagedocumentation_languageblock_is_not_abstract():
    assert not inspect.isabstract(vcml_MultipleLanguageDocumentation_LanguageBlock)


def test_vcml_multiplelanguagedocumentation_languageblock_constructor_exists():
    assert callable(vcml_MultipleLanguageDocumentation_LanguageBlock.__init__)


def test_vcml_multiplelanguagedocumentation_languageblock_constructor_args():
    sig = inspect.signature(vcml_MultipleLanguageDocumentation_LanguageBlock.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_vcml_multiplelanguagedocumentation_languageblock_has_language():
    assert hasattr(vcml_MultipleLanguageDocumentation_LanguageBlock, "language")
    descriptor = None
    for klass in vcml_MultipleLanguageDocumentation_LanguageBlock.__mro__:
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



def test_vcml_multiplelanguagedocumentation_is_not_abstract():
    assert not inspect.isabstract(vcml_MultipleLanguageDocumentation)


def test_vcml_multiplelanguagedocumentation_constructor_exists():
    assert callable(vcml_MultipleLanguageDocumentation.__init__)


def test_vcml_multiplelanguagedocumentation_constructor_args():
    sig = inspect.signature(vcml_MultipleLanguageDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_vcml_simpledocumentation_is_not_abstract():
    assert not inspect.isabstract(vcml_SimpleDocumentation)


def test_vcml_simpledocumentation_constructor_exists():
    assert callable(vcml_SimpleDocumentation.__init__)


def test_vcml_simpledocumentation_constructor_args():
    sig = inspect.signature(vcml_SimpleDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml_simpledocumentation_has_value():
    assert hasattr(vcml_SimpleDocumentation, "value")
    descriptor = None
    for klass in vcml_SimpleDocumentation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml_objecttype_is_not_abstract():
    assert not inspect.isabstract(vcml_ObjectType)


def test_vcml_objecttype_constructor_exists():
    assert callable(vcml_ObjectType.__init__)


def test_vcml_objecttype_constructor_args():
    sig = inspect.signature(vcml_ObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "classType" in params, "Missing parameter 'classType'"
    assert "type" in params, "Missing parameter 'type'"

def test_vcml_objecttype_has_classType():
    assert hasattr(vcml_ObjectType, "classType")
    descriptor = None
    for klass in vcml_ObjectType.__mro__:
        if "classType" in klass.__dict__:
            descriptor = klass.__dict__["classType"]
            break
    assert isinstance(descriptor, property)

def test_vcml_objecttype_has_type():
    assert hasattr(vcml_ObjectType, "type")
    descriptor = None
    for klass in vcml_ObjectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_vcml_constraintmaterial_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintMaterial)


def test_vcml_constraintmaterial_constructor_exists():
    assert callable(vcml_ConstraintMaterial.__init__)


def test_vcml_constraintmaterial_constructor_args():
    sig = inspect.signature(vcml_ConstraintMaterial.__init__)
    params = list(sig.parameters.keys())



def test_vcml_multilanguagedescription_is_not_abstract():
    assert not inspect.isabstract(vcml_MultiLanguageDescription)


def test_vcml_multilanguagedescription_constructor_exists():
    assert callable(vcml_MultiLanguageDescription.__init__)


def test_vcml_multilanguagedescription_constructor_args():
    sig = inspect.signature(vcml_MultiLanguageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "language" in params, "Missing parameter 'language'"

def test_vcml_multilanguagedescription_has_value():
    assert hasattr(vcml_MultiLanguageDescription, "value")
    descriptor = None
    for klass in vcml_MultiLanguageDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml_multilanguagedescription_has_language():
    assert hasattr(vcml_MultiLanguageDescription, "language")
    descriptor = None
    for klass in vcml_MultiLanguageDescription.__mro__:
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



def test_vcml_multilanguagedescriptions_is_not_abstract():
    assert not inspect.isabstract(vcml_MultiLanguageDescriptions)


def test_vcml_multilanguagedescriptions_constructor_exists():
    assert callable(vcml_MultiLanguageDescriptions.__init__)


def test_vcml_multilanguagedescriptions_constructor_args():
    sig = inspect.signature(vcml_MultiLanguageDescriptions.__init__)
    params = list(sig.parameters.keys())



def test_vcml_simpledescription_is_not_abstract():
    assert not inspect.isabstract(vcml_SimpleDescription)


def test_vcml_simpledescription_constructor_exists():
    assert callable(vcml_SimpleDescription.__init__)


def test_vcml_simpledescription_constructor_args():
    sig = inspect.signature(vcml_SimpleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml_simpledescription_has_value():
    assert hasattr(vcml_SimpleDescription, "value")
    descriptor = None
    for klass in vcml_SimpleDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml_row_is_not_abstract():
    assert not inspect.isabstract(vcml_Row)


def test_vcml_row_constructor_exists():
    assert callable(vcml_Row.__init__)


def test_vcml_row_constructor_args():
    sig = inspect.signature(vcml_Row.__init__)
    params = list(sig.parameters.keys())



def test_vcml_varianttableargument_is_not_abstract():
    assert not inspect.isabstract(vcml_VariantTableArgument)


def test_vcml_varianttableargument_constructor_exists():
    assert callable(vcml_VariantTableArgument.__init__)


def test_vcml_varianttableargument_constructor_args():
    sig = inspect.signature(vcml_VariantTableArgument.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_vcml_varianttableargument_has_key():
    assert hasattr(vcml_VariantTableArgument, "key")
    descriptor = None
    for klass in vcml_VariantTableArgument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_vcml_variantfunctionargument_is_not_abstract():
    assert not inspect.isabstract(vcml_VariantFunctionArgument)


def test_vcml_variantfunctionargument_constructor_exists():
    assert callable(vcml_VariantFunctionArgument.__init__)


def test_vcml_variantfunctionargument_constructor_args():
    sig = inspect.signature(vcml_VariantFunctionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_vcml_variantfunctionargument_has_in_():
    assert hasattr(vcml_VariantFunctionArgument, "in_")
    descriptor = None
    for klass in vcml_VariantFunctionArgument.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_vcml_valueassignment_is_not_abstract():
    assert not inspect.isabstract(vcml_ValueAssignment)


def test_vcml_valueassignment_constructor_exists():
    assert callable(vcml_ValueAssignment.__init__)


def test_vcml_valueassignment_constructor_args():
    sig = inspect.signature(vcml_ValueAssignment.__init__)
    params = list(sig.parameters.keys())



def test_vcml_classification_is_not_abstract():
    assert not inspect.isabstract(vcml_Classification)


def test_vcml_classification_constructor_exists():
    assert callable(vcml_Classification.__init__)


def test_vcml_classification_constructor_args():
    sig = inspect.signature(vcml_Classification.__init__)
    params = list(sig.parameters.keys())



def test_vcml_characteristicgroup_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicGroup)


def test_vcml_characteristicgroup_constructor_exists():
    assert callable(vcml_CharacteristicGroup.__init__)


def test_vcml_characteristicgroup_constructor_args():
    sig = inspect.signature(vcml_CharacteristicGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_characteristicgroup_has_name():
    assert hasattr(vcml_CharacteristicGroup, "name")
    descriptor = None
    for klass in vcml_CharacteristicGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_constraintsource_is_not_abstract():
    assert not inspect.isabstract(vcml_ConstraintSource)


def test_vcml_constraintsource_constructor_exists():
    assert callable(vcml_ConstraintSource.__init__)


def test_vcml_constraintsource_constructor_args():
    sig = inspect.signature(vcml_ConstraintSource.__init__)
    params = list(sig.parameters.keys())



def test_vcml_condition_is_not_abstract():
    assert not inspect.isabstract(vcml_Condition)


def test_vcml_condition_constructor_exists():
    assert callable(vcml_Condition.__init__)


def test_vcml_condition_constructor_args():
    sig = inspect.signature(vcml_Condition.__init__)
    params = list(sig.parameters.keys())



def test_vcml_conditionsource_is_not_abstract():
    assert not inspect.isabstract(vcml_ConditionSource)


def test_vcml_conditionsource_constructor_exists():
    assert callable(vcml_ConditionSource.__init__)


def test_vcml_conditionsource_constructor_args():
    sig = inspect.signature(vcml_ConditionSource.__init__)
    params = list(sig.parameters.keys())



def test_vcml_proceduresource_is_not_abstract():
    assert not inspect.isabstract(vcml_ProcedureSource)


def test_vcml_proceduresource_constructor_exists():
    assert callable(vcml_ProcedureSource.__init__)


def test_vcml_proceduresource_constructor_args():
    sig = inspect.signature(vcml_ProcedureSource.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_vcml_dependency_is_not_abstract():
    assert not inspect.isabstract(vcml_Dependency)


def test_vcml_dependency_constructor_exists():
    assert callable(vcml_Dependency.__init__)


def test_vcml_dependency_constructor_args():
    sig = inspect.signature(vcml_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_vcml_numberlistentry_is_not_abstract():
    assert not inspect.isabstract(vcml_NumberListEntry)


def test_vcml_numberlistentry_constructor_exists():
    assert callable(vcml_NumberListEntry.__init__)


def test_vcml_numberlistentry_constructor_args():
    sig = inspect.signature(vcml_NumberListEntry.__init__)
    params = list(sig.parameters.keys())



def test_vcml_datecharacteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml_DateCharacteristicValue)


def test_vcml_datecharacteristicvalue_constructor_exists():
    assert callable(vcml_DateCharacteristicValue.__init__)


def test_vcml_datecharacteristicvalue_constructor_args():
    sig = inspect.signature(vcml_DateCharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "to" in params, "Missing parameter 'to'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_vcml_datecharacteristicvalue_has_default():
    assert hasattr(vcml_DateCharacteristicValue, "default")
    descriptor = None
    for klass in vcml_DateCharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_vcml_datecharacteristicvalue_has_to():
    assert hasattr(vcml_DateCharacteristicValue, "to")
    descriptor = None
    for klass in vcml_DateCharacteristicValue.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_vcml_datecharacteristicvalue_has_from_():
    assert hasattr(vcml_DateCharacteristicValue, "from_")
    descriptor = None
    for klass in vcml_DateCharacteristicValue.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_vcml_characteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicValue)


def test_vcml_characteristicvalue_constructor_exists():
    assert callable(vcml_CharacteristicValue.__init__)


def test_vcml_characteristicvalue_constructor_args():
    sig = inspect.signature(vcml_CharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_characteristicvalue_has_default():
    assert hasattr(vcml_CharacteristicValue, "default")
    descriptor = None
    for klass in vcml_CharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristicvalue_has_name():
    assert hasattr(vcml_CharacteristicValue, "name")
    descriptor = None
    for klass in vcml_CharacteristicValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_numericcharacteristicvalue_is_not_abstract():
    assert not inspect.isabstract(vcml_NumericCharacteristicValue)


def test_vcml_numericcharacteristicvalue_constructor_exists():
    assert callable(vcml_NumericCharacteristicValue.__init__)


def test_vcml_numericcharacteristicvalue_constructor_args():
    sig = inspect.signature(vcml_NumericCharacteristicValue.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_vcml_numericcharacteristicvalue_has_default():
    assert hasattr(vcml_NumericCharacteristicValue, "default")
    descriptor = None
    for klass in vcml_NumericCharacteristicValue.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_vcml_characteristicorvaluedependencies_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicOrValueDependencies)


def test_vcml_characteristicorvaluedependencies_constructor_exists():
    assert callable(vcml_CharacteristicOrValueDependencies.__init__)


def test_vcml_characteristicorvaluedependencies_constructor_args():
    sig = inspect.signature(vcml_CharacteristicOrValueDependencies.__init__)
    params = list(sig.parameters.keys())



def test_vcml_characteristictype_is_not_abstract():
    assert not inspect.isabstract(vcml_CharacteristicType)


def test_vcml_characteristictype_constructor_exists():
    assert callable(vcml_CharacteristicType.__init__)


def test_vcml_characteristictype_constructor_args():
    sig = inspect.signature(vcml_CharacteristicType.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfChars" in params, "Missing parameter 'numberOfChars'"

def test_vcml_characteristictype_has_numberOfChars():
    assert hasattr(vcml_CharacteristicType, "numberOfChars")
    descriptor = None
    for klass in vcml_CharacteristicType.__mro__:
        if "numberOfChars" in klass.__dict__:
            descriptor = klass.__dict__["numberOfChars"]
            break
    assert isinstance(descriptor, property)



def test_vcml_documentation_is_not_abstract():
    assert not inspect.isabstract(vcml_Documentation)


def test_vcml_documentation_constructor_exists():
    assert callable(vcml_Documentation.__init__)


def test_vcml_documentation_constructor_args():
    sig = inspect.signature(vcml_Documentation.__init__)
    params = list(sig.parameters.keys())



def test_bomitem_is_not_abstract():
    assert not inspect.isabstract(BOMItem)


def test_bomitem_constructor_exists():
    assert callable(BOMItem.__init__)


def test_bomitem_constructor_args():
    sig = inspect.signature(BOMItem.__init__)
    params = list(sig.parameters.keys())



def test_vcml_bomitem_class_is_not_abstract():
    assert not inspect.isabstract(vcml_BOMItem_Class)


def test_vcml_bomitem_class_constructor_exists():
    assert callable(vcml_BOMItem_Class.__init__)


def test_vcml_bomitem_class_constructor_args():
    sig = inspect.signature(vcml_BOMItem_Class.__init__)
    params = list(sig.parameters.keys())



def test_vcml_bomitem_material_is_not_abstract():
    assert not inspect.isabstract(vcml_BOMItem_Material)


def test_vcml_bomitem_material_constructor_exists():
    assert callable(vcml_BOMItem_Material.__init__)


def test_vcml_bomitem_material_constructor_args():
    sig = inspect.signature(vcml_BOMItem_Material.__init__)
    params = list(sig.parameters.keys())



def test_vcml_configurationprofileentry_is_not_abstract():
    assert not inspect.isabstract(vcml_ConfigurationProfileEntry)


def test_vcml_configurationprofileentry_constructor_exists():
    assert callable(vcml_ConfigurationProfileEntry.__init__)


def test_vcml_configurationprofileentry_constructor_args():
    sig = inspect.signature(vcml_ConfigurationProfileEntry.__init__)
    params = list(sig.parameters.keys())
    assert "sequence" in params, "Missing parameter 'sequence'"

def test_vcml_configurationprofileentry_has_sequence():
    assert hasattr(vcml_ConfigurationProfileEntry, "sequence")
    descriptor = None
    for klass in vcml_ConfigurationProfileEntry.__mro__:
        if "sequence" in klass.__dict__:
            descriptor = klass.__dict__["sequence"]
            break
    assert isinstance(descriptor, property)



def test_vcml_bomitem_is_not_abstract():
    assert not inspect.isabstract(vcml_BOMItem)


def test_vcml_bomitem_constructor_exists():
    assert callable(vcml_BOMItem.__init__)


def test_vcml_bomitem_constructor_args():
    sig = inspect.signature(vcml_BOMItem.__init__)
    params = list(sig.parameters.keys())
    assert "itemnumber" in params, "Missing parameter 'itemnumber'"

def test_vcml_bomitem_has_itemnumber():
    assert hasattr(vcml_BOMItem, "itemnumber")
    descriptor = None
    for klass in vcml_BOMItem.__mro__:
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



def test_vcml_varianttable_is_not_abstract():
    assert not inspect.isabstract(vcml_VariantTable)


def test_vcml_varianttable_constructor_exists():
    assert callable(vcml_VariantTable.__init__)


def test_vcml_varianttable_constructor_args():
    sig = inspect.signature(vcml_VariantTable.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml_varianttable_has_status():
    assert hasattr(vcml_VariantTable, "status")
    descriptor = None
    for klass in vcml_VariantTable.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_varianttable_has_group():
    assert hasattr(vcml_VariantTable, "group")
    descriptor = None
    for klass in vcml_VariantTable.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml_constraint_is_not_abstract():
    assert not inspect.isabstract(vcml_Constraint)


def test_vcml_constraint_constructor_exists():
    assert callable(vcml_Constraint.__init__)


def test_vcml_constraint_constructor_args():
    sig = inspect.signature(vcml_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml_constraint_has_group():
    assert hasattr(vcml_Constraint, "group")
    descriptor = None
    for klass in vcml_Constraint.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml_constraint_has_status():
    assert hasattr(vcml_Constraint, "status")
    descriptor = None
    for klass in vcml_Constraint.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml_varianttablecontent_is_not_abstract():
    assert not inspect.isabstract(vcml_VariantTableContent)


def test_vcml_varianttablecontent_constructor_exists():
    assert callable(vcml_VariantTableContent.__init__)


def test_vcml_varianttablecontent_constructor_args():
    sig = inspect.signature(vcml_VariantTableContent.__init__)
    params = list(sig.parameters.keys())



def test_vcml_procedure_is_not_abstract():
    assert not inspect.isabstract(vcml_Procedure)


def test_vcml_procedure_constructor_exists():
    assert callable(vcml_Procedure.__init__)


def test_vcml_procedure_constructor_args():
    sig = inspect.signature(vcml_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml_procedure_has_status():
    assert hasattr(vcml_Procedure, "status")
    descriptor = None
    for klass in vcml_Procedure.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_procedure_has_group():
    assert hasattr(vcml_Procedure, "group")
    descriptor = None
    for klass in vcml_Procedure.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml_interfacedesign_is_not_abstract():
    assert not inspect.isabstract(vcml_InterfaceDesign)


def test_vcml_interfacedesign_constructor_exists():
    assert callable(vcml_InterfaceDesign.__init__)


def test_vcml_interfacedesign_constructor_args():
    sig = inspect.signature(vcml_InterfaceDesign.__init__)
    params = list(sig.parameters.keys())



def test_vcml_dependencynet_is_not_abstract():
    assert not inspect.isabstract(vcml_DependencyNet)


def test_vcml_dependencynet_constructor_exists():
    assert callable(vcml_DependencyNet.__init__)


def test_vcml_dependencynet_constructor_args():
    sig = inspect.signature(vcml_DependencyNet.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml_dependencynet_has_status():
    assert hasattr(vcml_DependencyNet, "status")
    descriptor = None
    for klass in vcml_DependencyNet.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_dependencynet_has_group():
    assert hasattr(vcml_DependencyNet, "group")
    descriptor = None
    for klass in vcml_DependencyNet.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml_material_is_not_abstract():
    assert not inspect.isabstract(vcml_Material)


def test_vcml_material_constructor_exists():
    assert callable(vcml_Material.__init__)


def test_vcml_material_constructor_args():
    sig = inspect.signature(vcml_Material.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_vcml_material_has_type():
    assert hasattr(vcml_Material, "type")
    descriptor = None
    for klass in vcml_Material.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_vcml_variantfunction_is_not_abstract():
    assert not inspect.isabstract(vcml_VariantFunction)


def test_vcml_variantfunction_constructor_exists():
    assert callable(vcml_VariantFunction.__init__)


def test_vcml_variantfunction_constructor_args():
    sig = inspect.signature(vcml_VariantFunction.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml_variantfunction_has_group():
    assert hasattr(vcml_VariantFunction, "group")
    descriptor = None
    for klass in vcml_VariantFunction.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml_variantfunction_has_status():
    assert hasattr(vcml_VariantFunction, "status")
    descriptor = None
    for klass in vcml_VariantFunction.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml_selectioncondition_is_not_abstract():
    assert not inspect.isabstract(vcml_SelectionCondition)


def test_vcml_selectioncondition_constructor_exists():
    assert callable(vcml_SelectionCondition.__init__)


def test_vcml_selectioncondition_constructor_args():
    sig = inspect.signature(vcml_SelectionCondition.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml_selectioncondition_has_group():
    assert hasattr(vcml_SelectionCondition, "group")
    descriptor = None
    for klass in vcml_SelectionCondition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml_selectioncondition_has_status():
    assert hasattr(vcml_SelectionCondition, "status")
    descriptor = None
    for klass in vcml_SelectionCondition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml_class_is_not_abstract():
    assert not inspect.isabstract(vcml_Class)


def test_vcml_class_constructor_exists():
    assert callable(vcml_Class.__init__)


def test_vcml_class_constructor_args():
    sig = inspect.signature(vcml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml_class_has_status():
    assert hasattr(vcml_Class, "status")
    descriptor = None
    for klass in vcml_Class.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_class_has_group():
    assert hasattr(vcml_Class, "group")
    descriptor = None
    for klass in vcml_Class.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml_precondition_is_not_abstract():
    assert not inspect.isabstract(vcml_Precondition)


def test_vcml_precondition_constructor_exists():
    assert callable(vcml_Precondition.__init__)


def test_vcml_precondition_constructor_args():
    sig = inspect.signature(vcml_Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "status" in params, "Missing parameter 'status'"

def test_vcml_precondition_has_group():
    assert hasattr(vcml_Precondition, "group")
    descriptor = None
    for klass in vcml_Precondition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_vcml_precondition_has_status():
    assert hasattr(vcml_Precondition, "status")
    descriptor = None
    for klass in vcml_Precondition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_vcml_characteristic_is_not_abstract():
    assert not inspect.isabstract(vcml_Characteristic)


def test_vcml_characteristic_constructor_exists():
    assert callable(vcml_Characteristic.__init__)


def test_vcml_characteristic_constructor_args():
    sig = inspect.signature(vcml_Characteristic.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"
    assert "additionalValues" in params, "Missing parameter 'additionalValues'"
    assert "status" in params, "Missing parameter 'status'"
    assert "required" in params, "Missing parameter 'required'"
    assert "displayAllowedValues" in params, "Missing parameter 'displayAllowedValues'"
    assert "multiValue" in params, "Missing parameter 'multiValue'"
    assert "noDisplay" in params, "Missing parameter 'noDisplay'"
    assert "notReadyForInput" in params, "Missing parameter 'notReadyForInput'"
    assert "field" in params, "Missing parameter 'field'"
    assert "restrictable" in params, "Missing parameter 'restrictable'"
    assert "group" in params, "Missing parameter 'group'"

def test_vcml_characteristic_has_table():
    assert hasattr(vcml_Characteristic, "table")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_additionalValues():
    assert hasattr(vcml_Characteristic, "additionalValues")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "additionalValues" in klass.__dict__:
            descriptor = klass.__dict__["additionalValues"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_status():
    assert hasattr(vcml_Characteristic, "status")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_required():
    assert hasattr(vcml_Characteristic, "required")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_displayAllowedValues():
    assert hasattr(vcml_Characteristic, "displayAllowedValues")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "displayAllowedValues" in klass.__dict__:
            descriptor = klass.__dict__["displayAllowedValues"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_multiValue():
    assert hasattr(vcml_Characteristic, "multiValue")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "multiValue" in klass.__dict__:
            descriptor = klass.__dict__["multiValue"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_noDisplay():
    assert hasattr(vcml_Characteristic, "noDisplay")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "noDisplay" in klass.__dict__:
            descriptor = klass.__dict__["noDisplay"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_notReadyForInput():
    assert hasattr(vcml_Characteristic, "notReadyForInput")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "notReadyForInput" in klass.__dict__:
            descriptor = klass.__dict__["notReadyForInput"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_field():
    assert hasattr(vcml_Characteristic, "field")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_restrictable():
    assert hasattr(vcml_Characteristic, "restrictable")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "restrictable" in klass.__dict__:
            descriptor = klass.__dict__["restrictable"]
            break
    assert isinstance(descriptor, property)

def test_vcml_characteristic_has_group():
    assert hasattr(vcml_Characteristic, "group")
    descriptor = None
    for klass in vcml_Characteristic.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_vcml_configurationprofile_is_not_abstract():
    assert not inspect.isabstract(vcml_ConfigurationProfile)


def test_vcml_configurationprofile_constructor_exists():
    assert callable(vcml_ConfigurationProfile.__init__)


def test_vcml_configurationprofile_constructor_args():
    sig = inspect.signature(vcml_ConfigurationProfile.__init__)
    params = list(sig.parameters.keys())
    assert "bomapplication" in params, "Missing parameter 'bomapplication'"
    assert "status" in params, "Missing parameter 'status'"
    assert "fixing" in params, "Missing parameter 'fixing'"

def test_vcml_configurationprofile_has_bomapplication():
    assert hasattr(vcml_ConfigurationProfile, "bomapplication")
    descriptor = None
    for klass in vcml_ConfigurationProfile.__mro__:
        if "bomapplication" in klass.__dict__:
            descriptor = klass.__dict__["bomapplication"]
            break
    assert isinstance(descriptor, property)

def test_vcml_configurationprofile_has_status():
    assert hasattr(vcml_ConfigurationProfile, "status")
    descriptor = None
    for klass in vcml_ConfigurationProfile.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_vcml_configurationprofile_has_fixing():
    assert hasattr(vcml_ConfigurationProfile, "fixing")
    descriptor = None
    for klass in vcml_ConfigurationProfile.__mro__:
        if "fixing" in klass.__dict__:
            descriptor = klass.__dict__["fixing"]
            break
    assert isinstance(descriptor, property)



def test_vcml_billofmaterial_is_not_abstract():
    assert not inspect.isabstract(vcml_BillOfMaterial)


def test_vcml_billofmaterial_constructor_exists():
    assert callable(vcml_BillOfMaterial.__init__)


def test_vcml_billofmaterial_constructor_args():
    sig = inspect.signature(vcml_BillOfMaterial.__init__)
    params = list(sig.parameters.keys())



def test_vcml_description_is_not_abstract():
    assert not inspect.isabstract(vcml_Description)


def test_vcml_description_constructor_exists():
    assert callable(vcml_Description.__init__)


def test_vcml_description_constructor_args():
    sig = inspect.signature(vcml_Description.__init__)
    params = list(sig.parameters.keys())



def test_characteristictype_is_not_abstract():
    assert not inspect.isabstract(CharacteristicType)


def test_characteristictype_constructor_exists():
    assert callable(CharacteristicType.__init__)


def test_characteristictype_constructor_args():
    sig = inspect.signature(CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_vcml_symbolictype_is_not_abstract():
    assert not inspect.isabstract(vcml_SymbolicType)


def test_vcml_symbolictype_constructor_exists():
    assert callable(vcml_SymbolicType.__init__)


def test_vcml_symbolictype_constructor_args():
    sig = inspect.signature(vcml_SymbolicType.__init__)
    params = list(sig.parameters.keys())
    assert "caseSensitive" in params, "Missing parameter 'caseSensitive'"

def test_vcml_symbolictype_has_caseSensitive():
    assert hasattr(vcml_SymbolicType, "caseSensitive")
    descriptor = None
    for klass in vcml_SymbolicType.__mro__:
        if "caseSensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseSensitive"]
            break
    assert isinstance(descriptor, property)



def test_vcml_datetype_is_not_abstract():
    assert not inspect.isabstract(vcml_DateType)


def test_vcml_datetype_constructor_exists():
    assert callable(vcml_DateType.__init__)


def test_vcml_datetype_constructor_args():
    sig = inspect.signature(vcml_DateType.__init__)
    params = list(sig.parameters.keys())
    assert "intervalValuesAllowed" in params, "Missing parameter 'intervalValuesAllowed'"

def test_vcml_datetype_has_intervalValuesAllowed():
    assert hasattr(vcml_DateType, "intervalValuesAllowed")
    descriptor = None
    for klass in vcml_DateType.__mro__:
        if "intervalValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["intervalValuesAllowed"]
            break
    assert isinstance(descriptor, property)



def test_vcml_numerictype_is_not_abstract():
    assert not inspect.isabstract(vcml_NumericType)


def test_vcml_numerictype_constructor_exists():
    assert callable(vcml_NumericType.__init__)


def test_vcml_numerictype_constructor_args():
    sig = inspect.signature(vcml_NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "negativeValuesAllowed" in params, "Missing parameter 'negativeValuesAllowed'"
    assert "intervalValuesAllowed" in params, "Missing parameter 'intervalValuesAllowed'"
    assert "decimalPlaces" in params, "Missing parameter 'decimalPlaces'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_vcml_numerictype_has_negativeValuesAllowed():
    assert hasattr(vcml_NumericType, "negativeValuesAllowed")
    descriptor = None
    for klass in vcml_NumericType.__mro__:
        if "negativeValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["negativeValuesAllowed"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numerictype_has_intervalValuesAllowed():
    assert hasattr(vcml_NumericType, "intervalValuesAllowed")
    descriptor = None
    for klass in vcml_NumericType.__mro__:
        if "intervalValuesAllowed" in klass.__dict__:
            descriptor = klass.__dict__["intervalValuesAllowed"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numerictype_has_decimalPlaces():
    assert hasattr(vcml_NumericType, "decimalPlaces")
    descriptor = None
    for klass in vcml_NumericType.__mro__:
        if "decimalPlaces" in klass.__dict__:
            descriptor = klass.__dict__["decimalPlaces"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numerictype_has_unit():
    assert hasattr(vcml_NumericType, "unit")
    descriptor = None
    for klass in vcml_NumericType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_vcml_vcobject_is_not_abstract():
    assert not inspect.isabstract(vcml_VCObject)


def test_vcml_vcobject_constructor_exists():
    assert callable(vcml_VCObject.__init__)


def test_vcml_vcobject_constructor_args():
    sig = inspect.signature(vcml_VCObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_vcobject_has_name():
    assert hasattr(vcml_VCObject, "name")
    descriptor = None
    for klass in vcml_VCObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_option_is_not_abstract():
    assert not inspect.isabstract(vcml_Option)


def test_vcml_option_constructor_exists():
    assert callable(vcml_Option.__init__)


def test_vcml_option_constructor_args():
    sig = inspect.signature(vcml_Option.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_vcml_option_has_value():
    assert hasattr(vcml_Option, "value")
    descriptor = None
    for klass in vcml_Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vcml_option_has_name():
    assert hasattr(vcml_Option, "name")
    descriptor = None
    for klass in vcml_Option.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vcml_import_is_not_abstract():
    assert not inspect.isabstract(vcml_Import)


def test_vcml_import_constructor_exists():
    assert callable(vcml_Import.__init__)


def test_vcml_import_constructor_args():
    sig = inspect.signature(vcml_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_vcml_import_has_importURI():
    assert hasattr(vcml_Import, "importURI")
    descriptor = None
    for klass in vcml_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_vcml_vcmlmodel_is_not_abstract():
    assert not inspect.isabstract(vcml_VcmlModel)


def test_vcml_vcmlmodel_constructor_exists():
    assert callable(vcml_VcmlModel.__init__)


def test_vcml_vcmlmodel_constructor_args():
    sig = inspect.signature(vcml_VcmlModel.__init__)
    params = list(sig.parameters.keys())



def test_vcml_binarycondition_is_not_abstract():
    assert not inspect.isabstract(vcml_BinaryCondition)


def test_vcml_binarycondition_constructor_exists():
    assert callable(vcml_BinaryCondition.__init__)


def test_vcml_binarycondition_constructor_args():
    sig = inspect.signature(vcml_BinaryCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml_binarycondition_has_operator():
    assert hasattr(vcml_BinaryCondition, "operator")
    descriptor = None
    for klass in vcml_BinaryCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml_conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(vcml_ConditionalStatement)


def test_vcml_conditionalstatement_constructor_exists():
    assert callable(vcml_ConditionalStatement.__init__)


def test_vcml_conditionalstatement_constructor_args():
    sig = inspect.signature(vcml_ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_vcml_conditionalconstraintrestriction_is_not_abstract():
    assert not inspect.isabstract(vcml_ConditionalConstraintRestriction)


def test_vcml_conditionalconstraintrestriction_constructor_exists():
    assert callable(vcml_ConditionalConstraintRestriction.__init__)


def test_vcml_conditionalconstraintrestriction_constructor_args():
    sig = inspect.signature(vcml_ConditionalConstraintRestriction.__init__)
    params = list(sig.parameters.keys())



def test_list_is_not_abstract():
    assert not inspect.isabstract(List)


def test_list_constructor_exists():
    assert callable(List.__init__)


def test_list_constructor_args():
    sig = inspect.signature(List.__init__)
    params = list(sig.parameters.keys())



def test_vcml_symbollist_is_not_abstract():
    assert not inspect.isabstract(vcml_SymbolList)


def test_vcml_symbollist_constructor_exists():
    assert callable(vcml_SymbolList.__init__)


def test_vcml_symbollist_constructor_args():
    sig = inspect.signature(vcml_SymbolList.__init__)
    params = list(sig.parameters.keys())



def test_vcml_numberlist_is_not_abstract():
    assert not inspect.isabstract(vcml_NumberList)


def test_vcml_numberlist_constructor_exists():
    assert callable(vcml_NumberList.__init__)


def test_vcml_numberlist_constructor_args():
    sig = inspect.signature(vcml_NumberList.__init__)
    params = list(sig.parameters.keys())



def test_vcml_incondition_p_is_not_abstract():
    assert not inspect.isabstract(vcml_InCondition_P)


def test_vcml_incondition_p_constructor_exists():
    assert callable(vcml_InCondition_P.__init__)


def test_vcml_incondition_p_constructor_args():
    sig = inspect.signature(vcml_InCondition_P.__init__)
    params = list(sig.parameters.keys())



def test_vcml_list_is_not_abstract():
    assert not inspect.isabstract(vcml_List)


def test_vcml_list_constructor_exists():
    assert callable(vcml_List.__init__)


def test_vcml_list_constructor_args():
    sig = inspect.signature(vcml_List.__init__)
    params = list(sig.parameters.keys())



def test_vcml_incondition_c_is_not_abstract():
    assert not inspect.isabstract(vcml_InCondition_C)


def test_vcml_incondition_c_constructor_exists():
    assert callable(vcml_InCondition_C.__init__)


def test_vcml_incondition_c_constructor_args():
    sig = inspect.signature(vcml_InCondition_C.__init__)
    params = list(sig.parameters.keys())



def test_vcml_isspecified_p_is_not_abstract():
    assert not inspect.isabstract(vcml_IsSpecified_P)


def test_vcml_isspecified_p_constructor_exists():
    assert callable(vcml_IsSpecified_P.__init__)


def test_vcml_isspecified_p_constructor_args():
    sig = inspect.signature(vcml_IsSpecified_P.__init__)
    params = list(sig.parameters.keys())



def test_vcml_isspecified_c_is_not_abstract():
    assert not inspect.isabstract(vcml_IsSpecified_C)


def test_vcml_isspecified_c_constructor_exists():
    assert callable(vcml_IsSpecified_C.__init__)


def test_vcml_isspecified_c_constructor_args():
    sig = inspect.signature(vcml_IsSpecified_C.__init__)
    params = list(sig.parameters.keys())



def test_vcml_comparison_is_not_abstract():
    assert not inspect.isabstract(vcml_Comparison)


def test_vcml_comparison_constructor_exists():
    assert callable(vcml_Comparison.__init__)


def test_vcml_comparison_constructor_args():
    sig = inspect.signature(vcml_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml_comparison_has_operator():
    assert hasattr(vcml_Comparison, "operator")
    descriptor = None
    for klass in vcml_Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml_unarycondition_is_not_abstract():
    assert not inspect.isabstract(vcml_UnaryCondition)


def test_vcml_unarycondition_constructor_exists():
    assert callable(vcml_UnaryCondition.__init__)


def test_vcml_unarycondition_constructor_args():
    sig = inspect.signature(vcml_UnaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_vcml_symbolicliteral_is_not_abstract():
    assert not inspect.isabstract(vcml_SymbolicLiteral)


def test_vcml_symbolicliteral_constructor_exists():
    assert callable(vcml_SymbolicLiteral.__init__)


def test_vcml_symbolicliteral_constructor_args():
    sig = inspect.signature(vcml_SymbolicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml_symbolicliteral_has_value():
    assert hasattr(vcml_SymbolicLiteral, "value")
    descriptor = None
    for klass in vcml_SymbolicLiteral.__mro__:
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



def test_vcml_numericinterval_is_not_abstract():
    assert not inspect.isabstract(vcml_NumericInterval)


def test_vcml_numericinterval_constructor_exists():
    assert callable(vcml_NumericInterval.__init__)


def test_vcml_numericinterval_constructor_args():
    sig = inspect.signature(vcml_NumericInterval.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBoundOp" in params, "Missing parameter 'lowerBoundOp'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBoundOp" in params, "Missing parameter 'upperBoundOp'"

def test_vcml_numericinterval_has_upperBound():
    assert hasattr(vcml_NumericInterval, "upperBound")
    descriptor = None
    for klass in vcml_NumericInterval.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numericinterval_has_lowerBoundOp():
    assert hasattr(vcml_NumericInterval, "lowerBoundOp")
    descriptor = None
    for klass in vcml_NumericInterval.__mro__:
        if "lowerBoundOp" in klass.__dict__:
            descriptor = klass.__dict__["lowerBoundOp"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numericinterval_has_lowerBound():
    assert hasattr(vcml_NumericInterval, "lowerBound")
    descriptor = None
    for klass in vcml_NumericInterval.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_vcml_numericinterval_has_upperBoundOp():
    assert hasattr(vcml_NumericInterval, "upperBoundOp")
    descriptor = None
    for klass in vcml_NumericInterval.__mro__:
        if "upperBoundOp" in klass.__dict__:
            descriptor = klass.__dict__["upperBoundOp"]
            break
    assert isinstance(descriptor, property)



def test_vcml_numericliteral_is_not_abstract():
    assert not inspect.isabstract(vcml_NumericLiteral)


def test_vcml_numericliteral_constructor_exists():
    assert callable(vcml_NumericLiteral.__init__)


def test_vcml_numericliteral_constructor_args():
    sig = inspect.signature(vcml_NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vcml_numericliteral_has_value():
    assert hasattr(vcml_NumericLiteral, "value")
    descriptor = None
    for klass in vcml_NumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vcml_mdatacharacteristic_p_is_not_abstract():
    assert not inspect.isabstract(vcml_MDataCharacteristic_P)


def test_vcml_mdatacharacteristic_p_constructor_exists():
    assert callable(vcml_MDataCharacteristic_P.__init__)


def test_vcml_mdatacharacteristic_p_constructor_args():
    sig = inspect.signature(vcml_MDataCharacteristic_P.__init__)
    params = list(sig.parameters.keys())



def test_vcml_mdatacharacteristic_c_is_not_abstract():
    assert not inspect.isabstract(vcml_MDataCharacteristic_C)


def test_vcml_mdatacharacteristic_c_constructor_exists():
    assert callable(vcml_MDataCharacteristic_C.__init__)


def test_vcml_mdatacharacteristic_c_constructor_args():
    sig = inspect.signature(vcml_MDataCharacteristic_C.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vcml_literal_is_not_abstract():
    assert not inspect.isabstract(vcml_Literal)


def test_vcml_literal_constructor_exists():
    assert callable(vcml_Literal.__init__)


def test_vcml_literal_constructor_args():
    sig = inspect.signature(vcml_Literal.__init__)
    params = list(sig.parameters.keys())



def test_vcml_functioncall_is_not_abstract():
    assert not inspect.isabstract(vcml_FunctionCall)


def test_vcml_functioncall_constructor_exists():
    assert callable(vcml_FunctionCall.__init__)


def test_vcml_functioncall_constructor_args():
    sig = inspect.signature(vcml_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_vcml_functioncall_has_function():
    assert hasattr(vcml_FunctionCall, "function")
    descriptor = None
    for klass in vcml_FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_vcml_sumparts_is_not_abstract():
    assert not inspect.isabstract(vcml_SumParts)


def test_vcml_sumparts_constructor_exists():
    assert callable(vcml_SumParts.__init__)


def test_vcml_sumparts_constructor_args():
    sig = inspect.signature(vcml_SumParts.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml_sumparts_has_location():
    assert hasattr(vcml_SumParts, "location")
    descriptor = None
    for klass in vcml_SumParts.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(vcml_BinaryExpression)


def test_vcml_binaryexpression_constructor_exists():
    assert callable(vcml_BinaryExpression.__init__)


def test_vcml_binaryexpression_constructor_args():
    sig = inspect.signature(vcml_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml_binaryexpression_has_operator():
    assert hasattr(vcml_BinaryExpression, "operator")
    descriptor = None
    for klass in vcml_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml_countparts_is_not_abstract():
    assert not inspect.isabstract(vcml_CountParts)


def test_vcml_countparts_constructor_exists():
    assert callable(vcml_CountParts.__init__)


def test_vcml_countparts_constructor_args():
    sig = inspect.signature(vcml_CountParts.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml_countparts_has_location():
    assert hasattr(vcml_CountParts, "location")
    descriptor = None
    for klass in vcml_CountParts.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(vcml_UnaryExpression)


def test_vcml_unaryexpression_constructor_exists():
    assert callable(vcml_UnaryExpression.__init__)


def test_vcml_unaryexpression_constructor_args():
    sig = inspect.signature(vcml_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vcml_unaryexpression_has_operator():
    assert hasattr(vcml_UnaryExpression, "operator")
    descriptor = None
    for klass in vcml_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vcml_typeof_is_not_abstract():
    assert not inspect.isabstract(vcml_TypeOf)


def test_vcml_typeof_constructor_exists():
    assert callable(vcml_TypeOf.__init__)


def test_vcml_typeof_constructor_args():
    sig = inspect.signature(vcml_TypeOf.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml_typeof_has_location():
    assert hasattr(vcml_TypeOf, "location")
    descriptor = None
    for klass in vcml_TypeOf.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml_setpricingfactor_is_not_abstract():
    assert not inspect.isabstract(vcml_SetPricingFactor)


def test_vcml_setpricingfactor_constructor_exists():
    assert callable(vcml_SetPricingFactor.__init__)


def test_vcml_setpricingfactor_constructor_args():
    sig = inspect.signature(vcml_SetPricingFactor.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_vcml_setpricingfactor_has_location():
    assert hasattr(vcml_SetPricingFactor, "location")
    descriptor = None
    for klass in vcml_SetPricingFactor.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_vcml_isinvisible_is_not_abstract():
    assert not inspect.isabstract(vcml_IsInvisible)


def test_vcml_isinvisible_constructor_exists():
    assert callable(vcml_IsInvisible.__init__)


def test_vcml_isinvisible_constructor_args():
    sig = inspect.signature(vcml_IsInvisible.__init__)
    params = list(sig.parameters.keys())



def test_setordeldefault_is_not_abstract():
    assert not inspect.isabstract(SetOrDelDefault)


def test_setordeldefault_constructor_exists():
    assert callable(SetOrDelDefault.__init__)


def test_setordeldefault_constructor_args():
    sig = inspect.signature(SetOrDelDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml_deldefault_is_not_abstract():
    assert not inspect.isabstract(vcml_DelDefault)


def test_vcml_deldefault_constructor_exists():
    assert callable(vcml_DelDefault.__init__)


def test_vcml_deldefault_constructor_args():
    sig = inspect.signature(vcml_DelDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml_setdefault_is_not_abstract():
    assert not inspect.isabstract(vcml_SetDefault)


def test_vcml_setdefault_constructor_exists():
    assert callable(vcml_SetDefault.__init__)


def test_vcml_setdefault_constructor_args():
    sig = inspect.signature(vcml_SetDefault.__init__)
    params = list(sig.parameters.keys())



def test_vcml_setordeldefault_is_not_abstract():
    assert not inspect.isabstract(vcml_SetOrDelDefault)


def test_vcml_setordeldefault_constructor_exists():
    assert callable(vcml_SetOrDelDefault.__init__)


def test_vcml_setordeldefault_constructor_args():
    sig = inspect.signature(vcml_SetOrDelDefault.__init__)
    params = list(sig.parameters.keys())



def test_functionortable_is_not_abstract():
    assert not inspect.isabstract(FunctionOrTable)


def test_functionortable_constructor_exists():
    assert callable(FunctionOrTable.__init__)


def test_functionortable_constructor_args():
    sig = inspect.signature(FunctionOrTable.__init__)
    params = list(sig.parameters.keys())



def test_vcml_pfunction_is_not_abstract():
    assert not inspect.isabstract(vcml_PFunction)


def test_vcml_pfunction_constructor_exists():
    assert callable(vcml_PFunction.__init__)


def test_vcml_pfunction_constructor_args():
    sig = inspect.signature(vcml_PFunction.__init__)
    params = list(sig.parameters.keys())



def test_vcml_table_is_not_abstract():
    assert not inspect.isabstract(vcml_Table)


def test_vcml_table_constructor_exists():
    assert callable(vcml_Table.__init__)


def test_vcml_table_constructor_args():
    sig = inspect.signature(vcml_Table.__init__)
    params = list(sig.parameters.keys())



def test_vcml_function_is_not_abstract():
    assert not inspect.isabstract(vcml_Function)


def test_vcml_function_constructor_exists():
    assert callable(vcml_Function.__init__)


def test_vcml_function_constructor_args():
    sig = inspect.signature(vcml_Function.__init__)
    params = list(sig.parameters.keys())

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "Released",
        "Locked",
        "InPreparation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_functionname_exists():
    # Check that the Enumeration exists
    assert FunctionName is not None

def test_functionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionName]
    expected_literals = [
        "SIN",
        "ARCCOS",
        "LOG10",
        "LN",
        "TAN",
        "COS",
        "TRUNK",
        "SIGN",
        "ABS",
        "FLOOR",
        "EXP",
        "FRAC",
        "CEIL",
        "SQRT",
        "ARCTAN",
        "ARCSIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionName"

def test_fixing_exists():
    # Check that the Enumeration exists
    assert Fixing is not None

def test_fixing_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Fixing]
    expected_literals = [
        "TopDown",
        "BottomUp",
        "None_",
        "Entry",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Fixing"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "HR",
        "CS",
        "AR",
        "TH",
        "RU",
        "MS",
        "ZH",
        "ZF",
        "NO",
        "SK",
        "EN",
        "ET",
        "SR",
        "AF",
        "NL",
        "HE",
        "Z1",
        "FI",
        "DA",
        "LV",
        "SL",
        "ID",
        "SV",
        "JA",
        "ES",
        "UK",
        "CA",
        "IT",
        "DE",
        "KO",
        "RO",
        "BG",
        "FR",
        "PT",
        "IS",
        "EL",
        "PL",
        "SH",
        "HU",
        "LT",
        "TR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "GE",
        "LT",
        "GT",
        "NE",
        "EQ",
        "LE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_optiontype_exists():
    # Check that the Enumeration exists
    assert OptionType is not None

def test_optiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptionType]
    expected_literals = [
        "ECM",
        "KeyDate",
        "UPS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptionType"

def test_procedurelocation_exists():
    # Check that the Enumeration exists
    assert ProcedureLocation is not None

def test_procedurelocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureLocation]
    expected_literals = [
        "ROOT",
        "SELF",
        "PARENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureLocation"

def test_unaryexpressionoperator_exists():
    # Check that the Enumeration exists
    assert UnaryExpressionOperator is not None

def test_unaryexpressionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryExpressionOperator]
    expected_literals = [
        "UC",
        "PLUS",
        "LC",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryExpressionOperator"


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
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
vcml_Assignment_strategy = st.builds(
    vcml_Assignment,
)
Statement_strategy = st.builds(
    Statement,
)
vcml_SimpleStatement_strategy = st.builds(
    vcml_SimpleStatement,
)
vcml_CompoundStatement_strategy = st.builds(
    vcml_CompoundStatement,
)
vcml_Statement_strategy = st.builds(
    vcml_Statement,
)
CharacteristicReference_C_strategy = st.builds(
    CharacteristicReference_C,
)
vcml_ShortVarReference_strategy = st.builds(
    vcml_ShortVarReference,
)
vcml_ObjectCharacteristicReference_strategy = st.builds(
    vcml_ObjectCharacteristicReference,
)
Literal_strategy = st.builds(
    Literal,
)
vcml_CharacteristicReference_P_strategy = st.builds(
    vcml_CharacteristicReference_P,
    location=
        safe_text
)
vcml_EObject_strategy = st.builds(
    vcml_EObject,
)
Condition_strategy = st.builds(
    Condition,
)
ConstraintRestriction_strategy = st.builds(
    ConstraintRestriction,
)
vcml_SubpartOfCondition_strategy = st.builds(
    vcml_SubpartOfCondition,
)
vcml_ConstraintRestrictionFalse_strategy = st.builds(
    vcml_ConstraintRestrictionFalse,
)
vcml_NegatedConstraintRestrictionLHS_strategy = st.builds(
    vcml_NegatedConstraintRestrictionLHS,
)
vcml_PartOfCondition_strategy = st.builds(
    vcml_PartOfCondition,
)
vcml_PartialKey_strategy = st.builds(
    vcml_PartialKey,
    key=
        safe_text
)
vcml_FunctionOrTable_strategy = st.builds(
    vcml_FunctionOrTable,
)
vcml_Expression_strategy = st.builds(
    vcml_Expression,
)
ConstraintObject_strategy = st.builds(
    ConstraintObject,
)
vcml_ConstraintClass_strategy = st.builds(
    vcml_ConstraintClass,
)
vcml_ShortVarDefinition_strategy = st.builds(
    vcml_ShortVarDefinition,
    name=
        safe_text
)
vcml_CharacteristicReference_C_strategy = st.builds(
    vcml_CharacteristicReference_C,
)
vcml_ConstraintRestriction_strategy = st.builds(
    vcml_ConstraintRestriction,
)
vcml_ConstraintObject_strategy = st.builds(
    vcml_ConstraintObject,
    name=
        safe_text
)
vcml_FormattedDocumentationBlock_strategy = st.builds(
    vcml_FormattedDocumentationBlock,
    value=
        safe_text,
    format=
        safe_text
)
vcml_MultipleLanguageDocumentation_LanguageBlock_strategy = st.builds(
    vcml_MultipleLanguageDocumentation_LanguageBlock,
    language=
        safe_text
)
Documentation_strategy = st.builds(
    Documentation,
)
vcml_MultipleLanguageDocumentation_strategy = st.builds(
    vcml_MultipleLanguageDocumentation,
)
vcml_SimpleDocumentation_strategy = st.builds(
    vcml_SimpleDocumentation,
    value=
        safe_text
)
vcml_ObjectType_strategy = st.builds(
    vcml_ObjectType,
    classType=
        st.integers(),
    type=
        safe_text
)
vcml_ConstraintMaterial_strategy = st.builds(
    vcml_ConstraintMaterial,
)
vcml_MultiLanguageDescription_strategy = st.builds(
    vcml_MultiLanguageDescription,
    value=
        safe_text,
    language=
        safe_text
)
Description_strategy = st.builds(
    Description,
)
vcml_MultiLanguageDescriptions_strategy = st.builds(
    vcml_MultiLanguageDescriptions,
)
vcml_SimpleDescription_strategy = st.builds(
    vcml_SimpleDescription,
    value=
        safe_text
)
vcml_Row_strategy = st.builds(
    vcml_Row,
)
vcml_VariantTableArgument_strategy = st.builds(
    vcml_VariantTableArgument,
    key=
        st.booleans()
)
vcml_VariantFunctionArgument_strategy = st.builds(
    vcml_VariantFunctionArgument,
    in_=
        st.booleans()
)
vcml_ValueAssignment_strategy = st.builds(
    vcml_ValueAssignment,
)
vcml_Classification_strategy = st.builds(
    vcml_Classification,
)
vcml_CharacteristicGroup_strategy = st.builds(
    vcml_CharacteristicGroup,
    name=
        safe_text
)
vcml_ConstraintSource_strategy = st.builds(
    vcml_ConstraintSource,
)
vcml_Condition_strategy = st.builds(
    vcml_Condition,
)
vcml_ConditionSource_strategy = st.builds(
    vcml_ConditionSource,
)
vcml_ProcedureSource_strategy = st.builds(
    vcml_ProcedureSource,
)
Dependency_strategy = st.builds(
    Dependency,
)
vcml_Dependency_strategy = st.builds(
    vcml_Dependency,
)
vcml_NumberListEntry_strategy = st.builds(
    vcml_NumberListEntry,
)
vcml_DateCharacteristicValue_strategy = st.builds(
    vcml_DateCharacteristicValue,
    default=
        st.booleans(),
    to=
        safe_text,
    from_=
        safe_text
)
vcml_CharacteristicValue_strategy = st.builds(
    vcml_CharacteristicValue,
    default=
        st.booleans(),
    name=
        safe_text
)
vcml_NumericCharacteristicValue_strategy = st.builds(
    vcml_NumericCharacteristicValue,
    default=
        st.booleans()
)
vcml_CharacteristicOrValueDependencies_strategy = st.builds(
    vcml_CharacteristicOrValueDependencies,
)
vcml_CharacteristicType_strategy = st.builds(
    vcml_CharacteristicType,
    numberOfChars=
        st.integers()
)
vcml_Documentation_strategy = st.builds(
    vcml_Documentation,
)
BOMItem_strategy = st.builds(
    BOMItem,
)
vcml_BOMItem_Class_strategy = st.builds(
    vcml_BOMItem_Class,
)
vcml_BOMItem_Material_strategy = st.builds(
    vcml_BOMItem_Material,
)
vcml_ConfigurationProfileEntry_strategy = st.builds(
    vcml_ConfigurationProfileEntry,
    sequence=
        st.integers()
)
vcml_BOMItem_strategy = st.builds(
    vcml_BOMItem,
    itemnumber=
        st.integers()
)
VCObject_strategy = st.builds(
    VCObject,
)
vcml_VariantTable_strategy = st.builds(
    vcml_VariantTable,
    status=
        safe_text,
    group=
        safe_text
)
vcml_Constraint_strategy = st.builds(
    vcml_Constraint,
    group=
        safe_text,
    status=
        safe_text
)
vcml_VariantTableContent_strategy = st.builds(
    vcml_VariantTableContent,
)
vcml_Procedure_strategy = st.builds(
    vcml_Procedure,
    status=
        safe_text,
    group=
        safe_text
)
vcml_InterfaceDesign_strategy = st.builds(
    vcml_InterfaceDesign,
)
vcml_DependencyNet_strategy = st.builds(
    vcml_DependencyNet,
    status=
        safe_text,
    group=
        safe_text
)
vcml_Material_strategy = st.builds(
    vcml_Material,
    type=
        safe_text
)
vcml_VariantFunction_strategy = st.builds(
    vcml_VariantFunction,
    group=
        safe_text,
    status=
        safe_text
)
vcml_SelectionCondition_strategy = st.builds(
    vcml_SelectionCondition,
    group=
        safe_text,
    status=
        safe_text
)
vcml_Class_strategy = st.builds(
    vcml_Class,
    status=
        safe_text,
    group=
        safe_text
)
vcml_Precondition_strategy = st.builds(
    vcml_Precondition,
    group=
        safe_text,
    status=
        safe_text
)
vcml_Characteristic_strategy = st.builds(
    vcml_Characteristic,
    table=
        safe_text,
    additionalValues=
        st.booleans(),
    status=
        safe_text,
    required=
        st.booleans(),
    displayAllowedValues=
        st.booleans(),
    multiValue=
        st.booleans(),
    noDisplay=
        st.booleans(),
    notReadyForInput=
        st.booleans(),
    field=
        safe_text,
    restrictable=
        st.booleans(),
    group=
        safe_text
)
vcml_ConfigurationProfile_strategy = st.builds(
    vcml_ConfigurationProfile,
    bomapplication=
        safe_text,
    status=
        safe_text,
    fixing=
        safe_text
)
vcml_BillOfMaterial_strategy = st.builds(
    vcml_BillOfMaterial,
)
vcml_Description_strategy = st.builds(
    vcml_Description,
)
CharacteristicType_strategy = st.builds(
    CharacteristicType,
)
vcml_SymbolicType_strategy = st.builds(
    vcml_SymbolicType,
    caseSensitive=
        st.booleans()
)
vcml_DateType_strategy = st.builds(
    vcml_DateType,
    intervalValuesAllowed=
        st.booleans()
)
vcml_NumericType_strategy = st.builds(
    vcml_NumericType,
    negativeValuesAllowed=
        st.booleans(),
    intervalValuesAllowed=
        st.booleans(),
    decimalPlaces=
        st.integers(),
    unit=
        safe_text
)
vcml_VCObject_strategy = st.builds(
    vcml_VCObject,
    name=
        safe_text
)
vcml_Option_strategy = st.builds(
    vcml_Option,
    value=
        safe_text,
    name=
        safe_text
)
vcml_Import_strategy = st.builds(
    vcml_Import,
    importURI=
        safe_text
)
vcml_VcmlModel_strategy = st.builds(
    vcml_VcmlModel,
)
vcml_BinaryCondition_strategy = st.builds(
    vcml_BinaryCondition,
    operator=
        safe_text
)
vcml_ConditionalStatement_strategy = st.builds(
    vcml_ConditionalStatement,
)
vcml_ConditionalConstraintRestriction_strategy = st.builds(
    vcml_ConditionalConstraintRestriction,
)
List_strategy = st.builds(
    List,
)
vcml_SymbolList_strategy = st.builds(
    vcml_SymbolList,
)
vcml_NumberList_strategy = st.builds(
    vcml_NumberList,
)
vcml_InCondition_P_strategy = st.builds(
    vcml_InCondition_P,
)
vcml_List_strategy = st.builds(
    vcml_List,
)
vcml_InCondition_C_strategy = st.builds(
    vcml_InCondition_C,
)
vcml_IsSpecified_P_strategy = st.builds(
    vcml_IsSpecified_P,
)
vcml_IsSpecified_C_strategy = st.builds(
    vcml_IsSpecified_C,
)
vcml_Comparison_strategy = st.builds(
    vcml_Comparison,
    operator=
        safe_text
)
vcml_UnaryCondition_strategy = st.builds(
    vcml_UnaryCondition,
)
vcml_SymbolicLiteral_strategy = st.builds(
    vcml_SymbolicLiteral,
    value=
        safe_text
)
NumberListEntry_strategy = st.builds(
    NumberListEntry,
)
vcml_NumericInterval_strategy = st.builds(
    vcml_NumericInterval,
    upperBound=
        safe_text,
    lowerBoundOp=
        safe_text,
    lowerBound=
        safe_text,
    upperBoundOp=
        safe_text
)
vcml_NumericLiteral_strategy = st.builds(
    vcml_NumericLiteral,
    value=
        safe_text
)
vcml_MDataCharacteristic_P_strategy = st.builds(
    vcml_MDataCharacteristic_P,
)
vcml_MDataCharacteristic_C_strategy = st.builds(
    vcml_MDataCharacteristic_C,
)
Expression_strategy = st.builds(
    Expression,
)
vcml_Literal_strategy = st.builds(
    vcml_Literal,
)
vcml_FunctionCall_strategy = st.builds(
    vcml_FunctionCall,
    function=
        safe_text
)
vcml_SumParts_strategy = st.builds(
    vcml_SumParts,
    location=
        safe_text
)
vcml_BinaryExpression_strategy = st.builds(
    vcml_BinaryExpression,
    operator=
        safe_text
)
vcml_CountParts_strategy = st.builds(
    vcml_CountParts,
    location=
        safe_text
)
vcml_UnaryExpression_strategy = st.builds(
    vcml_UnaryExpression,
    operator=
        safe_text
)
vcml_TypeOf_strategy = st.builds(
    vcml_TypeOf,
    location=
        safe_text
)
vcml_SetPricingFactor_strategy = st.builds(
    vcml_SetPricingFactor,
    location=
        safe_text
)
vcml_IsInvisible_strategy = st.builds(
    vcml_IsInvisible,
)
SetOrDelDefault_strategy = st.builds(
    SetOrDelDefault,
)
vcml_DelDefault_strategy = st.builds(
    vcml_DelDefault,
)
vcml_SetDefault_strategy = st.builds(
    vcml_SetDefault,
)
vcml_SetOrDelDefault_strategy = st.builds(
    vcml_SetOrDelDefault,
)
FunctionOrTable_strategy = st.builds(
    FunctionOrTable,
)
vcml_PFunction_strategy = st.builds(
    vcml_PFunction,
)
vcml_Table_strategy = st.builds(
    vcml_Table,
)
vcml_Function_strategy = st.builds(
    vcml_Function,
)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=vcml_Assignment_strategy)
@settings(max_examples=50)
def test_vcml_assignment_instantiation(instance):
    assert isinstance(instance, vcml_Assignment)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=vcml_SimpleStatement_strategy)
@settings(max_examples=50)
def test_vcml_simplestatement_instantiation(instance):
    assert isinstance(instance, vcml_SimpleStatement)

@given(instance=vcml_CompoundStatement_strategy)
@settings(max_examples=50)
def test_vcml_compoundstatement_instantiation(instance):
    assert isinstance(instance, vcml_CompoundStatement)

@given(instance=vcml_Statement_strategy)
@settings(max_examples=50)
def test_vcml_statement_instantiation(instance):
    assert isinstance(instance, vcml_Statement)

@given(instance=CharacteristicReference_C_strategy)
@settings(max_examples=50)
def test_characteristicreference_c_instantiation(instance):
    assert isinstance(instance, CharacteristicReference_C)

@given(instance=vcml_ShortVarReference_strategy)
@settings(max_examples=50)
def test_vcml_shortvarreference_instantiation(instance):
    assert isinstance(instance, vcml_ShortVarReference)

@given(instance=vcml_ObjectCharacteristicReference_strategy)
@settings(max_examples=50)
def test_vcml_objectcharacteristicreference_instantiation(instance):
    assert isinstance(instance, vcml_ObjectCharacteristicReference)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=vcml_CharacteristicReference_P_strategy)
@settings(max_examples=50)
def test_vcml_characteristicreference_p_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicReference_P)



@given(instance=vcml_CharacteristicReference_P_strategy)
def test_vcml_characteristicreference_p_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml_EObject_strategy)
@settings(max_examples=50)
def test_vcml_eobject_instantiation(instance):
    assert isinstance(instance, vcml_EObject)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=ConstraintRestriction_strategy)
@settings(max_examples=50)
def test_constraintrestriction_instantiation(instance):
    assert isinstance(instance, ConstraintRestriction)

@given(instance=vcml_SubpartOfCondition_strategy)
@settings(max_examples=50)
def test_vcml_subpartofcondition_instantiation(instance):
    assert isinstance(instance, vcml_SubpartOfCondition)

@given(instance=vcml_ConstraintRestrictionFalse_strategy)
@settings(max_examples=50)
def test_vcml_constraintrestrictionfalse_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintRestrictionFalse)

@given(instance=vcml_NegatedConstraintRestrictionLHS_strategy)
@settings(max_examples=50)
def test_vcml_negatedconstraintrestrictionlhs_instantiation(instance):
    assert isinstance(instance, vcml_NegatedConstraintRestrictionLHS)

@given(instance=vcml_PartOfCondition_strategy)
@settings(max_examples=50)
def test_vcml_partofcondition_instantiation(instance):
    assert isinstance(instance, vcml_PartOfCondition)

@given(instance=vcml_PartialKey_strategy)
@settings(max_examples=50)
def test_vcml_partialkey_instantiation(instance):
    assert isinstance(instance, vcml_PartialKey)



@given(instance=vcml_PartialKey_strategy)
def test_vcml_partialkey_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=vcml_FunctionOrTable_strategy)
@settings(max_examples=50)
def test_vcml_functionortable_instantiation(instance):
    assert isinstance(instance, vcml_FunctionOrTable)

@given(instance=vcml_Expression_strategy)
@settings(max_examples=50)
def test_vcml_expression_instantiation(instance):
    assert isinstance(instance, vcml_Expression)

@given(instance=ConstraintObject_strategy)
@settings(max_examples=50)
def test_constraintobject_instantiation(instance):
    assert isinstance(instance, ConstraintObject)

@given(instance=vcml_ConstraintClass_strategy)
@settings(max_examples=50)
def test_vcml_constraintclass_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintClass)

@given(instance=vcml_ShortVarDefinition_strategy)
@settings(max_examples=50)
def test_vcml_shortvardefinition_instantiation(instance):
    assert isinstance(instance, vcml_ShortVarDefinition)



@given(instance=vcml_ShortVarDefinition_strategy)
def test_vcml_shortvardefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_CharacteristicReference_C_strategy)
@settings(max_examples=50)
def test_vcml_characteristicreference_c_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicReference_C)

@given(instance=vcml_ConstraintRestriction_strategy)
@settings(max_examples=50)
def test_vcml_constraintrestriction_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintRestriction)

@given(instance=vcml_ConstraintObject_strategy)
@settings(max_examples=50)
def test_vcml_constraintobject_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintObject)



@given(instance=vcml_ConstraintObject_strategy)
def test_vcml_constraintobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_FormattedDocumentationBlock_strategy)
@settings(max_examples=50)
def test_vcml_formatteddocumentationblock_instantiation(instance):
    assert isinstance(instance, vcml_FormattedDocumentationBlock)



@given(instance=vcml_FormattedDocumentationBlock_strategy)
def test_vcml_formatteddocumentationblock_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=vcml_FormattedDocumentationBlock_strategy)
def test_vcml_formatteddocumentationblock_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=vcml_MultipleLanguageDocumentation_LanguageBlock_strategy)
@settings(max_examples=50)
def test_vcml_multiplelanguagedocumentation_languageblock_instantiation(instance):
    assert isinstance(instance, vcml_MultipleLanguageDocumentation_LanguageBlock)



@given(instance=vcml_MultipleLanguageDocumentation_LanguageBlock_strategy)
def test_vcml_multiplelanguagedocumentation_languageblock_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Documentation_strategy)
@settings(max_examples=50)
def test_documentation_instantiation(instance):
    assert isinstance(instance, Documentation)

@given(instance=vcml_MultipleLanguageDocumentation_strategy)
@settings(max_examples=50)
def test_vcml_multiplelanguagedocumentation_instantiation(instance):
    assert isinstance(instance, vcml_MultipleLanguageDocumentation)

@given(instance=vcml_SimpleDocumentation_strategy)
@settings(max_examples=50)
def test_vcml_simpledocumentation_instantiation(instance):
    assert isinstance(instance, vcml_SimpleDocumentation)



@given(instance=vcml_SimpleDocumentation_strategy)
def test_vcml_simpledocumentation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml_ObjectType_strategy)
@settings(max_examples=50)
def test_vcml_objecttype_instantiation(instance):
    assert isinstance(instance, vcml_ObjectType)



@given(instance=vcml_ObjectType_strategy)
def test_vcml_objecttype_classType_setter(instance):
    original = instance.classType
    instance.classType = original
    assert instance.classType == original



@given(instance=vcml_ObjectType_strategy)
def test_vcml_objecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vcml_ConstraintMaterial_strategy)
@settings(max_examples=50)
def test_vcml_constraintmaterial_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintMaterial)

@given(instance=vcml_MultiLanguageDescription_strategy)
@settings(max_examples=50)
def test_vcml_multilanguagedescription_instantiation(instance):
    assert isinstance(instance, vcml_MultiLanguageDescription)



@given(instance=vcml_MultiLanguageDescription_strategy)
def test_vcml_multilanguagedescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=vcml_MultiLanguageDescription_strategy)
def test_vcml_multilanguagedescription_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Description_strategy)
@settings(max_examples=50)
def test_description_instantiation(instance):
    assert isinstance(instance, Description)

@given(instance=vcml_MultiLanguageDescriptions_strategy)
@settings(max_examples=50)
def test_vcml_multilanguagedescriptions_instantiation(instance):
    assert isinstance(instance, vcml_MultiLanguageDescriptions)

@given(instance=vcml_SimpleDescription_strategy)
@settings(max_examples=50)
def test_vcml_simpledescription_instantiation(instance):
    assert isinstance(instance, vcml_SimpleDescription)



@given(instance=vcml_SimpleDescription_strategy)
def test_vcml_simpledescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml_Row_strategy)
@settings(max_examples=50)
def test_vcml_row_instantiation(instance):
    assert isinstance(instance, vcml_Row)

@given(instance=vcml_VariantTableArgument_strategy)
@settings(max_examples=50)
def test_vcml_varianttableargument_instantiation(instance):
    assert isinstance(instance, vcml_VariantTableArgument)



@given(instance=vcml_VariantTableArgument_strategy)
def test_vcml_varianttableargument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=vcml_VariantFunctionArgument_strategy)
@settings(max_examples=50)
def test_vcml_variantfunctionargument_instantiation(instance):
    assert isinstance(instance, vcml_VariantFunctionArgument)



@given(instance=vcml_VariantFunctionArgument_strategy)
def test_vcml_variantfunctionargument_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=vcml_ValueAssignment_strategy)
@settings(max_examples=50)
def test_vcml_valueassignment_instantiation(instance):
    assert isinstance(instance, vcml_ValueAssignment)

@given(instance=vcml_Classification_strategy)
@settings(max_examples=50)
def test_vcml_classification_instantiation(instance):
    assert isinstance(instance, vcml_Classification)

@given(instance=vcml_CharacteristicGroup_strategy)
@settings(max_examples=50)
def test_vcml_characteristicgroup_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicGroup)



@given(instance=vcml_CharacteristicGroup_strategy)
def test_vcml_characteristicgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_ConstraintSource_strategy)
@settings(max_examples=50)
def test_vcml_constraintsource_instantiation(instance):
    assert isinstance(instance, vcml_ConstraintSource)

@given(instance=vcml_Condition_strategy)
@settings(max_examples=50)
def test_vcml_condition_instantiation(instance):
    assert isinstance(instance, vcml_Condition)

@given(instance=vcml_ConditionSource_strategy)
@settings(max_examples=50)
def test_vcml_conditionsource_instantiation(instance):
    assert isinstance(instance, vcml_ConditionSource)

@given(instance=vcml_ProcedureSource_strategy)
@settings(max_examples=50)
def test_vcml_proceduresource_instantiation(instance):
    assert isinstance(instance, vcml_ProcedureSource)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=vcml_Dependency_strategy)
@settings(max_examples=50)
def test_vcml_dependency_instantiation(instance):
    assert isinstance(instance, vcml_Dependency)

@given(instance=vcml_NumberListEntry_strategy)
@settings(max_examples=50)
def test_vcml_numberlistentry_instantiation(instance):
    assert isinstance(instance, vcml_NumberListEntry)

@given(instance=vcml_DateCharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml_datecharacteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml_DateCharacteristicValue)



@given(instance=vcml_DateCharacteristicValue_strategy)
def test_vcml_datecharacteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=vcml_DateCharacteristicValue_strategy)
def test_vcml_datecharacteristicvalue_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=vcml_DateCharacteristicValue_strategy)
def test_vcml_datecharacteristicvalue_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=vcml_CharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml_characteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicValue)



@given(instance=vcml_CharacteristicValue_strategy)
def test_vcml_characteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=vcml_CharacteristicValue_strategy)
def test_vcml_characteristicvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_NumericCharacteristicValue_strategy)
@settings(max_examples=50)
def test_vcml_numericcharacteristicvalue_instantiation(instance):
    assert isinstance(instance, vcml_NumericCharacteristicValue)



@given(instance=vcml_NumericCharacteristicValue_strategy)
def test_vcml_numericcharacteristicvalue_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=vcml_CharacteristicOrValueDependencies_strategy)
@settings(max_examples=50)
def test_vcml_characteristicorvaluedependencies_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicOrValueDependencies)

@given(instance=vcml_CharacteristicType_strategy)
@settings(max_examples=50)
def test_vcml_characteristictype_instantiation(instance):
    assert isinstance(instance, vcml_CharacteristicType)



@given(instance=vcml_CharacteristicType_strategy)
def test_vcml_characteristictype_numberOfChars_setter(instance):
    original = instance.numberOfChars
    instance.numberOfChars = original
    assert instance.numberOfChars == original

@given(instance=vcml_Documentation_strategy)
@settings(max_examples=50)
def test_vcml_documentation_instantiation(instance):
    assert isinstance(instance, vcml_Documentation)

@given(instance=BOMItem_strategy)
@settings(max_examples=50)
def test_bomitem_instantiation(instance):
    assert isinstance(instance, BOMItem)

@given(instance=vcml_BOMItem_Class_strategy)
@settings(max_examples=50)
def test_vcml_bomitem_class_instantiation(instance):
    assert isinstance(instance, vcml_BOMItem_Class)

@given(instance=vcml_BOMItem_Material_strategy)
@settings(max_examples=50)
def test_vcml_bomitem_material_instantiation(instance):
    assert isinstance(instance, vcml_BOMItem_Material)

@given(instance=vcml_ConfigurationProfileEntry_strategy)
@settings(max_examples=50)
def test_vcml_configurationprofileentry_instantiation(instance):
    assert isinstance(instance, vcml_ConfigurationProfileEntry)



@given(instance=vcml_ConfigurationProfileEntry_strategy)
def test_vcml_configurationprofileentry_sequence_setter(instance):
    original = instance.sequence
    instance.sequence = original
    assert instance.sequence == original

@given(instance=vcml_BOMItem_strategy)
@settings(max_examples=50)
def test_vcml_bomitem_instantiation(instance):
    assert isinstance(instance, vcml_BOMItem)



@given(instance=vcml_BOMItem_strategy)
def test_vcml_bomitem_itemnumber_setter(instance):
    original = instance.itemnumber
    instance.itemnumber = original
    assert instance.itemnumber == original

@given(instance=VCObject_strategy)
@settings(max_examples=50)
def test_vcobject_instantiation(instance):
    assert isinstance(instance, VCObject)

@given(instance=vcml_VariantTable_strategy)
@settings(max_examples=50)
def test_vcml_varianttable_instantiation(instance):
    assert isinstance(instance, vcml_VariantTable)



@given(instance=vcml_VariantTable_strategy)
def test_vcml_varianttable_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_VariantTable_strategy)
def test_vcml_varianttable_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml_Constraint_strategy)
@settings(max_examples=50)
def test_vcml_constraint_instantiation(instance):
    assert isinstance(instance, vcml_Constraint)



@given(instance=vcml_Constraint_strategy)
def test_vcml_constraint_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=vcml_Constraint_strategy)
def test_vcml_constraint_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml_VariantTableContent_strategy)
@settings(max_examples=50)
def test_vcml_varianttablecontent_instantiation(instance):
    assert isinstance(instance, vcml_VariantTableContent)

@given(instance=vcml_Procedure_strategy)
@settings(max_examples=50)
def test_vcml_procedure_instantiation(instance):
    assert isinstance(instance, vcml_Procedure)



@given(instance=vcml_Procedure_strategy)
def test_vcml_procedure_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_Procedure_strategy)
def test_vcml_procedure_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml_InterfaceDesign_strategy)
@settings(max_examples=50)
def test_vcml_interfacedesign_instantiation(instance):
    assert isinstance(instance, vcml_InterfaceDesign)

@given(instance=vcml_DependencyNet_strategy)
@settings(max_examples=50)
def test_vcml_dependencynet_instantiation(instance):
    assert isinstance(instance, vcml_DependencyNet)



@given(instance=vcml_DependencyNet_strategy)
def test_vcml_dependencynet_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_DependencyNet_strategy)
def test_vcml_dependencynet_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml_Material_strategy)
@settings(max_examples=50)
def test_vcml_material_instantiation(instance):
    assert isinstance(instance, vcml_Material)



@given(instance=vcml_Material_strategy)
def test_vcml_material_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vcml_VariantFunction_strategy)
@settings(max_examples=50)
def test_vcml_variantfunction_instantiation(instance):
    assert isinstance(instance, vcml_VariantFunction)



@given(instance=vcml_VariantFunction_strategy)
def test_vcml_variantfunction_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=vcml_VariantFunction_strategy)
def test_vcml_variantfunction_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml_SelectionCondition_strategy)
@settings(max_examples=50)
def test_vcml_selectioncondition_instantiation(instance):
    assert isinstance(instance, vcml_SelectionCondition)



@given(instance=vcml_SelectionCondition_strategy)
def test_vcml_selectioncondition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=vcml_SelectionCondition_strategy)
def test_vcml_selectioncondition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml_Class_strategy)
@settings(max_examples=50)
def test_vcml_class_instantiation(instance):
    assert isinstance(instance, vcml_Class)



@given(instance=vcml_Class_strategy)
def test_vcml_class_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_Class_strategy)
def test_vcml_class_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml_Precondition_strategy)
@settings(max_examples=50)
def test_vcml_precondition_instantiation(instance):
    assert isinstance(instance, vcml_Precondition)



@given(instance=vcml_Precondition_strategy)
def test_vcml_precondition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=vcml_Precondition_strategy)
def test_vcml_precondition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=vcml_Characteristic_strategy)
@settings(max_examples=50)
def test_vcml_characteristic_instantiation(instance):
    assert isinstance(instance, vcml_Characteristic)



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_additionalValues_setter(instance):
    original = instance.additionalValues
    instance.additionalValues = original
    assert instance.additionalValues == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_displayAllowedValues_setter(instance):
    original = instance.displayAllowedValues
    instance.displayAllowedValues = original
    assert instance.displayAllowedValues == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_multiValue_setter(instance):
    original = instance.multiValue
    instance.multiValue = original
    assert instance.multiValue == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_noDisplay_setter(instance):
    original = instance.noDisplay
    instance.noDisplay = original
    assert instance.noDisplay == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_notReadyForInput_setter(instance):
    original = instance.notReadyForInput
    instance.notReadyForInput = original
    assert instance.notReadyForInput == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_restrictable_setter(instance):
    original = instance.restrictable
    instance.restrictable = original
    assert instance.restrictable == original



@given(instance=vcml_Characteristic_strategy)
def test_vcml_characteristic_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=vcml_ConfigurationProfile_strategy)
@settings(max_examples=50)
def test_vcml_configurationprofile_instantiation(instance):
    assert isinstance(instance, vcml_ConfigurationProfile)



@given(instance=vcml_ConfigurationProfile_strategy)
def test_vcml_configurationprofile_bomapplication_setter(instance):
    original = instance.bomapplication
    instance.bomapplication = original
    assert instance.bomapplication == original



@given(instance=vcml_ConfigurationProfile_strategy)
def test_vcml_configurationprofile_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=vcml_ConfigurationProfile_strategy)
def test_vcml_configurationprofile_fixing_setter(instance):
    original = instance.fixing
    instance.fixing = original
    assert instance.fixing == original

@given(instance=vcml_BillOfMaterial_strategy)
@settings(max_examples=50)
def test_vcml_billofmaterial_instantiation(instance):
    assert isinstance(instance, vcml_BillOfMaterial)

@given(instance=vcml_Description_strategy)
@settings(max_examples=50)
def test_vcml_description_instantiation(instance):
    assert isinstance(instance, vcml_Description)

@given(instance=CharacteristicType_strategy)
@settings(max_examples=50)
def test_characteristictype_instantiation(instance):
    assert isinstance(instance, CharacteristicType)

@given(instance=vcml_SymbolicType_strategy)
@settings(max_examples=50)
def test_vcml_symbolictype_instantiation(instance):
    assert isinstance(instance, vcml_SymbolicType)



@given(instance=vcml_SymbolicType_strategy)
def test_vcml_symbolictype_caseSensitive_setter(instance):
    original = instance.caseSensitive
    instance.caseSensitive = original
    assert instance.caseSensitive == original

@given(instance=vcml_DateType_strategy)
@settings(max_examples=50)
def test_vcml_datetype_instantiation(instance):
    assert isinstance(instance, vcml_DateType)



@given(instance=vcml_DateType_strategy)
def test_vcml_datetype_intervalValuesAllowed_setter(instance):
    original = instance.intervalValuesAllowed
    instance.intervalValuesAllowed = original
    assert instance.intervalValuesAllowed == original

@given(instance=vcml_NumericType_strategy)
@settings(max_examples=50)
def test_vcml_numerictype_instantiation(instance):
    assert isinstance(instance, vcml_NumericType)



@given(instance=vcml_NumericType_strategy)
def test_vcml_numerictype_negativeValuesAllowed_setter(instance):
    original = instance.negativeValuesAllowed
    instance.negativeValuesAllowed = original
    assert instance.negativeValuesAllowed == original



@given(instance=vcml_NumericType_strategy)
def test_vcml_numerictype_intervalValuesAllowed_setter(instance):
    original = instance.intervalValuesAllowed
    instance.intervalValuesAllowed = original
    assert instance.intervalValuesAllowed == original



@given(instance=vcml_NumericType_strategy)
def test_vcml_numerictype_decimalPlaces_setter(instance):
    original = instance.decimalPlaces
    instance.decimalPlaces = original
    assert instance.decimalPlaces == original



@given(instance=vcml_NumericType_strategy)
def test_vcml_numerictype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=vcml_VCObject_strategy)
@settings(max_examples=50)
def test_vcml_vcobject_instantiation(instance):
    assert isinstance(instance, vcml_VCObject)



@given(instance=vcml_VCObject_strategy)
def test_vcml_vcobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_Option_strategy)
@settings(max_examples=50)
def test_vcml_option_instantiation(instance):
    assert isinstance(instance, vcml_Option)



@given(instance=vcml_Option_strategy)
def test_vcml_option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=vcml_Option_strategy)
def test_vcml_option_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vcml_Import_strategy)
@settings(max_examples=50)
def test_vcml_import_instantiation(instance):
    assert isinstance(instance, vcml_Import)



@given(instance=vcml_Import_strategy)
def test_vcml_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=vcml_VcmlModel_strategy)
@settings(max_examples=50)
def test_vcml_vcmlmodel_instantiation(instance):
    assert isinstance(instance, vcml_VcmlModel)

@given(instance=vcml_BinaryCondition_strategy)
@settings(max_examples=50)
def test_vcml_binarycondition_instantiation(instance):
    assert isinstance(instance, vcml_BinaryCondition)



@given(instance=vcml_BinaryCondition_strategy)
def test_vcml_binarycondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml_ConditionalStatement_strategy)
@settings(max_examples=50)
def test_vcml_conditionalstatement_instantiation(instance):
    assert isinstance(instance, vcml_ConditionalStatement)

@given(instance=vcml_ConditionalConstraintRestriction_strategy)
@settings(max_examples=50)
def test_vcml_conditionalconstraintrestriction_instantiation(instance):
    assert isinstance(instance, vcml_ConditionalConstraintRestriction)

@given(instance=List_strategy)
@settings(max_examples=50)
def test_list_instantiation(instance):
    assert isinstance(instance, List)

@given(instance=vcml_SymbolList_strategy)
@settings(max_examples=50)
def test_vcml_symbollist_instantiation(instance):
    assert isinstance(instance, vcml_SymbolList)

@given(instance=vcml_NumberList_strategy)
@settings(max_examples=50)
def test_vcml_numberlist_instantiation(instance):
    assert isinstance(instance, vcml_NumberList)

@given(instance=vcml_InCondition_P_strategy)
@settings(max_examples=50)
def test_vcml_incondition_p_instantiation(instance):
    assert isinstance(instance, vcml_InCondition_P)

@given(instance=vcml_List_strategy)
@settings(max_examples=50)
def test_vcml_list_instantiation(instance):
    assert isinstance(instance, vcml_List)

@given(instance=vcml_InCondition_C_strategy)
@settings(max_examples=50)
def test_vcml_incondition_c_instantiation(instance):
    assert isinstance(instance, vcml_InCondition_C)

@given(instance=vcml_IsSpecified_P_strategy)
@settings(max_examples=50)
def test_vcml_isspecified_p_instantiation(instance):
    assert isinstance(instance, vcml_IsSpecified_P)

@given(instance=vcml_IsSpecified_C_strategy)
@settings(max_examples=50)
def test_vcml_isspecified_c_instantiation(instance):
    assert isinstance(instance, vcml_IsSpecified_C)

@given(instance=vcml_Comparison_strategy)
@settings(max_examples=50)
def test_vcml_comparison_instantiation(instance):
    assert isinstance(instance, vcml_Comparison)



@given(instance=vcml_Comparison_strategy)
def test_vcml_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml_UnaryCondition_strategy)
@settings(max_examples=50)
def test_vcml_unarycondition_instantiation(instance):
    assert isinstance(instance, vcml_UnaryCondition)

@given(instance=vcml_SymbolicLiteral_strategy)
@settings(max_examples=50)
def test_vcml_symbolicliteral_instantiation(instance):
    assert isinstance(instance, vcml_SymbolicLiteral)



@given(instance=vcml_SymbolicLiteral_strategy)
def test_vcml_symbolicliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberListEntry_strategy)
@settings(max_examples=50)
def test_numberlistentry_instantiation(instance):
    assert isinstance(instance, NumberListEntry)

@given(instance=vcml_NumericInterval_strategy)
@settings(max_examples=50)
def test_vcml_numericinterval_instantiation(instance):
    assert isinstance(instance, vcml_NumericInterval)



@given(instance=vcml_NumericInterval_strategy)
def test_vcml_numericinterval_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=vcml_NumericInterval_strategy)
def test_vcml_numericinterval_lowerBoundOp_setter(instance):
    original = instance.lowerBoundOp
    instance.lowerBoundOp = original
    assert instance.lowerBoundOp == original



@given(instance=vcml_NumericInterval_strategy)
def test_vcml_numericinterval_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=vcml_NumericInterval_strategy)
def test_vcml_numericinterval_upperBoundOp_setter(instance):
    original = instance.upperBoundOp
    instance.upperBoundOp = original
    assert instance.upperBoundOp == original

@given(instance=vcml_NumericLiteral_strategy)
@settings(max_examples=50)
def test_vcml_numericliteral_instantiation(instance):
    assert isinstance(instance, vcml_NumericLiteral)



@given(instance=vcml_NumericLiteral_strategy)
def test_vcml_numericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vcml_MDataCharacteristic_P_strategy)
@settings(max_examples=50)
def test_vcml_mdatacharacteristic_p_instantiation(instance):
    assert isinstance(instance, vcml_MDataCharacteristic_P)

@given(instance=vcml_MDataCharacteristic_C_strategy)
@settings(max_examples=50)
def test_vcml_mdatacharacteristic_c_instantiation(instance):
    assert isinstance(instance, vcml_MDataCharacteristic_C)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vcml_Literal_strategy)
@settings(max_examples=50)
def test_vcml_literal_instantiation(instance):
    assert isinstance(instance, vcml_Literal)

@given(instance=vcml_FunctionCall_strategy)
@settings(max_examples=50)
def test_vcml_functioncall_instantiation(instance):
    assert isinstance(instance, vcml_FunctionCall)



@given(instance=vcml_FunctionCall_strategy)
def test_vcml_functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=vcml_SumParts_strategy)
@settings(max_examples=50)
def test_vcml_sumparts_instantiation(instance):
    assert isinstance(instance, vcml_SumParts)



@given(instance=vcml_SumParts_strategy)
def test_vcml_sumparts_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml_BinaryExpression_strategy)
@settings(max_examples=50)
def test_vcml_binaryexpression_instantiation(instance):
    assert isinstance(instance, vcml_BinaryExpression)



@given(instance=vcml_BinaryExpression_strategy)
def test_vcml_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml_CountParts_strategy)
@settings(max_examples=50)
def test_vcml_countparts_instantiation(instance):
    assert isinstance(instance, vcml_CountParts)



@given(instance=vcml_CountParts_strategy)
def test_vcml_countparts_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml_UnaryExpression_strategy)
@settings(max_examples=50)
def test_vcml_unaryexpression_instantiation(instance):
    assert isinstance(instance, vcml_UnaryExpression)



@given(instance=vcml_UnaryExpression_strategy)
def test_vcml_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vcml_TypeOf_strategy)
@settings(max_examples=50)
def test_vcml_typeof_instantiation(instance):
    assert isinstance(instance, vcml_TypeOf)



@given(instance=vcml_TypeOf_strategy)
def test_vcml_typeof_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml_SetPricingFactor_strategy)
@settings(max_examples=50)
def test_vcml_setpricingfactor_instantiation(instance):
    assert isinstance(instance, vcml_SetPricingFactor)



@given(instance=vcml_SetPricingFactor_strategy)
def test_vcml_setpricingfactor_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=vcml_IsInvisible_strategy)
@settings(max_examples=50)
def test_vcml_isinvisible_instantiation(instance):
    assert isinstance(instance, vcml_IsInvisible)

@given(instance=SetOrDelDefault_strategy)
@settings(max_examples=50)
def test_setordeldefault_instantiation(instance):
    assert isinstance(instance, SetOrDelDefault)

@given(instance=vcml_DelDefault_strategy)
@settings(max_examples=50)
def test_vcml_deldefault_instantiation(instance):
    assert isinstance(instance, vcml_DelDefault)

@given(instance=vcml_SetDefault_strategy)
@settings(max_examples=50)
def test_vcml_setdefault_instantiation(instance):
    assert isinstance(instance, vcml_SetDefault)

@given(instance=vcml_SetOrDelDefault_strategy)
@settings(max_examples=50)
def test_vcml_setordeldefault_instantiation(instance):
    assert isinstance(instance, vcml_SetOrDelDefault)

@given(instance=FunctionOrTable_strategy)
@settings(max_examples=50)
def test_functionortable_instantiation(instance):
    assert isinstance(instance, FunctionOrTable)

@given(instance=vcml_PFunction_strategy)
@settings(max_examples=50)
def test_vcml_pfunction_instantiation(instance):
    assert isinstance(instance, vcml_PFunction)

@given(instance=vcml_Table_strategy)
@settings(max_examples=50)
def test_vcml_table_instantiation(instance):
    assert isinstance(instance, vcml_Table)

@given(instance=vcml_Function_strategy)
@settings(max_examples=50)
def test_vcml_function_instantiation(instance):
    assert isinstance(instance, vcml_Function)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mutatorenvironment_miniOCL_NavigationPathCS,
    NavigationPathCS,
    mutatorenvironment_miniOCL_NavigationPathVariableCS,
    mutatorenvironment_miniOCL_NavigationPathElementCS,
    mutatorenvironment_miniOCL_NavigationPathNameCS,
    NavigationPathNameCS,
    DoubleType,
    mutatorenvironment_SpecificDoubleType,
    IntegerType,
    mutatorenvironment_RandomIntegerType,
    mutatorenvironment_SpecificIntegerType,
    NumberType,
    mutatorenvironment_DoubleType,
    mutatorenvironment_IntegerType,
    StringType,
    mutatorenvironment_RandomStringType,
    mutatorenvironment_SpecificStringType,
    mutatorenvironment_ObjectEmitter,
    mutatorenvironment_Source,
    Definition,
    mutatorenvironment_Resource,
    mutatorenvironment_Program,
    mutatorenvironment_Library,
    mutatorenvironment_Constraint,
    mutatorenvironment_Block,
    ObSelectionStrategy,
    mutatorenvironment_RandomSelection,
    mutatorenvironment_Expression,
    mutatorenvironment_EReference,
    mutatorenvironment_ReferenceSet,
    mutatorenvironment_AttributeSet,
    Mutator,
    mutatorenvironment_CreateObjectMutator,
    mutatorenvironment_CompositeMutator,
    ObjectEmitter,
    mutatorenvironment_ObSelectionStrategy,
    mutatorenvironment_EClass,
    mutatorenvironment_Load,
    mutatorenvironment_Mutator,
    mutatorenvironment_Definition,
    mutatorenvironment_MutatorEnvironment,
    mutatorenvironment_miniOCL_IteratorVarCS,
    LoopExpCS,
    mutatorenvironment_miniOCL_IterateExpCS,
    mutatorenvironment_miniOCL_ForAllExpCS,
    mutatorenvironment_miniOCL_CollectExpCS,
    IteratorVarCS,
    mutatorenvironment_miniOCL_ExistsExpCS,
    BooleanLiteralExpCS,
    mutatorenvironment_miniOCL_BooleanExpCS,
    miniOCL_mutatorenvironment_EStructuralFeature,
    mutatorenvironment_miniOCL_PathCS,
    PathCS,
    mutatorenvironment_miniOCL_PathElementCS,
    mutatorenvironment_miniOCL_PathVariableCS,
    mutatorenvironment_miniOCL_PathNameCS,
    LiteralExpCS,
    mutatorenvironment_miniOCL_StringLiteralExpCS,
    mutatorenvironment_miniOCL_BooleanLiteralExpCS,
    mutatorenvironment_miniOCL_IntLiteralExpCS,
    mutatorenvironment_miniOCL_RoundedBracketClauseCS,
    mutatorenvironment_miniOCL_AccVarCS,
    AccVarCS,
    ExpCS,
    ParameterCS,
    mutatorenvironment_miniOCL_OperationCS,
    mutatorenvironment_miniOCL_PropertyCS,
    OperationCS,
    PropertyCS,
    RoundedBracketClauseCS,
    PrimaryExpCS,
    mutatorenvironment_miniOCL_LiteralExpCS,
    mutatorenvironment_miniOCL_NavigationExpCS,
    NavigationExpCS,
    mutatorenvironment_miniOCL_NavigationNameExpCS,
    mutatorenvironment_miniOCL_NameExpCS,
    mutatorenvironment_miniOCL_LoopExpCS,
    CallExpCS,
    mutatorenvironment_miniOCL_PrimaryExpCS,
    LogicExpCS,
    mutatorenvironment_miniOCL_CallExpCS,
    mutatorenvironment_miniOCL_LogicExpCS,
    mutatorenvironment_miniOCL_ExpCS,
    mutatorenvironment_miniOCL_InvariantCS,
    mutatorenvironment_miniOCL_ConstraintCS,
    mutatorenvironment_miniOCL_ParameterCS,
    mutatorenvironment_RetypeObjectMutator,
    mutatorenvironment_EStructuralFeature,
    mutatorenvironment_SelectSampleMutator,
    PathNameCS,
    mutatorenvironment_miniOCL_ClassCS,
    ClassCS,
    mutatorenvironment_miniOCL_PackageCS,
    ConstraintCS,
    PackageCS,
    mutatorenvironment_miniOCL_RootCS,
    mutatorenvironment_RandomStringNumberType,
    mutatorenvironment_TypedSelection,
    mutatorenvironment_EObject,
    RandomNumberType,
    mutatorenvironment_RandomIntegerNumberType,
    mutatorenvironment_RandomDoubleNumberType,
    mutatorenvironment_RandomNumberType,
    mutatorenvironment_MaxValueType,
    mutatorenvironment_MinValueType,
    mutatorenvironment_BinaryOperator,
    mutatorenvironment_CloneObjectMutator,
    InvariantCS,
    ReferenceSet,
    mutatorenvironment_ReferenceAdd,
    mutatorenvironment_ReferenceAtt,
    mutatorenvironment_ReferenceRemove,
    mutatorenvironment_ReferenceSwap,
    mutatorenvironment_ReferenceInit,
    mutatorenvironment_AttributeEvaluationType,
    Evaluation,
    mutatorenvironment_AttributeEvaluation,
    mutatorenvironment_Evaluation,
    mutatorenvironment_ReferenceEvaluation,
    mutatorenvironment_ReplaceStringType,
    mutatorenvironment_EAttribute,
    mutatorenvironment_CatEndStringType,
    mutatorenvironment_CatStartStringType,
    mutatorenvironment_LowerStringType,
    mutatorenvironment_UpperStringType,
    mutatorenvironment_SelectObjectMutator,
    OtherSelection,
    mutatorenvironment_OtherTypeSelection,
    mutatorenvironment_OtherSelection,
    CompleteSelection,
    mutatorenvironment_CompleteTypeSelection,
    mutatorenvironment_CompleteSelection,
    RemoveReferenceMutator,
    mutatorenvironment_RemoveSpecificReferenceMutator,
    mutatorenvironment_RemoveCompleteReferenceMutator,
    mutatorenvironment_RemoveRandomReferenceMutator,
    mutatorenvironment_ModifyTargetReferenceMutator,
    mutatorenvironment_ModifyInformationMutator,
    mutatorenvironment_RemoveReferenceMutator,
    mutatorenvironment_RemoveObjectMutator,
    mutatorenvironment_CreateReferenceMutator,
    BooleanType,
    mutatorenvironment_RandomBooleanType,
    mutatorenvironment_SpecificBooleanType,
    AttributeType,
    mutatorenvironment_ListType,
    mutatorenvironment_StringType,
    mutatorenvironment_NumberType,
    mutatorenvironment_ListStringType,
    mutatorenvironment_RandomType,
    mutatorenvironment_BooleanType,
    AttributeEvaluationType,
    mutatorenvironment_ObjectAttributeType,
    mutatorenvironment_AttributeType,
    AttributeSet,
    mutatorenvironment_AttributeUnset,
    mutatorenvironment_AttributeOperation,
    mutatorenvironment_AttributeCopy,
    mutatorenvironment_AttributeReverse,
    mutatorenvironment_AttributeSwap,
    mutatorenvironment_AttributeScalar,
    SpecificSelection,
    mutatorenvironment_SpecificClosureSelection,
    mutatorenvironment_SpecificObjectSelection,
    RandomSelection,
    mutatorenvironment_RandomTypeSelection,
    mutatorenvironment_SpecificReferenceSelection,
    mutatorenvironment_SpecificSelection,
    mutatorenvironment_ModifySourceReferenceMutator,
    mutatorenvironment_RandomDoubleType,
    Repeat,
    ArithmeticOperator,
    Operator,
    LogicOperator,
    SampleClause,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mutatorenvironment_miniocl_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationPathCS)


def test_mutatorenvironment_miniocl_navigationpathcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationPathCS.__init__)


def test_mutatorenvironment_miniocl_navigationpathcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationPathVariableCS)


def test_mutatorenvironment_miniocl_navigationpathvariablecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationPathVariableCS.__init__)


def test_mutatorenvironment_miniocl_navigationpathvariablecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_mutatorenvironment_miniocl_navigationpathvariablecs_has_varName():
    assert hasattr(mutatorenvironment_miniOCL_NavigationPathVariableCS, "varName")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_NavigationPathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationPathElementCS)


def test_mutatorenvironment_miniocl_navigationpathelementcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationPathElementCS.__init__)


def test_mutatorenvironment_miniocl_navigationpathelementcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationPathNameCS)


def test_mutatorenvironment_miniocl_navigationpathnamecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationPathNameCS.__init__)


def test_mutatorenvironment_miniocl_navigationpathnamecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathNameCS)


def test_navigationpathnamecs_constructor_exists():
    assert callable(NavigationPathNameCS.__init__)


def test_navigationpathnamecs_constructor_args():
    sig = inspect.signature(NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_doubletype_is_not_abstract():
    assert not inspect.isabstract(DoubleType)


def test_doubletype_constructor_exists():
    assert callable(DoubleType.__init__)


def test_doubletype_constructor_args():
    sig = inspect.signature(DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_specificdoubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificDoubleType)


def test_mutatorenvironment_specificdoubletype_constructor_exists():
    assert callable(mutatorenvironment_SpecificDoubleType.__init__)


def test_mutatorenvironment_specificdoubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificDoubleType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_specificdoubletype_has_value():
    assert hasattr(mutatorenvironment_SpecificDoubleType, "value")
    descriptor = None
    for klass in mutatorenvironment_SpecificDoubleType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomintegertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomIntegerType)


def test_mutatorenvironment_randomintegertype_constructor_exists():
    assert callable(mutatorenvironment_RandomIntegerType.__init__)


def test_mutatorenvironment_randomintegertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomIntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_mutatorenvironment_randomintegertype_has_allowsNull():
    assert hasattr(mutatorenvironment_RandomIntegerType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment_RandomIntegerType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomintegertype_has_min():
    assert hasattr(mutatorenvironment_RandomIntegerType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomIntegerType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomintegertype_has_max():
    assert hasattr(mutatorenvironment_RandomIntegerType, "max")
    descriptor = None
    for klass in mutatorenvironment_RandomIntegerType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_specificintegertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificIntegerType)


def test_mutatorenvironment_specificintegertype_constructor_exists():
    assert callable(mutatorenvironment_SpecificIntegerType.__init__)


def test_mutatorenvironment_specificintegertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificIntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_specificintegertype_has_value():
    assert hasattr(mutatorenvironment_SpecificIntegerType, "value")
    descriptor = None
    for klass in mutatorenvironment_SpecificIntegerType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_doubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_DoubleType)


def test_mutatorenvironment_doubletype_constructor_exists():
    assert callable(mutatorenvironment_DoubleType.__init__)


def test_mutatorenvironment_doubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_integertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_IntegerType)


def test_mutatorenvironment_integertype_constructor_exists():
    assert callable(mutatorenvironment_IntegerType.__init__)


def test_mutatorenvironment_integertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_stringtype_is_not_abstract():
    assert not inspect.isabstract(StringType)


def test_stringtype_constructor_exists():
    assert callable(StringType.__init__)


def test_stringtype_constructor_args():
    sig = inspect.signature(StringType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomStringType)


def test_mutatorenvironment_randomstringtype_constructor_exists():
    assert callable(mutatorenvironment_RandomStringType.__init__)


def test_mutatorenvironment_randomstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomStringType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_mutatorenvironment_randomstringtype_has_allowsNull():
    assert hasattr(mutatorenvironment_RandomStringType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment_RandomStringType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomstringtype_has_max():
    assert hasattr(mutatorenvironment_RandomStringType, "max")
    descriptor = None
    for klass in mutatorenvironment_RandomStringType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomstringtype_has_min():
    assert hasattr(mutatorenvironment_RandomStringType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomStringType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_specificstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificStringType)


def test_mutatorenvironment_specificstringtype_constructor_exists():
    assert callable(mutatorenvironment_SpecificStringType.__init__)


def test_mutatorenvironment_specificstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_specificstringtype_has_value():
    assert hasattr(mutatorenvironment_SpecificStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_SpecificStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_objectemitter_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ObjectEmitter)


def test_mutatorenvironment_objectemitter_constructor_exists():
    assert callable(mutatorenvironment_ObjectEmitter.__init__)


def test_mutatorenvironment_objectemitter_constructor_args():
    sig = inspect.signature(mutatorenvironment_ObjectEmitter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_objectemitter_has_name():
    assert hasattr(mutatorenvironment_ObjectEmitter, "name")
    descriptor = None
    for klass in mutatorenvironment_ObjectEmitter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_source_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Source)


def test_mutatorenvironment_source_constructor_exists():
    assert callable(mutatorenvironment_Source.__init__)


def test_mutatorenvironment_source_constructor_args():
    sig = inspect.signature(mutatorenvironment_Source.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_mutatorenvironment_source_has_path():
    assert hasattr(mutatorenvironment_Source, "path")
    descriptor = None
    for klass in mutatorenvironment_Source.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_resource_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Resource)


def test_mutatorenvironment_resource_constructor_exists():
    assert callable(mutatorenvironment_Resource.__init__)


def test_mutatorenvironment_resource_constructor_args():
    sig = inspect.signature(mutatorenvironment_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_resource_has_name():
    assert hasattr(mutatorenvironment_Resource, "name")
    descriptor = None
    for klass in mutatorenvironment_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_program_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Program)


def test_mutatorenvironment_program_constructor_exists():
    assert callable(mutatorenvironment_Program.__init__)


def test_mutatorenvironment_program_constructor_args():
    sig = inspect.signature(mutatorenvironment_Program.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "exhaustive" in params, "Missing parameter 'exhaustive'"
    assert "output" in params, "Missing parameter 'output'"
    assert "num" in params, "Missing parameter 'num'"

def test_mutatorenvironment_program_has_description():
    assert hasattr(mutatorenvironment_Program, "description")
    descriptor = None
    for klass in mutatorenvironment_Program.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_program_has_exhaustive():
    assert hasattr(mutatorenvironment_Program, "exhaustive")
    descriptor = None
    for klass in mutatorenvironment_Program.__mro__:
        if "exhaustive" in klass.__dict__:
            descriptor = klass.__dict__["exhaustive"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_program_has_output():
    assert hasattr(mutatorenvironment_Program, "output")
    descriptor = None
    for klass in mutatorenvironment_Program.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_program_has_num():
    assert hasattr(mutatorenvironment_Program, "num")
    descriptor = None
    for klass in mutatorenvironment_Program.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_library_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Library)


def test_mutatorenvironment_library_constructor_exists():
    assert callable(mutatorenvironment_Library.__init__)


def test_mutatorenvironment_library_constructor_args():
    sig = inspect.signature(mutatorenvironment_Library.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_constraint_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Constraint)


def test_mutatorenvironment_constraint_constructor_exists():
    assert callable(mutatorenvironment_Constraint.__init__)


def test_mutatorenvironment_constraint_constructor_args():
    sig = inspect.signature(mutatorenvironment_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "rules" in params, "Missing parameter 'rules'"

def test_mutatorenvironment_constraint_has_id():
    assert hasattr(mutatorenvironment_Constraint, "id")
    descriptor = None
    for klass in mutatorenvironment_Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_constraint_has_rules():
    assert hasattr(mutatorenvironment_Constraint, "rules")
    descriptor = None
    for klass in mutatorenvironment_Constraint.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_block_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Block)


def test_mutatorenvironment_block_constructor_exists():
    assert callable(mutatorenvironment_Block.__init__)


def test_mutatorenvironment_block_constructor_args():
    sig = inspect.signature(mutatorenvironment_Block.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "description" in params, "Missing parameter 'description'"
    assert "max" in params, "Missing parameter 'max'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_block_has_min():
    assert hasattr(mutatorenvironment_Block, "min")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_block_has_fixed():
    assert hasattr(mutatorenvironment_Block, "fixed")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_block_has_description():
    assert hasattr(mutatorenvironment_Block, "description")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_block_has_max():
    assert hasattr(mutatorenvironment_Block, "max")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_block_has_repeat():
    assert hasattr(mutatorenvironment_Block, "repeat")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_block_has_name():
    assert hasattr(mutatorenvironment_Block, "name")
    descriptor = None
    for klass in mutatorenvironment_Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_obselectionstrategy_is_not_abstract():
    assert not inspect.isabstract(ObSelectionStrategy)


def test_obselectionstrategy_constructor_exists():
    assert callable(ObSelectionStrategy.__init__)


def test_obselectionstrategy_constructor_args():
    sig = inspect.signature(ObSelectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomSelection)


def test_mutatorenvironment_randomselection_constructor_exists():
    assert callable(mutatorenvironment_RandomSelection.__init__)


def test_mutatorenvironment_randomselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_expression_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Expression)


def test_mutatorenvironment_expression_constructor_exists():
    assert callable(mutatorenvironment_Expression.__init__)


def test_mutatorenvironment_expression_constructor_args():
    sig = inspect.signature(mutatorenvironment_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_ereference_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_EReference)


def test_mutatorenvironment_ereference_constructor_exists():
    assert callable(mutatorenvironment_EReference.__init__)


def test_mutatorenvironment_ereference_constructor_args():
    sig = inspect.signature(mutatorenvironment_EReference.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceSet)


def test_mutatorenvironment_referenceset_constructor_exists():
    assert callable(mutatorenvironment_ReferenceSet.__init__)


def test_mutatorenvironment_referenceset_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeSet)


def test_mutatorenvironment_attributeset_constructor_exists():
    assert callable(mutatorenvironment_AttributeSet.__init__)


def test_mutatorenvironment_attributeset_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_mutator_is_not_abstract():
    assert not inspect.isabstract(Mutator)


def test_mutator_constructor_exists():
    assert callable(Mutator.__init__)


def test_mutator_constructor_args():
    sig = inspect.signature(Mutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_createobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CreateObjectMutator)


def test_mutatorenvironment_createobjectmutator_constructor_exists():
    assert callable(mutatorenvironment_CreateObjectMutator.__init__)


def test_mutatorenvironment_createobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_CreateObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_compositemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CompositeMutator)


def test_mutatorenvironment_compositemutator_constructor_exists():
    assert callable(mutatorenvironment_CompositeMutator.__init__)


def test_mutatorenvironment_compositemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_CompositeMutator.__init__)
    params = list(sig.parameters.keys())



def test_objectemitter_is_not_abstract():
    assert not inspect.isabstract(ObjectEmitter)


def test_objectemitter_constructor_exists():
    assert callable(ObjectEmitter.__init__)


def test_objectemitter_constructor_args():
    sig = inspect.signature(ObjectEmitter.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_obselectionstrategy_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ObSelectionStrategy)


def test_mutatorenvironment_obselectionstrategy_constructor_exists():
    assert callable(mutatorenvironment_ObSelectionStrategy.__init__)


def test_mutatorenvironment_obselectionstrategy_constructor_args():
    sig = inspect.signature(mutatorenvironment_ObSelectionStrategy.__init__)
    params = list(sig.parameters.keys())
    assert "resource" in params, "Missing parameter 'resource'"

def test_mutatorenvironment_obselectionstrategy_has_resource():
    assert hasattr(mutatorenvironment_ObSelectionStrategy, "resource")
    descriptor = None
    for klass in mutatorenvironment_ObSelectionStrategy.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_eclass_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_EClass)


def test_mutatorenvironment_eclass_constructor_exists():
    assert callable(mutatorenvironment_EClass.__init__)


def test_mutatorenvironment_eclass_constructor_args():
    sig = inspect.signature(mutatorenvironment_EClass.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_load_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Load)


def test_mutatorenvironment_load_constructor_exists():
    assert callable(mutatorenvironment_Load.__init__)


def test_mutatorenvironment_load_constructor_args():
    sig = inspect.signature(mutatorenvironment_Load.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mutatorenvironment_load_has_file():
    assert hasattr(mutatorenvironment_Load, "file")
    descriptor = None
    for klass in mutatorenvironment_Load.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_mutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Mutator)


def test_mutatorenvironment_mutator_constructor_exists():
    assert callable(mutatorenvironment_Mutator.__init__)


def test_mutatorenvironment_mutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_Mutator.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "fixed" in params, "Missing parameter 'fixed'"

def test_mutatorenvironment_mutator_has_max():
    assert hasattr(mutatorenvironment_Mutator, "max")
    descriptor = None
    for klass in mutatorenvironment_Mutator.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_mutator_has_min():
    assert hasattr(mutatorenvironment_Mutator, "min")
    descriptor = None
    for klass in mutatorenvironment_Mutator.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_mutator_has_fixed():
    assert hasattr(mutatorenvironment_Mutator, "fixed")
    descriptor = None
    for klass in mutatorenvironment_Mutator.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_definition_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Definition)


def test_mutatorenvironment_definition_constructor_exists():
    assert callable(mutatorenvironment_Definition.__init__)


def test_mutatorenvironment_definition_constructor_args():
    sig = inspect.signature(mutatorenvironment_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_mutatorenvironment_definition_has_metamodel():
    assert hasattr(mutatorenvironment_Definition, "metamodel")
    descriptor = None
    for klass in mutatorenvironment_Definition.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_mutatorenvironment_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_MutatorEnvironment)


def test_mutatorenvironment_mutatorenvironment_constructor_exists():
    assert callable(mutatorenvironment_MutatorEnvironment.__init__)


def test_mutatorenvironment_mutatorenvironment_constructor_args():
    sig = inspect.signature(mutatorenvironment_MutatorEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_IteratorVarCS)


def test_mutatorenvironment_miniocl_iteratorvarcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_IteratorVarCS.__init__)


def test_mutatorenvironment_miniocl_iteratorvarcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_mutatorenvironment_miniocl_iteratorvarcs_has_itName():
    assert hasattr(mutatorenvironment_miniOCL_IteratorVarCS, "itName")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_IterateExpCS)


def test_mutatorenvironment_miniocl_iterateexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_IterateExpCS.__init__)


def test_mutatorenvironment_miniocl_iterateexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_forallexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ForAllExpCS)


def test_mutatorenvironment_miniocl_forallexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ForAllExpCS.__init__)


def test_mutatorenvironment_miniocl_forallexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_collectexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_CollectExpCS)


def test_mutatorenvironment_miniocl_collectexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_CollectExpCS.__init__)


def test_mutatorenvironment_miniocl_collectexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(IteratorVarCS)


def test_iteratorvarcs_constructor_exists():
    assert callable(IteratorVarCS.__init__)


def test_iteratorvarcs_constructor_args():
    sig = inspect.signature(IteratorVarCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_existsexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ExistsExpCS)


def test_mutatorenvironment_miniocl_existsexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ExistsExpCS.__init__)


def test_mutatorenvironment_miniocl_existsexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_BooleanExpCS)


def test_mutatorenvironment_miniocl_booleanexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_BooleanExpCS.__init__)


def test_mutatorenvironment_miniocl_booleanexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_mutatorenvironment_miniocl_booleanexpcs_has_boolSymbol():
    assert hasattr(mutatorenvironment_miniOCL_BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_mutatorenvironment_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(miniOCL_mutatorenvironment_EStructuralFeature)


def test_miniocl_mutatorenvironment_estructuralfeature_constructor_exists():
    assert callable(miniOCL_mutatorenvironment_EStructuralFeature.__init__)


def test_miniocl_mutatorenvironment_estructuralfeature_constructor_args():
    sig = inspect.signature(miniOCL_mutatorenvironment_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_pathcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PathCS)


def test_mutatorenvironment_miniocl_pathcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PathCS.__init__)


def test_mutatorenvironment_miniocl_pathcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PathCS.__init__)
    params = list(sig.parameters.keys())



def test_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PathElementCS)


def test_mutatorenvironment_miniocl_pathelementcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PathElementCS.__init__)


def test_mutatorenvironment_miniocl_pathelementcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PathVariableCS)


def test_mutatorenvironment_miniocl_pathvariablecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PathVariableCS.__init__)


def test_mutatorenvironment_miniocl_pathvariablecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_mutatorenvironment_miniocl_pathvariablecs_has_varName():
    assert hasattr(mutatorenvironment_miniOCL_PathVariableCS, "varName")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_PathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PathNameCS)


def test_mutatorenvironment_miniocl_pathnamecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PathNameCS.__init__)


def test_mutatorenvironment_miniocl_pathnamecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_StringLiteralExpCS)


def test_mutatorenvironment_miniocl_stringliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_StringLiteralExpCS.__init__)


def test_mutatorenvironment_miniocl_stringliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_mutatorenvironment_miniocl_stringliteralexpcs_has_stringSymbol():
    assert hasattr(mutatorenvironment_miniOCL_StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_BooleanLiteralExpCS)


def test_mutatorenvironment_miniocl_booleanliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_BooleanLiteralExpCS.__init__)


def test_mutatorenvironment_miniocl_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_IntLiteralExpCS)


def test_mutatorenvironment_miniocl_intliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_IntLiteralExpCS.__init__)


def test_mutatorenvironment_miniocl_intliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_mutatorenvironment_miniocl_intliteralexpcs_has_intSymbol():
    assert hasattr(mutatorenvironment_miniOCL_IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_RoundedBracketClauseCS)


def test_mutatorenvironment_miniocl_roundedbracketclausecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_RoundedBracketClauseCS.__init__)


def test_mutatorenvironment_miniocl_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_accvarcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_AccVarCS)


def test_mutatorenvironment_miniocl_accvarcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_AccVarCS.__init__)


def test_mutatorenvironment_miniocl_accvarcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"

def test_mutatorenvironment_miniocl_accvarcs_has_accVarName():
    assert hasattr(mutatorenvironment_miniOCL_AccVarCS, "accVarName")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_AccVarCS.__mro__:
        if "accVarName" in klass.__dict__:
            descriptor = klass.__dict__["accVarName"]
            break
    assert isinstance(descriptor, property)



def test_accvarcs_is_not_abstract():
    assert not inspect.isabstract(AccVarCS)


def test_accvarcs_constructor_exists():
    assert callable(AccVarCS.__init__)


def test_accvarcs_constructor_args():
    sig = inspect.signature(AccVarCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_parametercs_is_not_abstract():
    assert not inspect.isabstract(ParameterCS)


def test_parametercs_constructor_exists():
    assert callable(ParameterCS.__init__)


def test_parametercs_constructor_args():
    sig = inspect.signature(ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_operationcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_OperationCS)


def test_mutatorenvironment_miniocl_operationcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_OperationCS.__init__)


def test_mutatorenvironment_miniocl_operationcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_miniocl_operationcs_has_name():
    assert hasattr(mutatorenvironment_miniOCL_OperationCS, "name")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_propertycs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PropertyCS)


def test_mutatorenvironment_miniocl_propertycs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PropertyCS.__init__)


def test_mutatorenvironment_miniocl_propertycs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_miniocl_propertycs_has_name():
    assert hasattr(mutatorenvironment_miniOCL_PropertyCS, "name")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operationcs_is_not_abstract():
    assert not inspect.isabstract(OperationCS)


def test_operationcs_constructor_exists():
    assert callable(OperationCS.__init__)


def test_operationcs_constructor_args():
    sig = inspect.signature(OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_propertycs_is_not_abstract():
    assert not inspect.isabstract(PropertyCS)


def test_propertycs_constructor_exists():
    assert callable(PropertyCS.__init__)


def test_propertycs_constructor_args():
    sig = inspect.signature(PropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(RoundedBracketClauseCS)


def test_roundedbracketclausecs_constructor_exists():
    assert callable(RoundedBracketClauseCS.__init__)


def test_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_LiteralExpCS)


def test_mutatorenvironment_miniocl_literalexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_LiteralExpCS.__init__)


def test_mutatorenvironment_miniocl_literalexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationExpCS)


def test_mutatorenvironment_miniocl_navigationexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationExpCS.__init__)


def test_mutatorenvironment_miniocl_navigationexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NavigationNameExpCS)


def test_mutatorenvironment_miniocl_navigationnameexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NavigationNameExpCS.__init__)


def test_mutatorenvironment_miniocl_navigationnameexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_NameExpCS)


def test_mutatorenvironment_miniocl_nameexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_NameExpCS.__init__)


def test_mutatorenvironment_miniocl_nameexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_LoopExpCS)


def test_mutatorenvironment_miniocl_loopexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_LoopExpCS.__init__)


def test_mutatorenvironment_miniocl_loopexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"

def test_mutatorenvironment_miniocl_loopexpcs_has_logicOp():
    assert hasattr(mutatorenvironment_miniOCL_LoopExpCS, "logicOp")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_LoopExpCS.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PrimaryExpCS)


def test_mutatorenvironment_miniocl_primaryexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PrimaryExpCS.__init__)


def test_mutatorenvironment_miniocl_primaryexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_callexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_CallExpCS)


def test_mutatorenvironment_miniocl_callexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_CallExpCS.__init__)


def test_mutatorenvironment_miniocl_callexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_LogicExpCS)


def test_mutatorenvironment_miniocl_logicexpcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_LogicExpCS.__init__)


def test_mutatorenvironment_miniocl_logicexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mutatorenvironment_miniocl_logicexpcs_has_op():
    assert hasattr(mutatorenvironment_miniOCL_LogicExpCS, "op")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_miniocl_expcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ExpCS)


def test_mutatorenvironment_miniocl_expcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ExpCS.__init__)


def test_mutatorenvironment_miniocl_expcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_invariantcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_InvariantCS)


def test_mutatorenvironment_miniocl_invariantcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_InvariantCS.__init__)


def test_mutatorenvironment_miniocl_invariantcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_constraintcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ConstraintCS)


def test_mutatorenvironment_miniocl_constraintcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ConstraintCS.__init__)


def test_mutatorenvironment_miniocl_constraintcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_parametercs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ParameterCS)


def test_mutatorenvironment_miniocl_parametercs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ParameterCS.__init__)


def test_mutatorenvironment_miniocl_parametercs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_miniocl_parametercs_has_name():
    assert hasattr(mutatorenvironment_miniOCL_ParameterCS, "name")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_retypeobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RetypeObjectMutator)


def test_mutatorenvironment_retypeobjectmutator_constructor_exists():
    assert callable(mutatorenvironment_RetypeObjectMutator.__init__)


def test_mutatorenvironment_retypeobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RetypeObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_EStructuralFeature)


def test_mutatorenvironment_estructuralfeature_constructor_exists():
    assert callable(mutatorenvironment_EStructuralFeature.__init__)


def test_mutatorenvironment_estructuralfeature_constructor_args():
    sig = inspect.signature(mutatorenvironment_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_selectsamplemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SelectSampleMutator)


def test_mutatorenvironment_selectsamplemutator_constructor_exists():
    assert callable(mutatorenvironment_SelectSampleMutator.__init__)


def test_mutatorenvironment_selectsamplemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_SelectSampleMutator.__init__)
    params = list(sig.parameters.keys())
    assert "clause" in params, "Missing parameter 'clause'"

def test_mutatorenvironment_selectsamplemutator_has_clause():
    assert hasattr(mutatorenvironment_SelectSampleMutator, "clause")
    descriptor = None
    for klass in mutatorenvironment_SelectSampleMutator.__mro__:
        if "clause" in klass.__dict__:
            descriptor = klass.__dict__["clause"]
            break
    assert isinstance(descriptor, property)



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_classcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_ClassCS)


def test_mutatorenvironment_miniocl_classcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_ClassCS.__init__)


def test_mutatorenvironment_miniocl_classcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_miniocl_classcs_has_name():
    assert hasattr(mutatorenvironment_miniOCL_ClassCS, "name")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classcs_is_not_abstract():
    assert not inspect.isabstract(ClassCS)


def test_classcs_constructor_exists():
    assert callable(ClassCS.__init__)


def test_classcs_constructor_args():
    sig = inspect.signature(ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_packagecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_PackageCS)


def test_mutatorenvironment_miniocl_packagecs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_PackageCS.__init__)


def test_mutatorenvironment_miniocl_packagecs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment_miniocl_packagecs_has_name():
    assert hasattr(mutatorenvironment_miniOCL_PackageCS, "name")
    descriptor = None
    for klass in mutatorenvironment_miniOCL_PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_constraintcs_is_not_abstract():
    assert not inspect.isabstract(ConstraintCS)


def test_constraintcs_constructor_exists():
    assert callable(ConstraintCS.__init__)


def test_constraintcs_constructor_args():
    sig = inspect.signature(ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_packagecs_is_not_abstract():
    assert not inspect.isabstract(PackageCS)


def test_packagecs_constructor_exists():
    assert callable(PackageCS.__init__)


def test_packagecs_constructor_args():
    sig = inspect.signature(PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_miniocl_rootcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_miniOCL_RootCS)


def test_mutatorenvironment_miniocl_rootcs_constructor_exists():
    assert callable(mutatorenvironment_miniOCL_RootCS.__init__)


def test_mutatorenvironment_miniocl_rootcs_constructor_args():
    sig = inspect.signature(mutatorenvironment_miniOCL_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomstringnumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomStringNumberType)


def test_mutatorenvironment_randomstringnumbertype_constructor_exists():
    assert callable(mutatorenvironment_RandomStringNumberType.__init__)


def test_mutatorenvironment_randomstringnumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomStringNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_mutatorenvironment_randomstringnumbertype_has_allowsNull():
    assert hasattr(mutatorenvironment_RandomStringNumberType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment_RandomStringNumberType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomstringnumbertype_has_min():
    assert hasattr(mutatorenvironment_RandomStringNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomStringNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomstringnumbertype_has_max():
    assert hasattr(mutatorenvironment_RandomStringNumberType, "max")
    descriptor = None
    for klass in mutatorenvironment_RandomStringNumberType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_typedselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_TypedSelection)


def test_mutatorenvironment_typedselection_constructor_exists():
    assert callable(mutatorenvironment_TypedSelection.__init__)


def test_mutatorenvironment_typedselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_TypedSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_eobject_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_EObject)


def test_mutatorenvironment_eobject_constructor_exists():
    assert callable(mutatorenvironment_EObject.__init__)


def test_mutatorenvironment_eobject_constructor_args():
    sig = inspect.signature(mutatorenvironment_EObject.__init__)
    params = list(sig.parameters.keys())



def test_randomnumbertype_is_not_abstract():
    assert not inspect.isabstract(RandomNumberType)


def test_randomnumbertype_constructor_exists():
    assert callable(RandomNumberType.__init__)


def test_randomnumbertype_constructor_args():
    sig = inspect.signature(RandomNumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomintegernumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomIntegerNumberType)


def test_mutatorenvironment_randomintegernumbertype_constructor_exists():
    assert callable(mutatorenvironment_RandomIntegerNumberType.__init__)


def test_mutatorenvironment_randomintegernumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomIntegerNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"

def test_mutatorenvironment_randomintegernumbertype_has_min():
    assert hasattr(mutatorenvironment_RandomIntegerNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomIntegerNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_randomdoublenumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomDoubleNumberType)


def test_mutatorenvironment_randomdoublenumbertype_constructor_exists():
    assert callable(mutatorenvironment_RandomDoubleNumberType.__init__)


def test_mutatorenvironment_randomdoublenumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomDoubleNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"

def test_mutatorenvironment_randomdoublenumbertype_has_min():
    assert hasattr(mutatorenvironment_RandomDoubleNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomDoubleNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_randomnumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomNumberType)


def test_mutatorenvironment_randomnumbertype_constructor_exists():
    assert callable(mutatorenvironment_RandomNumberType.__init__)


def test_mutatorenvironment_randomnumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomNumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_maxvaluetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_MaxValueType)


def test_mutatorenvironment_maxvaluetype_constructor_exists():
    assert callable(mutatorenvironment_MaxValueType.__init__)


def test_mutatorenvironment_maxvaluetype_constructor_args():
    sig = inspect.signature(mutatorenvironment_MaxValueType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_minvaluetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_MinValueType)


def test_mutatorenvironment_minvaluetype_constructor_exists():
    assert callable(mutatorenvironment_MinValueType.__init__)


def test_mutatorenvironment_minvaluetype_constructor_args():
    sig = inspect.signature(mutatorenvironment_MinValueType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_BinaryOperator)


def test_mutatorenvironment_binaryoperator_constructor_exists():
    assert callable(mutatorenvironment_BinaryOperator.__init__)


def test_mutatorenvironment_binaryoperator_constructor_args():
    sig = inspect.signature(mutatorenvironment_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mutatorenvironment_binaryoperator_has_type():
    assert hasattr(mutatorenvironment_BinaryOperator, "type")
    descriptor = None
    for klass in mutatorenvironment_BinaryOperator.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_cloneobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CloneObjectMutator)


def test_mutatorenvironment_cloneobjectmutator_constructor_exists():
    assert callable(mutatorenvironment_CloneObjectMutator.__init__)


def test_mutatorenvironment_cloneobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_CloneObjectMutator.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_mutatorenvironment_cloneobjectmutator_has_contents():
    assert hasattr(mutatorenvironment_CloneObjectMutator, "contents")
    descriptor = None
    for klass in mutatorenvironment_CloneObjectMutator.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)



def test_invariantcs_is_not_abstract():
    assert not inspect.isabstract(InvariantCS)


def test_invariantcs_constructor_exists():
    assert callable(InvariantCS.__init__)


def test_invariantcs_constructor_args():
    sig = inspect.signature(InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_referenceset_is_not_abstract():
    assert not inspect.isabstract(ReferenceSet)


def test_referenceset_constructor_exists():
    assert callable(ReferenceSet.__init__)


def test_referenceset_constructor_args():
    sig = inspect.signature(ReferenceSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceadd_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceAdd)


def test_mutatorenvironment_referenceadd_constructor_exists():
    assert callable(mutatorenvironment_ReferenceAdd.__init__)


def test_mutatorenvironment_referenceadd_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceAdd.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceatt_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceAtt)


def test_mutatorenvironment_referenceatt_constructor_exists():
    assert callable(mutatorenvironment_ReferenceAtt.__init__)


def test_mutatorenvironment_referenceatt_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceAtt.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceremove_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceRemove)


def test_mutatorenvironment_referenceremove_constructor_exists():
    assert callable(mutatorenvironment_ReferenceRemove.__init__)


def test_mutatorenvironment_referenceremove_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceRemove.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceswap_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceSwap)


def test_mutatorenvironment_referenceswap_constructor_exists():
    assert callable(mutatorenvironment_ReferenceSwap.__init__)


def test_mutatorenvironment_referenceswap_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceSwap.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceinit_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceInit)


def test_mutatorenvironment_referenceinit_constructor_exists():
    assert callable(mutatorenvironment_ReferenceInit.__init__)


def test_mutatorenvironment_referenceinit_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceInit.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeevaluationtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeEvaluationType)


def test_mutatorenvironment_attributeevaluationtype_constructor_exists():
    assert callable(mutatorenvironment_AttributeEvaluationType.__init__)


def test_mutatorenvironment_attributeevaluationtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeEvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeevaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeEvaluation)


def test_mutatorenvironment_attributeevaluation_constructor_exists():
    assert callable(mutatorenvironment_AttributeEvaluation.__init__)


def test_mutatorenvironment_attributeevaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_evaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_Evaluation)


def test_mutatorenvironment_evaluation_constructor_exists():
    assert callable(mutatorenvironment_Evaluation.__init__)


def test_mutatorenvironment_evaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment_Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_referenceevaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReferenceEvaluation)


def test_mutatorenvironment_referenceevaluation_constructor_exists():
    assert callable(mutatorenvironment_ReferenceEvaluation.__init__)


def test_mutatorenvironment_referenceevaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReferenceEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "container" in params, "Missing parameter 'container'"

def test_mutatorenvironment_referenceevaluation_has_operator():
    assert hasattr(mutatorenvironment_ReferenceEvaluation, "operator")
    descriptor = None
    for klass in mutatorenvironment_ReferenceEvaluation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_referenceevaluation_has_container():
    assert hasattr(mutatorenvironment_ReferenceEvaluation, "container")
    descriptor = None
    for klass in mutatorenvironment_ReferenceEvaluation.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_replacestringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ReplaceStringType)


def test_mutatorenvironment_replacestringtype_constructor_exists():
    assert callable(mutatorenvironment_ReplaceStringType.__init__)


def test_mutatorenvironment_replacestringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_ReplaceStringType.__init__)
    params = list(sig.parameters.keys())
    assert "newstring" in params, "Missing parameter 'newstring'"
    assert "oldstring" in params, "Missing parameter 'oldstring'"

def test_mutatorenvironment_replacestringtype_has_newstring():
    assert hasattr(mutatorenvironment_ReplaceStringType, "newstring")
    descriptor = None
    for klass in mutatorenvironment_ReplaceStringType.__mro__:
        if "newstring" in klass.__dict__:
            descriptor = klass.__dict__["newstring"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_replacestringtype_has_oldstring():
    assert hasattr(mutatorenvironment_ReplaceStringType, "oldstring")
    descriptor = None
    for klass in mutatorenvironment_ReplaceStringType.__mro__:
        if "oldstring" in klass.__dict__:
            descriptor = klass.__dict__["oldstring"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_eattribute_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_EAttribute)


def test_mutatorenvironment_eattribute_constructor_exists():
    assert callable(mutatorenvironment_EAttribute.__init__)


def test_mutatorenvironment_eattribute_constructor_args():
    sig = inspect.signature(mutatorenvironment_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_catendstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CatEndStringType)


def test_mutatorenvironment_catendstringtype_constructor_exists():
    assert callable(mutatorenvironment_CatEndStringType.__init__)


def test_mutatorenvironment_catendstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_CatEndStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_catendstringtype_has_value():
    assert hasattr(mutatorenvironment_CatEndStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_CatEndStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_catstartstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CatStartStringType)


def test_mutatorenvironment_catstartstringtype_constructor_exists():
    assert callable(mutatorenvironment_CatStartStringType.__init__)


def test_mutatorenvironment_catstartstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_CatStartStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_catstartstringtype_has_value():
    assert hasattr(mutatorenvironment_CatStartStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_CatStartStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_lowerstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_LowerStringType)


def test_mutatorenvironment_lowerstringtype_constructor_exists():
    assert callable(mutatorenvironment_LowerStringType.__init__)


def test_mutatorenvironment_lowerstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_LowerStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_lowerstringtype_has_value():
    assert hasattr(mutatorenvironment_LowerStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_LowerStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_upperstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_UpperStringType)


def test_mutatorenvironment_upperstringtype_constructor_exists():
    assert callable(mutatorenvironment_UpperStringType.__init__)


def test_mutatorenvironment_upperstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_UpperStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_upperstringtype_has_value():
    assert hasattr(mutatorenvironment_UpperStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_UpperStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_selectobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SelectObjectMutator)


def test_mutatorenvironment_selectobjectmutator_constructor_exists():
    assert callable(mutatorenvironment_SelectObjectMutator.__init__)


def test_mutatorenvironment_selectobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_SelectObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_otherselection_is_not_abstract():
    assert not inspect.isabstract(OtherSelection)


def test_otherselection_constructor_exists():
    assert callable(OtherSelection.__init__)


def test_otherselection_constructor_args():
    sig = inspect.signature(OtherSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_othertypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_OtherTypeSelection)


def test_mutatorenvironment_othertypeselection_constructor_exists():
    assert callable(mutatorenvironment_OtherTypeSelection.__init__)


def test_mutatorenvironment_othertypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_OtherTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_otherselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_OtherSelection)


def test_mutatorenvironment_otherselection_constructor_exists():
    assert callable(mutatorenvironment_OtherSelection.__init__)


def test_mutatorenvironment_otherselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_OtherSelection.__init__)
    params = list(sig.parameters.keys())



def test_completeselection_is_not_abstract():
    assert not inspect.isabstract(CompleteSelection)


def test_completeselection_constructor_exists():
    assert callable(CompleteSelection.__init__)


def test_completeselection_constructor_args():
    sig = inspect.signature(CompleteSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_completetypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CompleteTypeSelection)


def test_mutatorenvironment_completetypeselection_constructor_exists():
    assert callable(mutatorenvironment_CompleteTypeSelection.__init__)


def test_mutatorenvironment_completetypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_CompleteTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_completeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CompleteSelection)


def test_mutatorenvironment_completeselection_constructor_exists():
    assert callable(mutatorenvironment_CompleteSelection.__init__)


def test_mutatorenvironment_completeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_CompleteSelection.__init__)
    params = list(sig.parameters.keys())



def test_removereferencemutator_is_not_abstract():
    assert not inspect.isabstract(RemoveReferenceMutator)


def test_removereferencemutator_constructor_exists():
    assert callable(RemoveReferenceMutator.__init__)


def test_removereferencemutator_constructor_args():
    sig = inspect.signature(RemoveReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_removespecificreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RemoveSpecificReferenceMutator)


def test_mutatorenvironment_removespecificreferencemutator_constructor_exists():
    assert callable(mutatorenvironment_RemoveSpecificReferenceMutator.__init__)


def test_mutatorenvironment_removespecificreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RemoveSpecificReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_removecompletereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RemoveCompleteReferenceMutator)


def test_mutatorenvironment_removecompletereferencemutator_constructor_exists():
    assert callable(mutatorenvironment_RemoveCompleteReferenceMutator.__init__)


def test_mutatorenvironment_removecompletereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RemoveCompleteReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_removerandomreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RemoveRandomReferenceMutator)


def test_mutatorenvironment_removerandomreferencemutator_constructor_exists():
    assert callable(mutatorenvironment_RemoveRandomReferenceMutator.__init__)


def test_mutatorenvironment_removerandomreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RemoveRandomReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_modifytargetreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ModifyTargetReferenceMutator)


def test_mutatorenvironment_modifytargetreferencemutator_constructor_exists():
    assert callable(mutatorenvironment_ModifyTargetReferenceMutator.__init__)


def test_mutatorenvironment_modifytargetreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_ModifyTargetReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_modifyinformationmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ModifyInformationMutator)


def test_mutatorenvironment_modifyinformationmutator_constructor_exists():
    assert callable(mutatorenvironment_ModifyInformationMutator.__init__)


def test_mutatorenvironment_modifyinformationmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_ModifyInformationMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_removereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RemoveReferenceMutator)


def test_mutatorenvironment_removereferencemutator_constructor_exists():
    assert callable(mutatorenvironment_RemoveReferenceMutator.__init__)


def test_mutatorenvironment_removereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RemoveReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_removeobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RemoveObjectMutator)


def test_mutatorenvironment_removeobjectmutator_constructor_exists():
    assert callable(mutatorenvironment_RemoveObjectMutator.__init__)


def test_mutatorenvironment_removeobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_RemoveObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_createreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_CreateReferenceMutator)


def test_mutatorenvironment_createreferencemutator_constructor_exists():
    assert callable(mutatorenvironment_CreateReferenceMutator.__init__)


def test_mutatorenvironment_createreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_CreateReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_booleantype_is_not_abstract():
    assert not inspect.isabstract(BooleanType)


def test_booleantype_constructor_exists():
    assert callable(BooleanType.__init__)


def test_booleantype_constructor_args():
    sig = inspect.signature(BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randombooleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomBooleanType)


def test_mutatorenvironment_randombooleantype_constructor_exists():
    assert callable(mutatorenvironment_RandomBooleanType.__init__)


def test_mutatorenvironment_randombooleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomBooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment_randombooleantype_has_allowsNull():
    assert hasattr(mutatorenvironment_RandomBooleanType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment_RandomBooleanType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_specificbooleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificBooleanType)


def test_mutatorenvironment_specificbooleantype_constructor_exists():
    assert callable(mutatorenvironment_SpecificBooleanType.__init__)


def test_mutatorenvironment_specificbooleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificBooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_specificbooleantype_has_value():
    assert hasattr(mutatorenvironment_SpecificBooleanType, "value")
    descriptor = None
    for klass in mutatorenvironment_SpecificBooleanType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_listtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ListType)


def test_mutatorenvironment_listtype_constructor_exists():
    assert callable(mutatorenvironment_ListType.__init__)


def test_mutatorenvironment_listtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_ListType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_stringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_StringType)


def test_mutatorenvironment_stringtype_constructor_exists():
    assert callable(mutatorenvironment_StringType.__init__)


def test_mutatorenvironment_stringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_StringType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_numbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_NumberType)


def test_mutatorenvironment_numbertype_constructor_exists():
    assert callable(mutatorenvironment_NumberType.__init__)


def test_mutatorenvironment_numbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment_NumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_liststringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ListStringType)


def test_mutatorenvironment_liststringtype_constructor_exists():
    assert callable(mutatorenvironment_ListStringType.__init__)


def test_mutatorenvironment_liststringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_ListStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment_liststringtype_has_value():
    assert hasattr(mutatorenvironment_ListStringType, "value")
    descriptor = None
    for klass in mutatorenvironment_ListStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_randomtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomType)


def test_mutatorenvironment_randomtype_constructor_exists():
    assert callable(mutatorenvironment_RandomType.__init__)


def test_mutatorenvironment_randomtype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_booleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_BooleanType)


def test_mutatorenvironment_booleantype_constructor_exists():
    assert callable(mutatorenvironment_BooleanType.__init__)


def test_mutatorenvironment_booleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_attributeevaluationtype_is_not_abstract():
    assert not inspect.isabstract(AttributeEvaluationType)


def test_attributeevaluationtype_constructor_exists():
    assert callable(AttributeEvaluationType.__init__)


def test_attributeevaluationtype_constructor_args():
    sig = inspect.signature(AttributeEvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_objectattributetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ObjectAttributeType)


def test_mutatorenvironment_objectattributetype_constructor_exists():
    assert callable(mutatorenvironment_ObjectAttributeType.__init__)


def test_mutatorenvironment_objectattributetype_constructor_args():
    sig = inspect.signature(mutatorenvironment_ObjectAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment_objectattributetype_has_operator():
    assert hasattr(mutatorenvironment_ObjectAttributeType, "operator")
    descriptor = None
    for klass in mutatorenvironment_ObjectAttributeType.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_attributetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeType)


def test_mutatorenvironment_attributetype_constructor_exists():
    assert callable(mutatorenvironment_AttributeType.__init__)


def test_mutatorenvironment_attributetype_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment_attributetype_has_operator():
    assert hasattr(mutatorenvironment_AttributeType, "operator")
    descriptor = None
    for klass in mutatorenvironment_AttributeType.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_attributeset_is_not_abstract():
    assert not inspect.isabstract(AttributeSet)


def test_attributeset_constructor_exists():
    assert callable(AttributeSet.__init__)


def test_attributeset_constructor_args():
    sig = inspect.signature(AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeunset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeUnset)


def test_mutatorenvironment_attributeunset_constructor_exists():
    assert callable(mutatorenvironment_AttributeUnset.__init__)


def test_mutatorenvironment_attributeunset_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeUnset.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeOperation)


def test_mutatorenvironment_attributeoperation_constructor_exists():
    assert callable(mutatorenvironment_AttributeOperation.__init__)


def test_mutatorenvironment_attributeoperation_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment_attributeoperation_has_operator():
    assert hasattr(mutatorenvironment_AttributeOperation, "operator")
    descriptor = None
    for klass in mutatorenvironment_AttributeOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment_attributecopy_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeCopy)


def test_mutatorenvironment_attributecopy_constructor_exists():
    assert callable(mutatorenvironment_AttributeCopy.__init__)


def test_mutatorenvironment_attributecopy_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeCopy.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributereverse_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeReverse)


def test_mutatorenvironment_attributereverse_constructor_exists():
    assert callable(mutatorenvironment_AttributeReverse.__init__)


def test_mutatorenvironment_attributereverse_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeReverse.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributeswap_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeSwap)


def test_mutatorenvironment_attributeswap_constructor_exists():
    assert callable(mutatorenvironment_AttributeSwap.__init__)


def test_mutatorenvironment_attributeswap_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeSwap.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_attributescalar_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_AttributeScalar)


def test_mutatorenvironment_attributescalar_constructor_exists():
    assert callable(mutatorenvironment_AttributeScalar.__init__)


def test_mutatorenvironment_attributescalar_constructor_args():
    sig = inspect.signature(mutatorenvironment_AttributeScalar.__init__)
    params = list(sig.parameters.keys())



def test_specificselection_is_not_abstract():
    assert not inspect.isabstract(SpecificSelection)


def test_specificselection_constructor_exists():
    assert callable(SpecificSelection.__init__)


def test_specificselection_constructor_args():
    sig = inspect.signature(SpecificSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_specificclosureselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificClosureSelection)


def test_mutatorenvironment_specificclosureselection_constructor_exists():
    assert callable(mutatorenvironment_SpecificClosureSelection.__init__)


def test_mutatorenvironment_specificclosureselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificClosureSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_specificobjectselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificObjectSelection)


def test_mutatorenvironment_specificobjectselection_constructor_exists():
    assert callable(mutatorenvironment_SpecificObjectSelection.__init__)


def test_mutatorenvironment_specificobjectselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificObjectSelection.__init__)
    params = list(sig.parameters.keys())



def test_randomselection_is_not_abstract():
    assert not inspect.isabstract(RandomSelection)


def test_randomselection_constructor_exists():
    assert callable(RandomSelection.__init__)


def test_randomselection_constructor_args():
    sig = inspect.signature(RandomSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomtypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomTypeSelection)


def test_mutatorenvironment_randomtypeselection_constructor_exists():
    assert callable(mutatorenvironment_RandomTypeSelection.__init__)


def test_mutatorenvironment_randomtypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_specificreferenceselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificReferenceSelection)


def test_mutatorenvironment_specificreferenceselection_constructor_exists():
    assert callable(mutatorenvironment_SpecificReferenceSelection.__init__)


def test_mutatorenvironment_specificreferenceselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificReferenceSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_specificselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_SpecificSelection)


def test_mutatorenvironment_specificselection_constructor_exists():
    assert callable(mutatorenvironment_SpecificSelection.__init__)


def test_mutatorenvironment_specificselection_constructor_args():
    sig = inspect.signature(mutatorenvironment_SpecificSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_modifysourcereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_ModifySourceReferenceMutator)


def test_mutatorenvironment_modifysourcereferencemutator_constructor_exists():
    assert callable(mutatorenvironment_ModifySourceReferenceMutator.__init__)


def test_mutatorenvironment_modifysourcereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment_ModifySourceReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment_randomdoubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment_RandomDoubleType)


def test_mutatorenvironment_randomdoubletype_constructor_exists():
    assert callable(mutatorenvironment_RandomDoubleType.__init__)


def test_mutatorenvironment_randomdoubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment_RandomDoubleType.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment_randomdoubletype_has_max():
    assert hasattr(mutatorenvironment_RandomDoubleType, "max")
    descriptor = None
    for klass in mutatorenvironment_RandomDoubleType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomdoubletype_has_min():
    assert hasattr(mutatorenvironment_RandomDoubleType, "min")
    descriptor = None
    for klass in mutatorenvironment_RandomDoubleType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment_randomdoubletype_has_allowsNull():
    assert hasattr(mutatorenvironment_RandomDoubleType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment_RandomDoubleType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)

def test_repeat_exists():
    # Check that the Enumeration exists
    assert Repeat is not None

def test_repeat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repeat]
    expected_literals = [
        "no",
        "yes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repeat"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "add",
        "module",
        "subtract",
        "divide",
        "multiply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "different",
        "in_",
        "lte",
        "gte",
        "is_",
        "not_",
        "gt",
        "equals",
        "lt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_logicoperator_exists():
    # Check that the Enumeration exists
    assert LogicOperator is not None

def test_logicoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperator]
    expected_literals = [
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperator"

def test_sampleclause_exists():
    # Check that the Enumeration exists
    assert SampleClause is not None

def test_sampleclause_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SampleClause]
    expected_literals = [
        "distinct",
        "equals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SampleClause"


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
mutatorenvironment_miniOCL_NavigationPathCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationPathCS,
)
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
mutatorenvironment_miniOCL_NavigationPathVariableCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationPathVariableCS,
    varName=
        st.none()
)
mutatorenvironment_miniOCL_NavigationPathElementCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationPathElementCS,
)
mutatorenvironment_miniOCL_NavigationPathNameCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationPathNameCS,
)
NavigationPathNameCS_strategy = st.builds(
    NavigationPathNameCS,
)
DoubleType_strategy = st.builds(
    DoubleType,
)
mutatorenvironment_SpecificDoubleType_strategy = st.builds(
    mutatorenvironment_SpecificDoubleType,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
IntegerType_strategy = st.builds(
    IntegerType,
)
mutatorenvironment_RandomIntegerType_strategy = st.builds(
    mutatorenvironment_RandomIntegerType,
    allowsNull=
        st.none(),
    min=
        st.none(),
    max=
        st.none()
)
mutatorenvironment_SpecificIntegerType_strategy = st.builds(
    mutatorenvironment_SpecificIntegerType,
    value=
        st.none()
)
NumberType_strategy = st.builds(
    NumberType,
)
mutatorenvironment_DoubleType_strategy = st.builds(
    mutatorenvironment_DoubleType,
)
mutatorenvironment_IntegerType_strategy = st.builds(
    mutatorenvironment_IntegerType,
)
StringType_strategy = st.builds(
    StringType,
)
mutatorenvironment_RandomStringType_strategy = st.builds(
    mutatorenvironment_RandomStringType,
    allowsNull=
        st.none(),
    max=
        st.none(),
    min=
        st.none()
)
mutatorenvironment_SpecificStringType_strategy = st.builds(
    mutatorenvironment_SpecificStringType,
    value=
        st.none()
)
mutatorenvironment_ObjectEmitter_strategy = st.builds(
    mutatorenvironment_ObjectEmitter,
    name=
        st.none()
)
mutatorenvironment_Source_strategy = st.builds(
    mutatorenvironment_Source,
    path=
        st.none()
)
Definition_strategy = st.builds(
    Definition,
)
mutatorenvironment_Resource_strategy = st.builds(
    mutatorenvironment_Resource,
    name=
        st.none()
)
mutatorenvironment_Program_strategy = st.builds(
    mutatorenvironment_Program,
    description=
        st.none(),
    exhaustive=
        st.none(),
    output=
        st.none(),
    num=
        st.none()
)
mutatorenvironment_Library_strategy = st.builds(
    mutatorenvironment_Library,
)
mutatorenvironment_Constraint_strategy = st.builds(
    mutatorenvironment_Constraint,
    id=
        st.none(),
    rules=
        st.none()
)
mutatorenvironment_Block_strategy = st.builds(
    mutatorenvironment_Block,
    min=
        st.none(),
    fixed=
        st.none(),
    description=
        st.none(),
    max=
        st.none(),
    repeat=
        st.none(),
    name=
        st.none()
)
ObSelectionStrategy_strategy = st.builds(
    ObSelectionStrategy,
)
mutatorenvironment_RandomSelection_strategy = st.builds(
    mutatorenvironment_RandomSelection,
)
mutatorenvironment_Expression_strategy = st.builds(
    mutatorenvironment_Expression,
)
mutatorenvironment_EReference_strategy = st.builds(
    mutatorenvironment_EReference,
)
mutatorenvironment_ReferenceSet_strategy = st.builds(
    mutatorenvironment_ReferenceSet,
)
mutatorenvironment_AttributeSet_strategy = st.builds(
    mutatorenvironment_AttributeSet,
)
Mutator_strategy = st.builds(
    Mutator,
)
mutatorenvironment_CreateObjectMutator_strategy = st.builds(
    mutatorenvironment_CreateObjectMutator,
)
mutatorenvironment_CompositeMutator_strategy = st.builds(
    mutatorenvironment_CompositeMutator,
)
ObjectEmitter_strategy = st.builds(
    ObjectEmitter,
)
mutatorenvironment_ObSelectionStrategy_strategy = st.builds(
    mutatorenvironment_ObSelectionStrategy,
    resource=
        st.none()
)
mutatorenvironment_EClass_strategy = st.builds(
    mutatorenvironment_EClass,
)
mutatorenvironment_Load_strategy = st.builds(
    mutatorenvironment_Load,
    file=
        st.none()
)
mutatorenvironment_Mutator_strategy = st.builds(
    mutatorenvironment_Mutator,
    max=
        st.none(),
    min=
        st.none(),
    fixed=
        st.none()
)
mutatorenvironment_Definition_strategy = st.builds(
    mutatorenvironment_Definition,
    metamodel=
        st.none()
)
mutatorenvironment_MutatorEnvironment_strategy = st.builds(
    mutatorenvironment_MutatorEnvironment,
)
mutatorenvironment_miniOCL_IteratorVarCS_strategy = st.builds(
    mutatorenvironment_miniOCL_IteratorVarCS,
    itName=
        st.none()
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
mutatorenvironment_miniOCL_IterateExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_IterateExpCS,
)
mutatorenvironment_miniOCL_ForAllExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ForAllExpCS,
)
mutatorenvironment_miniOCL_CollectExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_CollectExpCS,
)
IteratorVarCS_strategy = st.builds(
    IteratorVarCS,
)
mutatorenvironment_miniOCL_ExistsExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ExistsExpCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
mutatorenvironment_miniOCL_BooleanExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_BooleanExpCS,
    boolSymbol=
        st.none()
)
miniOCL_mutatorenvironment_EStructuralFeature_strategy = st.builds(
    miniOCL_mutatorenvironment_EStructuralFeature,
)
mutatorenvironment_miniOCL_PathCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PathCS,
)
PathCS_strategy = st.builds(
    PathCS,
)
mutatorenvironment_miniOCL_PathElementCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PathElementCS,
)
mutatorenvironment_miniOCL_PathVariableCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PathVariableCS,
    varName=
        st.none()
)
mutatorenvironment_miniOCL_PathNameCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PathNameCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
mutatorenvironment_miniOCL_StringLiteralExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_StringLiteralExpCS,
    stringSymbol=
        st.none()
)
mutatorenvironment_miniOCL_BooleanLiteralExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_BooleanLiteralExpCS,
)
mutatorenvironment_miniOCL_IntLiteralExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_IntLiteralExpCS,
    intSymbol=
        st.none()
)
mutatorenvironment_miniOCL_RoundedBracketClauseCS_strategy = st.builds(
    mutatorenvironment_miniOCL_RoundedBracketClauseCS,
)
mutatorenvironment_miniOCL_AccVarCS_strategy = st.builds(
    mutatorenvironment_miniOCL_AccVarCS,
    accVarName=
        st.none()
)
AccVarCS_strategy = st.builds(
    AccVarCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
ParameterCS_strategy = st.builds(
    ParameterCS,
)
mutatorenvironment_miniOCL_OperationCS_strategy = st.builds(
    mutatorenvironment_miniOCL_OperationCS,
    name=
        st.none()
)
mutatorenvironment_miniOCL_PropertyCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PropertyCS,
    name=
        st.none()
)
OperationCS_strategy = st.builds(
    OperationCS,
)
PropertyCS_strategy = st.builds(
    PropertyCS,
)
RoundedBracketClauseCS_strategy = st.builds(
    RoundedBracketClauseCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
mutatorenvironment_miniOCL_LiteralExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_LiteralExpCS,
)
mutatorenvironment_miniOCL_NavigationExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationExpCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
mutatorenvironment_miniOCL_NavigationNameExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NavigationNameExpCS,
)
mutatorenvironment_miniOCL_NameExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_NameExpCS,
)
mutatorenvironment_miniOCL_LoopExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_LoopExpCS,
    logicOp=
        st.none()
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
mutatorenvironment_miniOCL_PrimaryExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PrimaryExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
mutatorenvironment_miniOCL_CallExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_CallExpCS,
)
mutatorenvironment_miniOCL_LogicExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_LogicExpCS,
    op=
        st.none()
)
mutatorenvironment_miniOCL_ExpCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ExpCS,
)
mutatorenvironment_miniOCL_InvariantCS_strategy = st.builds(
    mutatorenvironment_miniOCL_InvariantCS,
)
mutatorenvironment_miniOCL_ConstraintCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ConstraintCS,
)
mutatorenvironment_miniOCL_ParameterCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ParameterCS,
    name=
        st.none()
)
mutatorenvironment_RetypeObjectMutator_strategy = st.builds(
    mutatorenvironment_RetypeObjectMutator,
)
mutatorenvironment_EStructuralFeature_strategy = st.builds(
    mutatorenvironment_EStructuralFeature,
)
mutatorenvironment_SelectSampleMutator_strategy = st.builds(
    mutatorenvironment_SelectSampleMutator,
    clause=
        st.none()
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
mutatorenvironment_miniOCL_ClassCS_strategy = st.builds(
    mutatorenvironment_miniOCL_ClassCS,
    name=
        st.none()
)
ClassCS_strategy = st.builds(
    ClassCS,
)
mutatorenvironment_miniOCL_PackageCS_strategy = st.builds(
    mutatorenvironment_miniOCL_PackageCS,
    name=
        st.none()
)
ConstraintCS_strategy = st.builds(
    ConstraintCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
mutatorenvironment_miniOCL_RootCS_strategy = st.builds(
    mutatorenvironment_miniOCL_RootCS,
)
mutatorenvironment_RandomStringNumberType_strategy = st.builds(
    mutatorenvironment_RandomStringNumberType,
    allowsNull=
        st.none(),
    min=
        st.none(),
    max=
        st.none()
)
mutatorenvironment_TypedSelection_strategy = st.builds(
    mutatorenvironment_TypedSelection,
)
mutatorenvironment_EObject_strategy = st.builds(
    mutatorenvironment_EObject,
)
RandomNumberType_strategy = st.builds(
    RandomNumberType,
)
mutatorenvironment_RandomIntegerNumberType_strategy = st.builds(
    mutatorenvironment_RandomIntegerNumberType,
    min=
        st.none()
)
mutatorenvironment_RandomDoubleNumberType_strategy = st.builds(
    mutatorenvironment_RandomDoubleNumberType,
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mutatorenvironment_RandomNumberType_strategy = st.builds(
    mutatorenvironment_RandomNumberType,
)
mutatorenvironment_MaxValueType_strategy = st.builds(
    mutatorenvironment_MaxValueType,
)
mutatorenvironment_MinValueType_strategy = st.builds(
    mutatorenvironment_MinValueType,
)
mutatorenvironment_BinaryOperator_strategy = st.builds(
    mutatorenvironment_BinaryOperator,
    type=
        st.none()
)
mutatorenvironment_CloneObjectMutator_strategy = st.builds(
    mutatorenvironment_CloneObjectMutator,
    contents=
        st.none()
)
InvariantCS_strategy = st.builds(
    InvariantCS,
)
ReferenceSet_strategy = st.builds(
    ReferenceSet,
)
mutatorenvironment_ReferenceAdd_strategy = st.builds(
    mutatorenvironment_ReferenceAdd,
)
mutatorenvironment_ReferenceAtt_strategy = st.builds(
    mutatorenvironment_ReferenceAtt,
)
mutatorenvironment_ReferenceRemove_strategy = st.builds(
    mutatorenvironment_ReferenceRemove,
)
mutatorenvironment_ReferenceSwap_strategy = st.builds(
    mutatorenvironment_ReferenceSwap,
)
mutatorenvironment_ReferenceInit_strategy = st.builds(
    mutatorenvironment_ReferenceInit,
)
mutatorenvironment_AttributeEvaluationType_strategy = st.builds(
    mutatorenvironment_AttributeEvaluationType,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
mutatorenvironment_AttributeEvaluation_strategy = st.builds(
    mutatorenvironment_AttributeEvaluation,
)
mutatorenvironment_Evaluation_strategy = st.builds(
    mutatorenvironment_Evaluation,
)
mutatorenvironment_ReferenceEvaluation_strategy = st.builds(
    mutatorenvironment_ReferenceEvaluation,
    operator=
        st.none(),
    container=
        st.none()
)
mutatorenvironment_ReplaceStringType_strategy = st.builds(
    mutatorenvironment_ReplaceStringType,
    newstring=
        st.none(),
    oldstring=
        st.none()
)
mutatorenvironment_EAttribute_strategy = st.builds(
    mutatorenvironment_EAttribute,
)
mutatorenvironment_CatEndStringType_strategy = st.builds(
    mutatorenvironment_CatEndStringType,
    value=
        st.none()
)
mutatorenvironment_CatStartStringType_strategy = st.builds(
    mutatorenvironment_CatStartStringType,
    value=
        st.none()
)
mutatorenvironment_LowerStringType_strategy = st.builds(
    mutatorenvironment_LowerStringType,
    value=
        st.none()
)
mutatorenvironment_UpperStringType_strategy = st.builds(
    mutatorenvironment_UpperStringType,
    value=
        st.none()
)
mutatorenvironment_SelectObjectMutator_strategy = st.builds(
    mutatorenvironment_SelectObjectMutator,
)
OtherSelection_strategy = st.builds(
    OtherSelection,
)
mutatorenvironment_OtherTypeSelection_strategy = st.builds(
    mutatorenvironment_OtherTypeSelection,
)
mutatorenvironment_OtherSelection_strategy = st.builds(
    mutatorenvironment_OtherSelection,
)
CompleteSelection_strategy = st.builds(
    CompleteSelection,
)
mutatorenvironment_CompleteTypeSelection_strategy = st.builds(
    mutatorenvironment_CompleteTypeSelection,
)
mutatorenvironment_CompleteSelection_strategy = st.builds(
    mutatorenvironment_CompleteSelection,
)
RemoveReferenceMutator_strategy = st.builds(
    RemoveReferenceMutator,
)
mutatorenvironment_RemoveSpecificReferenceMutator_strategy = st.builds(
    mutatorenvironment_RemoveSpecificReferenceMutator,
)
mutatorenvironment_RemoveCompleteReferenceMutator_strategy = st.builds(
    mutatorenvironment_RemoveCompleteReferenceMutator,
)
mutatorenvironment_RemoveRandomReferenceMutator_strategy = st.builds(
    mutatorenvironment_RemoveRandomReferenceMutator,
)
mutatorenvironment_ModifyTargetReferenceMutator_strategy = st.builds(
    mutatorenvironment_ModifyTargetReferenceMutator,
)
mutatorenvironment_ModifyInformationMutator_strategy = st.builds(
    mutatorenvironment_ModifyInformationMutator,
)
mutatorenvironment_RemoveReferenceMutator_strategy = st.builds(
    mutatorenvironment_RemoveReferenceMutator,
)
mutatorenvironment_RemoveObjectMutator_strategy = st.builds(
    mutatorenvironment_RemoveObjectMutator,
)
mutatorenvironment_CreateReferenceMutator_strategy = st.builds(
    mutatorenvironment_CreateReferenceMutator,
)
BooleanType_strategy = st.builds(
    BooleanType,
)
mutatorenvironment_RandomBooleanType_strategy = st.builds(
    mutatorenvironment_RandomBooleanType,
    allowsNull=
        st.none()
)
mutatorenvironment_SpecificBooleanType_strategy = st.builds(
    mutatorenvironment_SpecificBooleanType,
    value=
        st.none()
)
AttributeType_strategy = st.builds(
    AttributeType,
)
mutatorenvironment_ListType_strategy = st.builds(
    mutatorenvironment_ListType,
)
mutatorenvironment_StringType_strategy = st.builds(
    mutatorenvironment_StringType,
)
mutatorenvironment_NumberType_strategy = st.builds(
    mutatorenvironment_NumberType,
)
mutatorenvironment_ListStringType_strategy = st.builds(
    mutatorenvironment_ListStringType,
    value=
        st.none()
)
mutatorenvironment_RandomType_strategy = st.builds(
    mutatorenvironment_RandomType,
)
mutatorenvironment_BooleanType_strategy = st.builds(
    mutatorenvironment_BooleanType,
)
AttributeEvaluationType_strategy = st.builds(
    AttributeEvaluationType,
)
mutatorenvironment_ObjectAttributeType_strategy = st.builds(
    mutatorenvironment_ObjectAttributeType,
    operator=
        st.none()
)
mutatorenvironment_AttributeType_strategy = st.builds(
    mutatorenvironment_AttributeType,
    operator=
        st.none()
)
AttributeSet_strategy = st.builds(
    AttributeSet,
)
mutatorenvironment_AttributeUnset_strategy = st.builds(
    mutatorenvironment_AttributeUnset,
)
mutatorenvironment_AttributeOperation_strategy = st.builds(
    mutatorenvironment_AttributeOperation,
    operator=
        st.none()
)
mutatorenvironment_AttributeCopy_strategy = st.builds(
    mutatorenvironment_AttributeCopy,
)
mutatorenvironment_AttributeReverse_strategy = st.builds(
    mutatorenvironment_AttributeReverse,
)
mutatorenvironment_AttributeSwap_strategy = st.builds(
    mutatorenvironment_AttributeSwap,
)
mutatorenvironment_AttributeScalar_strategy = st.builds(
    mutatorenvironment_AttributeScalar,
)
SpecificSelection_strategy = st.builds(
    SpecificSelection,
)
mutatorenvironment_SpecificClosureSelection_strategy = st.builds(
    mutatorenvironment_SpecificClosureSelection,
)
mutatorenvironment_SpecificObjectSelection_strategy = st.builds(
    mutatorenvironment_SpecificObjectSelection,
)
RandomSelection_strategy = st.builds(
    RandomSelection,
)
mutatorenvironment_RandomTypeSelection_strategy = st.builds(
    mutatorenvironment_RandomTypeSelection,
)
mutatorenvironment_SpecificReferenceSelection_strategy = st.builds(
    mutatorenvironment_SpecificReferenceSelection,
)
mutatorenvironment_SpecificSelection_strategy = st.builds(
    mutatorenvironment_SpecificSelection,
)
mutatorenvironment_ModifySourceReferenceMutator_strategy = st.builds(
    mutatorenvironment_ModifySourceReferenceMutator,
)
mutatorenvironment_RandomDoubleType_strategy = st.builds(
    mutatorenvironment_RandomDoubleType,
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    allowsNull=
        st.none()
)

@given(instance=mutatorenvironment_miniOCL_NavigationPathCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationpathcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathCS)

@given(instance=NavigationPathCS_strategy)
@settings(max_examples=50)
def test_navigationpathcs_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)

@given(instance=mutatorenvironment_miniOCL_NavigationPathVariableCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationpathvariablecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathVariableCS)



@given(instance=mutatorenvironment_miniOCL_NavigationPathVariableCS_strategy)
def test_mutatorenvironment_miniocl_navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=mutatorenvironment_miniOCL_NavigationPathElementCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationpathelementcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathElementCS)

@given(instance=mutatorenvironment_miniOCL_NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathNameCS)

@given(instance=NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, NavigationPathNameCS)

@given(instance=DoubleType_strategy)
@settings(max_examples=50)
def test_doubletype_instantiation(instance):
    assert isinstance(instance, DoubleType)

@given(instance=mutatorenvironment_SpecificDoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificdoubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificDoubleType)



@given(instance=mutatorenvironment_SpecificDoubleType_strategy)
def test_mutatorenvironment_specificdoubletype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=mutatorenvironment_RandomIntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomintegertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomIntegerType)



@given(instance=mutatorenvironment_RandomIntegerType_strategy)
def test_mutatorenvironment_randomintegertype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original



@given(instance=mutatorenvironment_RandomIntegerType_strategy)
def test_mutatorenvironment_randomintegertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=mutatorenvironment_RandomIntegerType_strategy)
def test_mutatorenvironment_randomintegertype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment_SpecificIntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificintegertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificIntegerType)



@given(instance=mutatorenvironment_SpecificIntegerType_strategy)
def test_mutatorenvironment_specificintegertype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=mutatorenvironment_DoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_doubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_DoubleType)

@given(instance=mutatorenvironment_IntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_integertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_IntegerType)

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=mutatorenvironment_RandomStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomStringType)



@given(instance=mutatorenvironment_RandomStringType_strategy)
def test_mutatorenvironment_randomstringtype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original



@given(instance=mutatorenvironment_RandomStringType_strategy)
def test_mutatorenvironment_randomstringtype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=mutatorenvironment_RandomStringType_strategy)
def test_mutatorenvironment_randomstringtype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment_SpecificStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificStringType)



@given(instance=mutatorenvironment_SpecificStringType_strategy)
def test_mutatorenvironment_specificstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_ObjectEmitter_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_objectemitter_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ObjectEmitter)



@given(instance=mutatorenvironment_ObjectEmitter_strategy)
def test_mutatorenvironment_objectemitter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment_Source_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_source_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Source)



@given(instance=mutatorenvironment_Source_strategy)
def test_mutatorenvironment_source_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=mutatorenvironment_Resource_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_resource_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Resource)



@given(instance=mutatorenvironment_Resource_strategy)
def test_mutatorenvironment_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment_Program_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_program_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Program)



@given(instance=mutatorenvironment_Program_strategy)
def test_mutatorenvironment_program_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mutatorenvironment_Program_strategy)
def test_mutatorenvironment_program_exhaustive_setter(instance):
    original = instance.exhaustive
    instance.exhaustive = original
    assert instance.exhaustive == original



@given(instance=mutatorenvironment_Program_strategy)
def test_mutatorenvironment_program_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=mutatorenvironment_Program_strategy)
def test_mutatorenvironment_program_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=mutatorenvironment_Library_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_library_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Library)

@given(instance=mutatorenvironment_Constraint_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_constraint_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Constraint)



@given(instance=mutatorenvironment_Constraint_strategy)
def test_mutatorenvironment_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=mutatorenvironment_Constraint_strategy)
def test_mutatorenvironment_constraint_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=mutatorenvironment_Block_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_block_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Block)



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=mutatorenvironment_Block_strategy)
def test_mutatorenvironment_block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ObSelectionStrategy_strategy)
@settings(max_examples=50)
def test_obselectionstrategy_instantiation(instance):
    assert isinstance(instance, ObSelectionStrategy)

@given(instance=mutatorenvironment_RandomSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomSelection)

@given(instance=mutatorenvironment_Expression_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_expression_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Expression)

@given(instance=mutatorenvironment_EReference_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_ereference_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EReference)

@given(instance=mutatorenvironment_ReferenceSet_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceSet)

@given(instance=mutatorenvironment_AttributeSet_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeSet)

@given(instance=Mutator_strategy)
@settings(max_examples=50)
def test_mutator_instantiation(instance):
    assert isinstance(instance, Mutator)

@given(instance=mutatorenvironment_CreateObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_createobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CreateObjectMutator)

@given(instance=mutatorenvironment_CompositeMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_compositemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompositeMutator)

@given(instance=ObjectEmitter_strategy)
@settings(max_examples=50)
def test_objectemitter_instantiation(instance):
    assert isinstance(instance, ObjectEmitter)

@given(instance=mutatorenvironment_ObSelectionStrategy_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_obselectionstrategy_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ObSelectionStrategy)



@given(instance=mutatorenvironment_ObSelectionStrategy_strategy)
def test_mutatorenvironment_obselectionstrategy_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=mutatorenvironment_EClass_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_eclass_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EClass)

@given(instance=mutatorenvironment_Load_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_load_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Load)



@given(instance=mutatorenvironment_Load_strategy)
def test_mutatorenvironment_load_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=mutatorenvironment_Mutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_mutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Mutator)



@given(instance=mutatorenvironment_Mutator_strategy)
def test_mutatorenvironment_mutator_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=mutatorenvironment_Mutator_strategy)
def test_mutatorenvironment_mutator_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=mutatorenvironment_Mutator_strategy)
def test_mutatorenvironment_mutator_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original

@given(instance=mutatorenvironment_Definition_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_definition_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Definition)



@given(instance=mutatorenvironment_Definition_strategy)
def test_mutatorenvironment_definition_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=mutatorenvironment_MutatorEnvironment_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_mutatorenvironment_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MutatorEnvironment)

@given(instance=mutatorenvironment_miniOCL_IteratorVarCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_IteratorVarCS)



@given(instance=mutatorenvironment_miniOCL_IteratorVarCS_strategy)
def test_mutatorenvironment_miniocl_iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=mutatorenvironment_miniOCL_IterateExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_iterateexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_IterateExpCS)

@given(instance=mutatorenvironment_miniOCL_ForAllExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_forallexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ForAllExpCS)

@given(instance=mutatorenvironment_miniOCL_CollectExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_collectexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_CollectExpCS)

@given(instance=IteratorVarCS_strategy)
@settings(max_examples=50)
def test_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, IteratorVarCS)

@given(instance=mutatorenvironment_miniOCL_ExistsExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_existsexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ExistsExpCS)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=mutatorenvironment_miniOCL_BooleanExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_booleanexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_BooleanExpCS)



@given(instance=mutatorenvironment_miniOCL_BooleanExpCS_strategy)
def test_mutatorenvironment_miniocl_booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=miniOCL_mutatorenvironment_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_miniocl_mutatorenvironment_estructuralfeature_instantiation(instance):
    assert isinstance(instance, miniOCL_mutatorenvironment_EStructuralFeature)

@given(instance=mutatorenvironment_miniOCL_PathCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_pathcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathCS)

@given(instance=PathCS_strategy)
@settings(max_examples=50)
def test_pathcs_instantiation(instance):
    assert isinstance(instance, PathCS)

@given(instance=mutatorenvironment_miniOCL_PathElementCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_pathelementcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathElementCS)

@given(instance=mutatorenvironment_miniOCL_PathVariableCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_pathvariablecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathVariableCS)



@given(instance=mutatorenvironment_miniOCL_PathVariableCS_strategy)
def test_mutatorenvironment_miniocl_pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=mutatorenvironment_miniOCL_PathNameCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_pathnamecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathNameCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=mutatorenvironment_miniOCL_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_StringLiteralExpCS)



@given(instance=mutatorenvironment_miniOCL_StringLiteralExpCS_strategy)
def test_mutatorenvironment_miniocl_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=mutatorenvironment_miniOCL_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_BooleanLiteralExpCS)

@given(instance=mutatorenvironment_miniOCL_IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_intliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_IntLiteralExpCS)



@given(instance=mutatorenvironment_miniOCL_IntLiteralExpCS_strategy)
def test_mutatorenvironment_miniocl_intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=mutatorenvironment_miniOCL_RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_RoundedBracketClauseCS)

@given(instance=mutatorenvironment_miniOCL_AccVarCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_accvarcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_AccVarCS)



@given(instance=mutatorenvironment_miniOCL_AccVarCS_strategy)
def test_mutatorenvironment_miniocl_accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original

@given(instance=AccVarCS_strategy)
@settings(max_examples=50)
def test_accvarcs_instantiation(instance):
    assert isinstance(instance, AccVarCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=ParameterCS_strategy)
@settings(max_examples=50)
def test_parametercs_instantiation(instance):
    assert isinstance(instance, ParameterCS)

@given(instance=mutatorenvironment_miniOCL_OperationCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_operationcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_OperationCS)



@given(instance=mutatorenvironment_miniOCL_OperationCS_strategy)
def test_mutatorenvironment_miniocl_operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment_miniOCL_PropertyCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_propertycs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PropertyCS)



@given(instance=mutatorenvironment_miniOCL_PropertyCS_strategy)
def test_mutatorenvironment_miniocl_propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=PropertyCS_strategy)
@settings(max_examples=50)
def test_propertycs_instantiation(instance):
    assert isinstance(instance, PropertyCS)

@given(instance=RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, RoundedBracketClauseCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=mutatorenvironment_miniOCL_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_literalexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_LiteralExpCS)

@given(instance=mutatorenvironment_miniOCL_NavigationExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationExpCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=mutatorenvironment_miniOCL_NavigationNameExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_navigationnameexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationNameExpCS)

@given(instance=mutatorenvironment_miniOCL_NameExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_nameexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NameExpCS)

@given(instance=mutatorenvironment_miniOCL_LoopExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_loopexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_LoopExpCS)



@given(instance=mutatorenvironment_miniOCL_LoopExpCS_strategy)
def test_mutatorenvironment_miniocl_loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=mutatorenvironment_miniOCL_PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_primaryexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PrimaryExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=mutatorenvironment_miniOCL_CallExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_callexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_CallExpCS)

@given(instance=mutatorenvironment_miniOCL_LogicExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_logicexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_LogicExpCS)



@given(instance=mutatorenvironment_miniOCL_LogicExpCS_strategy)
def test_mutatorenvironment_miniocl_logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mutatorenvironment_miniOCL_ExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_expcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ExpCS)

@given(instance=mutatorenvironment_miniOCL_InvariantCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_invariantcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_InvariantCS)

@given(instance=mutatorenvironment_miniOCL_ConstraintCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_constraintcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ConstraintCS)

@given(instance=mutatorenvironment_miniOCL_ParameterCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_parametercs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ParameterCS)



@given(instance=mutatorenvironment_miniOCL_ParameterCS_strategy)
def test_mutatorenvironment_miniocl_parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment_RetypeObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_retypeobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RetypeObjectMutator)

@given(instance=mutatorenvironment_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_estructuralfeature_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EStructuralFeature)

@given(instance=mutatorenvironment_SelectSampleMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_selectsamplemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SelectSampleMutator)



@given(instance=mutatorenvironment_SelectSampleMutator_strategy)
def test_mutatorenvironment_selectsamplemutator_clause_setter(instance):
    original = instance.clause
    instance.clause = original
    assert instance.clause == original

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=mutatorenvironment_miniOCL_ClassCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_classcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ClassCS)



@given(instance=mutatorenvironment_miniOCL_ClassCS_strategy)
def test_mutatorenvironment_miniocl_classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassCS_strategy)
@settings(max_examples=50)
def test_classcs_instantiation(instance):
    assert isinstance(instance, ClassCS)

@given(instance=mutatorenvironment_miniOCL_PackageCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_packagecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PackageCS)



@given(instance=mutatorenvironment_miniOCL_PackageCS_strategy)
def test_mutatorenvironment_miniocl_packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConstraintCS_strategy)
@settings(max_examples=50)
def test_constraintcs_instantiation(instance):
    assert isinstance(instance, ConstraintCS)

@given(instance=PackageCS_strategy)
@settings(max_examples=50)
def test_packagecs_instantiation(instance):
    assert isinstance(instance, PackageCS)

@given(instance=mutatorenvironment_miniOCL_RootCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_miniocl_rootcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_RootCS)

@given(instance=mutatorenvironment_RandomStringNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomstringnumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomStringNumberType)



@given(instance=mutatorenvironment_RandomStringNumberType_strategy)
def test_mutatorenvironment_randomstringnumbertype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original



@given(instance=mutatorenvironment_RandomStringNumberType_strategy)
def test_mutatorenvironment_randomstringnumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=mutatorenvironment_RandomStringNumberType_strategy)
def test_mutatorenvironment_randomstringnumbertype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment_TypedSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_typedselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_TypedSelection)

@given(instance=mutatorenvironment_EObject_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_eobject_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EObject)

@given(instance=RandomNumberType_strategy)
@settings(max_examples=50)
def test_randomnumbertype_instantiation(instance):
    assert isinstance(instance, RandomNumberType)

@given(instance=mutatorenvironment_RandomIntegerNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomintegernumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomIntegerNumberType)



@given(instance=mutatorenvironment_RandomIntegerNumberType_strategy)
def test_mutatorenvironment_randomintegernumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment_RandomDoubleNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomdoublenumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomDoubleNumberType)



@given(instance=mutatorenvironment_RandomDoubleNumberType_strategy)
def test_mutatorenvironment_randomdoublenumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment_RandomNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomnumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomNumberType)

@given(instance=mutatorenvironment_MaxValueType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_maxvaluetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MaxValueType)

@given(instance=mutatorenvironment_MinValueType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_minvaluetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MinValueType)

@given(instance=mutatorenvironment_BinaryOperator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_binaryoperator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_BinaryOperator)



@given(instance=mutatorenvironment_BinaryOperator_strategy)
def test_mutatorenvironment_binaryoperator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mutatorenvironment_CloneObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_cloneobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CloneObjectMutator)



@given(instance=mutatorenvironment_CloneObjectMutator_strategy)
def test_mutatorenvironment_cloneobjectmutator_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=InvariantCS_strategy)
@settings(max_examples=50)
def test_invariantcs_instantiation(instance):
    assert isinstance(instance, InvariantCS)

@given(instance=ReferenceSet_strategy)
@settings(max_examples=50)
def test_referenceset_instantiation(instance):
    assert isinstance(instance, ReferenceSet)

@given(instance=mutatorenvironment_ReferenceAdd_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceadd_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceAdd)

@given(instance=mutatorenvironment_ReferenceAtt_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceatt_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceAtt)

@given(instance=mutatorenvironment_ReferenceRemove_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceremove_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceRemove)

@given(instance=mutatorenvironment_ReferenceSwap_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceswap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceSwap)

@given(instance=mutatorenvironment_ReferenceInit_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceinit_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceInit)

@given(instance=mutatorenvironment_AttributeEvaluationType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeevaluationtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeEvaluationType)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=mutatorenvironment_AttributeEvaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeevaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeEvaluation)

@given(instance=mutatorenvironment_Evaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_evaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Evaluation)

@given(instance=mutatorenvironment_ReferenceEvaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_referenceevaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceEvaluation)



@given(instance=mutatorenvironment_ReferenceEvaluation_strategy)
def test_mutatorenvironment_referenceevaluation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=mutatorenvironment_ReferenceEvaluation_strategy)
def test_mutatorenvironment_referenceevaluation_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=mutatorenvironment_ReplaceStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_replacestringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReplaceStringType)



@given(instance=mutatorenvironment_ReplaceStringType_strategy)
def test_mutatorenvironment_replacestringtype_newstring_setter(instance):
    original = instance.newstring
    instance.newstring = original
    assert instance.newstring == original



@given(instance=mutatorenvironment_ReplaceStringType_strategy)
def test_mutatorenvironment_replacestringtype_oldstring_setter(instance):
    original = instance.oldstring
    instance.oldstring = original
    assert instance.oldstring == original

@given(instance=mutatorenvironment_EAttribute_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_eattribute_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EAttribute)

@given(instance=mutatorenvironment_CatEndStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_catendstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CatEndStringType)



@given(instance=mutatorenvironment_CatEndStringType_strategy)
def test_mutatorenvironment_catendstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_CatStartStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_catstartstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CatStartStringType)



@given(instance=mutatorenvironment_CatStartStringType_strategy)
def test_mutatorenvironment_catstartstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_LowerStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_lowerstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_LowerStringType)



@given(instance=mutatorenvironment_LowerStringType_strategy)
def test_mutatorenvironment_lowerstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_UpperStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_upperstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_UpperStringType)



@given(instance=mutatorenvironment_UpperStringType_strategy)
def test_mutatorenvironment_upperstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_SelectObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_selectobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SelectObjectMutator)

@given(instance=OtherSelection_strategy)
@settings(max_examples=50)
def test_otherselection_instantiation(instance):
    assert isinstance(instance, OtherSelection)

@given(instance=mutatorenvironment_OtherTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_othertypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_OtherTypeSelection)

@given(instance=mutatorenvironment_OtherSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_otherselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_OtherSelection)

@given(instance=CompleteSelection_strategy)
@settings(max_examples=50)
def test_completeselection_instantiation(instance):
    assert isinstance(instance, CompleteSelection)

@given(instance=mutatorenvironment_CompleteTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_completetypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompleteTypeSelection)

@given(instance=mutatorenvironment_CompleteSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_completeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompleteSelection)

@given(instance=RemoveReferenceMutator_strategy)
@settings(max_examples=50)
def test_removereferencemutator_instantiation(instance):
    assert isinstance(instance, RemoveReferenceMutator)

@given(instance=mutatorenvironment_RemoveSpecificReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_removespecificreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveSpecificReferenceMutator)

@given(instance=mutatorenvironment_RemoveCompleteReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_removecompletereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveCompleteReferenceMutator)

@given(instance=mutatorenvironment_RemoveRandomReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_removerandomreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveRandomReferenceMutator)

@given(instance=mutatorenvironment_ModifyTargetReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_modifytargetreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifyTargetReferenceMutator)

@given(instance=mutatorenvironment_ModifyInformationMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_modifyinformationmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifyInformationMutator)

@given(instance=mutatorenvironment_RemoveReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_removereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveReferenceMutator)

@given(instance=mutatorenvironment_RemoveObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_removeobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveObjectMutator)

@given(instance=mutatorenvironment_CreateReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_createreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CreateReferenceMutator)

@given(instance=BooleanType_strategy)
@settings(max_examples=50)
def test_booleantype_instantiation(instance):
    assert isinstance(instance, BooleanType)

@given(instance=mutatorenvironment_RandomBooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randombooleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomBooleanType)



@given(instance=mutatorenvironment_RandomBooleanType_strategy)
def test_mutatorenvironment_randombooleantype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment_SpecificBooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificbooleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificBooleanType)



@given(instance=mutatorenvironment_SpecificBooleanType_strategy)
def test_mutatorenvironment_specificbooleantype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=mutatorenvironment_ListType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_listtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ListType)

@given(instance=mutatorenvironment_StringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_stringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_StringType)

@given(instance=mutatorenvironment_NumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_numbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_NumberType)

@given(instance=mutatorenvironment_ListStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_liststringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ListStringType)



@given(instance=mutatorenvironment_ListStringType_strategy)
def test_mutatorenvironment_liststringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment_RandomType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomType)

@given(instance=mutatorenvironment_BooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_booleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_BooleanType)

@given(instance=AttributeEvaluationType_strategy)
@settings(max_examples=50)
def test_attributeevaluationtype_instantiation(instance):
    assert isinstance(instance, AttributeEvaluationType)

@given(instance=mutatorenvironment_ObjectAttributeType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_objectattributetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ObjectAttributeType)



@given(instance=mutatorenvironment_ObjectAttributeType_strategy)
def test_mutatorenvironment_objectattributetype_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mutatorenvironment_AttributeType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeType)



@given(instance=mutatorenvironment_AttributeType_strategy)
def test_mutatorenvironment_attributetype_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AttributeSet_strategy)
@settings(max_examples=50)
def test_attributeset_instantiation(instance):
    assert isinstance(instance, AttributeSet)

@given(instance=mutatorenvironment_AttributeUnset_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeunset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeUnset)

@given(instance=mutatorenvironment_AttributeOperation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeoperation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeOperation)



@given(instance=mutatorenvironment_AttributeOperation_strategy)
def test_mutatorenvironment_attributeoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mutatorenvironment_AttributeCopy_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributecopy_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeCopy)

@given(instance=mutatorenvironment_AttributeReverse_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributereverse_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeReverse)

@given(instance=mutatorenvironment_AttributeSwap_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributeswap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeSwap)

@given(instance=mutatorenvironment_AttributeScalar_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_attributescalar_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeScalar)

@given(instance=SpecificSelection_strategy)
@settings(max_examples=50)
def test_specificselection_instantiation(instance):
    assert isinstance(instance, SpecificSelection)

@given(instance=mutatorenvironment_SpecificClosureSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificclosureselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificClosureSelection)

@given(instance=mutatorenvironment_SpecificObjectSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificobjectselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificObjectSelection)

@given(instance=RandomSelection_strategy)
@settings(max_examples=50)
def test_randomselection_instantiation(instance):
    assert isinstance(instance, RandomSelection)

@given(instance=mutatorenvironment_RandomTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomtypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomTypeSelection)

@given(instance=mutatorenvironment_SpecificReferenceSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificreferenceselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificReferenceSelection)

@given(instance=mutatorenvironment_SpecificSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_specificselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificSelection)

@given(instance=mutatorenvironment_ModifySourceReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_modifysourcereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifySourceReferenceMutator)

@given(instance=mutatorenvironment_RandomDoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment_randomdoubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomDoubleType)



@given(instance=mutatorenvironment_RandomDoubleType_strategy)
def test_mutatorenvironment_randomdoubletype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=mutatorenvironment_RandomDoubleType_strategy)
def test_mutatorenvironment_randomdoubletype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=mutatorenvironment_RandomDoubleType_strategy)
def test_mutatorenvironment_randomdoubletype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

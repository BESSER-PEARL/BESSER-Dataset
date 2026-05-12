import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ValueExpression,
    vhdl_UnitValueExpression,
    vhdl_ValueExpression,
    ArrayTypeDefinition,
    vhdl_ConstrainedArrayTypeDefinition,
    vhdl_UnconstrainedArrayTypeDefinition,
    CompositeTypeDefinition,
    vhdl_ArrayTypeDefinition,
    vhdl_RecordTypeDefinition,
    vhdl_RecordField,
    TypeDefinition,
    vhdl_FileTypeDefinition,
    vhdl_EnumerationTypeDefinition,
    vhdl_CompositeTypeDefinition,
    vhdl_AccessTypeDefinition,
    vhdl_TypeDefinition,
    Type,
    vhdl_TypeDeclaration,
    vhdl_SubtypeDeclaration,
    Expression,
    vhdl_AddingExpression,
    vhdl_BitString,
    vhdl_Member,
    vhdl_Boolean,
    vhdl_Others,
    vhdl_Char,
    vhdl_Value,
    vhdl_MultiplyingExpression,
    vhdl_Factor,
    vhdl_ChoiceExpression,
    vhdl_MemberExpression,
    vhdl_ShiftExpression,
    vhdl_MultiExpression,
    vhdl_Variable,
    vhdl_RelationalExpression,
    vhdl_LogicalExpression,
    vhdl_ConditionalWaveformExpression,
    vhdl_BuiltinFuncs,
    vhdl_Open,
    vhdl_SliceExpression,
    vhdl_RangeExpression,
    vhdl_String,
    vhdl_IfStatementTest,
    IterationScheme,
    vhdl_ForIterationScheme,
    vhdl_WhileIterationScheme,
    vhdl_IterationScheme,
    vhdl_CaseAlternative,
    vhdl_GenericMapAssociation,
    vhdl_PortMapAssociation,
    SequentialStatement,
    vhdl_SequentialSignalAssignmentStatement,
    vhdl_CaseStatement,
    vhdl_IfStatement,
    vhdl_LoopStatement,
    vhdl_WaitStatement,
    vhdl_PortMap,
    vhdl_GenericMap,
    vhdl_SequentialStatement,
    vhdl_IdList,
    ArchitectureStatement,
    vhdl_ForGenerateStatement,
    vhdl_ComponentInstantiationStatement,
    vhdl_ConditionalSignalAssignmentStatement,
    vhdl_EntityInstantiationStatement,
    vhdl_IfGenerateStatement,
    vhdl_ProcessStatement,
    vhdl_SubtypeIndication,
    Variable,
    vhdl_LoopVariable,
    vhdl_Constant,
    vhdl_Port,
    vhdl_Ports,
    vhdl_Generics,
    vhdl_Var,
    vhdl_Signal,
    package_declarative_item,
    BlockDeclarativeItem,
    vhdl_VariableDeclaration,
    vhdl_Type,
    vhdl_ConstantDeclaration,
    vhdl_SignalDeclaration,
    vhdl_Component,
    vhdl_AttributeDeclaration,
    vhdl_AttributeSpecification,
    vhdl_Alias,
    vhdl_Generic,
    vhdl_Expression,
    vhdl_DesignFile,
    vhdl_ArchitectureStatement,
    vhdl_BlockDeclarativeItem,
    vhdl_package_declarative_part,
    vhdl_package_declarative_item,
    LibraryUnit,
    vhdl_Architecture,
    vhdl_Entity,
    vhdl_Package,
    vhdl_Library,
    ContextItem,
    vhdl_LibraryClause,
    vhdl_UseClause,
    vhdl_LibraryUnit,
    vhdl_ContextItem,
    AddingOperator,
    UnaryOperator,
    ShiftOperator,
    BuiltinLibs,
    EString,
    RangeDirection,
    LogicalOperator,
    SignalKind,
    EntityClass,
    RelationalOperator,
    Sign,
    Purity,
    Mode,
    MultiplyingOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_unitvalueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_UnitValueExpression)


def test_vhdl_unitvalueexpression_constructor_exists():
    assert callable(vhdl_UnitValueExpression.__init__)


def test_vhdl_unitvalueexpression_constructor_args():
    sig = inspect.signature(vhdl_UnitValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_vhdl_unitvalueexpression_has_unit():
    assert hasattr(vhdl_UnitValueExpression, "unit")
    descriptor = None
    for klass in vhdl_UnitValueExpression.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_valueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_ValueExpression)


def test_vhdl_valueexpression_constructor_exists():
    assert callable(vhdl_ValueExpression.__init__)


def test_vhdl_valueexpression_constructor_args():
    sig = inspect.signature(vhdl_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_valueexpression_has_value():
    assert hasattr(vhdl_ValueExpression, "value")
    descriptor = None
    for klass in vhdl_ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeDefinition)


def test_arraytypedefinition_constructor_exists():
    assert callable(ArrayTypeDefinition.__init__)


def test_arraytypedefinition_constructor_args():
    sig = inspect.signature(ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_constrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_ConstrainedArrayTypeDefinition)


def test_vhdl_constrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl_ConstrainedArrayTypeDefinition.__init__)


def test_vhdl_constrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_ConstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_unconstrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_UnconstrainedArrayTypeDefinition)


def test_vhdl_unconstrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl_UnconstrainedArrayTypeDefinition.__init__)


def test_vhdl_unconstrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_UnconstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_vhdl_unconstrainedarraytypedefinition_has_index():
    assert hasattr(vhdl_UnconstrainedArrayTypeDefinition, "index")
    descriptor = None
    for klass in vhdl_UnconstrainedArrayTypeDefinition.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeTypeDefinition)


def test_compositetypedefinition_constructor_exists():
    assert callable(CompositeTypeDefinition.__init__)


def test_compositetypedefinition_constructor_args():
    sig = inspect.signature(CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_ArrayTypeDefinition)


def test_vhdl_arraytypedefinition_constructor_exists():
    assert callable(vhdl_ArrayTypeDefinition.__init__)


def test_vhdl_arraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_RecordTypeDefinition)


def test_vhdl_recordtypedefinition_constructor_exists():
    assert callable(vhdl_RecordTypeDefinition.__init__)


def test_vhdl_recordtypedefinition_constructor_args():
    sig = inspect.signature(vhdl_RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_recordfield_is_not_abstract():
    assert not inspect.isabstract(vhdl_RecordField)


def test_vhdl_recordfield_constructor_exists():
    assert callable(vhdl_RecordField.__init__)


def test_vhdl_recordfield_constructor_args():
    sig = inspect.signature(vhdl_RecordField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_recordfield_has_name():
    assert hasattr(vhdl_RecordField, "name")
    descriptor = None
    for klass in vhdl_RecordField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_filetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_FileTypeDefinition)


def test_vhdl_filetypedefinition_constructor_exists():
    assert callable(vhdl_FileTypeDefinition.__init__)


def test_vhdl_filetypedefinition_constructor_args():
    sig = inspect.signature(vhdl_FileTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_vhdl_filetypedefinition_has_type():
    assert hasattr(vhdl_FileTypeDefinition, "type")
    descriptor = None
    for klass in vhdl_FileTypeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_EnumerationTypeDefinition)


def test_vhdl_enumerationtypedefinition_constructor_exists():
    assert callable(vhdl_EnumerationTypeDefinition.__init__)


def test_vhdl_enumerationtypedefinition_constructor_args():
    sig = inspect.signature(vhdl_EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_vhdl_enumerationtypedefinition_has_literal():
    assert hasattr(vhdl_EnumerationTypeDefinition, "literal")
    descriptor = None
    for klass in vhdl_EnumerationTypeDefinition.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_CompositeTypeDefinition)


def test_vhdl_compositetypedefinition_constructor_exists():
    assert callable(vhdl_CompositeTypeDefinition.__init__)


def test_vhdl_compositetypedefinition_constructor_args():
    sig = inspect.signature(vhdl_CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_AccessTypeDefinition)


def test_vhdl_accesstypedefinition_constructor_exists():
    assert callable(vhdl_AccessTypeDefinition.__init__)


def test_vhdl_accesstypedefinition_constructor_args():
    sig = inspect.signature(vhdl_AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_typedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_TypeDefinition)


def test_vhdl_typedefinition_constructor_exists():
    assert callable(vhdl_TypeDefinition.__init__)


def test_vhdl_typedefinition_constructor_args():
    sig = inspect.signature(vhdl_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_TypeDeclaration)


def test_vhdl_typedeclaration_constructor_exists():
    assert callable(vhdl_TypeDeclaration.__init__)


def test_vhdl_typedeclaration_constructor_args():
    sig = inspect.signature(vhdl_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_SubtypeDeclaration)


def test_vhdl_subtypedeclaration_constructor_exists():
    assert callable(vhdl_SubtypeDeclaration.__init__)


def test_vhdl_subtypedeclaration_constructor_args():
    sig = inspect.signature(vhdl_SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_addingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_AddingExpression)


def test_vhdl_addingexpression_constructor_exists():
    assert callable(vhdl_AddingExpression.__init__)


def test_vhdl_addingexpression_constructor_args():
    sig = inspect.signature(vhdl_AddingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_addingexpression_has_operator():
    assert hasattr(vhdl_AddingExpression, "operator")
    descriptor = None
    for klass in vhdl_AddingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_bitstring_is_not_abstract():
    assert not inspect.isabstract(vhdl_BitString)


def test_vhdl_bitstring_constructor_exists():
    assert callable(vhdl_BitString.__init__)


def test_vhdl_bitstring_constructor_args():
    sig = inspect.signature(vhdl_BitString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_bitstring_has_value():
    assert hasattr(vhdl_BitString, "value")
    descriptor = None
    for klass in vhdl_BitString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_member_is_not_abstract():
    assert not inspect.isabstract(vhdl_Member)


def test_vhdl_member_constructor_exists():
    assert callable(vhdl_Member.__init__)


def test_vhdl_member_constructor_args():
    sig = inspect.signature(vhdl_Member.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_boolean_is_not_abstract():
    assert not inspect.isabstract(vhdl_Boolean)


def test_vhdl_boolean_constructor_exists():
    assert callable(vhdl_Boolean.__init__)


def test_vhdl_boolean_constructor_args():
    sig = inspect.signature(vhdl_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_boolean_has_value():
    assert hasattr(vhdl_Boolean, "value")
    descriptor = None
    for klass in vhdl_Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_others_is_not_abstract():
    assert not inspect.isabstract(vhdl_Others)


def test_vhdl_others_constructor_exists():
    assert callable(vhdl_Others.__init__)


def test_vhdl_others_constructor_args():
    sig = inspect.signature(vhdl_Others.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_others_has_value():
    assert hasattr(vhdl_Others, "value")
    descriptor = None
    for klass in vhdl_Others.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_char_is_not_abstract():
    assert not inspect.isabstract(vhdl_Char)


def test_vhdl_char_constructor_exists():
    assert callable(vhdl_Char.__init__)


def test_vhdl_char_constructor_args():
    sig = inspect.signature(vhdl_Char.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_char_has_value():
    assert hasattr(vhdl_Char, "value")
    descriptor = None
    for klass in vhdl_Char.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_value_is_not_abstract():
    assert not inspect.isabstract(vhdl_Value)


def test_vhdl_value_constructor_exists():
    assert callable(vhdl_Value.__init__)


def test_vhdl_value_constructor_args():
    sig = inspect.signature(vhdl_Value.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_multiplyingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_MultiplyingExpression)


def test_vhdl_multiplyingexpression_constructor_exists():
    assert callable(vhdl_MultiplyingExpression.__init__)


def test_vhdl_multiplyingexpression_constructor_args():
    sig = inspect.signature(vhdl_MultiplyingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_multiplyingexpression_has_operator():
    assert hasattr(vhdl_MultiplyingExpression, "operator")
    descriptor = None
    for klass in vhdl_MultiplyingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_factor_is_not_abstract():
    assert not inspect.isabstract(vhdl_Factor)


def test_vhdl_factor_constructor_exists():
    assert callable(vhdl_Factor.__init__)


def test_vhdl_factor_constructor_args():
    sig = inspect.signature(vhdl_Factor.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_choiceexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_ChoiceExpression)


def test_vhdl_choiceexpression_constructor_exists():
    assert callable(vhdl_ChoiceExpression.__init__)


def test_vhdl_choiceexpression_constructor_args():
    sig = inspect.signature(vhdl_ChoiceExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_memberexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_MemberExpression)


def test_vhdl_memberexpression_constructor_exists():
    assert callable(vhdl_MemberExpression.__init__)


def test_vhdl_memberexpression_constructor_args():
    sig = inspect.signature(vhdl_MemberExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_ShiftExpression)


def test_vhdl_shiftexpression_constructor_exists():
    assert callable(vhdl_ShiftExpression.__init__)


def test_vhdl_shiftexpression_constructor_args():
    sig = inspect.signature(vhdl_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_shiftexpression_has_operator():
    assert hasattr(vhdl_ShiftExpression, "operator")
    descriptor = None
    for klass in vhdl_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_multiexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_MultiExpression)


def test_vhdl_multiexpression_constructor_exists():
    assert callable(vhdl_MultiExpression.__init__)


def test_vhdl_multiexpression_constructor_args():
    sig = inspect.signature(vhdl_MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_variable_is_not_abstract():
    assert not inspect.isabstract(vhdl_Variable)


def test_vhdl_variable_constructor_exists():
    assert callable(vhdl_Variable.__init__)


def test_vhdl_variable_constructor_args():
    sig = inspect.signature(vhdl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_variable_has_name():
    assert hasattr(vhdl_Variable, "name")
    descriptor = None
    for klass in vhdl_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_RelationalExpression)


def test_vhdl_relationalexpression_constructor_exists():
    assert callable(vhdl_RelationalExpression.__init__)


def test_vhdl_relationalexpression_constructor_args():
    sig = inspect.signature(vhdl_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_relationalexpression_has_operator():
    assert hasattr(vhdl_RelationalExpression, "operator")
    descriptor = None
    for klass in vhdl_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_LogicalExpression)


def test_vhdl_logicalexpression_constructor_exists():
    assert callable(vhdl_LogicalExpression.__init__)


def test_vhdl_logicalexpression_constructor_args():
    sig = inspect.signature(vhdl_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_logicalexpression_has_operator():
    assert hasattr(vhdl_LogicalExpression, "operator")
    descriptor = None
    for klass in vhdl_LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_conditionalwaveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_ConditionalWaveformExpression)


def test_vhdl_conditionalwaveformexpression_constructor_exists():
    assert callable(vhdl_ConditionalWaveformExpression.__init__)


def test_vhdl_conditionalwaveformexpression_constructor_args():
    sig = inspect.signature(vhdl_ConditionalWaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_builtinfuncs_is_not_abstract():
    assert not inspect.isabstract(vhdl_BuiltinFuncs)


def test_vhdl_builtinfuncs_constructor_exists():
    assert callable(vhdl_BuiltinFuncs.__init__)


def test_vhdl_builtinfuncs_constructor_args():
    sig = inspect.signature(vhdl_BuiltinFuncs.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_builtinfuncs_has_value():
    assert hasattr(vhdl_BuiltinFuncs, "value")
    descriptor = None
    for klass in vhdl_BuiltinFuncs.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_open_is_not_abstract():
    assert not inspect.isabstract(vhdl_Open)


def test_vhdl_open_constructor_exists():
    assert callable(vhdl_Open.__init__)


def test_vhdl_open_constructor_args():
    sig = inspect.signature(vhdl_Open.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_open_has_value():
    assert hasattr(vhdl_Open, "value")
    descriptor = None
    for klass in vhdl_Open.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_sliceexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_SliceExpression)


def test_vhdl_sliceexpression_constructor_exists():
    assert callable(vhdl_SliceExpression.__init__)


def test_vhdl_sliceexpression_constructor_args():
    sig = inspect.signature(vhdl_SliceExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_RangeExpression)


def test_vhdl_rangeexpression_constructor_exists():
    assert callable(vhdl_RangeExpression.__init__)


def test_vhdl_rangeexpression_constructor_args():
    sig = inspect.signature(vhdl_RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_vhdl_rangeexpression_has_operator():
    assert hasattr(vhdl_RangeExpression, "operator")
    descriptor = None
    for klass in vhdl_RangeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_rangeexpression_has_direction():
    assert hasattr(vhdl_RangeExpression, "direction")
    descriptor = None
    for klass in vhdl_RangeExpression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_string_is_not_abstract():
    assert not inspect.isabstract(vhdl_String)


def test_vhdl_string_constructor_exists():
    assert callable(vhdl_String.__init__)


def test_vhdl_string_constructor_args():
    sig = inspect.signature(vhdl_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_string_has_value():
    assert hasattr(vhdl_String, "value")
    descriptor = None
    for klass in vhdl_String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_ifstatementtest_is_not_abstract():
    assert not inspect.isabstract(vhdl_IfStatementTest)


def test_vhdl_ifstatementtest_constructor_exists():
    assert callable(vhdl_IfStatementTest.__init__)


def test_vhdl_ifstatementtest_constructor_args():
    sig = inspect.signature(vhdl_IfStatementTest.__init__)
    params = list(sig.parameters.keys())



def test_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(IterationScheme)


def test_iterationscheme_constructor_exists():
    assert callable(IterationScheme.__init__)


def test_iterationscheme_constructor_args():
    sig = inspect.signature(IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_foriterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_ForIterationScheme)


def test_vhdl_foriterationscheme_constructor_exists():
    assert callable(vhdl_ForIterationScheme.__init__)


def test_vhdl_foriterationscheme_constructor_args():
    sig = inspect.signature(vhdl_ForIterationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl_foriterationscheme_has_variable():
    assert hasattr(vhdl_ForIterationScheme, "variable")
    descriptor = None
    for klass in vhdl_ForIterationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_whileiterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_WhileIterationScheme)


def test_vhdl_whileiterationscheme_constructor_exists():
    assert callable(vhdl_WhileIterationScheme.__init__)


def test_vhdl_whileiterationscheme_constructor_args():
    sig = inspect.signature(vhdl_WhileIterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_IterationScheme)


def test_vhdl_iterationscheme_constructor_exists():
    assert callable(vhdl_IterationScheme.__init__)


def test_vhdl_iterationscheme_constructor_args():
    sig = inspect.signature(vhdl_IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_casealternative_is_not_abstract():
    assert not inspect.isabstract(vhdl_CaseAlternative)


def test_vhdl_casealternative_constructor_exists():
    assert callable(vhdl_CaseAlternative.__init__)


def test_vhdl_casealternative_constructor_args():
    sig = inspect.signature(vhdl_CaseAlternative.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_genericmapassociation_is_not_abstract():
    assert not inspect.isabstract(vhdl_GenericMapAssociation)


def test_vhdl_genericmapassociation_constructor_exists():
    assert callable(vhdl_GenericMapAssociation.__init__)


def test_vhdl_genericmapassociation_constructor_args():
    sig = inspect.signature(vhdl_GenericMapAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_vhdl_genericmapassociation_has_formal():
    assert hasattr(vhdl_GenericMapAssociation, "formal")
    descriptor = None
    for klass in vhdl_GenericMapAssociation.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_portmapassociation_is_not_abstract():
    assert not inspect.isabstract(vhdl_PortMapAssociation)


def test_vhdl_portmapassociation_constructor_exists():
    assert callable(vhdl_PortMapAssociation.__init__)


def test_vhdl_portmapassociation_constructor_args():
    sig = inspect.signature(vhdl_PortMapAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_vhdl_portmapassociation_has_formal():
    assert hasattr(vhdl_PortMapAssociation, "formal")
    descriptor = None
    for klass in vhdl_PortMapAssociation.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_sequentialstatement_is_not_abstract():
    assert not inspect.isabstract(SequentialStatement)


def test_sequentialstatement_constructor_exists():
    assert callable(SequentialStatement.__init__)


def test_sequentialstatement_constructor_args():
    sig = inspect.signature(SequentialStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_sequentialsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_SequentialSignalAssignmentStatement)


def test_vhdl_sequentialsignalassignmentstatement_constructor_exists():
    assert callable(vhdl_SequentialSignalAssignmentStatement.__init__)


def test_vhdl_sequentialsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_SequentialSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "guarded" in params, "Missing parameter 'guarded'"
    assert "postponed" in params, "Missing parameter 'postponed'"
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_sequentialsignalassignmentstatement_has_guarded():
    assert hasattr(vhdl_SequentialSignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl_SequentialSignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_sequentialsignalassignmentstatement_has_postponed():
    assert hasattr(vhdl_SequentialSignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl_SequentialSignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_sequentialsignalassignmentstatement_has_label():
    assert hasattr(vhdl_SequentialSignalAssignmentStatement, "label")
    descriptor = None
    for klass in vhdl_SequentialSignalAssignmentStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_casestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_CaseStatement)


def test_vhdl_casestatement_constructor_exists():
    assert callable(vhdl_CaseStatement.__init__)


def test_vhdl_casestatement_constructor_args():
    sig = inspect.signature(vhdl_CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_casestatement_has_label():
    assert hasattr(vhdl_CaseStatement, "label")
    descriptor = None
    for klass in vhdl_CaseStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_IfStatement)


def test_vhdl_ifstatement_constructor_exists():
    assert callable(vhdl_IfStatement.__init__)


def test_vhdl_ifstatement_constructor_args():
    sig = inspect.signature(vhdl_IfStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_ifstatement_has_label():
    assert hasattr(vhdl_IfStatement, "label")
    descriptor = None
    for klass in vhdl_IfStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_loopstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_LoopStatement)


def test_vhdl_loopstatement_constructor_exists():
    assert callable(vhdl_LoopStatement.__init__)


def test_vhdl_loopstatement_constructor_args():
    sig = inspect.signature(vhdl_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_waitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_WaitStatement)


def test_vhdl_waitstatement_constructor_exists():
    assert callable(vhdl_WaitStatement.__init__)


def test_vhdl_waitstatement_constructor_args():
    sig = inspect.signature(vhdl_WaitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_waitstatement_has_label():
    assert hasattr(vhdl_WaitStatement, "label")
    descriptor = None
    for klass in vhdl_WaitStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_portmap_is_not_abstract():
    assert not inspect.isabstract(vhdl_PortMap)


def test_vhdl_portmap_constructor_exists():
    assert callable(vhdl_PortMap.__init__)


def test_vhdl_portmap_constructor_args():
    sig = inspect.signature(vhdl_PortMap.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_genericmap_is_not_abstract():
    assert not inspect.isabstract(vhdl_GenericMap)


def test_vhdl_genericmap_constructor_exists():
    assert callable(vhdl_GenericMap.__init__)


def test_vhdl_genericmap_constructor_args():
    sig = inspect.signature(vhdl_GenericMap.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_sequentialstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_SequentialStatement)


def test_vhdl_sequentialstatement_constructor_exists():
    assert callable(vhdl_SequentialStatement.__init__)


def test_vhdl_sequentialstatement_constructor_args():
    sig = inspect.signature(vhdl_SequentialStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_idlist_is_not_abstract():
    assert not inspect.isabstract(vhdl_IdList)


def test_vhdl_idlist_constructor_exists():
    assert callable(vhdl_IdList.__init__)


def test_vhdl_idlist_constructor_args():
    sig = inspect.signature(vhdl_IdList.__init__)
    params = list(sig.parameters.keys())



def test_architecturestatement_is_not_abstract():
    assert not inspect.isabstract(ArchitectureStatement)


def test_architecturestatement_constructor_exists():
    assert callable(ArchitectureStatement.__init__)


def test_architecturestatement_constructor_args():
    sig = inspect.signature(ArchitectureStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_forgeneratestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_ForGenerateStatement)


def test_vhdl_forgeneratestatement_constructor_exists():
    assert callable(vhdl_ForGenerateStatement.__init__)


def test_vhdl_forgeneratestatement_constructor_args():
    sig = inspect.signature(vhdl_ForGenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_componentinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_ComponentInstantiationStatement)


def test_vhdl_componentinstantiationstatement_constructor_exists():
    assert callable(vhdl_ComponentInstantiationStatement.__init__)


def test_vhdl_componentinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_ComponentInstantiationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_componentinstantiationstatement_has_name():
    assert hasattr(vhdl_ComponentInstantiationStatement, "name")
    descriptor = None
    for klass in vhdl_ComponentInstantiationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_ConditionalSignalAssignmentStatement)


def test_vhdl_conditionalsignalassignmentstatement_constructor_exists():
    assert callable(vhdl_ConditionalSignalAssignmentStatement.__init__)


def test_vhdl_conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "guarded" in params, "Missing parameter 'guarded'"
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl_conditionalsignalassignmentstatement_has_guarded():
    assert hasattr(vhdl_ConditionalSignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl_ConditionalSignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_conditionalsignalassignmentstatement_has_postponed():
    assert hasattr(vhdl_ConditionalSignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl_ConditionalSignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_entityinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_EntityInstantiationStatement)


def test_vhdl_entityinstantiationstatement_constructor_exists():
    assert callable(vhdl_EntityInstantiationStatement.__init__)


def test_vhdl_entityinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_EntityInstantiationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_entityinstantiationstatement_has_name():
    assert hasattr(vhdl_EntityInstantiationStatement, "name")
    descriptor = None
    for klass in vhdl_EntityInstantiationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_ifgeneratestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_IfGenerateStatement)


def test_vhdl_ifgeneratestatement_constructor_exists():
    assert callable(vhdl_IfGenerateStatement.__init__)


def test_vhdl_ifgeneratestatement_constructor_args():
    sig = inspect.signature(vhdl_IfGenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_processstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_ProcessStatement)


def test_vhdl_processstatement_constructor_exists():
    assert callable(vhdl_ProcessStatement.__init__)


def test_vhdl_processstatement_constructor_args():
    sig = inspect.signature(vhdl_ProcessStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl_processstatement_has_postponed():
    assert hasattr(vhdl_ProcessStatement, "postponed")
    descriptor = None
    for klass in vhdl_ProcessStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_subtypeindication_is_not_abstract():
    assert not inspect.isabstract(vhdl_SubtypeIndication)


def test_vhdl_subtypeindication_constructor_exists():
    assert callable(vhdl_SubtypeIndication.__init__)


def test_vhdl_subtypeindication_constructor_args():
    sig = inspect.signature(vhdl_SubtypeIndication.__init__)
    params = list(sig.parameters.keys())
    assert "builtin_type" in params, "Missing parameter 'builtin_type'"

def test_vhdl_subtypeindication_has_builtin_type():
    assert hasattr(vhdl_SubtypeIndication, "builtin_type")
    descriptor = None
    for klass in vhdl_SubtypeIndication.__mro__:
        if "builtin_type" in klass.__dict__:
            descriptor = klass.__dict__["builtin_type"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_loopvariable_is_not_abstract():
    assert not inspect.isabstract(vhdl_LoopVariable)


def test_vhdl_loopvariable_constructor_exists():
    assert callable(vhdl_LoopVariable.__init__)


def test_vhdl_loopvariable_constructor_args():
    sig = inspect.signature(vhdl_LoopVariable.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_constant_is_not_abstract():
    assert not inspect.isabstract(vhdl_Constant)


def test_vhdl_constant_constructor_exists():
    assert callable(vhdl_Constant.__init__)


def test_vhdl_constant_constructor_args():
    sig = inspect.signature(vhdl_Constant.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_port_is_not_abstract():
    assert not inspect.isabstract(vhdl_Port)


def test_vhdl_port_constructor_exists():
    assert callable(vhdl_Port.__init__)


def test_vhdl_port_constructor_args():
    sig = inspect.signature(vhdl_Port.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_vhdl_port_has_kind():
    assert hasattr(vhdl_Port, "kind")
    descriptor = None
    for klass in vhdl_Port.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_port_has_mode():
    assert hasattr(vhdl_Port, "mode")
    descriptor = None
    for klass in vhdl_Port.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_ports_is_not_abstract():
    assert not inspect.isabstract(vhdl_Ports)


def test_vhdl_ports_constructor_exists():
    assert callable(vhdl_Ports.__init__)


def test_vhdl_ports_constructor_args():
    sig = inspect.signature(vhdl_Ports.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_generics_is_not_abstract():
    assert not inspect.isabstract(vhdl_Generics)


def test_vhdl_generics_constructor_exists():
    assert callable(vhdl_Generics.__init__)


def test_vhdl_generics_constructor_args():
    sig = inspect.signature(vhdl_Generics.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_var_is_not_abstract():
    assert not inspect.isabstract(vhdl_Var)


def test_vhdl_var_constructor_exists():
    assert callable(vhdl_Var.__init__)


def test_vhdl_var_constructor_args():
    sig = inspect.signature(vhdl_Var.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_signal_is_not_abstract():
    assert not inspect.isabstract(vhdl_Signal)


def test_vhdl_signal_constructor_exists():
    assert callable(vhdl_Signal.__init__)


def test_vhdl_signal_constructor_args():
    sig = inspect.signature(vhdl_Signal.__init__)
    params = list(sig.parameters.keys())



def test_package_declarative_item_is_not_abstract():
    assert not inspect.isabstract(package_declarative_item)


def test_package_declarative_item_constructor_exists():
    assert callable(package_declarative_item.__init__)


def test_package_declarative_item_constructor_args():
    sig = inspect.signature(package_declarative_item.__init__)
    params = list(sig.parameters.keys())



def test_blockdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(BlockDeclarativeItem)


def test_blockdeclarativeitem_constructor_exists():
    assert callable(BlockDeclarativeItem.__init__)


def test_blockdeclarativeitem_constructor_args():
    sig = inspect.signature(BlockDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_VariableDeclaration)


def test_vhdl_variabledeclaration_constructor_exists():
    assert callable(vhdl_VariableDeclaration.__init__)


def test_vhdl_variabledeclaration_constructor_args():
    sig = inspect.signature(vhdl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "shared" in params, "Missing parameter 'shared'"

def test_vhdl_variabledeclaration_has_shared():
    assert hasattr(vhdl_VariableDeclaration, "shared")
    descriptor = None
    for klass in vhdl_VariableDeclaration.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_type_is_not_abstract():
    assert not inspect.isabstract(vhdl_Type)


def test_vhdl_type_constructor_exists():
    assert callable(vhdl_Type.__init__)


def test_vhdl_type_constructor_args():
    sig = inspect.signature(vhdl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_type_has_value():
    assert hasattr(vhdl_Type, "value")
    descriptor = None
    for klass in vhdl_Type.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_type_has_name():
    assert hasattr(vhdl_Type, "name")
    descriptor = None
    for klass in vhdl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_ConstantDeclaration)


def test_vhdl_constantdeclaration_constructor_exists():
    assert callable(vhdl_ConstantDeclaration.__init__)


def test_vhdl_constantdeclaration_constructor_args():
    sig = inspect.signature(vhdl_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_SignalDeclaration)


def test_vhdl_signaldeclaration_constructor_exists():
    assert callable(vhdl_SignalDeclaration.__init__)


def test_vhdl_signaldeclaration_constructor_args():
    sig = inspect.signature(vhdl_SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_vhdl_signaldeclaration_has_kind():
    assert hasattr(vhdl_SignalDeclaration, "kind")
    descriptor = None
    for klass in vhdl_SignalDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_component_is_not_abstract():
    assert not inspect.isabstract(vhdl_Component)


def test_vhdl_component_constructor_exists():
    assert callable(vhdl_Component.__init__)


def test_vhdl_component_constructor_args():
    sig = inspect.signature(vhdl_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_component_has_name():
    assert hasattr(vhdl_Component, "name")
    descriptor = None
    for klass in vhdl_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_attributedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_AttributeDeclaration)


def test_vhdl_attributedeclaration_constructor_exists():
    assert callable(vhdl_AttributeDeclaration.__init__)


def test_vhdl_attributedeclaration_constructor_args():
    sig = inspect.signature(vhdl_AttributeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type_keyword" in params, "Missing parameter 'type_keyword'"
    assert "type_id" in params, "Missing parameter 'type_id'"

def test_vhdl_attributedeclaration_has_name():
    assert hasattr(vhdl_AttributeDeclaration, "name")
    descriptor = None
    for klass in vhdl_AttributeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_attributedeclaration_has_type_keyword():
    assert hasattr(vhdl_AttributeDeclaration, "type_keyword")
    descriptor = None
    for klass in vhdl_AttributeDeclaration.__mro__:
        if "type_keyword" in klass.__dict__:
            descriptor = klass.__dict__["type_keyword"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_attributedeclaration_has_type_id():
    assert hasattr(vhdl_AttributeDeclaration, "type_id")
    descriptor = None
    for klass in vhdl_AttributeDeclaration.__mro__:
        if "type_id" in klass.__dict__:
            descriptor = klass.__dict__["type_id"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_attributespecification_is_not_abstract():
    assert not inspect.isabstract(vhdl_AttributeSpecification)


def test_vhdl_attributespecification_constructor_exists():
    assert callable(vhdl_AttributeSpecification.__init__)


def test_vhdl_attributespecification_constructor_args():
    sig = inspect.signature(vhdl_AttributeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "entity" in params, "Missing parameter 'entity'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_vhdl_attributespecification_has_name():
    assert hasattr(vhdl_AttributeSpecification, "name")
    descriptor = None
    for klass in vhdl_AttributeSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_attributespecification_has_entity():
    assert hasattr(vhdl_AttributeSpecification, "entity")
    descriptor = None
    for klass in vhdl_AttributeSpecification.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_attributespecification_has_class_():
    assert hasattr(vhdl_AttributeSpecification, "class_")
    descriptor = None
    for klass in vhdl_AttributeSpecification.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_alias_is_not_abstract():
    assert not inspect.isabstract(vhdl_Alias)


def test_vhdl_alias_constructor_exists():
    assert callable(vhdl_Alias.__init__)


def test_vhdl_alias_constructor_args():
    sig = inspect.signature(vhdl_Alias.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_generic_is_not_abstract():
    assert not inspect.isabstract(vhdl_Generic)


def test_vhdl_generic_constructor_exists():
    assert callable(vhdl_Generic.__init__)


def test_vhdl_generic_constructor_args():
    sig = inspect.signature(vhdl_Generic.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_is_not_abstract():
    assert not inspect.isabstract(vhdl_Expression)


def test_vhdl_expression_constructor_exists():
    assert callable(vhdl_Expression.__init__)


def test_vhdl_expression_constructor_args():
    sig = inspect.signature(vhdl_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_vhdl_expression_has_unary_operator():
    assert hasattr(vhdl_Expression, "unary_operator")
    descriptor = None
    for klass in vhdl_Expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_expression_has_attribute():
    assert hasattr(vhdl_Expression, "attribute")
    descriptor = None
    for klass in vhdl_Expression.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_designfile_is_not_abstract():
    assert not inspect.isabstract(vhdl_DesignFile)


def test_vhdl_designfile_constructor_exists():
    assert callable(vhdl_DesignFile.__init__)


def test_vhdl_designfile_constructor_args():
    sig = inspect.signature(vhdl_DesignFile.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_architecturestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_ArchitectureStatement)


def test_vhdl_architecturestatement_constructor_exists():
    assert callable(vhdl_ArchitectureStatement.__init__)


def test_vhdl_architecturestatement_constructor_args():
    sig = inspect.signature(vhdl_ArchitectureStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_architecturestatement_has_label():
    assert hasattr(vhdl_ArchitectureStatement, "label")
    descriptor = None
    for klass in vhdl_ArchitectureStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_blockdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(vhdl_BlockDeclarativeItem)


def test_vhdl_blockdeclarativeitem_constructor_exists():
    assert callable(vhdl_BlockDeclarativeItem.__init__)


def test_vhdl_blockdeclarativeitem_constructor_args():
    sig = inspect.signature(vhdl_BlockDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_package_declarative_part_is_not_abstract():
    assert not inspect.isabstract(vhdl_package_declarative_part)


def test_vhdl_package_declarative_part_constructor_exists():
    assert callable(vhdl_package_declarative_part.__init__)


def test_vhdl_package_declarative_part_constructor_args():
    sig = inspect.signature(vhdl_package_declarative_part.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_package_declarative_item_is_not_abstract():
    assert not inspect.isabstract(vhdl_package_declarative_item)


def test_vhdl_package_declarative_item_constructor_exists():
    assert callable(vhdl_package_declarative_item.__init__)


def test_vhdl_package_declarative_item_constructor_args():
    sig = inspect.signature(vhdl_package_declarative_item.__init__)
    params = list(sig.parameters.keys())



def test_libraryunit_is_not_abstract():
    assert not inspect.isabstract(LibraryUnit)


def test_libraryunit_constructor_exists():
    assert callable(LibraryUnit.__init__)


def test_libraryunit_constructor_args():
    sig = inspect.signature(LibraryUnit.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_architecture_is_not_abstract():
    assert not inspect.isabstract(vhdl_Architecture)


def test_vhdl_architecture_constructor_exists():
    assert callable(vhdl_Architecture.__init__)


def test_vhdl_architecture_constructor_args():
    sig = inspect.signature(vhdl_Architecture.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_entity_is_not_abstract():
    assert not inspect.isabstract(vhdl_Entity)


def test_vhdl_entity_constructor_exists():
    assert callable(vhdl_Entity.__init__)


def test_vhdl_entity_constructor_args():
    sig = inspect.signature(vhdl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_package_is_not_abstract():
    assert not inspect.isabstract(vhdl_Package)


def test_vhdl_package_constructor_exists():
    assert callable(vhdl_Package.__init__)


def test_vhdl_package_constructor_args():
    sig = inspect.signature(vhdl_Package.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_library_is_not_abstract():
    assert not inspect.isabstract(vhdl_Library)


def test_vhdl_library_constructor_exists():
    assert callable(vhdl_Library.__init__)


def test_vhdl_library_constructor_args():
    sig = inspect.signature(vhdl_Library.__init__)
    params = list(sig.parameters.keys())
    assert "builtin_lib" in params, "Missing parameter 'builtin_lib'"

def test_vhdl_library_has_builtin_lib():
    assert hasattr(vhdl_Library, "builtin_lib")
    descriptor = None
    for klass in vhdl_Library.__mro__:
        if "builtin_lib" in klass.__dict__:
            descriptor = klass.__dict__["builtin_lib"]
            break
    assert isinstance(descriptor, property)



def test_contextitem_is_not_abstract():
    assert not inspect.isabstract(ContextItem)


def test_contextitem_constructor_exists():
    assert callable(ContextItem.__init__)


def test_contextitem_constructor_args():
    sig = inspect.signature(ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_libraryclause_is_not_abstract():
    assert not inspect.isabstract(vhdl_LibraryClause)


def test_vhdl_libraryclause_constructor_exists():
    assert callable(vhdl_LibraryClause.__init__)


def test_vhdl_libraryclause_constructor_args():
    sig = inspect.signature(vhdl_LibraryClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_libraryclause_has_name():
    assert hasattr(vhdl_LibraryClause, "name")
    descriptor = None
    for klass in vhdl_LibraryClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_useclause_is_not_abstract():
    assert not inspect.isabstract(vhdl_UseClause)


def test_vhdl_useclause_constructor_exists():
    assert callable(vhdl_UseClause.__init__)


def test_vhdl_useclause_constructor_args():
    sig = inspect.signature(vhdl_UseClause.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_vhdl_useclause_has_importedNamespace():
    assert hasattr(vhdl_UseClause, "importedNamespace")
    descriptor = None
    for klass in vhdl_UseClause.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_libraryunit_is_not_abstract():
    assert not inspect.isabstract(vhdl_LibraryUnit)


def test_vhdl_libraryunit_constructor_exists():
    assert callable(vhdl_LibraryUnit.__init__)


def test_vhdl_libraryunit_constructor_args():
    sig = inspect.signature(vhdl_LibraryUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_libraryunit_has_name():
    assert hasattr(vhdl_LibraryUnit, "name")
    descriptor = None
    for klass in vhdl_LibraryUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_contextitem_is_not_abstract():
    assert not inspect.isabstract(vhdl_ContextItem)


def test_vhdl_contextitem_constructor_exists():
    assert callable(vhdl_ContextItem.__init__)


def test_vhdl_contextitem_constructor_args():
    sig = inspect.signature(vhdl_ContextItem.__init__)
    params = list(sig.parameters.keys())

def test_addingoperator_exists():
    # Check that the Enumeration exists
    assert AddingOperator is not None

def test_addingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddingOperator]
    expected_literals = [
        "MINUS",
        "AMPERSAND",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddingOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "ABS",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "ROR",
        "ROL",
        "SLL",
        "SRA",
        "SLA",
        "SRL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_builtinlibs_exists():
    # Check that the Enumeration exists
    assert BuiltinLibs is not None

def test_builtinlibs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltinLibs]
    expected_literals = [
        "WORK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltinLibs"

def test_estring_exists():
    # Check that the Enumeration exists
    assert EString is not None

def test_estring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EString]
    expected_literals = [
        "STRING",
        "RISING_EDGE",
        "STD_LOGIC",
        "NATURAL",
        "TO_UNSIGNED",
        "FALLING_EDGE",
        "INTEGER",
        "STD_LOGIC_VECTOR",
        "UNSIGNED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EString"

def test_rangedirection_exists():
    # Check that the Enumeration exists
    assert RangeDirection is not None

def test_rangedirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeDirection]
    expected_literals = [
        "DOWNTO",
        "TO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeDirection"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "NAND",
        "OR",
        "XNOR",
        "NOR",
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_signalkind_exists():
    # Check that the Enumeration exists
    assert SignalKind is not None

def test_signalkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalKind]
    expected_literals = [
        "BUS",
        "REGISTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalKind"

def test_entityclass_exists():
    # Check that the Enumeration exists
    assert EntityClass is not None

def test_entityclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityClass]
    expected_literals = [
        "ARCHITECTURE",
        "COMPONENT",
        "CONFIGURATION",
        "PROCEDURE",
        "UNITS",
        "NATURE",
        "SUBNATURE",
        "QUANTITY",
        "SIGNAL",
        "ENTITY",
        "FILE",
        "CONSTANT",
        "TYPE",
        "TERMINAL",
        "SUBTYPE",
        "LABEL",
        "FUNCTION",
        "VARIABLE",
        "LITERAL",
        "PACKAGE",
        "GROUP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityClass"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "NEQ",
        "ASSOCIATE",
        "GE",
        "LOWERTHAN",
        "EQ",
        "GREATERTHAN",
        "LE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_sign_exists():
    # Check that the Enumeration exists
    assert Sign is not None

def test_sign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sign]
    expected_literals = [
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sign"

def test_purity_exists():
    # Check that the Enumeration exists
    assert Purity is not None

def test_purity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Purity]
    expected_literals = [
        "IMPURE",
        "PURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Purity"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "INOUT",
        "OUT",
        "IN",
        "BUFFER",
        "LINKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_multiplyingoperator_exists():
    # Check that the Enumeration exists
    assert MultiplyingOperator is not None

def test_multiplyingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplyingOperator]
    expected_literals = [
        "MUL",
        "DIV",
        "REM",
        "MOD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplyingOperator"


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
ValueExpression_strategy = st.builds(
    ValueExpression,
)
vhdl_UnitValueExpression_strategy = st.builds(
    vhdl_UnitValueExpression,
    unit=
        safe_text
)
vhdl_ValueExpression_strategy = st.builds(
    vhdl_ValueExpression,
    value=
        safe_text
)
ArrayTypeDefinition_strategy = st.builds(
    ArrayTypeDefinition,
)
vhdl_ConstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl_ConstrainedArrayTypeDefinition,
)
vhdl_UnconstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl_UnconstrainedArrayTypeDefinition,
    index=
        safe_text
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
vhdl_ArrayTypeDefinition_strategy = st.builds(
    vhdl_ArrayTypeDefinition,
)
vhdl_RecordTypeDefinition_strategy = st.builds(
    vhdl_RecordTypeDefinition,
)
vhdl_RecordField_strategy = st.builds(
    vhdl_RecordField,
    name=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
vhdl_FileTypeDefinition_strategy = st.builds(
    vhdl_FileTypeDefinition,
    type=
        safe_text
)
vhdl_EnumerationTypeDefinition_strategy = st.builds(
    vhdl_EnumerationTypeDefinition,
    literal=
        safe_text
)
vhdl_CompositeTypeDefinition_strategy = st.builds(
    vhdl_CompositeTypeDefinition,
)
vhdl_AccessTypeDefinition_strategy = st.builds(
    vhdl_AccessTypeDefinition,
)
vhdl_TypeDefinition_strategy = st.builds(
    vhdl_TypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
vhdl_TypeDeclaration_strategy = st.builds(
    vhdl_TypeDeclaration,
)
vhdl_SubtypeDeclaration_strategy = st.builds(
    vhdl_SubtypeDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
vhdl_AddingExpression_strategy = st.builds(
    vhdl_AddingExpression,
    operator=
        safe_text
)
vhdl_BitString_strategy = st.builds(
    vhdl_BitString,
    value=
        safe_text
)
vhdl_Member_strategy = st.builds(
    vhdl_Member,
)
vhdl_Boolean_strategy = st.builds(
    vhdl_Boolean,
    value=
        safe_text
)
vhdl_Others_strategy = st.builds(
    vhdl_Others,
    value=
        safe_text
)
vhdl_Char_strategy = st.builds(
    vhdl_Char,
    value=
        safe_text
)
vhdl_Value_strategy = st.builds(
    vhdl_Value,
)
vhdl_MultiplyingExpression_strategy = st.builds(
    vhdl_MultiplyingExpression,
    operator=
        safe_text
)
vhdl_Factor_strategy = st.builds(
    vhdl_Factor,
)
vhdl_ChoiceExpression_strategy = st.builds(
    vhdl_ChoiceExpression,
)
vhdl_MemberExpression_strategy = st.builds(
    vhdl_MemberExpression,
)
vhdl_ShiftExpression_strategy = st.builds(
    vhdl_ShiftExpression,
    operator=
        safe_text
)
vhdl_MultiExpression_strategy = st.builds(
    vhdl_MultiExpression,
)
vhdl_Variable_strategy = st.builds(
    vhdl_Variable,
    name=
        safe_text
)
vhdl_RelationalExpression_strategy = st.builds(
    vhdl_RelationalExpression,
    operator=
        safe_text
)
vhdl_LogicalExpression_strategy = st.builds(
    vhdl_LogicalExpression,
    operator=
        safe_text
)
vhdl_ConditionalWaveformExpression_strategy = st.builds(
    vhdl_ConditionalWaveformExpression,
)
vhdl_BuiltinFuncs_strategy = st.builds(
    vhdl_BuiltinFuncs,
    value=
        safe_text
)
vhdl_Open_strategy = st.builds(
    vhdl_Open,
    value=
        safe_text
)
vhdl_SliceExpression_strategy = st.builds(
    vhdl_SliceExpression,
)
vhdl_RangeExpression_strategy = st.builds(
    vhdl_RangeExpression,
    operator=
        safe_text,
    direction=
        safe_text
)
vhdl_String_strategy = st.builds(
    vhdl_String,
    value=
        safe_text
)
vhdl_IfStatementTest_strategy = st.builds(
    vhdl_IfStatementTest,
)
IterationScheme_strategy = st.builds(
    IterationScheme,
)
vhdl_ForIterationScheme_strategy = st.builds(
    vhdl_ForIterationScheme,
    variable=
        safe_text
)
vhdl_WhileIterationScheme_strategy = st.builds(
    vhdl_WhileIterationScheme,
)
vhdl_IterationScheme_strategy = st.builds(
    vhdl_IterationScheme,
)
vhdl_CaseAlternative_strategy = st.builds(
    vhdl_CaseAlternative,
)
vhdl_GenericMapAssociation_strategy = st.builds(
    vhdl_GenericMapAssociation,
    formal=
        safe_text
)
vhdl_PortMapAssociation_strategy = st.builds(
    vhdl_PortMapAssociation,
    formal=
        safe_text
)
SequentialStatement_strategy = st.builds(
    SequentialStatement,
)
vhdl_SequentialSignalAssignmentStatement_strategy = st.builds(
    vhdl_SequentialSignalAssignmentStatement,
    guarded=
        st.booleans(),
    postponed=
        st.booleans(),
    label=
        safe_text
)
vhdl_CaseStatement_strategy = st.builds(
    vhdl_CaseStatement,
    label=
        safe_text
)
vhdl_IfStatement_strategy = st.builds(
    vhdl_IfStatement,
    label=
        safe_text
)
vhdl_LoopStatement_strategy = st.builds(
    vhdl_LoopStatement,
)
vhdl_WaitStatement_strategy = st.builds(
    vhdl_WaitStatement,
    label=
        safe_text
)
vhdl_PortMap_strategy = st.builds(
    vhdl_PortMap,
)
vhdl_GenericMap_strategy = st.builds(
    vhdl_GenericMap,
)
vhdl_SequentialStatement_strategy = st.builds(
    vhdl_SequentialStatement,
)
vhdl_IdList_strategy = st.builds(
    vhdl_IdList,
)
ArchitectureStatement_strategy = st.builds(
    ArchitectureStatement,
)
vhdl_ForGenerateStatement_strategy = st.builds(
    vhdl_ForGenerateStatement,
)
vhdl_ComponentInstantiationStatement_strategy = st.builds(
    vhdl_ComponentInstantiationStatement,
    name=
        safe_text
)
vhdl_ConditionalSignalAssignmentStatement_strategy = st.builds(
    vhdl_ConditionalSignalAssignmentStatement,
    guarded=
        st.booleans(),
    postponed=
        st.booleans()
)
vhdl_EntityInstantiationStatement_strategy = st.builds(
    vhdl_EntityInstantiationStatement,
    name=
        safe_text
)
vhdl_IfGenerateStatement_strategy = st.builds(
    vhdl_IfGenerateStatement,
)
vhdl_ProcessStatement_strategy = st.builds(
    vhdl_ProcessStatement,
    postponed=
        st.booleans()
)
vhdl_SubtypeIndication_strategy = st.builds(
    vhdl_SubtypeIndication,
    builtin_type=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
vhdl_LoopVariable_strategy = st.builds(
    vhdl_LoopVariable,
)
vhdl_Constant_strategy = st.builds(
    vhdl_Constant,
)
vhdl_Port_strategy = st.builds(
    vhdl_Port,
    kind=
        safe_text,
    mode=
        safe_text
)
vhdl_Ports_strategy = st.builds(
    vhdl_Ports,
)
vhdl_Generics_strategy = st.builds(
    vhdl_Generics,
)
vhdl_Var_strategy = st.builds(
    vhdl_Var,
)
vhdl_Signal_strategy = st.builds(
    vhdl_Signal,
)
package_declarative_item_strategy = st.builds(
    package_declarative_item,
)
BlockDeclarativeItem_strategy = st.builds(
    BlockDeclarativeItem,
)
vhdl_VariableDeclaration_strategy = st.builds(
    vhdl_VariableDeclaration,
    shared=
        st.booleans()
)
vhdl_Type_strategy = st.builds(
    vhdl_Type,
    value=
        safe_text,
    name=
        safe_text
)
vhdl_ConstantDeclaration_strategy = st.builds(
    vhdl_ConstantDeclaration,
)
vhdl_SignalDeclaration_strategy = st.builds(
    vhdl_SignalDeclaration,
    kind=
        safe_text
)
vhdl_Component_strategy = st.builds(
    vhdl_Component,
    name=
        safe_text
)
vhdl_AttributeDeclaration_strategy = st.builds(
    vhdl_AttributeDeclaration,
    name=
        safe_text,
    type_keyword=
        safe_text,
    type_id=
        safe_text
)
vhdl_AttributeSpecification_strategy = st.builds(
    vhdl_AttributeSpecification,
    name=
        safe_text,
    entity=
        safe_text,
    class_=
        safe_text
)
vhdl_Alias_strategy = st.builds(
    vhdl_Alias,
)
vhdl_Generic_strategy = st.builds(
    vhdl_Generic,
)
vhdl_Expression_strategy = st.builds(
    vhdl_Expression,
    unary_operator=
        safe_text,
    attribute=
        safe_text
)
vhdl_DesignFile_strategy = st.builds(
    vhdl_DesignFile,
)
vhdl_ArchitectureStatement_strategy = st.builds(
    vhdl_ArchitectureStatement,
    label=
        safe_text
)
vhdl_BlockDeclarativeItem_strategy = st.builds(
    vhdl_BlockDeclarativeItem,
)
vhdl_package_declarative_part_strategy = st.builds(
    vhdl_package_declarative_part,
)
vhdl_package_declarative_item_strategy = st.builds(
    vhdl_package_declarative_item,
)
LibraryUnit_strategy = st.builds(
    LibraryUnit,
)
vhdl_Architecture_strategy = st.builds(
    vhdl_Architecture,
)
vhdl_Entity_strategy = st.builds(
    vhdl_Entity,
)
vhdl_Package_strategy = st.builds(
    vhdl_Package,
)
vhdl_Library_strategy = st.builds(
    vhdl_Library,
    builtin_lib=
        safe_text
)
ContextItem_strategy = st.builds(
    ContextItem,
)
vhdl_LibraryClause_strategy = st.builds(
    vhdl_LibraryClause,
    name=
        safe_text
)
vhdl_UseClause_strategy = st.builds(
    vhdl_UseClause,
    importedNamespace=
        safe_text
)
vhdl_LibraryUnit_strategy = st.builds(
    vhdl_LibraryUnit,
    name=
        safe_text
)
vhdl_ContextItem_strategy = st.builds(
    vhdl_ContextItem,
)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=vhdl_UnitValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl_unitvalueexpression_instantiation(instance):
    assert isinstance(instance, vhdl_UnitValueExpression)



@given(instance=vhdl_UnitValueExpression_strategy)
def test_vhdl_unitvalueexpression_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=vhdl_ValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl_valueexpression_instantiation(instance):
    assert isinstance(instance, vhdl_ValueExpression)



@given(instance=vhdl_ValueExpression_strategy)
def test_vhdl_valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, ArrayTypeDefinition)

@given(instance=vhdl_ConstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_constrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_ConstrainedArrayTypeDefinition)

@given(instance=vhdl_UnconstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_unconstrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_UnconstrainedArrayTypeDefinition)



@given(instance=vhdl_UnconstrainedArrayTypeDefinition_strategy)
def test_vhdl_unconstrainedarraytypedefinition_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=vhdl_ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_ArrayTypeDefinition)

@given(instance=vhdl_RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_recordtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_RecordTypeDefinition)

@given(instance=vhdl_RecordField_strategy)
@settings(max_examples=50)
def test_vhdl_recordfield_instantiation(instance):
    assert isinstance(instance, vhdl_RecordField)



@given(instance=vhdl_RecordField_strategy)
def test_vhdl_recordfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=vhdl_FileTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_filetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_FileTypeDefinition)



@given(instance=vhdl_FileTypeDefinition_strategy)
def test_vhdl_filetypedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vhdl_EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_EnumerationTypeDefinition)



@given(instance=vhdl_EnumerationTypeDefinition_strategy)
def test_vhdl_enumerationtypedefinition_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=vhdl_CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_CompositeTypeDefinition)

@given(instance=vhdl_AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_accesstypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_AccessTypeDefinition)

@given(instance=vhdl_TypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_typedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_TypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=vhdl_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_typedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_TypeDeclaration)

@given(instance=vhdl_SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_subtypedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_SubtypeDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vhdl_AddingExpression_strategy)
@settings(max_examples=50)
def test_vhdl_addingexpression_instantiation(instance):
    assert isinstance(instance, vhdl_AddingExpression)



@given(instance=vhdl_AddingExpression_strategy)
def test_vhdl_addingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_BitString_strategy)
@settings(max_examples=50)
def test_vhdl_bitstring_instantiation(instance):
    assert isinstance(instance, vhdl_BitString)



@given(instance=vhdl_BitString_strategy)
def test_vhdl_bitstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_Member_strategy)
@settings(max_examples=50)
def test_vhdl_member_instantiation(instance):
    assert isinstance(instance, vhdl_Member)

@given(instance=vhdl_Boolean_strategy)
@settings(max_examples=50)
def test_vhdl_boolean_instantiation(instance):
    assert isinstance(instance, vhdl_Boolean)



@given(instance=vhdl_Boolean_strategy)
def test_vhdl_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_Others_strategy)
@settings(max_examples=50)
def test_vhdl_others_instantiation(instance):
    assert isinstance(instance, vhdl_Others)



@given(instance=vhdl_Others_strategy)
def test_vhdl_others_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_Char_strategy)
@settings(max_examples=50)
def test_vhdl_char_instantiation(instance):
    assert isinstance(instance, vhdl_Char)



@given(instance=vhdl_Char_strategy)
def test_vhdl_char_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_Value_strategy)
@settings(max_examples=50)
def test_vhdl_value_instantiation(instance):
    assert isinstance(instance, vhdl_Value)

@given(instance=vhdl_MultiplyingExpression_strategy)
@settings(max_examples=50)
def test_vhdl_multiplyingexpression_instantiation(instance):
    assert isinstance(instance, vhdl_MultiplyingExpression)



@given(instance=vhdl_MultiplyingExpression_strategy)
def test_vhdl_multiplyingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_Factor_strategy)
@settings(max_examples=50)
def test_vhdl_factor_instantiation(instance):
    assert isinstance(instance, vhdl_Factor)

@given(instance=vhdl_ChoiceExpression_strategy)
@settings(max_examples=50)
def test_vhdl_choiceexpression_instantiation(instance):
    assert isinstance(instance, vhdl_ChoiceExpression)

@given(instance=vhdl_MemberExpression_strategy)
@settings(max_examples=50)
def test_vhdl_memberexpression_instantiation(instance):
    assert isinstance(instance, vhdl_MemberExpression)

@given(instance=vhdl_ShiftExpression_strategy)
@settings(max_examples=50)
def test_vhdl_shiftexpression_instantiation(instance):
    assert isinstance(instance, vhdl_ShiftExpression)



@given(instance=vhdl_ShiftExpression_strategy)
def test_vhdl_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_MultiExpression_strategy)
@settings(max_examples=50)
def test_vhdl_multiexpression_instantiation(instance):
    assert isinstance(instance, vhdl_MultiExpression)

@given(instance=vhdl_Variable_strategy)
@settings(max_examples=50)
def test_vhdl_variable_instantiation(instance):
    assert isinstance(instance, vhdl_Variable)



@given(instance=vhdl_Variable_strategy)
def test_vhdl_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_RelationalExpression_strategy)
@settings(max_examples=50)
def test_vhdl_relationalexpression_instantiation(instance):
    assert isinstance(instance, vhdl_RelationalExpression)



@given(instance=vhdl_RelationalExpression_strategy)
def test_vhdl_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_LogicalExpression_strategy)
@settings(max_examples=50)
def test_vhdl_logicalexpression_instantiation(instance):
    assert isinstance(instance, vhdl_LogicalExpression)



@given(instance=vhdl_LogicalExpression_strategy)
def test_vhdl_logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_ConditionalWaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl_conditionalwaveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl_ConditionalWaveformExpression)

@given(instance=vhdl_BuiltinFuncs_strategy)
@settings(max_examples=50)
def test_vhdl_builtinfuncs_instantiation(instance):
    assert isinstance(instance, vhdl_BuiltinFuncs)



@given(instance=vhdl_BuiltinFuncs_strategy)
def test_vhdl_builtinfuncs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_Open_strategy)
@settings(max_examples=50)
def test_vhdl_open_instantiation(instance):
    assert isinstance(instance, vhdl_Open)



@given(instance=vhdl_Open_strategy)
def test_vhdl_open_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_SliceExpression_strategy)
@settings(max_examples=50)
def test_vhdl_sliceexpression_instantiation(instance):
    assert isinstance(instance, vhdl_SliceExpression)

@given(instance=vhdl_RangeExpression_strategy)
@settings(max_examples=50)
def test_vhdl_rangeexpression_instantiation(instance):
    assert isinstance(instance, vhdl_RangeExpression)



@given(instance=vhdl_RangeExpression_strategy)
def test_vhdl_rangeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=vhdl_RangeExpression_strategy)
def test_vhdl_rangeexpression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=vhdl_String_strategy)
@settings(max_examples=50)
def test_vhdl_string_instantiation(instance):
    assert isinstance(instance, vhdl_String)



@given(instance=vhdl_String_strategy)
def test_vhdl_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_IfStatementTest_strategy)
@settings(max_examples=50)
def test_vhdl_ifstatementtest_instantiation(instance):
    assert isinstance(instance, vhdl_IfStatementTest)

@given(instance=IterationScheme_strategy)
@settings(max_examples=50)
def test_iterationscheme_instantiation(instance):
    assert isinstance(instance, IterationScheme)

@given(instance=vhdl_ForIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_foriterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_ForIterationScheme)



@given(instance=vhdl_ForIterationScheme_strategy)
def test_vhdl_foriterationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=vhdl_WhileIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_whileiterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_WhileIterationScheme)

@given(instance=vhdl_IterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_iterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_IterationScheme)

@given(instance=vhdl_CaseAlternative_strategy)
@settings(max_examples=50)
def test_vhdl_casealternative_instantiation(instance):
    assert isinstance(instance, vhdl_CaseAlternative)

@given(instance=vhdl_GenericMapAssociation_strategy)
@settings(max_examples=50)
def test_vhdl_genericmapassociation_instantiation(instance):
    assert isinstance(instance, vhdl_GenericMapAssociation)



@given(instance=vhdl_GenericMapAssociation_strategy)
def test_vhdl_genericmapassociation_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=vhdl_PortMapAssociation_strategy)
@settings(max_examples=50)
def test_vhdl_portmapassociation_instantiation(instance):
    assert isinstance(instance, vhdl_PortMapAssociation)



@given(instance=vhdl_PortMapAssociation_strategy)
def test_vhdl_portmapassociation_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=SequentialStatement_strategy)
@settings(max_examples=50)
def test_sequentialstatement_instantiation(instance):
    assert isinstance(instance, SequentialStatement)

@given(instance=vhdl_SequentialSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_sequentialsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_SequentialSignalAssignmentStatement)



@given(instance=vhdl_SequentialSignalAssignmentStatement_strategy)
def test_vhdl_sequentialsignalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original



@given(instance=vhdl_SequentialSignalAssignmentStatement_strategy)
def test_vhdl_sequentialsignalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original



@given(instance=vhdl_SequentialSignalAssignmentStatement_strategy)
def test_vhdl_sequentialsignalassignmentstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_CaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl_casestatement_instantiation(instance):
    assert isinstance(instance, vhdl_CaseStatement)



@given(instance=vhdl_CaseStatement_strategy)
def test_vhdl_casestatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_IfStatement_strategy)
@settings(max_examples=50)
def test_vhdl_ifstatement_instantiation(instance):
    assert isinstance(instance, vhdl_IfStatement)



@given(instance=vhdl_IfStatement_strategy)
def test_vhdl_ifstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_LoopStatement_strategy)
@settings(max_examples=50)
def test_vhdl_loopstatement_instantiation(instance):
    assert isinstance(instance, vhdl_LoopStatement)

@given(instance=vhdl_WaitStatement_strategy)
@settings(max_examples=50)
def test_vhdl_waitstatement_instantiation(instance):
    assert isinstance(instance, vhdl_WaitStatement)



@given(instance=vhdl_WaitStatement_strategy)
def test_vhdl_waitstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_PortMap_strategy)
@settings(max_examples=50)
def test_vhdl_portmap_instantiation(instance):
    assert isinstance(instance, vhdl_PortMap)

@given(instance=vhdl_GenericMap_strategy)
@settings(max_examples=50)
def test_vhdl_genericmap_instantiation(instance):
    assert isinstance(instance, vhdl_GenericMap)

@given(instance=vhdl_SequentialStatement_strategy)
@settings(max_examples=50)
def test_vhdl_sequentialstatement_instantiation(instance):
    assert isinstance(instance, vhdl_SequentialStatement)

@given(instance=vhdl_IdList_strategy)
@settings(max_examples=50)
def test_vhdl_idlist_instantiation(instance):
    assert isinstance(instance, vhdl_IdList)

@given(instance=ArchitectureStatement_strategy)
@settings(max_examples=50)
def test_architecturestatement_instantiation(instance):
    assert isinstance(instance, ArchitectureStatement)

@given(instance=vhdl_ForGenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl_forgeneratestatement_instantiation(instance):
    assert isinstance(instance, vhdl_ForGenerateStatement)

@given(instance=vhdl_ComponentInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_componentinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_ComponentInstantiationStatement)



@given(instance=vhdl_ComponentInstantiationStatement_strategy)
def test_vhdl_componentinstantiationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_ConditionalSignalAssignmentStatement)



@given(instance=vhdl_ConditionalSignalAssignmentStatement_strategy)
def test_vhdl_conditionalsignalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original



@given(instance=vhdl_ConditionalSignalAssignmentStatement_strategy)
def test_vhdl_conditionalsignalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl_EntityInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_entityinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_EntityInstantiationStatement)



@given(instance=vhdl_EntityInstantiationStatement_strategy)
def test_vhdl_entityinstantiationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_IfGenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl_ifgeneratestatement_instantiation(instance):
    assert isinstance(instance, vhdl_IfGenerateStatement)

@given(instance=vhdl_ProcessStatement_strategy)
@settings(max_examples=50)
def test_vhdl_processstatement_instantiation(instance):
    assert isinstance(instance, vhdl_ProcessStatement)



@given(instance=vhdl_ProcessStatement_strategy)
def test_vhdl_processstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl_SubtypeIndication_strategy)
@settings(max_examples=50)
def test_vhdl_subtypeindication_instantiation(instance):
    assert isinstance(instance, vhdl_SubtypeIndication)



@given(instance=vhdl_SubtypeIndication_strategy)
def test_vhdl_subtypeindication_builtin_type_setter(instance):
    original = instance.builtin_type
    instance.builtin_type = original
    assert instance.builtin_type == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=vhdl_LoopVariable_strategy)
@settings(max_examples=50)
def test_vhdl_loopvariable_instantiation(instance):
    assert isinstance(instance, vhdl_LoopVariable)

@given(instance=vhdl_Constant_strategy)
@settings(max_examples=50)
def test_vhdl_constant_instantiation(instance):
    assert isinstance(instance, vhdl_Constant)

@given(instance=vhdl_Port_strategy)
@settings(max_examples=50)
def test_vhdl_port_instantiation(instance):
    assert isinstance(instance, vhdl_Port)



@given(instance=vhdl_Port_strategy)
def test_vhdl_port_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=vhdl_Port_strategy)
def test_vhdl_port_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=vhdl_Ports_strategy)
@settings(max_examples=50)
def test_vhdl_ports_instantiation(instance):
    assert isinstance(instance, vhdl_Ports)

@given(instance=vhdl_Generics_strategy)
@settings(max_examples=50)
def test_vhdl_generics_instantiation(instance):
    assert isinstance(instance, vhdl_Generics)

@given(instance=vhdl_Var_strategy)
@settings(max_examples=50)
def test_vhdl_var_instantiation(instance):
    assert isinstance(instance, vhdl_Var)

@given(instance=vhdl_Signal_strategy)
@settings(max_examples=50)
def test_vhdl_signal_instantiation(instance):
    assert isinstance(instance, vhdl_Signal)

@given(instance=package_declarative_item_strategy)
@settings(max_examples=50)
def test_package_declarative_item_instantiation(instance):
    assert isinstance(instance, package_declarative_item)

@given(instance=BlockDeclarativeItem_strategy)
@settings(max_examples=50)
def test_blockdeclarativeitem_instantiation(instance):
    assert isinstance(instance, BlockDeclarativeItem)

@given(instance=vhdl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_VariableDeclaration)



@given(instance=vhdl_VariableDeclaration_strategy)
def test_vhdl_variabledeclaration_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=vhdl_Type_strategy)
@settings(max_examples=50)
def test_vhdl_type_instantiation(instance):
    assert isinstance(instance, vhdl_Type)



@given(instance=vhdl_Type_strategy)
def test_vhdl_type_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=vhdl_Type_strategy)
def test_vhdl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_constantdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_ConstantDeclaration)

@given(instance=vhdl_SignalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_signaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_SignalDeclaration)



@given(instance=vhdl_SignalDeclaration_strategy)
def test_vhdl_signaldeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=vhdl_Component_strategy)
@settings(max_examples=50)
def test_vhdl_component_instantiation(instance):
    assert isinstance(instance, vhdl_Component)



@given(instance=vhdl_Component_strategy)
def test_vhdl_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_AttributeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_attributedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_AttributeDeclaration)



@given(instance=vhdl_AttributeDeclaration_strategy)
def test_vhdl_attributedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vhdl_AttributeDeclaration_strategy)
def test_vhdl_attributedeclaration_type_keyword_setter(instance):
    original = instance.type_keyword
    instance.type_keyword = original
    assert instance.type_keyword == original



@given(instance=vhdl_AttributeDeclaration_strategy)
def test_vhdl_attributedeclaration_type_id_setter(instance):
    original = instance.type_id
    instance.type_id = original
    assert instance.type_id == original

@given(instance=vhdl_AttributeSpecification_strategy)
@settings(max_examples=50)
def test_vhdl_attributespecification_instantiation(instance):
    assert isinstance(instance, vhdl_AttributeSpecification)



@given(instance=vhdl_AttributeSpecification_strategy)
def test_vhdl_attributespecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vhdl_AttributeSpecification_strategy)
def test_vhdl_attributespecification_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original



@given(instance=vhdl_AttributeSpecification_strategy)
def test_vhdl_attributespecification_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=vhdl_Alias_strategy)
@settings(max_examples=50)
def test_vhdl_alias_instantiation(instance):
    assert isinstance(instance, vhdl_Alias)

@given(instance=vhdl_Generic_strategy)
@settings(max_examples=50)
def test_vhdl_generic_instantiation(instance):
    assert isinstance(instance, vhdl_Generic)

@given(instance=vhdl_Expression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_instantiation(instance):
    assert isinstance(instance, vhdl_Expression)



@given(instance=vhdl_Expression_strategy)
def test_vhdl_expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original



@given(instance=vhdl_Expression_strategy)
def test_vhdl_expression_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=vhdl_DesignFile_strategy)
@settings(max_examples=50)
def test_vhdl_designfile_instantiation(instance):
    assert isinstance(instance, vhdl_DesignFile)

@given(instance=vhdl_ArchitectureStatement_strategy)
@settings(max_examples=50)
def test_vhdl_architecturestatement_instantiation(instance):
    assert isinstance(instance, vhdl_ArchitectureStatement)



@given(instance=vhdl_ArchitectureStatement_strategy)
def test_vhdl_architecturestatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_BlockDeclarativeItem_strategy)
@settings(max_examples=50)
def test_vhdl_blockdeclarativeitem_instantiation(instance):
    assert isinstance(instance, vhdl_BlockDeclarativeItem)

@given(instance=vhdl_package_declarative_part_strategy)
@settings(max_examples=50)
def test_vhdl_package_declarative_part_instantiation(instance):
    assert isinstance(instance, vhdl_package_declarative_part)

@given(instance=vhdl_package_declarative_item_strategy)
@settings(max_examples=50)
def test_vhdl_package_declarative_item_instantiation(instance):
    assert isinstance(instance, vhdl_package_declarative_item)

@given(instance=LibraryUnit_strategy)
@settings(max_examples=50)
def test_libraryunit_instantiation(instance):
    assert isinstance(instance, LibraryUnit)

@given(instance=vhdl_Architecture_strategy)
@settings(max_examples=50)
def test_vhdl_architecture_instantiation(instance):
    assert isinstance(instance, vhdl_Architecture)

@given(instance=vhdl_Entity_strategy)
@settings(max_examples=50)
def test_vhdl_entity_instantiation(instance):
    assert isinstance(instance, vhdl_Entity)

@given(instance=vhdl_Package_strategy)
@settings(max_examples=50)
def test_vhdl_package_instantiation(instance):
    assert isinstance(instance, vhdl_Package)

@given(instance=vhdl_Library_strategy)
@settings(max_examples=50)
def test_vhdl_library_instantiation(instance):
    assert isinstance(instance, vhdl_Library)



@given(instance=vhdl_Library_strategy)
def test_vhdl_library_builtin_lib_setter(instance):
    original = instance.builtin_lib
    instance.builtin_lib = original
    assert instance.builtin_lib == original

@given(instance=ContextItem_strategy)
@settings(max_examples=50)
def test_contextitem_instantiation(instance):
    assert isinstance(instance, ContextItem)

@given(instance=vhdl_LibraryClause_strategy)
@settings(max_examples=50)
def test_vhdl_libraryclause_instantiation(instance):
    assert isinstance(instance, vhdl_LibraryClause)



@given(instance=vhdl_LibraryClause_strategy)
def test_vhdl_libraryclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_UseClause_strategy)
@settings(max_examples=50)
def test_vhdl_useclause_instantiation(instance):
    assert isinstance(instance, vhdl_UseClause)



@given(instance=vhdl_UseClause_strategy)
def test_vhdl_useclause_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=vhdl_LibraryUnit_strategy)
@settings(max_examples=50)
def test_vhdl_libraryunit_instantiation(instance):
    assert isinstance(instance, vhdl_LibraryUnit)



@given(instance=vhdl_LibraryUnit_strategy)
def test_vhdl_libraryunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl_ContextItem_strategy)
@settings(max_examples=50)
def test_vhdl_contextitem_instantiation(instance):
    assert isinstance(instance, vhdl_ContextItem)

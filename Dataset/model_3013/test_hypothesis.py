import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    miniJava_Inferior,
    miniJava_Inequality,
    miniJava_Superior,
    miniJava_InferiorOrEqual,
    miniJava_And,
    miniJava_Equality,
    miniJava_SuperiorOrEqual,
    miniJava_Or,
    miniJava_Assignee,
    Assignee,
    miniJava_NamedElement,
    SingleTypeRef,
    miniJava_VoidTypeRef,
    miniJava_IntegerTypeRef,
    miniJava_BooleanTypeRef,
    miniJava_StringTypeRef,
    miniJava_ClassRef,
    TypeRef,
    miniJava_ArrayTypeRef,
    miniJava_SingleTypeRef,
    miniJava_TypeRef,
    miniJava_Statement,
    Statement,
    miniJava_ForStatement,
    miniJava_PrintStatement,
    miniJava_WhileStatement,
    miniJava_Return,
    miniJava_IfStatement,
    miniJava_Assignment,
    miniJava_Expression,
    Symbol,
    miniJava_VariableDeclaration,
    miniJava_ClazzToMethodMap,
    miniJava_Block,
    Member,
    miniJava_Field,
    miniJava_Method,
    TypedDeclaration,
    miniJava_Symbol,
    TypeDeclaration,
    miniJava_Clazz,
    miniJava_Member,
    miniJava_Interface,
    NamedElement,
    miniJava_TypedDeclaration,
    miniJava_State,
    miniJava_TypeDeclaration,
    miniJava_Import,
    miniJava_Program,
    miniJava_Parameter,
    miniJava_Modulo,
    Call,
    miniJava_MethodCall2,
    miniJava_NewCall,
    miniJava_Call,
    miniJava_ArrayInstance,
    miniJava_ObjectInstance,
    miniJava_Frame,
    miniJava_OutputStream,
    miniJava_FieldBinding,
    Value,
    miniJava_NullValue,
    miniJava_ObjectRefValue,
    miniJava_StringValue,
    miniJava_ArrayRefValue,
    miniJava_IntegerValue,
    miniJava_Value,
    miniJava_SymbolToSymbolBindingMap,
    miniJava_SymbolBinding,
    miniJava_Context,
    miniJava_SymbolRef,
    miniJava_NewArray,
    miniJava_NewObject,
    miniJava_Null,
    miniJava_Super,
    miniJava_This,
    miniJava_BoolConstant,
    miniJava_IntConstant,
    miniJava_StringConstant,
    miniJava_BooleanValue,
    miniJava_MethodCall,
    miniJava_FieldAccess,
    miniJava_Neg,
    miniJava_Not,
    miniJava_ArrayLength,
    miniJava_ArrayAccess,
    miniJava_Division,
    miniJava_Multiplication,
    miniJava_Minus,
    miniJava_Plus,
    AccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_minijava_inferior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inferior)


def test_minijava_inferior_constructor_exists():
    assert callable(miniJava_Inferior.__init__)


def test_minijava_inferior_constructor_args():
    sig = inspect.signature(miniJava_Inferior.__init__)
    params = list(sig.parameters.keys())



def test_minijava_inequality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inequality)


def test_minijava_inequality_constructor_exists():
    assert callable(miniJava_Inequality.__init__)


def test_minijava_inequality_constructor_args():
    sig = inspect.signature(miniJava_Inequality.__init__)
    params = list(sig.parameters.keys())



def test_minijava_superior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Superior)


def test_minijava_superior_constructor_exists():
    assert callable(miniJava_Superior.__init__)


def test_minijava_superior_constructor_args():
    sig = inspect.signature(miniJava_Superior.__init__)
    params = list(sig.parameters.keys())



def test_minijava_inferiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_InferiorOrEqual)


def test_minijava_inferiororequal_constructor_exists():
    assert callable(miniJava_InferiorOrEqual.__init__)


def test_minijava_inferiororequal_constructor_args():
    sig = inspect.signature(miniJava_InferiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava_and_is_not_abstract():
    assert not inspect.isabstract(miniJava_And)


def test_minijava_and_constructor_exists():
    assert callable(miniJava_And.__init__)


def test_minijava_and_constructor_args():
    sig = inspect.signature(miniJava_And.__init__)
    params = list(sig.parameters.keys())



def test_minijava_equality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Equality)


def test_minijava_equality_constructor_exists():
    assert callable(miniJava_Equality.__init__)


def test_minijava_equality_constructor_args():
    sig = inspect.signature(miniJava_Equality.__init__)
    params = list(sig.parameters.keys())



def test_minijava_superiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_SuperiorOrEqual)


def test_minijava_superiororequal_constructor_exists():
    assert callable(miniJava_SuperiorOrEqual.__init__)


def test_minijava_superiororequal_constructor_args():
    sig = inspect.signature(miniJava_SuperiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava_or_is_not_abstract():
    assert not inspect.isabstract(miniJava_Or)


def test_minijava_or_constructor_exists():
    assert callable(miniJava_Or.__init__)


def test_minijava_or_constructor_args():
    sig = inspect.signature(miniJava_Or.__init__)
    params = list(sig.parameters.keys())



def test_minijava_assignee_is_not_abstract():
    assert not inspect.isabstract(miniJava_Assignee)


def test_minijava_assignee_constructor_exists():
    assert callable(miniJava_Assignee.__init__)


def test_minijava_assignee_constructor_args():
    sig = inspect.signature(miniJava_Assignee.__init__)
    params = list(sig.parameters.keys())



def test_assignee_is_not_abstract():
    assert not inspect.isabstract(Assignee)


def test_assignee_constructor_exists():
    assert callable(Assignee.__init__)


def test_assignee_constructor_args():
    sig = inspect.signature(Assignee.__init__)
    params = list(sig.parameters.keys())



def test_minijava_namedelement_is_not_abstract():
    assert not inspect.isabstract(miniJava_NamedElement)


def test_minijava_namedelement_constructor_exists():
    assert callable(miniJava_NamedElement.__init__)


def test_minijava_namedelement_constructor_args():
    sig = inspect.signature(miniJava_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava_namedelement_has_name():
    assert hasattr(miniJava_NamedElement, "name")
    descriptor = None
    for klass in miniJava_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_singletyperef_is_not_abstract():
    assert not inspect.isabstract(SingleTypeRef)


def test_singletyperef_constructor_exists():
    assert callable(SingleTypeRef.__init__)


def test_singletyperef_constructor_args():
    sig = inspect.signature(SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_voidtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_VoidTypeRef)


def test_minijava_voidtyperef_constructor_exists():
    assert callable(miniJava_VoidTypeRef.__init__)


def test_minijava_voidtyperef_constructor_args():
    sig = inspect.signature(miniJava_VoidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_integertyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntegerTypeRef)


def test_minijava_integertyperef_constructor_exists():
    assert callable(miniJava_IntegerTypeRef.__init__)


def test_minijava_integertyperef_constructor_args():
    sig = inspect.signature(miniJava_IntegerTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_booleantyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanTypeRef)


def test_minijava_booleantyperef_constructor_exists():
    assert callable(miniJava_BooleanTypeRef.__init__)


def test_minijava_booleantyperef_constructor_args():
    sig = inspect.signature(miniJava_BooleanTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_stringtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringTypeRef)


def test_minijava_stringtyperef_constructor_exists():
    assert callable(miniJava_StringTypeRef.__init__)


def test_minijava_stringtyperef_constructor_args():
    sig = inspect.signature(miniJava_StringTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_classref_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClassRef)


def test_minijava_classref_constructor_exists():
    assert callable(miniJava_ClassRef.__init__)


def test_minijava_classref_constructor_args():
    sig = inspect.signature(miniJava_ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_typeref_is_not_abstract():
    assert not inspect.isabstract(TypeRef)


def test_typeref_constructor_exists():
    assert callable(TypeRef.__init__)


def test_typeref_constructor_args():
    sig = inspect.signature(TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_arraytyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayTypeRef)


def test_minijava_arraytyperef_constructor_exists():
    assert callable(miniJava_ArrayTypeRef.__init__)


def test_minijava_arraytyperef_constructor_args():
    sig = inspect.signature(miniJava_ArrayTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_singletyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_SingleTypeRef)


def test_minijava_singletyperef_constructor_exists():
    assert callable(miniJava_SingleTypeRef.__init__)


def test_minijava_singletyperef_constructor_args():
    sig = inspect.signature(miniJava_SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_typeref_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypeRef)


def test_minijava_typeref_constructor_exists():
    assert callable(miniJava_TypeRef.__init__)


def test_minijava_typeref_constructor_args():
    sig = inspect.signature(miniJava_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_statement_is_not_abstract():
    assert not inspect.isabstract(miniJava_Statement)


def test_minijava_statement_constructor_exists():
    assert callable(miniJava_Statement.__init__)


def test_minijava_statement_constructor_args():
    sig = inspect.signature(miniJava_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_forstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_ForStatement)


def test_minijava_forstatement_constructor_exists():
    assert callable(miniJava_ForStatement.__init__)


def test_minijava_forstatement_constructor_args():
    sig = inspect.signature(miniJava_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_printstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_PrintStatement)


def test_minijava_printstatement_constructor_exists():
    assert callable(miniJava_PrintStatement.__init__)


def test_minijava_printstatement_constructor_args():
    sig = inspect.signature(miniJava_PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_whilestatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_WhileStatement)


def test_minijava_whilestatement_constructor_exists():
    assert callable(miniJava_WhileStatement.__init__)


def test_minijava_whilestatement_constructor_args():
    sig = inspect.signature(miniJava_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_return_is_not_abstract():
    assert not inspect.isabstract(miniJava_Return)


def test_minijava_return_constructor_exists():
    assert callable(miniJava_Return.__init__)


def test_minijava_return_constructor_args():
    sig = inspect.signature(miniJava_Return.__init__)
    params = list(sig.parameters.keys())



def test_minijava_ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_IfStatement)


def test_minijava_ifstatement_constructor_exists():
    assert callable(miniJava_IfStatement.__init__)


def test_minijava_ifstatement_constructor_args():
    sig = inspect.signature(miniJava_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava_Assignment)


def test_minijava_assignment_constructor_exists():
    assert callable(miniJava_Assignment.__init__)


def test_minijava_assignment_constructor_args():
    sig = inspect.signature(miniJava_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_minijava_expression_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expression)


def test_minijava_expression_constructor_exists():
    assert callable(miniJava_Expression.__init__)


def test_minijava_expression_constructor_args():
    sig = inspect.signature(miniJava_Expression.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_minijava_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_VariableDeclaration)


def test_minijava_variabledeclaration_constructor_exists():
    assert callable(miniJava_VariableDeclaration.__init__)


def test_minijava_variabledeclaration_constructor_args():
    sig = inspect.signature(miniJava_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava_clazztomethodmap_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClazzToMethodMap)


def test_minijava_clazztomethodmap_constructor_exists():
    assert callable(miniJava_ClazzToMethodMap.__init__)


def test_minijava_clazztomethodmap_constructor_args():
    sig = inspect.signature(miniJava_ClazzToMethodMap.__init__)
    params = list(sig.parameters.keys())



def test_minijava_block_is_not_abstract():
    assert not inspect.isabstract(miniJava_Block)


def test_minijava_block_constructor_exists():
    assert callable(miniJava_Block.__init__)


def test_minijava_block_constructor_args():
    sig = inspect.signature(miniJava_Block.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_minijava_field_is_not_abstract():
    assert not inspect.isabstract(miniJava_Field)


def test_minijava_field_constructor_exists():
    assert callable(miniJava_Field.__init__)


def test_minijava_field_constructor_args():
    sig = inspect.signature(miniJava_Field.__init__)
    params = list(sig.parameters.keys())



def test_minijava_method_is_not_abstract():
    assert not inspect.isabstract(miniJava_Method)


def test_minijava_method_constructor_exists():
    assert callable(miniJava_Method.__init__)


def test_minijava_method_constructor_args():
    sig = inspect.signature(miniJava_Method.__init__)
    params = list(sig.parameters.keys())
    assert "isabstract" in params, "Missing parameter 'isabstract'"
    assert "isstatic" in params, "Missing parameter 'isstatic'"

def test_minijava_method_has_isabstract():
    assert hasattr(miniJava_Method, "isabstract")
    descriptor = None
    for klass in miniJava_Method.__mro__:
        if "isabstract" in klass.__dict__:
            descriptor = klass.__dict__["isabstract"]
            break
    assert isinstance(descriptor, property)

def test_minijava_method_has_isstatic():
    assert hasattr(miniJava_Method, "isstatic")
    descriptor = None
    for klass in miniJava_Method.__mro__:
        if "isstatic" in klass.__dict__:
            descriptor = klass.__dict__["isstatic"]
            break
    assert isinstance(descriptor, property)



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava_symbol_is_not_abstract():
    assert not inspect.isabstract(miniJava_Symbol)


def test_minijava_symbol_constructor_exists():
    assert callable(miniJava_Symbol.__init__)


def test_minijava_symbol_constructor_args():
    sig = inspect.signature(miniJava_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava_clazz_is_not_abstract():
    assert not inspect.isabstract(miniJava_Clazz)


def test_minijava_clazz_constructor_exists():
    assert callable(miniJava_Clazz.__init__)


def test_minijava_clazz_constructor_args():
    sig = inspect.signature(miniJava_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "isabstract" in params, "Missing parameter 'isabstract'"

def test_minijava_clazz_has_isabstract():
    assert hasattr(miniJava_Clazz, "isabstract")
    descriptor = None
    for klass in miniJava_Clazz.__mro__:
        if "isabstract" in klass.__dict__:
            descriptor = klass.__dict__["isabstract"]
            break
    assert isinstance(descriptor, property)



def test_minijava_member_is_not_abstract():
    assert not inspect.isabstract(miniJava_Member)


def test_minijava_member_constructor_exists():
    assert callable(miniJava_Member.__init__)


def test_minijava_member_constructor_args():
    sig = inspect.signature(miniJava_Member.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"

def test_minijava_member_has_access():
    assert hasattr(miniJava_Member, "access")
    descriptor = None
    for klass in miniJava_Member.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_minijava_interface_is_not_abstract():
    assert not inspect.isabstract(miniJava_Interface)


def test_minijava_interface_constructor_exists():
    assert callable(miniJava_Interface.__init__)


def test_minijava_interface_constructor_args():
    sig = inspect.signature(miniJava_Interface.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_minijava_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypedDeclaration)


def test_minijava_typeddeclaration_constructor_exists():
    assert callable(miniJava_TypedDeclaration.__init__)


def test_minijava_typeddeclaration_constructor_args():
    sig = inspect.signature(miniJava_TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava_state_is_not_abstract():
    assert not inspect.isabstract(miniJava_State)


def test_minijava_state_constructor_exists():
    assert callable(miniJava_State.__init__)


def test_minijava_state_constructor_args():
    sig = inspect.signature(miniJava_State.__init__)
    params = list(sig.parameters.keys())



def test_minijava_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypeDeclaration)


def test_minijava_typedeclaration_constructor_exists():
    assert callable(miniJava_TypeDeclaration.__init__)


def test_minijava_typedeclaration_constructor_args():
    sig = inspect.signature(miniJava_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"

def test_minijava_typedeclaration_has_accessLevel():
    assert hasattr(miniJava_TypeDeclaration, "accessLevel")
    descriptor = None
    for klass in miniJava_TypeDeclaration.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)



def test_minijava_import_is_not_abstract():
    assert not inspect.isabstract(miniJava_Import)


def test_minijava_import_constructor_exists():
    assert callable(miniJava_Import.__init__)


def test_minijava_import_constructor_args():
    sig = inspect.signature(miniJava_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_minijava_import_has_importedNamespace():
    assert hasattr(miniJava_Import, "importedNamespace")
    descriptor = None
    for klass in miniJava_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_minijava_program_is_not_abstract():
    assert not inspect.isabstract(miniJava_Program)


def test_minijava_program_constructor_exists():
    assert callable(miniJava_Program.__init__)


def test_minijava_program_constructor_args():
    sig = inspect.signature(miniJava_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava_program_has_name():
    assert hasattr(miniJava_Program, "name")
    descriptor = None
    for klass in miniJava_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava_parameter_is_not_abstract():
    assert not inspect.isabstract(miniJava_Parameter)


def test_minijava_parameter_constructor_exists():
    assert callable(miniJava_Parameter.__init__)


def test_minijava_parameter_constructor_args():
    sig = inspect.signature(miniJava_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_minijava_modulo_is_not_abstract():
    assert not inspect.isabstract(miniJava_Modulo)


def test_minijava_modulo_constructor_exists():
    assert callable(miniJava_Modulo.__init__)


def test_minijava_modulo_constructor_args():
    sig = inspect.signature(miniJava_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_call_constructor_exists():
    assert callable(Call.__init__)


def test_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())



def test_minijava_methodcall2_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall2)


def test_minijava_methodcall2_constructor_exists():
    assert callable(miniJava_MethodCall2.__init__)


def test_minijava_methodcall2_constructor_args():
    sig = inspect.signature(miniJava_MethodCall2.__init__)
    params = list(sig.parameters.keys())



def test_minijava_newcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewCall)


def test_minijava_newcall_constructor_exists():
    assert callable(miniJava_NewCall.__init__)


def test_minijava_newcall_constructor_args():
    sig = inspect.signature(miniJava_NewCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava_call_is_not_abstract():
    assert not inspect.isabstract(miniJava_Call)


def test_minijava_call_constructor_exists():
    assert callable(miniJava_Call.__init__)


def test_minijava_call_constructor_args():
    sig = inspect.signature(miniJava_Call.__init__)
    params = list(sig.parameters.keys())



def test_minijava_arrayinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayInstance)


def test_minijava_arrayinstance_constructor_exists():
    assert callable(miniJava_ArrayInstance.__init__)


def test_minijava_arrayinstance_constructor_args():
    sig = inspect.signature(miniJava_ArrayInstance.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_minijava_arrayinstance_has_size():
    assert hasattr(miniJava_ArrayInstance, "size")
    descriptor = None
    for klass in miniJava_ArrayInstance.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_minijava_objectinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava_ObjectInstance)


def test_minijava_objectinstance_constructor_exists():
    assert callable(miniJava_ObjectInstance.__init__)


def test_minijava_objectinstance_constructor_args():
    sig = inspect.signature(miniJava_ObjectInstance.__init__)
    params = list(sig.parameters.keys())



def test_minijava_frame_is_not_abstract():
    assert not inspect.isabstract(miniJava_Frame)


def test_minijava_frame_constructor_exists():
    assert callable(miniJava_Frame.__init__)


def test_minijava_frame_constructor_args():
    sig = inspect.signature(miniJava_Frame.__init__)
    params = list(sig.parameters.keys())



def test_minijava_outputstream_is_not_abstract():
    assert not inspect.isabstract(miniJava_OutputStream)


def test_minijava_outputstream_constructor_exists():
    assert callable(miniJava_OutputStream.__init__)


def test_minijava_outputstream_constructor_args():
    sig = inspect.signature(miniJava_OutputStream.__init__)
    params = list(sig.parameters.keys())
    assert "stream" in params, "Missing parameter 'stream'"

def test_minijava_outputstream_has_stream():
    assert hasattr(miniJava_OutputStream, "stream")
    descriptor = None
    for klass in miniJava_OutputStream.__mro__:
        if "stream" in klass.__dict__:
            descriptor = klass.__dict__["stream"]
            break
    assert isinstance(descriptor, property)



def test_minijava_fieldbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava_FieldBinding)


def test_minijava_fieldbinding_constructor_exists():
    assert callable(miniJava_FieldBinding.__init__)


def test_minijava_fieldbinding_constructor_args():
    sig = inspect.signature(miniJava_FieldBinding.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_minijava_nullvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_NullValue)


def test_minijava_nullvalue_constructor_exists():
    assert callable(miniJava_NullValue.__init__)


def test_minijava_nullvalue_constructor_args():
    sig = inspect.signature(miniJava_NullValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava_objectrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ObjectRefValue)


def test_minijava_objectrefvalue_constructor_exists():
    assert callable(miniJava_ObjectRefValue.__init__)


def test_minijava_objectrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ObjectRefValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava_stringvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringValue)


def test_minijava_stringvalue_constructor_exists():
    assert callable(miniJava_StringValue.__init__)


def test_minijava_stringvalue_constructor_args():
    sig = inspect.signature(miniJava_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_stringvalue_has_value():
    assert hasattr(miniJava_StringValue, "value")
    descriptor = None
    for klass in miniJava_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_arrayrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayRefValue)


def test_minijava_arrayrefvalue_constructor_exists():
    assert callable(miniJava_ArrayRefValue.__init__)


def test_minijava_arrayrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ArrayRefValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava_integervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntegerValue)


def test_minijava_integervalue_constructor_exists():
    assert callable(miniJava_IntegerValue.__init__)


def test_minijava_integervalue_constructor_args():
    sig = inspect.signature(miniJava_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_integervalue_has_value():
    assert hasattr(miniJava_IntegerValue, "value")
    descriptor = None
    for klass in miniJava_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_value_is_not_abstract():
    assert not inspect.isabstract(miniJava_Value)


def test_minijava_value_constructor_exists():
    assert callable(miniJava_Value.__init__)


def test_minijava_value_constructor_args():
    sig = inspect.signature(miniJava_Value.__init__)
    params = list(sig.parameters.keys())



def test_minijava_symboltosymbolbindingmap_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolToSymbolBindingMap)


def test_minijava_symboltosymbolbindingmap_constructor_exists():
    assert callable(miniJava_SymbolToSymbolBindingMap.__init__)


def test_minijava_symboltosymbolbindingmap_constructor_args():
    sig = inspect.signature(miniJava_SymbolToSymbolBindingMap.__init__)
    params = list(sig.parameters.keys())



def test_minijava_symbolbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolBinding)


def test_minijava_symbolbinding_constructor_exists():
    assert callable(miniJava_SymbolBinding.__init__)


def test_minijava_symbolbinding_constructor_args():
    sig = inspect.signature(miniJava_SymbolBinding.__init__)
    params = list(sig.parameters.keys())



def test_minijava_context_is_not_abstract():
    assert not inspect.isabstract(miniJava_Context)


def test_minijava_context_constructor_exists():
    assert callable(miniJava_Context.__init__)


def test_minijava_context_constructor_args():
    sig = inspect.signature(miniJava_Context.__init__)
    params = list(sig.parameters.keys())



def test_minijava_symbolref_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolRef)


def test_minijava_symbolref_constructor_exists():
    assert callable(miniJava_SymbolRef.__init__)


def test_minijava_symbolref_constructor_args():
    sig = inspect.signature(miniJava_SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava_newarray_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewArray)


def test_minijava_newarray_constructor_exists():
    assert callable(miniJava_NewArray.__init__)


def test_minijava_newarray_constructor_args():
    sig = inspect.signature(miniJava_NewArray.__init__)
    params = list(sig.parameters.keys())



def test_minijava_newobject_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewObject)


def test_minijava_newobject_constructor_exists():
    assert callable(miniJava_NewObject.__init__)


def test_minijava_newobject_constructor_args():
    sig = inspect.signature(miniJava_NewObject.__init__)
    params = list(sig.parameters.keys())



def test_minijava_null_is_not_abstract():
    assert not inspect.isabstract(miniJava_Null)


def test_minijava_null_constructor_exists():
    assert callable(miniJava_Null.__init__)


def test_minijava_null_constructor_args():
    sig = inspect.signature(miniJava_Null.__init__)
    params = list(sig.parameters.keys())



def test_minijava_super_is_not_abstract():
    assert not inspect.isabstract(miniJava_Super)


def test_minijava_super_constructor_exists():
    assert callable(miniJava_Super.__init__)


def test_minijava_super_constructor_args():
    sig = inspect.signature(miniJava_Super.__init__)
    params = list(sig.parameters.keys())



def test_minijava_this_is_not_abstract():
    assert not inspect.isabstract(miniJava_This)


def test_minijava_this_constructor_exists():
    assert callable(miniJava_This.__init__)


def test_minijava_this_constructor_args():
    sig = inspect.signature(miniJava_This.__init__)
    params = list(sig.parameters.keys())



def test_minijava_boolconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_BoolConstant)


def test_minijava_boolconstant_constructor_exists():
    assert callable(miniJava_BoolConstant.__init__)


def test_minijava_boolconstant_constructor_args():
    sig = inspect.signature(miniJava_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_boolconstant_has_value():
    assert hasattr(miniJava_BoolConstant, "value")
    descriptor = None
    for klass in miniJava_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_intconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntConstant)


def test_minijava_intconstant_constructor_exists():
    assert callable(miniJava_IntConstant.__init__)


def test_minijava_intconstant_constructor_args():
    sig = inspect.signature(miniJava_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_intconstant_has_value():
    assert hasattr(miniJava_IntConstant, "value")
    descriptor = None
    for klass in miniJava_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_stringconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringConstant)


def test_minijava_stringconstant_constructor_exists():
    assert callable(miniJava_StringConstant.__init__)


def test_minijava_stringconstant_constructor_args():
    sig = inspect.signature(miniJava_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_stringconstant_has_value():
    assert hasattr(miniJava_StringConstant, "value")
    descriptor = None
    for klass in miniJava_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanValue)


def test_minijava_booleanvalue_constructor_exists():
    assert callable(miniJava_BooleanValue.__init__)


def test_minijava_booleanvalue_constructor_args():
    sig = inspect.signature(miniJava_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_booleanvalue_has_value():
    assert hasattr(miniJava_BooleanValue, "value")
    descriptor = None
    for klass in miniJava_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall)


def test_minijava_methodcall_constructor_exists():
    assert callable(miniJava_MethodCall.__init__)


def test_minijava_methodcall_constructor_args():
    sig = inspect.signature(miniJava_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_FieldAccess)


def test_minijava_fieldaccess_constructor_exists():
    assert callable(miniJava_FieldAccess.__init__)


def test_minijava_fieldaccess_constructor_args():
    sig = inspect.signature(miniJava_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_minijava_neg_is_not_abstract():
    assert not inspect.isabstract(miniJava_Neg)


def test_minijava_neg_constructor_exists():
    assert callable(miniJava_Neg.__init__)


def test_minijava_neg_constructor_args():
    sig = inspect.signature(miniJava_Neg.__init__)
    params = list(sig.parameters.keys())



def test_minijava_not_is_not_abstract():
    assert not inspect.isabstract(miniJava_Not)


def test_minijava_not_constructor_exists():
    assert callable(miniJava_Not.__init__)


def test_minijava_not_constructor_args():
    sig = inspect.signature(miniJava_Not.__init__)
    params = list(sig.parameters.keys())



def test_minijava_arraylength_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayLength)


def test_minijava_arraylength_constructor_exists():
    assert callable(miniJava_ArrayLength.__init__)


def test_minijava_arraylength_constructor_args():
    sig = inspect.signature(miniJava_ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_minijava_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayAccess)


def test_minijava_arrayaccess_constructor_exists():
    assert callable(miniJava_ArrayAccess.__init__)


def test_minijava_arrayaccess_constructor_args():
    sig = inspect.signature(miniJava_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_minijava_division_is_not_abstract():
    assert not inspect.isabstract(miniJava_Division)


def test_minijava_division_constructor_exists():
    assert callable(miniJava_Division.__init__)


def test_minijava_division_constructor_args():
    sig = inspect.signature(miniJava_Division.__init__)
    params = list(sig.parameters.keys())



def test_minijava_multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava_Multiplication)


def test_minijava_multiplication_constructor_exists():
    assert callable(miniJava_Multiplication.__init__)


def test_minijava_multiplication_constructor_args():
    sig = inspect.signature(miniJava_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_minijava_minus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Minus)


def test_minijava_minus_constructor_exists():
    assert callable(miniJava_Minus.__init__)


def test_minijava_minus_constructor_args():
    sig = inspect.signature(miniJava_Minus.__init__)
    params = list(sig.parameters.keys())



def test_minijava_plus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Plus)


def test_minijava_plus_constructor_exists():
    assert callable(miniJava_Plus.__init__)


def test_minijava_plus_constructor_args():
    sig = inspect.signature(miniJava_Plus.__init__)
    params = list(sig.parameters.keys())

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"


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
Expression_strategy = st.builds(
    Expression,
)
miniJava_Inferior_strategy = st.builds(
    miniJava_Inferior,
)
miniJava_Inequality_strategy = st.builds(
    miniJava_Inequality,
)
miniJava_Superior_strategy = st.builds(
    miniJava_Superior,
)
miniJava_InferiorOrEqual_strategy = st.builds(
    miniJava_InferiorOrEqual,
)
miniJava_And_strategy = st.builds(
    miniJava_And,
)
miniJava_Equality_strategy = st.builds(
    miniJava_Equality,
)
miniJava_SuperiorOrEqual_strategy = st.builds(
    miniJava_SuperiorOrEqual,
)
miniJava_Or_strategy = st.builds(
    miniJava_Or,
)
miniJava_Assignee_strategy = st.builds(
    miniJava_Assignee,
)
Assignee_strategy = st.builds(
    Assignee,
)
miniJava_NamedElement_strategy = st.builds(
    miniJava_NamedElement,
    name=
        safe_text
)
SingleTypeRef_strategy = st.builds(
    SingleTypeRef,
)
miniJava_VoidTypeRef_strategy = st.builds(
    miniJava_VoidTypeRef,
)
miniJava_IntegerTypeRef_strategy = st.builds(
    miniJava_IntegerTypeRef,
)
miniJava_BooleanTypeRef_strategy = st.builds(
    miniJava_BooleanTypeRef,
)
miniJava_StringTypeRef_strategy = st.builds(
    miniJava_StringTypeRef,
)
miniJava_ClassRef_strategy = st.builds(
    miniJava_ClassRef,
)
TypeRef_strategy = st.builds(
    TypeRef,
)
miniJava_ArrayTypeRef_strategy = st.builds(
    miniJava_ArrayTypeRef,
)
miniJava_SingleTypeRef_strategy = st.builds(
    miniJava_SingleTypeRef,
)
miniJava_TypeRef_strategy = st.builds(
    miniJava_TypeRef,
)
miniJava_Statement_strategy = st.builds(
    miniJava_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava_ForStatement_strategy = st.builds(
    miniJava_ForStatement,
)
miniJava_PrintStatement_strategy = st.builds(
    miniJava_PrintStatement,
)
miniJava_WhileStatement_strategy = st.builds(
    miniJava_WhileStatement,
)
miniJava_Return_strategy = st.builds(
    miniJava_Return,
)
miniJava_IfStatement_strategy = st.builds(
    miniJava_IfStatement,
)
miniJava_Assignment_strategy = st.builds(
    miniJava_Assignment,
)
miniJava_Expression_strategy = st.builds(
    miniJava_Expression,
)
Symbol_strategy = st.builds(
    Symbol,
)
miniJava_VariableDeclaration_strategy = st.builds(
    miniJava_VariableDeclaration,
)
miniJava_ClazzToMethodMap_strategy = st.builds(
    miniJava_ClazzToMethodMap,
)
miniJava_Block_strategy = st.builds(
    miniJava_Block,
)
Member_strategy = st.builds(
    Member,
)
miniJava_Field_strategy = st.builds(
    miniJava_Field,
)
miniJava_Method_strategy = st.builds(
    miniJava_Method,
    isabstract=
        st.booleans(),
    isstatic=
        st.booleans()
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
miniJava_Symbol_strategy = st.builds(
    miniJava_Symbol,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
miniJava_Clazz_strategy = st.builds(
    miniJava_Clazz,
    isabstract=
        st.booleans()
)
miniJava_Member_strategy = st.builds(
    miniJava_Member,
    access=
        safe_text
)
miniJava_Interface_strategy = st.builds(
    miniJava_Interface,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
miniJava_TypedDeclaration_strategy = st.builds(
    miniJava_TypedDeclaration,
)
miniJava_State_strategy = st.builds(
    miniJava_State,
)
miniJava_TypeDeclaration_strategy = st.builds(
    miniJava_TypeDeclaration,
    accessLevel=
        safe_text
)
miniJava_Import_strategy = st.builds(
    miniJava_Import,
    importedNamespace=
        safe_text
)
miniJava_Program_strategy = st.builds(
    miniJava_Program,
    name=
        safe_text
)
miniJava_Parameter_strategy = st.builds(
    miniJava_Parameter,
)
miniJava_Modulo_strategy = st.builds(
    miniJava_Modulo,
)
Call_strategy = st.builds(
    Call,
)
miniJava_MethodCall2_strategy = st.builds(
    miniJava_MethodCall2,
)
miniJava_NewCall_strategy = st.builds(
    miniJava_NewCall,
)
miniJava_Call_strategy = st.builds(
    miniJava_Call,
)
miniJava_ArrayInstance_strategy = st.builds(
    miniJava_ArrayInstance,
    size=
        st.integers()
)
miniJava_ObjectInstance_strategy = st.builds(
    miniJava_ObjectInstance,
)
miniJava_Frame_strategy = st.builds(
    miniJava_Frame,
)
miniJava_OutputStream_strategy = st.builds(
    miniJava_OutputStream,
    stream=
        safe_text
)
miniJava_FieldBinding_strategy = st.builds(
    miniJava_FieldBinding,
)
Value_strategy = st.builds(
    Value,
)
miniJava_NullValue_strategy = st.builds(
    miniJava_NullValue,
)
miniJava_ObjectRefValue_strategy = st.builds(
    miniJava_ObjectRefValue,
)
miniJava_StringValue_strategy = st.builds(
    miniJava_StringValue,
    value=
        safe_text
)
miniJava_ArrayRefValue_strategy = st.builds(
    miniJava_ArrayRefValue,
)
miniJava_IntegerValue_strategy = st.builds(
    miniJava_IntegerValue,
    value=
        st.integers()
)
miniJava_Value_strategy = st.builds(
    miniJava_Value,
)
miniJava_SymbolToSymbolBindingMap_strategy = st.builds(
    miniJava_SymbolToSymbolBindingMap,
)
miniJava_SymbolBinding_strategy = st.builds(
    miniJava_SymbolBinding,
)
miniJava_Context_strategy = st.builds(
    miniJava_Context,
)
miniJava_SymbolRef_strategy = st.builds(
    miniJava_SymbolRef,
)
miniJava_NewArray_strategy = st.builds(
    miniJava_NewArray,
)
miniJava_NewObject_strategy = st.builds(
    miniJava_NewObject,
)
miniJava_Null_strategy = st.builds(
    miniJava_Null,
)
miniJava_Super_strategy = st.builds(
    miniJava_Super,
)
miniJava_This_strategy = st.builds(
    miniJava_This,
)
miniJava_BoolConstant_strategy = st.builds(
    miniJava_BoolConstant,
    value=
        safe_text
)
miniJava_IntConstant_strategy = st.builds(
    miniJava_IntConstant,
    value=
        st.integers()
)
miniJava_StringConstant_strategy = st.builds(
    miniJava_StringConstant,
    value=
        safe_text
)
miniJava_BooleanValue_strategy = st.builds(
    miniJava_BooleanValue,
    value=
        st.booleans()
)
miniJava_MethodCall_strategy = st.builds(
    miniJava_MethodCall,
)
miniJava_FieldAccess_strategy = st.builds(
    miniJava_FieldAccess,
)
miniJava_Neg_strategy = st.builds(
    miniJava_Neg,
)
miniJava_Not_strategy = st.builds(
    miniJava_Not,
)
miniJava_ArrayLength_strategy = st.builds(
    miniJava_ArrayLength,
)
miniJava_ArrayAccess_strategy = st.builds(
    miniJava_ArrayAccess,
)
miniJava_Division_strategy = st.builds(
    miniJava_Division,
)
miniJava_Multiplication_strategy = st.builds(
    miniJava_Multiplication,
)
miniJava_Minus_strategy = st.builds(
    miniJava_Minus,
)
miniJava_Plus_strategy = st.builds(
    miniJava_Plus,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=miniJava_Inferior_strategy)
@settings(max_examples=50)
def test_minijava_inferior_instantiation(instance):
    assert isinstance(instance, miniJava_Inferior)

@given(instance=miniJava_Inequality_strategy)
@settings(max_examples=50)
def test_minijava_inequality_instantiation(instance):
    assert isinstance(instance, miniJava_Inequality)

@given(instance=miniJava_Superior_strategy)
@settings(max_examples=50)
def test_minijava_superior_instantiation(instance):
    assert isinstance(instance, miniJava_Superior)

@given(instance=miniJava_InferiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava_inferiororequal_instantiation(instance):
    assert isinstance(instance, miniJava_InferiorOrEqual)

@given(instance=miniJava_And_strategy)
@settings(max_examples=50)
def test_minijava_and_instantiation(instance):
    assert isinstance(instance, miniJava_And)

@given(instance=miniJava_Equality_strategy)
@settings(max_examples=50)
def test_minijava_equality_instantiation(instance):
    assert isinstance(instance, miniJava_Equality)

@given(instance=miniJava_SuperiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava_superiororequal_instantiation(instance):
    assert isinstance(instance, miniJava_SuperiorOrEqual)

@given(instance=miniJava_Or_strategy)
@settings(max_examples=50)
def test_minijava_or_instantiation(instance):
    assert isinstance(instance, miniJava_Or)

@given(instance=miniJava_Assignee_strategy)
@settings(max_examples=50)
def test_minijava_assignee_instantiation(instance):
    assert isinstance(instance, miniJava_Assignee)

@given(instance=Assignee_strategy)
@settings(max_examples=50)
def test_assignee_instantiation(instance):
    assert isinstance(instance, Assignee)

@given(instance=miniJava_NamedElement_strategy)
@settings(max_examples=50)
def test_minijava_namedelement_instantiation(instance):
    assert isinstance(instance, miniJava_NamedElement)



@given(instance=miniJava_NamedElement_strategy)
def test_minijava_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SingleTypeRef_strategy)
@settings(max_examples=50)
def test_singletyperef_instantiation(instance):
    assert isinstance(instance, SingleTypeRef)

@given(instance=miniJava_VoidTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_voidtyperef_instantiation(instance):
    assert isinstance(instance, miniJava_VoidTypeRef)

@given(instance=miniJava_IntegerTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_integertyperef_instantiation(instance):
    assert isinstance(instance, miniJava_IntegerTypeRef)

@given(instance=miniJava_BooleanTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_booleantyperef_instantiation(instance):
    assert isinstance(instance, miniJava_BooleanTypeRef)

@given(instance=miniJava_StringTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_stringtyperef_instantiation(instance):
    assert isinstance(instance, miniJava_StringTypeRef)

@given(instance=miniJava_ClassRef_strategy)
@settings(max_examples=50)
def test_minijava_classref_instantiation(instance):
    assert isinstance(instance, miniJava_ClassRef)

@given(instance=TypeRef_strategy)
@settings(max_examples=50)
def test_typeref_instantiation(instance):
    assert isinstance(instance, TypeRef)

@given(instance=miniJava_ArrayTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_arraytyperef_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayTypeRef)

@given(instance=miniJava_SingleTypeRef_strategy)
@settings(max_examples=50)
def test_minijava_singletyperef_instantiation(instance):
    assert isinstance(instance, miniJava_SingleTypeRef)

@given(instance=miniJava_TypeRef_strategy)
@settings(max_examples=50)
def test_minijava_typeref_instantiation(instance):
    assert isinstance(instance, miniJava_TypeRef)

@given(instance=miniJava_Statement_strategy)
@settings(max_examples=50)
def test_minijava_statement_instantiation(instance):
    assert isinstance(instance, miniJava_Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=miniJava_ForStatement_strategy)
@settings(max_examples=50)
def test_minijava_forstatement_instantiation(instance):
    assert isinstance(instance, miniJava_ForStatement)

@given(instance=miniJava_PrintStatement_strategy)
@settings(max_examples=50)
def test_minijava_printstatement_instantiation(instance):
    assert isinstance(instance, miniJava_PrintStatement)

@given(instance=miniJava_WhileStatement_strategy)
@settings(max_examples=50)
def test_minijava_whilestatement_instantiation(instance):
    assert isinstance(instance, miniJava_WhileStatement)

@given(instance=miniJava_Return_strategy)
@settings(max_examples=50)
def test_minijava_return_instantiation(instance):
    assert isinstance(instance, miniJava_Return)

@given(instance=miniJava_IfStatement_strategy)
@settings(max_examples=50)
def test_minijava_ifstatement_instantiation(instance):
    assert isinstance(instance, miniJava_IfStatement)

@given(instance=miniJava_Assignment_strategy)
@settings(max_examples=50)
def test_minijava_assignment_instantiation(instance):
    assert isinstance(instance, miniJava_Assignment)

@given(instance=miniJava_Expression_strategy)
@settings(max_examples=50)
def test_minijava_expression_instantiation(instance):
    assert isinstance(instance, miniJava_Expression)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=miniJava_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_minijava_variabledeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_VariableDeclaration)

@given(instance=miniJava_ClazzToMethodMap_strategy)
@settings(max_examples=50)
def test_minijava_clazztomethodmap_instantiation(instance):
    assert isinstance(instance, miniJava_ClazzToMethodMap)

@given(instance=miniJava_Block_strategy)
@settings(max_examples=50)
def test_minijava_block_instantiation(instance):
    assert isinstance(instance, miniJava_Block)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=miniJava_Field_strategy)
@settings(max_examples=50)
def test_minijava_field_instantiation(instance):
    assert isinstance(instance, miniJava_Field)

@given(instance=miniJava_Method_strategy)
@settings(max_examples=50)
def test_minijava_method_instantiation(instance):
    assert isinstance(instance, miniJava_Method)



@given(instance=miniJava_Method_strategy)
def test_minijava_method_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original



@given(instance=miniJava_Method_strategy)
def test_minijava_method_isstatic_setter(instance):
    original = instance.isstatic
    instance.isstatic = original
    assert instance.isstatic == original

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=miniJava_Symbol_strategy)
@settings(max_examples=50)
def test_minijava_symbol_instantiation(instance):
    assert isinstance(instance, miniJava_Symbol)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=miniJava_Clazz_strategy)
@settings(max_examples=50)
def test_minijava_clazz_instantiation(instance):
    assert isinstance(instance, miniJava_Clazz)



@given(instance=miniJava_Clazz_strategy)
def test_minijava_clazz_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original

@given(instance=miniJava_Member_strategy)
@settings(max_examples=50)
def test_minijava_member_instantiation(instance):
    assert isinstance(instance, miniJava_Member)



@given(instance=miniJava_Member_strategy)
def test_minijava_member_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=miniJava_Interface_strategy)
@settings(max_examples=50)
def test_minijava_interface_instantiation(instance):
    assert isinstance(instance, miniJava_Interface)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=miniJava_TypedDeclaration_strategy)
@settings(max_examples=50)
def test_minijava_typeddeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_TypedDeclaration)

@given(instance=miniJava_State_strategy)
@settings(max_examples=50)
def test_minijava_state_instantiation(instance):
    assert isinstance(instance, miniJava_State)

@given(instance=miniJava_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_minijava_typedeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_TypeDeclaration)



@given(instance=miniJava_TypeDeclaration_strategy)
def test_minijava_typedeclaration_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=miniJava_Import_strategy)
@settings(max_examples=50)
def test_minijava_import_instantiation(instance):
    assert isinstance(instance, miniJava_Import)



@given(instance=miniJava_Import_strategy)
def test_minijava_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=miniJava_Program_strategy)
@settings(max_examples=50)
def test_minijava_program_instantiation(instance):
    assert isinstance(instance, miniJava_Program)



@given(instance=miniJava_Program_strategy)
def test_minijava_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava_Parameter_strategy)
@settings(max_examples=50)
def test_minijava_parameter_instantiation(instance):
    assert isinstance(instance, miniJava_Parameter)

@given(instance=miniJava_Modulo_strategy)
@settings(max_examples=50)
def test_minijava_modulo_instantiation(instance):
    assert isinstance(instance, miniJava_Modulo)

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=miniJava_MethodCall2_strategy)
@settings(max_examples=50)
def test_minijava_methodcall2_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall2)

@given(instance=miniJava_NewCall_strategy)
@settings(max_examples=50)
def test_minijava_newcall_instantiation(instance):
    assert isinstance(instance, miniJava_NewCall)

@given(instance=miniJava_Call_strategy)
@settings(max_examples=50)
def test_minijava_call_instantiation(instance):
    assert isinstance(instance, miniJava_Call)

@given(instance=miniJava_ArrayInstance_strategy)
@settings(max_examples=50)
def test_minijava_arrayinstance_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayInstance)



@given(instance=miniJava_ArrayInstance_strategy)
def test_minijava_arrayinstance_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=miniJava_ObjectInstance_strategy)
@settings(max_examples=50)
def test_minijava_objectinstance_instantiation(instance):
    assert isinstance(instance, miniJava_ObjectInstance)

@given(instance=miniJava_Frame_strategy)
@settings(max_examples=50)
def test_minijava_frame_instantiation(instance):
    assert isinstance(instance, miniJava_Frame)

@given(instance=miniJava_OutputStream_strategy)
@settings(max_examples=50)
def test_minijava_outputstream_instantiation(instance):
    assert isinstance(instance, miniJava_OutputStream)



@given(instance=miniJava_OutputStream_strategy)
def test_minijava_outputstream_stream_setter(instance):
    original = instance.stream
    instance.stream = original
    assert instance.stream == original

@given(instance=miniJava_FieldBinding_strategy)
@settings(max_examples=50)
def test_minijava_fieldbinding_instantiation(instance):
    assert isinstance(instance, miniJava_FieldBinding)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=miniJava_NullValue_strategy)
@settings(max_examples=50)
def test_minijava_nullvalue_instantiation(instance):
    assert isinstance(instance, miniJava_NullValue)

@given(instance=miniJava_ObjectRefValue_strategy)
@settings(max_examples=50)
def test_minijava_objectrefvalue_instantiation(instance):
    assert isinstance(instance, miniJava_ObjectRefValue)

@given(instance=miniJava_StringValue_strategy)
@settings(max_examples=50)
def test_minijava_stringvalue_instantiation(instance):
    assert isinstance(instance, miniJava_StringValue)



@given(instance=miniJava_StringValue_strategy)
def test_minijava_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_ArrayRefValue_strategy)
@settings(max_examples=50)
def test_minijava_arrayrefvalue_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayRefValue)

@given(instance=miniJava_IntegerValue_strategy)
@settings(max_examples=50)
def test_minijava_integervalue_instantiation(instance):
    assert isinstance(instance, miniJava_IntegerValue)



@given(instance=miniJava_IntegerValue_strategy)
def test_minijava_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_Value_strategy)
@settings(max_examples=50)
def test_minijava_value_instantiation(instance):
    assert isinstance(instance, miniJava_Value)

@given(instance=miniJava_SymbolToSymbolBindingMap_strategy)
@settings(max_examples=50)
def test_minijava_symboltosymbolbindingmap_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolToSymbolBindingMap)

@given(instance=miniJava_SymbolBinding_strategy)
@settings(max_examples=50)
def test_minijava_symbolbinding_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolBinding)

@given(instance=miniJava_Context_strategy)
@settings(max_examples=50)
def test_minijava_context_instantiation(instance):
    assert isinstance(instance, miniJava_Context)

@given(instance=miniJava_SymbolRef_strategy)
@settings(max_examples=50)
def test_minijava_symbolref_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolRef)

@given(instance=miniJava_NewArray_strategy)
@settings(max_examples=50)
def test_minijava_newarray_instantiation(instance):
    assert isinstance(instance, miniJava_NewArray)

@given(instance=miniJava_NewObject_strategy)
@settings(max_examples=50)
def test_minijava_newobject_instantiation(instance):
    assert isinstance(instance, miniJava_NewObject)

@given(instance=miniJava_Null_strategy)
@settings(max_examples=50)
def test_minijava_null_instantiation(instance):
    assert isinstance(instance, miniJava_Null)

@given(instance=miniJava_Super_strategy)
@settings(max_examples=50)
def test_minijava_super_instantiation(instance):
    assert isinstance(instance, miniJava_Super)

@given(instance=miniJava_This_strategy)
@settings(max_examples=50)
def test_minijava_this_instantiation(instance):
    assert isinstance(instance, miniJava_This)

@given(instance=miniJava_BoolConstant_strategy)
@settings(max_examples=50)
def test_minijava_boolconstant_instantiation(instance):
    assert isinstance(instance, miniJava_BoolConstant)



@given(instance=miniJava_BoolConstant_strategy)
def test_minijava_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_IntConstant_strategy)
@settings(max_examples=50)
def test_minijava_intconstant_instantiation(instance):
    assert isinstance(instance, miniJava_IntConstant)



@given(instance=miniJava_IntConstant_strategy)
def test_minijava_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_StringConstant_strategy)
@settings(max_examples=50)
def test_minijava_stringconstant_instantiation(instance):
    assert isinstance(instance, miniJava_StringConstant)



@given(instance=miniJava_StringConstant_strategy)
def test_minijava_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_BooleanValue_strategy)
@settings(max_examples=50)
def test_minijava_booleanvalue_instantiation(instance):
    assert isinstance(instance, miniJava_BooleanValue)



@given(instance=miniJava_BooleanValue_strategy)
def test_minijava_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_MethodCall_strategy)
@settings(max_examples=50)
def test_minijava_methodcall_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall)

@given(instance=miniJava_FieldAccess_strategy)
@settings(max_examples=50)
def test_minijava_fieldaccess_instantiation(instance):
    assert isinstance(instance, miniJava_FieldAccess)

@given(instance=miniJava_Neg_strategy)
@settings(max_examples=50)
def test_minijava_neg_instantiation(instance):
    assert isinstance(instance, miniJava_Neg)

@given(instance=miniJava_Not_strategy)
@settings(max_examples=50)
def test_minijava_not_instantiation(instance):
    assert isinstance(instance, miniJava_Not)

@given(instance=miniJava_ArrayLength_strategy)
@settings(max_examples=50)
def test_minijava_arraylength_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayLength)

@given(instance=miniJava_ArrayAccess_strategy)
@settings(max_examples=50)
def test_minijava_arrayaccess_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayAccess)

@given(instance=miniJava_Division_strategy)
@settings(max_examples=50)
def test_minijava_division_instantiation(instance):
    assert isinstance(instance, miniJava_Division)

@given(instance=miniJava_Multiplication_strategy)
@settings(max_examples=50)
def test_minijava_multiplication_instantiation(instance):
    assert isinstance(instance, miniJava_Multiplication)

@given(instance=miniJava_Minus_strategy)
@settings(max_examples=50)
def test_minijava_minus_instantiation(instance):
    assert isinstance(instance, miniJava_Minus)

@given(instance=miniJava_Plus_strategy)
@settings(max_examples=50)
def test_minijava_plus_instantiation(instance):
    assert isinstance(instance, miniJava_Plus)

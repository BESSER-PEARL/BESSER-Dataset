import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    variables_Field,
    variables_Variable,
    ThrowTypeAccess,
    LocalVariable,
    FormalParameter,
    DeclarationTypeAccess,
    functions_Constructor,
    functions_Method,
    functions_GlobalFunction,
    functions_Function,
    VariableAccess,
    gast_accesses_PropertyAccess,
    gast_accesses_SelfAccess,
    FunctionAccess,
    gast_accesses_DelegateAccess,
    Variable,
    gast_variables_GlobalVariable,
    gast_variables_CatchParameter,
    gast_variables_FormalParameter,
    gast_variables_LocalVariable,
    CompositeAccess,
    TypeAccess,
    gast_accesses_InheritanceTypeAccess,
    gast_accesses_ThrowTypeAccess,
    gast_accesses_StaticTypeAccess,
    gast_accesses_DeclarationTypeAccess,
    gast_accesses_CastTypeAccess,
    gast_accesses_RunTimeTypeAccess,
    gast_accesses_ParameterInstantiationTypeAccess,
    Property,
    InheritanceTypeAccess,
    Method,
    Field,
    Destructor,
    Constructor,
    types_GASTType,
    core_GenericEntity,
    gast_functions_GenericConstructor,
    gast_functions_GenericFunction,
    gast_functions_GenericMethod,
    Member,
    types_TypeDecorator,
    types_Member,
    gast_functions_Constructor,
    gast_functions_Delegate,
    gast_variables_Property,
    gast_types_GASTClass,
    gast_variables_Field,
    gast_functions_Destructor,
    gast_functions_Method,
    gast_types_TypeAlias,
    TypeDecorator,
    gast_types_GASTArray,
    gast_types_Reference,
    gast_annotations_ModelAnnotation,
    core_SourceEntity,
    core_NamedModelElement,
    gast_functions_Function,
    gast_variables_Variable,
    core_ModelElement,
    annotations_ModelAnnotation,
    gast_annotations_Clone,
    gast_annotations_StructuralAbstraction,
    gast_annotations_CloneInstance,
    gast_annotations_Comment,
    types_GASTClass,
    gast_types_GenericClass,
    gast_annotations_Attribute,
    gast_core_Position,
    Position,
    File,
    BasePath,
    GASTType,
    gast_types_TypeDecorator,
    StructuralAbstraction,
    gast_annotations_Subsystem,
    gast_annotations_Layer,
    Clone,
    TypeParameterClass,
    TypeAlias,
    Package,
    gast_core_PackageAlias,
    GlobalVariable,
    Delegate,
    Access,
    gast_accesses_TypeAccess,
    gast_accesses_FunctionAccess,
    gast_accesses_VariableAccess,
    GASTClass,
    gast_types_GASTEnumeration,
    gast_types_GASTUnion,
    gast_types_TypeParameterClass,
    gast_types_GASTStruct,
    NamedModelElement,
    gast_core_Directory,
    gast_types_GASTType,
    gast_core_File,
    gast_core_Package,
    gast_core_Identifier,
    ModelAnnotation,
    GlobalFunction,
    Identifier,
    gast_core_ModelElement,
    Directory,
    Root,
    ModelElement,
    gast_core_Root,
    gast_core_NamedModelElement,
    gast_core_SourceEntity,
    gast_core_GenericEntity,
    gast_core_BasePath,
    gast_statements_GASTBehaviour,
    CatchParameter,
    BranchStatement,
    GASTExpression,
    Function,
    gast_functions_GlobalFunction,
    LoopStatement,
    Branch,
    CloneInstance,
    BaseAccess,
    gast_accesses_CompositeAccess,
    gast_accesses_Access,
    SourceEntity,
    gast_statements_Branch,
    gast_accesses_BaseAccess,
    gast_types_Member,
    gast_statements_GASTExpression,
    gast_statements_Statement,
    BlockStatement,
    gast_statements_CatchBlock,
    CatchBlock,
    Statement,
    gast_statements_JumpStatement,
    gast_statements_BranchStatement,
    gast_statements_LoopStatement,
    gast_statements_BlockStatement,
    gast_statements_SimpleStatement,
    gast_statements_ExceptionHandler,
    Status,
    GlobalFunctionKind,
    JumpStatementKind,
    Visibilities,
    LoopStatementKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variables_field_is_not_abstract():
    assert not inspect.isabstract(variables_Field)


def test_variables_field_constructor_exists():
    assert callable(variables_Field.__init__)


def test_variables_field_constructor_args():
    sig = inspect.signature(variables_Field.__init__)
    params = list(sig.parameters.keys())



def test_variables_variable_is_not_abstract():
    assert not inspect.isabstract(variables_Variable)


def test_variables_variable_constructor_exists():
    assert callable(variables_Variable.__init__)


def test_variables_variable_constructor_args():
    sig = inspect.signature(variables_Variable.__init__)
    params = list(sig.parameters.keys())



def test_throwtypeaccess_is_not_abstract():
    assert not inspect.isabstract(ThrowTypeAccess)


def test_throwtypeaccess_constructor_exists():
    assert callable(ThrowTypeAccess.__init__)


def test_throwtypeaccess_constructor_args():
    sig = inspect.signature(ThrowTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_formalparameter_is_not_abstract():
    assert not inspect.isabstract(FormalParameter)


def test_formalparameter_constructor_exists():
    assert callable(FormalParameter.__init__)


def test_formalparameter_constructor_args():
    sig = inspect.signature(FormalParameter.__init__)
    params = list(sig.parameters.keys())



def test_declarationtypeaccess_is_not_abstract():
    assert not inspect.isabstract(DeclarationTypeAccess)


def test_declarationtypeaccess_constructor_exists():
    assert callable(DeclarationTypeAccess.__init__)


def test_declarationtypeaccess_constructor_args():
    sig = inspect.signature(DeclarationTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_functions_constructor_is_not_abstract():
    assert not inspect.isabstract(functions_Constructor)


def test_functions_constructor_constructor_exists():
    assert callable(functions_Constructor.__init__)


def test_functions_constructor_constructor_args():
    sig = inspect.signature(functions_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_functions_method_is_not_abstract():
    assert not inspect.isabstract(functions_Method)


def test_functions_method_constructor_exists():
    assert callable(functions_Method.__init__)


def test_functions_method_constructor_args():
    sig = inspect.signature(functions_Method.__init__)
    params = list(sig.parameters.keys())



def test_functions_globalfunction_is_not_abstract():
    assert not inspect.isabstract(functions_GlobalFunction)


def test_functions_globalfunction_constructor_exists():
    assert callable(functions_GlobalFunction.__init__)


def test_functions_globalfunction_constructor_args():
    sig = inspect.signature(functions_GlobalFunction.__init__)
    params = list(sig.parameters.keys())



def test_functions_function_is_not_abstract():
    assert not inspect.isabstract(functions_Function)


def test_functions_function_constructor_exists():
    assert callable(functions_Function.__init__)


def test_functions_function_constructor_args():
    sig = inspect.signature(functions_Function.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_propertyaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_PropertyAccess)


def test_gast_accesses_propertyaccess_constructor_exists():
    assert callable(gast_accesses_PropertyAccess.__init__)


def test_gast_accesses_propertyaccess_constructor_args():
    sig = inspect.signature(gast_accesses_PropertyAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_selfaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_SelfAccess)


def test_gast_accesses_selfaccess_constructor_exists():
    assert callable(gast_accesses_SelfAccess.__init__)


def test_gast_accesses_selfaccess_constructor_args():
    sig = inspect.signature(gast_accesses_SelfAccess.__init__)
    params = list(sig.parameters.keys())
    assert "super" in params, "Missing parameter 'super'"

def test_gast_accesses_selfaccess_has_super():
    assert hasattr(gast_accesses_SelfAccess, "super")
    descriptor = None
    for klass in gast_accesses_SelfAccess.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)



def test_functionaccess_is_not_abstract():
    assert not inspect.isabstract(FunctionAccess)


def test_functionaccess_constructor_exists():
    assert callable(FunctionAccess.__init__)


def test_functionaccess_constructor_args():
    sig = inspect.signature(FunctionAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_delegateaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_DelegateAccess)


def test_gast_accesses_delegateaccess_constructor_exists():
    assert callable(gast_accesses_DelegateAccess.__init__)


def test_gast_accesses_delegateaccess_constructor_args():
    sig = inspect.signature(gast_accesses_DelegateAccess.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_gast_variables_globalvariable_is_not_abstract():
    assert not inspect.isabstract(gast_variables_GlobalVariable)


def test_gast_variables_globalvariable_constructor_exists():
    assert callable(gast_variables_GlobalVariable.__init__)


def test_gast_variables_globalvariable_constructor_args():
    sig = inspect.signature(gast_variables_GlobalVariable.__init__)
    params = list(sig.parameters.keys())



def test_gast_variables_catchparameter_is_not_abstract():
    assert not inspect.isabstract(gast_variables_CatchParameter)


def test_gast_variables_catchparameter_constructor_exists():
    assert callable(gast_variables_CatchParameter.__init__)


def test_gast_variables_catchparameter_constructor_args():
    sig = inspect.signature(gast_variables_CatchParameter.__init__)
    params = list(sig.parameters.keys())
    assert "rethrown" in params, "Missing parameter 'rethrown'"

def test_gast_variables_catchparameter_has_rethrown():
    assert hasattr(gast_variables_CatchParameter, "rethrown")
    descriptor = None
    for klass in gast_variables_CatchParameter.__mro__:
        if "rethrown" in klass.__dict__:
            descriptor = klass.__dict__["rethrown"]
            break
    assert isinstance(descriptor, property)



def test_gast_variables_formalparameter_is_not_abstract():
    assert not inspect.isabstract(gast_variables_FormalParameter)


def test_gast_variables_formalparameter_constructor_exists():
    assert callable(gast_variables_FormalParameter.__init__)


def test_gast_variables_formalparameter_constructor_args():
    sig = inspect.signature(gast_variables_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "passedByReference" in params, "Missing parameter 'passedByReference'"

def test_gast_variables_formalparameter_has_passedByReference():
    assert hasattr(gast_variables_FormalParameter, "passedByReference")
    descriptor = None
    for klass in gast_variables_FormalParameter.__mro__:
        if "passedByReference" in klass.__dict__:
            descriptor = klass.__dict__["passedByReference"]
            break
    assert isinstance(descriptor, property)



def test_gast_variables_localvariable_is_not_abstract():
    assert not inspect.isabstract(gast_variables_LocalVariable)


def test_gast_variables_localvariable_constructor_exists():
    assert callable(gast_variables_LocalVariable.__init__)


def test_gast_variables_localvariable_constructor_args():
    sig = inspect.signature(gast_variables_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_compositeaccess_is_not_abstract():
    assert not inspect.isabstract(CompositeAccess)


def test_compositeaccess_constructor_exists():
    assert callable(CompositeAccess.__init__)


def test_compositeaccess_constructor_args():
    sig = inspect.signature(CompositeAccess.__init__)
    params = list(sig.parameters.keys())



def test_typeaccess_is_not_abstract():
    assert not inspect.isabstract(TypeAccess)


def test_typeaccess_constructor_exists():
    assert callable(TypeAccess.__init__)


def test_typeaccess_constructor_args():
    sig = inspect.signature(TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_inheritancetypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_InheritanceTypeAccess)


def test_gast_accesses_inheritancetypeaccess_constructor_exists():
    assert callable(gast_accesses_InheritanceTypeAccess.__init__)


def test_gast_accesses_inheritancetypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_InheritanceTypeAccess.__init__)
    params = list(sig.parameters.keys())
    assert "implementationInheritance" in params, "Missing parameter 'implementationInheritance'"

def test_gast_accesses_inheritancetypeaccess_has_implementationInheritance():
    assert hasattr(gast_accesses_InheritanceTypeAccess, "implementationInheritance")
    descriptor = None
    for klass in gast_accesses_InheritanceTypeAccess.__mro__:
        if "implementationInheritance" in klass.__dict__:
            descriptor = klass.__dict__["implementationInheritance"]
            break
    assert isinstance(descriptor, property)



def test_gast_accesses_throwtypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_ThrowTypeAccess)


def test_gast_accesses_throwtypeaccess_constructor_exists():
    assert callable(gast_accesses_ThrowTypeAccess.__init__)


def test_gast_accesses_throwtypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_ThrowTypeAccess.__init__)
    params = list(sig.parameters.keys())
    assert "declared" in params, "Missing parameter 'declared'"

def test_gast_accesses_throwtypeaccess_has_declared():
    assert hasattr(gast_accesses_ThrowTypeAccess, "declared")
    descriptor = None
    for klass in gast_accesses_ThrowTypeAccess.__mro__:
        if "declared" in klass.__dict__:
            descriptor = klass.__dict__["declared"]
            break
    assert isinstance(descriptor, property)



def test_gast_accesses_statictypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_StaticTypeAccess)


def test_gast_accesses_statictypeaccess_constructor_exists():
    assert callable(gast_accesses_StaticTypeAccess.__init__)


def test_gast_accesses_statictypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_StaticTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_declarationtypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_DeclarationTypeAccess)


def test_gast_accesses_declarationtypeaccess_constructor_exists():
    assert callable(gast_accesses_DeclarationTypeAccess.__init__)


def test_gast_accesses_declarationtypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_DeclarationTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_casttypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_CastTypeAccess)


def test_gast_accesses_casttypeaccess_constructor_exists():
    assert callable(gast_accesses_CastTypeAccess.__init__)


def test_gast_accesses_casttypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_CastTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_runtimetypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_RunTimeTypeAccess)


def test_gast_accesses_runtimetypeaccess_constructor_exists():
    assert callable(gast_accesses_RunTimeTypeAccess.__init__)


def test_gast_accesses_runtimetypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_RunTimeTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_parameterinstantiationtypeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_ParameterInstantiationTypeAccess)


def test_gast_accesses_parameterinstantiationtypeaccess_constructor_exists():
    assert callable(gast_accesses_ParameterInstantiationTypeAccess.__init__)


def test_gast_accesses_parameterinstantiationtypeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_ParameterInstantiationTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_inheritancetypeaccess_is_not_abstract():
    assert not inspect.isabstract(InheritanceTypeAccess)


def test_inheritancetypeaccess_constructor_exists():
    assert callable(InheritanceTypeAccess.__init__)


def test_inheritancetypeaccess_constructor_args():
    sig = inspect.signature(InheritanceTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_destructor_is_not_abstract():
    assert not inspect.isabstract(Destructor)


def test_destructor_constructor_exists():
    assert callable(Destructor.__init__)


def test_destructor_constructor_args():
    sig = inspect.signature(Destructor.__init__)
    params = list(sig.parameters.keys())



def test_constructor_is_not_abstract():
    assert not inspect.isabstract(Constructor)


def test_constructor_constructor_exists():
    assert callable(Constructor.__init__)


def test_constructor_constructor_args():
    sig = inspect.signature(Constructor.__init__)
    params = list(sig.parameters.keys())



def test_types_gasttype_is_not_abstract():
    assert not inspect.isabstract(types_GASTType)


def test_types_gasttype_constructor_exists():
    assert callable(types_GASTType.__init__)


def test_types_gasttype_constructor_args():
    sig = inspect.signature(types_GASTType.__init__)
    params = list(sig.parameters.keys())



def test_core_genericentity_is_not_abstract():
    assert not inspect.isabstract(core_GenericEntity)


def test_core_genericentity_constructor_exists():
    assert callable(core_GenericEntity.__init__)


def test_core_genericentity_constructor_args():
    sig = inspect.signature(core_GenericEntity.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_genericconstructor_is_not_abstract():
    assert not inspect.isabstract(gast_functions_GenericConstructor)


def test_gast_functions_genericconstructor_constructor_exists():
    assert callable(gast_functions_GenericConstructor.__init__)


def test_gast_functions_genericconstructor_constructor_args():
    sig = inspect.signature(gast_functions_GenericConstructor.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_genericfunction_is_not_abstract():
    assert not inspect.isabstract(gast_functions_GenericFunction)


def test_gast_functions_genericfunction_constructor_exists():
    assert callable(gast_functions_GenericFunction.__init__)


def test_gast_functions_genericfunction_constructor_args():
    sig = inspect.signature(gast_functions_GenericFunction.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_genericmethod_is_not_abstract():
    assert not inspect.isabstract(gast_functions_GenericMethod)


def test_gast_functions_genericmethod_constructor_exists():
    assert callable(gast_functions_GenericMethod.__init__)


def test_gast_functions_genericmethod_constructor_args():
    sig = inspect.signature(gast_functions_GenericMethod.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_types_typedecorator_is_not_abstract():
    assert not inspect.isabstract(types_TypeDecorator)


def test_types_typedecorator_constructor_exists():
    assert callable(types_TypeDecorator.__init__)


def test_types_typedecorator_constructor_args():
    sig = inspect.signature(types_TypeDecorator.__init__)
    params = list(sig.parameters.keys())



def test_types_member_is_not_abstract():
    assert not inspect.isabstract(types_Member)


def test_types_member_constructor_exists():
    assert callable(types_Member.__init__)


def test_types_member_constructor_args():
    sig = inspect.signature(types_Member.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_constructor_is_not_abstract():
    assert not inspect.isabstract(gast_functions_Constructor)


def test_gast_functions_constructor_constructor_exists():
    assert callable(gast_functions_Constructor.__init__)


def test_gast_functions_constructor_constructor_args():
    sig = inspect.signature(gast_functions_Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "initializer" in params, "Missing parameter 'initializer'"

def test_gast_functions_constructor_has_initializer():
    assert hasattr(gast_functions_Constructor, "initializer")
    descriptor = None
    for klass in gast_functions_Constructor.__mro__:
        if "initializer" in klass.__dict__:
            descriptor = klass.__dict__["initializer"]
            break
    assert isinstance(descriptor, property)



def test_gast_functions_delegate_is_not_abstract():
    assert not inspect.isabstract(gast_functions_Delegate)


def test_gast_functions_delegate_constructor_exists():
    assert callable(gast_functions_Delegate.__init__)


def test_gast_functions_delegate_constructor_args():
    sig = inspect.signature(gast_functions_Delegate.__init__)
    params = list(sig.parameters.keys())
    assert "innerDelegate" in params, "Missing parameter 'innerDelegate'"

def test_gast_functions_delegate_has_innerDelegate():
    assert hasattr(gast_functions_Delegate, "innerDelegate")
    descriptor = None
    for klass in gast_functions_Delegate.__mro__:
        if "innerDelegate" in klass.__dict__:
            descriptor = klass.__dict__["innerDelegate"]
            break
    assert isinstance(descriptor, property)



def test_gast_variables_property_is_not_abstract():
    assert not inspect.isabstract(gast_variables_Property)


def test_gast_variables_property_constructor_exists():
    assert callable(gast_variables_Property.__init__)


def test_gast_variables_property_constructor_args():
    sig = inspect.signature(gast_variables_Property.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_gastclass_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTClass)


def test_gast_types_gastclass_constructor_exists():
    assert callable(gast_types_GASTClass.__init__)


def test_gast_types_gastclass_constructor_args():
    sig = inspect.signature(gast_types_GASTClass.__init__)
    params = list(sig.parameters.keys())
    assert "anonymous" in params, "Missing parameter 'anonymous'"
    assert "interface" in params, "Missing parameter 'interface'"
    assert "primitive" in params, "Missing parameter 'primitive'"
    assert "local" in params, "Missing parameter 'local'"
    assert "inner" in params, "Missing parameter 'inner'"
    assert "linesOfComments" in params, "Missing parameter 'linesOfComments'"

def test_gast_types_gastclass_has_anonymous():
    assert hasattr(gast_types_GASTClass, "anonymous")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "anonymous" in klass.__dict__:
            descriptor = klass.__dict__["anonymous"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gastclass_has_interface():
    assert hasattr(gast_types_GASTClass, "interface")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gastclass_has_primitive():
    assert hasattr(gast_types_GASTClass, "primitive")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gastclass_has_local():
    assert hasattr(gast_types_GASTClass, "local")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "local" in klass.__dict__:
            descriptor = klass.__dict__["local"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gastclass_has_inner():
    assert hasattr(gast_types_GASTClass, "inner")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gastclass_has_linesOfComments():
    assert hasattr(gast_types_GASTClass, "linesOfComments")
    descriptor = None
    for klass in gast_types_GASTClass.__mro__:
        if "linesOfComments" in klass.__dict__:
            descriptor = klass.__dict__["linesOfComments"]
            break
    assert isinstance(descriptor, property)



def test_gast_variables_field_is_not_abstract():
    assert not inspect.isabstract(gast_variables_Field)


def test_gast_variables_field_constructor_exists():
    assert callable(gast_variables_Field.__init__)


def test_gast_variables_field_constructor_args():
    sig = inspect.signature(gast_variables_Field.__init__)
    params = list(sig.parameters.keys())
    assert "propertyField" in params, "Missing parameter 'propertyField'"

def test_gast_variables_field_has_propertyField():
    assert hasattr(gast_variables_Field, "propertyField")
    descriptor = None
    for klass in gast_variables_Field.__mro__:
        if "propertyField" in klass.__dict__:
            descriptor = klass.__dict__["propertyField"]
            break
    assert isinstance(descriptor, property)



def test_gast_functions_destructor_is_not_abstract():
    assert not inspect.isabstract(gast_functions_Destructor)


def test_gast_functions_destructor_constructor_exists():
    assert callable(gast_functions_Destructor.__init__)


def test_gast_functions_destructor_constructor_args():
    sig = inspect.signature(gast_functions_Destructor.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_method_is_not_abstract():
    assert not inspect.isabstract(gast_functions_Method)


def test_gast_functions_method_constructor_exists():
    assert callable(gast_functions_Method.__init__)


def test_gast_functions_method_constructor_args():
    sig = inspect.signature(gast_functions_Method.__init__)
    params = list(sig.parameters.keys())
    assert "propertyMethod" in params, "Missing parameter 'propertyMethod'"

def test_gast_functions_method_has_propertyMethod():
    assert hasattr(gast_functions_Method, "propertyMethod")
    descriptor = None
    for klass in gast_functions_Method.__mro__:
        if "propertyMethod" in klass.__dict__:
            descriptor = klass.__dict__["propertyMethod"]
            break
    assert isinstance(descriptor, property)



def test_gast_types_typealias_is_not_abstract():
    assert not inspect.isabstract(gast_types_TypeAlias)


def test_gast_types_typealias_constructor_exists():
    assert callable(gast_types_TypeAlias.__init__)


def test_gast_types_typealias_constructor_args():
    sig = inspect.signature(gast_types_TypeAlias.__init__)
    params = list(sig.parameters.keys())
    assert "innerTypeAlias" in params, "Missing parameter 'innerTypeAlias'"

def test_gast_types_typealias_has_innerTypeAlias():
    assert hasattr(gast_types_TypeAlias, "innerTypeAlias")
    descriptor = None
    for klass in gast_types_TypeAlias.__mro__:
        if "innerTypeAlias" in klass.__dict__:
            descriptor = klass.__dict__["innerTypeAlias"]
            break
    assert isinstance(descriptor, property)



def test_typedecorator_is_not_abstract():
    assert not inspect.isabstract(TypeDecorator)


def test_typedecorator_constructor_exists():
    assert callable(TypeDecorator.__init__)


def test_typedecorator_constructor_args():
    sig = inspect.signature(TypeDecorator.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_gastarray_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTArray)


def test_gast_types_gastarray_constructor_exists():
    assert callable(gast_types_GASTArray.__init__)


def test_gast_types_gastarray_constructor_args():
    sig = inspect.signature(gast_types_GASTArray.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_gast_types_gastarray_has_dimensions():
    assert hasattr(gast_types_GASTArray, "dimensions")
    descriptor = None
    for klass in gast_types_GASTArray.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_gast_types_reference_is_not_abstract():
    assert not inspect.isabstract(gast_types_Reference)


def test_gast_types_reference_constructor_exists():
    assert callable(gast_types_Reference.__init__)


def test_gast_types_reference_constructor_args():
    sig = inspect.signature(gast_types_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "explicit" in params, "Missing parameter 'explicit'"

def test_gast_types_reference_has_explicit():
    assert hasattr(gast_types_Reference, "explicit")
    descriptor = None
    for klass in gast_types_Reference.__mro__:
        if "explicit" in klass.__dict__:
            descriptor = klass.__dict__["explicit"]
            break
    assert isinstance(descriptor, property)



def test_gast_annotations_modelannotation_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_ModelAnnotation)


def test_gast_annotations_modelannotation_constructor_exists():
    assert callable(gast_annotations_ModelAnnotation.__init__)


def test_gast_annotations_modelannotation_constructor_args():
    sig = inspect.signature(gast_annotations_ModelAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_core_sourceentity_is_not_abstract():
    assert not inspect.isabstract(core_SourceEntity)


def test_core_sourceentity_constructor_exists():
    assert callable(core_SourceEntity.__init__)


def test_core_sourceentity_constructor_args():
    sig = inspect.signature(core_SourceEntity.__init__)
    params = list(sig.parameters.keys())



def test_core_namedmodelelement_is_not_abstract():
    assert not inspect.isabstract(core_NamedModelElement)


def test_core_namedmodelelement_constructor_exists():
    assert callable(core_NamedModelElement.__init__)


def test_core_namedmodelelement_constructor_args():
    sig = inspect.signature(core_NamedModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_function_is_not_abstract():
    assert not inspect.isabstract(gast_functions_Function)


def test_gast_functions_function_constructor_exists():
    assert callable(gast_functions_Function.__init__)


def test_gast_functions_function_constructor_args():
    sig = inspect.signature(gast_functions_Function.__init__)
    params = list(sig.parameters.keys())
    assert "linesOfComments" in params, "Missing parameter 'linesOfComments'"
    assert "linesOfCode" in params, "Missing parameter 'linesOfCode'"
    assert "numberOfEdgesInCFG" in params, "Missing parameter 'numberOfEdgesInCFG'"
    assert "maximumNestingLevel" in params, "Missing parameter 'maximumNestingLevel'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "numberOfStatements" in params, "Missing parameter 'numberOfStatements'"
    assert "numberOfNodesInCFG" in params, "Missing parameter 'numberOfNodesInCFG'"

def test_gast_functions_function_has_linesOfComments():
    assert hasattr(gast_functions_Function, "linesOfComments")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "linesOfComments" in klass.__dict__:
            descriptor = klass.__dict__["linesOfComments"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_linesOfCode():
    assert hasattr(gast_functions_Function, "linesOfCode")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "linesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["linesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_numberOfEdgesInCFG():
    assert hasattr(gast_functions_Function, "numberOfEdgesInCFG")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "numberOfEdgesInCFG" in klass.__dict__:
            descriptor = klass.__dict__["numberOfEdgesInCFG"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_maximumNestingLevel():
    assert hasattr(gast_functions_Function, "maximumNestingLevel")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "maximumNestingLevel" in klass.__dict__:
            descriptor = klass.__dict__["maximumNestingLevel"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_operator():
    assert hasattr(gast_functions_Function, "operator")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_numberOfStatements():
    assert hasattr(gast_functions_Function, "numberOfStatements")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "numberOfStatements" in klass.__dict__:
            descriptor = klass.__dict__["numberOfStatements"]
            break
    assert isinstance(descriptor, property)

def test_gast_functions_function_has_numberOfNodesInCFG():
    assert hasattr(gast_functions_Function, "numberOfNodesInCFG")
    descriptor = None
    for klass in gast_functions_Function.__mro__:
        if "numberOfNodesInCFG" in klass.__dict__:
            descriptor = klass.__dict__["numberOfNodesInCFG"]
            break
    assert isinstance(descriptor, property)



def test_gast_variables_variable_is_not_abstract():
    assert not inspect.isabstract(gast_variables_Variable)


def test_gast_variables_variable_constructor_exists():
    assert callable(gast_variables_Variable.__init__)


def test_gast_variables_variable_constructor_args():
    sig = inspect.signature(gast_variables_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"

def test_gast_variables_variable_has_const():
    assert hasattr(gast_variables_Variable, "const")
    descriptor = None
    for klass in gast_variables_Variable.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_core_modelelement_is_not_abstract():
    assert not inspect.isabstract(core_ModelElement)


def test_core_modelelement_constructor_exists():
    assert callable(core_ModelElement.__init__)


def test_core_modelelement_constructor_args():
    sig = inspect.signature(core_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_annotations_modelannotation_is_not_abstract():
    assert not inspect.isabstract(annotations_ModelAnnotation)


def test_annotations_modelannotation_constructor_exists():
    assert callable(annotations_ModelAnnotation.__init__)


def test_annotations_modelannotation_constructor_args():
    sig = inspect.signature(annotations_ModelAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_clone_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_Clone)


def test_gast_annotations_clone_constructor_exists():
    assert callable(gast_annotations_Clone.__init__)


def test_gast_annotations_clone_constructor_args():
    sig = inspect.signature(gast_annotations_Clone.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_structuralabstraction_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_StructuralAbstraction)


def test_gast_annotations_structuralabstraction_constructor_exists():
    assert callable(gast_annotations_StructuralAbstraction.__init__)


def test_gast_annotations_structuralabstraction_constructor_args():
    sig = inspect.signature(gast_annotations_StructuralAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_cloneinstance_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_CloneInstance)


def test_gast_annotations_cloneinstance_constructor_exists():
    assert callable(gast_annotations_CloneInstance.__init__)


def test_gast_annotations_cloneinstance_constructor_args():
    sig = inspect.signature(gast_annotations_CloneInstance.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_comment_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_Comment)


def test_gast_annotations_comment_constructor_exists():
    assert callable(gast_annotations_Comment.__init__)


def test_gast_annotations_comment_constructor_args():
    sig = inspect.signature(gast_annotations_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "texts" in params, "Missing parameter 'texts'"
    assert "todo" in params, "Missing parameter 'todo'"
    assert "todoCount" in params, "Missing parameter 'todoCount'"
    assert "formal" in params, "Missing parameter 'formal'"

def test_gast_annotations_comment_has_texts():
    assert hasattr(gast_annotations_Comment, "texts")
    descriptor = None
    for klass in gast_annotations_Comment.__mro__:
        if "texts" in klass.__dict__:
            descriptor = klass.__dict__["texts"]
            break
    assert isinstance(descriptor, property)

def test_gast_annotations_comment_has_todo():
    assert hasattr(gast_annotations_Comment, "todo")
    descriptor = None
    for klass in gast_annotations_Comment.__mro__:
        if "todo" in klass.__dict__:
            descriptor = klass.__dict__["todo"]
            break
    assert isinstance(descriptor, property)

def test_gast_annotations_comment_has_todoCount():
    assert hasattr(gast_annotations_Comment, "todoCount")
    descriptor = None
    for klass in gast_annotations_Comment.__mro__:
        if "todoCount" in klass.__dict__:
            descriptor = klass.__dict__["todoCount"]
            break
    assert isinstance(descriptor, property)

def test_gast_annotations_comment_has_formal():
    assert hasattr(gast_annotations_Comment, "formal")
    descriptor = None
    for klass in gast_annotations_Comment.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_types_gastclass_is_not_abstract():
    assert not inspect.isabstract(types_GASTClass)


def test_types_gastclass_constructor_exists():
    assert callable(types_GASTClass.__init__)


def test_types_gastclass_constructor_args():
    sig = inspect.signature(types_GASTClass.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_genericclass_is_not_abstract():
    assert not inspect.isabstract(gast_types_GenericClass)


def test_gast_types_genericclass_constructor_exists():
    assert callable(gast_types_GenericClass.__init__)


def test_gast_types_genericclass_constructor_args():
    sig = inspect.signature(gast_types_GenericClass.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_attribute_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_Attribute)


def test_gast_annotations_attribute_constructor_exists():
    assert callable(gast_annotations_Attribute.__init__)


def test_gast_annotations_attribute_constructor_args():
    sig = inspect.signature(gast_annotations_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_position_is_not_abstract():
    assert not inspect.isabstract(gast_core_Position)


def test_gast_core_position_constructor_exists():
    assert callable(gast_core_Position.__init__)


def test_gast_core_position_constructor_args():
    sig = inspect.signature(gast_core_Position.__init__)
    params = list(sig.parameters.keys())
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"

def test_gast_core_position_has_startLine():
    assert hasattr(gast_core_Position, "startLine")
    descriptor = None
    for klass in gast_core_Position.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_position_has_endColumn():
    assert hasattr(gast_core_Position, "endColumn")
    descriptor = None
    for klass in gast_core_Position.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_position_has_endLine():
    assert hasattr(gast_core_Position, "endLine")
    descriptor = None
    for klass in gast_core_Position.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_position_has_startColumn():
    assert hasattr(gast_core_Position, "startColumn")
    descriptor = None
    for klass in gast_core_Position.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())



def test_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_file_constructor_exists():
    assert callable(File.__init__)


def test_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_basepath_is_not_abstract():
    assert not inspect.isabstract(BasePath)


def test_basepath_constructor_exists():
    assert callable(BasePath.__init__)


def test_basepath_constructor_args():
    sig = inspect.signature(BasePath.__init__)
    params = list(sig.parameters.keys())



def test_gasttype_is_not_abstract():
    assert not inspect.isabstract(GASTType)


def test_gasttype_constructor_exists():
    assert callable(GASTType.__init__)


def test_gasttype_constructor_args():
    sig = inspect.signature(GASTType.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_typedecorator_is_not_abstract():
    assert not inspect.isabstract(gast_types_TypeDecorator)


def test_gast_types_typedecorator_constructor_exists():
    assert callable(gast_types_TypeDecorator.__init__)


def test_gast_types_typedecorator_constructor_args():
    sig = inspect.signature(gast_types_TypeDecorator.__init__)
    params = list(sig.parameters.keys())



def test_structuralabstraction_is_not_abstract():
    assert not inspect.isabstract(StructuralAbstraction)


def test_structuralabstraction_constructor_exists():
    assert callable(StructuralAbstraction.__init__)


def test_structuralabstraction_constructor_args():
    sig = inspect.signature(StructuralAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_subsystem_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_Subsystem)


def test_gast_annotations_subsystem_constructor_exists():
    assert callable(gast_annotations_Subsystem.__init__)


def test_gast_annotations_subsystem_constructor_args():
    sig = inspect.signature(gast_annotations_Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_gast_annotations_layer_is_not_abstract():
    assert not inspect.isabstract(gast_annotations_Layer)


def test_gast_annotations_layer_constructor_exists():
    assert callable(gast_annotations_Layer.__init__)


def test_gast_annotations_layer_constructor_args():
    sig = inspect.signature(gast_annotations_Layer.__init__)
    params = list(sig.parameters.keys())



def test_clone_is_not_abstract():
    assert not inspect.isabstract(Clone)


def test_clone_constructor_exists():
    assert callable(Clone.__init__)


def test_clone_constructor_args():
    sig = inspect.signature(Clone.__init__)
    params = list(sig.parameters.keys())



def test_typeparameterclass_is_not_abstract():
    assert not inspect.isabstract(TypeParameterClass)


def test_typeparameterclass_constructor_exists():
    assert callable(TypeParameterClass.__init__)


def test_typeparameterclass_constructor_args():
    sig = inspect.signature(TypeParameterClass.__init__)
    params = list(sig.parameters.keys())



def test_typealias_is_not_abstract():
    assert not inspect.isabstract(TypeAlias)


def test_typealias_constructor_exists():
    assert callable(TypeAlias.__init__)


def test_typealias_constructor_args():
    sig = inspect.signature(TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_packagealias_is_not_abstract():
    assert not inspect.isabstract(gast_core_PackageAlias)


def test_gast_core_packagealias_constructor_exists():
    assert callable(gast_core_PackageAlias.__init__)


def test_gast_core_packagealias_constructor_args():
    sig = inspect.signature(gast_core_PackageAlias.__init__)
    params = list(sig.parameters.keys())



def test_globalvariable_is_not_abstract():
    assert not inspect.isabstract(GlobalVariable)


def test_globalvariable_constructor_exists():
    assert callable(GlobalVariable.__init__)


def test_globalvariable_constructor_args():
    sig = inspect.signature(GlobalVariable.__init__)
    params = list(sig.parameters.keys())



def test_delegate_is_not_abstract():
    assert not inspect.isabstract(Delegate)


def test_delegate_constructor_exists():
    assert callable(Delegate.__init__)


def test_delegate_constructor_args():
    sig = inspect.signature(Delegate.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_typeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_TypeAccess)


def test_gast_accesses_typeaccess_constructor_exists():
    assert callable(gast_accesses_TypeAccess.__init__)


def test_gast_accesses_typeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_functionaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_FunctionAccess)


def test_gast_accesses_functionaccess_constructor_exists():
    assert callable(gast_accesses_FunctionAccess.__init__)


def test_gast_accesses_functionaccess_constructor_args():
    sig = inspect.signature(gast_accesses_FunctionAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_variableaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_VariableAccess)


def test_gast_accesses_variableaccess_constructor_exists():
    assert callable(gast_accesses_VariableAccess.__init__)


def test_gast_accesses_variableaccess_constructor_args():
    sig = inspect.signature(gast_accesses_VariableAccess.__init__)
    params = list(sig.parameters.keys())
    assert "write" in params, "Missing parameter 'write'"

def test_gast_accesses_variableaccess_has_write():
    assert hasattr(gast_accesses_VariableAccess, "write")
    descriptor = None
    for klass in gast_accesses_VariableAccess.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)



def test_gastclass_is_not_abstract():
    assert not inspect.isabstract(GASTClass)


def test_gastclass_constructor_exists():
    assert callable(GASTClass.__init__)


def test_gastclass_constructor_args():
    sig = inspect.signature(GASTClass.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_gastenumeration_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTEnumeration)


def test_gast_types_gastenumeration_constructor_exists():
    assert callable(gast_types_GASTEnumeration.__init__)


def test_gast_types_gastenumeration_constructor_args():
    sig = inspect.signature(gast_types_GASTEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_gastunion_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTUnion)


def test_gast_types_gastunion_constructor_exists():
    assert callable(gast_types_GASTUnion.__init__)


def test_gast_types_gastunion_constructor_args():
    sig = inspect.signature(gast_types_GASTUnion.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_typeparameterclass_is_not_abstract():
    assert not inspect.isabstract(gast_types_TypeParameterClass)


def test_gast_types_typeparameterclass_constructor_exists():
    assert callable(gast_types_TypeParameterClass.__init__)


def test_gast_types_typeparameterclass_constructor_args():
    sig = inspect.signature(gast_types_TypeParameterClass.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_gaststruct_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTStruct)


def test_gast_types_gaststruct_constructor_exists():
    assert callable(gast_types_GASTStruct.__init__)


def test_gast_types_gaststruct_constructor_args():
    sig = inspect.signature(gast_types_GASTStruct.__init__)
    params = list(sig.parameters.keys())



def test_namedmodelelement_is_not_abstract():
    assert not inspect.isabstract(NamedModelElement)


def test_namedmodelelement_constructor_exists():
    assert callable(NamedModelElement.__init__)


def test_namedmodelelement_constructor_args():
    sig = inspect.signature(NamedModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_directory_is_not_abstract():
    assert not inspect.isabstract(gast_core_Directory)


def test_gast_core_directory_constructor_exists():
    assert callable(gast_core_Directory.__init__)


def test_gast_core_directory_constructor_args():
    sig = inspect.signature(gast_core_Directory.__init__)
    params = list(sig.parameters.keys())
    assert "fullQualifiedPath" in params, "Missing parameter 'fullQualifiedPath'"
    assert "fileSystemPath" in params, "Missing parameter 'fileSystemPath'"

def test_gast_core_directory_has_fullQualifiedPath():
    assert hasattr(gast_core_Directory, "fullQualifiedPath")
    descriptor = None
    for klass in gast_core_Directory.__mro__:
        if "fullQualifiedPath" in klass.__dict__:
            descriptor = klass.__dict__["fullQualifiedPath"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_directory_has_fileSystemPath():
    assert hasattr(gast_core_Directory, "fileSystemPath")
    descriptor = None
    for klass in gast_core_Directory.__mro__:
        if "fileSystemPath" in klass.__dict__:
            descriptor = klass.__dict__["fileSystemPath"]
            break
    assert isinstance(descriptor, property)



def test_gast_types_gasttype_is_not_abstract():
    assert not inspect.isabstract(gast_types_GASTType)


def test_gast_types_gasttype_constructor_exists():
    assert callable(gast_types_GASTType.__init__)


def test_gast_types_gasttype_constructor_args():
    sig = inspect.signature(gast_types_GASTType.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "referenceType" in params, "Missing parameter 'referenceType'"

def test_gast_types_gasttype_has_qualifiedName():
    assert hasattr(gast_types_GASTType, "qualifiedName")
    descriptor = None
    for klass in gast_types_GASTType.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_gasttype_has_referenceType():
    assert hasattr(gast_types_GASTType, "referenceType")
    descriptor = None
    for klass in gast_types_GASTType.__mro__:
        if "referenceType" in klass.__dict__:
            descriptor = klass.__dict__["referenceType"]
            break
    assert isinstance(descriptor, property)



def test_gast_core_file_is_not_abstract():
    assert not inspect.isabstract(gast_core_File)


def test_gast_core_file_constructor_exists():
    assert callable(gast_core_File.__init__)


def test_gast_core_file_constructor_args():
    sig = inspect.signature(gast_core_File.__init__)
    params = list(sig.parameters.keys())
    assert "assemblyFile" in params, "Missing parameter 'assemblyFile'"
    assert "linesOfCode" in params, "Missing parameter 'linesOfCode'"
    assert "fileSystemPath" in params, "Missing parameter 'fileSystemPath'"
    assert "size" in params, "Missing parameter 'size'"
    assert "sourceFile" in params, "Missing parameter 'sourceFile'"
    assert "fullQualifiedPath" in params, "Missing parameter 'fullQualifiedPath'"

def test_gast_core_file_has_assemblyFile():
    assert hasattr(gast_core_File, "assemblyFile")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "assemblyFile" in klass.__dict__:
            descriptor = klass.__dict__["assemblyFile"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_file_has_linesOfCode():
    assert hasattr(gast_core_File, "linesOfCode")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "linesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["linesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_file_has_fileSystemPath():
    assert hasattr(gast_core_File, "fileSystemPath")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "fileSystemPath" in klass.__dict__:
            descriptor = klass.__dict__["fileSystemPath"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_file_has_size():
    assert hasattr(gast_core_File, "size")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_file_has_sourceFile():
    assert hasattr(gast_core_File, "sourceFile")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "sourceFile" in klass.__dict__:
            descriptor = klass.__dict__["sourceFile"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_file_has_fullQualifiedPath():
    assert hasattr(gast_core_File, "fullQualifiedPath")
    descriptor = None
    for klass in gast_core_File.__mro__:
        if "fullQualifiedPath" in klass.__dict__:
            descriptor = klass.__dict__["fullQualifiedPath"]
            break
    assert isinstance(descriptor, property)



def test_gast_core_package_is_not_abstract():
    assert not inspect.isabstract(gast_core_Package)


def test_gast_core_package_constructor_exists():
    assert callable(gast_core_Package.__init__)


def test_gast_core_package_constructor_args():
    sig = inspect.signature(gast_core_Package.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "linesOfCode" in params, "Missing parameter 'linesOfCode'"
    assert "linesOfComments" in params, "Missing parameter 'linesOfComments'"

def test_gast_core_package_has_qualifiedName():
    assert hasattr(gast_core_Package, "qualifiedName")
    descriptor = None
    for klass in gast_core_Package.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_package_has_linesOfCode():
    assert hasattr(gast_core_Package, "linesOfCode")
    descriptor = None
    for klass in gast_core_Package.__mro__:
        if "linesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["linesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_package_has_linesOfComments():
    assert hasattr(gast_core_Package, "linesOfComments")
    descriptor = None
    for klass in gast_core_Package.__mro__:
        if "linesOfComments" in klass.__dict__:
            descriptor = klass.__dict__["linesOfComments"]
            break
    assert isinstance(descriptor, property)



def test_gast_core_identifier_is_not_abstract():
    assert not inspect.isabstract(gast_core_Identifier)


def test_gast_core_identifier_constructor_exists():
    assert callable(gast_core_Identifier.__init__)


def test_gast_core_identifier_constructor_args():
    sig = inspect.signature(gast_core_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_gast_core_identifier_has_id():
    assert hasattr(gast_core_Identifier, "id")
    descriptor = None
    for klass in gast_core_Identifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_modelannotation_is_not_abstract():
    assert not inspect.isabstract(ModelAnnotation)


def test_modelannotation_constructor_exists():
    assert callable(ModelAnnotation.__init__)


def test_modelannotation_constructor_args():
    sig = inspect.signature(ModelAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_globalfunction_is_not_abstract():
    assert not inspect.isabstract(GlobalFunction)


def test_globalfunction_constructor_exists():
    assert callable(GlobalFunction.__init__)


def test_globalfunction_constructor_args():
    sig = inspect.signature(GlobalFunction.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_modelelement_is_not_abstract():
    assert not inspect.isabstract(gast_core_ModelElement)


def test_gast_core_modelelement_constructor_exists():
    assert callable(gast_core_ModelElement.__init__)


def test_gast_core_modelelement_constructor_args():
    sig = inspect.signature(gast_core_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "sissyId" in params, "Missing parameter 'sissyId'"

def test_gast_core_modelelement_has_status():
    assert hasattr(gast_core_ModelElement, "status")
    descriptor = None
    for klass in gast_core_ModelElement.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_modelelement_has_sissyId():
    assert hasattr(gast_core_ModelElement, "sissyId")
    descriptor = None
    for klass in gast_core_ModelElement.__mro__:
        if "sissyId" in klass.__dict__:
            descriptor = klass.__dict__["sissyId"]
            break
    assert isinstance(descriptor, property)



def test_directory_is_not_abstract():
    assert not inspect.isabstract(Directory)


def test_directory_constructor_exists():
    assert callable(Directory.__init__)


def test_directory_constructor_args():
    sig = inspect.signature(Directory.__init__)
    params = list(sig.parameters.keys())



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_root_is_not_abstract():
    assert not inspect.isabstract(gast_core_Root)


def test_gast_core_root_constructor_exists():
    assert callable(gast_core_Root.__init__)


def test_gast_core_root_constructor_args():
    sig = inspect.signature(gast_core_Root.__init__)
    params = list(sig.parameters.keys())
    assert "linesOfCode" in params, "Missing parameter 'linesOfCode'"
    assert "linesOfComments" in params, "Missing parameter 'linesOfComments'"

def test_gast_core_root_has_linesOfCode():
    assert hasattr(gast_core_Root, "linesOfCode")
    descriptor = None
    for klass in gast_core_Root.__mro__:
        if "linesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["linesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_gast_core_root_has_linesOfComments():
    assert hasattr(gast_core_Root, "linesOfComments")
    descriptor = None
    for klass in gast_core_Root.__mro__:
        if "linesOfComments" in klass.__dict__:
            descriptor = klass.__dict__["linesOfComments"]
            break
    assert isinstance(descriptor, property)



def test_gast_core_namedmodelelement_is_not_abstract():
    assert not inspect.isabstract(gast_core_NamedModelElement)


def test_gast_core_namedmodelelement_constructor_exists():
    assert callable(gast_core_NamedModelElement.__init__)


def test_gast_core_namedmodelelement_constructor_args():
    sig = inspect.signature(gast_core_NamedModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_gast_core_namedmodelelement_has_simpleName():
    assert hasattr(gast_core_NamedModelElement, "simpleName")
    descriptor = None
    for klass in gast_core_NamedModelElement.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_gast_core_sourceentity_is_not_abstract():
    assert not inspect.isabstract(gast_core_SourceEntity)


def test_gast_core_sourceentity_constructor_exists():
    assert callable(gast_core_SourceEntity.__init__)


def test_gast_core_sourceentity_constructor_args():
    sig = inspect.signature(gast_core_SourceEntity.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_genericentity_is_not_abstract():
    assert not inspect.isabstract(gast_core_GenericEntity)


def test_gast_core_genericentity_constructor_exists():
    assert callable(gast_core_GenericEntity.__init__)


def test_gast_core_genericentity_constructor_args():
    sig = inspect.signature(gast_core_GenericEntity.__init__)
    params = list(sig.parameters.keys())



def test_gast_core_basepath_is_not_abstract():
    assert not inspect.isabstract(gast_core_BasePath)


def test_gast_core_basepath_constructor_exists():
    assert callable(gast_core_BasePath.__init__)


def test_gast_core_basepath_constructor_args():
    sig = inspect.signature(gast_core_BasePath.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_gast_core_basepath_has_path():
    assert hasattr(gast_core_BasePath, "path")
    descriptor = None
    for klass in gast_core_BasePath.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_gast_statements_gastbehaviour_is_not_abstract():
    assert not inspect.isabstract(gast_statements_GASTBehaviour)


def test_gast_statements_gastbehaviour_constructor_exists():
    assert callable(gast_statements_GASTBehaviour.__init__)


def test_gast_statements_gastbehaviour_constructor_args():
    sig = inspect.signature(gast_statements_GASTBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_catchparameter_is_not_abstract():
    assert not inspect.isabstract(CatchParameter)


def test_catchparameter_constructor_exists():
    assert callable(CatchParameter.__init__)


def test_catchparameter_constructor_args():
    sig = inspect.signature(CatchParameter.__init__)
    params = list(sig.parameters.keys())



def test_branchstatement_is_not_abstract():
    assert not inspect.isabstract(BranchStatement)


def test_branchstatement_constructor_exists():
    assert callable(BranchStatement.__init__)


def test_branchstatement_constructor_args():
    sig = inspect.signature(BranchStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastexpression_is_not_abstract():
    assert not inspect.isabstract(GASTExpression)


def test_gastexpression_constructor_exists():
    assert callable(GASTExpression.__init__)


def test_gastexpression_constructor_args():
    sig = inspect.signature(GASTExpression.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_gast_functions_globalfunction_is_not_abstract():
    assert not inspect.isabstract(gast_functions_GlobalFunction)


def test_gast_functions_globalfunction_constructor_exists():
    assert callable(gast_functions_GlobalFunction.__init__)


def test_gast_functions_globalfunction_constructor_args():
    sig = inspect.signature(gast_functions_GlobalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_gast_functions_globalfunction_has_kind():
    assert hasattr(gast_functions_GlobalFunction, "kind")
    descriptor = None
    for klass in gast_functions_GlobalFunction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())



def test_cloneinstance_is_not_abstract():
    assert not inspect.isabstract(CloneInstance)


def test_cloneinstance_constructor_exists():
    assert callable(CloneInstance.__init__)


def test_cloneinstance_constructor_args():
    sig = inspect.signature(CloneInstance.__init__)
    params = list(sig.parameters.keys())



def test_baseaccess_is_not_abstract():
    assert not inspect.isabstract(BaseAccess)


def test_baseaccess_constructor_exists():
    assert callable(BaseAccess.__init__)


def test_baseaccess_constructor_args():
    sig = inspect.signature(BaseAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_compositeaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_CompositeAccess)


def test_gast_accesses_compositeaccess_constructor_exists():
    assert callable(gast_accesses_CompositeAccess.__init__)


def test_gast_accesses_compositeaccess_constructor_args():
    sig = inspect.signature(gast_accesses_CompositeAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_access_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_Access)


def test_gast_accesses_access_constructor_exists():
    assert callable(gast_accesses_Access.__init__)


def test_gast_accesses_access_constructor_args():
    sig = inspect.signature(gast_accesses_Access.__init__)
    params = list(sig.parameters.keys())



def test_sourceentity_is_not_abstract():
    assert not inspect.isabstract(SourceEntity)


def test_sourceentity_constructor_exists():
    assert callable(SourceEntity.__init__)


def test_sourceentity_constructor_args():
    sig = inspect.signature(SourceEntity.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_branch_is_not_abstract():
    assert not inspect.isabstract(gast_statements_Branch)


def test_gast_statements_branch_constructor_exists():
    assert callable(gast_statements_Branch.__init__)


def test_gast_statements_branch_constructor_args():
    sig = inspect.signature(gast_statements_Branch.__init__)
    params = list(sig.parameters.keys())



def test_gast_accesses_baseaccess_is_not_abstract():
    assert not inspect.isabstract(gast_accesses_BaseAccess)


def test_gast_accesses_baseaccess_constructor_exists():
    assert callable(gast_accesses_BaseAccess.__init__)


def test_gast_accesses_baseaccess_constructor_args():
    sig = inspect.signature(gast_accesses_BaseAccess.__init__)
    params = list(sig.parameters.keys())



def test_gast_types_member_is_not_abstract():
    assert not inspect.isabstract(gast_types_Member)


def test_gast_types_member_constructor_exists():
    assert callable(gast_types_Member.__init__)


def test_gast_types_member_constructor_args():
    sig = inspect.signature(gast_types_Member.__init__)
    params = list(sig.parameters.keys())
    assert "extern" in params, "Missing parameter 'extern'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "introspectable" in params, "Missing parameter 'introspectable'"
    assert "internal" in params, "Missing parameter 'internal'"
    assert "final" in params, "Missing parameter 'final'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "virtual" in params, "Missing parameter 'virtual'"
    assert "override" in params, "Missing parameter 'override'"
    assert "typeParameterClassMember" in params, "Missing parameter 'typeParameterClassMember'"

def test_gast_types_member_has_extern():
    assert hasattr(gast_types_Member, "extern")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_abstract():
    assert hasattr(gast_types_Member, "abstract")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_static():
    assert hasattr(gast_types_Member, "static")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_introspectable():
    assert hasattr(gast_types_Member, "introspectable")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "introspectable" in klass.__dict__:
            descriptor = klass.__dict__["introspectable"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_internal():
    assert hasattr(gast_types_Member, "internal")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "internal" in klass.__dict__:
            descriptor = klass.__dict__["internal"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_final():
    assert hasattr(gast_types_Member, "final")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_visibility():
    assert hasattr(gast_types_Member, "visibility")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_virtual():
    assert hasattr(gast_types_Member, "virtual")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "virtual" in klass.__dict__:
            descriptor = klass.__dict__["virtual"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_override():
    assert hasattr(gast_types_Member, "override")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "override" in klass.__dict__:
            descriptor = klass.__dict__["override"]
            break
    assert isinstance(descriptor, property)

def test_gast_types_member_has_typeParameterClassMember():
    assert hasattr(gast_types_Member, "typeParameterClassMember")
    descriptor = None
    for klass in gast_types_Member.__mro__:
        if "typeParameterClassMember" in klass.__dict__:
            descriptor = klass.__dict__["typeParameterClassMember"]
            break
    assert isinstance(descriptor, property)



def test_gast_statements_gastexpression_is_not_abstract():
    assert not inspect.isabstract(gast_statements_GASTExpression)


def test_gast_statements_gastexpression_constructor_exists():
    assert callable(gast_statements_GASTExpression.__init__)


def test_gast_statements_gastexpression_constructor_args():
    sig = inspect.signature(gast_statements_GASTExpression.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_statement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_Statement)


def test_gast_statements_statement_constructor_exists():
    assert callable(gast_statements_Statement.__init__)


def test_gast_statements_statement_constructor_args():
    sig = inspect.signature(gast_statements_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "maximumNestingLevel" in params, "Missing parameter 'maximumNestingLevel'"
    assert "numberOfNodesInCFG" in params, "Missing parameter 'numberOfNodesInCFG'"
    assert "numberOfComments" in params, "Missing parameter 'numberOfComments'"
    assert "numberOfStatements" in params, "Missing parameter 'numberOfStatements'"
    assert "numberOfEdgesInCFG" in params, "Missing parameter 'numberOfEdgesInCFG'"
    assert "linesOfCode" in params, "Missing parameter 'linesOfCode'"

def test_gast_statements_statement_has_maximumNestingLevel():
    assert hasattr(gast_statements_Statement, "maximumNestingLevel")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "maximumNestingLevel" in klass.__dict__:
            descriptor = klass.__dict__["maximumNestingLevel"]
            break
    assert isinstance(descriptor, property)

def test_gast_statements_statement_has_numberOfNodesInCFG():
    assert hasattr(gast_statements_Statement, "numberOfNodesInCFG")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "numberOfNodesInCFG" in klass.__dict__:
            descriptor = klass.__dict__["numberOfNodesInCFG"]
            break
    assert isinstance(descriptor, property)

def test_gast_statements_statement_has_numberOfComments():
    assert hasattr(gast_statements_Statement, "numberOfComments")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "numberOfComments" in klass.__dict__:
            descriptor = klass.__dict__["numberOfComments"]
            break
    assert isinstance(descriptor, property)

def test_gast_statements_statement_has_numberOfStatements():
    assert hasattr(gast_statements_Statement, "numberOfStatements")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "numberOfStatements" in klass.__dict__:
            descriptor = klass.__dict__["numberOfStatements"]
            break
    assert isinstance(descriptor, property)

def test_gast_statements_statement_has_numberOfEdgesInCFG():
    assert hasattr(gast_statements_Statement, "numberOfEdgesInCFG")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "numberOfEdgesInCFG" in klass.__dict__:
            descriptor = klass.__dict__["numberOfEdgesInCFG"]
            break
    assert isinstance(descriptor, property)

def test_gast_statements_statement_has_linesOfCode():
    assert hasattr(gast_statements_Statement, "linesOfCode")
    descriptor = None
    for klass in gast_statements_Statement.__mro__:
        if "linesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["linesOfCode"]
            break
    assert isinstance(descriptor, property)



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_catchblock_is_not_abstract():
    assert not inspect.isabstract(gast_statements_CatchBlock)


def test_gast_statements_catchblock_constructor_exists():
    assert callable(gast_statements_CatchBlock.__init__)


def test_gast_statements_catchblock_constructor_args():
    sig = inspect.signature(gast_statements_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_JumpStatement)


def test_gast_statements_jumpstatement_constructor_exists():
    assert callable(gast_statements_JumpStatement.__init__)


def test_gast_statements_jumpstatement_constructor_args():
    sig = inspect.signature(gast_statements_JumpStatement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_gast_statements_jumpstatement_has_kind():
    assert hasattr(gast_statements_JumpStatement, "kind")
    descriptor = None
    for klass in gast_statements_JumpStatement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_gast_statements_branchstatement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_BranchStatement)


def test_gast_statements_branchstatement_constructor_exists():
    assert callable(gast_statements_BranchStatement.__init__)


def test_gast_statements_branchstatement_constructor_args():
    sig = inspect.signature(gast_statements_BranchStatement.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_loopstatement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_LoopStatement)


def test_gast_statements_loopstatement_constructor_exists():
    assert callable(gast_statements_LoopStatement.__init__)


def test_gast_statements_loopstatement_constructor_args():
    sig = inspect.signature(gast_statements_LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_gast_statements_loopstatement_has_kind():
    assert hasattr(gast_statements_LoopStatement, "kind")
    descriptor = None
    for klass in gast_statements_LoopStatement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_gast_statements_blockstatement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_BlockStatement)


def test_gast_statements_blockstatement_constructor_exists():
    assert callable(gast_statements_BlockStatement.__init__)


def test_gast_statements_blockstatement_constructor_args():
    sig = inspect.signature(gast_statements_BlockStatement.__init__)
    params = list(sig.parameters.keys())
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_gast_statements_blockstatement_has_synchronized():
    assert hasattr(gast_statements_BlockStatement, "synchronized")
    descriptor = None
    for klass in gast_statements_BlockStatement.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_gast_statements_simplestatement_is_not_abstract():
    assert not inspect.isabstract(gast_statements_SimpleStatement)


def test_gast_statements_simplestatement_constructor_exists():
    assert callable(gast_statements_SimpleStatement.__init__)


def test_gast_statements_simplestatement_constructor_args():
    sig = inspect.signature(gast_statements_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_gast_statements_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(gast_statements_ExceptionHandler)


def test_gast_statements_exceptionhandler_constructor_exists():
    assert callable(gast_statements_ExceptionHandler.__init__)


def test_gast_statements_exceptionhandler_constructor_args():
    sig = inspect.signature(gast_statements_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "LIBRARY",
        "IMPLICIT",
        "NORMAL",
        "FAILEDDEP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_globalfunctionkind_exists():
    # Check that the Enumeration exists
    assert GlobalFunctionKind is not None

def test_globalfunctionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GlobalFunctionKind]
    expected_literals = [
        "NORMAL",
        "UNITFINALIZER",
        "UNITINITIALIZER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GlobalFunctionKind"

def test_jumpstatementkind_exists():
    # Check that the Enumeration exists
    assert JumpStatementKind is not None

def test_jumpstatementkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpStatementKind]
    expected_literals = [
        "THROW",
        "JUMP",
        "RETURN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpStatementKind"

def test_visibilities_exists():
    # Check that the Enumeration exists
    assert Visibilities is not None

def test_visibilities_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibilities]
    expected_literals = [
        "VISIBILITYSTRICTPROTECTED",
        "VISIBILITYPRIVAT",
        "VISIBILITYPACKAGE",
        "VISIBILITYPROTECTED",
        "VISIBILITYPUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibilities"

def test_loopstatementkind_exists():
    # Check that the Enumeration exists
    assert LoopStatementKind is not None

def test_loopstatementkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoopStatementKind]
    expected_literals = [
        "FOREACH",
        "DOWHILE",
        "FOR",
        "WHILE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoopStatementKind"


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
variables_Field_strategy = st.builds(
    variables_Field,
)
variables_Variable_strategy = st.builds(
    variables_Variable,
)
ThrowTypeAccess_strategy = st.builds(
    ThrowTypeAccess,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
FormalParameter_strategy = st.builds(
    FormalParameter,
)
DeclarationTypeAccess_strategy = st.builds(
    DeclarationTypeAccess,
)
functions_Constructor_strategy = st.builds(
    functions_Constructor,
)
functions_Method_strategy = st.builds(
    functions_Method,
)
functions_GlobalFunction_strategy = st.builds(
    functions_GlobalFunction,
)
functions_Function_strategy = st.builds(
    functions_Function,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
gast_accesses_PropertyAccess_strategy = st.builds(
    gast_accesses_PropertyAccess,
)
gast_accesses_SelfAccess_strategy = st.builds(
    gast_accesses_SelfAccess,
    super=
        st.booleans()
)
FunctionAccess_strategy = st.builds(
    FunctionAccess,
)
gast_accesses_DelegateAccess_strategy = st.builds(
    gast_accesses_DelegateAccess,
)
Variable_strategy = st.builds(
    Variable,
)
gast_variables_GlobalVariable_strategy = st.builds(
    gast_variables_GlobalVariable,
)
gast_variables_CatchParameter_strategy = st.builds(
    gast_variables_CatchParameter,
    rethrown=
        st.booleans()
)
gast_variables_FormalParameter_strategy = st.builds(
    gast_variables_FormalParameter,
    passedByReference=
        st.booleans()
)
gast_variables_LocalVariable_strategy = st.builds(
    gast_variables_LocalVariable,
)
CompositeAccess_strategy = st.builds(
    CompositeAccess,
)
TypeAccess_strategy = st.builds(
    TypeAccess,
)
gast_accesses_InheritanceTypeAccess_strategy = st.builds(
    gast_accesses_InheritanceTypeAccess,
    implementationInheritance=
        st.booleans()
)
gast_accesses_ThrowTypeAccess_strategy = st.builds(
    gast_accesses_ThrowTypeAccess,
    declared=
        st.booleans()
)
gast_accesses_StaticTypeAccess_strategy = st.builds(
    gast_accesses_StaticTypeAccess,
)
gast_accesses_DeclarationTypeAccess_strategy = st.builds(
    gast_accesses_DeclarationTypeAccess,
)
gast_accesses_CastTypeAccess_strategy = st.builds(
    gast_accesses_CastTypeAccess,
)
gast_accesses_RunTimeTypeAccess_strategy = st.builds(
    gast_accesses_RunTimeTypeAccess,
)
gast_accesses_ParameterInstantiationTypeAccess_strategy = st.builds(
    gast_accesses_ParameterInstantiationTypeAccess,
)
Property_strategy = st.builds(
    Property,
)
InheritanceTypeAccess_strategy = st.builds(
    InheritanceTypeAccess,
)
Method_strategy = st.builds(
    Method,
)
Field_strategy = st.builds(
    Field,
)
Destructor_strategy = st.builds(
    Destructor,
)
Constructor_strategy = st.builds(
    Constructor,
)
types_GASTType_strategy = st.builds(
    types_GASTType,
)
core_GenericEntity_strategy = st.builds(
    core_GenericEntity,
)
gast_functions_GenericConstructor_strategy = st.builds(
    gast_functions_GenericConstructor,
)
gast_functions_GenericFunction_strategy = st.builds(
    gast_functions_GenericFunction,
)
gast_functions_GenericMethod_strategy = st.builds(
    gast_functions_GenericMethod,
)
Member_strategy = st.builds(
    Member,
)
types_TypeDecorator_strategy = st.builds(
    types_TypeDecorator,
)
types_Member_strategy = st.builds(
    types_Member,
)
gast_functions_Constructor_strategy = st.builds(
    gast_functions_Constructor,
    initializer=
        st.booleans()
)
gast_functions_Delegate_strategy = st.builds(
    gast_functions_Delegate,
    innerDelegate=
        st.booleans()
)
gast_variables_Property_strategy = st.builds(
    gast_variables_Property,
)
gast_types_GASTClass_strategy = st.builds(
    gast_types_GASTClass,
    anonymous=
        st.booleans(),
    interface=
        st.booleans(),
    primitive=
        st.booleans(),
    local=
        st.booleans(),
    inner=
        st.booleans(),
    linesOfComments=
        st.integers()
)
gast_variables_Field_strategy = st.builds(
    gast_variables_Field,
    propertyField=
        st.booleans()
)
gast_functions_Destructor_strategy = st.builds(
    gast_functions_Destructor,
)
gast_functions_Method_strategy = st.builds(
    gast_functions_Method,
    propertyMethod=
        st.booleans()
)
gast_types_TypeAlias_strategy = st.builds(
    gast_types_TypeAlias,
    innerTypeAlias=
        st.booleans()
)
TypeDecorator_strategy = st.builds(
    TypeDecorator,
)
gast_types_GASTArray_strategy = st.builds(
    gast_types_GASTArray,
    dimensions=
        st.integers()
)
gast_types_Reference_strategy = st.builds(
    gast_types_Reference,
    explicit=
        st.booleans()
)
gast_annotations_ModelAnnotation_strategy = st.builds(
    gast_annotations_ModelAnnotation,
)
core_SourceEntity_strategy = st.builds(
    core_SourceEntity,
)
core_NamedModelElement_strategy = st.builds(
    core_NamedModelElement,
)
gast_functions_Function_strategy = st.builds(
    gast_functions_Function,
    linesOfComments=
        st.integers(),
    linesOfCode=
        st.integers(),
    numberOfEdgesInCFG=
        st.integers(),
    maximumNestingLevel=
        st.integers(),
    operator=
        st.booleans(),
    numberOfStatements=
        st.integers(),
    numberOfNodesInCFG=
        st.integers()
)
gast_variables_Variable_strategy = st.builds(
    gast_variables_Variable,
    const=
        st.booleans()
)
core_ModelElement_strategy = st.builds(
    core_ModelElement,
)
annotations_ModelAnnotation_strategy = st.builds(
    annotations_ModelAnnotation,
)
gast_annotations_Clone_strategy = st.builds(
    gast_annotations_Clone,
)
gast_annotations_StructuralAbstraction_strategy = st.builds(
    gast_annotations_StructuralAbstraction,
)
gast_annotations_CloneInstance_strategy = st.builds(
    gast_annotations_CloneInstance,
)
gast_annotations_Comment_strategy = st.builds(
    gast_annotations_Comment,
    texts=
        safe_text,
    todo=
        st.booleans(),
    todoCount=
        st.integers(),
    formal=
        st.booleans()
)
types_GASTClass_strategy = st.builds(
    types_GASTClass,
)
gast_types_GenericClass_strategy = st.builds(
    gast_types_GenericClass,
)
gast_annotations_Attribute_strategy = st.builds(
    gast_annotations_Attribute,
)
gast_core_Position_strategy = st.builds(
    gast_core_Position,
    startLine=
        st.integers(),
    endColumn=
        st.integers(),
    endLine=
        st.integers(),
    startColumn=
        st.integers()
)
Position_strategy = st.builds(
    Position,
)
File_strategy = st.builds(
    File,
)
BasePath_strategy = st.builds(
    BasePath,
)
GASTType_strategy = st.builds(
    GASTType,
)
gast_types_TypeDecorator_strategy = st.builds(
    gast_types_TypeDecorator,
)
StructuralAbstraction_strategy = st.builds(
    StructuralAbstraction,
)
gast_annotations_Subsystem_strategy = st.builds(
    gast_annotations_Subsystem,
)
gast_annotations_Layer_strategy = st.builds(
    gast_annotations_Layer,
)
Clone_strategy = st.builds(
    Clone,
)
TypeParameterClass_strategy = st.builds(
    TypeParameterClass,
)
TypeAlias_strategy = st.builds(
    TypeAlias,
)
Package_strategy = st.builds(
    Package,
)
gast_core_PackageAlias_strategy = st.builds(
    gast_core_PackageAlias,
)
GlobalVariable_strategy = st.builds(
    GlobalVariable,
)
Delegate_strategy = st.builds(
    Delegate,
)
Access_strategy = st.builds(
    Access,
)
gast_accesses_TypeAccess_strategy = st.builds(
    gast_accesses_TypeAccess,
)
gast_accesses_FunctionAccess_strategy = st.builds(
    gast_accesses_FunctionAccess,
)
gast_accesses_VariableAccess_strategy = st.builds(
    gast_accesses_VariableAccess,
    write=
        st.booleans()
)
GASTClass_strategy = st.builds(
    GASTClass,
)
gast_types_GASTEnumeration_strategy = st.builds(
    gast_types_GASTEnumeration,
)
gast_types_GASTUnion_strategy = st.builds(
    gast_types_GASTUnion,
)
gast_types_TypeParameterClass_strategy = st.builds(
    gast_types_TypeParameterClass,
)
gast_types_GASTStruct_strategy = st.builds(
    gast_types_GASTStruct,
)
NamedModelElement_strategy = st.builds(
    NamedModelElement,
)
gast_core_Directory_strategy = st.builds(
    gast_core_Directory,
    fullQualifiedPath=
        safe_text,
    fileSystemPath=
        safe_text
)
gast_types_GASTType_strategy = st.builds(
    gast_types_GASTType,
    qualifiedName=
        safe_text,
    referenceType=
        st.booleans()
)
gast_core_File_strategy = st.builds(
    gast_core_File,
    assemblyFile=
        st.booleans(),
    linesOfCode=
        st.integers(),
    fileSystemPath=
        safe_text,
    size=
        safe_text,
    sourceFile=
        st.booleans(),
    fullQualifiedPath=
        safe_text
)
gast_core_Package_strategy = st.builds(
    gast_core_Package,
    qualifiedName=
        safe_text,
    linesOfCode=
        st.integers(),
    linesOfComments=
        st.integers()
)
gast_core_Identifier_strategy = st.builds(
    gast_core_Identifier,
    id=
        safe_text
)
ModelAnnotation_strategy = st.builds(
    ModelAnnotation,
)
GlobalFunction_strategy = st.builds(
    GlobalFunction,
)
Identifier_strategy = st.builds(
    Identifier,
)
gast_core_ModelElement_strategy = st.builds(
    gast_core_ModelElement,
    status=
        safe_text,
    sissyId=
        st.integers()
)
Directory_strategy = st.builds(
    Directory,
)
Root_strategy = st.builds(
    Root,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
gast_core_Root_strategy = st.builds(
    gast_core_Root,
    linesOfCode=
        st.integers(),
    linesOfComments=
        st.integers()
)
gast_core_NamedModelElement_strategy = st.builds(
    gast_core_NamedModelElement,
    simpleName=
        safe_text
)
gast_core_SourceEntity_strategy = st.builds(
    gast_core_SourceEntity,
)
gast_core_GenericEntity_strategy = st.builds(
    gast_core_GenericEntity,
)
gast_core_BasePath_strategy = st.builds(
    gast_core_BasePath,
    path=
        safe_text
)
gast_statements_GASTBehaviour_strategy = st.builds(
    gast_statements_GASTBehaviour,
)
CatchParameter_strategy = st.builds(
    CatchParameter,
)
BranchStatement_strategy = st.builds(
    BranchStatement,
)
GASTExpression_strategy = st.builds(
    GASTExpression,
)
Function_strategy = st.builds(
    Function,
)
gast_functions_GlobalFunction_strategy = st.builds(
    gast_functions_GlobalFunction,
    kind=
        safe_text
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
Branch_strategy = st.builds(
    Branch,
)
CloneInstance_strategy = st.builds(
    CloneInstance,
)
BaseAccess_strategy = st.builds(
    BaseAccess,
)
gast_accesses_CompositeAccess_strategy = st.builds(
    gast_accesses_CompositeAccess,
)
gast_accesses_Access_strategy = st.builds(
    gast_accesses_Access,
)
SourceEntity_strategy = st.builds(
    SourceEntity,
)
gast_statements_Branch_strategy = st.builds(
    gast_statements_Branch,
)
gast_accesses_BaseAccess_strategy = st.builds(
    gast_accesses_BaseAccess,
)
gast_types_Member_strategy = st.builds(
    gast_types_Member,
    extern=
        st.booleans(),
    abstract=
        st.booleans(),
    static=
        st.booleans(),
    introspectable=
        st.booleans(),
    internal=
        st.booleans(),
    final=
        st.booleans(),
    visibility=
        safe_text,
    virtual=
        st.booleans(),
    override=
        st.booleans(),
    typeParameterClassMember=
        st.booleans()
)
gast_statements_GASTExpression_strategy = st.builds(
    gast_statements_GASTExpression,
)
gast_statements_Statement_strategy = st.builds(
    gast_statements_Statement,
    maximumNestingLevel=
        st.integers(),
    numberOfNodesInCFG=
        st.integers(),
    numberOfComments=
        st.integers(),
    numberOfStatements=
        st.integers(),
    numberOfEdgesInCFG=
        st.integers(),
    linesOfCode=
        st.integers()
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
gast_statements_CatchBlock_strategy = st.builds(
    gast_statements_CatchBlock,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
Statement_strategy = st.builds(
    Statement,
)
gast_statements_JumpStatement_strategy = st.builds(
    gast_statements_JumpStatement,
    kind=
        safe_text
)
gast_statements_BranchStatement_strategy = st.builds(
    gast_statements_BranchStatement,
)
gast_statements_LoopStatement_strategy = st.builds(
    gast_statements_LoopStatement,
    kind=
        safe_text
)
gast_statements_BlockStatement_strategy = st.builds(
    gast_statements_BlockStatement,
    synchronized=
        st.booleans()
)
gast_statements_SimpleStatement_strategy = st.builds(
    gast_statements_SimpleStatement,
)
gast_statements_ExceptionHandler_strategy = st.builds(
    gast_statements_ExceptionHandler,
)

@given(instance=variables_Field_strategy)
@settings(max_examples=50)
def test_variables_field_instantiation(instance):
    assert isinstance(instance, variables_Field)

@given(instance=variables_Variable_strategy)
@settings(max_examples=50)
def test_variables_variable_instantiation(instance):
    assert isinstance(instance, variables_Variable)

@given(instance=ThrowTypeAccess_strategy)
@settings(max_examples=50)
def test_throwtypeaccess_instantiation(instance):
    assert isinstance(instance, ThrowTypeAccess)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=FormalParameter_strategy)
@settings(max_examples=50)
def test_formalparameter_instantiation(instance):
    assert isinstance(instance, FormalParameter)

@given(instance=DeclarationTypeAccess_strategy)
@settings(max_examples=50)
def test_declarationtypeaccess_instantiation(instance):
    assert isinstance(instance, DeclarationTypeAccess)

@given(instance=functions_Constructor_strategy)
@settings(max_examples=50)
def test_functions_constructor_instantiation(instance):
    assert isinstance(instance, functions_Constructor)

@given(instance=functions_Method_strategy)
@settings(max_examples=50)
def test_functions_method_instantiation(instance):
    assert isinstance(instance, functions_Method)

@given(instance=functions_GlobalFunction_strategy)
@settings(max_examples=50)
def test_functions_globalfunction_instantiation(instance):
    assert isinstance(instance, functions_GlobalFunction)

@given(instance=functions_Function_strategy)
@settings(max_examples=50)
def test_functions_function_instantiation(instance):
    assert isinstance(instance, functions_Function)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=gast_accesses_PropertyAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_propertyaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_PropertyAccess)

@given(instance=gast_accesses_SelfAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_selfaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_SelfAccess)



@given(instance=gast_accesses_SelfAccess_strategy)
def test_gast_accesses_selfaccess_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original

@given(instance=FunctionAccess_strategy)
@settings(max_examples=50)
def test_functionaccess_instantiation(instance):
    assert isinstance(instance, FunctionAccess)

@given(instance=gast_accesses_DelegateAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_delegateaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_DelegateAccess)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=gast_variables_GlobalVariable_strategy)
@settings(max_examples=50)
def test_gast_variables_globalvariable_instantiation(instance):
    assert isinstance(instance, gast_variables_GlobalVariable)

@given(instance=gast_variables_CatchParameter_strategy)
@settings(max_examples=50)
def test_gast_variables_catchparameter_instantiation(instance):
    assert isinstance(instance, gast_variables_CatchParameter)



@given(instance=gast_variables_CatchParameter_strategy)
def test_gast_variables_catchparameter_rethrown_setter(instance):
    original = instance.rethrown
    instance.rethrown = original
    assert instance.rethrown == original

@given(instance=gast_variables_FormalParameter_strategy)
@settings(max_examples=50)
def test_gast_variables_formalparameter_instantiation(instance):
    assert isinstance(instance, gast_variables_FormalParameter)



@given(instance=gast_variables_FormalParameter_strategy)
def test_gast_variables_formalparameter_passedByReference_setter(instance):
    original = instance.passedByReference
    instance.passedByReference = original
    assert instance.passedByReference == original

@given(instance=gast_variables_LocalVariable_strategy)
@settings(max_examples=50)
def test_gast_variables_localvariable_instantiation(instance):
    assert isinstance(instance, gast_variables_LocalVariable)

@given(instance=CompositeAccess_strategy)
@settings(max_examples=50)
def test_compositeaccess_instantiation(instance):
    assert isinstance(instance, CompositeAccess)

@given(instance=TypeAccess_strategy)
@settings(max_examples=50)
def test_typeaccess_instantiation(instance):
    assert isinstance(instance, TypeAccess)

@given(instance=gast_accesses_InheritanceTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_inheritancetypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_InheritanceTypeAccess)



@given(instance=gast_accesses_InheritanceTypeAccess_strategy)
def test_gast_accesses_inheritancetypeaccess_implementationInheritance_setter(instance):
    original = instance.implementationInheritance
    instance.implementationInheritance = original
    assert instance.implementationInheritance == original

@given(instance=gast_accesses_ThrowTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_throwtypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_ThrowTypeAccess)



@given(instance=gast_accesses_ThrowTypeAccess_strategy)
def test_gast_accesses_throwtypeaccess_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original

@given(instance=gast_accesses_StaticTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_statictypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_StaticTypeAccess)

@given(instance=gast_accesses_DeclarationTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_declarationtypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_DeclarationTypeAccess)

@given(instance=gast_accesses_CastTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_casttypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_CastTypeAccess)

@given(instance=gast_accesses_RunTimeTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_runtimetypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_RunTimeTypeAccess)

@given(instance=gast_accesses_ParameterInstantiationTypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_parameterinstantiationtypeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_ParameterInstantiationTypeAccess)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=InheritanceTypeAccess_strategy)
@settings(max_examples=50)
def test_inheritancetypeaccess_instantiation(instance):
    assert isinstance(instance, InheritanceTypeAccess)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=Destructor_strategy)
@settings(max_examples=50)
def test_destructor_instantiation(instance):
    assert isinstance(instance, Destructor)

@given(instance=Constructor_strategy)
@settings(max_examples=50)
def test_constructor_instantiation(instance):
    assert isinstance(instance, Constructor)

@given(instance=types_GASTType_strategy)
@settings(max_examples=50)
def test_types_gasttype_instantiation(instance):
    assert isinstance(instance, types_GASTType)

@given(instance=core_GenericEntity_strategy)
@settings(max_examples=50)
def test_core_genericentity_instantiation(instance):
    assert isinstance(instance, core_GenericEntity)

@given(instance=gast_functions_GenericConstructor_strategy)
@settings(max_examples=50)
def test_gast_functions_genericconstructor_instantiation(instance):
    assert isinstance(instance, gast_functions_GenericConstructor)

@given(instance=gast_functions_GenericFunction_strategy)
@settings(max_examples=50)
def test_gast_functions_genericfunction_instantiation(instance):
    assert isinstance(instance, gast_functions_GenericFunction)

@given(instance=gast_functions_GenericMethod_strategy)
@settings(max_examples=50)
def test_gast_functions_genericmethod_instantiation(instance):
    assert isinstance(instance, gast_functions_GenericMethod)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=types_TypeDecorator_strategy)
@settings(max_examples=50)
def test_types_typedecorator_instantiation(instance):
    assert isinstance(instance, types_TypeDecorator)

@given(instance=types_Member_strategy)
@settings(max_examples=50)
def test_types_member_instantiation(instance):
    assert isinstance(instance, types_Member)

@given(instance=gast_functions_Constructor_strategy)
@settings(max_examples=50)
def test_gast_functions_constructor_instantiation(instance):
    assert isinstance(instance, gast_functions_Constructor)



@given(instance=gast_functions_Constructor_strategy)
def test_gast_functions_constructor_initializer_setter(instance):
    original = instance.initializer
    instance.initializer = original
    assert instance.initializer == original

@given(instance=gast_functions_Delegate_strategy)
@settings(max_examples=50)
def test_gast_functions_delegate_instantiation(instance):
    assert isinstance(instance, gast_functions_Delegate)



@given(instance=gast_functions_Delegate_strategy)
def test_gast_functions_delegate_innerDelegate_setter(instance):
    original = instance.innerDelegate
    instance.innerDelegate = original
    assert instance.innerDelegate == original

@given(instance=gast_variables_Property_strategy)
@settings(max_examples=50)
def test_gast_variables_property_instantiation(instance):
    assert isinstance(instance, gast_variables_Property)

@given(instance=gast_types_GASTClass_strategy)
@settings(max_examples=50)
def test_gast_types_gastclass_instantiation(instance):
    assert isinstance(instance, gast_types_GASTClass)



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_anonymous_setter(instance):
    original = instance.anonymous
    instance.anonymous = original
    assert instance.anonymous == original



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_local_setter(instance):
    original = instance.local
    instance.local = original
    assert instance.local == original



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original



@given(instance=gast_types_GASTClass_strategy)
def test_gast_types_gastclass_linesOfComments_setter(instance):
    original = instance.linesOfComments
    instance.linesOfComments = original
    assert instance.linesOfComments == original

@given(instance=gast_variables_Field_strategy)
@settings(max_examples=50)
def test_gast_variables_field_instantiation(instance):
    assert isinstance(instance, gast_variables_Field)



@given(instance=gast_variables_Field_strategy)
def test_gast_variables_field_propertyField_setter(instance):
    original = instance.propertyField
    instance.propertyField = original
    assert instance.propertyField == original

@given(instance=gast_functions_Destructor_strategy)
@settings(max_examples=50)
def test_gast_functions_destructor_instantiation(instance):
    assert isinstance(instance, gast_functions_Destructor)

@given(instance=gast_functions_Method_strategy)
@settings(max_examples=50)
def test_gast_functions_method_instantiation(instance):
    assert isinstance(instance, gast_functions_Method)



@given(instance=gast_functions_Method_strategy)
def test_gast_functions_method_propertyMethod_setter(instance):
    original = instance.propertyMethod
    instance.propertyMethod = original
    assert instance.propertyMethod == original

@given(instance=gast_types_TypeAlias_strategy)
@settings(max_examples=50)
def test_gast_types_typealias_instantiation(instance):
    assert isinstance(instance, gast_types_TypeAlias)



@given(instance=gast_types_TypeAlias_strategy)
def test_gast_types_typealias_innerTypeAlias_setter(instance):
    original = instance.innerTypeAlias
    instance.innerTypeAlias = original
    assert instance.innerTypeAlias == original

@given(instance=TypeDecorator_strategy)
@settings(max_examples=50)
def test_typedecorator_instantiation(instance):
    assert isinstance(instance, TypeDecorator)

@given(instance=gast_types_GASTArray_strategy)
@settings(max_examples=50)
def test_gast_types_gastarray_instantiation(instance):
    assert isinstance(instance, gast_types_GASTArray)



@given(instance=gast_types_GASTArray_strategy)
def test_gast_types_gastarray_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=gast_types_Reference_strategy)
@settings(max_examples=50)
def test_gast_types_reference_instantiation(instance):
    assert isinstance(instance, gast_types_Reference)



@given(instance=gast_types_Reference_strategy)
def test_gast_types_reference_explicit_setter(instance):
    original = instance.explicit
    instance.explicit = original
    assert instance.explicit == original

@given(instance=gast_annotations_ModelAnnotation_strategy)
@settings(max_examples=50)
def test_gast_annotations_modelannotation_instantiation(instance):
    assert isinstance(instance, gast_annotations_ModelAnnotation)

@given(instance=core_SourceEntity_strategy)
@settings(max_examples=50)
def test_core_sourceentity_instantiation(instance):
    assert isinstance(instance, core_SourceEntity)

@given(instance=core_NamedModelElement_strategy)
@settings(max_examples=50)
def test_core_namedmodelelement_instantiation(instance):
    assert isinstance(instance, core_NamedModelElement)

@given(instance=gast_functions_Function_strategy)
@settings(max_examples=50)
def test_gast_functions_function_instantiation(instance):
    assert isinstance(instance, gast_functions_Function)



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_linesOfComments_setter(instance):
    original = instance.linesOfComments
    instance.linesOfComments = original
    assert instance.linesOfComments == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_linesOfCode_setter(instance):
    original = instance.linesOfCode
    instance.linesOfCode = original
    assert instance.linesOfCode == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_numberOfEdgesInCFG_setter(instance):
    original = instance.numberOfEdgesInCFG
    instance.numberOfEdgesInCFG = original
    assert instance.numberOfEdgesInCFG == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_maximumNestingLevel_setter(instance):
    original = instance.maximumNestingLevel
    instance.maximumNestingLevel = original
    assert instance.maximumNestingLevel == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_numberOfStatements_setter(instance):
    original = instance.numberOfStatements
    instance.numberOfStatements = original
    assert instance.numberOfStatements == original



@given(instance=gast_functions_Function_strategy)
def test_gast_functions_function_numberOfNodesInCFG_setter(instance):
    original = instance.numberOfNodesInCFG
    instance.numberOfNodesInCFG = original
    assert instance.numberOfNodesInCFG == original

@given(instance=gast_variables_Variable_strategy)
@settings(max_examples=50)
def test_gast_variables_variable_instantiation(instance):
    assert isinstance(instance, gast_variables_Variable)



@given(instance=gast_variables_Variable_strategy)
def test_gast_variables_variable_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=core_ModelElement_strategy)
@settings(max_examples=50)
def test_core_modelelement_instantiation(instance):
    assert isinstance(instance, core_ModelElement)

@given(instance=annotations_ModelAnnotation_strategy)
@settings(max_examples=50)
def test_annotations_modelannotation_instantiation(instance):
    assert isinstance(instance, annotations_ModelAnnotation)

@given(instance=gast_annotations_Clone_strategy)
@settings(max_examples=50)
def test_gast_annotations_clone_instantiation(instance):
    assert isinstance(instance, gast_annotations_Clone)

@given(instance=gast_annotations_StructuralAbstraction_strategy)
@settings(max_examples=50)
def test_gast_annotations_structuralabstraction_instantiation(instance):
    assert isinstance(instance, gast_annotations_StructuralAbstraction)

@given(instance=gast_annotations_CloneInstance_strategy)
@settings(max_examples=50)
def test_gast_annotations_cloneinstance_instantiation(instance):
    assert isinstance(instance, gast_annotations_CloneInstance)

@given(instance=gast_annotations_Comment_strategy)
@settings(max_examples=50)
def test_gast_annotations_comment_instantiation(instance):
    assert isinstance(instance, gast_annotations_Comment)



@given(instance=gast_annotations_Comment_strategy)
def test_gast_annotations_comment_texts_setter(instance):
    original = instance.texts
    instance.texts = original
    assert instance.texts == original



@given(instance=gast_annotations_Comment_strategy)
def test_gast_annotations_comment_todo_setter(instance):
    original = instance.todo
    instance.todo = original
    assert instance.todo == original



@given(instance=gast_annotations_Comment_strategy)
def test_gast_annotations_comment_todoCount_setter(instance):
    original = instance.todoCount
    instance.todoCount = original
    assert instance.todoCount == original



@given(instance=gast_annotations_Comment_strategy)
def test_gast_annotations_comment_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gast_annotations_Comment_strategy)
@settings(max_examples=30)
def test_gast_annotations_comment_ocltodo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.OCLtodo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.OCLtodo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'OCLtodo' in gast_annotations_Comment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'OCLtodo' in gast_annotations_Comment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'OCLtodo' in gast_annotations_Comment is not implemented or raised an error")

@given(instance=types_GASTClass_strategy)
@settings(max_examples=50)
def test_types_gastclass_instantiation(instance):
    assert isinstance(instance, types_GASTClass)

@given(instance=gast_types_GenericClass_strategy)
@settings(max_examples=50)
def test_gast_types_genericclass_instantiation(instance):
    assert isinstance(instance, gast_types_GenericClass)

@given(instance=gast_annotations_Attribute_strategy)
@settings(max_examples=50)
def test_gast_annotations_attribute_instantiation(instance):
    assert isinstance(instance, gast_annotations_Attribute)

@given(instance=gast_core_Position_strategy)
@settings(max_examples=50)
def test_gast_core_position_instantiation(instance):
    assert isinstance(instance, gast_core_Position)



@given(instance=gast_core_Position_strategy)
def test_gast_core_position_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=gast_core_Position_strategy)
def test_gast_core_position_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original



@given(instance=gast_core_Position_strategy)
def test_gast_core_position_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=gast_core_Position_strategy)
def test_gast_core_position_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gast_core_Position_strategy)
@settings(max_examples=30)
def test_gast_core_position_eitherassemblyfileorsourcefileset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EitherAssemblyFileOrSourceFileSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EitherAssemblyFileOrSourceFileSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EitherAssemblyFileOrSourceFileSet' in gast_core_Position is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EitherAssemblyFileOrSourceFileSet' in gast_core_Position did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EitherAssemblyFileOrSourceFileSet' in gast_core_Position is not implemented or raised an error")

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)

@given(instance=File_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, File)

@given(instance=BasePath_strategy)
@settings(max_examples=50)
def test_basepath_instantiation(instance):
    assert isinstance(instance, BasePath)

@given(instance=GASTType_strategy)
@settings(max_examples=50)
def test_gasttype_instantiation(instance):
    assert isinstance(instance, GASTType)

@given(instance=gast_types_TypeDecorator_strategy)
@settings(max_examples=50)
def test_gast_types_typedecorator_instantiation(instance):
    assert isinstance(instance, gast_types_TypeDecorator)

@given(instance=StructuralAbstraction_strategy)
@settings(max_examples=50)
def test_structuralabstraction_instantiation(instance):
    assert isinstance(instance, StructuralAbstraction)

@given(instance=gast_annotations_Subsystem_strategy)
@settings(max_examples=50)
def test_gast_annotations_subsystem_instantiation(instance):
    assert isinstance(instance, gast_annotations_Subsystem)

@given(instance=gast_annotations_Layer_strategy)
@settings(max_examples=50)
def test_gast_annotations_layer_instantiation(instance):
    assert isinstance(instance, gast_annotations_Layer)

@given(instance=Clone_strategy)
@settings(max_examples=50)
def test_clone_instantiation(instance):
    assert isinstance(instance, Clone)

@given(instance=TypeParameterClass_strategy)
@settings(max_examples=50)
def test_typeparameterclass_instantiation(instance):
    assert isinstance(instance, TypeParameterClass)

@given(instance=TypeAlias_strategy)
@settings(max_examples=50)
def test_typealias_instantiation(instance):
    assert isinstance(instance, TypeAlias)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=gast_core_PackageAlias_strategy)
@settings(max_examples=50)
def test_gast_core_packagealias_instantiation(instance):
    assert isinstance(instance, gast_core_PackageAlias)

@given(instance=GlobalVariable_strategy)
@settings(max_examples=50)
def test_globalvariable_instantiation(instance):
    assert isinstance(instance, GlobalVariable)

@given(instance=Delegate_strategy)
@settings(max_examples=50)
def test_delegate_instantiation(instance):
    assert isinstance(instance, Delegate)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=gast_accesses_TypeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_typeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_TypeAccess)

@given(instance=gast_accesses_FunctionAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_functionaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_FunctionAccess)

@given(instance=gast_accesses_VariableAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_variableaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_VariableAccess)



@given(instance=gast_accesses_VariableAccess_strategy)
def test_gast_accesses_variableaccess_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=GASTClass_strategy)
@settings(max_examples=50)
def test_gastclass_instantiation(instance):
    assert isinstance(instance, GASTClass)

@given(instance=gast_types_GASTEnumeration_strategy)
@settings(max_examples=50)
def test_gast_types_gastenumeration_instantiation(instance):
    assert isinstance(instance, gast_types_GASTEnumeration)

@given(instance=gast_types_GASTUnion_strategy)
@settings(max_examples=50)
def test_gast_types_gastunion_instantiation(instance):
    assert isinstance(instance, gast_types_GASTUnion)

@given(instance=gast_types_TypeParameterClass_strategy)
@settings(max_examples=50)
def test_gast_types_typeparameterclass_instantiation(instance):
    assert isinstance(instance, gast_types_TypeParameterClass)

@given(instance=gast_types_GASTStruct_strategy)
@settings(max_examples=50)
def test_gast_types_gaststruct_instantiation(instance):
    assert isinstance(instance, gast_types_GASTStruct)

@given(instance=NamedModelElement_strategy)
@settings(max_examples=50)
def test_namedmodelelement_instantiation(instance):
    assert isinstance(instance, NamedModelElement)

@given(instance=gast_core_Directory_strategy)
@settings(max_examples=50)
def test_gast_core_directory_instantiation(instance):
    assert isinstance(instance, gast_core_Directory)



@given(instance=gast_core_Directory_strategy)
def test_gast_core_directory_fullQualifiedPath_setter(instance):
    original = instance.fullQualifiedPath
    instance.fullQualifiedPath = original
    assert instance.fullQualifiedPath == original



@given(instance=gast_core_Directory_strategy)
def test_gast_core_directory_fileSystemPath_setter(instance):
    original = instance.fileSystemPath
    instance.fileSystemPath = original
    assert instance.fileSystemPath == original

@given(instance=gast_types_GASTType_strategy)
@settings(max_examples=50)
def test_gast_types_gasttype_instantiation(instance):
    assert isinstance(instance, gast_types_GASTType)



@given(instance=gast_types_GASTType_strategy)
def test_gast_types_gasttype_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=gast_types_GASTType_strategy)
def test_gast_types_gasttype_referenceType_setter(instance):
    original = instance.referenceType
    instance.referenceType = original
    assert instance.referenceType == original

@given(instance=gast_core_File_strategy)
@settings(max_examples=50)
def test_gast_core_file_instantiation(instance):
    assert isinstance(instance, gast_core_File)



@given(instance=gast_core_File_strategy)
def test_gast_core_file_assemblyFile_setter(instance):
    original = instance.assemblyFile
    instance.assemblyFile = original
    assert instance.assemblyFile == original



@given(instance=gast_core_File_strategy)
def test_gast_core_file_linesOfCode_setter(instance):
    original = instance.linesOfCode
    instance.linesOfCode = original
    assert instance.linesOfCode == original



@given(instance=gast_core_File_strategy)
def test_gast_core_file_fileSystemPath_setter(instance):
    original = instance.fileSystemPath
    instance.fileSystemPath = original
    assert instance.fileSystemPath == original



@given(instance=gast_core_File_strategy)
def test_gast_core_file_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=gast_core_File_strategy)
def test_gast_core_file_sourceFile_setter(instance):
    original = instance.sourceFile
    instance.sourceFile = original
    assert instance.sourceFile == original



@given(instance=gast_core_File_strategy)
def test_gast_core_file_fullQualifiedPath_setter(instance):
    original = instance.fullQualifiedPath
    instance.fullQualifiedPath = original
    assert instance.fullQualifiedPath == original

@given(instance=gast_core_Package_strategy)
@settings(max_examples=50)
def test_gast_core_package_instantiation(instance):
    assert isinstance(instance, gast_core_Package)



@given(instance=gast_core_Package_strategy)
def test_gast_core_package_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=gast_core_Package_strategy)
def test_gast_core_package_linesOfCode_setter(instance):
    original = instance.linesOfCode
    instance.linesOfCode = original
    assert instance.linesOfCode == original



@given(instance=gast_core_Package_strategy)
def test_gast_core_package_linesOfComments_setter(instance):
    original = instance.linesOfComments
    instance.linesOfComments = original
    assert instance.linesOfComments == original

@given(instance=gast_core_Identifier_strategy)
@settings(max_examples=50)
def test_gast_core_identifier_instantiation(instance):
    assert isinstance(instance, gast_core_Identifier)



@given(instance=gast_core_Identifier_strategy)
def test_gast_core_identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gast_core_Identifier_strategy)
@settings(max_examples=30)
def test_gast_core_identifier_idhastobeunique_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.idHasToBeUnique(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.idHasToBeUnique).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'idHasToBeUnique' in gast_core_Identifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'idHasToBeUnique' in gast_core_Identifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'idHasToBeUnique' in gast_core_Identifier is not implemented or raised an error")

@given(instance=ModelAnnotation_strategy)
@settings(max_examples=50)
def test_modelannotation_instantiation(instance):
    assert isinstance(instance, ModelAnnotation)

@given(instance=GlobalFunction_strategy)
@settings(max_examples=50)
def test_globalfunction_instantiation(instance):
    assert isinstance(instance, GlobalFunction)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=gast_core_ModelElement_strategy)
@settings(max_examples=50)
def test_gast_core_modelelement_instantiation(instance):
    assert isinstance(instance, gast_core_ModelElement)



@given(instance=gast_core_ModelElement_strategy)
def test_gast_core_modelelement_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=gast_core_ModelElement_strategy)
def test_gast_core_modelelement_sissyId_setter(instance):
    original = instance.sissyId
    instance.sissyId = original
    assert instance.sissyId == original

@given(instance=Directory_strategy)
@settings(max_examples=50)
def test_directory_instantiation(instance):
    assert isinstance(instance, Directory)

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=gast_core_Root_strategy)
@settings(max_examples=50)
def test_gast_core_root_instantiation(instance):
    assert isinstance(instance, gast_core_Root)



@given(instance=gast_core_Root_strategy)
def test_gast_core_root_linesOfCode_setter(instance):
    original = instance.linesOfCode
    instance.linesOfCode = original
    assert instance.linesOfCode == original



@given(instance=gast_core_Root_strategy)
def test_gast_core_root_linesOfComments_setter(instance):
    original = instance.linesOfComments
    instance.linesOfComments = original
    assert instance.linesOfComments == original

@given(instance=gast_core_NamedModelElement_strategy)
@settings(max_examples=50)
def test_gast_core_namedmodelelement_instantiation(instance):
    assert isinstance(instance, gast_core_NamedModelElement)



@given(instance=gast_core_NamedModelElement_strategy)
def test_gast_core_namedmodelelement_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=gast_core_SourceEntity_strategy)
@settings(max_examples=50)
def test_gast_core_sourceentity_instantiation(instance):
    assert isinstance(instance, gast_core_SourceEntity)

@given(instance=gast_core_GenericEntity_strategy)
@settings(max_examples=50)
def test_gast_core_genericentity_instantiation(instance):
    assert isinstance(instance, gast_core_GenericEntity)

@given(instance=gast_core_BasePath_strategy)
@settings(max_examples=50)
def test_gast_core_basepath_instantiation(instance):
    assert isinstance(instance, gast_core_BasePath)



@given(instance=gast_core_BasePath_strategy)
def test_gast_core_basepath_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=gast_statements_GASTBehaviour_strategy)
@settings(max_examples=50)
def test_gast_statements_gastbehaviour_instantiation(instance):
    assert isinstance(instance, gast_statements_GASTBehaviour)

@given(instance=CatchParameter_strategy)
@settings(max_examples=50)
def test_catchparameter_instantiation(instance):
    assert isinstance(instance, CatchParameter)

@given(instance=BranchStatement_strategy)
@settings(max_examples=50)
def test_branchstatement_instantiation(instance):
    assert isinstance(instance, BranchStatement)

@given(instance=GASTExpression_strategy)
@settings(max_examples=50)
def test_gastexpression_instantiation(instance):
    assert isinstance(instance, GASTExpression)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=gast_functions_GlobalFunction_strategy)
@settings(max_examples=50)
def test_gast_functions_globalfunction_instantiation(instance):
    assert isinstance(instance, gast_functions_GlobalFunction)



@given(instance=gast_functions_GlobalFunction_strategy)
def test_gast_functions_globalfunction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)

@given(instance=CloneInstance_strategy)
@settings(max_examples=50)
def test_cloneinstance_instantiation(instance):
    assert isinstance(instance, CloneInstance)

@given(instance=BaseAccess_strategy)
@settings(max_examples=50)
def test_baseaccess_instantiation(instance):
    assert isinstance(instance, BaseAccess)

@given(instance=gast_accesses_CompositeAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_compositeaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_CompositeAccess)

@given(instance=gast_accesses_Access_strategy)
@settings(max_examples=50)
def test_gast_accesses_access_instantiation(instance):
    assert isinstance(instance, gast_accesses_Access)

@given(instance=SourceEntity_strategy)
@settings(max_examples=50)
def test_sourceentity_instantiation(instance):
    assert isinstance(instance, SourceEntity)

@given(instance=gast_statements_Branch_strategy)
@settings(max_examples=50)
def test_gast_statements_branch_instantiation(instance):
    assert isinstance(instance, gast_statements_Branch)

@given(instance=gast_accesses_BaseAccess_strategy)
@settings(max_examples=50)
def test_gast_accesses_baseaccess_instantiation(instance):
    assert isinstance(instance, gast_accesses_BaseAccess)

@given(instance=gast_types_Member_strategy)
@settings(max_examples=50)
def test_gast_types_member_instantiation(instance):
    assert isinstance(instance, gast_types_Member)



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_introspectable_setter(instance):
    original = instance.introspectable
    instance.introspectable = original
    assert instance.introspectable == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_internal_setter(instance):
    original = instance.internal
    instance.internal = original
    assert instance.internal == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_virtual_setter(instance):
    original = instance.virtual
    instance.virtual = original
    assert instance.virtual == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_override_setter(instance):
    original = instance.override
    instance.override = original
    assert instance.override == original



@given(instance=gast_types_Member_strategy)
def test_gast_types_member_typeParameterClassMember_setter(instance):
    original = instance.typeParameterClassMember
    instance.typeParameterClassMember = original
    assert instance.typeParameterClassMember == original

@given(instance=gast_statements_GASTExpression_strategy)
@settings(max_examples=50)
def test_gast_statements_gastexpression_instantiation(instance):
    assert isinstance(instance, gast_statements_GASTExpression)

@given(instance=gast_statements_Statement_strategy)
@settings(max_examples=50)
def test_gast_statements_statement_instantiation(instance):
    assert isinstance(instance, gast_statements_Statement)



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_maximumNestingLevel_setter(instance):
    original = instance.maximumNestingLevel
    instance.maximumNestingLevel = original
    assert instance.maximumNestingLevel == original



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_numberOfNodesInCFG_setter(instance):
    original = instance.numberOfNodesInCFG
    instance.numberOfNodesInCFG = original
    assert instance.numberOfNodesInCFG == original



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_numberOfComments_setter(instance):
    original = instance.numberOfComments
    instance.numberOfComments = original
    assert instance.numberOfComments == original



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_numberOfStatements_setter(instance):
    original = instance.numberOfStatements
    instance.numberOfStatements = original
    assert instance.numberOfStatements == original



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_numberOfEdgesInCFG_setter(instance):
    original = instance.numberOfEdgesInCFG
    instance.numberOfEdgesInCFG = original
    assert instance.numberOfEdgesInCFG == original



@given(instance=gast_statements_Statement_strategy)
def test_gast_statements_statement_linesOfCode_setter(instance):
    original = instance.linesOfCode
    instance.linesOfCode = original
    assert instance.linesOfCode == original

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=gast_statements_CatchBlock_strategy)
@settings(max_examples=50)
def test_gast_statements_catchblock_instantiation(instance):
    assert isinstance(instance, gast_statements_CatchBlock)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gast_statements_JumpStatement_strategy)
@settings(max_examples=50)
def test_gast_statements_jumpstatement_instantiation(instance):
    assert isinstance(instance, gast_statements_JumpStatement)



@given(instance=gast_statements_JumpStatement_strategy)
def test_gast_statements_jumpstatement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=gast_statements_BranchStatement_strategy)
@settings(max_examples=50)
def test_gast_statements_branchstatement_instantiation(instance):
    assert isinstance(instance, gast_statements_BranchStatement)

@given(instance=gast_statements_LoopStatement_strategy)
@settings(max_examples=50)
def test_gast_statements_loopstatement_instantiation(instance):
    assert isinstance(instance, gast_statements_LoopStatement)



@given(instance=gast_statements_LoopStatement_strategy)
def test_gast_statements_loopstatement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=gast_statements_BlockStatement_strategy)
@settings(max_examples=50)
def test_gast_statements_blockstatement_instantiation(instance):
    assert isinstance(instance, gast_statements_BlockStatement)



@given(instance=gast_statements_BlockStatement_strategy)
def test_gast_statements_blockstatement_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=gast_statements_SimpleStatement_strategy)
@settings(max_examples=50)
def test_gast_statements_simplestatement_instantiation(instance):
    assert isinstance(instance, gast_statements_SimpleStatement)

@given(instance=gast_statements_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_gast_statements_exceptionhandler_instantiation(instance):
    assert isinstance(instance, gast_statements_ExceptionHandler)

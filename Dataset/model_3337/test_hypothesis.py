import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractMTypeWithNameDeclaration,
    jsm::AbstractMFieldDeclaration,
    AbstractMInterface,
    AbstractMExternalType,
    jsm::MExternalInterface,
    MDeclaredClass,
    jsm::MAbstractDeclaredClass,
    jsm::AbstractMMethodDeclaration,
    AbstractMDeclaredType,
    jsm::MDeclaredInterface,
    AbstractMClass,
    jsm::MExternalClass,
    jsm::MDeclaredClass,
    AbstractMType,
    jsm::AbstractMInterface,
    jsm::AbstractMClass,
    jsm::AbstractMTypeWithNameDeclaration,
    jsm::AbstractCStatement,
    AbstractModifiers,
    jsm::AbstractMMethodLike,
    jsm::AbstractModifiers,
    AbstractMTypeReference,
    jsm::MPrimitiveTypeReference,
    jsm::MExternalTypeReference,
    AbstractCExpression,
    jsm::CUnparsedExpression,
    jsm::CConditionalExpression,
    AbstractCStatement,
    jsm::CIfStatement,
    jsm::CDeclarationStatement,
    jsm::CExpressionStatement,
    jsm::CUnparsedStatement,
    jsm::CBlockStatement,
    jsm::MConstructorParameter,
    AbstractMMethodImplementation,
    jsm::MMethodImplementationParameter,
    AbstractMMethodLike,
    jsm::MConstructor,
    AbstractMImplementableMethodDeclaration,
    jsm::MAbstractClassMethodDeclaration,
    jsm::MInterfaceMethodDeclaration,
    jsm::MDeclaredMethodImplementation,
    jsm::MDirectMethodImplementation,
    AbstractMMethodDeclaration,
    jsm::MNativeMethodDeclaration,
    jsm::AbstractMImplementableMethodDeclaration,
    jsm::MImplicitMethodDeclaration,
    jsm::MMethodDeclarationParameter,
    AbstractMClassFieldDeclaration,
    jsm::MStaticClassFieldDeclaration,
    jsm::MInstanceClassFieldDeclaration,
    AbstractMFieldDeclaration,
    jsm::MConstantInterfaceFieldDeclaration,
    jsm::AbstractMClassFieldDeclaration,
    jsm::AbstractCExpression,
    jsm::MDeclaredTypeReference,
    jsm::AbstractMTypeReference,
    jsm::AbstractMMethodImplementation,
    jsm::AbstractMType,
    AbstractMTypeContainer,
    jsm::AbstractMDeclaredType,
    jsm::AbstractMTypeContainer,
    AbstractMResource,
    jsm::MCompilationUnit,
    jsm::MResource,
    jsm::AbstractMResource,
    jsm::AbstractMExternalType,
    jsm::AbstractMPackageContainer,
    AbstractMPackageContainer,
    jsm::MPackage,
    jsm::MRoot,
    MPrimitiveTypes,
    MVisibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractmtypewithnamedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeWithNameDeclaration)


def test_abstractmtypewithnamedeclaration_constructor_exists():
    assert callable(AbstractMTypeWithNameDeclaration.__init__)


def test_abstractmtypewithnamedeclaration_constructor_args():
    sig = inspect.signature(AbstractMTypeWithNameDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMFieldDeclaration)


def test_jsm::abstractmfielddeclaration_constructor_exists():
    assert callable(jsm::AbstractMFieldDeclaration.__init__)


def test_jsm::abstractmfielddeclaration_constructor_args():
    sig = inspect.signature(jsm::AbstractMFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractminterface_is_not_abstract():
    assert not inspect.isabstract(AbstractMInterface)


def test_abstractminterface_constructor_exists():
    assert callable(AbstractMInterface.__init__)


def test_abstractminterface_constructor_args():
    sig = inspect.signature(AbstractMInterface.__init__)
    params = list(sig.parameters.keys())



def test_abstractmexternaltype_is_not_abstract():
    assert not inspect.isabstract(AbstractMExternalType)


def test_abstractmexternaltype_constructor_exists():
    assert callable(AbstractMExternalType.__init__)


def test_abstractmexternaltype_constructor_args():
    sig = inspect.signature(AbstractMExternalType.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mexternalinterface_is_not_abstract():
    assert not inspect.isabstract(jsm::MExternalInterface)


def test_jsm::mexternalinterface_constructor_exists():
    assert callable(jsm::MExternalInterface.__init__)


def test_jsm::mexternalinterface_constructor_args():
    sig = inspect.signature(jsm::MExternalInterface.__init__)
    params = list(sig.parameters.keys())



def test_mdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(MDeclaredClass)


def test_mdeclaredclass_constructor_exists():
    assert callable(MDeclaredClass.__init__)


def test_mdeclaredclass_constructor_args():
    sig = inspect.signature(MDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mabstractdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(jsm::MAbstractDeclaredClass)


def test_jsm::mabstractdeclaredclass_constructor_exists():
    assert callable(jsm::MAbstractDeclaredClass.__init__)


def test_jsm::mabstractdeclaredclass_constructor_args():
    sig = inspect.signature(jsm::MAbstractDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMMethodDeclaration)


def test_jsm::abstractmmethoddeclaration_constructor_exists():
    assert callable(jsm::AbstractMMethodDeclaration.__init__)


def test_jsm::abstractmmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::AbstractMMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(AbstractMDeclaredType)


def test_abstractmdeclaredtype_constructor_exists():
    assert callable(AbstractMDeclaredType.__init__)


def test_abstractmdeclaredtype_constructor_args():
    sig = inspect.signature(AbstractMDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mdeclaredinterface_is_not_abstract():
    assert not inspect.isabstract(jsm::MDeclaredInterface)


def test_jsm::mdeclaredinterface_constructor_exists():
    assert callable(jsm::MDeclaredInterface.__init__)


def test_jsm::mdeclaredinterface_constructor_args():
    sig = inspect.signature(jsm::MDeclaredInterface.__init__)
    params = list(sig.parameters.keys())



def test_abstractmclass_is_not_abstract():
    assert not inspect.isabstract(AbstractMClass)


def test_abstractmclass_constructor_exists():
    assert callable(AbstractMClass.__init__)


def test_abstractmclass_constructor_args():
    sig = inspect.signature(AbstractMClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mexternalclass_is_not_abstract():
    assert not inspect.isabstract(jsm::MExternalClass)


def test_jsm::mexternalclass_constructor_exists():
    assert callable(jsm::MExternalClass.__init__)


def test_jsm::mexternalclass_constructor_args():
    sig = inspect.signature(jsm::MExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(jsm::MDeclaredClass)


def test_jsm::mdeclaredclass_constructor_exists():
    assert callable(jsm::MDeclaredClass.__init__)


def test_jsm::mdeclaredclass_constructor_args():
    sig = inspect.signature(jsm::MDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_abstractmtype_is_not_abstract():
    assert not inspect.isabstract(AbstractMType)


def test_abstractmtype_constructor_exists():
    assert callable(AbstractMType.__init__)


def test_abstractmtype_constructor_args():
    sig = inspect.signature(AbstractMType.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractminterface_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMInterface)


def test_jsm::abstractminterface_constructor_exists():
    assert callable(jsm::AbstractMInterface.__init__)


def test_jsm::abstractminterface_constructor_args():
    sig = inspect.signature(jsm::AbstractMInterface.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmclass_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMClass)


def test_jsm::abstractmclass_constructor_exists():
    assert callable(jsm::AbstractMClass.__init__)


def test_jsm::abstractmclass_constructor_args():
    sig = inspect.signature(jsm::AbstractMClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmtypewithnamedeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMTypeWithNameDeclaration)


def test_jsm::abstractmtypewithnamedeclaration_constructor_exists():
    assert callable(jsm::AbstractMTypeWithNameDeclaration.__init__)


def test_jsm::abstractmtypewithnamedeclaration_constructor_args():
    sig = inspect.signature(jsm::AbstractMTypeWithNameDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm::abstractmtypewithnamedeclaration_has_name():
    assert hasattr(jsm::AbstractMTypeWithNameDeclaration, "name")
    descriptor = None
    for klass in jsm::AbstractMTypeWithNameDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractcstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractCStatement)


def test_jsm::abstractcstatement_constructor_exists():
    assert callable(jsm::AbstractCStatement.__init__)


def test_jsm::abstractcstatement_constructor_args():
    sig = inspect.signature(jsm::AbstractCStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractmodifiers_is_not_abstract():
    assert not inspect.isabstract(AbstractModifiers)


def test_abstractmodifiers_constructor_exists():
    assert callable(AbstractModifiers.__init__)


def test_abstractmodifiers_constructor_args():
    sig = inspect.signature(AbstractModifiers.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmmethodlike_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMMethodLike)


def test_jsm::abstractmmethodlike_constructor_exists():
    assert callable(jsm::AbstractMMethodLike.__init__)


def test_jsm::abstractmmethodlike_constructor_args():
    sig = inspect.signature(jsm::AbstractMMethodLike.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmodifiers_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractModifiers)


def test_jsm::abstractmodifiers_constructor_exists():
    assert callable(jsm::AbstractModifiers.__init__)


def test_jsm::abstractmodifiers_constructor_args():
    sig = inspect.signature(jsm::AbstractModifiers.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "final" in params, "Missing parameter 'final'"

def test_jsm::abstractmodifiers_has_visibility():
    assert hasattr(jsm::AbstractModifiers, "visibility")
    descriptor = None
    for klass in jsm::AbstractModifiers.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_jsm::abstractmodifiers_has_synchronized():
    assert hasattr(jsm::AbstractModifiers, "synchronized")
    descriptor = None
    for klass in jsm::AbstractModifiers.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_jsm::abstractmodifiers_has_final():
    assert hasattr(jsm::AbstractModifiers, "final")
    descriptor = None
    for klass in jsm::AbstractModifiers.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_abstractmtypereference_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeReference)


def test_abstractmtypereference_constructor_exists():
    assert callable(AbstractMTypeReference.__init__)


def test_abstractmtypereference_constructor_args():
    sig = inspect.signature(AbstractMTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mprimitivetypereference_is_not_abstract():
    assert not inspect.isabstract(jsm::MPrimitiveTypeReference)


def test_jsm::mprimitivetypereference_constructor_exists():
    assert callable(jsm::MPrimitiveTypeReference.__init__)


def test_jsm::mprimitivetypereference_constructor_args():
    sig = inspect.signature(jsm::MPrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jsm::mprimitivetypereference_has_type():
    assert hasattr(jsm::MPrimitiveTypeReference, "type")
    descriptor = None
    for klass in jsm::MPrimitiveTypeReference.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jsm::mexternaltypereference_is_not_abstract():
    assert not inspect.isabstract(jsm::MExternalTypeReference)


def test_jsm::mexternaltypereference_constructor_exists():
    assert callable(jsm::MExternalTypeReference.__init__)


def test_jsm::mexternaltypereference_constructor_args():
    sig = inspect.signature(jsm::MExternalTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_abstractcexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractCExpression)


def test_abstractcexpression_constructor_exists():
    assert callable(AbstractCExpression.__init__)


def test_abstractcexpression_constructor_args():
    sig = inspect.signature(AbstractCExpression.__init__)
    params = list(sig.parameters.keys())



def test_jsm::cunparsedexpression_is_not_abstract():
    assert not inspect.isabstract(jsm::CUnparsedExpression)


def test_jsm::cunparsedexpression_constructor_exists():
    assert callable(jsm::CUnparsedExpression.__init__)


def test_jsm::cunparsedexpression_constructor_args():
    sig = inspect.signature(jsm::CUnparsedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jsm::cunparsedexpression_has_code():
    assert hasattr(jsm::CUnparsedExpression, "code")
    descriptor = None
    for klass in jsm::CUnparsedExpression.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_jsm::cconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(jsm::CConditionalExpression)


def test_jsm::cconditionalexpression_constructor_exists():
    assert callable(jsm::CConditionalExpression.__init__)


def test_jsm::cconditionalexpression_constructor_args():
    sig = inspect.signature(jsm::CConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractcstatement_is_not_abstract():
    assert not inspect.isabstract(AbstractCStatement)


def test_abstractcstatement_constructor_exists():
    assert callable(AbstractCStatement.__init__)


def test_abstractcstatement_constructor_args():
    sig = inspect.signature(AbstractCStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm::cifstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::CIfStatement)


def test_jsm::cifstatement_constructor_exists():
    assert callable(jsm::CIfStatement.__init__)


def test_jsm::cifstatement_constructor_args():
    sig = inspect.signature(jsm::CIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm::cdeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::CDeclarationStatement)


def test_jsm::cdeclarationstatement_constructor_exists():
    assert callable(jsm::CDeclarationStatement.__init__)


def test_jsm::cdeclarationstatement_constructor_args():
    sig = inspect.signature(jsm::CDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_jsm::cdeclarationstatement_has_final():
    assert hasattr(jsm::CDeclarationStatement, "final")
    descriptor = None
    for klass in jsm::CDeclarationStatement.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_jsm::cexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::CExpressionStatement)


def test_jsm::cexpressionstatement_constructor_exists():
    assert callable(jsm::CExpressionStatement.__init__)


def test_jsm::cexpressionstatement_constructor_args():
    sig = inspect.signature(jsm::CExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm::cunparsedstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::CUnparsedStatement)


def test_jsm::cunparsedstatement_constructor_exists():
    assert callable(jsm::CUnparsedStatement.__init__)


def test_jsm::cunparsedstatement_constructor_args():
    sig = inspect.signature(jsm::CUnparsedStatement.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jsm::cunparsedstatement_has_code():
    assert hasattr(jsm::CUnparsedStatement, "code")
    descriptor = None
    for klass in jsm::CUnparsedStatement.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_jsm::cblockstatement_is_not_abstract():
    assert not inspect.isabstract(jsm::CBlockStatement)


def test_jsm::cblockstatement_constructor_exists():
    assert callable(jsm::CBlockStatement.__init__)


def test_jsm::cblockstatement_constructor_args():
    sig = inspect.signature(jsm::CBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mconstructorparameter_is_not_abstract():
    assert not inspect.isabstract(jsm::MConstructorParameter)


def test_jsm::mconstructorparameter_constructor_exists():
    assert callable(jsm::MConstructorParameter.__init__)


def test_jsm::mconstructorparameter_constructor_args():
    sig = inspect.signature(jsm::MConstructorParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_jsm::mconstructorparameter_has_final():
    assert hasattr(jsm::MConstructorParameter, "final")
    descriptor = None
    for klass in jsm::MConstructorParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_abstractmmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(AbstractMMethodImplementation)


def test_abstractmmethodimplementation_constructor_exists():
    assert callable(AbstractMMethodImplementation.__init__)


def test_abstractmmethodimplementation_constructor_args():
    sig = inspect.signature(AbstractMMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mmethodimplementationparameter_is_not_abstract():
    assert not inspect.isabstract(jsm::MMethodImplementationParameter)


def test_jsm::mmethodimplementationparameter_constructor_exists():
    assert callable(jsm::MMethodImplementationParameter.__init__)


def test_jsm::mmethodimplementationparameter_constructor_args():
    sig = inspect.signature(jsm::MMethodImplementationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "name" in params, "Missing parameter 'name'"

def test_jsm::mmethodimplementationparameter_has_final():
    assert hasattr(jsm::MMethodImplementationParameter, "final")
    descriptor = None
    for klass in jsm::MMethodImplementationParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jsm::mmethodimplementationparameter_has_name():
    assert hasattr(jsm::MMethodImplementationParameter, "name")
    descriptor = None
    for klass in jsm::MMethodImplementationParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractmmethodlike_is_not_abstract():
    assert not inspect.isabstract(AbstractMMethodLike)


def test_abstractmmethodlike_constructor_exists():
    assert callable(AbstractMMethodLike.__init__)


def test_abstractmmethodlike_constructor_args():
    sig = inspect.signature(AbstractMMethodLike.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mconstructor_is_not_abstract():
    assert not inspect.isabstract(jsm::MConstructor)


def test_jsm::mconstructor_constructor_exists():
    assert callable(jsm::MConstructor.__init__)


def test_jsm::mconstructor_constructor_args():
    sig = inspect.signature(jsm::MConstructor.__init__)
    params = list(sig.parameters.keys())



def test_abstractmimplementablemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMImplementableMethodDeclaration)


def test_abstractmimplementablemethoddeclaration_constructor_exists():
    assert callable(AbstractMImplementableMethodDeclaration.__init__)


def test_abstractmimplementablemethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMImplementableMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mabstractclassmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MAbstractClassMethodDeclaration)


def test_jsm::mabstractclassmethoddeclaration_constructor_exists():
    assert callable(jsm::MAbstractClassMethodDeclaration.__init__)


def test_jsm::mabstractclassmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::MAbstractClassMethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_jsm::mabstractclassmethoddeclaration_has_visibility():
    assert hasattr(jsm::MAbstractClassMethodDeclaration, "visibility")
    descriptor = None
    for klass in jsm::MAbstractClassMethodDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_jsm::minterfacemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MInterfaceMethodDeclaration)


def test_jsm::minterfacemethoddeclaration_constructor_exists():
    assert callable(jsm::MInterfaceMethodDeclaration.__init__)


def test_jsm::minterfacemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::MInterfaceMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mdeclaredmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm::MDeclaredMethodImplementation)


def test_jsm::mdeclaredmethodimplementation_constructor_exists():
    assert callable(jsm::MDeclaredMethodImplementation.__init__)


def test_jsm::mdeclaredmethodimplementation_constructor_args():
    sig = inspect.signature(jsm::MDeclaredMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mdirectmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm::MDirectMethodImplementation)


def test_jsm::mdirectmethodimplementation_constructor_exists():
    assert callable(jsm::MDirectMethodImplementation.__init__)


def test_jsm::mdirectmethodimplementation_constructor_args():
    sig = inspect.signature(jsm::MDirectMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_abstractmmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMMethodDeclaration)


def test_abstractmmethoddeclaration_constructor_exists():
    assert callable(AbstractMMethodDeclaration.__init__)


def test_abstractmmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mnativemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MNativeMethodDeclaration)


def test_jsm::mnativemethoddeclaration_constructor_exists():
    assert callable(jsm::MNativeMethodDeclaration.__init__)


def test_jsm::mnativemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::MNativeMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmimplementablemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMImplementableMethodDeclaration)


def test_jsm::abstractmimplementablemethoddeclaration_constructor_exists():
    assert callable(jsm::AbstractMImplementableMethodDeclaration.__init__)


def test_jsm::abstractmimplementablemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::AbstractMImplementableMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mimplicitmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MImplicitMethodDeclaration)


def test_jsm::mimplicitmethoddeclaration_constructor_exists():
    assert callable(jsm::MImplicitMethodDeclaration.__init__)


def test_jsm::mimplicitmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm::MImplicitMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mmethoddeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(jsm::MMethodDeclarationParameter)


def test_jsm::mmethoddeclarationparameter_constructor_exists():
    assert callable(jsm::MMethodDeclarationParameter.__init__)


def test_jsm::mmethoddeclarationparameter_constructor_args():
    sig = inspect.signature(jsm::MMethodDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_abstractmclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMClassFieldDeclaration)


def test_abstractmclassfielddeclaration_constructor_exists():
    assert callable(AbstractMClassFieldDeclaration.__init__)


def test_abstractmclassfielddeclaration_constructor_args():
    sig = inspect.signature(AbstractMClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mstaticclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MStaticClassFieldDeclaration)


def test_jsm::mstaticclassfielddeclaration_constructor_exists():
    assert callable(jsm::MStaticClassFieldDeclaration.__init__)


def test_jsm::mstaticclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm::MStaticClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::minstanceclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MInstanceClassFieldDeclaration)


def test_jsm::minstanceclassfielddeclaration_constructor_exists():
    assert callable(jsm::MInstanceClassFieldDeclaration.__init__)


def test_jsm::minstanceclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm::MInstanceClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"

def test_jsm::minstanceclassfielddeclaration_has_transient():
    assert hasattr(jsm::MInstanceClassFieldDeclaration, "transient")
    descriptor = None
    for klass in jsm::MInstanceClassFieldDeclaration.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_abstractmfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMFieldDeclaration)


def test_abstractmfielddeclaration_constructor_exists():
    assert callable(AbstractMFieldDeclaration.__init__)


def test_abstractmfielddeclaration_constructor_args():
    sig = inspect.signature(AbstractMFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mconstantinterfacefielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::MConstantInterfaceFieldDeclaration)


def test_jsm::mconstantinterfacefielddeclaration_constructor_exists():
    assert callable(jsm::MConstantInterfaceFieldDeclaration.__init__)


def test_jsm::mconstantinterfacefielddeclaration_constructor_args():
    sig = inspect.signature(jsm::MConstantInterfaceFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMClassFieldDeclaration)


def test_jsm::abstractmclassfielddeclaration_constructor_exists():
    assert callable(jsm::AbstractMClassFieldDeclaration.__init__)


def test_jsm::abstractmclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm::AbstractMClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_jsm::abstractmclassfielddeclaration_has_final():
    assert hasattr(jsm::AbstractMClassFieldDeclaration, "final")
    descriptor = None
    for klass in jsm::AbstractMClassFieldDeclaration.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jsm::abstractmclassfielddeclaration_has_visibility():
    assert hasattr(jsm::AbstractMClassFieldDeclaration, "visibility")
    descriptor = None
    for klass in jsm::AbstractMClassFieldDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractcexpression_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractCExpression)


def test_jsm::abstractcexpression_constructor_exists():
    assert callable(jsm::AbstractCExpression.__init__)


def test_jsm::abstractcexpression_constructor_args():
    sig = inspect.signature(jsm::AbstractCExpression.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mdeclaredtypereference_is_not_abstract():
    assert not inspect.isabstract(jsm::MDeclaredTypeReference)


def test_jsm::mdeclaredtypereference_constructor_exists():
    assert callable(jsm::MDeclaredTypeReference.__init__)


def test_jsm::mdeclaredtypereference_constructor_args():
    sig = inspect.signature(jsm::MDeclaredTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmtypereference_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMTypeReference)


def test_jsm::abstractmtypereference_constructor_exists():
    assert callable(jsm::AbstractMTypeReference.__init__)


def test_jsm::abstractmtypereference_constructor_args():
    sig = inspect.signature(jsm::AbstractMTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_jsm::abstractmtypereference_has_array():
    assert hasattr(jsm::AbstractMTypeReference, "array")
    descriptor = None
    for klass in jsm::AbstractMTypeReference.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractmmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMMethodImplementation)


def test_jsm::abstractmmethodimplementation_constructor_exists():
    assert callable(jsm::AbstractMMethodImplementation.__init__)


def test_jsm::abstractmmethodimplementation_constructor_args():
    sig = inspect.signature(jsm::AbstractMMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmtype_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMType)


def test_jsm::abstractmtype_constructor_exists():
    assert callable(jsm::AbstractMType.__init__)


def test_jsm::abstractmtype_constructor_args():
    sig = inspect.signature(jsm::AbstractMType.__init__)
    params = list(sig.parameters.keys())



def test_abstractmtypecontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeContainer)


def test_abstractmtypecontainer_constructor_exists():
    assert callable(AbstractMTypeContainer.__init__)


def test_abstractmtypecontainer_constructor_args():
    sig = inspect.signature(AbstractMTypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_jsm::abstractmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMDeclaredType)


def test_jsm::abstractmdeclaredtype_constructor_exists():
    assert callable(jsm::AbstractMDeclaredType.__init__)


def test_jsm::abstractmdeclaredtype_constructor_args():
    sig = inspect.signature(jsm::AbstractMDeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm::abstractmdeclaredtype_has_name():
    assert hasattr(jsm::AbstractMDeclaredType, "name")
    descriptor = None
    for klass in jsm::AbstractMDeclaredType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractmtypecontainer_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMTypeContainer)


def test_jsm::abstractmtypecontainer_constructor_exists():
    assert callable(jsm::AbstractMTypeContainer.__init__)


def test_jsm::abstractmtypecontainer_constructor_args():
    sig = inspect.signature(jsm::AbstractMTypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_abstractmresource_is_not_abstract():
    assert not inspect.isabstract(AbstractMResource)


def test_abstractmresource_constructor_exists():
    assert callable(AbstractMResource.__init__)


def test_abstractmresource_constructor_args():
    sig = inspect.signature(AbstractMResource.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mcompilationunit_is_not_abstract():
    assert not inspect.isabstract(jsm::MCompilationUnit)


def test_jsm::mcompilationunit_constructor_exists():
    assert callable(jsm::MCompilationUnit.__init__)


def test_jsm::mcompilationunit_constructor_args():
    sig = inspect.signature(jsm::MCompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mresource_is_not_abstract():
    assert not inspect.isabstract(jsm::MResource)


def test_jsm::mresource_constructor_exists():
    assert callable(jsm::MResource.__init__)


def test_jsm::mresource_constructor_args():
    sig = inspect.signature(jsm::MResource.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_jsm::mresource_has_content():
    assert hasattr(jsm::MResource, "content")
    descriptor = None
    for klass in jsm::MResource.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractmresource_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMResource)


def test_jsm::abstractmresource_constructor_exists():
    assert callable(jsm::AbstractMResource.__init__)


def test_jsm::abstractmresource_constructor_args():
    sig = inspect.signature(jsm::AbstractMResource.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "name" in params, "Missing parameter 'name'"

def test_jsm::abstractmresource_has_derived():
    assert hasattr(jsm::AbstractMResource, "derived")
    descriptor = None
    for klass in jsm::AbstractMResource.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_jsm::abstractmresource_has_name():
    assert hasattr(jsm::AbstractMResource, "name")
    descriptor = None
    for klass in jsm::AbstractMResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractmexternaltype_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMExternalType)


def test_jsm::abstractmexternaltype_constructor_exists():
    assert callable(jsm::AbstractMExternalType.__init__)


def test_jsm::abstractmexternaltype_constructor_args():
    sig = inspect.signature(jsm::AbstractMExternalType.__init__)
    params = list(sig.parameters.keys())
    assert "fullQualifiedName" in params, "Missing parameter 'fullQualifiedName'"

def test_jsm::abstractmexternaltype_has_fullQualifiedName():
    assert hasattr(jsm::AbstractMExternalType, "fullQualifiedName")
    descriptor = None
    for klass in jsm::AbstractMExternalType.__mro__:
        if "fullQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_jsm::abstractmpackagecontainer_is_not_abstract():
    assert not inspect.isabstract(jsm::AbstractMPackageContainer)


def test_jsm::abstractmpackagecontainer_constructor_exists():
    assert callable(jsm::AbstractMPackageContainer.__init__)


def test_jsm::abstractmpackagecontainer_constructor_args():
    sig = inspect.signature(jsm::AbstractMPackageContainer.__init__)
    params = list(sig.parameters.keys())



def test_abstractmpackagecontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractMPackageContainer)


def test_abstractmpackagecontainer_constructor_exists():
    assert callable(AbstractMPackageContainer.__init__)


def test_abstractmpackagecontainer_constructor_args():
    sig = inspect.signature(AbstractMPackageContainer.__init__)
    params = list(sig.parameters.keys())



def test_jsm::mpackage_is_not_abstract():
    assert not inspect.isabstract(jsm::MPackage)


def test_jsm::mpackage_constructor_exists():
    assert callable(jsm::MPackage.__init__)


def test_jsm::mpackage_constructor_args():
    sig = inspect.signature(jsm::MPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm::mpackage_has_name():
    assert hasattr(jsm::MPackage, "name")
    descriptor = None
    for klass in jsm::MPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm::mroot_is_not_abstract():
    assert not inspect.isabstract(jsm::MRoot)


def test_jsm::mroot_constructor_exists():
    assert callable(jsm::MRoot.__init__)


def test_jsm::mroot_constructor_args():
    sig = inspect.signature(jsm::MRoot.__init__)
    params = list(sig.parameters.keys())

def test_mprimitivetypes_exists():
    # Check that the Enumeration exists
    assert MPrimitiveTypes is not None

def test_mprimitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MPrimitiveTypes]
    expected_literals = [
        "boolean",
        "int",
        "char",
        "long",
        "double",
        "float",
        "short",
        "byte",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MPrimitiveTypes"

def test_mvisibility_exists():
    # Check that the Enumeration exists
    assert MVisibility is not None

def test_mvisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MVisibility]
    expected_literals = [
        "DEFAULT",
        "PUBLIC",
        "PROTECTED",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MVisibility"


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
AbstractMTypeWithNameDeclaration_strategy = st.builds(
    AbstractMTypeWithNameDeclaration,
)
jsm::AbstractMFieldDeclaration_strategy = st.builds(
    jsm::AbstractMFieldDeclaration,
)
AbstractMInterface_strategy = st.builds(
    AbstractMInterface,
)
AbstractMExternalType_strategy = st.builds(
    AbstractMExternalType,
)
jsm::MExternalInterface_strategy = st.builds(
    jsm::MExternalInterface,
)
MDeclaredClass_strategy = st.builds(
    MDeclaredClass,
)
jsm::MAbstractDeclaredClass_strategy = st.builds(
    jsm::MAbstractDeclaredClass,
)
jsm::AbstractMMethodDeclaration_strategy = st.builds(
    jsm::AbstractMMethodDeclaration,
)
AbstractMDeclaredType_strategy = st.builds(
    AbstractMDeclaredType,
)
jsm::MDeclaredInterface_strategy = st.builds(
    jsm::MDeclaredInterface,
)
AbstractMClass_strategy = st.builds(
    AbstractMClass,
)
jsm::MExternalClass_strategy = st.builds(
    jsm::MExternalClass,
)
jsm::MDeclaredClass_strategy = st.builds(
    jsm::MDeclaredClass,
)
AbstractMType_strategy = st.builds(
    AbstractMType,
)
jsm::AbstractMInterface_strategy = st.builds(
    jsm::AbstractMInterface,
)
jsm::AbstractMClass_strategy = st.builds(
    jsm::AbstractMClass,
)
jsm::AbstractMTypeWithNameDeclaration_strategy = st.builds(
    jsm::AbstractMTypeWithNameDeclaration,
    name=
        safe_text
)
jsm::AbstractCStatement_strategy = st.builds(
    jsm::AbstractCStatement,
)
AbstractModifiers_strategy = st.builds(
    AbstractModifiers,
)
jsm::AbstractMMethodLike_strategy = st.builds(
    jsm::AbstractMMethodLike,
)
jsm::AbstractModifiers_strategy = st.builds(
    jsm::AbstractModifiers,
    visibility=
        safe_text,
    synchronized=
        st.booleans(),
    final=
        st.booleans()
)
AbstractMTypeReference_strategy = st.builds(
    AbstractMTypeReference,
)
jsm::MPrimitiveTypeReference_strategy = st.builds(
    jsm::MPrimitiveTypeReference,
    type=
        safe_text
)
jsm::MExternalTypeReference_strategy = st.builds(
    jsm::MExternalTypeReference,
)
AbstractCExpression_strategy = st.builds(
    AbstractCExpression,
)
jsm::CUnparsedExpression_strategy = st.builds(
    jsm::CUnparsedExpression,
    code=
        safe_text
)
jsm::CConditionalExpression_strategy = st.builds(
    jsm::CConditionalExpression,
)
AbstractCStatement_strategy = st.builds(
    AbstractCStatement,
)
jsm::CIfStatement_strategy = st.builds(
    jsm::CIfStatement,
)
jsm::CDeclarationStatement_strategy = st.builds(
    jsm::CDeclarationStatement,
    final=
        st.booleans()
)
jsm::CExpressionStatement_strategy = st.builds(
    jsm::CExpressionStatement,
)
jsm::CUnparsedStatement_strategy = st.builds(
    jsm::CUnparsedStatement,
    code=
        safe_text
)
jsm::CBlockStatement_strategy = st.builds(
    jsm::CBlockStatement,
)
jsm::MConstructorParameter_strategy = st.builds(
    jsm::MConstructorParameter,
    final=
        st.booleans()
)
AbstractMMethodImplementation_strategy = st.builds(
    AbstractMMethodImplementation,
)
jsm::MMethodImplementationParameter_strategy = st.builds(
    jsm::MMethodImplementationParameter,
    final=
        st.booleans(),
    name=
        safe_text
)
AbstractMMethodLike_strategy = st.builds(
    AbstractMMethodLike,
)
jsm::MConstructor_strategy = st.builds(
    jsm::MConstructor,
)
AbstractMImplementableMethodDeclaration_strategy = st.builds(
    AbstractMImplementableMethodDeclaration,
)
jsm::MAbstractClassMethodDeclaration_strategy = st.builds(
    jsm::MAbstractClassMethodDeclaration,
    visibility=
        safe_text
)
jsm::MInterfaceMethodDeclaration_strategy = st.builds(
    jsm::MInterfaceMethodDeclaration,
)
jsm::MDeclaredMethodImplementation_strategy = st.builds(
    jsm::MDeclaredMethodImplementation,
)
jsm::MDirectMethodImplementation_strategy = st.builds(
    jsm::MDirectMethodImplementation,
)
AbstractMMethodDeclaration_strategy = st.builds(
    AbstractMMethodDeclaration,
)
jsm::MNativeMethodDeclaration_strategy = st.builds(
    jsm::MNativeMethodDeclaration,
)
jsm::AbstractMImplementableMethodDeclaration_strategy = st.builds(
    jsm::AbstractMImplementableMethodDeclaration,
)
jsm::MImplicitMethodDeclaration_strategy = st.builds(
    jsm::MImplicitMethodDeclaration,
)
jsm::MMethodDeclarationParameter_strategy = st.builds(
    jsm::MMethodDeclarationParameter,
)
AbstractMClassFieldDeclaration_strategy = st.builds(
    AbstractMClassFieldDeclaration,
)
jsm::MStaticClassFieldDeclaration_strategy = st.builds(
    jsm::MStaticClassFieldDeclaration,
)
jsm::MInstanceClassFieldDeclaration_strategy = st.builds(
    jsm::MInstanceClassFieldDeclaration,
    transient=
        st.booleans()
)
AbstractMFieldDeclaration_strategy = st.builds(
    AbstractMFieldDeclaration,
)
jsm::MConstantInterfaceFieldDeclaration_strategy = st.builds(
    jsm::MConstantInterfaceFieldDeclaration,
)
jsm::AbstractMClassFieldDeclaration_strategy = st.builds(
    jsm::AbstractMClassFieldDeclaration,
    final=
        st.booleans(),
    visibility=
        safe_text
)
jsm::AbstractCExpression_strategy = st.builds(
    jsm::AbstractCExpression,
)
jsm::MDeclaredTypeReference_strategy = st.builds(
    jsm::MDeclaredTypeReference,
)
jsm::AbstractMTypeReference_strategy = st.builds(
    jsm::AbstractMTypeReference,
    array=
        st.booleans()
)
jsm::AbstractMMethodImplementation_strategy = st.builds(
    jsm::AbstractMMethodImplementation,
)
jsm::AbstractMType_strategy = st.builds(
    jsm::AbstractMType,
)
AbstractMTypeContainer_strategy = st.builds(
    AbstractMTypeContainer,
)
jsm::AbstractMDeclaredType_strategy = st.builds(
    jsm::AbstractMDeclaredType,
    name=
        safe_text
)
jsm::AbstractMTypeContainer_strategy = st.builds(
    jsm::AbstractMTypeContainer,
)
AbstractMResource_strategy = st.builds(
    AbstractMResource,
)
jsm::MCompilationUnit_strategy = st.builds(
    jsm::MCompilationUnit,
)
jsm::MResource_strategy = st.builds(
    jsm::MResource,
    content=
        safe_text
)
jsm::AbstractMResource_strategy = st.builds(
    jsm::AbstractMResource,
    derived=
        st.booleans(),
    name=
        safe_text
)
jsm::AbstractMExternalType_strategy = st.builds(
    jsm::AbstractMExternalType,
    fullQualifiedName=
        safe_text
)
jsm::AbstractMPackageContainer_strategy = st.builds(
    jsm::AbstractMPackageContainer,
)
AbstractMPackageContainer_strategy = st.builds(
    AbstractMPackageContainer,
)
jsm::MPackage_strategy = st.builds(
    jsm::MPackage,
    name=
        safe_text
)
jsm::MRoot_strategy = st.builds(
    jsm::MRoot,
)

@given(instance=AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmtypewithnamedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)

@given(instance=jsm::AbstractMFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::abstractmfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMFieldDeclaration)

@given(instance=AbstractMInterface_strategy)
@settings(max_examples=50)
def test_abstractminterface_instantiation(instance):
    assert isinstance(instance, AbstractMInterface)

@given(instance=AbstractMExternalType_strategy)
@settings(max_examples=50)
def test_abstractmexternaltype_instantiation(instance):
    assert isinstance(instance, AbstractMExternalType)

@given(instance=jsm::MExternalInterface_strategy)
@settings(max_examples=50)
def test_jsm::mexternalinterface_instantiation(instance):
    assert isinstance(instance, jsm::MExternalInterface)

@given(instance=MDeclaredClass_strategy)
@settings(max_examples=50)
def test_mdeclaredclass_instantiation(instance):
    assert isinstance(instance, MDeclaredClass)

@given(instance=jsm::MAbstractDeclaredClass_strategy)
@settings(max_examples=50)
def test_jsm::mabstractdeclaredclass_instantiation(instance):
    assert isinstance(instance, jsm::MAbstractDeclaredClass)

@given(instance=jsm::AbstractMMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::abstractmmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMMethodDeclaration)

@given(instance=AbstractMDeclaredType_strategy)
@settings(max_examples=50)
def test_abstractmdeclaredtype_instantiation(instance):
    assert isinstance(instance, AbstractMDeclaredType)

@given(instance=jsm::MDeclaredInterface_strategy)
@settings(max_examples=50)
def test_jsm::mdeclaredinterface_instantiation(instance):
    assert isinstance(instance, jsm::MDeclaredInterface)

@given(instance=AbstractMClass_strategy)
@settings(max_examples=50)
def test_abstractmclass_instantiation(instance):
    assert isinstance(instance, AbstractMClass)

@given(instance=jsm::MExternalClass_strategy)
@settings(max_examples=50)
def test_jsm::mexternalclass_instantiation(instance):
    assert isinstance(instance, jsm::MExternalClass)

@given(instance=jsm::MDeclaredClass_strategy)
@settings(max_examples=50)
def test_jsm::mdeclaredclass_instantiation(instance):
    assert isinstance(instance, jsm::MDeclaredClass)

@given(instance=AbstractMType_strategy)
@settings(max_examples=50)
def test_abstractmtype_instantiation(instance):
    assert isinstance(instance, AbstractMType)

@given(instance=jsm::AbstractMInterface_strategy)
@settings(max_examples=50)
def test_jsm::abstractminterface_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMInterface)

@given(instance=jsm::AbstractMClass_strategy)
@settings(max_examples=50)
def test_jsm::abstractmclass_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMClass)

@given(instance=jsm::AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::abstractmtypewithnamedeclaration_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMTypeWithNameDeclaration)

@given(instance=jsm::AbstractMTypeWithNameDeclaration_strategy)
def test_jsm::abstractmtypewithnamedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jsm::AbstractMTypeWithNameDeclaration_strategy)
def test_jsm::abstractmtypewithnamedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm::AbstractCStatement_strategy)
@settings(max_examples=50)
def test_jsm::abstractcstatement_instantiation(instance):
    assert isinstance(instance, jsm::AbstractCStatement)

@given(instance=AbstractModifiers_strategy)
@settings(max_examples=50)
def test_abstractmodifiers_instantiation(instance):
    assert isinstance(instance, AbstractModifiers)

@given(instance=jsm::AbstractMMethodLike_strategy)
@settings(max_examples=50)
def test_jsm::abstractmmethodlike_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMMethodLike)

@given(instance=jsm::AbstractModifiers_strategy)
@settings(max_examples=50)
def test_jsm::abstractmodifiers_instantiation(instance):
    assert isinstance(instance, jsm::AbstractModifiers)

@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=jsm::AbstractModifiers_strategy)
def test_jsm::abstractmodifiers_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=AbstractMTypeReference_strategy)
@settings(max_examples=50)
def test_abstractmtypereference_instantiation(instance):
    assert isinstance(instance, AbstractMTypeReference)

@given(instance=jsm::MPrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_jsm::mprimitivetypereference_instantiation(instance):
    assert isinstance(instance, jsm::MPrimitiveTypeReference)

@given(instance=jsm::MPrimitiveTypeReference_strategy)
def test_jsm::mprimitivetypereference_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jsm::MPrimitiveTypeReference_strategy)
def test_jsm::mprimitivetypereference_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jsm::MExternalTypeReference_strategy)
@settings(max_examples=50)
def test_jsm::mexternaltypereference_instantiation(instance):
    assert isinstance(instance, jsm::MExternalTypeReference)

@given(instance=AbstractCExpression_strategy)
@settings(max_examples=50)
def test_abstractcexpression_instantiation(instance):
    assert isinstance(instance, AbstractCExpression)

@given(instance=jsm::CUnparsedExpression_strategy)
@settings(max_examples=50)
def test_jsm::cunparsedexpression_instantiation(instance):
    assert isinstance(instance, jsm::CUnparsedExpression)

@given(instance=jsm::CUnparsedExpression_strategy)
def test_jsm::cunparsedexpression_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=jsm::CUnparsedExpression_strategy)
def test_jsm::cunparsedexpression_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=jsm::CConditionalExpression_strategy)
@settings(max_examples=50)
def test_jsm::cconditionalexpression_instantiation(instance):
    assert isinstance(instance, jsm::CConditionalExpression)

@given(instance=AbstractCStatement_strategy)
@settings(max_examples=50)
def test_abstractcstatement_instantiation(instance):
    assert isinstance(instance, AbstractCStatement)

@given(instance=jsm::CIfStatement_strategy)
@settings(max_examples=50)
def test_jsm::cifstatement_instantiation(instance):
    assert isinstance(instance, jsm::CIfStatement)

@given(instance=jsm::CDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jsm::cdeclarationstatement_instantiation(instance):
    assert isinstance(instance, jsm::CDeclarationStatement)

@given(instance=jsm::CDeclarationStatement_strategy)
def test_jsm::cdeclarationstatement_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=jsm::CDeclarationStatement_strategy)
def test_jsm::cdeclarationstatement_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=jsm::CExpressionStatement_strategy)
@settings(max_examples=50)
def test_jsm::cexpressionstatement_instantiation(instance):
    assert isinstance(instance, jsm::CExpressionStatement)

@given(instance=jsm::CUnparsedStatement_strategy)
@settings(max_examples=50)
def test_jsm::cunparsedstatement_instantiation(instance):
    assert isinstance(instance, jsm::CUnparsedStatement)

@given(instance=jsm::CUnparsedStatement_strategy)
def test_jsm::cunparsedstatement_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=jsm::CUnparsedStatement_strategy)
def test_jsm::cunparsedstatement_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=jsm::CBlockStatement_strategy)
@settings(max_examples=50)
def test_jsm::cblockstatement_instantiation(instance):
    assert isinstance(instance, jsm::CBlockStatement)

@given(instance=jsm::MConstructorParameter_strategy)
@settings(max_examples=50)
def test_jsm::mconstructorparameter_instantiation(instance):
    assert isinstance(instance, jsm::MConstructorParameter)

@given(instance=jsm::MConstructorParameter_strategy)
def test_jsm::mconstructorparameter_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=jsm::MConstructorParameter_strategy)
def test_jsm::mconstructorparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=AbstractMMethodImplementation_strategy)
@settings(max_examples=50)
def test_abstractmmethodimplementation_instantiation(instance):
    assert isinstance(instance, AbstractMMethodImplementation)

@given(instance=jsm::MMethodImplementationParameter_strategy)
@settings(max_examples=50)
def test_jsm::mmethodimplementationparameter_instantiation(instance):
    assert isinstance(instance, jsm::MMethodImplementationParameter)

@given(instance=jsm::MMethodImplementationParameter_strategy)
def test_jsm::mmethodimplementationparameter_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=jsm::MMethodImplementationParameter_strategy)
def test_jsm::mmethodimplementationparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=jsm::MMethodImplementationParameter_strategy)
def test_jsm::mmethodimplementationparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jsm::MMethodImplementationParameter_strategy)
def test_jsm::mmethodimplementationparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractMMethodLike_strategy)
@settings(max_examples=50)
def test_abstractmmethodlike_instantiation(instance):
    assert isinstance(instance, AbstractMMethodLike)

@given(instance=jsm::MConstructor_strategy)
@settings(max_examples=50)
def test_jsm::mconstructor_instantiation(instance):
    assert isinstance(instance, jsm::MConstructor)

@given(instance=AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmimplementablemethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMImplementableMethodDeclaration)

@given(instance=jsm::MAbstractClassMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::mabstractclassmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MAbstractClassMethodDeclaration)

@given(instance=jsm::MAbstractClassMethodDeclaration_strategy)
def test_jsm::mabstractclassmethoddeclaration_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=jsm::MAbstractClassMethodDeclaration_strategy)
def test_jsm::mabstractclassmethoddeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=jsm::MInterfaceMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::minterfacemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MInterfaceMethodDeclaration)

@given(instance=jsm::MDeclaredMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm::mdeclaredmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm::MDeclaredMethodImplementation)

@given(instance=jsm::MDirectMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm::mdirectmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm::MDirectMethodImplementation)

@given(instance=AbstractMMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMMethodDeclaration)

@given(instance=jsm::MNativeMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::mnativemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MNativeMethodDeclaration)

@given(instance=jsm::AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::abstractmimplementablemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMImplementableMethodDeclaration)

@given(instance=jsm::MImplicitMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::mimplicitmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MImplicitMethodDeclaration)

@given(instance=jsm::MMethodDeclarationParameter_strategy)
@settings(max_examples=50)
def test_jsm::mmethoddeclarationparameter_instantiation(instance):
    assert isinstance(instance, jsm::MMethodDeclarationParameter)

@given(instance=AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMClassFieldDeclaration)

@given(instance=jsm::MStaticClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::mstaticclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MStaticClassFieldDeclaration)

@given(instance=jsm::MInstanceClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::minstanceclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MInstanceClassFieldDeclaration)

@given(instance=jsm::MInstanceClassFieldDeclaration_strategy)
def test_jsm::minstanceclassfielddeclaration_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=jsm::MInstanceClassFieldDeclaration_strategy)
def test_jsm::minstanceclassfielddeclaration_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=AbstractMFieldDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmfielddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMFieldDeclaration)

@given(instance=jsm::MConstantInterfaceFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::mconstantinterfacefielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::MConstantInterfaceFieldDeclaration)

@given(instance=jsm::AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm::abstractmclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMClassFieldDeclaration)

@given(instance=jsm::AbstractMClassFieldDeclaration_strategy)
def test_jsm::abstractmclassfielddeclaration_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=jsm::AbstractMClassFieldDeclaration_strategy)
def test_jsm::abstractmclassfielddeclaration_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=jsm::AbstractMClassFieldDeclaration_strategy)
def test_jsm::abstractmclassfielddeclaration_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=jsm::AbstractMClassFieldDeclaration_strategy)
def test_jsm::abstractmclassfielddeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=jsm::AbstractCExpression_strategy)
@settings(max_examples=50)
def test_jsm::abstractcexpression_instantiation(instance):
    assert isinstance(instance, jsm::AbstractCExpression)

@given(instance=jsm::MDeclaredTypeReference_strategy)
@settings(max_examples=50)
def test_jsm::mdeclaredtypereference_instantiation(instance):
    assert isinstance(instance, jsm::MDeclaredTypeReference)

@given(instance=jsm::AbstractMTypeReference_strategy)
@settings(max_examples=50)
def test_jsm::abstractmtypereference_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMTypeReference)

@given(instance=jsm::AbstractMTypeReference_strategy)
def test_jsm::abstractmtypereference_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=jsm::AbstractMTypeReference_strategy)
def test_jsm::abstractmtypereference_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=jsm::AbstractMMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm::abstractmmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMMethodImplementation)

@given(instance=jsm::AbstractMType_strategy)
@settings(max_examples=50)
def test_jsm::abstractmtype_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMType)

@given(instance=AbstractMTypeContainer_strategy)
@settings(max_examples=50)
def test_abstractmtypecontainer_instantiation(instance):
    assert isinstance(instance, AbstractMTypeContainer)

@given(instance=jsm::AbstractMDeclaredType_strategy)
@settings(max_examples=50)
def test_jsm::abstractmdeclaredtype_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMDeclaredType)

@given(instance=jsm::AbstractMDeclaredType_strategy)
def test_jsm::abstractmdeclaredtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jsm::AbstractMDeclaredType_strategy)
def test_jsm::abstractmdeclaredtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm::AbstractMTypeContainer_strategy)
@settings(max_examples=50)
def test_jsm::abstractmtypecontainer_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMTypeContainer)

@given(instance=AbstractMResource_strategy)
@settings(max_examples=50)
def test_abstractmresource_instantiation(instance):
    assert isinstance(instance, AbstractMResource)

@given(instance=jsm::MCompilationUnit_strategy)
@settings(max_examples=50)
def test_jsm::mcompilationunit_instantiation(instance):
    assert isinstance(instance, jsm::MCompilationUnit)

@given(instance=jsm::MResource_strategy)
@settings(max_examples=50)
def test_jsm::mresource_instantiation(instance):
    assert isinstance(instance, jsm::MResource)

@given(instance=jsm::MResource_strategy)
def test_jsm::mresource_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=jsm::MResource_strategy)
def test_jsm::mresource_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=jsm::AbstractMResource_strategy)
@settings(max_examples=50)
def test_jsm::abstractmresource_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMResource)

@given(instance=jsm::AbstractMResource_strategy)
def test_jsm::abstractmresource_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=jsm::AbstractMResource_strategy)
def test_jsm::abstractmresource_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=jsm::AbstractMResource_strategy)
def test_jsm::abstractmresource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jsm::AbstractMResource_strategy)
def test_jsm::abstractmresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm::AbstractMExternalType_strategy)
@settings(max_examples=50)
def test_jsm::abstractmexternaltype_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMExternalType)

@given(instance=jsm::AbstractMExternalType_strategy)
def test_jsm::abstractmexternaltype_fullQualifiedName_type(instance):
    assert isinstance(instance.fullQualifiedName, str)


@given(instance=jsm::AbstractMExternalType_strategy)
def test_jsm::abstractmexternaltype_fullQualifiedName_setter(instance):
    original = instance.fullQualifiedName
    instance.fullQualifiedName = original
    assert instance.fullQualifiedName == original

@given(instance=jsm::AbstractMPackageContainer_strategy)
@settings(max_examples=50)
def test_jsm::abstractmpackagecontainer_instantiation(instance):
    assert isinstance(instance, jsm::AbstractMPackageContainer)

@given(instance=AbstractMPackageContainer_strategy)
@settings(max_examples=50)
def test_abstractmpackagecontainer_instantiation(instance):
    assert isinstance(instance, AbstractMPackageContainer)

@given(instance=jsm::MPackage_strategy)
@settings(max_examples=50)
def test_jsm::mpackage_instantiation(instance):
    assert isinstance(instance, jsm::MPackage)

@given(instance=jsm::MPackage_strategy)
def test_jsm::mpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jsm::MPackage_strategy)
def test_jsm::mpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm::MRoot_strategy)
@settings(max_examples=50)
def test_jsm::mroot_instantiation(instance):
    assert isinstance(instance, jsm::MRoot)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractMType,
    jsm_AbstractMClass,
    jsm_AbstractMTypeWithNameDeclaration,
    jsm_AbstractCStatement,
    AbstractModifiers,
    jsm_AbstractMMethodLike,
    jsm_AbstractModifiers,
    AbstractCExpression,
    jsm_CUnparsedExpression,
    jsm_CConditionalExpression,
    AbstractCStatement,
    jsm_CUnparsedStatement,
    jsm_CExpressionStatement,
    jsm_CIfStatement,
    jsm_CBlockStatement,
    AbstractMMethodImplementation,
    jsm_MMethodImplementationParameter,
    AbstractMMethodLike,
    AbstractMImplementableMethodDeclaration,
    jsm_MDeclaredMethodImplementation,
    jsm_MDirectMethodImplementation,
    AbstractMMethodDeclaration,
    jsm_AbstractMImplementableMethodDeclaration,
    jsm_MImplicitMethodDeclaration,
    AbstractMClassFieldDeclaration,
    AbstractMFieldDeclaration,
    jsm_AbstractMClassFieldDeclaration,
    jsm_AbstractCExpression,
    AbstractMTypeWithNameDeclaration,
    jsm_MConstructorParameter,
    jsm_MMethodDeclarationParameter,
    jsm_CDeclarationStatement,
    jsm_AbstractMFieldDeclaration,
    jsm_MInterfaceMethodDeclaration,
    jsm_MConstantInterfaceFieldDeclaration,
    AbstractMInterface,
    AbstractMExternalType,
    jsm_MExternalInterface,
    jsm_MAbstractClassMethodDeclaration,
    MDeclaredClass,
    jsm_MAbstractDeclaredClass,
    jsm_MNativeMethodDeclaration,
    jsm_AbstractMMethodDeclaration,
    jsm_MConstructor,
    jsm_MInstanceClassFieldDeclaration,
    jsm_MStaticClassFieldDeclaration,
    jsm_AbstractMInterface,
    AbstractMDeclaredType,
    jsm_MDeclaredInterface,
    AbstractMClass,
    jsm_MExternalClass,
    jsm_MDeclaredClass,
    AbstractMTypeReference,
    jsm_MPrimitiveTypeReference,
    jsm_MExternalTypeReference,
    jsm_MDeclaredTypeReference,
    jsm_AbstractMTypeReference,
    jsm_AbstractMMethodImplementation,
    jsm_AbstractMType,
    AbstractMTypeContainer,
    jsm_AbstractMDeclaredType,
    jsm_AbstractMTypeContainer,
    AbstractMResource,
    jsm_MCompilationUnit,
    jsm_MResource,
    jsm_AbstractMResource,
    jsm_AbstractMExternalType,
    jsm_AbstractMPackageContainer,
    AbstractMPackageContainer,
    jsm_MPackage,
    jsm_MRoot,
    MPrimitiveTypes,
    MVisibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractmtype_is_not_abstract():
    assert not inspect.isabstract(AbstractMType)


def test_abstractmtype_constructor_exists():
    assert callable(AbstractMType.__init__)


def test_abstractmtype_constructor_args():
    sig = inspect.signature(AbstractMType.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmclass_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMClass)


def test_jsm_abstractmclass_constructor_exists():
    assert callable(jsm_AbstractMClass.__init__)


def test_jsm_abstractmclass_constructor_args():
    sig = inspect.signature(jsm_AbstractMClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmtypewithnamedeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMTypeWithNameDeclaration)


def test_jsm_abstractmtypewithnamedeclaration_constructor_exists():
    assert callable(jsm_AbstractMTypeWithNameDeclaration.__init__)


def test_jsm_abstractmtypewithnamedeclaration_constructor_args():
    sig = inspect.signature(jsm_AbstractMTypeWithNameDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm_abstractmtypewithnamedeclaration_has_name():
    assert hasattr(jsm_AbstractMTypeWithNameDeclaration, "name")
    descriptor = None
    for klass in jsm_AbstractMTypeWithNameDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractcstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractCStatement)


def test_jsm_abstractcstatement_constructor_exists():
    assert callable(jsm_AbstractCStatement.__init__)


def test_jsm_abstractcstatement_constructor_args():
    sig = inspect.signature(jsm_AbstractCStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractmodifiers_is_not_abstract():
    assert not inspect.isabstract(AbstractModifiers)


def test_abstractmodifiers_constructor_exists():
    assert callable(AbstractModifiers.__init__)


def test_abstractmodifiers_constructor_args():
    sig = inspect.signature(AbstractModifiers.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmmethodlike_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMMethodLike)


def test_jsm_abstractmmethodlike_constructor_exists():
    assert callable(jsm_AbstractMMethodLike.__init__)


def test_jsm_abstractmmethodlike_constructor_args():
    sig = inspect.signature(jsm_AbstractMMethodLike.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmodifiers_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractModifiers)


def test_jsm_abstractmodifiers_constructor_exists():
    assert callable(jsm_AbstractModifiers.__init__)


def test_jsm_abstractmodifiers_constructor_args():
    sig = inspect.signature(jsm_AbstractModifiers.__init__)
    params = list(sig.parameters.keys())
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "final" in params, "Missing parameter 'final'"

def test_jsm_abstractmodifiers_has_synchronized():
    assert hasattr(jsm_AbstractModifiers, "synchronized")
    descriptor = None
    for klass in jsm_AbstractModifiers.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_jsm_abstractmodifiers_has_visibility():
    assert hasattr(jsm_AbstractModifiers, "visibility")
    descriptor = None
    for klass in jsm_AbstractModifiers.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_jsm_abstractmodifiers_has_final():
    assert hasattr(jsm_AbstractModifiers, "final")
    descriptor = None
    for klass in jsm_AbstractModifiers.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_abstractcexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractCExpression)


def test_abstractcexpression_constructor_exists():
    assert callable(AbstractCExpression.__init__)


def test_abstractcexpression_constructor_args():
    sig = inspect.signature(AbstractCExpression.__init__)
    params = list(sig.parameters.keys())



def test_jsm_cunparsedexpression_is_not_abstract():
    assert not inspect.isabstract(jsm_CUnparsedExpression)


def test_jsm_cunparsedexpression_constructor_exists():
    assert callable(jsm_CUnparsedExpression.__init__)


def test_jsm_cunparsedexpression_constructor_args():
    sig = inspect.signature(jsm_CUnparsedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jsm_cunparsedexpression_has_code():
    assert hasattr(jsm_CUnparsedExpression, "code")
    descriptor = None
    for klass in jsm_CUnparsedExpression.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_jsm_cconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(jsm_CConditionalExpression)


def test_jsm_cconditionalexpression_constructor_exists():
    assert callable(jsm_CConditionalExpression.__init__)


def test_jsm_cconditionalexpression_constructor_args():
    sig = inspect.signature(jsm_CConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractcstatement_is_not_abstract():
    assert not inspect.isabstract(AbstractCStatement)


def test_abstractcstatement_constructor_exists():
    assert callable(AbstractCStatement.__init__)


def test_abstractcstatement_constructor_args():
    sig = inspect.signature(AbstractCStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm_cunparsedstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_CUnparsedStatement)


def test_jsm_cunparsedstatement_constructor_exists():
    assert callable(jsm_CUnparsedStatement.__init__)


def test_jsm_cunparsedstatement_constructor_args():
    sig = inspect.signature(jsm_CUnparsedStatement.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jsm_cunparsedstatement_has_code():
    assert hasattr(jsm_CUnparsedStatement, "code")
    descriptor = None
    for klass in jsm_CUnparsedStatement.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_jsm_cexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_CExpressionStatement)


def test_jsm_cexpressionstatement_constructor_exists():
    assert callable(jsm_CExpressionStatement.__init__)


def test_jsm_cexpressionstatement_constructor_args():
    sig = inspect.signature(jsm_CExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm_cifstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_CIfStatement)


def test_jsm_cifstatement_constructor_exists():
    assert callable(jsm_CIfStatement.__init__)


def test_jsm_cifstatement_constructor_args():
    sig = inspect.signature(jsm_CIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_jsm_cblockstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_CBlockStatement)


def test_jsm_cblockstatement_constructor_exists():
    assert callable(jsm_CBlockStatement.__init__)


def test_jsm_cblockstatement_constructor_args():
    sig = inspect.signature(jsm_CBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractmmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(AbstractMMethodImplementation)


def test_abstractmmethodimplementation_constructor_exists():
    assert callable(AbstractMMethodImplementation.__init__)


def test_abstractmmethodimplementation_constructor_args():
    sig = inspect.signature(AbstractMMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mmethodimplementationparameter_is_not_abstract():
    assert not inspect.isabstract(jsm_MMethodImplementationParameter)


def test_jsm_mmethodimplementationparameter_constructor_exists():
    assert callable(jsm_MMethodImplementationParameter.__init__)


def test_jsm_mmethodimplementationparameter_constructor_args():
    sig = inspect.signature(jsm_MMethodImplementationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "name" in params, "Missing parameter 'name'"

def test_jsm_mmethodimplementationparameter_has_final():
    assert hasattr(jsm_MMethodImplementationParameter, "final")
    descriptor = None
    for klass in jsm_MMethodImplementationParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jsm_mmethodimplementationparameter_has_name():
    assert hasattr(jsm_MMethodImplementationParameter, "name")
    descriptor = None
    for klass in jsm_MMethodImplementationParameter.__mro__:
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



def test_abstractmimplementablemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMImplementableMethodDeclaration)


def test_abstractmimplementablemethoddeclaration_constructor_exists():
    assert callable(AbstractMImplementableMethodDeclaration.__init__)


def test_abstractmimplementablemethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMImplementableMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mdeclaredmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm_MDeclaredMethodImplementation)


def test_jsm_mdeclaredmethodimplementation_constructor_exists():
    assert callable(jsm_MDeclaredMethodImplementation.__init__)


def test_jsm_mdeclaredmethodimplementation_constructor_args():
    sig = inspect.signature(jsm_MDeclaredMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mdirectmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm_MDirectMethodImplementation)


def test_jsm_mdirectmethodimplementation_constructor_exists():
    assert callable(jsm_MDirectMethodImplementation.__init__)


def test_jsm_mdirectmethodimplementation_constructor_args():
    sig = inspect.signature(jsm_MDirectMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_abstractmmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMMethodDeclaration)


def test_abstractmmethoddeclaration_constructor_exists():
    assert callable(AbstractMMethodDeclaration.__init__)


def test_abstractmmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmimplementablemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMImplementableMethodDeclaration)


def test_jsm_abstractmimplementablemethoddeclaration_constructor_exists():
    assert callable(jsm_AbstractMImplementableMethodDeclaration.__init__)


def test_jsm_abstractmimplementablemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_AbstractMImplementableMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mimplicitmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MImplicitMethodDeclaration)


def test_jsm_mimplicitmethoddeclaration_constructor_exists():
    assert callable(jsm_MImplicitMethodDeclaration.__init__)


def test_jsm_mimplicitmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_MImplicitMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMClassFieldDeclaration)


def test_abstractmclassfielddeclaration_constructor_exists():
    assert callable(AbstractMClassFieldDeclaration.__init__)


def test_abstractmclassfielddeclaration_constructor_args():
    sig = inspect.signature(AbstractMClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMFieldDeclaration)


def test_abstractmfielddeclaration_constructor_exists():
    assert callable(AbstractMFieldDeclaration.__init__)


def test_abstractmfielddeclaration_constructor_args():
    sig = inspect.signature(AbstractMFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMClassFieldDeclaration)


def test_jsm_abstractmclassfielddeclaration_constructor_exists():
    assert callable(jsm_AbstractMClassFieldDeclaration.__init__)


def test_jsm_abstractmclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm_AbstractMClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_jsm_abstractmclassfielddeclaration_has_final():
    assert hasattr(jsm_AbstractMClassFieldDeclaration, "final")
    descriptor = None
    for klass in jsm_AbstractMClassFieldDeclaration.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jsm_abstractmclassfielddeclaration_has_visibility():
    assert hasattr(jsm_AbstractMClassFieldDeclaration, "visibility")
    descriptor = None
    for klass in jsm_AbstractMClassFieldDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractcexpression_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractCExpression)


def test_jsm_abstractcexpression_constructor_exists():
    assert callable(jsm_AbstractCExpression.__init__)


def test_jsm_abstractcexpression_constructor_args():
    sig = inspect.signature(jsm_AbstractCExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractmtypewithnamedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeWithNameDeclaration)


def test_abstractmtypewithnamedeclaration_constructor_exists():
    assert callable(AbstractMTypeWithNameDeclaration.__init__)


def test_abstractmtypewithnamedeclaration_constructor_args():
    sig = inspect.signature(AbstractMTypeWithNameDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mconstructorparameter_is_not_abstract():
    assert not inspect.isabstract(jsm_MConstructorParameter)


def test_jsm_mconstructorparameter_constructor_exists():
    assert callable(jsm_MConstructorParameter.__init__)


def test_jsm_mconstructorparameter_constructor_args():
    sig = inspect.signature(jsm_MConstructorParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_jsm_mconstructorparameter_has_final():
    assert hasattr(jsm_MConstructorParameter, "final")
    descriptor = None
    for klass in jsm_MConstructorParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_jsm_mmethoddeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(jsm_MMethodDeclarationParameter)


def test_jsm_mmethoddeclarationparameter_constructor_exists():
    assert callable(jsm_MMethodDeclarationParameter.__init__)


def test_jsm_mmethoddeclarationparameter_constructor_args():
    sig = inspect.signature(jsm_MMethodDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_jsm_cdeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(jsm_CDeclarationStatement)


def test_jsm_cdeclarationstatement_constructor_exists():
    assert callable(jsm_CDeclarationStatement.__init__)


def test_jsm_cdeclarationstatement_constructor_args():
    sig = inspect.signature(jsm_CDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_jsm_cdeclarationstatement_has_final():
    assert hasattr(jsm_CDeclarationStatement, "final")
    descriptor = None
    for klass in jsm_CDeclarationStatement.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMFieldDeclaration)


def test_jsm_abstractmfielddeclaration_constructor_exists():
    assert callable(jsm_AbstractMFieldDeclaration.__init__)


def test_jsm_abstractmfielddeclaration_constructor_args():
    sig = inspect.signature(jsm_AbstractMFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_minterfacemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MInterfaceMethodDeclaration)


def test_jsm_minterfacemethoddeclaration_constructor_exists():
    assert callable(jsm_MInterfaceMethodDeclaration.__init__)


def test_jsm_minterfacemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_MInterfaceMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mconstantinterfacefielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MConstantInterfaceFieldDeclaration)


def test_jsm_mconstantinterfacefielddeclaration_constructor_exists():
    assert callable(jsm_MConstantInterfaceFieldDeclaration.__init__)


def test_jsm_mconstantinterfacefielddeclaration_constructor_args():
    sig = inspect.signature(jsm_MConstantInterfaceFieldDeclaration.__init__)
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



def test_jsm_mexternalinterface_is_not_abstract():
    assert not inspect.isabstract(jsm_MExternalInterface)


def test_jsm_mexternalinterface_constructor_exists():
    assert callable(jsm_MExternalInterface.__init__)


def test_jsm_mexternalinterface_constructor_args():
    sig = inspect.signature(jsm_MExternalInterface.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mabstractclassmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MAbstractClassMethodDeclaration)


def test_jsm_mabstractclassmethoddeclaration_constructor_exists():
    assert callable(jsm_MAbstractClassMethodDeclaration.__init__)


def test_jsm_mabstractclassmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_MAbstractClassMethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_jsm_mabstractclassmethoddeclaration_has_visibility():
    assert hasattr(jsm_MAbstractClassMethodDeclaration, "visibility")
    descriptor = None
    for klass in jsm_MAbstractClassMethodDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_mdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(MDeclaredClass)


def test_mdeclaredclass_constructor_exists():
    assert callable(MDeclaredClass.__init__)


def test_mdeclaredclass_constructor_args():
    sig = inspect.signature(MDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mabstractdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(jsm_MAbstractDeclaredClass)


def test_jsm_mabstractdeclaredclass_constructor_exists():
    assert callable(jsm_MAbstractDeclaredClass.__init__)


def test_jsm_mabstractdeclaredclass_constructor_args():
    sig = inspect.signature(jsm_MAbstractDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mnativemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MNativeMethodDeclaration)


def test_jsm_mnativemethoddeclaration_constructor_exists():
    assert callable(jsm_MNativeMethodDeclaration.__init__)


def test_jsm_mnativemethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_MNativeMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMMethodDeclaration)


def test_jsm_abstractmmethoddeclaration_constructor_exists():
    assert callable(jsm_AbstractMMethodDeclaration.__init__)


def test_jsm_abstractmmethoddeclaration_constructor_args():
    sig = inspect.signature(jsm_AbstractMMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mconstructor_is_not_abstract():
    assert not inspect.isabstract(jsm_MConstructor)


def test_jsm_mconstructor_constructor_exists():
    assert callable(jsm_MConstructor.__init__)


def test_jsm_mconstructor_constructor_args():
    sig = inspect.signature(jsm_MConstructor.__init__)
    params = list(sig.parameters.keys())



def test_jsm_minstanceclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MInstanceClassFieldDeclaration)


def test_jsm_minstanceclassfielddeclaration_constructor_exists():
    assert callable(jsm_MInstanceClassFieldDeclaration.__init__)


def test_jsm_minstanceclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm_MInstanceClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"

def test_jsm_minstanceclassfielddeclaration_has_transient():
    assert hasattr(jsm_MInstanceClassFieldDeclaration, "transient")
    descriptor = None
    for klass in jsm_MInstanceClassFieldDeclaration.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_jsm_mstaticclassfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(jsm_MStaticClassFieldDeclaration)


def test_jsm_mstaticclassfielddeclaration_constructor_exists():
    assert callable(jsm_MStaticClassFieldDeclaration.__init__)


def test_jsm_mstaticclassfielddeclaration_constructor_args():
    sig = inspect.signature(jsm_MStaticClassFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractminterface_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMInterface)


def test_jsm_abstractminterface_constructor_exists():
    assert callable(jsm_AbstractMInterface.__init__)


def test_jsm_abstractminterface_constructor_args():
    sig = inspect.signature(jsm_AbstractMInterface.__init__)
    params = list(sig.parameters.keys())



def test_abstractmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(AbstractMDeclaredType)


def test_abstractmdeclaredtype_constructor_exists():
    assert callable(AbstractMDeclaredType.__init__)


def test_abstractmdeclaredtype_constructor_args():
    sig = inspect.signature(AbstractMDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mdeclaredinterface_is_not_abstract():
    assert not inspect.isabstract(jsm_MDeclaredInterface)


def test_jsm_mdeclaredinterface_constructor_exists():
    assert callable(jsm_MDeclaredInterface.__init__)


def test_jsm_mdeclaredinterface_constructor_args():
    sig = inspect.signature(jsm_MDeclaredInterface.__init__)
    params = list(sig.parameters.keys())



def test_abstractmclass_is_not_abstract():
    assert not inspect.isabstract(AbstractMClass)


def test_abstractmclass_constructor_exists():
    assert callable(AbstractMClass.__init__)


def test_abstractmclass_constructor_args():
    sig = inspect.signature(AbstractMClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mexternalclass_is_not_abstract():
    assert not inspect.isabstract(jsm_MExternalClass)


def test_jsm_mexternalclass_constructor_exists():
    assert callable(jsm_MExternalClass.__init__)


def test_jsm_mexternalclass_constructor_args():
    sig = inspect.signature(jsm_MExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mdeclaredclass_is_not_abstract():
    assert not inspect.isabstract(jsm_MDeclaredClass)


def test_jsm_mdeclaredclass_constructor_exists():
    assert callable(jsm_MDeclaredClass.__init__)


def test_jsm_mdeclaredclass_constructor_args():
    sig = inspect.signature(jsm_MDeclaredClass.__init__)
    params = list(sig.parameters.keys())



def test_abstractmtypereference_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeReference)


def test_abstractmtypereference_constructor_exists():
    assert callable(AbstractMTypeReference.__init__)


def test_abstractmtypereference_constructor_args():
    sig = inspect.signature(AbstractMTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mprimitivetypereference_is_not_abstract():
    assert not inspect.isabstract(jsm_MPrimitiveTypeReference)


def test_jsm_mprimitivetypereference_constructor_exists():
    assert callable(jsm_MPrimitiveTypeReference.__init__)


def test_jsm_mprimitivetypereference_constructor_args():
    sig = inspect.signature(jsm_MPrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jsm_mprimitivetypereference_has_type():
    assert hasattr(jsm_MPrimitiveTypeReference, "type")
    descriptor = None
    for klass in jsm_MPrimitiveTypeReference.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jsm_mexternaltypereference_is_not_abstract():
    assert not inspect.isabstract(jsm_MExternalTypeReference)


def test_jsm_mexternaltypereference_constructor_exists():
    assert callable(jsm_MExternalTypeReference.__init__)


def test_jsm_mexternaltypereference_constructor_args():
    sig = inspect.signature(jsm_MExternalTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mdeclaredtypereference_is_not_abstract():
    assert not inspect.isabstract(jsm_MDeclaredTypeReference)


def test_jsm_mdeclaredtypereference_constructor_exists():
    assert callable(jsm_MDeclaredTypeReference.__init__)


def test_jsm_mdeclaredtypereference_constructor_args():
    sig = inspect.signature(jsm_MDeclaredTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmtypereference_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMTypeReference)


def test_jsm_abstractmtypereference_constructor_exists():
    assert callable(jsm_AbstractMTypeReference.__init__)


def test_jsm_abstractmtypereference_constructor_args():
    sig = inspect.signature(jsm_AbstractMTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_jsm_abstractmtypereference_has_array():
    assert hasattr(jsm_AbstractMTypeReference, "array")
    descriptor = None
    for klass in jsm_AbstractMTypeReference.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmmethodimplementation_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMMethodImplementation)


def test_jsm_abstractmmethodimplementation_constructor_exists():
    assert callable(jsm_AbstractMMethodImplementation.__init__)


def test_jsm_abstractmmethodimplementation_constructor_args():
    sig = inspect.signature(jsm_AbstractMMethodImplementation.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmtype_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMType)


def test_jsm_abstractmtype_constructor_exists():
    assert callable(jsm_AbstractMType.__init__)


def test_jsm_abstractmtype_constructor_args():
    sig = inspect.signature(jsm_AbstractMType.__init__)
    params = list(sig.parameters.keys())



def test_abstractmtypecontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractMTypeContainer)


def test_abstractmtypecontainer_constructor_exists():
    assert callable(AbstractMTypeContainer.__init__)


def test_abstractmtypecontainer_constructor_args():
    sig = inspect.signature(AbstractMTypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_jsm_abstractmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMDeclaredType)


def test_jsm_abstractmdeclaredtype_constructor_exists():
    assert callable(jsm_AbstractMDeclaredType.__init__)


def test_jsm_abstractmdeclaredtype_constructor_args():
    sig = inspect.signature(jsm_AbstractMDeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm_abstractmdeclaredtype_has_name():
    assert hasattr(jsm_AbstractMDeclaredType, "name")
    descriptor = None
    for klass in jsm_AbstractMDeclaredType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmtypecontainer_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMTypeContainer)


def test_jsm_abstractmtypecontainer_constructor_exists():
    assert callable(jsm_AbstractMTypeContainer.__init__)


def test_jsm_abstractmtypecontainer_constructor_args():
    sig = inspect.signature(jsm_AbstractMTypeContainer.__init__)
    params = list(sig.parameters.keys())



def test_abstractmresource_is_not_abstract():
    assert not inspect.isabstract(AbstractMResource)


def test_abstractmresource_constructor_exists():
    assert callable(AbstractMResource.__init__)


def test_abstractmresource_constructor_args():
    sig = inspect.signature(AbstractMResource.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mcompilationunit_is_not_abstract():
    assert not inspect.isabstract(jsm_MCompilationUnit)


def test_jsm_mcompilationunit_constructor_exists():
    assert callable(jsm_MCompilationUnit.__init__)


def test_jsm_mcompilationunit_constructor_args():
    sig = inspect.signature(jsm_MCompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mresource_is_not_abstract():
    assert not inspect.isabstract(jsm_MResource)


def test_jsm_mresource_constructor_exists():
    assert callable(jsm_MResource.__init__)


def test_jsm_mresource_constructor_args():
    sig = inspect.signature(jsm_MResource.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_jsm_mresource_has_content():
    assert hasattr(jsm_MResource, "content")
    descriptor = None
    for klass in jsm_MResource.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmresource_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMResource)


def test_jsm_abstractmresource_constructor_exists():
    assert callable(jsm_AbstractMResource.__init__)


def test_jsm_abstractmresource_constructor_args():
    sig = inspect.signature(jsm_AbstractMResource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_jsm_abstractmresource_has_name():
    assert hasattr(jsm_AbstractMResource, "name")
    descriptor = None
    for klass in jsm_AbstractMResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jsm_abstractmresource_has_derived():
    assert hasattr(jsm_AbstractMResource, "derived")
    descriptor = None
    for klass in jsm_AbstractMResource.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmexternaltype_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMExternalType)


def test_jsm_abstractmexternaltype_constructor_exists():
    assert callable(jsm_AbstractMExternalType.__init__)


def test_jsm_abstractmexternaltype_constructor_args():
    sig = inspect.signature(jsm_AbstractMExternalType.__init__)
    params = list(sig.parameters.keys())
    assert "fullQualifiedName" in params, "Missing parameter 'fullQualifiedName'"

def test_jsm_abstractmexternaltype_has_fullQualifiedName():
    assert hasattr(jsm_AbstractMExternalType, "fullQualifiedName")
    descriptor = None
    for klass in jsm_AbstractMExternalType.__mro__:
        if "fullQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_jsm_abstractmpackagecontainer_is_not_abstract():
    assert not inspect.isabstract(jsm_AbstractMPackageContainer)


def test_jsm_abstractmpackagecontainer_constructor_exists():
    assert callable(jsm_AbstractMPackageContainer.__init__)


def test_jsm_abstractmpackagecontainer_constructor_args():
    sig = inspect.signature(jsm_AbstractMPackageContainer.__init__)
    params = list(sig.parameters.keys())



def test_abstractmpackagecontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractMPackageContainer)


def test_abstractmpackagecontainer_constructor_exists():
    assert callable(AbstractMPackageContainer.__init__)


def test_abstractmpackagecontainer_constructor_args():
    sig = inspect.signature(AbstractMPackageContainer.__init__)
    params = list(sig.parameters.keys())



def test_jsm_mpackage_is_not_abstract():
    assert not inspect.isabstract(jsm_MPackage)


def test_jsm_mpackage_constructor_exists():
    assert callable(jsm_MPackage.__init__)


def test_jsm_mpackage_constructor_args():
    sig = inspect.signature(jsm_MPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jsm_mpackage_has_name():
    assert hasattr(jsm_MPackage, "name")
    descriptor = None
    for klass in jsm_MPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jsm_mroot_is_not_abstract():
    assert not inspect.isabstract(jsm_MRoot)


def test_jsm_mroot_constructor_exists():
    assert callable(jsm_MRoot.__init__)


def test_jsm_mroot_constructor_args():
    sig = inspect.signature(jsm_MRoot.__init__)
    params = list(sig.parameters.keys())

def test_mprimitivetypes_exists():
    # Check that the Enumeration exists
    assert MPrimitiveTypes is not None

def test_mprimitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MPrimitiveTypes]
    expected_literals = [
        "byte",
        "short",
        "long",
        "float",
        "char",
        "boolean",
        "double",
        "int",
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
        "PROTECTED",
        "PUBLIC",
        "PRIVATE",
        "DEFAULT",
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
AbstractMType_strategy = st.builds(
    AbstractMType,
)
jsm_AbstractMClass_strategy = st.builds(
    jsm_AbstractMClass,
)
jsm_AbstractMTypeWithNameDeclaration_strategy = st.builds(
    jsm_AbstractMTypeWithNameDeclaration,
    name=
        safe_text
)
jsm_AbstractCStatement_strategy = st.builds(
    jsm_AbstractCStatement,
)
AbstractModifiers_strategy = st.builds(
    AbstractModifiers,
)
jsm_AbstractMMethodLike_strategy = st.builds(
    jsm_AbstractMMethodLike,
)
jsm_AbstractModifiers_strategy = st.builds(
    jsm_AbstractModifiers,
    synchronized=
        st.booleans(),
    visibility=
        safe_text,
    final=
        st.booleans()
)
AbstractCExpression_strategy = st.builds(
    AbstractCExpression,
)
jsm_CUnparsedExpression_strategy = st.builds(
    jsm_CUnparsedExpression,
    code=
        safe_text
)
jsm_CConditionalExpression_strategy = st.builds(
    jsm_CConditionalExpression,
)
AbstractCStatement_strategy = st.builds(
    AbstractCStatement,
)
jsm_CUnparsedStatement_strategy = st.builds(
    jsm_CUnparsedStatement,
    code=
        safe_text
)
jsm_CExpressionStatement_strategy = st.builds(
    jsm_CExpressionStatement,
)
jsm_CIfStatement_strategy = st.builds(
    jsm_CIfStatement,
)
jsm_CBlockStatement_strategy = st.builds(
    jsm_CBlockStatement,
)
AbstractMMethodImplementation_strategy = st.builds(
    AbstractMMethodImplementation,
)
jsm_MMethodImplementationParameter_strategy = st.builds(
    jsm_MMethodImplementationParameter,
    final=
        st.booleans(),
    name=
        safe_text
)
AbstractMMethodLike_strategy = st.builds(
    AbstractMMethodLike,
)
AbstractMImplementableMethodDeclaration_strategy = st.builds(
    AbstractMImplementableMethodDeclaration,
)
jsm_MDeclaredMethodImplementation_strategy = st.builds(
    jsm_MDeclaredMethodImplementation,
)
jsm_MDirectMethodImplementation_strategy = st.builds(
    jsm_MDirectMethodImplementation,
)
AbstractMMethodDeclaration_strategy = st.builds(
    AbstractMMethodDeclaration,
)
jsm_AbstractMImplementableMethodDeclaration_strategy = st.builds(
    jsm_AbstractMImplementableMethodDeclaration,
)
jsm_MImplicitMethodDeclaration_strategy = st.builds(
    jsm_MImplicitMethodDeclaration,
)
AbstractMClassFieldDeclaration_strategy = st.builds(
    AbstractMClassFieldDeclaration,
)
AbstractMFieldDeclaration_strategy = st.builds(
    AbstractMFieldDeclaration,
)
jsm_AbstractMClassFieldDeclaration_strategy = st.builds(
    jsm_AbstractMClassFieldDeclaration,
    final=
        st.booleans(),
    visibility=
        safe_text
)
jsm_AbstractCExpression_strategy = st.builds(
    jsm_AbstractCExpression,
)
AbstractMTypeWithNameDeclaration_strategy = st.builds(
    AbstractMTypeWithNameDeclaration,
)
jsm_MConstructorParameter_strategy = st.builds(
    jsm_MConstructorParameter,
    final=
        st.booleans()
)
jsm_MMethodDeclarationParameter_strategy = st.builds(
    jsm_MMethodDeclarationParameter,
)
jsm_CDeclarationStatement_strategy = st.builds(
    jsm_CDeclarationStatement,
    final=
        st.booleans()
)
jsm_AbstractMFieldDeclaration_strategy = st.builds(
    jsm_AbstractMFieldDeclaration,
)
jsm_MInterfaceMethodDeclaration_strategy = st.builds(
    jsm_MInterfaceMethodDeclaration,
)
jsm_MConstantInterfaceFieldDeclaration_strategy = st.builds(
    jsm_MConstantInterfaceFieldDeclaration,
)
AbstractMInterface_strategy = st.builds(
    AbstractMInterface,
)
AbstractMExternalType_strategy = st.builds(
    AbstractMExternalType,
)
jsm_MExternalInterface_strategy = st.builds(
    jsm_MExternalInterface,
)
jsm_MAbstractClassMethodDeclaration_strategy = st.builds(
    jsm_MAbstractClassMethodDeclaration,
    visibility=
        safe_text
)
MDeclaredClass_strategy = st.builds(
    MDeclaredClass,
)
jsm_MAbstractDeclaredClass_strategy = st.builds(
    jsm_MAbstractDeclaredClass,
)
jsm_MNativeMethodDeclaration_strategy = st.builds(
    jsm_MNativeMethodDeclaration,
)
jsm_AbstractMMethodDeclaration_strategy = st.builds(
    jsm_AbstractMMethodDeclaration,
)
jsm_MConstructor_strategy = st.builds(
    jsm_MConstructor,
)
jsm_MInstanceClassFieldDeclaration_strategy = st.builds(
    jsm_MInstanceClassFieldDeclaration,
    transient=
        st.booleans()
)
jsm_MStaticClassFieldDeclaration_strategy = st.builds(
    jsm_MStaticClassFieldDeclaration,
)
jsm_AbstractMInterface_strategy = st.builds(
    jsm_AbstractMInterface,
)
AbstractMDeclaredType_strategy = st.builds(
    AbstractMDeclaredType,
)
jsm_MDeclaredInterface_strategy = st.builds(
    jsm_MDeclaredInterface,
)
AbstractMClass_strategy = st.builds(
    AbstractMClass,
)
jsm_MExternalClass_strategy = st.builds(
    jsm_MExternalClass,
)
jsm_MDeclaredClass_strategy = st.builds(
    jsm_MDeclaredClass,
)
AbstractMTypeReference_strategy = st.builds(
    AbstractMTypeReference,
)
jsm_MPrimitiveTypeReference_strategy = st.builds(
    jsm_MPrimitiveTypeReference,
    type=
        safe_text
)
jsm_MExternalTypeReference_strategy = st.builds(
    jsm_MExternalTypeReference,
)
jsm_MDeclaredTypeReference_strategy = st.builds(
    jsm_MDeclaredTypeReference,
)
jsm_AbstractMTypeReference_strategy = st.builds(
    jsm_AbstractMTypeReference,
    array=
        st.booleans()
)
jsm_AbstractMMethodImplementation_strategy = st.builds(
    jsm_AbstractMMethodImplementation,
)
jsm_AbstractMType_strategy = st.builds(
    jsm_AbstractMType,
)
AbstractMTypeContainer_strategy = st.builds(
    AbstractMTypeContainer,
)
jsm_AbstractMDeclaredType_strategy = st.builds(
    jsm_AbstractMDeclaredType,
    name=
        safe_text
)
jsm_AbstractMTypeContainer_strategy = st.builds(
    jsm_AbstractMTypeContainer,
)
AbstractMResource_strategy = st.builds(
    AbstractMResource,
)
jsm_MCompilationUnit_strategy = st.builds(
    jsm_MCompilationUnit,
)
jsm_MResource_strategy = st.builds(
    jsm_MResource,
    content=
        safe_text
)
jsm_AbstractMResource_strategy = st.builds(
    jsm_AbstractMResource,
    name=
        safe_text,
    derived=
        st.booleans()
)
jsm_AbstractMExternalType_strategy = st.builds(
    jsm_AbstractMExternalType,
    fullQualifiedName=
        safe_text
)
jsm_AbstractMPackageContainer_strategy = st.builds(
    jsm_AbstractMPackageContainer,
)
AbstractMPackageContainer_strategy = st.builds(
    AbstractMPackageContainer,
)
jsm_MPackage_strategy = st.builds(
    jsm_MPackage,
    name=
        safe_text
)
jsm_MRoot_strategy = st.builds(
    jsm_MRoot,
)

@given(instance=AbstractMType_strategy)
@settings(max_examples=50)
def test_abstractmtype_instantiation(instance):
    assert isinstance(instance, AbstractMType)

@given(instance=jsm_AbstractMClass_strategy)
@settings(max_examples=50)
def test_jsm_abstractmclass_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMClass)

@given(instance=jsm_AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_abstractmtypewithnamedeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeWithNameDeclaration)



@given(instance=jsm_AbstractMTypeWithNameDeclaration_strategy)
def test_jsm_abstractmtypewithnamedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm_AbstractCStatement_strategy)
@settings(max_examples=50)
def test_jsm_abstractcstatement_instantiation(instance):
    assert isinstance(instance, jsm_AbstractCStatement)

@given(instance=AbstractModifiers_strategy)
@settings(max_examples=50)
def test_abstractmodifiers_instantiation(instance):
    assert isinstance(instance, AbstractModifiers)

@given(instance=jsm_AbstractMMethodLike_strategy)
@settings(max_examples=50)
def test_jsm_abstractmmethodlike_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodLike)

@given(instance=jsm_AbstractModifiers_strategy)
@settings(max_examples=50)
def test_jsm_abstractmodifiers_instantiation(instance):
    assert isinstance(instance, jsm_AbstractModifiers)



@given(instance=jsm_AbstractModifiers_strategy)
def test_jsm_abstractmodifiers_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=jsm_AbstractModifiers_strategy)
def test_jsm_abstractmodifiers_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=jsm_AbstractModifiers_strategy)
def test_jsm_abstractmodifiers_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=AbstractCExpression_strategy)
@settings(max_examples=50)
def test_abstractcexpression_instantiation(instance):
    assert isinstance(instance, AbstractCExpression)

@given(instance=jsm_CUnparsedExpression_strategy)
@settings(max_examples=50)
def test_jsm_cunparsedexpression_instantiation(instance):
    assert isinstance(instance, jsm_CUnparsedExpression)



@given(instance=jsm_CUnparsedExpression_strategy)
def test_jsm_cunparsedexpression_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=jsm_CConditionalExpression_strategy)
@settings(max_examples=50)
def test_jsm_cconditionalexpression_instantiation(instance):
    assert isinstance(instance, jsm_CConditionalExpression)

@given(instance=AbstractCStatement_strategy)
@settings(max_examples=50)
def test_abstractcstatement_instantiation(instance):
    assert isinstance(instance, AbstractCStatement)

@given(instance=jsm_CUnparsedStatement_strategy)
@settings(max_examples=50)
def test_jsm_cunparsedstatement_instantiation(instance):
    assert isinstance(instance, jsm_CUnparsedStatement)



@given(instance=jsm_CUnparsedStatement_strategy)
def test_jsm_cunparsedstatement_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=jsm_CExpressionStatement_strategy)
@settings(max_examples=50)
def test_jsm_cexpressionstatement_instantiation(instance):
    assert isinstance(instance, jsm_CExpressionStatement)

@given(instance=jsm_CIfStatement_strategy)
@settings(max_examples=50)
def test_jsm_cifstatement_instantiation(instance):
    assert isinstance(instance, jsm_CIfStatement)

@given(instance=jsm_CBlockStatement_strategy)
@settings(max_examples=50)
def test_jsm_cblockstatement_instantiation(instance):
    assert isinstance(instance, jsm_CBlockStatement)

@given(instance=AbstractMMethodImplementation_strategy)
@settings(max_examples=50)
def test_abstractmmethodimplementation_instantiation(instance):
    assert isinstance(instance, AbstractMMethodImplementation)

@given(instance=jsm_MMethodImplementationParameter_strategy)
@settings(max_examples=50)
def test_jsm_mmethodimplementationparameter_instantiation(instance):
    assert isinstance(instance, jsm_MMethodImplementationParameter)



@given(instance=jsm_MMethodImplementationParameter_strategy)
def test_jsm_mmethodimplementationparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=jsm_MMethodImplementationParameter_strategy)
def test_jsm_mmethodimplementationparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractMMethodLike_strategy)
@settings(max_examples=50)
def test_abstractmmethodlike_instantiation(instance):
    assert isinstance(instance, AbstractMMethodLike)

@given(instance=AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmimplementablemethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMImplementableMethodDeclaration)

@given(instance=jsm_MDeclaredMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm_mdeclaredmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredMethodImplementation)

@given(instance=jsm_MDirectMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm_mdirectmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm_MDirectMethodImplementation)

@given(instance=AbstractMMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMMethodDeclaration)

@given(instance=jsm_AbstractMImplementableMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_abstractmimplementablemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMImplementableMethodDeclaration)

@given(instance=jsm_MImplicitMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_mimplicitmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MImplicitMethodDeclaration)

@given(instance=AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMClassFieldDeclaration)

@given(instance=AbstractMFieldDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmfielddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMFieldDeclaration)

@given(instance=jsm_AbstractMClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_abstractmclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMClassFieldDeclaration)



@given(instance=jsm_AbstractMClassFieldDeclaration_strategy)
def test_jsm_abstractmclassfielddeclaration_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=jsm_AbstractMClassFieldDeclaration_strategy)
def test_jsm_abstractmclassfielddeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=jsm_AbstractCExpression_strategy)
@settings(max_examples=50)
def test_jsm_abstractcexpression_instantiation(instance):
    assert isinstance(instance, jsm_AbstractCExpression)

@given(instance=AbstractMTypeWithNameDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmtypewithnamedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMTypeWithNameDeclaration)

@given(instance=jsm_MConstructorParameter_strategy)
@settings(max_examples=50)
def test_jsm_mconstructorparameter_instantiation(instance):
    assert isinstance(instance, jsm_MConstructorParameter)



@given(instance=jsm_MConstructorParameter_strategy)
def test_jsm_mconstructorparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=jsm_MMethodDeclarationParameter_strategy)
@settings(max_examples=50)
def test_jsm_mmethoddeclarationparameter_instantiation(instance):
    assert isinstance(instance, jsm_MMethodDeclarationParameter)

@given(instance=jsm_CDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jsm_cdeclarationstatement_instantiation(instance):
    assert isinstance(instance, jsm_CDeclarationStatement)



@given(instance=jsm_CDeclarationStatement_strategy)
def test_jsm_cdeclarationstatement_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=jsm_AbstractMFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_abstractmfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMFieldDeclaration)

@given(instance=jsm_MInterfaceMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_minterfacemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MInterfaceMethodDeclaration)

@given(instance=jsm_MConstantInterfaceFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_mconstantinterfacefielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MConstantInterfaceFieldDeclaration)

@given(instance=AbstractMInterface_strategy)
@settings(max_examples=50)
def test_abstractminterface_instantiation(instance):
    assert isinstance(instance, AbstractMInterface)

@given(instance=AbstractMExternalType_strategy)
@settings(max_examples=50)
def test_abstractmexternaltype_instantiation(instance):
    assert isinstance(instance, AbstractMExternalType)

@given(instance=jsm_MExternalInterface_strategy)
@settings(max_examples=50)
def test_jsm_mexternalinterface_instantiation(instance):
    assert isinstance(instance, jsm_MExternalInterface)

@given(instance=jsm_MAbstractClassMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_mabstractclassmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MAbstractClassMethodDeclaration)



@given(instance=jsm_MAbstractClassMethodDeclaration_strategy)
def test_jsm_mabstractclassmethoddeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=MDeclaredClass_strategy)
@settings(max_examples=50)
def test_mdeclaredclass_instantiation(instance):
    assert isinstance(instance, MDeclaredClass)

@given(instance=jsm_MAbstractDeclaredClass_strategy)
@settings(max_examples=50)
def test_jsm_mabstractdeclaredclass_instantiation(instance):
    assert isinstance(instance, jsm_MAbstractDeclaredClass)

@given(instance=jsm_MNativeMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_mnativemethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MNativeMethodDeclaration)

@given(instance=jsm_AbstractMMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_abstractmmethoddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodDeclaration)

@given(instance=jsm_MConstructor_strategy)
@settings(max_examples=50)
def test_jsm_mconstructor_instantiation(instance):
    assert isinstance(instance, jsm_MConstructor)

@given(instance=jsm_MInstanceClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_minstanceclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MInstanceClassFieldDeclaration)



@given(instance=jsm_MInstanceClassFieldDeclaration_strategy)
def test_jsm_minstanceclassfielddeclaration_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=jsm_MStaticClassFieldDeclaration_strategy)
@settings(max_examples=50)
def test_jsm_mstaticclassfielddeclaration_instantiation(instance):
    assert isinstance(instance, jsm_MStaticClassFieldDeclaration)

@given(instance=jsm_AbstractMInterface_strategy)
@settings(max_examples=50)
def test_jsm_abstractminterface_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMInterface)

@given(instance=AbstractMDeclaredType_strategy)
@settings(max_examples=50)
def test_abstractmdeclaredtype_instantiation(instance):
    assert isinstance(instance, AbstractMDeclaredType)

@given(instance=jsm_MDeclaredInterface_strategy)
@settings(max_examples=50)
def test_jsm_mdeclaredinterface_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredInterface)

@given(instance=AbstractMClass_strategy)
@settings(max_examples=50)
def test_abstractmclass_instantiation(instance):
    assert isinstance(instance, AbstractMClass)

@given(instance=jsm_MExternalClass_strategy)
@settings(max_examples=50)
def test_jsm_mexternalclass_instantiation(instance):
    assert isinstance(instance, jsm_MExternalClass)

@given(instance=jsm_MDeclaredClass_strategy)
@settings(max_examples=50)
def test_jsm_mdeclaredclass_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredClass)

@given(instance=AbstractMTypeReference_strategy)
@settings(max_examples=50)
def test_abstractmtypereference_instantiation(instance):
    assert isinstance(instance, AbstractMTypeReference)

@given(instance=jsm_MPrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_jsm_mprimitivetypereference_instantiation(instance):
    assert isinstance(instance, jsm_MPrimitiveTypeReference)



@given(instance=jsm_MPrimitiveTypeReference_strategy)
def test_jsm_mprimitivetypereference_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jsm_MExternalTypeReference_strategy)
@settings(max_examples=50)
def test_jsm_mexternaltypereference_instantiation(instance):
    assert isinstance(instance, jsm_MExternalTypeReference)

@given(instance=jsm_MDeclaredTypeReference_strategy)
@settings(max_examples=50)
def test_jsm_mdeclaredtypereference_instantiation(instance):
    assert isinstance(instance, jsm_MDeclaredTypeReference)

@given(instance=jsm_AbstractMTypeReference_strategy)
@settings(max_examples=50)
def test_jsm_abstractmtypereference_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeReference)



@given(instance=jsm_AbstractMTypeReference_strategy)
def test_jsm_abstractmtypereference_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=jsm_AbstractMMethodImplementation_strategy)
@settings(max_examples=50)
def test_jsm_abstractmmethodimplementation_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMMethodImplementation)

@given(instance=jsm_AbstractMType_strategy)
@settings(max_examples=50)
def test_jsm_abstractmtype_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMType)

@given(instance=AbstractMTypeContainer_strategy)
@settings(max_examples=50)
def test_abstractmtypecontainer_instantiation(instance):
    assert isinstance(instance, AbstractMTypeContainer)

@given(instance=jsm_AbstractMDeclaredType_strategy)
@settings(max_examples=50)
def test_jsm_abstractmdeclaredtype_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMDeclaredType)



@given(instance=jsm_AbstractMDeclaredType_strategy)
def test_jsm_abstractmdeclaredtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm_AbstractMTypeContainer_strategy)
@settings(max_examples=50)
def test_jsm_abstractmtypecontainer_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMTypeContainer)

@given(instance=AbstractMResource_strategy)
@settings(max_examples=50)
def test_abstractmresource_instantiation(instance):
    assert isinstance(instance, AbstractMResource)

@given(instance=jsm_MCompilationUnit_strategy)
@settings(max_examples=50)
def test_jsm_mcompilationunit_instantiation(instance):
    assert isinstance(instance, jsm_MCompilationUnit)

@given(instance=jsm_MResource_strategy)
@settings(max_examples=50)
def test_jsm_mresource_instantiation(instance):
    assert isinstance(instance, jsm_MResource)



@given(instance=jsm_MResource_strategy)
def test_jsm_mresource_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=jsm_AbstractMResource_strategy)
@settings(max_examples=50)
def test_jsm_abstractmresource_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMResource)



@given(instance=jsm_AbstractMResource_strategy)
def test_jsm_abstractmresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jsm_AbstractMResource_strategy)
def test_jsm_abstractmresource_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=jsm_AbstractMExternalType_strategy)
@settings(max_examples=50)
def test_jsm_abstractmexternaltype_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMExternalType)



@given(instance=jsm_AbstractMExternalType_strategy)
def test_jsm_abstractmexternaltype_fullQualifiedName_setter(instance):
    original = instance.fullQualifiedName
    instance.fullQualifiedName = original
    assert instance.fullQualifiedName == original

@given(instance=jsm_AbstractMPackageContainer_strategy)
@settings(max_examples=50)
def test_jsm_abstractmpackagecontainer_instantiation(instance):
    assert isinstance(instance, jsm_AbstractMPackageContainer)

@given(instance=AbstractMPackageContainer_strategy)
@settings(max_examples=50)
def test_abstractmpackagecontainer_instantiation(instance):
    assert isinstance(instance, AbstractMPackageContainer)

@given(instance=jsm_MPackage_strategy)
@settings(max_examples=50)
def test_jsm_mpackage_instantiation(instance):
    assert isinstance(instance, jsm_MPackage)



@given(instance=jsm_MPackage_strategy)
def test_jsm_mpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jsm_MRoot_strategy)
@settings(max_examples=50)
def test_jsm_mroot_instantiation(instance):
    assert isinstance(instance, jsm_MRoot)

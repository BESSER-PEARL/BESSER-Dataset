import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cst::TypeCS,
    cst::SimpleNameCS,
    ocl::cst::CollectionTypeCS,
    ocl::cst::PrimitiveTypeCS,
    IsMarkedPreCS,
    VariableCS,
    PrePostOrBodyDeclCS,
    DefExpressionCS,
    OperationCS,
    InvOrDefCS,
    ocl::cst::DefCS,
    ocl::cst::InvCS,
    InitOrDerValueCS,
    ocl::cst::InitValueCS,
    ocl::cst::DerValueCS,
    OCLExpressionCS,
    ocl::cst::SimpleNameCS,
    ocl::cst::LiteralExpCS,
    ocl::cst::IfExpCS,
    ocl::cst::MessageExpCS,
    ocl::cst::LetExpCS,
    ocl::cst::VariableExpCS,
    ocl::cst::TypeCS,
    SimpleNameCS,
    TypeCS,
    ocl::cst::TupleTypeCS,
    ocl::cst::PathNameCS,
    PackageDeclarationCS,
    ContextDeclCS,
    ocl::cst::ClassifierContextDeclCS,
    ocl::cst::PropertyContextCS,
    ocl::cst::OperationContextDeclCS,
    PathNameCS,
    CSTNode,
    ocl::cst::OCLMessageArgCS,
    ocl::cst::PrePostOrBodyDeclCS,
    ocl::cst::IsMarkedPreCS,
    ocl::cst::DefExpressionCS,
    ocl::cst::ContextDeclCS,
    ocl::cst::OperationCS,
    ocl::cst::VariableCS,
    ocl::cst::InitOrDerValueCS,
    ocl::cst::OCLExpressionCS,
    ocl::cst::InvOrDefCS,
    ocl::cst::PackageDeclarationCS,
    ocl::cst::CSTNode,
    cst::LiteralExpCS,
    ocl::cst::InvalidLiteralExpCS,
    ocl::cst::NullLiteralExpCS,
    cst::PrimitiveLiteralExpCS,
    ocl::cst::BooleanLiteralExpCS,
    ocl::cst::OCLDocumentCS,
    FeatureCallExpCS,
    ocl::cst::OperationCallExpCS,
    LoopExpCS,
    ocl::cst::IterateExpCS,
    ocl::cst::IteratorExpCS,
    CallExpCS,
    ocl::cst::FeatureCallExpCS,
    ocl::cst::LoopExpCS,
    ocl::cst::CallExpCS,
    OCLMessageArgCS,
    PrimitiveLiteralExpCS,
    ocl::cst::UnlimitedNaturalLiteralExpCS,
    ocl::cst::StringLiteralExpCS,
    ocl::cst::RealLiteralExpCS,
    ocl::cst::IntegerLiteralExpCS,
    ocl::cst::CollectionLiteralPartCS,
    CollectionLiteralPartCS,
    ocl::cst::CollectionRangeCS,
    LiteralExpCS,
    ocl::cst::TupleLiteralExpCS,
    ocl::cst::PrimitiveLiteralExpCS,
    ocl::cst::CollectionLiteralExpCS,
    PrePostOrBodyEnum,
    SimpleTypeEnum,
    DotOrArrowEnum,
    CollectionTypeIdentifierEnum,
    MessageExpKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cst::typecs_is_not_abstract():
    assert not inspect.isabstract(cst::TypeCS)


def test_cst::typecs_constructor_exists():
    assert callable(cst::TypeCS.__init__)


def test_cst::typecs_constructor_args():
    sig = inspect.signature(cst::TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::simplenamecs_is_not_abstract():
    assert not inspect.isabstract(cst::SimpleNameCS)


def test_cst::simplenamecs_constructor_exists():
    assert callable(cst::SimpleNameCS.__init__)


def test_cst::simplenamecs_constructor_args():
    sig = inspect.signature(cst::SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CollectionTypeCS)


def test_ocl::cst::collectiontypecs_constructor_exists():
    assert callable(ocl::cst::CollectionTypeCS.__init__)


def test_ocl::cst::collectiontypecs_constructor_args():
    sig = inspect.signature(ocl::cst::CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "collectionTypeIdentifier" in params, "Missing parameter 'collectionTypeIdentifier'"

def test_ocl::cst::collectiontypecs_has_collectionTypeIdentifier():
    assert hasattr(ocl::cst::CollectionTypeCS, "collectionTypeIdentifier")
    descriptor = None
    for klass in ocl::cst::CollectionTypeCS.__mro__:
        if "collectionTypeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["collectionTypeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::primitivetypecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PrimitiveTypeCS)


def test_ocl::cst::primitivetypecs_constructor_exists():
    assert callable(ocl::cst::PrimitiveTypeCS.__init__)


def test_ocl::cst::primitivetypecs_constructor_args():
    sig = inspect.signature(ocl::cst::PrimitiveTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ismarkedprecs_is_not_abstract():
    assert not inspect.isabstract(IsMarkedPreCS)


def test_ismarkedprecs_constructor_exists():
    assert callable(IsMarkedPreCS.__init__)


def test_ismarkedprecs_constructor_args():
    sig = inspect.signature(IsMarkedPreCS.__init__)
    params = list(sig.parameters.keys())



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_prepostorbodydeclcs_is_not_abstract():
    assert not inspect.isabstract(PrePostOrBodyDeclCS)


def test_prepostorbodydeclcs_constructor_exists():
    assert callable(PrePostOrBodyDeclCS.__init__)


def test_prepostorbodydeclcs_constructor_args():
    sig = inspect.signature(PrePostOrBodyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_defexpressioncs_is_not_abstract():
    assert not inspect.isabstract(DefExpressionCS)


def test_defexpressioncs_constructor_exists():
    assert callable(DefExpressionCS.__init__)


def test_defexpressioncs_constructor_args():
    sig = inspect.signature(DefExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_operationcs_is_not_abstract():
    assert not inspect.isabstract(OperationCS)


def test_operationcs_constructor_exists():
    assert callable(OperationCS.__init__)


def test_operationcs_constructor_args():
    sig = inspect.signature(OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_invordefcs_is_not_abstract():
    assert not inspect.isabstract(InvOrDefCS)


def test_invordefcs_constructor_exists():
    assert callable(InvOrDefCS.__init__)


def test_invordefcs_constructor_args():
    sig = inspect.signature(InvOrDefCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::defcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::DefCS)


def test_ocl::cst::defcs_constructor_exists():
    assert callable(ocl::cst::DefCS.__init__)


def test_ocl::cst::defcs_constructor_args():
    sig = inspect.signature(ocl::cst::DefCS.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ocl::cst::defcs_has_static():
    assert hasattr(ocl::cst::DefCS, "static")
    descriptor = None
    for klass in ocl::cst::DefCS.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::invcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::InvCS)


def test_ocl::cst::invcs_constructor_exists():
    assert callable(ocl::cst::InvCS.__init__)


def test_ocl::cst::invcs_constructor_args():
    sig = inspect.signature(ocl::cst::InvCS.__init__)
    params = list(sig.parameters.keys())



def test_initordervaluecs_is_not_abstract():
    assert not inspect.isabstract(InitOrDerValueCS)


def test_initordervaluecs_constructor_exists():
    assert callable(InitOrDerValueCS.__init__)


def test_initordervaluecs_constructor_args():
    sig = inspect.signature(InitOrDerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::initvaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::InitValueCS)


def test_ocl::cst::initvaluecs_constructor_exists():
    assert callable(ocl::cst::InitValueCS.__init__)


def test_ocl::cst::initvaluecs_constructor_args():
    sig = inspect.signature(ocl::cst::InitValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::dervaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::DerValueCS)


def test_ocl::cst::dervaluecs_constructor_exists():
    assert callable(ocl::cst::DerValueCS.__init__)


def test_ocl::cst::dervaluecs_constructor_args():
    sig = inspect.signature(ocl::cst::DerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::simplenamecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::SimpleNameCS)


def test_ocl::cst::simplenamecs_constructor_exists():
    assert callable(ocl::cst::SimpleNameCS.__init__)


def test_ocl::cst::simplenamecs_constructor_args():
    sig = inspect.signature(ocl::cst::SimpleNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_ocl::cst::simplenamecs_has_value():
    assert hasattr(ocl::cst::SimpleNameCS, "value")
    descriptor = None
    for klass in ocl::cst::SimpleNameCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::simplenamecs_has_type():
    assert hasattr(ocl::cst::SimpleNameCS, "type")
    descriptor = None
    for klass in ocl::cst::SimpleNameCS.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::LiteralExpCS)


def test_ocl::cst::literalexpcs_constructor_exists():
    assert callable(ocl::cst::LiteralExpCS.__init__)


def test_ocl::cst::literalexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::ifexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::IfExpCS)


def test_ocl::cst::ifexpcs_constructor_exists():
    assert callable(ocl::cst::IfExpCS.__init__)


def test_ocl::cst::ifexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::messageexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::MessageExpCS)


def test_ocl::cst::messageexpcs_constructor_exists():
    assert callable(ocl::cst::MessageExpCS.__init__)


def test_ocl::cst::messageexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::MessageExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::cst::messageexpcs_has_kind():
    assert hasattr(ocl::cst::MessageExpCS, "kind")
    descriptor = None
    for klass in ocl::cst::MessageExpCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::letexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::LetExpCS)


def test_ocl::cst::letexpcs_constructor_exists():
    assert callable(ocl::cst::LetExpCS.__init__)


def test_ocl::cst::letexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::variableexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::VariableExpCS)


def test_ocl::cst::variableexpcs_constructor_exists():
    assert callable(ocl::cst::VariableExpCS.__init__)


def test_ocl::cst::variableexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::typecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::TypeCS)


def test_ocl::cst::typecs_constructor_exists():
    assert callable(ocl::cst::TypeCS.__init__)


def test_ocl::cst::typecs_constructor_args():
    sig = inspect.signature(ocl::cst::TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(SimpleNameCS)


def test_simplenamecs_constructor_exists():
    assert callable(SimpleNameCS.__init__)


def test_simplenamecs_constructor_args():
    sig = inspect.signature(SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::tupletypecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::TupleTypeCS)


def test_ocl::cst::tupletypecs_constructor_exists():
    assert callable(ocl::cst::TupleTypeCS.__init__)


def test_ocl::cst::tupletypecs_constructor_args():
    sig = inspect.signature(ocl::cst::TupleTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PathNameCS)


def test_ocl::cst::pathnamecs_constructor_exists():
    assert callable(ocl::cst::PathNameCS.__init__)


def test_ocl::cst::pathnamecs_constructor_args():
    sig = inspect.signature(ocl::cst::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(PackageDeclarationCS)


def test_packagedeclarationcs_constructor_exists():
    assert callable(PackageDeclarationCS.__init__)


def test_packagedeclarationcs_constructor_args():
    sig = inspect.signature(PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ContextDeclCS)


def test_contextdeclcs_constructor_exists():
    assert callable(ContextDeclCS.__init__)


def test_contextdeclcs_constructor_args():
    sig = inspect.signature(ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::classifiercontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::ClassifierContextDeclCS)


def test_ocl::cst::classifiercontextdeclcs_constructor_exists():
    assert callable(ocl::cst::ClassifierContextDeclCS.__init__)


def test_ocl::cst::classifiercontextdeclcs_constructor_args():
    sig = inspect.signature(ocl::cst::ClassifierContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::propertycontextcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PropertyContextCS)


def test_ocl::cst::propertycontextcs_constructor_exists():
    assert callable(ocl::cst::PropertyContextCS.__init__)


def test_ocl::cst::propertycontextcs_constructor_args():
    sig = inspect.signature(ocl::cst::PropertyContextCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::operationcontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OperationContextDeclCS)


def test_ocl::cst::operationcontextdeclcs_constructor_exists():
    assert callable(ocl::cst::OperationContextDeclCS.__init__)


def test_ocl::cst::operationcontextdeclcs_constructor_args():
    sig = inspect.signature(ocl::cst::OperationContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OCLMessageArgCS)


def test_ocl::cst::oclmessageargcs_constructor_exists():
    assert callable(ocl::cst::OCLMessageArgCS.__init__)


def test_ocl::cst::oclmessageargcs_constructor_args():
    sig = inspect.signature(ocl::cst::OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::prepostorbodydeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PrePostOrBodyDeclCS)


def test_ocl::cst::prepostorbodydeclcs_constructor_exists():
    assert callable(ocl::cst::PrePostOrBodyDeclCS.__init__)


def test_ocl::cst::prepostorbodydeclcs_constructor_args():
    sig = inspect.signature(ocl::cst::PrePostOrBodyDeclCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::cst::prepostorbodydeclcs_has_kind():
    assert hasattr(ocl::cst::PrePostOrBodyDeclCS, "kind")
    descriptor = None
    for klass in ocl::cst::PrePostOrBodyDeclCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::ismarkedprecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::IsMarkedPreCS)


def test_ocl::cst::ismarkedprecs_constructor_exists():
    assert callable(ocl::cst::IsMarkedPreCS.__init__)


def test_ocl::cst::ismarkedprecs_constructor_args():
    sig = inspect.signature(ocl::cst::IsMarkedPreCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::defexpressioncs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::DefExpressionCS)


def test_ocl::cst::defexpressioncs_constructor_exists():
    assert callable(ocl::cst::DefExpressionCS.__init__)


def test_ocl::cst::defexpressioncs_constructor_args():
    sig = inspect.signature(ocl::cst::DefExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::ContextDeclCS)


def test_ocl::cst::contextdeclcs_constructor_exists():
    assert callable(ocl::cst::ContextDeclCS.__init__)


def test_ocl::cst::contextdeclcs_constructor_args():
    sig = inspect.signature(ocl::cst::ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::operationcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OperationCS)


def test_ocl::cst::operationcs_constructor_exists():
    assert callable(ocl::cst::OperationCS.__init__)


def test_ocl::cst::operationcs_constructor_args():
    sig = inspect.signature(ocl::cst::OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::variablecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::VariableCS)


def test_ocl::cst::variablecs_constructor_exists():
    assert callable(ocl::cst::VariableCS.__init__)


def test_ocl::cst::variablecs_constructor_args():
    sig = inspect.signature(ocl::cst::VariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::cst::variablecs_has_name():
    assert hasattr(ocl::cst::VariableCS, "name")
    descriptor = None
    for klass in ocl::cst::VariableCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::initordervaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::InitOrDerValueCS)


def test_ocl::cst::initordervaluecs_constructor_exists():
    assert callable(ocl::cst::InitOrDerValueCS.__init__)


def test_ocl::cst::initordervaluecs_constructor_args():
    sig = inspect.signature(ocl::cst::InitOrDerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OCLExpressionCS)


def test_ocl::cst::oclexpressioncs_constructor_exists():
    assert callable(ocl::cst::OCLExpressionCS.__init__)


def test_ocl::cst::oclexpressioncs_constructor_args():
    sig = inspect.signature(ocl::cst::OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::invordefcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::InvOrDefCS)


def test_ocl::cst::invordefcs_constructor_exists():
    assert callable(ocl::cst::InvOrDefCS.__init__)


def test_ocl::cst::invordefcs_constructor_args():
    sig = inspect.signature(ocl::cst::InvOrDefCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PackageDeclarationCS)


def test_ocl::cst::packagedeclarationcs_constructor_exists():
    assert callable(ocl::cst::PackageDeclarationCS.__init__)


def test_ocl::cst::packagedeclarationcs_constructor_args():
    sig = inspect.signature(ocl::cst::PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::cstnode_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CSTNode)


def test_ocl::cst::cstnode_constructor_exists():
    assert callable(ocl::cst::CSTNode.__init__)


def test_ocl::cst::cstnode_constructor_args():
    sig = inspect.signature(ocl::cst::CSTNode.__init__)
    params = list(sig.parameters.keys())
    assert "endToken" in params, "Missing parameter 'endToken'"
    assert "ast" in params, "Missing parameter 'ast'"
    assert "endOffset" in params, "Missing parameter 'endOffset'"
    assert "startOffset" in params, "Missing parameter 'startOffset'"
    assert "startToken" in params, "Missing parameter 'startToken'"

def test_ocl::cst::cstnode_has_endToken():
    assert hasattr(ocl::cst::CSTNode, "endToken")
    descriptor = None
    for klass in ocl::cst::CSTNode.__mro__:
        if "endToken" in klass.__dict__:
            descriptor = klass.__dict__["endToken"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::cstnode_has_ast():
    assert hasattr(ocl::cst::CSTNode, "ast")
    descriptor = None
    for klass in ocl::cst::CSTNode.__mro__:
        if "ast" in klass.__dict__:
            descriptor = klass.__dict__["ast"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::cstnode_has_endOffset():
    assert hasattr(ocl::cst::CSTNode, "endOffset")
    descriptor = None
    for klass in ocl::cst::CSTNode.__mro__:
        if "endOffset" in klass.__dict__:
            descriptor = klass.__dict__["endOffset"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::cstnode_has_startOffset():
    assert hasattr(ocl::cst::CSTNode, "startOffset")
    descriptor = None
    for klass in ocl::cst::CSTNode.__mro__:
        if "startOffset" in klass.__dict__:
            descriptor = klass.__dict__["startOffset"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::cstnode_has_startToken():
    assert hasattr(ocl::cst::CSTNode, "startToken")
    descriptor = None
    for klass in ocl::cst::CSTNode.__mro__:
        if "startToken" in klass.__dict__:
            descriptor = klass.__dict__["startToken"]
            break
    assert isinstance(descriptor, property)



def test_cst::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(cst::LiteralExpCS)


def test_cst::literalexpcs_constructor_exists():
    assert callable(cst::LiteralExpCS.__init__)


def test_cst::literalexpcs_constructor_args():
    sig = inspect.signature(cst::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::InvalidLiteralExpCS)


def test_ocl::cst::invalidliteralexpcs_constructor_exists():
    assert callable(ocl::cst::InvalidLiteralExpCS.__init__)


def test_ocl::cst::invalidliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::NullLiteralExpCS)


def test_ocl::cst::nullliteralexpcs_constructor_exists():
    assert callable(ocl::cst::NullLiteralExpCS.__init__)


def test_ocl::cst::nullliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(cst::PrimitiveLiteralExpCS)


def test_cst::primitiveliteralexpcs_constructor_exists():
    assert callable(cst::PrimitiveLiteralExpCS.__init__)


def test_cst::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(cst::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::BooleanLiteralExpCS)


def test_ocl::cst::booleanliteralexpcs_constructor_exists():
    assert callable(ocl::cst::BooleanLiteralExpCS.__init__)


def test_ocl::cst::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl::cst::booleanliteralexpcs_has_booleanSymbol():
    assert hasattr(ocl::cst::BooleanLiteralExpCS, "booleanSymbol")
    descriptor = None
    for klass in ocl::cst::BooleanLiteralExpCS.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::ocldocumentcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OCLDocumentCS)


def test_ocl::cst::ocldocumentcs_constructor_exists():
    assert callable(ocl::cst::OCLDocumentCS.__init__)


def test_ocl::cst::ocldocumentcs_constructor_args():
    sig = inspect.signature(ocl::cst::OCLDocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpcs_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpCS)


def test_featurecallexpcs_constructor_exists():
    assert callable(FeatureCallExpCS.__init__)


def test_featurecallexpcs_constructor_args():
    sig = inspect.signature(FeatureCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::OperationCallExpCS)


def test_ocl::cst::operationcallexpcs_constructor_exists():
    assert callable(ocl::cst::OperationCallExpCS.__init__)


def test_ocl::cst::operationcallexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_ocl::cst::operationcallexpcs_has_isAtomic():
    assert hasattr(ocl::cst::OperationCallExpCS, "isAtomic")
    descriptor = None
    for klass in ocl::cst::OperationCallExpCS.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::IterateExpCS)


def test_ocl::cst::iterateexpcs_constructor_exists():
    assert callable(ocl::cst::IterateExpCS.__init__)


def test_ocl::cst::iterateexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::iteratorexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::IteratorExpCS)


def test_ocl::cst::iteratorexpcs_constructor_exists():
    assert callable(ocl::cst::IteratorExpCS.__init__)


def test_ocl::cst::iteratorexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::IteratorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::featurecallexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::FeatureCallExpCS)


def test_ocl::cst::featurecallexpcs_constructor_exists():
    assert callable(ocl::cst::FeatureCallExpCS.__init__)


def test_ocl::cst::featurecallexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::FeatureCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::loopexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::LoopExpCS)


def test_ocl::cst::loopexpcs_constructor_exists():
    assert callable(ocl::cst::LoopExpCS.__init__)


def test_ocl::cst::loopexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::callexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CallExpCS)


def test_ocl::cst::callexpcs_constructor_exists():
    assert callable(ocl::cst::CallExpCS.__init__)


def test_ocl::cst::callexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::CallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_ocl::cst::callexpcs_has_accessor():
    assert hasattr(ocl::cst::CallExpCS, "accessor")
    descriptor = None
    for klass in ocl::cst::CallExpCS.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(OCLMessageArgCS)


def test_oclmessageargcs_constructor_exists():
    assert callable(OCLMessageArgCS.__init__)


def test_oclmessageargcs_constructor_args():
    sig = inspect.signature(OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::UnlimitedNaturalLiteralExpCS)


def test_ocl::cst::unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(ocl::cst::UnlimitedNaturalLiteralExpCS.__init__)


def test_ocl::cst::unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"
    assert "extendedIntegerSymbol" in params, "Missing parameter 'extendedIntegerSymbol'"
    assert "longSymbol" in params, "Missing parameter 'longSymbol'"

def test_ocl::cst::unlimitednaturalliteralexpcs_has_integerSymbol():
    assert hasattr(ocl::cst::UnlimitedNaturalLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in ocl::cst::UnlimitedNaturalLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::unlimitednaturalliteralexpcs_has_extendedIntegerSymbol():
    assert hasattr(ocl::cst::UnlimitedNaturalLiteralExpCS, "extendedIntegerSymbol")
    descriptor = None
    for klass in ocl::cst::UnlimitedNaturalLiteralExpCS.__mro__:
        if "extendedIntegerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["extendedIntegerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::unlimitednaturalliteralexpcs_has_longSymbol():
    assert hasattr(ocl::cst::UnlimitedNaturalLiteralExpCS, "longSymbol")
    descriptor = None
    for klass in ocl::cst::UnlimitedNaturalLiteralExpCS.__mro__:
        if "longSymbol" in klass.__dict__:
            descriptor = klass.__dict__["longSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::StringLiteralExpCS)


def test_ocl::cst::stringliteralexpcs_constructor_exists():
    assert callable(ocl::cst::StringLiteralExpCS.__init__)


def test_ocl::cst::stringliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "unescapedStringSymbol" in params, "Missing parameter 'unescapedStringSymbol'"
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl::cst::stringliteralexpcs_has_unescapedStringSymbol():
    assert hasattr(ocl::cst::StringLiteralExpCS, "unescapedStringSymbol")
    descriptor = None
    for klass in ocl::cst::StringLiteralExpCS.__mro__:
        if "unescapedStringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["unescapedStringSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::stringliteralexpcs_has_stringSymbol():
    assert hasattr(ocl::cst::StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in ocl::cst::StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::realliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::RealLiteralExpCS)


def test_ocl::cst::realliteralexpcs_constructor_exists():
    assert callable(ocl::cst::RealLiteralExpCS.__init__)


def test_ocl::cst::realliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::RealLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl::cst::realliteralexpcs_has_realSymbol():
    assert hasattr(ocl::cst::RealLiteralExpCS, "realSymbol")
    descriptor = None
    for klass in ocl::cst::RealLiteralExpCS.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::integerliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::IntegerLiteralExpCS)


def test_ocl::cst::integerliteralexpcs_constructor_exists():
    assert callable(ocl::cst::IntegerLiteralExpCS.__init__)


def test_ocl::cst::integerliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::IntegerLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "extendedIntegerSymbol" in params, "Missing parameter 'extendedIntegerSymbol'"
    assert "longSymbol" in params, "Missing parameter 'longSymbol'"
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl::cst::integerliteralexpcs_has_extendedIntegerSymbol():
    assert hasattr(ocl::cst::IntegerLiteralExpCS, "extendedIntegerSymbol")
    descriptor = None
    for klass in ocl::cst::IntegerLiteralExpCS.__mro__:
        if "extendedIntegerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["extendedIntegerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::integerliteralexpcs_has_longSymbol():
    assert hasattr(ocl::cst::IntegerLiteralExpCS, "longSymbol")
    descriptor = None
    for klass in ocl::cst::IntegerLiteralExpCS.__mro__:
        if "longSymbol" in klass.__dict__:
            descriptor = klass.__dict__["longSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl::cst::integerliteralexpcs_has_integerSymbol():
    assert hasattr(ocl::cst::IntegerLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in ocl::cst::IntegerLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CollectionLiteralPartCS)


def test_ocl::cst::collectionliteralpartcs_constructor_exists():
    assert callable(ocl::cst::CollectionLiteralPartCS.__init__)


def test_ocl::cst::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(ocl::cst::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPartCS)


def test_collectionliteralpartcs_constructor_exists():
    assert callable(CollectionLiteralPartCS.__init__)


def test_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::collectionrangecs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CollectionRangeCS)


def test_ocl::cst::collectionrangecs_constructor_exists():
    assert callable(ocl::cst::CollectionRangeCS.__init__)


def test_ocl::cst::collectionrangecs_constructor_args():
    sig = inspect.signature(ocl::cst::CollectionRangeCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::TupleLiteralExpCS)


def test_ocl::cst::tupleliteralexpcs_constructor_exists():
    assert callable(ocl::cst::TupleLiteralExpCS.__init__)


def test_ocl::cst::tupleliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl::cst::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::PrimitiveLiteralExpCS)


def test_ocl::cst::primitiveliteralexpcs_constructor_exists():
    assert callable(ocl::cst::PrimitiveLiteralExpCS.__init__)


def test_ocl::cst::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocl::cst::primitiveliteralexpcs_has_symbol():
    assert hasattr(ocl::cst::PrimitiveLiteralExpCS, "symbol")
    descriptor = None
    for klass in ocl::cst::PrimitiveLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::cst::collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl::cst::CollectionLiteralExpCS)


def test_ocl::cst::collectionliteralexpcs_constructor_exists():
    assert callable(ocl::cst::CollectionLiteralExpCS.__init__)


def test_ocl::cst::collectionliteralexpcs_constructor_args():
    sig = inspect.signature(ocl::cst::CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "collectionType" in params, "Missing parameter 'collectionType'"

def test_ocl::cst::collectionliteralexpcs_has_collectionType():
    assert hasattr(ocl::cst::CollectionLiteralExpCS, "collectionType")
    descriptor = None
    for klass in ocl::cst::CollectionLiteralExpCS.__mro__:
        if "collectionType" in klass.__dict__:
            descriptor = klass.__dict__["collectionType"]
            break
    assert isinstance(descriptor, property)

def test_prepostorbodyenum_exists():
    # Check that the Enumeration exists
    assert PrePostOrBodyEnum is not None

def test_prepostorbodyenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrePostOrBodyEnum]
    expected_literals = [
        "body",
        "pre",
        "post",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrePostOrBodyEnum"

def test_simpletypeenum_exists():
    # Check that the Enumeration exists
    assert SimpleTypeEnum is not None

def test_simpletypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleTypeEnum]
    expected_literals = [
        "Integer",
        "identifier",
        "OclAny",
        "String",
        "Boolean",
        "OclMessage",
        "self",
        "UnlimitedNatural",
        "OclVoid",
        "OclInvalid",
        "keyword",
        "Real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleTypeEnum"

def test_dotorarrowenum_exists():
    # Check that the Enumeration exists
    assert DotOrArrowEnum is not None

def test_dotorarrowenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DotOrArrowEnum]
    expected_literals = [
        "none",
        "arrow",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DotOrArrowEnum"

def test_collectiontypeidentifierenum_exists():
    # Check that the Enumeration exists
    assert CollectionTypeIdentifierEnum is not None

def test_collectiontypeidentifierenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionTypeIdentifierEnum]
    expected_literals = [
        "Set",
        "Collection",
        "Bag",
        "Sequence",
        "OrderedSet",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionTypeIdentifierEnum"

def test_messageexpkind_exists():
    # Check that the Enumeration exists
    assert MessageExpKind is not None

def test_messageexpkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageExpKind]
    expected_literals = [
        "sent",
        "hasSent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageExpKind"


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
cst::TypeCS_strategy = st.builds(
    cst::TypeCS,
)
cst::SimpleNameCS_strategy = st.builds(
    cst::SimpleNameCS,
)
ocl::cst::CollectionTypeCS_strategy = st.builds(
    ocl::cst::CollectionTypeCS,
    collectionTypeIdentifier=
        safe_text
)
ocl::cst::PrimitiveTypeCS_strategy = st.builds(
    ocl::cst::PrimitiveTypeCS,
)
IsMarkedPreCS_strategy = st.builds(
    IsMarkedPreCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
PrePostOrBodyDeclCS_strategy = st.builds(
    PrePostOrBodyDeclCS,
)
DefExpressionCS_strategy = st.builds(
    DefExpressionCS,
)
OperationCS_strategy = st.builds(
    OperationCS,
)
InvOrDefCS_strategy = st.builds(
    InvOrDefCS,
)
ocl::cst::DefCS_strategy = st.builds(
    ocl::cst::DefCS,
    static=
        st.booleans()
)
ocl::cst::InvCS_strategy = st.builds(
    ocl::cst::InvCS,
)
InitOrDerValueCS_strategy = st.builds(
    InitOrDerValueCS,
)
ocl::cst::InitValueCS_strategy = st.builds(
    ocl::cst::InitValueCS,
)
ocl::cst::DerValueCS_strategy = st.builds(
    ocl::cst::DerValueCS,
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
ocl::cst::SimpleNameCS_strategy = st.builds(
    ocl::cst::SimpleNameCS,
    value=
        safe_text,
    type=
        safe_text
)
ocl::cst::LiteralExpCS_strategy = st.builds(
    ocl::cst::LiteralExpCS,
)
ocl::cst::IfExpCS_strategy = st.builds(
    ocl::cst::IfExpCS,
)
ocl::cst::MessageExpCS_strategy = st.builds(
    ocl::cst::MessageExpCS,
    kind=
        safe_text
)
ocl::cst::LetExpCS_strategy = st.builds(
    ocl::cst::LetExpCS,
)
ocl::cst::VariableExpCS_strategy = st.builds(
    ocl::cst::VariableExpCS,
)
ocl::cst::TypeCS_strategy = st.builds(
    ocl::cst::TypeCS,
)
SimpleNameCS_strategy = st.builds(
    SimpleNameCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
ocl::cst::TupleTypeCS_strategy = st.builds(
    ocl::cst::TupleTypeCS,
)
ocl::cst::PathNameCS_strategy = st.builds(
    ocl::cst::PathNameCS,
)
PackageDeclarationCS_strategy = st.builds(
    PackageDeclarationCS,
)
ContextDeclCS_strategy = st.builds(
    ContextDeclCS,
)
ocl::cst::ClassifierContextDeclCS_strategy = st.builds(
    ocl::cst::ClassifierContextDeclCS,
)
ocl::cst::PropertyContextCS_strategy = st.builds(
    ocl::cst::PropertyContextCS,
)
ocl::cst::OperationContextDeclCS_strategy = st.builds(
    ocl::cst::OperationContextDeclCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
ocl::cst::OCLMessageArgCS_strategy = st.builds(
    ocl::cst::OCLMessageArgCS,
)
ocl::cst::PrePostOrBodyDeclCS_strategy = st.builds(
    ocl::cst::PrePostOrBodyDeclCS,
    kind=
        safe_text
)
ocl::cst::IsMarkedPreCS_strategy = st.builds(
    ocl::cst::IsMarkedPreCS,
)
ocl::cst::DefExpressionCS_strategy = st.builds(
    ocl::cst::DefExpressionCS,
)
ocl::cst::ContextDeclCS_strategy = st.builds(
    ocl::cst::ContextDeclCS,
)
ocl::cst::OperationCS_strategy = st.builds(
    ocl::cst::OperationCS,
)
ocl::cst::VariableCS_strategy = st.builds(
    ocl::cst::VariableCS,
    name=
        safe_text
)
ocl::cst::InitOrDerValueCS_strategy = st.builds(
    ocl::cst::InitOrDerValueCS,
)
ocl::cst::OCLExpressionCS_strategy = st.builds(
    ocl::cst::OCLExpressionCS,
)
ocl::cst::InvOrDefCS_strategy = st.builds(
    ocl::cst::InvOrDefCS,
)
ocl::cst::PackageDeclarationCS_strategy = st.builds(
    ocl::cst::PackageDeclarationCS,
)
ocl::cst::CSTNode_strategy = st.builds(
    ocl::cst::CSTNode,
    endToken=
        safe_text,
    ast=
        safe_text,
    endOffset=
        st.integers(),
    startOffset=
        st.integers(),
    startToken=
        safe_text
)
cst::LiteralExpCS_strategy = st.builds(
    cst::LiteralExpCS,
)
ocl::cst::InvalidLiteralExpCS_strategy = st.builds(
    ocl::cst::InvalidLiteralExpCS,
)
ocl::cst::NullLiteralExpCS_strategy = st.builds(
    ocl::cst::NullLiteralExpCS,
)
cst::PrimitiveLiteralExpCS_strategy = st.builds(
    cst::PrimitiveLiteralExpCS,
)
ocl::cst::BooleanLiteralExpCS_strategy = st.builds(
    ocl::cst::BooleanLiteralExpCS,
    booleanSymbol=
        safe_text
)
ocl::cst::OCLDocumentCS_strategy = st.builds(
    ocl::cst::OCLDocumentCS,
)
FeatureCallExpCS_strategy = st.builds(
    FeatureCallExpCS,
)
ocl::cst::OperationCallExpCS_strategy = st.builds(
    ocl::cst::OperationCallExpCS,
    isAtomic=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
ocl::cst::IterateExpCS_strategy = st.builds(
    ocl::cst::IterateExpCS,
)
ocl::cst::IteratorExpCS_strategy = st.builds(
    ocl::cst::IteratorExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
ocl::cst::FeatureCallExpCS_strategy = st.builds(
    ocl::cst::FeatureCallExpCS,
)
ocl::cst::LoopExpCS_strategy = st.builds(
    ocl::cst::LoopExpCS,
)
ocl::cst::CallExpCS_strategy = st.builds(
    ocl::cst::CallExpCS,
    accessor=
        safe_text
)
OCLMessageArgCS_strategy = st.builds(
    OCLMessageArgCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
ocl::cst::UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    ocl::cst::UnlimitedNaturalLiteralExpCS,
    integerSymbol=
        safe_text,
    extendedIntegerSymbol=
        safe_text,
    longSymbol=
        safe_text
)
ocl::cst::StringLiteralExpCS_strategy = st.builds(
    ocl::cst::StringLiteralExpCS,
    unescapedStringSymbol=
        safe_text,
    stringSymbol=
        safe_text
)
ocl::cst::RealLiteralExpCS_strategy = st.builds(
    ocl::cst::RealLiteralExpCS,
    realSymbol=
        safe_text
)
ocl::cst::IntegerLiteralExpCS_strategy = st.builds(
    ocl::cst::IntegerLiteralExpCS,
    extendedIntegerSymbol=
        safe_text,
    longSymbol=
        safe_text,
    integerSymbol=
        safe_text
)
ocl::cst::CollectionLiteralPartCS_strategy = st.builds(
    ocl::cst::CollectionLiteralPartCS,
)
CollectionLiteralPartCS_strategy = st.builds(
    CollectionLiteralPartCS,
)
ocl::cst::CollectionRangeCS_strategy = st.builds(
    ocl::cst::CollectionRangeCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
ocl::cst::TupleLiteralExpCS_strategy = st.builds(
    ocl::cst::TupleLiteralExpCS,
)
ocl::cst::PrimitiveLiteralExpCS_strategy = st.builds(
    ocl::cst::PrimitiveLiteralExpCS,
    symbol=
        safe_text
)
ocl::cst::CollectionLiteralExpCS_strategy = st.builds(
    ocl::cst::CollectionLiteralExpCS,
    collectionType=
        safe_text
)

@given(instance=cst::TypeCS_strategy)
@settings(max_examples=50)
def test_cst::typecs_instantiation(instance):
    assert isinstance(instance, cst::TypeCS)

@given(instance=cst::SimpleNameCS_strategy)
@settings(max_examples=50)
def test_cst::simplenamecs_instantiation(instance):
    assert isinstance(instance, cst::SimpleNameCS)

@given(instance=ocl::cst::CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::collectiontypecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::CollectionTypeCS)

@given(instance=ocl::cst::CollectionTypeCS_strategy)
def test_ocl::cst::collectiontypecs_collectionTypeIdentifier_type(instance):
    assert isinstance(instance.collectionTypeIdentifier, str)


@given(instance=ocl::cst::CollectionTypeCS_strategy)
def test_ocl::cst::collectiontypecs_collectionTypeIdentifier_setter(instance):
    original = instance.collectionTypeIdentifier
    instance.collectionTypeIdentifier = original
    assert instance.collectionTypeIdentifier == original

@given(instance=ocl::cst::PrimitiveTypeCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::primitivetypecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PrimitiveTypeCS)

@given(instance=IsMarkedPreCS_strategy)
@settings(max_examples=50)
def test_ismarkedprecs_instantiation(instance):
    assert isinstance(instance, IsMarkedPreCS)

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=PrePostOrBodyDeclCS_strategy)
@settings(max_examples=50)
def test_prepostorbodydeclcs_instantiation(instance):
    assert isinstance(instance, PrePostOrBodyDeclCS)

@given(instance=DefExpressionCS_strategy)
@settings(max_examples=50)
def test_defexpressioncs_instantiation(instance):
    assert isinstance(instance, DefExpressionCS)

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=InvOrDefCS_strategy)
@settings(max_examples=50)
def test_invordefcs_instantiation(instance):
    assert isinstance(instance, InvOrDefCS)

@given(instance=ocl::cst::DefCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::defcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::DefCS)

@given(instance=ocl::cst::DefCS_strategy)
def test_ocl::cst::defcs_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ocl::cst::DefCS_strategy)
def test_ocl::cst::defcs_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ocl::cst::InvCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::invcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::InvCS)

@given(instance=InitOrDerValueCS_strategy)
@settings(max_examples=50)
def test_initordervaluecs_instantiation(instance):
    assert isinstance(instance, InitOrDerValueCS)

@given(instance=ocl::cst::InitValueCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::initvaluecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::InitValueCS)

@given(instance=ocl::cst::DerValueCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::dervaluecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::DerValueCS)

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=ocl::cst::SimpleNameCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::simplenamecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::SimpleNameCS)

@given(instance=ocl::cst::SimpleNameCS_strategy)
def test_ocl::cst::simplenamecs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ocl::cst::SimpleNameCS_strategy)
def test_ocl::cst::simplenamecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ocl::cst::SimpleNameCS_strategy)
def test_ocl::cst::simplenamecs_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ocl::cst::SimpleNameCS_strategy)
def test_ocl::cst::simplenamecs_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ocl::cst::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::literalexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::LiteralExpCS)

@given(instance=ocl::cst::IfExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::ifexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::IfExpCS)

@given(instance=ocl::cst::MessageExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::messageexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::MessageExpCS)

@given(instance=ocl::cst::MessageExpCS_strategy)
def test_ocl::cst::messageexpcs_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ocl::cst::MessageExpCS_strategy)
def test_ocl::cst::messageexpcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl::cst::LetExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::letexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::LetExpCS)

@given(instance=ocl::cst::VariableExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::variableexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::VariableExpCS)

@given(instance=ocl::cst::TypeCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::typecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::TypeCS)

@given(instance=SimpleNameCS_strategy)
@settings(max_examples=50)
def test_simplenamecs_instantiation(instance):
    assert isinstance(instance, SimpleNameCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=ocl::cst::TupleTypeCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::tupletypecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::TupleTypeCS)

@given(instance=ocl::cst::PathNameCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::pathnamecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PathNameCS)

@given(instance=PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, PackageDeclarationCS)

@given(instance=ContextDeclCS_strategy)
@settings(max_examples=50)
def test_contextdeclcs_instantiation(instance):
    assert isinstance(instance, ContextDeclCS)

@given(instance=ocl::cst::ClassifierContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::classifiercontextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::ClassifierContextDeclCS)

@given(instance=ocl::cst::PropertyContextCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::propertycontextcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PropertyContextCS)

@given(instance=ocl::cst::OperationContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::operationcontextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OperationContextDeclCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=ocl::cst::OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::oclmessageargcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OCLMessageArgCS)

@given(instance=ocl::cst::PrePostOrBodyDeclCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::prepostorbodydeclcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PrePostOrBodyDeclCS)

@given(instance=ocl::cst::PrePostOrBodyDeclCS_strategy)
def test_ocl::cst::prepostorbodydeclcs_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ocl::cst::PrePostOrBodyDeclCS_strategy)
def test_ocl::cst::prepostorbodydeclcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl::cst::IsMarkedPreCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::ismarkedprecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::IsMarkedPreCS)

@given(instance=ocl::cst::DefExpressionCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::defexpressioncs_instantiation(instance):
    assert isinstance(instance, ocl::cst::DefExpressionCS)

@given(instance=ocl::cst::ContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::contextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::ContextDeclCS)

@given(instance=ocl::cst::OperationCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::operationcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OperationCS)

@given(instance=ocl::cst::VariableCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::variablecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::VariableCS)

@given(instance=ocl::cst::VariableCS_strategy)
def test_ocl::cst::variablecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::cst::VariableCS_strategy)
def test_ocl::cst::variablecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl::cst::InitOrDerValueCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::initordervaluecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::InitOrDerValueCS)

@given(instance=ocl::cst::OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::oclexpressioncs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OCLExpressionCS)

@given(instance=ocl::cst::InvOrDefCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::invordefcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::InvOrDefCS)

@given(instance=ocl::cst::PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PackageDeclarationCS)

@given(instance=ocl::cst::CSTNode_strategy)
@settings(max_examples=50)
def test_ocl::cst::cstnode_instantiation(instance):
    assert isinstance(instance, ocl::cst::CSTNode)

@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_endToken_type(instance):
    assert isinstance(instance.endToken, str)


@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_endToken_setter(instance):
    original = instance.endToken
    instance.endToken = original
    assert instance.endToken == original

@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_ast_type(instance):
    assert isinstance(instance.ast, str)


@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_ast_setter(instance):
    original = instance.ast
    instance.ast = original
    assert instance.ast == original

@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_endOffset_type(instance):
    assert isinstance(instance.endOffset, int)


@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_endOffset_setter(instance):
    original = instance.endOffset
    instance.endOffset = original
    assert instance.endOffset == original

@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_startOffset_type(instance):
    assert isinstance(instance.startOffset, int)


@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_startOffset_setter(instance):
    original = instance.startOffset
    instance.startOffset = original
    assert instance.startOffset == original

@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_startToken_type(instance):
    assert isinstance(instance.startToken, str)


@given(instance=ocl::cst::CSTNode_strategy)
def test_ocl::cst::cstnode_startToken_setter(instance):
    original = instance.startToken
    instance.startToken = original
    assert instance.startToken == original

@given(instance=cst::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_cst::literalexpcs_instantiation(instance):
    assert isinstance(instance, cst::LiteralExpCS)

@given(instance=ocl::cst::InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::InvalidLiteralExpCS)

@given(instance=ocl::cst::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::NullLiteralExpCS)

@given(instance=cst::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_cst::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, cst::PrimitiveLiteralExpCS)

@given(instance=ocl::cst::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::BooleanLiteralExpCS)

@given(instance=ocl::cst::BooleanLiteralExpCS_strategy)
def test_ocl::cst::booleanliteralexpcs_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=ocl::cst::BooleanLiteralExpCS_strategy)
def test_ocl::cst::booleanliteralexpcs_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=ocl::cst::OCLDocumentCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::ocldocumentcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OCLDocumentCS)

@given(instance=FeatureCallExpCS_strategy)
@settings(max_examples=50)
def test_featurecallexpcs_instantiation(instance):
    assert isinstance(instance, FeatureCallExpCS)

@given(instance=ocl::cst::OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::operationcallexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::OperationCallExpCS)

@given(instance=ocl::cst::OperationCallExpCS_strategy)
def test_ocl::cst::operationcallexpcs_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=ocl::cst::OperationCallExpCS_strategy)
def test_ocl::cst::operationcallexpcs_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=ocl::cst::IterateExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::iterateexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::IterateExpCS)

@given(instance=ocl::cst::IteratorExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::iteratorexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::IteratorExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=ocl::cst::FeatureCallExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::featurecallexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::FeatureCallExpCS)

@given(instance=ocl::cst::LoopExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::loopexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::LoopExpCS)

@given(instance=ocl::cst::CallExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::callexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::CallExpCS)

@given(instance=ocl::cst::CallExpCS_strategy)
def test_ocl::cst::callexpcs_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=ocl::cst::CallExpCS_strategy)
def test_ocl::cst::callexpcs_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_oclmessageargcs_instantiation(instance):
    assert isinstance(instance, OCLMessageArgCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::UnlimitedNaturalLiteralExpCS)

@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_extendedIntegerSymbol_type(instance):
    assert isinstance(instance.extendedIntegerSymbol, str)


@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_extendedIntegerSymbol_setter(instance):
    original = instance.extendedIntegerSymbol
    instance.extendedIntegerSymbol = original
    assert instance.extendedIntegerSymbol == original

@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_longSymbol_type(instance):
    assert isinstance(instance.longSymbol, str)


@given(instance=ocl::cst::UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl::cst::unlimitednaturalliteralexpcs_longSymbol_setter(instance):
    original = instance.longSymbol
    instance.longSymbol = original
    assert instance.longSymbol == original

@given(instance=ocl::cst::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::StringLiteralExpCS)

@given(instance=ocl::cst::StringLiteralExpCS_strategy)
def test_ocl::cst::stringliteralexpcs_unescapedStringSymbol_type(instance):
    assert isinstance(instance.unescapedStringSymbol, str)


@given(instance=ocl::cst::StringLiteralExpCS_strategy)
def test_ocl::cst::stringliteralexpcs_unescapedStringSymbol_setter(instance):
    original = instance.unescapedStringSymbol
    instance.unescapedStringSymbol = original
    assert instance.unescapedStringSymbol == original

@given(instance=ocl::cst::StringLiteralExpCS_strategy)
def test_ocl::cst::stringliteralexpcs_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=ocl::cst::StringLiteralExpCS_strategy)
def test_ocl::cst::stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=ocl::cst::RealLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::realliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::RealLiteralExpCS)

@given(instance=ocl::cst::RealLiteralExpCS_strategy)
def test_ocl::cst::realliteralexpcs_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=ocl::cst::RealLiteralExpCS_strategy)
def test_ocl::cst::realliteralexpcs_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::integerliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::IntegerLiteralExpCS)

@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_extendedIntegerSymbol_type(instance):
    assert isinstance(instance.extendedIntegerSymbol, str)


@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_extendedIntegerSymbol_setter(instance):
    original = instance.extendedIntegerSymbol
    instance.extendedIntegerSymbol = original
    assert instance.extendedIntegerSymbol == original

@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_longSymbol_type(instance):
    assert isinstance(instance.longSymbol, str)


@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_longSymbol_setter(instance):
    original = instance.longSymbol
    instance.longSymbol = original
    assert instance.longSymbol == original

@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=ocl::cst::IntegerLiteralExpCS_strategy)
def test_ocl::cst::integerliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=ocl::cst::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::CollectionLiteralPartCS)

@given(instance=CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPartCS)

@given(instance=ocl::cst::CollectionRangeCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::collectionrangecs_instantiation(instance):
    assert isinstance(instance, ocl::cst::CollectionRangeCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=ocl::cst::TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::TupleLiteralExpCS)

@given(instance=ocl::cst::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::PrimitiveLiteralExpCS)

@given(instance=ocl::cst::PrimitiveLiteralExpCS_strategy)
def test_ocl::cst::primitiveliteralexpcs_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=ocl::cst::PrimitiveLiteralExpCS_strategy)
def test_ocl::cst::primitiveliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=ocl::cst::CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl::cst::collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl::cst::CollectionLiteralExpCS)

@given(instance=ocl::cst::CollectionLiteralExpCS_strategy)
def test_ocl::cst::collectionliteralexpcs_collectionType_type(instance):
    assert isinstance(instance.collectionType, str)


@given(instance=ocl::cst::CollectionLiteralExpCS_strategy)
def test_ocl::cst::collectionliteralexpcs_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original

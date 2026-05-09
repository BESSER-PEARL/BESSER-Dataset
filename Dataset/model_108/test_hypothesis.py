import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Block,
    Javadoc,
    CompilationUnit,
    StructuralPackage,
    JavaAbstractSyntax::StructuralPackage,
    MemberValuePair,
    VariableDeclaration,
    JavaAbstractSyntax::VariableDeclarationFragment,
    JavaAbstractSyntax::SingleVariableDeclaration,
    CatchClause,
    Statement,
    JavaAbstractSyntax::VariableDeclarationStatement,
    JavaAbstractSyntax::SynchronizedStatement,
    JavaAbstractSyntax::EmptyStatement,
    JavaAbstractSyntax::DoStatement,
    JavaAbstractSyntax::SwitchStatement,
    JavaAbstractSyntax::SwitchCase,
    JavaAbstractSyntax::LabeledStatement,
    JavaAbstractSyntax::SuperConstructorInvocation,
    JavaAbstractSyntax::WhileStatement,
    JavaAbstractSyntax::ForStatement,
    JavaAbstractSyntax::EnhancedForStatement,
    JavaAbstractSyntax::TypeDeclarationStatement,
    JavaAbstractSyntax::ReturnStatement,
    JavaAbstractSyntax::ThrowStatement,
    JavaAbstractSyntax::ExpressionStatement,
    JavaAbstractSyntax::TryStatement,
    JavaAbstractSyntax::IfStatement,
    JavaAbstractSyntax::AssertStatement,
    JavaAbstractSyntax::ContinueStatement,
    JavaAbstractSyntax::ConstructorInvocation,
    JavaAbstractSyntax::BreakStatement,
    JavaAbstractSyntax::Block,
    TagElement,
    EnumConstantDeclaration,
    ArrayType,
    ArrayInitializer,
    VariableDeclarationFragment,
    AnonymousClassDeclaration,
    TypeParameter,
    Annotation,
    JavaAbstractSyntax::SingleMemberAnnotation,
    JavaAbstractSyntax::NormalAnnotation,
    JavaAbstractSyntax::MarkerAnnotation,
    SimpleName,
    Name,
    JavaAbstractSyntax::SimpleName,
    JavaAbstractSyntax::QualifiedName,
    AbstractTypeDeclaration,
    JavaAbstractSyntax::TypeDeclaration,
    JavaAbstractSyntax::EnumDeclaration,
    JavaAbstractSyntax::AnnotationTypeDeclaration,
    JavaAbstractSyntax::ExtendedModifier,
    Type,
    JavaAbstractSyntax::ArrayType,
    JavaAbstractSyntax::WildcardType,
    JavaAbstractSyntax::SimpleType,
    JavaAbstractSyntax::PrimitiveType,
    JavaAbstractSyntax::ParameterizedType,
    JavaAbstractSyntax::QualifiedType,
    MethodRefParameter,
    Expression,
    JavaAbstractSyntax::ArrayCreation,
    JavaAbstractSyntax::InfixExpression,
    JavaAbstractSyntax::MethodInvocation,
    JavaAbstractSyntax::Name,
    JavaAbstractSyntax::ClassInstanceCreation,
    JavaAbstractSyntax::CharacterLiteral,
    JavaAbstractSyntax::ArrayInitializer,
    JavaAbstractSyntax::ParenthesizedExpression,
    JavaAbstractSyntax::NumberLiteral,
    JavaAbstractSyntax::VariableDeclarationExpression,
    JavaAbstractSyntax::NullLiteral,
    JavaAbstractSyntax::ThisExpression,
    JavaAbstractSyntax::PostfixExpression,
    JavaAbstractSyntax::BooleanLiteral,
    JavaAbstractSyntax::ConditionalExpression,
    JavaAbstractSyntax::ArrayAccess,
    JavaAbstractSyntax::InstanceofExpression,
    JavaAbstractSyntax::StringLiteral,
    JavaAbstractSyntax::CastExpression,
    JavaAbstractSyntax::FieldAccess,
    JavaAbstractSyntax::SuperMethodInvocation,
    JavaAbstractSyntax::PrefixExpression,
    JavaAbstractSyntax::TypeLiteral,
    JavaAbstractSyntax::Assignment,
    JavaAbstractSyntax::SuperFieldAccess,
    BodyDeclaration,
    JavaAbstractSyntax::EnumConstantDeclaration,
    JavaAbstractSyntax::AnnotationTypeMemberDeclaration,
    JavaAbstractSyntax::FieldDeclaration,
    JavaAbstractSyntax::MethodDeclaration,
    JavaAbstractSyntax::Initializer,
    JavaAbstractSyntax::AbstractTypeDeclaration,
    JavaAbstractSyntax::ASTNode,
    ASTNode,
    JavaAbstractSyntax::ImportDeclaration,
    JavaAbstractSyntax::MethodRef,
    JavaAbstractSyntax::Expression,
    JavaAbstractSyntax::MemberValuePair,
    JavaAbstractSyntax::Statement,
    JavaAbstractSyntax::AnonymousClassDeclaration,
    JavaAbstractSyntax::TextElement,
    JavaAbstractSyntax::TagElement,
    JavaAbstractSyntax::MemberRef,
    JavaAbstractSyntax::Type,
    JavaAbstractSyntax::PackageDeclaration,
    JavaAbstractSyntax::VariableDeclaration,
    JavaAbstractSyntax::CatchClause,
    JavaAbstractSyntax::TypeParameter,
    JavaAbstractSyntax::MethodRefParameter,
    JavaAbstractSyntax::AST,
    ImportDeclaration,
    PackageDeclaration,
    Comment,
    JavaAbstractSyntax::LineComment,
    JavaAbstractSyntax::Javadoc,
    JavaAbstractSyntax::BlockComment,
    JavaAbstractSyntax::CompilationUnit,
    JavaAbstractSyntax::Comment,
    SingleVariableDeclaration,
    ExtendedModifier,
    JavaAbstractSyntax::Modifier,
    JavaAbstractSyntax::Annotation,
    JavaAbstractSyntax::BodyDeclaration,
    InfixExpressionOperatorKind,
    PrefixExpresssionOperatorKind,
    PostfixExpresssionOperatorKind,
    AssignementOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_javadoc_is_not_abstract():
    assert not inspect.isabstract(Javadoc)


def test_javadoc_constructor_exists():
    assert callable(Javadoc.__init__)


def test_javadoc_constructor_args():
    sig = inspect.signature(Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_structuralpackage_is_not_abstract():
    assert not inspect.isabstract(StructuralPackage)


def test_structuralpackage_constructor_exists():
    assert callable(StructuralPackage.__init__)


def test_structuralpackage_constructor_args():
    sig = inspect.signature(StructuralPackage.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::structuralpackage_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::StructuralPackage)


def test_javaabstractsyntax::structuralpackage_constructor_exists():
    assert callable(JavaAbstractSyntax::StructuralPackage.__init__)


def test_javaabstractsyntax::structuralpackage_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::StructuralPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javaabstractsyntax::structuralpackage_has_name():
    assert hasattr(JavaAbstractSyntax::StructuralPackage, "name")
    descriptor = None
    for klass in JavaAbstractSyntax::StructuralPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(MemberValuePair)


def test_membervaluepair_constructor_exists():
    assert callable(MemberValuePair.__init__)


def test_membervaluepair_constructor_args():
    sig = inspect.signature(MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::VariableDeclarationFragment)


def test_javaabstractsyntax::variabledeclarationfragment_constructor_exists():
    assert callable(JavaAbstractSyntax::VariableDeclarationFragment.__init__)


def test_javaabstractsyntax::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SingleVariableDeclaration)


def test_javaabstractsyntax::singlevariabledeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::SingleVariableDeclaration.__init__)


def test_javaabstractsyntax::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_javaabstractsyntax::singlevariabledeclaration_has_varargs():
    assert hasattr(JavaAbstractSyntax::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_catchclause_is_not_abstract():
    assert not inspect.isabstract(CatchClause)


def test_catchclause_constructor_exists():
    assert callable(CatchClause.__init__)


def test_catchclause_constructor_args():
    sig = inspect.signature(CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::VariableDeclarationStatement)


def test_javaabstractsyntax::variabledeclarationstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::VariableDeclarationStatement.__init__)


def test_javaabstractsyntax::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SynchronizedStatement)


def test_javaabstractsyntax::synchronizedstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::SynchronizedStatement.__init__)


def test_javaabstractsyntax::synchronizedstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::emptystatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::EmptyStatement)


def test_javaabstractsyntax::emptystatement_constructor_exists():
    assert callable(JavaAbstractSyntax::EmptyStatement.__init__)


def test_javaabstractsyntax::emptystatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::dostatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::DoStatement)


def test_javaabstractsyntax::dostatement_constructor_exists():
    assert callable(JavaAbstractSyntax::DoStatement.__init__)


def test_javaabstractsyntax::dostatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::switchstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SwitchStatement)


def test_javaabstractsyntax::switchstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::SwitchStatement.__init__)


def test_javaabstractsyntax::switchstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::switchcase_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SwitchCase)


def test_javaabstractsyntax::switchcase_constructor_exists():
    assert callable(JavaAbstractSyntax::SwitchCase.__init__)


def test_javaabstractsyntax::switchcase_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_javaabstractsyntax::switchcase_has_default():
    assert hasattr(JavaAbstractSyntax::SwitchCase, "default")
    descriptor = None
    for klass in JavaAbstractSyntax::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::LabeledStatement)


def test_javaabstractsyntax::labeledstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::LabeledStatement.__init__)


def test_javaabstractsyntax::labeledstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SuperConstructorInvocation)


def test_javaabstractsyntax::superconstructorinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax::SuperConstructorInvocation.__init__)


def test_javaabstractsyntax::superconstructorinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::whilestatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::WhileStatement)


def test_javaabstractsyntax::whilestatement_constructor_exists():
    assert callable(JavaAbstractSyntax::WhileStatement.__init__)


def test_javaabstractsyntax::whilestatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::forstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ForStatement)


def test_javaabstractsyntax::forstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::ForStatement.__init__)


def test_javaabstractsyntax::forstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::EnhancedForStatement)


def test_javaabstractsyntax::enhancedforstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::EnhancedForStatement.__init__)


def test_javaabstractsyntax::enhancedforstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TypeDeclarationStatement)


def test_javaabstractsyntax::typedeclarationstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::TypeDeclarationStatement.__init__)


def test_javaabstractsyntax::typedeclarationstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::returnstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ReturnStatement)


def test_javaabstractsyntax::returnstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::ReturnStatement.__init__)


def test_javaabstractsyntax::returnstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::throwstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ThrowStatement)


def test_javaabstractsyntax::throwstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::ThrowStatement.__init__)


def test_javaabstractsyntax::throwstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ExpressionStatement)


def test_javaabstractsyntax::expressionstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::ExpressionStatement.__init__)


def test_javaabstractsyntax::expressionstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::trystatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TryStatement)


def test_javaabstractsyntax::trystatement_constructor_exists():
    assert callable(JavaAbstractSyntax::TryStatement.__init__)


def test_javaabstractsyntax::trystatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::ifstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::IfStatement)


def test_javaabstractsyntax::ifstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::IfStatement.__init__)


def test_javaabstractsyntax::ifstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::assertstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AssertStatement)


def test_javaabstractsyntax::assertstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::AssertStatement.__init__)


def test_javaabstractsyntax::assertstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::continuestatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ContinueStatement)


def test_javaabstractsyntax::continuestatement_constructor_exists():
    assert callable(JavaAbstractSyntax::ContinueStatement.__init__)


def test_javaabstractsyntax::continuestatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ConstructorInvocation)


def test_javaabstractsyntax::constructorinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax::ConstructorInvocation.__init__)


def test_javaabstractsyntax::constructorinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::breakstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::BreakStatement)


def test_javaabstractsyntax::breakstatement_constructor_exists():
    assert callable(JavaAbstractSyntax::BreakStatement.__init__)


def test_javaabstractsyntax::breakstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::block_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Block)


def test_javaabstractsyntax::block_constructor_exists():
    assert callable(JavaAbstractSyntax::Block.__init__)


def test_javaabstractsyntax::block_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Block.__init__)
    params = list(sig.parameters.keys())



def test_tagelement_is_not_abstract():
    assert not inspect.isabstract(TagElement)


def test_tagelement_constructor_exists():
    assert callable(TagElement.__init__)


def test_tagelement_constructor_args():
    sig = inspect.signature(TagElement.__init__)
    params = list(sig.parameters.keys())



def test_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumConstantDeclaration)


def test_enumconstantdeclaration_constructor_exists():
    assert callable(EnumConstantDeclaration.__init__)


def test_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(AnonymousClassDeclaration)


def test_anonymousclassdeclaration_constructor_exists():
    assert callable(AnonymousClassDeclaration.__init__)


def test_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SingleMemberAnnotation)


def test_javaabstractsyntax::singlememberannotation_constructor_exists():
    assert callable(JavaAbstractSyntax::SingleMemberAnnotation.__init__)


def test_javaabstractsyntax::singlememberannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::normalannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::NormalAnnotation)


def test_javaabstractsyntax::normalannotation_constructor_exists():
    assert callable(JavaAbstractSyntax::NormalAnnotation.__init__)


def test_javaabstractsyntax::normalannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::markerannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MarkerAnnotation)


def test_javaabstractsyntax::markerannotation_constructor_exists():
    assert callable(JavaAbstractSyntax::MarkerAnnotation.__init__)


def test_javaabstractsyntax::markerannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_simplename_is_not_abstract():
    assert not inspect.isabstract(SimpleName)


def test_simplename_constructor_exists():
    assert callable(SimpleName.__init__)


def test_simplename_constructor_args():
    sig = inspect.signature(SimpleName.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::simplename_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SimpleName)


def test_javaabstractsyntax::simplename_constructor_exists():
    assert callable(JavaAbstractSyntax::SimpleName.__init__)


def test_javaabstractsyntax::simplename_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_javaabstractsyntax::simplename_has_declaration():
    assert hasattr(JavaAbstractSyntax::SimpleName, "declaration")
    descriptor = None
    for klass in JavaAbstractSyntax::SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::simplename_has_identifier():
    assert hasattr(JavaAbstractSyntax::SimpleName, "identifier")
    descriptor = None
    for klass in JavaAbstractSyntax::SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::QualifiedName)


def test_javaabstractsyntax::qualifiedname_constructor_exists():
    assert callable(JavaAbstractSyntax::QualifiedName.__init__)


def test_javaabstractsyntax::qualifiedname_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TypeDeclaration)


def test_javaabstractsyntax::typedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::TypeDeclaration.__init__)


def test_javaabstractsyntax::typedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_javaabstractsyntax::typedeclaration_has_interface():
    assert hasattr(JavaAbstractSyntax::TypeDeclaration, "interface")
    descriptor = None
    for klass in JavaAbstractSyntax::TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::EnumDeclaration)


def test_javaabstractsyntax::enumdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::EnumDeclaration.__init__)


def test_javaabstractsyntax::enumdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AnnotationTypeDeclaration)


def test_javaabstractsyntax::annotationtypedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::AnnotationTypeDeclaration.__init__)


def test_javaabstractsyntax::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ExtendedModifier)


def test_javaabstractsyntax::extendedmodifier_constructor_exists():
    assert callable(JavaAbstractSyntax::ExtendedModifier.__init__)


def test_javaabstractsyntax::extendedmodifier_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::arraytype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ArrayType)


def test_javaabstractsyntax::arraytype_constructor_exists():
    assert callable(JavaAbstractSyntax::ArrayType.__init__)


def test_javaabstractsyntax::arraytype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_javaabstractsyntax::arraytype_has_dimensions():
    assert hasattr(JavaAbstractSyntax::ArrayType, "dimensions")
    descriptor = None
    for klass in JavaAbstractSyntax::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::WildcardType)


def test_javaabstractsyntax::wildcardtype_constructor_exists():
    assert callable(JavaAbstractSyntax::WildcardType.__init__)


def test_javaabstractsyntax::wildcardtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_javaabstractsyntax::wildcardtype_has_upperBound():
    assert hasattr(JavaAbstractSyntax::WildcardType, "upperBound")
    descriptor = None
    for klass in JavaAbstractSyntax::WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::simpletype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SimpleType)


def test_javaabstractsyntax::simpletype_constructor_exists():
    assert callable(JavaAbstractSyntax::SimpleType.__init__)


def test_javaabstractsyntax::simpletype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::primitivetype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::PrimitiveType)


def test_javaabstractsyntax::primitivetype_constructor_exists():
    assert callable(JavaAbstractSyntax::PrimitiveType.__init__)


def test_javaabstractsyntax::primitivetype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_javaabstractsyntax::primitivetype_has_code():
    assert hasattr(JavaAbstractSyntax::PrimitiveType, "code")
    descriptor = None
    for klass in JavaAbstractSyntax::PrimitiveType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ParameterizedType)


def test_javaabstractsyntax::parameterizedtype_constructor_exists():
    assert callable(JavaAbstractSyntax::ParameterizedType.__init__)


def test_javaabstractsyntax::parameterizedtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::QualifiedType)


def test_javaabstractsyntax::qualifiedtype_constructor_exists():
    assert callable(JavaAbstractSyntax::QualifiedType.__init__)


def test_javaabstractsyntax::qualifiedtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(MethodRefParameter)


def test_methodrefparameter_constructor_exists():
    assert callable(MethodRefParameter.__init__)


def test_methodrefparameter_constructor_args():
    sig = inspect.signature(MethodRefParameter.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::arraycreation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ArrayCreation)


def test_javaabstractsyntax::arraycreation_constructor_exists():
    assert callable(JavaAbstractSyntax::ArrayCreation.__init__)


def test_javaabstractsyntax::arraycreation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::infixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::InfixExpression)


def test_javaabstractsyntax::infixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::InfixExpression.__init__)


def test_javaabstractsyntax::infixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax::infixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax::InfixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MethodInvocation)


def test_javaabstractsyntax::methodinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax::MethodInvocation.__init__)


def test_javaabstractsyntax::methodinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::name_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Name)


def test_javaabstractsyntax::name_constructor_exists():
    assert callable(JavaAbstractSyntax::Name.__init__)


def test_javaabstractsyntax::name_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_javaabstractsyntax::name_has_fullyQualifiedName():
    assert hasattr(JavaAbstractSyntax::Name, "fullyQualifiedName")
    descriptor = None
    for klass in JavaAbstractSyntax::Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ClassInstanceCreation)


def test_javaabstractsyntax::classinstancecreation_constructor_exists():
    assert callable(JavaAbstractSyntax::ClassInstanceCreation.__init__)


def test_javaabstractsyntax::classinstancecreation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::characterliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::CharacterLiteral)


def test_javaabstractsyntax::characterliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::CharacterLiteral.__init__)


def test_javaabstractsyntax::characterliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_javaabstractsyntax::characterliteral_has_escapedValue():
    assert hasattr(JavaAbstractSyntax::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in JavaAbstractSyntax::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::characterliteral_has_charValue():
    assert hasattr(JavaAbstractSyntax::CharacterLiteral, "charValue")
    descriptor = None
    for klass in JavaAbstractSyntax::CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ArrayInitializer)


def test_javaabstractsyntax::arrayinitializer_constructor_exists():
    assert callable(JavaAbstractSyntax::ArrayInitializer.__init__)


def test_javaabstractsyntax::arrayinitializer_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ParenthesizedExpression)


def test_javaabstractsyntax::parenthesizedexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::ParenthesizedExpression.__init__)


def test_javaabstractsyntax::parenthesizedexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::numberliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::NumberLiteral)


def test_javaabstractsyntax::numberliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::NumberLiteral.__init__)


def test_javaabstractsyntax::numberliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_javaabstractsyntax::numberliteral_has_token():
    assert hasattr(JavaAbstractSyntax::NumberLiteral, "token")
    descriptor = None
    for klass in JavaAbstractSyntax::NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::VariableDeclarationExpression)


def test_javaabstractsyntax::variabledeclarationexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::VariableDeclarationExpression.__init__)


def test_javaabstractsyntax::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::nullliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::NullLiteral)


def test_javaabstractsyntax::nullliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::NullLiteral.__init__)


def test_javaabstractsyntax::nullliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::thisexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ThisExpression)


def test_javaabstractsyntax::thisexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::ThisExpression.__init__)


def test_javaabstractsyntax::thisexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::PostfixExpression)


def test_javaabstractsyntax::postfixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::PostfixExpression.__init__)


def test_javaabstractsyntax::postfixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax::postfixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax::PostfixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::BooleanLiteral)


def test_javaabstractsyntax::booleanliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::BooleanLiteral.__init__)


def test_javaabstractsyntax::booleanliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_javaabstractsyntax::booleanliteral_has_booleanValue():
    assert hasattr(JavaAbstractSyntax::BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in JavaAbstractSyntax::BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ConditionalExpression)


def test_javaabstractsyntax::conditionalexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::ConditionalExpression.__init__)


def test_javaabstractsyntax::conditionalexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ArrayAccess)


def test_javaabstractsyntax::arrayaccess_constructor_exists():
    assert callable(JavaAbstractSyntax::ArrayAccess.__init__)


def test_javaabstractsyntax::arrayaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::InstanceofExpression)


def test_javaabstractsyntax::instanceofexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::InstanceofExpression.__init__)


def test_javaabstractsyntax::instanceofexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::stringliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::StringLiteral)


def test_javaabstractsyntax::stringliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::StringLiteral.__init__)


def test_javaabstractsyntax::stringliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_javaabstractsyntax::stringliteral_has_literalValue():
    assert hasattr(JavaAbstractSyntax::StringLiteral, "literalValue")
    descriptor = None
    for klass in JavaAbstractSyntax::StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::stringliteral_has_escapedValue():
    assert hasattr(JavaAbstractSyntax::StringLiteral, "escapedValue")
    descriptor = None
    for klass in JavaAbstractSyntax::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::castexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::CastExpression)


def test_javaabstractsyntax::castexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::CastExpression.__init__)


def test_javaabstractsyntax::castexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::FieldAccess)


def test_javaabstractsyntax::fieldaccess_constructor_exists():
    assert callable(JavaAbstractSyntax::FieldAccess.__init__)


def test_javaabstractsyntax::fieldaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SuperMethodInvocation)


def test_javaabstractsyntax::supermethodinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax::SuperMethodInvocation.__init__)


def test_javaabstractsyntax::supermethodinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::PrefixExpression)


def test_javaabstractsyntax::prefixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax::PrefixExpression.__init__)


def test_javaabstractsyntax::prefixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax::prefixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax::PrefixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::typeliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TypeLiteral)


def test_javaabstractsyntax::typeliteral_constructor_exists():
    assert callable(JavaAbstractSyntax::TypeLiteral.__init__)


def test_javaabstractsyntax::typeliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::assignment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Assignment)


def test_javaabstractsyntax::assignment_constructor_exists():
    assert callable(JavaAbstractSyntax::Assignment.__init__)


def test_javaabstractsyntax::assignment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax::assignment_has_operator():
    assert hasattr(JavaAbstractSyntax::Assignment, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::SuperFieldAccess)


def test_javaabstractsyntax::superfieldaccess_constructor_exists():
    assert callable(JavaAbstractSyntax::SuperFieldAccess.__init__)


def test_javaabstractsyntax::superfieldaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::EnumConstantDeclaration)


def test_javaabstractsyntax::enumconstantdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::EnumConstantDeclaration.__init__)


def test_javaabstractsyntax::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AnnotationTypeMemberDeclaration)


def test_javaabstractsyntax::annotationtypememberdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::AnnotationTypeMemberDeclaration.__init__)


def test_javaabstractsyntax::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::FieldDeclaration)


def test_javaabstractsyntax::fielddeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::FieldDeclaration.__init__)


def test_javaabstractsyntax::fielddeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MethodDeclaration)


def test_javaabstractsyntax::methoddeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::MethodDeclaration.__init__)


def test_javaabstractsyntax::methoddeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_javaabstractsyntax::methoddeclaration_has_extraDimensions():
    assert hasattr(JavaAbstractSyntax::MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in JavaAbstractSyntax::MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::methoddeclaration_has_constructor():
    assert hasattr(JavaAbstractSyntax::MethodDeclaration, "constructor")
    descriptor = None
    for klass in JavaAbstractSyntax::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::methoddeclaration_has_varargs():
    assert hasattr(JavaAbstractSyntax::MethodDeclaration, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax::MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::initializer_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Initializer)


def test_javaabstractsyntax::initializer_constructor_exists():
    assert callable(JavaAbstractSyntax::Initializer.__init__)


def test_javaabstractsyntax::initializer_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AbstractTypeDeclaration)


def test_javaabstractsyntax::abstracttypedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::AbstractTypeDeclaration.__init__)


def test_javaabstractsyntax::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"

def test_javaabstractsyntax::abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(JavaAbstractSyntax::AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax::AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(JavaAbstractSyntax::AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax::AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(JavaAbstractSyntax::AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax::AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::astnode_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ASTNode)


def test_javaabstractsyntax::astnode_constructor_exists():
    assert callable(JavaAbstractSyntax::ASTNode.__init__)


def test_javaabstractsyntax::astnode_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::ImportDeclaration)


def test_javaabstractsyntax::importdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::ImportDeclaration.__init__)


def test_javaabstractsyntax::importdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_javaabstractsyntax::importdeclaration_has_onDemand():
    assert hasattr(JavaAbstractSyntax::ImportDeclaration, "onDemand")
    descriptor = None
    for klass in JavaAbstractSyntax::ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::importdeclaration_has_static():
    assert hasattr(JavaAbstractSyntax::ImportDeclaration, "static")
    descriptor = None
    for klass in JavaAbstractSyntax::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::methodref_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MethodRef)


def test_javaabstractsyntax::methodref_constructor_exists():
    assert callable(JavaAbstractSyntax::MethodRef.__init__)


def test_javaabstractsyntax::methodref_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::expression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Expression)


def test_javaabstractsyntax::expression_constructor_exists():
    assert callable(JavaAbstractSyntax::Expression.__init__)


def test_javaabstractsyntax::expression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"

def test_javaabstractsyntax::expression_has_resolveUnboxing():
    assert hasattr(JavaAbstractSyntax::Expression, "resolveUnboxing")
    descriptor = None
    for klass in JavaAbstractSyntax::Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::expression_has_resolveBoxing():
    assert hasattr(JavaAbstractSyntax::Expression, "resolveBoxing")
    descriptor = None
    for klass in JavaAbstractSyntax::Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MemberValuePair)


def test_javaabstractsyntax::membervaluepair_constructor_exists():
    assert callable(JavaAbstractSyntax::MemberValuePair.__init__)


def test_javaabstractsyntax::membervaluepair_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::statement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Statement)


def test_javaabstractsyntax::statement_constructor_exists():
    assert callable(JavaAbstractSyntax::Statement.__init__)


def test_javaabstractsyntax::statement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Statement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AnonymousClassDeclaration)


def test_javaabstractsyntax::anonymousclassdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::AnonymousClassDeclaration.__init__)


def test_javaabstractsyntax::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::textelement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TextElement)


def test_javaabstractsyntax::textelement_constructor_exists():
    assert callable(JavaAbstractSyntax::TextElement.__init__)


def test_javaabstractsyntax::textelement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_javaabstractsyntax::textelement_has_text():
    assert hasattr(JavaAbstractSyntax::TextElement, "text")
    descriptor = None
    for klass in JavaAbstractSyntax::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::tagelement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TagElement)


def test_javaabstractsyntax::tagelement_constructor_exists():
    assert callable(JavaAbstractSyntax::TagElement.__init__)


def test_javaabstractsyntax::tagelement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "nested" in params, "Missing parameter 'nested'"

def test_javaabstractsyntax::tagelement_has_tagName():
    assert hasattr(JavaAbstractSyntax::TagElement, "tagName")
    descriptor = None
    for klass in JavaAbstractSyntax::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::tagelement_has_nested():
    assert hasattr(JavaAbstractSyntax::TagElement, "nested")
    descriptor = None
    for klass in JavaAbstractSyntax::TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::memberref_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MemberRef)


def test_javaabstractsyntax::memberref_constructor_exists():
    assert callable(JavaAbstractSyntax::MemberRef.__init__)


def test_javaabstractsyntax::memberref_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::type_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Type)


def test_javaabstractsyntax::type_constructor_exists():
    assert callable(JavaAbstractSyntax::Type.__init__)


def test_javaabstractsyntax::type_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Type.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::PackageDeclaration)


def test_javaabstractsyntax::packagedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::PackageDeclaration.__init__)


def test_javaabstractsyntax::packagedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::VariableDeclaration)


def test_javaabstractsyntax::variabledeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::VariableDeclaration.__init__)


def test_javaabstractsyntax::variabledeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_javaabstractsyntax::variabledeclaration_has_extraDimensions():
    assert hasattr(JavaAbstractSyntax::VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in JavaAbstractSyntax::VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::catchclause_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::CatchClause)


def test_javaabstractsyntax::catchclause_constructor_exists():
    assert callable(JavaAbstractSyntax::CatchClause.__init__)


def test_javaabstractsyntax::catchclause_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::typeparameter_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::TypeParameter)


def test_javaabstractsyntax::typeparameter_constructor_exists():
    assert callable(JavaAbstractSyntax::TypeParameter.__init__)


def test_javaabstractsyntax::typeparameter_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::MethodRefParameter)


def test_javaabstractsyntax::methodrefparameter_constructor_exists():
    assert callable(JavaAbstractSyntax::MethodRefParameter.__init__)


def test_javaabstractsyntax::methodrefparameter_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_javaabstractsyntax::methodrefparameter_has_varargs():
    assert hasattr(JavaAbstractSyntax::MethodRefParameter, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::ast_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::AST)


def test_javaabstractsyntax::ast_constructor_exists():
    assert callable(JavaAbstractSyntax::AST.__init__)


def test_javaabstractsyntax::ast_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::AST.__init__)
    params = list(sig.parameters.keys())



def test_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(ImportDeclaration)


def test_importdeclaration_constructor_exists():
    assert callable(ImportDeclaration.__init__)


def test_importdeclaration_constructor_args():
    sig = inspect.signature(ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(PackageDeclaration)


def test_packagedeclaration_constructor_exists():
    assert callable(PackageDeclaration.__init__)


def test_packagedeclaration_constructor_args():
    sig = inspect.signature(PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::linecomment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::LineComment)


def test_javaabstractsyntax::linecomment_constructor_exists():
    assert callable(JavaAbstractSyntax::LineComment.__init__)


def test_javaabstractsyntax::linecomment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::javadoc_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Javadoc)


def test_javaabstractsyntax::javadoc_constructor_exists():
    assert callable(JavaAbstractSyntax::Javadoc.__init__)


def test_javaabstractsyntax::javadoc_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::blockcomment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::BlockComment)


def test_javaabstractsyntax::blockcomment_constructor_exists():
    assert callable(JavaAbstractSyntax::BlockComment.__init__)


def test_javaabstractsyntax::blockcomment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::compilationunit_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::CompilationUnit)


def test_javaabstractsyntax::compilationunit_constructor_exists():
    assert callable(JavaAbstractSyntax::CompilationUnit.__init__)


def test_javaabstractsyntax::compilationunit_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::comment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Comment)


def test_javaabstractsyntax::comment_constructor_exists():
    assert callable(JavaAbstractSyntax::Comment.__init__)


def test_javaabstractsyntax::comment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Comment.__init__)
    params = list(sig.parameters.keys())



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::modifier_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Modifier)


def test_javaabstractsyntax::modifier_constructor_exists():
    assert callable(JavaAbstractSyntax::Modifier.__init__)


def test_javaabstractsyntax::modifier_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "public" in params, "Missing parameter 'public'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "native" in params, "Missing parameter 'native'"
    assert "private" in params, "Missing parameter 'private'"
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"

def test_javaabstractsyntax::modifier_has_none():
    assert hasattr(JavaAbstractSyntax::Modifier, "none")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_protected():
    assert hasattr(JavaAbstractSyntax::Modifier, "protected")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_abstract():
    assert hasattr(JavaAbstractSyntax::Modifier, "abstract")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_transient():
    assert hasattr(JavaAbstractSyntax::Modifier, "transient")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_volatile():
    assert hasattr(JavaAbstractSyntax::Modifier, "volatile")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_strictfp():
    assert hasattr(JavaAbstractSyntax::Modifier, "strictfp")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_public():
    assert hasattr(JavaAbstractSyntax::Modifier, "public")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_synchronized():
    assert hasattr(JavaAbstractSyntax::Modifier, "synchronized")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_native():
    assert hasattr(JavaAbstractSyntax::Modifier, "native")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_private():
    assert hasattr(JavaAbstractSyntax::Modifier, "private")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_static():
    assert hasattr(JavaAbstractSyntax::Modifier, "static")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax::modifier_has_final():
    assert hasattr(JavaAbstractSyntax::Modifier, "final")
    descriptor = None
    for klass in JavaAbstractSyntax::Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax::annotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::Annotation)


def test_javaabstractsyntax::annotation_constructor_exists():
    assert callable(JavaAbstractSyntax::Annotation.__init__)


def test_javaabstractsyntax::annotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax::BodyDeclaration)


def test_javaabstractsyntax::bodydeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax::BodyDeclaration.__init__)


def test_javaabstractsyntax::bodydeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "REMAINDER",
        "CONDITIONAL_AND",
        "MINUS",
        "DIVIDE",
        "AND",
        "PLUS",
        "RIGHT_SHIFT_UNSIGNED",
        "EQUALS",
        "LEFT_SHIFT",
        "XOR",
        "LESS_EQUALS",
        "NOT_EQUALS",
        "CONDITIONAL_OR",
        "LESS",
        "TIMES",
        "OR",
        "GREATER",
        "GREATER_EQUALS",
        "RIGHT_SHIFT_SIGNED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

def test_prefixexpresssionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpresssionOperatorKind is not None

def test_prefixexpresssionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpresssionOperatorKind]
    expected_literals = [
        "NOT",
        "PLUS",
        "MINUS",
        "INCREMENT",
        "COMPLEMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpresssionOperatorKind"

def test_postfixexpresssionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpresssionOperatorKind is not None

def test_postfixexpresssionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpresssionOperatorKind]
    expected_literals = [
        "INCREMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpresssionOperatorKind"

def test_assignementoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignementOperatorKind is not None

def test_assignementoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignementOperatorKind]
    expected_literals = [
        "DIVIDE_ASSIGN",
        "BIT_XOR_ASSIGN",
        "MINUS_ASSIGN",
        "BIT_OR_ASSIGN",
        "TIMES_ASSIGN",
        "ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "PLUS_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "BIT_AND_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "REMAINDER_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignementOperatorKind"


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
Block_strategy = st.builds(
    Block,
)
Javadoc_strategy = st.builds(
    Javadoc,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
StructuralPackage_strategy = st.builds(
    StructuralPackage,
)
JavaAbstractSyntax::StructuralPackage_strategy = st.builds(
    JavaAbstractSyntax::StructuralPackage,
    name=
        safe_text
)
MemberValuePair_strategy = st.builds(
    MemberValuePair,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
JavaAbstractSyntax::VariableDeclarationFragment_strategy = st.builds(
    JavaAbstractSyntax::VariableDeclarationFragment,
)
JavaAbstractSyntax::SingleVariableDeclaration_strategy = st.builds(
    JavaAbstractSyntax::SingleVariableDeclaration,
    varargs=
        safe_text
)
CatchClause_strategy = st.builds(
    CatchClause,
)
Statement_strategy = st.builds(
    Statement,
)
JavaAbstractSyntax::VariableDeclarationStatement_strategy = st.builds(
    JavaAbstractSyntax::VariableDeclarationStatement,
)
JavaAbstractSyntax::SynchronizedStatement_strategy = st.builds(
    JavaAbstractSyntax::SynchronizedStatement,
)
JavaAbstractSyntax::EmptyStatement_strategy = st.builds(
    JavaAbstractSyntax::EmptyStatement,
)
JavaAbstractSyntax::DoStatement_strategy = st.builds(
    JavaAbstractSyntax::DoStatement,
)
JavaAbstractSyntax::SwitchStatement_strategy = st.builds(
    JavaAbstractSyntax::SwitchStatement,
)
JavaAbstractSyntax::SwitchCase_strategy = st.builds(
    JavaAbstractSyntax::SwitchCase,
    default=
        safe_text
)
JavaAbstractSyntax::LabeledStatement_strategy = st.builds(
    JavaAbstractSyntax::LabeledStatement,
)
JavaAbstractSyntax::SuperConstructorInvocation_strategy = st.builds(
    JavaAbstractSyntax::SuperConstructorInvocation,
)
JavaAbstractSyntax::WhileStatement_strategy = st.builds(
    JavaAbstractSyntax::WhileStatement,
)
JavaAbstractSyntax::ForStatement_strategy = st.builds(
    JavaAbstractSyntax::ForStatement,
)
JavaAbstractSyntax::EnhancedForStatement_strategy = st.builds(
    JavaAbstractSyntax::EnhancedForStatement,
)
JavaAbstractSyntax::TypeDeclarationStatement_strategy = st.builds(
    JavaAbstractSyntax::TypeDeclarationStatement,
)
JavaAbstractSyntax::ReturnStatement_strategy = st.builds(
    JavaAbstractSyntax::ReturnStatement,
)
JavaAbstractSyntax::ThrowStatement_strategy = st.builds(
    JavaAbstractSyntax::ThrowStatement,
)
JavaAbstractSyntax::ExpressionStatement_strategy = st.builds(
    JavaAbstractSyntax::ExpressionStatement,
)
JavaAbstractSyntax::TryStatement_strategy = st.builds(
    JavaAbstractSyntax::TryStatement,
)
JavaAbstractSyntax::IfStatement_strategy = st.builds(
    JavaAbstractSyntax::IfStatement,
)
JavaAbstractSyntax::AssertStatement_strategy = st.builds(
    JavaAbstractSyntax::AssertStatement,
)
JavaAbstractSyntax::ContinueStatement_strategy = st.builds(
    JavaAbstractSyntax::ContinueStatement,
)
JavaAbstractSyntax::ConstructorInvocation_strategy = st.builds(
    JavaAbstractSyntax::ConstructorInvocation,
)
JavaAbstractSyntax::BreakStatement_strategy = st.builds(
    JavaAbstractSyntax::BreakStatement,
)
JavaAbstractSyntax::Block_strategy = st.builds(
    JavaAbstractSyntax::Block,
)
TagElement_strategy = st.builds(
    TagElement,
)
EnumConstantDeclaration_strategy = st.builds(
    EnumConstantDeclaration,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
AnonymousClassDeclaration_strategy = st.builds(
    AnonymousClassDeclaration,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
Annotation_strategy = st.builds(
    Annotation,
)
JavaAbstractSyntax::SingleMemberAnnotation_strategy = st.builds(
    JavaAbstractSyntax::SingleMemberAnnotation,
)
JavaAbstractSyntax::NormalAnnotation_strategy = st.builds(
    JavaAbstractSyntax::NormalAnnotation,
)
JavaAbstractSyntax::MarkerAnnotation_strategy = st.builds(
    JavaAbstractSyntax::MarkerAnnotation,
)
SimpleName_strategy = st.builds(
    SimpleName,
)
Name_strategy = st.builds(
    Name,
)
JavaAbstractSyntax::SimpleName_strategy = st.builds(
    JavaAbstractSyntax::SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
JavaAbstractSyntax::QualifiedName_strategy = st.builds(
    JavaAbstractSyntax::QualifiedName,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JavaAbstractSyntax::TypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax::TypeDeclaration,
    interface=
        safe_text
)
JavaAbstractSyntax::EnumDeclaration_strategy = st.builds(
    JavaAbstractSyntax::EnumDeclaration,
)
JavaAbstractSyntax::AnnotationTypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax::AnnotationTypeDeclaration,
)
JavaAbstractSyntax::ExtendedModifier_strategy = st.builds(
    JavaAbstractSyntax::ExtendedModifier,
)
Type_strategy = st.builds(
    Type,
)
JavaAbstractSyntax::ArrayType_strategy = st.builds(
    JavaAbstractSyntax::ArrayType,
    dimensions=
        safe_text
)
JavaAbstractSyntax::WildcardType_strategy = st.builds(
    JavaAbstractSyntax::WildcardType,
    upperBound=
        safe_text
)
JavaAbstractSyntax::SimpleType_strategy = st.builds(
    JavaAbstractSyntax::SimpleType,
)
JavaAbstractSyntax::PrimitiveType_strategy = st.builds(
    JavaAbstractSyntax::PrimitiveType,
    code=
        safe_text
)
JavaAbstractSyntax::ParameterizedType_strategy = st.builds(
    JavaAbstractSyntax::ParameterizedType,
)
JavaAbstractSyntax::QualifiedType_strategy = st.builds(
    JavaAbstractSyntax::QualifiedType,
)
MethodRefParameter_strategy = st.builds(
    MethodRefParameter,
)
Expression_strategy = st.builds(
    Expression,
)
JavaAbstractSyntax::ArrayCreation_strategy = st.builds(
    JavaAbstractSyntax::ArrayCreation,
)
JavaAbstractSyntax::InfixExpression_strategy = st.builds(
    JavaAbstractSyntax::InfixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax::MethodInvocation_strategy = st.builds(
    JavaAbstractSyntax::MethodInvocation,
)
JavaAbstractSyntax::Name_strategy = st.builds(
    JavaAbstractSyntax::Name,
    fullyQualifiedName=
        safe_text
)
JavaAbstractSyntax::ClassInstanceCreation_strategy = st.builds(
    JavaAbstractSyntax::ClassInstanceCreation,
)
JavaAbstractSyntax::CharacterLiteral_strategy = st.builds(
    JavaAbstractSyntax::CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
JavaAbstractSyntax::ArrayInitializer_strategy = st.builds(
    JavaAbstractSyntax::ArrayInitializer,
)
JavaAbstractSyntax::ParenthesizedExpression_strategy = st.builds(
    JavaAbstractSyntax::ParenthesizedExpression,
)
JavaAbstractSyntax::NumberLiteral_strategy = st.builds(
    JavaAbstractSyntax::NumberLiteral,
    token=
        safe_text
)
JavaAbstractSyntax::VariableDeclarationExpression_strategy = st.builds(
    JavaAbstractSyntax::VariableDeclarationExpression,
)
JavaAbstractSyntax::NullLiteral_strategy = st.builds(
    JavaAbstractSyntax::NullLiteral,
)
JavaAbstractSyntax::ThisExpression_strategy = st.builds(
    JavaAbstractSyntax::ThisExpression,
)
JavaAbstractSyntax::PostfixExpression_strategy = st.builds(
    JavaAbstractSyntax::PostfixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax::BooleanLiteral_strategy = st.builds(
    JavaAbstractSyntax::BooleanLiteral,
    booleanValue=
        safe_text
)
JavaAbstractSyntax::ConditionalExpression_strategy = st.builds(
    JavaAbstractSyntax::ConditionalExpression,
)
JavaAbstractSyntax::ArrayAccess_strategy = st.builds(
    JavaAbstractSyntax::ArrayAccess,
)
JavaAbstractSyntax::InstanceofExpression_strategy = st.builds(
    JavaAbstractSyntax::InstanceofExpression,
)
JavaAbstractSyntax::StringLiteral_strategy = st.builds(
    JavaAbstractSyntax::StringLiteral,
    literalValue=
        safe_text,
    escapedValue=
        safe_text
)
JavaAbstractSyntax::CastExpression_strategy = st.builds(
    JavaAbstractSyntax::CastExpression,
)
JavaAbstractSyntax::FieldAccess_strategy = st.builds(
    JavaAbstractSyntax::FieldAccess,
)
JavaAbstractSyntax::SuperMethodInvocation_strategy = st.builds(
    JavaAbstractSyntax::SuperMethodInvocation,
)
JavaAbstractSyntax::PrefixExpression_strategy = st.builds(
    JavaAbstractSyntax::PrefixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax::TypeLiteral_strategy = st.builds(
    JavaAbstractSyntax::TypeLiteral,
)
JavaAbstractSyntax::Assignment_strategy = st.builds(
    JavaAbstractSyntax::Assignment,
    operator=
        safe_text
)
JavaAbstractSyntax::SuperFieldAccess_strategy = st.builds(
    JavaAbstractSyntax::SuperFieldAccess,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JavaAbstractSyntax::EnumConstantDeclaration_strategy = st.builds(
    JavaAbstractSyntax::EnumConstantDeclaration,
)
JavaAbstractSyntax::AnnotationTypeMemberDeclaration_strategy = st.builds(
    JavaAbstractSyntax::AnnotationTypeMemberDeclaration,
)
JavaAbstractSyntax::FieldDeclaration_strategy = st.builds(
    JavaAbstractSyntax::FieldDeclaration,
)
JavaAbstractSyntax::MethodDeclaration_strategy = st.builds(
    JavaAbstractSyntax::MethodDeclaration,
    extraDimensions=
        safe_text,
    constructor=
        safe_text,
    varargs=
        safe_text
)
JavaAbstractSyntax::Initializer_strategy = st.builds(
    JavaAbstractSyntax::Initializer,
)
JavaAbstractSyntax::AbstractTypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax::AbstractTypeDeclaration,
    localTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text
)
JavaAbstractSyntax::ASTNode_strategy = st.builds(
    JavaAbstractSyntax::ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JavaAbstractSyntax::ImportDeclaration_strategy = st.builds(
    JavaAbstractSyntax::ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
JavaAbstractSyntax::MethodRef_strategy = st.builds(
    JavaAbstractSyntax::MethodRef,
)
JavaAbstractSyntax::Expression_strategy = st.builds(
    JavaAbstractSyntax::Expression,
    resolveUnboxing=
        safe_text,
    resolveBoxing=
        safe_text
)
JavaAbstractSyntax::MemberValuePair_strategy = st.builds(
    JavaAbstractSyntax::MemberValuePair,
)
JavaAbstractSyntax::Statement_strategy = st.builds(
    JavaAbstractSyntax::Statement,
)
JavaAbstractSyntax::AnonymousClassDeclaration_strategy = st.builds(
    JavaAbstractSyntax::AnonymousClassDeclaration,
)
JavaAbstractSyntax::TextElement_strategy = st.builds(
    JavaAbstractSyntax::TextElement,
    text=
        safe_text
)
JavaAbstractSyntax::TagElement_strategy = st.builds(
    JavaAbstractSyntax::TagElement,
    tagName=
        safe_text,
    nested=
        safe_text
)
JavaAbstractSyntax::MemberRef_strategy = st.builds(
    JavaAbstractSyntax::MemberRef,
)
JavaAbstractSyntax::Type_strategy = st.builds(
    JavaAbstractSyntax::Type,
)
JavaAbstractSyntax::PackageDeclaration_strategy = st.builds(
    JavaAbstractSyntax::PackageDeclaration,
)
JavaAbstractSyntax::VariableDeclaration_strategy = st.builds(
    JavaAbstractSyntax::VariableDeclaration,
    extraDimensions=
        safe_text
)
JavaAbstractSyntax::CatchClause_strategy = st.builds(
    JavaAbstractSyntax::CatchClause,
)
JavaAbstractSyntax::TypeParameter_strategy = st.builds(
    JavaAbstractSyntax::TypeParameter,
)
JavaAbstractSyntax::MethodRefParameter_strategy = st.builds(
    JavaAbstractSyntax::MethodRefParameter,
    varargs=
        safe_text
)
JavaAbstractSyntax::AST_strategy = st.builds(
    JavaAbstractSyntax::AST,
)
ImportDeclaration_strategy = st.builds(
    ImportDeclaration,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
Comment_strategy = st.builds(
    Comment,
)
JavaAbstractSyntax::LineComment_strategy = st.builds(
    JavaAbstractSyntax::LineComment,
)
JavaAbstractSyntax::Javadoc_strategy = st.builds(
    JavaAbstractSyntax::Javadoc,
)
JavaAbstractSyntax::BlockComment_strategy = st.builds(
    JavaAbstractSyntax::BlockComment,
)
JavaAbstractSyntax::CompilationUnit_strategy = st.builds(
    JavaAbstractSyntax::CompilationUnit,
)
JavaAbstractSyntax::Comment_strategy = st.builds(
    JavaAbstractSyntax::Comment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
JavaAbstractSyntax::Modifier_strategy = st.builds(
    JavaAbstractSyntax::Modifier,
    none=
        safe_text,
    protected=
        safe_text,
    abstract=
        safe_text,
    transient=
        safe_text,
    volatile=
        safe_text,
    strictfp=
        safe_text,
    public=
        safe_text,
    synchronized=
        safe_text,
    native=
        safe_text,
    private=
        safe_text,
    static=
        safe_text,
    final=
        safe_text
)
JavaAbstractSyntax::Annotation_strategy = st.builds(
    JavaAbstractSyntax::Annotation,
)
JavaAbstractSyntax::BodyDeclaration_strategy = st.builds(
    JavaAbstractSyntax::BodyDeclaration,
)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=Javadoc_strategy)
@settings(max_examples=50)
def test_javadoc_instantiation(instance):
    assert isinstance(instance, Javadoc)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=StructuralPackage_strategy)
@settings(max_examples=50)
def test_structuralpackage_instantiation(instance):
    assert isinstance(instance, StructuralPackage)

@given(instance=JavaAbstractSyntax::StructuralPackage_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::structuralpackage_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::StructuralPackage)

@given(instance=JavaAbstractSyntax::StructuralPackage_strategy)
def test_javaabstractsyntax::structuralpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JavaAbstractSyntax::StructuralPackage_strategy)
def test_javaabstractsyntax::structuralpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MemberValuePair_strategy)
@settings(max_examples=50)
def test_membervaluepair_instantiation(instance):
    assert isinstance(instance, MemberValuePair)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=JavaAbstractSyntax::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::VariableDeclarationFragment)

@given(instance=JavaAbstractSyntax::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SingleVariableDeclaration)

@given(instance=JavaAbstractSyntax::SingleVariableDeclaration_strategy)
def test_javaabstractsyntax::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JavaAbstractSyntax::SingleVariableDeclaration_strategy)
def test_javaabstractsyntax::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=CatchClause_strategy)
@settings(max_examples=50)
def test_catchclause_instantiation(instance):
    assert isinstance(instance, CatchClause)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JavaAbstractSyntax::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::VariableDeclarationStatement)

@given(instance=JavaAbstractSyntax::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SynchronizedStatement)

@given(instance=JavaAbstractSyntax::EmptyStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::emptystatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::EmptyStatement)

@given(instance=JavaAbstractSyntax::DoStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::dostatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::DoStatement)

@given(instance=JavaAbstractSyntax::SwitchStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::switchstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SwitchStatement)

@given(instance=JavaAbstractSyntax::SwitchCase_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::switchcase_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SwitchCase)

@given(instance=JavaAbstractSyntax::SwitchCase_strategy)
def test_javaabstractsyntax::switchcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=JavaAbstractSyntax::SwitchCase_strategy)
def test_javaabstractsyntax::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JavaAbstractSyntax::LabeledStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::labeledstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::LabeledStatement)

@given(instance=JavaAbstractSyntax::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SuperConstructorInvocation)

@given(instance=JavaAbstractSyntax::WhileStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::whilestatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::WhileStatement)

@given(instance=JavaAbstractSyntax::ForStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::forstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ForStatement)

@given(instance=JavaAbstractSyntax::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::EnhancedForStatement)

@given(instance=JavaAbstractSyntax::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TypeDeclarationStatement)

@given(instance=JavaAbstractSyntax::ReturnStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::returnstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ReturnStatement)

@given(instance=JavaAbstractSyntax::ThrowStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::throwstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ThrowStatement)

@given(instance=JavaAbstractSyntax::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::expressionstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ExpressionStatement)

@given(instance=JavaAbstractSyntax::TryStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::trystatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TryStatement)

@given(instance=JavaAbstractSyntax::IfStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::ifstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::IfStatement)

@given(instance=JavaAbstractSyntax::AssertStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::assertstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AssertStatement)

@given(instance=JavaAbstractSyntax::ContinueStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::continuestatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ContinueStatement)

@given(instance=JavaAbstractSyntax::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::constructorinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ConstructorInvocation)

@given(instance=JavaAbstractSyntax::BreakStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::breakstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::BreakStatement)

@given(instance=JavaAbstractSyntax::Block_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::block_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Block)

@given(instance=TagElement_strategy)
@settings(max_examples=50)
def test_tagelement_instantiation(instance):
    assert isinstance(instance, TagElement)

@given(instance=EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, EnumConstantDeclaration)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, AnonymousClassDeclaration)

@given(instance=TypeParameter_strategy)
@settings(max_examples=50)
def test_typeparameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=JavaAbstractSyntax::SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::singlememberannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SingleMemberAnnotation)

@given(instance=JavaAbstractSyntax::NormalAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::normalannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::NormalAnnotation)

@given(instance=JavaAbstractSyntax::MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::markerannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MarkerAnnotation)

@given(instance=SimpleName_strategy)
@settings(max_examples=50)
def test_simplename_instantiation(instance):
    assert isinstance(instance, SimpleName)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=JavaAbstractSyntax::SimpleName_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::simplename_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SimpleName)

@given(instance=JavaAbstractSyntax::SimpleName_strategy)
def test_javaabstractsyntax::simplename_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=JavaAbstractSyntax::SimpleName_strategy)
def test_javaabstractsyntax::simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=JavaAbstractSyntax::SimpleName_strategy)
def test_javaabstractsyntax::simplename_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=JavaAbstractSyntax::SimpleName_strategy)
def test_javaabstractsyntax::simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=JavaAbstractSyntax::QualifiedName_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::qualifiedname_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::QualifiedName)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JavaAbstractSyntax::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::typedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TypeDeclaration)

@given(instance=JavaAbstractSyntax::TypeDeclaration_strategy)
def test_javaabstractsyntax::typedeclaration_interface_type(instance):
    assert isinstance(instance.interface, str)


@given(instance=JavaAbstractSyntax::TypeDeclaration_strategy)
def test_javaabstractsyntax::typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=JavaAbstractSyntax::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::enumdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::EnumDeclaration)

@given(instance=JavaAbstractSyntax::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AnnotationTypeDeclaration)

@given(instance=JavaAbstractSyntax::ExtendedModifier_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::extendedmodifier_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ExtendedModifier)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JavaAbstractSyntax::ArrayType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::arraytype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ArrayType)

@given(instance=JavaAbstractSyntax::ArrayType_strategy)
def test_javaabstractsyntax::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=JavaAbstractSyntax::ArrayType_strategy)
def test_javaabstractsyntax::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=JavaAbstractSyntax::WildcardType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::wildcardtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::WildcardType)

@given(instance=JavaAbstractSyntax::WildcardType_strategy)
def test_javaabstractsyntax::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=JavaAbstractSyntax::WildcardType_strategy)
def test_javaabstractsyntax::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=JavaAbstractSyntax::SimpleType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::simpletype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SimpleType)

@given(instance=JavaAbstractSyntax::PrimitiveType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::primitivetype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::PrimitiveType)

@given(instance=JavaAbstractSyntax::PrimitiveType_strategy)
def test_javaabstractsyntax::primitivetype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=JavaAbstractSyntax::PrimitiveType_strategy)
def test_javaabstractsyntax::primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=JavaAbstractSyntax::ParameterizedType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::parameterizedtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ParameterizedType)

@given(instance=JavaAbstractSyntax::QualifiedType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::qualifiedtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::QualifiedType)

@given(instance=MethodRefParameter_strategy)
@settings(max_examples=50)
def test_methodrefparameter_instantiation(instance):
    assert isinstance(instance, MethodRefParameter)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JavaAbstractSyntax::ArrayCreation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::arraycreation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ArrayCreation)

@given(instance=JavaAbstractSyntax::InfixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::infixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::InfixExpression)

@given(instance=JavaAbstractSyntax::InfixExpression_strategy)
def test_javaabstractsyntax::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaAbstractSyntax::InfixExpression_strategy)
def test_javaabstractsyntax::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax::MethodInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::methodinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MethodInvocation)

@given(instance=JavaAbstractSyntax::Name_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::name_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Name)

@given(instance=JavaAbstractSyntax::Name_strategy)
def test_javaabstractsyntax::name_fullyQualifiedName_type(instance):
    assert isinstance(instance.fullyQualifiedName, str)


@given(instance=JavaAbstractSyntax::Name_strategy)
def test_javaabstractsyntax::name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=JavaAbstractSyntax::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::classinstancecreation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ClassInstanceCreation)

@given(instance=JavaAbstractSyntax::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::characterliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::CharacterLiteral)

@given(instance=JavaAbstractSyntax::CharacterLiteral_strategy)
def test_javaabstractsyntax::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=JavaAbstractSyntax::CharacterLiteral_strategy)
def test_javaabstractsyntax::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=JavaAbstractSyntax::CharacterLiteral_strategy)
def test_javaabstractsyntax::characterliteral_charValue_type(instance):
    assert isinstance(instance.charValue, str)


@given(instance=JavaAbstractSyntax::CharacterLiteral_strategy)
def test_javaabstractsyntax::characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=JavaAbstractSyntax::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::arrayinitializer_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ArrayInitializer)

@given(instance=JavaAbstractSyntax::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ParenthesizedExpression)

@given(instance=JavaAbstractSyntax::NumberLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::numberliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::NumberLiteral)

@given(instance=JavaAbstractSyntax::NumberLiteral_strategy)
def test_javaabstractsyntax::numberliteral_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=JavaAbstractSyntax::NumberLiteral_strategy)
def test_javaabstractsyntax::numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=JavaAbstractSyntax::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::VariableDeclarationExpression)

@given(instance=JavaAbstractSyntax::NullLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::nullliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::NullLiteral)

@given(instance=JavaAbstractSyntax::ThisExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::thisexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ThisExpression)

@given(instance=JavaAbstractSyntax::PostfixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::postfixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::PostfixExpression)

@given(instance=JavaAbstractSyntax::PostfixExpression_strategy)
def test_javaabstractsyntax::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaAbstractSyntax::PostfixExpression_strategy)
def test_javaabstractsyntax::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::booleanliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::BooleanLiteral)

@given(instance=JavaAbstractSyntax::BooleanLiteral_strategy)
def test_javaabstractsyntax::booleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, str)


@given(instance=JavaAbstractSyntax::BooleanLiteral_strategy)
def test_javaabstractsyntax::booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=JavaAbstractSyntax::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::conditionalexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ConditionalExpression)

@given(instance=JavaAbstractSyntax::ArrayAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::arrayaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ArrayAccess)

@given(instance=JavaAbstractSyntax::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::instanceofexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::InstanceofExpression)

@given(instance=JavaAbstractSyntax::StringLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::stringliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::StringLiteral)

@given(instance=JavaAbstractSyntax::StringLiteral_strategy)
def test_javaabstractsyntax::stringliteral_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=JavaAbstractSyntax::StringLiteral_strategy)
def test_javaabstractsyntax::stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=JavaAbstractSyntax::StringLiteral_strategy)
def test_javaabstractsyntax::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=JavaAbstractSyntax::StringLiteral_strategy)
def test_javaabstractsyntax::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=JavaAbstractSyntax::CastExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::castexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::CastExpression)

@given(instance=JavaAbstractSyntax::FieldAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::fieldaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::FieldAccess)

@given(instance=JavaAbstractSyntax::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SuperMethodInvocation)

@given(instance=JavaAbstractSyntax::PrefixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::prefixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::PrefixExpression)

@given(instance=JavaAbstractSyntax::PrefixExpression_strategy)
def test_javaabstractsyntax::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaAbstractSyntax::PrefixExpression_strategy)
def test_javaabstractsyntax::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax::TypeLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::typeliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TypeLiteral)

@given(instance=JavaAbstractSyntax::Assignment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::assignment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Assignment)

@given(instance=JavaAbstractSyntax::Assignment_strategy)
def test_javaabstractsyntax::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaAbstractSyntax::Assignment_strategy)
def test_javaabstractsyntax::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::superfieldaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::SuperFieldAccess)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JavaAbstractSyntax::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::EnumConstantDeclaration)

@given(instance=JavaAbstractSyntax::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AnnotationTypeMemberDeclaration)

@given(instance=JavaAbstractSyntax::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::fielddeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::FieldDeclaration)

@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::methoddeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MethodDeclaration)

@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, str)


@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JavaAbstractSyntax::MethodDeclaration_strategy)
def test_javaabstractsyntax::methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JavaAbstractSyntax::Initializer_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::initializer_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Initializer)

@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AbstractTypeDeclaration)

@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_localTypeDeclaration_type(instance):
    assert isinstance(instance.localTypeDeclaration, str)


@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original

@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_memberTypeDeclaration_type(instance):
    assert isinstance(instance.memberTypeDeclaration, str)


@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original

@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_packageMemberTypeDeclaration_type(instance):
    assert isinstance(instance.packageMemberTypeDeclaration, str)


@given(instance=JavaAbstractSyntax::AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax::abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original

@given(instance=JavaAbstractSyntax::ASTNode_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::astnode_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ASTNode)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JavaAbstractSyntax::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::importdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::ImportDeclaration)

@given(instance=JavaAbstractSyntax::ImportDeclaration_strategy)
def test_javaabstractsyntax::importdeclaration_onDemand_type(instance):
    assert isinstance(instance.onDemand, str)


@given(instance=JavaAbstractSyntax::ImportDeclaration_strategy)
def test_javaabstractsyntax::importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original

@given(instance=JavaAbstractSyntax::ImportDeclaration_strategy)
def test_javaabstractsyntax::importdeclaration_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=JavaAbstractSyntax::ImportDeclaration_strategy)
def test_javaabstractsyntax::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JavaAbstractSyntax::MethodRef_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::methodref_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MethodRef)

@given(instance=JavaAbstractSyntax::Expression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::expression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Expression)

@given(instance=JavaAbstractSyntax::Expression_strategy)
def test_javaabstractsyntax::expression_resolveUnboxing_type(instance):
    assert isinstance(instance.resolveUnboxing, str)


@given(instance=JavaAbstractSyntax::Expression_strategy)
def test_javaabstractsyntax::expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original

@given(instance=JavaAbstractSyntax::Expression_strategy)
def test_javaabstractsyntax::expression_resolveBoxing_type(instance):
    assert isinstance(instance.resolveBoxing, str)


@given(instance=JavaAbstractSyntax::Expression_strategy)
def test_javaabstractsyntax::expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original

@given(instance=JavaAbstractSyntax::MemberValuePair_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::membervaluepair_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MemberValuePair)

@given(instance=JavaAbstractSyntax::Statement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::statement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Statement)

@given(instance=JavaAbstractSyntax::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AnonymousClassDeclaration)

@given(instance=JavaAbstractSyntax::TextElement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::textelement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TextElement)

@given(instance=JavaAbstractSyntax::TextElement_strategy)
def test_javaabstractsyntax::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=JavaAbstractSyntax::TextElement_strategy)
def test_javaabstractsyntax::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=JavaAbstractSyntax::TagElement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::tagelement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TagElement)

@given(instance=JavaAbstractSyntax::TagElement_strategy)
def test_javaabstractsyntax::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=JavaAbstractSyntax::TagElement_strategy)
def test_javaabstractsyntax::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=JavaAbstractSyntax::TagElement_strategy)
def test_javaabstractsyntax::tagelement_nested_type(instance):
    assert isinstance(instance.nested, str)


@given(instance=JavaAbstractSyntax::TagElement_strategy)
def test_javaabstractsyntax::tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=JavaAbstractSyntax::MemberRef_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::memberref_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MemberRef)

@given(instance=JavaAbstractSyntax::Type_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::type_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Type)

@given(instance=JavaAbstractSyntax::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::packagedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::PackageDeclaration)

@given(instance=JavaAbstractSyntax::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::variabledeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::VariableDeclaration)

@given(instance=JavaAbstractSyntax::VariableDeclaration_strategy)
def test_javaabstractsyntax::variabledeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=JavaAbstractSyntax::VariableDeclaration_strategy)
def test_javaabstractsyntax::variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JavaAbstractSyntax::CatchClause_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::catchclause_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::CatchClause)

@given(instance=JavaAbstractSyntax::TypeParameter_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::typeparameter_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::TypeParameter)

@given(instance=JavaAbstractSyntax::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::methodrefparameter_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::MethodRefParameter)

@given(instance=JavaAbstractSyntax::MethodRefParameter_strategy)
def test_javaabstractsyntax::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JavaAbstractSyntax::MethodRefParameter_strategy)
def test_javaabstractsyntax::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JavaAbstractSyntax::AST_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::ast_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::AST)

@given(instance=ImportDeclaration_strategy)
@settings(max_examples=50)
def test_importdeclaration_instantiation(instance):
    assert isinstance(instance, ImportDeclaration)

@given(instance=PackageDeclaration_strategy)
@settings(max_examples=50)
def test_packagedeclaration_instantiation(instance):
    assert isinstance(instance, PackageDeclaration)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=JavaAbstractSyntax::LineComment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::linecomment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::LineComment)

@given(instance=JavaAbstractSyntax::Javadoc_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::javadoc_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Javadoc)

@given(instance=JavaAbstractSyntax::BlockComment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::blockcomment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::BlockComment)

@given(instance=JavaAbstractSyntax::CompilationUnit_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::compilationunit_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::CompilationUnit)

@given(instance=JavaAbstractSyntax::Comment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::comment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Comment)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=JavaAbstractSyntax::Modifier_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::modifier_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Modifier)

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_none_type(instance):
    assert isinstance(instance.none, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_transient_type(instance):
    assert isinstance(instance.transient, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_public_type(instance):
    assert isinstance(instance.public, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_native_type(instance):
    assert isinstance(instance.native, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_private_type(instance):
    assert isinstance(instance.private, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=JavaAbstractSyntax::Modifier_strategy)
def test_javaabstractsyntax::modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=JavaAbstractSyntax::Annotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::annotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::Annotation)

@given(instance=JavaAbstractSyntax::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax::bodydeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax::BodyDeclaration)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    term,
    delphi::factor,
    simpleExpression,
    delphi::term,
    expression,
    delphi::simpleExpression,
    strucType,
    delphi::setType,
    delphi::fileType,
    delphi::recType,
    delphi::arrayType,
    ordinalType,
    delphi::enumeratedType,
    delphi::subrangeType,
    delphi::ordIdent,
    simpleType,
    delphi::ordinalType,
    delphi::realType,
    type,
    delphi::procedureType,
    delphi::pointerType,
    delphi::simpleType,
    delphi::strucType,
    delphi::stringType,
    delphi::variantType,
    delphi::classRefType,
    interfaceDecl,
    delphi::exportedHeading,
    declSection,
    delphi::constSection,
    delphi::varSection,
    delphi::typeSection,
    delphi::labelDeclSection,
    file,
    delphi::library,
    delphi::packageDecl,
    delphi::unit,
    delphi::program,
    CSTrace,
    delphi::implementationSection,
    delphi::directive,
    delphi::exportsItem,
    delphi::ident,
    delphi::initSection,
    delphi::enumeratedTypeElement,
    delphi::varDecl,
    delphi::exportsStmt,
    delphi::type,
    delphi::programBlock,
    delphi::containsClause,
    delphi::mulOp,
    delphi::block,
    delphi::recVariant,
    delphi::variantSection,
    delphi::typeDecl,
    delphi::usesClause,
    delphi::restrictedType,
    delphi::fieldList,
    delphi::typedConstant,
    delphi::declSection,
    delphi::recordConstant,
    delphi::requiresClause,
    delphi::constExpr,
    delphi::arrayConstant,
    delphi::interfaceDecl,
    delphi::constantDecl,
    delphi::recordFieldConstant,
    delphi::fieldDecl,
    delphi::interfaceSection,
    delphi::exprList,
    delphi::relOp,
    delphi::expression,
    delphi::file,
    delphi::designator,
    delphi::addOp,
    delphi::mainRule,
    delphi::Visitable,
    delphi::CSTrace,
    constExpr,
    delphi::MultipleConstExp,
    delphi::RecordConstExp,
    delphi::ConstExp,
    ident,
    delphi::ReservedId,
    delphi::MineID,
    delphi::MultipleId,
    parameter,
    delphi::parameterSimple,
    delphi::parameterList,
    simpleStatement,
    delphi::inheritedStamnt,
    delphi::callStmnt,
    delphi::gotoStmnt,
    delphi::assignmentStmnt,
    addOp,
    delphi::adOp,
    factor,
    delphi::simpleFactor,
    delphi::multExp,
    delphi::addExp,
    delphi::relExp,
    delphi::recordConstExpr,
    pointerType,
    delphi::typeId,
    delphi::unitId,
    classHeritage,
    objFieldList,
    delphi::identList,
    delphi::propertySpecifiers,
    delphi::propertyInterface,
    delphi::interfaceHeritage,
    delphi::propertyParameterList,
    delphi::classHeritage,
    delphi::propertyList,
    delphi::classProperty,
    delphi::classMethod,
    delphi::classField,
    delphi::classPropertyList,
    delphi::classMethodList,
    delphi::classFieldList,
    delphi::methodHeading,
    delphi::methodList,
    delphi::objFieldList,
    delphi::objHeritage,
    restrictedType,
    delphi::classType,
    delphi::interfaceType,
    delphi::objectType,
    delphi::parameter,
    delphi::formalParm,
    delphi::formalParameters,
    methodHeading,
    delphi::constructorHeading,
    delphi::destructorHeading,
    delphi::procedureHeading,
    delphi::functionHeading,
    procedureDeclSection,
    delphi::functionDecl,
    delphi::procedureDecl,
    delphi::procedureDeclSection,
    delphi::exceptionBlock,
    delphi::qualId,
    loopStmt,
    delphi::forStmt,
    delphi::whileStmt,
    delphi::repeatStmt,
    delphi::stmtList,
    delphi::caseLabel,
    delphi::caseSelector,
    conditionalStmt,
    delphi::caseStmt,
    delphi::ifStmt,
    structStmt,
    delphi::loopStmt,
    delphi::conditionalStmt,
    delphi::tryStmt,
    delphi::withStmt,
    delphi::raiseStmt,
    delphi::compoundStmt,
    delphi::assemblerStmt,
    unlabelledStatement,
    delphi::structStmt,
    delphi::simpleStatement,
    delphi::unlabelledStatement,
    delphi::statement,
    delphi::setConstructor,
    delphi::setElement,
    delphi::reservedWord,
    delphi::designatorPart,
    delphi::designatorSubPart,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_term_is_not_abstract():
    assert not inspect.isabstract(term)


def test_term_constructor_exists():
    assert callable(term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(term.__init__)
    params = list(sig.parameters.keys())



def test_delphi::factor_is_not_abstract():
    assert not inspect.isabstract(delphi::factor)


def test_delphi::factor_constructor_exists():
    assert callable(delphi::factor.__init__)


def test_delphi::factor_constructor_args():
    sig = inspect.signature(delphi::factor.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "number" in params, "Missing parameter 'number'"

def test_delphi::factor_has_string():
    assert hasattr(delphi::factor, "string")
    descriptor = None
    for klass in delphi::factor.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_delphi::factor_has_number():
    assert hasattr(delphi::factor, "number")
    descriptor = None
    for klass in delphi::factor.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(simpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(simpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(simpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_delphi::term_is_not_abstract():
    assert not inspect.isabstract(delphi::term)


def test_delphi::term_constructor_exists():
    assert callable(delphi::term.__init__)


def test_delphi::term_constructor_args():
    sig = inspect.signature(delphi::term.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(expression)


def test_expression_constructor_exists():
    assert callable(expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(expression.__init__)
    params = list(sig.parameters.keys())



def test_delphi::simpleexpression_is_not_abstract():
    assert not inspect.isabstract(delphi::simpleExpression)


def test_delphi::simpleexpression_constructor_exists():
    assert callable(delphi::simpleExpression.__init__)


def test_delphi::simpleexpression_constructor_args():
    sig = inspect.signature(delphi::simpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_structype_is_not_abstract():
    assert not inspect.isabstract(strucType)


def test_structype_constructor_exists():
    assert callable(strucType.__init__)


def test_structype_constructor_args():
    sig = inspect.signature(strucType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::settype_is_not_abstract():
    assert not inspect.isabstract(delphi::setType)


def test_delphi::settype_constructor_exists():
    assert callable(delphi::setType.__init__)


def test_delphi::settype_constructor_args():
    sig = inspect.signature(delphi::setType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::filetype_is_not_abstract():
    assert not inspect.isabstract(delphi::fileType)


def test_delphi::filetype_constructor_exists():
    assert callable(delphi::fileType.__init__)


def test_delphi::filetype_constructor_args():
    sig = inspect.signature(delphi::fileType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::rectype_is_not_abstract():
    assert not inspect.isabstract(delphi::recType)


def test_delphi::rectype_constructor_exists():
    assert callable(delphi::recType.__init__)


def test_delphi::rectype_constructor_args():
    sig = inspect.signature(delphi::recType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::arraytype_is_not_abstract():
    assert not inspect.isabstract(delphi::arrayType)


def test_delphi::arraytype_constructor_exists():
    assert callable(delphi::arrayType.__init__)


def test_delphi::arraytype_constructor_args():
    sig = inspect.signature(delphi::arrayType.__init__)
    params = list(sig.parameters.keys())



def test_ordinaltype_is_not_abstract():
    assert not inspect.isabstract(ordinalType)


def test_ordinaltype_constructor_exists():
    assert callable(ordinalType.__init__)


def test_ordinaltype_constructor_args():
    sig = inspect.signature(ordinalType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::enumeratedtype_is_not_abstract():
    assert not inspect.isabstract(delphi::enumeratedType)


def test_delphi::enumeratedtype_constructor_exists():
    assert callable(delphi::enumeratedType.__init__)


def test_delphi::enumeratedtype_constructor_args():
    sig = inspect.signature(delphi::enumeratedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::subrangetype_is_not_abstract():
    assert not inspect.isabstract(delphi::subrangeType)


def test_delphi::subrangetype_constructor_exists():
    assert callable(delphi::subrangeType.__init__)


def test_delphi::subrangetype_constructor_args():
    sig = inspect.signature(delphi::subrangeType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::ordident_is_not_abstract():
    assert not inspect.isabstract(delphi::ordIdent)


def test_delphi::ordident_constructor_exists():
    assert callable(delphi::ordIdent.__init__)


def test_delphi::ordident_constructor_args():
    sig = inspect.signature(delphi::ordIdent.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(simpleType)


def test_simpletype_constructor_exists():
    assert callable(simpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(simpleType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::ordinaltype_is_not_abstract():
    assert not inspect.isabstract(delphi::ordinalType)


def test_delphi::ordinaltype_constructor_exists():
    assert callable(delphi::ordinalType.__init__)


def test_delphi::ordinaltype_constructor_args():
    sig = inspect.signature(delphi::ordinalType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::realtype_is_not_abstract():
    assert not inspect.isabstract(delphi::realType)


def test_delphi::realtype_constructor_exists():
    assert callable(delphi::realType.__init__)


def test_delphi::realtype_constructor_args():
    sig = inspect.signature(delphi::realType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(type)


def test_type_constructor_exists():
    assert callable(type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(type.__init__)
    params = list(sig.parameters.keys())



def test_delphi::proceduretype_is_not_abstract():
    assert not inspect.isabstract(delphi::procedureType)


def test_delphi::proceduretype_constructor_exists():
    assert callable(delphi::procedureType.__init__)


def test_delphi::proceduretype_constructor_args():
    sig = inspect.signature(delphi::procedureType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::pointertype_is_not_abstract():
    assert not inspect.isabstract(delphi::pointerType)


def test_delphi::pointertype_constructor_exists():
    assert callable(delphi::pointerType.__init__)


def test_delphi::pointertype_constructor_args():
    sig = inspect.signature(delphi::pointerType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::simpletype_is_not_abstract():
    assert not inspect.isabstract(delphi::simpleType)


def test_delphi::simpletype_constructor_exists():
    assert callable(delphi::simpleType.__init__)


def test_delphi::simpletype_constructor_args():
    sig = inspect.signature(delphi::simpleType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::structype_is_not_abstract():
    assert not inspect.isabstract(delphi::strucType)


def test_delphi::structype_constructor_exists():
    assert callable(delphi::strucType.__init__)


def test_delphi::structype_constructor_args():
    sig = inspect.signature(delphi::strucType.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::structype_has_port():
    assert hasattr(delphi::strucType, "port")
    descriptor = None
    for klass in delphi::strucType.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::stringtype_is_not_abstract():
    assert not inspect.isabstract(delphi::stringType)


def test_delphi::stringtype_constructor_exists():
    assert callable(delphi::stringType.__init__)


def test_delphi::stringtype_constructor_args():
    sig = inspect.signature(delphi::stringType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::varianttype_is_not_abstract():
    assert not inspect.isabstract(delphi::variantType)


def test_delphi::varianttype_constructor_exists():
    assert callable(delphi::variantType.__init__)


def test_delphi::varianttype_constructor_args():
    sig = inspect.signature(delphi::variantType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::classreftype_is_not_abstract():
    assert not inspect.isabstract(delphi::classRefType)


def test_delphi::classreftype_constructor_exists():
    assert callable(delphi::classRefType.__init__)


def test_delphi::classreftype_constructor_args():
    sig = inspect.signature(delphi::classRefType.__init__)
    params = list(sig.parameters.keys())



def test_interfacedecl_is_not_abstract():
    assert not inspect.isabstract(interfaceDecl)


def test_interfacedecl_constructor_exists():
    assert callable(interfaceDecl.__init__)


def test_interfacedecl_constructor_args():
    sig = inspect.signature(interfaceDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::exportedheading_is_not_abstract():
    assert not inspect.isabstract(delphi::exportedHeading)


def test_delphi::exportedheading_constructor_exists():
    assert callable(delphi::exportedHeading.__init__)


def test_delphi::exportedheading_constructor_args():
    sig = inspect.signature(delphi::exportedHeading.__init__)
    params = list(sig.parameters.keys())



def test_declsection_is_not_abstract():
    assert not inspect.isabstract(declSection)


def test_declsection_constructor_exists():
    assert callable(declSection.__init__)


def test_declsection_constructor_args():
    sig = inspect.signature(declSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::constsection_is_not_abstract():
    assert not inspect.isabstract(delphi::constSection)


def test_delphi::constsection_constructor_exists():
    assert callable(delphi::constSection.__init__)


def test_delphi::constsection_constructor_args():
    sig = inspect.signature(delphi::constSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::varsection_is_not_abstract():
    assert not inspect.isabstract(delphi::varSection)


def test_delphi::varsection_constructor_exists():
    assert callable(delphi::varSection.__init__)


def test_delphi::varsection_constructor_args():
    sig = inspect.signature(delphi::varSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::typesection_is_not_abstract():
    assert not inspect.isabstract(delphi::typeSection)


def test_delphi::typesection_constructor_exists():
    assert callable(delphi::typeSection.__init__)


def test_delphi::typesection_constructor_args():
    sig = inspect.signature(delphi::typeSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::labeldeclsection_is_not_abstract():
    assert not inspect.isabstract(delphi::labelDeclSection)


def test_delphi::labeldeclsection_constructor_exists():
    assert callable(delphi::labelDeclSection.__init__)


def test_delphi::labeldeclsection_constructor_args():
    sig = inspect.signature(delphi::labelDeclSection.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi::labeldeclsection_has_id():
    assert hasattr(delphi::labelDeclSection, "id")
    descriptor = None
    for klass in delphi::labelDeclSection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_file_is_not_abstract():
    assert not inspect.isabstract(file)


def test_file_constructor_exists():
    assert callable(file.__init__)


def test_file_constructor_args():
    sig = inspect.signature(file.__init__)
    params = list(sig.parameters.keys())



def test_delphi::library_is_not_abstract():
    assert not inspect.isabstract(delphi::library)


def test_delphi::library_constructor_exists():
    assert callable(delphi::library.__init__)


def test_delphi::library_constructor_args():
    sig = inspect.signature(delphi::library.__init__)
    params = list(sig.parameters.keys())



def test_delphi::packagedecl_is_not_abstract():
    assert not inspect.isabstract(delphi::packageDecl)


def test_delphi::packagedecl_constructor_exists():
    assert callable(delphi::packageDecl.__init__)


def test_delphi::packagedecl_constructor_args():
    sig = inspect.signature(delphi::packageDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::unit_is_not_abstract():
    assert not inspect.isabstract(delphi::unit)


def test_delphi::unit_constructor_exists():
    assert callable(delphi::unit.__init__)


def test_delphi::unit_constructor_args():
    sig = inspect.signature(delphi::unit.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::unit_has_port():
    assert hasattr(delphi::unit, "port")
    descriptor = None
    for klass in delphi::unit.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::program_is_not_abstract():
    assert not inspect.isabstract(delphi::program)


def test_delphi::program_constructor_exists():
    assert callable(delphi::program.__init__)


def test_delphi::program_constructor_args():
    sig = inspect.signature(delphi::program.__init__)
    params = list(sig.parameters.keys())



def test_cstrace_is_not_abstract():
    assert not inspect.isabstract(CSTrace)


def test_cstrace_constructor_exists():
    assert callable(CSTrace.__init__)


def test_cstrace_constructor_args():
    sig = inspect.signature(CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_delphi::implementationsection_is_not_abstract():
    assert not inspect.isabstract(delphi::implementationSection)


def test_delphi::implementationsection_constructor_exists():
    assert callable(delphi::implementationSection.__init__)


def test_delphi::implementationsection_constructor_args():
    sig = inspect.signature(delphi::implementationSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::directive_is_not_abstract():
    assert not inspect.isabstract(delphi::directive)


def test_delphi::directive_constructor_exists():
    assert callable(delphi::directive.__init__)


def test_delphi::directive_constructor_args():
    sig = inspect.signature(delphi::directive.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_delphi::directive_has_dir():
    assert hasattr(delphi::directive, "dir")
    descriptor = None
    for klass in delphi::directive.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_delphi::exportsitem_is_not_abstract():
    assert not inspect.isabstract(delphi::exportsItem)


def test_delphi::exportsitem_constructor_exists():
    assert callable(delphi::exportsItem.__init__)


def test_delphi::exportsitem_constructor_args():
    sig = inspect.signature(delphi::exportsItem.__init__)
    params = list(sig.parameters.keys())



def test_delphi::ident_is_not_abstract():
    assert not inspect.isabstract(delphi::ident)


def test_delphi::ident_constructor_exists():
    assert callable(delphi::ident.__init__)


def test_delphi::ident_constructor_args():
    sig = inspect.signature(delphi::ident.__init__)
    params = list(sig.parameters.keys())



def test_delphi::initsection_is_not_abstract():
    assert not inspect.isabstract(delphi::initSection)


def test_delphi::initsection_constructor_exists():
    assert callable(delphi::initSection.__init__)


def test_delphi::initsection_constructor_args():
    sig = inspect.signature(delphi::initSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::enumeratedtypeelement_is_not_abstract():
    assert not inspect.isabstract(delphi::enumeratedTypeElement)


def test_delphi::enumeratedtypeelement_constructor_exists():
    assert callable(delphi::enumeratedTypeElement.__init__)


def test_delphi::enumeratedtypeelement_constructor_args():
    sig = inspect.signature(delphi::enumeratedTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::vardecl_is_not_abstract():
    assert not inspect.isabstract(delphi::varDecl)


def test_delphi::vardecl_constructor_exists():
    assert callable(delphi::varDecl.__init__)


def test_delphi::vardecl_constructor_args():
    sig = inspect.signature(delphi::varDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::exportsstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::exportsStmt)


def test_delphi::exportsstmt_constructor_exists():
    assert callable(delphi::exportsStmt.__init__)


def test_delphi::exportsstmt_constructor_args():
    sig = inspect.signature(delphi::exportsStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::type_is_not_abstract():
    assert not inspect.isabstract(delphi::type)


def test_delphi::type_constructor_exists():
    assert callable(delphi::type.__init__)


def test_delphi::type_constructor_args():
    sig = inspect.signature(delphi::type.__init__)
    params = list(sig.parameters.keys())



def test_delphi::programblock_is_not_abstract():
    assert not inspect.isabstract(delphi::programBlock)


def test_delphi::programblock_constructor_exists():
    assert callable(delphi::programBlock.__init__)


def test_delphi::programblock_constructor_args():
    sig = inspect.signature(delphi::programBlock.__init__)
    params = list(sig.parameters.keys())



def test_delphi::containsclause_is_not_abstract():
    assert not inspect.isabstract(delphi::containsClause)


def test_delphi::containsclause_constructor_exists():
    assert callable(delphi::containsClause.__init__)


def test_delphi::containsclause_constructor_args():
    sig = inspect.signature(delphi::containsClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi::mulop_is_not_abstract():
    assert not inspect.isabstract(delphi::mulOp)


def test_delphi::mulop_constructor_exists():
    assert callable(delphi::mulOp.__init__)


def test_delphi::mulop_constructor_args():
    sig = inspect.signature(delphi::mulOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi::mulop_has_op():
    assert hasattr(delphi::mulOp, "op")
    descriptor = None
    for klass in delphi::mulOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_delphi::block_is_not_abstract():
    assert not inspect.isabstract(delphi::block)


def test_delphi::block_constructor_exists():
    assert callable(delphi::block.__init__)


def test_delphi::block_constructor_args():
    sig = inspect.signature(delphi::block.__init__)
    params = list(sig.parameters.keys())



def test_delphi::recvariant_is_not_abstract():
    assert not inspect.isabstract(delphi::recVariant)


def test_delphi::recvariant_constructor_exists():
    assert callable(delphi::recVariant.__init__)


def test_delphi::recvariant_constructor_args():
    sig = inspect.signature(delphi::recVariant.__init__)
    params = list(sig.parameters.keys())



def test_delphi::variantsection_is_not_abstract():
    assert not inspect.isabstract(delphi::variantSection)


def test_delphi::variantsection_constructor_exists():
    assert callable(delphi::variantSection.__init__)


def test_delphi::variantsection_constructor_args():
    sig = inspect.signature(delphi::variantSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::typedecl_is_not_abstract():
    assert not inspect.isabstract(delphi::typeDecl)


def test_delphi::typedecl_constructor_exists():
    assert callable(delphi::typeDecl.__init__)


def test_delphi::typedecl_constructor_args():
    sig = inspect.signature(delphi::typeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::typedecl_has_port():
    assert hasattr(delphi::typeDecl, "port")
    descriptor = None
    for klass in delphi::typeDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::usesclause_is_not_abstract():
    assert not inspect.isabstract(delphi::usesClause)


def test_delphi::usesclause_constructor_exists():
    assert callable(delphi::usesClause.__init__)


def test_delphi::usesclause_constructor_args():
    sig = inspect.signature(delphi::usesClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi::restrictedtype_is_not_abstract():
    assert not inspect.isabstract(delphi::restrictedType)


def test_delphi::restrictedtype_constructor_exists():
    assert callable(delphi::restrictedType.__init__)


def test_delphi::restrictedtype_constructor_args():
    sig = inspect.signature(delphi::restrictedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::fieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi::fieldList)


def test_delphi::fieldlist_constructor_exists():
    assert callable(delphi::fieldList.__init__)


def test_delphi::fieldlist_constructor_args():
    sig = inspect.signature(delphi::fieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::typedconstant_is_not_abstract():
    assert not inspect.isabstract(delphi::typedConstant)


def test_delphi::typedconstant_constructor_exists():
    assert callable(delphi::typedConstant.__init__)


def test_delphi::typedconstant_constructor_args():
    sig = inspect.signature(delphi::typedConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi::declsection_is_not_abstract():
    assert not inspect.isabstract(delphi::declSection)


def test_delphi::declsection_constructor_exists():
    assert callable(delphi::declSection.__init__)


def test_delphi::declsection_constructor_args():
    sig = inspect.signature(delphi::declSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::recordconstant_is_not_abstract():
    assert not inspect.isabstract(delphi::recordConstant)


def test_delphi::recordconstant_constructor_exists():
    assert callable(delphi::recordConstant.__init__)


def test_delphi::recordconstant_constructor_args():
    sig = inspect.signature(delphi::recordConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi::requiresclause_is_not_abstract():
    assert not inspect.isabstract(delphi::requiresClause)


def test_delphi::requiresclause_constructor_exists():
    assert callable(delphi::requiresClause.__init__)


def test_delphi::requiresclause_constructor_args():
    sig = inspect.signature(delphi::requiresClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi::constexpr_is_not_abstract():
    assert not inspect.isabstract(delphi::constExpr)


def test_delphi::constexpr_constructor_exists():
    assert callable(delphi::constExpr.__init__)


def test_delphi::constexpr_constructor_args():
    sig = inspect.signature(delphi::constExpr.__init__)
    params = list(sig.parameters.keys())



def test_delphi::arrayconstant_is_not_abstract():
    assert not inspect.isabstract(delphi::arrayConstant)


def test_delphi::arrayconstant_constructor_exists():
    assert callable(delphi::arrayConstant.__init__)


def test_delphi::arrayconstant_constructor_args():
    sig = inspect.signature(delphi::arrayConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi::interfacedecl_is_not_abstract():
    assert not inspect.isabstract(delphi::interfaceDecl)


def test_delphi::interfacedecl_constructor_exists():
    assert callable(delphi::interfaceDecl.__init__)


def test_delphi::interfacedecl_constructor_args():
    sig = inspect.signature(delphi::interfaceDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::constantdecl_is_not_abstract():
    assert not inspect.isabstract(delphi::constantDecl)


def test_delphi::constantdecl_constructor_exists():
    assert callable(delphi::constantDecl.__init__)


def test_delphi::constantdecl_constructor_args():
    sig = inspect.signature(delphi::constantDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::constantdecl_has_port():
    assert hasattr(delphi::constantDecl, "port")
    descriptor = None
    for klass in delphi::constantDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::recordfieldconstant_is_not_abstract():
    assert not inspect.isabstract(delphi::recordFieldConstant)


def test_delphi::recordfieldconstant_constructor_exists():
    assert callable(delphi::recordFieldConstant.__init__)


def test_delphi::recordfieldconstant_constructor_args():
    sig = inspect.signature(delphi::recordFieldConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi::fielddecl_is_not_abstract():
    assert not inspect.isabstract(delphi::fieldDecl)


def test_delphi::fielddecl_constructor_exists():
    assert callable(delphi::fieldDecl.__init__)


def test_delphi::fielddecl_constructor_args():
    sig = inspect.signature(delphi::fieldDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::fielddecl_has_port():
    assert hasattr(delphi::fieldDecl, "port")
    descriptor = None
    for klass in delphi::fieldDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::interfacesection_is_not_abstract():
    assert not inspect.isabstract(delphi::interfaceSection)


def test_delphi::interfacesection_constructor_exists():
    assert callable(delphi::interfaceSection.__init__)


def test_delphi::interfacesection_constructor_args():
    sig = inspect.signature(delphi::interfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::exprlist_is_not_abstract():
    assert not inspect.isabstract(delphi::exprList)


def test_delphi::exprlist_constructor_exists():
    assert callable(delphi::exprList.__init__)


def test_delphi::exprlist_constructor_args():
    sig = inspect.signature(delphi::exprList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::relop_is_not_abstract():
    assert not inspect.isabstract(delphi::relOp)


def test_delphi::relop_constructor_exists():
    assert callable(delphi::relOp.__init__)


def test_delphi::relop_constructor_args():
    sig = inspect.signature(delphi::relOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi::relop_has_op():
    assert hasattr(delphi::relOp, "op")
    descriptor = None
    for klass in delphi::relOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_delphi::expression_is_not_abstract():
    assert not inspect.isabstract(delphi::expression)


def test_delphi::expression_constructor_exists():
    assert callable(delphi::expression.__init__)


def test_delphi::expression_constructor_args():
    sig = inspect.signature(delphi::expression.__init__)
    params = list(sig.parameters.keys())



def test_delphi::file_is_not_abstract():
    assert not inspect.isabstract(delphi::file)


def test_delphi::file_constructor_exists():
    assert callable(delphi::file.__init__)


def test_delphi::file_constructor_args():
    sig = inspect.signature(delphi::file.__init__)
    params = list(sig.parameters.keys())



def test_delphi::designator_is_not_abstract():
    assert not inspect.isabstract(delphi::designator)


def test_delphi::designator_constructor_exists():
    assert callable(delphi::designator.__init__)


def test_delphi::designator_constructor_args():
    sig = inspect.signature(delphi::designator.__init__)
    params = list(sig.parameters.keys())



def test_delphi::addop_is_not_abstract():
    assert not inspect.isabstract(delphi::addOp)


def test_delphi::addop_constructor_exists():
    assert callable(delphi::addOp.__init__)


def test_delphi::addop_constructor_args():
    sig = inspect.signature(delphi::addOp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::mainrule_is_not_abstract():
    assert not inspect.isabstract(delphi::mainRule)


def test_delphi::mainrule_constructor_exists():
    assert callable(delphi::mainRule.__init__)


def test_delphi::mainrule_constructor_args():
    sig = inspect.signature(delphi::mainRule.__init__)
    params = list(sig.parameters.keys())



def test_delphi::visitable_is_not_abstract():
    assert not inspect.isabstract(delphi::Visitable)


def test_delphi::visitable_constructor_exists():
    assert callable(delphi::Visitable.__init__)


def test_delphi::visitable_constructor_args():
    sig = inspect.signature(delphi::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_delphi::cstrace_is_not_abstract():
    assert not inspect.isabstract(delphi::CSTrace)


def test_delphi::cstrace_constructor_exists():
    assert callable(delphi::CSTrace.__init__)


def test_delphi::cstrace_constructor_args():
    sig = inspect.signature(delphi::CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_constexpr_is_not_abstract():
    assert not inspect.isabstract(constExpr)


def test_constexpr_constructor_exists():
    assert callable(constExpr.__init__)


def test_constexpr_constructor_args():
    sig = inspect.signature(constExpr.__init__)
    params = list(sig.parameters.keys())



def test_delphi::multipleconstexp_is_not_abstract():
    assert not inspect.isabstract(delphi::MultipleConstExp)


def test_delphi::multipleconstexp_constructor_exists():
    assert callable(delphi::MultipleConstExp.__init__)


def test_delphi::multipleconstexp_constructor_args():
    sig = inspect.signature(delphi::MultipleConstExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::recordconstexp_is_not_abstract():
    assert not inspect.isabstract(delphi::RecordConstExp)


def test_delphi::recordconstexp_constructor_exists():
    assert callable(delphi::RecordConstExp.__init__)


def test_delphi::recordconstexp_constructor_args():
    sig = inspect.signature(delphi::RecordConstExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::constexp_is_not_abstract():
    assert not inspect.isabstract(delphi::ConstExp)


def test_delphi::constexp_constructor_exists():
    assert callable(delphi::ConstExp.__init__)


def test_delphi::constexp_constructor_args():
    sig = inspect.signature(delphi::ConstExp.__init__)
    params = list(sig.parameters.keys())



def test_ident_is_not_abstract():
    assert not inspect.isabstract(ident)


def test_ident_constructor_exists():
    assert callable(ident.__init__)


def test_ident_constructor_args():
    sig = inspect.signature(ident.__init__)
    params = list(sig.parameters.keys())



def test_delphi::reservedid_is_not_abstract():
    assert not inspect.isabstract(delphi::ReservedId)


def test_delphi::reservedid_constructor_exists():
    assert callable(delphi::ReservedId.__init__)


def test_delphi::reservedid_constructor_args():
    sig = inspect.signature(delphi::ReservedId.__init__)
    params = list(sig.parameters.keys())



def test_delphi::mineid_is_not_abstract():
    assert not inspect.isabstract(delphi::MineID)


def test_delphi::mineid_constructor_exists():
    assert callable(delphi::MineID.__init__)


def test_delphi::mineid_constructor_args():
    sig = inspect.signature(delphi::MineID.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "first" in params, "Missing parameter 'first'"

def test_delphi::mineid_has_second():
    assert hasattr(delphi::MineID, "second")
    descriptor = None
    for klass in delphi::MineID.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_delphi::mineid_has_first():
    assert hasattr(delphi::MineID, "first")
    descriptor = None
    for klass in delphi::MineID.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)



def test_delphi::multipleid_is_not_abstract():
    assert not inspect.isabstract(delphi::MultipleId)


def test_delphi::multipleid_constructor_exists():
    assert callable(delphi::MultipleId.__init__)


def test_delphi::multipleid_constructor_args():
    sig = inspect.signature(delphi::MultipleId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi::multipleid_has_id():
    assert hasattr(delphi::MultipleId, "id")
    descriptor = None
    for klass in delphi::MultipleId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(parameter)


def test_parameter_constructor_exists():
    assert callable(parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(parameter.__init__)
    params = list(sig.parameters.keys())



def test_delphi::parametersimple_is_not_abstract():
    assert not inspect.isabstract(delphi::parameterSimple)


def test_delphi::parametersimple_constructor_exists():
    assert callable(delphi::parameterSimple.__init__)


def test_delphi::parametersimple_constructor_args():
    sig = inspect.signature(delphi::parameterSimple.__init__)
    params = list(sig.parameters.keys())



def test_delphi::parameterlist_is_not_abstract():
    assert not inspect.isabstract(delphi::parameterList)


def test_delphi::parameterlist_constructor_exists():
    assert callable(delphi::parameterList.__init__)


def test_delphi::parameterlist_constructor_args():
    sig = inspect.signature(delphi::parameterList.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(simpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(simpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(simpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::inheritedstamnt_is_not_abstract():
    assert not inspect.isabstract(delphi::inheritedStamnt)


def test_delphi::inheritedstamnt_constructor_exists():
    assert callable(delphi::inheritedStamnt.__init__)


def test_delphi::inheritedstamnt_constructor_args():
    sig = inspect.signature(delphi::inheritedStamnt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::callstmnt_is_not_abstract():
    assert not inspect.isabstract(delphi::callStmnt)


def test_delphi::callstmnt_constructor_exists():
    assert callable(delphi::callStmnt.__init__)


def test_delphi::callstmnt_constructor_args():
    sig = inspect.signature(delphi::callStmnt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::gotostmnt_is_not_abstract():
    assert not inspect.isabstract(delphi::gotoStmnt)


def test_delphi::gotostmnt_constructor_exists():
    assert callable(delphi::gotoStmnt.__init__)


def test_delphi::gotostmnt_constructor_args():
    sig = inspect.signature(delphi::gotoStmnt.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_delphi::gotostmnt_has_label():
    assert hasattr(delphi::gotoStmnt, "label")
    descriptor = None
    for klass in delphi::gotoStmnt.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_delphi::assignmentstmnt_is_not_abstract():
    assert not inspect.isabstract(delphi::assignmentStmnt)


def test_delphi::assignmentstmnt_constructor_exists():
    assert callable(delphi::assignmentStmnt.__init__)


def test_delphi::assignmentstmnt_constructor_args():
    sig = inspect.signature(delphi::assignmentStmnt.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_delphi::assignmentstmnt_has_operator():
    assert hasattr(delphi::assignmentStmnt, "operator")
    descriptor = None
    for klass in delphi::assignmentStmnt.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_addop_is_not_abstract():
    assert not inspect.isabstract(addOp)


def test_addop_constructor_exists():
    assert callable(addOp.__init__)


def test_addop_constructor_args():
    sig = inspect.signature(addOp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::adop_is_not_abstract():
    assert not inspect.isabstract(delphi::adOp)


def test_delphi::adop_constructor_exists():
    assert callable(delphi::adOp.__init__)


def test_delphi::adop_constructor_args():
    sig = inspect.signature(delphi::adOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi::adop_has_op():
    assert hasattr(delphi::adOp, "op")
    descriptor = None
    for klass in delphi::adOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_factor_is_not_abstract():
    assert not inspect.isabstract(factor)


def test_factor_constructor_exists():
    assert callable(factor.__init__)


def test_factor_constructor_args():
    sig = inspect.signature(factor.__init__)
    params = list(sig.parameters.keys())



def test_delphi::simplefactor_is_not_abstract():
    assert not inspect.isabstract(delphi::simpleFactor)


def test_delphi::simplefactor_constructor_exists():
    assert callable(delphi::simpleFactor.__init__)


def test_delphi::simplefactor_constructor_args():
    sig = inspect.signature(delphi::simpleFactor.__init__)
    params = list(sig.parameters.keys())



def test_delphi::multexp_is_not_abstract():
    assert not inspect.isabstract(delphi::multExp)


def test_delphi::multexp_constructor_exists():
    assert callable(delphi::multExp.__init__)


def test_delphi::multexp_constructor_args():
    sig = inspect.signature(delphi::multExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::addexp_is_not_abstract():
    assert not inspect.isabstract(delphi::addExp)


def test_delphi::addexp_constructor_exists():
    assert callable(delphi::addExp.__init__)


def test_delphi::addexp_constructor_args():
    sig = inspect.signature(delphi::addExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::relexp_is_not_abstract():
    assert not inspect.isabstract(delphi::relExp)


def test_delphi::relexp_constructor_exists():
    assert callable(delphi::relExp.__init__)


def test_delphi::relexp_constructor_args():
    sig = inspect.signature(delphi::relExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi::recordconstexpr_is_not_abstract():
    assert not inspect.isabstract(delphi::recordConstExpr)


def test_delphi::recordconstexpr_constructor_exists():
    assert callable(delphi::recordConstExpr.__init__)


def test_delphi::recordconstexpr_constructor_args():
    sig = inspect.signature(delphi::recordConstExpr.__init__)
    params = list(sig.parameters.keys())



def test_pointertype_is_not_abstract():
    assert not inspect.isabstract(pointerType)


def test_pointertype_constructor_exists():
    assert callable(pointerType.__init__)


def test_pointertype_constructor_args():
    sig = inspect.signature(pointerType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::typeid_is_not_abstract():
    assert not inspect.isabstract(delphi::typeId)


def test_delphi::typeid_constructor_exists():
    assert callable(delphi::typeId.__init__)


def test_delphi::typeid_constructor_args():
    sig = inspect.signature(delphi::typeId.__init__)
    params = list(sig.parameters.keys())



def test_delphi::unitid_is_not_abstract():
    assert not inspect.isabstract(delphi::unitId)


def test_delphi::unitid_constructor_exists():
    assert callable(delphi::unitId.__init__)


def test_delphi::unitid_constructor_args():
    sig = inspect.signature(delphi::unitId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi::unitid_has_id():
    assert hasattr(delphi::unitId, "id")
    descriptor = None
    for klass in delphi::unitId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_classheritage_is_not_abstract():
    assert not inspect.isabstract(classHeritage)


def test_classheritage_constructor_exists():
    assert callable(classHeritage.__init__)


def test_classheritage_constructor_args():
    sig = inspect.signature(classHeritage.__init__)
    params = list(sig.parameters.keys())



def test_objfieldlist_is_not_abstract():
    assert not inspect.isabstract(objFieldList)


def test_objfieldlist_constructor_exists():
    assert callable(objFieldList.__init__)


def test_objfieldlist_constructor_args():
    sig = inspect.signature(objFieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::identlist_is_not_abstract():
    assert not inspect.isabstract(delphi::identList)


def test_delphi::identlist_constructor_exists():
    assert callable(delphi::identList.__init__)


def test_delphi::identlist_constructor_args():
    sig = inspect.signature(delphi::identList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::propertyspecifiers_is_not_abstract():
    assert not inspect.isabstract(delphi::propertySpecifiers)


def test_delphi::propertyspecifiers_constructor_exists():
    assert callable(delphi::propertySpecifiers.__init__)


def test_delphi::propertyspecifiers_constructor_args():
    sig = inspect.signature(delphi::propertySpecifiers.__init__)
    params = list(sig.parameters.keys())



def test_delphi::propertyinterface_is_not_abstract():
    assert not inspect.isabstract(delphi::propertyInterface)


def test_delphi::propertyinterface_constructor_exists():
    assert callable(delphi::propertyInterface.__init__)


def test_delphi::propertyinterface_constructor_args():
    sig = inspect.signature(delphi::propertyInterface.__init__)
    params = list(sig.parameters.keys())



def test_delphi::interfaceheritage_is_not_abstract():
    assert not inspect.isabstract(delphi::interfaceHeritage)


def test_delphi::interfaceheritage_constructor_exists():
    assert callable(delphi::interfaceHeritage.__init__)


def test_delphi::interfaceheritage_constructor_args():
    sig = inspect.signature(delphi::interfaceHeritage.__init__)
    params = list(sig.parameters.keys())



def test_delphi::propertyparameterlist_is_not_abstract():
    assert not inspect.isabstract(delphi::propertyParameterList)


def test_delphi::propertyparameterlist_constructor_exists():
    assert callable(delphi::propertyParameterList.__init__)


def test_delphi::propertyparameterlist_constructor_args():
    sig = inspect.signature(delphi::propertyParameterList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::classheritage_is_not_abstract():
    assert not inspect.isabstract(delphi::classHeritage)


def test_delphi::classheritage_constructor_exists():
    assert callable(delphi::classHeritage.__init__)


def test_delphi::classheritage_constructor_args():
    sig = inspect.signature(delphi::classHeritage.__init__)
    params = list(sig.parameters.keys())



def test_delphi::propertylist_is_not_abstract():
    assert not inspect.isabstract(delphi::propertyList)


def test_delphi::propertylist_constructor_exists():
    assert callable(delphi::propertyList.__init__)


def test_delphi::propertylist_constructor_args():
    sig = inspect.signature(delphi::propertyList.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::propertylist_has_port():
    assert hasattr(delphi::propertyList, "port")
    descriptor = None
    for klass in delphi::propertyList.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::classproperty_is_not_abstract():
    assert not inspect.isabstract(delphi::classProperty)


def test_delphi::classproperty_constructor_exists():
    assert callable(delphi::classProperty.__init__)


def test_delphi::classproperty_constructor_args():
    sig = inspect.signature(delphi::classProperty.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi::classproperty_has_visibility():
    assert hasattr(delphi::classProperty, "visibility")
    descriptor = None
    for klass in delphi::classProperty.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi::classmethod_is_not_abstract():
    assert not inspect.isabstract(delphi::classMethod)


def test_delphi::classmethod_constructor_exists():
    assert callable(delphi::classMethod.__init__)


def test_delphi::classmethod_constructor_args():
    sig = inspect.signature(delphi::classMethod.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi::classmethod_has_visibility():
    assert hasattr(delphi::classMethod, "visibility")
    descriptor = None
    for klass in delphi::classMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi::classfield_is_not_abstract():
    assert not inspect.isabstract(delphi::classField)


def test_delphi::classfield_constructor_exists():
    assert callable(delphi::classField.__init__)


def test_delphi::classfield_constructor_args():
    sig = inspect.signature(delphi::classField.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi::classfield_has_visibility():
    assert hasattr(delphi::classField, "visibility")
    descriptor = None
    for klass in delphi::classField.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi::classpropertylist_is_not_abstract():
    assert not inspect.isabstract(delphi::classPropertyList)


def test_delphi::classpropertylist_constructor_exists():
    assert callable(delphi::classPropertyList.__init__)


def test_delphi::classpropertylist_constructor_args():
    sig = inspect.signature(delphi::classPropertyList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::classmethodlist_is_not_abstract():
    assert not inspect.isabstract(delphi::classMethodList)


def test_delphi::classmethodlist_constructor_exists():
    assert callable(delphi::classMethodList.__init__)


def test_delphi::classmethodlist_constructor_args():
    sig = inspect.signature(delphi::classMethodList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::classfieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi::classFieldList)


def test_delphi::classfieldlist_constructor_exists():
    assert callable(delphi::classFieldList.__init__)


def test_delphi::classfieldlist_constructor_args():
    sig = inspect.signature(delphi::classFieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::methodheading_is_not_abstract():
    assert not inspect.isabstract(delphi::methodHeading)


def test_delphi::methodheading_constructor_exists():
    assert callable(delphi::methodHeading.__init__)


def test_delphi::methodheading_constructor_args():
    sig = inspect.signature(delphi::methodHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi::methodlist_is_not_abstract():
    assert not inspect.isabstract(delphi::methodList)


def test_delphi::methodlist_constructor_exists():
    assert callable(delphi::methodList.__init__)


def test_delphi::methodlist_constructor_args():
    sig = inspect.signature(delphi::methodList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::objfieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi::objFieldList)


def test_delphi::objfieldlist_constructor_exists():
    assert callable(delphi::objFieldList.__init__)


def test_delphi::objfieldlist_constructor_args():
    sig = inspect.signature(delphi::objFieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::objheritage_is_not_abstract():
    assert not inspect.isabstract(delphi::objHeritage)


def test_delphi::objheritage_constructor_exists():
    assert callable(delphi::objHeritage.__init__)


def test_delphi::objheritage_constructor_args():
    sig = inspect.signature(delphi::objHeritage.__init__)
    params = list(sig.parameters.keys())



def test_restrictedtype_is_not_abstract():
    assert not inspect.isabstract(restrictedType)


def test_restrictedtype_constructor_exists():
    assert callable(restrictedType.__init__)


def test_restrictedtype_constructor_args():
    sig = inspect.signature(restrictedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::classtype_is_not_abstract():
    assert not inspect.isabstract(delphi::classType)


def test_delphi::classtype_constructor_exists():
    assert callable(delphi::classType.__init__)


def test_delphi::classtype_constructor_args():
    sig = inspect.signature(delphi::classType.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi::classtype_has_visibility():
    assert hasattr(delphi::classType, "visibility")
    descriptor = None
    for klass in delphi::classType.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi::interfacetype_is_not_abstract():
    assert not inspect.isabstract(delphi::interfaceType)


def test_delphi::interfacetype_constructor_exists():
    assert callable(delphi::interfaceType.__init__)


def test_delphi::interfacetype_constructor_args():
    sig = inspect.signature(delphi::interfaceType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::objecttype_is_not_abstract():
    assert not inspect.isabstract(delphi::objectType)


def test_delphi::objecttype_constructor_exists():
    assert callable(delphi::objectType.__init__)


def test_delphi::objecttype_constructor_args():
    sig = inspect.signature(delphi::objectType.__init__)
    params = list(sig.parameters.keys())



def test_delphi::parameter_is_not_abstract():
    assert not inspect.isabstract(delphi::parameter)


def test_delphi::parameter_constructor_exists():
    assert callable(delphi::parameter.__init__)


def test_delphi::parameter_constructor_args():
    sig = inspect.signature(delphi::parameter.__init__)
    params = list(sig.parameters.keys())



def test_delphi::formalparm_is_not_abstract():
    assert not inspect.isabstract(delphi::formalParm)


def test_delphi::formalparm_constructor_exists():
    assert callable(delphi::formalParm.__init__)


def test_delphi::formalparm_constructor_args():
    sig = inspect.signature(delphi::formalParm.__init__)
    params = list(sig.parameters.keys())



def test_delphi::formalparameters_is_not_abstract():
    assert not inspect.isabstract(delphi::formalParameters)


def test_delphi::formalparameters_constructor_exists():
    assert callable(delphi::formalParameters.__init__)


def test_delphi::formalparameters_constructor_args():
    sig = inspect.signature(delphi::formalParameters.__init__)
    params = list(sig.parameters.keys())



def test_methodheading_is_not_abstract():
    assert not inspect.isabstract(methodHeading)


def test_methodheading_constructor_exists():
    assert callable(methodHeading.__init__)


def test_methodheading_constructor_args():
    sig = inspect.signature(methodHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi::constructorheading_is_not_abstract():
    assert not inspect.isabstract(delphi::constructorHeading)


def test_delphi::constructorheading_constructor_exists():
    assert callable(delphi::constructorHeading.__init__)


def test_delphi::constructorheading_constructor_args():
    sig = inspect.signature(delphi::constructorHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi::destructorheading_is_not_abstract():
    assert not inspect.isabstract(delphi::destructorHeading)


def test_delphi::destructorheading_constructor_exists():
    assert callable(delphi::destructorHeading.__init__)


def test_delphi::destructorheading_constructor_args():
    sig = inspect.signature(delphi::destructorHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi::procedureheading_is_not_abstract():
    assert not inspect.isabstract(delphi::procedureHeading)


def test_delphi::procedureheading_constructor_exists():
    assert callable(delphi::procedureHeading.__init__)


def test_delphi::procedureheading_constructor_args():
    sig = inspect.signature(delphi::procedureHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi::functionheading_is_not_abstract():
    assert not inspect.isabstract(delphi::functionHeading)


def test_delphi::functionheading_constructor_exists():
    assert callable(delphi::functionHeading.__init__)


def test_delphi::functionheading_constructor_args():
    sig = inspect.signature(delphi::functionHeading.__init__)
    params = list(sig.parameters.keys())



def test_proceduredeclsection_is_not_abstract():
    assert not inspect.isabstract(procedureDeclSection)


def test_proceduredeclsection_constructor_exists():
    assert callable(procedureDeclSection.__init__)


def test_proceduredeclsection_constructor_args():
    sig = inspect.signature(procedureDeclSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi::functiondecl_is_not_abstract():
    assert not inspect.isabstract(delphi::functionDecl)


def test_delphi::functiondecl_constructor_exists():
    assert callable(delphi::functionDecl.__init__)


def test_delphi::functiondecl_constructor_args():
    sig = inspect.signature(delphi::functionDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::proceduredecl_is_not_abstract():
    assert not inspect.isabstract(delphi::procedureDecl)


def test_delphi::proceduredecl_constructor_exists():
    assert callable(delphi::procedureDecl.__init__)


def test_delphi::proceduredecl_constructor_args():
    sig = inspect.signature(delphi::procedureDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi::proceduredeclsection_is_not_abstract():
    assert not inspect.isabstract(delphi::procedureDeclSection)


def test_delphi::proceduredeclsection_constructor_exists():
    assert callable(delphi::procedureDeclSection.__init__)


def test_delphi::proceduredeclsection_constructor_args():
    sig = inspect.signature(delphi::procedureDeclSection.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi::proceduredeclsection_has_port():
    assert hasattr(delphi::procedureDeclSection, "port")
    descriptor = None
    for klass in delphi::procedureDeclSection.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi::exceptionblock_is_not_abstract():
    assert not inspect.isabstract(delphi::exceptionBlock)


def test_delphi::exceptionblock_constructor_exists():
    assert callable(delphi::exceptionBlock.__init__)


def test_delphi::exceptionblock_constructor_args():
    sig = inspect.signature(delphi::exceptionBlock.__init__)
    params = list(sig.parameters.keys())



def test_delphi::qualid_is_not_abstract():
    assert not inspect.isabstract(delphi::qualId)


def test_delphi::qualid_constructor_exists():
    assert callable(delphi::qualId.__init__)


def test_delphi::qualid_constructor_args():
    sig = inspect.signature(delphi::qualId.__init__)
    params = list(sig.parameters.keys())



def test_loopstmt_is_not_abstract():
    assert not inspect.isabstract(loopStmt)


def test_loopstmt_constructor_exists():
    assert callable(loopStmt.__init__)


def test_loopstmt_constructor_args():
    sig = inspect.signature(loopStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::forstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::forStmt)


def test_delphi::forstmt_constructor_exists():
    assert callable(delphi::forStmt.__init__)


def test_delphi::forstmt_constructor_args():
    sig = inspect.signature(delphi::forStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::whilestmt_is_not_abstract():
    assert not inspect.isabstract(delphi::whileStmt)


def test_delphi::whilestmt_constructor_exists():
    assert callable(delphi::whileStmt.__init__)


def test_delphi::whilestmt_constructor_args():
    sig = inspect.signature(delphi::whileStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::repeatstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::repeatStmt)


def test_delphi::repeatstmt_constructor_exists():
    assert callable(delphi::repeatStmt.__init__)


def test_delphi::repeatstmt_constructor_args():
    sig = inspect.signature(delphi::repeatStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::stmtlist_is_not_abstract():
    assert not inspect.isabstract(delphi::stmtList)


def test_delphi::stmtlist_constructor_exists():
    assert callable(delphi::stmtList.__init__)


def test_delphi::stmtlist_constructor_args():
    sig = inspect.signature(delphi::stmtList.__init__)
    params = list(sig.parameters.keys())



def test_delphi::caselabel_is_not_abstract():
    assert not inspect.isabstract(delphi::caseLabel)


def test_delphi::caselabel_constructor_exists():
    assert callable(delphi::caseLabel.__init__)


def test_delphi::caselabel_constructor_args():
    sig = inspect.signature(delphi::caseLabel.__init__)
    params = list(sig.parameters.keys())



def test_delphi::caseselector_is_not_abstract():
    assert not inspect.isabstract(delphi::caseSelector)


def test_delphi::caseselector_constructor_exists():
    assert callable(delphi::caseSelector.__init__)


def test_delphi::caseselector_constructor_args():
    sig = inspect.signature(delphi::caseSelector.__init__)
    params = list(sig.parameters.keys())



def test_conditionalstmt_is_not_abstract():
    assert not inspect.isabstract(conditionalStmt)


def test_conditionalstmt_constructor_exists():
    assert callable(conditionalStmt.__init__)


def test_conditionalstmt_constructor_args():
    sig = inspect.signature(conditionalStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::casestmt_is_not_abstract():
    assert not inspect.isabstract(delphi::caseStmt)


def test_delphi::casestmt_constructor_exists():
    assert callable(delphi::caseStmt.__init__)


def test_delphi::casestmt_constructor_args():
    sig = inspect.signature(delphi::caseStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::ifstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::ifStmt)


def test_delphi::ifstmt_constructor_exists():
    assert callable(delphi::ifStmt.__init__)


def test_delphi::ifstmt_constructor_args():
    sig = inspect.signature(delphi::ifStmt.__init__)
    params = list(sig.parameters.keys())



def test_structstmt_is_not_abstract():
    assert not inspect.isabstract(structStmt)


def test_structstmt_constructor_exists():
    assert callable(structStmt.__init__)


def test_structstmt_constructor_args():
    sig = inspect.signature(structStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::loopstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::loopStmt)


def test_delphi::loopstmt_constructor_exists():
    assert callable(delphi::loopStmt.__init__)


def test_delphi::loopstmt_constructor_args():
    sig = inspect.signature(delphi::loopStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::conditionalstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::conditionalStmt)


def test_delphi::conditionalstmt_constructor_exists():
    assert callable(delphi::conditionalStmt.__init__)


def test_delphi::conditionalstmt_constructor_args():
    sig = inspect.signature(delphi::conditionalStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::trystmt_is_not_abstract():
    assert not inspect.isabstract(delphi::tryStmt)


def test_delphi::trystmt_constructor_exists():
    assert callable(delphi::tryStmt.__init__)


def test_delphi::trystmt_constructor_args():
    sig = inspect.signature(delphi::tryStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::withstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::withStmt)


def test_delphi::withstmt_constructor_exists():
    assert callable(delphi::withStmt.__init__)


def test_delphi::withstmt_constructor_args():
    sig = inspect.signature(delphi::withStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::raisestmt_is_not_abstract():
    assert not inspect.isabstract(delphi::raiseStmt)


def test_delphi::raisestmt_constructor_exists():
    assert callable(delphi::raiseStmt.__init__)


def test_delphi::raisestmt_constructor_args():
    sig = inspect.signature(delphi::raiseStmt.__init__)
    params = list(sig.parameters.keys())
    assert "at" in params, "Missing parameter 'at'"
    assert "raise_" in params, "Missing parameter 'raise_'"

def test_delphi::raisestmt_has_at():
    assert hasattr(delphi::raiseStmt, "at")
    descriptor = None
    for klass in delphi::raiseStmt.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)

def test_delphi::raisestmt_has_raise_():
    assert hasattr(delphi::raiseStmt, "raise_")
    descriptor = None
    for klass in delphi::raiseStmt.__mro__:
        if "raise_" in klass.__dict__:
            descriptor = klass.__dict__["raise_"]
            break
    assert isinstance(descriptor, property)



def test_delphi::compoundstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::compoundStmt)


def test_delphi::compoundstmt_constructor_exists():
    assert callable(delphi::compoundStmt.__init__)


def test_delphi::compoundstmt_constructor_args():
    sig = inspect.signature(delphi::compoundStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::assemblerstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::assemblerStmt)


def test_delphi::assemblerstmt_constructor_exists():
    assert callable(delphi::assemblerStmt.__init__)


def test_delphi::assemblerstmt_constructor_args():
    sig = inspect.signature(delphi::assemblerStmt.__init__)
    params = list(sig.parameters.keys())



def test_unlabelledstatement_is_not_abstract():
    assert not inspect.isabstract(unlabelledStatement)


def test_unlabelledstatement_constructor_exists():
    assert callable(unlabelledStatement.__init__)


def test_unlabelledstatement_constructor_args():
    sig = inspect.signature(unlabelledStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::structstmt_is_not_abstract():
    assert not inspect.isabstract(delphi::structStmt)


def test_delphi::structstmt_constructor_exists():
    assert callable(delphi::structStmt.__init__)


def test_delphi::structstmt_constructor_args():
    sig = inspect.signature(delphi::structStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi::simplestatement_is_not_abstract():
    assert not inspect.isabstract(delphi::simpleStatement)


def test_delphi::simplestatement_constructor_exists():
    assert callable(delphi::simpleStatement.__init__)


def test_delphi::simplestatement_constructor_args():
    sig = inspect.signature(delphi::simpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::unlabelledstatement_is_not_abstract():
    assert not inspect.isabstract(delphi::unlabelledStatement)


def test_delphi::unlabelledstatement_constructor_exists():
    assert callable(delphi::unlabelledStatement.__init__)


def test_delphi::unlabelledstatement_constructor_args():
    sig = inspect.signature(delphi::unlabelledStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::statement_is_not_abstract():
    assert not inspect.isabstract(delphi::statement)


def test_delphi::statement_constructor_exists():
    assert callable(delphi::statement.__init__)


def test_delphi::statement_constructor_args():
    sig = inspect.signature(delphi::statement.__init__)
    params = list(sig.parameters.keys())
    assert "labelId" in params, "Missing parameter 'labelId'"

def test_delphi::statement_has_labelId():
    assert hasattr(delphi::statement, "labelId")
    descriptor = None
    for klass in delphi::statement.__mro__:
        if "labelId" in klass.__dict__:
            descriptor = klass.__dict__["labelId"]
            break
    assert isinstance(descriptor, property)



def test_delphi::setconstructor_is_not_abstract():
    assert not inspect.isabstract(delphi::setConstructor)


def test_delphi::setconstructor_constructor_exists():
    assert callable(delphi::setConstructor.__init__)


def test_delphi::setconstructor_constructor_args():
    sig = inspect.signature(delphi::setConstructor.__init__)
    params = list(sig.parameters.keys())



def test_delphi::setelement_is_not_abstract():
    assert not inspect.isabstract(delphi::setElement)


def test_delphi::setelement_constructor_exists():
    assert callable(delphi::setElement.__init__)


def test_delphi::setelement_constructor_args():
    sig = inspect.signature(delphi::setElement.__init__)
    params = list(sig.parameters.keys())



def test_delphi::reservedword_is_not_abstract():
    assert not inspect.isabstract(delphi::reservedWord)


def test_delphi::reservedword_constructor_exists():
    assert callable(delphi::reservedWord.__init__)


def test_delphi::reservedword_constructor_args():
    sig = inspect.signature(delphi::reservedWord.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi::reservedword_has_id():
    assert hasattr(delphi::reservedWord, "id")
    descriptor = None
    for klass in delphi::reservedWord.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_delphi::designatorpart_is_not_abstract():
    assert not inspect.isabstract(delphi::designatorPart)


def test_delphi::designatorpart_constructor_exists():
    assert callable(delphi::designatorPart.__init__)


def test_delphi::designatorpart_constructor_args():
    sig = inspect.signature(delphi::designatorPart.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "id2" in params, "Missing parameter 'id2'"

def test_delphi::designatorpart_has_id():
    assert hasattr(delphi::designatorPart, "id")
    descriptor = None
    for klass in delphi::designatorPart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_delphi::designatorpart_has_id2():
    assert hasattr(delphi::designatorPart, "id2")
    descriptor = None
    for klass in delphi::designatorPart.__mro__:
        if "id2" in klass.__dict__:
            descriptor = klass.__dict__["id2"]
            break
    assert isinstance(descriptor, property)



def test_delphi::designatorsubpart_is_not_abstract():
    assert not inspect.isabstract(delphi::designatorSubPart)


def test_delphi::designatorsubpart_constructor_exists():
    assert callable(delphi::designatorSubPart.__init__)


def test_delphi::designatorsubpart_constructor_args():
    sig = inspect.signature(delphi::designatorSubPart.__init__)
    params = list(sig.parameters.keys())


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
term_strategy = st.builds(
    term,
)
delphi::factor_strategy = st.builds(
    delphi::factor,
    string=
        safe_text,
    number=
        safe_text
)
simpleExpression_strategy = st.builds(
    simpleExpression,
)
delphi::term_strategy = st.builds(
    delphi::term,
)
expression_strategy = st.builds(
    expression,
)
delphi::simpleExpression_strategy = st.builds(
    delphi::simpleExpression,
)
strucType_strategy = st.builds(
    strucType,
)
delphi::setType_strategy = st.builds(
    delphi::setType,
)
delphi::fileType_strategy = st.builds(
    delphi::fileType,
)
delphi::recType_strategy = st.builds(
    delphi::recType,
)
delphi::arrayType_strategy = st.builds(
    delphi::arrayType,
)
ordinalType_strategy = st.builds(
    ordinalType,
)
delphi::enumeratedType_strategy = st.builds(
    delphi::enumeratedType,
)
delphi::subrangeType_strategy = st.builds(
    delphi::subrangeType,
)
delphi::ordIdent_strategy = st.builds(
    delphi::ordIdent,
)
simpleType_strategy = st.builds(
    simpleType,
)
delphi::ordinalType_strategy = st.builds(
    delphi::ordinalType,
)
delphi::realType_strategy = st.builds(
    delphi::realType,
)
type_strategy = st.builds(
    type,
)
delphi::procedureType_strategy = st.builds(
    delphi::procedureType,
)
delphi::pointerType_strategy = st.builds(
    delphi::pointerType,
)
delphi::simpleType_strategy = st.builds(
    delphi::simpleType,
)
delphi::strucType_strategy = st.builds(
    delphi::strucType,
    port=
        safe_text
)
delphi::stringType_strategy = st.builds(
    delphi::stringType,
)
delphi::variantType_strategy = st.builds(
    delphi::variantType,
)
delphi::classRefType_strategy = st.builds(
    delphi::classRefType,
)
interfaceDecl_strategy = st.builds(
    interfaceDecl,
)
delphi::exportedHeading_strategy = st.builds(
    delphi::exportedHeading,
)
declSection_strategy = st.builds(
    declSection,
)
delphi::constSection_strategy = st.builds(
    delphi::constSection,
)
delphi::varSection_strategy = st.builds(
    delphi::varSection,
)
delphi::typeSection_strategy = st.builds(
    delphi::typeSection,
)
delphi::labelDeclSection_strategy = st.builds(
    delphi::labelDeclSection,
    id=
        safe_text
)
file_strategy = st.builds(
    file,
)
delphi::library_strategy = st.builds(
    delphi::library,
)
delphi::packageDecl_strategy = st.builds(
    delphi::packageDecl,
)
delphi::unit_strategy = st.builds(
    delphi::unit,
    port=
        safe_text
)
delphi::program_strategy = st.builds(
    delphi::program,
)
CSTrace_strategy = st.builds(
    CSTrace,
)
delphi::implementationSection_strategy = st.builds(
    delphi::implementationSection,
)
delphi::directive_strategy = st.builds(
    delphi::directive,
    dir=
        safe_text
)
delphi::exportsItem_strategy = st.builds(
    delphi::exportsItem,
)
delphi::ident_strategy = st.builds(
    delphi::ident,
)
delphi::initSection_strategy = st.builds(
    delphi::initSection,
)
delphi::enumeratedTypeElement_strategy = st.builds(
    delphi::enumeratedTypeElement,
)
delphi::varDecl_strategy = st.builds(
    delphi::varDecl,
)
delphi::exportsStmt_strategy = st.builds(
    delphi::exportsStmt,
)
delphi::type_strategy = st.builds(
    delphi::type,
)
delphi::programBlock_strategy = st.builds(
    delphi::programBlock,
)
delphi::containsClause_strategy = st.builds(
    delphi::containsClause,
)
delphi::mulOp_strategy = st.builds(
    delphi::mulOp,
    op=
        safe_text
)
delphi::block_strategy = st.builds(
    delphi::block,
)
delphi::recVariant_strategy = st.builds(
    delphi::recVariant,
)
delphi::variantSection_strategy = st.builds(
    delphi::variantSection,
)
delphi::typeDecl_strategy = st.builds(
    delphi::typeDecl,
    port=
        safe_text
)
delphi::usesClause_strategy = st.builds(
    delphi::usesClause,
)
delphi::restrictedType_strategy = st.builds(
    delphi::restrictedType,
)
delphi::fieldList_strategy = st.builds(
    delphi::fieldList,
)
delphi::typedConstant_strategy = st.builds(
    delphi::typedConstant,
)
delphi::declSection_strategy = st.builds(
    delphi::declSection,
)
delphi::recordConstant_strategy = st.builds(
    delphi::recordConstant,
)
delphi::requiresClause_strategy = st.builds(
    delphi::requiresClause,
)
delphi::constExpr_strategy = st.builds(
    delphi::constExpr,
)
delphi::arrayConstant_strategy = st.builds(
    delphi::arrayConstant,
)
delphi::interfaceDecl_strategy = st.builds(
    delphi::interfaceDecl,
)
delphi::constantDecl_strategy = st.builds(
    delphi::constantDecl,
    port=
        safe_text
)
delphi::recordFieldConstant_strategy = st.builds(
    delphi::recordFieldConstant,
)
delphi::fieldDecl_strategy = st.builds(
    delphi::fieldDecl,
    port=
        safe_text
)
delphi::interfaceSection_strategy = st.builds(
    delphi::interfaceSection,
)
delphi::exprList_strategy = st.builds(
    delphi::exprList,
)
delphi::relOp_strategy = st.builds(
    delphi::relOp,
    op=
        safe_text
)
delphi::expression_strategy = st.builds(
    delphi::expression,
)
delphi::file_strategy = st.builds(
    delphi::file,
)
delphi::designator_strategy = st.builds(
    delphi::designator,
)
delphi::addOp_strategy = st.builds(
    delphi::addOp,
)
delphi::mainRule_strategy = st.builds(
    delphi::mainRule,
)
delphi::Visitable_strategy = st.builds(
    delphi::Visitable,
)
delphi::CSTrace_strategy = st.builds(
    delphi::CSTrace,
)
constExpr_strategy = st.builds(
    constExpr,
)
delphi::MultipleConstExp_strategy = st.builds(
    delphi::MultipleConstExp,
)
delphi::RecordConstExp_strategy = st.builds(
    delphi::RecordConstExp,
)
delphi::ConstExp_strategy = st.builds(
    delphi::ConstExp,
)
ident_strategy = st.builds(
    ident,
)
delphi::ReservedId_strategy = st.builds(
    delphi::ReservedId,
)
delphi::MineID_strategy = st.builds(
    delphi::MineID,
    second=
        safe_text,
    first=
        safe_text
)
delphi::MultipleId_strategy = st.builds(
    delphi::MultipleId,
    id=
        safe_text
)
parameter_strategy = st.builds(
    parameter,
)
delphi::parameterSimple_strategy = st.builds(
    delphi::parameterSimple,
)
delphi::parameterList_strategy = st.builds(
    delphi::parameterList,
)
simpleStatement_strategy = st.builds(
    simpleStatement,
)
delphi::inheritedStamnt_strategy = st.builds(
    delphi::inheritedStamnt,
)
delphi::callStmnt_strategy = st.builds(
    delphi::callStmnt,
)
delphi::gotoStmnt_strategy = st.builds(
    delphi::gotoStmnt,
    label=
        safe_text
)
delphi::assignmentStmnt_strategy = st.builds(
    delphi::assignmentStmnt,
    operator=
        safe_text
)
addOp_strategy = st.builds(
    addOp,
)
delphi::adOp_strategy = st.builds(
    delphi::adOp,
    op=
        safe_text
)
factor_strategy = st.builds(
    factor,
)
delphi::simpleFactor_strategy = st.builds(
    delphi::simpleFactor,
)
delphi::multExp_strategy = st.builds(
    delphi::multExp,
)
delphi::addExp_strategy = st.builds(
    delphi::addExp,
)
delphi::relExp_strategy = st.builds(
    delphi::relExp,
)
delphi::recordConstExpr_strategy = st.builds(
    delphi::recordConstExpr,
)
pointerType_strategy = st.builds(
    pointerType,
)
delphi::typeId_strategy = st.builds(
    delphi::typeId,
)
delphi::unitId_strategy = st.builds(
    delphi::unitId,
    id=
        safe_text
)
classHeritage_strategy = st.builds(
    classHeritage,
)
objFieldList_strategy = st.builds(
    objFieldList,
)
delphi::identList_strategy = st.builds(
    delphi::identList,
)
delphi::propertySpecifiers_strategy = st.builds(
    delphi::propertySpecifiers,
)
delphi::propertyInterface_strategy = st.builds(
    delphi::propertyInterface,
)
delphi::interfaceHeritage_strategy = st.builds(
    delphi::interfaceHeritage,
)
delphi::propertyParameterList_strategy = st.builds(
    delphi::propertyParameterList,
)
delphi::classHeritage_strategy = st.builds(
    delphi::classHeritage,
)
delphi::propertyList_strategy = st.builds(
    delphi::propertyList,
    port=
        safe_text
)
delphi::classProperty_strategy = st.builds(
    delphi::classProperty,
    visibility=
        safe_text
)
delphi::classMethod_strategy = st.builds(
    delphi::classMethod,
    visibility=
        safe_text
)
delphi::classField_strategy = st.builds(
    delphi::classField,
    visibility=
        safe_text
)
delphi::classPropertyList_strategy = st.builds(
    delphi::classPropertyList,
)
delphi::classMethodList_strategy = st.builds(
    delphi::classMethodList,
)
delphi::classFieldList_strategy = st.builds(
    delphi::classFieldList,
)
delphi::methodHeading_strategy = st.builds(
    delphi::methodHeading,
)
delphi::methodList_strategy = st.builds(
    delphi::methodList,
)
delphi::objFieldList_strategy = st.builds(
    delphi::objFieldList,
)
delphi::objHeritage_strategy = st.builds(
    delphi::objHeritage,
)
restrictedType_strategy = st.builds(
    restrictedType,
)
delphi::classType_strategy = st.builds(
    delphi::classType,
    visibility=
        safe_text
)
delphi::interfaceType_strategy = st.builds(
    delphi::interfaceType,
)
delphi::objectType_strategy = st.builds(
    delphi::objectType,
)
delphi::parameter_strategy = st.builds(
    delphi::parameter,
)
delphi::formalParm_strategy = st.builds(
    delphi::formalParm,
)
delphi::formalParameters_strategy = st.builds(
    delphi::formalParameters,
)
methodHeading_strategy = st.builds(
    methodHeading,
)
delphi::constructorHeading_strategy = st.builds(
    delphi::constructorHeading,
)
delphi::destructorHeading_strategy = st.builds(
    delphi::destructorHeading,
)
delphi::procedureHeading_strategy = st.builds(
    delphi::procedureHeading,
)
delphi::functionHeading_strategy = st.builds(
    delphi::functionHeading,
)
procedureDeclSection_strategy = st.builds(
    procedureDeclSection,
)
delphi::functionDecl_strategy = st.builds(
    delphi::functionDecl,
)
delphi::procedureDecl_strategy = st.builds(
    delphi::procedureDecl,
)
delphi::procedureDeclSection_strategy = st.builds(
    delphi::procedureDeclSection,
    port=
        safe_text
)
delphi::exceptionBlock_strategy = st.builds(
    delphi::exceptionBlock,
)
delphi::qualId_strategy = st.builds(
    delphi::qualId,
)
loopStmt_strategy = st.builds(
    loopStmt,
)
delphi::forStmt_strategy = st.builds(
    delphi::forStmt,
)
delphi::whileStmt_strategy = st.builds(
    delphi::whileStmt,
)
delphi::repeatStmt_strategy = st.builds(
    delphi::repeatStmt,
)
delphi::stmtList_strategy = st.builds(
    delphi::stmtList,
)
delphi::caseLabel_strategy = st.builds(
    delphi::caseLabel,
)
delphi::caseSelector_strategy = st.builds(
    delphi::caseSelector,
)
conditionalStmt_strategy = st.builds(
    conditionalStmt,
)
delphi::caseStmt_strategy = st.builds(
    delphi::caseStmt,
)
delphi::ifStmt_strategy = st.builds(
    delphi::ifStmt,
)
structStmt_strategy = st.builds(
    structStmt,
)
delphi::loopStmt_strategy = st.builds(
    delphi::loopStmt,
)
delphi::conditionalStmt_strategy = st.builds(
    delphi::conditionalStmt,
)
delphi::tryStmt_strategy = st.builds(
    delphi::tryStmt,
)
delphi::withStmt_strategy = st.builds(
    delphi::withStmt,
)
delphi::raiseStmt_strategy = st.builds(
    delphi::raiseStmt,
    at=
        safe_text,
    raise_=
        safe_text
)
delphi::compoundStmt_strategy = st.builds(
    delphi::compoundStmt,
)
delphi::assemblerStmt_strategy = st.builds(
    delphi::assemblerStmt,
)
unlabelledStatement_strategy = st.builds(
    unlabelledStatement,
)
delphi::structStmt_strategy = st.builds(
    delphi::structStmt,
)
delphi::simpleStatement_strategy = st.builds(
    delphi::simpleStatement,
)
delphi::unlabelledStatement_strategy = st.builds(
    delphi::unlabelledStatement,
)
delphi::statement_strategy = st.builds(
    delphi::statement,
    labelId=
        safe_text
)
delphi::setConstructor_strategy = st.builds(
    delphi::setConstructor,
)
delphi::setElement_strategy = st.builds(
    delphi::setElement,
)
delphi::reservedWord_strategy = st.builds(
    delphi::reservedWord,
    id=
        safe_text
)
delphi::designatorPart_strategy = st.builds(
    delphi::designatorPart,
    id=
        safe_text,
    id2=
        safe_text
)
delphi::designatorSubPart_strategy = st.builds(
    delphi::designatorSubPart,
)

@given(instance=term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, term)

@given(instance=delphi::factor_strategy)
@settings(max_examples=50)
def test_delphi::factor_instantiation(instance):
    assert isinstance(instance, delphi::factor)

@given(instance=delphi::factor_strategy)
def test_delphi::factor_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=delphi::factor_strategy)
def test_delphi::factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=delphi::factor_strategy)
def test_delphi::factor_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=delphi::factor_strategy)
def test_delphi::factor_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=simpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, simpleExpression)

@given(instance=delphi::term_strategy)
@settings(max_examples=50)
def test_delphi::term_instantiation(instance):
    assert isinstance(instance, delphi::term)

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=delphi::simpleExpression_strategy)
@settings(max_examples=50)
def test_delphi::simpleexpression_instantiation(instance):
    assert isinstance(instance, delphi::simpleExpression)

@given(instance=strucType_strategy)
@settings(max_examples=50)
def test_structype_instantiation(instance):
    assert isinstance(instance, strucType)

@given(instance=delphi::setType_strategy)
@settings(max_examples=50)
def test_delphi::settype_instantiation(instance):
    assert isinstance(instance, delphi::setType)

@given(instance=delphi::fileType_strategy)
@settings(max_examples=50)
def test_delphi::filetype_instantiation(instance):
    assert isinstance(instance, delphi::fileType)

@given(instance=delphi::recType_strategy)
@settings(max_examples=50)
def test_delphi::rectype_instantiation(instance):
    assert isinstance(instance, delphi::recType)

@given(instance=delphi::arrayType_strategy)
@settings(max_examples=50)
def test_delphi::arraytype_instantiation(instance):
    assert isinstance(instance, delphi::arrayType)

@given(instance=ordinalType_strategy)
@settings(max_examples=50)
def test_ordinaltype_instantiation(instance):
    assert isinstance(instance, ordinalType)

@given(instance=delphi::enumeratedType_strategy)
@settings(max_examples=50)
def test_delphi::enumeratedtype_instantiation(instance):
    assert isinstance(instance, delphi::enumeratedType)

@given(instance=delphi::subrangeType_strategy)
@settings(max_examples=50)
def test_delphi::subrangetype_instantiation(instance):
    assert isinstance(instance, delphi::subrangeType)

@given(instance=delphi::ordIdent_strategy)
@settings(max_examples=50)
def test_delphi::ordident_instantiation(instance):
    assert isinstance(instance, delphi::ordIdent)

@given(instance=simpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, simpleType)

@given(instance=delphi::ordinalType_strategy)
@settings(max_examples=50)
def test_delphi::ordinaltype_instantiation(instance):
    assert isinstance(instance, delphi::ordinalType)

@given(instance=delphi::realType_strategy)
@settings(max_examples=50)
def test_delphi::realtype_instantiation(instance):
    assert isinstance(instance, delphi::realType)

@given(instance=type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, type)

@given(instance=delphi::procedureType_strategy)
@settings(max_examples=50)
def test_delphi::proceduretype_instantiation(instance):
    assert isinstance(instance, delphi::procedureType)

@given(instance=delphi::pointerType_strategy)
@settings(max_examples=50)
def test_delphi::pointertype_instantiation(instance):
    assert isinstance(instance, delphi::pointerType)

@given(instance=delphi::simpleType_strategy)
@settings(max_examples=50)
def test_delphi::simpletype_instantiation(instance):
    assert isinstance(instance, delphi::simpleType)

@given(instance=delphi::strucType_strategy)
@settings(max_examples=50)
def test_delphi::structype_instantiation(instance):
    assert isinstance(instance, delphi::strucType)

@given(instance=delphi::strucType_strategy)
def test_delphi::structype_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::strucType_strategy)
def test_delphi::structype_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::stringType_strategy)
@settings(max_examples=50)
def test_delphi::stringtype_instantiation(instance):
    assert isinstance(instance, delphi::stringType)

@given(instance=delphi::variantType_strategy)
@settings(max_examples=50)
def test_delphi::varianttype_instantiation(instance):
    assert isinstance(instance, delphi::variantType)

@given(instance=delphi::classRefType_strategy)
@settings(max_examples=50)
def test_delphi::classreftype_instantiation(instance):
    assert isinstance(instance, delphi::classRefType)

@given(instance=interfaceDecl_strategy)
@settings(max_examples=50)
def test_interfacedecl_instantiation(instance):
    assert isinstance(instance, interfaceDecl)

@given(instance=delphi::exportedHeading_strategy)
@settings(max_examples=50)
def test_delphi::exportedheading_instantiation(instance):
    assert isinstance(instance, delphi::exportedHeading)

@given(instance=declSection_strategy)
@settings(max_examples=50)
def test_declsection_instantiation(instance):
    assert isinstance(instance, declSection)

@given(instance=delphi::constSection_strategy)
@settings(max_examples=50)
def test_delphi::constsection_instantiation(instance):
    assert isinstance(instance, delphi::constSection)

@given(instance=delphi::varSection_strategy)
@settings(max_examples=50)
def test_delphi::varsection_instantiation(instance):
    assert isinstance(instance, delphi::varSection)

@given(instance=delphi::typeSection_strategy)
@settings(max_examples=50)
def test_delphi::typesection_instantiation(instance):
    assert isinstance(instance, delphi::typeSection)

@given(instance=delphi::labelDeclSection_strategy)
@settings(max_examples=50)
def test_delphi::labeldeclsection_instantiation(instance):
    assert isinstance(instance, delphi::labelDeclSection)

@given(instance=delphi::labelDeclSection_strategy)
def test_delphi::labeldeclsection_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=delphi::labelDeclSection_strategy)
def test_delphi::labeldeclsection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=file_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, file)

@given(instance=delphi::library_strategy)
@settings(max_examples=50)
def test_delphi::library_instantiation(instance):
    assert isinstance(instance, delphi::library)

@given(instance=delphi::packageDecl_strategy)
@settings(max_examples=50)
def test_delphi::packagedecl_instantiation(instance):
    assert isinstance(instance, delphi::packageDecl)

@given(instance=delphi::unit_strategy)
@settings(max_examples=50)
def test_delphi::unit_instantiation(instance):
    assert isinstance(instance, delphi::unit)

@given(instance=delphi::unit_strategy)
def test_delphi::unit_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::unit_strategy)
def test_delphi::unit_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::program_strategy)
@settings(max_examples=50)
def test_delphi::program_instantiation(instance):
    assert isinstance(instance, delphi::program)

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=delphi::implementationSection_strategy)
@settings(max_examples=50)
def test_delphi::implementationsection_instantiation(instance):
    assert isinstance(instance, delphi::implementationSection)

@given(instance=delphi::directive_strategy)
@settings(max_examples=50)
def test_delphi::directive_instantiation(instance):
    assert isinstance(instance, delphi::directive)

@given(instance=delphi::directive_strategy)
def test_delphi::directive_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=delphi::directive_strategy)
def test_delphi::directive_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=delphi::exportsItem_strategy)
@settings(max_examples=50)
def test_delphi::exportsitem_instantiation(instance):
    assert isinstance(instance, delphi::exportsItem)

@given(instance=delphi::ident_strategy)
@settings(max_examples=50)
def test_delphi::ident_instantiation(instance):
    assert isinstance(instance, delphi::ident)

@given(instance=delphi::initSection_strategy)
@settings(max_examples=50)
def test_delphi::initsection_instantiation(instance):
    assert isinstance(instance, delphi::initSection)

@given(instance=delphi::enumeratedTypeElement_strategy)
@settings(max_examples=50)
def test_delphi::enumeratedtypeelement_instantiation(instance):
    assert isinstance(instance, delphi::enumeratedTypeElement)

@given(instance=delphi::varDecl_strategy)
@settings(max_examples=50)
def test_delphi::vardecl_instantiation(instance):
    assert isinstance(instance, delphi::varDecl)

@given(instance=delphi::exportsStmt_strategy)
@settings(max_examples=50)
def test_delphi::exportsstmt_instantiation(instance):
    assert isinstance(instance, delphi::exportsStmt)

@given(instance=delphi::type_strategy)
@settings(max_examples=50)
def test_delphi::type_instantiation(instance):
    assert isinstance(instance, delphi::type)

@given(instance=delphi::programBlock_strategy)
@settings(max_examples=50)
def test_delphi::programblock_instantiation(instance):
    assert isinstance(instance, delphi::programBlock)

@given(instance=delphi::containsClause_strategy)
@settings(max_examples=50)
def test_delphi::containsclause_instantiation(instance):
    assert isinstance(instance, delphi::containsClause)

@given(instance=delphi::mulOp_strategy)
@settings(max_examples=50)
def test_delphi::mulop_instantiation(instance):
    assert isinstance(instance, delphi::mulOp)

@given(instance=delphi::mulOp_strategy)
def test_delphi::mulop_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=delphi::mulOp_strategy)
def test_delphi::mulop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=delphi::block_strategy)
@settings(max_examples=50)
def test_delphi::block_instantiation(instance):
    assert isinstance(instance, delphi::block)

@given(instance=delphi::recVariant_strategy)
@settings(max_examples=50)
def test_delphi::recvariant_instantiation(instance):
    assert isinstance(instance, delphi::recVariant)

@given(instance=delphi::variantSection_strategy)
@settings(max_examples=50)
def test_delphi::variantsection_instantiation(instance):
    assert isinstance(instance, delphi::variantSection)

@given(instance=delphi::typeDecl_strategy)
@settings(max_examples=50)
def test_delphi::typedecl_instantiation(instance):
    assert isinstance(instance, delphi::typeDecl)

@given(instance=delphi::typeDecl_strategy)
def test_delphi::typedecl_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::typeDecl_strategy)
def test_delphi::typedecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::usesClause_strategy)
@settings(max_examples=50)
def test_delphi::usesclause_instantiation(instance):
    assert isinstance(instance, delphi::usesClause)

@given(instance=delphi::restrictedType_strategy)
@settings(max_examples=50)
def test_delphi::restrictedtype_instantiation(instance):
    assert isinstance(instance, delphi::restrictedType)

@given(instance=delphi::fieldList_strategy)
@settings(max_examples=50)
def test_delphi::fieldlist_instantiation(instance):
    assert isinstance(instance, delphi::fieldList)

@given(instance=delphi::typedConstant_strategy)
@settings(max_examples=50)
def test_delphi::typedconstant_instantiation(instance):
    assert isinstance(instance, delphi::typedConstant)

@given(instance=delphi::declSection_strategy)
@settings(max_examples=50)
def test_delphi::declsection_instantiation(instance):
    assert isinstance(instance, delphi::declSection)

@given(instance=delphi::recordConstant_strategy)
@settings(max_examples=50)
def test_delphi::recordconstant_instantiation(instance):
    assert isinstance(instance, delphi::recordConstant)

@given(instance=delphi::requiresClause_strategy)
@settings(max_examples=50)
def test_delphi::requiresclause_instantiation(instance):
    assert isinstance(instance, delphi::requiresClause)

@given(instance=delphi::constExpr_strategy)
@settings(max_examples=50)
def test_delphi::constexpr_instantiation(instance):
    assert isinstance(instance, delphi::constExpr)

@given(instance=delphi::arrayConstant_strategy)
@settings(max_examples=50)
def test_delphi::arrayconstant_instantiation(instance):
    assert isinstance(instance, delphi::arrayConstant)

@given(instance=delphi::interfaceDecl_strategy)
@settings(max_examples=50)
def test_delphi::interfacedecl_instantiation(instance):
    assert isinstance(instance, delphi::interfaceDecl)

@given(instance=delphi::constantDecl_strategy)
@settings(max_examples=50)
def test_delphi::constantdecl_instantiation(instance):
    assert isinstance(instance, delphi::constantDecl)

@given(instance=delphi::constantDecl_strategy)
def test_delphi::constantdecl_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::constantDecl_strategy)
def test_delphi::constantdecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::recordFieldConstant_strategy)
@settings(max_examples=50)
def test_delphi::recordfieldconstant_instantiation(instance):
    assert isinstance(instance, delphi::recordFieldConstant)

@given(instance=delphi::fieldDecl_strategy)
@settings(max_examples=50)
def test_delphi::fielddecl_instantiation(instance):
    assert isinstance(instance, delphi::fieldDecl)

@given(instance=delphi::fieldDecl_strategy)
def test_delphi::fielddecl_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::fieldDecl_strategy)
def test_delphi::fielddecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::interfaceSection_strategy)
@settings(max_examples=50)
def test_delphi::interfacesection_instantiation(instance):
    assert isinstance(instance, delphi::interfaceSection)

@given(instance=delphi::exprList_strategy)
@settings(max_examples=50)
def test_delphi::exprlist_instantiation(instance):
    assert isinstance(instance, delphi::exprList)

@given(instance=delphi::relOp_strategy)
@settings(max_examples=50)
def test_delphi::relop_instantiation(instance):
    assert isinstance(instance, delphi::relOp)

@given(instance=delphi::relOp_strategy)
def test_delphi::relop_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=delphi::relOp_strategy)
def test_delphi::relop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=delphi::expression_strategy)
@settings(max_examples=50)
def test_delphi::expression_instantiation(instance):
    assert isinstance(instance, delphi::expression)

@given(instance=delphi::file_strategy)
@settings(max_examples=50)
def test_delphi::file_instantiation(instance):
    assert isinstance(instance, delphi::file)

@given(instance=delphi::designator_strategy)
@settings(max_examples=50)
def test_delphi::designator_instantiation(instance):
    assert isinstance(instance, delphi::designator)

@given(instance=delphi::addOp_strategy)
@settings(max_examples=50)
def test_delphi::addop_instantiation(instance):
    assert isinstance(instance, delphi::addOp)

@given(instance=delphi::mainRule_strategy)
@settings(max_examples=50)
def test_delphi::mainrule_instantiation(instance):
    assert isinstance(instance, delphi::mainRule)

@given(instance=delphi::Visitable_strategy)
@settings(max_examples=50)
def test_delphi::visitable_instantiation(instance):
    assert isinstance(instance, delphi::Visitable)

@given(instance=delphi::CSTrace_strategy)
@settings(max_examples=50)
def test_delphi::cstrace_instantiation(instance):
    assert isinstance(instance, delphi::CSTrace)

@given(instance=constExpr_strategy)
@settings(max_examples=50)
def test_constexpr_instantiation(instance):
    assert isinstance(instance, constExpr)

@given(instance=delphi::MultipleConstExp_strategy)
@settings(max_examples=50)
def test_delphi::multipleconstexp_instantiation(instance):
    assert isinstance(instance, delphi::MultipleConstExp)

@given(instance=delphi::RecordConstExp_strategy)
@settings(max_examples=50)
def test_delphi::recordconstexp_instantiation(instance):
    assert isinstance(instance, delphi::RecordConstExp)

@given(instance=delphi::ConstExp_strategy)
@settings(max_examples=50)
def test_delphi::constexp_instantiation(instance):
    assert isinstance(instance, delphi::ConstExp)

@given(instance=ident_strategy)
@settings(max_examples=50)
def test_ident_instantiation(instance):
    assert isinstance(instance, ident)

@given(instance=delphi::ReservedId_strategy)
@settings(max_examples=50)
def test_delphi::reservedid_instantiation(instance):
    assert isinstance(instance, delphi::ReservedId)

@given(instance=delphi::MineID_strategy)
@settings(max_examples=50)
def test_delphi::mineid_instantiation(instance):
    assert isinstance(instance, delphi::MineID)

@given(instance=delphi::MineID_strategy)
def test_delphi::mineid_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=delphi::MineID_strategy)
def test_delphi::mineid_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=delphi::MineID_strategy)
def test_delphi::mineid_first_type(instance):
    assert isinstance(instance.first, str)


@given(instance=delphi::MineID_strategy)
def test_delphi::mineid_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=delphi::MultipleId_strategy)
@settings(max_examples=50)
def test_delphi::multipleid_instantiation(instance):
    assert isinstance(instance, delphi::MultipleId)

@given(instance=delphi::MultipleId_strategy)
def test_delphi::multipleid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=delphi::MultipleId_strategy)
def test_delphi::multipleid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, parameter)

@given(instance=delphi::parameterSimple_strategy)
@settings(max_examples=50)
def test_delphi::parametersimple_instantiation(instance):
    assert isinstance(instance, delphi::parameterSimple)

@given(instance=delphi::parameterList_strategy)
@settings(max_examples=50)
def test_delphi::parameterlist_instantiation(instance):
    assert isinstance(instance, delphi::parameterList)

@given(instance=simpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, simpleStatement)

@given(instance=delphi::inheritedStamnt_strategy)
@settings(max_examples=50)
def test_delphi::inheritedstamnt_instantiation(instance):
    assert isinstance(instance, delphi::inheritedStamnt)

@given(instance=delphi::callStmnt_strategy)
@settings(max_examples=50)
def test_delphi::callstmnt_instantiation(instance):
    assert isinstance(instance, delphi::callStmnt)

@given(instance=delphi::gotoStmnt_strategy)
@settings(max_examples=50)
def test_delphi::gotostmnt_instantiation(instance):
    assert isinstance(instance, delphi::gotoStmnt)

@given(instance=delphi::gotoStmnt_strategy)
def test_delphi::gotostmnt_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=delphi::gotoStmnt_strategy)
def test_delphi::gotostmnt_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=delphi::assignmentStmnt_strategy)
@settings(max_examples=50)
def test_delphi::assignmentstmnt_instantiation(instance):
    assert isinstance(instance, delphi::assignmentStmnt)

@given(instance=delphi::assignmentStmnt_strategy)
def test_delphi::assignmentstmnt_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=delphi::assignmentStmnt_strategy)
def test_delphi::assignmentstmnt_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=addOp_strategy)
@settings(max_examples=50)
def test_addop_instantiation(instance):
    assert isinstance(instance, addOp)

@given(instance=delphi::adOp_strategy)
@settings(max_examples=50)
def test_delphi::adop_instantiation(instance):
    assert isinstance(instance, delphi::adOp)

@given(instance=delphi::adOp_strategy)
def test_delphi::adop_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=delphi::adOp_strategy)
def test_delphi::adop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=factor_strategy)
@settings(max_examples=50)
def test_factor_instantiation(instance):
    assert isinstance(instance, factor)

@given(instance=delphi::simpleFactor_strategy)
@settings(max_examples=50)
def test_delphi::simplefactor_instantiation(instance):
    assert isinstance(instance, delphi::simpleFactor)

@given(instance=delphi::multExp_strategy)
@settings(max_examples=50)
def test_delphi::multexp_instantiation(instance):
    assert isinstance(instance, delphi::multExp)

@given(instance=delphi::addExp_strategy)
@settings(max_examples=50)
def test_delphi::addexp_instantiation(instance):
    assert isinstance(instance, delphi::addExp)

@given(instance=delphi::relExp_strategy)
@settings(max_examples=50)
def test_delphi::relexp_instantiation(instance):
    assert isinstance(instance, delphi::relExp)

@given(instance=delphi::recordConstExpr_strategy)
@settings(max_examples=50)
def test_delphi::recordconstexpr_instantiation(instance):
    assert isinstance(instance, delphi::recordConstExpr)

@given(instance=pointerType_strategy)
@settings(max_examples=50)
def test_pointertype_instantiation(instance):
    assert isinstance(instance, pointerType)

@given(instance=delphi::typeId_strategy)
@settings(max_examples=50)
def test_delphi::typeid_instantiation(instance):
    assert isinstance(instance, delphi::typeId)

@given(instance=delphi::unitId_strategy)
@settings(max_examples=50)
def test_delphi::unitid_instantiation(instance):
    assert isinstance(instance, delphi::unitId)

@given(instance=delphi::unitId_strategy)
def test_delphi::unitid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=delphi::unitId_strategy)
def test_delphi::unitid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=classHeritage_strategy)
@settings(max_examples=50)
def test_classheritage_instantiation(instance):
    assert isinstance(instance, classHeritage)

@given(instance=objFieldList_strategy)
@settings(max_examples=50)
def test_objfieldlist_instantiation(instance):
    assert isinstance(instance, objFieldList)

@given(instance=delphi::identList_strategy)
@settings(max_examples=50)
def test_delphi::identlist_instantiation(instance):
    assert isinstance(instance, delphi::identList)

@given(instance=delphi::propertySpecifiers_strategy)
@settings(max_examples=50)
def test_delphi::propertyspecifiers_instantiation(instance):
    assert isinstance(instance, delphi::propertySpecifiers)

@given(instance=delphi::propertyInterface_strategy)
@settings(max_examples=50)
def test_delphi::propertyinterface_instantiation(instance):
    assert isinstance(instance, delphi::propertyInterface)

@given(instance=delphi::interfaceHeritage_strategy)
@settings(max_examples=50)
def test_delphi::interfaceheritage_instantiation(instance):
    assert isinstance(instance, delphi::interfaceHeritage)

@given(instance=delphi::propertyParameterList_strategy)
@settings(max_examples=50)
def test_delphi::propertyparameterlist_instantiation(instance):
    assert isinstance(instance, delphi::propertyParameterList)

@given(instance=delphi::classHeritage_strategy)
@settings(max_examples=50)
def test_delphi::classheritage_instantiation(instance):
    assert isinstance(instance, delphi::classHeritage)

@given(instance=delphi::propertyList_strategy)
@settings(max_examples=50)
def test_delphi::propertylist_instantiation(instance):
    assert isinstance(instance, delphi::propertyList)

@given(instance=delphi::propertyList_strategy)
def test_delphi::propertylist_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::propertyList_strategy)
def test_delphi::propertylist_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::classProperty_strategy)
@settings(max_examples=50)
def test_delphi::classproperty_instantiation(instance):
    assert isinstance(instance, delphi::classProperty)

@given(instance=delphi::classProperty_strategy)
def test_delphi::classproperty_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=delphi::classProperty_strategy)
def test_delphi::classproperty_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi::classMethod_strategy)
@settings(max_examples=50)
def test_delphi::classmethod_instantiation(instance):
    assert isinstance(instance, delphi::classMethod)

@given(instance=delphi::classMethod_strategy)
def test_delphi::classmethod_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=delphi::classMethod_strategy)
def test_delphi::classmethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi::classField_strategy)
@settings(max_examples=50)
def test_delphi::classfield_instantiation(instance):
    assert isinstance(instance, delphi::classField)

@given(instance=delphi::classField_strategy)
def test_delphi::classfield_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=delphi::classField_strategy)
def test_delphi::classfield_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi::classPropertyList_strategy)
@settings(max_examples=50)
def test_delphi::classpropertylist_instantiation(instance):
    assert isinstance(instance, delphi::classPropertyList)

@given(instance=delphi::classMethodList_strategy)
@settings(max_examples=50)
def test_delphi::classmethodlist_instantiation(instance):
    assert isinstance(instance, delphi::classMethodList)

@given(instance=delphi::classFieldList_strategy)
@settings(max_examples=50)
def test_delphi::classfieldlist_instantiation(instance):
    assert isinstance(instance, delphi::classFieldList)

@given(instance=delphi::methodHeading_strategy)
@settings(max_examples=50)
def test_delphi::methodheading_instantiation(instance):
    assert isinstance(instance, delphi::methodHeading)

@given(instance=delphi::methodList_strategy)
@settings(max_examples=50)
def test_delphi::methodlist_instantiation(instance):
    assert isinstance(instance, delphi::methodList)

@given(instance=delphi::objFieldList_strategy)
@settings(max_examples=50)
def test_delphi::objfieldlist_instantiation(instance):
    assert isinstance(instance, delphi::objFieldList)

@given(instance=delphi::objHeritage_strategy)
@settings(max_examples=50)
def test_delphi::objheritage_instantiation(instance):
    assert isinstance(instance, delphi::objHeritage)

@given(instance=restrictedType_strategy)
@settings(max_examples=50)
def test_restrictedtype_instantiation(instance):
    assert isinstance(instance, restrictedType)

@given(instance=delphi::classType_strategy)
@settings(max_examples=50)
def test_delphi::classtype_instantiation(instance):
    assert isinstance(instance, delphi::classType)

@given(instance=delphi::classType_strategy)
def test_delphi::classtype_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=delphi::classType_strategy)
def test_delphi::classtype_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi::interfaceType_strategy)
@settings(max_examples=50)
def test_delphi::interfacetype_instantiation(instance):
    assert isinstance(instance, delphi::interfaceType)

@given(instance=delphi::objectType_strategy)
@settings(max_examples=50)
def test_delphi::objecttype_instantiation(instance):
    assert isinstance(instance, delphi::objectType)

@given(instance=delphi::parameter_strategy)
@settings(max_examples=50)
def test_delphi::parameter_instantiation(instance):
    assert isinstance(instance, delphi::parameter)

@given(instance=delphi::formalParm_strategy)
@settings(max_examples=50)
def test_delphi::formalparm_instantiation(instance):
    assert isinstance(instance, delphi::formalParm)

@given(instance=delphi::formalParameters_strategy)
@settings(max_examples=50)
def test_delphi::formalparameters_instantiation(instance):
    assert isinstance(instance, delphi::formalParameters)

@given(instance=methodHeading_strategy)
@settings(max_examples=50)
def test_methodheading_instantiation(instance):
    assert isinstance(instance, methodHeading)

@given(instance=delphi::constructorHeading_strategy)
@settings(max_examples=50)
def test_delphi::constructorheading_instantiation(instance):
    assert isinstance(instance, delphi::constructorHeading)

@given(instance=delphi::destructorHeading_strategy)
@settings(max_examples=50)
def test_delphi::destructorheading_instantiation(instance):
    assert isinstance(instance, delphi::destructorHeading)

@given(instance=delphi::procedureHeading_strategy)
@settings(max_examples=50)
def test_delphi::procedureheading_instantiation(instance):
    assert isinstance(instance, delphi::procedureHeading)

@given(instance=delphi::functionHeading_strategy)
@settings(max_examples=50)
def test_delphi::functionheading_instantiation(instance):
    assert isinstance(instance, delphi::functionHeading)

@given(instance=procedureDeclSection_strategy)
@settings(max_examples=50)
def test_proceduredeclsection_instantiation(instance):
    assert isinstance(instance, procedureDeclSection)

@given(instance=delphi::functionDecl_strategy)
@settings(max_examples=50)
def test_delphi::functiondecl_instantiation(instance):
    assert isinstance(instance, delphi::functionDecl)

@given(instance=delphi::procedureDecl_strategy)
@settings(max_examples=50)
def test_delphi::proceduredecl_instantiation(instance):
    assert isinstance(instance, delphi::procedureDecl)

@given(instance=delphi::procedureDeclSection_strategy)
@settings(max_examples=50)
def test_delphi::proceduredeclsection_instantiation(instance):
    assert isinstance(instance, delphi::procedureDeclSection)

@given(instance=delphi::procedureDeclSection_strategy)
def test_delphi::proceduredeclsection_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=delphi::procedureDeclSection_strategy)
def test_delphi::proceduredeclsection_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi::exceptionBlock_strategy)
@settings(max_examples=50)
def test_delphi::exceptionblock_instantiation(instance):
    assert isinstance(instance, delphi::exceptionBlock)

@given(instance=delphi::qualId_strategy)
@settings(max_examples=50)
def test_delphi::qualid_instantiation(instance):
    assert isinstance(instance, delphi::qualId)

@given(instance=loopStmt_strategy)
@settings(max_examples=50)
def test_loopstmt_instantiation(instance):
    assert isinstance(instance, loopStmt)

@given(instance=delphi::forStmt_strategy)
@settings(max_examples=50)
def test_delphi::forstmt_instantiation(instance):
    assert isinstance(instance, delphi::forStmt)

@given(instance=delphi::whileStmt_strategy)
@settings(max_examples=50)
def test_delphi::whilestmt_instantiation(instance):
    assert isinstance(instance, delphi::whileStmt)

@given(instance=delphi::repeatStmt_strategy)
@settings(max_examples=50)
def test_delphi::repeatstmt_instantiation(instance):
    assert isinstance(instance, delphi::repeatStmt)

@given(instance=delphi::stmtList_strategy)
@settings(max_examples=50)
def test_delphi::stmtlist_instantiation(instance):
    assert isinstance(instance, delphi::stmtList)

@given(instance=delphi::caseLabel_strategy)
@settings(max_examples=50)
def test_delphi::caselabel_instantiation(instance):
    assert isinstance(instance, delphi::caseLabel)

@given(instance=delphi::caseSelector_strategy)
@settings(max_examples=50)
def test_delphi::caseselector_instantiation(instance):
    assert isinstance(instance, delphi::caseSelector)

@given(instance=conditionalStmt_strategy)
@settings(max_examples=50)
def test_conditionalstmt_instantiation(instance):
    assert isinstance(instance, conditionalStmt)

@given(instance=delphi::caseStmt_strategy)
@settings(max_examples=50)
def test_delphi::casestmt_instantiation(instance):
    assert isinstance(instance, delphi::caseStmt)

@given(instance=delphi::ifStmt_strategy)
@settings(max_examples=50)
def test_delphi::ifstmt_instantiation(instance):
    assert isinstance(instance, delphi::ifStmt)

@given(instance=structStmt_strategy)
@settings(max_examples=50)
def test_structstmt_instantiation(instance):
    assert isinstance(instance, structStmt)

@given(instance=delphi::loopStmt_strategy)
@settings(max_examples=50)
def test_delphi::loopstmt_instantiation(instance):
    assert isinstance(instance, delphi::loopStmt)

@given(instance=delphi::conditionalStmt_strategy)
@settings(max_examples=50)
def test_delphi::conditionalstmt_instantiation(instance):
    assert isinstance(instance, delphi::conditionalStmt)

@given(instance=delphi::tryStmt_strategy)
@settings(max_examples=50)
def test_delphi::trystmt_instantiation(instance):
    assert isinstance(instance, delphi::tryStmt)

@given(instance=delphi::withStmt_strategy)
@settings(max_examples=50)
def test_delphi::withstmt_instantiation(instance):
    assert isinstance(instance, delphi::withStmt)

@given(instance=delphi::raiseStmt_strategy)
@settings(max_examples=50)
def test_delphi::raisestmt_instantiation(instance):
    assert isinstance(instance, delphi::raiseStmt)

@given(instance=delphi::raiseStmt_strategy)
def test_delphi::raisestmt_at_type(instance):
    assert isinstance(instance.at, str)


@given(instance=delphi::raiseStmt_strategy)
def test_delphi::raisestmt_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=delphi::raiseStmt_strategy)
def test_delphi::raisestmt_raise__type(instance):
    assert isinstance(instance.raise_, str)


@given(instance=delphi::raiseStmt_strategy)
def test_delphi::raisestmt_raise__setter(instance):
    original = instance.raise_
    instance.raise_ = original
    assert instance.raise_ == original

@given(instance=delphi::compoundStmt_strategy)
@settings(max_examples=50)
def test_delphi::compoundstmt_instantiation(instance):
    assert isinstance(instance, delphi::compoundStmt)

@given(instance=delphi::assemblerStmt_strategy)
@settings(max_examples=50)
def test_delphi::assemblerstmt_instantiation(instance):
    assert isinstance(instance, delphi::assemblerStmt)

@given(instance=unlabelledStatement_strategy)
@settings(max_examples=50)
def test_unlabelledstatement_instantiation(instance):
    assert isinstance(instance, unlabelledStatement)

@given(instance=delphi::structStmt_strategy)
@settings(max_examples=50)
def test_delphi::structstmt_instantiation(instance):
    assert isinstance(instance, delphi::structStmt)

@given(instance=delphi::simpleStatement_strategy)
@settings(max_examples=50)
def test_delphi::simplestatement_instantiation(instance):
    assert isinstance(instance, delphi::simpleStatement)

@given(instance=delphi::unlabelledStatement_strategy)
@settings(max_examples=50)
def test_delphi::unlabelledstatement_instantiation(instance):
    assert isinstance(instance, delphi::unlabelledStatement)

@given(instance=delphi::statement_strategy)
@settings(max_examples=50)
def test_delphi::statement_instantiation(instance):
    assert isinstance(instance, delphi::statement)

@given(instance=delphi::statement_strategy)
def test_delphi::statement_labelId_type(instance):
    assert isinstance(instance.labelId, str)


@given(instance=delphi::statement_strategy)
def test_delphi::statement_labelId_setter(instance):
    original = instance.labelId
    instance.labelId = original
    assert instance.labelId == original

@given(instance=delphi::setConstructor_strategy)
@settings(max_examples=50)
def test_delphi::setconstructor_instantiation(instance):
    assert isinstance(instance, delphi::setConstructor)

@given(instance=delphi::setElement_strategy)
@settings(max_examples=50)
def test_delphi::setelement_instantiation(instance):
    assert isinstance(instance, delphi::setElement)

@given(instance=delphi::reservedWord_strategy)
@settings(max_examples=50)
def test_delphi::reservedword_instantiation(instance):
    assert isinstance(instance, delphi::reservedWord)

@given(instance=delphi::reservedWord_strategy)
def test_delphi::reservedword_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=delphi::reservedWord_strategy)
def test_delphi::reservedword_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi::designatorPart_strategy)
@settings(max_examples=50)
def test_delphi::designatorpart_instantiation(instance):
    assert isinstance(instance, delphi::designatorPart)

@given(instance=delphi::designatorPart_strategy)
def test_delphi::designatorpart_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=delphi::designatorPart_strategy)
def test_delphi::designatorpart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi::designatorPart_strategy)
def test_delphi::designatorpart_id2_type(instance):
    assert isinstance(instance.id2, str)


@given(instance=delphi::designatorPart_strategy)
def test_delphi::designatorpart_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original

@given(instance=delphi::designatorSubPart_strategy)
@settings(max_examples=50)
def test_delphi::designatorsubpart_instantiation(instance):
    assert isinstance(instance, delphi::designatorSubPart)

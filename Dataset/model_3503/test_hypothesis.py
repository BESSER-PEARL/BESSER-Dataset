import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleStatement,
    delphi_callStmnt,
    delphi_assignmentStmnt,
    addOp,
    delphi_adOp,
    factor,
    delphi_simpleFactor,
    pointerType,
    classHeritage,
    objFieldList,
    restrictedType,
    delphi_interfaceType,
    delphi_classType,
    delphi_objectType,
    methodHeading,
    delphi_constructorHeading,
    delphi_destructorHeading,
    procedureDeclSection,
    delphi_functionDecl,
    delphi_procedureDecl,
    loopStmt,
    delphi_forStmt,
    delphi_whileStmt,
    delphi_repeatStmt,
    conditionalStmt,
    delphi_caseStmt,
    delphi_ifStmt,
    structStmt,
    delphi_tryStmt,
    delphi_assemblerStmt,
    delphi_withStmt,
    delphi_raiseStmt,
    delphi_loopStmt,
    delphi_conditionalStmt,
    unlabelledStatement,
    delphi_structStmt,
    delphi_simpleStatement,
    term,
    delphi_multExp,
    delphi_factor,
    simpleExpression,
    delphi_addExp,
    delphi_term,
    expression,
    delphi_relExp,
    delphi_simpleExpression,
    strucType,
    delphi_recType,
    delphi_fileType,
    delphi_setType,
    delphi_arrayType,
    ordinalType,
    delphi_enumeratedType,
    delphi_subrangeType,
    delphi_ordIdent,
    simpleType,
    delphi_ordinalType,
    delphi_realType,
    type,
    delphi_procedureType,
    delphi_stringType,
    delphi_variantType,
    delphi_pointerType,
    delphi_simpleType,
    delphi_strucType,
    delphi_classRefType,
    delphi_typeId,
    delphi_procedureHeading,
    interfaceDecl,
    delphi_exportedHeading,
    declSection,
    delphi_constSection,
    delphi_procedureDeclSection,
    delphi_typeSection,
    delphi_varSection,
    delphi_labelDeclSection,
    delphi_compoundStmt,
    delphi_functionHeading,
    delphi_identList,
    file,
    delphi_library,
    delphi_packageDecl,
    delphi_unit,
    delphi_program,
    CSTrace,
    delphi_classFieldList,
    delphi_ident,
    delphi_block,
    delphi_propertyInterface,
    delphi_typedConstant,
    delphi_usesClause,
    delphi_objFieldList,
    delphi_recordConstExpr,
    delphi_reservedWord,
    delphi_file,
    delphi_caseLabel,
    delphi_exprList,
    delphi_type,
    delphi_propertyList,
    delphi_recordConstant,
    delphi_classProperty,
    delphi_varDecl,
    delphi_parameter,
    delphi_interfaceHeritage,
    delphi_formalParameters,
    delphi_statement,
    delphi_declSection,
    delphi_designator,
    delphi_enumeratedTypeElement,
    delphi_designatorSubPart,
    delphi_initSection,
    delphi_caseSelector,
    delphi_variantSection,
    delphi_mulOp,
    delphi_designatorPart,
    delphi_restrictedType,
    delphi_exportsStmt,
    delphi_arrayConstant,
    delphi_requiresClause,
    delphi_setConstructor,
    delphi_recordFieldConstant,
    delphi_constantDecl,
    delphi_implementationSection,
    delphi_fieldList,
    delphi_unlabelledStatement,
    delphi_methodHeading,
    delphi_classMethod,
    delphi_objHeritage,
    delphi_constExpr,
    delphi_recVariant,
    delphi_classField,
    delphi_classMethodList,
    delphi_unitId,
    delphi_programBlock,
    delphi_exportsItem,
    delphi_classHeritage,
    delphi_setElement,
    delphi_propertySpecifiers,
    delphi_interfaceDecl,
    delphi_qualId,
    delphi_directive,
    delphi_typeDecl,
    delphi_fieldDecl,
    delphi_classPropertyList,
    delphi_interfaceSection,
    delphi_propertyParameterList,
    delphi_formalParm,
    delphi_stmtList,
    delphi_relOp,
    delphi_methodList,
    delphi_expression,
    delphi_exceptionBlock,
    delphi_containsClause,
    delphi_addOp,
    delphi_mainRule,
    delphi_inheritedStamnt,
    delphi_Visitable,
    delphi_CSTrace,
    constExpr,
    delphi_MultipleConstExp,
    delphi_RecordConstExp,
    delphi_ConstExp,
    ident,
    delphi_MineID,
    delphi_ReservedId,
    delphi_MultipleId,
    parameter,
    delphi_parameterSimple,
    delphi_parameterList,
    delphi_gotoStmnt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(simpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(simpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(simpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi_callstmnt_is_not_abstract():
    assert not inspect.isabstract(delphi_callStmnt)


def test_delphi_callstmnt_constructor_exists():
    assert callable(delphi_callStmnt.__init__)


def test_delphi_callstmnt_constructor_args():
    sig = inspect.signature(delphi_callStmnt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_assignmentstmnt_is_not_abstract():
    assert not inspect.isabstract(delphi_assignmentStmnt)


def test_delphi_assignmentstmnt_constructor_exists():
    assert callable(delphi_assignmentStmnt.__init__)


def test_delphi_assignmentstmnt_constructor_args():
    sig = inspect.signature(delphi_assignmentStmnt.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_delphi_assignmentstmnt_has_operator():
    assert hasattr(delphi_assignmentStmnt, "operator")
    descriptor = None
    for klass in delphi_assignmentStmnt.__mro__:
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



def test_delphi_adop_is_not_abstract():
    assert not inspect.isabstract(delphi_adOp)


def test_delphi_adop_constructor_exists():
    assert callable(delphi_adOp.__init__)


def test_delphi_adop_constructor_args():
    sig = inspect.signature(delphi_adOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi_adop_has_op():
    assert hasattr(delphi_adOp, "op")
    descriptor = None
    for klass in delphi_adOp.__mro__:
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



def test_delphi_simplefactor_is_not_abstract():
    assert not inspect.isabstract(delphi_simpleFactor)


def test_delphi_simplefactor_constructor_exists():
    assert callable(delphi_simpleFactor.__init__)


def test_delphi_simplefactor_constructor_args():
    sig = inspect.signature(delphi_simpleFactor.__init__)
    params = list(sig.parameters.keys())



def test_pointertype_is_not_abstract():
    assert not inspect.isabstract(pointerType)


def test_pointertype_constructor_exists():
    assert callable(pointerType.__init__)


def test_pointertype_constructor_args():
    sig = inspect.signature(pointerType.__init__)
    params = list(sig.parameters.keys())



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



def test_restrictedtype_is_not_abstract():
    assert not inspect.isabstract(restrictedType)


def test_restrictedtype_constructor_exists():
    assert callable(restrictedType.__init__)


def test_restrictedtype_constructor_args():
    sig = inspect.signature(restrictedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_interfacetype_is_not_abstract():
    assert not inspect.isabstract(delphi_interfaceType)


def test_delphi_interfacetype_constructor_exists():
    assert callable(delphi_interfaceType.__init__)


def test_delphi_interfacetype_constructor_args():
    sig = inspect.signature(delphi_interfaceType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classtype_is_not_abstract():
    assert not inspect.isabstract(delphi_classType)


def test_delphi_classtype_constructor_exists():
    assert callable(delphi_classType.__init__)


def test_delphi_classtype_constructor_args():
    sig = inspect.signature(delphi_classType.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi_classtype_has_visibility():
    assert hasattr(delphi_classType, "visibility")
    descriptor = None
    for klass in delphi_classType.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi_objecttype_is_not_abstract():
    assert not inspect.isabstract(delphi_objectType)


def test_delphi_objecttype_constructor_exists():
    assert callable(delphi_objectType.__init__)


def test_delphi_objecttype_constructor_args():
    sig = inspect.signature(delphi_objectType.__init__)
    params = list(sig.parameters.keys())



def test_methodheading_is_not_abstract():
    assert not inspect.isabstract(methodHeading)


def test_methodheading_constructor_exists():
    assert callable(methodHeading.__init__)


def test_methodheading_constructor_args():
    sig = inspect.signature(methodHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi_constructorheading_is_not_abstract():
    assert not inspect.isabstract(delphi_constructorHeading)


def test_delphi_constructorheading_constructor_exists():
    assert callable(delphi_constructorHeading.__init__)


def test_delphi_constructorheading_constructor_args():
    sig = inspect.signature(delphi_constructorHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi_destructorheading_is_not_abstract():
    assert not inspect.isabstract(delphi_destructorHeading)


def test_delphi_destructorheading_constructor_exists():
    assert callable(delphi_destructorHeading.__init__)


def test_delphi_destructorheading_constructor_args():
    sig = inspect.signature(delphi_destructorHeading.__init__)
    params = list(sig.parameters.keys())



def test_proceduredeclsection_is_not_abstract():
    assert not inspect.isabstract(procedureDeclSection)


def test_proceduredeclsection_constructor_exists():
    assert callable(procedureDeclSection.__init__)


def test_proceduredeclsection_constructor_args():
    sig = inspect.signature(procedureDeclSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_functiondecl_is_not_abstract():
    assert not inspect.isabstract(delphi_functionDecl)


def test_delphi_functiondecl_constructor_exists():
    assert callable(delphi_functionDecl.__init__)


def test_delphi_functiondecl_constructor_args():
    sig = inspect.signature(delphi_functionDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi_proceduredecl_is_not_abstract():
    assert not inspect.isabstract(delphi_procedureDecl)


def test_delphi_proceduredecl_constructor_exists():
    assert callable(delphi_procedureDecl.__init__)


def test_delphi_proceduredecl_constructor_args():
    sig = inspect.signature(delphi_procedureDecl.__init__)
    params = list(sig.parameters.keys())



def test_loopstmt_is_not_abstract():
    assert not inspect.isabstract(loopStmt)


def test_loopstmt_constructor_exists():
    assert callable(loopStmt.__init__)


def test_loopstmt_constructor_args():
    sig = inspect.signature(loopStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_forstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_forStmt)


def test_delphi_forstmt_constructor_exists():
    assert callable(delphi_forStmt.__init__)


def test_delphi_forstmt_constructor_args():
    sig = inspect.signature(delphi_forStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_whilestmt_is_not_abstract():
    assert not inspect.isabstract(delphi_whileStmt)


def test_delphi_whilestmt_constructor_exists():
    assert callable(delphi_whileStmt.__init__)


def test_delphi_whilestmt_constructor_args():
    sig = inspect.signature(delphi_whileStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_repeatstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_repeatStmt)


def test_delphi_repeatstmt_constructor_exists():
    assert callable(delphi_repeatStmt.__init__)


def test_delphi_repeatstmt_constructor_args():
    sig = inspect.signature(delphi_repeatStmt.__init__)
    params = list(sig.parameters.keys())



def test_conditionalstmt_is_not_abstract():
    assert not inspect.isabstract(conditionalStmt)


def test_conditionalstmt_constructor_exists():
    assert callable(conditionalStmt.__init__)


def test_conditionalstmt_constructor_args():
    sig = inspect.signature(conditionalStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_casestmt_is_not_abstract():
    assert not inspect.isabstract(delphi_caseStmt)


def test_delphi_casestmt_constructor_exists():
    assert callable(delphi_caseStmt.__init__)


def test_delphi_casestmt_constructor_args():
    sig = inspect.signature(delphi_caseStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_ifstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_ifStmt)


def test_delphi_ifstmt_constructor_exists():
    assert callable(delphi_ifStmt.__init__)


def test_delphi_ifstmt_constructor_args():
    sig = inspect.signature(delphi_ifStmt.__init__)
    params = list(sig.parameters.keys())



def test_structstmt_is_not_abstract():
    assert not inspect.isabstract(structStmt)


def test_structstmt_constructor_exists():
    assert callable(structStmt.__init__)


def test_structstmt_constructor_args():
    sig = inspect.signature(structStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_trystmt_is_not_abstract():
    assert not inspect.isabstract(delphi_tryStmt)


def test_delphi_trystmt_constructor_exists():
    assert callable(delphi_tryStmt.__init__)


def test_delphi_trystmt_constructor_args():
    sig = inspect.signature(delphi_tryStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_assemblerstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_assemblerStmt)


def test_delphi_assemblerstmt_constructor_exists():
    assert callable(delphi_assemblerStmt.__init__)


def test_delphi_assemblerstmt_constructor_args():
    sig = inspect.signature(delphi_assemblerStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_withstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_withStmt)


def test_delphi_withstmt_constructor_exists():
    assert callable(delphi_withStmt.__init__)


def test_delphi_withstmt_constructor_args():
    sig = inspect.signature(delphi_withStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_raisestmt_is_not_abstract():
    assert not inspect.isabstract(delphi_raiseStmt)


def test_delphi_raisestmt_constructor_exists():
    assert callable(delphi_raiseStmt.__init__)


def test_delphi_raisestmt_constructor_args():
    sig = inspect.signature(delphi_raiseStmt.__init__)
    params = list(sig.parameters.keys())
    assert "raise_" in params, "Missing parameter 'raise_'"
    assert "at" in params, "Missing parameter 'at'"

def test_delphi_raisestmt_has_raise_():
    assert hasattr(delphi_raiseStmt, "raise_")
    descriptor = None
    for klass in delphi_raiseStmt.__mro__:
        if "raise_" in klass.__dict__:
            descriptor = klass.__dict__["raise_"]
            break
    assert isinstance(descriptor, property)

def test_delphi_raisestmt_has_at():
    assert hasattr(delphi_raiseStmt, "at")
    descriptor = None
    for klass in delphi_raiseStmt.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)



def test_delphi_loopstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_loopStmt)


def test_delphi_loopstmt_constructor_exists():
    assert callable(delphi_loopStmt.__init__)


def test_delphi_loopstmt_constructor_args():
    sig = inspect.signature(delphi_loopStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_conditionalstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_conditionalStmt)


def test_delphi_conditionalstmt_constructor_exists():
    assert callable(delphi_conditionalStmt.__init__)


def test_delphi_conditionalstmt_constructor_args():
    sig = inspect.signature(delphi_conditionalStmt.__init__)
    params = list(sig.parameters.keys())



def test_unlabelledstatement_is_not_abstract():
    assert not inspect.isabstract(unlabelledStatement)


def test_unlabelledstatement_constructor_exists():
    assert callable(unlabelledStatement.__init__)


def test_unlabelledstatement_constructor_args():
    sig = inspect.signature(unlabelledStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi_structstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_structStmt)


def test_delphi_structstmt_constructor_exists():
    assert callable(delphi_structStmt.__init__)


def test_delphi_structstmt_constructor_args():
    sig = inspect.signature(delphi_structStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_simplestatement_is_not_abstract():
    assert not inspect.isabstract(delphi_simpleStatement)


def test_delphi_simplestatement_constructor_exists():
    assert callable(delphi_simpleStatement.__init__)


def test_delphi_simplestatement_constructor_args():
    sig = inspect.signature(delphi_simpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(term)


def test_term_constructor_exists():
    assert callable(term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(term.__init__)
    params = list(sig.parameters.keys())



def test_delphi_multexp_is_not_abstract():
    assert not inspect.isabstract(delphi_multExp)


def test_delphi_multexp_constructor_exists():
    assert callable(delphi_multExp.__init__)


def test_delphi_multexp_constructor_args():
    sig = inspect.signature(delphi_multExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_factor_is_not_abstract():
    assert not inspect.isabstract(delphi_factor)


def test_delphi_factor_constructor_exists():
    assert callable(delphi_factor.__init__)


def test_delphi_factor_constructor_args():
    sig = inspect.signature(delphi_factor.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "string" in params, "Missing parameter 'string'"

def test_delphi_factor_has_number():
    assert hasattr(delphi_factor, "number")
    descriptor = None
    for klass in delphi_factor.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_delphi_factor_has_string():
    assert hasattr(delphi_factor, "string")
    descriptor = None
    for klass in delphi_factor.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(simpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(simpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(simpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_delphi_addexp_is_not_abstract():
    assert not inspect.isabstract(delphi_addExp)


def test_delphi_addexp_constructor_exists():
    assert callable(delphi_addExp.__init__)


def test_delphi_addexp_constructor_args():
    sig = inspect.signature(delphi_addExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_term_is_not_abstract():
    assert not inspect.isabstract(delphi_term)


def test_delphi_term_constructor_exists():
    assert callable(delphi_term.__init__)


def test_delphi_term_constructor_args():
    sig = inspect.signature(delphi_term.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(expression)


def test_expression_constructor_exists():
    assert callable(expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(expression.__init__)
    params = list(sig.parameters.keys())



def test_delphi_relexp_is_not_abstract():
    assert not inspect.isabstract(delphi_relExp)


def test_delphi_relexp_constructor_exists():
    assert callable(delphi_relExp.__init__)


def test_delphi_relexp_constructor_args():
    sig = inspect.signature(delphi_relExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(delphi_simpleExpression)


def test_delphi_simpleexpression_constructor_exists():
    assert callable(delphi_simpleExpression.__init__)


def test_delphi_simpleexpression_constructor_args():
    sig = inspect.signature(delphi_simpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_structype_is_not_abstract():
    assert not inspect.isabstract(strucType)


def test_structype_constructor_exists():
    assert callable(strucType.__init__)


def test_structype_constructor_args():
    sig = inspect.signature(strucType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_rectype_is_not_abstract():
    assert not inspect.isabstract(delphi_recType)


def test_delphi_rectype_constructor_exists():
    assert callable(delphi_recType.__init__)


def test_delphi_rectype_constructor_args():
    sig = inspect.signature(delphi_recType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_filetype_is_not_abstract():
    assert not inspect.isabstract(delphi_fileType)


def test_delphi_filetype_constructor_exists():
    assert callable(delphi_fileType.__init__)


def test_delphi_filetype_constructor_args():
    sig = inspect.signature(delphi_fileType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_settype_is_not_abstract():
    assert not inspect.isabstract(delphi_setType)


def test_delphi_settype_constructor_exists():
    assert callable(delphi_setType.__init__)


def test_delphi_settype_constructor_args():
    sig = inspect.signature(delphi_setType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_arraytype_is_not_abstract():
    assert not inspect.isabstract(delphi_arrayType)


def test_delphi_arraytype_constructor_exists():
    assert callable(delphi_arrayType.__init__)


def test_delphi_arraytype_constructor_args():
    sig = inspect.signature(delphi_arrayType.__init__)
    params = list(sig.parameters.keys())



def test_ordinaltype_is_not_abstract():
    assert not inspect.isabstract(ordinalType)


def test_ordinaltype_constructor_exists():
    assert callable(ordinalType.__init__)


def test_ordinaltype_constructor_args():
    sig = inspect.signature(ordinalType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_enumeratedtype_is_not_abstract():
    assert not inspect.isabstract(delphi_enumeratedType)


def test_delphi_enumeratedtype_constructor_exists():
    assert callable(delphi_enumeratedType.__init__)


def test_delphi_enumeratedtype_constructor_args():
    sig = inspect.signature(delphi_enumeratedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_subrangetype_is_not_abstract():
    assert not inspect.isabstract(delphi_subrangeType)


def test_delphi_subrangetype_constructor_exists():
    assert callable(delphi_subrangeType.__init__)


def test_delphi_subrangetype_constructor_args():
    sig = inspect.signature(delphi_subrangeType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_ordident_is_not_abstract():
    assert not inspect.isabstract(delphi_ordIdent)


def test_delphi_ordident_constructor_exists():
    assert callable(delphi_ordIdent.__init__)


def test_delphi_ordident_constructor_args():
    sig = inspect.signature(delphi_ordIdent.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(simpleType)


def test_simpletype_constructor_exists():
    assert callable(simpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(simpleType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_ordinaltype_is_not_abstract():
    assert not inspect.isabstract(delphi_ordinalType)


def test_delphi_ordinaltype_constructor_exists():
    assert callable(delphi_ordinalType.__init__)


def test_delphi_ordinaltype_constructor_args():
    sig = inspect.signature(delphi_ordinalType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_realtype_is_not_abstract():
    assert not inspect.isabstract(delphi_realType)


def test_delphi_realtype_constructor_exists():
    assert callable(delphi_realType.__init__)


def test_delphi_realtype_constructor_args():
    sig = inspect.signature(delphi_realType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(type)


def test_type_constructor_exists():
    assert callable(type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(type.__init__)
    params = list(sig.parameters.keys())



def test_delphi_proceduretype_is_not_abstract():
    assert not inspect.isabstract(delphi_procedureType)


def test_delphi_proceduretype_constructor_exists():
    assert callable(delphi_procedureType.__init__)


def test_delphi_proceduretype_constructor_args():
    sig = inspect.signature(delphi_procedureType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_stringtype_is_not_abstract():
    assert not inspect.isabstract(delphi_stringType)


def test_delphi_stringtype_constructor_exists():
    assert callable(delphi_stringType.__init__)


def test_delphi_stringtype_constructor_args():
    sig = inspect.signature(delphi_stringType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_varianttype_is_not_abstract():
    assert not inspect.isabstract(delphi_variantType)


def test_delphi_varianttype_constructor_exists():
    assert callable(delphi_variantType.__init__)


def test_delphi_varianttype_constructor_args():
    sig = inspect.signature(delphi_variantType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_pointertype_is_not_abstract():
    assert not inspect.isabstract(delphi_pointerType)


def test_delphi_pointertype_constructor_exists():
    assert callable(delphi_pointerType.__init__)


def test_delphi_pointertype_constructor_args():
    sig = inspect.signature(delphi_pointerType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_simpletype_is_not_abstract():
    assert not inspect.isabstract(delphi_simpleType)


def test_delphi_simpletype_constructor_exists():
    assert callable(delphi_simpleType.__init__)


def test_delphi_simpletype_constructor_args():
    sig = inspect.signature(delphi_simpleType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_structype_is_not_abstract():
    assert not inspect.isabstract(delphi_strucType)


def test_delphi_structype_constructor_exists():
    assert callable(delphi_strucType.__init__)


def test_delphi_structype_constructor_args():
    sig = inspect.signature(delphi_strucType.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_structype_has_port():
    assert hasattr(delphi_strucType, "port")
    descriptor = None
    for klass in delphi_strucType.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_classreftype_is_not_abstract():
    assert not inspect.isabstract(delphi_classRefType)


def test_delphi_classreftype_constructor_exists():
    assert callable(delphi_classRefType.__init__)


def test_delphi_classreftype_constructor_args():
    sig = inspect.signature(delphi_classRefType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_typeid_is_not_abstract():
    assert not inspect.isabstract(delphi_typeId)


def test_delphi_typeid_constructor_exists():
    assert callable(delphi_typeId.__init__)


def test_delphi_typeid_constructor_args():
    sig = inspect.signature(delphi_typeId.__init__)
    params = list(sig.parameters.keys())



def test_delphi_procedureheading_is_not_abstract():
    assert not inspect.isabstract(delphi_procedureHeading)


def test_delphi_procedureheading_constructor_exists():
    assert callable(delphi_procedureHeading.__init__)


def test_delphi_procedureheading_constructor_args():
    sig = inspect.signature(delphi_procedureHeading.__init__)
    params = list(sig.parameters.keys())



def test_interfacedecl_is_not_abstract():
    assert not inspect.isabstract(interfaceDecl)


def test_interfacedecl_constructor_exists():
    assert callable(interfaceDecl.__init__)


def test_interfacedecl_constructor_args():
    sig = inspect.signature(interfaceDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi_exportedheading_is_not_abstract():
    assert not inspect.isabstract(delphi_exportedHeading)


def test_delphi_exportedheading_constructor_exists():
    assert callable(delphi_exportedHeading.__init__)


def test_delphi_exportedheading_constructor_args():
    sig = inspect.signature(delphi_exportedHeading.__init__)
    params = list(sig.parameters.keys())



def test_declsection_is_not_abstract():
    assert not inspect.isabstract(declSection)


def test_declsection_constructor_exists():
    assert callable(declSection.__init__)


def test_declsection_constructor_args():
    sig = inspect.signature(declSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_constsection_is_not_abstract():
    assert not inspect.isabstract(delphi_constSection)


def test_delphi_constsection_constructor_exists():
    assert callable(delphi_constSection.__init__)


def test_delphi_constsection_constructor_args():
    sig = inspect.signature(delphi_constSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_proceduredeclsection_is_not_abstract():
    assert not inspect.isabstract(delphi_procedureDeclSection)


def test_delphi_proceduredeclsection_constructor_exists():
    assert callable(delphi_procedureDeclSection.__init__)


def test_delphi_proceduredeclsection_constructor_args():
    sig = inspect.signature(delphi_procedureDeclSection.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_proceduredeclsection_has_port():
    assert hasattr(delphi_procedureDeclSection, "port")
    descriptor = None
    for klass in delphi_procedureDeclSection.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_typesection_is_not_abstract():
    assert not inspect.isabstract(delphi_typeSection)


def test_delphi_typesection_constructor_exists():
    assert callable(delphi_typeSection.__init__)


def test_delphi_typesection_constructor_args():
    sig = inspect.signature(delphi_typeSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_varsection_is_not_abstract():
    assert not inspect.isabstract(delphi_varSection)


def test_delphi_varsection_constructor_exists():
    assert callable(delphi_varSection.__init__)


def test_delphi_varsection_constructor_args():
    sig = inspect.signature(delphi_varSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_labeldeclsection_is_not_abstract():
    assert not inspect.isabstract(delphi_labelDeclSection)


def test_delphi_labeldeclsection_constructor_exists():
    assert callable(delphi_labelDeclSection.__init__)


def test_delphi_labeldeclsection_constructor_args():
    sig = inspect.signature(delphi_labelDeclSection.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi_labeldeclsection_has_id():
    assert hasattr(delphi_labelDeclSection, "id")
    descriptor = None
    for klass in delphi_labelDeclSection.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_delphi_compoundstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_compoundStmt)


def test_delphi_compoundstmt_constructor_exists():
    assert callable(delphi_compoundStmt.__init__)


def test_delphi_compoundstmt_constructor_args():
    sig = inspect.signature(delphi_compoundStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_functionheading_is_not_abstract():
    assert not inspect.isabstract(delphi_functionHeading)


def test_delphi_functionheading_constructor_exists():
    assert callable(delphi_functionHeading.__init__)


def test_delphi_functionheading_constructor_args():
    sig = inspect.signature(delphi_functionHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi_identlist_is_not_abstract():
    assert not inspect.isabstract(delphi_identList)


def test_delphi_identlist_constructor_exists():
    assert callable(delphi_identList.__init__)


def test_delphi_identlist_constructor_args():
    sig = inspect.signature(delphi_identList.__init__)
    params = list(sig.parameters.keys())



def test_file_is_not_abstract():
    assert not inspect.isabstract(file)


def test_file_constructor_exists():
    assert callable(file.__init__)


def test_file_constructor_args():
    sig = inspect.signature(file.__init__)
    params = list(sig.parameters.keys())



def test_delphi_library_is_not_abstract():
    assert not inspect.isabstract(delphi_library)


def test_delphi_library_constructor_exists():
    assert callable(delphi_library.__init__)


def test_delphi_library_constructor_args():
    sig = inspect.signature(delphi_library.__init__)
    params = list(sig.parameters.keys())



def test_delphi_packagedecl_is_not_abstract():
    assert not inspect.isabstract(delphi_packageDecl)


def test_delphi_packagedecl_constructor_exists():
    assert callable(delphi_packageDecl.__init__)


def test_delphi_packagedecl_constructor_args():
    sig = inspect.signature(delphi_packageDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi_unit_is_not_abstract():
    assert not inspect.isabstract(delphi_unit)


def test_delphi_unit_constructor_exists():
    assert callable(delphi_unit.__init__)


def test_delphi_unit_constructor_args():
    sig = inspect.signature(delphi_unit.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_unit_has_port():
    assert hasattr(delphi_unit, "port")
    descriptor = None
    for klass in delphi_unit.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_program_is_not_abstract():
    assert not inspect.isabstract(delphi_program)


def test_delphi_program_constructor_exists():
    assert callable(delphi_program.__init__)


def test_delphi_program_constructor_args():
    sig = inspect.signature(delphi_program.__init__)
    params = list(sig.parameters.keys())



def test_cstrace_is_not_abstract():
    assert not inspect.isabstract(CSTrace)


def test_cstrace_constructor_exists():
    assert callable(CSTrace.__init__)


def test_cstrace_constructor_args():
    sig = inspect.signature(CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classfieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi_classFieldList)


def test_delphi_classfieldlist_constructor_exists():
    assert callable(delphi_classFieldList.__init__)


def test_delphi_classfieldlist_constructor_args():
    sig = inspect.signature(delphi_classFieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_ident_is_not_abstract():
    assert not inspect.isabstract(delphi_ident)


def test_delphi_ident_constructor_exists():
    assert callable(delphi_ident.__init__)


def test_delphi_ident_constructor_args():
    sig = inspect.signature(delphi_ident.__init__)
    params = list(sig.parameters.keys())



def test_delphi_block_is_not_abstract():
    assert not inspect.isabstract(delphi_block)


def test_delphi_block_constructor_exists():
    assert callable(delphi_block.__init__)


def test_delphi_block_constructor_args():
    sig = inspect.signature(delphi_block.__init__)
    params = list(sig.parameters.keys())



def test_delphi_propertyinterface_is_not_abstract():
    assert not inspect.isabstract(delphi_propertyInterface)


def test_delphi_propertyinterface_constructor_exists():
    assert callable(delphi_propertyInterface.__init__)


def test_delphi_propertyinterface_constructor_args():
    sig = inspect.signature(delphi_propertyInterface.__init__)
    params = list(sig.parameters.keys())



def test_delphi_typedconstant_is_not_abstract():
    assert not inspect.isabstract(delphi_typedConstant)


def test_delphi_typedconstant_constructor_exists():
    assert callable(delphi_typedConstant.__init__)


def test_delphi_typedconstant_constructor_args():
    sig = inspect.signature(delphi_typedConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi_usesclause_is_not_abstract():
    assert not inspect.isabstract(delphi_usesClause)


def test_delphi_usesclause_constructor_exists():
    assert callable(delphi_usesClause.__init__)


def test_delphi_usesclause_constructor_args():
    sig = inspect.signature(delphi_usesClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi_objfieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi_objFieldList)


def test_delphi_objfieldlist_constructor_exists():
    assert callable(delphi_objFieldList.__init__)


def test_delphi_objfieldlist_constructor_args():
    sig = inspect.signature(delphi_objFieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_recordconstexpr_is_not_abstract():
    assert not inspect.isabstract(delphi_recordConstExpr)


def test_delphi_recordconstexpr_constructor_exists():
    assert callable(delphi_recordConstExpr.__init__)


def test_delphi_recordconstexpr_constructor_args():
    sig = inspect.signature(delphi_recordConstExpr.__init__)
    params = list(sig.parameters.keys())



def test_delphi_reservedword_is_not_abstract():
    assert not inspect.isabstract(delphi_reservedWord)


def test_delphi_reservedword_constructor_exists():
    assert callable(delphi_reservedWord.__init__)


def test_delphi_reservedword_constructor_args():
    sig = inspect.signature(delphi_reservedWord.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi_reservedword_has_id():
    assert hasattr(delphi_reservedWord, "id")
    descriptor = None
    for klass in delphi_reservedWord.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_delphi_file_is_not_abstract():
    assert not inspect.isabstract(delphi_file)


def test_delphi_file_constructor_exists():
    assert callable(delphi_file.__init__)


def test_delphi_file_constructor_args():
    sig = inspect.signature(delphi_file.__init__)
    params = list(sig.parameters.keys())



def test_delphi_caselabel_is_not_abstract():
    assert not inspect.isabstract(delphi_caseLabel)


def test_delphi_caselabel_constructor_exists():
    assert callable(delphi_caseLabel.__init__)


def test_delphi_caselabel_constructor_args():
    sig = inspect.signature(delphi_caseLabel.__init__)
    params = list(sig.parameters.keys())



def test_delphi_exprlist_is_not_abstract():
    assert not inspect.isabstract(delphi_exprList)


def test_delphi_exprlist_constructor_exists():
    assert callable(delphi_exprList.__init__)


def test_delphi_exprlist_constructor_args():
    sig = inspect.signature(delphi_exprList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_type_is_not_abstract():
    assert not inspect.isabstract(delphi_type)


def test_delphi_type_constructor_exists():
    assert callable(delphi_type.__init__)


def test_delphi_type_constructor_args():
    sig = inspect.signature(delphi_type.__init__)
    params = list(sig.parameters.keys())



def test_delphi_propertylist_is_not_abstract():
    assert not inspect.isabstract(delphi_propertyList)


def test_delphi_propertylist_constructor_exists():
    assert callable(delphi_propertyList.__init__)


def test_delphi_propertylist_constructor_args():
    sig = inspect.signature(delphi_propertyList.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_propertylist_has_port():
    assert hasattr(delphi_propertyList, "port")
    descriptor = None
    for klass in delphi_propertyList.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_recordconstant_is_not_abstract():
    assert not inspect.isabstract(delphi_recordConstant)


def test_delphi_recordconstant_constructor_exists():
    assert callable(delphi_recordConstant.__init__)


def test_delphi_recordconstant_constructor_args():
    sig = inspect.signature(delphi_recordConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classproperty_is_not_abstract():
    assert not inspect.isabstract(delphi_classProperty)


def test_delphi_classproperty_constructor_exists():
    assert callable(delphi_classProperty.__init__)


def test_delphi_classproperty_constructor_args():
    sig = inspect.signature(delphi_classProperty.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi_classproperty_has_visibility():
    assert hasattr(delphi_classProperty, "visibility")
    descriptor = None
    for klass in delphi_classProperty.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi_vardecl_is_not_abstract():
    assert not inspect.isabstract(delphi_varDecl)


def test_delphi_vardecl_constructor_exists():
    assert callable(delphi_varDecl.__init__)


def test_delphi_vardecl_constructor_args():
    sig = inspect.signature(delphi_varDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi_parameter_is_not_abstract():
    assert not inspect.isabstract(delphi_parameter)


def test_delphi_parameter_constructor_exists():
    assert callable(delphi_parameter.__init__)


def test_delphi_parameter_constructor_args():
    sig = inspect.signature(delphi_parameter.__init__)
    params = list(sig.parameters.keys())



def test_delphi_interfaceheritage_is_not_abstract():
    assert not inspect.isabstract(delphi_interfaceHeritage)


def test_delphi_interfaceheritage_constructor_exists():
    assert callable(delphi_interfaceHeritage.__init__)


def test_delphi_interfaceheritage_constructor_args():
    sig = inspect.signature(delphi_interfaceHeritage.__init__)
    params = list(sig.parameters.keys())



def test_delphi_formalparameters_is_not_abstract():
    assert not inspect.isabstract(delphi_formalParameters)


def test_delphi_formalparameters_constructor_exists():
    assert callable(delphi_formalParameters.__init__)


def test_delphi_formalparameters_constructor_args():
    sig = inspect.signature(delphi_formalParameters.__init__)
    params = list(sig.parameters.keys())



def test_delphi_statement_is_not_abstract():
    assert not inspect.isabstract(delphi_statement)


def test_delphi_statement_constructor_exists():
    assert callable(delphi_statement.__init__)


def test_delphi_statement_constructor_args():
    sig = inspect.signature(delphi_statement.__init__)
    params = list(sig.parameters.keys())
    assert "labelId" in params, "Missing parameter 'labelId'"

def test_delphi_statement_has_labelId():
    assert hasattr(delphi_statement, "labelId")
    descriptor = None
    for klass in delphi_statement.__mro__:
        if "labelId" in klass.__dict__:
            descriptor = klass.__dict__["labelId"]
            break
    assert isinstance(descriptor, property)



def test_delphi_declsection_is_not_abstract():
    assert not inspect.isabstract(delphi_declSection)


def test_delphi_declsection_constructor_exists():
    assert callable(delphi_declSection.__init__)


def test_delphi_declsection_constructor_args():
    sig = inspect.signature(delphi_declSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_designator_is_not_abstract():
    assert not inspect.isabstract(delphi_designator)


def test_delphi_designator_constructor_exists():
    assert callable(delphi_designator.__init__)


def test_delphi_designator_constructor_args():
    sig = inspect.signature(delphi_designator.__init__)
    params = list(sig.parameters.keys())



def test_delphi_enumeratedtypeelement_is_not_abstract():
    assert not inspect.isabstract(delphi_enumeratedTypeElement)


def test_delphi_enumeratedtypeelement_constructor_exists():
    assert callable(delphi_enumeratedTypeElement.__init__)


def test_delphi_enumeratedtypeelement_constructor_args():
    sig = inspect.signature(delphi_enumeratedTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_delphi_designatorsubpart_is_not_abstract():
    assert not inspect.isabstract(delphi_designatorSubPart)


def test_delphi_designatorsubpart_constructor_exists():
    assert callable(delphi_designatorSubPart.__init__)


def test_delphi_designatorsubpart_constructor_args():
    sig = inspect.signature(delphi_designatorSubPart.__init__)
    params = list(sig.parameters.keys())



def test_delphi_initsection_is_not_abstract():
    assert not inspect.isabstract(delphi_initSection)


def test_delphi_initsection_constructor_exists():
    assert callable(delphi_initSection.__init__)


def test_delphi_initsection_constructor_args():
    sig = inspect.signature(delphi_initSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_caseselector_is_not_abstract():
    assert not inspect.isabstract(delphi_caseSelector)


def test_delphi_caseselector_constructor_exists():
    assert callable(delphi_caseSelector.__init__)


def test_delphi_caseselector_constructor_args():
    sig = inspect.signature(delphi_caseSelector.__init__)
    params = list(sig.parameters.keys())



def test_delphi_variantsection_is_not_abstract():
    assert not inspect.isabstract(delphi_variantSection)


def test_delphi_variantsection_constructor_exists():
    assert callable(delphi_variantSection.__init__)


def test_delphi_variantsection_constructor_args():
    sig = inspect.signature(delphi_variantSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_mulop_is_not_abstract():
    assert not inspect.isabstract(delphi_mulOp)


def test_delphi_mulop_constructor_exists():
    assert callable(delphi_mulOp.__init__)


def test_delphi_mulop_constructor_args():
    sig = inspect.signature(delphi_mulOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi_mulop_has_op():
    assert hasattr(delphi_mulOp, "op")
    descriptor = None
    for klass in delphi_mulOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_delphi_designatorpart_is_not_abstract():
    assert not inspect.isabstract(delphi_designatorPart)


def test_delphi_designatorpart_constructor_exists():
    assert callable(delphi_designatorPart.__init__)


def test_delphi_designatorpart_constructor_args():
    sig = inspect.signature(delphi_designatorPart.__init__)
    params = list(sig.parameters.keys())
    assert "id2" in params, "Missing parameter 'id2'"
    assert "id" in params, "Missing parameter 'id'"

def test_delphi_designatorpart_has_id2():
    assert hasattr(delphi_designatorPart, "id2")
    descriptor = None
    for klass in delphi_designatorPart.__mro__:
        if "id2" in klass.__dict__:
            descriptor = klass.__dict__["id2"]
            break
    assert isinstance(descriptor, property)

def test_delphi_designatorpart_has_id():
    assert hasattr(delphi_designatorPart, "id")
    descriptor = None
    for klass in delphi_designatorPart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_delphi_restrictedtype_is_not_abstract():
    assert not inspect.isabstract(delphi_restrictedType)


def test_delphi_restrictedtype_constructor_exists():
    assert callable(delphi_restrictedType.__init__)


def test_delphi_restrictedtype_constructor_args():
    sig = inspect.signature(delphi_restrictedType.__init__)
    params = list(sig.parameters.keys())



def test_delphi_exportsstmt_is_not_abstract():
    assert not inspect.isabstract(delphi_exportsStmt)


def test_delphi_exportsstmt_constructor_exists():
    assert callable(delphi_exportsStmt.__init__)


def test_delphi_exportsstmt_constructor_args():
    sig = inspect.signature(delphi_exportsStmt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_arrayconstant_is_not_abstract():
    assert not inspect.isabstract(delphi_arrayConstant)


def test_delphi_arrayconstant_constructor_exists():
    assert callable(delphi_arrayConstant.__init__)


def test_delphi_arrayconstant_constructor_args():
    sig = inspect.signature(delphi_arrayConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi_requiresclause_is_not_abstract():
    assert not inspect.isabstract(delphi_requiresClause)


def test_delphi_requiresclause_constructor_exists():
    assert callable(delphi_requiresClause.__init__)


def test_delphi_requiresclause_constructor_args():
    sig = inspect.signature(delphi_requiresClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi_setconstructor_is_not_abstract():
    assert not inspect.isabstract(delphi_setConstructor)


def test_delphi_setconstructor_constructor_exists():
    assert callable(delphi_setConstructor.__init__)


def test_delphi_setconstructor_constructor_args():
    sig = inspect.signature(delphi_setConstructor.__init__)
    params = list(sig.parameters.keys())



def test_delphi_recordfieldconstant_is_not_abstract():
    assert not inspect.isabstract(delphi_recordFieldConstant)


def test_delphi_recordfieldconstant_constructor_exists():
    assert callable(delphi_recordFieldConstant.__init__)


def test_delphi_recordfieldconstant_constructor_args():
    sig = inspect.signature(delphi_recordFieldConstant.__init__)
    params = list(sig.parameters.keys())



def test_delphi_constantdecl_is_not_abstract():
    assert not inspect.isabstract(delphi_constantDecl)


def test_delphi_constantdecl_constructor_exists():
    assert callable(delphi_constantDecl.__init__)


def test_delphi_constantdecl_constructor_args():
    sig = inspect.signature(delphi_constantDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_constantdecl_has_port():
    assert hasattr(delphi_constantDecl, "port")
    descriptor = None
    for klass in delphi_constantDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_implementationsection_is_not_abstract():
    assert not inspect.isabstract(delphi_implementationSection)


def test_delphi_implementationsection_constructor_exists():
    assert callable(delphi_implementationSection.__init__)


def test_delphi_implementationsection_constructor_args():
    sig = inspect.signature(delphi_implementationSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_fieldlist_is_not_abstract():
    assert not inspect.isabstract(delphi_fieldList)


def test_delphi_fieldlist_constructor_exists():
    assert callable(delphi_fieldList.__init__)


def test_delphi_fieldlist_constructor_args():
    sig = inspect.signature(delphi_fieldList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_unlabelledstatement_is_not_abstract():
    assert not inspect.isabstract(delphi_unlabelledStatement)


def test_delphi_unlabelledstatement_constructor_exists():
    assert callable(delphi_unlabelledStatement.__init__)


def test_delphi_unlabelledstatement_constructor_args():
    sig = inspect.signature(delphi_unlabelledStatement.__init__)
    params = list(sig.parameters.keys())



def test_delphi_methodheading_is_not_abstract():
    assert not inspect.isabstract(delphi_methodHeading)


def test_delphi_methodheading_constructor_exists():
    assert callable(delphi_methodHeading.__init__)


def test_delphi_methodheading_constructor_args():
    sig = inspect.signature(delphi_methodHeading.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classmethod_is_not_abstract():
    assert not inspect.isabstract(delphi_classMethod)


def test_delphi_classmethod_constructor_exists():
    assert callable(delphi_classMethod.__init__)


def test_delphi_classmethod_constructor_args():
    sig = inspect.signature(delphi_classMethod.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi_classmethod_has_visibility():
    assert hasattr(delphi_classMethod, "visibility")
    descriptor = None
    for klass in delphi_classMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi_objheritage_is_not_abstract():
    assert not inspect.isabstract(delphi_objHeritage)


def test_delphi_objheritage_constructor_exists():
    assert callable(delphi_objHeritage.__init__)


def test_delphi_objheritage_constructor_args():
    sig = inspect.signature(delphi_objHeritage.__init__)
    params = list(sig.parameters.keys())



def test_delphi_constexpr_is_not_abstract():
    assert not inspect.isabstract(delphi_constExpr)


def test_delphi_constexpr_constructor_exists():
    assert callable(delphi_constExpr.__init__)


def test_delphi_constexpr_constructor_args():
    sig = inspect.signature(delphi_constExpr.__init__)
    params = list(sig.parameters.keys())



def test_delphi_recvariant_is_not_abstract():
    assert not inspect.isabstract(delphi_recVariant)


def test_delphi_recvariant_constructor_exists():
    assert callable(delphi_recVariant.__init__)


def test_delphi_recvariant_constructor_args():
    sig = inspect.signature(delphi_recVariant.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classfield_is_not_abstract():
    assert not inspect.isabstract(delphi_classField)


def test_delphi_classfield_constructor_exists():
    assert callable(delphi_classField.__init__)


def test_delphi_classfield_constructor_args():
    sig = inspect.signature(delphi_classField.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_delphi_classfield_has_visibility():
    assert hasattr(delphi_classField, "visibility")
    descriptor = None
    for klass in delphi_classField.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_delphi_classmethodlist_is_not_abstract():
    assert not inspect.isabstract(delphi_classMethodList)


def test_delphi_classmethodlist_constructor_exists():
    assert callable(delphi_classMethodList.__init__)


def test_delphi_classmethodlist_constructor_args():
    sig = inspect.signature(delphi_classMethodList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_unitid_is_not_abstract():
    assert not inspect.isabstract(delphi_unitId)


def test_delphi_unitid_constructor_exists():
    assert callable(delphi_unitId.__init__)


def test_delphi_unitid_constructor_args():
    sig = inspect.signature(delphi_unitId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi_unitid_has_id():
    assert hasattr(delphi_unitId, "id")
    descriptor = None
    for klass in delphi_unitId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_delphi_programblock_is_not_abstract():
    assert not inspect.isabstract(delphi_programBlock)


def test_delphi_programblock_constructor_exists():
    assert callable(delphi_programBlock.__init__)


def test_delphi_programblock_constructor_args():
    sig = inspect.signature(delphi_programBlock.__init__)
    params = list(sig.parameters.keys())



def test_delphi_exportsitem_is_not_abstract():
    assert not inspect.isabstract(delphi_exportsItem)


def test_delphi_exportsitem_constructor_exists():
    assert callable(delphi_exportsItem.__init__)


def test_delphi_exportsitem_constructor_args():
    sig = inspect.signature(delphi_exportsItem.__init__)
    params = list(sig.parameters.keys())



def test_delphi_classheritage_is_not_abstract():
    assert not inspect.isabstract(delphi_classHeritage)


def test_delphi_classheritage_constructor_exists():
    assert callable(delphi_classHeritage.__init__)


def test_delphi_classheritage_constructor_args():
    sig = inspect.signature(delphi_classHeritage.__init__)
    params = list(sig.parameters.keys())



def test_delphi_setelement_is_not_abstract():
    assert not inspect.isabstract(delphi_setElement)


def test_delphi_setelement_constructor_exists():
    assert callable(delphi_setElement.__init__)


def test_delphi_setelement_constructor_args():
    sig = inspect.signature(delphi_setElement.__init__)
    params = list(sig.parameters.keys())



def test_delphi_propertyspecifiers_is_not_abstract():
    assert not inspect.isabstract(delphi_propertySpecifiers)


def test_delphi_propertyspecifiers_constructor_exists():
    assert callable(delphi_propertySpecifiers.__init__)


def test_delphi_propertyspecifiers_constructor_args():
    sig = inspect.signature(delphi_propertySpecifiers.__init__)
    params = list(sig.parameters.keys())



def test_delphi_interfacedecl_is_not_abstract():
    assert not inspect.isabstract(delphi_interfaceDecl)


def test_delphi_interfacedecl_constructor_exists():
    assert callable(delphi_interfaceDecl.__init__)


def test_delphi_interfacedecl_constructor_args():
    sig = inspect.signature(delphi_interfaceDecl.__init__)
    params = list(sig.parameters.keys())



def test_delphi_qualid_is_not_abstract():
    assert not inspect.isabstract(delphi_qualId)


def test_delphi_qualid_constructor_exists():
    assert callable(delphi_qualId.__init__)


def test_delphi_qualid_constructor_args():
    sig = inspect.signature(delphi_qualId.__init__)
    params = list(sig.parameters.keys())



def test_delphi_directive_is_not_abstract():
    assert not inspect.isabstract(delphi_directive)


def test_delphi_directive_constructor_exists():
    assert callable(delphi_directive.__init__)


def test_delphi_directive_constructor_args():
    sig = inspect.signature(delphi_directive.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_delphi_directive_has_dir():
    assert hasattr(delphi_directive, "dir")
    descriptor = None
    for klass in delphi_directive.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_delphi_typedecl_is_not_abstract():
    assert not inspect.isabstract(delphi_typeDecl)


def test_delphi_typedecl_constructor_exists():
    assert callable(delphi_typeDecl.__init__)


def test_delphi_typedecl_constructor_args():
    sig = inspect.signature(delphi_typeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_typedecl_has_port():
    assert hasattr(delphi_typeDecl, "port")
    descriptor = None
    for klass in delphi_typeDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_fielddecl_is_not_abstract():
    assert not inspect.isabstract(delphi_fieldDecl)


def test_delphi_fielddecl_constructor_exists():
    assert callable(delphi_fieldDecl.__init__)


def test_delphi_fielddecl_constructor_args():
    sig = inspect.signature(delphi_fieldDecl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_delphi_fielddecl_has_port():
    assert hasattr(delphi_fieldDecl, "port")
    descriptor = None
    for klass in delphi_fieldDecl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_delphi_classpropertylist_is_not_abstract():
    assert not inspect.isabstract(delphi_classPropertyList)


def test_delphi_classpropertylist_constructor_exists():
    assert callable(delphi_classPropertyList.__init__)


def test_delphi_classpropertylist_constructor_args():
    sig = inspect.signature(delphi_classPropertyList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_interfacesection_is_not_abstract():
    assert not inspect.isabstract(delphi_interfaceSection)


def test_delphi_interfacesection_constructor_exists():
    assert callable(delphi_interfaceSection.__init__)


def test_delphi_interfacesection_constructor_args():
    sig = inspect.signature(delphi_interfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_delphi_propertyparameterlist_is_not_abstract():
    assert not inspect.isabstract(delphi_propertyParameterList)


def test_delphi_propertyparameterlist_constructor_exists():
    assert callable(delphi_propertyParameterList.__init__)


def test_delphi_propertyparameterlist_constructor_args():
    sig = inspect.signature(delphi_propertyParameterList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_formalparm_is_not_abstract():
    assert not inspect.isabstract(delphi_formalParm)


def test_delphi_formalparm_constructor_exists():
    assert callable(delphi_formalParm.__init__)


def test_delphi_formalparm_constructor_args():
    sig = inspect.signature(delphi_formalParm.__init__)
    params = list(sig.parameters.keys())



def test_delphi_stmtlist_is_not_abstract():
    assert not inspect.isabstract(delphi_stmtList)


def test_delphi_stmtlist_constructor_exists():
    assert callable(delphi_stmtList.__init__)


def test_delphi_stmtlist_constructor_args():
    sig = inspect.signature(delphi_stmtList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_relop_is_not_abstract():
    assert not inspect.isabstract(delphi_relOp)


def test_delphi_relop_constructor_exists():
    assert callable(delphi_relOp.__init__)


def test_delphi_relop_constructor_args():
    sig = inspect.signature(delphi_relOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_delphi_relop_has_op():
    assert hasattr(delphi_relOp, "op")
    descriptor = None
    for klass in delphi_relOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_delphi_methodlist_is_not_abstract():
    assert not inspect.isabstract(delphi_methodList)


def test_delphi_methodlist_constructor_exists():
    assert callable(delphi_methodList.__init__)


def test_delphi_methodlist_constructor_args():
    sig = inspect.signature(delphi_methodList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_expression_is_not_abstract():
    assert not inspect.isabstract(delphi_expression)


def test_delphi_expression_constructor_exists():
    assert callable(delphi_expression.__init__)


def test_delphi_expression_constructor_args():
    sig = inspect.signature(delphi_expression.__init__)
    params = list(sig.parameters.keys())



def test_delphi_exceptionblock_is_not_abstract():
    assert not inspect.isabstract(delphi_exceptionBlock)


def test_delphi_exceptionblock_constructor_exists():
    assert callable(delphi_exceptionBlock.__init__)


def test_delphi_exceptionblock_constructor_args():
    sig = inspect.signature(delphi_exceptionBlock.__init__)
    params = list(sig.parameters.keys())



def test_delphi_containsclause_is_not_abstract():
    assert not inspect.isabstract(delphi_containsClause)


def test_delphi_containsclause_constructor_exists():
    assert callable(delphi_containsClause.__init__)


def test_delphi_containsclause_constructor_args():
    sig = inspect.signature(delphi_containsClause.__init__)
    params = list(sig.parameters.keys())



def test_delphi_addop_is_not_abstract():
    assert not inspect.isabstract(delphi_addOp)


def test_delphi_addop_constructor_exists():
    assert callable(delphi_addOp.__init__)


def test_delphi_addop_constructor_args():
    sig = inspect.signature(delphi_addOp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_mainrule_is_not_abstract():
    assert not inspect.isabstract(delphi_mainRule)


def test_delphi_mainrule_constructor_exists():
    assert callable(delphi_mainRule.__init__)


def test_delphi_mainrule_constructor_args():
    sig = inspect.signature(delphi_mainRule.__init__)
    params = list(sig.parameters.keys())



def test_delphi_inheritedstamnt_is_not_abstract():
    assert not inspect.isabstract(delphi_inheritedStamnt)


def test_delphi_inheritedstamnt_constructor_exists():
    assert callable(delphi_inheritedStamnt.__init__)


def test_delphi_inheritedstamnt_constructor_args():
    sig = inspect.signature(delphi_inheritedStamnt.__init__)
    params = list(sig.parameters.keys())



def test_delphi_visitable_is_not_abstract():
    assert not inspect.isabstract(delphi_Visitable)


def test_delphi_visitable_constructor_exists():
    assert callable(delphi_Visitable.__init__)


def test_delphi_visitable_constructor_args():
    sig = inspect.signature(delphi_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_delphi_cstrace_is_not_abstract():
    assert not inspect.isabstract(delphi_CSTrace)


def test_delphi_cstrace_constructor_exists():
    assert callable(delphi_CSTrace.__init__)


def test_delphi_cstrace_constructor_args():
    sig = inspect.signature(delphi_CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_constexpr_is_not_abstract():
    assert not inspect.isabstract(constExpr)


def test_constexpr_constructor_exists():
    assert callable(constExpr.__init__)


def test_constexpr_constructor_args():
    sig = inspect.signature(constExpr.__init__)
    params = list(sig.parameters.keys())



def test_delphi_multipleconstexp_is_not_abstract():
    assert not inspect.isabstract(delphi_MultipleConstExp)


def test_delphi_multipleconstexp_constructor_exists():
    assert callable(delphi_MultipleConstExp.__init__)


def test_delphi_multipleconstexp_constructor_args():
    sig = inspect.signature(delphi_MultipleConstExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_recordconstexp_is_not_abstract():
    assert not inspect.isabstract(delphi_RecordConstExp)


def test_delphi_recordconstexp_constructor_exists():
    assert callable(delphi_RecordConstExp.__init__)


def test_delphi_recordconstexp_constructor_args():
    sig = inspect.signature(delphi_RecordConstExp.__init__)
    params = list(sig.parameters.keys())



def test_delphi_constexp_is_not_abstract():
    assert not inspect.isabstract(delphi_ConstExp)


def test_delphi_constexp_constructor_exists():
    assert callable(delphi_ConstExp.__init__)


def test_delphi_constexp_constructor_args():
    sig = inspect.signature(delphi_ConstExp.__init__)
    params = list(sig.parameters.keys())



def test_ident_is_not_abstract():
    assert not inspect.isabstract(ident)


def test_ident_constructor_exists():
    assert callable(ident.__init__)


def test_ident_constructor_args():
    sig = inspect.signature(ident.__init__)
    params = list(sig.parameters.keys())



def test_delphi_mineid_is_not_abstract():
    assert not inspect.isabstract(delphi_MineID)


def test_delphi_mineid_constructor_exists():
    assert callable(delphi_MineID.__init__)


def test_delphi_mineid_constructor_args():
    sig = inspect.signature(delphi_MineID.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"
    assert "second" in params, "Missing parameter 'second'"

def test_delphi_mineid_has_first():
    assert hasattr(delphi_MineID, "first")
    descriptor = None
    for klass in delphi_MineID.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_delphi_mineid_has_second():
    assert hasattr(delphi_MineID, "second")
    descriptor = None
    for klass in delphi_MineID.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)



def test_delphi_reservedid_is_not_abstract():
    assert not inspect.isabstract(delphi_ReservedId)


def test_delphi_reservedid_constructor_exists():
    assert callable(delphi_ReservedId.__init__)


def test_delphi_reservedid_constructor_args():
    sig = inspect.signature(delphi_ReservedId.__init__)
    params = list(sig.parameters.keys())



def test_delphi_multipleid_is_not_abstract():
    assert not inspect.isabstract(delphi_MultipleId)


def test_delphi_multipleid_constructor_exists():
    assert callable(delphi_MultipleId.__init__)


def test_delphi_multipleid_constructor_args():
    sig = inspect.signature(delphi_MultipleId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_delphi_multipleid_has_id():
    assert hasattr(delphi_MultipleId, "id")
    descriptor = None
    for klass in delphi_MultipleId.__mro__:
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



def test_delphi_parametersimple_is_not_abstract():
    assert not inspect.isabstract(delphi_parameterSimple)


def test_delphi_parametersimple_constructor_exists():
    assert callable(delphi_parameterSimple.__init__)


def test_delphi_parametersimple_constructor_args():
    sig = inspect.signature(delphi_parameterSimple.__init__)
    params = list(sig.parameters.keys())



def test_delphi_parameterlist_is_not_abstract():
    assert not inspect.isabstract(delphi_parameterList)


def test_delphi_parameterlist_constructor_exists():
    assert callable(delphi_parameterList.__init__)


def test_delphi_parameterlist_constructor_args():
    sig = inspect.signature(delphi_parameterList.__init__)
    params = list(sig.parameters.keys())



def test_delphi_gotostmnt_is_not_abstract():
    assert not inspect.isabstract(delphi_gotoStmnt)


def test_delphi_gotostmnt_constructor_exists():
    assert callable(delphi_gotoStmnt.__init__)


def test_delphi_gotostmnt_constructor_args():
    sig = inspect.signature(delphi_gotoStmnt.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_delphi_gotostmnt_has_label():
    assert hasattr(delphi_gotoStmnt, "label")
    descriptor = None
    for klass in delphi_gotoStmnt.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)


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
simpleStatement_strategy = st.builds(
    simpleStatement,
)
delphi_callStmnt_strategy = st.builds(
    delphi_callStmnt,
)
delphi_assignmentStmnt_strategy = st.builds(
    delphi_assignmentStmnt,
    operator=
        safe_text
)
addOp_strategy = st.builds(
    addOp,
)
delphi_adOp_strategy = st.builds(
    delphi_adOp,
    op=
        safe_text
)
factor_strategy = st.builds(
    factor,
)
delphi_simpleFactor_strategy = st.builds(
    delphi_simpleFactor,
)
pointerType_strategy = st.builds(
    pointerType,
)
classHeritage_strategy = st.builds(
    classHeritage,
)
objFieldList_strategy = st.builds(
    objFieldList,
)
restrictedType_strategy = st.builds(
    restrictedType,
)
delphi_interfaceType_strategy = st.builds(
    delphi_interfaceType,
)
delphi_classType_strategy = st.builds(
    delphi_classType,
    visibility=
        safe_text
)
delphi_objectType_strategy = st.builds(
    delphi_objectType,
)
methodHeading_strategy = st.builds(
    methodHeading,
)
delphi_constructorHeading_strategy = st.builds(
    delphi_constructorHeading,
)
delphi_destructorHeading_strategy = st.builds(
    delphi_destructorHeading,
)
procedureDeclSection_strategy = st.builds(
    procedureDeclSection,
)
delphi_functionDecl_strategy = st.builds(
    delphi_functionDecl,
)
delphi_procedureDecl_strategy = st.builds(
    delphi_procedureDecl,
)
loopStmt_strategy = st.builds(
    loopStmt,
)
delphi_forStmt_strategy = st.builds(
    delphi_forStmt,
)
delphi_whileStmt_strategy = st.builds(
    delphi_whileStmt,
)
delphi_repeatStmt_strategy = st.builds(
    delphi_repeatStmt,
)
conditionalStmt_strategy = st.builds(
    conditionalStmt,
)
delphi_caseStmt_strategy = st.builds(
    delphi_caseStmt,
)
delphi_ifStmt_strategy = st.builds(
    delphi_ifStmt,
)
structStmt_strategy = st.builds(
    structStmt,
)
delphi_tryStmt_strategy = st.builds(
    delphi_tryStmt,
)
delphi_assemblerStmt_strategy = st.builds(
    delphi_assemblerStmt,
)
delphi_withStmt_strategy = st.builds(
    delphi_withStmt,
)
delphi_raiseStmt_strategy = st.builds(
    delphi_raiseStmt,
    raise_=
        safe_text,
    at=
        safe_text
)
delphi_loopStmt_strategy = st.builds(
    delphi_loopStmt,
)
delphi_conditionalStmt_strategy = st.builds(
    delphi_conditionalStmt,
)
unlabelledStatement_strategy = st.builds(
    unlabelledStatement,
)
delphi_structStmt_strategy = st.builds(
    delphi_structStmt,
)
delphi_simpleStatement_strategy = st.builds(
    delphi_simpleStatement,
)
term_strategy = st.builds(
    term,
)
delphi_multExp_strategy = st.builds(
    delphi_multExp,
)
delphi_factor_strategy = st.builds(
    delphi_factor,
    number=
        safe_text,
    string=
        safe_text
)
simpleExpression_strategy = st.builds(
    simpleExpression,
)
delphi_addExp_strategy = st.builds(
    delphi_addExp,
)
delphi_term_strategy = st.builds(
    delphi_term,
)
expression_strategy = st.builds(
    expression,
)
delphi_relExp_strategy = st.builds(
    delphi_relExp,
)
delphi_simpleExpression_strategy = st.builds(
    delphi_simpleExpression,
)
strucType_strategy = st.builds(
    strucType,
)
delphi_recType_strategy = st.builds(
    delphi_recType,
)
delphi_fileType_strategy = st.builds(
    delphi_fileType,
)
delphi_setType_strategy = st.builds(
    delphi_setType,
)
delphi_arrayType_strategy = st.builds(
    delphi_arrayType,
)
ordinalType_strategy = st.builds(
    ordinalType,
)
delphi_enumeratedType_strategy = st.builds(
    delphi_enumeratedType,
)
delphi_subrangeType_strategy = st.builds(
    delphi_subrangeType,
)
delphi_ordIdent_strategy = st.builds(
    delphi_ordIdent,
)
simpleType_strategy = st.builds(
    simpleType,
)
delphi_ordinalType_strategy = st.builds(
    delphi_ordinalType,
)
delphi_realType_strategy = st.builds(
    delphi_realType,
)
type_strategy = st.builds(
    type,
)
delphi_procedureType_strategy = st.builds(
    delphi_procedureType,
)
delphi_stringType_strategy = st.builds(
    delphi_stringType,
)
delphi_variantType_strategy = st.builds(
    delphi_variantType,
)
delphi_pointerType_strategy = st.builds(
    delphi_pointerType,
)
delphi_simpleType_strategy = st.builds(
    delphi_simpleType,
)
delphi_strucType_strategy = st.builds(
    delphi_strucType,
    port=
        safe_text
)
delphi_classRefType_strategy = st.builds(
    delphi_classRefType,
)
delphi_typeId_strategy = st.builds(
    delphi_typeId,
)
delphi_procedureHeading_strategy = st.builds(
    delphi_procedureHeading,
)
interfaceDecl_strategy = st.builds(
    interfaceDecl,
)
delphi_exportedHeading_strategy = st.builds(
    delphi_exportedHeading,
)
declSection_strategy = st.builds(
    declSection,
)
delphi_constSection_strategy = st.builds(
    delphi_constSection,
)
delphi_procedureDeclSection_strategy = st.builds(
    delphi_procedureDeclSection,
    port=
        safe_text
)
delphi_typeSection_strategy = st.builds(
    delphi_typeSection,
)
delphi_varSection_strategy = st.builds(
    delphi_varSection,
)
delphi_labelDeclSection_strategy = st.builds(
    delphi_labelDeclSection,
    id=
        safe_text
)
delphi_compoundStmt_strategy = st.builds(
    delphi_compoundStmt,
)
delphi_functionHeading_strategy = st.builds(
    delphi_functionHeading,
)
delphi_identList_strategy = st.builds(
    delphi_identList,
)
file_strategy = st.builds(
    file,
)
delphi_library_strategy = st.builds(
    delphi_library,
)
delphi_packageDecl_strategy = st.builds(
    delphi_packageDecl,
)
delphi_unit_strategy = st.builds(
    delphi_unit,
    port=
        safe_text
)
delphi_program_strategy = st.builds(
    delphi_program,
)
CSTrace_strategy = st.builds(
    CSTrace,
)
delphi_classFieldList_strategy = st.builds(
    delphi_classFieldList,
)
delphi_ident_strategy = st.builds(
    delphi_ident,
)
delphi_block_strategy = st.builds(
    delphi_block,
)
delphi_propertyInterface_strategy = st.builds(
    delphi_propertyInterface,
)
delphi_typedConstant_strategy = st.builds(
    delphi_typedConstant,
)
delphi_usesClause_strategy = st.builds(
    delphi_usesClause,
)
delphi_objFieldList_strategy = st.builds(
    delphi_objFieldList,
)
delphi_recordConstExpr_strategy = st.builds(
    delphi_recordConstExpr,
)
delphi_reservedWord_strategy = st.builds(
    delphi_reservedWord,
    id=
        safe_text
)
delphi_file_strategy = st.builds(
    delphi_file,
)
delphi_caseLabel_strategy = st.builds(
    delphi_caseLabel,
)
delphi_exprList_strategy = st.builds(
    delphi_exprList,
)
delphi_type_strategy = st.builds(
    delphi_type,
)
delphi_propertyList_strategy = st.builds(
    delphi_propertyList,
    port=
        safe_text
)
delphi_recordConstant_strategy = st.builds(
    delphi_recordConstant,
)
delphi_classProperty_strategy = st.builds(
    delphi_classProperty,
    visibility=
        safe_text
)
delphi_varDecl_strategy = st.builds(
    delphi_varDecl,
)
delphi_parameter_strategy = st.builds(
    delphi_parameter,
)
delphi_interfaceHeritage_strategy = st.builds(
    delphi_interfaceHeritage,
)
delphi_formalParameters_strategy = st.builds(
    delphi_formalParameters,
)
delphi_statement_strategy = st.builds(
    delphi_statement,
    labelId=
        safe_text
)
delphi_declSection_strategy = st.builds(
    delphi_declSection,
)
delphi_designator_strategy = st.builds(
    delphi_designator,
)
delphi_enumeratedTypeElement_strategy = st.builds(
    delphi_enumeratedTypeElement,
)
delphi_designatorSubPart_strategy = st.builds(
    delphi_designatorSubPart,
)
delphi_initSection_strategy = st.builds(
    delphi_initSection,
)
delphi_caseSelector_strategy = st.builds(
    delphi_caseSelector,
)
delphi_variantSection_strategy = st.builds(
    delphi_variantSection,
)
delphi_mulOp_strategy = st.builds(
    delphi_mulOp,
    op=
        safe_text
)
delphi_designatorPart_strategy = st.builds(
    delphi_designatorPart,
    id2=
        safe_text,
    id=
        safe_text
)
delphi_restrictedType_strategy = st.builds(
    delphi_restrictedType,
)
delphi_exportsStmt_strategy = st.builds(
    delphi_exportsStmt,
)
delphi_arrayConstant_strategy = st.builds(
    delphi_arrayConstant,
)
delphi_requiresClause_strategy = st.builds(
    delphi_requiresClause,
)
delphi_setConstructor_strategy = st.builds(
    delphi_setConstructor,
)
delphi_recordFieldConstant_strategy = st.builds(
    delphi_recordFieldConstant,
)
delphi_constantDecl_strategy = st.builds(
    delphi_constantDecl,
    port=
        safe_text
)
delphi_implementationSection_strategy = st.builds(
    delphi_implementationSection,
)
delphi_fieldList_strategy = st.builds(
    delphi_fieldList,
)
delphi_unlabelledStatement_strategy = st.builds(
    delphi_unlabelledStatement,
)
delphi_methodHeading_strategy = st.builds(
    delphi_methodHeading,
)
delphi_classMethod_strategy = st.builds(
    delphi_classMethod,
    visibility=
        safe_text
)
delphi_objHeritage_strategy = st.builds(
    delphi_objHeritage,
)
delphi_constExpr_strategy = st.builds(
    delphi_constExpr,
)
delphi_recVariant_strategy = st.builds(
    delphi_recVariant,
)
delphi_classField_strategy = st.builds(
    delphi_classField,
    visibility=
        safe_text
)
delphi_classMethodList_strategy = st.builds(
    delphi_classMethodList,
)
delphi_unitId_strategy = st.builds(
    delphi_unitId,
    id=
        safe_text
)
delphi_programBlock_strategy = st.builds(
    delphi_programBlock,
)
delphi_exportsItem_strategy = st.builds(
    delphi_exportsItem,
)
delphi_classHeritage_strategy = st.builds(
    delphi_classHeritage,
)
delphi_setElement_strategy = st.builds(
    delphi_setElement,
)
delphi_propertySpecifiers_strategy = st.builds(
    delphi_propertySpecifiers,
)
delphi_interfaceDecl_strategy = st.builds(
    delphi_interfaceDecl,
)
delphi_qualId_strategy = st.builds(
    delphi_qualId,
)
delphi_directive_strategy = st.builds(
    delphi_directive,
    dir=
        safe_text
)
delphi_typeDecl_strategy = st.builds(
    delphi_typeDecl,
    port=
        safe_text
)
delphi_fieldDecl_strategy = st.builds(
    delphi_fieldDecl,
    port=
        safe_text
)
delphi_classPropertyList_strategy = st.builds(
    delphi_classPropertyList,
)
delphi_interfaceSection_strategy = st.builds(
    delphi_interfaceSection,
)
delphi_propertyParameterList_strategy = st.builds(
    delphi_propertyParameterList,
)
delphi_formalParm_strategy = st.builds(
    delphi_formalParm,
)
delphi_stmtList_strategy = st.builds(
    delphi_stmtList,
)
delphi_relOp_strategy = st.builds(
    delphi_relOp,
    op=
        safe_text
)
delphi_methodList_strategy = st.builds(
    delphi_methodList,
)
delphi_expression_strategy = st.builds(
    delphi_expression,
)
delphi_exceptionBlock_strategy = st.builds(
    delphi_exceptionBlock,
)
delphi_containsClause_strategy = st.builds(
    delphi_containsClause,
)
delphi_addOp_strategy = st.builds(
    delphi_addOp,
)
delphi_mainRule_strategy = st.builds(
    delphi_mainRule,
)
delphi_inheritedStamnt_strategy = st.builds(
    delphi_inheritedStamnt,
)
delphi_Visitable_strategy = st.builds(
    delphi_Visitable,
)
delphi_CSTrace_strategy = st.builds(
    delphi_CSTrace,
)
constExpr_strategy = st.builds(
    constExpr,
)
delphi_MultipleConstExp_strategy = st.builds(
    delphi_MultipleConstExp,
)
delphi_RecordConstExp_strategy = st.builds(
    delphi_RecordConstExp,
)
delphi_ConstExp_strategy = st.builds(
    delphi_ConstExp,
)
ident_strategy = st.builds(
    ident,
)
delphi_MineID_strategy = st.builds(
    delphi_MineID,
    first=
        safe_text,
    second=
        safe_text
)
delphi_ReservedId_strategy = st.builds(
    delphi_ReservedId,
)
delphi_MultipleId_strategy = st.builds(
    delphi_MultipleId,
    id=
        safe_text
)
parameter_strategy = st.builds(
    parameter,
)
delphi_parameterSimple_strategy = st.builds(
    delphi_parameterSimple,
)
delphi_parameterList_strategy = st.builds(
    delphi_parameterList,
)
delphi_gotoStmnt_strategy = st.builds(
    delphi_gotoStmnt,
    label=
        safe_text
)

@given(instance=simpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, simpleStatement)

@given(instance=delphi_callStmnt_strategy)
@settings(max_examples=50)
def test_delphi_callstmnt_instantiation(instance):
    assert isinstance(instance, delphi_callStmnt)

@given(instance=delphi_assignmentStmnt_strategy)
@settings(max_examples=50)
def test_delphi_assignmentstmnt_instantiation(instance):
    assert isinstance(instance, delphi_assignmentStmnt)



@given(instance=delphi_assignmentStmnt_strategy)
def test_delphi_assignmentstmnt_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=addOp_strategy)
@settings(max_examples=50)
def test_addop_instantiation(instance):
    assert isinstance(instance, addOp)

@given(instance=delphi_adOp_strategy)
@settings(max_examples=50)
def test_delphi_adop_instantiation(instance):
    assert isinstance(instance, delphi_adOp)



@given(instance=delphi_adOp_strategy)
def test_delphi_adop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=factor_strategy)
@settings(max_examples=50)
def test_factor_instantiation(instance):
    assert isinstance(instance, factor)

@given(instance=delphi_simpleFactor_strategy)
@settings(max_examples=50)
def test_delphi_simplefactor_instantiation(instance):
    assert isinstance(instance, delphi_simpleFactor)

@given(instance=pointerType_strategy)
@settings(max_examples=50)
def test_pointertype_instantiation(instance):
    assert isinstance(instance, pointerType)

@given(instance=classHeritage_strategy)
@settings(max_examples=50)
def test_classheritage_instantiation(instance):
    assert isinstance(instance, classHeritage)

@given(instance=objFieldList_strategy)
@settings(max_examples=50)
def test_objfieldlist_instantiation(instance):
    assert isinstance(instance, objFieldList)

@given(instance=restrictedType_strategy)
@settings(max_examples=50)
def test_restrictedtype_instantiation(instance):
    assert isinstance(instance, restrictedType)

@given(instance=delphi_interfaceType_strategy)
@settings(max_examples=50)
def test_delphi_interfacetype_instantiation(instance):
    assert isinstance(instance, delphi_interfaceType)

@given(instance=delphi_classType_strategy)
@settings(max_examples=50)
def test_delphi_classtype_instantiation(instance):
    assert isinstance(instance, delphi_classType)



@given(instance=delphi_classType_strategy)
def test_delphi_classtype_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi_objectType_strategy)
@settings(max_examples=50)
def test_delphi_objecttype_instantiation(instance):
    assert isinstance(instance, delphi_objectType)

@given(instance=methodHeading_strategy)
@settings(max_examples=50)
def test_methodheading_instantiation(instance):
    assert isinstance(instance, methodHeading)

@given(instance=delphi_constructorHeading_strategy)
@settings(max_examples=50)
def test_delphi_constructorheading_instantiation(instance):
    assert isinstance(instance, delphi_constructorHeading)

@given(instance=delphi_destructorHeading_strategy)
@settings(max_examples=50)
def test_delphi_destructorheading_instantiation(instance):
    assert isinstance(instance, delphi_destructorHeading)

@given(instance=procedureDeclSection_strategy)
@settings(max_examples=50)
def test_proceduredeclsection_instantiation(instance):
    assert isinstance(instance, procedureDeclSection)

@given(instance=delphi_functionDecl_strategy)
@settings(max_examples=50)
def test_delphi_functiondecl_instantiation(instance):
    assert isinstance(instance, delphi_functionDecl)

@given(instance=delphi_procedureDecl_strategy)
@settings(max_examples=50)
def test_delphi_proceduredecl_instantiation(instance):
    assert isinstance(instance, delphi_procedureDecl)

@given(instance=loopStmt_strategy)
@settings(max_examples=50)
def test_loopstmt_instantiation(instance):
    assert isinstance(instance, loopStmt)

@given(instance=delphi_forStmt_strategy)
@settings(max_examples=50)
def test_delphi_forstmt_instantiation(instance):
    assert isinstance(instance, delphi_forStmt)

@given(instance=delphi_whileStmt_strategy)
@settings(max_examples=50)
def test_delphi_whilestmt_instantiation(instance):
    assert isinstance(instance, delphi_whileStmt)

@given(instance=delphi_repeatStmt_strategy)
@settings(max_examples=50)
def test_delphi_repeatstmt_instantiation(instance):
    assert isinstance(instance, delphi_repeatStmt)

@given(instance=conditionalStmt_strategy)
@settings(max_examples=50)
def test_conditionalstmt_instantiation(instance):
    assert isinstance(instance, conditionalStmt)

@given(instance=delphi_caseStmt_strategy)
@settings(max_examples=50)
def test_delphi_casestmt_instantiation(instance):
    assert isinstance(instance, delphi_caseStmt)

@given(instance=delphi_ifStmt_strategy)
@settings(max_examples=50)
def test_delphi_ifstmt_instantiation(instance):
    assert isinstance(instance, delphi_ifStmt)

@given(instance=structStmt_strategy)
@settings(max_examples=50)
def test_structstmt_instantiation(instance):
    assert isinstance(instance, structStmt)

@given(instance=delphi_tryStmt_strategy)
@settings(max_examples=50)
def test_delphi_trystmt_instantiation(instance):
    assert isinstance(instance, delphi_tryStmt)

@given(instance=delphi_assemblerStmt_strategy)
@settings(max_examples=50)
def test_delphi_assemblerstmt_instantiation(instance):
    assert isinstance(instance, delphi_assemblerStmt)

@given(instance=delphi_withStmt_strategy)
@settings(max_examples=50)
def test_delphi_withstmt_instantiation(instance):
    assert isinstance(instance, delphi_withStmt)

@given(instance=delphi_raiseStmt_strategy)
@settings(max_examples=50)
def test_delphi_raisestmt_instantiation(instance):
    assert isinstance(instance, delphi_raiseStmt)



@given(instance=delphi_raiseStmt_strategy)
def test_delphi_raisestmt_raise__setter(instance):
    original = instance.raise_
    instance.raise_ = original
    assert instance.raise_ == original



@given(instance=delphi_raiseStmt_strategy)
def test_delphi_raisestmt_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=delphi_loopStmt_strategy)
@settings(max_examples=50)
def test_delphi_loopstmt_instantiation(instance):
    assert isinstance(instance, delphi_loopStmt)

@given(instance=delphi_conditionalStmt_strategy)
@settings(max_examples=50)
def test_delphi_conditionalstmt_instantiation(instance):
    assert isinstance(instance, delphi_conditionalStmt)

@given(instance=unlabelledStatement_strategy)
@settings(max_examples=50)
def test_unlabelledstatement_instantiation(instance):
    assert isinstance(instance, unlabelledStatement)

@given(instance=delphi_structStmt_strategy)
@settings(max_examples=50)
def test_delphi_structstmt_instantiation(instance):
    assert isinstance(instance, delphi_structStmt)

@given(instance=delphi_simpleStatement_strategy)
@settings(max_examples=50)
def test_delphi_simplestatement_instantiation(instance):
    assert isinstance(instance, delphi_simpleStatement)

@given(instance=term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, term)

@given(instance=delphi_multExp_strategy)
@settings(max_examples=50)
def test_delphi_multexp_instantiation(instance):
    assert isinstance(instance, delphi_multExp)

@given(instance=delphi_factor_strategy)
@settings(max_examples=50)
def test_delphi_factor_instantiation(instance):
    assert isinstance(instance, delphi_factor)



@given(instance=delphi_factor_strategy)
def test_delphi_factor_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=delphi_factor_strategy)
def test_delphi_factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=simpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, simpleExpression)

@given(instance=delphi_addExp_strategy)
@settings(max_examples=50)
def test_delphi_addexp_instantiation(instance):
    assert isinstance(instance, delphi_addExp)

@given(instance=delphi_term_strategy)
@settings(max_examples=50)
def test_delphi_term_instantiation(instance):
    assert isinstance(instance, delphi_term)

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=delphi_relExp_strategy)
@settings(max_examples=50)
def test_delphi_relexp_instantiation(instance):
    assert isinstance(instance, delphi_relExp)

@given(instance=delphi_simpleExpression_strategy)
@settings(max_examples=50)
def test_delphi_simpleexpression_instantiation(instance):
    assert isinstance(instance, delphi_simpleExpression)

@given(instance=strucType_strategy)
@settings(max_examples=50)
def test_structype_instantiation(instance):
    assert isinstance(instance, strucType)

@given(instance=delphi_recType_strategy)
@settings(max_examples=50)
def test_delphi_rectype_instantiation(instance):
    assert isinstance(instance, delphi_recType)

@given(instance=delphi_fileType_strategy)
@settings(max_examples=50)
def test_delphi_filetype_instantiation(instance):
    assert isinstance(instance, delphi_fileType)

@given(instance=delphi_setType_strategy)
@settings(max_examples=50)
def test_delphi_settype_instantiation(instance):
    assert isinstance(instance, delphi_setType)

@given(instance=delphi_arrayType_strategy)
@settings(max_examples=50)
def test_delphi_arraytype_instantiation(instance):
    assert isinstance(instance, delphi_arrayType)

@given(instance=ordinalType_strategy)
@settings(max_examples=50)
def test_ordinaltype_instantiation(instance):
    assert isinstance(instance, ordinalType)

@given(instance=delphi_enumeratedType_strategy)
@settings(max_examples=50)
def test_delphi_enumeratedtype_instantiation(instance):
    assert isinstance(instance, delphi_enumeratedType)

@given(instance=delphi_subrangeType_strategy)
@settings(max_examples=50)
def test_delphi_subrangetype_instantiation(instance):
    assert isinstance(instance, delphi_subrangeType)

@given(instance=delphi_ordIdent_strategy)
@settings(max_examples=50)
def test_delphi_ordident_instantiation(instance):
    assert isinstance(instance, delphi_ordIdent)

@given(instance=simpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, simpleType)

@given(instance=delphi_ordinalType_strategy)
@settings(max_examples=50)
def test_delphi_ordinaltype_instantiation(instance):
    assert isinstance(instance, delphi_ordinalType)

@given(instance=delphi_realType_strategy)
@settings(max_examples=50)
def test_delphi_realtype_instantiation(instance):
    assert isinstance(instance, delphi_realType)

@given(instance=type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, type)

@given(instance=delphi_procedureType_strategy)
@settings(max_examples=50)
def test_delphi_proceduretype_instantiation(instance):
    assert isinstance(instance, delphi_procedureType)

@given(instance=delphi_stringType_strategy)
@settings(max_examples=50)
def test_delphi_stringtype_instantiation(instance):
    assert isinstance(instance, delphi_stringType)

@given(instance=delphi_variantType_strategy)
@settings(max_examples=50)
def test_delphi_varianttype_instantiation(instance):
    assert isinstance(instance, delphi_variantType)

@given(instance=delphi_pointerType_strategy)
@settings(max_examples=50)
def test_delphi_pointertype_instantiation(instance):
    assert isinstance(instance, delphi_pointerType)

@given(instance=delphi_simpleType_strategy)
@settings(max_examples=50)
def test_delphi_simpletype_instantiation(instance):
    assert isinstance(instance, delphi_simpleType)

@given(instance=delphi_strucType_strategy)
@settings(max_examples=50)
def test_delphi_structype_instantiation(instance):
    assert isinstance(instance, delphi_strucType)



@given(instance=delphi_strucType_strategy)
def test_delphi_structype_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_classRefType_strategy)
@settings(max_examples=50)
def test_delphi_classreftype_instantiation(instance):
    assert isinstance(instance, delphi_classRefType)

@given(instance=delphi_typeId_strategy)
@settings(max_examples=50)
def test_delphi_typeid_instantiation(instance):
    assert isinstance(instance, delphi_typeId)

@given(instance=delphi_procedureHeading_strategy)
@settings(max_examples=50)
def test_delphi_procedureheading_instantiation(instance):
    assert isinstance(instance, delphi_procedureHeading)

@given(instance=interfaceDecl_strategy)
@settings(max_examples=50)
def test_interfacedecl_instantiation(instance):
    assert isinstance(instance, interfaceDecl)

@given(instance=delphi_exportedHeading_strategy)
@settings(max_examples=50)
def test_delphi_exportedheading_instantiation(instance):
    assert isinstance(instance, delphi_exportedHeading)

@given(instance=declSection_strategy)
@settings(max_examples=50)
def test_declsection_instantiation(instance):
    assert isinstance(instance, declSection)

@given(instance=delphi_constSection_strategy)
@settings(max_examples=50)
def test_delphi_constsection_instantiation(instance):
    assert isinstance(instance, delphi_constSection)

@given(instance=delphi_procedureDeclSection_strategy)
@settings(max_examples=50)
def test_delphi_proceduredeclsection_instantiation(instance):
    assert isinstance(instance, delphi_procedureDeclSection)



@given(instance=delphi_procedureDeclSection_strategy)
def test_delphi_proceduredeclsection_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_typeSection_strategy)
@settings(max_examples=50)
def test_delphi_typesection_instantiation(instance):
    assert isinstance(instance, delphi_typeSection)

@given(instance=delphi_varSection_strategy)
@settings(max_examples=50)
def test_delphi_varsection_instantiation(instance):
    assert isinstance(instance, delphi_varSection)

@given(instance=delphi_labelDeclSection_strategy)
@settings(max_examples=50)
def test_delphi_labeldeclsection_instantiation(instance):
    assert isinstance(instance, delphi_labelDeclSection)



@given(instance=delphi_labelDeclSection_strategy)
def test_delphi_labeldeclsection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi_compoundStmt_strategy)
@settings(max_examples=50)
def test_delphi_compoundstmt_instantiation(instance):
    assert isinstance(instance, delphi_compoundStmt)

@given(instance=delphi_functionHeading_strategy)
@settings(max_examples=50)
def test_delphi_functionheading_instantiation(instance):
    assert isinstance(instance, delphi_functionHeading)

@given(instance=delphi_identList_strategy)
@settings(max_examples=50)
def test_delphi_identlist_instantiation(instance):
    assert isinstance(instance, delphi_identList)

@given(instance=file_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, file)

@given(instance=delphi_library_strategy)
@settings(max_examples=50)
def test_delphi_library_instantiation(instance):
    assert isinstance(instance, delphi_library)

@given(instance=delphi_packageDecl_strategy)
@settings(max_examples=50)
def test_delphi_packagedecl_instantiation(instance):
    assert isinstance(instance, delphi_packageDecl)

@given(instance=delphi_unit_strategy)
@settings(max_examples=50)
def test_delphi_unit_instantiation(instance):
    assert isinstance(instance, delphi_unit)



@given(instance=delphi_unit_strategy)
def test_delphi_unit_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_program_strategy)
@settings(max_examples=50)
def test_delphi_program_instantiation(instance):
    assert isinstance(instance, delphi_program)

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=delphi_classFieldList_strategy)
@settings(max_examples=50)
def test_delphi_classfieldlist_instantiation(instance):
    assert isinstance(instance, delphi_classFieldList)

@given(instance=delphi_ident_strategy)
@settings(max_examples=50)
def test_delphi_ident_instantiation(instance):
    assert isinstance(instance, delphi_ident)

@given(instance=delphi_block_strategy)
@settings(max_examples=50)
def test_delphi_block_instantiation(instance):
    assert isinstance(instance, delphi_block)

@given(instance=delphi_propertyInterface_strategy)
@settings(max_examples=50)
def test_delphi_propertyinterface_instantiation(instance):
    assert isinstance(instance, delphi_propertyInterface)

@given(instance=delphi_typedConstant_strategy)
@settings(max_examples=50)
def test_delphi_typedconstant_instantiation(instance):
    assert isinstance(instance, delphi_typedConstant)

@given(instance=delphi_usesClause_strategy)
@settings(max_examples=50)
def test_delphi_usesclause_instantiation(instance):
    assert isinstance(instance, delphi_usesClause)

@given(instance=delphi_objFieldList_strategy)
@settings(max_examples=50)
def test_delphi_objfieldlist_instantiation(instance):
    assert isinstance(instance, delphi_objFieldList)

@given(instance=delphi_recordConstExpr_strategy)
@settings(max_examples=50)
def test_delphi_recordconstexpr_instantiation(instance):
    assert isinstance(instance, delphi_recordConstExpr)

@given(instance=delphi_reservedWord_strategy)
@settings(max_examples=50)
def test_delphi_reservedword_instantiation(instance):
    assert isinstance(instance, delphi_reservedWord)



@given(instance=delphi_reservedWord_strategy)
def test_delphi_reservedword_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi_file_strategy)
@settings(max_examples=50)
def test_delphi_file_instantiation(instance):
    assert isinstance(instance, delphi_file)

@given(instance=delphi_caseLabel_strategy)
@settings(max_examples=50)
def test_delphi_caselabel_instantiation(instance):
    assert isinstance(instance, delphi_caseLabel)

@given(instance=delphi_exprList_strategy)
@settings(max_examples=50)
def test_delphi_exprlist_instantiation(instance):
    assert isinstance(instance, delphi_exprList)

@given(instance=delphi_type_strategy)
@settings(max_examples=50)
def test_delphi_type_instantiation(instance):
    assert isinstance(instance, delphi_type)

@given(instance=delphi_propertyList_strategy)
@settings(max_examples=50)
def test_delphi_propertylist_instantiation(instance):
    assert isinstance(instance, delphi_propertyList)



@given(instance=delphi_propertyList_strategy)
def test_delphi_propertylist_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_recordConstant_strategy)
@settings(max_examples=50)
def test_delphi_recordconstant_instantiation(instance):
    assert isinstance(instance, delphi_recordConstant)

@given(instance=delphi_classProperty_strategy)
@settings(max_examples=50)
def test_delphi_classproperty_instantiation(instance):
    assert isinstance(instance, delphi_classProperty)



@given(instance=delphi_classProperty_strategy)
def test_delphi_classproperty_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi_varDecl_strategy)
@settings(max_examples=50)
def test_delphi_vardecl_instantiation(instance):
    assert isinstance(instance, delphi_varDecl)

@given(instance=delphi_parameter_strategy)
@settings(max_examples=50)
def test_delphi_parameter_instantiation(instance):
    assert isinstance(instance, delphi_parameter)

@given(instance=delphi_interfaceHeritage_strategy)
@settings(max_examples=50)
def test_delphi_interfaceheritage_instantiation(instance):
    assert isinstance(instance, delphi_interfaceHeritage)

@given(instance=delphi_formalParameters_strategy)
@settings(max_examples=50)
def test_delphi_formalparameters_instantiation(instance):
    assert isinstance(instance, delphi_formalParameters)

@given(instance=delphi_statement_strategy)
@settings(max_examples=50)
def test_delphi_statement_instantiation(instance):
    assert isinstance(instance, delphi_statement)



@given(instance=delphi_statement_strategy)
def test_delphi_statement_labelId_setter(instance):
    original = instance.labelId
    instance.labelId = original
    assert instance.labelId == original

@given(instance=delphi_declSection_strategy)
@settings(max_examples=50)
def test_delphi_declsection_instantiation(instance):
    assert isinstance(instance, delphi_declSection)

@given(instance=delphi_designator_strategy)
@settings(max_examples=50)
def test_delphi_designator_instantiation(instance):
    assert isinstance(instance, delphi_designator)

@given(instance=delphi_enumeratedTypeElement_strategy)
@settings(max_examples=50)
def test_delphi_enumeratedtypeelement_instantiation(instance):
    assert isinstance(instance, delphi_enumeratedTypeElement)

@given(instance=delphi_designatorSubPart_strategy)
@settings(max_examples=50)
def test_delphi_designatorsubpart_instantiation(instance):
    assert isinstance(instance, delphi_designatorSubPart)

@given(instance=delphi_initSection_strategy)
@settings(max_examples=50)
def test_delphi_initsection_instantiation(instance):
    assert isinstance(instance, delphi_initSection)

@given(instance=delphi_caseSelector_strategy)
@settings(max_examples=50)
def test_delphi_caseselector_instantiation(instance):
    assert isinstance(instance, delphi_caseSelector)

@given(instance=delphi_variantSection_strategy)
@settings(max_examples=50)
def test_delphi_variantsection_instantiation(instance):
    assert isinstance(instance, delphi_variantSection)

@given(instance=delphi_mulOp_strategy)
@settings(max_examples=50)
def test_delphi_mulop_instantiation(instance):
    assert isinstance(instance, delphi_mulOp)



@given(instance=delphi_mulOp_strategy)
def test_delphi_mulop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=delphi_designatorPart_strategy)
@settings(max_examples=50)
def test_delphi_designatorpart_instantiation(instance):
    assert isinstance(instance, delphi_designatorPart)



@given(instance=delphi_designatorPart_strategy)
def test_delphi_designatorpart_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original



@given(instance=delphi_designatorPart_strategy)
def test_delphi_designatorpart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi_restrictedType_strategy)
@settings(max_examples=50)
def test_delphi_restrictedtype_instantiation(instance):
    assert isinstance(instance, delphi_restrictedType)

@given(instance=delphi_exportsStmt_strategy)
@settings(max_examples=50)
def test_delphi_exportsstmt_instantiation(instance):
    assert isinstance(instance, delphi_exportsStmt)

@given(instance=delphi_arrayConstant_strategy)
@settings(max_examples=50)
def test_delphi_arrayconstant_instantiation(instance):
    assert isinstance(instance, delphi_arrayConstant)

@given(instance=delphi_requiresClause_strategy)
@settings(max_examples=50)
def test_delphi_requiresclause_instantiation(instance):
    assert isinstance(instance, delphi_requiresClause)

@given(instance=delphi_setConstructor_strategy)
@settings(max_examples=50)
def test_delphi_setconstructor_instantiation(instance):
    assert isinstance(instance, delphi_setConstructor)

@given(instance=delphi_recordFieldConstant_strategy)
@settings(max_examples=50)
def test_delphi_recordfieldconstant_instantiation(instance):
    assert isinstance(instance, delphi_recordFieldConstant)

@given(instance=delphi_constantDecl_strategy)
@settings(max_examples=50)
def test_delphi_constantdecl_instantiation(instance):
    assert isinstance(instance, delphi_constantDecl)



@given(instance=delphi_constantDecl_strategy)
def test_delphi_constantdecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_implementationSection_strategy)
@settings(max_examples=50)
def test_delphi_implementationsection_instantiation(instance):
    assert isinstance(instance, delphi_implementationSection)

@given(instance=delphi_fieldList_strategy)
@settings(max_examples=50)
def test_delphi_fieldlist_instantiation(instance):
    assert isinstance(instance, delphi_fieldList)

@given(instance=delphi_unlabelledStatement_strategy)
@settings(max_examples=50)
def test_delphi_unlabelledstatement_instantiation(instance):
    assert isinstance(instance, delphi_unlabelledStatement)

@given(instance=delphi_methodHeading_strategy)
@settings(max_examples=50)
def test_delphi_methodheading_instantiation(instance):
    assert isinstance(instance, delphi_methodHeading)

@given(instance=delphi_classMethod_strategy)
@settings(max_examples=50)
def test_delphi_classmethod_instantiation(instance):
    assert isinstance(instance, delphi_classMethod)



@given(instance=delphi_classMethod_strategy)
def test_delphi_classmethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi_objHeritage_strategy)
@settings(max_examples=50)
def test_delphi_objheritage_instantiation(instance):
    assert isinstance(instance, delphi_objHeritage)

@given(instance=delphi_constExpr_strategy)
@settings(max_examples=50)
def test_delphi_constexpr_instantiation(instance):
    assert isinstance(instance, delphi_constExpr)

@given(instance=delphi_recVariant_strategy)
@settings(max_examples=50)
def test_delphi_recvariant_instantiation(instance):
    assert isinstance(instance, delphi_recVariant)

@given(instance=delphi_classField_strategy)
@settings(max_examples=50)
def test_delphi_classfield_instantiation(instance):
    assert isinstance(instance, delphi_classField)



@given(instance=delphi_classField_strategy)
def test_delphi_classfield_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=delphi_classMethodList_strategy)
@settings(max_examples=50)
def test_delphi_classmethodlist_instantiation(instance):
    assert isinstance(instance, delphi_classMethodList)

@given(instance=delphi_unitId_strategy)
@settings(max_examples=50)
def test_delphi_unitid_instantiation(instance):
    assert isinstance(instance, delphi_unitId)



@given(instance=delphi_unitId_strategy)
def test_delphi_unitid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=delphi_programBlock_strategy)
@settings(max_examples=50)
def test_delphi_programblock_instantiation(instance):
    assert isinstance(instance, delphi_programBlock)

@given(instance=delphi_exportsItem_strategy)
@settings(max_examples=50)
def test_delphi_exportsitem_instantiation(instance):
    assert isinstance(instance, delphi_exportsItem)

@given(instance=delphi_classHeritage_strategy)
@settings(max_examples=50)
def test_delphi_classheritage_instantiation(instance):
    assert isinstance(instance, delphi_classHeritage)

@given(instance=delphi_setElement_strategy)
@settings(max_examples=50)
def test_delphi_setelement_instantiation(instance):
    assert isinstance(instance, delphi_setElement)

@given(instance=delphi_propertySpecifiers_strategy)
@settings(max_examples=50)
def test_delphi_propertyspecifiers_instantiation(instance):
    assert isinstance(instance, delphi_propertySpecifiers)

@given(instance=delphi_interfaceDecl_strategy)
@settings(max_examples=50)
def test_delphi_interfacedecl_instantiation(instance):
    assert isinstance(instance, delphi_interfaceDecl)

@given(instance=delphi_qualId_strategy)
@settings(max_examples=50)
def test_delphi_qualid_instantiation(instance):
    assert isinstance(instance, delphi_qualId)

@given(instance=delphi_directive_strategy)
@settings(max_examples=50)
def test_delphi_directive_instantiation(instance):
    assert isinstance(instance, delphi_directive)



@given(instance=delphi_directive_strategy)
def test_delphi_directive_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=delphi_typeDecl_strategy)
@settings(max_examples=50)
def test_delphi_typedecl_instantiation(instance):
    assert isinstance(instance, delphi_typeDecl)



@given(instance=delphi_typeDecl_strategy)
def test_delphi_typedecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_fieldDecl_strategy)
@settings(max_examples=50)
def test_delphi_fielddecl_instantiation(instance):
    assert isinstance(instance, delphi_fieldDecl)



@given(instance=delphi_fieldDecl_strategy)
def test_delphi_fielddecl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=delphi_classPropertyList_strategy)
@settings(max_examples=50)
def test_delphi_classpropertylist_instantiation(instance):
    assert isinstance(instance, delphi_classPropertyList)

@given(instance=delphi_interfaceSection_strategy)
@settings(max_examples=50)
def test_delphi_interfacesection_instantiation(instance):
    assert isinstance(instance, delphi_interfaceSection)

@given(instance=delphi_propertyParameterList_strategy)
@settings(max_examples=50)
def test_delphi_propertyparameterlist_instantiation(instance):
    assert isinstance(instance, delphi_propertyParameterList)

@given(instance=delphi_formalParm_strategy)
@settings(max_examples=50)
def test_delphi_formalparm_instantiation(instance):
    assert isinstance(instance, delphi_formalParm)

@given(instance=delphi_stmtList_strategy)
@settings(max_examples=50)
def test_delphi_stmtlist_instantiation(instance):
    assert isinstance(instance, delphi_stmtList)

@given(instance=delphi_relOp_strategy)
@settings(max_examples=50)
def test_delphi_relop_instantiation(instance):
    assert isinstance(instance, delphi_relOp)



@given(instance=delphi_relOp_strategy)
def test_delphi_relop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=delphi_methodList_strategy)
@settings(max_examples=50)
def test_delphi_methodlist_instantiation(instance):
    assert isinstance(instance, delphi_methodList)

@given(instance=delphi_expression_strategy)
@settings(max_examples=50)
def test_delphi_expression_instantiation(instance):
    assert isinstance(instance, delphi_expression)

@given(instance=delphi_exceptionBlock_strategy)
@settings(max_examples=50)
def test_delphi_exceptionblock_instantiation(instance):
    assert isinstance(instance, delphi_exceptionBlock)

@given(instance=delphi_containsClause_strategy)
@settings(max_examples=50)
def test_delphi_containsclause_instantiation(instance):
    assert isinstance(instance, delphi_containsClause)

@given(instance=delphi_addOp_strategy)
@settings(max_examples=50)
def test_delphi_addop_instantiation(instance):
    assert isinstance(instance, delphi_addOp)

@given(instance=delphi_mainRule_strategy)
@settings(max_examples=50)
def test_delphi_mainrule_instantiation(instance):
    assert isinstance(instance, delphi_mainRule)

@given(instance=delphi_inheritedStamnt_strategy)
@settings(max_examples=50)
def test_delphi_inheritedstamnt_instantiation(instance):
    assert isinstance(instance, delphi_inheritedStamnt)

@given(instance=delphi_Visitable_strategy)
@settings(max_examples=50)
def test_delphi_visitable_instantiation(instance):
    assert isinstance(instance, delphi_Visitable)

@given(instance=delphi_CSTrace_strategy)
@settings(max_examples=50)
def test_delphi_cstrace_instantiation(instance):
    assert isinstance(instance, delphi_CSTrace)

@given(instance=constExpr_strategy)
@settings(max_examples=50)
def test_constexpr_instantiation(instance):
    assert isinstance(instance, constExpr)

@given(instance=delphi_MultipleConstExp_strategy)
@settings(max_examples=50)
def test_delphi_multipleconstexp_instantiation(instance):
    assert isinstance(instance, delphi_MultipleConstExp)

@given(instance=delphi_RecordConstExp_strategy)
@settings(max_examples=50)
def test_delphi_recordconstexp_instantiation(instance):
    assert isinstance(instance, delphi_RecordConstExp)

@given(instance=delphi_ConstExp_strategy)
@settings(max_examples=50)
def test_delphi_constexp_instantiation(instance):
    assert isinstance(instance, delphi_ConstExp)

@given(instance=ident_strategy)
@settings(max_examples=50)
def test_ident_instantiation(instance):
    assert isinstance(instance, ident)

@given(instance=delphi_MineID_strategy)
@settings(max_examples=50)
def test_delphi_mineid_instantiation(instance):
    assert isinstance(instance, delphi_MineID)



@given(instance=delphi_MineID_strategy)
def test_delphi_mineid_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original



@given(instance=delphi_MineID_strategy)
def test_delphi_mineid_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=delphi_ReservedId_strategy)
@settings(max_examples=50)
def test_delphi_reservedid_instantiation(instance):
    assert isinstance(instance, delphi_ReservedId)

@given(instance=delphi_MultipleId_strategy)
@settings(max_examples=50)
def test_delphi_multipleid_instantiation(instance):
    assert isinstance(instance, delphi_MultipleId)



@given(instance=delphi_MultipleId_strategy)
def test_delphi_multipleid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, parameter)

@given(instance=delphi_parameterSimple_strategy)
@settings(max_examples=50)
def test_delphi_parametersimple_instantiation(instance):
    assert isinstance(instance, delphi_parameterSimple)

@given(instance=delphi_parameterList_strategy)
@settings(max_examples=50)
def test_delphi_parameterlist_instantiation(instance):
    assert isinstance(instance, delphi_parameterList)

@given(instance=delphi_gotoStmnt_strategy)
@settings(max_examples=50)
def test_delphi_gotostmnt_instantiation(instance):
    assert isinstance(instance, delphi_gotoStmnt)



@given(instance=delphi_gotoStmnt_strategy)
def test_delphi_gotostmnt_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

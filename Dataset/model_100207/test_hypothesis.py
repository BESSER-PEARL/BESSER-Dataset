import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DataType,
    XMLValueFunctionValidateAccordingTo,
    query_XMLValueFunctionValidateAccordingToIdentifier,
    query_XMLValueFunctionValidateAccordingToURI,
    XMLTableColumnDefinitionItem,
    query_XMLTableColumnDefinitionOrdinality,
    query_XMLTableColumnDefinitionRegular,
    TableFunction,
    query_OrderBySpecification,
    query_XMLTableFunction,
    XMLPredicate,
    query_XMLPredicateDocument,
    query_XMLPredicateExists,
    query_XMLPredicateValid,
    query_XMLPredicateContent,
    Predicate,
    query_XMLPredicate,
    ValueExpressionCast,
    query_XMLValueExpressionCast,
    SQLQueryObject,
    query_XMLSerializeFunctionEncoding,
    query_XMLValueFunctionValidateElement,
    query_XMLAggregateSortSpecification,
    query_XMLNamespacesDeclaration,
    query_XMLValueFunctionValidateElementName,
    query_XMLTableColumnDefinitionItem,
    query_XMLQueryExpression,
    query_XMLValueFunctionValidateElementNamespace,
    query_XMLValueFunctionQueryReturning,
    query_XMLValueFunctionValidateAccordingTo,
    query_XMLQueryArgumentList,
    query_XMLNamespaceDeclarationItem,
    query_XMLValueFunctionElementContentList,
    XMLNamespaceDeclarationItem,
    query_XMLNamespaceDeclarationDefault,
    query_XMLNamespaceDeclarationPrefix,
    ValueExpressionFunction,
    query_XMLAggregateFunction,
    query_XMLSerializeFunction,
    query_XMLValueFunction,
    query_XMLAttributesDeclaration,
    query_QueryValueExpression,
    QueryValueExpression,
    query_XMLValueFunctionParseContent,
    query_XMLValueFunctionCommentContent,
    query_XMLTableColumnDefinitionDefault,
    query_XMLValueFunctionPIContent,
    query_XMLValueFunctionValidateContent,
    query_XMLQueryArgumentItem,
    query_XMLValueFunctionDocumentContent,
    query_XMLValueFunctionTextContent,
    query_XMLValueFunctionForestContentItem,
    query_XMLSerializeFunctionTarget,
    query_XMLValueFunctionElementContentItem,
    query_XMLValueFunctionConcatContentItem,
    query_XMLAttributeDeclarationItem,
    XMLValueFunction,
    query_XMLValueFunctionElement,
    query_XMLValueFunctionDocument,
    query_XMLValueFunctionForest,
    query_XMLValueFunctionText,
    query_XMLValueFunctionValidate,
    query_XMLValueFunctionPI,
    query_XMLValueFunctionQuery,
    query_XMLValueFunctionParse,
    query_XMLValueFunctionComment,
    query_XMLValueFunctionConcat,
    XMLContentType,
    XMLDeclarationType,
    XMLContentType2,
    XMLReturningType,
    XMLPassingType,
    XMLEmptyHandlingType,
    XMLNullHandlingType,
    XMLWhitespaceHandlingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_xmlvaluefunctionvalidateaccordingto_is_not_abstract():
    assert not inspect.isabstract(XMLValueFunctionValidateAccordingTo)


def test_xmlvaluefunctionvalidateaccordingto_constructor_exists():
    assert callable(XMLValueFunctionValidateAccordingTo.__init__)


def test_xmlvaluefunctionvalidateaccordingto_constructor_args():
    sig = inspect.signature(XMLValueFunctionValidateAccordingTo.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateAccordingToIdentifier)


def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_constructor_exists():
    assert callable(query_XMLValueFunctionValidateAccordingToIdentifier.__init__)


def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateAccordingToIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "registeredXMLSchemaName" in params, "Missing parameter 'registeredXMLSchemaName'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_has_registeredXMLSchemaName():
    assert hasattr(query_XMLValueFunctionValidateAccordingToIdentifier, "registeredXMLSchemaName")
    descriptor = None
    for klass in query_XMLValueFunctionValidateAccordingToIdentifier.__mro__:
        if "registeredXMLSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["registeredXMLSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_has_schemaName():
    assert hasattr(query_XMLValueFunctionValidateAccordingToIdentifier, "schemaName")
    descriptor = None
    for klass in query_XMLValueFunctionValidateAccordingToIdentifier.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionvalidateaccordingtouri_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateAccordingToURI)


def test_query_xmlvaluefunctionvalidateaccordingtouri_constructor_exists():
    assert callable(query_XMLValueFunctionValidateAccordingToURI.__init__)


def test_query_xmlvaluefunctionvalidateaccordingtouri_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateAccordingToURI.__init__)
    params = list(sig.parameters.keys())
    assert "noNamespace" in params, "Missing parameter 'noNamespace'"
    assert "targetNamespaceURI" in params, "Missing parameter 'targetNamespaceURI'"
    assert "schemaLocationURI" in params, "Missing parameter 'schemaLocationURI'"

def test_query_xmlvaluefunctionvalidateaccordingtouri_has_noNamespace():
    assert hasattr(query_XMLValueFunctionValidateAccordingToURI, "noNamespace")
    descriptor = None
    for klass in query_XMLValueFunctionValidateAccordingToURI.__mro__:
        if "noNamespace" in klass.__dict__:
            descriptor = klass.__dict__["noNamespace"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionvalidateaccordingtouri_has_targetNamespaceURI():
    assert hasattr(query_XMLValueFunctionValidateAccordingToURI, "targetNamespaceURI")
    descriptor = None
    for klass in query_XMLValueFunctionValidateAccordingToURI.__mro__:
        if "targetNamespaceURI" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespaceURI"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionvalidateaccordingtouri_has_schemaLocationURI():
    assert hasattr(query_XMLValueFunctionValidateAccordingToURI, "schemaLocationURI")
    descriptor = None
    for klass in query_XMLValueFunctionValidateAccordingToURI.__mro__:
        if "schemaLocationURI" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocationURI"]
            break
    assert isinstance(descriptor, property)



def test_xmltablecolumndefinitionitem_is_not_abstract():
    assert not inspect.isabstract(XMLTableColumnDefinitionItem)


def test_xmltablecolumndefinitionitem_constructor_exists():
    assert callable(XMLTableColumnDefinitionItem.__init__)


def test_xmltablecolumndefinitionitem_constructor_args():
    sig = inspect.signature(XMLTableColumnDefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmltablecolumndefinitionordinality_is_not_abstract():
    assert not inspect.isabstract(query_XMLTableColumnDefinitionOrdinality)


def test_query_xmltablecolumndefinitionordinality_constructor_exists():
    assert callable(query_XMLTableColumnDefinitionOrdinality.__init__)


def test_query_xmltablecolumndefinitionordinality_constructor_args():
    sig = inspect.signature(query_XMLTableColumnDefinitionOrdinality.__init__)
    params = list(sig.parameters.keys())



def test_query_xmltablecolumndefinitionregular_is_not_abstract():
    assert not inspect.isabstract(query_XMLTableColumnDefinitionRegular)


def test_query_xmltablecolumndefinitionregular_constructor_exists():
    assert callable(query_XMLTableColumnDefinitionRegular.__init__)


def test_query_xmltablecolumndefinitionregular_constructor_args():
    sig = inspect.signature(query_XMLTableColumnDefinitionRegular.__init__)
    params = list(sig.parameters.keys())
    assert "passingOption" in params, "Missing parameter 'passingOption'"
    assert "tableColumnPattern" in params, "Missing parameter 'tableColumnPattern'"

def test_query_xmltablecolumndefinitionregular_has_passingOption():
    assert hasattr(query_XMLTableColumnDefinitionRegular, "passingOption")
    descriptor = None
    for klass in query_XMLTableColumnDefinitionRegular.__mro__:
        if "passingOption" in klass.__dict__:
            descriptor = klass.__dict__["passingOption"]
            break
    assert isinstance(descriptor, property)

def test_query_xmltablecolumndefinitionregular_has_tableColumnPattern():
    assert hasattr(query_XMLTableColumnDefinitionRegular, "tableColumnPattern")
    descriptor = None
    for klass in query_XMLTableColumnDefinitionRegular.__mro__:
        if "tableColumnPattern" in klass.__dict__:
            descriptor = klass.__dict__["tableColumnPattern"]
            break
    assert isinstance(descriptor, property)



def test_tablefunction_is_not_abstract():
    assert not inspect.isabstract(TableFunction)


def test_tablefunction_constructor_exists():
    assert callable(TableFunction.__init__)


def test_tablefunction_constructor_args():
    sig = inspect.signature(TableFunction.__init__)
    params = list(sig.parameters.keys())



def test_query_orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(query_OrderBySpecification)


def test_query_orderbyspecification_constructor_exists():
    assert callable(query_OrderBySpecification.__init__)


def test_query_orderbyspecification_constructor_args():
    sig = inspect.signature(query_OrderBySpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_xmltablefunction_is_not_abstract():
    assert not inspect.isabstract(query_XMLTableFunction)


def test_query_xmltablefunction_constructor_exists():
    assert callable(query_XMLTableFunction.__init__)


def test_query_xmltablefunction_constructor_args():
    sig = inspect.signature(query_XMLTableFunction.__init__)
    params = list(sig.parameters.keys())
    assert "tableRowPattern" in params, "Missing parameter 'tableRowPattern'"

def test_query_xmltablefunction_has_tableRowPattern():
    assert hasattr(query_XMLTableFunction, "tableRowPattern")
    descriptor = None
    for klass in query_XMLTableFunction.__mro__:
        if "tableRowPattern" in klass.__dict__:
            descriptor = klass.__dict__["tableRowPattern"]
            break
    assert isinstance(descriptor, property)



def test_xmlpredicate_is_not_abstract():
    assert not inspect.isabstract(XMLPredicate)


def test_xmlpredicate_constructor_exists():
    assert callable(XMLPredicate.__init__)


def test_xmlpredicate_constructor_args():
    sig = inspect.signature(XMLPredicate.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlpredicatedocument_is_not_abstract():
    assert not inspect.isabstract(query_XMLPredicateDocument)


def test_query_xmlpredicatedocument_constructor_exists():
    assert callable(query_XMLPredicateDocument.__init__)


def test_query_xmlpredicatedocument_constructor_args():
    sig = inspect.signature(query_XMLPredicateDocument.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlpredicateexists_is_not_abstract():
    assert not inspect.isabstract(query_XMLPredicateExists)


def test_query_xmlpredicateexists_constructor_exists():
    assert callable(query_XMLPredicateExists.__init__)


def test_query_xmlpredicateexists_constructor_args():
    sig = inspect.signature(query_XMLPredicateExists.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlpredicatevalid_is_not_abstract():
    assert not inspect.isabstract(query_XMLPredicateValid)


def test_query_xmlpredicatevalid_constructor_exists():
    assert callable(query_XMLPredicateValid.__init__)


def test_query_xmlpredicatevalid_constructor_args():
    sig = inspect.signature(query_XMLPredicateValid.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlpredicatecontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLPredicateContent)


def test_query_xmlpredicatecontent_constructor_exists():
    assert callable(query_XMLPredicateContent.__init__)


def test_query_xmlpredicatecontent_constructor_args():
    sig = inspect.signature(query_XMLPredicateContent.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlpredicate_is_not_abstract():
    assert not inspect.isabstract(query_XMLPredicate)


def test_query_xmlpredicate_constructor_exists():
    assert callable(query_XMLPredicate.__init__)


def test_query_xmlpredicate_constructor_args():
    sig = inspect.signature(query_XMLPredicate.__init__)
    params = list(sig.parameters.keys())



def test_valueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionCast)


def test_valueexpressioncast_constructor_exists():
    assert callable(ValueExpressionCast.__init__)


def test_valueexpressioncast_constructor_args():
    sig = inspect.signature(ValueExpressionCast.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvalueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueExpressionCast)


def test_query_xmlvalueexpressioncast_constructor_exists():
    assert callable(query_XMLValueExpressionCast.__init__)


def test_query_xmlvalueexpressioncast_constructor_args():
    sig = inspect.signature(query_XMLValueExpressionCast.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query_xmlvalueexpressioncast_has_passingMechanism():
    assert hasattr(query_XMLValueExpressionCast, "passingMechanism")
    descriptor = None
    for klass in query_XMLValueExpressionCast.__mro__:
        if "passingMechanism" in klass.__dict__:
            descriptor = klass.__dict__["passingMechanism"]
            break
    assert isinstance(descriptor, property)



def test_sqlqueryobject_is_not_abstract():
    assert not inspect.isabstract(SQLQueryObject)


def test_sqlqueryobject_constructor_exists():
    assert callable(SQLQueryObject.__init__)


def test_sqlqueryobject_constructor_args():
    sig = inspect.signature(SQLQueryObject.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlserializefunctionencoding_is_not_abstract():
    assert not inspect.isabstract(query_XMLSerializeFunctionEncoding)


def test_query_xmlserializefunctionencoding_constructor_exists():
    assert callable(query_XMLSerializeFunctionEncoding.__init__)


def test_query_xmlserializefunctionencoding_constructor_args():
    sig = inspect.signature(query_XMLSerializeFunctionEncoding.__init__)
    params = list(sig.parameters.keys())
    assert "encodingName" in params, "Missing parameter 'encodingName'"

def test_query_xmlserializefunctionencoding_has_encodingName():
    assert hasattr(query_XMLSerializeFunctionEncoding, "encodingName")
    descriptor = None
    for klass in query_XMLSerializeFunctionEncoding.__mro__:
        if "encodingName" in klass.__dict__:
            descriptor = klass.__dict__["encodingName"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionvalidateelement_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateElement)


def test_query_xmlvaluefunctionvalidateelement_constructor_exists():
    assert callable(query_XMLValueFunctionValidateElement.__init__)


def test_query_xmlvaluefunctionvalidateelement_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateElement.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlaggregatesortspecification_is_not_abstract():
    assert not inspect.isabstract(query_XMLAggregateSortSpecification)


def test_query_xmlaggregatesortspecification_constructor_exists():
    assert callable(query_XMLAggregateSortSpecification.__init__)


def test_query_xmlaggregatesortspecification_constructor_args():
    sig = inspect.signature(query_XMLAggregateSortSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlnamespacesdeclaration_is_not_abstract():
    assert not inspect.isabstract(query_XMLNamespacesDeclaration)


def test_query_xmlnamespacesdeclaration_constructor_exists():
    assert callable(query_XMLNamespacesDeclaration.__init__)


def test_query_xmlnamespacesdeclaration_constructor_args():
    sig = inspect.signature(query_XMLNamespacesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionvalidateelementname_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateElementName)


def test_query_xmlvaluefunctionvalidateelementname_constructor_exists():
    assert callable(query_XMLValueFunctionValidateElementName.__init__)


def test_query_xmlvaluefunctionvalidateelementname_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateElementName.__init__)
    params = list(sig.parameters.keys())



def test_query_xmltablecolumndefinitionitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLTableColumnDefinitionItem)


def test_query_xmltablecolumndefinitionitem_constructor_exists():
    assert callable(query_XMLTableColumnDefinitionItem.__init__)


def test_query_xmltablecolumndefinitionitem_constructor_args():
    sig = inspect.signature(query_XMLTableColumnDefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlqueryexpression_is_not_abstract():
    assert not inspect.isabstract(query_XMLQueryExpression)


def test_query_xmlqueryexpression_constructor_exists():
    assert callable(query_XMLQueryExpression.__init__)


def test_query_xmlqueryexpression_constructor_args():
    sig = inspect.signature(query_XMLQueryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "xqueryExprContent" in params, "Missing parameter 'xqueryExprContent'"

def test_query_xmlqueryexpression_has_xqueryExprContent():
    assert hasattr(query_XMLQueryExpression, "xqueryExprContent")
    descriptor = None
    for klass in query_XMLQueryExpression.__mro__:
        if "xqueryExprContent" in klass.__dict__:
            descriptor = klass.__dict__["xqueryExprContent"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionvalidateelementnamespace_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateElementNamespace)


def test_query_xmlvaluefunctionvalidateelementnamespace_constructor_exists():
    assert callable(query_XMLValueFunctionValidateElementNamespace.__init__)


def test_query_xmlvaluefunctionvalidateelementnamespace_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateElementNamespace.__init__)
    params = list(sig.parameters.keys())
    assert "noNamespace" in params, "Missing parameter 'noNamespace'"
    assert "namespaceURI" in params, "Missing parameter 'namespaceURI'"

def test_query_xmlvaluefunctionvalidateelementnamespace_has_noNamespace():
    assert hasattr(query_XMLValueFunctionValidateElementNamespace, "noNamespace")
    descriptor = None
    for klass in query_XMLValueFunctionValidateElementNamespace.__mro__:
        if "noNamespace" in klass.__dict__:
            descriptor = klass.__dict__["noNamespace"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionvalidateelementnamespace_has_namespaceURI():
    assert hasattr(query_XMLValueFunctionValidateElementNamespace, "namespaceURI")
    descriptor = None
    for klass in query_XMLValueFunctionValidateElementNamespace.__mro__:
        if "namespaceURI" in klass.__dict__:
            descriptor = klass.__dict__["namespaceURI"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionqueryreturning_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionQueryReturning)


def test_query_xmlvaluefunctionqueryreturning_constructor_exists():
    assert callable(query_XMLValueFunctionQueryReturning.__init__)


def test_query_xmlvaluefunctionqueryreturning_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionQueryReturning.__init__)
    params = list(sig.parameters.keys())
    assert "passingOption" in params, "Missing parameter 'passingOption'"
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctionqueryreturning_has_passingOption():
    assert hasattr(query_XMLValueFunctionQueryReturning, "passingOption")
    descriptor = None
    for klass in query_XMLValueFunctionQueryReturning.__mro__:
        if "passingOption" in klass.__dict__:
            descriptor = klass.__dict__["passingOption"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionqueryreturning_has_returningOption():
    assert hasattr(query_XMLValueFunctionQueryReturning, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionQueryReturning.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionvalidateaccordingto_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateAccordingTo)


def test_query_xmlvaluefunctionvalidateaccordingto_constructor_exists():
    assert callable(query_XMLValueFunctionValidateAccordingTo.__init__)


def test_query_xmlvaluefunctionvalidateaccordingto_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateAccordingTo.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlqueryargumentlist_is_not_abstract():
    assert not inspect.isabstract(query_XMLQueryArgumentList)


def test_query_xmlqueryargumentlist_constructor_exists():
    assert callable(query_XMLQueryArgumentList.__init__)


def test_query_xmlqueryargumentlist_constructor_args():
    sig = inspect.signature(query_XMLQueryArgumentList.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query_xmlqueryargumentlist_has_passingMechanism():
    assert hasattr(query_XMLQueryArgumentList, "passingMechanism")
    descriptor = None
    for klass in query_XMLQueryArgumentList.__mro__:
        if "passingMechanism" in klass.__dict__:
            descriptor = klass.__dict__["passingMechanism"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlnamespacedeclarationitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLNamespaceDeclarationItem)


def test_query_xmlnamespacedeclarationitem_constructor_exists():
    assert callable(query_XMLNamespaceDeclarationItem.__init__)


def test_query_xmlnamespacedeclarationitem_constructor_args():
    sig = inspect.signature(query_XMLNamespaceDeclarationItem.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_query_xmlnamespacedeclarationitem_has_uri():
    assert hasattr(query_XMLNamespaceDeclarationItem, "uri")
    descriptor = None
    for klass in query_XMLNamespaceDeclarationItem.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionelementcontentlist_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionElementContentList)


def test_query_xmlvaluefunctionelementcontentlist_constructor_exists():
    assert callable(query_XMLValueFunctionElementContentList.__init__)


def test_query_xmlvaluefunctionelementcontentlist_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionElementContentList.__init__)
    params = list(sig.parameters.keys())
    assert "nullHandlingOption" in params, "Missing parameter 'nullHandlingOption'"

def test_query_xmlvaluefunctionelementcontentlist_has_nullHandlingOption():
    assert hasattr(query_XMLValueFunctionElementContentList, "nullHandlingOption")
    descriptor = None
    for klass in query_XMLValueFunctionElementContentList.__mro__:
        if "nullHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["nullHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_xmlnamespacedeclarationitem_is_not_abstract():
    assert not inspect.isabstract(XMLNamespaceDeclarationItem)


def test_xmlnamespacedeclarationitem_constructor_exists():
    assert callable(XMLNamespaceDeclarationItem.__init__)


def test_xmlnamespacedeclarationitem_constructor_args():
    sig = inspect.signature(XMLNamespaceDeclarationItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlnamespacedeclarationdefault_is_not_abstract():
    assert not inspect.isabstract(query_XMLNamespaceDeclarationDefault)


def test_query_xmlnamespacedeclarationdefault_constructor_exists():
    assert callable(query_XMLNamespaceDeclarationDefault.__init__)


def test_query_xmlnamespacedeclarationdefault_constructor_args():
    sig = inspect.signature(query_XMLNamespaceDeclarationDefault.__init__)
    params = list(sig.parameters.keys())
    assert "noDefault" in params, "Missing parameter 'noDefault'"

def test_query_xmlnamespacedeclarationdefault_has_noDefault():
    assert hasattr(query_XMLNamespaceDeclarationDefault, "noDefault")
    descriptor = None
    for klass in query_XMLNamespaceDeclarationDefault.__mro__:
        if "noDefault" in klass.__dict__:
            descriptor = klass.__dict__["noDefault"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlnamespacedeclarationprefix_is_not_abstract():
    assert not inspect.isabstract(query_XMLNamespaceDeclarationPrefix)


def test_query_xmlnamespacedeclarationprefix_constructor_exists():
    assert callable(query_XMLNamespaceDeclarationPrefix.__init__)


def test_query_xmlnamespacedeclarationprefix_constructor_args():
    sig = inspect.signature(query_XMLNamespaceDeclarationPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_query_xmlnamespacedeclarationprefix_has_prefix():
    assert hasattr(query_XMLNamespaceDeclarationPrefix, "prefix")
    descriptor = None
    for klass in query_XMLNamespaceDeclarationPrefix.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_valueexpressionfunction_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionFunction)


def test_valueexpressionfunction_constructor_exists():
    assert callable(ValueExpressionFunction.__init__)


def test_valueexpressionfunction_constructor_args():
    sig = inspect.signature(ValueExpressionFunction.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlaggregatefunction_is_not_abstract():
    assert not inspect.isabstract(query_XMLAggregateFunction)


def test_query_xmlaggregatefunction_constructor_exists():
    assert callable(query_XMLAggregateFunction.__init__)


def test_query_xmlaggregatefunction_constructor_args():
    sig = inspect.signature(query_XMLAggregateFunction.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlaggregatefunction_has_returningOption():
    assert hasattr(query_XMLAggregateFunction, "returningOption")
    descriptor = None
    for klass in query_XMLAggregateFunction.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlserializefunction_is_not_abstract():
    assert not inspect.isabstract(query_XMLSerializeFunction)


def test_query_xmlserializefunction_constructor_exists():
    assert callable(query_XMLSerializeFunction.__init__)


def test_query_xmlserializefunction_constructor_args():
    sig = inspect.signature(query_XMLSerializeFunction.__init__)
    params = list(sig.parameters.keys())
    assert "serializeVersion" in params, "Missing parameter 'serializeVersion'"
    assert "declarationOption" in params, "Missing parameter 'declarationOption'"
    assert "contentOption" in params, "Missing parameter 'contentOption'"

def test_query_xmlserializefunction_has_serializeVersion():
    assert hasattr(query_XMLSerializeFunction, "serializeVersion")
    descriptor = None
    for klass in query_XMLSerializeFunction.__mro__:
        if "serializeVersion" in klass.__dict__:
            descriptor = klass.__dict__["serializeVersion"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlserializefunction_has_declarationOption():
    assert hasattr(query_XMLSerializeFunction, "declarationOption")
    descriptor = None
    for klass in query_XMLSerializeFunction.__mro__:
        if "declarationOption" in klass.__dict__:
            descriptor = klass.__dict__["declarationOption"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlserializefunction_has_contentOption():
    assert hasattr(query_XMLSerializeFunction, "contentOption")
    descriptor = None
    for klass in query_XMLSerializeFunction.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunction_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunction)


def test_query_xmlvaluefunction_constructor_exists():
    assert callable(query_XMLValueFunction.__init__)


def test_query_xmlvaluefunction_constructor_args():
    sig = inspect.signature(query_XMLValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlattributesdeclaration_is_not_abstract():
    assert not inspect.isabstract(query_XMLAttributesDeclaration)


def test_query_xmlattributesdeclaration_constructor_exists():
    assert callable(query_XMLAttributesDeclaration.__init__)


def test_query_xmlattributesdeclaration_constructor_args():
    sig = inspect.signature(query_XMLAttributesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_query_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query_QueryValueExpression)


def test_query_queryvalueexpression_constructor_exists():
    assert callable(query_QueryValueExpression.__init__)


def test_query_queryvalueexpression_constructor_args():
    sig = inspect.signature(query_QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(QueryValueExpression)


def test_queryvalueexpression_constructor_exists():
    assert callable(QueryValueExpression.__init__)


def test_queryvalueexpression_constructor_args():
    sig = inspect.signature(QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionparsecontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionParseContent)


def test_query_xmlvaluefunctionparsecontent_constructor_exists():
    assert callable(query_XMLValueFunctionParseContent.__init__)


def test_query_xmlvaluefunctionparsecontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionParseContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctioncommentcontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionCommentContent)


def test_query_xmlvaluefunctioncommentcontent_constructor_exists():
    assert callable(query_XMLValueFunctionCommentContent.__init__)


def test_query_xmlvaluefunctioncommentcontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionCommentContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmltablecolumndefinitiondefault_is_not_abstract():
    assert not inspect.isabstract(query_XMLTableColumnDefinitionDefault)


def test_query_xmltablecolumndefinitiondefault_constructor_exists():
    assert callable(query_XMLTableColumnDefinitionDefault.__init__)


def test_query_xmltablecolumndefinitiondefault_constructor_args():
    sig = inspect.signature(query_XMLTableColumnDefinitionDefault.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionpicontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionPIContent)


def test_query_xmlvaluefunctionpicontent_constructor_exists():
    assert callable(query_XMLValueFunctionPIContent.__init__)


def test_query_xmlvaluefunctionpicontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionPIContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionvalidatecontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidateContent)


def test_query_xmlvaluefunctionvalidatecontent_constructor_exists():
    assert callable(query_XMLValueFunctionValidateContent.__init__)


def test_query_xmlvaluefunctionvalidatecontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidateContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlqueryargumentitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLQueryArgumentItem)


def test_query_xmlqueryargumentitem_constructor_exists():
    assert callable(query_XMLQueryArgumentItem.__init__)


def test_query_xmlqueryargumentitem_constructor_args():
    sig = inspect.signature(query_XMLQueryArgumentItem.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query_xmlqueryargumentitem_has_passingMechanism():
    assert hasattr(query_XMLQueryArgumentItem, "passingMechanism")
    descriptor = None
    for klass in query_XMLQueryArgumentItem.__mro__:
        if "passingMechanism" in klass.__dict__:
            descriptor = klass.__dict__["passingMechanism"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctiondocumentcontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionDocumentContent)


def test_query_xmlvaluefunctiondocumentcontent_constructor_exists():
    assert callable(query_XMLValueFunctionDocumentContent.__init__)


def test_query_xmlvaluefunctiondocumentcontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionDocumentContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctiontextcontent_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionTextContent)


def test_query_xmlvaluefunctiontextcontent_constructor_exists():
    assert callable(query_XMLValueFunctionTextContent.__init__)


def test_query_xmlvaluefunctiontextcontent_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionTextContent.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionforestcontentitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionForestContentItem)


def test_query_xmlvaluefunctionforestcontentitem_constructor_exists():
    assert callable(query_XMLValueFunctionForestContentItem.__init__)


def test_query_xmlvaluefunctionforestcontentitem_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionForestContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlserializefunctiontarget_is_not_abstract():
    assert not inspect.isabstract(query_XMLSerializeFunctionTarget)


def test_query_xmlserializefunctiontarget_constructor_exists():
    assert callable(query_XMLSerializeFunctionTarget.__init__)


def test_query_xmlserializefunctiontarget_constructor_args():
    sig = inspect.signature(query_XMLSerializeFunctionTarget.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionelementcontentitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionElementContentItem)


def test_query_xmlvaluefunctionelementcontentitem_constructor_exists():
    assert callable(query_XMLValueFunctionElementContentItem.__init__)


def test_query_xmlvaluefunctionelementcontentitem_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionElementContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionconcatcontentitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionConcatContentItem)


def test_query_xmlvaluefunctionconcatcontentitem_constructor_exists():
    assert callable(query_XMLValueFunctionConcatContentItem.__init__)


def test_query_xmlvaluefunctionconcatcontentitem_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionConcatContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlattributedeclarationitem_is_not_abstract():
    assert not inspect.isabstract(query_XMLAttributeDeclarationItem)


def test_query_xmlattributedeclarationitem_constructor_exists():
    assert callable(query_XMLAttributeDeclarationItem.__init__)


def test_query_xmlattributedeclarationitem_constructor_args():
    sig = inspect.signature(query_XMLAttributeDeclarationItem.__init__)
    params = list(sig.parameters.keys())



def test_xmlvaluefunction_is_not_abstract():
    assert not inspect.isabstract(XMLValueFunction)


def test_xmlvaluefunction_constructor_exists():
    assert callable(XMLValueFunction.__init__)


def test_xmlvaluefunction_constructor_args():
    sig = inspect.signature(XMLValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_query_xmlvaluefunctionelement_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionElement)


def test_query_xmlvaluefunctionelement_constructor_exists():
    assert callable(query_XMLValueFunctionElement.__init__)


def test_query_xmlvaluefunctionelement_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctionelement_has_elementName():
    assert hasattr(query_XMLValueFunctionElement, "elementName")
    descriptor = None
    for klass in query_XMLValueFunctionElement.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionelement_has_returningOption():
    assert hasattr(query_XMLValueFunctionElement, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionElement.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctiondocument_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionDocument)


def test_query_xmlvaluefunctiondocument_constructor_exists():
    assert callable(query_XMLValueFunctionDocument.__init__)


def test_query_xmlvaluefunctiondocument_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionDocument.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctiondocument_has_returningOption():
    assert hasattr(query_XMLValueFunctionDocument, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionDocument.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionforest_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionForest)


def test_query_xmlvaluefunctionforest_constructor_exists():
    assert callable(query_XMLValueFunctionForest.__init__)


def test_query_xmlvaluefunctionforest_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionForest.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"
    assert "nullHandlingOption" in params, "Missing parameter 'nullHandlingOption'"

def test_query_xmlvaluefunctionforest_has_returningOption():
    assert hasattr(query_XMLValueFunctionForest, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionForest.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionforest_has_nullHandlingOption():
    assert hasattr(query_XMLValueFunctionForest, "nullHandlingOption")
    descriptor = None
    for klass in query_XMLValueFunctionForest.__mro__:
        if "nullHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["nullHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctiontext_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionText)


def test_query_xmlvaluefunctiontext_constructor_exists():
    assert callable(query_XMLValueFunctionText.__init__)


def test_query_xmlvaluefunctiontext_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionText.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctiontext_has_returningOption():
    assert hasattr(query_XMLValueFunctionText, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionText.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionvalidate_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionValidate)


def test_query_xmlvaluefunctionvalidate_constructor_exists():
    assert callable(query_XMLValueFunctionValidate.__init__)


def test_query_xmlvaluefunctionvalidate_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionValidate.__init__)
    params = list(sig.parameters.keys())
    assert "contentOption" in params, "Missing parameter 'contentOption'"

def test_query_xmlvaluefunctionvalidate_has_contentOption():
    assert hasattr(query_XMLValueFunctionValidate, "contentOption")
    descriptor = None
    for klass in query_XMLValueFunctionValidate.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionpi_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionPI)


def test_query_xmlvaluefunctionpi_constructor_exists():
    assert callable(query_XMLValueFunctionPI.__init__)


def test_query_xmlvaluefunctionpi_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionPI.__init__)
    params = list(sig.parameters.keys())
    assert "targetName" in params, "Missing parameter 'targetName'"
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctionpi_has_targetName():
    assert hasattr(query_XMLValueFunctionPI, "targetName")
    descriptor = None
    for klass in query_XMLValueFunctionPI.__mro__:
        if "targetName" in klass.__dict__:
            descriptor = klass.__dict__["targetName"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionpi_has_returningOption():
    assert hasattr(query_XMLValueFunctionPI, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionPI.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionquery_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionQuery)


def test_query_xmlvaluefunctionquery_constructor_exists():
    assert callable(query_XMLValueFunctionQuery.__init__)


def test_query_xmlvaluefunctionquery_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionQuery.__init__)
    params = list(sig.parameters.keys())
    assert "emptyHandlingOption" in params, "Missing parameter 'emptyHandlingOption'"

def test_query_xmlvaluefunctionquery_has_emptyHandlingOption():
    assert hasattr(query_XMLValueFunctionQuery, "emptyHandlingOption")
    descriptor = None
    for klass in query_XMLValueFunctionQuery.__mro__:
        if "emptyHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["emptyHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionparse_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionParse)


def test_query_xmlvaluefunctionparse_constructor_exists():
    assert callable(query_XMLValueFunctionParse.__init__)


def test_query_xmlvaluefunctionparse_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionParse.__init__)
    params = list(sig.parameters.keys())
    assert "whitespaceHandlingOption" in params, "Missing parameter 'whitespaceHandlingOption'"
    assert "contentOption" in params, "Missing parameter 'contentOption'"

def test_query_xmlvaluefunctionparse_has_whitespaceHandlingOption():
    assert hasattr(query_XMLValueFunctionParse, "whitespaceHandlingOption")
    descriptor = None
    for klass in query_XMLValueFunctionParse.__mro__:
        if "whitespaceHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["whitespaceHandlingOption"]
            break
    assert isinstance(descriptor, property)

def test_query_xmlvaluefunctionparse_has_contentOption():
    assert hasattr(query_XMLValueFunctionParse, "contentOption")
    descriptor = None
    for klass in query_XMLValueFunctionParse.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctioncomment_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionComment)


def test_query_xmlvaluefunctioncomment_constructor_exists():
    assert callable(query_XMLValueFunctionComment.__init__)


def test_query_xmlvaluefunctioncomment_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionComment.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctioncomment_has_returningOption():
    assert hasattr(query_XMLValueFunctionComment, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionComment.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query_xmlvaluefunctionconcat_is_not_abstract():
    assert not inspect.isabstract(query_XMLValueFunctionConcat)


def test_query_xmlvaluefunctionconcat_constructor_exists():
    assert callable(query_XMLValueFunctionConcat.__init__)


def test_query_xmlvaluefunctionconcat_constructor_args():
    sig = inspect.signature(query_XMLValueFunctionConcat.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query_xmlvaluefunctionconcat_has_returningOption():
    assert hasattr(query_XMLValueFunctionConcat, "returningOption")
    descriptor = None
    for klass in query_XMLValueFunctionConcat.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)

def test_xmlcontenttype_exists():
    # Check that the Enumeration exists
    assert XMLContentType is not None

def test_xmlcontenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLContentType]
    expected_literals = [
        "DOCUMENT",
        "CONTENT",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLContentType"

def test_xmldeclarationtype_exists():
    # Check that the Enumeration exists
    assert XMLDeclarationType is not None

def test_xmldeclarationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLDeclarationType]
    expected_literals = [
        "EXCLUDING_XMLDECLARATION",
        "NONE",
        "INCLUDING_XMLDECLARATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLDeclarationType"

def test_xmlcontenttype2_exists():
    # Check that the Enumeration exists
    assert XMLContentType2 is not None

def test_xmlcontenttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLContentType2]
    expected_literals = [
        "CONTENT",
        "DOCUMENT",
        "SEQUENCE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLContentType2"

def test_xmlreturningtype_exists():
    # Check that the Enumeration exists
    assert XMLReturningType is not None

def test_xmlreturningtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLReturningType]
    expected_literals = [
        "RETURNING_CONTENT",
        "RETURNING_SEQUENCE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLReturningType"

def test_xmlpassingtype_exists():
    # Check that the Enumeration exists
    assert XMLPassingType is not None

def test_xmlpassingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLPassingType]
    expected_literals = [
        "NONE",
        "BY_REF",
        "BY_VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLPassingType"

def test_xmlemptyhandlingtype_exists():
    # Check that the Enumeration exists
    assert XMLEmptyHandlingType is not None

def test_xmlemptyhandlingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLEmptyHandlingType]
    expected_literals = [
        "NULL_ON_EMPTY",
        "NONE",
        "EMPTY_ON_EMPTY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLEmptyHandlingType"

def test_xmlnullhandlingtype_exists():
    # Check that the Enumeration exists
    assert XMLNullHandlingType is not None

def test_xmlnullhandlingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLNullHandlingType]
    expected_literals = [
        "NIL_ON_NO_CONTENT",
        "NULL_ON_NULL",
        "EMPTY_ON_NULL",
        "NONE",
        "NIL_ON_NULL",
        "ABSENT_ON_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLNullHandlingType"

def test_xmlwhitespacehandlingtype_exists():
    # Check that the Enumeration exists
    assert XMLWhitespaceHandlingType is not None

def test_xmlwhitespacehandlingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLWhitespaceHandlingType]
    expected_literals = [
        "PRESERE_WHITESPACE",
        "NONE",
        "STRIP_WHITESPACE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLWhitespaceHandlingType"


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
DataType_strategy = st.builds(
    DataType,
)
XMLValueFunctionValidateAccordingTo_strategy = st.builds(
    XMLValueFunctionValidateAccordingTo,
)
query_XMLValueFunctionValidateAccordingToIdentifier_strategy = st.builds(
    query_XMLValueFunctionValidateAccordingToIdentifier,
    registeredXMLSchemaName=
        safe_text,
    schemaName=
        safe_text
)
query_XMLValueFunctionValidateAccordingToURI_strategy = st.builds(
    query_XMLValueFunctionValidateAccordingToURI,
    noNamespace=
        st.booleans(),
    targetNamespaceURI=
        safe_text,
    schemaLocationURI=
        safe_text
)
XMLTableColumnDefinitionItem_strategy = st.builds(
    XMLTableColumnDefinitionItem,
)
query_XMLTableColumnDefinitionOrdinality_strategy = st.builds(
    query_XMLTableColumnDefinitionOrdinality,
)
query_XMLTableColumnDefinitionRegular_strategy = st.builds(
    query_XMLTableColumnDefinitionRegular,
    passingOption=
        safe_text,
    tableColumnPattern=
        safe_text
)
TableFunction_strategy = st.builds(
    TableFunction,
)
query_OrderBySpecification_strategy = st.builds(
    query_OrderBySpecification,
)
query_XMLTableFunction_strategy = st.builds(
    query_XMLTableFunction,
    tableRowPattern=
        safe_text
)
XMLPredicate_strategy = st.builds(
    XMLPredicate,
)
query_XMLPredicateDocument_strategy = st.builds(
    query_XMLPredicateDocument,
)
query_XMLPredicateExists_strategy = st.builds(
    query_XMLPredicateExists,
)
query_XMLPredicateValid_strategy = st.builds(
    query_XMLPredicateValid,
)
query_XMLPredicateContent_strategy = st.builds(
    query_XMLPredicateContent,
)
Predicate_strategy = st.builds(
    Predicate,
)
query_XMLPredicate_strategy = st.builds(
    query_XMLPredicate,
)
ValueExpressionCast_strategy = st.builds(
    ValueExpressionCast,
)
query_XMLValueExpressionCast_strategy = st.builds(
    query_XMLValueExpressionCast,
    passingMechanism=
        safe_text
)
SQLQueryObject_strategy = st.builds(
    SQLQueryObject,
)
query_XMLSerializeFunctionEncoding_strategy = st.builds(
    query_XMLSerializeFunctionEncoding,
    encodingName=
        safe_text
)
query_XMLValueFunctionValidateElement_strategy = st.builds(
    query_XMLValueFunctionValidateElement,
)
query_XMLAggregateSortSpecification_strategy = st.builds(
    query_XMLAggregateSortSpecification,
)
query_XMLNamespacesDeclaration_strategy = st.builds(
    query_XMLNamespacesDeclaration,
)
query_XMLValueFunctionValidateElementName_strategy = st.builds(
    query_XMLValueFunctionValidateElementName,
)
query_XMLTableColumnDefinitionItem_strategy = st.builds(
    query_XMLTableColumnDefinitionItem,
)
query_XMLQueryExpression_strategy = st.builds(
    query_XMLQueryExpression,
    xqueryExprContent=
        safe_text
)
query_XMLValueFunctionValidateElementNamespace_strategy = st.builds(
    query_XMLValueFunctionValidateElementNamespace,
    noNamespace=
        st.booleans(),
    namespaceURI=
        safe_text
)
query_XMLValueFunctionQueryReturning_strategy = st.builds(
    query_XMLValueFunctionQueryReturning,
    passingOption=
        safe_text,
    returningOption=
        safe_text
)
query_XMLValueFunctionValidateAccordingTo_strategy = st.builds(
    query_XMLValueFunctionValidateAccordingTo,
)
query_XMLQueryArgumentList_strategy = st.builds(
    query_XMLQueryArgumentList,
    passingMechanism=
        safe_text
)
query_XMLNamespaceDeclarationItem_strategy = st.builds(
    query_XMLNamespaceDeclarationItem,
    uri=
        safe_text
)
query_XMLValueFunctionElementContentList_strategy = st.builds(
    query_XMLValueFunctionElementContentList,
    nullHandlingOption=
        safe_text
)
XMLNamespaceDeclarationItem_strategy = st.builds(
    XMLNamespaceDeclarationItem,
)
query_XMLNamespaceDeclarationDefault_strategy = st.builds(
    query_XMLNamespaceDeclarationDefault,
    noDefault=
        st.booleans()
)
query_XMLNamespaceDeclarationPrefix_strategy = st.builds(
    query_XMLNamespaceDeclarationPrefix,
    prefix=
        safe_text
)
ValueExpressionFunction_strategy = st.builds(
    ValueExpressionFunction,
)
query_XMLAggregateFunction_strategy = st.builds(
    query_XMLAggregateFunction,
    returningOption=
        safe_text
)
query_XMLSerializeFunction_strategy = st.builds(
    query_XMLSerializeFunction,
    serializeVersion=
        safe_text,
    declarationOption=
        safe_text,
    contentOption=
        safe_text
)
query_XMLValueFunction_strategy = st.builds(
    query_XMLValueFunction,
)
query_XMLAttributesDeclaration_strategy = st.builds(
    query_XMLAttributesDeclaration,
)
query_QueryValueExpression_strategy = st.builds(
    query_QueryValueExpression,
)
QueryValueExpression_strategy = st.builds(
    QueryValueExpression,
)
query_XMLValueFunctionParseContent_strategy = st.builds(
    query_XMLValueFunctionParseContent,
)
query_XMLValueFunctionCommentContent_strategy = st.builds(
    query_XMLValueFunctionCommentContent,
)
query_XMLTableColumnDefinitionDefault_strategy = st.builds(
    query_XMLTableColumnDefinitionDefault,
)
query_XMLValueFunctionPIContent_strategy = st.builds(
    query_XMLValueFunctionPIContent,
)
query_XMLValueFunctionValidateContent_strategy = st.builds(
    query_XMLValueFunctionValidateContent,
)
query_XMLQueryArgumentItem_strategy = st.builds(
    query_XMLQueryArgumentItem,
    passingMechanism=
        safe_text
)
query_XMLValueFunctionDocumentContent_strategy = st.builds(
    query_XMLValueFunctionDocumentContent,
)
query_XMLValueFunctionTextContent_strategy = st.builds(
    query_XMLValueFunctionTextContent,
)
query_XMLValueFunctionForestContentItem_strategy = st.builds(
    query_XMLValueFunctionForestContentItem,
)
query_XMLSerializeFunctionTarget_strategy = st.builds(
    query_XMLSerializeFunctionTarget,
)
query_XMLValueFunctionElementContentItem_strategy = st.builds(
    query_XMLValueFunctionElementContentItem,
)
query_XMLValueFunctionConcatContentItem_strategy = st.builds(
    query_XMLValueFunctionConcatContentItem,
)
query_XMLAttributeDeclarationItem_strategy = st.builds(
    query_XMLAttributeDeclarationItem,
)
XMLValueFunction_strategy = st.builds(
    XMLValueFunction,
)
query_XMLValueFunctionElement_strategy = st.builds(
    query_XMLValueFunctionElement,
    elementName=
        safe_text,
    returningOption=
        safe_text
)
query_XMLValueFunctionDocument_strategy = st.builds(
    query_XMLValueFunctionDocument,
    returningOption=
        safe_text
)
query_XMLValueFunctionForest_strategy = st.builds(
    query_XMLValueFunctionForest,
    returningOption=
        safe_text,
    nullHandlingOption=
        safe_text
)
query_XMLValueFunctionText_strategy = st.builds(
    query_XMLValueFunctionText,
    returningOption=
        safe_text
)
query_XMLValueFunctionValidate_strategy = st.builds(
    query_XMLValueFunctionValidate,
    contentOption=
        safe_text
)
query_XMLValueFunctionPI_strategy = st.builds(
    query_XMLValueFunctionPI,
    targetName=
        safe_text,
    returningOption=
        safe_text
)
query_XMLValueFunctionQuery_strategy = st.builds(
    query_XMLValueFunctionQuery,
    emptyHandlingOption=
        safe_text
)
query_XMLValueFunctionParse_strategy = st.builds(
    query_XMLValueFunctionParse,
    whitespaceHandlingOption=
        safe_text,
    contentOption=
        safe_text
)
query_XMLValueFunctionComment_strategy = st.builds(
    query_XMLValueFunctionComment,
    returningOption=
        safe_text
)
query_XMLValueFunctionConcat_strategy = st.builds(
    query_XMLValueFunctionConcat,
    returningOption=
        safe_text
)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=XMLValueFunctionValidateAccordingTo_strategy)
@settings(max_examples=50)
def test_xmlvaluefunctionvalidateaccordingto_instantiation(instance):
    assert isinstance(instance, XMLValueFunctionValidateAccordingTo)

@given(instance=query_XMLValueFunctionValidateAccordingToIdentifier_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateAccordingToIdentifier)



@given(instance=query_XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_registeredXMLSchemaName_setter(instance):
    original = instance.registeredXMLSchemaName
    instance.registeredXMLSchemaName = original
    assert instance.registeredXMLSchemaName == original



@given(instance=query_XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query_xmlvaluefunctionvalidateaccordingtoidentifier_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=query_XMLValueFunctionValidateAccordingToURI_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateaccordingtouri_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateAccordingToURI)



@given(instance=query_XMLValueFunctionValidateAccordingToURI_strategy)
def test_query_xmlvaluefunctionvalidateaccordingtouri_noNamespace_setter(instance):
    original = instance.noNamespace
    instance.noNamespace = original
    assert instance.noNamespace == original



@given(instance=query_XMLValueFunctionValidateAccordingToURI_strategy)
def test_query_xmlvaluefunctionvalidateaccordingtouri_targetNamespaceURI_setter(instance):
    original = instance.targetNamespaceURI
    instance.targetNamespaceURI = original
    assert instance.targetNamespaceURI == original



@given(instance=query_XMLValueFunctionValidateAccordingToURI_strategy)
def test_query_xmlvaluefunctionvalidateaccordingtouri_schemaLocationURI_setter(instance):
    original = instance.schemaLocationURI
    instance.schemaLocationURI = original
    assert instance.schemaLocationURI == original

@given(instance=XMLTableColumnDefinitionItem_strategy)
@settings(max_examples=50)
def test_xmltablecolumndefinitionitem_instantiation(instance):
    assert isinstance(instance, XMLTableColumnDefinitionItem)

@given(instance=query_XMLTableColumnDefinitionOrdinality_strategy)
@settings(max_examples=50)
def test_query_xmltablecolumndefinitionordinality_instantiation(instance):
    assert isinstance(instance, query_XMLTableColumnDefinitionOrdinality)

@given(instance=query_XMLTableColumnDefinitionRegular_strategy)
@settings(max_examples=50)
def test_query_xmltablecolumndefinitionregular_instantiation(instance):
    assert isinstance(instance, query_XMLTableColumnDefinitionRegular)



@given(instance=query_XMLTableColumnDefinitionRegular_strategy)
def test_query_xmltablecolumndefinitionregular_passingOption_setter(instance):
    original = instance.passingOption
    instance.passingOption = original
    assert instance.passingOption == original



@given(instance=query_XMLTableColumnDefinitionRegular_strategy)
def test_query_xmltablecolumndefinitionregular_tableColumnPattern_setter(instance):
    original = instance.tableColumnPattern
    instance.tableColumnPattern = original
    assert instance.tableColumnPattern == original

@given(instance=TableFunction_strategy)
@settings(max_examples=50)
def test_tablefunction_instantiation(instance):
    assert isinstance(instance, TableFunction)

@given(instance=query_OrderBySpecification_strategy)
@settings(max_examples=50)
def test_query_orderbyspecification_instantiation(instance):
    assert isinstance(instance, query_OrderBySpecification)

@given(instance=query_XMLTableFunction_strategy)
@settings(max_examples=50)
def test_query_xmltablefunction_instantiation(instance):
    assert isinstance(instance, query_XMLTableFunction)



@given(instance=query_XMLTableFunction_strategy)
def test_query_xmltablefunction_tableRowPattern_setter(instance):
    original = instance.tableRowPattern
    instance.tableRowPattern = original
    assert instance.tableRowPattern == original

@given(instance=XMLPredicate_strategy)
@settings(max_examples=50)
def test_xmlpredicate_instantiation(instance):
    assert isinstance(instance, XMLPredicate)

@given(instance=query_XMLPredicateDocument_strategy)
@settings(max_examples=50)
def test_query_xmlpredicatedocument_instantiation(instance):
    assert isinstance(instance, query_XMLPredicateDocument)

@given(instance=query_XMLPredicateExists_strategy)
@settings(max_examples=50)
def test_query_xmlpredicateexists_instantiation(instance):
    assert isinstance(instance, query_XMLPredicateExists)

@given(instance=query_XMLPredicateValid_strategy)
@settings(max_examples=50)
def test_query_xmlpredicatevalid_instantiation(instance):
    assert isinstance(instance, query_XMLPredicateValid)

@given(instance=query_XMLPredicateContent_strategy)
@settings(max_examples=50)
def test_query_xmlpredicatecontent_instantiation(instance):
    assert isinstance(instance, query_XMLPredicateContent)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=query_XMLPredicate_strategy)
@settings(max_examples=50)
def test_query_xmlpredicate_instantiation(instance):
    assert isinstance(instance, query_XMLPredicate)

@given(instance=ValueExpressionCast_strategy)
@settings(max_examples=50)
def test_valueexpressioncast_instantiation(instance):
    assert isinstance(instance, ValueExpressionCast)

@given(instance=query_XMLValueExpressionCast_strategy)
@settings(max_examples=50)
def test_query_xmlvalueexpressioncast_instantiation(instance):
    assert isinstance(instance, query_XMLValueExpressionCast)



@given(instance=query_XMLValueExpressionCast_strategy)
def test_query_xmlvalueexpressioncast_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=SQLQueryObject_strategy)
@settings(max_examples=50)
def test_sqlqueryobject_instantiation(instance):
    assert isinstance(instance, SQLQueryObject)

@given(instance=query_XMLSerializeFunctionEncoding_strategy)
@settings(max_examples=50)
def test_query_xmlserializefunctionencoding_instantiation(instance):
    assert isinstance(instance, query_XMLSerializeFunctionEncoding)



@given(instance=query_XMLSerializeFunctionEncoding_strategy)
def test_query_xmlserializefunctionencoding_encodingName_setter(instance):
    original = instance.encodingName
    instance.encodingName = original
    assert instance.encodingName == original

@given(instance=query_XMLValueFunctionValidateElement_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateelement_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateElement)

@given(instance=query_XMLAggregateSortSpecification_strategy)
@settings(max_examples=50)
def test_query_xmlaggregatesortspecification_instantiation(instance):
    assert isinstance(instance, query_XMLAggregateSortSpecification)

@given(instance=query_XMLNamespacesDeclaration_strategy)
@settings(max_examples=50)
def test_query_xmlnamespacesdeclaration_instantiation(instance):
    assert isinstance(instance, query_XMLNamespacesDeclaration)

@given(instance=query_XMLValueFunctionValidateElementName_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateelementname_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateElementName)

@given(instance=query_XMLTableColumnDefinitionItem_strategy)
@settings(max_examples=50)
def test_query_xmltablecolumndefinitionitem_instantiation(instance):
    assert isinstance(instance, query_XMLTableColumnDefinitionItem)

@given(instance=query_XMLQueryExpression_strategy)
@settings(max_examples=50)
def test_query_xmlqueryexpression_instantiation(instance):
    assert isinstance(instance, query_XMLQueryExpression)



@given(instance=query_XMLQueryExpression_strategy)
def test_query_xmlqueryexpression_xqueryExprContent_setter(instance):
    original = instance.xqueryExprContent
    instance.xqueryExprContent = original
    assert instance.xqueryExprContent == original

@given(instance=query_XMLValueFunctionValidateElementNamespace_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateelementnamespace_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateElementNamespace)



@given(instance=query_XMLValueFunctionValidateElementNamespace_strategy)
def test_query_xmlvaluefunctionvalidateelementnamespace_noNamespace_setter(instance):
    original = instance.noNamespace
    instance.noNamespace = original
    assert instance.noNamespace == original



@given(instance=query_XMLValueFunctionValidateElementNamespace_strategy)
def test_query_xmlvaluefunctionvalidateelementnamespace_namespaceURI_setter(instance):
    original = instance.namespaceURI
    instance.namespaceURI = original
    assert instance.namespaceURI == original

@given(instance=query_XMLValueFunctionQueryReturning_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionqueryreturning_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionQueryReturning)



@given(instance=query_XMLValueFunctionQueryReturning_strategy)
def test_query_xmlvaluefunctionqueryreturning_passingOption_setter(instance):
    original = instance.passingOption
    instance.passingOption = original
    assert instance.passingOption == original



@given(instance=query_XMLValueFunctionQueryReturning_strategy)
def test_query_xmlvaluefunctionqueryreturning_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionValidateAccordingTo_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidateaccordingto_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateAccordingTo)

@given(instance=query_XMLQueryArgumentList_strategy)
@settings(max_examples=50)
def test_query_xmlqueryargumentlist_instantiation(instance):
    assert isinstance(instance, query_XMLQueryArgumentList)



@given(instance=query_XMLQueryArgumentList_strategy)
def test_query_xmlqueryargumentlist_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=query_XMLNamespaceDeclarationItem_strategy)
@settings(max_examples=50)
def test_query_xmlnamespacedeclarationitem_instantiation(instance):
    assert isinstance(instance, query_XMLNamespaceDeclarationItem)



@given(instance=query_XMLNamespaceDeclarationItem_strategy)
def test_query_xmlnamespacedeclarationitem_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=query_XMLValueFunctionElementContentList_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionelementcontentlist_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionElementContentList)



@given(instance=query_XMLValueFunctionElementContentList_strategy)
def test_query_xmlvaluefunctionelementcontentlist_nullHandlingOption_setter(instance):
    original = instance.nullHandlingOption
    instance.nullHandlingOption = original
    assert instance.nullHandlingOption == original

@given(instance=XMLNamespaceDeclarationItem_strategy)
@settings(max_examples=50)
def test_xmlnamespacedeclarationitem_instantiation(instance):
    assert isinstance(instance, XMLNamespaceDeclarationItem)

@given(instance=query_XMLNamespaceDeclarationDefault_strategy)
@settings(max_examples=50)
def test_query_xmlnamespacedeclarationdefault_instantiation(instance):
    assert isinstance(instance, query_XMLNamespaceDeclarationDefault)



@given(instance=query_XMLNamespaceDeclarationDefault_strategy)
def test_query_xmlnamespacedeclarationdefault_noDefault_setter(instance):
    original = instance.noDefault
    instance.noDefault = original
    assert instance.noDefault == original

@given(instance=query_XMLNamespaceDeclarationPrefix_strategy)
@settings(max_examples=50)
def test_query_xmlnamespacedeclarationprefix_instantiation(instance):
    assert isinstance(instance, query_XMLNamespaceDeclarationPrefix)



@given(instance=query_XMLNamespaceDeclarationPrefix_strategy)
def test_query_xmlnamespacedeclarationprefix_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=ValueExpressionFunction_strategy)
@settings(max_examples=50)
def test_valueexpressionfunction_instantiation(instance):
    assert isinstance(instance, ValueExpressionFunction)

@given(instance=query_XMLAggregateFunction_strategy)
@settings(max_examples=50)
def test_query_xmlaggregatefunction_instantiation(instance):
    assert isinstance(instance, query_XMLAggregateFunction)



@given(instance=query_XMLAggregateFunction_strategy)
def test_query_xmlaggregatefunction_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLSerializeFunction_strategy)
@settings(max_examples=50)
def test_query_xmlserializefunction_instantiation(instance):
    assert isinstance(instance, query_XMLSerializeFunction)



@given(instance=query_XMLSerializeFunction_strategy)
def test_query_xmlserializefunction_serializeVersion_setter(instance):
    original = instance.serializeVersion
    instance.serializeVersion = original
    assert instance.serializeVersion == original



@given(instance=query_XMLSerializeFunction_strategy)
def test_query_xmlserializefunction_declarationOption_setter(instance):
    original = instance.declarationOption
    instance.declarationOption = original
    assert instance.declarationOption == original



@given(instance=query_XMLSerializeFunction_strategy)
def test_query_xmlserializefunction_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query_XMLValueFunction_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunction_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunction)

@given(instance=query_XMLAttributesDeclaration_strategy)
@settings(max_examples=50)
def test_query_xmlattributesdeclaration_instantiation(instance):
    assert isinstance(instance, query_XMLAttributesDeclaration)

@given(instance=query_QueryValueExpression_strategy)
@settings(max_examples=50)
def test_query_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, query_QueryValueExpression)

@given(instance=QueryValueExpression_strategy)
@settings(max_examples=50)
def test_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, QueryValueExpression)

@given(instance=query_XMLValueFunctionParseContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionparsecontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionParseContent)

@given(instance=query_XMLValueFunctionCommentContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctioncommentcontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionCommentContent)

@given(instance=query_XMLTableColumnDefinitionDefault_strategy)
@settings(max_examples=50)
def test_query_xmltablecolumndefinitiondefault_instantiation(instance):
    assert isinstance(instance, query_XMLTableColumnDefinitionDefault)

@given(instance=query_XMLValueFunctionPIContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionpicontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionPIContent)

@given(instance=query_XMLValueFunctionValidateContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidatecontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidateContent)

@given(instance=query_XMLQueryArgumentItem_strategy)
@settings(max_examples=50)
def test_query_xmlqueryargumentitem_instantiation(instance):
    assert isinstance(instance, query_XMLQueryArgumentItem)



@given(instance=query_XMLQueryArgumentItem_strategy)
def test_query_xmlqueryargumentitem_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=query_XMLValueFunctionDocumentContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctiondocumentcontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionDocumentContent)

@given(instance=query_XMLValueFunctionTextContent_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctiontextcontent_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionTextContent)

@given(instance=query_XMLValueFunctionForestContentItem_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionforestcontentitem_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionForestContentItem)

@given(instance=query_XMLSerializeFunctionTarget_strategy)
@settings(max_examples=50)
def test_query_xmlserializefunctiontarget_instantiation(instance):
    assert isinstance(instance, query_XMLSerializeFunctionTarget)

@given(instance=query_XMLValueFunctionElementContentItem_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionelementcontentitem_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionElementContentItem)

@given(instance=query_XMLValueFunctionConcatContentItem_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionconcatcontentitem_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionConcatContentItem)

@given(instance=query_XMLAttributeDeclarationItem_strategy)
@settings(max_examples=50)
def test_query_xmlattributedeclarationitem_instantiation(instance):
    assert isinstance(instance, query_XMLAttributeDeclarationItem)

@given(instance=XMLValueFunction_strategy)
@settings(max_examples=50)
def test_xmlvaluefunction_instantiation(instance):
    assert isinstance(instance, XMLValueFunction)

@given(instance=query_XMLValueFunctionElement_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionelement_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionElement)



@given(instance=query_XMLValueFunctionElement_strategy)
def test_query_xmlvaluefunctionelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original



@given(instance=query_XMLValueFunctionElement_strategy)
def test_query_xmlvaluefunctionelement_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionDocument_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctiondocument_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionDocument)



@given(instance=query_XMLValueFunctionDocument_strategy)
def test_query_xmlvaluefunctiondocument_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionForest_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionforest_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionForest)



@given(instance=query_XMLValueFunctionForest_strategy)
def test_query_xmlvaluefunctionforest_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original



@given(instance=query_XMLValueFunctionForest_strategy)
def test_query_xmlvaluefunctionforest_nullHandlingOption_setter(instance):
    original = instance.nullHandlingOption
    instance.nullHandlingOption = original
    assert instance.nullHandlingOption == original

@given(instance=query_XMLValueFunctionText_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctiontext_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionText)



@given(instance=query_XMLValueFunctionText_strategy)
def test_query_xmlvaluefunctiontext_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionValidate_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionvalidate_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionValidate)



@given(instance=query_XMLValueFunctionValidate_strategy)
def test_query_xmlvaluefunctionvalidate_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query_XMLValueFunctionPI_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionpi_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionPI)



@given(instance=query_XMLValueFunctionPI_strategy)
def test_query_xmlvaluefunctionpi_targetName_setter(instance):
    original = instance.targetName
    instance.targetName = original
    assert instance.targetName == original



@given(instance=query_XMLValueFunctionPI_strategy)
def test_query_xmlvaluefunctionpi_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionQuery_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionquery_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionQuery)



@given(instance=query_XMLValueFunctionQuery_strategy)
def test_query_xmlvaluefunctionquery_emptyHandlingOption_setter(instance):
    original = instance.emptyHandlingOption
    instance.emptyHandlingOption = original
    assert instance.emptyHandlingOption == original

@given(instance=query_XMLValueFunctionParse_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionparse_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionParse)



@given(instance=query_XMLValueFunctionParse_strategy)
def test_query_xmlvaluefunctionparse_whitespaceHandlingOption_setter(instance):
    original = instance.whitespaceHandlingOption
    instance.whitespaceHandlingOption = original
    assert instance.whitespaceHandlingOption == original



@given(instance=query_XMLValueFunctionParse_strategy)
def test_query_xmlvaluefunctionparse_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query_XMLValueFunctionComment_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctioncomment_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionComment)



@given(instance=query_XMLValueFunctionComment_strategy)
def test_query_xmlvaluefunctioncomment_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query_XMLValueFunctionConcat_strategy)
@settings(max_examples=50)
def test_query_xmlvaluefunctionconcat_instantiation(instance):
    assert isinstance(instance, query_XMLValueFunctionConcat)



@given(instance=query_XMLValueFunctionConcat_strategy)
def test_query_xmlvaluefunctionconcat_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

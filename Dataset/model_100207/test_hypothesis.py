import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataType,
    XMLValueFunctionValidateAccordingTo,
    query::XMLValueFunctionValidateAccordingToIdentifier,
    query::XMLValueFunctionValidateAccordingToURI,
    XMLTableColumnDefinitionItem,
    query::XMLTableColumnDefinitionOrdinality,
    query::XMLTableColumnDefinitionRegular,
    TableFunction,
    query::OrderBySpecification,
    query::XMLTableFunction,
    XMLPredicate,
    query::XMLPredicateValid,
    query::XMLPredicateExists,
    query::XMLPredicateDocument,
    query::XMLPredicateContent,
    Predicate,
    query::XMLPredicate,
    ValueExpressionCast,
    query::XMLValueExpressionCast,
    SQLQueryObject,
    query::XMLQueryArgumentList,
    query::XMLValueFunctionQueryReturning,
    query::XMLQueryExpression,
    query::XMLValueFunctionValidateAccordingTo,
    query::XMLTableColumnDefinitionItem,
    query::XMLValueFunctionValidateElementNamespace,
    query::XMLAggregateSortSpecification,
    query::XMLNamespacesDeclaration,
    query::XMLSerializeFunctionEncoding,
    query::XMLValueFunctionValidateElement,
    query::XMLValueFunctionValidateElementName,
    query::XMLNamespaceDeclarationItem,
    query::XMLValueFunctionElementContentList,
    XMLNamespaceDeclarationItem,
    query::XMLNamespaceDeclarationDefault,
    query::XMLNamespaceDeclarationPrefix,
    ValueExpressionFunction,
    query::XMLSerializeFunction,
    query::XMLAggregateFunction,
    query::XMLValueFunction,
    query::XMLAttributesDeclaration,
    query::QueryValueExpression,
    QueryValueExpression,
    query::XMLValueFunctionConcatContentItem,
    query::XMLValueFunctionCommentContent,
    query::XMLValueFunctionParseContent,
    query::XMLValueFunctionElementContentItem,
    query::XMLValueFunctionTextContent,
    query::XMLValueFunctionValidateContent,
    query::XMLTableColumnDefinitionDefault,
    query::XMLSerializeFunctionTarget,
    query::XMLQueryArgumentItem,
    query::XMLValueFunctionPIContent,
    query::XMLValueFunctionDocumentContent,
    query::XMLValueFunctionForestContentItem,
    query::XMLAttributeDeclarationItem,
    XMLValueFunction,
    query::XMLValueFunctionValidate,
    query::XMLValueFunctionPI,
    query::XMLValueFunctionQuery,
    query::XMLValueFunctionParse,
    query::XMLValueFunctionElement,
    query::XMLValueFunctionComment,
    query::XMLValueFunctionText,
    query::XMLValueFunctionDocument,
    query::XMLValueFunctionForest,
    query::XMLValueFunctionConcat,
    XMLDeclarationType,
    XMLPassingType,
    XMLContentType,
    XMLNullHandlingType,
    XMLEmptyHandlingType,
    XMLReturningType,
    XMLWhitespaceHandlingType,
    XMLContentType2,
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



def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateAccordingToIdentifier)


def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_constructor_exists():
    assert callable(query::XMLValueFunctionValidateAccordingToIdentifier.__init__)


def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateAccordingToIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "registeredXMLSchemaName" in params, "Missing parameter 'registeredXMLSchemaName'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_has_registeredXMLSchemaName():
    assert hasattr(query::XMLValueFunctionValidateAccordingToIdentifier, "registeredXMLSchemaName")
    descriptor = None
    for klass in query::XMLValueFunctionValidateAccordingToIdentifier.__mro__:
        if "registeredXMLSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["registeredXMLSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_has_schemaName():
    assert hasattr(query::XMLValueFunctionValidateAccordingToIdentifier, "schemaName")
    descriptor = None
    for klass in query::XMLValueFunctionValidateAccordingToIdentifier.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionvalidateaccordingtouri_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateAccordingToURI)


def test_query::xmlvaluefunctionvalidateaccordingtouri_constructor_exists():
    assert callable(query::XMLValueFunctionValidateAccordingToURI.__init__)


def test_query::xmlvaluefunctionvalidateaccordingtouri_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateAccordingToURI.__init__)
    params = list(sig.parameters.keys())
    assert "noNamespace" in params, "Missing parameter 'noNamespace'"
    assert "schemaLocationURI" in params, "Missing parameter 'schemaLocationURI'"
    assert "targetNamespaceURI" in params, "Missing parameter 'targetNamespaceURI'"

def test_query::xmlvaluefunctionvalidateaccordingtouri_has_noNamespace():
    assert hasattr(query::XMLValueFunctionValidateAccordingToURI, "noNamespace")
    descriptor = None
    for klass in query::XMLValueFunctionValidateAccordingToURI.__mro__:
        if "noNamespace" in klass.__dict__:
            descriptor = klass.__dict__["noNamespace"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionvalidateaccordingtouri_has_schemaLocationURI():
    assert hasattr(query::XMLValueFunctionValidateAccordingToURI, "schemaLocationURI")
    descriptor = None
    for klass in query::XMLValueFunctionValidateAccordingToURI.__mro__:
        if "schemaLocationURI" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocationURI"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionvalidateaccordingtouri_has_targetNamespaceURI():
    assert hasattr(query::XMLValueFunctionValidateAccordingToURI, "targetNamespaceURI")
    descriptor = None
    for klass in query::XMLValueFunctionValidateAccordingToURI.__mro__:
        if "targetNamespaceURI" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespaceURI"]
            break
    assert isinstance(descriptor, property)



def test_xmltablecolumndefinitionitem_is_not_abstract():
    assert not inspect.isabstract(XMLTableColumnDefinitionItem)


def test_xmltablecolumndefinitionitem_constructor_exists():
    assert callable(XMLTableColumnDefinitionItem.__init__)


def test_xmltablecolumndefinitionitem_constructor_args():
    sig = inspect.signature(XMLTableColumnDefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_query::xmltablecolumndefinitionordinality_is_not_abstract():
    assert not inspect.isabstract(query::XMLTableColumnDefinitionOrdinality)


def test_query::xmltablecolumndefinitionordinality_constructor_exists():
    assert callable(query::XMLTableColumnDefinitionOrdinality.__init__)


def test_query::xmltablecolumndefinitionordinality_constructor_args():
    sig = inspect.signature(query::XMLTableColumnDefinitionOrdinality.__init__)
    params = list(sig.parameters.keys())



def test_query::xmltablecolumndefinitionregular_is_not_abstract():
    assert not inspect.isabstract(query::XMLTableColumnDefinitionRegular)


def test_query::xmltablecolumndefinitionregular_constructor_exists():
    assert callable(query::XMLTableColumnDefinitionRegular.__init__)


def test_query::xmltablecolumndefinitionregular_constructor_args():
    sig = inspect.signature(query::XMLTableColumnDefinitionRegular.__init__)
    params = list(sig.parameters.keys())
    assert "passingOption" in params, "Missing parameter 'passingOption'"
    assert "tableColumnPattern" in params, "Missing parameter 'tableColumnPattern'"

def test_query::xmltablecolumndefinitionregular_has_passingOption():
    assert hasattr(query::XMLTableColumnDefinitionRegular, "passingOption")
    descriptor = None
    for klass in query::XMLTableColumnDefinitionRegular.__mro__:
        if "passingOption" in klass.__dict__:
            descriptor = klass.__dict__["passingOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmltablecolumndefinitionregular_has_tableColumnPattern():
    assert hasattr(query::XMLTableColumnDefinitionRegular, "tableColumnPattern")
    descriptor = None
    for klass in query::XMLTableColumnDefinitionRegular.__mro__:
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



def test_query::orderbyspecification_is_not_abstract():
    assert not inspect.isabstract(query::OrderBySpecification)


def test_query::orderbyspecification_constructor_exists():
    assert callable(query::OrderBySpecification.__init__)


def test_query::orderbyspecification_constructor_args():
    sig = inspect.signature(query::OrderBySpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::xmltablefunction_is_not_abstract():
    assert not inspect.isabstract(query::XMLTableFunction)


def test_query::xmltablefunction_constructor_exists():
    assert callable(query::XMLTableFunction.__init__)


def test_query::xmltablefunction_constructor_args():
    sig = inspect.signature(query::XMLTableFunction.__init__)
    params = list(sig.parameters.keys())
    assert "tableRowPattern" in params, "Missing parameter 'tableRowPattern'"

def test_query::xmltablefunction_has_tableRowPattern():
    assert hasattr(query::XMLTableFunction, "tableRowPattern")
    descriptor = None
    for klass in query::XMLTableFunction.__mro__:
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



def test_query::xmlpredicatevalid_is_not_abstract():
    assert not inspect.isabstract(query::XMLPredicateValid)


def test_query::xmlpredicatevalid_constructor_exists():
    assert callable(query::XMLPredicateValid.__init__)


def test_query::xmlpredicatevalid_constructor_args():
    sig = inspect.signature(query::XMLPredicateValid.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlpredicateexists_is_not_abstract():
    assert not inspect.isabstract(query::XMLPredicateExists)


def test_query::xmlpredicateexists_constructor_exists():
    assert callable(query::XMLPredicateExists.__init__)


def test_query::xmlpredicateexists_constructor_args():
    sig = inspect.signature(query::XMLPredicateExists.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlpredicatedocument_is_not_abstract():
    assert not inspect.isabstract(query::XMLPredicateDocument)


def test_query::xmlpredicatedocument_constructor_exists():
    assert callable(query::XMLPredicateDocument.__init__)


def test_query::xmlpredicatedocument_constructor_args():
    sig = inspect.signature(query::XMLPredicateDocument.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlpredicatecontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLPredicateContent)


def test_query::xmlpredicatecontent_constructor_exists():
    assert callable(query::XMLPredicateContent.__init__)


def test_query::xmlpredicatecontent_constructor_args():
    sig = inspect.signature(query::XMLPredicateContent.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlpredicate_is_not_abstract():
    assert not inspect.isabstract(query::XMLPredicate)


def test_query::xmlpredicate_constructor_exists():
    assert callable(query::XMLPredicate.__init__)


def test_query::xmlpredicate_constructor_args():
    sig = inspect.signature(query::XMLPredicate.__init__)
    params = list(sig.parameters.keys())



def test_valueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionCast)


def test_valueexpressioncast_constructor_exists():
    assert callable(ValueExpressionCast.__init__)


def test_valueexpressioncast_constructor_args():
    sig = inspect.signature(ValueExpressionCast.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvalueexpressioncast_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueExpressionCast)


def test_query::xmlvalueexpressioncast_constructor_exists():
    assert callable(query::XMLValueExpressionCast.__init__)


def test_query::xmlvalueexpressioncast_constructor_args():
    sig = inspect.signature(query::XMLValueExpressionCast.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query::xmlvalueexpressioncast_has_passingMechanism():
    assert hasattr(query::XMLValueExpressionCast, "passingMechanism")
    descriptor = None
    for klass in query::XMLValueExpressionCast.__mro__:
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



def test_query::xmlqueryargumentlist_is_not_abstract():
    assert not inspect.isabstract(query::XMLQueryArgumentList)


def test_query::xmlqueryargumentlist_constructor_exists():
    assert callable(query::XMLQueryArgumentList.__init__)


def test_query::xmlqueryargumentlist_constructor_args():
    sig = inspect.signature(query::XMLQueryArgumentList.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query::xmlqueryargumentlist_has_passingMechanism():
    assert hasattr(query::XMLQueryArgumentList, "passingMechanism")
    descriptor = None
    for klass in query::XMLQueryArgumentList.__mro__:
        if "passingMechanism" in klass.__dict__:
            descriptor = klass.__dict__["passingMechanism"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionqueryreturning_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionQueryReturning)


def test_query::xmlvaluefunctionqueryreturning_constructor_exists():
    assert callable(query::XMLValueFunctionQueryReturning.__init__)


def test_query::xmlvaluefunctionqueryreturning_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionQueryReturning.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"
    assert "passingOption" in params, "Missing parameter 'passingOption'"

def test_query::xmlvaluefunctionqueryreturning_has_returningOption():
    assert hasattr(query::XMLValueFunctionQueryReturning, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionQueryReturning.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionqueryreturning_has_passingOption():
    assert hasattr(query::XMLValueFunctionQueryReturning, "passingOption")
    descriptor = None
    for klass in query::XMLValueFunctionQueryReturning.__mro__:
        if "passingOption" in klass.__dict__:
            descriptor = klass.__dict__["passingOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlqueryexpression_is_not_abstract():
    assert not inspect.isabstract(query::XMLQueryExpression)


def test_query::xmlqueryexpression_constructor_exists():
    assert callable(query::XMLQueryExpression.__init__)


def test_query::xmlqueryexpression_constructor_args():
    sig = inspect.signature(query::XMLQueryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "xqueryExprContent" in params, "Missing parameter 'xqueryExprContent'"

def test_query::xmlqueryexpression_has_xqueryExprContent():
    assert hasattr(query::XMLQueryExpression, "xqueryExprContent")
    descriptor = None
    for klass in query::XMLQueryExpression.__mro__:
        if "xqueryExprContent" in klass.__dict__:
            descriptor = klass.__dict__["xqueryExprContent"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionvalidateaccordingto_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateAccordingTo)


def test_query::xmlvaluefunctionvalidateaccordingto_constructor_exists():
    assert callable(query::XMLValueFunctionValidateAccordingTo.__init__)


def test_query::xmlvaluefunctionvalidateaccordingto_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateAccordingTo.__init__)
    params = list(sig.parameters.keys())



def test_query::xmltablecolumndefinitionitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLTableColumnDefinitionItem)


def test_query::xmltablecolumndefinitionitem_constructor_exists():
    assert callable(query::XMLTableColumnDefinitionItem.__init__)


def test_query::xmltablecolumndefinitionitem_constructor_args():
    sig = inspect.signature(query::XMLTableColumnDefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionvalidateelementnamespace_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateElementNamespace)


def test_query::xmlvaluefunctionvalidateelementnamespace_constructor_exists():
    assert callable(query::XMLValueFunctionValidateElementNamespace.__init__)


def test_query::xmlvaluefunctionvalidateelementnamespace_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateElementNamespace.__init__)
    params = list(sig.parameters.keys())
    assert "noNamespace" in params, "Missing parameter 'noNamespace'"
    assert "namespaceURI" in params, "Missing parameter 'namespaceURI'"

def test_query::xmlvaluefunctionvalidateelementnamespace_has_noNamespace():
    assert hasattr(query::XMLValueFunctionValidateElementNamespace, "noNamespace")
    descriptor = None
    for klass in query::XMLValueFunctionValidateElementNamespace.__mro__:
        if "noNamespace" in klass.__dict__:
            descriptor = klass.__dict__["noNamespace"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionvalidateelementnamespace_has_namespaceURI():
    assert hasattr(query::XMLValueFunctionValidateElementNamespace, "namespaceURI")
    descriptor = None
    for klass in query::XMLValueFunctionValidateElementNamespace.__mro__:
        if "namespaceURI" in klass.__dict__:
            descriptor = klass.__dict__["namespaceURI"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlaggregatesortspecification_is_not_abstract():
    assert not inspect.isabstract(query::XMLAggregateSortSpecification)


def test_query::xmlaggregatesortspecification_constructor_exists():
    assert callable(query::XMLAggregateSortSpecification.__init__)


def test_query::xmlaggregatesortspecification_constructor_args():
    sig = inspect.signature(query::XMLAggregateSortSpecification.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlnamespacesdeclaration_is_not_abstract():
    assert not inspect.isabstract(query::XMLNamespacesDeclaration)


def test_query::xmlnamespacesdeclaration_constructor_exists():
    assert callable(query::XMLNamespacesDeclaration.__init__)


def test_query::xmlnamespacesdeclaration_constructor_args():
    sig = inspect.signature(query::XMLNamespacesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlserializefunctionencoding_is_not_abstract():
    assert not inspect.isabstract(query::XMLSerializeFunctionEncoding)


def test_query::xmlserializefunctionencoding_constructor_exists():
    assert callable(query::XMLSerializeFunctionEncoding.__init__)


def test_query::xmlserializefunctionencoding_constructor_args():
    sig = inspect.signature(query::XMLSerializeFunctionEncoding.__init__)
    params = list(sig.parameters.keys())
    assert "encodingName" in params, "Missing parameter 'encodingName'"

def test_query::xmlserializefunctionencoding_has_encodingName():
    assert hasattr(query::XMLSerializeFunctionEncoding, "encodingName")
    descriptor = None
    for klass in query::XMLSerializeFunctionEncoding.__mro__:
        if "encodingName" in klass.__dict__:
            descriptor = klass.__dict__["encodingName"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionvalidateelement_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateElement)


def test_query::xmlvaluefunctionvalidateelement_constructor_exists():
    assert callable(query::XMLValueFunctionValidateElement.__init__)


def test_query::xmlvaluefunctionvalidateelement_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateElement.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionvalidateelementname_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateElementName)


def test_query::xmlvaluefunctionvalidateelementname_constructor_exists():
    assert callable(query::XMLValueFunctionValidateElementName.__init__)


def test_query::xmlvaluefunctionvalidateelementname_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateElementName.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlnamespacedeclarationitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLNamespaceDeclarationItem)


def test_query::xmlnamespacedeclarationitem_constructor_exists():
    assert callable(query::XMLNamespaceDeclarationItem.__init__)


def test_query::xmlnamespacedeclarationitem_constructor_args():
    sig = inspect.signature(query::XMLNamespaceDeclarationItem.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_query::xmlnamespacedeclarationitem_has_uri():
    assert hasattr(query::XMLNamespaceDeclarationItem, "uri")
    descriptor = None
    for klass in query::XMLNamespaceDeclarationItem.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionelementcontentlist_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionElementContentList)


def test_query::xmlvaluefunctionelementcontentlist_constructor_exists():
    assert callable(query::XMLValueFunctionElementContentList.__init__)


def test_query::xmlvaluefunctionelementcontentlist_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionElementContentList.__init__)
    params = list(sig.parameters.keys())
    assert "nullHandlingOption" in params, "Missing parameter 'nullHandlingOption'"

def test_query::xmlvaluefunctionelementcontentlist_has_nullHandlingOption():
    assert hasattr(query::XMLValueFunctionElementContentList, "nullHandlingOption")
    descriptor = None
    for klass in query::XMLValueFunctionElementContentList.__mro__:
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



def test_query::xmlnamespacedeclarationdefault_is_not_abstract():
    assert not inspect.isabstract(query::XMLNamespaceDeclarationDefault)


def test_query::xmlnamespacedeclarationdefault_constructor_exists():
    assert callable(query::XMLNamespaceDeclarationDefault.__init__)


def test_query::xmlnamespacedeclarationdefault_constructor_args():
    sig = inspect.signature(query::XMLNamespaceDeclarationDefault.__init__)
    params = list(sig.parameters.keys())
    assert "noDefault" in params, "Missing parameter 'noDefault'"

def test_query::xmlnamespacedeclarationdefault_has_noDefault():
    assert hasattr(query::XMLNamespaceDeclarationDefault, "noDefault")
    descriptor = None
    for klass in query::XMLNamespaceDeclarationDefault.__mro__:
        if "noDefault" in klass.__dict__:
            descriptor = klass.__dict__["noDefault"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlnamespacedeclarationprefix_is_not_abstract():
    assert not inspect.isabstract(query::XMLNamespaceDeclarationPrefix)


def test_query::xmlnamespacedeclarationprefix_constructor_exists():
    assert callable(query::XMLNamespaceDeclarationPrefix.__init__)


def test_query::xmlnamespacedeclarationprefix_constructor_args():
    sig = inspect.signature(query::XMLNamespaceDeclarationPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_query::xmlnamespacedeclarationprefix_has_prefix():
    assert hasattr(query::XMLNamespaceDeclarationPrefix, "prefix")
    descriptor = None
    for klass in query::XMLNamespaceDeclarationPrefix.__mro__:
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



def test_query::xmlserializefunction_is_not_abstract():
    assert not inspect.isabstract(query::XMLSerializeFunction)


def test_query::xmlserializefunction_constructor_exists():
    assert callable(query::XMLSerializeFunction.__init__)


def test_query::xmlserializefunction_constructor_args():
    sig = inspect.signature(query::XMLSerializeFunction.__init__)
    params = list(sig.parameters.keys())
    assert "contentOption" in params, "Missing parameter 'contentOption'"
    assert "declarationOption" in params, "Missing parameter 'declarationOption'"
    assert "serializeVersion" in params, "Missing parameter 'serializeVersion'"

def test_query::xmlserializefunction_has_contentOption():
    assert hasattr(query::XMLSerializeFunction, "contentOption")
    descriptor = None
    for klass in query::XMLSerializeFunction.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlserializefunction_has_declarationOption():
    assert hasattr(query::XMLSerializeFunction, "declarationOption")
    descriptor = None
    for klass in query::XMLSerializeFunction.__mro__:
        if "declarationOption" in klass.__dict__:
            descriptor = klass.__dict__["declarationOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlserializefunction_has_serializeVersion():
    assert hasattr(query::XMLSerializeFunction, "serializeVersion")
    descriptor = None
    for klass in query::XMLSerializeFunction.__mro__:
        if "serializeVersion" in klass.__dict__:
            descriptor = klass.__dict__["serializeVersion"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlaggregatefunction_is_not_abstract():
    assert not inspect.isabstract(query::XMLAggregateFunction)


def test_query::xmlaggregatefunction_constructor_exists():
    assert callable(query::XMLAggregateFunction.__init__)


def test_query::xmlaggregatefunction_constructor_args():
    sig = inspect.signature(query::XMLAggregateFunction.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlaggregatefunction_has_returningOption():
    assert hasattr(query::XMLAggregateFunction, "returningOption")
    descriptor = None
    for klass in query::XMLAggregateFunction.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunction_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunction)


def test_query::xmlvaluefunction_constructor_exists():
    assert callable(query::XMLValueFunction.__init__)


def test_query::xmlvaluefunction_constructor_args():
    sig = inspect.signature(query::XMLValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlattributesdeclaration_is_not_abstract():
    assert not inspect.isabstract(query::XMLAttributesDeclaration)


def test_query::xmlattributesdeclaration_constructor_exists():
    assert callable(query::XMLAttributesDeclaration.__init__)


def test_query::xmlattributesdeclaration_constructor_args():
    sig = inspect.signature(query::XMLAttributesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_query::queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(query::QueryValueExpression)


def test_query::queryvalueexpression_constructor_exists():
    assert callable(query::QueryValueExpression.__init__)


def test_query::queryvalueexpression_constructor_args():
    sig = inspect.signature(query::QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_queryvalueexpression_is_not_abstract():
    assert not inspect.isabstract(QueryValueExpression)


def test_queryvalueexpression_constructor_exists():
    assert callable(QueryValueExpression.__init__)


def test_queryvalueexpression_constructor_args():
    sig = inspect.signature(QueryValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionconcatcontentitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionConcatContentItem)


def test_query::xmlvaluefunctionconcatcontentitem_constructor_exists():
    assert callable(query::XMLValueFunctionConcatContentItem.__init__)


def test_query::xmlvaluefunctionconcatcontentitem_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionConcatContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctioncommentcontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionCommentContent)


def test_query::xmlvaluefunctioncommentcontent_constructor_exists():
    assert callable(query::XMLValueFunctionCommentContent.__init__)


def test_query::xmlvaluefunctioncommentcontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionCommentContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionparsecontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionParseContent)


def test_query::xmlvaluefunctionparsecontent_constructor_exists():
    assert callable(query::XMLValueFunctionParseContent.__init__)


def test_query::xmlvaluefunctionparsecontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionParseContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionelementcontentitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionElementContentItem)


def test_query::xmlvaluefunctionelementcontentitem_constructor_exists():
    assert callable(query::XMLValueFunctionElementContentItem.__init__)


def test_query::xmlvaluefunctionelementcontentitem_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionElementContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctiontextcontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionTextContent)


def test_query::xmlvaluefunctiontextcontent_constructor_exists():
    assert callable(query::XMLValueFunctionTextContent.__init__)


def test_query::xmlvaluefunctiontextcontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionTextContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionvalidatecontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidateContent)


def test_query::xmlvaluefunctionvalidatecontent_constructor_exists():
    assert callable(query::XMLValueFunctionValidateContent.__init__)


def test_query::xmlvaluefunctionvalidatecontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidateContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmltablecolumndefinitiondefault_is_not_abstract():
    assert not inspect.isabstract(query::XMLTableColumnDefinitionDefault)


def test_query::xmltablecolumndefinitiondefault_constructor_exists():
    assert callable(query::XMLTableColumnDefinitionDefault.__init__)


def test_query::xmltablecolumndefinitiondefault_constructor_args():
    sig = inspect.signature(query::XMLTableColumnDefinitionDefault.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlserializefunctiontarget_is_not_abstract():
    assert not inspect.isabstract(query::XMLSerializeFunctionTarget)


def test_query::xmlserializefunctiontarget_constructor_exists():
    assert callable(query::XMLSerializeFunctionTarget.__init__)


def test_query::xmlserializefunctiontarget_constructor_args():
    sig = inspect.signature(query::XMLSerializeFunctionTarget.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlqueryargumentitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLQueryArgumentItem)


def test_query::xmlqueryargumentitem_constructor_exists():
    assert callable(query::XMLQueryArgumentItem.__init__)


def test_query::xmlqueryargumentitem_constructor_args():
    sig = inspect.signature(query::XMLQueryArgumentItem.__init__)
    params = list(sig.parameters.keys())
    assert "passingMechanism" in params, "Missing parameter 'passingMechanism'"

def test_query::xmlqueryargumentitem_has_passingMechanism():
    assert hasattr(query::XMLQueryArgumentItem, "passingMechanism")
    descriptor = None
    for klass in query::XMLQueryArgumentItem.__mro__:
        if "passingMechanism" in klass.__dict__:
            descriptor = klass.__dict__["passingMechanism"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionpicontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionPIContent)


def test_query::xmlvaluefunctionpicontent_constructor_exists():
    assert callable(query::XMLValueFunctionPIContent.__init__)


def test_query::xmlvaluefunctionpicontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionPIContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctiondocumentcontent_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionDocumentContent)


def test_query::xmlvaluefunctiondocumentcontent_constructor_exists():
    assert callable(query::XMLValueFunctionDocumentContent.__init__)


def test_query::xmlvaluefunctiondocumentcontent_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionDocumentContent.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionforestcontentitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionForestContentItem)


def test_query::xmlvaluefunctionforestcontentitem_constructor_exists():
    assert callable(query::XMLValueFunctionForestContentItem.__init__)


def test_query::xmlvaluefunctionforestcontentitem_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionForestContentItem.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlattributedeclarationitem_is_not_abstract():
    assert not inspect.isabstract(query::XMLAttributeDeclarationItem)


def test_query::xmlattributedeclarationitem_constructor_exists():
    assert callable(query::XMLAttributeDeclarationItem.__init__)


def test_query::xmlattributedeclarationitem_constructor_args():
    sig = inspect.signature(query::XMLAttributeDeclarationItem.__init__)
    params = list(sig.parameters.keys())



def test_xmlvaluefunction_is_not_abstract():
    assert not inspect.isabstract(XMLValueFunction)


def test_xmlvaluefunction_constructor_exists():
    assert callable(XMLValueFunction.__init__)


def test_xmlvaluefunction_constructor_args():
    sig = inspect.signature(XMLValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_query::xmlvaluefunctionvalidate_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionValidate)


def test_query::xmlvaluefunctionvalidate_constructor_exists():
    assert callable(query::XMLValueFunctionValidate.__init__)


def test_query::xmlvaluefunctionvalidate_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionValidate.__init__)
    params = list(sig.parameters.keys())
    assert "contentOption" in params, "Missing parameter 'contentOption'"

def test_query::xmlvaluefunctionvalidate_has_contentOption():
    assert hasattr(query::XMLValueFunctionValidate, "contentOption")
    descriptor = None
    for klass in query::XMLValueFunctionValidate.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionpi_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionPI)


def test_query::xmlvaluefunctionpi_constructor_exists():
    assert callable(query::XMLValueFunctionPI.__init__)


def test_query::xmlvaluefunctionpi_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionPI.__init__)
    params = list(sig.parameters.keys())
    assert "targetName" in params, "Missing parameter 'targetName'"
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctionpi_has_targetName():
    assert hasattr(query::XMLValueFunctionPI, "targetName")
    descriptor = None
    for klass in query::XMLValueFunctionPI.__mro__:
        if "targetName" in klass.__dict__:
            descriptor = klass.__dict__["targetName"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionpi_has_returningOption():
    assert hasattr(query::XMLValueFunctionPI, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionPI.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionquery_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionQuery)


def test_query::xmlvaluefunctionquery_constructor_exists():
    assert callable(query::XMLValueFunctionQuery.__init__)


def test_query::xmlvaluefunctionquery_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionQuery.__init__)
    params = list(sig.parameters.keys())
    assert "emptyHandlingOption" in params, "Missing parameter 'emptyHandlingOption'"

def test_query::xmlvaluefunctionquery_has_emptyHandlingOption():
    assert hasattr(query::XMLValueFunctionQuery, "emptyHandlingOption")
    descriptor = None
    for klass in query::XMLValueFunctionQuery.__mro__:
        if "emptyHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["emptyHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionparse_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionParse)


def test_query::xmlvaluefunctionparse_constructor_exists():
    assert callable(query::XMLValueFunctionParse.__init__)


def test_query::xmlvaluefunctionparse_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionParse.__init__)
    params = list(sig.parameters.keys())
    assert "contentOption" in params, "Missing parameter 'contentOption'"
    assert "whitespaceHandlingOption" in params, "Missing parameter 'whitespaceHandlingOption'"

def test_query::xmlvaluefunctionparse_has_contentOption():
    assert hasattr(query::XMLValueFunctionParse, "contentOption")
    descriptor = None
    for klass in query::XMLValueFunctionParse.__mro__:
        if "contentOption" in klass.__dict__:
            descriptor = klass.__dict__["contentOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionparse_has_whitespaceHandlingOption():
    assert hasattr(query::XMLValueFunctionParse, "whitespaceHandlingOption")
    descriptor = None
    for klass in query::XMLValueFunctionParse.__mro__:
        if "whitespaceHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["whitespaceHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionelement_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionElement)


def test_query::xmlvaluefunctionelement_constructor_exists():
    assert callable(query::XMLValueFunctionElement.__init__)


def test_query::xmlvaluefunctionelement_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctionelement_has_elementName():
    assert hasattr(query::XMLValueFunctionElement, "elementName")
    descriptor = None
    for klass in query::XMLValueFunctionElement.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionelement_has_returningOption():
    assert hasattr(query::XMLValueFunctionElement, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionElement.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctioncomment_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionComment)


def test_query::xmlvaluefunctioncomment_constructor_exists():
    assert callable(query::XMLValueFunctionComment.__init__)


def test_query::xmlvaluefunctioncomment_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionComment.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctioncomment_has_returningOption():
    assert hasattr(query::XMLValueFunctionComment, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionComment.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctiontext_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionText)


def test_query::xmlvaluefunctiontext_constructor_exists():
    assert callable(query::XMLValueFunctionText.__init__)


def test_query::xmlvaluefunctiontext_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionText.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctiontext_has_returningOption():
    assert hasattr(query::XMLValueFunctionText, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionText.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctiondocument_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionDocument)


def test_query::xmlvaluefunctiondocument_constructor_exists():
    assert callable(query::XMLValueFunctionDocument.__init__)


def test_query::xmlvaluefunctiondocument_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionDocument.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctiondocument_has_returningOption():
    assert hasattr(query::XMLValueFunctionDocument, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionDocument.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionforest_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionForest)


def test_query::xmlvaluefunctionforest_constructor_exists():
    assert callable(query::XMLValueFunctionForest.__init__)


def test_query::xmlvaluefunctionforest_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionForest.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"
    assert "nullHandlingOption" in params, "Missing parameter 'nullHandlingOption'"

def test_query::xmlvaluefunctionforest_has_returningOption():
    assert hasattr(query::XMLValueFunctionForest, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionForest.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)

def test_query::xmlvaluefunctionforest_has_nullHandlingOption():
    assert hasattr(query::XMLValueFunctionForest, "nullHandlingOption")
    descriptor = None
    for klass in query::XMLValueFunctionForest.__mro__:
        if "nullHandlingOption" in klass.__dict__:
            descriptor = klass.__dict__["nullHandlingOption"]
            break
    assert isinstance(descriptor, property)



def test_query::xmlvaluefunctionconcat_is_not_abstract():
    assert not inspect.isabstract(query::XMLValueFunctionConcat)


def test_query::xmlvaluefunctionconcat_constructor_exists():
    assert callable(query::XMLValueFunctionConcat.__init__)


def test_query::xmlvaluefunctionconcat_constructor_args():
    sig = inspect.signature(query::XMLValueFunctionConcat.__init__)
    params = list(sig.parameters.keys())
    assert "returningOption" in params, "Missing parameter 'returningOption'"

def test_query::xmlvaluefunctionconcat_has_returningOption():
    assert hasattr(query::XMLValueFunctionConcat, "returningOption")
    descriptor = None
    for klass in query::XMLValueFunctionConcat.__mro__:
        if "returningOption" in klass.__dict__:
            descriptor = klass.__dict__["returningOption"]
            break
    assert isinstance(descriptor, property)

def test_xmldeclarationtype_exists():
    # Check that the Enumeration exists
    assert XMLDeclarationType is not None

def test_xmldeclarationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLDeclarationType]
    expected_literals = [
        "EXCLUDING_XMLDECLARATION",
        "INCLUDING_XMLDECLARATION",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLDeclarationType"

def test_xmlpassingtype_exists():
    # Check that the Enumeration exists
    assert XMLPassingType is not None

def test_xmlpassingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLPassingType]
    expected_literals = [
        "BY_VALUE",
        "NONE",
        "BY_REF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLPassingType"

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

def test_xmlnullhandlingtype_exists():
    # Check that the Enumeration exists
    assert XMLNullHandlingType is not None

def test_xmlnullhandlingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLNullHandlingType]
    expected_literals = [
        "NONE",
        "EMPTY_ON_NULL",
        "NULL_ON_NULL",
        "NIL_ON_NULL",
        "ABSENT_ON_NULL",
        "NIL_ON_NO_CONTENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLNullHandlingType"

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

def test_xmlreturningtype_exists():
    # Check that the Enumeration exists
    assert XMLReturningType is not None

def test_xmlreturningtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLReturningType]
    expected_literals = [
        "RETURNING_SEQUENCE",
        "NONE",
        "RETURNING_CONTENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLReturningType"

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

def test_xmlcontenttype2_exists():
    # Check that the Enumeration exists
    assert XMLContentType2 is not None

def test_xmlcontenttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLContentType2]
    expected_literals = [
        "CONTENT",
        "SEQUENCE",
        "NONE",
        "DOCUMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLContentType2"


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
query::XMLValueFunctionValidateAccordingToIdentifier_strategy = st.builds(
    query::XMLValueFunctionValidateAccordingToIdentifier,
    registeredXMLSchemaName=
        safe_text,
    schemaName=
        safe_text
)
query::XMLValueFunctionValidateAccordingToURI_strategy = st.builds(
    query::XMLValueFunctionValidateAccordingToURI,
    noNamespace=
        st.booleans(),
    schemaLocationURI=
        safe_text,
    targetNamespaceURI=
        safe_text
)
XMLTableColumnDefinitionItem_strategy = st.builds(
    XMLTableColumnDefinitionItem,
)
query::XMLTableColumnDefinitionOrdinality_strategy = st.builds(
    query::XMLTableColumnDefinitionOrdinality,
)
query::XMLTableColumnDefinitionRegular_strategy = st.builds(
    query::XMLTableColumnDefinitionRegular,
    passingOption=
        safe_text,
    tableColumnPattern=
        safe_text
)
TableFunction_strategy = st.builds(
    TableFunction,
)
query::OrderBySpecification_strategy = st.builds(
    query::OrderBySpecification,
)
query::XMLTableFunction_strategy = st.builds(
    query::XMLTableFunction,
    tableRowPattern=
        safe_text
)
XMLPredicate_strategy = st.builds(
    XMLPredicate,
)
query::XMLPredicateValid_strategy = st.builds(
    query::XMLPredicateValid,
)
query::XMLPredicateExists_strategy = st.builds(
    query::XMLPredicateExists,
)
query::XMLPredicateDocument_strategy = st.builds(
    query::XMLPredicateDocument,
)
query::XMLPredicateContent_strategy = st.builds(
    query::XMLPredicateContent,
)
Predicate_strategy = st.builds(
    Predicate,
)
query::XMLPredicate_strategy = st.builds(
    query::XMLPredicate,
)
ValueExpressionCast_strategy = st.builds(
    ValueExpressionCast,
)
query::XMLValueExpressionCast_strategy = st.builds(
    query::XMLValueExpressionCast,
    passingMechanism=
        safe_text
)
SQLQueryObject_strategy = st.builds(
    SQLQueryObject,
)
query::XMLQueryArgumentList_strategy = st.builds(
    query::XMLQueryArgumentList,
    passingMechanism=
        safe_text
)
query::XMLValueFunctionQueryReturning_strategy = st.builds(
    query::XMLValueFunctionQueryReturning,
    returningOption=
        safe_text,
    passingOption=
        safe_text
)
query::XMLQueryExpression_strategy = st.builds(
    query::XMLQueryExpression,
    xqueryExprContent=
        safe_text
)
query::XMLValueFunctionValidateAccordingTo_strategy = st.builds(
    query::XMLValueFunctionValidateAccordingTo,
)
query::XMLTableColumnDefinitionItem_strategy = st.builds(
    query::XMLTableColumnDefinitionItem,
)
query::XMLValueFunctionValidateElementNamespace_strategy = st.builds(
    query::XMLValueFunctionValidateElementNamespace,
    noNamespace=
        st.booleans(),
    namespaceURI=
        safe_text
)
query::XMLAggregateSortSpecification_strategy = st.builds(
    query::XMLAggregateSortSpecification,
)
query::XMLNamespacesDeclaration_strategy = st.builds(
    query::XMLNamespacesDeclaration,
)
query::XMLSerializeFunctionEncoding_strategy = st.builds(
    query::XMLSerializeFunctionEncoding,
    encodingName=
        safe_text
)
query::XMLValueFunctionValidateElement_strategy = st.builds(
    query::XMLValueFunctionValidateElement,
)
query::XMLValueFunctionValidateElementName_strategy = st.builds(
    query::XMLValueFunctionValidateElementName,
)
query::XMLNamespaceDeclarationItem_strategy = st.builds(
    query::XMLNamespaceDeclarationItem,
    uri=
        safe_text
)
query::XMLValueFunctionElementContentList_strategy = st.builds(
    query::XMLValueFunctionElementContentList,
    nullHandlingOption=
        safe_text
)
XMLNamespaceDeclarationItem_strategy = st.builds(
    XMLNamespaceDeclarationItem,
)
query::XMLNamespaceDeclarationDefault_strategy = st.builds(
    query::XMLNamespaceDeclarationDefault,
    noDefault=
        st.booleans()
)
query::XMLNamespaceDeclarationPrefix_strategy = st.builds(
    query::XMLNamespaceDeclarationPrefix,
    prefix=
        safe_text
)
ValueExpressionFunction_strategy = st.builds(
    ValueExpressionFunction,
)
query::XMLSerializeFunction_strategy = st.builds(
    query::XMLSerializeFunction,
    contentOption=
        safe_text,
    declarationOption=
        safe_text,
    serializeVersion=
        safe_text
)
query::XMLAggregateFunction_strategy = st.builds(
    query::XMLAggregateFunction,
    returningOption=
        safe_text
)
query::XMLValueFunction_strategy = st.builds(
    query::XMLValueFunction,
)
query::XMLAttributesDeclaration_strategy = st.builds(
    query::XMLAttributesDeclaration,
)
query::QueryValueExpression_strategy = st.builds(
    query::QueryValueExpression,
)
QueryValueExpression_strategy = st.builds(
    QueryValueExpression,
)
query::XMLValueFunctionConcatContentItem_strategy = st.builds(
    query::XMLValueFunctionConcatContentItem,
)
query::XMLValueFunctionCommentContent_strategy = st.builds(
    query::XMLValueFunctionCommentContent,
)
query::XMLValueFunctionParseContent_strategy = st.builds(
    query::XMLValueFunctionParseContent,
)
query::XMLValueFunctionElementContentItem_strategy = st.builds(
    query::XMLValueFunctionElementContentItem,
)
query::XMLValueFunctionTextContent_strategy = st.builds(
    query::XMLValueFunctionTextContent,
)
query::XMLValueFunctionValidateContent_strategy = st.builds(
    query::XMLValueFunctionValidateContent,
)
query::XMLTableColumnDefinitionDefault_strategy = st.builds(
    query::XMLTableColumnDefinitionDefault,
)
query::XMLSerializeFunctionTarget_strategy = st.builds(
    query::XMLSerializeFunctionTarget,
)
query::XMLQueryArgumentItem_strategy = st.builds(
    query::XMLQueryArgumentItem,
    passingMechanism=
        safe_text
)
query::XMLValueFunctionPIContent_strategy = st.builds(
    query::XMLValueFunctionPIContent,
)
query::XMLValueFunctionDocumentContent_strategy = st.builds(
    query::XMLValueFunctionDocumentContent,
)
query::XMLValueFunctionForestContentItem_strategy = st.builds(
    query::XMLValueFunctionForestContentItem,
)
query::XMLAttributeDeclarationItem_strategy = st.builds(
    query::XMLAttributeDeclarationItem,
)
XMLValueFunction_strategy = st.builds(
    XMLValueFunction,
)
query::XMLValueFunctionValidate_strategy = st.builds(
    query::XMLValueFunctionValidate,
    contentOption=
        safe_text
)
query::XMLValueFunctionPI_strategy = st.builds(
    query::XMLValueFunctionPI,
    targetName=
        safe_text,
    returningOption=
        safe_text
)
query::XMLValueFunctionQuery_strategy = st.builds(
    query::XMLValueFunctionQuery,
    emptyHandlingOption=
        safe_text
)
query::XMLValueFunctionParse_strategy = st.builds(
    query::XMLValueFunctionParse,
    contentOption=
        safe_text,
    whitespaceHandlingOption=
        safe_text
)
query::XMLValueFunctionElement_strategy = st.builds(
    query::XMLValueFunctionElement,
    elementName=
        safe_text,
    returningOption=
        safe_text
)
query::XMLValueFunctionComment_strategy = st.builds(
    query::XMLValueFunctionComment,
    returningOption=
        safe_text
)
query::XMLValueFunctionText_strategy = st.builds(
    query::XMLValueFunctionText,
    returningOption=
        safe_text
)
query::XMLValueFunctionDocument_strategy = st.builds(
    query::XMLValueFunctionDocument,
    returningOption=
        safe_text
)
query::XMLValueFunctionForest_strategy = st.builds(
    query::XMLValueFunctionForest,
    returningOption=
        safe_text,
    nullHandlingOption=
        safe_text
)
query::XMLValueFunctionConcat_strategy = st.builds(
    query::XMLValueFunctionConcat,
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

@given(instance=query::XMLValueFunctionValidateAccordingToIdentifier_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateAccordingToIdentifier)

@given(instance=query::XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_registeredXMLSchemaName_type(instance):
    assert isinstance(instance.registeredXMLSchemaName, str)


@given(instance=query::XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_registeredXMLSchemaName_setter(instance):
    original = instance.registeredXMLSchemaName
    instance.registeredXMLSchemaName = original
    assert instance.registeredXMLSchemaName == original

@given(instance=query::XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=query::XMLValueFunctionValidateAccordingToIdentifier_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtoidentifier_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateaccordingtouri_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateAccordingToURI)

@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_noNamespace_type(instance):
    assert isinstance(instance.noNamespace, bool)


@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_noNamespace_setter(instance):
    original = instance.noNamespace
    instance.noNamespace = original
    assert instance.noNamespace == original

@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_schemaLocationURI_type(instance):
    assert isinstance(instance.schemaLocationURI, str)


@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_schemaLocationURI_setter(instance):
    original = instance.schemaLocationURI
    instance.schemaLocationURI = original
    assert instance.schemaLocationURI == original

@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_targetNamespaceURI_type(instance):
    assert isinstance(instance.targetNamespaceURI, str)


@given(instance=query::XMLValueFunctionValidateAccordingToURI_strategy)
def test_query::xmlvaluefunctionvalidateaccordingtouri_targetNamespaceURI_setter(instance):
    original = instance.targetNamespaceURI
    instance.targetNamespaceURI = original
    assert instance.targetNamespaceURI == original

@given(instance=XMLTableColumnDefinitionItem_strategy)
@settings(max_examples=50)
def test_xmltablecolumndefinitionitem_instantiation(instance):
    assert isinstance(instance, XMLTableColumnDefinitionItem)

@given(instance=query::XMLTableColumnDefinitionOrdinality_strategy)
@settings(max_examples=50)
def test_query::xmltablecolumndefinitionordinality_instantiation(instance):
    assert isinstance(instance, query::XMLTableColumnDefinitionOrdinality)

@given(instance=query::XMLTableColumnDefinitionRegular_strategy)
@settings(max_examples=50)
def test_query::xmltablecolumndefinitionregular_instantiation(instance):
    assert isinstance(instance, query::XMLTableColumnDefinitionRegular)

@given(instance=query::XMLTableColumnDefinitionRegular_strategy)
def test_query::xmltablecolumndefinitionregular_passingOption_type(instance):
    assert isinstance(instance.passingOption, str)


@given(instance=query::XMLTableColumnDefinitionRegular_strategy)
def test_query::xmltablecolumndefinitionregular_passingOption_setter(instance):
    original = instance.passingOption
    instance.passingOption = original
    assert instance.passingOption == original

@given(instance=query::XMLTableColumnDefinitionRegular_strategy)
def test_query::xmltablecolumndefinitionregular_tableColumnPattern_type(instance):
    assert isinstance(instance.tableColumnPattern, str)


@given(instance=query::XMLTableColumnDefinitionRegular_strategy)
def test_query::xmltablecolumndefinitionregular_tableColumnPattern_setter(instance):
    original = instance.tableColumnPattern
    instance.tableColumnPattern = original
    assert instance.tableColumnPattern == original

@given(instance=TableFunction_strategy)
@settings(max_examples=50)
def test_tablefunction_instantiation(instance):
    assert isinstance(instance, TableFunction)

@given(instance=query::OrderBySpecification_strategy)
@settings(max_examples=50)
def test_query::orderbyspecification_instantiation(instance):
    assert isinstance(instance, query::OrderBySpecification)

@given(instance=query::XMLTableFunction_strategy)
@settings(max_examples=50)
def test_query::xmltablefunction_instantiation(instance):
    assert isinstance(instance, query::XMLTableFunction)

@given(instance=query::XMLTableFunction_strategy)
def test_query::xmltablefunction_tableRowPattern_type(instance):
    assert isinstance(instance.tableRowPattern, str)


@given(instance=query::XMLTableFunction_strategy)
def test_query::xmltablefunction_tableRowPattern_setter(instance):
    original = instance.tableRowPattern
    instance.tableRowPattern = original
    assert instance.tableRowPattern == original

@given(instance=XMLPredicate_strategy)
@settings(max_examples=50)
def test_xmlpredicate_instantiation(instance):
    assert isinstance(instance, XMLPredicate)

@given(instance=query::XMLPredicateValid_strategy)
@settings(max_examples=50)
def test_query::xmlpredicatevalid_instantiation(instance):
    assert isinstance(instance, query::XMLPredicateValid)

@given(instance=query::XMLPredicateExists_strategy)
@settings(max_examples=50)
def test_query::xmlpredicateexists_instantiation(instance):
    assert isinstance(instance, query::XMLPredicateExists)

@given(instance=query::XMLPredicateDocument_strategy)
@settings(max_examples=50)
def test_query::xmlpredicatedocument_instantiation(instance):
    assert isinstance(instance, query::XMLPredicateDocument)

@given(instance=query::XMLPredicateContent_strategy)
@settings(max_examples=50)
def test_query::xmlpredicatecontent_instantiation(instance):
    assert isinstance(instance, query::XMLPredicateContent)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=query::XMLPredicate_strategy)
@settings(max_examples=50)
def test_query::xmlpredicate_instantiation(instance):
    assert isinstance(instance, query::XMLPredicate)

@given(instance=ValueExpressionCast_strategy)
@settings(max_examples=50)
def test_valueexpressioncast_instantiation(instance):
    assert isinstance(instance, ValueExpressionCast)

@given(instance=query::XMLValueExpressionCast_strategy)
@settings(max_examples=50)
def test_query::xmlvalueexpressioncast_instantiation(instance):
    assert isinstance(instance, query::XMLValueExpressionCast)

@given(instance=query::XMLValueExpressionCast_strategy)
def test_query::xmlvalueexpressioncast_passingMechanism_type(instance):
    assert isinstance(instance.passingMechanism, str)


@given(instance=query::XMLValueExpressionCast_strategy)
def test_query::xmlvalueexpressioncast_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=SQLQueryObject_strategy)
@settings(max_examples=50)
def test_sqlqueryobject_instantiation(instance):
    assert isinstance(instance, SQLQueryObject)

@given(instance=query::XMLQueryArgumentList_strategy)
@settings(max_examples=50)
def test_query::xmlqueryargumentlist_instantiation(instance):
    assert isinstance(instance, query::XMLQueryArgumentList)

@given(instance=query::XMLQueryArgumentList_strategy)
def test_query::xmlqueryargumentlist_passingMechanism_type(instance):
    assert isinstance(instance.passingMechanism, str)


@given(instance=query::XMLQueryArgumentList_strategy)
def test_query::xmlqueryargumentlist_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=query::XMLValueFunctionQueryReturning_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionqueryreturning_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionQueryReturning)

@given(instance=query::XMLValueFunctionQueryReturning_strategy)
def test_query::xmlvaluefunctionqueryreturning_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionQueryReturning_strategy)
def test_query::xmlvaluefunctionqueryreturning_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionQueryReturning_strategy)
def test_query::xmlvaluefunctionqueryreturning_passingOption_type(instance):
    assert isinstance(instance.passingOption, str)


@given(instance=query::XMLValueFunctionQueryReturning_strategy)
def test_query::xmlvaluefunctionqueryreturning_passingOption_setter(instance):
    original = instance.passingOption
    instance.passingOption = original
    assert instance.passingOption == original

@given(instance=query::XMLQueryExpression_strategy)
@settings(max_examples=50)
def test_query::xmlqueryexpression_instantiation(instance):
    assert isinstance(instance, query::XMLQueryExpression)

@given(instance=query::XMLQueryExpression_strategy)
def test_query::xmlqueryexpression_xqueryExprContent_type(instance):
    assert isinstance(instance.xqueryExprContent, str)


@given(instance=query::XMLQueryExpression_strategy)
def test_query::xmlqueryexpression_xqueryExprContent_setter(instance):
    original = instance.xqueryExprContent
    instance.xqueryExprContent = original
    assert instance.xqueryExprContent == original

@given(instance=query::XMLValueFunctionValidateAccordingTo_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateaccordingto_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateAccordingTo)

@given(instance=query::XMLTableColumnDefinitionItem_strategy)
@settings(max_examples=50)
def test_query::xmltablecolumndefinitionitem_instantiation(instance):
    assert isinstance(instance, query::XMLTableColumnDefinitionItem)

@given(instance=query::XMLValueFunctionValidateElementNamespace_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateelementnamespace_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateElementNamespace)

@given(instance=query::XMLValueFunctionValidateElementNamespace_strategy)
def test_query::xmlvaluefunctionvalidateelementnamespace_noNamespace_type(instance):
    assert isinstance(instance.noNamespace, bool)


@given(instance=query::XMLValueFunctionValidateElementNamespace_strategy)
def test_query::xmlvaluefunctionvalidateelementnamespace_noNamespace_setter(instance):
    original = instance.noNamespace
    instance.noNamespace = original
    assert instance.noNamespace == original

@given(instance=query::XMLValueFunctionValidateElementNamespace_strategy)
def test_query::xmlvaluefunctionvalidateelementnamespace_namespaceURI_type(instance):
    assert isinstance(instance.namespaceURI, str)


@given(instance=query::XMLValueFunctionValidateElementNamespace_strategy)
def test_query::xmlvaluefunctionvalidateelementnamespace_namespaceURI_setter(instance):
    original = instance.namespaceURI
    instance.namespaceURI = original
    assert instance.namespaceURI == original

@given(instance=query::XMLAggregateSortSpecification_strategy)
@settings(max_examples=50)
def test_query::xmlaggregatesortspecification_instantiation(instance):
    assert isinstance(instance, query::XMLAggregateSortSpecification)

@given(instance=query::XMLNamespacesDeclaration_strategy)
@settings(max_examples=50)
def test_query::xmlnamespacesdeclaration_instantiation(instance):
    assert isinstance(instance, query::XMLNamespacesDeclaration)

@given(instance=query::XMLSerializeFunctionEncoding_strategy)
@settings(max_examples=50)
def test_query::xmlserializefunctionencoding_instantiation(instance):
    assert isinstance(instance, query::XMLSerializeFunctionEncoding)

@given(instance=query::XMLSerializeFunctionEncoding_strategy)
def test_query::xmlserializefunctionencoding_encodingName_type(instance):
    assert isinstance(instance.encodingName, str)


@given(instance=query::XMLSerializeFunctionEncoding_strategy)
def test_query::xmlserializefunctionencoding_encodingName_setter(instance):
    original = instance.encodingName
    instance.encodingName = original
    assert instance.encodingName == original

@given(instance=query::XMLValueFunctionValidateElement_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateelement_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateElement)

@given(instance=query::XMLValueFunctionValidateElementName_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidateelementname_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateElementName)

@given(instance=query::XMLNamespaceDeclarationItem_strategy)
@settings(max_examples=50)
def test_query::xmlnamespacedeclarationitem_instantiation(instance):
    assert isinstance(instance, query::XMLNamespaceDeclarationItem)

@given(instance=query::XMLNamespaceDeclarationItem_strategy)
def test_query::xmlnamespacedeclarationitem_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=query::XMLNamespaceDeclarationItem_strategy)
def test_query::xmlnamespacedeclarationitem_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=query::XMLValueFunctionElementContentList_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionelementcontentlist_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionElementContentList)

@given(instance=query::XMLValueFunctionElementContentList_strategy)
def test_query::xmlvaluefunctionelementcontentlist_nullHandlingOption_type(instance):
    assert isinstance(instance.nullHandlingOption, str)


@given(instance=query::XMLValueFunctionElementContentList_strategy)
def test_query::xmlvaluefunctionelementcontentlist_nullHandlingOption_setter(instance):
    original = instance.nullHandlingOption
    instance.nullHandlingOption = original
    assert instance.nullHandlingOption == original

@given(instance=XMLNamespaceDeclarationItem_strategy)
@settings(max_examples=50)
def test_xmlnamespacedeclarationitem_instantiation(instance):
    assert isinstance(instance, XMLNamespaceDeclarationItem)

@given(instance=query::XMLNamespaceDeclarationDefault_strategy)
@settings(max_examples=50)
def test_query::xmlnamespacedeclarationdefault_instantiation(instance):
    assert isinstance(instance, query::XMLNamespaceDeclarationDefault)

@given(instance=query::XMLNamespaceDeclarationDefault_strategy)
def test_query::xmlnamespacedeclarationdefault_noDefault_type(instance):
    assert isinstance(instance.noDefault, bool)


@given(instance=query::XMLNamespaceDeclarationDefault_strategy)
def test_query::xmlnamespacedeclarationdefault_noDefault_setter(instance):
    original = instance.noDefault
    instance.noDefault = original
    assert instance.noDefault == original

@given(instance=query::XMLNamespaceDeclarationPrefix_strategy)
@settings(max_examples=50)
def test_query::xmlnamespacedeclarationprefix_instantiation(instance):
    assert isinstance(instance, query::XMLNamespaceDeclarationPrefix)

@given(instance=query::XMLNamespaceDeclarationPrefix_strategy)
def test_query::xmlnamespacedeclarationprefix_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=query::XMLNamespaceDeclarationPrefix_strategy)
def test_query::xmlnamespacedeclarationprefix_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=ValueExpressionFunction_strategy)
@settings(max_examples=50)
def test_valueexpressionfunction_instantiation(instance):
    assert isinstance(instance, ValueExpressionFunction)

@given(instance=query::XMLSerializeFunction_strategy)
@settings(max_examples=50)
def test_query::xmlserializefunction_instantiation(instance):
    assert isinstance(instance, query::XMLSerializeFunction)

@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_contentOption_type(instance):
    assert isinstance(instance.contentOption, str)


@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_declarationOption_type(instance):
    assert isinstance(instance.declarationOption, str)


@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_declarationOption_setter(instance):
    original = instance.declarationOption
    instance.declarationOption = original
    assert instance.declarationOption == original

@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_serializeVersion_type(instance):
    assert isinstance(instance.serializeVersion, str)


@given(instance=query::XMLSerializeFunction_strategy)
def test_query::xmlserializefunction_serializeVersion_setter(instance):
    original = instance.serializeVersion
    instance.serializeVersion = original
    assert instance.serializeVersion == original

@given(instance=query::XMLAggregateFunction_strategy)
@settings(max_examples=50)
def test_query::xmlaggregatefunction_instantiation(instance):
    assert isinstance(instance, query::XMLAggregateFunction)

@given(instance=query::XMLAggregateFunction_strategy)
def test_query::xmlaggregatefunction_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLAggregateFunction_strategy)
def test_query::xmlaggregatefunction_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunction_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunction_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunction)

@given(instance=query::XMLAttributesDeclaration_strategy)
@settings(max_examples=50)
def test_query::xmlattributesdeclaration_instantiation(instance):
    assert isinstance(instance, query::XMLAttributesDeclaration)

@given(instance=query::QueryValueExpression_strategy)
@settings(max_examples=50)
def test_query::queryvalueexpression_instantiation(instance):
    assert isinstance(instance, query::QueryValueExpression)

@given(instance=QueryValueExpression_strategy)
@settings(max_examples=50)
def test_queryvalueexpression_instantiation(instance):
    assert isinstance(instance, QueryValueExpression)

@given(instance=query::XMLValueFunctionConcatContentItem_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionconcatcontentitem_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionConcatContentItem)

@given(instance=query::XMLValueFunctionCommentContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctioncommentcontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionCommentContent)

@given(instance=query::XMLValueFunctionParseContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionparsecontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionParseContent)

@given(instance=query::XMLValueFunctionElementContentItem_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionelementcontentitem_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionElementContentItem)

@given(instance=query::XMLValueFunctionTextContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctiontextcontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionTextContent)

@given(instance=query::XMLValueFunctionValidateContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidatecontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidateContent)

@given(instance=query::XMLTableColumnDefinitionDefault_strategy)
@settings(max_examples=50)
def test_query::xmltablecolumndefinitiondefault_instantiation(instance):
    assert isinstance(instance, query::XMLTableColumnDefinitionDefault)

@given(instance=query::XMLSerializeFunctionTarget_strategy)
@settings(max_examples=50)
def test_query::xmlserializefunctiontarget_instantiation(instance):
    assert isinstance(instance, query::XMLSerializeFunctionTarget)

@given(instance=query::XMLQueryArgumentItem_strategy)
@settings(max_examples=50)
def test_query::xmlqueryargumentitem_instantiation(instance):
    assert isinstance(instance, query::XMLQueryArgumentItem)

@given(instance=query::XMLQueryArgumentItem_strategy)
def test_query::xmlqueryargumentitem_passingMechanism_type(instance):
    assert isinstance(instance.passingMechanism, str)


@given(instance=query::XMLQueryArgumentItem_strategy)
def test_query::xmlqueryargumentitem_passingMechanism_setter(instance):
    original = instance.passingMechanism
    instance.passingMechanism = original
    assert instance.passingMechanism == original

@given(instance=query::XMLValueFunctionPIContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionpicontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionPIContent)

@given(instance=query::XMLValueFunctionDocumentContent_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctiondocumentcontent_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionDocumentContent)

@given(instance=query::XMLValueFunctionForestContentItem_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionforestcontentitem_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionForestContentItem)

@given(instance=query::XMLAttributeDeclarationItem_strategy)
@settings(max_examples=50)
def test_query::xmlattributedeclarationitem_instantiation(instance):
    assert isinstance(instance, query::XMLAttributeDeclarationItem)

@given(instance=XMLValueFunction_strategy)
@settings(max_examples=50)
def test_xmlvaluefunction_instantiation(instance):
    assert isinstance(instance, XMLValueFunction)

@given(instance=query::XMLValueFunctionValidate_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionvalidate_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionValidate)

@given(instance=query::XMLValueFunctionValidate_strategy)
def test_query::xmlvaluefunctionvalidate_contentOption_type(instance):
    assert isinstance(instance.contentOption, str)


@given(instance=query::XMLValueFunctionValidate_strategy)
def test_query::xmlvaluefunctionvalidate_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query::XMLValueFunctionPI_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionpi_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionPI)

@given(instance=query::XMLValueFunctionPI_strategy)
def test_query::xmlvaluefunctionpi_targetName_type(instance):
    assert isinstance(instance.targetName, str)


@given(instance=query::XMLValueFunctionPI_strategy)
def test_query::xmlvaluefunctionpi_targetName_setter(instance):
    original = instance.targetName
    instance.targetName = original
    assert instance.targetName == original

@given(instance=query::XMLValueFunctionPI_strategy)
def test_query::xmlvaluefunctionpi_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionPI_strategy)
def test_query::xmlvaluefunctionpi_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionQuery_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionquery_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionQuery)

@given(instance=query::XMLValueFunctionQuery_strategy)
def test_query::xmlvaluefunctionquery_emptyHandlingOption_type(instance):
    assert isinstance(instance.emptyHandlingOption, str)


@given(instance=query::XMLValueFunctionQuery_strategy)
def test_query::xmlvaluefunctionquery_emptyHandlingOption_setter(instance):
    original = instance.emptyHandlingOption
    instance.emptyHandlingOption = original
    assert instance.emptyHandlingOption == original

@given(instance=query::XMLValueFunctionParse_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionparse_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionParse)

@given(instance=query::XMLValueFunctionParse_strategy)
def test_query::xmlvaluefunctionparse_contentOption_type(instance):
    assert isinstance(instance.contentOption, str)


@given(instance=query::XMLValueFunctionParse_strategy)
def test_query::xmlvaluefunctionparse_contentOption_setter(instance):
    original = instance.contentOption
    instance.contentOption = original
    assert instance.contentOption == original

@given(instance=query::XMLValueFunctionParse_strategy)
def test_query::xmlvaluefunctionparse_whitespaceHandlingOption_type(instance):
    assert isinstance(instance.whitespaceHandlingOption, str)


@given(instance=query::XMLValueFunctionParse_strategy)
def test_query::xmlvaluefunctionparse_whitespaceHandlingOption_setter(instance):
    original = instance.whitespaceHandlingOption
    instance.whitespaceHandlingOption = original
    assert instance.whitespaceHandlingOption == original

@given(instance=query::XMLValueFunctionElement_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionelement_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionElement)

@given(instance=query::XMLValueFunctionElement_strategy)
def test_query::xmlvaluefunctionelement_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=query::XMLValueFunctionElement_strategy)
def test_query::xmlvaluefunctionelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=query::XMLValueFunctionElement_strategy)
def test_query::xmlvaluefunctionelement_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionElement_strategy)
def test_query::xmlvaluefunctionelement_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionComment_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctioncomment_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionComment)

@given(instance=query::XMLValueFunctionComment_strategy)
def test_query::xmlvaluefunctioncomment_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionComment_strategy)
def test_query::xmlvaluefunctioncomment_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionText_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctiontext_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionText)

@given(instance=query::XMLValueFunctionText_strategy)
def test_query::xmlvaluefunctiontext_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionText_strategy)
def test_query::xmlvaluefunctiontext_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionDocument_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctiondocument_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionDocument)

@given(instance=query::XMLValueFunctionDocument_strategy)
def test_query::xmlvaluefunctiondocument_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionDocument_strategy)
def test_query::xmlvaluefunctiondocument_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionForest_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionforest_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionForest)

@given(instance=query::XMLValueFunctionForest_strategy)
def test_query::xmlvaluefunctionforest_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionForest_strategy)
def test_query::xmlvaluefunctionforest_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

@given(instance=query::XMLValueFunctionForest_strategy)
def test_query::xmlvaluefunctionforest_nullHandlingOption_type(instance):
    assert isinstance(instance.nullHandlingOption, str)


@given(instance=query::XMLValueFunctionForest_strategy)
def test_query::xmlvaluefunctionforest_nullHandlingOption_setter(instance):
    original = instance.nullHandlingOption
    instance.nullHandlingOption = original
    assert instance.nullHandlingOption == original

@given(instance=query::XMLValueFunctionConcat_strategy)
@settings(max_examples=50)
def test_query::xmlvaluefunctionconcat_instantiation(instance):
    assert isinstance(instance, query::XMLValueFunctionConcat)

@given(instance=query::XMLValueFunctionConcat_strategy)
def test_query::xmlvaluefunctionconcat_returningOption_type(instance):
    assert isinstance(instance.returningOption, str)


@given(instance=query::XMLValueFunctionConcat_strategy)
def test_query::xmlvaluefunctionconcat_returningOption_setter(instance):
    original = instance.returningOption
    instance.returningOption = original
    assert instance.returningOption == original

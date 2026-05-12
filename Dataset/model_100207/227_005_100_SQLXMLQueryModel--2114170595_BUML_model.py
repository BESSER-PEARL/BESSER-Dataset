####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
XMLPassingType: Enumeration = Enumeration(
    name="XMLPassingType",
    literals={
            EnumerationLiteral(name="BY_REF"),
			EnumerationLiteral(name="BY_VALUE"),
			EnumerationLiteral(name="NONE")
    }
)

XMLContentType: Enumeration = Enumeration(
    name="XMLContentType",
    literals={
            EnumerationLiteral(name="CONTENT"),
			EnumerationLiteral(name="DOCUMENT"),
			EnumerationLiteral(name="NONE")
    }
)

XMLDeclarationType: Enumeration = Enumeration(
    name="XMLDeclarationType",
    literals={
            EnumerationLiteral(name="EXCLUDING_XMLDECLARATION"),
			EnumerationLiteral(name="INCLUDING_XMLDECLARATION"),
			EnumerationLiteral(name="NONE")
    }
)

XMLReturningType: Enumeration = Enumeration(
    name="XMLReturningType",
    literals={
            EnumerationLiteral(name="RETURNING_CONTENT"),
			EnumerationLiteral(name="RETURNING_SEQUENCE"),
			EnumerationLiteral(name="NONE")
    }
)

XMLNullHandlingType: Enumeration = Enumeration(
    name="XMLNullHandlingType",
    literals={
            EnumerationLiteral(name="ABSENT_ON_NULL"),
			EnumerationLiteral(name="NIL_ON_NULL"),
			EnumerationLiteral(name="NULL_ON_NULL"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="EMPTY_ON_NULL"),
			EnumerationLiteral(name="NIL_ON_NO_CONTENT")
    }
)

XMLWhitespaceHandlingType: Enumeration = Enumeration(
    name="XMLWhitespaceHandlingType",
    literals={
            EnumerationLiteral(name="PRESERE_WHITESPACE"),
			EnumerationLiteral(name="STRIP_WHITESPACE"),
			EnumerationLiteral(name="NONE")
    }
)

XMLEmptyHandlingType: Enumeration = Enumeration(
    name="XMLEmptyHandlingType",
    literals={
            EnumerationLiteral(name="EMPTY_ON_EMPTY"),
			EnumerationLiteral(name="NULL_ON_EMPTY"),
			EnumerationLiteral(name="NONE")
    }
)

XMLContentType2: Enumeration = Enumeration(
    name="XMLContentType2",
    literals={
            EnumerationLiteral(name="CONTENT"),
			EnumerationLiteral(name="DOCUMENT"),
			EnumerationLiteral(name="SEQUENCE"),
			EnumerationLiteral(name="NONE")
    }
)

# Classes
query_XMLValueFunctionConcat = Class(name="query_XMLValueFunctionConcat")
XMLValueFunction = Class(name="XMLValueFunction")
query_XMLAttributeDeclarationItem = Class(name="query_XMLAttributeDeclarationItem")
QueryValueExpression = Class(name="QueryValueExpression")
query_QueryValueExpression = Class(name="query_QueryValueExpression")
query_XMLAttributesDeclaration = Class(name="query_XMLAttributesDeclaration")
query_XMLValueFunctionConcatContentItem = Class(name="query_XMLValueFunctionConcatContentItem")
query_XMLValueFunction = Class(name="query_XMLValueFunction", is_abstract=True)
ValueExpressionFunction = Class(name="ValueExpressionFunction")
query_XMLNamespaceDeclarationPrefix = Class(name="query_XMLNamespaceDeclarationPrefix")
XMLNamespaceDeclarationItem = Class(name="XMLNamespaceDeclarationItem")
query_XMLNamespaceDeclarationDefault = Class(name="query_XMLNamespaceDeclarationDefault")
query_XMLValueFunctionElementContentList = Class(name="query_XMLValueFunctionElementContentList")
query_XMLValueFunctionElement = Class(name="query_XMLValueFunctionElement")
query_XMLNamespaceDeclarationItem = Class(name="query_XMLNamespaceDeclarationItem")
SQLQueryObject = Class(name="SQLQueryObject")
query_XMLNamespacesDeclaration = Class(name="query_XMLNamespacesDeclaration")
query_XMLValueFunctionElementContentItem = Class(name="query_XMLValueFunctionElementContentItem")
query_XMLValueFunctionForest = Class(name="query_XMLValueFunctionForest")
query_XMLValueFunctionComment = Class(name="query_XMLValueFunctionComment")
query_XMLValueFunctionCommentContent = Class(name="query_XMLValueFunctionCommentContent")
query_XMLValueFunctionDocument = Class(name="query_XMLValueFunctionDocument")
query_XMLValueFunctionDocumentContent = Class(name="query_XMLValueFunctionDocumentContent")
query_XMLValueFunctionParse = Class(name="query_XMLValueFunctionParse")
query_XMLValueFunctionForestContentItem = Class(name="query_XMLValueFunctionForestContentItem")
query_XMLValueFunctionParseContent = Class(name="query_XMLValueFunctionParseContent")
query_XMLValueFunctionPI = Class(name="query_XMLValueFunctionPI")
query_XMLValueFunctionPIContent = Class(name="query_XMLValueFunctionPIContent")
query_XMLValueFunctionQuery = Class(name="query_XMLValueFunctionQuery")
query_XMLQueryExpression = Class(name="query_XMLQueryExpression")
query_XMLQueryArgumentList = Class(name="query_XMLQueryArgumentList")
query_XMLValueFunctionQueryReturning = Class(name="query_XMLValueFunctionQueryReturning")
query_XMLValueFunctionText = Class(name="query_XMLValueFunctionText")
query_XMLValueFunctionTextContent = Class(name="query_XMLValueFunctionTextContent")
query_XMLValueFunctionValidate = Class(name="query_XMLValueFunctionValidate")
query_XMLValueFunctionValidateContent = Class(name="query_XMLValueFunctionValidateContent")
query_XMLValueFunctionValidateAccordingTo = Class(name="query_XMLValueFunctionValidateAccordingTo")
query_XMLValueExpressionCast = Class(name="query_XMLValueExpressionCast")
ValueExpressionCast = Class(name="ValueExpressionCast")
query_XMLPredicate = Class(name="query_XMLPredicate", is_abstract=True)
Predicate = Class(name="Predicate")
query_XMLPredicateContent = Class(name="query_XMLPredicateContent")
XMLPredicate = Class(name="XMLPredicate")
query_XMLPredicateDocument = Class(name="query_XMLPredicateDocument")
query_XMLPredicateValid = Class(name="query_XMLPredicateValid")
query_XMLPredicateExists = Class(name="query_XMLPredicateExists")
query_XMLQueryArgumentItem = Class(name="query_XMLQueryArgumentItem")
query_XMLTableFunction = Class(name="query_XMLTableFunction")
query_XMLSerializeFunctionTarget = Class(name="query_XMLSerializeFunctionTarget")
query_XMLSerializeFunctionEncoding = Class(name="query_XMLSerializeFunctionEncoding")
query_XMLSerializeFunction = Class(name="query_XMLSerializeFunction")
query_XMLAggregateFunction = Class(name="query_XMLAggregateFunction")
query_XMLAggregateSortSpecification = Class(name="query_XMLAggregateSortSpecification")
query_OrderBySpecification = Class(name="query_OrderBySpecification")
TableFunction = Class(name="TableFunction")
query_XMLTableColumnDefinitionItem = Class(name="query_XMLTableColumnDefinitionItem")
query_XMLTableColumnDefinitionRegular = Class(name="query_XMLTableColumnDefinitionRegular")
XMLTableColumnDefinitionItem = Class(name="XMLTableColumnDefinitionItem")
query_XMLTableColumnDefinitionDefault = Class(name="query_XMLTableColumnDefinitionDefault")
query_XMLTableColumnDefinitionOrdinality = Class(name="query_XMLTableColumnDefinitionOrdinality")
query_XMLValueFunctionValidateElement = Class(name="query_XMLValueFunctionValidateElement")
query_XMLValueFunctionValidateAccordingToURI = Class(name="query_XMLValueFunctionValidateAccordingToURI")
XMLValueFunctionValidateAccordingTo = Class(name="XMLValueFunctionValidateAccordingTo")
DataType = Class(name="DataType")
query_XMLValueFunctionValidateAccordingToIdentifier = Class(name="query_XMLValueFunctionValidateAccordingToIdentifier")
query_XMLValueFunctionValidateElementName = Class(name="query_XMLValueFunctionValidateElementName")
query_XMLValueFunctionValidateElementNamespace = Class(name="query_XMLValueFunctionValidateElementNamespace")

# query_XMLValueFunctionConcat class attributes and methods
query_XMLValueFunctionConcat_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionConcat.attributes={query_XMLValueFunctionConcat_returningOption}

# XMLValueFunction class attributes and methods

# query_XMLAttributeDeclarationItem class attributes and methods

# QueryValueExpression class attributes and methods

# query_QueryValueExpression class attributes and methods

# query_XMLAttributesDeclaration class attributes and methods

# query_XMLValueFunctionConcatContentItem class attributes and methods

# query_XMLValueFunction class attributes and methods

# ValueExpressionFunction class attributes and methods

# query_XMLNamespaceDeclarationPrefix class attributes and methods
query_XMLNamespaceDeclarationPrefix_prefix: Property = Property(name="prefix", type=StringType)
query_XMLNamespaceDeclarationPrefix.attributes={query_XMLNamespaceDeclarationPrefix_prefix}

# XMLNamespaceDeclarationItem class attributes and methods

# query_XMLNamespaceDeclarationDefault class attributes and methods
query_XMLNamespaceDeclarationDefault_noDefault: Property = Property(name="noDefault", type=BooleanType)
query_XMLNamespaceDeclarationDefault.attributes={query_XMLNamespaceDeclarationDefault_noDefault}

# query_XMLValueFunctionElementContentList class attributes and methods
query_XMLValueFunctionElementContentList_nullHandlingOption: Property = Property(name="nullHandlingOption", type=StringType)
query_XMLValueFunctionElementContentList.attributes={query_XMLValueFunctionElementContentList_nullHandlingOption}

# query_XMLValueFunctionElement class attributes and methods
query_XMLValueFunctionElement_elementName: Property = Property(name="elementName", type=StringType)
query_XMLValueFunctionElement_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionElement.attributes={query_XMLValueFunctionElement_elementName, query_XMLValueFunctionElement_returningOption}

# query_XMLNamespaceDeclarationItem class attributes and methods
query_XMLNamespaceDeclarationItem_uri: Property = Property(name="uri", type=StringType)
query_XMLNamespaceDeclarationItem.attributes={query_XMLNamespaceDeclarationItem_uri}

# SQLQueryObject class attributes and methods

# query_XMLNamespacesDeclaration class attributes and methods

# query_XMLValueFunctionElementContentItem class attributes and methods

# query_XMLValueFunctionForest class attributes and methods
query_XMLValueFunctionForest_nullHandlingOption: Property = Property(name="nullHandlingOption", type=StringType)
query_XMLValueFunctionForest_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionForest.attributes={query_XMLValueFunctionForest_returningOption, query_XMLValueFunctionForest_nullHandlingOption}

# query_XMLValueFunctionComment class attributes and methods
query_XMLValueFunctionComment_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionComment.attributes={query_XMLValueFunctionComment_returningOption}

# query_XMLValueFunctionCommentContent class attributes and methods

# query_XMLValueFunctionDocument class attributes and methods
query_XMLValueFunctionDocument_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionDocument.attributes={query_XMLValueFunctionDocument_returningOption}

# query_XMLValueFunctionDocumentContent class attributes and methods

# query_XMLValueFunctionParse class attributes and methods
query_XMLValueFunctionParse_contentOption: Property = Property(name="contentOption", type=StringType)
query_XMLValueFunctionParse_whitespaceHandlingOption: Property = Property(name="whitespaceHandlingOption", type=StringType)
query_XMLValueFunctionParse.attributes={query_XMLValueFunctionParse_contentOption, query_XMLValueFunctionParse_whitespaceHandlingOption}

# query_XMLValueFunctionForestContentItem class attributes and methods

# query_XMLValueFunctionParseContent class attributes and methods

# query_XMLValueFunctionPI class attributes and methods
query_XMLValueFunctionPI_targetName: Property = Property(name="targetName", type=StringType)
query_XMLValueFunctionPI_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionPI.attributes={query_XMLValueFunctionPI_returningOption, query_XMLValueFunctionPI_targetName}

# query_XMLValueFunctionPIContent class attributes and methods

# query_XMLValueFunctionQuery class attributes and methods
query_XMLValueFunctionQuery_emptyHandlingOption: Property = Property(name="emptyHandlingOption", type=StringType)
query_XMLValueFunctionQuery.attributes={query_XMLValueFunctionQuery_emptyHandlingOption}

# query_XMLQueryExpression class attributes and methods
query_XMLQueryExpression_xqueryExprContent: Property = Property(name="xqueryExprContent", type=StringType)
query_XMLQueryExpression.attributes={query_XMLQueryExpression_xqueryExprContent}

# query_XMLQueryArgumentList class attributes and methods
query_XMLQueryArgumentList_passingMechanism: Property = Property(name="passingMechanism", type=StringType)
query_XMLQueryArgumentList.attributes={query_XMLQueryArgumentList_passingMechanism}

# query_XMLValueFunctionQueryReturning class attributes and methods
query_XMLValueFunctionQueryReturning_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionQueryReturning_passingOption: Property = Property(name="passingOption", type=StringType)
query_XMLValueFunctionQueryReturning.attributes={query_XMLValueFunctionQueryReturning_returningOption, query_XMLValueFunctionQueryReturning_passingOption}

# query_XMLValueFunctionText class attributes and methods
query_XMLValueFunctionText_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLValueFunctionText.attributes={query_XMLValueFunctionText_returningOption}

# query_XMLValueFunctionTextContent class attributes and methods

# query_XMLValueFunctionValidate class attributes and methods
query_XMLValueFunctionValidate_contentOption: Property = Property(name="contentOption", type=StringType)
query_XMLValueFunctionValidate.attributes={query_XMLValueFunctionValidate_contentOption}

# query_XMLValueFunctionValidateContent class attributes and methods

# query_XMLValueFunctionValidateAccordingTo class attributes and methods

# query_XMLValueExpressionCast class attributes and methods
query_XMLValueExpressionCast_passingMechanism: Property = Property(name="passingMechanism", type=StringType)
query_XMLValueExpressionCast.attributes={query_XMLValueExpressionCast_passingMechanism}

# ValueExpressionCast class attributes and methods

# query_XMLPredicate class attributes and methods

# Predicate class attributes and methods

# query_XMLPredicateContent class attributes and methods

# XMLPredicate class attributes and methods

# query_XMLPredicateDocument class attributes and methods

# query_XMLPredicateValid class attributes and methods

# query_XMLPredicateExists class attributes and methods

# query_XMLQueryArgumentItem class attributes and methods
query_XMLQueryArgumentItem_passingMechanism: Property = Property(name="passingMechanism", type=StringType)
query_XMLQueryArgumentItem.attributes={query_XMLQueryArgumentItem_passingMechanism}

# query_XMLTableFunction class attributes and methods
query_XMLTableFunction_tableRowPattern: Property = Property(name="tableRowPattern", type=StringType)
query_XMLTableFunction.attributes={query_XMLTableFunction_tableRowPattern}

# query_XMLSerializeFunctionTarget class attributes and methods

# query_XMLSerializeFunctionEncoding class attributes and methods
query_XMLSerializeFunctionEncoding_encodingName: Property = Property(name="encodingName", type=StringType)
query_XMLSerializeFunctionEncoding.attributes={query_XMLSerializeFunctionEncoding_encodingName}

# query_XMLSerializeFunction class attributes and methods
query_XMLSerializeFunction_contentOption: Property = Property(name="contentOption", type=StringType)
query_XMLSerializeFunction_serializeVersion: Property = Property(name="serializeVersion", type=StringType)
query_XMLSerializeFunction_declarationOption: Property = Property(name="declarationOption", type=StringType)
query_XMLSerializeFunction.attributes={query_XMLSerializeFunction_serializeVersion, query_XMLSerializeFunction_declarationOption, query_XMLSerializeFunction_contentOption}

# query_XMLAggregateFunction class attributes and methods
query_XMLAggregateFunction_returningOption: Property = Property(name="returningOption", type=StringType)
query_XMLAggregateFunction.attributes={query_XMLAggregateFunction_returningOption}

# query_XMLAggregateSortSpecification class attributes and methods

# query_OrderBySpecification class attributes and methods

# TableFunction class attributes and methods

# query_XMLTableColumnDefinitionItem class attributes and methods

# query_XMLTableColumnDefinitionRegular class attributes and methods
query_XMLTableColumnDefinitionRegular_passingOption: Property = Property(name="passingOption", type=StringType)
query_XMLTableColumnDefinitionRegular_tableColumnPattern: Property = Property(name="tableColumnPattern", type=StringType)
query_XMLTableColumnDefinitionRegular.attributes={query_XMLTableColumnDefinitionRegular_passingOption, query_XMLTableColumnDefinitionRegular_tableColumnPattern}

# XMLTableColumnDefinitionItem class attributes and methods

# query_XMLTableColumnDefinitionDefault class attributes and methods

# query_XMLTableColumnDefinitionOrdinality class attributes and methods

# query_XMLValueFunctionValidateElement class attributes and methods

# query_XMLValueFunctionValidateAccordingToURI class attributes and methods
query_XMLValueFunctionValidateAccordingToURI_noNamespace: Property = Property(name="noNamespace", type=BooleanType)
query_XMLValueFunctionValidateAccordingToURI_targetNamespaceURI: Property = Property(name="targetNamespaceURI", type=StringType)
query_XMLValueFunctionValidateAccordingToURI_schemaLocationURI: Property = Property(name="schemaLocationURI", type=StringType)
query_XMLValueFunctionValidateAccordingToURI.attributes={query_XMLValueFunctionValidateAccordingToURI_schemaLocationURI, query_XMLValueFunctionValidateAccordingToURI_targetNamespaceURI, query_XMLValueFunctionValidateAccordingToURI_noNamespace}

# XMLValueFunctionValidateAccordingTo class attributes and methods

# DataType class attributes and methods

# query_XMLValueFunctionValidateAccordingToIdentifier class attributes and methods
query_XMLValueFunctionValidateAccordingToIdentifier_schemaName: Property = Property(name="schemaName", type=StringType)
query_XMLValueFunctionValidateAccordingToIdentifier_registeredXMLSchemaName: Property = Property(name="registeredXMLSchemaName", type=StringType)
query_XMLValueFunctionValidateAccordingToIdentifier.attributes={query_XMLValueFunctionValidateAccordingToIdentifier_schemaName, query_XMLValueFunctionValidateAccordingToIdentifier_registeredXMLSchemaName}

# query_XMLValueFunctionValidateElementName class attributes and methods

# query_XMLValueFunctionValidateElementNamespace class attributes and methods
query_XMLValueFunctionValidateElementNamespace_noNamespace: Property = Property(name="noNamespace", type=BooleanType)
query_XMLValueFunctionValidateElementNamespace_namespaceURI: Property = Property(name="namespaceURI", type=StringType)
query_XMLValueFunctionValidateElementNamespace.attributes={query_XMLValueFunctionValidateElementNamespace_namespaceURI, query_XMLValueFunctionValidateElementNamespace_noNamespace}

# Relationships
valueExpr1: BinaryAssociation = BinaryAssociation(
    name="valueExpr1",
    ends={
        Property(name="query_QueryValueExpression", type=query_XMLAttributeDeclarationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLAttributeDeclarationItem", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concatContentList0: BinaryAssociation = BinaryAssociation(
    name="concatContentList0",
    ends={
        Property(name="XMLValueFunctionConcatContentItem", type=query_XMLValueFunctionConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionConcat", type=query_XMLValueFunctionConcatContentItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attributesDecl2: BinaryAssociation = BinaryAssociation(
    name="attributesDecl2",
    ends={
        Property(name="XMLAttributesDeclaration", type=query_XMLAttributeDeclarationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeDeclItem", type=query_XMLAttributesDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elementContentList7: BinaryAssociation = BinaryAssociation(
    name="elementContentList7",
    ends={
        Property(name="XMLValueFunctionElementContentList", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionElement8", type=query_XMLValueFunctionElementContentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespacesDecl3: BinaryAssociation = BinaryAssociation(
    name="namespacesDecl3",
    ends={
        Property(name="XMLNamespacesDeclaration", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionElement", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespacesDecl9: BinaryAssociation = BinaryAssociation(
    name="namespacesDecl9",
    ends={
        Property(name="XMLNamespacesDeclaration10", type=query_XMLNamespaceDeclarationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="namespaceDecltemList", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr11: BinaryAssociation = BinaryAssociation(
    name="valueExpr11",
    ends={
        Property(name="query_QueryValueExpression12", type=query_XMLValueFunctionElementContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionElementContentItem", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementContentList13: BinaryAssociation = BinaryAssociation(
    name="elementContentList13",
    ends={
        Property(name="XMLValueFunctionElementContentList14", type=query_XMLValueFunctionElementContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="elementContentListChildren", type=query_XMLValueFunctionElementContentList, multiplicity=Multiplicity(1, 1))
    }
)
attributesDecl4: BinaryAssociation = BinaryAssociation(
    name="attributesDecl4",
    ends={
        Property(name="XMLAttributesDeclaration6", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionElement5", type=query_XMLAttributesDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forestContentList15: BinaryAssociation = BinaryAssociation(
    name="forestContentList15",
    ends={
        Property(name="valueFunctionForest", type=query_XMLValueFunctionForestContentItem, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="XMLValueFunctionForestContentItem", type=query_XMLValueFunctionForest, multiplicity=Multiplicity(1, 1))
    }
)
namespacesDecl16: BinaryAssociation = BinaryAssociation(
    name="namespacesDecl16",
    ends={
        Property(name="XMLNamespacesDeclaration18", type=query_XMLValueFunctionForest, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionForest17", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commentContent19: BinaryAssociation = BinaryAssociation(
    name="commentContent19",
    ends={
        Property(name="XMLValueFunctionCommentContent", type=query_XMLValueFunctionComment, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionComment", type=query_XMLValueFunctionCommentContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
documentContent20: BinaryAssociation = BinaryAssociation(
    name="documentContent20",
    ends={
        Property(name="XMLValueFunctionDocumentContent", type=query_XMLValueFunctionDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionDocument", type=query_XMLValueFunctionDocumentContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parseContent21: BinaryAssociation = BinaryAssociation(
    name="parseContent21",
    ends={
        Property(name="XMLValueFunctionParseContent", type=query_XMLValueFunctionParse, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionParse", type=query_XMLValueFunctionParseContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PIContent22: BinaryAssociation = BinaryAssociation(
    name="PIContent22",
    ends={
        Property(name="XMLValueFunctionPIContent", type=query_XMLValueFunctionPI, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionPI", type=query_XMLValueFunctionPIContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xqueryExpr23: BinaryAssociation = BinaryAssociation(
    name="xqueryExpr23",
    ends={
        Property(name="XMLQueryExpression", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionQuery", type=query_XMLQueryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xqueryArgList24: BinaryAssociation = BinaryAssociation(
    name="xqueryArgList24",
    ends={
        Property(name="XMLQueryArgumentList", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionQuery25", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
queryReturning26: BinaryAssociation = BinaryAssociation(
    name="queryReturning26",
    ends={
        Property(name="XMLValueFunctionQueryReturning", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionQuery27", type=query_XMLValueFunctionQueryReturning, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textContent28: BinaryAssociation = BinaryAssociation(
    name="textContent28",
    ends={
        Property(name="XMLValueFunctionTextContent", type=query_XMLValueFunctionText, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionText", type=query_XMLValueFunctionTextContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
validateContent29: BinaryAssociation = BinaryAssociation(
    name="validateContent29",
    ends={
        Property(name="XMLValueFunctionValidateContent", type=query_XMLValueFunctionValidate, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionValidate", type=query_XMLValueFunctionValidateContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
validateAccordingTo30: BinaryAssociation = BinaryAssociation(
    name="validateAccordingTo30",
    ends={
        Property(name="XMLValueFunctionValidateAccordingTo", type=query_XMLValueFunctionValidate, multiplicity=Multiplicity(1, 1)),
        Property(name="valueFunctionValidate31", type=query_XMLValueFunctionValidateAccordingTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xqueryExpr32: BinaryAssociation = BinaryAssociation(
    name="xqueryExpr32",
    ends={
        Property(name="XMLQueryExpression33", type=query_XMLPredicateExists, multiplicity=Multiplicity(1, 1)),
        Property(name="predicateExists", type=query_XMLQueryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xqueryArgList34: BinaryAssociation = BinaryAssociation(
    name="xqueryArgList34",
    ends={
        Property(name="XMLQueryArgumentList36", type=query_XMLPredicateExists, multiplicity=Multiplicity(1, 1)),
        Property(name="predicateExists35", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicateExists37: BinaryAssociation = BinaryAssociation(
    name="predicateExists37",
    ends={
        Property(name="XMLPredicateExists", type=query_XMLQueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryExpr", type=query_XMLPredicateExists, multiplicity=Multiplicity(1, 1))
    }
)
valueFunctionQuery38: BinaryAssociation = BinaryAssociation(
    name="valueFunctionQuery38",
    ends={
        Property(name="XMLValueFunctionQuery", type=query_XMLQueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryExpr39", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1))
    }
)
predicateExists40: BinaryAssociation = BinaryAssociation(
    name="predicateExists40",
    ends={
        Property(name="xqueryArgList", type=query_XMLPredicateExists, multiplicity=Multiplicity(1, 1)),
        Property(name="XMLPredicateExists41", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(1, 1))
    }
)
xqueryArgListChildren42: BinaryAssociation = BinaryAssociation(
    name="xqueryArgListChildren42",
    ends={
        Property(name="XMLQueryArgumentItem", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryArgList43", type=query_XMLQueryArgumentItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueFunctionQuery44: BinaryAssociation = BinaryAssociation(
    name="valueFunctionQuery44",
    ends={
        Property(name="XMLValueFunctionQuery46", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryArgList45", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1))
    }
)
tableFunction47: BinaryAssociation = BinaryAssociation(
    name="tableFunction47",
    ends={
        Property(name="XMLTableFunction", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryArgList48", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1))
    }
)
xqueryArgList49: BinaryAssociation = BinaryAssociation(
    name="xqueryArgList49",
    ends={
        Property(name="XMLQueryArgumentList50", type=query_XMLQueryArgumentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="xqueryArgListChildren", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr51: BinaryAssociation = BinaryAssociation(
    name="valueExpr51",
    ends={
        Property(name="query_QueryValueExpression52", type=query_XMLQueryArgumentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLQueryArgumentItem", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
serializeTarget53: BinaryAssociation = BinaryAssociation(
    name="serializeTarget53",
    ends={
        Property(name="XMLSerializeFunctionTarget", type=query_XMLSerializeFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="serializeFunction", type=query_XMLSerializeFunctionTarget, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
serializeEncoding54: BinaryAssociation = BinaryAssociation(
    name="serializeEncoding54",
    ends={
        Property(name="query_XMLSerializeFunctionEncoding", type=query_XMLSerializeFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLSerializeFunction", type=query_XMLSerializeFunctionEncoding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serializeFunction55: BinaryAssociation = BinaryAssociation(
    name="serializeFunction55",
    ends={
        Property(name="XMLSerializeFunction", type=query_XMLSerializeFunctionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="serializeTarget", type=query_XMLSerializeFunction, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr56: BinaryAssociation = BinaryAssociation(
    name="valueExpr56",
    ends={
        Property(name="query_QueryValueExpression57", type=query_XMLSerializeFunctionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLSerializeFunctionTarget", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sortSpecList58: BinaryAssociation = BinaryAssociation(
    name="sortSpecList58",
    ends={
        Property(name="XMLAggregateSortSpecification", type=query_XMLAggregateFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregateFunction", type=query_XMLAggregateSortSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueFunctionConcat59: BinaryAssociation = BinaryAssociation(
    name="valueFunctionConcat59",
    ends={
        Property(name="XMLValueFunctionConcat", type=query_XMLValueFunctionConcatContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="concatContentList", type=query_XMLValueFunctionConcat, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr60: BinaryAssociation = BinaryAssociation(
    name="valueExpr60",
    ends={
        Property(name="query_QueryValueExpression61", type=query_XMLValueFunctionConcatContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionConcatContentItem", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr63: BinaryAssociation = BinaryAssociation(
    name="valueExpr63",
    ends={
        Property(name="query_QueryValueExpression64", type=query_XMLValueFunctionCommentContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionCommentContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueFunctionDocument65: BinaryAssociation = BinaryAssociation(
    name="valueFunctionDocument65",
    ends={
        Property(name="XMLValueFunctionDocument", type=query_XMLValueFunctionDocumentContent, multiplicity=Multiplicity(1, 1)),
        Property(name="documentContent", type=query_XMLValueFunctionDocument, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr66: BinaryAssociation = BinaryAssociation(
    name="valueExpr66",
    ends={
        Property(name="query_QueryValueExpression67", type=query_XMLValueFunctionDocumentContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionDocumentContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aggregateFunction68: BinaryAssociation = BinaryAssociation(
    name="aggregateFunction68",
    ends={
        Property(name="XMLAggregateFunction", type=query_XMLAggregateSortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="sortSpecList", type=query_XMLAggregateFunction, multiplicity=Multiplicity(1, 1))
    }
)
orderBySpec69: BinaryAssociation = BinaryAssociation(
    name="orderBySpec69",
    ends={
        Property(name="query_OrderBySpecification", type=query_XMLAggregateSortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLAggregateSortSpecification", type=query_OrderBySpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueFunctionComment62: BinaryAssociation = BinaryAssociation(
    name="valueFunctionComment62",
    ends={
        Property(name="XMLValueFunctionComment", type=query_XMLValueFunctionCommentContent, multiplicity=Multiplicity(1, 1)),
        Property(name="commentContent", type=query_XMLValueFunctionComment, multiplicity=Multiplicity(1, 1))
    }
)
valueFunctionForest70: BinaryAssociation = BinaryAssociation(
    name="valueFunctionForest70",
    ends={
        Property(name="XMLValueFunctionForest", type=query_XMLValueFunctionForestContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="forestContentList", type=query_XMLValueFunctionForest, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr71: BinaryAssociation = BinaryAssociation(
    name="valueExpr71",
    ends={
        Property(name="query_QueryValueExpression72", type=query_XMLValueFunctionForestContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionForestContentItem", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueFunctionParse73: BinaryAssociation = BinaryAssociation(
    name="valueFunctionParse73",
    ends={
        Property(name="XMLValueFunctionParse", type=query_XMLValueFunctionParseContent, multiplicity=Multiplicity(1, 1)),
        Property(name="parseContent", type=query_XMLValueFunctionParse, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr74: BinaryAssociation = BinaryAssociation(
    name="valueExpr74",
    ends={
        Property(name="query_QueryValueExpression75", type=query_XMLValueFunctionParseContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionParseContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueFunctionPI76: BinaryAssociation = BinaryAssociation(
    name="valueFunctionPI76",
    ends={
        Property(name="XMLValueFunctionPI", type=query_XMLValueFunctionPIContent, multiplicity=Multiplicity(1, 1)),
        Property(name="PIContent", type=query_XMLValueFunctionPI, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr77: BinaryAssociation = BinaryAssociation(
    name="valueExpr77",
    ends={
        Property(name="query_QueryValueExpression78", type=query_XMLValueFunctionPIContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionPIContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xqueryArgList79: BinaryAssociation = BinaryAssociation(
    name="xqueryArgList79",
    ends={
        Property(name="XMLQueryArgumentList80", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="tableFunction", type=query_XMLQueryArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnDefList81: BinaryAssociation = BinaryAssociation(
    name="columnDefList81",
    ends={
        Property(name="XMLTableColumnDefinitionItem", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="tableFunction82", type=query_XMLTableColumnDefinitionItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
namespacesDecl83: BinaryAssociation = BinaryAssociation(
    name="namespacesDecl83",
    ends={
        Property(name="XMLNamespacesDeclaration85", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="tableFunction84", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueFunctionText86: BinaryAssociation = BinaryAssociation(
    name="valueFunctionText86",
    ends={
        Property(name="textContent", type=query_XMLValueFunctionText, multiplicity=Multiplicity(1, 1)),
        Property(name="XMLValueFunctionText", type=query_XMLValueFunctionTextContent, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr87: BinaryAssociation = BinaryAssociation(
    name="valueExpr87",
    ends={
        Property(name="query_QueryValueExpression88", type=query_XMLValueFunctionTextContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionTextContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueFunctionValidate89: BinaryAssociation = BinaryAssociation(
    name="valueFunctionValidate89",
    ends={
        Property(name="XMLValueFunctionValidate", type=query_XMLValueFunctionValidateContent, multiplicity=Multiplicity(1, 1)),
        Property(name="validateContent", type=query_XMLValueFunctionValidate, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr90: BinaryAssociation = BinaryAssociation(
    name="valueExpr90",
    ends={
        Property(name="query_QueryValueExpression91", type=query_XMLValueFunctionValidateContent, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLValueFunctionValidateContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableFunction92: BinaryAssociation = BinaryAssociation(
    name="tableFunction92",
    ends={
        Property(name="XMLTableFunction93", type=query_XMLTableColumnDefinitionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="columnDefList", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1))
    }
)
dataType94: BinaryAssociation = BinaryAssociation(
    name="dataType94",
    ends={
        Property(name="DataType", type=query_XMLTableColumnDefinitionRegular, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLTableColumnDefinitionRegular", type=DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnDefinitionDefault95: BinaryAssociation = BinaryAssociation(
    name="columnDefinitionDefault95",
    ends={
        Property(name="XMLTableColumnDefinitionDefault", type=query_XMLTableColumnDefinitionRegular, multiplicity=Multiplicity(1, 1)),
        Property(name="columnDefinitionRegular", type=query_XMLTableColumnDefinitionDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueFunctionValidate96: BinaryAssociation = BinaryAssociation(
    name="valueFunctionValidate96",
    ends={
        Property(name="XMLValueFunctionValidate97", type=query_XMLValueFunctionValidateAccordingTo, multiplicity=Multiplicity(1, 1)),
        Property(name="validateAccordingTo", type=query_XMLValueFunctionValidate, multiplicity=Multiplicity(1, 1))
    }
)
validateElement98: BinaryAssociation = BinaryAssociation(
    name="validateElement98",
    ends={
        Property(name="XMLValueFunctionValidateElement", type=query_XMLValueFunctionValidateAccordingTo, multiplicity=Multiplicity(1, 1)),
        Property(name="validateAccordingTo99", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validateElement100: BinaryAssociation = BinaryAssociation(
    name="validateElement100",
    ends={
        Property(name="XMLValueFunctionValidateElement101", type=query_XMLValueFunctionValidateElementName, multiplicity=Multiplicity(1, 1)),
        Property(name="validateElementName", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(1, 1))
    }
)
validateElement102: BinaryAssociation = BinaryAssociation(
    name="validateElement102",
    ends={
        Property(name="XMLValueFunctionValidateElement103", type=query_XMLValueFunctionValidateElementNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="validateElementNamespace", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(1, 1))
    }
)
namespaceDecltemList104: BinaryAssociation = BinaryAssociation(
    name="namespaceDecltemList104",
    ends={
        Property(name="XMLNamespaceDeclarationItem", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="namespacesDecl", type=query_XMLNamespaceDeclarationItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueFunctionElement105: BinaryAssociation = BinaryAssociation(
    name="valueFunctionElement105",
    ends={
        Property(name="XMLValueFunctionElement", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="namespacesDecl106", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1))
    }
)
valueFunctionForest107: BinaryAssociation = BinaryAssociation(
    name="valueFunctionForest107",
    ends={
        Property(name="XMLValueFunctionForest109", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="namespacesDecl108", type=query_XMLValueFunctionForest, multiplicity=Multiplicity(1, 1))
    }
)
tableFunction110: BinaryAssociation = BinaryAssociation(
    name="tableFunction110",
    ends={
        Property(name="XMLTableFunction112", type=query_XMLNamespacesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="namespacesDecl111", type=query_XMLTableFunction, multiplicity=Multiplicity(1, 1))
    }
)
valueFunctionElement113: BinaryAssociation = BinaryAssociation(
    name="valueFunctionElement113",
    ends={
        Property(name="XMLValueFunctionElement114", type=query_XMLAttributesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="attributesDecl", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1))
    }
)
attributeDeclItem115: BinaryAssociation = BinaryAssociation(
    name="attributeDeclItem115",
    ends={
        Property(name="XMLAttributeDeclarationItem", type=query_XMLAttributesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="attributesDecl116", type=query_XMLAttributeDeclarationItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueFunctionElement117: BinaryAssociation = BinaryAssociation(
    name="valueFunctionElement117",
    ends={
        Property(name="XMLValueFunctionElement118", type=query_XMLValueFunctionElementContentList, multiplicity=Multiplicity(1, 1)),
        Property(name="elementContentList", type=query_XMLValueFunctionElement, multiplicity=Multiplicity(1, 1))
    }
)
elementContentListChildren119: BinaryAssociation = BinaryAssociation(
    name="elementContentListChildren119",
    ends={
        Property(name="XMLValueFunctionElementContentItem", type=query_XMLValueFunctionElementContentList, multiplicity=Multiplicity(1, 1)),
        Property(name="elementContentList120", type=query_XMLValueFunctionElementContentItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueFunctionQuery121: BinaryAssociation = BinaryAssociation(
    name="valueFunctionQuery121",
    ends={
        Property(name="XMLValueFunctionQuery122", type=query_XMLValueFunctionQueryReturning, multiplicity=Multiplicity(1, 1)),
        Property(name="queryReturning", type=query_XMLValueFunctionQuery, multiplicity=Multiplicity(1, 1))
    }
)
validateElementNamespace123: BinaryAssociation = BinaryAssociation(
    name="validateElementNamespace123",
    ends={
        Property(name="XMLValueFunctionValidateElementNamespace", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="validateElement", type=query_XMLValueFunctionValidateElementNamespace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validateElementName124: BinaryAssociation = BinaryAssociation(
    name="validateElementName124",
    ends={
        Property(name="XMLValueFunctionValidateElementName", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="validateElement125", type=query_XMLValueFunctionValidateElementName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validateAccordingTo126: BinaryAssociation = BinaryAssociation(
    name="validateAccordingTo126",
    ends={
        Property(name="XMLValueFunctionValidateAccordingTo128", type=query_XMLValueFunctionValidateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="validateElement127", type=query_XMLValueFunctionValidateAccordingTo, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr129: BinaryAssociation = BinaryAssociation(
    name="valueExpr129",
    ends={
        Property(name="query_QueryValueExpression130", type=query_XMLTableColumnDefinitionDefault, multiplicity=Multiplicity(1, 1)),
        Property(name="query_XMLTableColumnDefinitionDefault", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columnDefinitionRegular131: BinaryAssociation = BinaryAssociation(
    name="columnDefinitionRegular131",
    ends={
        Property(name="XMLTableColumnDefinitionRegular", type=query_XMLTableColumnDefinitionDefault, multiplicity=Multiplicity(1, 1)),
        Property(name="columnDefinitionDefault", type=query_XMLTableColumnDefinitionRegular, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_query_XMLNamespaceDeclarationDefault_XMLNamespaceDeclarationItem = Generalization(general=XMLNamespaceDeclarationItem, specific=query_XMLNamespaceDeclarationDefault)
gen_query_XMLValueFunctionConcat_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionConcat)
gen_query_XMLAttributeDeclarationItem_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLAttributeDeclarationItem)
gen_query_XMLValueFunction_ValueExpressionFunction = Generalization(general=ValueExpressionFunction, specific=query_XMLValueFunction)
gen_query_XMLNamespaceDeclarationPrefix_XMLNamespaceDeclarationItem = Generalization(general=XMLNamespaceDeclarationItem, specific=query_XMLNamespaceDeclarationPrefix)
gen_query_XMLValueFunctionElement_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionElement)
gen_query_XMLNamespaceDeclarationItem_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLNamespaceDeclarationItem)
gen_query_XMLValueFunctionElementContentItem_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionElementContentItem)
gen_query_XMLValueFunctionForest_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionForest)
gen_query_XMLValueFunctionComment_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionComment)
gen_query_XMLValueFunctionDocument_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionDocument)
gen_query_XMLValueFunctionParse_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionParse)
gen_query_XMLValueFunctionPI_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionPI)
gen_query_XMLValueFunctionQuery_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionQuery)
gen_query_XMLValueFunctionText_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionText)
gen_query_XMLValueFunctionValidate_XMLValueFunction = Generalization(general=XMLValueFunction, specific=query_XMLValueFunctionValidate)
gen_query_XMLValueExpressionCast_ValueExpressionCast = Generalization(general=ValueExpressionCast, specific=query_XMLValueExpressionCast)
gen_query_XMLPredicate_Predicate = Generalization(general=Predicate, specific=query_XMLPredicate)
gen_query_XMLPredicateContent_XMLPredicate = Generalization(general=XMLPredicate, specific=query_XMLPredicateContent)
gen_query_XMLPredicateDocument_XMLPredicate = Generalization(general=XMLPredicate, specific=query_XMLPredicateDocument)
gen_query_XMLPredicateValid_XMLPredicate = Generalization(general=XMLPredicate, specific=query_XMLPredicateValid)
gen_query_XMLQueryExpression_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLQueryExpression)
gen_query_XMLQueryArgumentList_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLQueryArgumentList)
gen_query_XMLPredicateExists_XMLPredicate = Generalization(general=XMLPredicate, specific=query_XMLPredicateExists)
gen_query_XMLQueryArgumentItem_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLQueryArgumentItem)
gen_query_XMLSerializeFunctionTarget_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLSerializeFunctionTarget)
gen_query_XMLSerializeFunction_ValueExpressionFunction = Generalization(general=ValueExpressionFunction, specific=query_XMLSerializeFunction)
gen_query_XMLAggregateFunction_ValueExpressionFunction = Generalization(general=ValueExpressionFunction, specific=query_XMLAggregateFunction)
gen_query_XMLValueFunctionConcatContentItem_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionConcatContentItem)
gen_query_XMLValueFunctionCommentContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionCommentContent)
gen_query_XMLValueFunctionDocumentContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionDocumentContent)
gen_query_XMLAggregateSortSpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLAggregateSortSpecification)
gen_query_XMLValueFunctionForestContentItem_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionForestContentItem)
gen_query_XMLValueFunctionParseContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionParseContent)
gen_query_XMLValueFunctionPIContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionPIContent)
gen_query_XMLTableFunction_TableFunction = Generalization(general=TableFunction, specific=query_XMLTableFunction)
gen_query_XMLValueFunctionTextContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionTextContent)
gen_query_XMLValueFunctionValidateContent_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLValueFunctionValidateContent)
gen_query_XMLTableColumnDefinitionItem_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLTableColumnDefinitionItem)
gen_query_XMLTableColumnDefinitionRegular_XMLTableColumnDefinitionItem = Generalization(general=XMLTableColumnDefinitionItem, specific=query_XMLTableColumnDefinitionRegular)
gen_query_XMLTableColumnDefinitionOrdinality_XMLTableColumnDefinitionItem = Generalization(general=XMLTableColumnDefinitionItem, specific=query_XMLTableColumnDefinitionOrdinality)
gen_query_XMLValueFunctionValidateAccordingTo_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionValidateAccordingTo)
gen_query_XMLValueFunctionValidateAccordingToURI_XMLValueFunctionValidateAccordingTo = Generalization(general=XMLValueFunctionValidateAccordingTo, specific=query_XMLValueFunctionValidateAccordingToURI)
gen_query_XMLValueFunctionValidateAccordingToIdentifier_XMLValueFunctionValidateAccordingTo = Generalization(general=XMLValueFunctionValidateAccordingTo, specific=query_XMLValueFunctionValidateAccordingToIdentifier)
gen_query_XMLValueFunctionValidateElementName_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionValidateElementName)
gen_query_XMLValueFunctionValidateElementNamespace_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionValidateElementNamespace)
gen_query_XMLNamespacesDeclaration_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLNamespacesDeclaration)
gen_query_XMLValueFunctionElementContentList_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionElementContentList)
gen_query_XMLValueFunctionQueryReturning_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionQueryReturning)
gen_query_XMLValueFunctionValidateElement_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLValueFunctionValidateElement)
gen_query_XMLTableColumnDefinitionDefault_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_XMLTableColumnDefinitionDefault)
gen_query_XMLSerializeFunctionEncoding_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_XMLSerializeFunctionEncoding)

# Domain Model
domain_model = DomainModel(
    name="query",
    types={query_XMLValueFunctionConcat, XMLValueFunction, query_XMLAttributeDeclarationItem, QueryValueExpression, query_QueryValueExpression, query_XMLAttributesDeclaration, query_XMLValueFunctionConcatContentItem, query_XMLValueFunction, ValueExpressionFunction, query_XMLNamespaceDeclarationPrefix, XMLNamespaceDeclarationItem, query_XMLNamespaceDeclarationDefault, query_XMLValueFunctionElementContentList, query_XMLValueFunctionElement, query_XMLNamespaceDeclarationItem, SQLQueryObject, query_XMLNamespacesDeclaration, query_XMLValueFunctionElementContentItem, query_XMLValueFunctionForest, query_XMLValueFunctionComment, query_XMLValueFunctionCommentContent, query_XMLValueFunctionDocument, query_XMLValueFunctionDocumentContent, query_XMLValueFunctionParse, query_XMLValueFunctionForestContentItem, query_XMLValueFunctionParseContent, query_XMLValueFunctionPI, query_XMLValueFunctionPIContent, query_XMLValueFunctionQuery, query_XMLQueryExpression, query_XMLQueryArgumentList, query_XMLValueFunctionQueryReturning, query_XMLValueFunctionText, query_XMLValueFunctionTextContent, query_XMLValueFunctionValidate, query_XMLValueFunctionValidateContent, query_XMLValueFunctionValidateAccordingTo, query_XMLValueExpressionCast, ValueExpressionCast, query_XMLPredicate, Predicate, query_XMLPredicateContent, XMLPredicate, query_XMLPredicateDocument, query_XMLPredicateValid, query_XMLPredicateExists, query_XMLQueryArgumentItem, query_XMLTableFunction, query_XMLSerializeFunctionTarget, query_XMLSerializeFunctionEncoding, query_XMLSerializeFunction, query_XMLAggregateFunction, query_XMLAggregateSortSpecification, query_OrderBySpecification, TableFunction, query_XMLTableColumnDefinitionItem, query_XMLTableColumnDefinitionRegular, XMLTableColumnDefinitionItem, query_XMLTableColumnDefinitionDefault, query_XMLTableColumnDefinitionOrdinality, query_XMLValueFunctionValidateElement, query_XMLValueFunctionValidateAccordingToURI, XMLValueFunctionValidateAccordingTo, DataType, query_XMLValueFunctionValidateAccordingToIdentifier, query_XMLValueFunctionValidateElementName, query_XMLValueFunctionValidateElementNamespace, XMLPassingType, XMLContentType, XMLDeclarationType, XMLReturningType, XMLNullHandlingType, XMLWhitespaceHandlingType, XMLEmptyHandlingType, XMLContentType2},
    associations={valueExpr1, concatContentList0, attributesDecl2, elementContentList7, namespacesDecl3, namespacesDecl9, valueExpr11, elementContentList13, attributesDecl4, forestContentList15, namespacesDecl16, commentContent19, documentContent20, parseContent21, PIContent22, xqueryExpr23, xqueryArgList24, queryReturning26, textContent28, validateContent29, validateAccordingTo30, xqueryExpr32, xqueryArgList34, predicateExists37, valueFunctionQuery38, predicateExists40, xqueryArgListChildren42, valueFunctionQuery44, tableFunction47, xqueryArgList49, valueExpr51, serializeTarget53, serializeEncoding54, serializeFunction55, valueExpr56, sortSpecList58, valueFunctionConcat59, valueExpr60, valueExpr63, valueFunctionDocument65, valueExpr66, aggregateFunction68, orderBySpec69, valueFunctionComment62, valueFunctionForest70, valueExpr71, valueFunctionParse73, valueExpr74, valueFunctionPI76, valueExpr77, xqueryArgList79, columnDefList81, namespacesDecl83, valueFunctionText86, valueExpr87, valueFunctionValidate89, valueExpr90, tableFunction92, dataType94, columnDefinitionDefault95, valueFunctionValidate96, validateElement98, validateElement100, validateElement102, namespaceDecltemList104, valueFunctionElement105, valueFunctionForest107, tableFunction110, valueFunctionElement113, attributeDeclItem115, valueFunctionElement117, elementContentListChildren119, valueFunctionQuery121, validateElementNamespace123, validateElementName124, validateAccordingTo126, valueExpr129, columnDefinitionRegular131},
    generalizations={gen_query_XMLNamespaceDeclarationDefault_XMLNamespaceDeclarationItem, gen_query_XMLValueFunctionConcat_XMLValueFunction, gen_query_XMLAttributeDeclarationItem_QueryValueExpression, gen_query_XMLValueFunction_ValueExpressionFunction, gen_query_XMLNamespaceDeclarationPrefix_XMLNamespaceDeclarationItem, gen_query_XMLValueFunctionElement_XMLValueFunction, gen_query_XMLNamespaceDeclarationItem_SQLQueryObject, gen_query_XMLValueFunctionElementContentItem_QueryValueExpression, gen_query_XMLValueFunctionForest_XMLValueFunction, gen_query_XMLValueFunctionComment_XMLValueFunction, gen_query_XMLValueFunctionDocument_XMLValueFunction, gen_query_XMLValueFunctionParse_XMLValueFunction, gen_query_XMLValueFunctionPI_XMLValueFunction, gen_query_XMLValueFunctionQuery_XMLValueFunction, gen_query_XMLValueFunctionText_XMLValueFunction, gen_query_XMLValueFunctionValidate_XMLValueFunction, gen_query_XMLValueExpressionCast_ValueExpressionCast, gen_query_XMLPredicate_Predicate, gen_query_XMLPredicateContent_XMLPredicate, gen_query_XMLPredicateDocument_XMLPredicate, gen_query_XMLPredicateValid_XMLPredicate, gen_query_XMLQueryExpression_SQLQueryObject, gen_query_XMLQueryArgumentList_SQLQueryObject, gen_query_XMLPredicateExists_XMLPredicate, gen_query_XMLQueryArgumentItem_QueryValueExpression, gen_query_XMLSerializeFunctionTarget_QueryValueExpression, gen_query_XMLSerializeFunction_ValueExpressionFunction, gen_query_XMLAggregateFunction_ValueExpressionFunction, gen_query_XMLValueFunctionConcatContentItem_QueryValueExpression, gen_query_XMLValueFunctionCommentContent_QueryValueExpression, gen_query_XMLValueFunctionDocumentContent_QueryValueExpression, gen_query_XMLAggregateSortSpecification_SQLQueryObject, gen_query_XMLValueFunctionForestContentItem_QueryValueExpression, gen_query_XMLValueFunctionParseContent_QueryValueExpression, gen_query_XMLValueFunctionPIContent_QueryValueExpression, gen_query_XMLTableFunction_TableFunction, gen_query_XMLValueFunctionTextContent_QueryValueExpression, gen_query_XMLValueFunctionValidateContent_QueryValueExpression, gen_query_XMLTableColumnDefinitionItem_SQLQueryObject, gen_query_XMLTableColumnDefinitionRegular_XMLTableColumnDefinitionItem, gen_query_XMLTableColumnDefinitionOrdinality_XMLTableColumnDefinitionItem, gen_query_XMLValueFunctionValidateAccordingTo_SQLQueryObject, gen_query_XMLValueFunctionValidateAccordingToURI_XMLValueFunctionValidateAccordingTo, gen_query_XMLValueFunctionValidateAccordingToIdentifier_XMLValueFunctionValidateAccordingTo, gen_query_XMLValueFunctionValidateElementName_SQLQueryObject, gen_query_XMLValueFunctionValidateElementNamespace_SQLQueryObject, gen_query_XMLNamespacesDeclaration_SQLQueryObject, gen_query_XMLValueFunctionElementContentList_SQLQueryObject, gen_query_XMLValueFunctionQueryReturning_SQLQueryObject, gen_query_XMLValueFunctionValidateElement_SQLQueryObject, gen_query_XMLTableColumnDefinitionDefault_QueryValueExpression, gen_query_XMLSerializeFunctionEncoding_SQLQueryObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
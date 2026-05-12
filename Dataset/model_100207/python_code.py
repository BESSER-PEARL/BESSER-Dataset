from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class XMLEmptyHandlingType(Enum):
    EMPTY_ON_EMPTY = "EMPTY_ON_EMPTY"
    NULL_ON_EMPTY = "NULL_ON_EMPTY"
    NONE = "NONE"
class XMLContentType2(Enum):
    CONTENT = "CONTENT"
    DOCUMENT = "DOCUMENT"
    SEQUENCE = "SEQUENCE"
    NONE = "NONE"
class XMLNullHandlingType(Enum):
    ABSENT_ON_NULL = "ABSENT_ON_NULL"
    NIL_ON_NULL = "NIL_ON_NULL"
    NULL_ON_NULL = "NULL_ON_NULL"
    NONE = "NONE"
    EMPTY_ON_NULL = "EMPTY_ON_NULL"
    NIL_ON_NO_CONTENT = "NIL_ON_NO_CONTENT"
class XMLContentType(Enum):
    CONTENT = "CONTENT"
    DOCUMENT = "DOCUMENT"
    NONE = "NONE"
class XMLWhitespaceHandlingType(Enum):
    PRESERE_WHITESPACE = "PRESERE_WHITESPACE"
    STRIP_WHITESPACE = "STRIP_WHITESPACE"
    NONE = "NONE"
class XMLReturningType(Enum):
    RETURNING_CONTENT = "RETURNING_CONTENT"
    RETURNING_SEQUENCE = "RETURNING_SEQUENCE"
    NONE = "NONE"
class XMLPassingType(Enum):
    BY_REF = "BY_REF"
    BY_VALUE = "BY_VALUE"
    NONE = "NONE"
class XMLDeclarationType(Enum):
    EXCLUDING_XMLDECLARATION = "EXCLUDING_XMLDECLARATION"
    INCLUDING_XMLDECLARATION = "INCLUDING_XMLDECLARATION"
    NONE = "NONE"


############################################
# Definition of Classes
############################################

class DataType:

    pass
class XMLValueFunctionValidateAccordingTo:

    pass
class query_XMLValueFunctionValidateAccordingToIdentifier(XMLValueFunctionValidateAccordingTo):

    def __init__(self, schemaName: str, registeredXMLSchemaName: str):
        self.schemaName = schemaName
        self.registeredXMLSchemaName = registeredXMLSchemaName
        
        pass
    @property
    def registeredXMLSchemaName(self):
        return self.__registeredXMLSchemaName

    @registeredXMLSchemaName.setter
    def registeredXMLSchemaName(self, registeredXMLSchemaName: str):
        self.__registeredXMLSchemaName = registeredXMLSchemaName


    @property
    def schemaName(self):
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName


class query_XMLValueFunctionValidateAccordingToURI(XMLValueFunctionValidateAccordingTo):

    def __init__(self, noNamespace: bool, targetNamespaceURI: str, schemaLocationURI: str):
        self.noNamespace = noNamespace
        self.targetNamespaceURI = targetNamespaceURI
        self.schemaLocationURI = schemaLocationURI
        
        pass
    @property
    def targetNamespaceURI(self):
        return self.__targetNamespaceURI

    @targetNamespaceURI.setter
    def targetNamespaceURI(self, targetNamespaceURI: str):
        self.__targetNamespaceURI = targetNamespaceURI


    @property
    def noNamespace(self):
        return self.__noNamespace

    @noNamespace.setter
    def noNamespace(self, noNamespace: bool):
        self.__noNamespace = noNamespace


    @property
    def schemaLocationURI(self):
        return self.__schemaLocationURI

    @schemaLocationURI.setter
    def schemaLocationURI(self, schemaLocationURI: str):
        self.__schemaLocationURI = schemaLocationURI


class XMLTableColumnDefinitionItem:

    pass
class query_XMLTableColumnDefinitionOrdinality(XMLTableColumnDefinitionItem):

    pass
class query_XMLTableColumnDefinitionRegular(XMLTableColumnDefinitionItem):

    def __init__(self, passingOption: str, tableColumnPattern: str, query_XMLTableColumnDefinitionRegular: "DataType" = None, columnDefinitionRegular: "query_XMLTableColumnDefinitionDefault" = None, XMLTableColumnDefinitionRegular: "query_XMLTableColumnDefinitionDefault" = None):
        self.passingOption = passingOption
        self.tableColumnPattern = tableColumnPattern
        self.query_XMLTableColumnDefinitionRegular = query_XMLTableColumnDefinitionRegular
        self.columnDefinitionRegular = columnDefinitionRegular
        self.XMLTableColumnDefinitionRegular = XMLTableColumnDefinitionRegular
        
        pass
    @property
    def passingOption(self):
        return self.__passingOption

    @passingOption.setter
    def passingOption(self, passingOption: str):
        self.__passingOption = passingOption


    @property
    def tableColumnPattern(self):
        return self.__tableColumnPattern

    @tableColumnPattern.setter
    def tableColumnPattern(self, tableColumnPattern: str):
        self.__tableColumnPattern = tableColumnPattern


    @property
    def columnDefinitionRegular(self):
        return self.__columnDefinitionRegular

    @columnDefinitionRegular.setter
    def columnDefinitionRegular(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableColumnDefinitionRegular__columnDefinitionRegular", None)
        self.__columnDefinitionRegular = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLTableColumnDefinitionDefault"):
                opp_val = getattr(old_value, "XMLTableColumnDefinitionDefault", None)
                if opp_val == self:
                    setattr(old_value, "XMLTableColumnDefinitionDefault", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLTableColumnDefinitionDefault"):
                opp_val = getattr(value, "XMLTableColumnDefinitionDefault", None)
                setattr(value, "XMLTableColumnDefinitionDefault", self)

    @property
    def XMLTableColumnDefinitionRegular(self):
        return self.__XMLTableColumnDefinitionRegular

    @XMLTableColumnDefinitionRegular.setter
    def XMLTableColumnDefinitionRegular(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableColumnDefinitionRegular__XMLTableColumnDefinitionRegular", None)
        self.__XMLTableColumnDefinitionRegular = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnDefinitionDefault"):
                opp_val = getattr(old_value, "columnDefinitionDefault", None)
                if opp_val == self:
                    setattr(old_value, "columnDefinitionDefault", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnDefinitionDefault"):
                opp_val = getattr(value, "columnDefinitionDefault", None)
                setattr(value, "columnDefinitionDefault", self)

    @property
    def query_XMLTableColumnDefinitionRegular(self):
        return self.__query_XMLTableColumnDefinitionRegular

    @query_XMLTableColumnDefinitionRegular.setter
    def query_XMLTableColumnDefinitionRegular(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableColumnDefinitionRegular__query_XMLTableColumnDefinitionRegular", None)
        self.__query_XMLTableColumnDefinitionRegular = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

class TableFunction:

    pass
class query_OrderBySpecification:

    pass
class query_XMLTableFunction(TableFunction):

    def __init__(self, tableRowPattern: str, XMLTableFunction: "query_XMLQueryArgumentList" = None, tableFunction: "query_XMLQueryArgumentList" = None, tableFunction82: set["query_XMLTableColumnDefinitionItem"] = None, tableFunction84: "query_XMLNamespacesDeclaration" = None, XMLTableFunction93: "query_XMLTableColumnDefinitionItem" = None, XMLTableFunction112: "query_XMLNamespacesDeclaration" = None):
        self.tableRowPattern = tableRowPattern
        self.XMLTableFunction = XMLTableFunction
        self.tableFunction = tableFunction
        self.tableFunction82 = tableFunction82 if tableFunction82 is not None else set()
        self.tableFunction84 = tableFunction84
        self.XMLTableFunction93 = XMLTableFunction93
        self.XMLTableFunction112 = XMLTableFunction112
        
        pass
    @property
    def tableRowPattern(self):
        return self.__tableRowPattern

    @tableRowPattern.setter
    def tableRowPattern(self, tableRowPattern: str):
        self.__tableRowPattern = tableRowPattern


    @property
    def XMLTableFunction(self):
        return self.__XMLTableFunction

    @XMLTableFunction.setter
    def XMLTableFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__XMLTableFunction", None)
        self.__XMLTableFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xqueryArgList48"):
                opp_val = getattr(old_value, "xqueryArgList48", None)
                if opp_val == self:
                    setattr(old_value, "xqueryArgList48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xqueryArgList48"):
                opp_val = getattr(value, "xqueryArgList48", None)
                setattr(value, "xqueryArgList48", self)

    @property
    def XMLTableFunction112(self):
        return self.__XMLTableFunction112

    @XMLTableFunction112.setter
    def XMLTableFunction112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__XMLTableFunction112", None)
        self.__XMLTableFunction112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespacesDecl111"):
                opp_val = getattr(old_value, "namespacesDecl111", None)
                if opp_val == self:
                    setattr(old_value, "namespacesDecl111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespacesDecl111"):
                opp_val = getattr(value, "namespacesDecl111", None)
                setattr(value, "namespacesDecl111", self)

    @property
    def tableFunction84(self):
        return self.__tableFunction84

    @tableFunction84.setter
    def tableFunction84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__tableFunction84", None)
        self.__tableFunction84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLNamespacesDeclaration85"):
                opp_val = getattr(old_value, "XMLNamespacesDeclaration85", None)
                if opp_val == self:
                    setattr(old_value, "XMLNamespacesDeclaration85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLNamespacesDeclaration85"):
                opp_val = getattr(value, "XMLNamespacesDeclaration85", None)
                setattr(value, "XMLNamespacesDeclaration85", self)

    @property
    def tableFunction82(self):
        return self.__tableFunction82

    @tableFunction82.setter
    def tableFunction82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__tableFunction82", None)
        self.__tableFunction82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLTableColumnDefinitionItem"):
                    opp_val = getattr(item, "XMLTableColumnDefinitionItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLTableColumnDefinitionItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLTableColumnDefinitionItem"):
                    opp_val = getattr(item, "XMLTableColumnDefinitionItem", None)
                    
                    setattr(item, "XMLTableColumnDefinitionItem", self)
                    

    @property
    def tableFunction(self):
        return self.__tableFunction

    @tableFunction.setter
    def tableFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__tableFunction", None)
        self.__tableFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLQueryArgumentList80"):
                opp_val = getattr(old_value, "XMLQueryArgumentList80", None)
                if opp_val == self:
                    setattr(old_value, "XMLQueryArgumentList80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLQueryArgumentList80"):
                opp_val = getattr(value, "XMLQueryArgumentList80", None)
                setattr(value, "XMLQueryArgumentList80", self)

    @property
    def XMLTableFunction93(self):
        return self.__XMLTableFunction93

    @XMLTableFunction93.setter
    def XMLTableFunction93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLTableFunction__XMLTableFunction93", None)
        self.__XMLTableFunction93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnDefList"):
                opp_val = getattr(old_value, "columnDefList", None)
                if opp_val == self:
                    setattr(old_value, "columnDefList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnDefList"):
                opp_val = getattr(value, "columnDefList", None)
                setattr(value, "columnDefList", self)

class XMLPredicate:

    pass
class query_XMLPredicateDocument(XMLPredicate):

    pass
class query_XMLPredicateExists(XMLPredicate):

    pass
class query_XMLPredicateValid(XMLPredicate):

    pass
class query_XMLPredicateContent(XMLPredicate):

    pass
class Predicate:

    pass
class query_XMLPredicate(Predicate):

    pass
class ValueExpressionCast:

    pass
class query_XMLValueExpressionCast(ValueExpressionCast):

    def __init__(self, passingMechanism: str):
        self.passingMechanism = passingMechanism
        
        pass
    @property
    def passingMechanism(self):
        return self.__passingMechanism

    @passingMechanism.setter
    def passingMechanism(self, passingMechanism: str):
        self.__passingMechanism = passingMechanism


class SQLQueryObject:

    pass
class query_XMLQueryExpression(SQLQueryObject):

    def __init__(self, xqueryExprContent: str, XMLQueryExpression: "query_XMLValueFunctionQuery" = None, XMLQueryExpression33: "query_XMLPredicateExists" = None, xqueryExpr: "query_XMLPredicateExists" = None, xqueryExpr39: "query_XMLValueFunctionQuery" = None):
        self.xqueryExprContent = xqueryExprContent
        self.XMLQueryExpression = XMLQueryExpression
        self.XMLQueryExpression33 = XMLQueryExpression33
        self.xqueryExpr = xqueryExpr
        self.xqueryExpr39 = xqueryExpr39
        
        pass
    @property
    def xqueryExprContent(self):
        return self.__xqueryExprContent

    @xqueryExprContent.setter
    def xqueryExprContent(self, xqueryExprContent: str):
        self.__xqueryExprContent = xqueryExprContent


    @property
    def XMLQueryExpression(self):
        return self.__XMLQueryExpression

    @XMLQueryExpression.setter
    def XMLQueryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryExpression__XMLQueryExpression", None)
        self.__XMLQueryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueFunctionQuery"):
                opp_val = getattr(old_value, "valueFunctionQuery", None)
                if opp_val == self:
                    setattr(old_value, "valueFunctionQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueFunctionQuery"):
                opp_val = getattr(value, "valueFunctionQuery", None)
                setattr(value, "valueFunctionQuery", self)

    @property
    def xqueryExpr(self):
        return self.__xqueryExpr

    @xqueryExpr.setter
    def xqueryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryExpression__xqueryExpr", None)
        self.__xqueryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLPredicateExists"):
                opp_val = getattr(old_value, "XMLPredicateExists", None)
                if opp_val == self:
                    setattr(old_value, "XMLPredicateExists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLPredicateExists"):
                opp_val = getattr(value, "XMLPredicateExists", None)
                setattr(value, "XMLPredicateExists", self)

    @property
    def XMLQueryExpression33(self):
        return self.__XMLQueryExpression33

    @XMLQueryExpression33.setter
    def XMLQueryExpression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryExpression__XMLQueryExpression33", None)
        self.__XMLQueryExpression33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predicateExists"):
                opp_val = getattr(old_value, "predicateExists", None)
                if opp_val == self:
                    setattr(old_value, "predicateExists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predicateExists"):
                opp_val = getattr(value, "predicateExists", None)
                setattr(value, "predicateExists", self)

    @property
    def xqueryExpr39(self):
        return self.__xqueryExpr39

    @xqueryExpr39.setter
    def xqueryExpr39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryExpression__xqueryExpr39", None)
        self.__xqueryExpr39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionQuery"):
                opp_val = getattr(old_value, "XMLValueFunctionQuery", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionQuery"):
                opp_val = getattr(value, "XMLValueFunctionQuery", None)
                setattr(value, "XMLValueFunctionQuery", self)

class query_XMLQueryArgumentList(SQLQueryObject):

    def __init__(self, passingMechanism: str, xqueryArgList43: set["query_XMLQueryArgumentItem"] = None, xqueryArgList45: "query_XMLValueFunctionQuery" = None, xqueryArgList48: "query_XMLTableFunction" = None, XMLQueryArgumentList: "query_XMLValueFunctionQuery" = None, XMLQueryArgumentList36: "query_XMLPredicateExists" = None, xqueryArgList: "query_XMLPredicateExists" = None, XMLQueryArgumentList50: "query_XMLQueryArgumentItem" = None, XMLQueryArgumentList80: "query_XMLTableFunction" = None):
        self.passingMechanism = passingMechanism
        self.xqueryArgList43 = xqueryArgList43 if xqueryArgList43 is not None else set()
        self.xqueryArgList45 = xqueryArgList45
        self.xqueryArgList48 = xqueryArgList48
        self.XMLQueryArgumentList = XMLQueryArgumentList
        self.XMLQueryArgumentList36 = XMLQueryArgumentList36
        self.xqueryArgList = xqueryArgList
        self.XMLQueryArgumentList50 = XMLQueryArgumentList50
        self.XMLQueryArgumentList80 = XMLQueryArgumentList80
        
        pass
    @property
    def passingMechanism(self):
        return self.__passingMechanism

    @passingMechanism.setter
    def passingMechanism(self, passingMechanism: str):
        self.__passingMechanism = passingMechanism


    @property
    def XMLQueryArgumentList(self):
        return self.__XMLQueryArgumentList

    @XMLQueryArgumentList.setter
    def XMLQueryArgumentList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__XMLQueryArgumentList", None)
        self.__XMLQueryArgumentList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueFunctionQuery25"):
                opp_val = getattr(old_value, "valueFunctionQuery25", None)
                if opp_val == self:
                    setattr(old_value, "valueFunctionQuery25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueFunctionQuery25"):
                opp_val = getattr(value, "valueFunctionQuery25", None)
                setattr(value, "valueFunctionQuery25", self)

    @property
    def xqueryArgList43(self):
        return self.__xqueryArgList43

    @xqueryArgList43.setter
    def xqueryArgList43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__xqueryArgList43", None)
        self.__xqueryArgList43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLQueryArgumentItem"):
                    opp_val = getattr(item, "XMLQueryArgumentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLQueryArgumentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLQueryArgumentItem"):
                    opp_val = getattr(item, "XMLQueryArgumentItem", None)
                    
                    setattr(item, "XMLQueryArgumentItem", self)
                    

    @property
    def XMLQueryArgumentList36(self):
        return self.__XMLQueryArgumentList36

    @XMLQueryArgumentList36.setter
    def XMLQueryArgumentList36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__XMLQueryArgumentList36", None)
        self.__XMLQueryArgumentList36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predicateExists35"):
                opp_val = getattr(old_value, "predicateExists35", None)
                if opp_val == self:
                    setattr(old_value, "predicateExists35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predicateExists35"):
                opp_val = getattr(value, "predicateExists35", None)
                setattr(value, "predicateExists35", self)

    @property
    def xqueryArgList48(self):
        return self.__xqueryArgList48

    @xqueryArgList48.setter
    def xqueryArgList48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__xqueryArgList48", None)
        self.__xqueryArgList48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLTableFunction"):
                opp_val = getattr(old_value, "XMLTableFunction", None)
                if opp_val == self:
                    setattr(old_value, "XMLTableFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLTableFunction"):
                opp_val = getattr(value, "XMLTableFunction", None)
                setattr(value, "XMLTableFunction", self)

    @property
    def XMLQueryArgumentList80(self):
        return self.__XMLQueryArgumentList80

    @XMLQueryArgumentList80.setter
    def XMLQueryArgumentList80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__XMLQueryArgumentList80", None)
        self.__XMLQueryArgumentList80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableFunction"):
                opp_val = getattr(old_value, "tableFunction", None)
                if opp_val == self:
                    setattr(old_value, "tableFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableFunction"):
                opp_val = getattr(value, "tableFunction", None)
                setattr(value, "tableFunction", self)

    @property
    def xqueryArgList(self):
        return self.__xqueryArgList

    @xqueryArgList.setter
    def xqueryArgList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__xqueryArgList", None)
        self.__xqueryArgList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLPredicateExists41"):
                opp_val = getattr(old_value, "XMLPredicateExists41", None)
                if opp_val == self:
                    setattr(old_value, "XMLPredicateExists41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLPredicateExists41"):
                opp_val = getattr(value, "XMLPredicateExists41", None)
                setattr(value, "XMLPredicateExists41", self)

    @property
    def xqueryArgList45(self):
        return self.__xqueryArgList45

    @xqueryArgList45.setter
    def xqueryArgList45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__xqueryArgList45", None)
        self.__xqueryArgList45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionQuery46"):
                opp_val = getattr(old_value, "XMLValueFunctionQuery46", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionQuery46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionQuery46"):
                opp_val = getattr(value, "XMLValueFunctionQuery46", None)
                setattr(value, "XMLValueFunctionQuery46", self)

    @property
    def XMLQueryArgumentList50(self):
        return self.__XMLQueryArgumentList50

    @XMLQueryArgumentList50.setter
    def XMLQueryArgumentList50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentList__XMLQueryArgumentList50", None)
        self.__XMLQueryArgumentList50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xqueryArgListChildren"):
                opp_val = getattr(old_value, "xqueryArgListChildren", None)
                if opp_val == self:
                    setattr(old_value, "xqueryArgListChildren", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xqueryArgListChildren"):
                opp_val = getattr(value, "xqueryArgListChildren", None)
                setattr(value, "xqueryArgListChildren", self)

class query_XMLValueFunctionValidateElementNamespace(SQLQueryObject):

    def __init__(self, noNamespace: bool, namespaceURI: str, XMLValueFunctionValidateElementNamespace: "query_XMLValueFunctionValidateElement" = None, validateElementNamespace: "query_XMLValueFunctionValidateElement" = None):
        self.noNamespace = noNamespace
        self.namespaceURI = namespaceURI
        self.XMLValueFunctionValidateElementNamespace = XMLValueFunctionValidateElementNamespace
        self.validateElementNamespace = validateElementNamespace
        
        pass
    @property
    def namespaceURI(self):
        return self.__namespaceURI

    @namespaceURI.setter
    def namespaceURI(self, namespaceURI: str):
        self.__namespaceURI = namespaceURI


    @property
    def noNamespace(self):
        return self.__noNamespace

    @noNamespace.setter
    def noNamespace(self, noNamespace: bool):
        self.__noNamespace = noNamespace


    @property
    def validateElementNamespace(self):
        return self.__validateElementNamespace

    @validateElementNamespace.setter
    def validateElementNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidateElementNamespace__validateElementNamespace", None)
        self.__validateElementNamespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionValidateElement103"):
                opp_val = getattr(old_value, "XMLValueFunctionValidateElement103", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionValidateElement103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionValidateElement103"):
                opp_val = getattr(value, "XMLValueFunctionValidateElement103", None)
                setattr(value, "XMLValueFunctionValidateElement103", self)

    @property
    def XMLValueFunctionValidateElementNamespace(self):
        return self.__XMLValueFunctionValidateElementNamespace

    @XMLValueFunctionValidateElementNamespace.setter
    def XMLValueFunctionValidateElementNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidateElementNamespace__XMLValueFunctionValidateElementNamespace", None)
        self.__XMLValueFunctionValidateElementNamespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validateElement"):
                opp_val = getattr(old_value, "validateElement", None)
                if opp_val == self:
                    setattr(old_value, "validateElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validateElement"):
                opp_val = getattr(value, "validateElement", None)
                setattr(value, "validateElement", self)

class query_XMLAggregateSortSpecification(SQLQueryObject):

    pass
class query_XMLValueFunctionValidateElement(SQLQueryObject):

    pass
class query_XMLNamespacesDeclaration(SQLQueryObject):

    pass
class query_XMLValueFunctionQueryReturning(SQLQueryObject):

    def __init__(self, returningOption: str, passingOption: str, XMLValueFunctionQueryReturning: "query_XMLValueFunctionQuery" = None, queryReturning: "query_XMLValueFunctionQuery" = None):
        self.returningOption = returningOption
        self.passingOption = passingOption
        self.XMLValueFunctionQueryReturning = XMLValueFunctionQueryReturning
        self.queryReturning = queryReturning
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def passingOption(self):
        return self.__passingOption

    @passingOption.setter
    def passingOption(self, passingOption: str):
        self.__passingOption = passingOption


    @property
    def queryReturning(self):
        return self.__queryReturning

    @queryReturning.setter
    def queryReturning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQueryReturning__queryReturning", None)
        self.__queryReturning = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionQuery122"):
                opp_val = getattr(old_value, "XMLValueFunctionQuery122", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionQuery122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionQuery122"):
                opp_val = getattr(value, "XMLValueFunctionQuery122", None)
                setattr(value, "XMLValueFunctionQuery122", self)

    @property
    def XMLValueFunctionQueryReturning(self):
        return self.__XMLValueFunctionQueryReturning

    @XMLValueFunctionQueryReturning.setter
    def XMLValueFunctionQueryReturning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQueryReturning__XMLValueFunctionQueryReturning", None)
        self.__XMLValueFunctionQueryReturning = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueFunctionQuery27"):
                opp_val = getattr(old_value, "valueFunctionQuery27", None)
                if opp_val == self:
                    setattr(old_value, "valueFunctionQuery27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueFunctionQuery27"):
                opp_val = getattr(value, "valueFunctionQuery27", None)
                setattr(value, "valueFunctionQuery27", self)

class query_XMLValueFunctionValidateAccordingTo(SQLQueryObject):

    pass
class query_XMLTableColumnDefinitionItem(SQLQueryObject):

    pass
class query_XMLValueFunctionValidateElementName(SQLQueryObject):

    pass
class query_XMLSerializeFunctionEncoding(SQLQueryObject):

    def __init__(self, encodingName: str, query_XMLSerializeFunctionEncoding: "query_XMLSerializeFunction" = None):
        self.encodingName = encodingName
        self.query_XMLSerializeFunctionEncoding = query_XMLSerializeFunctionEncoding
        
        pass
    @property
    def encodingName(self):
        return self.__encodingName

    @encodingName.setter
    def encodingName(self, encodingName: str):
        self.__encodingName = encodingName


    @property
    def query_XMLSerializeFunctionEncoding(self):
        return self.__query_XMLSerializeFunctionEncoding

    @query_XMLSerializeFunctionEncoding.setter
    def query_XMLSerializeFunctionEncoding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLSerializeFunctionEncoding__query_XMLSerializeFunctionEncoding", None)
        self.__query_XMLSerializeFunctionEncoding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_XMLSerializeFunction"):
                opp_val = getattr(old_value, "query_XMLSerializeFunction", None)
                if opp_val == self:
                    setattr(old_value, "query_XMLSerializeFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_XMLSerializeFunction"):
                opp_val = getattr(value, "query_XMLSerializeFunction", None)
                setattr(value, "query_XMLSerializeFunction", self)

class query_XMLNamespaceDeclarationItem(SQLQueryObject):

    def __init__(self, uri: str, namespaceDecltemList: "query_XMLNamespacesDeclaration" = None, XMLNamespaceDeclarationItem: "query_XMLNamespacesDeclaration" = None):
        self.uri = uri
        self.namespaceDecltemList = namespaceDecltemList
        self.XMLNamespaceDeclarationItem = XMLNamespaceDeclarationItem
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def namespaceDecltemList(self):
        return self.__namespaceDecltemList

    @namespaceDecltemList.setter
    def namespaceDecltemList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLNamespaceDeclarationItem__namespaceDecltemList", None)
        self.__namespaceDecltemList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLNamespacesDeclaration10"):
                opp_val = getattr(old_value, "XMLNamespacesDeclaration10", None)
                if opp_val == self:
                    setattr(old_value, "XMLNamespacesDeclaration10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLNamespacesDeclaration10"):
                opp_val = getattr(value, "XMLNamespacesDeclaration10", None)
                setattr(value, "XMLNamespacesDeclaration10", self)

    @property
    def XMLNamespaceDeclarationItem(self):
        return self.__XMLNamespaceDeclarationItem

    @XMLNamespaceDeclarationItem.setter
    def XMLNamespaceDeclarationItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLNamespaceDeclarationItem__XMLNamespaceDeclarationItem", None)
        self.__XMLNamespaceDeclarationItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespacesDecl"):
                opp_val = getattr(old_value, "namespacesDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespacesDecl"):
                opp_val = getattr(value, "namespacesDecl", None)
                if opp_val is None:
                    setattr(value, "namespacesDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class query_XMLValueFunctionElementContentList(SQLQueryObject):

    def __init__(self, nullHandlingOption: str, XMLValueFunctionElementContentList: "query_XMLValueFunctionElement" = None, XMLValueFunctionElementContentList14: "query_XMLValueFunctionElementContentItem" = None, elementContentList: "query_XMLValueFunctionElement" = None, elementContentList120: set["query_XMLValueFunctionElementContentItem"] = None):
        self.nullHandlingOption = nullHandlingOption
        self.XMLValueFunctionElementContentList = XMLValueFunctionElementContentList
        self.XMLValueFunctionElementContentList14 = XMLValueFunctionElementContentList14
        self.elementContentList = elementContentList
        self.elementContentList120 = elementContentList120 if elementContentList120 is not None else set()
        
        pass
    @property
    def nullHandlingOption(self):
        return self.__nullHandlingOption

    @nullHandlingOption.setter
    def nullHandlingOption(self, nullHandlingOption: str):
        self.__nullHandlingOption = nullHandlingOption


    @property
    def elementContentList120(self):
        return self.__elementContentList120

    @elementContentList120.setter
    def elementContentList120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElementContentList__elementContentList120", None)
        self.__elementContentList120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLValueFunctionElementContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionElementContentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLValueFunctionElementContentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLValueFunctionElementContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionElementContentItem", None)
                    
                    setattr(item, "XMLValueFunctionElementContentItem", self)
                    

    @property
    def XMLValueFunctionElementContentList(self):
        return self.__XMLValueFunctionElementContentList

    @XMLValueFunctionElementContentList.setter
    def XMLValueFunctionElementContentList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElementContentList__XMLValueFunctionElementContentList", None)
        self.__XMLValueFunctionElementContentList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueFunctionElement8"):
                opp_val = getattr(old_value, "valueFunctionElement8", None)
                if opp_val == self:
                    setattr(old_value, "valueFunctionElement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueFunctionElement8"):
                opp_val = getattr(value, "valueFunctionElement8", None)
                setattr(value, "valueFunctionElement8", self)

    @property
    def XMLValueFunctionElementContentList14(self):
        return self.__XMLValueFunctionElementContentList14

    @XMLValueFunctionElementContentList14.setter
    def XMLValueFunctionElementContentList14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElementContentList__XMLValueFunctionElementContentList14", None)
        self.__XMLValueFunctionElementContentList14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementContentListChildren"):
                opp_val = getattr(old_value, "elementContentListChildren", None)
                if opp_val == self:
                    setattr(old_value, "elementContentListChildren", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementContentListChildren"):
                opp_val = getattr(value, "elementContentListChildren", None)
                setattr(value, "elementContentListChildren", self)

    @property
    def elementContentList(self):
        return self.__elementContentList

    @elementContentList.setter
    def elementContentList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElementContentList__elementContentList", None)
        self.__elementContentList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionElement118"):
                opp_val = getattr(old_value, "XMLValueFunctionElement118", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionElement118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionElement118"):
                opp_val = getattr(value, "XMLValueFunctionElement118", None)
                setattr(value, "XMLValueFunctionElement118", self)

class XMLNamespaceDeclarationItem:

    pass
class query_XMLNamespaceDeclarationDefault(XMLNamespaceDeclarationItem):

    def __init__(self, noDefault: bool):
        self.noDefault = noDefault
        
        pass
    @property
    def noDefault(self):
        return self.__noDefault

    @noDefault.setter
    def noDefault(self, noDefault: bool):
        self.__noDefault = noDefault


class query_XMLNamespaceDeclarationPrefix(XMLNamespaceDeclarationItem):

    def __init__(self, prefix: str):
        self.prefix = prefix
        
        pass
    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


class ValueExpressionFunction:

    pass
class query_XMLAggregateFunction(ValueExpressionFunction):

    def __init__(self, returningOption: str, aggregateFunction: set["query_XMLAggregateSortSpecification"] = None, XMLAggregateFunction: "query_XMLAggregateSortSpecification" = None):
        self.returningOption = returningOption
        self.aggregateFunction = aggregateFunction if aggregateFunction is not None else set()
        self.XMLAggregateFunction = XMLAggregateFunction
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def aggregateFunction(self):
        return self.__aggregateFunction

    @aggregateFunction.setter
    def aggregateFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLAggregateFunction__aggregateFunction", None)
        self.__aggregateFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLAggregateSortSpecification"):
                    opp_val = getattr(item, "XMLAggregateSortSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLAggregateSortSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLAggregateSortSpecification"):
                    opp_val = getattr(item, "XMLAggregateSortSpecification", None)
                    
                    setattr(item, "XMLAggregateSortSpecification", self)
                    

    @property
    def XMLAggregateFunction(self):
        return self.__XMLAggregateFunction

    @XMLAggregateFunction.setter
    def XMLAggregateFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLAggregateFunction__XMLAggregateFunction", None)
        self.__XMLAggregateFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sortSpecList"):
                opp_val = getattr(old_value, "sortSpecList", None)
                if opp_val == self:
                    setattr(old_value, "sortSpecList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sortSpecList"):
                opp_val = getattr(value, "sortSpecList", None)
                setattr(value, "sortSpecList", self)

class query_XMLSerializeFunction(ValueExpressionFunction):

    def __init__(self, contentOption: str, serializeVersion: str, declarationOption: str, serializeFunction: "query_XMLSerializeFunctionTarget" = None, query_XMLSerializeFunction: "query_XMLSerializeFunctionEncoding" = None, XMLSerializeFunction: "query_XMLSerializeFunctionTarget" = None):
        self.contentOption = contentOption
        self.serializeVersion = serializeVersion
        self.declarationOption = declarationOption
        self.serializeFunction = serializeFunction
        self.query_XMLSerializeFunction = query_XMLSerializeFunction
        self.XMLSerializeFunction = XMLSerializeFunction
        
        pass
    @property
    def contentOption(self):
        return self.__contentOption

    @contentOption.setter
    def contentOption(self, contentOption: str):
        self.__contentOption = contentOption


    @property
    def declarationOption(self):
        return self.__declarationOption

    @declarationOption.setter
    def declarationOption(self, declarationOption: str):
        self.__declarationOption = declarationOption


    @property
    def serializeVersion(self):
        return self.__serializeVersion

    @serializeVersion.setter
    def serializeVersion(self, serializeVersion: str):
        self.__serializeVersion = serializeVersion


    @property
    def serializeFunction(self):
        return self.__serializeFunction

    @serializeFunction.setter
    def serializeFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLSerializeFunction__serializeFunction", None)
        self.__serializeFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLSerializeFunctionTarget"):
                opp_val = getattr(old_value, "XMLSerializeFunctionTarget", None)
                if opp_val == self:
                    setattr(old_value, "XMLSerializeFunctionTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLSerializeFunctionTarget"):
                opp_val = getattr(value, "XMLSerializeFunctionTarget", None)
                setattr(value, "XMLSerializeFunctionTarget", self)

    @property
    def XMLSerializeFunction(self):
        return self.__XMLSerializeFunction

    @XMLSerializeFunction.setter
    def XMLSerializeFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLSerializeFunction__XMLSerializeFunction", None)
        self.__XMLSerializeFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "serializeTarget"):
                opp_val = getattr(old_value, "serializeTarget", None)
                if opp_val == self:
                    setattr(old_value, "serializeTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "serializeTarget"):
                opp_val = getattr(value, "serializeTarget", None)
                setattr(value, "serializeTarget", self)

    @property
    def query_XMLSerializeFunction(self):
        return self.__query_XMLSerializeFunction

    @query_XMLSerializeFunction.setter
    def query_XMLSerializeFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLSerializeFunction__query_XMLSerializeFunction", None)
        self.__query_XMLSerializeFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_XMLSerializeFunctionEncoding"):
                opp_val = getattr(old_value, "query_XMLSerializeFunctionEncoding", None)
                if opp_val == self:
                    setattr(old_value, "query_XMLSerializeFunctionEncoding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_XMLSerializeFunctionEncoding"):
                opp_val = getattr(value, "query_XMLSerializeFunctionEncoding", None)
                setattr(value, "query_XMLSerializeFunctionEncoding", self)

class query_XMLValueFunction(ValueExpressionFunction):

    pass
class query_XMLAttributesDeclaration:

    pass
class query_QueryValueExpression:

    pass
class QueryValueExpression:

    pass
class query_XMLTableColumnDefinitionDefault(QueryValueExpression):

    pass
class query_XMLValueFunctionValidateContent(QueryValueExpression):

    pass
class query_XMLValueFunctionPIContent(QueryValueExpression):

    pass
class query_XMLValueFunctionDocumentContent(QueryValueExpression):

    pass
class query_XMLValueFunctionCommentContent(QueryValueExpression):

    pass
class query_XMLValueFunctionConcatContentItem(QueryValueExpression):

    pass
class query_XMLValueFunctionForestContentItem(QueryValueExpression):

    pass
class query_XMLSerializeFunctionTarget(QueryValueExpression):

    pass
class query_XMLQueryArgumentItem(QueryValueExpression):

    def __init__(self, passingMechanism: str, XMLQueryArgumentItem: "query_XMLQueryArgumentList" = None, xqueryArgListChildren: "query_XMLQueryArgumentList" = None, query_XMLQueryArgumentItem: "query_QueryValueExpression" = None):
        self.passingMechanism = passingMechanism
        self.XMLQueryArgumentItem = XMLQueryArgumentItem
        self.xqueryArgListChildren = xqueryArgListChildren
        self.query_XMLQueryArgumentItem = query_XMLQueryArgumentItem
        
        pass
    @property
    def passingMechanism(self):
        return self.__passingMechanism

    @passingMechanism.setter
    def passingMechanism(self, passingMechanism: str):
        self.__passingMechanism = passingMechanism


    @property
    def query_XMLQueryArgumentItem(self):
        return self.__query_XMLQueryArgumentItem

    @query_XMLQueryArgumentItem.setter
    def query_XMLQueryArgumentItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentItem__query_XMLQueryArgumentItem", None)
        self.__query_XMLQueryArgumentItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_QueryValueExpression52"):
                opp_val = getattr(old_value, "query_QueryValueExpression52", None)
                if opp_val == self:
                    setattr(old_value, "query_QueryValueExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_QueryValueExpression52"):
                opp_val = getattr(value, "query_QueryValueExpression52", None)
                setattr(value, "query_QueryValueExpression52", self)

    @property
    def xqueryArgListChildren(self):
        return self.__xqueryArgListChildren

    @xqueryArgListChildren.setter
    def xqueryArgListChildren(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentItem__xqueryArgListChildren", None)
        self.__xqueryArgListChildren = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLQueryArgumentList50"):
                opp_val = getattr(old_value, "XMLQueryArgumentList50", None)
                if opp_val == self:
                    setattr(old_value, "XMLQueryArgumentList50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLQueryArgumentList50"):
                opp_val = getattr(value, "XMLQueryArgumentList50", None)
                setattr(value, "XMLQueryArgumentList50", self)

    @property
    def XMLQueryArgumentItem(self):
        return self.__XMLQueryArgumentItem

    @XMLQueryArgumentItem.setter
    def XMLQueryArgumentItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLQueryArgumentItem__XMLQueryArgumentItem", None)
        self.__XMLQueryArgumentItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xqueryArgList43"):
                opp_val = getattr(old_value, "xqueryArgList43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xqueryArgList43"):
                opp_val = getattr(value, "xqueryArgList43", None)
                if opp_val is None:
                    setattr(value, "xqueryArgList43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class query_XMLValueFunctionParseContent(QueryValueExpression):

    pass
class query_XMLValueFunctionElementContentItem(QueryValueExpression):

    pass
class query_XMLValueFunctionTextContent(QueryValueExpression):

    pass
class query_XMLAttributeDeclarationItem(QueryValueExpression):

    pass
class XMLValueFunction:

    pass
class query_XMLValueFunctionPI(XMLValueFunction):

    def __init__(self, targetName: str, returningOption: str, valueFunctionPI: "query_XMLValueFunctionPIContent" = None, XMLValueFunctionPI: "query_XMLValueFunctionPIContent" = None):
        self.targetName = targetName
        self.returningOption = returningOption
        self.valueFunctionPI = valueFunctionPI
        self.XMLValueFunctionPI = XMLValueFunctionPI
        
        pass
    @property
    def targetName(self):
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName


    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def valueFunctionPI(self):
        return self.__valueFunctionPI

    @valueFunctionPI.setter
    def valueFunctionPI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionPI__valueFunctionPI", None)
        self.__valueFunctionPI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionPIContent"):
                opp_val = getattr(old_value, "XMLValueFunctionPIContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionPIContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionPIContent"):
                opp_val = getattr(value, "XMLValueFunctionPIContent", None)
                setattr(value, "XMLValueFunctionPIContent", self)

    @property
    def XMLValueFunctionPI(self):
        return self.__XMLValueFunctionPI

    @XMLValueFunctionPI.setter
    def XMLValueFunctionPI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionPI__XMLValueFunctionPI", None)
        self.__XMLValueFunctionPI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PIContent"):
                opp_val = getattr(old_value, "PIContent", None)
                if opp_val == self:
                    setattr(old_value, "PIContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PIContent"):
                opp_val = getattr(value, "PIContent", None)
                setattr(value, "PIContent", self)

class query_XMLValueFunctionForest(XMLValueFunction):

    def __init__(self, nullHandlingOption: str, returningOption: str, valueFunctionForest: set["query_XMLValueFunctionForestContentItem"] = None, valueFunctionForest17: "query_XMLNamespacesDeclaration" = None, XMLValueFunctionForest: "query_XMLValueFunctionForestContentItem" = None, XMLValueFunctionForest109: "query_XMLNamespacesDeclaration" = None):
        self.nullHandlingOption = nullHandlingOption
        self.returningOption = returningOption
        self.valueFunctionForest = valueFunctionForest if valueFunctionForest is not None else set()
        self.valueFunctionForest17 = valueFunctionForest17
        self.XMLValueFunctionForest = XMLValueFunctionForest
        self.XMLValueFunctionForest109 = XMLValueFunctionForest109
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def nullHandlingOption(self):
        return self.__nullHandlingOption

    @nullHandlingOption.setter
    def nullHandlingOption(self, nullHandlingOption: str):
        self.__nullHandlingOption = nullHandlingOption


    @property
    def valueFunctionForest17(self):
        return self.__valueFunctionForest17

    @valueFunctionForest17.setter
    def valueFunctionForest17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionForest__valueFunctionForest17", None)
        self.__valueFunctionForest17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLNamespacesDeclaration18"):
                opp_val = getattr(old_value, "XMLNamespacesDeclaration18", None)
                if opp_val == self:
                    setattr(old_value, "XMLNamespacesDeclaration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLNamespacesDeclaration18"):
                opp_val = getattr(value, "XMLNamespacesDeclaration18", None)
                setattr(value, "XMLNamespacesDeclaration18", self)

    @property
    def XMLValueFunctionForest109(self):
        return self.__XMLValueFunctionForest109

    @XMLValueFunctionForest109.setter
    def XMLValueFunctionForest109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionForest__XMLValueFunctionForest109", None)
        self.__XMLValueFunctionForest109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespacesDecl108"):
                opp_val = getattr(old_value, "namespacesDecl108", None)
                if opp_val == self:
                    setattr(old_value, "namespacesDecl108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespacesDecl108"):
                opp_val = getattr(value, "namespacesDecl108", None)
                setattr(value, "namespacesDecl108", self)

    @property
    def valueFunctionForest(self):
        return self.__valueFunctionForest

    @valueFunctionForest.setter
    def valueFunctionForest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionForest__valueFunctionForest", None)
        self.__valueFunctionForest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLValueFunctionForestContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionForestContentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLValueFunctionForestContentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLValueFunctionForestContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionForestContentItem", None)
                    
                    setattr(item, "XMLValueFunctionForestContentItem", self)
                    

    @property
    def XMLValueFunctionForest(self):
        return self.__XMLValueFunctionForest

    @XMLValueFunctionForest.setter
    def XMLValueFunctionForest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionForest__XMLValueFunctionForest", None)
        self.__XMLValueFunctionForest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forestContentList"):
                opp_val = getattr(old_value, "forestContentList", None)
                if opp_val == self:
                    setattr(old_value, "forestContentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forestContentList"):
                opp_val = getattr(value, "forestContentList", None)
                setattr(value, "forestContentList", self)

class query_XMLValueFunctionParse(XMLValueFunction):

    def __init__(self, contentOption: str, whitespaceHandlingOption: str, valueFunctionParse: "query_XMLValueFunctionParseContent" = None, XMLValueFunctionParse: "query_XMLValueFunctionParseContent" = None):
        self.contentOption = contentOption
        self.whitespaceHandlingOption = whitespaceHandlingOption
        self.valueFunctionParse = valueFunctionParse
        self.XMLValueFunctionParse = XMLValueFunctionParse
        
        pass
    @property
    def whitespaceHandlingOption(self):
        return self.__whitespaceHandlingOption

    @whitespaceHandlingOption.setter
    def whitespaceHandlingOption(self, whitespaceHandlingOption: str):
        self.__whitespaceHandlingOption = whitespaceHandlingOption


    @property
    def contentOption(self):
        return self.__contentOption

    @contentOption.setter
    def contentOption(self, contentOption: str):
        self.__contentOption = contentOption


    @property
    def valueFunctionParse(self):
        return self.__valueFunctionParse

    @valueFunctionParse.setter
    def valueFunctionParse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionParse__valueFunctionParse", None)
        self.__valueFunctionParse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionParseContent"):
                opp_val = getattr(old_value, "XMLValueFunctionParseContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionParseContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionParseContent"):
                opp_val = getattr(value, "XMLValueFunctionParseContent", None)
                setattr(value, "XMLValueFunctionParseContent", self)

    @property
    def XMLValueFunctionParse(self):
        return self.__XMLValueFunctionParse

    @XMLValueFunctionParse.setter
    def XMLValueFunctionParse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionParse__XMLValueFunctionParse", None)
        self.__XMLValueFunctionParse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parseContent"):
                opp_val = getattr(old_value, "parseContent", None)
                if opp_val == self:
                    setattr(old_value, "parseContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parseContent"):
                opp_val = getattr(value, "parseContent", None)
                setattr(value, "parseContent", self)

class query_XMLValueFunctionText(XMLValueFunction):

    def __init__(self, returningOption: str, valueFunctionText: "query_XMLValueFunctionTextContent" = None, XMLValueFunctionText: "query_XMLValueFunctionTextContent" = None):
        self.returningOption = returningOption
        self.valueFunctionText = valueFunctionText
        self.XMLValueFunctionText = XMLValueFunctionText
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def XMLValueFunctionText(self):
        return self.__XMLValueFunctionText

    @XMLValueFunctionText.setter
    def XMLValueFunctionText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionText__XMLValueFunctionText", None)
        self.__XMLValueFunctionText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textContent"):
                opp_val = getattr(old_value, "textContent", None)
                if opp_val == self:
                    setattr(old_value, "textContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textContent"):
                opp_val = getattr(value, "textContent", None)
                setattr(value, "textContent", self)

    @property
    def valueFunctionText(self):
        return self.__valueFunctionText

    @valueFunctionText.setter
    def valueFunctionText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionText__valueFunctionText", None)
        self.__valueFunctionText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionTextContent"):
                opp_val = getattr(old_value, "XMLValueFunctionTextContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionTextContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionTextContent"):
                opp_val = getattr(value, "XMLValueFunctionTextContent", None)
                setattr(value, "XMLValueFunctionTextContent", self)

class query_XMLValueFunctionElement(XMLValueFunction):

    def __init__(self, elementName: str, returningOption: str, valueFunctionElement8: "query_XMLValueFunctionElementContentList" = None, valueFunctionElement: "query_XMLNamespacesDeclaration" = None, valueFunctionElement5: "query_XMLAttributesDeclaration" = None, XMLValueFunctionElement118: "query_XMLValueFunctionElementContentList" = None, XMLValueFunctionElement: "query_XMLNamespacesDeclaration" = None, XMLValueFunctionElement114: "query_XMLAttributesDeclaration" = None):
        self.elementName = elementName
        self.returningOption = returningOption
        self.valueFunctionElement8 = valueFunctionElement8
        self.valueFunctionElement = valueFunctionElement
        self.valueFunctionElement5 = valueFunctionElement5
        self.XMLValueFunctionElement118 = XMLValueFunctionElement118
        self.XMLValueFunctionElement = XMLValueFunctionElement
        self.XMLValueFunctionElement114 = XMLValueFunctionElement114
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def elementName(self):
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName


    @property
    def XMLValueFunctionElement114(self):
        return self.__XMLValueFunctionElement114

    @XMLValueFunctionElement114.setter
    def XMLValueFunctionElement114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__XMLValueFunctionElement114", None)
        self.__XMLValueFunctionElement114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributesDecl"):
                opp_val = getattr(old_value, "attributesDecl", None)
                if opp_val == self:
                    setattr(old_value, "attributesDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributesDecl"):
                opp_val = getattr(value, "attributesDecl", None)
                setattr(value, "attributesDecl", self)

    @property
    def XMLValueFunctionElement118(self):
        return self.__XMLValueFunctionElement118

    @XMLValueFunctionElement118.setter
    def XMLValueFunctionElement118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__XMLValueFunctionElement118", None)
        self.__XMLValueFunctionElement118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementContentList"):
                opp_val = getattr(old_value, "elementContentList", None)
                if opp_val == self:
                    setattr(old_value, "elementContentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementContentList"):
                opp_val = getattr(value, "elementContentList", None)
                setattr(value, "elementContentList", self)

    @property
    def valueFunctionElement(self):
        return self.__valueFunctionElement

    @valueFunctionElement.setter
    def valueFunctionElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__valueFunctionElement", None)
        self.__valueFunctionElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLNamespacesDeclaration"):
                opp_val = getattr(old_value, "XMLNamespacesDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "XMLNamespacesDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLNamespacesDeclaration"):
                opp_val = getattr(value, "XMLNamespacesDeclaration", None)
                setattr(value, "XMLNamespacesDeclaration", self)

    @property
    def valueFunctionElement5(self):
        return self.__valueFunctionElement5

    @valueFunctionElement5.setter
    def valueFunctionElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__valueFunctionElement5", None)
        self.__valueFunctionElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLAttributesDeclaration6"):
                opp_val = getattr(old_value, "XMLAttributesDeclaration6", None)
                if opp_val == self:
                    setattr(old_value, "XMLAttributesDeclaration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLAttributesDeclaration6"):
                opp_val = getattr(value, "XMLAttributesDeclaration6", None)
                setattr(value, "XMLAttributesDeclaration6", self)

    @property
    def valueFunctionElement8(self):
        return self.__valueFunctionElement8

    @valueFunctionElement8.setter
    def valueFunctionElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__valueFunctionElement8", None)
        self.__valueFunctionElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionElementContentList"):
                opp_val = getattr(old_value, "XMLValueFunctionElementContentList", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionElementContentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionElementContentList"):
                opp_val = getattr(value, "XMLValueFunctionElementContentList", None)
                setattr(value, "XMLValueFunctionElementContentList", self)

    @property
    def XMLValueFunctionElement(self):
        return self.__XMLValueFunctionElement

    @XMLValueFunctionElement.setter
    def XMLValueFunctionElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionElement__XMLValueFunctionElement", None)
        self.__XMLValueFunctionElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespacesDecl106"):
                opp_val = getattr(old_value, "namespacesDecl106", None)
                if opp_val == self:
                    setattr(old_value, "namespacesDecl106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespacesDecl106"):
                opp_val = getattr(value, "namespacesDecl106", None)
                setattr(value, "namespacesDecl106", self)

class query_XMLValueFunctionDocument(XMLValueFunction):

    def __init__(self, returningOption: str, valueFunctionDocument: "query_XMLValueFunctionDocumentContent" = None, XMLValueFunctionDocument: "query_XMLValueFunctionDocumentContent" = None):
        self.returningOption = returningOption
        self.valueFunctionDocument = valueFunctionDocument
        self.XMLValueFunctionDocument = XMLValueFunctionDocument
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def valueFunctionDocument(self):
        return self.__valueFunctionDocument

    @valueFunctionDocument.setter
    def valueFunctionDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionDocument__valueFunctionDocument", None)
        self.__valueFunctionDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionDocumentContent"):
                opp_val = getattr(old_value, "XMLValueFunctionDocumentContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionDocumentContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionDocumentContent"):
                opp_val = getattr(value, "XMLValueFunctionDocumentContent", None)
                setattr(value, "XMLValueFunctionDocumentContent", self)

    @property
    def XMLValueFunctionDocument(self):
        return self.__XMLValueFunctionDocument

    @XMLValueFunctionDocument.setter
    def XMLValueFunctionDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionDocument__XMLValueFunctionDocument", None)
        self.__XMLValueFunctionDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentContent"):
                opp_val = getattr(old_value, "documentContent", None)
                if opp_val == self:
                    setattr(old_value, "documentContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentContent"):
                opp_val = getattr(value, "documentContent", None)
                setattr(value, "documentContent", self)

class query_XMLValueFunctionComment(XMLValueFunction):

    def __init__(self, returningOption: str, valueFunctionComment: "query_XMLValueFunctionCommentContent" = None, XMLValueFunctionComment: "query_XMLValueFunctionCommentContent" = None):
        self.returningOption = returningOption
        self.valueFunctionComment = valueFunctionComment
        self.XMLValueFunctionComment = XMLValueFunctionComment
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def valueFunctionComment(self):
        return self.__valueFunctionComment

    @valueFunctionComment.setter
    def valueFunctionComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionComment__valueFunctionComment", None)
        self.__valueFunctionComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionCommentContent"):
                opp_val = getattr(old_value, "XMLValueFunctionCommentContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionCommentContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionCommentContent"):
                opp_val = getattr(value, "XMLValueFunctionCommentContent", None)
                setattr(value, "XMLValueFunctionCommentContent", self)

    @property
    def XMLValueFunctionComment(self):
        return self.__XMLValueFunctionComment

    @XMLValueFunctionComment.setter
    def XMLValueFunctionComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionComment__XMLValueFunctionComment", None)
        self.__XMLValueFunctionComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentContent"):
                opp_val = getattr(old_value, "commentContent", None)
                if opp_val == self:
                    setattr(old_value, "commentContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentContent"):
                opp_val = getattr(value, "commentContent", None)
                setattr(value, "commentContent", self)

class query_XMLValueFunctionQuery(XMLValueFunction):

    def __init__(self, emptyHandlingOption: str, XMLValueFunctionQuery46: "query_XMLQueryArgumentList" = None, valueFunctionQuery: "query_XMLQueryExpression" = None, valueFunctionQuery25: "query_XMLQueryArgumentList" = None, valueFunctionQuery27: "query_XMLValueFunctionQueryReturning" = None, XMLValueFunctionQuery: "query_XMLQueryExpression" = None, XMLValueFunctionQuery122: "query_XMLValueFunctionQueryReturning" = None):
        self.emptyHandlingOption = emptyHandlingOption
        self.XMLValueFunctionQuery46 = XMLValueFunctionQuery46
        self.valueFunctionQuery = valueFunctionQuery
        self.valueFunctionQuery25 = valueFunctionQuery25
        self.valueFunctionQuery27 = valueFunctionQuery27
        self.XMLValueFunctionQuery = XMLValueFunctionQuery
        self.XMLValueFunctionQuery122 = XMLValueFunctionQuery122
        
        pass
    @property
    def emptyHandlingOption(self):
        return self.__emptyHandlingOption

    @emptyHandlingOption.setter
    def emptyHandlingOption(self, emptyHandlingOption: str):
        self.__emptyHandlingOption = emptyHandlingOption


    @property
    def XMLValueFunctionQuery46(self):
        return self.__XMLValueFunctionQuery46

    @XMLValueFunctionQuery46.setter
    def XMLValueFunctionQuery46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__XMLValueFunctionQuery46", None)
        self.__XMLValueFunctionQuery46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xqueryArgList45"):
                opp_val = getattr(old_value, "xqueryArgList45", None)
                if opp_val == self:
                    setattr(old_value, "xqueryArgList45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xqueryArgList45"):
                opp_val = getattr(value, "xqueryArgList45", None)
                setattr(value, "xqueryArgList45", self)

    @property
    def valueFunctionQuery(self):
        return self.__valueFunctionQuery

    @valueFunctionQuery.setter
    def valueFunctionQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__valueFunctionQuery", None)
        self.__valueFunctionQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLQueryExpression"):
                opp_val = getattr(old_value, "XMLQueryExpression", None)
                if opp_val == self:
                    setattr(old_value, "XMLQueryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLQueryExpression"):
                opp_val = getattr(value, "XMLQueryExpression", None)
                setattr(value, "XMLQueryExpression", self)

    @property
    def valueFunctionQuery27(self):
        return self.__valueFunctionQuery27

    @valueFunctionQuery27.setter
    def valueFunctionQuery27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__valueFunctionQuery27", None)
        self.__valueFunctionQuery27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionQueryReturning"):
                opp_val = getattr(old_value, "XMLValueFunctionQueryReturning", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionQueryReturning", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionQueryReturning"):
                opp_val = getattr(value, "XMLValueFunctionQueryReturning", None)
                setattr(value, "XMLValueFunctionQueryReturning", self)

    @property
    def XMLValueFunctionQuery122(self):
        return self.__XMLValueFunctionQuery122

    @XMLValueFunctionQuery122.setter
    def XMLValueFunctionQuery122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__XMLValueFunctionQuery122", None)
        self.__XMLValueFunctionQuery122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queryReturning"):
                opp_val = getattr(old_value, "queryReturning", None)
                if opp_val == self:
                    setattr(old_value, "queryReturning", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queryReturning"):
                opp_val = getattr(value, "queryReturning", None)
                setattr(value, "queryReturning", self)

    @property
    def valueFunctionQuery25(self):
        return self.__valueFunctionQuery25

    @valueFunctionQuery25.setter
    def valueFunctionQuery25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__valueFunctionQuery25", None)
        self.__valueFunctionQuery25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLQueryArgumentList"):
                opp_val = getattr(old_value, "XMLQueryArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "XMLQueryArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLQueryArgumentList"):
                opp_val = getattr(value, "XMLQueryArgumentList", None)
                setattr(value, "XMLQueryArgumentList", self)

    @property
    def XMLValueFunctionQuery(self):
        return self.__XMLValueFunctionQuery

    @XMLValueFunctionQuery.setter
    def XMLValueFunctionQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionQuery__XMLValueFunctionQuery", None)
        self.__XMLValueFunctionQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xqueryExpr39"):
                opp_val = getattr(old_value, "xqueryExpr39", None)
                if opp_val == self:
                    setattr(old_value, "xqueryExpr39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xqueryExpr39"):
                opp_val = getattr(value, "xqueryExpr39", None)
                setattr(value, "xqueryExpr39", self)

class query_XMLValueFunctionValidate(XMLValueFunction):

    def __init__(self, contentOption: str, valueFunctionValidate: "query_XMLValueFunctionValidateContent" = None, valueFunctionValidate31: "query_XMLValueFunctionValidateAccordingTo" = None, XMLValueFunctionValidate: "query_XMLValueFunctionValidateContent" = None, XMLValueFunctionValidate97: "query_XMLValueFunctionValidateAccordingTo" = None):
        self.contentOption = contentOption
        self.valueFunctionValidate = valueFunctionValidate
        self.valueFunctionValidate31 = valueFunctionValidate31
        self.XMLValueFunctionValidate = XMLValueFunctionValidate
        self.XMLValueFunctionValidate97 = XMLValueFunctionValidate97
        
        pass
    @property
    def contentOption(self):
        return self.__contentOption

    @contentOption.setter
    def contentOption(self, contentOption: str):
        self.__contentOption = contentOption


    @property
    def XMLValueFunctionValidate(self):
        return self.__XMLValueFunctionValidate

    @XMLValueFunctionValidate.setter
    def XMLValueFunctionValidate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidate__XMLValueFunctionValidate", None)
        self.__XMLValueFunctionValidate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validateContent"):
                opp_val = getattr(old_value, "validateContent", None)
                if opp_val == self:
                    setattr(old_value, "validateContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validateContent"):
                opp_val = getattr(value, "validateContent", None)
                setattr(value, "validateContent", self)

    @property
    def valueFunctionValidate31(self):
        return self.__valueFunctionValidate31

    @valueFunctionValidate31.setter
    def valueFunctionValidate31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidate__valueFunctionValidate31", None)
        self.__valueFunctionValidate31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionValidateAccordingTo"):
                opp_val = getattr(old_value, "XMLValueFunctionValidateAccordingTo", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionValidateAccordingTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionValidateAccordingTo"):
                opp_val = getattr(value, "XMLValueFunctionValidateAccordingTo", None)
                setattr(value, "XMLValueFunctionValidateAccordingTo", self)

    @property
    def XMLValueFunctionValidate97(self):
        return self.__XMLValueFunctionValidate97

    @XMLValueFunctionValidate97.setter
    def XMLValueFunctionValidate97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidate__XMLValueFunctionValidate97", None)
        self.__XMLValueFunctionValidate97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validateAccordingTo"):
                opp_val = getattr(old_value, "validateAccordingTo", None)
                if opp_val == self:
                    setattr(old_value, "validateAccordingTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validateAccordingTo"):
                opp_val = getattr(value, "validateAccordingTo", None)
                setattr(value, "validateAccordingTo", self)

    @property
    def valueFunctionValidate(self):
        return self.__valueFunctionValidate

    @valueFunctionValidate.setter
    def valueFunctionValidate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionValidate__valueFunctionValidate", None)
        self.__valueFunctionValidate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XMLValueFunctionValidateContent"):
                opp_val = getattr(old_value, "XMLValueFunctionValidateContent", None)
                if opp_val == self:
                    setattr(old_value, "XMLValueFunctionValidateContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XMLValueFunctionValidateContent"):
                opp_val = getattr(value, "XMLValueFunctionValidateContent", None)
                setattr(value, "XMLValueFunctionValidateContent", self)

class query_XMLValueFunctionConcat(XMLValueFunction):

    def __init__(self, returningOption: str, valueFunctionConcat: set["query_XMLValueFunctionConcatContentItem"] = None, XMLValueFunctionConcat: "query_XMLValueFunctionConcatContentItem" = None):
        self.returningOption = returningOption
        self.valueFunctionConcat = valueFunctionConcat if valueFunctionConcat is not None else set()
        self.XMLValueFunctionConcat = XMLValueFunctionConcat
        
        pass
    @property
    def returningOption(self):
        return self.__returningOption

    @returningOption.setter
    def returningOption(self, returningOption: str):
        self.__returningOption = returningOption


    @property
    def valueFunctionConcat(self):
        return self.__valueFunctionConcat

    @valueFunctionConcat.setter
    def valueFunctionConcat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionConcat__valueFunctionConcat", None)
        self.__valueFunctionConcat = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XMLValueFunctionConcatContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionConcatContentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XMLValueFunctionConcatContentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XMLValueFunctionConcatContentItem"):
                    opp_val = getattr(item, "XMLValueFunctionConcatContentItem", None)
                    
                    setattr(item, "XMLValueFunctionConcatContentItem", self)
                    

    @property
    def XMLValueFunctionConcat(self):
        return self.__XMLValueFunctionConcat

    @XMLValueFunctionConcat.setter
    def XMLValueFunctionConcat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_XMLValueFunctionConcat__XMLValueFunctionConcat", None)
        self.__XMLValueFunctionConcat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concatContentList"):
                opp_val = getattr(old_value, "concatContentList", None)
                if opp_val == self:
                    setattr(old_value, "concatContentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concatContentList"):
                opp_val = getattr(value, "concatContentList", None)
                setattr(value, "concatContentList", self)

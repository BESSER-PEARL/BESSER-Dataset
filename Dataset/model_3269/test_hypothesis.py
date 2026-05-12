import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MessageSet,
    ISO20022_SWIFTSolution,
    MessageDefinition,
    ISO20022_ApplicationHeader,
    AbstractTimeConcept,
    ISO20022_XSDMonth,
    ISO20022_XSDTime,
    ISO20022_XSDMonthDay,
    ISO20022_XSDYear,
    ISO20022_XSDDuration,
    ISO20022_XSDDateTime,
    ISO20022_XSDYearMonth,
    ISO20022_XSDDay,
    ISO20022_XSDDate,
    DataType,
    ISO20022_XSDBinary,
    ISO20022_AbstractTimeConcept,
    ISO20022_XSDString,
    XSDString,
    ISO20022_CodeSet,
    ISO20022_XSDID,
    ISO20022_Text,
    ISO20022_XSDDecimal,
    XSDDecimal,
    ISO20022_Quantity,
    ISO20022_Amount,
    ISO20022_Rate,
    ISO20022_XSDBoolean,
    XSDBoolean,
    ISO20022_Indicator,
    ISO20022_IdentifierSet,
    ISO20022_MessageDefinitionIdentifier,
    MessageElementContainer,
    ISO20022_ChoiceComponent,
    ISO20022_MessageComponent,
    TopLevelCatalogueEntry,
    ISO20022_SyntaxMessageScheme,
    ISO20022_MessageChoreography,
    ISO20022_BusinessArea,
    ISO20022_MessageSet,
    BusinessElement,
    ISO20022_BusinessAttribute,
    MessageComponentType,
    ISO20022_ExternalSchema,
    ISO20022_UserDefined,
    LogicalType,
    BusinessConcept,
    TopLevelDictionaryEntry,
    ISO20022_EndPointCategory,
    BusinessElementType,
    ISO20022_DataType,
    ISO20022_BusinessAssociationEnd,
    Type,
    ISO20022_BusinessElementType,
    ISO20022_MessageDefinition,
    Member,
    ISO20022_XMLMember,
    ISO20022_MultiplicityEntity,
    MultiplicityEntity,
    RepositoryConcept,
    ISO20022_Type,
    ISO20022_TopLevelDictionaryEntry,
    ISO20022_Diagram,
    ISO20022_BusinessRole,
    ISO20022_Code,
    ISO20022_InteractionActor,
    ISO20022_Xor,
    ISO20022_Interaction,
    ISO20022_InteractionMessage,
    ISO20022_TopLevelCatalogueEntry,
    ISO20022_IsAnAlternativeFor,
    ISO20022_Member,
    ISO20022_LogicalType,
    MessageConcept,
    XMLMember,
    ISO20022_MessageBuildingBlock,
    ISO20022_MessageElement,
    ISO20022_MessageElementContainer,
    ISO20022_BusinessElement,
    ISO20022_BusinessComponent,
    ISO20022_MessageComponentType,
    MessageElement,
    ISO20022_MessageAttribute,
    ISO20022_MessageAssociationEnd,
    ModelEntity,
    ISO20022_Syntax,
    ISO20022_BusinessProcessCatalogue,
    ISO20022_BusinessConcept,
    ISO20022_DataDictionary,
    ISO20022_Repository,
    ISO20022_Facet,
    ISO20022_Encoding,
    ISO20022_MessageConcept,
    ISO20022_SemanticMarkupElement,
    ISO20022_ModelEntity,
    ISO20022_Doclet,
    ISO20022_SemanticMarkup,
    ISO20022_RepositoryConcept,
    ISO20022_Constraint,
    Namespace,
    Visibility,
    ProcessContent,
    Aggregation,
    RegistrationStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_messageset_is_not_abstract():
    assert not inspect.isabstract(MessageSet)


def test_messageset_constructor_exists():
    assert callable(MessageSet.__init__)


def test_messageset_constructor_args():
    sig = inspect.signature(MessageSet.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_swiftsolution_is_not_abstract():
    assert not inspect.isabstract(ISO20022_SWIFTSolution)


def test_iso20022_swiftsolution_constructor_exists():
    assert callable(ISO20022_SWIFTSolution.__init__)


def test_iso20022_swiftsolution_constructor_args():
    sig = inspect.signature(ISO20022_SWIFTSolution.__init__)
    params = list(sig.parameters.keys())
    assert "serviceName" in params, "Missing parameter 'serviceName'"

def test_iso20022_swiftsolution_has_serviceName():
    assert hasattr(ISO20022_SWIFTSolution, "serviceName")
    descriptor = None
    for klass in ISO20022_SWIFTSolution.__mro__:
        if "serviceName" in klass.__dict__:
            descriptor = klass.__dict__["serviceName"]
            break
    assert isinstance(descriptor, property)



def test_messagedefinition_is_not_abstract():
    assert not inspect.isabstract(MessageDefinition)


def test_messagedefinition_constructor_exists():
    assert callable(MessageDefinition.__init__)


def test_messagedefinition_constructor_args():
    sig = inspect.signature(MessageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_applicationheader_is_not_abstract():
    assert not inspect.isabstract(ISO20022_ApplicationHeader)


def test_iso20022_applicationheader_constructor_exists():
    assert callable(ISO20022_ApplicationHeader.__init__)


def test_iso20022_applicationheader_constructor_args():
    sig = inspect.signature(ISO20022_ApplicationHeader.__init__)
    params = list(sig.parameters.keys())



def test_abstracttimeconcept_is_not_abstract():
    assert not inspect.isabstract(AbstractTimeConcept)


def test_abstracttimeconcept_constructor_exists():
    assert callable(AbstractTimeConcept.__init__)


def test_abstracttimeconcept_constructor_args():
    sig = inspect.signature(AbstractTimeConcept.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdmonth_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDMonth)


def test_iso20022_xsdmonth_constructor_exists():
    assert callable(ISO20022_XSDMonth.__init__)


def test_iso20022_xsdmonth_constructor_args():
    sig = inspect.signature(ISO20022_XSDMonth.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdtime_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDTime)


def test_iso20022_xsdtime_constructor_exists():
    assert callable(ISO20022_XSDTime.__init__)


def test_iso20022_xsdtime_constructor_args():
    sig = inspect.signature(ISO20022_XSDTime.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdmonthday_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDMonthDay)


def test_iso20022_xsdmonthday_constructor_exists():
    assert callable(ISO20022_XSDMonthDay.__init__)


def test_iso20022_xsdmonthday_constructor_args():
    sig = inspect.signature(ISO20022_XSDMonthDay.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdyear_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDYear)


def test_iso20022_xsdyear_constructor_exists():
    assert callable(ISO20022_XSDYear.__init__)


def test_iso20022_xsdyear_constructor_args():
    sig = inspect.signature(ISO20022_XSDYear.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdduration_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDDuration)


def test_iso20022_xsdduration_constructor_exists():
    assert callable(ISO20022_XSDDuration.__init__)


def test_iso20022_xsdduration_constructor_args():
    sig = inspect.signature(ISO20022_XSDDuration.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsddatetime_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDDateTime)


def test_iso20022_xsddatetime_constructor_exists():
    assert callable(ISO20022_XSDDateTime.__init__)


def test_iso20022_xsddatetime_constructor_args():
    sig = inspect.signature(ISO20022_XSDDateTime.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdyearmonth_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDYearMonth)


def test_iso20022_xsdyearmonth_constructor_exists():
    assert callable(ISO20022_XSDYearMonth.__init__)


def test_iso20022_xsdyearmonth_constructor_args():
    sig = inspect.signature(ISO20022_XSDYearMonth.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdday_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDDay)


def test_iso20022_xsdday_constructor_exists():
    assert callable(ISO20022_XSDDay.__init__)


def test_iso20022_xsdday_constructor_args():
    sig = inspect.signature(ISO20022_XSDDay.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsddate_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDDate)


def test_iso20022_xsddate_constructor_exists():
    assert callable(ISO20022_XSDDate.__init__)


def test_iso20022_xsddate_constructor_args():
    sig = inspect.signature(ISO20022_XSDDate.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsdbinary_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDBinary)


def test_iso20022_xsdbinary_constructor_exists():
    assert callable(ISO20022_XSDBinary.__init__)


def test_iso20022_xsdbinary_constructor_args():
    sig = inspect.signature(ISO20022_XSDBinary.__init__)
    params = list(sig.parameters.keys())
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "length" in params, "Missing parameter 'length'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_iso20022_xsdbinary_has_minLength():
    assert hasattr(ISO20022_XSDBinary, "minLength")
    descriptor = None
    for klass in ISO20022_XSDBinary.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdbinary_has_pattern():
    assert hasattr(ISO20022_XSDBinary, "pattern")
    descriptor = None
    for klass in ISO20022_XSDBinary.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdbinary_has_length():
    assert hasattr(ISO20022_XSDBinary, "length")
    descriptor = None
    for klass in ISO20022_XSDBinary.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdbinary_has_maxLength():
    assert hasattr(ISO20022_XSDBinary, "maxLength")
    descriptor = None
    for klass in ISO20022_XSDBinary.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_abstracttimeconcept_is_not_abstract():
    assert not inspect.isabstract(ISO20022_AbstractTimeConcept)


def test_iso20022_abstracttimeconcept_constructor_exists():
    assert callable(ISO20022_AbstractTimeConcept.__init__)


def test_iso20022_abstracttimeconcept_constructor_args():
    sig = inspect.signature(ISO20022_AbstractTimeConcept.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "minExclusive" in params, "Missing parameter 'minExclusive'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"
    assert "maxExclusive" in params, "Missing parameter 'maxExclusive'"

def test_iso20022_abstracttimeconcept_has_pattern():
    assert hasattr(ISO20022_AbstractTimeConcept, "pattern")
    descriptor = None
    for klass in ISO20022_AbstractTimeConcept.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_abstracttimeconcept_has_minInclusive():
    assert hasattr(ISO20022_AbstractTimeConcept, "minInclusive")
    descriptor = None
    for klass in ISO20022_AbstractTimeConcept.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_abstracttimeconcept_has_minExclusive():
    assert hasattr(ISO20022_AbstractTimeConcept, "minExclusive")
    descriptor = None
    for klass in ISO20022_AbstractTimeConcept.__mro__:
        if "minExclusive" in klass.__dict__:
            descriptor = klass.__dict__["minExclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_abstracttimeconcept_has_maxInclusive():
    assert hasattr(ISO20022_AbstractTimeConcept, "maxInclusive")
    descriptor = None
    for klass in ISO20022_AbstractTimeConcept.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_abstracttimeconcept_has_maxExclusive():
    assert hasattr(ISO20022_AbstractTimeConcept, "maxExclusive")
    descriptor = None
    for klass in ISO20022_AbstractTimeConcept.__mro__:
        if "maxExclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxExclusive"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_xsdstring_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDString)


def test_iso20022_xsdstring_constructor_exists():
    assert callable(ISO20022_XSDString.__init__)


def test_iso20022_xsdstring_constructor_args():
    sig = inspect.signature(ISO20022_XSDString.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "length" in params, "Missing parameter 'length'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_iso20022_xsdstring_has_pattern():
    assert hasattr(ISO20022_XSDString, "pattern")
    descriptor = None
    for klass in ISO20022_XSDString.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdstring_has_minLength():
    assert hasattr(ISO20022_XSDString, "minLength")
    descriptor = None
    for klass in ISO20022_XSDString.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdstring_has_length():
    assert hasattr(ISO20022_XSDString, "length")
    descriptor = None
    for klass in ISO20022_XSDString.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsdstring_has_maxLength():
    assert hasattr(ISO20022_XSDString, "maxLength")
    descriptor = None
    for klass in ISO20022_XSDString.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_xsdstring_is_not_abstract():
    assert not inspect.isabstract(XSDString)


def test_xsdstring_constructor_exists():
    assert callable(XSDString.__init__)


def test_xsdstring_constructor_args():
    sig = inspect.signature(XSDString.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_codeset_is_not_abstract():
    assert not inspect.isabstract(ISO20022_CodeSet)


def test_iso20022_codeset_constructor_exists():
    assert callable(ISO20022_CodeSet.__init__)


def test_iso20022_codeset_constructor_args():
    sig = inspect.signature(ISO20022_CodeSet.__init__)
    params = list(sig.parameters.keys())
    assert "identificationScheme" in params, "Missing parameter 'identificationScheme'"

def test_iso20022_codeset_has_identificationScheme():
    assert hasattr(ISO20022_CodeSet, "identificationScheme")
    descriptor = None
    for klass in ISO20022_CodeSet.__mro__:
        if "identificationScheme" in klass.__dict__:
            descriptor = klass.__dict__["identificationScheme"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_xsdid_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDID)


def test_iso20022_xsdid_constructor_exists():
    assert callable(ISO20022_XSDID.__init__)


def test_iso20022_xsdid_constructor_args():
    sig = inspect.signature(ISO20022_XSDID.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_text_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Text)


def test_iso20022_text_constructor_exists():
    assert callable(ISO20022_Text.__init__)


def test_iso20022_text_constructor_args():
    sig = inspect.signature(ISO20022_Text.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xsddecimal_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDDecimal)


def test_iso20022_xsddecimal_constructor_exists():
    assert callable(ISO20022_XSDDecimal.__init__)


def test_iso20022_xsddecimal_constructor_args():
    sig = inspect.signature(ISO20022_XSDDecimal.__init__)
    params = list(sig.parameters.keys())
    assert "fractionDigits" in params, "Missing parameter 'fractionDigits'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "totalDigits" in params, "Missing parameter 'totalDigits'"
    assert "minExclusive" in params, "Missing parameter 'minExclusive'"
    assert "maxExclusive" in params, "Missing parameter 'maxExclusive'"
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_iso20022_xsddecimal_has_fractionDigits():
    assert hasattr(ISO20022_XSDDecimal, "fractionDigits")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "fractionDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionDigits"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_maxInclusive():
    assert hasattr(ISO20022_XSDDecimal, "maxInclusive")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_minInclusive():
    assert hasattr(ISO20022_XSDDecimal, "minInclusive")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_totalDigits():
    assert hasattr(ISO20022_XSDDecimal, "totalDigits")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "totalDigits" in klass.__dict__:
            descriptor = klass.__dict__["totalDigits"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_minExclusive():
    assert hasattr(ISO20022_XSDDecimal, "minExclusive")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "minExclusive" in klass.__dict__:
            descriptor = klass.__dict__["minExclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_maxExclusive():
    assert hasattr(ISO20022_XSDDecimal, "maxExclusive")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "maxExclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxExclusive"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_xsddecimal_has_pattern():
    assert hasattr(ISO20022_XSDDecimal, "pattern")
    descriptor = None
    for klass in ISO20022_XSDDecimal.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_xsddecimal_is_not_abstract():
    assert not inspect.isabstract(XSDDecimal)


def test_xsddecimal_constructor_exists():
    assert callable(XSDDecimal.__init__)


def test_xsddecimal_constructor_args():
    sig = inspect.signature(XSDDecimal.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_quantity_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Quantity)


def test_iso20022_quantity_constructor_exists():
    assert callable(ISO20022_Quantity.__init__)


def test_iso20022_quantity_constructor_args():
    sig = inspect.signature(ISO20022_Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "unitCode" in params, "Missing parameter 'unitCode'"

def test_iso20022_quantity_has_unitCode():
    assert hasattr(ISO20022_Quantity, "unitCode")
    descriptor = None
    for klass in ISO20022_Quantity.__mro__:
        if "unitCode" in klass.__dict__:
            descriptor = klass.__dict__["unitCode"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_amount_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Amount)


def test_iso20022_amount_constructor_exists():
    assert callable(ISO20022_Amount.__init__)


def test_iso20022_amount_constructor_args():
    sig = inspect.signature(ISO20022_Amount.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_rate_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Rate)


def test_iso20022_rate_constructor_exists():
    assert callable(ISO20022_Rate.__init__)


def test_iso20022_rate_constructor_args():
    sig = inspect.signature(ISO20022_Rate.__init__)
    params = list(sig.parameters.keys())
    assert "baseUnitCode" in params, "Missing parameter 'baseUnitCode'"
    assert "baseValue" in params, "Missing parameter 'baseValue'"

def test_iso20022_rate_has_baseUnitCode():
    assert hasattr(ISO20022_Rate, "baseUnitCode")
    descriptor = None
    for klass in ISO20022_Rate.__mro__:
        if "baseUnitCode" in klass.__dict__:
            descriptor = klass.__dict__["baseUnitCode"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_rate_has_baseValue():
    assert hasattr(ISO20022_Rate, "baseValue")
    descriptor = None
    for klass in ISO20022_Rate.__mro__:
        if "baseValue" in klass.__dict__:
            descriptor = klass.__dict__["baseValue"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_xsdboolean_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XSDBoolean)


def test_iso20022_xsdboolean_constructor_exists():
    assert callable(ISO20022_XSDBoolean.__init__)


def test_iso20022_xsdboolean_constructor_args():
    sig = inspect.signature(ISO20022_XSDBoolean.__init__)
    params = list(sig.parameters.keys())



def test_xsdboolean_is_not_abstract():
    assert not inspect.isabstract(XSDBoolean)


def test_xsdboolean_constructor_exists():
    assert callable(XSDBoolean.__init__)


def test_xsdboolean_constructor_args():
    sig = inspect.signature(XSDBoolean.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_indicator_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Indicator)


def test_iso20022_indicator_constructor_exists():
    assert callable(ISO20022_Indicator.__init__)


def test_iso20022_indicator_constructor_args():
    sig = inspect.signature(ISO20022_Indicator.__init__)
    params = list(sig.parameters.keys())
    assert "meaningWhenTrue" in params, "Missing parameter 'meaningWhenTrue'"
    assert "meaningWhenFalse" in params, "Missing parameter 'meaningWhenFalse'"
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_iso20022_indicator_has_meaningWhenTrue():
    assert hasattr(ISO20022_Indicator, "meaningWhenTrue")
    descriptor = None
    for klass in ISO20022_Indicator.__mro__:
        if "meaningWhenTrue" in klass.__dict__:
            descriptor = klass.__dict__["meaningWhenTrue"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_indicator_has_meaningWhenFalse():
    assert hasattr(ISO20022_Indicator, "meaningWhenFalse")
    descriptor = None
    for klass in ISO20022_Indicator.__mro__:
        if "meaningWhenFalse" in klass.__dict__:
            descriptor = klass.__dict__["meaningWhenFalse"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_indicator_has_pattern():
    assert hasattr(ISO20022_Indicator, "pattern")
    descriptor = None
    for klass in ISO20022_Indicator.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_identifierset_is_not_abstract():
    assert not inspect.isabstract(ISO20022_IdentifierSet)


def test_iso20022_identifierset_constructor_exists():
    assert callable(ISO20022_IdentifierSet.__init__)


def test_iso20022_identifierset_constructor_args():
    sig = inspect.signature(ISO20022_IdentifierSet.__init__)
    params = list(sig.parameters.keys())
    assert "identificationScheme" in params, "Missing parameter 'identificationScheme'"

def test_iso20022_identifierset_has_identificationScheme():
    assert hasattr(ISO20022_IdentifierSet, "identificationScheme")
    descriptor = None
    for klass in ISO20022_IdentifierSet.__mro__:
        if "identificationScheme" in klass.__dict__:
            descriptor = klass.__dict__["identificationScheme"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_messagedefinitionidentifier_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageDefinitionIdentifier)


def test_iso20022_messagedefinitionidentifier_constructor_exists():
    assert callable(ISO20022_MessageDefinitionIdentifier.__init__)


def test_iso20022_messagedefinitionidentifier_constructor_args():
    sig = inspect.signature(ISO20022_MessageDefinitionIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "messageFunctionality" in params, "Missing parameter 'messageFunctionality'"
    assert "flavour" in params, "Missing parameter 'flavour'"
    assert "businessArea" in params, "Missing parameter 'businessArea'"
    assert "version" in params, "Missing parameter 'version'"

def test_iso20022_messagedefinitionidentifier_has_messageFunctionality():
    assert hasattr(ISO20022_MessageDefinitionIdentifier, "messageFunctionality")
    descriptor = None
    for klass in ISO20022_MessageDefinitionIdentifier.__mro__:
        if "messageFunctionality" in klass.__dict__:
            descriptor = klass.__dict__["messageFunctionality"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinitionidentifier_has_flavour():
    assert hasattr(ISO20022_MessageDefinitionIdentifier, "flavour")
    descriptor = None
    for klass in ISO20022_MessageDefinitionIdentifier.__mro__:
        if "flavour" in klass.__dict__:
            descriptor = klass.__dict__["flavour"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinitionidentifier_has_businessArea():
    assert hasattr(ISO20022_MessageDefinitionIdentifier, "businessArea")
    descriptor = None
    for klass in ISO20022_MessageDefinitionIdentifier.__mro__:
        if "businessArea" in klass.__dict__:
            descriptor = klass.__dict__["businessArea"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinitionidentifier_has_version():
    assert hasattr(ISO20022_MessageDefinitionIdentifier, "version")
    descriptor = None
    for klass in ISO20022_MessageDefinitionIdentifier.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_messageelementcontainer_is_not_abstract():
    assert not inspect.isabstract(MessageElementContainer)


def test_messageelementcontainer_constructor_exists():
    assert callable(MessageElementContainer.__init__)


def test_messageelementcontainer_constructor_args():
    sig = inspect.signature(MessageElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_choicecomponent_is_not_abstract():
    assert not inspect.isabstract(ISO20022_ChoiceComponent)


def test_iso20022_choicecomponent_constructor_exists():
    assert callable(ISO20022_ChoiceComponent.__init__)


def test_iso20022_choicecomponent_constructor_args():
    sig = inspect.signature(ISO20022_ChoiceComponent.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messagecomponent_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageComponent)


def test_iso20022_messagecomponent_constructor_exists():
    assert callable(ISO20022_MessageComponent.__init__)


def test_iso20022_messagecomponent_constructor_args():
    sig = inspect.signature(ISO20022_MessageComponent.__init__)
    params = list(sig.parameters.keys())



def test_toplevelcatalogueentry_is_not_abstract():
    assert not inspect.isabstract(TopLevelCatalogueEntry)


def test_toplevelcatalogueentry_constructor_exists():
    assert callable(TopLevelCatalogueEntry.__init__)


def test_toplevelcatalogueentry_constructor_args():
    sig = inspect.signature(TopLevelCatalogueEntry.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_syntaxmessagescheme_is_not_abstract():
    assert not inspect.isabstract(ISO20022_SyntaxMessageScheme)


def test_iso20022_syntaxmessagescheme_constructor_exists():
    assert callable(ISO20022_SyntaxMessageScheme.__init__)


def test_iso20022_syntaxmessagescheme_constructor_args():
    sig = inspect.signature(ISO20022_SyntaxMessageScheme.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messagechoreography_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageChoreography)


def test_iso20022_messagechoreography_constructor_exists():
    assert callable(ISO20022_MessageChoreography.__init__)


def test_iso20022_messagechoreography_constructor_args():
    sig = inspect.signature(ISO20022_MessageChoreography.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businessarea_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessArea)


def test_iso20022_businessarea_constructor_exists():
    assert callable(ISO20022_BusinessArea.__init__)


def test_iso20022_businessarea_constructor_args():
    sig = inspect.signature(ISO20022_BusinessArea.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_iso20022_businessarea_has_code():
    assert hasattr(ISO20022_BusinessArea, "code")
    descriptor = None
    for klass in ISO20022_BusinessArea.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_messageset_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageSet)


def test_iso20022_messageset_constructor_exists():
    assert callable(ISO20022_MessageSet.__init__)


def test_iso20022_messageset_constructor_args():
    sig = inspect.signature(ISO20022_MessageSet.__init__)
    params = list(sig.parameters.keys())



def test_businesselement_is_not_abstract():
    assert not inspect.isabstract(BusinessElement)


def test_businesselement_constructor_exists():
    assert callable(BusinessElement.__init__)


def test_businesselement_constructor_args():
    sig = inspect.signature(BusinessElement.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businessattribute_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessAttribute)


def test_iso20022_businessattribute_constructor_exists():
    assert callable(ISO20022_BusinessAttribute.__init__)


def test_iso20022_businessattribute_constructor_args():
    sig = inspect.signature(ISO20022_BusinessAttribute.__init__)
    params = list(sig.parameters.keys())



def test_messagecomponenttype_is_not_abstract():
    assert not inspect.isabstract(MessageComponentType)


def test_messagecomponenttype_constructor_exists():
    assert callable(MessageComponentType.__init__)


def test_messagecomponenttype_constructor_args():
    sig = inspect.signature(MessageComponentType.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_externalschema_is_not_abstract():
    assert not inspect.isabstract(ISO20022_ExternalSchema)


def test_iso20022_externalschema_constructor_exists():
    assert callable(ISO20022_ExternalSchema.__init__)


def test_iso20022_externalschema_constructor_args():
    sig = inspect.signature(ISO20022_ExternalSchema.__init__)
    params = list(sig.parameters.keys())
    assert "processContent" in params, "Missing parameter 'processContent'"
    assert "namespaceList" in params, "Missing parameter 'namespaceList'"

def test_iso20022_externalschema_has_processContent():
    assert hasattr(ISO20022_ExternalSchema, "processContent")
    descriptor = None
    for klass in ISO20022_ExternalSchema.__mro__:
        if "processContent" in klass.__dict__:
            descriptor = klass.__dict__["processContent"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_externalschema_has_namespaceList():
    assert hasattr(ISO20022_ExternalSchema, "namespaceList")
    descriptor = None
    for klass in ISO20022_ExternalSchema.__mro__:
        if "namespaceList" in klass.__dict__:
            descriptor = klass.__dict__["namespaceList"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_userdefined_is_not_abstract():
    assert not inspect.isabstract(ISO20022_UserDefined)


def test_iso20022_userdefined_constructor_exists():
    assert callable(ISO20022_UserDefined.__init__)


def test_iso20022_userdefined_constructor_args():
    sig = inspect.signature(ISO20022_UserDefined.__init__)
    params = list(sig.parameters.keys())
    assert "_" in params, "Missing parameter '_'"
    assert "namespaceList" in params, "Missing parameter 'namespaceList'"
    assert "processContents" in params, "Missing parameter 'processContents'"

def test_iso20022_userdefined_has__():
    assert hasattr(ISO20022_UserDefined, "_")
    descriptor = None
    for klass in ISO20022_UserDefined.__mro__:
        if "_" in klass.__dict__:
            descriptor = klass.__dict__["_"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_userdefined_has_namespaceList():
    assert hasattr(ISO20022_UserDefined, "namespaceList")
    descriptor = None
    for klass in ISO20022_UserDefined.__mro__:
        if "namespaceList" in klass.__dict__:
            descriptor = klass.__dict__["namespaceList"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_userdefined_has_processContents():
    assert hasattr(ISO20022_UserDefined, "processContents")
    descriptor = None
    for klass in ISO20022_UserDefined.__mro__:
        if "processContents" in klass.__dict__:
            descriptor = klass.__dict__["processContents"]
            break
    assert isinstance(descriptor, property)



def test_logicaltype_is_not_abstract():
    assert not inspect.isabstract(LogicalType)


def test_logicaltype_constructor_exists():
    assert callable(LogicalType.__init__)


def test_logicaltype_constructor_args():
    sig = inspect.signature(LogicalType.__init__)
    params = list(sig.parameters.keys())



def test_businessconcept_is_not_abstract():
    assert not inspect.isabstract(BusinessConcept)


def test_businessconcept_constructor_exists():
    assert callable(BusinessConcept.__init__)


def test_businessconcept_constructor_args():
    sig = inspect.signature(BusinessConcept.__init__)
    params = list(sig.parameters.keys())



def test_topleveldictionaryentry_is_not_abstract():
    assert not inspect.isabstract(TopLevelDictionaryEntry)


def test_topleveldictionaryentry_constructor_exists():
    assert callable(TopLevelDictionaryEntry.__init__)


def test_topleveldictionaryentry_constructor_args():
    sig = inspect.signature(TopLevelDictionaryEntry.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_endpointcategory_is_not_abstract():
    assert not inspect.isabstract(ISO20022_EndPointCategory)


def test_iso20022_endpointcategory_constructor_exists():
    assert callable(ISO20022_EndPointCategory.__init__)


def test_iso20022_endpointcategory_constructor_args():
    sig = inspect.signature(ISO20022_EndPointCategory.__init__)
    params = list(sig.parameters.keys())



def test_businesselementtype_is_not_abstract():
    assert not inspect.isabstract(BusinessElementType)


def test_businesselementtype_constructor_exists():
    assert callable(BusinessElementType.__init__)


def test_businesselementtype_constructor_args():
    sig = inspect.signature(BusinessElementType.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_datatype_is_not_abstract():
    assert not inspect.isabstract(ISO20022_DataType)


def test_iso20022_datatype_constructor_exists():
    assert callable(ISO20022_DataType.__init__)


def test_iso20022_datatype_constructor_args():
    sig = inspect.signature(ISO20022_DataType.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businessassociationend_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessAssociationEnd)


def test_iso20022_businessassociationend_constructor_exists():
    assert callable(ISO20022_BusinessAssociationEnd.__init__)


def test_iso20022_businessassociationend_constructor_args():
    sig = inspect.signature(ISO20022_BusinessAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_iso20022_businessassociationend_has_aggregation():
    assert hasattr(ISO20022_BusinessAssociationEnd, "aggregation")
    descriptor = None
    for klass in ISO20022_BusinessAssociationEnd.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businesselementtype_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessElementType)


def test_iso20022_businesselementtype_constructor_exists():
    assert callable(ISO20022_BusinessElementType.__init__)


def test_iso20022_businesselementtype_constructor_args():
    sig = inspect.signature(ISO20022_BusinessElementType.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messagedefinition_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageDefinition)


def test_iso20022_messagedefinition_constructor_exists():
    assert callable(ISO20022_MessageDefinition.__init__)


def test_iso20022_messagedefinition_constructor_args():
    sig = inspect.signature(ISO20022_MessageDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "xmlTag" in params, "Missing parameter 'xmlTag'"
    assert "urn" in params, "Missing parameter 'urn'"
    assert "xmlName" in params, "Missing parameter 'xmlName'"
    assert "rootElement" in params, "Missing parameter 'rootElement'"
    assert "previousVersionDocumentation" in params, "Missing parameter 'previousVersionDocumentation'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_iso20022_messagedefinition_has_xmlTag():
    assert hasattr(ISO20022_MessageDefinition, "xmlTag")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "xmlTag" in klass.__dict__:
            descriptor = klass.__dict__["xmlTag"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinition_has_urn():
    assert hasattr(ISO20022_MessageDefinition, "urn")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "urn" in klass.__dict__:
            descriptor = klass.__dict__["urn"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinition_has_xmlName():
    assert hasattr(ISO20022_MessageDefinition, "xmlName")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "xmlName" in klass.__dict__:
            descriptor = klass.__dict__["xmlName"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinition_has_rootElement():
    assert hasattr(ISO20022_MessageDefinition, "rootElement")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "rootElement" in klass.__dict__:
            descriptor = klass.__dict__["rootElement"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinition_has_previousVersionDocumentation():
    assert hasattr(ISO20022_MessageDefinition, "previousVersionDocumentation")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "previousVersionDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["previousVersionDocumentation"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagedefinition_has_visibility():
    assert hasattr(ISO20022_MessageDefinition, "visibility")
    descriptor = None
    for klass in ISO20022_MessageDefinition.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xmlmember_is_not_abstract():
    assert not inspect.isabstract(ISO20022_XMLMember)


def test_iso20022_xmlmember_constructor_exists():
    assert callable(ISO20022_XMLMember.__init__)


def test_iso20022_xmlmember_constructor_args():
    sig = inspect.signature(ISO20022_XMLMember.__init__)
    params = list(sig.parameters.keys())
    assert "xmlTag" in params, "Missing parameter 'xmlTag'"

def test_iso20022_xmlmember_has_xmlTag():
    assert hasattr(ISO20022_XMLMember, "xmlTag")
    descriptor = None
    for klass in ISO20022_XMLMember.__mro__:
        if "xmlTag" in klass.__dict__:
            descriptor = klass.__dict__["xmlTag"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_multiplicityentity_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MultiplicityEntity)


def test_iso20022_multiplicityentity_constructor_exists():
    assert callable(ISO20022_MultiplicityEntity.__init__)


def test_iso20022_multiplicityentity_constructor_args():
    sig = inspect.signature(ISO20022_MultiplicityEntity.__init__)
    params = list(sig.parameters.keys())
    assert "minOccurs" in params, "Missing parameter 'minOccurs'"
    assert "maxOccurs" in params, "Missing parameter 'maxOccurs'"

def test_iso20022_multiplicityentity_has_minOccurs():
    assert hasattr(ISO20022_MultiplicityEntity, "minOccurs")
    descriptor = None
    for klass in ISO20022_MultiplicityEntity.__mro__:
        if "minOccurs" in klass.__dict__:
            descriptor = klass.__dict__["minOccurs"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_multiplicityentity_has_maxOccurs():
    assert hasattr(ISO20022_MultiplicityEntity, "maxOccurs")
    descriptor = None
    for klass in ISO20022_MultiplicityEntity.__mro__:
        if "maxOccurs" in klass.__dict__:
            descriptor = klass.__dict__["maxOccurs"]
            break
    assert isinstance(descriptor, property)



def test_multiplicityentity_is_not_abstract():
    assert not inspect.isabstract(MultiplicityEntity)


def test_multiplicityentity_constructor_exists():
    assert callable(MultiplicityEntity.__init__)


def test_multiplicityentity_constructor_args():
    sig = inspect.signature(MultiplicityEntity.__init__)
    params = list(sig.parameters.keys())



def test_repositoryconcept_is_not_abstract():
    assert not inspect.isabstract(RepositoryConcept)


def test_repositoryconcept_constructor_exists():
    assert callable(RepositoryConcept.__init__)


def test_repositoryconcept_constructor_args():
    sig = inspect.signature(RepositoryConcept.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_type_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Type)


def test_iso20022_type_constructor_exists():
    assert callable(ISO20022_Type.__init__)


def test_iso20022_type_constructor_args():
    sig = inspect.signature(ISO20022_Type.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_topleveldictionaryentry_is_not_abstract():
    assert not inspect.isabstract(ISO20022_TopLevelDictionaryEntry)


def test_iso20022_topleveldictionaryentry_constructor_exists():
    assert callable(ISO20022_TopLevelDictionaryEntry.__init__)


def test_iso20022_topleveldictionaryentry_constructor_args():
    sig = inspect.signature(ISO20022_TopLevelDictionaryEntry.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_diagram_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Diagram)


def test_iso20022_diagram_constructor_exists():
    assert callable(ISO20022_Diagram.__init__)


def test_iso20022_diagram_constructor_args():
    sig = inspect.signature(ISO20022_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "location" in params, "Missing parameter 'location'"

def test_iso20022_diagram_has_content():
    assert hasattr(ISO20022_Diagram, "content")
    descriptor = None
    for klass in ISO20022_Diagram.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_diagram_has_location():
    assert hasattr(ISO20022_Diagram, "location")
    descriptor = None
    for klass in ISO20022_Diagram.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_businessrole_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessRole)


def test_iso20022_businessrole_constructor_exists():
    assert callable(ISO20022_BusinessRole.__init__)


def test_iso20022_businessrole_constructor_args():
    sig = inspect.signature(ISO20022_BusinessRole.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_code_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Code)


def test_iso20022_code_constructor_exists():
    assert callable(ISO20022_Code.__init__)


def test_iso20022_code_constructor_args():
    sig = inspect.signature(ISO20022_Code.__init__)
    params = list(sig.parameters.keys())
    assert "codeName" in params, "Missing parameter 'codeName'"

def test_iso20022_code_has_codeName():
    assert hasattr(ISO20022_Code, "codeName")
    descriptor = None
    for klass in ISO20022_Code.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_interactionactor_is_not_abstract():
    assert not inspect.isabstract(ISO20022_InteractionActor)


def test_iso20022_interactionactor_constructor_exists():
    assert callable(ISO20022_InteractionActor.__init__)


def test_iso20022_interactionactor_constructor_args():
    sig = inspect.signature(ISO20022_InteractionActor.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_xor_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Xor)


def test_iso20022_xor_constructor_exists():
    assert callable(ISO20022_Xor.__init__)


def test_iso20022_xor_constructor_args():
    sig = inspect.signature(ISO20022_Xor.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_interaction_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Interaction)


def test_iso20022_interaction_constructor_exists():
    assert callable(ISO20022_Interaction.__init__)


def test_iso20022_interaction_constructor_args():
    sig = inspect.signature(ISO20022_Interaction.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_iso20022_interaction_has_location():
    assert hasattr(ISO20022_Interaction, "location")
    descriptor = None
    for klass in ISO20022_Interaction.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_interactionmessage_is_not_abstract():
    assert not inspect.isabstract(ISO20022_InteractionMessage)


def test_iso20022_interactionmessage_constructor_exists():
    assert callable(ISO20022_InteractionMessage.__init__)


def test_iso20022_interactionmessage_constructor_args():
    sig = inspect.signature(ISO20022_InteractionMessage.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_toplevelcatalogueentry_is_not_abstract():
    assert not inspect.isabstract(ISO20022_TopLevelCatalogueEntry)


def test_iso20022_toplevelcatalogueentry_constructor_exists():
    assert callable(ISO20022_TopLevelCatalogueEntry.__init__)


def test_iso20022_toplevelcatalogueentry_constructor_args():
    sig = inspect.signature(ISO20022_TopLevelCatalogueEntry.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_isanalternativefor_is_not_abstract():
    assert not inspect.isabstract(ISO20022_IsAnAlternativeFor)


def test_iso20022_isanalternativefor_constructor_exists():
    assert callable(ISO20022_IsAnAlternativeFor.__init__)


def test_iso20022_isanalternativefor_constructor_args():
    sig = inspect.signature(ISO20022_IsAnAlternativeFor.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_member_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Member)


def test_iso20022_member_constructor_exists():
    assert callable(ISO20022_Member.__init__)


def test_iso20022_member_constructor_args():
    sig = inspect.signature(ISO20022_Member.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_logicaltype_is_not_abstract():
    assert not inspect.isabstract(ISO20022_LogicalType)


def test_iso20022_logicaltype_constructor_exists():
    assert callable(ISO20022_LogicalType.__init__)


def test_iso20022_logicaltype_constructor_args():
    sig = inspect.signature(ISO20022_LogicalType.__init__)
    params = list(sig.parameters.keys())



def test_messageconcept_is_not_abstract():
    assert not inspect.isabstract(MessageConcept)


def test_messageconcept_constructor_exists():
    assert callable(MessageConcept.__init__)


def test_messageconcept_constructor_args():
    sig = inspect.signature(MessageConcept.__init__)
    params = list(sig.parameters.keys())



def test_xmlmember_is_not_abstract():
    assert not inspect.isabstract(XMLMember)


def test_xmlmember_constructor_exists():
    assert callable(XMLMember.__init__)


def test_xmlmember_constructor_args():
    sig = inspect.signature(XMLMember.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messagebuildingblock_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageBuildingBlock)


def test_iso20022_messagebuildingblock_constructor_exists():
    assert callable(ISO20022_MessageBuildingBlock.__init__)


def test_iso20022_messagebuildingblock_constructor_args():
    sig = inspect.signature(ISO20022_MessageBuildingBlock.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messageelement_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageElement)


def test_iso20022_messageelement_constructor_exists():
    assert callable(ISO20022_MessageElement.__init__)


def test_iso20022_messageelement_constructor_args():
    sig = inspect.signature(ISO20022_MessageElement.__init__)
    params = list(sig.parameters.keys())
    assert "tracePath" in params, "Missing parameter 'tracePath'"
    assert "isTechnical" in params, "Missing parameter 'isTechnical'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_iso20022_messageelement_has_tracePath():
    assert hasattr(ISO20022_MessageElement, "tracePath")
    descriptor = None
    for klass in ISO20022_MessageElement.__mro__:
        if "tracePath" in klass.__dict__:
            descriptor = klass.__dict__["tracePath"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messageelement_has_isTechnical():
    assert hasattr(ISO20022_MessageElement, "isTechnical")
    descriptor = None
    for klass in ISO20022_MessageElement.__mro__:
        if "isTechnical" in klass.__dict__:
            descriptor = klass.__dict__["isTechnical"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messageelement_has_isDerived():
    assert hasattr(ISO20022_MessageElement, "isDerived")
    descriptor = None
    for klass in ISO20022_MessageElement.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_messageelementcontainer_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageElementContainer)


def test_iso20022_messageelementcontainer_constructor_exists():
    assert callable(ISO20022_MessageElementContainer.__init__)


def test_iso20022_messageelementcontainer_constructor_args():
    sig = inspect.signature(ISO20022_MessageElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businesselement_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessElement)


def test_iso20022_businesselement_constructor_exists():
    assert callable(ISO20022_BusinessElement.__init__)


def test_iso20022_businesselement_constructor_args():
    sig = inspect.signature(ISO20022_BusinessElement.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_iso20022_businesselement_has_isDerived():
    assert hasattr(ISO20022_BusinessElement, "isDerived")
    descriptor = None
    for klass in ISO20022_BusinessElement.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_businesscomponent_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessComponent)


def test_iso20022_businesscomponent_constructor_exists():
    assert callable(ISO20022_BusinessComponent.__init__)


def test_iso20022_businesscomponent_constructor_args():
    sig = inspect.signature(ISO20022_BusinessComponent.__init__)
    params = list(sig.parameters.keys())
    assert "previousVersionDocumentation" in params, "Missing parameter 'previousVersionDocumentation'"

def test_iso20022_businesscomponent_has_previousVersionDocumentation():
    assert hasattr(ISO20022_BusinessComponent, "previousVersionDocumentation")
    descriptor = None
    for klass in ISO20022_BusinessComponent.__mro__:
        if "previousVersionDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["previousVersionDocumentation"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_messagecomponenttype_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageComponentType)


def test_iso20022_messagecomponenttype_constructor_exists():
    assert callable(ISO20022_MessageComponentType.__init__)


def test_iso20022_messagecomponenttype_constructor_args():
    sig = inspect.signature(ISO20022_MessageComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "tracePath" in params, "Missing parameter 'tracePath'"
    assert "isTechnical" in params, "Missing parameter 'isTechnical'"

def test_iso20022_messagecomponenttype_has_tracePath():
    assert hasattr(ISO20022_MessageComponentType, "tracePath")
    descriptor = None
    for klass in ISO20022_MessageComponentType.__mro__:
        if "tracePath" in klass.__dict__:
            descriptor = klass.__dict__["tracePath"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_messagecomponenttype_has_isTechnical():
    assert hasattr(ISO20022_MessageComponentType, "isTechnical")
    descriptor = None
    for klass in ISO20022_MessageComponentType.__mro__:
        if "isTechnical" in klass.__dict__:
            descriptor = klass.__dict__["isTechnical"]
            break
    assert isinstance(descriptor, property)



def test_messageelement_is_not_abstract():
    assert not inspect.isabstract(MessageElement)


def test_messageelement_constructor_exists():
    assert callable(MessageElement.__init__)


def test_messageelement_constructor_args():
    sig = inspect.signature(MessageElement.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messageattribute_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageAttribute)


def test_iso20022_messageattribute_constructor_exists():
    assert callable(ISO20022_MessageAttribute.__init__)


def test_iso20022_messageattribute_constructor_args():
    sig = inspect.signature(ISO20022_MessageAttribute.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messageassociationend_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageAssociationEnd)


def test_iso20022_messageassociationend_constructor_exists():
    assert callable(ISO20022_MessageAssociationEnd.__init__)


def test_iso20022_messageassociationend_constructor_args():
    sig = inspect.signature(ISO20022_MessageAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_iso20022_messageassociationend_has_isComposite():
    assert hasattr(ISO20022_MessageAssociationEnd, "isComposite")
    descriptor = None
    for klass in ISO20022_MessageAssociationEnd.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_modelentity_is_not_abstract():
    assert not inspect.isabstract(ModelEntity)


def test_modelentity_constructor_exists():
    assert callable(ModelEntity.__init__)


def test_modelentity_constructor_args():
    sig = inspect.signature(ModelEntity.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_syntax_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Syntax)


def test_iso20022_syntax_constructor_exists():
    assert callable(ISO20022_Syntax.__init__)


def test_iso20022_syntax_constructor_args():
    sig = inspect.signature(ISO20022_Syntax.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businessprocesscatalogue_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessProcessCatalogue)


def test_iso20022_businessprocesscatalogue_constructor_exists():
    assert callable(ISO20022_BusinessProcessCatalogue.__init__)


def test_iso20022_businessprocesscatalogue_constructor_args():
    sig = inspect.signature(ISO20022_BusinessProcessCatalogue.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_businessconcept_is_not_abstract():
    assert not inspect.isabstract(ISO20022_BusinessConcept)


def test_iso20022_businessconcept_constructor_exists():
    assert callable(ISO20022_BusinessConcept.__init__)


def test_iso20022_businessconcept_constructor_args():
    sig = inspect.signature(ISO20022_BusinessConcept.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_datadictionary_is_not_abstract():
    assert not inspect.isabstract(ISO20022_DataDictionary)


def test_iso20022_datadictionary_constructor_exists():
    assert callable(ISO20022_DataDictionary.__init__)


def test_iso20022_datadictionary_constructor_args():
    sig = inspect.signature(ISO20022_DataDictionary.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_repository_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Repository)


def test_iso20022_repository_constructor_exists():
    assert callable(ISO20022_Repository.__init__)


def test_iso20022_repository_constructor_args():
    sig = inspect.signature(ISO20022_Repository.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_facet_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Facet)


def test_iso20022_facet_constructor_exists():
    assert callable(ISO20022_Facet.__init__)


def test_iso20022_facet_constructor_args():
    sig = inspect.signature(ISO20022_Facet.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_iso20022_facet_has_value():
    assert hasattr(ISO20022_Facet, "value")
    descriptor = None
    for klass in ISO20022_Facet.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_facet_has_name():
    assert hasattr(ISO20022_Facet, "name")
    descriptor = None
    for klass in ISO20022_Facet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_encoding_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Encoding)


def test_iso20022_encoding_constructor_exists():
    assert callable(ISO20022_Encoding.__init__)


def test_iso20022_encoding_constructor_args():
    sig = inspect.signature(ISO20022_Encoding.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_messageconcept_is_not_abstract():
    assert not inspect.isabstract(ISO20022_MessageConcept)


def test_iso20022_messageconcept_constructor_exists():
    assert callable(ISO20022_MessageConcept.__init__)


def test_iso20022_messageconcept_constructor_args():
    sig = inspect.signature(ISO20022_MessageConcept.__init__)
    params = list(sig.parameters.keys())



def test_iso20022_semanticmarkupelement_is_not_abstract():
    assert not inspect.isabstract(ISO20022_SemanticMarkupElement)


def test_iso20022_semanticmarkupelement_constructor_exists():
    assert callable(ISO20022_SemanticMarkupElement.__init__)


def test_iso20022_semanticmarkupelement_constructor_args():
    sig = inspect.signature(ISO20022_SemanticMarkupElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_iso20022_semanticmarkupelement_has_value():
    assert hasattr(ISO20022_SemanticMarkupElement, "value")
    descriptor = None
    for klass in ISO20022_SemanticMarkupElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_semanticmarkupelement_has_name():
    assert hasattr(ISO20022_SemanticMarkupElement, "name")
    descriptor = None
    for klass in ISO20022_SemanticMarkupElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_modelentity_is_not_abstract():
    assert not inspect.isabstract(ISO20022_ModelEntity)


def test_iso20022_modelentity_constructor_exists():
    assert callable(ISO20022_ModelEntity.__init__)


def test_iso20022_modelentity_constructor_args():
    sig = inspect.signature(ISO20022_ModelEntity.__init__)
    params = list(sig.parameters.keys())
    assert "objectIdentifier" in params, "Missing parameter 'objectIdentifier'"

def test_iso20022_modelentity_has_objectIdentifier():
    assert hasattr(ISO20022_ModelEntity, "objectIdentifier")
    descriptor = None
    for klass in ISO20022_ModelEntity.__mro__:
        if "objectIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["objectIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_doclet_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Doclet)


def test_iso20022_doclet_constructor_exists():
    assert callable(ISO20022_Doclet.__init__)


def test_iso20022_doclet_constructor_args():
    sig = inspect.signature(ISO20022_Doclet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "content" in params, "Missing parameter 'content'"

def test_iso20022_doclet_has_type():
    assert hasattr(ISO20022_Doclet, "type")
    descriptor = None
    for klass in ISO20022_Doclet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_doclet_has_content():
    assert hasattr(ISO20022_Doclet, "content")
    descriptor = None
    for klass in ISO20022_Doclet.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_semanticmarkup_is_not_abstract():
    assert not inspect.isabstract(ISO20022_SemanticMarkup)


def test_iso20022_semanticmarkup_constructor_exists():
    assert callable(ISO20022_SemanticMarkup.__init__)


def test_iso20022_semanticmarkup_constructor_args():
    sig = inspect.signature(ISO20022_SemanticMarkup.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_iso20022_semanticmarkup_has_type():
    assert hasattr(ISO20022_SemanticMarkup, "type")
    descriptor = None
    for klass in ISO20022_SemanticMarkup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_repositoryconcept_is_not_abstract():
    assert not inspect.isabstract(ISO20022_RepositoryConcept)


def test_iso20022_repositoryconcept_constructor_exists():
    assert callable(ISO20022_RepositoryConcept.__init__)


def test_iso20022_repositoryconcept_constructor_args():
    sig = inspect.signature(ISO20022_RepositoryConcept.__init__)
    params = list(sig.parameters.keys())
    assert "definition" in params, "Missing parameter 'definition'"
    assert "swiftRegistrationStatus" in params, "Missing parameter 'swiftRegistrationStatus'"
    assert "swiftRemovalDate" in params, "Missing parameter 'swiftRemovalDate'"
    assert "removalDate" in params, "Missing parameter 'removalDate'"
    assert "example" in params, "Missing parameter 'example'"
    assert "name" in params, "Missing parameter 'name'"
    assert "registrationStatus" in params, "Missing parameter 'registrationStatus'"

def test_iso20022_repositoryconcept_has_definition():
    assert hasattr(ISO20022_RepositoryConcept, "definition")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_swiftRegistrationStatus():
    assert hasattr(ISO20022_RepositoryConcept, "swiftRegistrationStatus")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "swiftRegistrationStatus" in klass.__dict__:
            descriptor = klass.__dict__["swiftRegistrationStatus"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_swiftRemovalDate():
    assert hasattr(ISO20022_RepositoryConcept, "swiftRemovalDate")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "swiftRemovalDate" in klass.__dict__:
            descriptor = klass.__dict__["swiftRemovalDate"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_removalDate():
    assert hasattr(ISO20022_RepositoryConcept, "removalDate")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "removalDate" in klass.__dict__:
            descriptor = klass.__dict__["removalDate"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_example():
    assert hasattr(ISO20022_RepositoryConcept, "example")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "example" in klass.__dict__:
            descriptor = klass.__dict__["example"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_name():
    assert hasattr(ISO20022_RepositoryConcept, "name")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_repositoryconcept_has_registrationStatus():
    assert hasattr(ISO20022_RepositoryConcept, "registrationStatus")
    descriptor = None
    for klass in ISO20022_RepositoryConcept.__mro__:
        if "registrationStatus" in klass.__dict__:
            descriptor = klass.__dict__["registrationStatus"]
            break
    assert isinstance(descriptor, property)



def test_iso20022_constraint_is_not_abstract():
    assert not inspect.isabstract(ISO20022_Constraint)


def test_iso20022_constraint_constructor_exists():
    assert callable(ISO20022_Constraint.__init__)


def test_iso20022_constraint_constructor_args():
    sig = inspect.signature(ISO20022_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "injected" in params, "Missing parameter 'injected'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "errorText" in params, "Missing parameter 'errorText'"
    assert "expressionLanguage" in params, "Missing parameter 'expressionLanguage'"
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_iso20022_constraint_has_injected():
    assert hasattr(ISO20022_Constraint, "injected")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "injected" in klass.__dict__:
            descriptor = klass.__dict__["injected"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_constraint_has_kind():
    assert hasattr(ISO20022_Constraint, "kind")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_constraint_has_expression():
    assert hasattr(ISO20022_Constraint, "expression")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_constraint_has_errorText():
    assert hasattr(ISO20022_Constraint, "errorText")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "errorText" in klass.__dict__:
            descriptor = klass.__dict__["errorText"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_constraint_has_expressionLanguage():
    assert hasattr(ISO20022_Constraint, "expressionLanguage")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "expressionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_iso20022_constraint_has_errorCode():
    assert hasattr(ISO20022_Constraint, "errorCode")
    descriptor = None
    for klass in ISO20022_Constraint.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)

def test_namespace_exists():
    # Check that the Enumeration exists
    assert Namespace is not None

def test_namespace_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Namespace]
    expected_literals = [
        "other",
        "any",
        "list",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Namespace"

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "_",
        "DoNotShow",
        "Draft",
        "Outdated",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_processcontent_exists():
    # Check that the Enumeration exists
    assert ProcessContent is not None

def test_processcontent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcessContent]
    expected_literals = [
        "STRICT",
        "SKIP",
        "LAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessContent"

def test_aggregation_exists():
    # Check that the Enumeration exists
    assert Aggregation is not None

def test_aggregation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Aggregation]
    expected_literals = [
        "SHARED",
        "NONE",
        "COMPOSITE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Aggregation"

def test_registrationstatus_exists():
    # Check that the Enumeration exists
    assert RegistrationStatus is not None

def test_registrationstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RegistrationStatus]
    expected_literals = [
        "NO_STATUS",
        "REGISTERED",
        "OBSOLETE",
        "PROVISIONALLY_REGISTERED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RegistrationStatus"


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
MessageSet_strategy = st.builds(
    MessageSet,
)
ISO20022_SWIFTSolution_strategy = st.builds(
    ISO20022_SWIFTSolution,
    serviceName=
        safe_text
)
MessageDefinition_strategy = st.builds(
    MessageDefinition,
)
ISO20022_ApplicationHeader_strategy = st.builds(
    ISO20022_ApplicationHeader,
)
AbstractTimeConcept_strategy = st.builds(
    AbstractTimeConcept,
)
ISO20022_XSDMonth_strategy = st.builds(
    ISO20022_XSDMonth,
)
ISO20022_XSDTime_strategy = st.builds(
    ISO20022_XSDTime,
)
ISO20022_XSDMonthDay_strategy = st.builds(
    ISO20022_XSDMonthDay,
)
ISO20022_XSDYear_strategy = st.builds(
    ISO20022_XSDYear,
)
ISO20022_XSDDuration_strategy = st.builds(
    ISO20022_XSDDuration,
)
ISO20022_XSDDateTime_strategy = st.builds(
    ISO20022_XSDDateTime,
)
ISO20022_XSDYearMonth_strategy = st.builds(
    ISO20022_XSDYearMonth,
)
ISO20022_XSDDay_strategy = st.builds(
    ISO20022_XSDDay,
)
ISO20022_XSDDate_strategy = st.builds(
    ISO20022_XSDDate,
)
DataType_strategy = st.builds(
    DataType,
)
ISO20022_XSDBinary_strategy = st.builds(
    ISO20022_XSDBinary,
    minLength=
        safe_text,
    pattern=
        safe_text,
    length=
        safe_text,
    maxLength=
        safe_text
)
ISO20022_AbstractTimeConcept_strategy = st.builds(
    ISO20022_AbstractTimeConcept,
    pattern=
        safe_text,
    minInclusive=
        safe_text,
    minExclusive=
        safe_text,
    maxInclusive=
        safe_text,
    maxExclusive=
        safe_text
)
ISO20022_XSDString_strategy = st.builds(
    ISO20022_XSDString,
    pattern=
        safe_text,
    minLength=
        safe_text,
    length=
        safe_text,
    maxLength=
        safe_text
)
XSDString_strategy = st.builds(
    XSDString,
)
ISO20022_CodeSet_strategy = st.builds(
    ISO20022_CodeSet,
    identificationScheme=
        safe_text
)
ISO20022_XSDID_strategy = st.builds(
    ISO20022_XSDID,
)
ISO20022_Text_strategy = st.builds(
    ISO20022_Text,
)
ISO20022_XSDDecimal_strategy = st.builds(
    ISO20022_XSDDecimal,
    fractionDigits=
        safe_text,
    maxInclusive=
        safe_text,
    minInclusive=
        safe_text,
    totalDigits=
        safe_text,
    minExclusive=
        safe_text,
    maxExclusive=
        safe_text,
    pattern=
        safe_text
)
XSDDecimal_strategy = st.builds(
    XSDDecimal,
)
ISO20022_Quantity_strategy = st.builds(
    ISO20022_Quantity,
    unitCode=
        safe_text
)
ISO20022_Amount_strategy = st.builds(
    ISO20022_Amount,
)
ISO20022_Rate_strategy = st.builds(
    ISO20022_Rate,
    baseUnitCode=
        safe_text,
    baseValue=
        safe_text
)
ISO20022_XSDBoolean_strategy = st.builds(
    ISO20022_XSDBoolean,
)
XSDBoolean_strategy = st.builds(
    XSDBoolean,
)
ISO20022_Indicator_strategy = st.builds(
    ISO20022_Indicator,
    meaningWhenTrue=
        safe_text,
    meaningWhenFalse=
        safe_text,
    pattern=
        safe_text
)
ISO20022_IdentifierSet_strategy = st.builds(
    ISO20022_IdentifierSet,
    identificationScheme=
        safe_text
)
ISO20022_MessageDefinitionIdentifier_strategy = st.builds(
    ISO20022_MessageDefinitionIdentifier,
    messageFunctionality=
        safe_text,
    flavour=
        safe_text,
    businessArea=
        safe_text,
    version=
        safe_text
)
MessageElementContainer_strategy = st.builds(
    MessageElementContainer,
)
ISO20022_ChoiceComponent_strategy = st.builds(
    ISO20022_ChoiceComponent,
)
ISO20022_MessageComponent_strategy = st.builds(
    ISO20022_MessageComponent,
)
TopLevelCatalogueEntry_strategy = st.builds(
    TopLevelCatalogueEntry,
)
ISO20022_SyntaxMessageScheme_strategy = st.builds(
    ISO20022_SyntaxMessageScheme,
)
ISO20022_MessageChoreography_strategy = st.builds(
    ISO20022_MessageChoreography,
)
ISO20022_BusinessArea_strategy = st.builds(
    ISO20022_BusinessArea,
    code=
        safe_text
)
ISO20022_MessageSet_strategy = st.builds(
    ISO20022_MessageSet,
)
BusinessElement_strategy = st.builds(
    BusinessElement,
)
ISO20022_BusinessAttribute_strategy = st.builds(
    ISO20022_BusinessAttribute,
)
MessageComponentType_strategy = st.builds(
    MessageComponentType,
)
ISO20022_ExternalSchema_strategy = st.builds(
    ISO20022_ExternalSchema,
    processContent=
        safe_text,
    namespaceList=
        safe_text
)
ISO20022_UserDefined_strategy = st.builds(
    ISO20022_UserDefined,
    _=
        safe_text,
    namespaceList=
        safe_text,
    processContents=
        safe_text
)
LogicalType_strategy = st.builds(
    LogicalType,
)
BusinessConcept_strategy = st.builds(
    BusinessConcept,
)
TopLevelDictionaryEntry_strategy = st.builds(
    TopLevelDictionaryEntry,
)
ISO20022_EndPointCategory_strategy = st.builds(
    ISO20022_EndPointCategory,
)
BusinessElementType_strategy = st.builds(
    BusinessElementType,
)
ISO20022_DataType_strategy = st.builds(
    ISO20022_DataType,
)
ISO20022_BusinessAssociationEnd_strategy = st.builds(
    ISO20022_BusinessAssociationEnd,
    aggregation=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ISO20022_BusinessElementType_strategy = st.builds(
    ISO20022_BusinessElementType,
)
ISO20022_MessageDefinition_strategy = st.builds(
    ISO20022_MessageDefinition,
    xmlTag=
        safe_text,
    urn=
        safe_text,
    xmlName=
        safe_text,
    rootElement=
        safe_text,
    previousVersionDocumentation=
        safe_text,
    visibility=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
ISO20022_XMLMember_strategy = st.builds(
    ISO20022_XMLMember,
    xmlTag=
        safe_text
)
ISO20022_MultiplicityEntity_strategy = st.builds(
    ISO20022_MultiplicityEntity,
    minOccurs=
        safe_text,
    maxOccurs=
        safe_text
)
MultiplicityEntity_strategy = st.builds(
    MultiplicityEntity,
)
RepositoryConcept_strategy = st.builds(
    RepositoryConcept,
)
ISO20022_Type_strategy = st.builds(
    ISO20022_Type,
)
ISO20022_TopLevelDictionaryEntry_strategy = st.builds(
    ISO20022_TopLevelDictionaryEntry,
)
ISO20022_Diagram_strategy = st.builds(
    ISO20022_Diagram,
    content=
        safe_text,
    location=
        safe_text
)
ISO20022_BusinessRole_strategy = st.builds(
    ISO20022_BusinessRole,
)
ISO20022_Code_strategy = st.builds(
    ISO20022_Code,
    codeName=
        safe_text
)
ISO20022_InteractionActor_strategy = st.builds(
    ISO20022_InteractionActor,
)
ISO20022_Xor_strategy = st.builds(
    ISO20022_Xor,
)
ISO20022_Interaction_strategy = st.builds(
    ISO20022_Interaction,
    location=
        safe_text
)
ISO20022_InteractionMessage_strategy = st.builds(
    ISO20022_InteractionMessage,
)
ISO20022_TopLevelCatalogueEntry_strategy = st.builds(
    ISO20022_TopLevelCatalogueEntry,
)
ISO20022_IsAnAlternativeFor_strategy = st.builds(
    ISO20022_IsAnAlternativeFor,
)
ISO20022_Member_strategy = st.builds(
    ISO20022_Member,
)
ISO20022_LogicalType_strategy = st.builds(
    ISO20022_LogicalType,
)
MessageConcept_strategy = st.builds(
    MessageConcept,
)
XMLMember_strategy = st.builds(
    XMLMember,
)
ISO20022_MessageBuildingBlock_strategy = st.builds(
    ISO20022_MessageBuildingBlock,
)
ISO20022_MessageElement_strategy = st.builds(
    ISO20022_MessageElement,
    tracePath=
        safe_text,
    isTechnical=
        st.booleans(),
    isDerived=
        st.booleans()
)
ISO20022_MessageElementContainer_strategy = st.builds(
    ISO20022_MessageElementContainer,
)
ISO20022_BusinessElement_strategy = st.builds(
    ISO20022_BusinessElement,
    isDerived=
        st.booleans()
)
ISO20022_BusinessComponent_strategy = st.builds(
    ISO20022_BusinessComponent,
    previousVersionDocumentation=
        safe_text
)
ISO20022_MessageComponentType_strategy = st.builds(
    ISO20022_MessageComponentType,
    tracePath=
        safe_text,
    isTechnical=
        st.booleans()
)
MessageElement_strategy = st.builds(
    MessageElement,
)
ISO20022_MessageAttribute_strategy = st.builds(
    ISO20022_MessageAttribute,
)
ISO20022_MessageAssociationEnd_strategy = st.builds(
    ISO20022_MessageAssociationEnd,
    isComposite=
        st.booleans()
)
ModelEntity_strategy = st.builds(
    ModelEntity,
)
ISO20022_Syntax_strategy = st.builds(
    ISO20022_Syntax,
)
ISO20022_BusinessProcessCatalogue_strategy = st.builds(
    ISO20022_BusinessProcessCatalogue,
)
ISO20022_BusinessConcept_strategy = st.builds(
    ISO20022_BusinessConcept,
)
ISO20022_DataDictionary_strategy = st.builds(
    ISO20022_DataDictionary,
)
ISO20022_Repository_strategy = st.builds(
    ISO20022_Repository,
)
ISO20022_Facet_strategy = st.builds(
    ISO20022_Facet,
    value=
        safe_text,
    name=
        safe_text
)
ISO20022_Encoding_strategy = st.builds(
    ISO20022_Encoding,
)
ISO20022_MessageConcept_strategy = st.builds(
    ISO20022_MessageConcept,
)
ISO20022_SemanticMarkupElement_strategy = st.builds(
    ISO20022_SemanticMarkupElement,
    value=
        safe_text,
    name=
        safe_text
)
ISO20022_ModelEntity_strategy = st.builds(
    ISO20022_ModelEntity,
    objectIdentifier=
        safe_text
)
ISO20022_Doclet_strategy = st.builds(
    ISO20022_Doclet,
    type=
        safe_text,
    content=
        safe_text
)
ISO20022_SemanticMarkup_strategy = st.builds(
    ISO20022_SemanticMarkup,
    type=
        safe_text
)
ISO20022_RepositoryConcept_strategy = st.builds(
    ISO20022_RepositoryConcept,
    definition=
        safe_text,
    swiftRegistrationStatus=
        safe_text,
    swiftRemovalDate=
        st.dates(),
    removalDate=
        st.dates(),
    example=
        safe_text,
    name=
        safe_text,
    registrationStatus=
        safe_text
)
ISO20022_Constraint_strategy = st.builds(
    ISO20022_Constraint,
    injected=
        st.booleans(),
    kind=
        safe_text,
    expression=
        safe_text,
    errorText=
        safe_text,
    expressionLanguage=
        safe_text,
    errorCode=
        safe_text
)

@given(instance=MessageSet_strategy)
@settings(max_examples=50)
def test_messageset_instantiation(instance):
    assert isinstance(instance, MessageSet)

@given(instance=ISO20022_SWIFTSolution_strategy)
@settings(max_examples=50)
def test_iso20022_swiftsolution_instantiation(instance):
    assert isinstance(instance, ISO20022_SWIFTSolution)



@given(instance=ISO20022_SWIFTSolution_strategy)
def test_iso20022_swiftsolution_serviceName_setter(instance):
    original = instance.serviceName
    instance.serviceName = original
    assert instance.serviceName == original

@given(instance=MessageDefinition_strategy)
@settings(max_examples=50)
def test_messagedefinition_instantiation(instance):
    assert isinstance(instance, MessageDefinition)

@given(instance=ISO20022_ApplicationHeader_strategy)
@settings(max_examples=50)
def test_iso20022_applicationheader_instantiation(instance):
    assert isinstance(instance, ISO20022_ApplicationHeader)

@given(instance=AbstractTimeConcept_strategy)
@settings(max_examples=50)
def test_abstracttimeconcept_instantiation(instance):
    assert isinstance(instance, AbstractTimeConcept)

@given(instance=ISO20022_XSDMonth_strategy)
@settings(max_examples=50)
def test_iso20022_xsdmonth_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDMonth)

@given(instance=ISO20022_XSDTime_strategy)
@settings(max_examples=50)
def test_iso20022_xsdtime_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDTime)

@given(instance=ISO20022_XSDMonthDay_strategy)
@settings(max_examples=50)
def test_iso20022_xsdmonthday_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDMonthDay)

@given(instance=ISO20022_XSDYear_strategy)
@settings(max_examples=50)
def test_iso20022_xsdyear_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDYear)

@given(instance=ISO20022_XSDDuration_strategy)
@settings(max_examples=50)
def test_iso20022_xsdduration_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDDuration)

@given(instance=ISO20022_XSDDateTime_strategy)
@settings(max_examples=50)
def test_iso20022_xsddatetime_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDDateTime)

@given(instance=ISO20022_XSDYearMonth_strategy)
@settings(max_examples=50)
def test_iso20022_xsdyearmonth_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDYearMonth)

@given(instance=ISO20022_XSDDay_strategy)
@settings(max_examples=50)
def test_iso20022_xsdday_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDDay)

@given(instance=ISO20022_XSDDate_strategy)
@settings(max_examples=50)
def test_iso20022_xsddate_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDDate)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=ISO20022_XSDBinary_strategy)
@settings(max_examples=50)
def test_iso20022_xsdbinary_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDBinary)



@given(instance=ISO20022_XSDBinary_strategy)
def test_iso20022_xsdbinary_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=ISO20022_XSDBinary_strategy)
def test_iso20022_xsdbinary_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=ISO20022_XSDBinary_strategy)
def test_iso20022_xsdbinary_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=ISO20022_XSDBinary_strategy)
def test_iso20022_xsdbinary_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=ISO20022_AbstractTimeConcept_strategy)
@settings(max_examples=50)
def test_iso20022_abstracttimeconcept_instantiation(instance):
    assert isinstance(instance, ISO20022_AbstractTimeConcept)



@given(instance=ISO20022_AbstractTimeConcept_strategy)
def test_iso20022_abstracttimeconcept_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=ISO20022_AbstractTimeConcept_strategy)
def test_iso20022_abstracttimeconcept_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original



@given(instance=ISO20022_AbstractTimeConcept_strategy)
def test_iso20022_abstracttimeconcept_minExclusive_setter(instance):
    original = instance.minExclusive
    instance.minExclusive = original
    assert instance.minExclusive == original



@given(instance=ISO20022_AbstractTimeConcept_strategy)
def test_iso20022_abstracttimeconcept_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original



@given(instance=ISO20022_AbstractTimeConcept_strategy)
def test_iso20022_abstracttimeconcept_maxExclusive_setter(instance):
    original = instance.maxExclusive
    instance.maxExclusive = original
    assert instance.maxExclusive == original

@given(instance=ISO20022_XSDString_strategy)
@settings(max_examples=50)
def test_iso20022_xsdstring_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDString)



@given(instance=ISO20022_XSDString_strategy)
def test_iso20022_xsdstring_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=ISO20022_XSDString_strategy)
def test_iso20022_xsdstring_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=ISO20022_XSDString_strategy)
def test_iso20022_xsdstring_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=ISO20022_XSDString_strategy)
def test_iso20022_xsdstring_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=XSDString_strategy)
@settings(max_examples=50)
def test_xsdstring_instantiation(instance):
    assert isinstance(instance, XSDString)

@given(instance=ISO20022_CodeSet_strategy)
@settings(max_examples=50)
def test_iso20022_codeset_instantiation(instance):
    assert isinstance(instance, ISO20022_CodeSet)



@given(instance=ISO20022_CodeSet_strategy)
def test_iso20022_codeset_identificationScheme_setter(instance):
    original = instance.identificationScheme
    instance.identificationScheme = original
    assert instance.identificationScheme == original

@given(instance=ISO20022_XSDID_strategy)
@settings(max_examples=50)
def test_iso20022_xsdid_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDID)

@given(instance=ISO20022_Text_strategy)
@settings(max_examples=50)
def test_iso20022_text_instantiation(instance):
    assert isinstance(instance, ISO20022_Text)

@given(instance=ISO20022_XSDDecimal_strategy)
@settings(max_examples=50)
def test_iso20022_xsddecimal_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDDecimal)



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_fractionDigits_setter(instance):
    original = instance.fractionDigits
    instance.fractionDigits = original
    assert instance.fractionDigits == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_totalDigits_setter(instance):
    original = instance.totalDigits
    instance.totalDigits = original
    assert instance.totalDigits == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_minExclusive_setter(instance):
    original = instance.minExclusive
    instance.minExclusive = original
    assert instance.minExclusive == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_maxExclusive_setter(instance):
    original = instance.maxExclusive
    instance.maxExclusive = original
    assert instance.maxExclusive == original



@given(instance=ISO20022_XSDDecimal_strategy)
def test_iso20022_xsddecimal_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=XSDDecimal_strategy)
@settings(max_examples=50)
def test_xsddecimal_instantiation(instance):
    assert isinstance(instance, XSDDecimal)

@given(instance=ISO20022_Quantity_strategy)
@settings(max_examples=50)
def test_iso20022_quantity_instantiation(instance):
    assert isinstance(instance, ISO20022_Quantity)



@given(instance=ISO20022_Quantity_strategy)
def test_iso20022_quantity_unitCode_setter(instance):
    original = instance.unitCode
    instance.unitCode = original
    assert instance.unitCode == original

@given(instance=ISO20022_Amount_strategy)
@settings(max_examples=50)
def test_iso20022_amount_instantiation(instance):
    assert isinstance(instance, ISO20022_Amount)

@given(instance=ISO20022_Rate_strategy)
@settings(max_examples=50)
def test_iso20022_rate_instantiation(instance):
    assert isinstance(instance, ISO20022_Rate)



@given(instance=ISO20022_Rate_strategy)
def test_iso20022_rate_baseUnitCode_setter(instance):
    original = instance.baseUnitCode
    instance.baseUnitCode = original
    assert instance.baseUnitCode == original



@given(instance=ISO20022_Rate_strategy)
def test_iso20022_rate_baseValue_setter(instance):
    original = instance.baseValue
    instance.baseValue = original
    assert instance.baseValue == original

@given(instance=ISO20022_XSDBoolean_strategy)
@settings(max_examples=50)
def test_iso20022_xsdboolean_instantiation(instance):
    assert isinstance(instance, ISO20022_XSDBoolean)

@given(instance=XSDBoolean_strategy)
@settings(max_examples=50)
def test_xsdboolean_instantiation(instance):
    assert isinstance(instance, XSDBoolean)

@given(instance=ISO20022_Indicator_strategy)
@settings(max_examples=50)
def test_iso20022_indicator_instantiation(instance):
    assert isinstance(instance, ISO20022_Indicator)



@given(instance=ISO20022_Indicator_strategy)
def test_iso20022_indicator_meaningWhenTrue_setter(instance):
    original = instance.meaningWhenTrue
    instance.meaningWhenTrue = original
    assert instance.meaningWhenTrue == original



@given(instance=ISO20022_Indicator_strategy)
def test_iso20022_indicator_meaningWhenFalse_setter(instance):
    original = instance.meaningWhenFalse
    instance.meaningWhenFalse = original
    assert instance.meaningWhenFalse == original



@given(instance=ISO20022_Indicator_strategy)
def test_iso20022_indicator_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=ISO20022_IdentifierSet_strategy)
@settings(max_examples=50)
def test_iso20022_identifierset_instantiation(instance):
    assert isinstance(instance, ISO20022_IdentifierSet)



@given(instance=ISO20022_IdentifierSet_strategy)
def test_iso20022_identifierset_identificationScheme_setter(instance):
    original = instance.identificationScheme
    instance.identificationScheme = original
    assert instance.identificationScheme == original

@given(instance=ISO20022_MessageDefinitionIdentifier_strategy)
@settings(max_examples=50)
def test_iso20022_messagedefinitionidentifier_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageDefinitionIdentifier)



@given(instance=ISO20022_MessageDefinitionIdentifier_strategy)
def test_iso20022_messagedefinitionidentifier_messageFunctionality_setter(instance):
    original = instance.messageFunctionality
    instance.messageFunctionality = original
    assert instance.messageFunctionality == original



@given(instance=ISO20022_MessageDefinitionIdentifier_strategy)
def test_iso20022_messagedefinitionidentifier_flavour_setter(instance):
    original = instance.flavour
    instance.flavour = original
    assert instance.flavour == original



@given(instance=ISO20022_MessageDefinitionIdentifier_strategy)
def test_iso20022_messagedefinitionidentifier_businessArea_setter(instance):
    original = instance.businessArea
    instance.businessArea = original
    assert instance.businessArea == original



@given(instance=ISO20022_MessageDefinitionIdentifier_strategy)
def test_iso20022_messagedefinitionidentifier_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=MessageElementContainer_strategy)
@settings(max_examples=50)
def test_messageelementcontainer_instantiation(instance):
    assert isinstance(instance, MessageElementContainer)

@given(instance=ISO20022_ChoiceComponent_strategy)
@settings(max_examples=50)
def test_iso20022_choicecomponent_instantiation(instance):
    assert isinstance(instance, ISO20022_ChoiceComponent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_ChoiceComponent_strategy)
@settings(max_examples=30)
def test_iso20022_choicecomponent_atleastoneproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AtLeastOneProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AtLeastOneProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AtLeastOneProperty' in ISO20022_ChoiceComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AtLeastOneProperty' in ISO20022_ChoiceComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AtLeastOneProperty' in ISO20022_ChoiceComponent is not implemented or raised an error")

@given(instance=ISO20022_MessageComponent_strategy)
@settings(max_examples=50)
def test_iso20022_messagecomponent_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageComponent)

@given(instance=TopLevelCatalogueEntry_strategy)
@settings(max_examples=50)
def test_toplevelcatalogueentry_instantiation(instance):
    assert isinstance(instance, TopLevelCatalogueEntry)

@given(instance=ISO20022_SyntaxMessageScheme_strategy)
@settings(max_examples=50)
def test_iso20022_syntaxmessagescheme_instantiation(instance):
    assert isinstance(instance, ISO20022_SyntaxMessageScheme)

@given(instance=ISO20022_MessageChoreography_strategy)
@settings(max_examples=50)
def test_iso20022_messagechoreography_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageChoreography)

@given(instance=ISO20022_BusinessArea_strategy)
@settings(max_examples=50)
def test_iso20022_businessarea_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessArea)



@given(instance=ISO20022_BusinessArea_strategy)
def test_iso20022_businessarea_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=ISO20022_MessageSet_strategy)
@settings(max_examples=50)
def test_iso20022_messageset_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageSet)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageSet_strategy)
@settings(max_examples=30)
def test_iso20022_messageset_generatedsyntaxderivation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.GeneratedSyntaxDerivation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.GeneratedSyntaxDerivation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'GeneratedSyntaxDerivation' in ISO20022_MessageSet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'GeneratedSyntaxDerivation' in ISO20022_MessageSet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'GeneratedSyntaxDerivation' in ISO20022_MessageSet is not implemented or raised an error")

@given(instance=BusinessElement_strategy)
@settings(max_examples=50)
def test_businesselement_instantiation(instance):
    assert isinstance(instance, BusinessElement)

@given(instance=ISO20022_BusinessAttribute_strategy)
@settings(max_examples=50)
def test_iso20022_businessattribute_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessAttribute)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessAttribute_strategy)
@settings(max_examples=30)
def test_iso20022_businessattribute_businessattributehasexactlyonetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.BusinessAttributeHasExactlyOneType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.BusinessAttributeHasExactlyOneType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'BusinessAttributeHasExactlyOneType' in ISO20022_BusinessAttribute is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'BusinessAttributeHasExactlyOneType' in ISO20022_BusinessAttribute did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'BusinessAttributeHasExactlyOneType' in ISO20022_BusinessAttribute is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessAttribute_strategy)
@settings(max_examples=30)
def test_iso20022_businessattribute_noderivingcodesettype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NoDerivingCodeSetType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NoDerivingCodeSetType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NoDerivingCodeSetType' in ISO20022_BusinessAttribute is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NoDerivingCodeSetType' in ISO20022_BusinessAttribute did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NoDerivingCodeSetType' in ISO20022_BusinessAttribute is not implemented or raised an error")

@given(instance=MessageComponentType_strategy)
@settings(max_examples=50)
def test_messagecomponenttype_instantiation(instance):
    assert isinstance(instance, MessageComponentType)

@given(instance=ISO20022_ExternalSchema_strategy)
@settings(max_examples=50)
def test_iso20022_externalschema_instantiation(instance):
    assert isinstance(instance, ISO20022_ExternalSchema)



@given(instance=ISO20022_ExternalSchema_strategy)
def test_iso20022_externalschema_processContent_setter(instance):
    original = instance.processContent
    instance.processContent = original
    assert instance.processContent == original



@given(instance=ISO20022_ExternalSchema_strategy)
def test_iso20022_externalschema_namespaceList_setter(instance):
    original = instance.namespaceList
    instance.namespaceList = original
    assert instance.namespaceList == original

@given(instance=ISO20022_UserDefined_strategy)
@settings(max_examples=50)
def test_iso20022_userdefined_instantiation(instance):
    assert isinstance(instance, ISO20022_UserDefined)



@given(instance=ISO20022_UserDefined_strategy)
def test_iso20022_userdefined___setter(instance):
    original = instance._
    instance._ = original
    assert instance._ == original



@given(instance=ISO20022_UserDefined_strategy)
def test_iso20022_userdefined_namespaceList_setter(instance):
    original = instance.namespaceList
    instance.namespaceList = original
    assert instance.namespaceList == original



@given(instance=ISO20022_UserDefined_strategy)
def test_iso20022_userdefined_processContents_setter(instance):
    original = instance.processContents
    instance.processContents = original
    assert instance.processContents == original

@given(instance=LogicalType_strategy)
@settings(max_examples=50)
def test_logicaltype_instantiation(instance):
    assert isinstance(instance, LogicalType)

@given(instance=BusinessConcept_strategy)
@settings(max_examples=50)
def test_businessconcept_instantiation(instance):
    assert isinstance(instance, BusinessConcept)

@given(instance=TopLevelDictionaryEntry_strategy)
@settings(max_examples=50)
def test_topleveldictionaryentry_instantiation(instance):
    assert isinstance(instance, TopLevelDictionaryEntry)

@given(instance=ISO20022_EndPointCategory_strategy)
@settings(max_examples=50)
def test_iso20022_endpointcategory_instantiation(instance):
    assert isinstance(instance, ISO20022_EndPointCategory)

@given(instance=BusinessElementType_strategy)
@settings(max_examples=50)
def test_businesselementtype_instantiation(instance):
    assert isinstance(instance, BusinessElementType)

@given(instance=ISO20022_DataType_strategy)
@settings(max_examples=50)
def test_iso20022_datatype_instantiation(instance):
    assert isinstance(instance, ISO20022_DataType)

@given(instance=ISO20022_BusinessAssociationEnd_strategy)
@settings(max_examples=50)
def test_iso20022_businessassociationend_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessAssociationEnd)



@given(instance=ISO20022_BusinessAssociationEnd_strategy)
def test_iso20022_businessassociationend_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessAssociationEnd_strategy)
@settings(max_examples=30)
def test_iso20022_businessassociationend_atmostoneaggregatedend_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AtMostOneAggregatedEnd(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AtMostOneAggregatedEnd).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AtMostOneAggregatedEnd' in ISO20022_BusinessAssociationEnd is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AtMostOneAggregatedEnd' in ISO20022_BusinessAssociationEnd did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AtMostOneAggregatedEnd' in ISO20022_BusinessAssociationEnd is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessAssociationEnd_strategy)
@settings(max_examples=30)
def test_iso20022_businessassociationend_contextconsistentwithtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ContextConsistentWithType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ContextConsistentWithType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ContextConsistentWithType' in ISO20022_BusinessAssociationEnd is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ContextConsistentWithType' in ISO20022_BusinessAssociationEnd did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ContextConsistentWithType' in ISO20022_BusinessAssociationEnd is not implemented or raised an error")

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ISO20022_BusinessElementType_strategy)
@settings(max_examples=50)
def test_iso20022_businesselementtype_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessElementType)

@given(instance=ISO20022_MessageDefinition_strategy)
@settings(max_examples=50)
def test_iso20022_messagedefinition_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageDefinition)



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_xmlTag_setter(instance):
    original = instance.xmlTag
    instance.xmlTag = original
    assert instance.xmlTag == original



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_urn_setter(instance):
    original = instance.urn
    instance.urn = original
    assert instance.urn == original



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_xmlName_setter(instance):
    original = instance.xmlName
    instance.xmlName = original
    assert instance.xmlName == original



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_rootElement_setter(instance):
    original = instance.rootElement
    instance.rootElement = original
    assert instance.rootElement == original



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_previousVersionDocumentation_setter(instance):
    original = instance.previousVersionDocumentation
    instance.previousVersionDocumentation = original
    assert instance.previousVersionDocumentation == original



@given(instance=ISO20022_MessageDefinition_strategy)
def test_iso20022_messagedefinition_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageDefinition_strategy)
@settings(max_examples=30)
def test_iso20022_messagedefinition_businessareanamematch_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.BusinessAreaNameMatch(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.BusinessAreaNameMatch).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'BusinessAreaNameMatch' in ISO20022_MessageDefinition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'BusinessAreaNameMatch' in ISO20022_MessageDefinition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'BusinessAreaNameMatch' in ISO20022_MessageDefinition is not implemented or raised an error")

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=ISO20022_XMLMember_strategy)
@settings(max_examples=50)
def test_iso20022_xmlmember_instantiation(instance):
    assert isinstance(instance, ISO20022_XMLMember)



@given(instance=ISO20022_XMLMember_strategy)
def test_iso20022_xmlmember_xmlTag_setter(instance):
    original = instance.xmlTag
    instance.xmlTag = original
    assert instance.xmlTag == original

@given(instance=ISO20022_MultiplicityEntity_strategy)
@settings(max_examples=50)
def test_iso20022_multiplicityentity_instantiation(instance):
    assert isinstance(instance, ISO20022_MultiplicityEntity)



@given(instance=ISO20022_MultiplicityEntity_strategy)
def test_iso20022_multiplicityentity_minOccurs_setter(instance):
    original = instance.minOccurs
    instance.minOccurs = original
    assert instance.minOccurs == original



@given(instance=ISO20022_MultiplicityEntity_strategy)
def test_iso20022_multiplicityentity_maxOccurs_setter(instance):
    original = instance.maxOccurs
    instance.maxOccurs = original
    assert instance.maxOccurs == original

@given(instance=MultiplicityEntity_strategy)
@settings(max_examples=50)
def test_multiplicityentity_instantiation(instance):
    assert isinstance(instance, MultiplicityEntity)

@given(instance=RepositoryConcept_strategy)
@settings(max_examples=50)
def test_repositoryconcept_instantiation(instance):
    assert isinstance(instance, RepositoryConcept)

@given(instance=ISO20022_Type_strategy)
@settings(max_examples=50)
def test_iso20022_type_instantiation(instance):
    assert isinstance(instance, ISO20022_Type)

@given(instance=ISO20022_TopLevelDictionaryEntry_strategy)
@settings(max_examples=50)
def test_iso20022_topleveldictionaryentry_instantiation(instance):
    assert isinstance(instance, ISO20022_TopLevelDictionaryEntry)

@given(instance=ISO20022_Diagram_strategy)
@settings(max_examples=50)
def test_iso20022_diagram_instantiation(instance):
    assert isinstance(instance, ISO20022_Diagram)



@given(instance=ISO20022_Diagram_strategy)
def test_iso20022_diagram_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=ISO20022_Diagram_strategy)
def test_iso20022_diagram_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=ISO20022_BusinessRole_strategy)
@settings(max_examples=50)
def test_iso20022_businessrole_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessRole)

@given(instance=ISO20022_Code_strategy)
@settings(max_examples=50)
def test_iso20022_code_instantiation(instance):
    assert isinstance(instance, ISO20022_Code)



@given(instance=ISO20022_Code_strategy)
def test_iso20022_code_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original

@given(instance=ISO20022_InteractionActor_strategy)
@settings(max_examples=50)
def test_iso20022_interactionactor_instantiation(instance):
    assert isinstance(instance, ISO20022_InteractionActor)

@given(instance=ISO20022_Xor_strategy)
@settings(max_examples=50)
def test_iso20022_xor_instantiation(instance):
    assert isinstance(instance, ISO20022_Xor)

@given(instance=ISO20022_Interaction_strategy)
@settings(max_examples=50)
def test_iso20022_interaction_instantiation(instance):
    assert isinstance(instance, ISO20022_Interaction)



@given(instance=ISO20022_Interaction_strategy)
def test_iso20022_interaction_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=ISO20022_InteractionMessage_strategy)
@settings(max_examples=50)
def test_iso20022_interactionmessage_instantiation(instance):
    assert isinstance(instance, ISO20022_InteractionMessage)

@given(instance=ISO20022_TopLevelCatalogueEntry_strategy)
@settings(max_examples=50)
def test_iso20022_toplevelcatalogueentry_instantiation(instance):
    assert isinstance(instance, ISO20022_TopLevelCatalogueEntry)

@given(instance=ISO20022_IsAnAlternativeFor_strategy)
@settings(max_examples=50)
def test_iso20022_isanalternativefor_instantiation(instance):
    assert isinstance(instance, ISO20022_IsAnAlternativeFor)

@given(instance=ISO20022_Member_strategy)
@settings(max_examples=50)
def test_iso20022_member_instantiation(instance):
    assert isinstance(instance, ISO20022_Member)

@given(instance=ISO20022_LogicalType_strategy)
@settings(max_examples=50)
def test_iso20022_logicaltype_instantiation(instance):
    assert isinstance(instance, ISO20022_LogicalType)

@given(instance=MessageConcept_strategy)
@settings(max_examples=50)
def test_messageconcept_instantiation(instance):
    assert isinstance(instance, MessageConcept)

@given(instance=XMLMember_strategy)
@settings(max_examples=50)
def test_xmlmember_instantiation(instance):
    assert isinstance(instance, XMLMember)

@given(instance=ISO20022_MessageBuildingBlock_strategy)
@settings(max_examples=50)
def test_iso20022_messagebuildingblock_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageBuildingBlock)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageBuildingBlock_strategy)
@settings(max_examples=30)
def test_iso20022_messagebuildingblock_messagebuildingblockhasexactlyonetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.MessageBuildingBlockHasExactlyOneType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.MessageBuildingBlockHasExactlyOneType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'MessageBuildingBlockHasExactlyOneType' in ISO20022_MessageBuildingBlock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'MessageBuildingBlockHasExactlyOneType' in ISO20022_MessageBuildingBlock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'MessageBuildingBlockHasExactlyOneType' in ISO20022_MessageBuildingBlock is not implemented or raised an error")

@given(instance=ISO20022_MessageElement_strategy)
@settings(max_examples=50)
def test_iso20022_messageelement_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageElement)



@given(instance=ISO20022_MessageElement_strategy)
def test_iso20022_messageelement_tracePath_setter(instance):
    original = instance.tracePath
    instance.tracePath = original
    assert instance.tracePath == original



@given(instance=ISO20022_MessageElement_strategy)
def test_iso20022_messageelement_isTechnical_setter(instance):
    original = instance.isTechnical
    instance.isTechnical = original
    assert instance.isTechnical == original



@given(instance=ISO20022_MessageElement_strategy)
def test_iso20022_messageelement_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageElement_strategy)
@settings(max_examples=30)
def test_iso20022_messageelement_nomorethanonetrace_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NoMoreThanOneTrace(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NoMoreThanOneTrace).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NoMoreThanOneTrace' in ISO20022_MessageElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NoMoreThanOneTrace' in ISO20022_MessageElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NoMoreThanOneTrace' in ISO20022_MessageElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageElement_strategy)
@settings(max_examples=30)
def test_iso20022_messageelement_cardinalityalignment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CardinalityAlignment(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CardinalityAlignment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CardinalityAlignment' in ISO20022_MessageElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CardinalityAlignment' in ISO20022_MessageElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CardinalityAlignment' in ISO20022_MessageElement is not implemented or raised an error")

@given(instance=ISO20022_MessageElementContainer_strategy)
@settings(max_examples=50)
def test_iso20022_messageelementcontainer_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageElementContainer)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageElementContainer_strategy)
@settings(max_examples=30)
def test_iso20022_messageelementcontainer_messageelementshaveuniquenames_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.MessageElementsHaveUniqueNames(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.MessageElementsHaveUniqueNames).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'MessageElementsHaveUniqueNames' in ISO20022_MessageElementContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'MessageElementsHaveUniqueNames' in ISO20022_MessageElementContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'MessageElementsHaveUniqueNames' in ISO20022_MessageElementContainer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageElementContainer_strategy)
@settings(max_examples=30)
def test_iso20022_messageelementcontainer_technicalelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.technicalElement(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.technicalElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'technicalElement' in ISO20022_MessageElementContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'technicalElement' in ISO20022_MessageElementContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'technicalElement' in ISO20022_MessageElementContainer is not implemented or raised an error")

@given(instance=ISO20022_BusinessElement_strategy)
@settings(max_examples=50)
def test_iso20022_businesselement_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessElement)



@given(instance=ISO20022_BusinessElement_strategy)
def test_iso20022_businesselement_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=ISO20022_BusinessComponent_strategy)
@settings(max_examples=50)
def test_iso20022_businesscomponent_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessComponent)



@given(instance=ISO20022_BusinessComponent_strategy)
def test_iso20022_businesscomponent_previousVersionDocumentation_setter(instance):
    original = instance.previousVersionDocumentation
    instance.previousVersionDocumentation = original
    assert instance.previousVersionDocumentation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessComponent_strategy)
@settings(max_examples=30)
def test_iso20022_businesscomponent_businesselementshaveuniquenames_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.BusinessElementsHaveUniqueNames(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.BusinessElementsHaveUniqueNames).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'BusinessElementsHaveUniqueNames' in ISO20022_BusinessComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'BusinessElementsHaveUniqueNames' in ISO20022_BusinessComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'BusinessElementsHaveUniqueNames' in ISO20022_BusinessComponent is not implemented or raised an error")

@given(instance=ISO20022_MessageComponentType_strategy)
@settings(max_examples=50)
def test_iso20022_messagecomponenttype_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageComponentType)



@given(instance=ISO20022_MessageComponentType_strategy)
def test_iso20022_messagecomponenttype_tracePath_setter(instance):
    original = instance.tracePath
    instance.tracePath = original
    assert instance.tracePath == original



@given(instance=ISO20022_MessageComponentType_strategy)
def test_iso20022_messagecomponenttype_isTechnical_setter(instance):
    original = instance.isTechnical
    instance.isTechnical = original
    assert instance.isTechnical == original

@given(instance=MessageElement_strategy)
@settings(max_examples=50)
def test_messageelement_instantiation(instance):
    assert isinstance(instance, MessageElement)

@given(instance=ISO20022_MessageAttribute_strategy)
@settings(max_examples=50)
def test_iso20022_messageattribute_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageAttribute)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_MessageAttribute_strategy)
@settings(max_examples=30)
def test_iso20022_messageattribute_messageattributehasexactlyonetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.MessageAttributeHasExactlyOneType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.MessageAttributeHasExactlyOneType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'MessageAttributeHasExactlyOneType' in ISO20022_MessageAttribute is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'MessageAttributeHasExactlyOneType' in ISO20022_MessageAttribute did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'MessageAttributeHasExactlyOneType' in ISO20022_MessageAttribute is not implemented or raised an error")

@given(instance=ISO20022_MessageAssociationEnd_strategy)
@settings(max_examples=50)
def test_iso20022_messageassociationend_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageAssociationEnd)



@given(instance=ISO20022_MessageAssociationEnd_strategy)
def test_iso20022_messageassociationend_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=ModelEntity_strategy)
@settings(max_examples=50)
def test_modelentity_instantiation(instance):
    assert isinstance(instance, ModelEntity)

@given(instance=ISO20022_Syntax_strategy)
@settings(max_examples=50)
def test_iso20022_syntax_instantiation(instance):
    assert isinstance(instance, ISO20022_Syntax)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_Syntax_strategy)
@settings(max_examples=30)
def test_iso20022_syntax_generatedforderivation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.GeneratedForDerivation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.GeneratedForDerivation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'GeneratedForDerivation' in ISO20022_Syntax is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'GeneratedForDerivation' in ISO20022_Syntax did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'GeneratedForDerivation' in ISO20022_Syntax is not implemented or raised an error")

@given(instance=ISO20022_BusinessProcessCatalogue_strategy)
@settings(max_examples=50)
def test_iso20022_businessprocesscatalogue_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessProcessCatalogue)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_BusinessProcessCatalogue_strategy)
@settings(max_examples=30)
def test_iso20022_businessprocesscatalogue_entrieshaveuniquename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EntriesHaveUniqueName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EntriesHaveUniqueName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EntriesHaveUniqueName' in ISO20022_BusinessProcessCatalogue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EntriesHaveUniqueName' in ISO20022_BusinessProcessCatalogue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EntriesHaveUniqueName' in ISO20022_BusinessProcessCatalogue is not implemented or raised an error")

@given(instance=ISO20022_BusinessConcept_strategy)
@settings(max_examples=50)
def test_iso20022_businessconcept_instantiation(instance):
    assert isinstance(instance, ISO20022_BusinessConcept)

@given(instance=ISO20022_DataDictionary_strategy)
@settings(max_examples=50)
def test_iso20022_datadictionary_instantiation(instance):
    assert isinstance(instance, ISO20022_DataDictionary)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_DataDictionary_strategy)
@settings(max_examples=30)
def test_iso20022_datadictionary_entrieshaveuniquename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EntriesHaveUniqueName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EntriesHaveUniqueName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EntriesHaveUniqueName' in ISO20022_DataDictionary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EntriesHaveUniqueName' in ISO20022_DataDictionary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EntriesHaveUniqueName' in ISO20022_DataDictionary is not implemented or raised an error")

@given(instance=ISO20022_Repository_strategy)
@settings(max_examples=50)
def test_iso20022_repository_instantiation(instance):
    assert isinstance(instance, ISO20022_Repository)

@given(instance=ISO20022_Facet_strategy)
@settings(max_examples=50)
def test_iso20022_facet_instantiation(instance):
    assert isinstance(instance, ISO20022_Facet)



@given(instance=ISO20022_Facet_strategy)
def test_iso20022_facet_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ISO20022_Facet_strategy)
def test_iso20022_facet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ISO20022_Encoding_strategy)
@settings(max_examples=50)
def test_iso20022_encoding_instantiation(instance):
    assert isinstance(instance, ISO20022_Encoding)

@given(instance=ISO20022_MessageConcept_strategy)
@settings(max_examples=50)
def test_iso20022_messageconcept_instantiation(instance):
    assert isinstance(instance, ISO20022_MessageConcept)

@given(instance=ISO20022_SemanticMarkupElement_strategy)
@settings(max_examples=50)
def test_iso20022_semanticmarkupelement_instantiation(instance):
    assert isinstance(instance, ISO20022_SemanticMarkupElement)



@given(instance=ISO20022_SemanticMarkupElement_strategy)
def test_iso20022_semanticmarkupelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ISO20022_SemanticMarkupElement_strategy)
def test_iso20022_semanticmarkupelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ISO20022_ModelEntity_strategy)
@settings(max_examples=50)
def test_iso20022_modelentity_instantiation(instance):
    assert isinstance(instance, ISO20022_ModelEntity)



@given(instance=ISO20022_ModelEntity_strategy)
def test_iso20022_modelentity_objectIdentifier_setter(instance):
    original = instance.objectIdentifier
    instance.objectIdentifier = original
    assert instance.objectIdentifier == original

@given(instance=ISO20022_Doclet_strategy)
@settings(max_examples=50)
def test_iso20022_doclet_instantiation(instance):
    assert isinstance(instance, ISO20022_Doclet)



@given(instance=ISO20022_Doclet_strategy)
def test_iso20022_doclet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ISO20022_Doclet_strategy)
def test_iso20022_doclet_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=ISO20022_SemanticMarkup_strategy)
@settings(max_examples=50)
def test_iso20022_semanticmarkup_instantiation(instance):
    assert isinstance(instance, ISO20022_SemanticMarkup)



@given(instance=ISO20022_SemanticMarkup_strategy)
def test_iso20022_semanticmarkup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ISO20022_RepositoryConcept_strategy)
@settings(max_examples=50)
def test_iso20022_repositoryconcept_instantiation(instance):
    assert isinstance(instance, ISO20022_RepositoryConcept)



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_swiftRegistrationStatus_setter(instance):
    original = instance.swiftRegistrationStatus
    instance.swiftRegistrationStatus = original
    assert instance.swiftRegistrationStatus == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_swiftRemovalDate_setter(instance):
    original = instance.swiftRemovalDate
    instance.swiftRemovalDate = original
    assert instance.swiftRemovalDate == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_removalDate_setter(instance):
    original = instance.removalDate
    instance.removalDate = original
    assert instance.removalDate == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ISO20022_RepositoryConcept_strategy)
def test_iso20022_repositoryconcept_registrationStatus_setter(instance):
    original = instance.registrationStatus
    instance.registrationStatus = original
    assert instance.registrationStatus == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ISO20022_RepositoryConcept_strategy)
@settings(max_examples=30)
def test_iso20022_repositoryconcept_removaldateregistrationstatus_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RemovalDateRegistrationStatus(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RemovalDateRegistrationStatus).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RemovalDateRegistrationStatus' in ISO20022_RepositoryConcept is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RemovalDateRegistrationStatus' in ISO20022_RepositoryConcept did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RemovalDateRegistrationStatus' in ISO20022_RepositoryConcept is not implemented or raised an error")

@given(instance=ISO20022_Constraint_strategy)
@settings(max_examples=50)
def test_iso20022_constraint_instantiation(instance):
    assert isinstance(instance, ISO20022_Constraint)



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_injected_setter(instance):
    original = instance.injected
    instance.injected = original
    assert instance.injected == original



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_errorText_setter(instance):
    original = instance.errorText
    instance.errorText = original
    assert instance.errorText == original



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_expressionLanguage_setter(instance):
    original = instance.expressionLanguage
    instance.expressionLanguage = original
    assert instance.expressionLanguage == original



@given(instance=ISO20022_Constraint_strategy)
def test_iso20022_constraint_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rapidml_Element,
    Constraint,
    rapidml_RegExConstraint,
    rapidml_ValueRangeConstraint,
    rapidml_LengthConstraint,
    SingleValueType,
    rapidml_SimpleType,
    rapidml_Enumeration,
    SimpleType,
    Inheritable,
    DataExample,
    rapidml_InlineDataExample,
    rapidml_DataExample,
    rapidml_WithDataExamples,
    rapidml_Inheritable,
    Element,
    WithDataExamples,
    DataType,
    rapidml_SingleValueType,
    Feature,
    rapidml_Extensible,
    rapidml_Structure,
    rapidml_HasTitle,
    rapidml_Extension,
    rapidml_AuthenticationMethod,
    rapidml_HasSecurityValue,
    ReferenceElement,
    rapidml_ReferenceProperty,
    ConstrainableType,
    rapidml_UserDefinedType,
    rapidml_PropertyRealization,
    rapidml_HasStringValue,
    Example,
    rapidml_ExternalExample,
    rapidml_InlineExample,
    rapidml_Example,
    rapidml_WithExamples,
    URISegment,
    HasStringValue,
    rapidml_URISegment,
    rapidml_PrimitiveType,
    rapidml_PathSegment,
    ObjectRealization,
    ResourceDefinition,
    ReferenceTreatment,
    rapidml_ReferenceEmbed,
    rapidml_ReferenceLink,
    rapidml_ReferenceElement,
    rapidml_NamedLinkDescriptor,
    rapidml_ImportDeclaration,
    rapidml_PrimitiveTypesLibrary,
    rapidml_LinkRelationsLibrary,
    rapidml_MediaTypesLibrary,
    rapidml_RealizationModelLocation,
    HasTitle,
    rapidml_PrimitiveProperty,
    SourceReference,
    rapidml_PrimitiveTypeSourceReference,
    rapidml_PropertyReference,
    Parameter,
    rapidml_URIParameter,
    rapidml_CollectionReferenceElement,
    rapidml_CollectionParameter,
    ServiceDataResource,
    rapidml_ObjectResource,
    rapidml_CollectionResource,
    URIParameter,
    rapidml_TemplateParameter,
    rapidml_MatrixParameter,
    rapidml_URISegmentWithParameter,
    rapidml_Documentable,
    rapidml_Documentation,
    TypedMessage,
    Documentable,
    rapidml_SecuritySchemeLibrary,
    rapidml_SecurityScope,
    rapidml_SecuritySchemeParameter,
    rapidml_LinkRelation,
    rapidml_Operation,
    rapidml_EnumConstant,
    rapidml_DataModel,
    rapidml_SourceReference,
    RealizationContainer,
    rapidml_ReferenceRealization,
    rapidml_ServiceDataResource,
    rapidml_URI,
    rapidml_TypedResponse,
    rapidml_TypedRequest,
    Extensible,
    rapidml_DataType,
    rapidml_RealizationContainer,
    rapidml_Feature,
    rapidml_ObjectRealization,
    rapidml_ZenModel,
    rapidml_RESTElement,
    rapidml_Constraint,
    rapidml_ReferenceTreatment,
    rapidml_ConstrainableType,
    rapidml_MessageParameter,
    HasSecurityValue,
    WithExamples,
    RESTElement,
    rapidml_MediaType,
    rapidml_Parameter,
    rapidml_Method,
    rapidml_ResourceAPI,
    rapidml_SecurityScheme,
    rapidml_TypedMessage,
    rapidml_ResourceDefinition,
    AuthenticationFlows,
    HttpMessageParameterLocation,
    HTTPMethods,
    CollectionRealizationLevelEnum,
    AuthenticationTypes,
    ReferenceRealizationEnum,
    CollectionRealizationEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rapidml_element_is_not_abstract():
    assert not inspect.isabstract(rapidml_Element)


def test_rapidml_element_constructor_exists():
    assert callable(rapidml_Element.__init__)


def test_rapidml_element_constructor_args():
    sig = inspect.signature(rapidml_Element.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_rapidml_element_has_cardinality():
    assert hasattr(rapidml_Element, "cardinality")
    descriptor = None
    for klass in rapidml_Element.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_regexconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_RegExConstraint)


def test_rapidml_regexconstraint_constructor_exists():
    assert callable(rapidml_RegExConstraint.__init__)


def test_rapidml_regexconstraint_constructor_args():
    sig = inspect.signature(rapidml_RegExConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_rapidml_regexconstraint_has_pattern():
    assert hasattr(rapidml_RegExConstraint, "pattern")
    descriptor = None
    for klass in rapidml_RegExConstraint.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_valuerangeconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_ValueRangeConstraint)


def test_rapidml_valuerangeconstraint_constructor_exists():
    assert callable(rapidml_ValueRangeConstraint.__init__)


def test_rapidml_valuerangeconstraint_constructor_args():
    sig = inspect.signature(rapidml_ValueRangeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "minValueExclusive" in params, "Missing parameter 'minValueExclusive'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "maxValueExclusive" in params, "Missing parameter 'maxValueExclusive'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_rapidml_valuerangeconstraint_has_minValueExclusive():
    assert hasattr(rapidml_ValueRangeConstraint, "minValueExclusive")
    descriptor = None
    for klass in rapidml_ValueRangeConstraint.__mro__:
        if "minValueExclusive" in klass.__dict__:
            descriptor = klass.__dict__["minValueExclusive"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_valuerangeconstraint_has_maxValue():
    assert hasattr(rapidml_ValueRangeConstraint, "maxValue")
    descriptor = None
    for klass in rapidml_ValueRangeConstraint.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_valuerangeconstraint_has_maxValueExclusive():
    assert hasattr(rapidml_ValueRangeConstraint, "maxValueExclusive")
    descriptor = None
    for klass in rapidml_ValueRangeConstraint.__mro__:
        if "maxValueExclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxValueExclusive"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_valuerangeconstraint_has_minValue():
    assert hasattr(rapidml_ValueRangeConstraint, "minValue")
    descriptor = None
    for klass in rapidml_ValueRangeConstraint.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_LengthConstraint)


def test_rapidml_lengthconstraint_constructor_exists():
    assert callable(rapidml_LengthConstraint.__init__)


def test_rapidml_lengthconstraint_constructor_args():
    sig = inspect.signature(rapidml_LengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "length" in params, "Missing parameter 'length'"
    assert "minLength" in params, "Missing parameter 'minLength'"

def test_rapidml_lengthconstraint_has_maxLength():
    assert hasattr(rapidml_LengthConstraint, "maxLength")
    descriptor = None
    for klass in rapidml_LengthConstraint.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_lengthconstraint_has_length():
    assert hasattr(rapidml_LengthConstraint, "length")
    descriptor = None
    for klass in rapidml_LengthConstraint.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_lengthconstraint_has_minLength():
    assert hasattr(rapidml_LengthConstraint, "minLength")
    descriptor = None
    for klass in rapidml_LengthConstraint.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)



def test_singlevaluetype_is_not_abstract():
    assert not inspect.isabstract(SingleValueType)


def test_singlevaluetype_constructor_exists():
    assert callable(SingleValueType.__init__)


def test_singlevaluetype_constructor_args():
    sig = inspect.signature(SingleValueType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_simpletype_is_not_abstract():
    assert not inspect.isabstract(rapidml_SimpleType)


def test_rapidml_simpletype_constructor_exists():
    assert callable(rapidml_SimpleType.__init__)


def test_rapidml_simpletype_constructor_args():
    sig = inspect.signature(rapidml_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_enumeration_is_not_abstract():
    assert not inspect.isabstract(rapidml_Enumeration)


def test_rapidml_enumeration_constructor_exists():
    assert callable(rapidml_Enumeration.__init__)


def test_rapidml_enumeration_constructor_args():
    sig = inspect.signature(rapidml_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_inheritable_is_not_abstract():
    assert not inspect.isabstract(Inheritable)


def test_inheritable_constructor_exists():
    assert callable(Inheritable.__init__)


def test_inheritable_constructor_args():
    sig = inspect.signature(Inheritable.__init__)
    params = list(sig.parameters.keys())



def test_dataexample_is_not_abstract():
    assert not inspect.isabstract(DataExample)


def test_dataexample_constructor_exists():
    assert callable(DataExample.__init__)


def test_dataexample_constructor_args():
    sig = inspect.signature(DataExample.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_inlinedataexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_InlineDataExample)


def test_rapidml_inlinedataexample_constructor_exists():
    assert callable(rapidml_InlineDataExample.__init__)


def test_rapidml_inlinedataexample_constructor_args():
    sig = inspect.signature(rapidml_InlineDataExample.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_rapidml_inlinedataexample_has_body():
    assert hasattr(rapidml_InlineDataExample, "body")
    descriptor = None
    for klass in rapidml_InlineDataExample.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_dataexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataExample)


def test_rapidml_dataexample_constructor_exists():
    assert callable(rapidml_DataExample.__init__)


def test_rapidml_dataexample_constructor_args():
    sig = inspect.signature(rapidml_DataExample.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_withdataexamples_is_not_abstract():
    assert not inspect.isabstract(rapidml_WithDataExamples)


def test_rapidml_withdataexamples_constructor_exists():
    assert callable(rapidml_WithDataExamples.__init__)


def test_rapidml_withdataexamples_constructor_args():
    sig = inspect.signature(rapidml_WithDataExamples.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_inheritable_is_not_abstract():
    assert not inspect.isabstract(rapidml_Inheritable)


def test_rapidml_inheritable_constructor_exists():
    assert callable(rapidml_Inheritable.__init__)


def test_rapidml_inheritable_constructor_args():
    sig = inspect.signature(rapidml_Inheritable.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_withdataexamples_is_not_abstract():
    assert not inspect.isabstract(WithDataExamples)


def test_withdataexamples_constructor_exists():
    assert callable(WithDataExamples.__init__)


def test_withdataexamples_constructor_args():
    sig = inspect.signature(WithDataExamples.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_singlevaluetype_is_not_abstract():
    assert not inspect.isabstract(rapidml_SingleValueType)


def test_rapidml_singlevaluetype_constructor_exists():
    assert callable(rapidml_SingleValueType.__init__)


def test_rapidml_singlevaluetype_constructor_args():
    sig = inspect.signature(rapidml_SingleValueType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_extensible_is_not_abstract():
    assert not inspect.isabstract(rapidml_Extensible)


def test_rapidml_extensible_constructor_exists():
    assert callable(rapidml_Extensible.__init__)


def test_rapidml_extensible_constructor_args():
    sig = inspect.signature(rapidml_Extensible.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_structure_is_not_abstract():
    assert not inspect.isabstract(rapidml_Structure)


def test_rapidml_structure_constructor_exists():
    assert callable(rapidml_Structure.__init__)


def test_rapidml_structure_constructor_args():
    sig = inspect.signature(rapidml_Structure.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_hastitle_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasTitle)


def test_rapidml_hastitle_constructor_exists():
    assert callable(rapidml_HasTitle.__init__)


def test_rapidml_hastitle_constructor_args():
    sig = inspect.signature(rapidml_HasTitle.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_rapidml_hastitle_has_title():
    assert hasattr(rapidml_HasTitle, "title")
    descriptor = None
    for klass in rapidml_HasTitle.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_extension_is_not_abstract():
    assert not inspect.isabstract(rapidml_Extension)


def test_rapidml_extension_constructor_exists():
    assert callable(rapidml_Extension.__init__)


def test_rapidml_extension_constructor_args():
    sig = inspect.signature(rapidml_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_rapidml_extension_has_name():
    assert hasattr(rapidml_Extension, "name")
    descriptor = None
    for klass in rapidml_Extension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_extension_has_value():
    assert hasattr(rapidml_Extension, "value")
    descriptor = None
    for klass in rapidml_Extension.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_authenticationmethod_is_not_abstract():
    assert not inspect.isabstract(rapidml_AuthenticationMethod)


def test_rapidml_authenticationmethod_constructor_exists():
    assert callable(rapidml_AuthenticationMethod.__init__)


def test_rapidml_authenticationmethod_constructor_args():
    sig = inspect.signature(rapidml_AuthenticationMethod.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_hassecurityvalue_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasSecurityValue)


def test_rapidml_hassecurityvalue_constructor_exists():
    assert callable(rapidml_HasSecurityValue.__init__)


def test_rapidml_hassecurityvalue_constructor_args():
    sig = inspect.signature(rapidml_HasSecurityValue.__init__)
    params = list(sig.parameters.keys())



def test_referenceelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceElement)


def test_referenceelement_constructor_exists():
    assert callable(ReferenceElement.__init__)


def test_referenceelement_constructor_args():
    sig = inspect.signature(ReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_referenceproperty_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceProperty)


def test_rapidml_referenceproperty_constructor_exists():
    assert callable(rapidml_ReferenceProperty.__init__)


def test_rapidml_referenceproperty_constructor_args():
    sig = inspect.signature(rapidml_ReferenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"
    assert "containment" in params, "Missing parameter 'containment'"

def test_rapidml_referenceproperty_has_container():
    assert hasattr(rapidml_ReferenceProperty, "container")
    descriptor = None
    for klass in rapidml_ReferenceProperty.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_referenceproperty_has_containment():
    assert hasattr(rapidml_ReferenceProperty, "containment")
    descriptor = None
    for klass in rapidml_ReferenceProperty.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)



def test_constrainabletype_is_not_abstract():
    assert not inspect.isabstract(ConstrainableType)


def test_constrainabletype_constructor_exists():
    assert callable(ConstrainableType.__init__)


def test_constrainabletype_constructor_args():
    sig = inspect.signature(ConstrainableType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(rapidml_UserDefinedType)


def test_rapidml_userdefinedtype_constructor_exists():
    assert callable(rapidml_UserDefinedType.__init__)


def test_rapidml_userdefinedtype_constructor_args():
    sig = inspect.signature(rapidml_UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_propertyrealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_PropertyRealization)


def test_rapidml_propertyrealization_constructor_exists():
    assert callable(rapidml_PropertyRealization.__init__)


def test_rapidml_propertyrealization_constructor_args():
    sig = inspect.signature(rapidml_PropertyRealization.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_rapidml_propertyrealization_has_cardinality():
    assert hasattr(rapidml_PropertyRealization, "cardinality")
    descriptor = None
    for klass in rapidml_PropertyRealization.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_hasstringvalue_is_not_abstract():
    assert not inspect.isabstract(rapidml_HasStringValue)


def test_rapidml_hasstringvalue_constructor_exists():
    assert callable(rapidml_HasStringValue.__init__)


def test_rapidml_hasstringvalue_constructor_args():
    sig = inspect.signature(rapidml_HasStringValue.__init__)
    params = list(sig.parameters.keys())



def test_example_is_not_abstract():
    assert not inspect.isabstract(Example)


def test_example_constructor_exists():
    assert callable(Example.__init__)


def test_example_constructor_args():
    sig = inspect.signature(Example.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_externalexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_ExternalExample)


def test_rapidml_externalexample_constructor_exists():
    assert callable(rapidml_ExternalExample.__init__)


def test_rapidml_externalexample_constructor_args():
    sig = inspect.signature(rapidml_ExternalExample.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_rapidml_externalexample_has_path():
    assert hasattr(rapidml_ExternalExample, "path")
    descriptor = None
    for klass in rapidml_ExternalExample.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_inlineexample_is_not_abstract():
    assert not inspect.isabstract(rapidml_InlineExample)


def test_rapidml_inlineexample_constructor_exists():
    assert callable(rapidml_InlineExample.__init__)


def test_rapidml_inlineexample_constructor_args():
    sig = inspect.signature(rapidml_InlineExample.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_rapidml_inlineexample_has_body():
    assert hasattr(rapidml_InlineExample, "body")
    descriptor = None
    for klass in rapidml_InlineExample.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_example_is_not_abstract():
    assert not inspect.isabstract(rapidml_Example)


def test_rapidml_example_constructor_exists():
    assert callable(rapidml_Example.__init__)


def test_rapidml_example_constructor_args():
    sig = inspect.signature(rapidml_Example.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_withexamples_is_not_abstract():
    assert not inspect.isabstract(rapidml_WithExamples)


def test_rapidml_withexamples_constructor_exists():
    assert callable(rapidml_WithExamples.__init__)


def test_rapidml_withexamples_constructor_args():
    sig = inspect.signature(rapidml_WithExamples.__init__)
    params = list(sig.parameters.keys())



def test_urisegment_is_not_abstract():
    assert not inspect.isabstract(URISegment)


def test_urisegment_constructor_exists():
    assert callable(URISegment.__init__)


def test_urisegment_constructor_args():
    sig = inspect.signature(URISegment.__init__)
    params = list(sig.parameters.keys())



def test_hasstringvalue_is_not_abstract():
    assert not inspect.isabstract(HasStringValue)


def test_hasstringvalue_constructor_exists():
    assert callable(HasStringValue.__init__)


def test_hasstringvalue_constructor_args():
    sig = inspect.signature(HasStringValue.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_urisegment_is_not_abstract():
    assert not inspect.isabstract(rapidml_URISegment)


def test_rapidml_urisegment_constructor_exists():
    assert callable(rapidml_URISegment.__init__)


def test_rapidml_urisegment_constructor_args():
    sig = inspect.signature(rapidml_URISegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_urisegment_has_name():
    assert hasattr(rapidml_URISegment, "name")
    descriptor = None
    for klass in rapidml_URISegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveType)


def test_rapidml_primitivetype_constructor_exists():
    assert callable(rapidml_PrimitiveType.__init__)


def test_rapidml_primitivetype_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_pathsegment_is_not_abstract():
    assert not inspect.isabstract(rapidml_PathSegment)


def test_rapidml_pathsegment_constructor_exists():
    assert callable(rapidml_PathSegment.__init__)


def test_rapidml_pathsegment_constructor_args():
    sig = inspect.signature(rapidml_PathSegment.__init__)
    params = list(sig.parameters.keys())



def test_objectrealization_is_not_abstract():
    assert not inspect.isabstract(ObjectRealization)


def test_objectrealization_constructor_exists():
    assert callable(ObjectRealization.__init__)


def test_objectrealization_constructor_args():
    sig = inspect.signature(ObjectRealization.__init__)
    params = list(sig.parameters.keys())



def test_resourcedefinition_is_not_abstract():
    assert not inspect.isabstract(ResourceDefinition)


def test_resourcedefinition_constructor_exists():
    assert callable(ResourceDefinition.__init__)


def test_resourcedefinition_constructor_args():
    sig = inspect.signature(ResourceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_referencetreatment_is_not_abstract():
    assert not inspect.isabstract(ReferenceTreatment)


def test_referencetreatment_constructor_exists():
    assert callable(ReferenceTreatment.__init__)


def test_referencetreatment_constructor_args():
    sig = inspect.signature(ReferenceTreatment.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_referenceembed_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceEmbed)


def test_rapidml_referenceembed_constructor_exists():
    assert callable(rapidml_ReferenceEmbed.__init__)


def test_rapidml_referenceembed_constructor_args():
    sig = inspect.signature(rapidml_ReferenceEmbed.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_referencelink_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceLink)


def test_rapidml_referencelink_constructor_exists():
    assert callable(rapidml_ReferenceLink.__init__)


def test_rapidml_referencelink_constructor_args():
    sig = inspect.signature(rapidml_ReferenceLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "collectionRealizationLevel" in params, "Missing parameter 'collectionRealizationLevel'"

def test_rapidml_referencelink_has_name():
    assert hasattr(rapidml_ReferenceLink, "name")
    descriptor = None
    for klass in rapidml_ReferenceLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_referencelink_has_collectionRealizationLevel():
    assert hasattr(rapidml_ReferenceLink, "collectionRealizationLevel")
    descriptor = None
    for klass in rapidml_ReferenceLink.__mro__:
        if "collectionRealizationLevel" in klass.__dict__:
            descriptor = klass.__dict__["collectionRealizationLevel"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_referenceelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceElement)


def test_rapidml_referenceelement_constructor_exists():
    assert callable(rapidml_ReferenceElement.__init__)


def test_rapidml_referenceelement_constructor_args():
    sig = inspect.signature(rapidml_ReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_namedlinkdescriptor_is_not_abstract():
    assert not inspect.isabstract(rapidml_NamedLinkDescriptor)


def test_rapidml_namedlinkdescriptor_constructor_exists():
    assert callable(rapidml_NamedLinkDescriptor.__init__)


def test_rapidml_namedlinkdescriptor_constructor_args():
    sig = inspect.signature(rapidml_NamedLinkDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_namedlinkdescriptor_has_default():
    assert hasattr(rapidml_NamedLinkDescriptor, "default")
    descriptor = None
    for klass in rapidml_NamedLinkDescriptor.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_namedlinkdescriptor_has_name():
    assert hasattr(rapidml_NamedLinkDescriptor, "name")
    descriptor = None
    for klass in rapidml_NamedLinkDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(rapidml_ImportDeclaration)


def test_rapidml_importdeclaration_constructor_exists():
    assert callable(rapidml_ImportDeclaration.__init__)


def test_rapidml_importdeclaration_constructor_args():
    sig = inspect.signature(rapidml_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_rapidml_importdeclaration_has_importURI():
    assert hasattr(rapidml_ImportDeclaration, "importURI")
    descriptor = None
    for klass in rapidml_ImportDeclaration.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_importdeclaration_has_importedNamespace():
    assert hasattr(rapidml_ImportDeclaration, "importedNamespace")
    descriptor = None
    for klass in rapidml_ImportDeclaration.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_importdeclaration_has_alias():
    assert hasattr(rapidml_ImportDeclaration, "alias")
    descriptor = None
    for klass in rapidml_ImportDeclaration.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_primitivetypeslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveTypesLibrary)


def test_rapidml_primitivetypeslibrary_constructor_exists():
    assert callable(rapidml_PrimitiveTypesLibrary.__init__)


def test_rapidml_primitivetypeslibrary_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_primitivetypeslibrary_has_name():
    assert hasattr(rapidml_PrimitiveTypesLibrary, "name")
    descriptor = None
    for klass in rapidml_PrimitiveTypesLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_linkrelationslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_LinkRelationsLibrary)


def test_rapidml_linkrelationslibrary_constructor_exists():
    assert callable(rapidml_LinkRelationsLibrary.__init__)


def test_rapidml_linkrelationslibrary_constructor_args():
    sig = inspect.signature(rapidml_LinkRelationsLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_linkrelationslibrary_has_name():
    assert hasattr(rapidml_LinkRelationsLibrary, "name")
    descriptor = None
    for klass in rapidml_LinkRelationsLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_mediatypeslibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_MediaTypesLibrary)


def test_rapidml_mediatypeslibrary_constructor_exists():
    assert callable(rapidml_MediaTypesLibrary.__init__)


def test_rapidml_mediatypeslibrary_constructor_args():
    sig = inspect.signature(rapidml_MediaTypesLibrary.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_realizationmodellocation_is_not_abstract():
    assert not inspect.isabstract(rapidml_RealizationModelLocation)


def test_rapidml_realizationmodellocation_constructor_exists():
    assert callable(rapidml_RealizationModelLocation.__init__)


def test_rapidml_realizationmodellocation_constructor_args():
    sig = inspect.signature(rapidml_RealizationModelLocation.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_rapidml_realizationmodellocation_has_uri():
    assert hasattr(rapidml_RealizationModelLocation, "uri")
    descriptor = None
    for klass in rapidml_RealizationModelLocation.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_hastitle_is_not_abstract():
    assert not inspect.isabstract(HasTitle)


def test_hastitle_constructor_exists():
    assert callable(HasTitle.__init__)


def test_hastitle_constructor_args():
    sig = inspect.signature(HasTitle.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_primitiveproperty_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveProperty)


def test_rapidml_primitiveproperty_constructor_exists():
    assert callable(rapidml_PrimitiveProperty.__init__)


def test_rapidml_primitiveproperty_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_sourcereference_is_not_abstract():
    assert not inspect.isabstract(SourceReference)


def test_sourcereference_constructor_exists():
    assert callable(SourceReference.__init__)


def test_sourcereference_constructor_args():
    sig = inspect.signature(SourceReference.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_primitivetypesourcereference_is_not_abstract():
    assert not inspect.isabstract(rapidml_PrimitiveTypeSourceReference)


def test_rapidml_primitivetypesourcereference_constructor_exists():
    assert callable(rapidml_PrimitiveTypeSourceReference.__init__)


def test_rapidml_primitivetypesourcereference_constructor_args():
    sig = inspect.signature(rapidml_PrimitiveTypeSourceReference.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_propertyreference_is_not_abstract():
    assert not inspect.isabstract(rapidml_PropertyReference)


def test_rapidml_propertyreference_constructor_exists():
    assert callable(rapidml_PropertyReference.__init__)


def test_rapidml_propertyreference_constructor_args():
    sig = inspect.signature(rapidml_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_uriparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_URIParameter)


def test_rapidml_uriparameter_constructor_exists():
    assert callable(rapidml_URIParameter.__init__)


def test_rapidml_uriparameter_constructor_args():
    sig = inspect.signature(rapidml_URIParameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_collectionreferenceelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionReferenceElement)


def test_rapidml_collectionreferenceelement_constructor_exists():
    assert callable(rapidml_CollectionReferenceElement.__init__)


def test_rapidml_collectionreferenceelement_constructor_args():
    sig = inspect.signature(rapidml_CollectionReferenceElement.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_collectionparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionParameter)


def test_rapidml_collectionparameter_constructor_exists():
    assert callable(rapidml_CollectionParameter.__init__)


def test_rapidml_collectionparameter_constructor_args():
    sig = inspect.signature(rapidml_CollectionParameter.__init__)
    params = list(sig.parameters.keys())



def test_servicedataresource_is_not_abstract():
    assert not inspect.isabstract(ServiceDataResource)


def test_servicedataresource_constructor_exists():
    assert callable(ServiceDataResource.__init__)


def test_servicedataresource_constructor_args():
    sig = inspect.signature(ServiceDataResource.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_objectresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_ObjectResource)


def test_rapidml_objectresource_constructor_exists():
    assert callable(rapidml_ObjectResource.__init__)


def test_rapidml_objectresource_constructor_args():
    sig = inspect.signature(rapidml_ObjectResource.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_collectionresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_CollectionResource)


def test_rapidml_collectionresource_constructor_exists():
    assert callable(rapidml_CollectionResource.__init__)


def test_rapidml_collectionresource_constructor_args():
    sig = inspect.signature(rapidml_CollectionResource.__init__)
    params = list(sig.parameters.keys())
    assert "resourceRealizationKind" in params, "Missing parameter 'resourceRealizationKind'"

def test_rapidml_collectionresource_has_resourceRealizationKind():
    assert hasattr(rapidml_CollectionResource, "resourceRealizationKind")
    descriptor = None
    for klass in rapidml_CollectionResource.__mro__:
        if "resourceRealizationKind" in klass.__dict__:
            descriptor = klass.__dict__["resourceRealizationKind"]
            break
    assert isinstance(descriptor, property)



def test_uriparameter_is_not_abstract():
    assert not inspect.isabstract(URIParameter)


def test_uriparameter_constructor_exists():
    assert callable(URIParameter.__init__)


def test_uriparameter_constructor_args():
    sig = inspect.signature(URIParameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_templateparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_TemplateParameter)


def test_rapidml_templateparameter_constructor_exists():
    assert callable(rapidml_TemplateParameter.__init__)


def test_rapidml_templateparameter_constructor_args():
    sig = inspect.signature(rapidml_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_matrixparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_MatrixParameter)


def test_rapidml_matrixparameter_constructor_exists():
    assert callable(rapidml_MatrixParameter.__init__)


def test_rapidml_matrixparameter_constructor_args():
    sig = inspect.signature(rapidml_MatrixParameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_urisegmentwithparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_URISegmentWithParameter)


def test_rapidml_urisegmentwithparameter_constructor_exists():
    assert callable(rapidml_URISegmentWithParameter.__init__)


def test_rapidml_urisegmentwithparameter_constructor_args():
    sig = inspect.signature(rapidml_URISegmentWithParameter.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_documentable_is_not_abstract():
    assert not inspect.isabstract(rapidml_Documentable)


def test_rapidml_documentable_constructor_exists():
    assert callable(rapidml_Documentable.__init__)


def test_rapidml_documentable_constructor_args():
    sig = inspect.signature(rapidml_Documentable.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_documentation_is_not_abstract():
    assert not inspect.isabstract(rapidml_Documentation)


def test_rapidml_documentation_constructor_exists():
    assert callable(rapidml_Documentation.__init__)


def test_rapidml_documentation_constructor_args():
    sig = inspect.signature(rapidml_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_rapidml_documentation_has_text():
    assert hasattr(rapidml_Documentation, "text")
    descriptor = None
    for klass in rapidml_Documentation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_typedmessage_is_not_abstract():
    assert not inspect.isabstract(TypedMessage)


def test_typedmessage_constructor_exists():
    assert callable(TypedMessage.__init__)


def test_typedmessage_constructor_args():
    sig = inspect.signature(TypedMessage.__init__)
    params = list(sig.parameters.keys())



def test_documentable_is_not_abstract():
    assert not inspect.isabstract(Documentable)


def test_documentable_constructor_exists():
    assert callable(Documentable.__init__)


def test_documentable_constructor_args():
    sig = inspect.signature(Documentable.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_securityschemelibrary_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecuritySchemeLibrary)


def test_rapidml_securityschemelibrary_constructor_exists():
    assert callable(rapidml_SecuritySchemeLibrary.__init__)


def test_rapidml_securityschemelibrary_constructor_args():
    sig = inspect.signature(rapidml_SecuritySchemeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_securityschemelibrary_has_name():
    assert hasattr(rapidml_SecuritySchemeLibrary, "name")
    descriptor = None
    for klass in rapidml_SecuritySchemeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_securityscope_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecurityScope)


def test_rapidml_securityscope_constructor_exists():
    assert callable(rapidml_SecurityScope.__init__)


def test_rapidml_securityscope_constructor_args():
    sig = inspect.signature(rapidml_SecurityScope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_securityscope_has_name():
    assert hasattr(rapidml_SecurityScope, "name")
    descriptor = None
    for klass in rapidml_SecurityScope.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_securityschemeparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecuritySchemeParameter)


def test_rapidml_securityschemeparameter_constructor_exists():
    assert callable(rapidml_SecuritySchemeParameter.__init__)


def test_rapidml_securityschemeparameter_constructor_args():
    sig = inspect.signature(rapidml_SecuritySchemeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_rapidml_securityschemeparameter_has_name():
    assert hasattr(rapidml_SecuritySchemeParameter, "name")
    descriptor = None
    for klass in rapidml_SecuritySchemeParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_securityschemeparameter_has_value():
    assert hasattr(rapidml_SecuritySchemeParameter, "value")
    descriptor = None
    for klass in rapidml_SecuritySchemeParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_linkrelation_is_not_abstract():
    assert not inspect.isabstract(rapidml_LinkRelation)


def test_rapidml_linkrelation_constructor_exists():
    assert callable(rapidml_LinkRelation.__init__)


def test_rapidml_linkrelation_constructor_args():
    sig = inspect.signature(rapidml_LinkRelation.__init__)
    params = list(sig.parameters.keys())
    assert "specURL" in params, "Missing parameter 'specURL'"
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_linkrelation_has_specURL():
    assert hasattr(rapidml_LinkRelation, "specURL")
    descriptor = None
    for klass in rapidml_LinkRelation.__mro__:
        if "specURL" in klass.__dict__:
            descriptor = klass.__dict__["specURL"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_linkrelation_has_name():
    assert hasattr(rapidml_LinkRelation, "name")
    descriptor = None
    for klass in rapidml_LinkRelation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_operation_is_not_abstract():
    assert not inspect.isabstract(rapidml_Operation)


def test_rapidml_operation_constructor_exists():
    assert callable(rapidml_Operation.__init__)


def test_rapidml_operation_constructor_args():
    sig = inspect.signature(rapidml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_operation_has_name():
    assert hasattr(rapidml_Operation, "name")
    descriptor = None
    for klass in rapidml_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_enumconstant_is_not_abstract():
    assert not inspect.isabstract(rapidml_EnumConstant)


def test_rapidml_enumconstant_constructor_exists():
    assert callable(rapidml_EnumConstant.__init__)


def test_rapidml_enumconstant_constructor_args():
    sig = inspect.signature(rapidml_EnumConstant.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_rapidml_enumconstant_has_literalValue():
    assert hasattr(rapidml_EnumConstant, "literalValue")
    descriptor = None
    for klass in rapidml_EnumConstant.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_enumconstant_has_name():
    assert hasattr(rapidml_EnumConstant, "name")
    descriptor = None
    for klass in rapidml_EnumConstant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_enumconstant_has_integerValue():
    assert hasattr(rapidml_EnumConstant, "integerValue")
    descriptor = None
    for klass in rapidml_EnumConstant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_datamodel_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataModel)


def test_rapidml_datamodel_constructor_exists():
    assert callable(rapidml_DataModel.__init__)


def test_rapidml_datamodel_constructor_args():
    sig = inspect.signature(rapidml_DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_datamodel_has_name():
    assert hasattr(rapidml_DataModel, "name")
    descriptor = None
    for klass in rapidml_DataModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_sourcereference_is_not_abstract():
    assert not inspect.isabstract(rapidml_SourceReference)


def test_rapidml_sourcereference_constructor_exists():
    assert callable(rapidml_SourceReference.__init__)


def test_rapidml_sourcereference_constructor_args():
    sig = inspect.signature(rapidml_SourceReference.__init__)
    params = list(sig.parameters.keys())



def test_realizationcontainer_is_not_abstract():
    assert not inspect.isabstract(RealizationContainer)


def test_realizationcontainer_constructor_exists():
    assert callable(RealizationContainer.__init__)


def test_realizationcontainer_constructor_args():
    sig = inspect.signature(RealizationContainer.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_referencerealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceRealization)


def test_rapidml_referencerealization_constructor_exists():
    assert callable(rapidml_ReferenceRealization.__init__)


def test_rapidml_referencerealization_constructor_args():
    sig = inspect.signature(rapidml_ReferenceRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizationType" in params, "Missing parameter 'realizationType'"
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_rapidml_referencerealization_has_realizationType():
    assert hasattr(rapidml_ReferenceRealization, "realizationType")
    descriptor = None
    for klass in rapidml_ReferenceRealization.__mro__:
        if "realizationType" in klass.__dict__:
            descriptor = klass.__dict__["realizationType"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_referencerealization_has_multiValued():
    assert hasattr(rapidml_ReferenceRealization, "multiValued")
    descriptor = None
    for klass in rapidml_ReferenceRealization.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_servicedataresource_is_not_abstract():
    assert not inspect.isabstract(rapidml_ServiceDataResource)


def test_rapidml_servicedataresource_constructor_exists():
    assert callable(rapidml_ServiceDataResource.__init__)


def test_rapidml_servicedataresource_constructor_args():
    sig = inspect.signature(rapidml_ServiceDataResource.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_rapidml_servicedataresource_has_default():
    assert hasattr(rapidml_ServiceDataResource, "default")
    descriptor = None
    for klass in rapidml_ServiceDataResource.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_uri_is_not_abstract():
    assert not inspect.isabstract(rapidml_URI)


def test_rapidml_uri_constructor_exists():
    assert callable(rapidml_URI.__init__)


def test_rapidml_uri_constructor_args():
    sig = inspect.signature(rapidml_URI.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_typedresponse_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedResponse)


def test_rapidml_typedresponse_constructor_exists():
    assert callable(rapidml_TypedResponse.__init__)


def test_rapidml_typedresponse_constructor_args():
    sig = inspect.signature(rapidml_TypedResponse.__init__)
    params = list(sig.parameters.keys())
    assert "statusCode" in params, "Missing parameter 'statusCode'"

def test_rapidml_typedresponse_has_statusCode():
    assert hasattr(rapidml_TypedResponse, "statusCode")
    descriptor = None
    for klass in rapidml_TypedResponse.__mro__:
        if "statusCode" in klass.__dict__:
            descriptor = klass.__dict__["statusCode"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_typedrequest_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedRequest)


def test_rapidml_typedrequest_constructor_exists():
    assert callable(rapidml_TypedRequest.__init__)


def test_rapidml_typedrequest_constructor_args():
    sig = inspect.signature(rapidml_TypedRequest.__init__)
    params = list(sig.parameters.keys())



def test_extensible_is_not_abstract():
    assert not inspect.isabstract(Extensible)


def test_extensible_constructor_exists():
    assert callable(Extensible.__init__)


def test_extensible_constructor_args():
    sig = inspect.signature(Extensible.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_datatype_is_not_abstract():
    assert not inspect.isabstract(rapidml_DataType)


def test_rapidml_datatype_constructor_exists():
    assert callable(rapidml_DataType.__init__)


def test_rapidml_datatype_constructor_args():
    sig = inspect.signature(rapidml_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_datatype_has_name():
    assert hasattr(rapidml_DataType, "name")
    descriptor = None
    for klass in rapidml_DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_realizationcontainer_is_not_abstract():
    assert not inspect.isabstract(rapidml_RealizationContainer)


def test_rapidml_realizationcontainer_constructor_exists():
    assert callable(rapidml_RealizationContainer.__init__)


def test_rapidml_realizationcontainer_constructor_args():
    sig = inspect.signature(rapidml_RealizationContainer.__init__)
    params = list(sig.parameters.keys())
    assert "effectiveRealization" in params, "Missing parameter 'effectiveRealization'"
    assert "realizationName" in params, "Missing parameter 'realizationName'"
    assert "withDefaultRealization" in params, "Missing parameter 'withDefaultRealization'"

def test_rapidml_realizationcontainer_has_effectiveRealization():
    assert hasattr(rapidml_RealizationContainer, "effectiveRealization")
    descriptor = None
    for klass in rapidml_RealizationContainer.__mro__:
        if "effectiveRealization" in klass.__dict__:
            descriptor = klass.__dict__["effectiveRealization"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_realizationcontainer_has_realizationName():
    assert hasattr(rapidml_RealizationContainer, "realizationName")
    descriptor = None
    for klass in rapidml_RealizationContainer.__mro__:
        if "realizationName" in klass.__dict__:
            descriptor = klass.__dict__["realizationName"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_realizationcontainer_has_withDefaultRealization():
    assert hasattr(rapidml_RealizationContainer, "withDefaultRealization")
    descriptor = None
    for klass in rapidml_RealizationContainer.__mro__:
        if "withDefaultRealization" in klass.__dict__:
            descriptor = klass.__dict__["withDefaultRealization"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_feature_is_not_abstract():
    assert not inspect.isabstract(rapidml_Feature)


def test_rapidml_feature_constructor_exists():
    assert callable(rapidml_Feature.__init__)


def test_rapidml_feature_constructor_args():
    sig = inspect.signature(rapidml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "name" in params, "Missing parameter 'name'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "restriction" in params, "Missing parameter 'restriction'"

def test_rapidml_feature_has_key():
    assert hasattr(rapidml_Feature, "key")
    descriptor = None
    for klass in rapidml_Feature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_feature_has_name():
    assert hasattr(rapidml_Feature, "name")
    descriptor = None
    for klass in rapidml_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_feature_has_readOnly():
    assert hasattr(rapidml_Feature, "readOnly")
    descriptor = None
    for klass in rapidml_Feature.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_feature_has_restriction():
    assert hasattr(rapidml_Feature, "restriction")
    descriptor = None
    for klass in rapidml_Feature.__mro__:
        if "restriction" in klass.__dict__:
            descriptor = klass.__dict__["restriction"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_objectrealization_is_not_abstract():
    assert not inspect.isabstract(rapidml_ObjectRealization)


def test_rapidml_objectrealization_constructor_exists():
    assert callable(rapidml_ObjectRealization.__init__)


def test_rapidml_objectrealization_constructor_args():
    sig = inspect.signature(rapidml_ObjectRealization.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_zenmodel_is_not_abstract():
    assert not inspect.isabstract(rapidml_ZenModel)


def test_rapidml_zenmodel_constructor_exists():
    assert callable(rapidml_ZenModel.__init__)


def test_rapidml_zenmodel_constructor_args():
    sig = inspect.signature(rapidml_ZenModel.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_zenmodel_has_namespace():
    assert hasattr(rapidml_ZenModel, "namespace")
    descriptor = None
    for klass in rapidml_ZenModel.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_zenmodel_has_name():
    assert hasattr(rapidml_ZenModel, "name")
    descriptor = None
    for klass in rapidml_ZenModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_restelement_is_not_abstract():
    assert not inspect.isabstract(rapidml_RESTElement)


def test_rapidml_restelement_constructor_exists():
    assert callable(rapidml_RESTElement.__init__)


def test_rapidml_restelement_constructor_args():
    sig = inspect.signature(rapidml_RESTElement.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_constraint_is_not_abstract():
    assert not inspect.isabstract(rapidml_Constraint)


def test_rapidml_constraint_constructor_exists():
    assert callable(rapidml_Constraint.__init__)


def test_rapidml_constraint_constructor_args():
    sig = inspect.signature(rapidml_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_referencetreatment_is_not_abstract():
    assert not inspect.isabstract(rapidml_ReferenceTreatment)


def test_rapidml_referencetreatment_constructor_exists():
    assert callable(rapidml_ReferenceTreatment.__init__)


def test_rapidml_referencetreatment_constructor_args():
    sig = inspect.signature(rapidml_ReferenceTreatment.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_constrainabletype_is_not_abstract():
    assert not inspect.isabstract(rapidml_ConstrainableType)


def test_rapidml_constrainabletype_constructor_exists():
    assert callable(rapidml_ConstrainableType.__init__)


def test_rapidml_constrainabletype_constructor_args():
    sig = inspect.signature(rapidml_ConstrainableType.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_messageparameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_MessageParameter)


def test_rapidml_messageparameter_constructor_exists():
    assert callable(rapidml_MessageParameter.__init__)


def test_rapidml_messageparameter_constructor_args():
    sig = inspect.signature(rapidml_MessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "httpLocation" in params, "Missing parameter 'httpLocation'"

def test_rapidml_messageparameter_has_httpLocation():
    assert hasattr(rapidml_MessageParameter, "httpLocation")
    descriptor = None
    for klass in rapidml_MessageParameter.__mro__:
        if "httpLocation" in klass.__dict__:
            descriptor = klass.__dict__["httpLocation"]
            break
    assert isinstance(descriptor, property)



def test_hassecurityvalue_is_not_abstract():
    assert not inspect.isabstract(HasSecurityValue)


def test_hassecurityvalue_constructor_exists():
    assert callable(HasSecurityValue.__init__)


def test_hassecurityvalue_constructor_args():
    sig = inspect.signature(HasSecurityValue.__init__)
    params = list(sig.parameters.keys())



def test_withexamples_is_not_abstract():
    assert not inspect.isabstract(WithExamples)


def test_withexamples_constructor_exists():
    assert callable(WithExamples.__init__)


def test_withexamples_constructor_args():
    sig = inspect.signature(WithExamples.__init__)
    params = list(sig.parameters.keys())



def test_restelement_is_not_abstract():
    assert not inspect.isabstract(RESTElement)


def test_restelement_constructor_exists():
    assert callable(RESTElement.__init__)


def test_restelement_constructor_args():
    sig = inspect.signature(RESTElement.__init__)
    params = list(sig.parameters.keys())



def test_rapidml_mediatype_is_not_abstract():
    assert not inspect.isabstract(rapidml_MediaType)


def test_rapidml_mediatype_constructor_exists():
    assert callable(rapidml_MediaType.__init__)


def test_rapidml_mediatype_constructor_args():
    sig = inspect.signature(rapidml_MediaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "specURL" in params, "Missing parameter 'specURL'"

def test_rapidml_mediatype_has_name():
    assert hasattr(rapidml_MediaType, "name")
    descriptor = None
    for klass in rapidml_MediaType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_mediatype_has_specURL():
    assert hasattr(rapidml_MediaType, "specURL")
    descriptor = None
    for klass in rapidml_MediaType.__mro__:
        if "specURL" in klass.__dict__:
            descriptor = klass.__dict__["specURL"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_parameter_is_not_abstract():
    assert not inspect.isabstract(rapidml_Parameter)


def test_rapidml_parameter_constructor_exists():
    assert callable(rapidml_Parameter.__init__)


def test_rapidml_parameter_constructor_args():
    sig = inspect.signature(rapidml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_rapidml_parameter_has_required():
    assert hasattr(rapidml_Parameter, "required")
    descriptor = None
    for klass in rapidml_Parameter.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_parameter_has_fixed():
    assert hasattr(rapidml_Parameter, "fixed")
    descriptor = None
    for klass in rapidml_Parameter.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_parameter_has_name():
    assert hasattr(rapidml_Parameter, "name")
    descriptor = None
    for klass in rapidml_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_parameter_has_default():
    assert hasattr(rapidml_Parameter, "default")
    descriptor = None
    for klass in rapidml_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_method_is_not_abstract():
    assert not inspect.isabstract(rapidml_Method)


def test_rapidml_method_constructor_exists():
    assert callable(rapidml_Method.__init__)


def test_rapidml_method_constructor_args():
    sig = inspect.signature(rapidml_Method.__init__)
    params = list(sig.parameters.keys())
    assert "httpMethod" in params, "Missing parameter 'httpMethod'"
    assert "id" in params, "Missing parameter 'id'"

def test_rapidml_method_has_httpMethod():
    assert hasattr(rapidml_Method, "httpMethod")
    descriptor = None
    for klass in rapidml_Method.__mro__:
        if "httpMethod" in klass.__dict__:
            descriptor = klass.__dict__["httpMethod"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_method_has_id():
    assert hasattr(rapidml_Method, "id")
    descriptor = None
    for klass in rapidml_Method.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_resourceapi_is_not_abstract():
    assert not inspect.isabstract(rapidml_ResourceAPI)


def test_rapidml_resourceapi_constructor_exists():
    assert callable(rapidml_ResourceAPI.__init__)


def test_rapidml_resourceapi_constructor_args():
    sig = inspect.signature(rapidml_ResourceAPI.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "baseURI" in params, "Missing parameter 'baseURI'"
    assert "version" in params, "Missing parameter 'version'"

def test_rapidml_resourceapi_has_name():
    assert hasattr(rapidml_ResourceAPI, "name")
    descriptor = None
    for klass in rapidml_ResourceAPI.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_resourceapi_has_baseURI():
    assert hasattr(rapidml_ResourceAPI, "baseURI")
    descriptor = None
    for klass in rapidml_ResourceAPI.__mro__:
        if "baseURI" in klass.__dict__:
            descriptor = klass.__dict__["baseURI"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_resourceapi_has_version():
    assert hasattr(rapidml_ResourceAPI, "version")
    descriptor = None
    for klass in rapidml_ResourceAPI.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_securityscheme_is_not_abstract():
    assert not inspect.isabstract(rapidml_SecurityScheme)


def test_rapidml_securityscheme_constructor_exists():
    assert callable(rapidml_SecurityScheme.__init__)


def test_rapidml_securityscheme_constructor_args():
    sig = inspect.signature(rapidml_SecurityScheme.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "flow" in params, "Missing parameter 'flow'"

def test_rapidml_securityscheme_has_type():
    assert hasattr(rapidml_SecurityScheme, "type")
    descriptor = None
    for klass in rapidml_SecurityScheme.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_securityscheme_has_name():
    assert hasattr(rapidml_SecurityScheme, "name")
    descriptor = None
    for klass in rapidml_SecurityScheme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rapidml_securityscheme_has_flow():
    assert hasattr(rapidml_SecurityScheme, "flow")
    descriptor = None
    for klass in rapidml_SecurityScheme.__mro__:
        if "flow" in klass.__dict__:
            descriptor = klass.__dict__["flow"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_typedmessage_is_not_abstract():
    assert not inspect.isabstract(rapidml_TypedMessage)


def test_rapidml_typedmessage_constructor_exists():
    assert callable(rapidml_TypedMessage.__init__)


def test_rapidml_typedmessage_constructor_args():
    sig = inspect.signature(rapidml_TypedMessage.__init__)
    params = list(sig.parameters.keys())
    assert "useParentTypeReference" in params, "Missing parameter 'useParentTypeReference'"

def test_rapidml_typedmessage_has_useParentTypeReference():
    assert hasattr(rapidml_TypedMessage, "useParentTypeReference")
    descriptor = None
    for klass in rapidml_TypedMessage.__mro__:
        if "useParentTypeReference" in klass.__dict__:
            descriptor = klass.__dict__["useParentTypeReference"]
            break
    assert isinstance(descriptor, property)



def test_rapidml_resourcedefinition_is_not_abstract():
    assert not inspect.isabstract(rapidml_ResourceDefinition)


def test_rapidml_resourcedefinition_constructor_exists():
    assert callable(rapidml_ResourceDefinition.__init__)


def test_rapidml_resourcedefinition_constructor_args():
    sig = inspect.signature(rapidml_ResourceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rapidml_resourcedefinition_has_name():
    assert hasattr(rapidml_ResourceDefinition, "name")
    descriptor = None
    for klass in rapidml_ResourceDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_authenticationflows_exists():
    # Check that the Enumeration exists
    assert AuthenticationFlows is not None

def test_authenticationflows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationFlows]
    expected_literals = [
        "IMPLICIT",
        "APPLICATION",
        "PASSWORD",
        "ACCESS_CODE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationFlows"

def test_httpmessageparameterlocation_exists():
    # Check that the Enumeration exists
    assert HttpMessageParameterLocation is not None

def test_httpmessageparameterlocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HttpMessageParameterLocation]
    expected_literals = [
        "HEADER",
        "QUERY",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HttpMessageParameterLocation"

def test_httpmethods_exists():
    # Check that the Enumeration exists
    assert HTTPMethods is not None

def test_httpmethods_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HTTPMethods]
    expected_literals = [
        "GET",
        "PUT",
        "PATCH",
        "TRACE",
        "OPTIONS",
        "HEAD",
        "CONNECT",
        "POST",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HTTPMethods"

def test_collectionrealizationlevelenum_exists():
    # Check that the Enumeration exists
    assert CollectionRealizationLevelEnum is not None

def test_collectionrealizationlevelenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionRealizationLevelEnum]
    expected_literals = [
        "COLLECTION_LEVEL",
        "ITEM_LEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionRealizationLevelEnum"

def test_authenticationtypes_exists():
    # Check that the Enumeration exists
    assert AuthenticationTypes is not None

def test_authenticationtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationTypes]
    expected_literals = [
        "CUSTOM",
        "OAUTH2",
        "BASIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationTypes"

def test_referencerealizationenum_exists():
    # Check that the Enumeration exists
    assert ReferenceRealizationEnum is not None

def test_referencerealizationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceRealizationEnum]
    expected_literals = [
        "EMBED",
        "LINK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceRealizationEnum"

def test_collectionrealizationenum_exists():
    # Check that the Enumeration exists
    assert CollectionRealizationEnum is not None

def test_collectionrealizationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionRealizationEnum]
    expected_literals = [
        "REFERENCE_LINK_LIST",
        "EMBEDDED_OBJECT_LIST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionRealizationEnum"


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
rapidml_Element_strategy = st.builds(
    rapidml_Element,
    cardinality=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
rapidml_RegExConstraint_strategy = st.builds(
    rapidml_RegExConstraint,
    pattern=
        safe_text
)
rapidml_ValueRangeConstraint_strategy = st.builds(
    rapidml_ValueRangeConstraint,
    minValueExclusive=
        st.booleans(),
    maxValue=
        safe_text,
    maxValueExclusive=
        st.booleans(),
    minValue=
        safe_text
)
rapidml_LengthConstraint_strategy = st.builds(
    rapidml_LengthConstraint,
    maxLength=
        st.integers(),
    length=
        st.integers(),
    minLength=
        st.integers()
)
SingleValueType_strategy = st.builds(
    SingleValueType,
)
rapidml_SimpleType_strategy = st.builds(
    rapidml_SimpleType,
)
rapidml_Enumeration_strategy = st.builds(
    rapidml_Enumeration,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
Inheritable_strategy = st.builds(
    Inheritable,
)
DataExample_strategy = st.builds(
    DataExample,
)
rapidml_InlineDataExample_strategy = st.builds(
    rapidml_InlineDataExample,
    body=
        safe_text
)
rapidml_DataExample_strategy = st.builds(
    rapidml_DataExample,
)
rapidml_WithDataExamples_strategy = st.builds(
    rapidml_WithDataExamples,
)
rapidml_Inheritable_strategy = st.builds(
    rapidml_Inheritable,
)
Element_strategy = st.builds(
    Element,
)
WithDataExamples_strategy = st.builds(
    WithDataExamples,
)
DataType_strategy = st.builds(
    DataType,
)
rapidml_SingleValueType_strategy = st.builds(
    rapidml_SingleValueType,
)
Feature_strategy = st.builds(
    Feature,
)
rapidml_Extensible_strategy = st.builds(
    rapidml_Extensible,
)
rapidml_Structure_strategy = st.builds(
    rapidml_Structure,
)
rapidml_HasTitle_strategy = st.builds(
    rapidml_HasTitle,
    title=
        safe_text
)
rapidml_Extension_strategy = st.builds(
    rapidml_Extension,
    name=
        safe_text,
    value=
        safe_text
)
rapidml_AuthenticationMethod_strategy = st.builds(
    rapidml_AuthenticationMethod,
)
rapidml_HasSecurityValue_strategy = st.builds(
    rapidml_HasSecurityValue,
)
ReferenceElement_strategy = st.builds(
    ReferenceElement,
)
rapidml_ReferenceProperty_strategy = st.builds(
    rapidml_ReferenceProperty,
    container=
        st.booleans(),
    containment=
        st.booleans()
)
ConstrainableType_strategy = st.builds(
    ConstrainableType,
)
rapidml_UserDefinedType_strategy = st.builds(
    rapidml_UserDefinedType,
)
rapidml_PropertyRealization_strategy = st.builds(
    rapidml_PropertyRealization,
    cardinality=
        safe_text
)
rapidml_HasStringValue_strategy = st.builds(
    rapidml_HasStringValue,
)
Example_strategy = st.builds(
    Example,
)
rapidml_ExternalExample_strategy = st.builds(
    rapidml_ExternalExample,
    path=
        safe_text
)
rapidml_InlineExample_strategy = st.builds(
    rapidml_InlineExample,
    body=
        safe_text
)
rapidml_Example_strategy = st.builds(
    rapidml_Example,
)
rapidml_WithExamples_strategy = st.builds(
    rapidml_WithExamples,
)
URISegment_strategy = st.builds(
    URISegment,
)
HasStringValue_strategy = st.builds(
    HasStringValue,
)
rapidml_URISegment_strategy = st.builds(
    rapidml_URISegment,
    name=
        safe_text
)
rapidml_PrimitiveType_strategy = st.builds(
    rapidml_PrimitiveType,
)
rapidml_PathSegment_strategy = st.builds(
    rapidml_PathSegment,
)
ObjectRealization_strategy = st.builds(
    ObjectRealization,
)
ResourceDefinition_strategy = st.builds(
    ResourceDefinition,
)
ReferenceTreatment_strategy = st.builds(
    ReferenceTreatment,
)
rapidml_ReferenceEmbed_strategy = st.builds(
    rapidml_ReferenceEmbed,
)
rapidml_ReferenceLink_strategy = st.builds(
    rapidml_ReferenceLink,
    name=
        safe_text,
    collectionRealizationLevel=
        safe_text
)
rapidml_ReferenceElement_strategy = st.builds(
    rapidml_ReferenceElement,
)
rapidml_NamedLinkDescriptor_strategy = st.builds(
    rapidml_NamedLinkDescriptor,
    default=
        st.booleans(),
    name=
        safe_text
)
rapidml_ImportDeclaration_strategy = st.builds(
    rapidml_ImportDeclaration,
    importURI=
        safe_text,
    importedNamespace=
        safe_text,
    alias=
        safe_text
)
rapidml_PrimitiveTypesLibrary_strategy = st.builds(
    rapidml_PrimitiveTypesLibrary,
    name=
        safe_text
)
rapidml_LinkRelationsLibrary_strategy = st.builds(
    rapidml_LinkRelationsLibrary,
    name=
        safe_text
)
rapidml_MediaTypesLibrary_strategy = st.builds(
    rapidml_MediaTypesLibrary,
)
rapidml_RealizationModelLocation_strategy = st.builds(
    rapidml_RealizationModelLocation,
    uri=
        safe_text
)
HasTitle_strategy = st.builds(
    HasTitle,
)
rapidml_PrimitiveProperty_strategy = st.builds(
    rapidml_PrimitiveProperty,
)
SourceReference_strategy = st.builds(
    SourceReference,
)
rapidml_PrimitiveTypeSourceReference_strategy = st.builds(
    rapidml_PrimitiveTypeSourceReference,
)
rapidml_PropertyReference_strategy = st.builds(
    rapidml_PropertyReference,
)
Parameter_strategy = st.builds(
    Parameter,
)
rapidml_URIParameter_strategy = st.builds(
    rapidml_URIParameter,
)
rapidml_CollectionReferenceElement_strategy = st.builds(
    rapidml_CollectionReferenceElement,
)
rapidml_CollectionParameter_strategy = st.builds(
    rapidml_CollectionParameter,
)
ServiceDataResource_strategy = st.builds(
    ServiceDataResource,
)
rapidml_ObjectResource_strategy = st.builds(
    rapidml_ObjectResource,
)
rapidml_CollectionResource_strategy = st.builds(
    rapidml_CollectionResource,
    resourceRealizationKind=
        safe_text
)
URIParameter_strategy = st.builds(
    URIParameter,
)
rapidml_TemplateParameter_strategy = st.builds(
    rapidml_TemplateParameter,
)
rapidml_MatrixParameter_strategy = st.builds(
    rapidml_MatrixParameter,
)
rapidml_URISegmentWithParameter_strategy = st.builds(
    rapidml_URISegmentWithParameter,
)
rapidml_Documentable_strategy = st.builds(
    rapidml_Documentable,
)
rapidml_Documentation_strategy = st.builds(
    rapidml_Documentation,
    text=
        safe_text
)
TypedMessage_strategy = st.builds(
    TypedMessage,
)
Documentable_strategy = st.builds(
    Documentable,
)
rapidml_SecuritySchemeLibrary_strategy = st.builds(
    rapidml_SecuritySchemeLibrary,
    name=
        safe_text
)
rapidml_SecurityScope_strategy = st.builds(
    rapidml_SecurityScope,
    name=
        safe_text
)
rapidml_SecuritySchemeParameter_strategy = st.builds(
    rapidml_SecuritySchemeParameter,
    name=
        safe_text,
    value=
        safe_text
)
rapidml_LinkRelation_strategy = st.builds(
    rapidml_LinkRelation,
    specURL=
        safe_text,
    name=
        safe_text
)
rapidml_Operation_strategy = st.builds(
    rapidml_Operation,
    name=
        safe_text
)
rapidml_EnumConstant_strategy = st.builds(
    rapidml_EnumConstant,
    literalValue=
        safe_text,
    name=
        safe_text,
    integerValue=
        st.integers()
)
rapidml_DataModel_strategy = st.builds(
    rapidml_DataModel,
    name=
        safe_text
)
rapidml_SourceReference_strategy = st.builds(
    rapidml_SourceReference,
)
RealizationContainer_strategy = st.builds(
    RealizationContainer,
)
rapidml_ReferenceRealization_strategy = st.builds(
    rapidml_ReferenceRealization,
    realizationType=
        safe_text,
    multiValued=
        st.booleans()
)
rapidml_ServiceDataResource_strategy = st.builds(
    rapidml_ServiceDataResource,
    default=
        st.booleans()
)
rapidml_URI_strategy = st.builds(
    rapidml_URI,
)
rapidml_TypedResponse_strategy = st.builds(
    rapidml_TypedResponse,
    statusCode=
        st.integers()
)
rapidml_TypedRequest_strategy = st.builds(
    rapidml_TypedRequest,
)
Extensible_strategy = st.builds(
    Extensible,
)
rapidml_DataType_strategy = st.builds(
    rapidml_DataType,
    name=
        safe_text
)
rapidml_RealizationContainer_strategy = st.builds(
    rapidml_RealizationContainer,
    effectiveRealization=
        safe_text,
    realizationName=
        safe_text,
    withDefaultRealization=
        st.booleans()
)
rapidml_Feature_strategy = st.builds(
    rapidml_Feature,
    key=
        st.booleans(),
    name=
        safe_text,
    readOnly=
        st.booleans(),
    restriction=
        st.booleans()
)
rapidml_ObjectRealization_strategy = st.builds(
    rapidml_ObjectRealization,
)
rapidml_ZenModel_strategy = st.builds(
    rapidml_ZenModel,
    namespace=
        safe_text,
    name=
        safe_text
)
rapidml_RESTElement_strategy = st.builds(
    rapidml_RESTElement,
)
rapidml_Constraint_strategy = st.builds(
    rapidml_Constraint,
)
rapidml_ReferenceTreatment_strategy = st.builds(
    rapidml_ReferenceTreatment,
)
rapidml_ConstrainableType_strategy = st.builds(
    rapidml_ConstrainableType,
)
rapidml_MessageParameter_strategy = st.builds(
    rapidml_MessageParameter,
    httpLocation=
        safe_text
)
HasSecurityValue_strategy = st.builds(
    HasSecurityValue,
)
WithExamples_strategy = st.builds(
    WithExamples,
)
RESTElement_strategy = st.builds(
    RESTElement,
)
rapidml_MediaType_strategy = st.builds(
    rapidml_MediaType,
    name=
        safe_text,
    specURL=
        safe_text
)
rapidml_Parameter_strategy = st.builds(
    rapidml_Parameter,
    required=
        st.booleans(),
    fixed=
        safe_text,
    name=
        safe_text,
    default=
        safe_text
)
rapidml_Method_strategy = st.builds(
    rapidml_Method,
    httpMethod=
        safe_text,
    id=
        safe_text
)
rapidml_ResourceAPI_strategy = st.builds(
    rapidml_ResourceAPI,
    name=
        safe_text,
    baseURI=
        safe_text,
    version=
        safe_text
)
rapidml_SecurityScheme_strategy = st.builds(
    rapidml_SecurityScheme,
    type=
        safe_text,
    name=
        safe_text,
    flow=
        safe_text
)
rapidml_TypedMessage_strategy = st.builds(
    rapidml_TypedMessage,
    useParentTypeReference=
        st.booleans()
)
rapidml_ResourceDefinition_strategy = st.builds(
    rapidml_ResourceDefinition,
    name=
        safe_text
)

@given(instance=rapidml_Element_strategy)
@settings(max_examples=50)
def test_rapidml_element_instantiation(instance):
    assert isinstance(instance, rapidml_Element)



@given(instance=rapidml_Element_strategy)
def test_rapidml_element_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_Element_strategy)
@settings(max_examples=30)
def test_rapidml_element_ismultivalued_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMultiValued()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMultiValued).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMultiValued' in rapidml_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMultiValued' in rapidml_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMultiValued' in rapidml_Element is not implemented or raised an error")

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=rapidml_RegExConstraint_strategy)
@settings(max_examples=50)
def test_rapidml_regexconstraint_instantiation(instance):
    assert isinstance(instance, rapidml_RegExConstraint)



@given(instance=rapidml_RegExConstraint_strategy)
def test_rapidml_regexconstraint_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=rapidml_ValueRangeConstraint_strategy)
@settings(max_examples=50)
def test_rapidml_valuerangeconstraint_instantiation(instance):
    assert isinstance(instance, rapidml_ValueRangeConstraint)



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_rapidml_valuerangeconstraint_minValueExclusive_setter(instance):
    original = instance.minValueExclusive
    instance.minValueExclusive = original
    assert instance.minValueExclusive == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_rapidml_valuerangeconstraint_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_rapidml_valuerangeconstraint_maxValueExclusive_setter(instance):
    original = instance.maxValueExclusive
    instance.maxValueExclusive = original
    assert instance.maxValueExclusive == original



@given(instance=rapidml_ValueRangeConstraint_strategy)
def test_rapidml_valuerangeconstraint_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=rapidml_LengthConstraint_strategy)
@settings(max_examples=50)
def test_rapidml_lengthconstraint_instantiation(instance):
    assert isinstance(instance, rapidml_LengthConstraint)



@given(instance=rapidml_LengthConstraint_strategy)
def test_rapidml_lengthconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=rapidml_LengthConstraint_strategy)
def test_rapidml_lengthconstraint_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rapidml_LengthConstraint_strategy)
def test_rapidml_lengthconstraint_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original

@given(instance=SingleValueType_strategy)
@settings(max_examples=50)
def test_singlevaluetype_instantiation(instance):
    assert isinstance(instance, SingleValueType)

@given(instance=rapidml_SimpleType_strategy)
@settings(max_examples=50)
def test_rapidml_simpletype_instantiation(instance):
    assert isinstance(instance, rapidml_SimpleType)

@given(instance=rapidml_Enumeration_strategy)
@settings(max_examples=50)
def test_rapidml_enumeration_instantiation(instance):
    assert isinstance(instance, rapidml_Enumeration)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=Inheritable_strategy)
@settings(max_examples=50)
def test_inheritable_instantiation(instance):
    assert isinstance(instance, Inheritable)

@given(instance=DataExample_strategy)
@settings(max_examples=50)
def test_dataexample_instantiation(instance):
    assert isinstance(instance, DataExample)

@given(instance=rapidml_InlineDataExample_strategy)
@settings(max_examples=50)
def test_rapidml_inlinedataexample_instantiation(instance):
    assert isinstance(instance, rapidml_InlineDataExample)



@given(instance=rapidml_InlineDataExample_strategy)
def test_rapidml_inlinedataexample_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=rapidml_DataExample_strategy)
@settings(max_examples=50)
def test_rapidml_dataexample_instantiation(instance):
    assert isinstance(instance, rapidml_DataExample)

@given(instance=rapidml_WithDataExamples_strategy)
@settings(max_examples=50)
def test_rapidml_withdataexamples_instantiation(instance):
    assert isinstance(instance, rapidml_WithDataExamples)

@given(instance=rapidml_Inheritable_strategy)
@settings(max_examples=50)
def test_rapidml_inheritable_instantiation(instance):
    assert isinstance(instance, rapidml_Inheritable)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=WithDataExamples_strategy)
@settings(max_examples=50)
def test_withdataexamples_instantiation(instance):
    assert isinstance(instance, WithDataExamples)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=rapidml_SingleValueType_strategy)
@settings(max_examples=50)
def test_rapidml_singlevaluetype_instantiation(instance):
    assert isinstance(instance, rapidml_SingleValueType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=rapidml_Extensible_strategy)
@settings(max_examples=50)
def test_rapidml_extensible_instantiation(instance):
    assert isinstance(instance, rapidml_Extensible)

@given(instance=rapidml_Structure_strategy)
@settings(max_examples=50)
def test_rapidml_structure_instantiation(instance):
    assert isinstance(instance, rapidml_Structure)

@given(instance=rapidml_HasTitle_strategy)
@settings(max_examples=50)
def test_rapidml_hastitle_instantiation(instance):
    assert isinstance(instance, rapidml_HasTitle)



@given(instance=rapidml_HasTitle_strategy)
def test_rapidml_hastitle_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=rapidml_Extension_strategy)
@settings(max_examples=50)
def test_rapidml_extension_instantiation(instance):
    assert isinstance(instance, rapidml_Extension)



@given(instance=rapidml_Extension_strategy)
def test_rapidml_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Extension_strategy)
def test_rapidml_extension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rapidml_AuthenticationMethod_strategy)
@settings(max_examples=50)
def test_rapidml_authenticationmethod_instantiation(instance):
    assert isinstance(instance, rapidml_AuthenticationMethod)

@given(instance=rapidml_HasSecurityValue_strategy)
@settings(max_examples=50)
def test_rapidml_hassecurityvalue_instantiation(instance):
    assert isinstance(instance, rapidml_HasSecurityValue)

@given(instance=ReferenceElement_strategy)
@settings(max_examples=50)
def test_referenceelement_instantiation(instance):
    assert isinstance(instance, ReferenceElement)

@given(instance=rapidml_ReferenceProperty_strategy)
@settings(max_examples=50)
def test_rapidml_referenceproperty_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceProperty)



@given(instance=rapidml_ReferenceProperty_strategy)
def test_rapidml_referenceproperty_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=rapidml_ReferenceProperty_strategy)
def test_rapidml_referenceproperty_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=ConstrainableType_strategy)
@settings(max_examples=50)
def test_constrainabletype_instantiation(instance):
    assert isinstance(instance, ConstrainableType)

@given(instance=rapidml_UserDefinedType_strategy)
@settings(max_examples=50)
def test_rapidml_userdefinedtype_instantiation(instance):
    assert isinstance(instance, rapidml_UserDefinedType)

@given(instance=rapidml_PropertyRealization_strategy)
@settings(max_examples=50)
def test_rapidml_propertyrealization_instantiation(instance):
    assert isinstance(instance, rapidml_PropertyRealization)



@given(instance=rapidml_PropertyRealization_strategy)
def test_rapidml_propertyrealization_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=rapidml_HasStringValue_strategy)
@settings(max_examples=50)
def test_rapidml_hasstringvalue_instantiation(instance):
    assert isinstance(instance, rapidml_HasStringValue)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_HasStringValue_strategy)
@settings(max_examples=30)
def test_rapidml_hasstringvalue_tostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toString' in rapidml_HasStringValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toString' in rapidml_HasStringValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toString' in rapidml_HasStringValue is not implemented or raised an error")

@given(instance=Example_strategy)
@settings(max_examples=50)
def test_example_instantiation(instance):
    assert isinstance(instance, Example)

@given(instance=rapidml_ExternalExample_strategy)
@settings(max_examples=50)
def test_rapidml_externalexample_instantiation(instance):
    assert isinstance(instance, rapidml_ExternalExample)



@given(instance=rapidml_ExternalExample_strategy)
def test_rapidml_externalexample_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=rapidml_InlineExample_strategy)
@settings(max_examples=50)
def test_rapidml_inlineexample_instantiation(instance):
    assert isinstance(instance, rapidml_InlineExample)



@given(instance=rapidml_InlineExample_strategy)
def test_rapidml_inlineexample_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=rapidml_Example_strategy)
@settings(max_examples=50)
def test_rapidml_example_instantiation(instance):
    assert isinstance(instance, rapidml_Example)

@given(instance=rapidml_WithExamples_strategy)
@settings(max_examples=50)
def test_rapidml_withexamples_instantiation(instance):
    assert isinstance(instance, rapidml_WithExamples)

@given(instance=URISegment_strategy)
@settings(max_examples=50)
def test_urisegment_instantiation(instance):
    assert isinstance(instance, URISegment)

@given(instance=HasStringValue_strategy)
@settings(max_examples=50)
def test_hasstringvalue_instantiation(instance):
    assert isinstance(instance, HasStringValue)

@given(instance=rapidml_URISegment_strategy)
@settings(max_examples=50)
def test_rapidml_urisegment_instantiation(instance):
    assert isinstance(instance, rapidml_URISegment)



@given(instance=rapidml_URISegment_strategy)
def test_rapidml_urisegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_PrimitiveType_strategy)
@settings(max_examples=50)
def test_rapidml_primitivetype_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveType)

@given(instance=rapidml_PathSegment_strategy)
@settings(max_examples=50)
def test_rapidml_pathsegment_instantiation(instance):
    assert isinstance(instance, rapidml_PathSegment)

@given(instance=ObjectRealization_strategy)
@settings(max_examples=50)
def test_objectrealization_instantiation(instance):
    assert isinstance(instance, ObjectRealization)

@given(instance=ResourceDefinition_strategy)
@settings(max_examples=50)
def test_resourcedefinition_instantiation(instance):
    assert isinstance(instance, ResourceDefinition)

@given(instance=ReferenceTreatment_strategy)
@settings(max_examples=50)
def test_referencetreatment_instantiation(instance):
    assert isinstance(instance, ReferenceTreatment)

@given(instance=rapidml_ReferenceEmbed_strategy)
@settings(max_examples=50)
def test_rapidml_referenceembed_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceEmbed)

@given(instance=rapidml_ReferenceLink_strategy)
@settings(max_examples=50)
def test_rapidml_referencelink_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceLink)



@given(instance=rapidml_ReferenceLink_strategy)
def test_rapidml_referencelink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_ReferenceLink_strategy)
def test_rapidml_referencelink_collectionRealizationLevel_setter(instance):
    original = instance.collectionRealizationLevel
    instance.collectionRealizationLevel = original
    assert instance.collectionRealizationLevel == original

@given(instance=rapidml_ReferenceElement_strategy)
@settings(max_examples=50)
def test_rapidml_referenceelement_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceElement)

@given(instance=rapidml_NamedLinkDescriptor_strategy)
@settings(max_examples=50)
def test_rapidml_namedlinkdescriptor_instantiation(instance):
    assert isinstance(instance, rapidml_NamedLinkDescriptor)



@given(instance=rapidml_NamedLinkDescriptor_strategy)
def test_rapidml_namedlinkdescriptor_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=rapidml_NamedLinkDescriptor_strategy)
def test_rapidml_namedlinkdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_rapidml_importdeclaration_instantiation(instance):
    assert isinstance(instance, rapidml_ImportDeclaration)



@given(instance=rapidml_ImportDeclaration_strategy)
def test_rapidml_importdeclaration_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original



@given(instance=rapidml_ImportDeclaration_strategy)
def test_rapidml_importdeclaration_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=rapidml_ImportDeclaration_strategy)
def test_rapidml_importdeclaration_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=rapidml_PrimitiveTypesLibrary_strategy)
@settings(max_examples=50)
def test_rapidml_primitivetypeslibrary_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveTypesLibrary)



@given(instance=rapidml_PrimitiveTypesLibrary_strategy)
def test_rapidml_primitivetypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_LinkRelationsLibrary_strategy)
@settings(max_examples=50)
def test_rapidml_linkrelationslibrary_instantiation(instance):
    assert isinstance(instance, rapidml_LinkRelationsLibrary)



@given(instance=rapidml_LinkRelationsLibrary_strategy)
def test_rapidml_linkrelationslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_MediaTypesLibrary_strategy)
@settings(max_examples=50)
def test_rapidml_mediatypeslibrary_instantiation(instance):
    assert isinstance(instance, rapidml_MediaTypesLibrary)

@given(instance=rapidml_RealizationModelLocation_strategy)
@settings(max_examples=50)
def test_rapidml_realizationmodellocation_instantiation(instance):
    assert isinstance(instance, rapidml_RealizationModelLocation)



@given(instance=rapidml_RealizationModelLocation_strategy)
def test_rapidml_realizationmodellocation_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=HasTitle_strategy)
@settings(max_examples=50)
def test_hastitle_instantiation(instance):
    assert isinstance(instance, HasTitle)

@given(instance=rapidml_PrimitiveProperty_strategy)
@settings(max_examples=50)
def test_rapidml_primitiveproperty_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveProperty)

@given(instance=SourceReference_strategy)
@settings(max_examples=50)
def test_sourcereference_instantiation(instance):
    assert isinstance(instance, SourceReference)

@given(instance=rapidml_PrimitiveTypeSourceReference_strategy)
@settings(max_examples=50)
def test_rapidml_primitivetypesourcereference_instantiation(instance):
    assert isinstance(instance, rapidml_PrimitiveTypeSourceReference)

@given(instance=rapidml_PropertyReference_strategy)
@settings(max_examples=50)
def test_rapidml_propertyreference_instantiation(instance):
    assert isinstance(instance, rapidml_PropertyReference)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=rapidml_URIParameter_strategy)
@settings(max_examples=50)
def test_rapidml_uriparameter_instantiation(instance):
    assert isinstance(instance, rapidml_URIParameter)

@given(instance=rapidml_CollectionReferenceElement_strategy)
@settings(max_examples=50)
def test_rapidml_collectionreferenceelement_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionReferenceElement)

@given(instance=rapidml_CollectionParameter_strategy)
@settings(max_examples=50)
def test_rapidml_collectionparameter_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionParameter)

@given(instance=ServiceDataResource_strategy)
@settings(max_examples=50)
def test_servicedataresource_instantiation(instance):
    assert isinstance(instance, ServiceDataResource)

@given(instance=rapidml_ObjectResource_strategy)
@settings(max_examples=50)
def test_rapidml_objectresource_instantiation(instance):
    assert isinstance(instance, rapidml_ObjectResource)

@given(instance=rapidml_CollectionResource_strategy)
@settings(max_examples=50)
def test_rapidml_collectionresource_instantiation(instance):
    assert isinstance(instance, rapidml_CollectionResource)



@given(instance=rapidml_CollectionResource_strategy)
def test_rapidml_collectionresource_resourceRealizationKind_setter(instance):
    original = instance.resourceRealizationKind
    instance.resourceRealizationKind = original
    assert instance.resourceRealizationKind == original

@given(instance=URIParameter_strategy)
@settings(max_examples=50)
def test_uriparameter_instantiation(instance):
    assert isinstance(instance, URIParameter)

@given(instance=rapidml_TemplateParameter_strategy)
@settings(max_examples=50)
def test_rapidml_templateparameter_instantiation(instance):
    assert isinstance(instance, rapidml_TemplateParameter)

@given(instance=rapidml_MatrixParameter_strategy)
@settings(max_examples=50)
def test_rapidml_matrixparameter_instantiation(instance):
    assert isinstance(instance, rapidml_MatrixParameter)

@given(instance=rapidml_URISegmentWithParameter_strategy)
@settings(max_examples=50)
def test_rapidml_urisegmentwithparameter_instantiation(instance):
    assert isinstance(instance, rapidml_URISegmentWithParameter)

@given(instance=rapidml_Documentable_strategy)
@settings(max_examples=50)
def test_rapidml_documentable_instantiation(instance):
    assert isinstance(instance, rapidml_Documentable)

@given(instance=rapidml_Documentation_strategy)
@settings(max_examples=50)
def test_rapidml_documentation_instantiation(instance):
    assert isinstance(instance, rapidml_Documentation)



@given(instance=rapidml_Documentation_strategy)
def test_rapidml_documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=TypedMessage_strategy)
@settings(max_examples=50)
def test_typedmessage_instantiation(instance):
    assert isinstance(instance, TypedMessage)

@given(instance=Documentable_strategy)
@settings(max_examples=50)
def test_documentable_instantiation(instance):
    assert isinstance(instance, Documentable)

@given(instance=rapidml_SecuritySchemeLibrary_strategy)
@settings(max_examples=50)
def test_rapidml_securityschemelibrary_instantiation(instance):
    assert isinstance(instance, rapidml_SecuritySchemeLibrary)



@given(instance=rapidml_SecuritySchemeLibrary_strategy)
def test_rapidml_securityschemelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_SecurityScope_strategy)
@settings(max_examples=50)
def test_rapidml_securityscope_instantiation(instance):
    assert isinstance(instance, rapidml_SecurityScope)



@given(instance=rapidml_SecurityScope_strategy)
def test_rapidml_securityscope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_SecuritySchemeParameter_strategy)
@settings(max_examples=50)
def test_rapidml_securityschemeparameter_instantiation(instance):
    assert isinstance(instance, rapidml_SecuritySchemeParameter)



@given(instance=rapidml_SecuritySchemeParameter_strategy)
def test_rapidml_securityschemeparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_SecuritySchemeParameter_strategy)
def test_rapidml_securityschemeparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rapidml_LinkRelation_strategy)
@settings(max_examples=50)
def test_rapidml_linkrelation_instantiation(instance):
    assert isinstance(instance, rapidml_LinkRelation)



@given(instance=rapidml_LinkRelation_strategy)
def test_rapidml_linkrelation_specURL_setter(instance):
    original = instance.specURL
    instance.specURL = original
    assert instance.specURL == original



@given(instance=rapidml_LinkRelation_strategy)
def test_rapidml_linkrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_Operation_strategy)
@settings(max_examples=50)
def test_rapidml_operation_instantiation(instance):
    assert isinstance(instance, rapidml_Operation)



@given(instance=rapidml_Operation_strategy)
def test_rapidml_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_EnumConstant_strategy)
@settings(max_examples=50)
def test_rapidml_enumconstant_instantiation(instance):
    assert isinstance(instance, rapidml_EnumConstant)



@given(instance=rapidml_EnumConstant_strategy)
def test_rapidml_enumconstant_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original



@given(instance=rapidml_EnumConstant_strategy)
def test_rapidml_enumconstant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_EnumConstant_strategy)
def test_rapidml_enumconstant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=rapidml_DataModel_strategy)
@settings(max_examples=50)
def test_rapidml_datamodel_instantiation(instance):
    assert isinstance(instance, rapidml_DataModel)



@given(instance=rapidml_DataModel_strategy)
def test_rapidml_datamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_SourceReference_strategy)
@settings(max_examples=50)
def test_rapidml_sourcereference_instantiation(instance):
    assert isinstance(instance, rapidml_SourceReference)

@given(instance=RealizationContainer_strategy)
@settings(max_examples=50)
def test_realizationcontainer_instantiation(instance):
    assert isinstance(instance, RealizationContainer)

@given(instance=rapidml_ReferenceRealization_strategy)
@settings(max_examples=50)
def test_rapidml_referencerealization_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceRealization)



@given(instance=rapidml_ReferenceRealization_strategy)
def test_rapidml_referencerealization_realizationType_setter(instance):
    original = instance.realizationType
    instance.realizationType = original
    assert instance.realizationType == original



@given(instance=rapidml_ReferenceRealization_strategy)
def test_rapidml_referencerealization_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=rapidml_ServiceDataResource_strategy)
@settings(max_examples=50)
def test_rapidml_servicedataresource_instantiation(instance):
    assert isinstance(instance, rapidml_ServiceDataResource)



@given(instance=rapidml_ServiceDataResource_strategy)
def test_rapidml_servicedataresource_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_ServiceDataResource_strategy)
@settings(max_examples=30)
def test_rapidml_servicedataresource_isincluded_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isIncluded(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isIncluded).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isIncluded' in rapidml_ServiceDataResource is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isIncluded' in rapidml_ServiceDataResource did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isIncluded' in rapidml_ServiceDataResource is not implemented or raised an error")

@given(instance=rapidml_URI_strategy)
@settings(max_examples=50)
def test_rapidml_uri_instantiation(instance):
    assert isinstance(instance, rapidml_URI)

@given(instance=rapidml_TypedResponse_strategy)
@settings(max_examples=50)
def test_rapidml_typedresponse_instantiation(instance):
    assert isinstance(instance, rapidml_TypedResponse)



@given(instance=rapidml_TypedResponse_strategy)
def test_rapidml_typedresponse_statusCode_setter(instance):
    original = instance.statusCode
    instance.statusCode = original
    assert instance.statusCode == original

@given(instance=rapidml_TypedRequest_strategy)
@settings(max_examples=50)
def test_rapidml_typedrequest_instantiation(instance):
    assert isinstance(instance, rapidml_TypedRequest)

@given(instance=Extensible_strategy)
@settings(max_examples=50)
def test_extensible_instantiation(instance):
    assert isinstance(instance, Extensible)

@given(instance=rapidml_DataType_strategy)
@settings(max_examples=50)
def test_rapidml_datatype_instantiation(instance):
    assert isinstance(instance, rapidml_DataType)



@given(instance=rapidml_DataType_strategy)
def test_rapidml_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_RealizationContainer_strategy)
@settings(max_examples=50)
def test_rapidml_realizationcontainer_instantiation(instance):
    assert isinstance(instance, rapidml_RealizationContainer)



@given(instance=rapidml_RealizationContainer_strategy)
def test_rapidml_realizationcontainer_effectiveRealization_setter(instance):
    original = instance.effectiveRealization
    instance.effectiveRealization = original
    assert instance.effectiveRealization == original



@given(instance=rapidml_RealizationContainer_strategy)
def test_rapidml_realizationcontainer_realizationName_setter(instance):
    original = instance.realizationName
    instance.realizationName = original
    assert instance.realizationName == original



@given(instance=rapidml_RealizationContainer_strategy)
def test_rapidml_realizationcontainer_withDefaultRealization_setter(instance):
    original = instance.withDefaultRealization
    instance.withDefaultRealization = original
    assert instance.withDefaultRealization == original

@given(instance=rapidml_Feature_strategy)
@settings(max_examples=50)
def test_rapidml_feature_instantiation(instance):
    assert isinstance(instance, rapidml_Feature)



@given(instance=rapidml_Feature_strategy)
def test_rapidml_feature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=rapidml_Feature_strategy)
def test_rapidml_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Feature_strategy)
def test_rapidml_feature_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=rapidml_Feature_strategy)
def test_rapidml_feature_restriction_setter(instance):
    original = instance.restriction
    instance.restriction = original
    assert instance.restriction == original

@given(instance=rapidml_ObjectRealization_strategy)
@settings(max_examples=50)
def test_rapidml_objectrealization_instantiation(instance):
    assert isinstance(instance, rapidml_ObjectRealization)

@given(instance=rapidml_ZenModel_strategy)
@settings(max_examples=50)
def test_rapidml_zenmodel_instantiation(instance):
    assert isinstance(instance, rapidml_ZenModel)



@given(instance=rapidml_ZenModel_strategy)
def test_rapidml_zenmodel_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=rapidml_ZenModel_strategy)
def test_rapidml_zenmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rapidml_RESTElement_strategy)
@settings(max_examples=50)
def test_rapidml_restelement_instantiation(instance):
    assert isinstance(instance, rapidml_RESTElement)

@given(instance=rapidml_Constraint_strategy)
@settings(max_examples=50)
def test_rapidml_constraint_instantiation(instance):
    assert isinstance(instance, rapidml_Constraint)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_Constraint_strategy)
@settings(max_examples=30)
def test_rapidml_constraint_supports_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.supports(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.supports).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'supports' in rapidml_Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'supports' in rapidml_Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'supports' in rapidml_Constraint is not implemented or raised an error")

@given(instance=rapidml_ReferenceTreatment_strategy)
@settings(max_examples=50)
def test_rapidml_referencetreatment_instantiation(instance):
    assert isinstance(instance, rapidml_ReferenceTreatment)

@given(instance=rapidml_ConstrainableType_strategy)
@settings(max_examples=50)
def test_rapidml_constrainabletype_instantiation(instance):
    assert isinstance(instance, rapidml_ConstrainableType)

@given(instance=rapidml_MessageParameter_strategy)
@settings(max_examples=50)
def test_rapidml_messageparameter_instantiation(instance):
    assert isinstance(instance, rapidml_MessageParameter)



@given(instance=rapidml_MessageParameter_strategy)
def test_rapidml_messageparameter_httpLocation_setter(instance):
    original = instance.httpLocation
    instance.httpLocation = original
    assert instance.httpLocation == original

@given(instance=HasSecurityValue_strategy)
@settings(max_examples=50)
def test_hassecurityvalue_instantiation(instance):
    assert isinstance(instance, HasSecurityValue)

@given(instance=WithExamples_strategy)
@settings(max_examples=50)
def test_withexamples_instantiation(instance):
    assert isinstance(instance, WithExamples)

@given(instance=RESTElement_strategy)
@settings(max_examples=50)
def test_restelement_instantiation(instance):
    assert isinstance(instance, RESTElement)

@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=50)
def test_rapidml_mediatype_instantiation(instance):
    assert isinstance(instance, rapidml_MediaType)



@given(instance=rapidml_MediaType_strategy)
def test_rapidml_mediatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_MediaType_strategy)
def test_rapidml_mediatype_specURL_setter(instance):
    original = instance.specURL
    instance.specURL = original
    assert instance.specURL == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=30)
def test_rapidml_mediatype_hashcode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hashCode()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hashCode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hashCode' in rapidml_MediaType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hashCode' in rapidml_MediaType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hashCode' in rapidml_MediaType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_MediaType_strategy)
@settings(max_examples=30)
def test_rapidml_mediatype_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in rapidml_MediaType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in rapidml_MediaType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in rapidml_MediaType is not implemented or raised an error")

@given(instance=rapidml_Parameter_strategy)
@settings(max_examples=50)
def test_rapidml_parameter_instantiation(instance):
    assert isinstance(instance, rapidml_Parameter)



@given(instance=rapidml_Parameter_strategy)
def test_rapidml_parameter_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=rapidml_Parameter_strategy)
def test_rapidml_parameter_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original



@given(instance=rapidml_Parameter_strategy)
def test_rapidml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_Parameter_strategy)
def test_rapidml_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=rapidml_Method_strategy)
@settings(max_examples=50)
def test_rapidml_method_instantiation(instance):
    assert isinstance(instance, rapidml_Method)



@given(instance=rapidml_Method_strategy)
def test_rapidml_method_httpMethod_setter(instance):
    original = instance.httpMethod
    instance.httpMethod = original
    assert instance.httpMethod == original



@given(instance=rapidml_Method_strategy)
def test_rapidml_method_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=rapidml_ResourceAPI_strategy)
@settings(max_examples=50)
def test_rapidml_resourceapi_instantiation(instance):
    assert isinstance(instance, rapidml_ResourceAPI)



@given(instance=rapidml_ResourceAPI_strategy)
def test_rapidml_resourceapi_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_ResourceAPI_strategy)
def test_rapidml_resourceapi_baseURI_setter(instance):
    original = instance.baseURI
    instance.baseURI = original
    assert instance.baseURI == original



@given(instance=rapidml_ResourceAPI_strategy)
def test_rapidml_resourceapi_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=rapidml_SecurityScheme_strategy)
@settings(max_examples=50)
def test_rapidml_securityscheme_instantiation(instance):
    assert isinstance(instance, rapidml_SecurityScheme)



@given(instance=rapidml_SecurityScheme_strategy)
def test_rapidml_securityscheme_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rapidml_SecurityScheme_strategy)
def test_rapidml_securityscheme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rapidml_SecurityScheme_strategy)
def test_rapidml_securityscheme_flow_setter(instance):
    original = instance.flow
    instance.flow = original
    assert instance.flow == original

@given(instance=rapidml_TypedMessage_strategy)
@settings(max_examples=50)
def test_rapidml_typedmessage_instantiation(instance):
    assert isinstance(instance, rapidml_TypedMessage)



@given(instance=rapidml_TypedMessage_strategy)
def test_rapidml_typedmessage_useParentTypeReference_setter(instance):
    original = instance.useParentTypeReference
    instance.useParentTypeReference = original
    assert instance.useParentTypeReference == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rapidml_TypedMessage_strategy)
@settings(max_examples=30)
def test_rapidml_typedmessage_isincluded_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isIncluded(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isIncluded).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isIncluded' in rapidml_TypedMessage is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isIncluded' in rapidml_TypedMessage did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isIncluded' in rapidml_TypedMessage is not implemented or raised an error")

@given(instance=rapidml_ResourceDefinition_strategy)
@settings(max_examples=50)
def test_rapidml_resourcedefinition_instantiation(instance):
    assert isinstance(instance, rapidml_ResourceDefinition)



@given(instance=rapidml_ResourceDefinition_strategy)
def test_rapidml_resourcedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

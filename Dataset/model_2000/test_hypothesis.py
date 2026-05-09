import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iTrace::Feature,
    TraceLinkElement,
    Artefact,
    iTrace::Code,
    iTrace::Block,
    iTrace::TargetElement,
    TraceLink,
    iTrace::M2TLink,
    iTrace::M2MLink,
    iTrace::EObject,
    iTrace::Model,
    iTrace::TraceLinkElement,
    iTrace::SourceElement,
    iTrace::Artefact,
    iTrace::TraceLink,
    iTrace::iTraceModel,
    iTrace::SpecificFeature,
    Mode,
    Type,
    Aspect,
    ModelType,
    AbstractionLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itrace::feature_is_not_abstract():
    assert not inspect.isabstract(iTrace::Feature)


def test_itrace::feature_constructor_exists():
    assert callable(iTrace::Feature.__init__)


def test_itrace::feature_constructor_args():
    sig = inspect.signature(iTrace::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_itrace::feature_has_value():
    assert hasattr(iTrace::Feature, "value")
    descriptor = None
    for klass in iTrace::Feature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_itrace::feature_has_attribute():
    assert hasattr(iTrace::Feature, "attribute")
    descriptor = None
    for klass in iTrace::Feature.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_tracelinkelement_is_not_abstract():
    assert not inspect.isabstract(TraceLinkElement)


def test_tracelinkelement_constructor_exists():
    assert callable(TraceLinkElement.__init__)


def test_tracelinkelement_constructor_args():
    sig = inspect.signature(TraceLinkElement.__init__)
    params = list(sig.parameters.keys())



def test_artefact_is_not_abstract():
    assert not inspect.isabstract(Artefact)


def test_artefact_constructor_exists():
    assert callable(Artefact.__init__)


def test_artefact_constructor_args():
    sig = inspect.signature(Artefact.__init__)
    params = list(sig.parameters.keys())



def test_itrace::code_is_not_abstract():
    assert not inspect.isabstract(iTrace::Code)


def test_itrace::code_constructor_exists():
    assert callable(iTrace::Code.__init__)


def test_itrace::code_constructor_args():
    sig = inspect.signature(iTrace::Code.__init__)
    params = list(sig.parameters.keys())



def test_itrace::block_is_not_abstract():
    assert not inspect.isabstract(iTrace::Block)


def test_itrace::block_constructor_exists():
    assert callable(iTrace::Block.__init__)


def test_itrace::block_constructor_args():
    sig = inspect.signature(iTrace::Block.__init__)
    params = list(sig.parameters.keys())
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "blockNumber" in params, "Missing parameter 'blockNumber'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"

def test_itrace::block_has_endColumn():
    assert hasattr(iTrace::Block, "endColumn")
    descriptor = None
    for klass in iTrace::Block.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_itrace::block_has_blockNumber():
    assert hasattr(iTrace::Block, "blockNumber")
    descriptor = None
    for klass in iTrace::Block.__mro__:
        if "blockNumber" in klass.__dict__:
            descriptor = klass.__dict__["blockNumber"]
            break
    assert isinstance(descriptor, property)

def test_itrace::block_has_endLine():
    assert hasattr(iTrace::Block, "endLine")
    descriptor = None
    for klass in iTrace::Block.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_itrace::block_has_startLine():
    assert hasattr(iTrace::Block, "startLine")
    descriptor = None
    for klass in iTrace::Block.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_itrace::block_has_startColumn():
    assert hasattr(iTrace::Block, "startColumn")
    descriptor = None
    for klass in iTrace::Block.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)



def test_itrace::targetelement_is_not_abstract():
    assert not inspect.isabstract(iTrace::TargetElement)


def test_itrace::targetelement_constructor_exists():
    assert callable(iTrace::TargetElement.__init__)


def test_itrace::targetelement_constructor_args():
    sig = inspect.signature(iTrace::TargetElement.__init__)
    params = list(sig.parameters.keys())



def test_tracelink_is_not_abstract():
    assert not inspect.isabstract(TraceLink)


def test_tracelink_constructor_exists():
    assert callable(TraceLink.__init__)


def test_tracelink_constructor_args():
    sig = inspect.signature(TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace::m2tlink_is_not_abstract():
    assert not inspect.isabstract(iTrace::M2TLink)


def test_itrace::m2tlink_constructor_exists():
    assert callable(iTrace::M2TLink.__init__)


def test_itrace::m2tlink_constructor_args():
    sig = inspect.signature(iTrace::M2TLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace::m2mlink_is_not_abstract():
    assert not inspect.isabstract(iTrace::M2MLink)


def test_itrace::m2mlink_constructor_exists():
    assert callable(iTrace::M2MLink.__init__)


def test_itrace::m2mlink_constructor_args():
    sig = inspect.signature(iTrace::M2MLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace::eobject_is_not_abstract():
    assert not inspect.isabstract(iTrace::EObject)


def test_itrace::eobject_constructor_exists():
    assert callable(iTrace::EObject.__init__)


def test_itrace::eobject_constructor_args():
    sig = inspect.signature(iTrace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_itrace::model_is_not_abstract():
    assert not inspect.isabstract(iTrace::Model)


def test_itrace::model_constructor_exists():
    assert callable(iTrace::Model.__init__)


def test_itrace::model_constructor_args():
    sig = inspect.signature(iTrace::Model.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_itrace::model_has_metamodel():
    assert hasattr(iTrace::Model, "metamodel")
    descriptor = None
    for klass in iTrace::Model.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_itrace::tracelinkelement_is_not_abstract():
    assert not inspect.isabstract(iTrace::TraceLinkElement)


def test_itrace::tracelinkelement_constructor_exists():
    assert callable(iTrace::TraceLinkElement.__init__)


def test_itrace::tracelinkelement_constructor_args():
    sig = inspect.signature(iTrace::TraceLinkElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "name" in params, "Missing parameter 'name'"

def test_itrace::tracelinkelement_has_type():
    assert hasattr(iTrace::TraceLinkElement, "type")
    descriptor = None
    for klass in iTrace::TraceLinkElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelinkelement_has_ref():
    assert hasattr(iTrace::TraceLinkElement, "ref")
    descriptor = None
    for klass in iTrace::TraceLinkElement.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelinkelement_has_name():
    assert hasattr(iTrace::TraceLinkElement, "name")
    descriptor = None
    for klass in iTrace::TraceLinkElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_itrace::sourceelement_is_not_abstract():
    assert not inspect.isabstract(iTrace::SourceElement)


def test_itrace::sourceelement_constructor_exists():
    assert callable(iTrace::SourceElement.__init__)


def test_itrace::sourceelement_constructor_args():
    sig = inspect.signature(iTrace::SourceElement.__init__)
    params = list(sig.parameters.keys())



def test_itrace::artefact_is_not_abstract():
    assert not inspect.isabstract(iTrace::Artefact)


def test_itrace::artefact_constructor_exists():
    assert callable(iTrace::Artefact.__init__)


def test_itrace::artefact_constructor_args():
    sig = inspect.signature(iTrace::Artefact.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "abstractionLevel" in params, "Missing parameter 'abstractionLevel'"
    assert "name" in params, "Missing parameter 'name'"
    assert "aspect" in params, "Missing parameter 'aspect'"

def test_itrace::artefact_has_path():
    assert hasattr(iTrace::Artefact, "path")
    descriptor = None
    for klass in iTrace::Artefact.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_itrace::artefact_has_abstractionLevel():
    assert hasattr(iTrace::Artefact, "abstractionLevel")
    descriptor = None
    for klass in iTrace::Artefact.__mro__:
        if "abstractionLevel" in klass.__dict__:
            descriptor = klass.__dict__["abstractionLevel"]
            break
    assert isinstance(descriptor, property)

def test_itrace::artefact_has_name():
    assert hasattr(iTrace::Artefact, "name")
    descriptor = None
    for klass in iTrace::Artefact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_itrace::artefact_has_aspect():
    assert hasattr(iTrace::Artefact, "aspect")
    descriptor = None
    for klass in iTrace::Artefact.__mro__:
        if "aspect" in klass.__dict__:
            descriptor = klass.__dict__["aspect"]
            break
    assert isinstance(descriptor, property)



def test_itrace::tracelink_is_not_abstract():
    assert not inspect.isabstract(iTrace::TraceLink)


def test_itrace::tracelink_constructor_exists():
    assert callable(iTrace::TraceLink.__init__)


def test_itrace::tracelink_constructor_args():
    sig = inspect.signature(iTrace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "createdBy" in params, "Missing parameter 'createdBy'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "type" in params, "Missing parameter 'type'"
    assert "technicalBinding" in params, "Missing parameter 'technicalBinding'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "fromFileName" in params, "Missing parameter 'fromFileName'"
    assert "createdOn" in params, "Missing parameter 'createdOn'"
    assert "ruleName" in params, "Missing parameter 'ruleName'"

def test_itrace::tracelink_has_createdBy():
    assert hasattr(iTrace::TraceLink, "createdBy")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "createdBy" in klass.__dict__:
            descriptor = klass.__dict__["createdBy"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_comment():
    assert hasattr(iTrace::TraceLink, "comment")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_type():
    assert hasattr(iTrace::TraceLink, "type")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_technicalBinding():
    assert hasattr(iTrace::TraceLink, "technicalBinding")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "technicalBinding" in klass.__dict__:
            descriptor = klass.__dict__["technicalBinding"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_mode():
    assert hasattr(iTrace::TraceLink, "mode")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_fromFileName():
    assert hasattr(iTrace::TraceLink, "fromFileName")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "fromFileName" in klass.__dict__:
            descriptor = klass.__dict__["fromFileName"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_createdOn():
    assert hasattr(iTrace::TraceLink, "createdOn")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "createdOn" in klass.__dict__:
            descriptor = klass.__dict__["createdOn"]
            break
    assert isinstance(descriptor, property)

def test_itrace::tracelink_has_ruleName():
    assert hasattr(iTrace::TraceLink, "ruleName")
    descriptor = None
    for klass in iTrace::TraceLink.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
            break
    assert isinstance(descriptor, property)



def test_itrace::itracemodel_is_not_abstract():
    assert not inspect.isabstract(iTrace::iTraceModel)


def test_itrace::itracemodel_constructor_exists():
    assert callable(iTrace::iTraceModel.__init__)


def test_itrace::itracemodel_constructor_args():
    sig = inspect.signature(iTrace::iTraceModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "projectName" in params, "Missing parameter 'projectName'"

def test_itrace::itracemodel_has_version():
    assert hasattr(iTrace::iTraceModel, "version")
    descriptor = None
    for klass in iTrace::iTraceModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_itrace::itracemodel_has_projectName():
    assert hasattr(iTrace::iTraceModel, "projectName")
    descriptor = None
    for klass in iTrace::iTraceModel.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)



def test_itrace::specificfeature_is_not_abstract():
    assert not inspect.isabstract(iTrace::SpecificFeature)


def test_itrace::specificfeature_constructor_exists():
    assert callable(iTrace::SpecificFeature.__init__)


def test_itrace::specificfeature_constructor_args():
    sig = inspect.signature(iTrace::SpecificFeature.__init__)
    params = list(sig.parameters.keys())
    assert "groupName" in params, "Missing parameter 'groupName'"

def test_itrace::specificfeature_has_groupName():
    assert hasattr(iTrace::SpecificFeature, "groupName")
    descriptor = None
    for klass in iTrace::SpecificFeature.__mro__:
        if "groupName" in klass.__dict__:
            descriptor = klass.__dict__["groupName"]
            break
    assert isinstance(descriptor, property)

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "Automatic",
        "Manual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Annotation",
        "Transformation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_aspect_exists():
    # Check that the Enumeration exists
    assert Aspect is not None

def test_aspect_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Aspect]
    expected_literals = [
        "Behaviour",
        "Content",
        "Semantics",
        "Unspecified",
        "Quality",
        "Architecture",
        "Interface",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Aspect"

def test_modeltype_exists():
    # Check that the Enumeration exists
    assert ModelType is not None

def test_modeltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModelType]
    expected_literals = [
        "Both",
        "None_",
        "Target",
        "Source",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModelType"

def test_abstractionlevel_exists():
    # Check that the Enumeration exists
    assert AbstractionLevel is not None

def test_abstractionlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AbstractionLevel]
    expected_literals = [
        "CIM",
        "UNSPECIFIED",
        "PSM",
        "CODE",
        "PDM",
        "ANNOTATION",
        "PIM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AbstractionLevel"


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
iTrace::Feature_strategy = st.builds(
    iTrace::Feature,
    value=
        safe_text,
    attribute=
        safe_text
)
TraceLinkElement_strategy = st.builds(
    TraceLinkElement,
)
Artefact_strategy = st.builds(
    Artefact,
)
iTrace::Code_strategy = st.builds(
    iTrace::Code,
)
iTrace::Block_strategy = st.builds(
    iTrace::Block,
    endColumn=
        st.integers(),
    blockNumber=
        st.integers(),
    endLine=
        st.integers(),
    startLine=
        st.integers(),
    startColumn=
        st.integers()
)
iTrace::TargetElement_strategy = st.builds(
    iTrace::TargetElement,
)
TraceLink_strategy = st.builds(
    TraceLink,
)
iTrace::M2TLink_strategy = st.builds(
    iTrace::M2TLink,
)
iTrace::M2MLink_strategy = st.builds(
    iTrace::M2MLink,
)
iTrace::EObject_strategy = st.builds(
    iTrace::EObject,
)
iTrace::Model_strategy = st.builds(
    iTrace::Model,
    metamodel=
        safe_text
)
iTrace::TraceLinkElement_strategy = st.builds(
    iTrace::TraceLinkElement,
    type=
        safe_text,
    ref=
        safe_text,
    name=
        safe_text
)
iTrace::SourceElement_strategy = st.builds(
    iTrace::SourceElement,
)
iTrace::Artefact_strategy = st.builds(
    iTrace::Artefact,
    path=
        safe_text,
    abstractionLevel=
        safe_text,
    name=
        safe_text,
    aspect=
        safe_text
)
iTrace::TraceLink_strategy = st.builds(
    iTrace::TraceLink,
    createdBy=
        safe_text,
    comment=
        safe_text,
    type=
        safe_text,
    technicalBinding=
        safe_text,
    mode=
        safe_text,
    fromFileName=
        safe_text,
    createdOn=
        safe_text,
    ruleName=
        safe_text
)
iTrace::iTraceModel_strategy = st.builds(
    iTrace::iTraceModel,
    version=
        safe_text,
    projectName=
        safe_text
)
iTrace::SpecificFeature_strategy = st.builds(
    iTrace::SpecificFeature,
    groupName=
        safe_text
)

@given(instance=iTrace::Feature_strategy)
@settings(max_examples=50)
def test_itrace::feature_instantiation(instance):
    assert isinstance(instance, iTrace::Feature)

@given(instance=iTrace::Feature_strategy)
def test_itrace::feature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iTrace::Feature_strategy)
def test_itrace::feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iTrace::Feature_strategy)
def test_itrace::feature_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=iTrace::Feature_strategy)
def test_itrace::feature_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=TraceLinkElement_strategy)
@settings(max_examples=50)
def test_tracelinkelement_instantiation(instance):
    assert isinstance(instance, TraceLinkElement)

@given(instance=Artefact_strategy)
@settings(max_examples=50)
def test_artefact_instantiation(instance):
    assert isinstance(instance, Artefact)

@given(instance=iTrace::Code_strategy)
@settings(max_examples=50)
def test_itrace::code_instantiation(instance):
    assert isinstance(instance, iTrace::Code)

@given(instance=iTrace::Block_strategy)
@settings(max_examples=50)
def test_itrace::block_instantiation(instance):
    assert isinstance(instance, iTrace::Block)

@given(instance=iTrace::Block_strategy)
def test_itrace::block_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=iTrace::Block_strategy)
def test_itrace::block_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=iTrace::Block_strategy)
def test_itrace::block_blockNumber_type(instance):
    assert isinstance(instance.blockNumber, int)


@given(instance=iTrace::Block_strategy)
def test_itrace::block_blockNumber_setter(instance):
    original = instance.blockNumber
    instance.blockNumber = original
    assert instance.blockNumber == original

@given(instance=iTrace::Block_strategy)
def test_itrace::block_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=iTrace::Block_strategy)
def test_itrace::block_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=iTrace::Block_strategy)
def test_itrace::block_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=iTrace::Block_strategy)
def test_itrace::block_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=iTrace::Block_strategy)
def test_itrace::block_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=iTrace::Block_strategy)
def test_itrace::block_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=iTrace::TargetElement_strategy)
@settings(max_examples=50)
def test_itrace::targetelement_instantiation(instance):
    assert isinstance(instance, iTrace::TargetElement)

@given(instance=TraceLink_strategy)
@settings(max_examples=50)
def test_tracelink_instantiation(instance):
    assert isinstance(instance, TraceLink)

@given(instance=iTrace::M2TLink_strategy)
@settings(max_examples=50)
def test_itrace::m2tlink_instantiation(instance):
    assert isinstance(instance, iTrace::M2TLink)

@given(instance=iTrace::M2MLink_strategy)
@settings(max_examples=50)
def test_itrace::m2mlink_instantiation(instance):
    assert isinstance(instance, iTrace::M2MLink)

@given(instance=iTrace::EObject_strategy)
@settings(max_examples=50)
def test_itrace::eobject_instantiation(instance):
    assert isinstance(instance, iTrace::EObject)

@given(instance=iTrace::Model_strategy)
@settings(max_examples=50)
def test_itrace::model_instantiation(instance):
    assert isinstance(instance, iTrace::Model)

@given(instance=iTrace::Model_strategy)
def test_itrace::model_metamodel_type(instance):
    assert isinstance(instance.metamodel, str)


@given(instance=iTrace::Model_strategy)
def test_itrace::model_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=iTrace::TraceLinkElement_strategy)
@settings(max_examples=50)
def test_itrace::tracelinkelement_instantiation(instance):
    assert isinstance(instance, iTrace::TraceLinkElement)

@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iTrace::TraceLinkElement_strategy)
def test_itrace::tracelinkelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iTrace::SourceElement_strategy)
@settings(max_examples=50)
def test_itrace::sourceelement_instantiation(instance):
    assert isinstance(instance, iTrace::SourceElement)

@given(instance=iTrace::Artefact_strategy)
@settings(max_examples=50)
def test_itrace::artefact_instantiation(instance):
    assert isinstance(instance, iTrace::Artefact)

@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_abstractionLevel_type(instance):
    assert isinstance(instance.abstractionLevel, str)


@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_abstractionLevel_setter(instance):
    original = instance.abstractionLevel
    instance.abstractionLevel = original
    assert instance.abstractionLevel == original

@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_aspect_type(instance):
    assert isinstance(instance.aspect, str)


@given(instance=iTrace::Artefact_strategy)
def test_itrace::artefact_aspect_setter(instance):
    original = instance.aspect
    instance.aspect = original
    assert instance.aspect == original

@given(instance=iTrace::TraceLink_strategy)
@settings(max_examples=50)
def test_itrace::tracelink_instantiation(instance):
    assert isinstance(instance, iTrace::TraceLink)

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_createdBy_type(instance):
    assert isinstance(instance.createdBy, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_createdBy_setter(instance):
    original = instance.createdBy
    instance.createdBy = original
    assert instance.createdBy == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_technicalBinding_type(instance):
    assert isinstance(instance.technicalBinding, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_technicalBinding_setter(instance):
    original = instance.technicalBinding
    instance.technicalBinding = original
    assert instance.technicalBinding == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_fromFileName_type(instance):
    assert isinstance(instance.fromFileName, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_fromFileName_setter(instance):
    original = instance.fromFileName
    instance.fromFileName = original
    assert instance.fromFileName == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_createdOn_type(instance):
    assert isinstance(instance.createdOn, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_createdOn_setter(instance):
    original = instance.createdOn
    instance.createdOn = original
    assert instance.createdOn == original

@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_ruleName_type(instance):
    assert isinstance(instance.ruleName, str)


@given(instance=iTrace::TraceLink_strategy)
def test_itrace::tracelink_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original

@given(instance=iTrace::iTraceModel_strategy)
@settings(max_examples=50)
def test_itrace::itracemodel_instantiation(instance):
    assert isinstance(instance, iTrace::iTraceModel)

@given(instance=iTrace::iTraceModel_strategy)
def test_itrace::itracemodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=iTrace::iTraceModel_strategy)
def test_itrace::itracemodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=iTrace::iTraceModel_strategy)
def test_itrace::itracemodel_projectName_type(instance):
    assert isinstance(instance.projectName, str)


@given(instance=iTrace::iTraceModel_strategy)
def test_itrace::itracemodel_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original

@given(instance=iTrace::SpecificFeature_strategy)
@settings(max_examples=50)
def test_itrace::specificfeature_instantiation(instance):
    assert isinstance(instance, iTrace::SpecificFeature)

@given(instance=iTrace::SpecificFeature_strategy)
def test_itrace::specificfeature_groupName_type(instance):
    assert isinstance(instance.groupName, str)


@given(instance=iTrace::SpecificFeature_strategy)
def test_itrace::specificfeature_groupName_setter(instance):
    original = instance.groupName
    instance.groupName = original
    assert instance.groupName == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iTrace_Feature,
    TraceLinkElement,
    Artefact,
    iTrace_Code,
    iTrace_Block,
    iTrace_TargetElement,
    TraceLink,
    iTrace_M2TLink,
    iTrace_M2MLink,
    iTrace_EObject,
    iTrace_Model,
    iTrace_TraceLinkElement,
    iTrace_SourceElement,
    iTrace_Artefact,
    iTrace_TraceLink,
    iTrace_iTraceModel,
    iTrace_SpecificFeature,
    AbstractionLevel,
    Aspect,
    ModelType,
    Mode,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itrace_feature_is_not_abstract():
    assert not inspect.isabstract(iTrace_Feature)


def test_itrace_feature_constructor_exists():
    assert callable(iTrace_Feature.__init__)


def test_itrace_feature_constructor_args():
    sig = inspect.signature(iTrace_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_itrace_feature_has_value():
    assert hasattr(iTrace_Feature, "value")
    descriptor = None
    for klass in iTrace_Feature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_itrace_feature_has_attribute():
    assert hasattr(iTrace_Feature, "attribute")
    descriptor = None
    for klass in iTrace_Feature.__mro__:
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



def test_itrace_code_is_not_abstract():
    assert not inspect.isabstract(iTrace_Code)


def test_itrace_code_constructor_exists():
    assert callable(iTrace_Code.__init__)


def test_itrace_code_constructor_args():
    sig = inspect.signature(iTrace_Code.__init__)
    params = list(sig.parameters.keys())



def test_itrace_block_is_not_abstract():
    assert not inspect.isabstract(iTrace_Block)


def test_itrace_block_constructor_exists():
    assert callable(iTrace_Block.__init__)


def test_itrace_block_constructor_args():
    sig = inspect.signature(iTrace_Block.__init__)
    params = list(sig.parameters.keys())
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "blockNumber" in params, "Missing parameter 'blockNumber'"

def test_itrace_block_has_endColumn():
    assert hasattr(iTrace_Block, "endColumn")
    descriptor = None
    for klass in iTrace_Block.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_itrace_block_has_endLine():
    assert hasattr(iTrace_Block, "endLine")
    descriptor = None
    for klass in iTrace_Block.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_itrace_block_has_startColumn():
    assert hasattr(iTrace_Block, "startColumn")
    descriptor = None
    for klass in iTrace_Block.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_itrace_block_has_startLine():
    assert hasattr(iTrace_Block, "startLine")
    descriptor = None
    for klass in iTrace_Block.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_itrace_block_has_blockNumber():
    assert hasattr(iTrace_Block, "blockNumber")
    descriptor = None
    for klass in iTrace_Block.__mro__:
        if "blockNumber" in klass.__dict__:
            descriptor = klass.__dict__["blockNumber"]
            break
    assert isinstance(descriptor, property)



def test_itrace_targetelement_is_not_abstract():
    assert not inspect.isabstract(iTrace_TargetElement)


def test_itrace_targetelement_constructor_exists():
    assert callable(iTrace_TargetElement.__init__)


def test_itrace_targetelement_constructor_args():
    sig = inspect.signature(iTrace_TargetElement.__init__)
    params = list(sig.parameters.keys())



def test_tracelink_is_not_abstract():
    assert not inspect.isabstract(TraceLink)


def test_tracelink_constructor_exists():
    assert callable(TraceLink.__init__)


def test_tracelink_constructor_args():
    sig = inspect.signature(TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace_m2tlink_is_not_abstract():
    assert not inspect.isabstract(iTrace_M2TLink)


def test_itrace_m2tlink_constructor_exists():
    assert callable(iTrace_M2TLink.__init__)


def test_itrace_m2tlink_constructor_args():
    sig = inspect.signature(iTrace_M2TLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace_m2mlink_is_not_abstract():
    assert not inspect.isabstract(iTrace_M2MLink)


def test_itrace_m2mlink_constructor_exists():
    assert callable(iTrace_M2MLink.__init__)


def test_itrace_m2mlink_constructor_args():
    sig = inspect.signature(iTrace_M2MLink.__init__)
    params = list(sig.parameters.keys())



def test_itrace_eobject_is_not_abstract():
    assert not inspect.isabstract(iTrace_EObject)


def test_itrace_eobject_constructor_exists():
    assert callable(iTrace_EObject.__init__)


def test_itrace_eobject_constructor_args():
    sig = inspect.signature(iTrace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_itrace_model_is_not_abstract():
    assert not inspect.isabstract(iTrace_Model)


def test_itrace_model_constructor_exists():
    assert callable(iTrace_Model.__init__)


def test_itrace_model_constructor_args():
    sig = inspect.signature(iTrace_Model.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_itrace_model_has_metamodel():
    assert hasattr(iTrace_Model, "metamodel")
    descriptor = None
    for klass in iTrace_Model.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_itrace_tracelinkelement_is_not_abstract():
    assert not inspect.isabstract(iTrace_TraceLinkElement)


def test_itrace_tracelinkelement_constructor_exists():
    assert callable(iTrace_TraceLinkElement.__init__)


def test_itrace_tracelinkelement_constructor_args():
    sig = inspect.signature(iTrace_TraceLinkElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "name" in params, "Missing parameter 'name'"

def test_itrace_tracelinkelement_has_type():
    assert hasattr(iTrace_TraceLinkElement, "type")
    descriptor = None
    for klass in iTrace_TraceLinkElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelinkelement_has_ref():
    assert hasattr(iTrace_TraceLinkElement, "ref")
    descriptor = None
    for klass in iTrace_TraceLinkElement.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelinkelement_has_name():
    assert hasattr(iTrace_TraceLinkElement, "name")
    descriptor = None
    for klass in iTrace_TraceLinkElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_itrace_sourceelement_is_not_abstract():
    assert not inspect.isabstract(iTrace_SourceElement)


def test_itrace_sourceelement_constructor_exists():
    assert callable(iTrace_SourceElement.__init__)


def test_itrace_sourceelement_constructor_args():
    sig = inspect.signature(iTrace_SourceElement.__init__)
    params = list(sig.parameters.keys())



def test_itrace_artefact_is_not_abstract():
    assert not inspect.isabstract(iTrace_Artefact)


def test_itrace_artefact_constructor_exists():
    assert callable(iTrace_Artefact.__init__)


def test_itrace_artefact_constructor_args():
    sig = inspect.signature(iTrace_Artefact.__init__)
    params = list(sig.parameters.keys())
    assert "abstractionLevel" in params, "Missing parameter 'abstractionLevel'"
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"
    assert "aspect" in params, "Missing parameter 'aspect'"

def test_itrace_artefact_has_abstractionLevel():
    assert hasattr(iTrace_Artefact, "abstractionLevel")
    descriptor = None
    for klass in iTrace_Artefact.__mro__:
        if "abstractionLevel" in klass.__dict__:
            descriptor = klass.__dict__["abstractionLevel"]
            break
    assert isinstance(descriptor, property)

def test_itrace_artefact_has_path():
    assert hasattr(iTrace_Artefact, "path")
    descriptor = None
    for klass in iTrace_Artefact.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_itrace_artefact_has_name():
    assert hasattr(iTrace_Artefact, "name")
    descriptor = None
    for klass in iTrace_Artefact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_itrace_artefact_has_aspect():
    assert hasattr(iTrace_Artefact, "aspect")
    descriptor = None
    for klass in iTrace_Artefact.__mro__:
        if "aspect" in klass.__dict__:
            descriptor = klass.__dict__["aspect"]
            break
    assert isinstance(descriptor, property)



def test_itrace_tracelink_is_not_abstract():
    assert not inspect.isabstract(iTrace_TraceLink)


def test_itrace_tracelink_constructor_exists():
    assert callable(iTrace_TraceLink.__init__)


def test_itrace_tracelink_constructor_args():
    sig = inspect.signature(iTrace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "createdBy" in params, "Missing parameter 'createdBy'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "technicalBinding" in params, "Missing parameter 'technicalBinding'"
    assert "type" in params, "Missing parameter 'type'"
    assert "fromFileName" in params, "Missing parameter 'fromFileName'"
    assert "ruleName" in params, "Missing parameter 'ruleName'"
    assert "createdOn" in params, "Missing parameter 'createdOn'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_itrace_tracelink_has_createdBy():
    assert hasattr(iTrace_TraceLink, "createdBy")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "createdBy" in klass.__dict__:
            descriptor = klass.__dict__["createdBy"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_mode():
    assert hasattr(iTrace_TraceLink, "mode")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_technicalBinding():
    assert hasattr(iTrace_TraceLink, "technicalBinding")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "technicalBinding" in klass.__dict__:
            descriptor = klass.__dict__["technicalBinding"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_type():
    assert hasattr(iTrace_TraceLink, "type")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_fromFileName():
    assert hasattr(iTrace_TraceLink, "fromFileName")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "fromFileName" in klass.__dict__:
            descriptor = klass.__dict__["fromFileName"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_ruleName():
    assert hasattr(iTrace_TraceLink, "ruleName")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_createdOn():
    assert hasattr(iTrace_TraceLink, "createdOn")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "createdOn" in klass.__dict__:
            descriptor = klass.__dict__["createdOn"]
            break
    assert isinstance(descriptor, property)

def test_itrace_tracelink_has_comment():
    assert hasattr(iTrace_TraceLink, "comment")
    descriptor = None
    for klass in iTrace_TraceLink.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_itrace_itracemodel_is_not_abstract():
    assert not inspect.isabstract(iTrace_iTraceModel)


def test_itrace_itracemodel_constructor_exists():
    assert callable(iTrace_iTraceModel.__init__)


def test_itrace_itracemodel_constructor_args():
    sig = inspect.signature(iTrace_iTraceModel.__init__)
    params = list(sig.parameters.keys())
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "version" in params, "Missing parameter 'version'"

def test_itrace_itracemodel_has_projectName():
    assert hasattr(iTrace_iTraceModel, "projectName")
    descriptor = None
    for klass in iTrace_iTraceModel.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_itrace_itracemodel_has_version():
    assert hasattr(iTrace_iTraceModel, "version")
    descriptor = None
    for klass in iTrace_iTraceModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_itrace_specificfeature_is_not_abstract():
    assert not inspect.isabstract(iTrace_SpecificFeature)


def test_itrace_specificfeature_constructor_exists():
    assert callable(iTrace_SpecificFeature.__init__)


def test_itrace_specificfeature_constructor_args():
    sig = inspect.signature(iTrace_SpecificFeature.__init__)
    params = list(sig.parameters.keys())
    assert "groupName" in params, "Missing parameter 'groupName'"

def test_itrace_specificfeature_has_groupName():
    assert hasattr(iTrace_SpecificFeature, "groupName")
    descriptor = None
    for klass in iTrace_SpecificFeature.__mro__:
        if "groupName" in klass.__dict__:
            descriptor = klass.__dict__["groupName"]
            break
    assert isinstance(descriptor, property)

def test_abstractionlevel_exists():
    # Check that the Enumeration exists
    assert AbstractionLevel is not None

def test_abstractionlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AbstractionLevel]
    expected_literals = [
        "CODE",
        "UNSPECIFIED",
        "CIM",
        "PSM",
        "PDM",
        "PIM",
        "ANNOTATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AbstractionLevel"

def test_aspect_exists():
    # Check that the Enumeration exists
    assert Aspect is not None

def test_aspect_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Aspect]
    expected_literals = [
        "Behaviour",
        "Architecture",
        "Interface",
        "Unspecified",
        "Content",
        "Semantics",
        "Quality",
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
        "Source",
        "None_",
        "Target",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModelType"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "Manual",
        "Automatic",
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
        "Transformation",
        "Annotation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
iTrace_Feature_strategy = st.builds(
    iTrace_Feature,
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
iTrace_Code_strategy = st.builds(
    iTrace_Code,
)
iTrace_Block_strategy = st.builds(
    iTrace_Block,
    endColumn=
        st.integers(),
    endLine=
        st.integers(),
    startColumn=
        st.integers(),
    startLine=
        st.integers(),
    blockNumber=
        st.integers()
)
iTrace_TargetElement_strategy = st.builds(
    iTrace_TargetElement,
)
TraceLink_strategy = st.builds(
    TraceLink,
)
iTrace_M2TLink_strategy = st.builds(
    iTrace_M2TLink,
)
iTrace_M2MLink_strategy = st.builds(
    iTrace_M2MLink,
)
iTrace_EObject_strategy = st.builds(
    iTrace_EObject,
)
iTrace_Model_strategy = st.builds(
    iTrace_Model,
    metamodel=
        safe_text
)
iTrace_TraceLinkElement_strategy = st.builds(
    iTrace_TraceLinkElement,
    type=
        safe_text,
    ref=
        safe_text,
    name=
        safe_text
)
iTrace_SourceElement_strategy = st.builds(
    iTrace_SourceElement,
)
iTrace_Artefact_strategy = st.builds(
    iTrace_Artefact,
    abstractionLevel=
        safe_text,
    path=
        safe_text,
    name=
        safe_text,
    aspect=
        safe_text
)
iTrace_TraceLink_strategy = st.builds(
    iTrace_TraceLink,
    createdBy=
        safe_text,
    mode=
        safe_text,
    technicalBinding=
        safe_text,
    type=
        safe_text,
    fromFileName=
        safe_text,
    ruleName=
        safe_text,
    createdOn=
        safe_text,
    comment=
        safe_text
)
iTrace_iTraceModel_strategy = st.builds(
    iTrace_iTraceModel,
    projectName=
        safe_text,
    version=
        safe_text
)
iTrace_SpecificFeature_strategy = st.builds(
    iTrace_SpecificFeature,
    groupName=
        safe_text
)

@given(instance=iTrace_Feature_strategy)
@settings(max_examples=50)
def test_itrace_feature_instantiation(instance):
    assert isinstance(instance, iTrace_Feature)



@given(instance=iTrace_Feature_strategy)
def test_itrace_feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=iTrace_Feature_strategy)
def test_itrace_feature_attribute_setter(instance):
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

@given(instance=iTrace_Code_strategy)
@settings(max_examples=50)
def test_itrace_code_instantiation(instance):
    assert isinstance(instance, iTrace_Code)

@given(instance=iTrace_Block_strategy)
@settings(max_examples=50)
def test_itrace_block_instantiation(instance):
    assert isinstance(instance, iTrace_Block)



@given(instance=iTrace_Block_strategy)
def test_itrace_block_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original



@given(instance=iTrace_Block_strategy)
def test_itrace_block_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=iTrace_Block_strategy)
def test_itrace_block_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=iTrace_Block_strategy)
def test_itrace_block_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=iTrace_Block_strategy)
def test_itrace_block_blockNumber_setter(instance):
    original = instance.blockNumber
    instance.blockNumber = original
    assert instance.blockNumber == original

@given(instance=iTrace_TargetElement_strategy)
@settings(max_examples=50)
def test_itrace_targetelement_instantiation(instance):
    assert isinstance(instance, iTrace_TargetElement)

@given(instance=TraceLink_strategy)
@settings(max_examples=50)
def test_tracelink_instantiation(instance):
    assert isinstance(instance, TraceLink)

@given(instance=iTrace_M2TLink_strategy)
@settings(max_examples=50)
def test_itrace_m2tlink_instantiation(instance):
    assert isinstance(instance, iTrace_M2TLink)

@given(instance=iTrace_M2MLink_strategy)
@settings(max_examples=50)
def test_itrace_m2mlink_instantiation(instance):
    assert isinstance(instance, iTrace_M2MLink)

@given(instance=iTrace_EObject_strategy)
@settings(max_examples=50)
def test_itrace_eobject_instantiation(instance):
    assert isinstance(instance, iTrace_EObject)

@given(instance=iTrace_Model_strategy)
@settings(max_examples=50)
def test_itrace_model_instantiation(instance):
    assert isinstance(instance, iTrace_Model)



@given(instance=iTrace_Model_strategy)
def test_itrace_model_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=iTrace_TraceLinkElement_strategy)
@settings(max_examples=50)
def test_itrace_tracelinkelement_instantiation(instance):
    assert isinstance(instance, iTrace_TraceLinkElement)



@given(instance=iTrace_TraceLinkElement_strategy)
def test_itrace_tracelinkelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=iTrace_TraceLinkElement_strategy)
def test_itrace_tracelinkelement_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



@given(instance=iTrace_TraceLinkElement_strategy)
def test_itrace_tracelinkelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iTrace_SourceElement_strategy)
@settings(max_examples=50)
def test_itrace_sourceelement_instantiation(instance):
    assert isinstance(instance, iTrace_SourceElement)

@given(instance=iTrace_Artefact_strategy)
@settings(max_examples=50)
def test_itrace_artefact_instantiation(instance):
    assert isinstance(instance, iTrace_Artefact)



@given(instance=iTrace_Artefact_strategy)
def test_itrace_artefact_abstractionLevel_setter(instance):
    original = instance.abstractionLevel
    instance.abstractionLevel = original
    assert instance.abstractionLevel == original



@given(instance=iTrace_Artefact_strategy)
def test_itrace_artefact_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=iTrace_Artefact_strategy)
def test_itrace_artefact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iTrace_Artefact_strategy)
def test_itrace_artefact_aspect_setter(instance):
    original = instance.aspect
    instance.aspect = original
    assert instance.aspect == original

@given(instance=iTrace_TraceLink_strategy)
@settings(max_examples=50)
def test_itrace_tracelink_instantiation(instance):
    assert isinstance(instance, iTrace_TraceLink)



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_createdBy_setter(instance):
    original = instance.createdBy
    instance.createdBy = original
    assert instance.createdBy == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_technicalBinding_setter(instance):
    original = instance.technicalBinding
    instance.technicalBinding = original
    assert instance.technicalBinding == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_fromFileName_setter(instance):
    original = instance.fromFileName
    instance.fromFileName = original
    assert instance.fromFileName == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_createdOn_setter(instance):
    original = instance.createdOn
    instance.createdOn = original
    assert instance.createdOn == original



@given(instance=iTrace_TraceLink_strategy)
def test_itrace_tracelink_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=iTrace_iTraceModel_strategy)
@settings(max_examples=50)
def test_itrace_itracemodel_instantiation(instance):
    assert isinstance(instance, iTrace_iTraceModel)



@given(instance=iTrace_iTraceModel_strategy)
def test_itrace_itracemodel_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original



@given(instance=iTrace_iTraceModel_strategy)
def test_itrace_itracemodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=iTrace_SpecificFeature_strategy)
@settings(max_examples=50)
def test_itrace_specificfeature_instantiation(instance):
    assert isinstance(instance, iTrace_SpecificFeature)



@given(instance=iTrace_SpecificFeature_strategy)
def test_itrace_specificfeature_groupName_setter(instance):
    original = instance.groupName
    instance.groupName = original
    assert instance.groupName == original

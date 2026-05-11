import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traceabilitymodel::Block,
    traceabilitymodel::TraceableSegment,
    traceabilitymodel::Trace,
    traceabilitymodel::MetaModel,
    traceabilitymodel::ModelElementRef,
    traceabilitymodel::File,
    traceabilitymodel::TraceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceabilitymodel::block_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::Block)


def test_traceabilitymodel::block_constructor_exists():
    assert callable(traceabilitymodel::Block.__init__)


def test_traceabilitymodel::block_constructor_args():
    sig = inspect.signature(traceabilitymodel::Block.__init__)
    params = list(sig.parameters.keys())
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startPos" in params, "Missing parameter 'startPos'"
    assert "endPos" in params, "Missing parameter 'endPos'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "protectedBlock" in params, "Missing parameter 'protectedBlock'"

def test_traceabilitymodel::block_has_endLine():
    assert hasattr(traceabilitymodel::Block, "endLine")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_startColumn():
    assert hasattr(traceabilitymodel::Block, "startColumn")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_endColumn():
    assert hasattr(traceabilitymodel::Block, "endColumn")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_startPos():
    assert hasattr(traceabilitymodel::Block, "startPos")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "startPos" in klass.__dict__:
            descriptor = klass.__dict__["startPos"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_endPos():
    assert hasattr(traceabilitymodel::Block, "endPos")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "endPos" in klass.__dict__:
            descriptor = klass.__dict__["endPos"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_startLine():
    assert hasattr(traceabilitymodel::Block, "startLine")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_ID():
    assert hasattr(traceabilitymodel::Block, "ID")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::block_has_protectedBlock():
    assert hasattr(traceabilitymodel::Block, "protectedBlock")
    descriptor = None
    for klass in traceabilitymodel::Block.__mro__:
        if "protectedBlock" in klass.__dict__:
            descriptor = klass.__dict__["protectedBlock"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::traceablesegment_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::TraceableSegment)


def test_traceabilitymodel::traceablesegment_constructor_exists():
    assert callable(traceabilitymodel::TraceableSegment.__init__)


def test_traceabilitymodel::traceablesegment_constructor_args():
    sig = inspect.signature(traceabilitymodel::TraceableSegment.__init__)
    params = list(sig.parameters.keys())
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "startPos" in params, "Missing parameter 'startPos'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "endPos" in params, "Missing parameter 'endPos'"

def test_traceabilitymodel::traceablesegment_has_startColumn():
    assert hasattr(traceabilitymodel::TraceableSegment, "startColumn")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::traceablesegment_has_startLine():
    assert hasattr(traceabilitymodel::TraceableSegment, "startLine")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::traceablesegment_has_startPos():
    assert hasattr(traceabilitymodel::TraceableSegment, "startPos")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "startPos" in klass.__dict__:
            descriptor = klass.__dict__["startPos"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::traceablesegment_has_endColumn():
    assert hasattr(traceabilitymodel::TraceableSegment, "endColumn")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::traceablesegment_has_endLine():
    assert hasattr(traceabilitymodel::TraceableSegment, "endLine")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::traceablesegment_has_endPos():
    assert hasattr(traceabilitymodel::TraceableSegment, "endPos")
    descriptor = None
    for klass in traceabilitymodel::TraceableSegment.__mro__:
        if "endPos" in klass.__dict__:
            descriptor = klass.__dict__["endPos"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::trace_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::Trace)


def test_traceabilitymodel::trace_constructor_exists():
    assert callable(traceabilitymodel::Trace.__init__)


def test_traceabilitymodel::trace_constructor_args():
    sig = inspect.signature(traceabilitymodel::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "sourceOperationID" in params, "Missing parameter 'sourceOperationID'"
    assert "specificationName" in params, "Missing parameter 'specificationName'"
    assert "sourceOperationName" in params, "Missing parameter 'sourceOperationName'"

def test_traceabilitymodel::trace_has_sourceOperationID():
    assert hasattr(traceabilitymodel::Trace, "sourceOperationID")
    descriptor = None
    for klass in traceabilitymodel::Trace.__mro__:
        if "sourceOperationID" in klass.__dict__:
            descriptor = klass.__dict__["sourceOperationID"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::trace_has_specificationName():
    assert hasattr(traceabilitymodel::Trace, "specificationName")
    descriptor = None
    for klass in traceabilitymodel::Trace.__mro__:
        if "specificationName" in klass.__dict__:
            descriptor = klass.__dict__["specificationName"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::trace_has_sourceOperationName():
    assert hasattr(traceabilitymodel::Trace, "sourceOperationName")
    descriptor = None
    for klass in traceabilitymodel::Trace.__mro__:
        if "sourceOperationName" in klass.__dict__:
            descriptor = klass.__dict__["sourceOperationName"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::metamodel_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::MetaModel)


def test_traceabilitymodel::metamodel_constructor_exists():
    assert callable(traceabilitymodel::MetaModel.__init__)


def test_traceabilitymodel::metamodel_constructor_args():
    sig = inspect.signature(traceabilitymodel::MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nsUri" in params, "Missing parameter 'nsUri'"

def test_traceabilitymodel::metamodel_has_name():
    assert hasattr(traceabilitymodel::MetaModel, "name")
    descriptor = None
    for klass in traceabilitymodel::MetaModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::metamodel_has_nsUri():
    assert hasattr(traceabilitymodel::MetaModel, "nsUri")
    descriptor = None
    for klass in traceabilitymodel::MetaModel.__mro__:
        if "nsUri" in klass.__dict__:
            descriptor = klass.__dict__["nsUri"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::modelelementref_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::ModelElementRef)


def test_traceabilitymodel::modelelementref_constructor_exists():
    assert callable(traceabilitymodel::ModelElementRef.__init__)


def test_traceabilitymodel::modelelementref_constructor_args():
    sig = inspect.signature(traceabilitymodel::ModelElementRef.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "uri" in params, "Missing parameter 'uri'"
    assert "featureRef" in params, "Missing parameter 'featureRef'"
    assert "name" in params, "Missing parameter 'name'"

def test_traceabilitymodel::modelelementref_has_ID():
    assert hasattr(traceabilitymodel::ModelElementRef, "ID")
    descriptor = None
    for klass in traceabilitymodel::ModelElementRef.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::modelelementref_has_uri():
    assert hasattr(traceabilitymodel::ModelElementRef, "uri")
    descriptor = None
    for klass in traceabilitymodel::ModelElementRef.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::modelelementref_has_featureRef():
    assert hasattr(traceabilitymodel::ModelElementRef, "featureRef")
    descriptor = None
    for klass in traceabilitymodel::ModelElementRef.__mro__:
        if "featureRef" in klass.__dict__:
            descriptor = klass.__dict__["featureRef"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::modelelementref_has_name():
    assert hasattr(traceabilitymodel::ModelElementRef, "name")
    descriptor = None
    for klass in traceabilitymodel::ModelElementRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::file_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::File)


def test_traceabilitymodel::file_constructor_exists():
    assert callable(traceabilitymodel::File.__init__)


def test_traceabilitymodel::file_constructor_args():
    sig = inspect.signature(traceabilitymodel::File.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_traceabilitymodel::file_has_URI():
    assert hasattr(traceabilitymodel::File, "URI")
    descriptor = None
    for klass in traceabilitymodel::File.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::file_has_ID():
    assert hasattr(traceabilitymodel::File, "ID")
    descriptor = None
    for klass in traceabilitymodel::File.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_traceabilitymodel::file_has_name():
    assert hasattr(traceabilitymodel::File, "name")
    descriptor = None
    for klass in traceabilitymodel::File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_traceabilitymodel::tracemodel_is_not_abstract():
    assert not inspect.isabstract(traceabilitymodel::TraceModel)


def test_traceabilitymodel::tracemodel_constructor_exists():
    assert callable(traceabilitymodel::TraceModel.__init__)


def test_traceabilitymodel::tracemodel_constructor_args():
    sig = inspect.signature(traceabilitymodel::TraceModel.__init__)
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
traceabilitymodel::Block_strategy = st.builds(
    traceabilitymodel::Block,
    endLine=
        safe_text,
    startColumn=
        safe_text,
    endColumn=
        safe_text,
    startPos=
        safe_text,
    endPos=
        safe_text,
    startLine=
        safe_text,
    ID=
        safe_text,
    protectedBlock=
        st.booleans()
)
traceabilitymodel::TraceableSegment_strategy = st.builds(
    traceabilitymodel::TraceableSegment,
    startColumn=
        safe_text,
    startLine=
        safe_text,
    startPos=
        safe_text,
    endColumn=
        safe_text,
    endLine=
        safe_text,
    endPos=
        safe_text
)
traceabilitymodel::Trace_strategy = st.builds(
    traceabilitymodel::Trace,
    sourceOperationID=
        safe_text,
    specificationName=
        safe_text,
    sourceOperationName=
        safe_text
)
traceabilitymodel::MetaModel_strategy = st.builds(
    traceabilitymodel::MetaModel,
    name=
        safe_text,
    nsUri=
        safe_text
)
traceabilitymodel::ModelElementRef_strategy = st.builds(
    traceabilitymodel::ModelElementRef,
    ID=
        safe_text,
    uri=
        safe_text,
    featureRef=
        safe_text,
    name=
        safe_text
)
traceabilitymodel::File_strategy = st.builds(
    traceabilitymodel::File,
    URI=
        safe_text,
    ID=
        safe_text,
    name=
        safe_text
)
traceabilitymodel::TraceModel_strategy = st.builds(
    traceabilitymodel::TraceModel,
)

@given(instance=traceabilitymodel::Block_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::block_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::Block)

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endLine_type(instance):
    assert isinstance(instance.endLine, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startColumn_type(instance):
    assert isinstance(instance.startColumn, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endColumn_type(instance):
    assert isinstance(instance.endColumn, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startPos_type(instance):
    assert isinstance(instance.startPos, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startPos_setter(instance):
    original = instance.startPos
    instance.startPos = original
    assert instance.startPos == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endPos_type(instance):
    assert isinstance(instance.endPos, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_endPos_setter(instance):
    original = instance.endPos
    instance.endPos = original
    assert instance.endPos == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startLine_type(instance):
    assert isinstance(instance.startLine, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_protectedBlock_type(instance):
    assert isinstance(instance.protectedBlock, bool)


@given(instance=traceabilitymodel::Block_strategy)
def test_traceabilitymodel::block_protectedBlock_setter(instance):
    original = instance.protectedBlock
    instance.protectedBlock = original
    assert instance.protectedBlock == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::traceablesegment_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::TraceableSegment)

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startColumn_type(instance):
    assert isinstance(instance.startColumn, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startLine_type(instance):
    assert isinstance(instance.startLine, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startPos_type(instance):
    assert isinstance(instance.startPos, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_startPos_setter(instance):
    original = instance.startPos
    instance.startPos = original
    assert instance.startPos == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endColumn_type(instance):
    assert isinstance(instance.endColumn, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endLine_type(instance):
    assert isinstance(instance.endLine, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endPos_type(instance):
    assert isinstance(instance.endPos, str)


@given(instance=traceabilitymodel::TraceableSegment_strategy)
def test_traceabilitymodel::traceablesegment_endPos_setter(instance):
    original = instance.endPos
    instance.endPos = original
    assert instance.endPos == original

@given(instance=traceabilitymodel::Trace_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::trace_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::Trace)

@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_sourceOperationID_type(instance):
    assert isinstance(instance.sourceOperationID, str)


@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_sourceOperationID_setter(instance):
    original = instance.sourceOperationID
    instance.sourceOperationID = original
    assert instance.sourceOperationID == original

@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_specificationName_type(instance):
    assert isinstance(instance.specificationName, str)


@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_specificationName_setter(instance):
    original = instance.specificationName
    instance.specificationName = original
    assert instance.specificationName == original

@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_sourceOperationName_type(instance):
    assert isinstance(instance.sourceOperationName, str)


@given(instance=traceabilitymodel::Trace_strategy)
def test_traceabilitymodel::trace_sourceOperationName_setter(instance):
    original = instance.sourceOperationName
    instance.sourceOperationName = original
    assert instance.sourceOperationName == original

@given(instance=traceabilitymodel::MetaModel_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::metamodel_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::MetaModel)

@given(instance=traceabilitymodel::MetaModel_strategy)
def test_traceabilitymodel::metamodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traceabilitymodel::MetaModel_strategy)
def test_traceabilitymodel::metamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=traceabilitymodel::MetaModel_strategy)
def test_traceabilitymodel::metamodel_nsUri_type(instance):
    assert isinstance(instance.nsUri, str)


@given(instance=traceabilitymodel::MetaModel_strategy)
def test_traceabilitymodel::metamodel_nsUri_setter(instance):
    original = instance.nsUri
    instance.nsUri = original
    assert instance.nsUri == original

@given(instance=traceabilitymodel::ModelElementRef_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::modelelementref_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::ModelElementRef)

@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_featureRef_type(instance):
    assert isinstance(instance.featureRef, str)


@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_featureRef_setter(instance):
    original = instance.featureRef
    instance.featureRef = original
    assert instance.featureRef == original

@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traceabilitymodel::ModelElementRef_strategy)
def test_traceabilitymodel::modelelementref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=traceabilitymodel::File_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::file_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::File)

@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traceabilitymodel::File_strategy)
def test_traceabilitymodel::file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=traceabilitymodel::TraceModel_strategy)
@settings(max_examples=50)
def test_traceabilitymodel::tracemodel_instantiation(instance):
    assert isinstance(instance, traceabilitymodel::TraceModel)

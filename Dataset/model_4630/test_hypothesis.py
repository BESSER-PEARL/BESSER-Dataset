import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TBasicMessageMapping,
    TMessageExtremity,
    TSourceTargetMessageMapping,
    sequence_template_TCreationMessageMapping,
    sequence_template_TDestructionMessageMapping,
    sequence_template_TBasicMessageMapping,
    TConditionalMessageStyle,
    TMessageStyle,
    TAbstractMapping,
    sequence_template_TMessageMapping,
    TExecutionStyle,
    TConditionalExecutionStyle,
    sequence_template_TMessageExtremity,
    ColorDescription,
    TConditionalLifelineStyle,
    TLifelineStyle,
    style_NodeStyleDescription,
    TExecutionMapping,
    template_TMessageExtremity,
    template_TAbstractMapping,
    sequence_template_TExecutionMapping,
    sequence_template_TLifelineMapping,
    sequence_ordering_InstanceRolesOrdering,
    SingleEventEnd,
    TMessageMapping,
    sequence_template_TSourceTargetMessageMapping,
    sequence_template_TReturnMessageMapping,
    TLifelineMapping,
    template_TTransformer,
    description_RepresentationTemplate,
    sequence_template_TSequenceDiagram,
    TTransformer,
    sequence_template_TLifelineStyle,
    sequence_template_TConditionalMessageStyle,
    sequence_template_TConditionalLifelineStyle,
    sequence_template_TExecutionStyle,
    sequence_template_TConditionalExecutionStyle,
    sequence_template_TMessageStyle,
    sequence_template_TAbstractMapping,
    template_sequence_EObject,
    sequence_template_TTransformer,
    ordering_sequence_EObject,
    sequence_ordering_EventEnd,
    EventEnd,
    sequence_ordering_SingleEventEnd,
    sequence_ordering_CompoundEventEnd,
    ordering_sequence_SequenceDDiagram,
    sequence_ordering_EventEndsOrdering,
    InstanceRoleMapping,
    tool_InitialOperation,
    tool_CoveringElementCreationTool,
    tool_AbstractToolDescription,
    sequence_tool_CoveringElementCreationTool,
    tool_OrderedElementCreationTool,
    tool_EdgeCreationDescription,
    tool_ContainerCreationDescription,
    tool_ElementVariable,
    tool_SequenceDiagramToolDescription,
    sequence_tool_ReorderTool,
    sequence_tool_CombinedFragmentCreationTool,
    sequence_tool_LifelineCreationTool,
    sequence_tool_InteractionUseCreationTool,
    sequence_tool_InstanceRoleReorderTool,
    sequence_tool_OperandCreationTool,
    sequence_tool_MessageCreationTool,
    tool_NodeCreationDescription,
    sequence_tool_StateCreationTool,
    sequence_tool_ExecutionCreationTool,
    sequence_tool_ObservationPointCreationTool,
    sequence_tool_InstanceRoleCreationTool,
    CoveredLifelinesVariable,
    MessageMapping,
    sequence_description_CreationMessageMapping,
    sequence_description_DestructionMessageMapping,
    sequence_description_ReturnMessageMapping,
    sequence_description_BasicMessageMapping,
    MessageEndVariable,
    description_EventMapping,
    sequence_tool_OrderedElementCreationTool,
    description_EdgeMapping,
    sequence_description_MessageMapping,
    sequence_tool_SequenceDiagramToolDescription,
    FrameMapping,
    sequence_description_CombinedFragmentMapping,
    sequence_description_InteractionUseMapping,
    description_ContainerMapping,
    AbstractVariable,
    sequence_description_MessageEndVariable,
    sequence_description_CoveredLifelinesVariable,
    EventMapping,
    sequence_description_DelimitedEventMapping,
    sequence_description_EventMapping,
    NodeMapping,
    sequence_description_ObservationPointMapping,
    sequence_description_EndOfLifeMapping,
    sequence_description_InstanceRoleMapping,
    DiagramDescription,
    sequence_description_SequenceDiagramDescription,
    description_DelimitedEventMapping,
    sequence_description_OperandMapping,
    sequence_description_FrameMapping,
    description_NodeMapping,
    sequence_description_StateMapping,
    sequence_description_ExecutionMapping,
    DSemanticDiagram,
    sequence_SequenceDDiagram,
    InstanceRolesOrdering,
    EventEndsOrdering,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tbasicmessagemapping_is_not_abstract():
    assert not inspect.isabstract(TBasicMessageMapping)


def test_tbasicmessagemapping_constructor_exists():
    assert callable(TBasicMessageMapping.__init__)


def test_tbasicmessagemapping_constructor_args():
    sig = inspect.signature(TBasicMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_tmessageextremity_is_not_abstract():
    assert not inspect.isabstract(TMessageExtremity)


def test_tmessageextremity_constructor_exists():
    assert callable(TMessageExtremity.__init__)


def test_tmessageextremity_constructor_args():
    sig = inspect.signature(TMessageExtremity.__init__)
    params = list(sig.parameters.keys())



def test_tsourcetargetmessagemapping_is_not_abstract():
    assert not inspect.isabstract(TSourceTargetMessageMapping)


def test_tsourcetargetmessagemapping_constructor_exists():
    assert callable(TSourceTargetMessageMapping.__init__)


def test_tsourcetargetmessagemapping_constructor_args():
    sig = inspect.signature(TSourceTargetMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tcreationmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TCreationMessageMapping)


def test_sequence_template_tcreationmessagemapping_constructor_exists():
    assert callable(sequence_template_TCreationMessageMapping.__init__)


def test_sequence_template_tcreationmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TCreationMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tdestructionmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TDestructionMessageMapping)


def test_sequence_template_tdestructionmessagemapping_constructor_exists():
    assert callable(sequence_template_TDestructionMessageMapping.__init__)


def test_sequence_template_tdestructionmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TDestructionMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tbasicmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TBasicMessageMapping)


def test_sequence_template_tbasicmessagemapping_constructor_exists():
    assert callable(sequence_template_TBasicMessageMapping.__init__)


def test_sequence_template_tbasicmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TBasicMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_tconditionalmessagestyle_is_not_abstract():
    assert not inspect.isabstract(TConditionalMessageStyle)


def test_tconditionalmessagestyle_constructor_exists():
    assert callable(TConditionalMessageStyle.__init__)


def test_tconditionalmessagestyle_constructor_args():
    sig = inspect.signature(TConditionalMessageStyle.__init__)
    params = list(sig.parameters.keys())



def test_tmessagestyle_is_not_abstract():
    assert not inspect.isabstract(TMessageStyle)


def test_tmessagestyle_constructor_exists():
    assert callable(TMessageStyle.__init__)


def test_tmessagestyle_constructor_args():
    sig = inspect.signature(TMessageStyle.__init__)
    params = list(sig.parameters.keys())



def test_tabstractmapping_is_not_abstract():
    assert not inspect.isabstract(TAbstractMapping)


def test_tabstractmapping_constructor_exists():
    assert callable(TAbstractMapping.__init__)


def test_tabstractmapping_constructor_args():
    sig = inspect.signature(TAbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TMessageMapping)


def test_sequence_template_tmessagemapping_constructor_exists():
    assert callable(sequence_template_TMessageMapping.__init__)


def test_sequence_template_tmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "receivingEndFinderExpression" in params, "Missing parameter 'receivingEndFinderExpression'"
    assert "sendingEndFinderExpression" in params, "Missing parameter 'sendingEndFinderExpression'"

def test_sequence_template_tmessagemapping_has_receivingEndFinderExpression():
    assert hasattr(sequence_template_TMessageMapping, "receivingEndFinderExpression")
    descriptor = None
    for klass in sequence_template_TMessageMapping.__mro__:
        if "receivingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["receivingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tmessagemapping_has_sendingEndFinderExpression():
    assert hasattr(sequence_template_TMessageMapping, "sendingEndFinderExpression")
    descriptor = None
    for klass in sequence_template_TMessageMapping.__mro__:
        if "sendingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sendingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_texecutionstyle_is_not_abstract():
    assert not inspect.isabstract(TExecutionStyle)


def test_texecutionstyle_constructor_exists():
    assert callable(TExecutionStyle.__init__)


def test_texecutionstyle_constructor_args():
    sig = inspect.signature(TExecutionStyle.__init__)
    params = list(sig.parameters.keys())



def test_tconditionalexecutionstyle_is_not_abstract():
    assert not inspect.isabstract(TConditionalExecutionStyle)


def test_tconditionalexecutionstyle_constructor_exists():
    assert callable(TConditionalExecutionStyle.__init__)


def test_tconditionalexecutionstyle_constructor_args():
    sig = inspect.signature(TConditionalExecutionStyle.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tmessageextremity_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TMessageExtremity)


def test_sequence_template_tmessageextremity_constructor_exists():
    assert callable(sequence_template_TMessageExtremity.__init__)


def test_sequence_template_tmessageextremity_constructor_args():
    sig = inspect.signature(sequence_template_TMessageExtremity.__init__)
    params = list(sig.parameters.keys())



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_tconditionallifelinestyle_is_not_abstract():
    assert not inspect.isabstract(TConditionalLifelineStyle)


def test_tconditionallifelinestyle_constructor_exists():
    assert callable(TConditionalLifelineStyle.__init__)


def test_tconditionallifelinestyle_constructor_args():
    sig = inspect.signature(TConditionalLifelineStyle.__init__)
    params = list(sig.parameters.keys())



def test_tlifelinestyle_is_not_abstract():
    assert not inspect.isabstract(TLifelineStyle)


def test_tlifelinestyle_constructor_exists():
    assert callable(TLifelineStyle.__init__)


def test_tlifelinestyle_constructor_args():
    sig = inspect.signature(TLifelineStyle.__init__)
    params = list(sig.parameters.keys())



def test_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_NodeStyleDescription)


def test_style_nodestyledescription_constructor_exists():
    assert callable(style_NodeStyleDescription.__init__)


def test_style_nodestyledescription_constructor_args():
    sig = inspect.signature(style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_texecutionmapping_is_not_abstract():
    assert not inspect.isabstract(TExecutionMapping)


def test_texecutionmapping_constructor_exists():
    assert callable(TExecutionMapping.__init__)


def test_texecutionmapping_constructor_args():
    sig = inspect.signature(TExecutionMapping.__init__)
    params = list(sig.parameters.keys())



def test_template_tmessageextremity_is_not_abstract():
    assert not inspect.isabstract(template_TMessageExtremity)


def test_template_tmessageextremity_constructor_exists():
    assert callable(template_TMessageExtremity.__init__)


def test_template_tmessageextremity_constructor_args():
    sig = inspect.signature(template_TMessageExtremity.__init__)
    params = list(sig.parameters.keys())



def test_template_tabstractmapping_is_not_abstract():
    assert not inspect.isabstract(template_TAbstractMapping)


def test_template_tabstractmapping_constructor_exists():
    assert callable(template_TAbstractMapping.__init__)


def test_template_tabstractmapping_constructor_args():
    sig = inspect.signature(template_TAbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_texecutionmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TExecutionMapping)


def test_sequence_template_texecutionmapping_constructor_exists():
    assert callable(sequence_template_TExecutionMapping.__init__)


def test_sequence_template_texecutionmapping_constructor_args():
    sig = inspect.signature(sequence_template_TExecutionMapping.__init__)
    params = list(sig.parameters.keys())
    assert "recursive" in params, "Missing parameter 'recursive'"
    assert "finishingEndFinderExpression" in params, "Missing parameter 'finishingEndFinderExpression'"
    assert "startingEndFinderExpression" in params, "Missing parameter 'startingEndFinderExpression'"

def test_sequence_template_texecutionmapping_has_recursive():
    assert hasattr(sequence_template_TExecutionMapping, "recursive")
    descriptor = None
    for klass in sequence_template_TExecutionMapping.__mro__:
        if "recursive" in klass.__dict__:
            descriptor = klass.__dict__["recursive"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_texecutionmapping_has_finishingEndFinderExpression():
    assert hasattr(sequence_template_TExecutionMapping, "finishingEndFinderExpression")
    descriptor = None
    for klass in sequence_template_TExecutionMapping.__mro__:
        if "finishingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["finishingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_texecutionmapping_has_startingEndFinderExpression():
    assert hasattr(sequence_template_TExecutionMapping, "startingEndFinderExpression")
    descriptor = None
    for klass in sequence_template_TExecutionMapping.__mro__:
        if "startingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["startingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tlifelinemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TLifelineMapping)


def test_sequence_template_tlifelinemapping_constructor_exists():
    assert callable(sequence_template_TLifelineMapping.__init__)


def test_sequence_template_tlifelinemapping_constructor_args():
    sig = inspect.signature(sequence_template_TLifelineMapping.__init__)
    params = list(sig.parameters.keys())
    assert "eolVisibleExpression" in params, "Missing parameter 'eolVisibleExpression'"

def test_sequence_template_tlifelinemapping_has_eolVisibleExpression():
    assert hasattr(sequence_template_TLifelineMapping, "eolVisibleExpression")
    descriptor = None
    for klass in sequence_template_TLifelineMapping.__mro__:
        if "eolVisibleExpression" in klass.__dict__:
            descriptor = klass.__dict__["eolVisibleExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_ordering_instancerolesordering_is_not_abstract():
    assert not inspect.isabstract(sequence_ordering_InstanceRolesOrdering)


def test_sequence_ordering_instancerolesordering_constructor_exists():
    assert callable(sequence_ordering_InstanceRolesOrdering.__init__)


def test_sequence_ordering_instancerolesordering_constructor_args():
    sig = inspect.signature(sequence_ordering_InstanceRolesOrdering.__init__)
    params = list(sig.parameters.keys())



def test_singleeventend_is_not_abstract():
    assert not inspect.isabstract(SingleEventEnd)


def test_singleeventend_constructor_exists():
    assert callable(SingleEventEnd.__init__)


def test_singleeventend_constructor_args():
    sig = inspect.signature(SingleEventEnd.__init__)
    params = list(sig.parameters.keys())



def test_tmessagemapping_is_not_abstract():
    assert not inspect.isabstract(TMessageMapping)


def test_tmessagemapping_constructor_exists():
    assert callable(TMessageMapping.__init__)


def test_tmessagemapping_constructor_args():
    sig = inspect.signature(TMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tsourcetargetmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TSourceTargetMessageMapping)


def test_sequence_template_tsourcetargetmessagemapping_constructor_exists():
    assert callable(sequence_template_TSourceTargetMessageMapping.__init__)


def test_sequence_template_tsourcetargetmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TSourceTargetMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"

def test_sequence_template_tsourcetargetmessagemapping_has_sourceFinderExpression():
    assert hasattr(sequence_template_TSourceTargetMessageMapping, "sourceFinderExpression")
    descriptor = None
    for klass in sequence_template_TSourceTargetMessageMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tsourcetargetmessagemapping_has_targetFinderExpression():
    assert hasattr(sequence_template_TSourceTargetMessageMapping, "targetFinderExpression")
    descriptor = None
    for klass in sequence_template_TSourceTargetMessageMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tsourcetargetmessagemapping_has_useDomainElement():
    assert hasattr(sequence_template_TSourceTargetMessageMapping, "useDomainElement")
    descriptor = None
    for klass in sequence_template_TSourceTargetMessageMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_treturnmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TReturnMessageMapping)


def test_sequence_template_treturnmessagemapping_constructor_exists():
    assert callable(sequence_template_TReturnMessageMapping.__init__)


def test_sequence_template_treturnmessagemapping_constructor_args():
    sig = inspect.signature(sequence_template_TReturnMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "invocationMessageFinderExpression" in params, "Missing parameter 'invocationMessageFinderExpression'"

def test_sequence_template_treturnmessagemapping_has_invocationMessageFinderExpression():
    assert hasattr(sequence_template_TReturnMessageMapping, "invocationMessageFinderExpression")
    descriptor = None
    for klass in sequence_template_TReturnMessageMapping.__mro__:
        if "invocationMessageFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["invocationMessageFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_tlifelinemapping_is_not_abstract():
    assert not inspect.isabstract(TLifelineMapping)


def test_tlifelinemapping_constructor_exists():
    assert callable(TLifelineMapping.__init__)


def test_tlifelinemapping_constructor_args():
    sig = inspect.signature(TLifelineMapping.__init__)
    params = list(sig.parameters.keys())



def test_template_ttransformer_is_not_abstract():
    assert not inspect.isabstract(template_TTransformer)


def test_template_ttransformer_constructor_exists():
    assert callable(template_TTransformer.__init__)


def test_template_ttransformer_constructor_args():
    sig = inspect.signature(template_TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_description_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationTemplate)


def test_description_representationtemplate_constructor_exists():
    assert callable(description_RepresentationTemplate.__init__)


def test_description_representationtemplate_constructor_args():
    sig = inspect.signature(description_RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tsequencediagram_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TSequenceDiagram)


def test_sequence_template_tsequencediagram_constructor_exists():
    assert callable(sequence_template_TSequenceDiagram.__init__)


def test_sequence_template_tsequencediagram_constructor_args():
    sig = inspect.signature(sequence_template_TSequenceDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "endsOrdering" in params, "Missing parameter 'endsOrdering'"

def test_sequence_template_tsequencediagram_has_domainClass():
    assert hasattr(sequence_template_TSequenceDiagram, "domainClass")
    descriptor = None
    for klass in sequence_template_TSequenceDiagram.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tsequencediagram_has_endsOrdering():
    assert hasattr(sequence_template_TSequenceDiagram, "endsOrdering")
    descriptor = None
    for klass in sequence_template_TSequenceDiagram.__mro__:
        if "endsOrdering" in klass.__dict__:
            descriptor = klass.__dict__["endsOrdering"]
            break
    assert isinstance(descriptor, property)



def test_ttransformer_is_not_abstract():
    assert not inspect.isabstract(TTransformer)


def test_ttransformer_constructor_exists():
    assert callable(TTransformer.__init__)


def test_ttransformer_constructor_args():
    sig = inspect.signature(TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_tlifelinestyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TLifelineStyle)


def test_sequence_template_tlifelinestyle_constructor_exists():
    assert callable(sequence_template_TLifelineStyle.__init__)


def test_sequence_template_tlifelinestyle_constructor_args():
    sig = inspect.signature(sequence_template_TLifelineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lifelineWidthComputationExpression" in params, "Missing parameter 'lifelineWidthComputationExpression'"

def test_sequence_template_tlifelinestyle_has_lifelineWidthComputationExpression():
    assert hasattr(sequence_template_TLifelineStyle, "lifelineWidthComputationExpression")
    descriptor = None
    for klass in sequence_template_TLifelineStyle.__mro__:
        if "lifelineWidthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["lifelineWidthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tconditionalmessagestyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TConditionalMessageStyle)


def test_sequence_template_tconditionalmessagestyle_constructor_exists():
    assert callable(sequence_template_TConditionalMessageStyle.__init__)


def test_sequence_template_tconditionalmessagestyle_constructor_args():
    sig = inspect.signature(sequence_template_TConditionalMessageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence_template_tconditionalmessagestyle_has_predicateExpression():
    assert hasattr(sequence_template_TConditionalMessageStyle, "predicateExpression")
    descriptor = None
    for klass in sequence_template_TConditionalMessageStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tconditionallifelinestyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TConditionalLifelineStyle)


def test_sequence_template_tconditionallifelinestyle_constructor_exists():
    assert callable(sequence_template_TConditionalLifelineStyle.__init__)


def test_sequence_template_tconditionallifelinestyle_constructor_args():
    sig = inspect.signature(sequence_template_TConditionalLifelineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence_template_tconditionallifelinestyle_has_predicateExpression():
    assert hasattr(sequence_template_TConditionalLifelineStyle, "predicateExpression")
    descriptor = None
    for klass in sequence_template_TConditionalLifelineStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_texecutionstyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TExecutionStyle)


def test_sequence_template_texecutionstyle_constructor_exists():
    assert callable(sequence_template_TExecutionStyle.__init__)


def test_sequence_template_texecutionstyle_constructor_args():
    sig = inspect.signature(sequence_template_TExecutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_sequence_template_texecutionstyle_has_borderSizeComputationExpression():
    assert hasattr(sequence_template_TExecutionStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in sequence_template_TExecutionStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tconditionalexecutionstyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TConditionalExecutionStyle)


def test_sequence_template_tconditionalexecutionstyle_constructor_exists():
    assert callable(sequence_template_TConditionalExecutionStyle.__init__)


def test_sequence_template_tconditionalexecutionstyle_constructor_args():
    sig = inspect.signature(sequence_template_TConditionalExecutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence_template_tconditionalexecutionstyle_has_predicateExpression():
    assert hasattr(sequence_template_TConditionalExecutionStyle, "predicateExpression")
    descriptor = None
    for klass in sequence_template_TConditionalExecutionStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tmessagestyle_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TMessageStyle)


def test_sequence_template_tmessagestyle_constructor_exists():
    assert callable(sequence_template_TMessageStyle.__init__)


def test_sequence_template_tmessagestyle_constructor_args():
    sig = inspect.signature(sequence_template_TMessageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_sequence_template_tmessagestyle_has_sourceArrow():
    assert hasattr(sequence_template_TMessageStyle, "sourceArrow")
    descriptor = None
    for klass in sequence_template_TMessageStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tmessagestyle_has_labelExpression():
    assert hasattr(sequence_template_TMessageStyle, "labelExpression")
    descriptor = None
    for klass in sequence_template_TMessageStyle.__mro__:
        if "labelExpression" in klass.__dict__:
            descriptor = klass.__dict__["labelExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tmessagestyle_has_targetArrow():
    assert hasattr(sequence_template_TMessageStyle, "targetArrow")
    descriptor = None
    for klass in sequence_template_TMessageStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tmessagestyle_has_lineStyle():
    assert hasattr(sequence_template_TMessageStyle, "lineStyle")
    descriptor = None
    for klass in sequence_template_TMessageStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_sequence_template_tabstractmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TAbstractMapping)


def test_sequence_template_tabstractmapping_constructor_exists():
    assert callable(sequence_template_TAbstractMapping.__init__)


def test_sequence_template_tabstractmapping_constructor_args():
    sig = inspect.signature(sequence_template_TAbstractMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "name" in params, "Missing parameter 'name'"

def test_sequence_template_tabstractmapping_has_domainClass():
    assert hasattr(sequence_template_TAbstractMapping, "domainClass")
    descriptor = None
    for klass in sequence_template_TAbstractMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tabstractmapping_has_semanticCandidatesExpression():
    assert hasattr(sequence_template_TAbstractMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in sequence_template_TAbstractMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_template_tabstractmapping_has_name():
    assert hasattr(sequence_template_TAbstractMapping, "name")
    descriptor = None
    for klass in sequence_template_TAbstractMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_template_sequence_eobject_is_not_abstract():
    assert not inspect.isabstract(template_sequence_EObject)


def test_template_sequence_eobject_constructor_exists():
    assert callable(template_sequence_EObject.__init__)


def test_template_sequence_eobject_constructor_args():
    sig = inspect.signature(template_sequence_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sequence_template_ttransformer_is_not_abstract():
    assert not inspect.isabstract(sequence_template_TTransformer)


def test_sequence_template_ttransformer_constructor_exists():
    assert callable(sequence_template_TTransformer.__init__)


def test_sequence_template_ttransformer_constructor_args():
    sig = inspect.signature(sequence_template_TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_ordering_sequence_eobject_is_not_abstract():
    assert not inspect.isabstract(ordering_sequence_EObject)


def test_ordering_sequence_eobject_constructor_exists():
    assert callable(ordering_sequence_EObject.__init__)


def test_ordering_sequence_eobject_constructor_args():
    sig = inspect.signature(ordering_sequence_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sequence_ordering_eventend_is_not_abstract():
    assert not inspect.isabstract(sequence_ordering_EventEnd)


def test_sequence_ordering_eventend_constructor_exists():
    assert callable(sequence_ordering_EventEnd.__init__)


def test_sequence_ordering_eventend_constructor_args():
    sig = inspect.signature(sequence_ordering_EventEnd.__init__)
    params = list(sig.parameters.keys())



def test_eventend_is_not_abstract():
    assert not inspect.isabstract(EventEnd)


def test_eventend_constructor_exists():
    assert callable(EventEnd.__init__)


def test_eventend_constructor_args():
    sig = inspect.signature(EventEnd.__init__)
    params = list(sig.parameters.keys())



def test_sequence_ordering_singleeventend_is_not_abstract():
    assert not inspect.isabstract(sequence_ordering_SingleEventEnd)


def test_sequence_ordering_singleeventend_constructor_exists():
    assert callable(sequence_ordering_SingleEventEnd.__init__)


def test_sequence_ordering_singleeventend_constructor_args():
    sig = inspect.signature(sequence_ordering_SingleEventEnd.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_sequence_ordering_singleeventend_has_start():
    assert hasattr(sequence_ordering_SingleEventEnd, "start")
    descriptor = None
    for klass in sequence_ordering_SingleEventEnd.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_sequence_ordering_compoundeventend_is_not_abstract():
    assert not inspect.isabstract(sequence_ordering_CompoundEventEnd)


def test_sequence_ordering_compoundeventend_constructor_exists():
    assert callable(sequence_ordering_CompoundEventEnd.__init__)


def test_sequence_ordering_compoundeventend_constructor_args():
    sig = inspect.signature(sequence_ordering_CompoundEventEnd.__init__)
    params = list(sig.parameters.keys())



def test_ordering_sequence_sequenceddiagram_is_not_abstract():
    assert not inspect.isabstract(ordering_sequence_SequenceDDiagram)


def test_ordering_sequence_sequenceddiagram_constructor_exists():
    assert callable(ordering_sequence_SequenceDDiagram.__init__)


def test_ordering_sequence_sequenceddiagram_constructor_args():
    sig = inspect.signature(ordering_sequence_SequenceDDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sequence_ordering_eventendsordering_is_not_abstract():
    assert not inspect.isabstract(sequence_ordering_EventEndsOrdering)


def test_sequence_ordering_eventendsordering_constructor_exists():
    assert callable(sequence_ordering_EventEndsOrdering.__init__)


def test_sequence_ordering_eventendsordering_constructor_args():
    sig = inspect.signature(sequence_ordering_EventEndsOrdering.__init__)
    params = list(sig.parameters.keys())



def test_instancerolemapping_is_not_abstract():
    assert not inspect.isabstract(InstanceRoleMapping)


def test_instancerolemapping_constructor_exists():
    assert callable(InstanceRoleMapping.__init__)


def test_instancerolemapping_constructor_args():
    sig = inspect.signature(InstanceRoleMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_coveringelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(tool_CoveringElementCreationTool)


def test_tool_coveringelementcreationtool_constructor_exists():
    assert callable(tool_CoveringElementCreationTool.__init__)


def test_tool_coveringelementcreationtool_constructor_args():
    sig = inspect.signature(tool_CoveringElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_coveringelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_CoveringElementCreationTool)


def test_sequence_tool_coveringelementcreationtool_constructor_exists():
    assert callable(sequence_tool_CoveringElementCreationTool.__init__)


def test_sequence_tool_coveringelementcreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_CoveringElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool_orderedelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(tool_OrderedElementCreationTool)


def test_tool_orderedelementcreationtool_constructor_exists():
    assert callable(tool_OrderedElementCreationTool.__init__)


def test_tool_orderedelementcreationtool_constructor_args():
    sig = inspect.signature(tool_OrderedElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool_edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_EdgeCreationDescription)


def test_tool_edgecreationdescription_constructor_exists():
    assert callable(tool_EdgeCreationDescription.__init__)


def test_tool_edgecreationdescription_constructor_args():
    sig = inspect.signature(tool_EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerCreationDescription)


def test_tool_containercreationdescription_constructor_exists():
    assert callable(tool_ContainerCreationDescription.__init__)


def test_tool_containercreationdescription_constructor_args():
    sig = inspect.signature(tool_ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementVariable)


def test_tool_elementvariable_constructor_exists():
    assert callable(tool_ElementVariable.__init__)


def test_tool_elementvariable_constructor_args():
    sig = inspect.signature(tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_sequencediagramtooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_SequenceDiagramToolDescription)


def test_tool_sequencediagramtooldescription_constructor_exists():
    assert callable(tool_SequenceDiagramToolDescription.__init__)


def test_tool_sequencediagramtooldescription_constructor_args():
    sig = inspect.signature(tool_SequenceDiagramToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_reordertool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_ReorderTool)


def test_sequence_tool_reordertool_constructor_exists():
    assert callable(sequence_tool_ReorderTool.__init__)


def test_sequence_tool_reordertool_constructor_args():
    sig = inspect.signature(sequence_tool_ReorderTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_combinedfragmentcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_CombinedFragmentCreationTool)


def test_sequence_tool_combinedfragmentcreationtool_constructor_exists():
    assert callable(sequence_tool_CombinedFragmentCreationTool.__init__)


def test_sequence_tool_combinedfragmentcreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_CombinedFragmentCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_lifelinecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_LifelineCreationTool)


def test_sequence_tool_lifelinecreationtool_constructor_exists():
    assert callable(sequence_tool_LifelineCreationTool.__init__)


def test_sequence_tool_lifelinecreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_LifelineCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_interactionusecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_InteractionUseCreationTool)


def test_sequence_tool_interactionusecreationtool_constructor_exists():
    assert callable(sequence_tool_InteractionUseCreationTool.__init__)


def test_sequence_tool_interactionusecreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_InteractionUseCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_instancerolereordertool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_InstanceRoleReorderTool)


def test_sequence_tool_instancerolereordertool_constructor_exists():
    assert callable(sequence_tool_InstanceRoleReorderTool.__init__)


def test_sequence_tool_instancerolereordertool_constructor_args():
    sig = inspect.signature(sequence_tool_InstanceRoleReorderTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_operandcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_OperandCreationTool)


def test_sequence_tool_operandcreationtool_constructor_exists():
    assert callable(sequence_tool_OperandCreationTool.__init__)


def test_sequence_tool_operandcreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_OperandCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_messagecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_MessageCreationTool)


def test_sequence_tool_messagecreationtool_constructor_exists():
    assert callable(sequence_tool_MessageCreationTool.__init__)


def test_sequence_tool_messagecreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_MessageCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool_nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_NodeCreationDescription)


def test_tool_nodecreationdescription_constructor_exists():
    assert callable(tool_NodeCreationDescription.__init__)


def test_tool_nodecreationdescription_constructor_args():
    sig = inspect.signature(tool_NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_statecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_StateCreationTool)


def test_sequence_tool_statecreationtool_constructor_exists():
    assert callable(sequence_tool_StateCreationTool.__init__)


def test_sequence_tool_statecreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_StateCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_executioncreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_ExecutionCreationTool)


def test_sequence_tool_executioncreationtool_constructor_exists():
    assert callable(sequence_tool_ExecutionCreationTool.__init__)


def test_sequence_tool_executioncreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_ExecutionCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_observationpointcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_ObservationPointCreationTool)


def test_sequence_tool_observationpointcreationtool_constructor_exists():
    assert callable(sequence_tool_ObservationPointCreationTool.__init__)


def test_sequence_tool_observationpointcreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_ObservationPointCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_instancerolecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_InstanceRoleCreationTool)


def test_sequence_tool_instancerolecreationtool_constructor_exists():
    assert callable(sequence_tool_InstanceRoleCreationTool.__init__)


def test_sequence_tool_instancerolecreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_InstanceRoleCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_coveredlifelinesvariable_is_not_abstract():
    assert not inspect.isabstract(CoveredLifelinesVariable)


def test_coveredlifelinesvariable_constructor_exists():
    assert callable(CoveredLifelinesVariable.__init__)


def test_coveredlifelinesvariable_constructor_args():
    sig = inspect.signature(CoveredLifelinesVariable.__init__)
    params = list(sig.parameters.keys())



def test_messagemapping_is_not_abstract():
    assert not inspect.isabstract(MessageMapping)


def test_messagemapping_constructor_exists():
    assert callable(MessageMapping.__init__)


def test_messagemapping_constructor_args():
    sig = inspect.signature(MessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_creationmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_CreationMessageMapping)


def test_sequence_description_creationmessagemapping_constructor_exists():
    assert callable(sequence_description_CreationMessageMapping.__init__)


def test_sequence_description_creationmessagemapping_constructor_args():
    sig = inspect.signature(sequence_description_CreationMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_destructionmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_DestructionMessageMapping)


def test_sequence_description_destructionmessagemapping_constructor_exists():
    assert callable(sequence_description_DestructionMessageMapping.__init__)


def test_sequence_description_destructionmessagemapping_constructor_args():
    sig = inspect.signature(sequence_description_DestructionMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_returnmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_ReturnMessageMapping)


def test_sequence_description_returnmessagemapping_constructor_exists():
    assert callable(sequence_description_ReturnMessageMapping.__init__)


def test_sequence_description_returnmessagemapping_constructor_args():
    sig = inspect.signature(sequence_description_ReturnMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "invocationMessageFinderExpression" in params, "Missing parameter 'invocationMessageFinderExpression'"

def test_sequence_description_returnmessagemapping_has_invocationMessageFinderExpression():
    assert hasattr(sequence_description_ReturnMessageMapping, "invocationMessageFinderExpression")
    descriptor = None
    for klass in sequence_description_ReturnMessageMapping.__mro__:
        if "invocationMessageFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["invocationMessageFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_description_basicmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_BasicMessageMapping)


def test_sequence_description_basicmessagemapping_constructor_exists():
    assert callable(sequence_description_BasicMessageMapping.__init__)


def test_sequence_description_basicmessagemapping_constructor_args():
    sig = inspect.signature(sequence_description_BasicMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_messageendvariable_is_not_abstract():
    assert not inspect.isabstract(MessageEndVariable)


def test_messageendvariable_constructor_exists():
    assert callable(MessageEndVariable.__init__)


def test_messageendvariable_constructor_args():
    sig = inspect.signature(MessageEndVariable.__init__)
    params = list(sig.parameters.keys())



def test_description_eventmapping_is_not_abstract():
    assert not inspect.isabstract(description_EventMapping)


def test_description_eventmapping_constructor_exists():
    assert callable(description_EventMapping.__init__)


def test_description_eventmapping_constructor_args():
    sig = inspect.signature(description_EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_tool_orderedelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_OrderedElementCreationTool)


def test_sequence_tool_orderedelementcreationtool_constructor_exists():
    assert callable(sequence_tool_OrderedElementCreationTool.__init__)


def test_sequence_tool_orderedelementcreationtool_constructor_args():
    sig = inspect.signature(sequence_tool_OrderedElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_description_edgemapping_is_not_abstract():
    assert not inspect.isabstract(description_EdgeMapping)


def test_description_edgemapping_constructor_exists():
    assert callable(description_EdgeMapping.__init__)


def test_description_edgemapping_constructor_args():
    sig = inspect.signature(description_EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_messagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_MessageMapping)


def test_sequence_description_messagemapping_constructor_exists():
    assert callable(sequence_description_MessageMapping.__init__)


def test_sequence_description_messagemapping_constructor_args():
    sig = inspect.signature(sequence_description_MessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "sendingEndFinderExpression" in params, "Missing parameter 'sendingEndFinderExpression'"
    assert "receivingEndFinderExpression" in params, "Missing parameter 'receivingEndFinderExpression'"

def test_sequence_description_messagemapping_has_sendingEndFinderExpression():
    assert hasattr(sequence_description_MessageMapping, "sendingEndFinderExpression")
    descriptor = None
    for klass in sequence_description_MessageMapping.__mro__:
        if "sendingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sendingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_description_messagemapping_has_receivingEndFinderExpression():
    assert hasattr(sequence_description_MessageMapping, "receivingEndFinderExpression")
    descriptor = None
    for klass in sequence_description_MessageMapping.__mro__:
        if "receivingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["receivingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_tool_sequencediagramtooldescription_is_not_abstract():
    assert not inspect.isabstract(sequence_tool_SequenceDiagramToolDescription)


def test_sequence_tool_sequencediagramtooldescription_constructor_exists():
    assert callable(sequence_tool_SequenceDiagramToolDescription.__init__)


def test_sequence_tool_sequencediagramtooldescription_constructor_args():
    sig = inspect.signature(sequence_tool_SequenceDiagramToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_framemapping_is_not_abstract():
    assert not inspect.isabstract(FrameMapping)


def test_framemapping_constructor_exists():
    assert callable(FrameMapping.__init__)


def test_framemapping_constructor_args():
    sig = inspect.signature(FrameMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_combinedfragmentmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_CombinedFragmentMapping)


def test_sequence_description_combinedfragmentmapping_constructor_exists():
    assert callable(sequence_description_CombinedFragmentMapping.__init__)


def test_sequence_description_combinedfragmentmapping_constructor_args():
    sig = inspect.signature(sequence_description_CombinedFragmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_interactionusemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_InteractionUseMapping)


def test_sequence_description_interactionusemapping_constructor_exists():
    assert callable(sequence_description_InteractionUseMapping.__init__)


def test_sequence_description_interactionusemapping_constructor_args():
    sig = inspect.signature(sequence_description_InteractionUseMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(description_ContainerMapping)


def test_description_containermapping_constructor_exists():
    assert callable(description_ContainerMapping.__init__)


def test_description_containermapping_constructor_args():
    sig = inspect.signature(description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_messageendvariable_is_not_abstract():
    assert not inspect.isabstract(sequence_description_MessageEndVariable)


def test_sequence_description_messageendvariable_constructor_exists():
    assert callable(sequence_description_MessageEndVariable.__init__)


def test_sequence_description_messageendvariable_constructor_args():
    sig = inspect.signature(sequence_description_MessageEndVariable.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_coveredlifelinesvariable_is_not_abstract():
    assert not inspect.isabstract(sequence_description_CoveredLifelinesVariable)


def test_sequence_description_coveredlifelinesvariable_constructor_exists():
    assert callable(sequence_description_CoveredLifelinesVariable.__init__)


def test_sequence_description_coveredlifelinesvariable_constructor_args():
    sig = inspect.signature(sequence_description_CoveredLifelinesVariable.__init__)
    params = list(sig.parameters.keys())



def test_eventmapping_is_not_abstract():
    assert not inspect.isabstract(EventMapping)


def test_eventmapping_constructor_exists():
    assert callable(EventMapping.__init__)


def test_eventmapping_constructor_args():
    sig = inspect.signature(EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_delimitedeventmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_DelimitedEventMapping)


def test_sequence_description_delimitedeventmapping_constructor_exists():
    assert callable(sequence_description_DelimitedEventMapping.__init__)


def test_sequence_description_delimitedeventmapping_constructor_args():
    sig = inspect.signature(sequence_description_DelimitedEventMapping.__init__)
    params = list(sig.parameters.keys())
    assert "startingEndFinderExpression" in params, "Missing parameter 'startingEndFinderExpression'"
    assert "finishingEndFinderExpression" in params, "Missing parameter 'finishingEndFinderExpression'"

def test_sequence_description_delimitedeventmapping_has_startingEndFinderExpression():
    assert hasattr(sequence_description_DelimitedEventMapping, "startingEndFinderExpression")
    descriptor = None
    for klass in sequence_description_DelimitedEventMapping.__mro__:
        if "startingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["startingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_description_delimitedeventmapping_has_finishingEndFinderExpression():
    assert hasattr(sequence_description_DelimitedEventMapping, "finishingEndFinderExpression")
    descriptor = None
    for klass in sequence_description_DelimitedEventMapping.__mro__:
        if "finishingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["finishingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence_description_eventmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_EventMapping)


def test_sequence_description_eventmapping_constructor_exists():
    assert callable(sequence_description_EventMapping.__init__)


def test_sequence_description_eventmapping_constructor_args():
    sig = inspect.signature(sequence_description_EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_observationpointmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_ObservationPointMapping)


def test_sequence_description_observationpointmapping_constructor_exists():
    assert callable(sequence_description_ObservationPointMapping.__init__)


def test_sequence_description_observationpointmapping_constructor_args():
    sig = inspect.signature(sequence_description_ObservationPointMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_endoflifemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_EndOfLifeMapping)


def test_sequence_description_endoflifemapping_constructor_exists():
    assert callable(sequence_description_EndOfLifeMapping.__init__)


def test_sequence_description_endoflifemapping_constructor_args():
    sig = inspect.signature(sequence_description_EndOfLifeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_instancerolemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_InstanceRoleMapping)


def test_sequence_description_instancerolemapping_constructor_exists():
    assert callable(sequence_description_InstanceRoleMapping.__init__)


def test_sequence_description_instancerolemapping_constructor_args():
    sig = inspect.signature(sequence_description_InstanceRoleMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(DiagramDescription)


def test_diagramdescription_constructor_exists():
    assert callable(DiagramDescription.__init__)


def test_diagramdescription_constructor_args():
    sig = inspect.signature(DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_sequencediagramdescription_is_not_abstract():
    assert not inspect.isabstract(sequence_description_SequenceDiagramDescription)


def test_sequence_description_sequencediagramdescription_constructor_exists():
    assert callable(sequence_description_SequenceDiagramDescription.__init__)


def test_sequence_description_sequencediagramdescription_constructor_args():
    sig = inspect.signature(sequence_description_SequenceDiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "instanceRolesOrdering" in params, "Missing parameter 'instanceRolesOrdering'"
    assert "endsOrdering" in params, "Missing parameter 'endsOrdering'"

def test_sequence_description_sequencediagramdescription_has_instanceRolesOrdering():
    assert hasattr(sequence_description_SequenceDiagramDescription, "instanceRolesOrdering")
    descriptor = None
    for klass in sequence_description_SequenceDiagramDescription.__mro__:
        if "instanceRolesOrdering" in klass.__dict__:
            descriptor = klass.__dict__["instanceRolesOrdering"]
            break
    assert isinstance(descriptor, property)

def test_sequence_description_sequencediagramdescription_has_endsOrdering():
    assert hasattr(sequence_description_SequenceDiagramDescription, "endsOrdering")
    descriptor = None
    for klass in sequence_description_SequenceDiagramDescription.__mro__:
        if "endsOrdering" in klass.__dict__:
            descriptor = klass.__dict__["endsOrdering"]
            break
    assert isinstance(descriptor, property)



def test_description_delimitedeventmapping_is_not_abstract():
    assert not inspect.isabstract(description_DelimitedEventMapping)


def test_description_delimitedeventmapping_constructor_exists():
    assert callable(description_DelimitedEventMapping.__init__)


def test_description_delimitedeventmapping_constructor_args():
    sig = inspect.signature(description_DelimitedEventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_operandmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_OperandMapping)


def test_sequence_description_operandmapping_constructor_exists():
    assert callable(sequence_description_OperandMapping.__init__)


def test_sequence_description_operandmapping_constructor_args():
    sig = inspect.signature(sequence_description_OperandMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_framemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_FrameMapping)


def test_sequence_description_framemapping_constructor_exists():
    assert callable(sequence_description_FrameMapping.__init__)


def test_sequence_description_framemapping_constructor_args():
    sig = inspect.signature(sequence_description_FrameMapping.__init__)
    params = list(sig.parameters.keys())
    assert "coveredLifelinesExpression" in params, "Missing parameter 'coveredLifelinesExpression'"
    assert "centerLabelExpression" in params, "Missing parameter 'centerLabelExpression'"

def test_sequence_description_framemapping_has_coveredLifelinesExpression():
    assert hasattr(sequence_description_FrameMapping, "coveredLifelinesExpression")
    descriptor = None
    for klass in sequence_description_FrameMapping.__mro__:
        if "coveredLifelinesExpression" in klass.__dict__:
            descriptor = klass.__dict__["coveredLifelinesExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence_description_framemapping_has_centerLabelExpression():
    assert hasattr(sequence_description_FrameMapping, "centerLabelExpression")
    descriptor = None
    for klass in sequence_description_FrameMapping.__mro__:
        if "centerLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["centerLabelExpression"]
            break
    assert isinstance(descriptor, property)



def test_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(description_NodeMapping)


def test_description_nodemapping_constructor_exists():
    assert callable(description_NodeMapping.__init__)


def test_description_nodemapping_constructor_args():
    sig = inspect.signature(description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_statemapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_StateMapping)


def test_sequence_description_statemapping_constructor_exists():
    assert callable(sequence_description_StateMapping.__init__)


def test_sequence_description_statemapping_constructor_args():
    sig = inspect.signature(sequence_description_StateMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence_description_executionmapping_is_not_abstract():
    assert not inspect.isabstract(sequence_description_ExecutionMapping)


def test_sequence_description_executionmapping_constructor_exists():
    assert callable(sequence_description_ExecutionMapping.__init__)


def test_sequence_description_executionmapping_constructor_args():
    sig = inspect.signature(sequence_description_ExecutionMapping.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(DSemanticDiagram)


def test_dsemanticdiagram_constructor_exists():
    assert callable(DSemanticDiagram.__init__)


def test_dsemanticdiagram_constructor_args():
    sig = inspect.signature(DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sequence_sequenceddiagram_is_not_abstract():
    assert not inspect.isabstract(sequence_SequenceDDiagram)


def test_sequence_sequenceddiagram_constructor_exists():
    assert callable(sequence_SequenceDDiagram.__init__)


def test_sequence_sequenceddiagram_constructor_args():
    sig = inspect.signature(sequence_SequenceDDiagram.__init__)
    params = list(sig.parameters.keys())



def test_instancerolesordering_is_not_abstract():
    assert not inspect.isabstract(InstanceRolesOrdering)


def test_instancerolesordering_constructor_exists():
    assert callable(InstanceRolesOrdering.__init__)


def test_instancerolesordering_constructor_args():
    sig = inspect.signature(InstanceRolesOrdering.__init__)
    params = list(sig.parameters.keys())



def test_eventendsordering_is_not_abstract():
    assert not inspect.isabstract(EventEndsOrdering)


def test_eventendsordering_constructor_exists():
    assert callable(EventEndsOrdering.__init__)


def test_eventendsordering_constructor_args():
    sig = inspect.signature(EventEndsOrdering.__init__)
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
TBasicMessageMapping_strategy = st.builds(
    TBasicMessageMapping,
)
TMessageExtremity_strategy = st.builds(
    TMessageExtremity,
)
TSourceTargetMessageMapping_strategy = st.builds(
    TSourceTargetMessageMapping,
)
sequence_template_TCreationMessageMapping_strategy = st.builds(
    sequence_template_TCreationMessageMapping,
)
sequence_template_TDestructionMessageMapping_strategy = st.builds(
    sequence_template_TDestructionMessageMapping,
)
sequence_template_TBasicMessageMapping_strategy = st.builds(
    sequence_template_TBasicMessageMapping,
)
TConditionalMessageStyle_strategy = st.builds(
    TConditionalMessageStyle,
)
TMessageStyle_strategy = st.builds(
    TMessageStyle,
)
TAbstractMapping_strategy = st.builds(
    TAbstractMapping,
)
sequence_template_TMessageMapping_strategy = st.builds(
    sequence_template_TMessageMapping,
    receivingEndFinderExpression=
        safe_text,
    sendingEndFinderExpression=
        safe_text
)
TExecutionStyle_strategy = st.builds(
    TExecutionStyle,
)
TConditionalExecutionStyle_strategy = st.builds(
    TConditionalExecutionStyle,
)
sequence_template_TMessageExtremity_strategy = st.builds(
    sequence_template_TMessageExtremity,
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
TConditionalLifelineStyle_strategy = st.builds(
    TConditionalLifelineStyle,
)
TLifelineStyle_strategy = st.builds(
    TLifelineStyle,
)
style_NodeStyleDescription_strategy = st.builds(
    style_NodeStyleDescription,
)
TExecutionMapping_strategy = st.builds(
    TExecutionMapping,
)
template_TMessageExtremity_strategy = st.builds(
    template_TMessageExtremity,
)
template_TAbstractMapping_strategy = st.builds(
    template_TAbstractMapping,
)
sequence_template_TExecutionMapping_strategy = st.builds(
    sequence_template_TExecutionMapping,
    recursive=
        st.booleans(),
    finishingEndFinderExpression=
        safe_text,
    startingEndFinderExpression=
        safe_text
)
sequence_template_TLifelineMapping_strategy = st.builds(
    sequence_template_TLifelineMapping,
    eolVisibleExpression=
        safe_text
)
sequence_ordering_InstanceRolesOrdering_strategy = st.builds(
    sequence_ordering_InstanceRolesOrdering,
)
SingleEventEnd_strategy = st.builds(
    SingleEventEnd,
)
TMessageMapping_strategy = st.builds(
    TMessageMapping,
)
sequence_template_TSourceTargetMessageMapping_strategy = st.builds(
    sequence_template_TSourceTargetMessageMapping,
    sourceFinderExpression=
        safe_text,
    targetFinderExpression=
        safe_text,
    useDomainElement=
        st.booleans()
)
sequence_template_TReturnMessageMapping_strategy = st.builds(
    sequence_template_TReturnMessageMapping,
    invocationMessageFinderExpression=
        safe_text
)
TLifelineMapping_strategy = st.builds(
    TLifelineMapping,
)
template_TTransformer_strategy = st.builds(
    template_TTransformer,
)
description_RepresentationTemplate_strategy = st.builds(
    description_RepresentationTemplate,
)
sequence_template_TSequenceDiagram_strategy = st.builds(
    sequence_template_TSequenceDiagram,
    domainClass=
        safe_text,
    endsOrdering=
        safe_text
)
TTransformer_strategy = st.builds(
    TTransformer,
)
sequence_template_TLifelineStyle_strategy = st.builds(
    sequence_template_TLifelineStyle,
    lifelineWidthComputationExpression=
        safe_text
)
sequence_template_TConditionalMessageStyle_strategy = st.builds(
    sequence_template_TConditionalMessageStyle,
    predicateExpression=
        safe_text
)
sequence_template_TConditionalLifelineStyle_strategy = st.builds(
    sequence_template_TConditionalLifelineStyle,
    predicateExpression=
        safe_text
)
sequence_template_TExecutionStyle_strategy = st.builds(
    sequence_template_TExecutionStyle,
    borderSizeComputationExpression=
        safe_text
)
sequence_template_TConditionalExecutionStyle_strategy = st.builds(
    sequence_template_TConditionalExecutionStyle,
    predicateExpression=
        safe_text
)
sequence_template_TMessageStyle_strategy = st.builds(
    sequence_template_TMessageStyle,
    sourceArrow=
        safe_text,
    labelExpression=
        safe_text,
    targetArrow=
        safe_text,
    lineStyle=
        safe_text
)
sequence_template_TAbstractMapping_strategy = st.builds(
    sequence_template_TAbstractMapping,
    domainClass=
        safe_text,
    semanticCandidatesExpression=
        safe_text,
    name=
        safe_text
)
template_sequence_EObject_strategy = st.builds(
    template_sequence_EObject,
)
sequence_template_TTransformer_strategy = st.builds(
    sequence_template_TTransformer,
)
ordering_sequence_EObject_strategy = st.builds(
    ordering_sequence_EObject,
)
sequence_ordering_EventEnd_strategy = st.builds(
    sequence_ordering_EventEnd,
)
EventEnd_strategy = st.builds(
    EventEnd,
)
sequence_ordering_SingleEventEnd_strategy = st.builds(
    sequence_ordering_SingleEventEnd,
    start=
        st.booleans()
)
sequence_ordering_CompoundEventEnd_strategy = st.builds(
    sequence_ordering_CompoundEventEnd,
)
ordering_sequence_SequenceDDiagram_strategy = st.builds(
    ordering_sequence_SequenceDDiagram,
)
sequence_ordering_EventEndsOrdering_strategy = st.builds(
    sequence_ordering_EventEndsOrdering,
)
InstanceRoleMapping_strategy = st.builds(
    InstanceRoleMapping,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
tool_CoveringElementCreationTool_strategy = st.builds(
    tool_CoveringElementCreationTool,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
sequence_tool_CoveringElementCreationTool_strategy = st.builds(
    sequence_tool_CoveringElementCreationTool,
)
tool_OrderedElementCreationTool_strategy = st.builds(
    tool_OrderedElementCreationTool,
)
tool_EdgeCreationDescription_strategy = st.builds(
    tool_EdgeCreationDescription,
)
tool_ContainerCreationDescription_strategy = st.builds(
    tool_ContainerCreationDescription,
)
tool_ElementVariable_strategy = st.builds(
    tool_ElementVariable,
)
tool_SequenceDiagramToolDescription_strategy = st.builds(
    tool_SequenceDiagramToolDescription,
)
sequence_tool_ReorderTool_strategy = st.builds(
    sequence_tool_ReorderTool,
)
sequence_tool_CombinedFragmentCreationTool_strategy = st.builds(
    sequence_tool_CombinedFragmentCreationTool,
)
sequence_tool_LifelineCreationTool_strategy = st.builds(
    sequence_tool_LifelineCreationTool,
)
sequence_tool_InteractionUseCreationTool_strategy = st.builds(
    sequence_tool_InteractionUseCreationTool,
)
sequence_tool_InstanceRoleReorderTool_strategy = st.builds(
    sequence_tool_InstanceRoleReorderTool,
)
sequence_tool_OperandCreationTool_strategy = st.builds(
    sequence_tool_OperandCreationTool,
)
sequence_tool_MessageCreationTool_strategy = st.builds(
    sequence_tool_MessageCreationTool,
)
tool_NodeCreationDescription_strategy = st.builds(
    tool_NodeCreationDescription,
)
sequence_tool_StateCreationTool_strategy = st.builds(
    sequence_tool_StateCreationTool,
)
sequence_tool_ExecutionCreationTool_strategy = st.builds(
    sequence_tool_ExecutionCreationTool,
)
sequence_tool_ObservationPointCreationTool_strategy = st.builds(
    sequence_tool_ObservationPointCreationTool,
)
sequence_tool_InstanceRoleCreationTool_strategy = st.builds(
    sequence_tool_InstanceRoleCreationTool,
)
CoveredLifelinesVariable_strategy = st.builds(
    CoveredLifelinesVariable,
)
MessageMapping_strategy = st.builds(
    MessageMapping,
)
sequence_description_CreationMessageMapping_strategy = st.builds(
    sequence_description_CreationMessageMapping,
)
sequence_description_DestructionMessageMapping_strategy = st.builds(
    sequence_description_DestructionMessageMapping,
)
sequence_description_ReturnMessageMapping_strategy = st.builds(
    sequence_description_ReturnMessageMapping,
    invocationMessageFinderExpression=
        safe_text
)
sequence_description_BasicMessageMapping_strategy = st.builds(
    sequence_description_BasicMessageMapping,
)
MessageEndVariable_strategy = st.builds(
    MessageEndVariable,
)
description_EventMapping_strategy = st.builds(
    description_EventMapping,
)
sequence_tool_OrderedElementCreationTool_strategy = st.builds(
    sequence_tool_OrderedElementCreationTool,
)
description_EdgeMapping_strategy = st.builds(
    description_EdgeMapping,
)
sequence_description_MessageMapping_strategy = st.builds(
    sequence_description_MessageMapping,
    sendingEndFinderExpression=
        safe_text,
    receivingEndFinderExpression=
        safe_text
)
sequence_tool_SequenceDiagramToolDescription_strategy = st.builds(
    sequence_tool_SequenceDiagramToolDescription,
)
FrameMapping_strategy = st.builds(
    FrameMapping,
)
sequence_description_CombinedFragmentMapping_strategy = st.builds(
    sequence_description_CombinedFragmentMapping,
)
sequence_description_InteractionUseMapping_strategy = st.builds(
    sequence_description_InteractionUseMapping,
)
description_ContainerMapping_strategy = st.builds(
    description_ContainerMapping,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
sequence_description_MessageEndVariable_strategy = st.builds(
    sequence_description_MessageEndVariable,
)
sequence_description_CoveredLifelinesVariable_strategy = st.builds(
    sequence_description_CoveredLifelinesVariable,
)
EventMapping_strategy = st.builds(
    EventMapping,
)
sequence_description_DelimitedEventMapping_strategy = st.builds(
    sequence_description_DelimitedEventMapping,
    startingEndFinderExpression=
        safe_text,
    finishingEndFinderExpression=
        safe_text
)
sequence_description_EventMapping_strategy = st.builds(
    sequence_description_EventMapping,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
sequence_description_ObservationPointMapping_strategy = st.builds(
    sequence_description_ObservationPointMapping,
)
sequence_description_EndOfLifeMapping_strategy = st.builds(
    sequence_description_EndOfLifeMapping,
)
sequence_description_InstanceRoleMapping_strategy = st.builds(
    sequence_description_InstanceRoleMapping,
)
DiagramDescription_strategy = st.builds(
    DiagramDescription,
)
sequence_description_SequenceDiagramDescription_strategy = st.builds(
    sequence_description_SequenceDiagramDescription,
    instanceRolesOrdering=
        safe_text,
    endsOrdering=
        safe_text
)
description_DelimitedEventMapping_strategy = st.builds(
    description_DelimitedEventMapping,
)
sequence_description_OperandMapping_strategy = st.builds(
    sequence_description_OperandMapping,
)
sequence_description_FrameMapping_strategy = st.builds(
    sequence_description_FrameMapping,
    coveredLifelinesExpression=
        safe_text,
    centerLabelExpression=
        safe_text
)
description_NodeMapping_strategy = st.builds(
    description_NodeMapping,
)
sequence_description_StateMapping_strategy = st.builds(
    sequence_description_StateMapping,
)
sequence_description_ExecutionMapping_strategy = st.builds(
    sequence_description_ExecutionMapping,
)
DSemanticDiagram_strategy = st.builds(
    DSemanticDiagram,
)
sequence_SequenceDDiagram_strategy = st.builds(
    sequence_SequenceDDiagram,
)
InstanceRolesOrdering_strategy = st.builds(
    InstanceRolesOrdering,
)
EventEndsOrdering_strategy = st.builds(
    EventEndsOrdering,
)

@given(instance=TBasicMessageMapping_strategy)
@settings(max_examples=50)
def test_tbasicmessagemapping_instantiation(instance):
    assert isinstance(instance, TBasicMessageMapping)

@given(instance=TMessageExtremity_strategy)
@settings(max_examples=50)
def test_tmessageextremity_instantiation(instance):
    assert isinstance(instance, TMessageExtremity)

@given(instance=TSourceTargetMessageMapping_strategy)
@settings(max_examples=50)
def test_tsourcetargetmessagemapping_instantiation(instance):
    assert isinstance(instance, TSourceTargetMessageMapping)

@given(instance=sequence_template_TCreationMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tcreationmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TCreationMessageMapping)

@given(instance=sequence_template_TDestructionMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tdestructionmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TDestructionMessageMapping)

@given(instance=sequence_template_TBasicMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tbasicmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TBasicMessageMapping)

@given(instance=TConditionalMessageStyle_strategy)
@settings(max_examples=50)
def test_tconditionalmessagestyle_instantiation(instance):
    assert isinstance(instance, TConditionalMessageStyle)

@given(instance=TMessageStyle_strategy)
@settings(max_examples=50)
def test_tmessagestyle_instantiation(instance):
    assert isinstance(instance, TMessageStyle)

@given(instance=TAbstractMapping_strategy)
@settings(max_examples=50)
def test_tabstractmapping_instantiation(instance):
    assert isinstance(instance, TAbstractMapping)

@given(instance=sequence_template_TMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TMessageMapping)



@given(instance=sequence_template_TMessageMapping_strategy)
def test_sequence_template_tmessagemapping_receivingEndFinderExpression_setter(instance):
    original = instance.receivingEndFinderExpression
    instance.receivingEndFinderExpression = original
    assert instance.receivingEndFinderExpression == original



@given(instance=sequence_template_TMessageMapping_strategy)
def test_sequence_template_tmessagemapping_sendingEndFinderExpression_setter(instance):
    original = instance.sendingEndFinderExpression
    instance.sendingEndFinderExpression = original
    assert instance.sendingEndFinderExpression == original

@given(instance=TExecutionStyle_strategy)
@settings(max_examples=50)
def test_texecutionstyle_instantiation(instance):
    assert isinstance(instance, TExecutionStyle)

@given(instance=TConditionalExecutionStyle_strategy)
@settings(max_examples=50)
def test_tconditionalexecutionstyle_instantiation(instance):
    assert isinstance(instance, TConditionalExecutionStyle)

@given(instance=sequence_template_TMessageExtremity_strategy)
@settings(max_examples=50)
def test_sequence_template_tmessageextremity_instantiation(instance):
    assert isinstance(instance, sequence_template_TMessageExtremity)

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=TConditionalLifelineStyle_strategy)
@settings(max_examples=50)
def test_tconditionallifelinestyle_instantiation(instance):
    assert isinstance(instance, TConditionalLifelineStyle)

@given(instance=TLifelineStyle_strategy)
@settings(max_examples=50)
def test_tlifelinestyle_instantiation(instance):
    assert isinstance(instance, TLifelineStyle)

@given(instance=style_NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style_nodestyledescription_instantiation(instance):
    assert isinstance(instance, style_NodeStyleDescription)

@given(instance=TExecutionMapping_strategy)
@settings(max_examples=50)
def test_texecutionmapping_instantiation(instance):
    assert isinstance(instance, TExecutionMapping)

@given(instance=template_TMessageExtremity_strategy)
@settings(max_examples=50)
def test_template_tmessageextremity_instantiation(instance):
    assert isinstance(instance, template_TMessageExtremity)

@given(instance=template_TAbstractMapping_strategy)
@settings(max_examples=50)
def test_template_tabstractmapping_instantiation(instance):
    assert isinstance(instance, template_TAbstractMapping)

@given(instance=sequence_template_TExecutionMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_texecutionmapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TExecutionMapping)



@given(instance=sequence_template_TExecutionMapping_strategy)
def test_sequence_template_texecutionmapping_recursive_setter(instance):
    original = instance.recursive
    instance.recursive = original
    assert instance.recursive == original



@given(instance=sequence_template_TExecutionMapping_strategy)
def test_sequence_template_texecutionmapping_finishingEndFinderExpression_setter(instance):
    original = instance.finishingEndFinderExpression
    instance.finishingEndFinderExpression = original
    assert instance.finishingEndFinderExpression == original



@given(instance=sequence_template_TExecutionMapping_strategy)
def test_sequence_template_texecutionmapping_startingEndFinderExpression_setter(instance):
    original = instance.startingEndFinderExpression
    instance.startingEndFinderExpression = original
    assert instance.startingEndFinderExpression == original

@given(instance=sequence_template_TLifelineMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tlifelinemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TLifelineMapping)



@given(instance=sequence_template_TLifelineMapping_strategy)
def test_sequence_template_tlifelinemapping_eolVisibleExpression_setter(instance):
    original = instance.eolVisibleExpression
    instance.eolVisibleExpression = original
    assert instance.eolVisibleExpression == original

@given(instance=sequence_ordering_InstanceRolesOrdering_strategy)
@settings(max_examples=50)
def test_sequence_ordering_instancerolesordering_instantiation(instance):
    assert isinstance(instance, sequence_ordering_InstanceRolesOrdering)

@given(instance=SingleEventEnd_strategy)
@settings(max_examples=50)
def test_singleeventend_instantiation(instance):
    assert isinstance(instance, SingleEventEnd)

@given(instance=TMessageMapping_strategy)
@settings(max_examples=50)
def test_tmessagemapping_instantiation(instance):
    assert isinstance(instance, TMessageMapping)

@given(instance=sequence_template_TSourceTargetMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tsourcetargetmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TSourceTargetMessageMapping)



@given(instance=sequence_template_TSourceTargetMessageMapping_strategy)
def test_sequence_template_tsourcetargetmessagemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original



@given(instance=sequence_template_TSourceTargetMessageMapping_strategy)
def test_sequence_template_tsourcetargetmessagemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original



@given(instance=sequence_template_TSourceTargetMessageMapping_strategy)
def test_sequence_template_tsourcetargetmessagemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original

@given(instance=sequence_template_TReturnMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_treturnmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TReturnMessageMapping)



@given(instance=sequence_template_TReturnMessageMapping_strategy)
def test_sequence_template_treturnmessagemapping_invocationMessageFinderExpression_setter(instance):
    original = instance.invocationMessageFinderExpression
    instance.invocationMessageFinderExpression = original
    assert instance.invocationMessageFinderExpression == original

@given(instance=TLifelineMapping_strategy)
@settings(max_examples=50)
def test_tlifelinemapping_instantiation(instance):
    assert isinstance(instance, TLifelineMapping)

@given(instance=template_TTransformer_strategy)
@settings(max_examples=50)
def test_template_ttransformer_instantiation(instance):
    assert isinstance(instance, template_TTransformer)

@given(instance=description_RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_description_representationtemplate_instantiation(instance):
    assert isinstance(instance, description_RepresentationTemplate)

@given(instance=sequence_template_TSequenceDiagram_strategy)
@settings(max_examples=50)
def test_sequence_template_tsequencediagram_instantiation(instance):
    assert isinstance(instance, sequence_template_TSequenceDiagram)



@given(instance=sequence_template_TSequenceDiagram_strategy)
def test_sequence_template_tsequencediagram_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=sequence_template_TSequenceDiagram_strategy)
def test_sequence_template_tsequencediagram_endsOrdering_setter(instance):
    original = instance.endsOrdering
    instance.endsOrdering = original
    assert instance.endsOrdering == original

@given(instance=TTransformer_strategy)
@settings(max_examples=50)
def test_ttransformer_instantiation(instance):
    assert isinstance(instance, TTransformer)

@given(instance=sequence_template_TLifelineStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_tlifelinestyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TLifelineStyle)



@given(instance=sequence_template_TLifelineStyle_strategy)
def test_sequence_template_tlifelinestyle_lifelineWidthComputationExpression_setter(instance):
    original = instance.lifelineWidthComputationExpression
    instance.lifelineWidthComputationExpression = original
    assert instance.lifelineWidthComputationExpression == original

@given(instance=sequence_template_TConditionalMessageStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_tconditionalmessagestyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TConditionalMessageStyle)



@given(instance=sequence_template_TConditionalMessageStyle_strategy)
def test_sequence_template_tconditionalmessagestyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence_template_TConditionalLifelineStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_tconditionallifelinestyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TConditionalLifelineStyle)



@given(instance=sequence_template_TConditionalLifelineStyle_strategy)
def test_sequence_template_tconditionallifelinestyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence_template_TExecutionStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_texecutionstyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TExecutionStyle)



@given(instance=sequence_template_TExecutionStyle_strategy)
def test_sequence_template_texecutionstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=sequence_template_TConditionalExecutionStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_tconditionalexecutionstyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TConditionalExecutionStyle)



@given(instance=sequence_template_TConditionalExecutionStyle_strategy)
def test_sequence_template_tconditionalexecutionstyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence_template_TMessageStyle_strategy)
@settings(max_examples=50)
def test_sequence_template_tmessagestyle_instantiation(instance):
    assert isinstance(instance, sequence_template_TMessageStyle)



@given(instance=sequence_template_TMessageStyle_strategy)
def test_sequence_template_tmessagestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original



@given(instance=sequence_template_TMessageStyle_strategy)
def test_sequence_template_tmessagestyle_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original



@given(instance=sequence_template_TMessageStyle_strategy)
def test_sequence_template_tmessagestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=sequence_template_TMessageStyle_strategy)
def test_sequence_template_tmessagestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=sequence_template_TAbstractMapping_strategy)
@settings(max_examples=50)
def test_sequence_template_tabstractmapping_instantiation(instance):
    assert isinstance(instance, sequence_template_TAbstractMapping)



@given(instance=sequence_template_TAbstractMapping_strategy)
def test_sequence_template_tabstractmapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=sequence_template_TAbstractMapping_strategy)
def test_sequence_template_tabstractmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original



@given(instance=sequence_template_TAbstractMapping_strategy)
def test_sequence_template_tabstractmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=template_sequence_EObject_strategy)
@settings(max_examples=50)
def test_template_sequence_eobject_instantiation(instance):
    assert isinstance(instance, template_sequence_EObject)

@given(instance=sequence_template_TTransformer_strategy)
@settings(max_examples=50)
def test_sequence_template_ttransformer_instantiation(instance):
    assert isinstance(instance, sequence_template_TTransformer)

@given(instance=ordering_sequence_EObject_strategy)
@settings(max_examples=50)
def test_ordering_sequence_eobject_instantiation(instance):
    assert isinstance(instance, ordering_sequence_EObject)

@given(instance=sequence_ordering_EventEnd_strategy)
@settings(max_examples=50)
def test_sequence_ordering_eventend_instantiation(instance):
    assert isinstance(instance, sequence_ordering_EventEnd)

@given(instance=EventEnd_strategy)
@settings(max_examples=50)
def test_eventend_instantiation(instance):
    assert isinstance(instance, EventEnd)

@given(instance=sequence_ordering_SingleEventEnd_strategy)
@settings(max_examples=50)
def test_sequence_ordering_singleeventend_instantiation(instance):
    assert isinstance(instance, sequence_ordering_SingleEventEnd)



@given(instance=sequence_ordering_SingleEventEnd_strategy)
def test_sequence_ordering_singleeventend_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=sequence_ordering_CompoundEventEnd_strategy)
@settings(max_examples=50)
def test_sequence_ordering_compoundeventend_instantiation(instance):
    assert isinstance(instance, sequence_ordering_CompoundEventEnd)

@given(instance=ordering_sequence_SequenceDDiagram_strategy)
@settings(max_examples=50)
def test_ordering_sequence_sequenceddiagram_instantiation(instance):
    assert isinstance(instance, ordering_sequence_SequenceDDiagram)

@given(instance=sequence_ordering_EventEndsOrdering_strategy)
@settings(max_examples=50)
def test_sequence_ordering_eventendsordering_instantiation(instance):
    assert isinstance(instance, sequence_ordering_EventEndsOrdering)

@given(instance=InstanceRoleMapping_strategy)
@settings(max_examples=50)
def test_instancerolemapping_instantiation(instance):
    assert isinstance(instance, InstanceRoleMapping)

@given(instance=tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialOperation)

@given(instance=tool_CoveringElementCreationTool_strategy)
@settings(max_examples=50)
def test_tool_coveringelementcreationtool_instantiation(instance):
    assert isinstance(instance, tool_CoveringElementCreationTool)

@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)

@given(instance=sequence_tool_CoveringElementCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_coveringelementcreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_CoveringElementCreationTool)

@given(instance=tool_OrderedElementCreationTool_strategy)
@settings(max_examples=50)
def test_tool_orderedelementcreationtool_instantiation(instance):
    assert isinstance(instance, tool_OrderedElementCreationTool)

@given(instance=tool_EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_edgecreationdescription_instantiation(instance):
    assert isinstance(instance, tool_EdgeCreationDescription)

@given(instance=tool_ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_containercreationdescription_instantiation(instance):
    assert isinstance(instance, tool_ContainerCreationDescription)

@given(instance=tool_ElementVariable_strategy)
@settings(max_examples=50)
def test_tool_elementvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementVariable)

@given(instance=tool_SequenceDiagramToolDescription_strategy)
@settings(max_examples=50)
def test_tool_sequencediagramtooldescription_instantiation(instance):
    assert isinstance(instance, tool_SequenceDiagramToolDescription)

@given(instance=sequence_tool_ReorderTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_reordertool_instantiation(instance):
    assert isinstance(instance, sequence_tool_ReorderTool)

@given(instance=sequence_tool_CombinedFragmentCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_combinedfragmentcreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_CombinedFragmentCreationTool)

@given(instance=sequence_tool_LifelineCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_lifelinecreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_LifelineCreationTool)

@given(instance=sequence_tool_InteractionUseCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_interactionusecreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_InteractionUseCreationTool)

@given(instance=sequence_tool_InstanceRoleReorderTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_instancerolereordertool_instantiation(instance):
    assert isinstance(instance, sequence_tool_InstanceRoleReorderTool)

@given(instance=sequence_tool_OperandCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_operandcreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_OperandCreationTool)

@given(instance=sequence_tool_MessageCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_messagecreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_MessageCreationTool)

@given(instance=tool_NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_nodecreationdescription_instantiation(instance):
    assert isinstance(instance, tool_NodeCreationDescription)

@given(instance=sequence_tool_StateCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_statecreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_StateCreationTool)

@given(instance=sequence_tool_ExecutionCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_executioncreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_ExecutionCreationTool)

@given(instance=sequence_tool_ObservationPointCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_observationpointcreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_ObservationPointCreationTool)

@given(instance=sequence_tool_InstanceRoleCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_instancerolecreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_InstanceRoleCreationTool)

@given(instance=CoveredLifelinesVariable_strategy)
@settings(max_examples=50)
def test_coveredlifelinesvariable_instantiation(instance):
    assert isinstance(instance, CoveredLifelinesVariable)

@given(instance=MessageMapping_strategy)
@settings(max_examples=50)
def test_messagemapping_instantiation(instance):
    assert isinstance(instance, MessageMapping)

@given(instance=sequence_description_CreationMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_creationmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_CreationMessageMapping)

@given(instance=sequence_description_DestructionMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_destructionmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_DestructionMessageMapping)

@given(instance=sequence_description_ReturnMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_returnmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_ReturnMessageMapping)



@given(instance=sequence_description_ReturnMessageMapping_strategy)
def test_sequence_description_returnmessagemapping_invocationMessageFinderExpression_setter(instance):
    original = instance.invocationMessageFinderExpression
    instance.invocationMessageFinderExpression = original
    assert instance.invocationMessageFinderExpression == original

@given(instance=sequence_description_BasicMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_basicmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_BasicMessageMapping)

@given(instance=MessageEndVariable_strategy)
@settings(max_examples=50)
def test_messageendvariable_instantiation(instance):
    assert isinstance(instance, MessageEndVariable)

@given(instance=description_EventMapping_strategy)
@settings(max_examples=50)
def test_description_eventmapping_instantiation(instance):
    assert isinstance(instance, description_EventMapping)

@given(instance=sequence_tool_OrderedElementCreationTool_strategy)
@settings(max_examples=50)
def test_sequence_tool_orderedelementcreationtool_instantiation(instance):
    assert isinstance(instance, sequence_tool_OrderedElementCreationTool)

@given(instance=description_EdgeMapping_strategy)
@settings(max_examples=50)
def test_description_edgemapping_instantiation(instance):
    assert isinstance(instance, description_EdgeMapping)

@given(instance=sequence_description_MessageMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_messagemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_MessageMapping)



@given(instance=sequence_description_MessageMapping_strategy)
def test_sequence_description_messagemapping_sendingEndFinderExpression_setter(instance):
    original = instance.sendingEndFinderExpression
    instance.sendingEndFinderExpression = original
    assert instance.sendingEndFinderExpression == original



@given(instance=sequence_description_MessageMapping_strategy)
def test_sequence_description_messagemapping_receivingEndFinderExpression_setter(instance):
    original = instance.receivingEndFinderExpression
    instance.receivingEndFinderExpression = original
    assert instance.receivingEndFinderExpression == original

@given(instance=sequence_tool_SequenceDiagramToolDescription_strategy)
@settings(max_examples=50)
def test_sequence_tool_sequencediagramtooldescription_instantiation(instance):
    assert isinstance(instance, sequence_tool_SequenceDiagramToolDescription)

@given(instance=FrameMapping_strategy)
@settings(max_examples=50)
def test_framemapping_instantiation(instance):
    assert isinstance(instance, FrameMapping)

@given(instance=sequence_description_CombinedFragmentMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_combinedfragmentmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_CombinedFragmentMapping)

@given(instance=sequence_description_InteractionUseMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_interactionusemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_InteractionUseMapping)

@given(instance=description_ContainerMapping_strategy)
@settings(max_examples=50)
def test_description_containermapping_instantiation(instance):
    assert isinstance(instance, description_ContainerMapping)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=sequence_description_MessageEndVariable_strategy)
@settings(max_examples=50)
def test_sequence_description_messageendvariable_instantiation(instance):
    assert isinstance(instance, sequence_description_MessageEndVariable)

@given(instance=sequence_description_CoveredLifelinesVariable_strategy)
@settings(max_examples=50)
def test_sequence_description_coveredlifelinesvariable_instantiation(instance):
    assert isinstance(instance, sequence_description_CoveredLifelinesVariable)

@given(instance=EventMapping_strategy)
@settings(max_examples=50)
def test_eventmapping_instantiation(instance):
    assert isinstance(instance, EventMapping)

@given(instance=sequence_description_DelimitedEventMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_delimitedeventmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_DelimitedEventMapping)



@given(instance=sequence_description_DelimitedEventMapping_strategy)
def test_sequence_description_delimitedeventmapping_startingEndFinderExpression_setter(instance):
    original = instance.startingEndFinderExpression
    instance.startingEndFinderExpression = original
    assert instance.startingEndFinderExpression == original



@given(instance=sequence_description_DelimitedEventMapping_strategy)
def test_sequence_description_delimitedeventmapping_finishingEndFinderExpression_setter(instance):
    original = instance.finishingEndFinderExpression
    instance.finishingEndFinderExpression = original
    assert instance.finishingEndFinderExpression == original

@given(instance=sequence_description_EventMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_eventmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_EventMapping)

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=sequence_description_ObservationPointMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_observationpointmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_ObservationPointMapping)

@given(instance=sequence_description_EndOfLifeMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_endoflifemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_EndOfLifeMapping)

@given(instance=sequence_description_InstanceRoleMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_instancerolemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_InstanceRoleMapping)

@given(instance=DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagramdescription_instantiation(instance):
    assert isinstance(instance, DiagramDescription)

@given(instance=sequence_description_SequenceDiagramDescription_strategy)
@settings(max_examples=50)
def test_sequence_description_sequencediagramdescription_instantiation(instance):
    assert isinstance(instance, sequence_description_SequenceDiagramDescription)



@given(instance=sequence_description_SequenceDiagramDescription_strategy)
def test_sequence_description_sequencediagramdescription_instanceRolesOrdering_setter(instance):
    original = instance.instanceRolesOrdering
    instance.instanceRolesOrdering = original
    assert instance.instanceRolesOrdering == original



@given(instance=sequence_description_SequenceDiagramDescription_strategy)
def test_sequence_description_sequencediagramdescription_endsOrdering_setter(instance):
    original = instance.endsOrdering
    instance.endsOrdering = original
    assert instance.endsOrdering == original

@given(instance=description_DelimitedEventMapping_strategy)
@settings(max_examples=50)
def test_description_delimitedeventmapping_instantiation(instance):
    assert isinstance(instance, description_DelimitedEventMapping)

@given(instance=sequence_description_OperandMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_operandmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_OperandMapping)

@given(instance=sequence_description_FrameMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_framemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_FrameMapping)



@given(instance=sequence_description_FrameMapping_strategy)
def test_sequence_description_framemapping_coveredLifelinesExpression_setter(instance):
    original = instance.coveredLifelinesExpression
    instance.coveredLifelinesExpression = original
    assert instance.coveredLifelinesExpression == original



@given(instance=sequence_description_FrameMapping_strategy)
def test_sequence_description_framemapping_centerLabelExpression_setter(instance):
    original = instance.centerLabelExpression
    instance.centerLabelExpression = original
    assert instance.centerLabelExpression == original

@given(instance=description_NodeMapping_strategy)
@settings(max_examples=50)
def test_description_nodemapping_instantiation(instance):
    assert isinstance(instance, description_NodeMapping)

@given(instance=sequence_description_StateMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_statemapping_instantiation(instance):
    assert isinstance(instance, sequence_description_StateMapping)

@given(instance=sequence_description_ExecutionMapping_strategy)
@settings(max_examples=50)
def test_sequence_description_executionmapping_instantiation(instance):
    assert isinstance(instance, sequence_description_ExecutionMapping)

@given(instance=DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, DSemanticDiagram)

@given(instance=sequence_SequenceDDiagram_strategy)
@settings(max_examples=50)
def test_sequence_sequenceddiagram_instantiation(instance):
    assert isinstance(instance, sequence_SequenceDDiagram)

@given(instance=InstanceRolesOrdering_strategy)
@settings(max_examples=50)
def test_instancerolesordering_instantiation(instance):
    assert isinstance(instance, InstanceRolesOrdering)

@given(instance=EventEndsOrdering_strategy)
@settings(max_examples=50)
def test_eventendsordering_instantiation(instance):
    assert isinstance(instance, EventEndsOrdering)

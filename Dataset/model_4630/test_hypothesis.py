import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TBasicMessageMapping,
    TMessageExtremity,
    TSourceTargetMessageMapping,
    sequence::template::TCreationMessageMapping,
    sequence::template::TDestructionMessageMapping,
    sequence::template::TBasicMessageMapping,
    TConditionalMessageStyle,
    TMessageStyle,
    TAbstractMapping,
    sequence::template::TMessageMapping,
    TExecutionStyle,
    TConditionalExecutionStyle,
    sequence::template::TMessageExtremity,
    ColorDescription,
    TConditionalLifelineStyle,
    TLifelineStyle,
    style::NodeStyleDescription,
    TExecutionMapping,
    template::TMessageExtremity,
    template::TAbstractMapping,
    sequence::template::TExecutionMapping,
    sequence::template::TLifelineMapping,
    sequence::ordering::InstanceRolesOrdering,
    SingleEventEnd,
    TMessageMapping,
    sequence::template::TReturnMessageMapping,
    sequence::template::TSourceTargetMessageMapping,
    TLifelineMapping,
    template::TTransformer,
    description::RepresentationTemplate,
    sequence::template::TSequenceDiagram,
    TTransformer,
    sequence::template::TMessageStyle,
    sequence::template::TConditionalExecutionStyle,
    sequence::template::TExecutionStyle,
    sequence::template::TConditionalLifelineStyle,
    sequence::template::TLifelineStyle,
    sequence::template::TConditionalMessageStyle,
    sequence::template::TAbstractMapping,
    template::sequence::EObject,
    sequence::template::TTransformer,
    ordering::sequence::EObject,
    sequence::ordering::EventEnd,
    EventEnd,
    sequence::ordering::SingleEventEnd,
    sequence::ordering::CompoundEventEnd,
    ordering::sequence::SequenceDDiagram,
    sequence::ordering::EventEndsOrdering,
    InstanceRoleMapping,
    tool::InitialOperation,
    tool::CoveringElementCreationTool,
    tool::ContainerCreationDescription,
    tool::ElementVariable,
    tool::SequenceDiagramToolDescription,
    sequence::tool::LifelineCreationTool,
    tool::NodeCreationDescription,
    sequence::tool::InstanceRoleCreationTool,
    CoveredLifelinesVariable,
    MessageMapping,
    sequence::description::ReturnMessageMapping,
    sequence::description::CreationMessageMapping,
    sequence::description::DestructionMessageMapping,
    sequence::description::BasicMessageMapping,
    MessageEndVariable,
    description::EventMapping,
    sequence::tool::OrderedElementCreationTool,
    description::EdgeMapping,
    sequence::description::MessageMapping,
    sequence::tool::SequenceDiagramToolDescription,
    FrameMapping,
    sequence::description::CombinedFragmentMapping,
    sequence::description::InteractionUseMapping,
    description::ContainerMapping,
    AbstractVariable,
    sequence::description::CoveredLifelinesVariable,
    sequence::description::MessageEndVariable,
    EventMapping,
    sequence::description::DelimitedEventMapping,
    sequence::description::EventMapping,
    NodeMapping,
    sequence::description::ObservationPointMapping,
    sequence::description::EndOfLifeMapping,
    sequence::description::InstanceRoleMapping,
    DiagramDescription,
    sequence::description::SequenceDiagramDescription,
    description::DelimitedEventMapping,
    sequence::description::FrameMapping,
    sequence::description::OperandMapping,
    description::NodeMapping,
    sequence::description::StateMapping,
    sequence::description::ExecutionMapping,
    DSemanticDiagram,
    sequence::SequenceDDiagram,
    InstanceRolesOrdering,
    EventEndsOrdering,
    tool::AbstractToolDescription,
    sequence::tool::InstanceRoleReorderTool,
    sequence::tool::ReorderTool,
    sequence::tool::CoveringElementCreationTool,
    tool::OrderedElementCreationTool,
    sequence::tool::InteractionUseCreationTool,
    sequence::tool::ExecutionCreationTool,
    sequence::tool::ObservationPointCreationTool,
    sequence::tool::StateCreationTool,
    sequence::tool::OperandCreationTool,
    sequence::tool::CombinedFragmentCreationTool,
    tool::EdgeCreationDescription,
    sequence::tool::MessageCreationTool,
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



def test_sequence::template::tcreationmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TCreationMessageMapping)


def test_sequence::template::tcreationmessagemapping_constructor_exists():
    assert callable(sequence::template::TCreationMessageMapping.__init__)


def test_sequence::template::tcreationmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TCreationMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::tdestructionmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TDestructionMessageMapping)


def test_sequence::template::tdestructionmessagemapping_constructor_exists():
    assert callable(sequence::template::TDestructionMessageMapping.__init__)


def test_sequence::template::tdestructionmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TDestructionMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::tbasicmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TBasicMessageMapping)


def test_sequence::template::tbasicmessagemapping_constructor_exists():
    assert callable(sequence::template::TBasicMessageMapping.__init__)


def test_sequence::template::tbasicmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TBasicMessageMapping.__init__)
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



def test_sequence::template::tmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TMessageMapping)


def test_sequence::template::tmessagemapping_constructor_exists():
    assert callable(sequence::template::TMessageMapping.__init__)


def test_sequence::template::tmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "sendingEndFinderExpression" in params, "Missing parameter 'sendingEndFinderExpression'"
    assert "receivingEndFinderExpression" in params, "Missing parameter 'receivingEndFinderExpression'"

def test_sequence::template::tmessagemapping_has_sendingEndFinderExpression():
    assert hasattr(sequence::template::TMessageMapping, "sendingEndFinderExpression")
    descriptor = None
    for klass in sequence::template::TMessageMapping.__mro__:
        if "sendingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sendingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tmessagemapping_has_receivingEndFinderExpression():
    assert hasattr(sequence::template::TMessageMapping, "receivingEndFinderExpression")
    descriptor = None
    for klass in sequence::template::TMessageMapping.__mro__:
        if "receivingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["receivingEndFinderExpression"]
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



def test_sequence::template::tmessageextremity_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TMessageExtremity)


def test_sequence::template::tmessageextremity_constructor_exists():
    assert callable(sequence::template::TMessageExtremity.__init__)


def test_sequence::template::tmessageextremity_constructor_args():
    sig = inspect.signature(sequence::template::TMessageExtremity.__init__)
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



def test_style::nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style::NodeStyleDescription)


def test_style::nodestyledescription_constructor_exists():
    assert callable(style::NodeStyleDescription.__init__)


def test_style::nodestyledescription_constructor_args():
    sig = inspect.signature(style::NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_texecutionmapping_is_not_abstract():
    assert not inspect.isabstract(TExecutionMapping)


def test_texecutionmapping_constructor_exists():
    assert callable(TExecutionMapping.__init__)


def test_texecutionmapping_constructor_args():
    sig = inspect.signature(TExecutionMapping.__init__)
    params = list(sig.parameters.keys())



def test_template::tmessageextremity_is_not_abstract():
    assert not inspect.isabstract(template::TMessageExtremity)


def test_template::tmessageextremity_constructor_exists():
    assert callable(template::TMessageExtremity.__init__)


def test_template::tmessageextremity_constructor_args():
    sig = inspect.signature(template::TMessageExtremity.__init__)
    params = list(sig.parameters.keys())



def test_template::tabstractmapping_is_not_abstract():
    assert not inspect.isabstract(template::TAbstractMapping)


def test_template::tabstractmapping_constructor_exists():
    assert callable(template::TAbstractMapping.__init__)


def test_template::tabstractmapping_constructor_args():
    sig = inspect.signature(template::TAbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::texecutionmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TExecutionMapping)


def test_sequence::template::texecutionmapping_constructor_exists():
    assert callable(sequence::template::TExecutionMapping.__init__)


def test_sequence::template::texecutionmapping_constructor_args():
    sig = inspect.signature(sequence::template::TExecutionMapping.__init__)
    params = list(sig.parameters.keys())
    assert "recursive" in params, "Missing parameter 'recursive'"
    assert "startingEndFinderExpression" in params, "Missing parameter 'startingEndFinderExpression'"
    assert "finishingEndFinderExpression" in params, "Missing parameter 'finishingEndFinderExpression'"

def test_sequence::template::texecutionmapping_has_recursive():
    assert hasattr(sequence::template::TExecutionMapping, "recursive")
    descriptor = None
    for klass in sequence::template::TExecutionMapping.__mro__:
        if "recursive" in klass.__dict__:
            descriptor = klass.__dict__["recursive"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::texecutionmapping_has_startingEndFinderExpression():
    assert hasattr(sequence::template::TExecutionMapping, "startingEndFinderExpression")
    descriptor = None
    for klass in sequence::template::TExecutionMapping.__mro__:
        if "startingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["startingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::texecutionmapping_has_finishingEndFinderExpression():
    assert hasattr(sequence::template::TExecutionMapping, "finishingEndFinderExpression")
    descriptor = None
    for klass in sequence::template::TExecutionMapping.__mro__:
        if "finishingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["finishingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tlifelinemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TLifelineMapping)


def test_sequence::template::tlifelinemapping_constructor_exists():
    assert callable(sequence::template::TLifelineMapping.__init__)


def test_sequence::template::tlifelinemapping_constructor_args():
    sig = inspect.signature(sequence::template::TLifelineMapping.__init__)
    params = list(sig.parameters.keys())
    assert "eolVisibleExpression" in params, "Missing parameter 'eolVisibleExpression'"

def test_sequence::template::tlifelinemapping_has_eolVisibleExpression():
    assert hasattr(sequence::template::TLifelineMapping, "eolVisibleExpression")
    descriptor = None
    for klass in sequence::template::TLifelineMapping.__mro__:
        if "eolVisibleExpression" in klass.__dict__:
            descriptor = klass.__dict__["eolVisibleExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::ordering::instancerolesordering_is_not_abstract():
    assert not inspect.isabstract(sequence::ordering::InstanceRolesOrdering)


def test_sequence::ordering::instancerolesordering_constructor_exists():
    assert callable(sequence::ordering::InstanceRolesOrdering.__init__)


def test_sequence::ordering::instancerolesordering_constructor_args():
    sig = inspect.signature(sequence::ordering::InstanceRolesOrdering.__init__)
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



def test_sequence::template::treturnmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TReturnMessageMapping)


def test_sequence::template::treturnmessagemapping_constructor_exists():
    assert callable(sequence::template::TReturnMessageMapping.__init__)


def test_sequence::template::treturnmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TReturnMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "invocationMessageFinderExpression" in params, "Missing parameter 'invocationMessageFinderExpression'"

def test_sequence::template::treturnmessagemapping_has_invocationMessageFinderExpression():
    assert hasattr(sequence::template::TReturnMessageMapping, "invocationMessageFinderExpression")
    descriptor = None
    for klass in sequence::template::TReturnMessageMapping.__mro__:
        if "invocationMessageFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["invocationMessageFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tsourcetargetmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TSourceTargetMessageMapping)


def test_sequence::template::tsourcetargetmessagemapping_constructor_exists():
    assert callable(sequence::template::TSourceTargetMessageMapping.__init__)


def test_sequence::template::tsourcetargetmessagemapping_constructor_args():
    sig = inspect.signature(sequence::template::TSourceTargetMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"

def test_sequence::template::tsourcetargetmessagemapping_has_targetFinderExpression():
    assert hasattr(sequence::template::TSourceTargetMessageMapping, "targetFinderExpression")
    descriptor = None
    for klass in sequence::template::TSourceTargetMessageMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tsourcetargetmessagemapping_has_useDomainElement():
    assert hasattr(sequence::template::TSourceTargetMessageMapping, "useDomainElement")
    descriptor = None
    for klass in sequence::template::TSourceTargetMessageMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tsourcetargetmessagemapping_has_sourceFinderExpression():
    assert hasattr(sequence::template::TSourceTargetMessageMapping, "sourceFinderExpression")
    descriptor = None
    for klass in sequence::template::TSourceTargetMessageMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_tlifelinemapping_is_not_abstract():
    assert not inspect.isabstract(TLifelineMapping)


def test_tlifelinemapping_constructor_exists():
    assert callable(TLifelineMapping.__init__)


def test_tlifelinemapping_constructor_args():
    sig = inspect.signature(TLifelineMapping.__init__)
    params = list(sig.parameters.keys())



def test_template::ttransformer_is_not_abstract():
    assert not inspect.isabstract(template::TTransformer)


def test_template::ttransformer_constructor_exists():
    assert callable(template::TTransformer.__init__)


def test_template::ttransformer_constructor_args():
    sig = inspect.signature(template::TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_description::representationtemplate_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationTemplate)


def test_description::representationtemplate_constructor_exists():
    assert callable(description::RepresentationTemplate.__init__)


def test_description::representationtemplate_constructor_args():
    sig = inspect.signature(description::RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::tsequencediagram_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TSequenceDiagram)


def test_sequence::template::tsequencediagram_constructor_exists():
    assert callable(sequence::template::TSequenceDiagram.__init__)


def test_sequence::template::tsequencediagram_constructor_args():
    sig = inspect.signature(sequence::template::TSequenceDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "endsOrdering" in params, "Missing parameter 'endsOrdering'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_sequence::template::tsequencediagram_has_endsOrdering():
    assert hasattr(sequence::template::TSequenceDiagram, "endsOrdering")
    descriptor = None
    for klass in sequence::template::TSequenceDiagram.__mro__:
        if "endsOrdering" in klass.__dict__:
            descriptor = klass.__dict__["endsOrdering"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tsequencediagram_has_domainClass():
    assert hasattr(sequence::template::TSequenceDiagram, "domainClass")
    descriptor = None
    for klass in sequence::template::TSequenceDiagram.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_ttransformer_is_not_abstract():
    assert not inspect.isabstract(TTransformer)


def test_ttransformer_constructor_exists():
    assert callable(TTransformer.__init__)


def test_ttransformer_constructor_args():
    sig = inspect.signature(TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::tmessagestyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TMessageStyle)


def test_sequence::template::tmessagestyle_constructor_exists():
    assert callable(sequence::template::TMessageStyle.__init__)


def test_sequence::template::tmessagestyle_constructor_args():
    sig = inspect.signature(sequence::template::TMessageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"

def test_sequence::template::tmessagestyle_has_labelExpression():
    assert hasattr(sequence::template::TMessageStyle, "labelExpression")
    descriptor = None
    for klass in sequence::template::TMessageStyle.__mro__:
        if "labelExpression" in klass.__dict__:
            descriptor = klass.__dict__["labelExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tmessagestyle_has_lineStyle():
    assert hasattr(sequence::template::TMessageStyle, "lineStyle")
    descriptor = None
    for klass in sequence::template::TMessageStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tmessagestyle_has_sourceArrow():
    assert hasattr(sequence::template::TMessageStyle, "sourceArrow")
    descriptor = None
    for klass in sequence::template::TMessageStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tmessagestyle_has_targetArrow():
    assert hasattr(sequence::template::TMessageStyle, "targetArrow")
    descriptor = None
    for klass in sequence::template::TMessageStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tconditionalexecutionstyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TConditionalExecutionStyle)


def test_sequence::template::tconditionalexecutionstyle_constructor_exists():
    assert callable(sequence::template::TConditionalExecutionStyle.__init__)


def test_sequence::template::tconditionalexecutionstyle_constructor_args():
    sig = inspect.signature(sequence::template::TConditionalExecutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence::template::tconditionalexecutionstyle_has_predicateExpression():
    assert hasattr(sequence::template::TConditionalExecutionStyle, "predicateExpression")
    descriptor = None
    for klass in sequence::template::TConditionalExecutionStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::texecutionstyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TExecutionStyle)


def test_sequence::template::texecutionstyle_constructor_exists():
    assert callable(sequence::template::TExecutionStyle.__init__)


def test_sequence::template::texecutionstyle_constructor_args():
    sig = inspect.signature(sequence::template::TExecutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_sequence::template::texecutionstyle_has_borderSizeComputationExpression():
    assert hasattr(sequence::template::TExecutionStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in sequence::template::TExecutionStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tconditionallifelinestyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TConditionalLifelineStyle)


def test_sequence::template::tconditionallifelinestyle_constructor_exists():
    assert callable(sequence::template::TConditionalLifelineStyle.__init__)


def test_sequence::template::tconditionallifelinestyle_constructor_args():
    sig = inspect.signature(sequence::template::TConditionalLifelineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence::template::tconditionallifelinestyle_has_predicateExpression():
    assert hasattr(sequence::template::TConditionalLifelineStyle, "predicateExpression")
    descriptor = None
    for klass in sequence::template::TConditionalLifelineStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tlifelinestyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TLifelineStyle)


def test_sequence::template::tlifelinestyle_constructor_exists():
    assert callable(sequence::template::TLifelineStyle.__init__)


def test_sequence::template::tlifelinestyle_constructor_args():
    sig = inspect.signature(sequence::template::TLifelineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lifelineWidthComputationExpression" in params, "Missing parameter 'lifelineWidthComputationExpression'"

def test_sequence::template::tlifelinestyle_has_lifelineWidthComputationExpression():
    assert hasattr(sequence::template::TLifelineStyle, "lifelineWidthComputationExpression")
    descriptor = None
    for klass in sequence::template::TLifelineStyle.__mro__:
        if "lifelineWidthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["lifelineWidthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tconditionalmessagestyle_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TConditionalMessageStyle)


def test_sequence::template::tconditionalmessagestyle_constructor_exists():
    assert callable(sequence::template::TConditionalMessageStyle.__init__)


def test_sequence::template::tconditionalmessagestyle_constructor_args():
    sig = inspect.signature(sequence::template::TConditionalMessageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_sequence::template::tconditionalmessagestyle_has_predicateExpression():
    assert hasattr(sequence::template::TConditionalMessageStyle, "predicateExpression")
    descriptor = None
    for klass in sequence::template::TConditionalMessageStyle.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::template::tabstractmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TAbstractMapping)


def test_sequence::template::tabstractmapping_constructor_exists():
    assert callable(sequence::template::TAbstractMapping.__init__)


def test_sequence::template::tabstractmapping_constructor_args():
    sig = inspect.signature(sequence::template::TAbstractMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "name" in params, "Missing parameter 'name'"

def test_sequence::template::tabstractmapping_has_domainClass():
    assert hasattr(sequence::template::TAbstractMapping, "domainClass")
    descriptor = None
    for klass in sequence::template::TAbstractMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tabstractmapping_has_semanticCandidatesExpression():
    assert hasattr(sequence::template::TAbstractMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in sequence::template::TAbstractMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::template::tabstractmapping_has_name():
    assert hasattr(sequence::template::TAbstractMapping, "name")
    descriptor = None
    for klass in sequence::template::TAbstractMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_template::sequence::eobject_is_not_abstract():
    assert not inspect.isabstract(template::sequence::EObject)


def test_template::sequence::eobject_constructor_exists():
    assert callable(template::sequence::EObject.__init__)


def test_template::sequence::eobject_constructor_args():
    sig = inspect.signature(template::sequence::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sequence::template::ttransformer_is_not_abstract():
    assert not inspect.isabstract(sequence::template::TTransformer)


def test_sequence::template::ttransformer_constructor_exists():
    assert callable(sequence::template::TTransformer.__init__)


def test_sequence::template::ttransformer_constructor_args():
    sig = inspect.signature(sequence::template::TTransformer.__init__)
    params = list(sig.parameters.keys())



def test_ordering::sequence::eobject_is_not_abstract():
    assert not inspect.isabstract(ordering::sequence::EObject)


def test_ordering::sequence::eobject_constructor_exists():
    assert callable(ordering::sequence::EObject.__init__)


def test_ordering::sequence::eobject_constructor_args():
    sig = inspect.signature(ordering::sequence::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sequence::ordering::eventend_is_not_abstract():
    assert not inspect.isabstract(sequence::ordering::EventEnd)


def test_sequence::ordering::eventend_constructor_exists():
    assert callable(sequence::ordering::EventEnd.__init__)


def test_sequence::ordering::eventend_constructor_args():
    sig = inspect.signature(sequence::ordering::EventEnd.__init__)
    params = list(sig.parameters.keys())



def test_eventend_is_not_abstract():
    assert not inspect.isabstract(EventEnd)


def test_eventend_constructor_exists():
    assert callable(EventEnd.__init__)


def test_eventend_constructor_args():
    sig = inspect.signature(EventEnd.__init__)
    params = list(sig.parameters.keys())



def test_sequence::ordering::singleeventend_is_not_abstract():
    assert not inspect.isabstract(sequence::ordering::SingleEventEnd)


def test_sequence::ordering::singleeventend_constructor_exists():
    assert callable(sequence::ordering::SingleEventEnd.__init__)


def test_sequence::ordering::singleeventend_constructor_args():
    sig = inspect.signature(sequence::ordering::SingleEventEnd.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_sequence::ordering::singleeventend_has_start():
    assert hasattr(sequence::ordering::SingleEventEnd, "start")
    descriptor = None
    for klass in sequence::ordering::SingleEventEnd.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_sequence::ordering::compoundeventend_is_not_abstract():
    assert not inspect.isabstract(sequence::ordering::CompoundEventEnd)


def test_sequence::ordering::compoundeventend_constructor_exists():
    assert callable(sequence::ordering::CompoundEventEnd.__init__)


def test_sequence::ordering::compoundeventend_constructor_args():
    sig = inspect.signature(sequence::ordering::CompoundEventEnd.__init__)
    params = list(sig.parameters.keys())



def test_ordering::sequence::sequenceddiagram_is_not_abstract():
    assert not inspect.isabstract(ordering::sequence::SequenceDDiagram)


def test_ordering::sequence::sequenceddiagram_constructor_exists():
    assert callable(ordering::sequence::SequenceDDiagram.__init__)


def test_ordering::sequence::sequenceddiagram_constructor_args():
    sig = inspect.signature(ordering::sequence::SequenceDDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sequence::ordering::eventendsordering_is_not_abstract():
    assert not inspect.isabstract(sequence::ordering::EventEndsOrdering)


def test_sequence::ordering::eventendsordering_constructor_exists():
    assert callable(sequence::ordering::EventEndsOrdering.__init__)


def test_sequence::ordering::eventendsordering_constructor_args():
    sig = inspect.signature(sequence::ordering::EventEndsOrdering.__init__)
    params = list(sig.parameters.keys())



def test_instancerolemapping_is_not_abstract():
    assert not inspect.isabstract(InstanceRoleMapping)


def test_instancerolemapping_constructor_exists():
    assert callable(InstanceRoleMapping.__init__)


def test_instancerolemapping_constructor_args():
    sig = inspect.signature(InstanceRoleMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialOperation)


def test_tool::initialoperation_constructor_exists():
    assert callable(tool::InitialOperation.__init__)


def test_tool::initialoperation_constructor_args():
    sig = inspect.signature(tool::InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::coveringelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(tool::CoveringElementCreationTool)


def test_tool::coveringelementcreationtool_constructor_exists():
    assert callable(tool::CoveringElementCreationTool.__init__)


def test_tool::coveringelementcreationtool_constructor_args():
    sig = inspect.signature(tool::CoveringElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool::containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerCreationDescription)


def test_tool::containercreationdescription_constructor_exists():
    assert callable(tool::ContainerCreationDescription.__init__)


def test_tool::containercreationdescription_constructor_args():
    sig = inspect.signature(tool::ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementVariable)


def test_tool::elementvariable_constructor_exists():
    assert callable(tool::ElementVariable.__init__)


def test_tool::elementvariable_constructor_args():
    sig = inspect.signature(tool::ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::sequencediagramtooldescription_is_not_abstract():
    assert not inspect.isabstract(tool::SequenceDiagramToolDescription)


def test_tool::sequencediagramtooldescription_constructor_exists():
    assert callable(tool::SequenceDiagramToolDescription.__init__)


def test_tool::sequencediagramtooldescription_constructor_args():
    sig = inspect.signature(tool::SequenceDiagramToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::lifelinecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::LifelineCreationTool)


def test_sequence::tool::lifelinecreationtool_constructor_exists():
    assert callable(sequence::tool::LifelineCreationTool.__init__)


def test_sequence::tool::lifelinecreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::LifelineCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool::nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::NodeCreationDescription)


def test_tool::nodecreationdescription_constructor_exists():
    assert callable(tool::NodeCreationDescription.__init__)


def test_tool::nodecreationdescription_constructor_args():
    sig = inspect.signature(tool::NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::instancerolecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::InstanceRoleCreationTool)


def test_sequence::tool::instancerolecreationtool_constructor_exists():
    assert callable(sequence::tool::InstanceRoleCreationTool.__init__)


def test_sequence::tool::instancerolecreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::InstanceRoleCreationTool.__init__)
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



def test_sequence::description::returnmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::ReturnMessageMapping)


def test_sequence::description::returnmessagemapping_constructor_exists():
    assert callable(sequence::description::ReturnMessageMapping.__init__)


def test_sequence::description::returnmessagemapping_constructor_args():
    sig = inspect.signature(sequence::description::ReturnMessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "invocationMessageFinderExpression" in params, "Missing parameter 'invocationMessageFinderExpression'"

def test_sequence::description::returnmessagemapping_has_invocationMessageFinderExpression():
    assert hasattr(sequence::description::ReturnMessageMapping, "invocationMessageFinderExpression")
    descriptor = None
    for klass in sequence::description::ReturnMessageMapping.__mro__:
        if "invocationMessageFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["invocationMessageFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::description::creationmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::CreationMessageMapping)


def test_sequence::description::creationmessagemapping_constructor_exists():
    assert callable(sequence::description::CreationMessageMapping.__init__)


def test_sequence::description::creationmessagemapping_constructor_args():
    sig = inspect.signature(sequence::description::CreationMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::destructionmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::DestructionMessageMapping)


def test_sequence::description::destructionmessagemapping_constructor_exists():
    assert callable(sequence::description::DestructionMessageMapping.__init__)


def test_sequence::description::destructionmessagemapping_constructor_args():
    sig = inspect.signature(sequence::description::DestructionMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::basicmessagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::BasicMessageMapping)


def test_sequence::description::basicmessagemapping_constructor_exists():
    assert callable(sequence::description::BasicMessageMapping.__init__)


def test_sequence::description::basicmessagemapping_constructor_args():
    sig = inspect.signature(sequence::description::BasicMessageMapping.__init__)
    params = list(sig.parameters.keys())



def test_messageendvariable_is_not_abstract():
    assert not inspect.isabstract(MessageEndVariable)


def test_messageendvariable_constructor_exists():
    assert callable(MessageEndVariable.__init__)


def test_messageendvariable_constructor_args():
    sig = inspect.signature(MessageEndVariable.__init__)
    params = list(sig.parameters.keys())



def test_description::eventmapping_is_not_abstract():
    assert not inspect.isabstract(description::EventMapping)


def test_description::eventmapping_constructor_exists():
    assert callable(description::EventMapping.__init__)


def test_description::eventmapping_constructor_args():
    sig = inspect.signature(description::EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::orderedelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::OrderedElementCreationTool)


def test_sequence::tool::orderedelementcreationtool_constructor_exists():
    assert callable(sequence::tool::OrderedElementCreationTool.__init__)


def test_sequence::tool::orderedelementcreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::OrderedElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_description::edgemapping_is_not_abstract():
    assert not inspect.isabstract(description::EdgeMapping)


def test_description::edgemapping_constructor_exists():
    assert callable(description::EdgeMapping.__init__)


def test_description::edgemapping_constructor_args():
    sig = inspect.signature(description::EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::messagemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::MessageMapping)


def test_sequence::description::messagemapping_constructor_exists():
    assert callable(sequence::description::MessageMapping.__init__)


def test_sequence::description::messagemapping_constructor_args():
    sig = inspect.signature(sequence::description::MessageMapping.__init__)
    params = list(sig.parameters.keys())
    assert "sendingEndFinderExpression" in params, "Missing parameter 'sendingEndFinderExpression'"
    assert "receivingEndFinderExpression" in params, "Missing parameter 'receivingEndFinderExpression'"

def test_sequence::description::messagemapping_has_sendingEndFinderExpression():
    assert hasattr(sequence::description::MessageMapping, "sendingEndFinderExpression")
    descriptor = None
    for klass in sequence::description::MessageMapping.__mro__:
        if "sendingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sendingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::description::messagemapping_has_receivingEndFinderExpression():
    assert hasattr(sequence::description::MessageMapping, "receivingEndFinderExpression")
    descriptor = None
    for klass in sequence::description::MessageMapping.__mro__:
        if "receivingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["receivingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::tool::sequencediagramtooldescription_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::SequenceDiagramToolDescription)


def test_sequence::tool::sequencediagramtooldescription_constructor_exists():
    assert callable(sequence::tool::SequenceDiagramToolDescription.__init__)


def test_sequence::tool::sequencediagramtooldescription_constructor_args():
    sig = inspect.signature(sequence::tool::SequenceDiagramToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_framemapping_is_not_abstract():
    assert not inspect.isabstract(FrameMapping)


def test_framemapping_constructor_exists():
    assert callable(FrameMapping.__init__)


def test_framemapping_constructor_args():
    sig = inspect.signature(FrameMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::combinedfragmentmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::CombinedFragmentMapping)


def test_sequence::description::combinedfragmentmapping_constructor_exists():
    assert callable(sequence::description::CombinedFragmentMapping.__init__)


def test_sequence::description::combinedfragmentmapping_constructor_args():
    sig = inspect.signature(sequence::description::CombinedFragmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::interactionusemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::InteractionUseMapping)


def test_sequence::description::interactionusemapping_constructor_exists():
    assert callable(sequence::description::InteractionUseMapping.__init__)


def test_sequence::description::interactionusemapping_constructor_args():
    sig = inspect.signature(sequence::description::InteractionUseMapping.__init__)
    params = list(sig.parameters.keys())



def test_description::containermapping_is_not_abstract():
    assert not inspect.isabstract(description::ContainerMapping)


def test_description::containermapping_constructor_exists():
    assert callable(description::ContainerMapping.__init__)


def test_description::containermapping_constructor_args():
    sig = inspect.signature(description::ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::coveredlifelinesvariable_is_not_abstract():
    assert not inspect.isabstract(sequence::description::CoveredLifelinesVariable)


def test_sequence::description::coveredlifelinesvariable_constructor_exists():
    assert callable(sequence::description::CoveredLifelinesVariable.__init__)


def test_sequence::description::coveredlifelinesvariable_constructor_args():
    sig = inspect.signature(sequence::description::CoveredLifelinesVariable.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::messageendvariable_is_not_abstract():
    assert not inspect.isabstract(sequence::description::MessageEndVariable)


def test_sequence::description::messageendvariable_constructor_exists():
    assert callable(sequence::description::MessageEndVariable.__init__)


def test_sequence::description::messageendvariable_constructor_args():
    sig = inspect.signature(sequence::description::MessageEndVariable.__init__)
    params = list(sig.parameters.keys())



def test_eventmapping_is_not_abstract():
    assert not inspect.isabstract(EventMapping)


def test_eventmapping_constructor_exists():
    assert callable(EventMapping.__init__)


def test_eventmapping_constructor_args():
    sig = inspect.signature(EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::delimitedeventmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::DelimitedEventMapping)


def test_sequence::description::delimitedeventmapping_constructor_exists():
    assert callable(sequence::description::DelimitedEventMapping.__init__)


def test_sequence::description::delimitedeventmapping_constructor_args():
    sig = inspect.signature(sequence::description::DelimitedEventMapping.__init__)
    params = list(sig.parameters.keys())
    assert "finishingEndFinderExpression" in params, "Missing parameter 'finishingEndFinderExpression'"
    assert "startingEndFinderExpression" in params, "Missing parameter 'startingEndFinderExpression'"

def test_sequence::description::delimitedeventmapping_has_finishingEndFinderExpression():
    assert hasattr(sequence::description::DelimitedEventMapping, "finishingEndFinderExpression")
    descriptor = None
    for klass in sequence::description::DelimitedEventMapping.__mro__:
        if "finishingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["finishingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::description::delimitedeventmapping_has_startingEndFinderExpression():
    assert hasattr(sequence::description::DelimitedEventMapping, "startingEndFinderExpression")
    descriptor = None
    for klass in sequence::description::DelimitedEventMapping.__mro__:
        if "startingEndFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["startingEndFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::description::eventmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::EventMapping)


def test_sequence::description::eventmapping_constructor_exists():
    assert callable(sequence::description::EventMapping.__init__)


def test_sequence::description::eventmapping_constructor_args():
    sig = inspect.signature(sequence::description::EventMapping.__init__)
    params = list(sig.parameters.keys())



def test_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::observationpointmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::ObservationPointMapping)


def test_sequence::description::observationpointmapping_constructor_exists():
    assert callable(sequence::description::ObservationPointMapping.__init__)


def test_sequence::description::observationpointmapping_constructor_args():
    sig = inspect.signature(sequence::description::ObservationPointMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::endoflifemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::EndOfLifeMapping)


def test_sequence::description::endoflifemapping_constructor_exists():
    assert callable(sequence::description::EndOfLifeMapping.__init__)


def test_sequence::description::endoflifemapping_constructor_args():
    sig = inspect.signature(sequence::description::EndOfLifeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::instancerolemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::InstanceRoleMapping)


def test_sequence::description::instancerolemapping_constructor_exists():
    assert callable(sequence::description::InstanceRoleMapping.__init__)


def test_sequence::description::instancerolemapping_constructor_args():
    sig = inspect.signature(sequence::description::InstanceRoleMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(DiagramDescription)


def test_diagramdescription_constructor_exists():
    assert callable(DiagramDescription.__init__)


def test_diagramdescription_constructor_args():
    sig = inspect.signature(DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::sequencediagramdescription_is_not_abstract():
    assert not inspect.isabstract(sequence::description::SequenceDiagramDescription)


def test_sequence::description::sequencediagramdescription_constructor_exists():
    assert callable(sequence::description::SequenceDiagramDescription.__init__)


def test_sequence::description::sequencediagramdescription_constructor_args():
    sig = inspect.signature(sequence::description::SequenceDiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "instanceRolesOrdering" in params, "Missing parameter 'instanceRolesOrdering'"
    assert "endsOrdering" in params, "Missing parameter 'endsOrdering'"

def test_sequence::description::sequencediagramdescription_has_instanceRolesOrdering():
    assert hasattr(sequence::description::SequenceDiagramDescription, "instanceRolesOrdering")
    descriptor = None
    for klass in sequence::description::SequenceDiagramDescription.__mro__:
        if "instanceRolesOrdering" in klass.__dict__:
            descriptor = klass.__dict__["instanceRolesOrdering"]
            break
    assert isinstance(descriptor, property)

def test_sequence::description::sequencediagramdescription_has_endsOrdering():
    assert hasattr(sequence::description::SequenceDiagramDescription, "endsOrdering")
    descriptor = None
    for klass in sequence::description::SequenceDiagramDescription.__mro__:
        if "endsOrdering" in klass.__dict__:
            descriptor = klass.__dict__["endsOrdering"]
            break
    assert isinstance(descriptor, property)



def test_description::delimitedeventmapping_is_not_abstract():
    assert not inspect.isabstract(description::DelimitedEventMapping)


def test_description::delimitedeventmapping_constructor_exists():
    assert callable(description::DelimitedEventMapping.__init__)


def test_description::delimitedeventmapping_constructor_args():
    sig = inspect.signature(description::DelimitedEventMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::framemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::FrameMapping)


def test_sequence::description::framemapping_constructor_exists():
    assert callable(sequence::description::FrameMapping.__init__)


def test_sequence::description::framemapping_constructor_args():
    sig = inspect.signature(sequence::description::FrameMapping.__init__)
    params = list(sig.parameters.keys())
    assert "centerLabelExpression" in params, "Missing parameter 'centerLabelExpression'"
    assert "coveredLifelinesExpression" in params, "Missing parameter 'coveredLifelinesExpression'"

def test_sequence::description::framemapping_has_centerLabelExpression():
    assert hasattr(sequence::description::FrameMapping, "centerLabelExpression")
    descriptor = None
    for klass in sequence::description::FrameMapping.__mro__:
        if "centerLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["centerLabelExpression"]
            break
    assert isinstance(descriptor, property)

def test_sequence::description::framemapping_has_coveredLifelinesExpression():
    assert hasattr(sequence::description::FrameMapping, "coveredLifelinesExpression")
    descriptor = None
    for klass in sequence::description::FrameMapping.__mro__:
        if "coveredLifelinesExpression" in klass.__dict__:
            descriptor = klass.__dict__["coveredLifelinesExpression"]
            break
    assert isinstance(descriptor, property)



def test_sequence::description::operandmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::OperandMapping)


def test_sequence::description::operandmapping_constructor_exists():
    assert callable(sequence::description::OperandMapping.__init__)


def test_sequence::description::operandmapping_constructor_args():
    sig = inspect.signature(sequence::description::OperandMapping.__init__)
    params = list(sig.parameters.keys())



def test_description::nodemapping_is_not_abstract():
    assert not inspect.isabstract(description::NodeMapping)


def test_description::nodemapping_constructor_exists():
    assert callable(description::NodeMapping.__init__)


def test_description::nodemapping_constructor_args():
    sig = inspect.signature(description::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::statemapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::StateMapping)


def test_sequence::description::statemapping_constructor_exists():
    assert callable(sequence::description::StateMapping.__init__)


def test_sequence::description::statemapping_constructor_args():
    sig = inspect.signature(sequence::description::StateMapping.__init__)
    params = list(sig.parameters.keys())



def test_sequence::description::executionmapping_is_not_abstract():
    assert not inspect.isabstract(sequence::description::ExecutionMapping)


def test_sequence::description::executionmapping_constructor_exists():
    assert callable(sequence::description::ExecutionMapping.__init__)


def test_sequence::description::executionmapping_constructor_args():
    sig = inspect.signature(sequence::description::ExecutionMapping.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(DSemanticDiagram)


def test_dsemanticdiagram_constructor_exists():
    assert callable(DSemanticDiagram.__init__)


def test_dsemanticdiagram_constructor_args():
    sig = inspect.signature(DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sequence::sequenceddiagram_is_not_abstract():
    assert not inspect.isabstract(sequence::SequenceDDiagram)


def test_sequence::sequenceddiagram_constructor_exists():
    assert callable(sequence::SequenceDDiagram.__init__)


def test_sequence::sequenceddiagram_constructor_args():
    sig = inspect.signature(sequence::SequenceDDiagram.__init__)
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



def test_tool::abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool::AbstractToolDescription)


def test_tool::abstracttooldescription_constructor_exists():
    assert callable(tool::AbstractToolDescription.__init__)


def test_tool::abstracttooldescription_constructor_args():
    sig = inspect.signature(tool::AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::instancerolereordertool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::InstanceRoleReorderTool)


def test_sequence::tool::instancerolereordertool_constructor_exists():
    assert callable(sequence::tool::InstanceRoleReorderTool.__init__)


def test_sequence::tool::instancerolereordertool_constructor_args():
    sig = inspect.signature(sequence::tool::InstanceRoleReorderTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::reordertool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::ReorderTool)


def test_sequence::tool::reordertool_constructor_exists():
    assert callable(sequence::tool::ReorderTool.__init__)


def test_sequence::tool::reordertool_constructor_args():
    sig = inspect.signature(sequence::tool::ReorderTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::coveringelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::CoveringElementCreationTool)


def test_sequence::tool::coveringelementcreationtool_constructor_exists():
    assert callable(sequence::tool::CoveringElementCreationTool.__init__)


def test_sequence::tool::coveringelementcreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::CoveringElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool::orderedelementcreationtool_is_not_abstract():
    assert not inspect.isabstract(tool::OrderedElementCreationTool)


def test_tool::orderedelementcreationtool_constructor_exists():
    assert callable(tool::OrderedElementCreationTool.__init__)


def test_tool::orderedelementcreationtool_constructor_args():
    sig = inspect.signature(tool::OrderedElementCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::interactionusecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::InteractionUseCreationTool)


def test_sequence::tool::interactionusecreationtool_constructor_exists():
    assert callable(sequence::tool::InteractionUseCreationTool.__init__)


def test_sequence::tool::interactionusecreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::InteractionUseCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::executioncreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::ExecutionCreationTool)


def test_sequence::tool::executioncreationtool_constructor_exists():
    assert callable(sequence::tool::ExecutionCreationTool.__init__)


def test_sequence::tool::executioncreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::ExecutionCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::observationpointcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::ObservationPointCreationTool)


def test_sequence::tool::observationpointcreationtool_constructor_exists():
    assert callable(sequence::tool::ObservationPointCreationTool.__init__)


def test_sequence::tool::observationpointcreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::ObservationPointCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::statecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::StateCreationTool)


def test_sequence::tool::statecreationtool_constructor_exists():
    assert callable(sequence::tool::StateCreationTool.__init__)


def test_sequence::tool::statecreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::StateCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::operandcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::OperandCreationTool)


def test_sequence::tool::operandcreationtool_constructor_exists():
    assert callable(sequence::tool::OperandCreationTool.__init__)


def test_sequence::tool::operandcreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::OperandCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::combinedfragmentcreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::CombinedFragmentCreationTool)


def test_sequence::tool::combinedfragmentcreationtool_constructor_exists():
    assert callable(sequence::tool::CombinedFragmentCreationTool.__init__)


def test_sequence::tool::combinedfragmentcreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::CombinedFragmentCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_tool::edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::EdgeCreationDescription)


def test_tool::edgecreationdescription_constructor_exists():
    assert callable(tool::EdgeCreationDescription.__init__)


def test_tool::edgecreationdescription_constructor_args():
    sig = inspect.signature(tool::EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_sequence::tool::messagecreationtool_is_not_abstract():
    assert not inspect.isabstract(sequence::tool::MessageCreationTool)


def test_sequence::tool::messagecreationtool_constructor_exists():
    assert callable(sequence::tool::MessageCreationTool.__init__)


def test_sequence::tool::messagecreationtool_constructor_args():
    sig = inspect.signature(sequence::tool::MessageCreationTool.__init__)
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
sequence::template::TCreationMessageMapping_strategy = st.builds(
    sequence::template::TCreationMessageMapping,
)
sequence::template::TDestructionMessageMapping_strategy = st.builds(
    sequence::template::TDestructionMessageMapping,
)
sequence::template::TBasicMessageMapping_strategy = st.builds(
    sequence::template::TBasicMessageMapping,
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
sequence::template::TMessageMapping_strategy = st.builds(
    sequence::template::TMessageMapping,
    sendingEndFinderExpression=
        safe_text,
    receivingEndFinderExpression=
        safe_text
)
TExecutionStyle_strategy = st.builds(
    TExecutionStyle,
)
TConditionalExecutionStyle_strategy = st.builds(
    TConditionalExecutionStyle,
)
sequence::template::TMessageExtremity_strategy = st.builds(
    sequence::template::TMessageExtremity,
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
style::NodeStyleDescription_strategy = st.builds(
    style::NodeStyleDescription,
)
TExecutionMapping_strategy = st.builds(
    TExecutionMapping,
)
template::TMessageExtremity_strategy = st.builds(
    template::TMessageExtremity,
)
template::TAbstractMapping_strategy = st.builds(
    template::TAbstractMapping,
)
sequence::template::TExecutionMapping_strategy = st.builds(
    sequence::template::TExecutionMapping,
    recursive=
        st.booleans(),
    startingEndFinderExpression=
        safe_text,
    finishingEndFinderExpression=
        safe_text
)
sequence::template::TLifelineMapping_strategy = st.builds(
    sequence::template::TLifelineMapping,
    eolVisibleExpression=
        safe_text
)
sequence::ordering::InstanceRolesOrdering_strategy = st.builds(
    sequence::ordering::InstanceRolesOrdering,
)
SingleEventEnd_strategy = st.builds(
    SingleEventEnd,
)
TMessageMapping_strategy = st.builds(
    TMessageMapping,
)
sequence::template::TReturnMessageMapping_strategy = st.builds(
    sequence::template::TReturnMessageMapping,
    invocationMessageFinderExpression=
        safe_text
)
sequence::template::TSourceTargetMessageMapping_strategy = st.builds(
    sequence::template::TSourceTargetMessageMapping,
    targetFinderExpression=
        safe_text,
    useDomainElement=
        st.booleans(),
    sourceFinderExpression=
        safe_text
)
TLifelineMapping_strategy = st.builds(
    TLifelineMapping,
)
template::TTransformer_strategy = st.builds(
    template::TTransformer,
)
description::RepresentationTemplate_strategy = st.builds(
    description::RepresentationTemplate,
)
sequence::template::TSequenceDiagram_strategy = st.builds(
    sequence::template::TSequenceDiagram,
    endsOrdering=
        safe_text,
    domainClass=
        safe_text
)
TTransformer_strategy = st.builds(
    TTransformer,
)
sequence::template::TMessageStyle_strategy = st.builds(
    sequence::template::TMessageStyle,
    labelExpression=
        safe_text,
    lineStyle=
        safe_text,
    sourceArrow=
        safe_text,
    targetArrow=
        safe_text
)
sequence::template::TConditionalExecutionStyle_strategy = st.builds(
    sequence::template::TConditionalExecutionStyle,
    predicateExpression=
        safe_text
)
sequence::template::TExecutionStyle_strategy = st.builds(
    sequence::template::TExecutionStyle,
    borderSizeComputationExpression=
        safe_text
)
sequence::template::TConditionalLifelineStyle_strategy = st.builds(
    sequence::template::TConditionalLifelineStyle,
    predicateExpression=
        safe_text
)
sequence::template::TLifelineStyle_strategy = st.builds(
    sequence::template::TLifelineStyle,
    lifelineWidthComputationExpression=
        safe_text
)
sequence::template::TConditionalMessageStyle_strategy = st.builds(
    sequence::template::TConditionalMessageStyle,
    predicateExpression=
        safe_text
)
sequence::template::TAbstractMapping_strategy = st.builds(
    sequence::template::TAbstractMapping,
    domainClass=
        safe_text,
    semanticCandidatesExpression=
        safe_text,
    name=
        safe_text
)
template::sequence::EObject_strategy = st.builds(
    template::sequence::EObject,
)
sequence::template::TTransformer_strategy = st.builds(
    sequence::template::TTransformer,
)
ordering::sequence::EObject_strategy = st.builds(
    ordering::sequence::EObject,
)
sequence::ordering::EventEnd_strategy = st.builds(
    sequence::ordering::EventEnd,
)
EventEnd_strategy = st.builds(
    EventEnd,
)
sequence::ordering::SingleEventEnd_strategy = st.builds(
    sequence::ordering::SingleEventEnd,
    start=
        st.booleans()
)
sequence::ordering::CompoundEventEnd_strategy = st.builds(
    sequence::ordering::CompoundEventEnd,
)
ordering::sequence::SequenceDDiagram_strategy = st.builds(
    ordering::sequence::SequenceDDiagram,
)
sequence::ordering::EventEndsOrdering_strategy = st.builds(
    sequence::ordering::EventEndsOrdering,
)
InstanceRoleMapping_strategy = st.builds(
    InstanceRoleMapping,
)
tool::InitialOperation_strategy = st.builds(
    tool::InitialOperation,
)
tool::CoveringElementCreationTool_strategy = st.builds(
    tool::CoveringElementCreationTool,
)
tool::ContainerCreationDescription_strategy = st.builds(
    tool::ContainerCreationDescription,
)
tool::ElementVariable_strategy = st.builds(
    tool::ElementVariable,
)
tool::SequenceDiagramToolDescription_strategy = st.builds(
    tool::SequenceDiagramToolDescription,
)
sequence::tool::LifelineCreationTool_strategy = st.builds(
    sequence::tool::LifelineCreationTool,
)
tool::NodeCreationDescription_strategy = st.builds(
    tool::NodeCreationDescription,
)
sequence::tool::InstanceRoleCreationTool_strategy = st.builds(
    sequence::tool::InstanceRoleCreationTool,
)
CoveredLifelinesVariable_strategy = st.builds(
    CoveredLifelinesVariable,
)
MessageMapping_strategy = st.builds(
    MessageMapping,
)
sequence::description::ReturnMessageMapping_strategy = st.builds(
    sequence::description::ReturnMessageMapping,
    invocationMessageFinderExpression=
        safe_text
)
sequence::description::CreationMessageMapping_strategy = st.builds(
    sequence::description::CreationMessageMapping,
)
sequence::description::DestructionMessageMapping_strategy = st.builds(
    sequence::description::DestructionMessageMapping,
)
sequence::description::BasicMessageMapping_strategy = st.builds(
    sequence::description::BasicMessageMapping,
)
MessageEndVariable_strategy = st.builds(
    MessageEndVariable,
)
description::EventMapping_strategy = st.builds(
    description::EventMapping,
)
sequence::tool::OrderedElementCreationTool_strategy = st.builds(
    sequence::tool::OrderedElementCreationTool,
)
description::EdgeMapping_strategy = st.builds(
    description::EdgeMapping,
)
sequence::description::MessageMapping_strategy = st.builds(
    sequence::description::MessageMapping,
    sendingEndFinderExpression=
        safe_text,
    receivingEndFinderExpression=
        safe_text
)
sequence::tool::SequenceDiagramToolDescription_strategy = st.builds(
    sequence::tool::SequenceDiagramToolDescription,
)
FrameMapping_strategy = st.builds(
    FrameMapping,
)
sequence::description::CombinedFragmentMapping_strategy = st.builds(
    sequence::description::CombinedFragmentMapping,
)
sequence::description::InteractionUseMapping_strategy = st.builds(
    sequence::description::InteractionUseMapping,
)
description::ContainerMapping_strategy = st.builds(
    description::ContainerMapping,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
sequence::description::CoveredLifelinesVariable_strategy = st.builds(
    sequence::description::CoveredLifelinesVariable,
)
sequence::description::MessageEndVariable_strategy = st.builds(
    sequence::description::MessageEndVariable,
)
EventMapping_strategy = st.builds(
    EventMapping,
)
sequence::description::DelimitedEventMapping_strategy = st.builds(
    sequence::description::DelimitedEventMapping,
    finishingEndFinderExpression=
        safe_text,
    startingEndFinderExpression=
        safe_text
)
sequence::description::EventMapping_strategy = st.builds(
    sequence::description::EventMapping,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
sequence::description::ObservationPointMapping_strategy = st.builds(
    sequence::description::ObservationPointMapping,
)
sequence::description::EndOfLifeMapping_strategy = st.builds(
    sequence::description::EndOfLifeMapping,
)
sequence::description::InstanceRoleMapping_strategy = st.builds(
    sequence::description::InstanceRoleMapping,
)
DiagramDescription_strategy = st.builds(
    DiagramDescription,
)
sequence::description::SequenceDiagramDescription_strategy = st.builds(
    sequence::description::SequenceDiagramDescription,
    instanceRolesOrdering=
        safe_text,
    endsOrdering=
        safe_text
)
description::DelimitedEventMapping_strategy = st.builds(
    description::DelimitedEventMapping,
)
sequence::description::FrameMapping_strategy = st.builds(
    sequence::description::FrameMapping,
    centerLabelExpression=
        safe_text,
    coveredLifelinesExpression=
        safe_text
)
sequence::description::OperandMapping_strategy = st.builds(
    sequence::description::OperandMapping,
)
description::NodeMapping_strategy = st.builds(
    description::NodeMapping,
)
sequence::description::StateMapping_strategy = st.builds(
    sequence::description::StateMapping,
)
sequence::description::ExecutionMapping_strategy = st.builds(
    sequence::description::ExecutionMapping,
)
DSemanticDiagram_strategy = st.builds(
    DSemanticDiagram,
)
sequence::SequenceDDiagram_strategy = st.builds(
    sequence::SequenceDDiagram,
)
InstanceRolesOrdering_strategy = st.builds(
    InstanceRolesOrdering,
)
EventEndsOrdering_strategy = st.builds(
    EventEndsOrdering,
)
tool::AbstractToolDescription_strategy = st.builds(
    tool::AbstractToolDescription,
)
sequence::tool::InstanceRoleReorderTool_strategy = st.builds(
    sequence::tool::InstanceRoleReorderTool,
)
sequence::tool::ReorderTool_strategy = st.builds(
    sequence::tool::ReorderTool,
)
sequence::tool::CoveringElementCreationTool_strategy = st.builds(
    sequence::tool::CoveringElementCreationTool,
)
tool::OrderedElementCreationTool_strategy = st.builds(
    tool::OrderedElementCreationTool,
)
sequence::tool::InteractionUseCreationTool_strategy = st.builds(
    sequence::tool::InteractionUseCreationTool,
)
sequence::tool::ExecutionCreationTool_strategy = st.builds(
    sequence::tool::ExecutionCreationTool,
)
sequence::tool::ObservationPointCreationTool_strategy = st.builds(
    sequence::tool::ObservationPointCreationTool,
)
sequence::tool::StateCreationTool_strategy = st.builds(
    sequence::tool::StateCreationTool,
)
sequence::tool::OperandCreationTool_strategy = st.builds(
    sequence::tool::OperandCreationTool,
)
sequence::tool::CombinedFragmentCreationTool_strategy = st.builds(
    sequence::tool::CombinedFragmentCreationTool,
)
tool::EdgeCreationDescription_strategy = st.builds(
    tool::EdgeCreationDescription,
)
sequence::tool::MessageCreationTool_strategy = st.builds(
    sequence::tool::MessageCreationTool,
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

@given(instance=sequence::template::TCreationMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tcreationmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TCreationMessageMapping)

@given(instance=sequence::template::TDestructionMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tdestructionmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TDestructionMessageMapping)

@given(instance=sequence::template::TBasicMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tbasicmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TBasicMessageMapping)

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

@given(instance=sequence::template::TMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TMessageMapping)

@given(instance=sequence::template::TMessageMapping_strategy)
def test_sequence::template::tmessagemapping_sendingEndFinderExpression_type(instance):
    assert isinstance(instance.sendingEndFinderExpression, str)


@given(instance=sequence::template::TMessageMapping_strategy)
def test_sequence::template::tmessagemapping_sendingEndFinderExpression_setter(instance):
    original = instance.sendingEndFinderExpression
    instance.sendingEndFinderExpression = original
    assert instance.sendingEndFinderExpression == original

@given(instance=sequence::template::TMessageMapping_strategy)
def test_sequence::template::tmessagemapping_receivingEndFinderExpression_type(instance):
    assert isinstance(instance.receivingEndFinderExpression, str)


@given(instance=sequence::template::TMessageMapping_strategy)
def test_sequence::template::tmessagemapping_receivingEndFinderExpression_setter(instance):
    original = instance.receivingEndFinderExpression
    instance.receivingEndFinderExpression = original
    assert instance.receivingEndFinderExpression == original

@given(instance=TExecutionStyle_strategy)
@settings(max_examples=50)
def test_texecutionstyle_instantiation(instance):
    assert isinstance(instance, TExecutionStyle)

@given(instance=TConditionalExecutionStyle_strategy)
@settings(max_examples=50)
def test_tconditionalexecutionstyle_instantiation(instance):
    assert isinstance(instance, TConditionalExecutionStyle)

@given(instance=sequence::template::TMessageExtremity_strategy)
@settings(max_examples=50)
def test_sequence::template::tmessageextremity_instantiation(instance):
    assert isinstance(instance, sequence::template::TMessageExtremity)

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

@given(instance=style::NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style::nodestyledescription_instantiation(instance):
    assert isinstance(instance, style::NodeStyleDescription)

@given(instance=TExecutionMapping_strategy)
@settings(max_examples=50)
def test_texecutionmapping_instantiation(instance):
    assert isinstance(instance, TExecutionMapping)

@given(instance=template::TMessageExtremity_strategy)
@settings(max_examples=50)
def test_template::tmessageextremity_instantiation(instance):
    assert isinstance(instance, template::TMessageExtremity)

@given(instance=template::TAbstractMapping_strategy)
@settings(max_examples=50)
def test_template::tabstractmapping_instantiation(instance):
    assert isinstance(instance, template::TAbstractMapping)

@given(instance=sequence::template::TExecutionMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::texecutionmapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TExecutionMapping)

@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_recursive_type(instance):
    assert isinstance(instance.recursive, bool)


@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_recursive_setter(instance):
    original = instance.recursive
    instance.recursive = original
    assert instance.recursive == original

@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_startingEndFinderExpression_type(instance):
    assert isinstance(instance.startingEndFinderExpression, str)


@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_startingEndFinderExpression_setter(instance):
    original = instance.startingEndFinderExpression
    instance.startingEndFinderExpression = original
    assert instance.startingEndFinderExpression == original

@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_finishingEndFinderExpression_type(instance):
    assert isinstance(instance.finishingEndFinderExpression, str)


@given(instance=sequence::template::TExecutionMapping_strategy)
def test_sequence::template::texecutionmapping_finishingEndFinderExpression_setter(instance):
    original = instance.finishingEndFinderExpression
    instance.finishingEndFinderExpression = original
    assert instance.finishingEndFinderExpression == original

@given(instance=sequence::template::TLifelineMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tlifelinemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TLifelineMapping)

@given(instance=sequence::template::TLifelineMapping_strategy)
def test_sequence::template::tlifelinemapping_eolVisibleExpression_type(instance):
    assert isinstance(instance.eolVisibleExpression, str)


@given(instance=sequence::template::TLifelineMapping_strategy)
def test_sequence::template::tlifelinemapping_eolVisibleExpression_setter(instance):
    original = instance.eolVisibleExpression
    instance.eolVisibleExpression = original
    assert instance.eolVisibleExpression == original

@given(instance=sequence::ordering::InstanceRolesOrdering_strategy)
@settings(max_examples=50)
def test_sequence::ordering::instancerolesordering_instantiation(instance):
    assert isinstance(instance, sequence::ordering::InstanceRolesOrdering)

@given(instance=SingleEventEnd_strategy)
@settings(max_examples=50)
def test_singleeventend_instantiation(instance):
    assert isinstance(instance, SingleEventEnd)

@given(instance=TMessageMapping_strategy)
@settings(max_examples=50)
def test_tmessagemapping_instantiation(instance):
    assert isinstance(instance, TMessageMapping)

@given(instance=sequence::template::TReturnMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::treturnmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TReturnMessageMapping)

@given(instance=sequence::template::TReturnMessageMapping_strategy)
def test_sequence::template::treturnmessagemapping_invocationMessageFinderExpression_type(instance):
    assert isinstance(instance.invocationMessageFinderExpression, str)


@given(instance=sequence::template::TReturnMessageMapping_strategy)
def test_sequence::template::treturnmessagemapping_invocationMessageFinderExpression_setter(instance):
    original = instance.invocationMessageFinderExpression
    instance.invocationMessageFinderExpression = original
    assert instance.invocationMessageFinderExpression == original

@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tsourcetargetmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TSourceTargetMessageMapping)

@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_targetFinderExpression_type(instance):
    assert isinstance(instance.targetFinderExpression, str)


@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original

@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_useDomainElement_type(instance):
    assert isinstance(instance.useDomainElement, bool)


@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original

@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_sourceFinderExpression_type(instance):
    assert isinstance(instance.sourceFinderExpression, str)


@given(instance=sequence::template::TSourceTargetMessageMapping_strategy)
def test_sequence::template::tsourcetargetmessagemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original

@given(instance=TLifelineMapping_strategy)
@settings(max_examples=50)
def test_tlifelinemapping_instantiation(instance):
    assert isinstance(instance, TLifelineMapping)

@given(instance=template::TTransformer_strategy)
@settings(max_examples=50)
def test_template::ttransformer_instantiation(instance):
    assert isinstance(instance, template::TTransformer)

@given(instance=description::RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_description::representationtemplate_instantiation(instance):
    assert isinstance(instance, description::RepresentationTemplate)

@given(instance=sequence::template::TSequenceDiagram_strategy)
@settings(max_examples=50)
def test_sequence::template::tsequencediagram_instantiation(instance):
    assert isinstance(instance, sequence::template::TSequenceDiagram)

@given(instance=sequence::template::TSequenceDiagram_strategy)
def test_sequence::template::tsequencediagram_endsOrdering_type(instance):
    assert isinstance(instance.endsOrdering, str)


@given(instance=sequence::template::TSequenceDiagram_strategy)
def test_sequence::template::tsequencediagram_endsOrdering_setter(instance):
    original = instance.endsOrdering
    instance.endsOrdering = original
    assert instance.endsOrdering == original

@given(instance=sequence::template::TSequenceDiagram_strategy)
def test_sequence::template::tsequencediagram_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=sequence::template::TSequenceDiagram_strategy)
def test_sequence::template::tsequencediagram_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=TTransformer_strategy)
@settings(max_examples=50)
def test_ttransformer_instantiation(instance):
    assert isinstance(instance, TTransformer)

@given(instance=sequence::template::TMessageStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::tmessagestyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TMessageStyle)

@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_labelExpression_type(instance):
    assert isinstance(instance.labelExpression, str)


@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original

@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_sourceArrow_type(instance):
    assert isinstance(instance.sourceArrow, str)


@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_targetArrow_type(instance):
    assert isinstance(instance.targetArrow, str)


@given(instance=sequence::template::TMessageStyle_strategy)
def test_sequence::template::tmessagestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original

@given(instance=sequence::template::TConditionalExecutionStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::tconditionalexecutionstyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TConditionalExecutionStyle)

@given(instance=sequence::template::TConditionalExecutionStyle_strategy)
def test_sequence::template::tconditionalexecutionstyle_predicateExpression_type(instance):
    assert isinstance(instance.predicateExpression, str)


@given(instance=sequence::template::TConditionalExecutionStyle_strategy)
def test_sequence::template::tconditionalexecutionstyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence::template::TExecutionStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::texecutionstyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TExecutionStyle)

@given(instance=sequence::template::TExecutionStyle_strategy)
def test_sequence::template::texecutionstyle_borderSizeComputationExpression_type(instance):
    assert isinstance(instance.borderSizeComputationExpression, str)


@given(instance=sequence::template::TExecutionStyle_strategy)
def test_sequence::template::texecutionstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=sequence::template::TConditionalLifelineStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::tconditionallifelinestyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TConditionalLifelineStyle)

@given(instance=sequence::template::TConditionalLifelineStyle_strategy)
def test_sequence::template::tconditionallifelinestyle_predicateExpression_type(instance):
    assert isinstance(instance.predicateExpression, str)


@given(instance=sequence::template::TConditionalLifelineStyle_strategy)
def test_sequence::template::tconditionallifelinestyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence::template::TLifelineStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::tlifelinestyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TLifelineStyle)

@given(instance=sequence::template::TLifelineStyle_strategy)
def test_sequence::template::tlifelinestyle_lifelineWidthComputationExpression_type(instance):
    assert isinstance(instance.lifelineWidthComputationExpression, str)


@given(instance=sequence::template::TLifelineStyle_strategy)
def test_sequence::template::tlifelinestyle_lifelineWidthComputationExpression_setter(instance):
    original = instance.lifelineWidthComputationExpression
    instance.lifelineWidthComputationExpression = original
    assert instance.lifelineWidthComputationExpression == original

@given(instance=sequence::template::TConditionalMessageStyle_strategy)
@settings(max_examples=50)
def test_sequence::template::tconditionalmessagestyle_instantiation(instance):
    assert isinstance(instance, sequence::template::TConditionalMessageStyle)

@given(instance=sequence::template::TConditionalMessageStyle_strategy)
def test_sequence::template::tconditionalmessagestyle_predicateExpression_type(instance):
    assert isinstance(instance.predicateExpression, str)


@given(instance=sequence::template::TConditionalMessageStyle_strategy)
def test_sequence::template::tconditionalmessagestyle_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=sequence::template::TAbstractMapping_strategy)
@settings(max_examples=50)
def test_sequence::template::tabstractmapping_instantiation(instance):
    assert isinstance(instance, sequence::template::TAbstractMapping)

@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_semanticCandidatesExpression_type(instance):
    assert isinstance(instance.semanticCandidatesExpression, str)


@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original

@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sequence::template::TAbstractMapping_strategy)
def test_sequence::template::tabstractmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=template::sequence::EObject_strategy)
@settings(max_examples=50)
def test_template::sequence::eobject_instantiation(instance):
    assert isinstance(instance, template::sequence::EObject)

@given(instance=sequence::template::TTransformer_strategy)
@settings(max_examples=50)
def test_sequence::template::ttransformer_instantiation(instance):
    assert isinstance(instance, sequence::template::TTransformer)

@given(instance=ordering::sequence::EObject_strategy)
@settings(max_examples=50)
def test_ordering::sequence::eobject_instantiation(instance):
    assert isinstance(instance, ordering::sequence::EObject)

@given(instance=sequence::ordering::EventEnd_strategy)
@settings(max_examples=50)
def test_sequence::ordering::eventend_instantiation(instance):
    assert isinstance(instance, sequence::ordering::EventEnd)

@given(instance=EventEnd_strategy)
@settings(max_examples=50)
def test_eventend_instantiation(instance):
    assert isinstance(instance, EventEnd)

@given(instance=sequence::ordering::SingleEventEnd_strategy)
@settings(max_examples=50)
def test_sequence::ordering::singleeventend_instantiation(instance):
    assert isinstance(instance, sequence::ordering::SingleEventEnd)

@given(instance=sequence::ordering::SingleEventEnd_strategy)
def test_sequence::ordering::singleeventend_start_type(instance):
    assert isinstance(instance.start, bool)


@given(instance=sequence::ordering::SingleEventEnd_strategy)
def test_sequence::ordering::singleeventend_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=sequence::ordering::CompoundEventEnd_strategy)
@settings(max_examples=50)
def test_sequence::ordering::compoundeventend_instantiation(instance):
    assert isinstance(instance, sequence::ordering::CompoundEventEnd)

@given(instance=ordering::sequence::SequenceDDiagram_strategy)
@settings(max_examples=50)
def test_ordering::sequence::sequenceddiagram_instantiation(instance):
    assert isinstance(instance, ordering::sequence::SequenceDDiagram)

@given(instance=sequence::ordering::EventEndsOrdering_strategy)
@settings(max_examples=50)
def test_sequence::ordering::eventendsordering_instantiation(instance):
    assert isinstance(instance, sequence::ordering::EventEndsOrdering)

@given(instance=InstanceRoleMapping_strategy)
@settings(max_examples=50)
def test_instancerolemapping_instantiation(instance):
    assert isinstance(instance, InstanceRoleMapping)

@given(instance=tool::InitialOperation_strategy)
@settings(max_examples=50)
def test_tool::initialoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialOperation)

@given(instance=tool::CoveringElementCreationTool_strategy)
@settings(max_examples=50)
def test_tool::coveringelementcreationtool_instantiation(instance):
    assert isinstance(instance, tool::CoveringElementCreationTool)

@given(instance=tool::ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_tool::containercreationdescription_instantiation(instance):
    assert isinstance(instance, tool::ContainerCreationDescription)

@given(instance=tool::ElementVariable_strategy)
@settings(max_examples=50)
def test_tool::elementvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementVariable)

@given(instance=tool::SequenceDiagramToolDescription_strategy)
@settings(max_examples=50)
def test_tool::sequencediagramtooldescription_instantiation(instance):
    assert isinstance(instance, tool::SequenceDiagramToolDescription)

@given(instance=sequence::tool::LifelineCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::lifelinecreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::LifelineCreationTool)

@given(instance=tool::NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_tool::nodecreationdescription_instantiation(instance):
    assert isinstance(instance, tool::NodeCreationDescription)

@given(instance=sequence::tool::InstanceRoleCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::instancerolecreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::InstanceRoleCreationTool)

@given(instance=CoveredLifelinesVariable_strategy)
@settings(max_examples=50)
def test_coveredlifelinesvariable_instantiation(instance):
    assert isinstance(instance, CoveredLifelinesVariable)

@given(instance=MessageMapping_strategy)
@settings(max_examples=50)
def test_messagemapping_instantiation(instance):
    assert isinstance(instance, MessageMapping)

@given(instance=sequence::description::ReturnMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::returnmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::ReturnMessageMapping)

@given(instance=sequence::description::ReturnMessageMapping_strategy)
def test_sequence::description::returnmessagemapping_invocationMessageFinderExpression_type(instance):
    assert isinstance(instance.invocationMessageFinderExpression, str)


@given(instance=sequence::description::ReturnMessageMapping_strategy)
def test_sequence::description::returnmessagemapping_invocationMessageFinderExpression_setter(instance):
    original = instance.invocationMessageFinderExpression
    instance.invocationMessageFinderExpression = original
    assert instance.invocationMessageFinderExpression == original

@given(instance=sequence::description::CreationMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::creationmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::CreationMessageMapping)

@given(instance=sequence::description::DestructionMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::destructionmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::DestructionMessageMapping)

@given(instance=sequence::description::BasicMessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::basicmessagemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::BasicMessageMapping)

@given(instance=MessageEndVariable_strategy)
@settings(max_examples=50)
def test_messageendvariable_instantiation(instance):
    assert isinstance(instance, MessageEndVariable)

@given(instance=description::EventMapping_strategy)
@settings(max_examples=50)
def test_description::eventmapping_instantiation(instance):
    assert isinstance(instance, description::EventMapping)

@given(instance=sequence::tool::OrderedElementCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::orderedelementcreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::OrderedElementCreationTool)

@given(instance=description::EdgeMapping_strategy)
@settings(max_examples=50)
def test_description::edgemapping_instantiation(instance):
    assert isinstance(instance, description::EdgeMapping)

@given(instance=sequence::description::MessageMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::messagemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::MessageMapping)

@given(instance=sequence::description::MessageMapping_strategy)
def test_sequence::description::messagemapping_sendingEndFinderExpression_type(instance):
    assert isinstance(instance.sendingEndFinderExpression, str)


@given(instance=sequence::description::MessageMapping_strategy)
def test_sequence::description::messagemapping_sendingEndFinderExpression_setter(instance):
    original = instance.sendingEndFinderExpression
    instance.sendingEndFinderExpression = original
    assert instance.sendingEndFinderExpression == original

@given(instance=sequence::description::MessageMapping_strategy)
def test_sequence::description::messagemapping_receivingEndFinderExpression_type(instance):
    assert isinstance(instance.receivingEndFinderExpression, str)


@given(instance=sequence::description::MessageMapping_strategy)
def test_sequence::description::messagemapping_receivingEndFinderExpression_setter(instance):
    original = instance.receivingEndFinderExpression
    instance.receivingEndFinderExpression = original
    assert instance.receivingEndFinderExpression == original

@given(instance=sequence::tool::SequenceDiagramToolDescription_strategy)
@settings(max_examples=50)
def test_sequence::tool::sequencediagramtooldescription_instantiation(instance):
    assert isinstance(instance, sequence::tool::SequenceDiagramToolDescription)

@given(instance=FrameMapping_strategy)
@settings(max_examples=50)
def test_framemapping_instantiation(instance):
    assert isinstance(instance, FrameMapping)

@given(instance=sequence::description::CombinedFragmentMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::combinedfragmentmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::CombinedFragmentMapping)

@given(instance=sequence::description::InteractionUseMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::interactionusemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::InteractionUseMapping)

@given(instance=description::ContainerMapping_strategy)
@settings(max_examples=50)
def test_description::containermapping_instantiation(instance):
    assert isinstance(instance, description::ContainerMapping)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=sequence::description::CoveredLifelinesVariable_strategy)
@settings(max_examples=50)
def test_sequence::description::coveredlifelinesvariable_instantiation(instance):
    assert isinstance(instance, sequence::description::CoveredLifelinesVariable)

@given(instance=sequence::description::MessageEndVariable_strategy)
@settings(max_examples=50)
def test_sequence::description::messageendvariable_instantiation(instance):
    assert isinstance(instance, sequence::description::MessageEndVariable)

@given(instance=EventMapping_strategy)
@settings(max_examples=50)
def test_eventmapping_instantiation(instance):
    assert isinstance(instance, EventMapping)

@given(instance=sequence::description::DelimitedEventMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::delimitedeventmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::DelimitedEventMapping)

@given(instance=sequence::description::DelimitedEventMapping_strategy)
def test_sequence::description::delimitedeventmapping_finishingEndFinderExpression_type(instance):
    assert isinstance(instance.finishingEndFinderExpression, str)


@given(instance=sequence::description::DelimitedEventMapping_strategy)
def test_sequence::description::delimitedeventmapping_finishingEndFinderExpression_setter(instance):
    original = instance.finishingEndFinderExpression
    instance.finishingEndFinderExpression = original
    assert instance.finishingEndFinderExpression == original

@given(instance=sequence::description::DelimitedEventMapping_strategy)
def test_sequence::description::delimitedeventmapping_startingEndFinderExpression_type(instance):
    assert isinstance(instance.startingEndFinderExpression, str)


@given(instance=sequence::description::DelimitedEventMapping_strategy)
def test_sequence::description::delimitedeventmapping_startingEndFinderExpression_setter(instance):
    original = instance.startingEndFinderExpression
    instance.startingEndFinderExpression = original
    assert instance.startingEndFinderExpression == original

@given(instance=sequence::description::EventMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::eventmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::EventMapping)

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=sequence::description::ObservationPointMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::observationpointmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::ObservationPointMapping)

@given(instance=sequence::description::EndOfLifeMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::endoflifemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::EndOfLifeMapping)

@given(instance=sequence::description::InstanceRoleMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::instancerolemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::InstanceRoleMapping)

@given(instance=DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagramdescription_instantiation(instance):
    assert isinstance(instance, DiagramDescription)

@given(instance=sequence::description::SequenceDiagramDescription_strategy)
@settings(max_examples=50)
def test_sequence::description::sequencediagramdescription_instantiation(instance):
    assert isinstance(instance, sequence::description::SequenceDiagramDescription)

@given(instance=sequence::description::SequenceDiagramDescription_strategy)
def test_sequence::description::sequencediagramdescription_instanceRolesOrdering_type(instance):
    assert isinstance(instance.instanceRolesOrdering, str)


@given(instance=sequence::description::SequenceDiagramDescription_strategy)
def test_sequence::description::sequencediagramdescription_instanceRolesOrdering_setter(instance):
    original = instance.instanceRolesOrdering
    instance.instanceRolesOrdering = original
    assert instance.instanceRolesOrdering == original

@given(instance=sequence::description::SequenceDiagramDescription_strategy)
def test_sequence::description::sequencediagramdescription_endsOrdering_type(instance):
    assert isinstance(instance.endsOrdering, str)


@given(instance=sequence::description::SequenceDiagramDescription_strategy)
def test_sequence::description::sequencediagramdescription_endsOrdering_setter(instance):
    original = instance.endsOrdering
    instance.endsOrdering = original
    assert instance.endsOrdering == original

@given(instance=description::DelimitedEventMapping_strategy)
@settings(max_examples=50)
def test_description::delimitedeventmapping_instantiation(instance):
    assert isinstance(instance, description::DelimitedEventMapping)

@given(instance=sequence::description::FrameMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::framemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::FrameMapping)

@given(instance=sequence::description::FrameMapping_strategy)
def test_sequence::description::framemapping_centerLabelExpression_type(instance):
    assert isinstance(instance.centerLabelExpression, str)


@given(instance=sequence::description::FrameMapping_strategy)
def test_sequence::description::framemapping_centerLabelExpression_setter(instance):
    original = instance.centerLabelExpression
    instance.centerLabelExpression = original
    assert instance.centerLabelExpression == original

@given(instance=sequence::description::FrameMapping_strategy)
def test_sequence::description::framemapping_coveredLifelinesExpression_type(instance):
    assert isinstance(instance.coveredLifelinesExpression, str)


@given(instance=sequence::description::FrameMapping_strategy)
def test_sequence::description::framemapping_coveredLifelinesExpression_setter(instance):
    original = instance.coveredLifelinesExpression
    instance.coveredLifelinesExpression = original
    assert instance.coveredLifelinesExpression == original

@given(instance=sequence::description::OperandMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::operandmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::OperandMapping)

@given(instance=description::NodeMapping_strategy)
@settings(max_examples=50)
def test_description::nodemapping_instantiation(instance):
    assert isinstance(instance, description::NodeMapping)

@given(instance=sequence::description::StateMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::statemapping_instantiation(instance):
    assert isinstance(instance, sequence::description::StateMapping)

@given(instance=sequence::description::ExecutionMapping_strategy)
@settings(max_examples=50)
def test_sequence::description::executionmapping_instantiation(instance):
    assert isinstance(instance, sequence::description::ExecutionMapping)

@given(instance=DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, DSemanticDiagram)

@given(instance=sequence::SequenceDDiagram_strategy)
@settings(max_examples=50)
def test_sequence::sequenceddiagram_instantiation(instance):
    assert isinstance(instance, sequence::SequenceDDiagram)

@given(instance=InstanceRolesOrdering_strategy)
@settings(max_examples=50)
def test_instancerolesordering_instantiation(instance):
    assert isinstance(instance, InstanceRolesOrdering)

@given(instance=EventEndsOrdering_strategy)
@settings(max_examples=50)
def test_eventendsordering_instantiation(instance):
    assert isinstance(instance, EventEndsOrdering)

@given(instance=tool::AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool::abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool::AbstractToolDescription)

@given(instance=sequence::tool::InstanceRoleReorderTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::instancerolereordertool_instantiation(instance):
    assert isinstance(instance, sequence::tool::InstanceRoleReorderTool)

@given(instance=sequence::tool::ReorderTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::reordertool_instantiation(instance):
    assert isinstance(instance, sequence::tool::ReorderTool)

@given(instance=sequence::tool::CoveringElementCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::coveringelementcreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::CoveringElementCreationTool)

@given(instance=tool::OrderedElementCreationTool_strategy)
@settings(max_examples=50)
def test_tool::orderedelementcreationtool_instantiation(instance):
    assert isinstance(instance, tool::OrderedElementCreationTool)

@given(instance=sequence::tool::InteractionUseCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::interactionusecreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::InteractionUseCreationTool)

@given(instance=sequence::tool::ExecutionCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::executioncreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::ExecutionCreationTool)

@given(instance=sequence::tool::ObservationPointCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::observationpointcreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::ObservationPointCreationTool)

@given(instance=sequence::tool::StateCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::statecreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::StateCreationTool)

@given(instance=sequence::tool::OperandCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::operandcreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::OperandCreationTool)

@given(instance=sequence::tool::CombinedFragmentCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::combinedfragmentcreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::CombinedFragmentCreationTool)

@given(instance=tool::EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_tool::edgecreationdescription_instantiation(instance):
    assert isinstance(instance, tool::EdgeCreationDescription)

@given(instance=sequence::tool::MessageCreationTool_strategy)
@settings(max_examples=50)
def test_sequence::tool::messagecreationtool_instantiation(instance):
    assert isinstance(instance, sequence::tool::MessageCreationTool)

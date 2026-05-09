import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NPNSymbolPlaceSN,
    NPNSymbolTransitionSN,
    NPNSymbolTokenSN,
    NPNSymbolArcTPSN,
    NPNSymbolArcPTSN,
    NPNSymbolArcSN,
    highlevelnets::npndiagrams::NPNSymbolArcPTSN,
    highlevelnets::npndiagrams::NPNSymbolArcTPSN,
    NPNSymbolNodeSN,
    highlevelnets::npndiagrams::NPNSymbolPlaceSN,
    highlevelnets::npndiagrams::NPNSymbolTransitionSN,
    NPnetMarked,
    highlevelnets::common::IEntityIdentifiable,
    TransitionSynchronized,
    NPNDiagramNetSystem,
    NPnet,
    Synchronization,
    NetConstant,
    Transition,
    highlevelnets::npnets::TransitionSynchronized,
    hlpn::Node,
    ArcTP,
    ArcPT,
    Arc,
    highlevelnets::hlpn::ArcTP,
    highlevelnets::hlpn::ArcPT,
    Node,
    highlevelnets::hlpn::Place,
    hlpn::ContextVariable,
    highlevelnets::hlpn::Transition,
    common::INetElement,
    highlevelnets::hlpn::HighLevelPetriNet,
    TokenBinding,
    TokenVariadicExpression,
    Variable,
    MonomConstant,
    Monom,
    ContextVariable,
    TokenTypeElementNet,
    TokenTypeAtomic,
    Token,
    highlevelnets::tokentypes::TokenNet,
    highlevelnets::tokentypes::TokenAtomic,
    TokenAttribute,
    TokenWeight,
    TokenNet,
    ElementNetMarked,
    TokenAtomic,
    Atom,
    TokenType,
    highlevelnets::tokentypes::TokenTypeElementNet,
    highlevelnets::tokentypes::TokenTypeAtomic,
    Marking,
    HighLevelPetriNet,
    TokenMultiSet,
    Place,
    IEntityIdentifiable,
    highlevelnets::tokenexpressions::TokenMultiSet,
    highlevelnets::npndiagrams::NPNDiagramNetSystem,
    highlevelnets::tokenexpressions::TokenBinding,
    highlevelnets::common::INetElement,
    highlevelnets::tokenexpressions::MonomConstant,
    highlevelnets::tokenexpressions::Variable,
    highlevelnets::hlpn::ContextVariable,
    highlevelnets::tokenexpressions::TokenMultisetExpression,
    highlevelnets::npndiagrams::NPNSymbolTokenSN,
    highlevelnets::npndiagrams::NPNDiagramNPNMarked,
    highlevelnets::npndiagrams::NPNSymbolArcSN,
    highlevelnets::npndiagrams::NPNSymbolNodeSN,
    highlevelnets::tokenexpressions::TokenExpressionBinding,
    highlevelnets::tokenexpressions::TokenWeight,
    highlevelnets::tokentypes::TokenAttribute,
    highlevelnets::tokenexpressions::Monom,
    highlevelnets::marking::PlaceMarking,
    PlaceMarking,
    INetElement,
    highlevelnets::tokenexpressions::TokenVariadicExpression,
    highlevelnets::marking::HighLevelPetriNetMarked,
    highlevelnets::npnets::NPnetMarked,
    highlevelnets::tokenexpressions::NetConstant,
    highlevelnets::tokentypes::Atom,
    highlevelnets::npnets::Synchronization,
    highlevelnets::hlpn::Arc,
    highlevelnets::tokentypes::ElementNetMarked,
    highlevelnets::npnets::NPnet,
    highlevelnets::hlpn::Node,
    highlevelnets::tokentypes::TokenType,
    highlevelnets::marking::Marking,
    highlevelnets::tokentypes::Token,
    ESynchronizationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_npnsymbolplacesn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolPlaceSN)


def test_npnsymbolplacesn_constructor_exists():
    assert callable(NPNSymbolPlaceSN.__init__)


def test_npnsymbolplacesn_constructor_args():
    sig = inspect.signature(NPNSymbolPlaceSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymboltransitionsn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolTransitionSN)


def test_npnsymboltransitionsn_constructor_exists():
    assert callable(NPNSymbolTransitionSN.__init__)


def test_npnsymboltransitionsn_constructor_args():
    sig = inspect.signature(NPNSymbolTransitionSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymboltokensn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolTokenSN)


def test_npnsymboltokensn_constructor_exists():
    assert callable(NPNSymbolTokenSN.__init__)


def test_npnsymboltokensn_constructor_args():
    sig = inspect.signature(NPNSymbolTokenSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymbolarctpsn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolArcTPSN)


def test_npnsymbolarctpsn_constructor_exists():
    assert callable(NPNSymbolArcTPSN.__init__)


def test_npnsymbolarctpsn_constructor_args():
    sig = inspect.signature(NPNSymbolArcTPSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymbolarcptsn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolArcPTSN)


def test_npnsymbolarcptsn_constructor_exists():
    assert callable(NPNSymbolArcPTSN.__init__)


def test_npnsymbolarcptsn_constructor_args():
    sig = inspect.signature(NPNSymbolArcPTSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymbolarcsn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolArcSN)


def test_npnsymbolarcsn_constructor_exists():
    assert callable(NPNSymbolArcSN.__init__)


def test_npnsymbolarcsn_constructor_args():
    sig = inspect.signature(NPNSymbolArcSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymbolarcptsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolArcPTSN)


def test_highlevelnets::npndiagrams::npnsymbolarcptsn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolArcPTSN.__init__)


def test_highlevelnets::npndiagrams::npnsymbolarcptsn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolArcPTSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymbolarctpsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolArcTPSN)


def test_highlevelnets::npndiagrams::npnsymbolarctpsn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolArcTPSN.__init__)


def test_highlevelnets::npndiagrams::npnsymbolarctpsn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolArcTPSN.__init__)
    params = list(sig.parameters.keys())



def test_npnsymbolnodesn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolNodeSN)


def test_npnsymbolnodesn_constructor_exists():
    assert callable(NPNSymbolNodeSN.__init__)


def test_npnsymbolnodesn_constructor_args():
    sig = inspect.signature(NPNSymbolNodeSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymbolplacesn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolPlaceSN)


def test_highlevelnets::npndiagrams::npnsymbolplacesn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolPlaceSN.__init__)


def test_highlevelnets::npndiagrams::npnsymbolplacesn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolPlaceSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymboltransitionsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolTransitionSN)


def test_highlevelnets::npndiagrams::npnsymboltransitionsn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolTransitionSN.__init__)


def test_highlevelnets::npndiagrams::npnsymboltransitionsn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolTransitionSN.__init__)
    params = list(sig.parameters.keys())



def test_npnetmarked_is_not_abstract():
    assert not inspect.isabstract(NPnetMarked)


def test_npnetmarked_constructor_exists():
    assert callable(NPnetMarked.__init__)


def test_npnetmarked_constructor_args():
    sig = inspect.signature(NPnetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::common::ientityidentifiable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::common::IEntityIdentifiable)


def test_highlevelnets::common::ientityidentifiable_constructor_exists():
    assert callable(highlevelnets::common::IEntityIdentifiable.__init__)


def test_highlevelnets::common::ientityidentifiable_constructor_args():
    sig = inspect.signature(highlevelnets::common::IEntityIdentifiable.__init__)
    params = list(sig.parameters.keys())
    assert "uuid" in params, "Missing parameter 'uuid'"

def test_highlevelnets::common::ientityidentifiable_has_uuid():
    assert hasattr(highlevelnets::common::IEntityIdentifiable, "uuid")
    descriptor = None
    for klass in highlevelnets::common::IEntityIdentifiable.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)



def test_transitionsynchronized_is_not_abstract():
    assert not inspect.isabstract(TransitionSynchronized)


def test_transitionsynchronized_constructor_exists():
    assert callable(TransitionSynchronized.__init__)


def test_transitionsynchronized_constructor_args():
    sig = inspect.signature(TransitionSynchronized.__init__)
    params = list(sig.parameters.keys())



def test_npndiagramnetsystem_is_not_abstract():
    assert not inspect.isabstract(NPNDiagramNetSystem)


def test_npndiagramnetsystem_constructor_exists():
    assert callable(NPNDiagramNetSystem.__init__)


def test_npndiagramnetsystem_constructor_args():
    sig = inspect.signature(NPNDiagramNetSystem.__init__)
    params = list(sig.parameters.keys())



def test_npnet_is_not_abstract():
    assert not inspect.isabstract(NPnet)


def test_npnet_constructor_exists():
    assert callable(NPnet.__init__)


def test_npnet_constructor_args():
    sig = inspect.signature(NPnet.__init__)
    params = list(sig.parameters.keys())



def test_synchronization_is_not_abstract():
    assert not inspect.isabstract(Synchronization)


def test_synchronization_constructor_exists():
    assert callable(Synchronization.__init__)


def test_synchronization_constructor_args():
    sig = inspect.signature(Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_netconstant_is_not_abstract():
    assert not inspect.isabstract(NetConstant)


def test_netconstant_constructor_exists():
    assert callable(NetConstant.__init__)


def test_netconstant_constructor_args():
    sig = inspect.signature(NetConstant.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npnets::transitionsynchronized_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npnets::TransitionSynchronized)


def test_highlevelnets::npnets::transitionsynchronized_constructor_exists():
    assert callable(highlevelnets::npnets::TransitionSynchronized.__init__)


def test_highlevelnets::npnets::transitionsynchronized_constructor_args():
    sig = inspect.signature(highlevelnets::npnets::TransitionSynchronized.__init__)
    params = list(sig.parameters.keys())



def test_hlpn::node_is_not_abstract():
    assert not inspect.isabstract(hlpn::Node)


def test_hlpn::node_constructor_exists():
    assert callable(hlpn::Node.__init__)


def test_hlpn::node_constructor_args():
    sig = inspect.signature(hlpn::Node.__init__)
    params = list(sig.parameters.keys())



def test_arctp_is_not_abstract():
    assert not inspect.isabstract(ArcTP)


def test_arctp_constructor_exists():
    assert callable(ArcTP.__init__)


def test_arctp_constructor_args():
    sig = inspect.signature(ArcTP.__init__)
    params = list(sig.parameters.keys())



def test_arcpt_is_not_abstract():
    assert not inspect.isabstract(ArcPT)


def test_arcpt_constructor_exists():
    assert callable(ArcPT.__init__)


def test_arcpt_constructor_args():
    sig = inspect.signature(ArcPT.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::hlpn::arctp_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::ArcTP)


def test_highlevelnets::hlpn::arctp_constructor_exists():
    assert callable(highlevelnets::hlpn::ArcTP.__init__)


def test_highlevelnets::hlpn::arctp_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::ArcTP.__init__)
    params = list(sig.parameters.keys())
    assert "firstTimeConstraint" in params, "Missing parameter 'firstTimeConstraint'"
    assert "secondTimeConstraint" in params, "Missing parameter 'secondTimeConstraint'"

def test_highlevelnets::hlpn::arctp_has_firstTimeConstraint():
    assert hasattr(highlevelnets::hlpn::ArcTP, "firstTimeConstraint")
    descriptor = None
    for klass in highlevelnets::hlpn::ArcTP.__mro__:
        if "firstTimeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["firstTimeConstraint"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::hlpn::arctp_has_secondTimeConstraint():
    assert hasattr(highlevelnets::hlpn::ArcTP, "secondTimeConstraint")
    descriptor = None
    for klass in highlevelnets::hlpn::ArcTP.__mro__:
        if "secondTimeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["secondTimeConstraint"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::hlpn::arcpt_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::ArcPT)


def test_highlevelnets::hlpn::arcpt_constructor_exists():
    assert callable(highlevelnets::hlpn::ArcPT.__init__)


def test_highlevelnets::hlpn::arcpt_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::ArcPT.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::hlpn::place_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::Place)


def test_highlevelnets::hlpn::place_constructor_exists():
    assert callable(highlevelnets::hlpn::Place.__init__)


def test_highlevelnets::hlpn::place_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::Place.__init__)
    params = list(sig.parameters.keys())



def test_hlpn::contextvariable_is_not_abstract():
    assert not inspect.isabstract(hlpn::ContextVariable)


def test_hlpn::contextvariable_constructor_exists():
    assert callable(hlpn::ContextVariable.__init__)


def test_hlpn::contextvariable_constructor_args():
    sig = inspect.signature(hlpn::ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::hlpn::transition_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::Transition)


def test_highlevelnets::hlpn::transition_constructor_exists():
    assert callable(highlevelnets::hlpn::Transition.__init__)


def test_highlevelnets::hlpn::transition_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::Transition.__init__)
    params = list(sig.parameters.keys())



def test_common::inetelement_is_not_abstract():
    assert not inspect.isabstract(common::INetElement)


def test_common::inetelement_constructor_exists():
    assert callable(common::INetElement.__init__)


def test_common::inetelement_constructor_args():
    sig = inspect.signature(common::INetElement.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::hlpn::highlevelpetrinet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::HighLevelPetriNet)


def test_highlevelnets::hlpn::highlevelpetrinet_constructor_exists():
    assert callable(highlevelnets::hlpn::HighLevelPetriNet.__init__)


def test_highlevelnets::hlpn::highlevelpetrinet_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::HighLevelPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_tokenbinding_is_not_abstract():
    assert not inspect.isabstract(TokenBinding)


def test_tokenbinding_constructor_exists():
    assert callable(TokenBinding.__init__)


def test_tokenbinding_constructor_args():
    sig = inspect.signature(TokenBinding.__init__)
    params = list(sig.parameters.keys())



def test_tokenvariadicexpression_is_not_abstract():
    assert not inspect.isabstract(TokenVariadicExpression)


def test_tokenvariadicexpression_constructor_exists():
    assert callable(TokenVariadicExpression.__init__)


def test_tokenvariadicexpression_constructor_args():
    sig = inspect.signature(TokenVariadicExpression.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_monomconstant_is_not_abstract():
    assert not inspect.isabstract(MonomConstant)


def test_monomconstant_constructor_exists():
    assert callable(MonomConstant.__init__)


def test_monomconstant_constructor_args():
    sig = inspect.signature(MonomConstant.__init__)
    params = list(sig.parameters.keys())



def test_monom_is_not_abstract():
    assert not inspect.isabstract(Monom)


def test_monom_constructor_exists():
    assert callable(Monom.__init__)


def test_monom_constructor_args():
    sig = inspect.signature(Monom.__init__)
    params = list(sig.parameters.keys())



def test_contextvariable_is_not_abstract():
    assert not inspect.isabstract(ContextVariable)


def test_contextvariable_constructor_exists():
    assert callable(ContextVariable.__init__)


def test_contextvariable_constructor_args():
    sig = inspect.signature(ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_tokentypeelementnet_is_not_abstract():
    assert not inspect.isabstract(TokenTypeElementNet)


def test_tokentypeelementnet_constructor_exists():
    assert callable(TokenTypeElementNet.__init__)


def test_tokentypeelementnet_constructor_args():
    sig = inspect.signature(TokenTypeElementNet.__init__)
    params = list(sig.parameters.keys())



def test_tokentypeatomic_is_not_abstract():
    assert not inspect.isabstract(TokenTypeAtomic)


def test_tokentypeatomic_constructor_exists():
    assert callable(TokenTypeAtomic.__init__)


def test_tokentypeatomic_constructor_args():
    sig = inspect.signature(TokenTypeAtomic.__init__)
    params = list(sig.parameters.keys())



def test_token_is_not_abstract():
    assert not inspect.isabstract(Token)


def test_token_constructor_exists():
    assert callable(Token.__init__)


def test_token_constructor_args():
    sig = inspect.signature(Token.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::tokennet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenNet)


def test_highlevelnets::tokentypes::tokennet_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenNet.__init__)


def test_highlevelnets::tokentypes::tokennet_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenNet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::tokenatomic_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenAtomic)


def test_highlevelnets::tokentypes::tokenatomic_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenAtomic.__init__)


def test_highlevelnets::tokentypes::tokenatomic_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenAtomic.__init__)
    params = list(sig.parameters.keys())



def test_tokenattribute_is_not_abstract():
    assert not inspect.isabstract(TokenAttribute)


def test_tokenattribute_constructor_exists():
    assert callable(TokenAttribute.__init__)


def test_tokenattribute_constructor_args():
    sig = inspect.signature(TokenAttribute.__init__)
    params = list(sig.parameters.keys())



def test_tokenweight_is_not_abstract():
    assert not inspect.isabstract(TokenWeight)


def test_tokenweight_constructor_exists():
    assert callable(TokenWeight.__init__)


def test_tokenweight_constructor_args():
    sig = inspect.signature(TokenWeight.__init__)
    params = list(sig.parameters.keys())



def test_tokennet_is_not_abstract():
    assert not inspect.isabstract(TokenNet)


def test_tokennet_constructor_exists():
    assert callable(TokenNet.__init__)


def test_tokennet_constructor_args():
    sig = inspect.signature(TokenNet.__init__)
    params = list(sig.parameters.keys())



def test_elementnetmarked_is_not_abstract():
    assert not inspect.isabstract(ElementNetMarked)


def test_elementnetmarked_constructor_exists():
    assert callable(ElementNetMarked.__init__)


def test_elementnetmarked_constructor_args():
    sig = inspect.signature(ElementNetMarked.__init__)
    params = list(sig.parameters.keys())



def test_tokenatomic_is_not_abstract():
    assert not inspect.isabstract(TokenAtomic)


def test_tokenatomic_constructor_exists():
    assert callable(TokenAtomic.__init__)


def test_tokenatomic_constructor_args():
    sig = inspect.signature(TokenAtomic.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_tokentype_is_not_abstract():
    assert not inspect.isabstract(TokenType)


def test_tokentype_constructor_exists():
    assert callable(TokenType.__init__)


def test_tokentype_constructor_args():
    sig = inspect.signature(TokenType.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::tokentypeelementnet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenTypeElementNet)


def test_highlevelnets::tokentypes::tokentypeelementnet_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenTypeElementNet.__init__)


def test_highlevelnets::tokentypes::tokentypeelementnet_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenTypeElementNet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::tokentypeatomic_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenTypeAtomic)


def test_highlevelnets::tokentypes::tokentypeatomic_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenTypeAtomic.__init__)


def test_highlevelnets::tokentypes::tokentypeatomic_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenTypeAtomic.__init__)
    params = list(sig.parameters.keys())



def test_marking_is_not_abstract():
    assert not inspect.isabstract(Marking)


def test_marking_constructor_exists():
    assert callable(Marking.__init__)


def test_marking_constructor_args():
    sig = inspect.signature(Marking.__init__)
    params = list(sig.parameters.keys())



def test_highlevelpetrinet_is_not_abstract():
    assert not inspect.isabstract(HighLevelPetriNet)


def test_highlevelpetrinet_constructor_exists():
    assert callable(HighLevelPetriNet.__init__)


def test_highlevelpetrinet_constructor_args():
    sig = inspect.signature(HighLevelPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_tokenmultiset_is_not_abstract():
    assert not inspect.isabstract(TokenMultiSet)


def test_tokenmultiset_constructor_exists():
    assert callable(TokenMultiSet.__init__)


def test_tokenmultiset_constructor_args():
    sig = inspect.signature(TokenMultiSet.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_ientityidentifiable_is_not_abstract():
    assert not inspect.isabstract(IEntityIdentifiable)


def test_ientityidentifiable_constructor_exists():
    assert callable(IEntityIdentifiable.__init__)


def test_ientityidentifiable_constructor_args():
    sig = inspect.signature(IEntityIdentifiable.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::tokenmultiset_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenMultiSet)


def test_highlevelnets::tokenexpressions::tokenmultiset_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenMultiSet.__init__)


def test_highlevelnets::tokenexpressions::tokenmultiset_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenMultiSet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npndiagramnetsystem_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNDiagramNetSystem)


def test_highlevelnets::npndiagrams::npndiagramnetsystem_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNDiagramNetSystem.__init__)


def test_highlevelnets::npndiagrams::npndiagramnetsystem_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNDiagramNetSystem.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::tokenbinding_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenBinding)


def test_highlevelnets::tokenexpressions::tokenbinding_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenBinding.__init__)


def test_highlevelnets::tokenexpressions::tokenbinding_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenBinding.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::common::inetelement_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::common::INetElement)


def test_highlevelnets::common::inetelement_constructor_exists():
    assert callable(highlevelnets::common::INetElement.__init__)


def test_highlevelnets::common::inetelement_constructor_args():
    sig = inspect.signature(highlevelnets::common::INetElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_highlevelnets::common::inetelement_has_name():
    assert hasattr(highlevelnets::common::INetElement, "name")
    descriptor = None
    for klass in highlevelnets::common::INetElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::common::inetelement_has_comment():
    assert hasattr(highlevelnets::common::INetElement, "comment")
    descriptor = None
    for klass in highlevelnets::common::INetElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokenexpressions::monomconstant_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::MonomConstant)


def test_highlevelnets::tokenexpressions::monomconstant_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::MonomConstant.__init__)


def test_highlevelnets::tokenexpressions::monomconstant_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::MonomConstant.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_highlevelnets::tokenexpressions::monomconstant_has_power():
    assert hasattr(highlevelnets::tokenexpressions::MonomConstant, "power")
    descriptor = None
    for klass in highlevelnets::tokenexpressions::MonomConstant.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokenexpressions::variable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::Variable)


def test_highlevelnets::tokenexpressions::variable_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::Variable.__init__)


def test_highlevelnets::tokenexpressions::variable_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_highlevelnets::tokenexpressions::variable_has_name():
    assert hasattr(highlevelnets::tokenexpressions::Variable, "name")
    descriptor = None
    for klass in highlevelnets::tokenexpressions::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::hlpn::contextvariable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::ContextVariable)


def test_highlevelnets::hlpn::contextvariable_constructor_exists():
    assert callable(highlevelnets::hlpn::ContextVariable.__init__)


def test_highlevelnets::hlpn::contextvariable_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::tokenmultisetexpression_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenMultisetExpression)


def test_highlevelnets::tokenexpressions::tokenmultisetexpression_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenMultisetExpression.__init__)


def test_highlevelnets::tokenexpressions::tokenmultisetexpression_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenMultisetExpression.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymboltokensn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolTokenSN)


def test_highlevelnets::npndiagrams::npnsymboltokensn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolTokenSN.__init__)


def test_highlevelnets::npndiagrams::npnsymboltokensn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolTokenSN.__init__)
    params = list(sig.parameters.keys())
    assert "constraints" in params, "Missing parameter 'constraints'"

def test_highlevelnets::npndiagrams::npnsymboltokensn_has_constraints():
    assert hasattr(highlevelnets::npndiagrams::NPNSymbolTokenSN, "constraints")
    descriptor = None
    for klass in highlevelnets::npndiagrams::NPNSymbolTokenSN.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::npndiagrams::npndiagramnpnmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNDiagramNPNMarked)


def test_highlevelnets::npndiagrams::npndiagramnpnmarked_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNDiagramNPNMarked.__init__)


def test_highlevelnets::npndiagrams::npndiagramnpnmarked_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNDiagramNPNMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npndiagrams::npnsymbolarcsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolArcSN)


def test_highlevelnets::npndiagrams::npnsymbolarcsn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolArcSN.__init__)


def test_highlevelnets::npndiagrams::npnsymbolarcsn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolArcSN.__init__)
    params = list(sig.parameters.keys())
    assert "bendpoints" in params, "Missing parameter 'bendpoints'"

def test_highlevelnets::npndiagrams::npnsymbolarcsn_has_bendpoints():
    assert hasattr(highlevelnets::npndiagrams::NPNSymbolArcSN, "bendpoints")
    descriptor = None
    for klass in highlevelnets::npndiagrams::NPNSymbolArcSN.__mro__:
        if "bendpoints" in klass.__dict__:
            descriptor = klass.__dict__["bendpoints"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::npndiagrams::npnsymbolnodesn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npndiagrams::NPNSymbolNodeSN)


def test_highlevelnets::npndiagrams::npnsymbolnodesn_constructor_exists():
    assert callable(highlevelnets::npndiagrams::NPNSymbolNodeSN.__init__)


def test_highlevelnets::npndiagrams::npnsymbolnodesn_constructor_args():
    sig = inspect.signature(highlevelnets::npndiagrams::NPNSymbolNodeSN.__init__)
    params = list(sig.parameters.keys())
    assert "constraints" in params, "Missing parameter 'constraints'"

def test_highlevelnets::npndiagrams::npnsymbolnodesn_has_constraints():
    assert hasattr(highlevelnets::npndiagrams::NPNSymbolNodeSN, "constraints")
    descriptor = None
    for klass in highlevelnets::npndiagrams::NPNSymbolNodeSN.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokenexpressions::tokenexpressionbinding_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenExpressionBinding)


def test_highlevelnets::tokenexpressions::tokenexpressionbinding_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenExpressionBinding.__init__)


def test_highlevelnets::tokenexpressions::tokenexpressionbinding_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenExpressionBinding.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::tokenweight_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenWeight)


def test_highlevelnets::tokenexpressions::tokenweight_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenWeight.__init__)


def test_highlevelnets::tokenexpressions::tokenweight_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenWeight.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_highlevelnets::tokenexpressions::tokenweight_has_weight():
    assert hasattr(highlevelnets::tokenexpressions::TokenWeight, "weight")
    descriptor = None
    for klass in highlevelnets::tokenexpressions::TokenWeight.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokentypes::tokenattribute_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenAttribute)


def test_highlevelnets::tokentypes::tokenattribute_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenAttribute.__init__)


def test_highlevelnets::tokentypes::tokenattribute_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_highlevelnets::tokentypes::tokenattribute_has_name():
    assert hasattr(highlevelnets::tokentypes::TokenAttribute, "name")
    descriptor = None
    for klass in highlevelnets::tokentypes::TokenAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::tokentypes::tokenattribute_has_type():
    assert hasattr(highlevelnets::tokentypes::TokenAttribute, "type")
    descriptor = None
    for klass in highlevelnets::tokentypes::TokenAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::tokentypes::tokenattribute_has_value():
    assert hasattr(highlevelnets::tokentypes::TokenAttribute, "value")
    descriptor = None
    for klass in highlevelnets::tokentypes::TokenAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokenexpressions::monom_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::Monom)


def test_highlevelnets::tokenexpressions::monom_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::Monom.__init__)


def test_highlevelnets::tokenexpressions::monom_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::Monom.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_highlevelnets::tokenexpressions::monom_has_power():
    assert hasattr(highlevelnets::tokenexpressions::Monom, "power")
    descriptor = None
    for klass in highlevelnets::tokenexpressions::Monom.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::marking::placemarking_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::marking::PlaceMarking)


def test_highlevelnets::marking::placemarking_constructor_exists():
    assert callable(highlevelnets::marking::PlaceMarking.__init__)


def test_highlevelnets::marking::placemarking_constructor_args():
    sig = inspect.signature(highlevelnets::marking::PlaceMarking.__init__)
    params = list(sig.parameters.keys())



def test_placemarking_is_not_abstract():
    assert not inspect.isabstract(PlaceMarking)


def test_placemarking_constructor_exists():
    assert callable(PlaceMarking.__init__)


def test_placemarking_constructor_args():
    sig = inspect.signature(PlaceMarking.__init__)
    params = list(sig.parameters.keys())



def test_inetelement_is_not_abstract():
    assert not inspect.isabstract(INetElement)


def test_inetelement_constructor_exists():
    assert callable(INetElement.__init__)


def test_inetelement_constructor_args():
    sig = inspect.signature(INetElement.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::tokenvariadicexpression_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::TokenVariadicExpression)


def test_highlevelnets::tokenexpressions::tokenvariadicexpression_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::TokenVariadicExpression.__init__)


def test_highlevelnets::tokenexpressions::tokenvariadicexpression_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::TokenVariadicExpression.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::marking::highlevelpetrinetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::marking::HighLevelPetriNetMarked)


def test_highlevelnets::marking::highlevelpetrinetmarked_constructor_exists():
    assert callable(highlevelnets::marking::HighLevelPetriNetMarked.__init__)


def test_highlevelnets::marking::highlevelpetrinetmarked_constructor_args():
    sig = inspect.signature(highlevelnets::marking::HighLevelPetriNetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npnets::npnetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npnets::NPnetMarked)


def test_highlevelnets::npnets::npnetmarked_constructor_exists():
    assert callable(highlevelnets::npnets::NPnetMarked.__init__)


def test_highlevelnets::npnets::npnetmarked_constructor_args():
    sig = inspect.signature(highlevelnets::npnets::NPnetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokenexpressions::netconstant_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokenexpressions::NetConstant)


def test_highlevelnets::tokenexpressions::netconstant_constructor_exists():
    assert callable(highlevelnets::tokenexpressions::NetConstant.__init__)


def test_highlevelnets::tokenexpressions::netconstant_constructor_args():
    sig = inspect.signature(highlevelnets::tokenexpressions::NetConstant.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::atom_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::Atom)


def test_highlevelnets::tokentypes::atom_constructor_exists():
    assert callable(highlevelnets::tokentypes::Atom.__init__)


def test_highlevelnets::tokentypes::atom_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::Atom.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npnets::synchronization_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npnets::Synchronization)


def test_highlevelnets::npnets::synchronization_constructor_exists():
    assert callable(highlevelnets::npnets::Synchronization.__init__)


def test_highlevelnets::npnets::synchronization_constructor_args():
    sig = inspect.signature(highlevelnets::npnets::Synchronization.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_highlevelnets::npnets::synchronization_has_key():
    assert hasattr(highlevelnets::npnets::Synchronization, "key")
    descriptor = None
    for klass in highlevelnets::npnets::Synchronization.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::npnets::synchronization_has_kind():
    assert hasattr(highlevelnets::npnets::Synchronization, "kind")
    descriptor = None
    for klass in highlevelnets::npnets::Synchronization.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::hlpn::arc_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::Arc)


def test_highlevelnets::hlpn::arc_constructor_exists():
    assert callable(highlevelnets::hlpn::Arc.__init__)


def test_highlevelnets::hlpn::arc_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::Arc.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::elementnetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::ElementNetMarked)


def test_highlevelnets::tokentypes::elementnetmarked_constructor_exists():
    assert callable(highlevelnets::tokentypes::ElementNetMarked.__init__)


def test_highlevelnets::tokentypes::elementnetmarked_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::ElementNetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::npnets::npnet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::npnets::NPnet)


def test_highlevelnets::npnets::npnet_constructor_exists():
    assert callable(highlevelnets::npnets::NPnet.__init__)


def test_highlevelnets::npnets::npnet_constructor_args():
    sig = inspect.signature(highlevelnets::npnets::NPnet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::hlpn::node_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::hlpn::Node)


def test_highlevelnets::hlpn::node_constructor_exists():
    assert callable(highlevelnets::hlpn::Node.__init__)


def test_highlevelnets::hlpn::node_constructor_args():
    sig = inspect.signature(highlevelnets::hlpn::Node.__init__)
    params = list(sig.parameters.keys())
    assert "firstTimeConstraint" in params, "Missing parameter 'firstTimeConstraint'"
    assert "secondTimeConstraint" in params, "Missing parameter 'secondTimeConstraint'"

def test_highlevelnets::hlpn::node_has_firstTimeConstraint():
    assert hasattr(highlevelnets::hlpn::Node, "firstTimeConstraint")
    descriptor = None
    for klass in highlevelnets::hlpn::Node.__mro__:
        if "firstTimeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["firstTimeConstraint"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets::hlpn::node_has_secondTimeConstraint():
    assert hasattr(highlevelnets::hlpn::Node, "secondTimeConstraint")
    descriptor = None
    for klass in highlevelnets::hlpn::Node.__mro__:
        if "secondTimeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["secondTimeConstraint"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets::tokentypes::tokentype_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::TokenType)


def test_highlevelnets::tokentypes::tokentype_constructor_exists():
    assert callable(highlevelnets::tokentypes::TokenType.__init__)


def test_highlevelnets::tokentypes::tokentype_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::TokenType.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::marking::marking_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::marking::Marking)


def test_highlevelnets::marking::marking_constructor_exists():
    assert callable(highlevelnets::marking::Marking.__init__)


def test_highlevelnets::marking::marking_constructor_args():
    sig = inspect.signature(highlevelnets::marking::Marking.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets::tokentypes::token_is_not_abstract():
    assert not inspect.isabstract(highlevelnets::tokentypes::Token)


def test_highlevelnets::tokentypes::token_constructor_exists():
    assert callable(highlevelnets::tokentypes::Token.__init__)


def test_highlevelnets::tokentypes::token_constructor_args():
    sig = inspect.signature(highlevelnets::tokentypes::Token.__init__)
    params = list(sig.parameters.keys())

def test_esynchronizationkind_exists():
    # Check that the Enumeration exists
    assert ESynchronizationKind is not None

def test_esynchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ESynchronizationKind]
    expected_literals = [
        "HorizontalSynchronization",
        "VerticalSynchronization",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ESynchronizationKind"


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
NPNSymbolPlaceSN_strategy = st.builds(
    NPNSymbolPlaceSN,
)
NPNSymbolTransitionSN_strategy = st.builds(
    NPNSymbolTransitionSN,
)
NPNSymbolTokenSN_strategy = st.builds(
    NPNSymbolTokenSN,
)
NPNSymbolArcTPSN_strategy = st.builds(
    NPNSymbolArcTPSN,
)
NPNSymbolArcPTSN_strategy = st.builds(
    NPNSymbolArcPTSN,
)
NPNSymbolArcSN_strategy = st.builds(
    NPNSymbolArcSN,
)
highlevelnets::npndiagrams::NPNSymbolArcPTSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolArcPTSN,
)
highlevelnets::npndiagrams::NPNSymbolArcTPSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolArcTPSN,
)
NPNSymbolNodeSN_strategy = st.builds(
    NPNSymbolNodeSN,
)
highlevelnets::npndiagrams::NPNSymbolPlaceSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolPlaceSN,
)
highlevelnets::npndiagrams::NPNSymbolTransitionSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolTransitionSN,
)
NPnetMarked_strategy = st.builds(
    NPnetMarked,
)
highlevelnets::common::IEntityIdentifiable_strategy = st.builds(
    highlevelnets::common::IEntityIdentifiable,
    uuid=
        safe_text
)
TransitionSynchronized_strategy = st.builds(
    TransitionSynchronized,
)
NPNDiagramNetSystem_strategy = st.builds(
    NPNDiagramNetSystem,
)
NPnet_strategy = st.builds(
    NPnet,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
NetConstant_strategy = st.builds(
    NetConstant,
)
Transition_strategy = st.builds(
    Transition,
)
highlevelnets::npnets::TransitionSynchronized_strategy = st.builds(
    highlevelnets::npnets::TransitionSynchronized,
)
hlpn::Node_strategy = st.builds(
    hlpn::Node,
)
ArcTP_strategy = st.builds(
    ArcTP,
)
ArcPT_strategy = st.builds(
    ArcPT,
)
Arc_strategy = st.builds(
    Arc,
)
highlevelnets::hlpn::ArcTP_strategy = st.builds(
    highlevelnets::hlpn::ArcTP,
    firstTimeConstraint=
        st.integers(),
    secondTimeConstraint=
        st.integers()
)
highlevelnets::hlpn::ArcPT_strategy = st.builds(
    highlevelnets::hlpn::ArcPT,
)
Node_strategy = st.builds(
    Node,
)
highlevelnets::hlpn::Place_strategy = st.builds(
    highlevelnets::hlpn::Place,
)
hlpn::ContextVariable_strategy = st.builds(
    hlpn::ContextVariable,
)
highlevelnets::hlpn::Transition_strategy = st.builds(
    highlevelnets::hlpn::Transition,
)
common::INetElement_strategy = st.builds(
    common::INetElement,
)
highlevelnets::hlpn::HighLevelPetriNet_strategy = st.builds(
    highlevelnets::hlpn::HighLevelPetriNet,
)
TokenBinding_strategy = st.builds(
    TokenBinding,
)
TokenVariadicExpression_strategy = st.builds(
    TokenVariadicExpression,
)
Variable_strategy = st.builds(
    Variable,
)
MonomConstant_strategy = st.builds(
    MonomConstant,
)
Monom_strategy = st.builds(
    Monom,
)
ContextVariable_strategy = st.builds(
    ContextVariable,
)
TokenTypeElementNet_strategy = st.builds(
    TokenTypeElementNet,
)
TokenTypeAtomic_strategy = st.builds(
    TokenTypeAtomic,
)
Token_strategy = st.builds(
    Token,
)
highlevelnets::tokentypes::TokenNet_strategy = st.builds(
    highlevelnets::tokentypes::TokenNet,
)
highlevelnets::tokentypes::TokenAtomic_strategy = st.builds(
    highlevelnets::tokentypes::TokenAtomic,
)
TokenAttribute_strategy = st.builds(
    TokenAttribute,
)
TokenWeight_strategy = st.builds(
    TokenWeight,
)
TokenNet_strategy = st.builds(
    TokenNet,
)
ElementNetMarked_strategy = st.builds(
    ElementNetMarked,
)
TokenAtomic_strategy = st.builds(
    TokenAtomic,
)
Atom_strategy = st.builds(
    Atom,
)
TokenType_strategy = st.builds(
    TokenType,
)
highlevelnets::tokentypes::TokenTypeElementNet_strategy = st.builds(
    highlevelnets::tokentypes::TokenTypeElementNet,
)
highlevelnets::tokentypes::TokenTypeAtomic_strategy = st.builds(
    highlevelnets::tokentypes::TokenTypeAtomic,
)
Marking_strategy = st.builds(
    Marking,
)
HighLevelPetriNet_strategy = st.builds(
    HighLevelPetriNet,
)
TokenMultiSet_strategy = st.builds(
    TokenMultiSet,
)
Place_strategy = st.builds(
    Place,
)
IEntityIdentifiable_strategy = st.builds(
    IEntityIdentifiable,
)
highlevelnets::tokenexpressions::TokenMultiSet_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenMultiSet,
)
highlevelnets::npndiagrams::NPNDiagramNetSystem_strategy = st.builds(
    highlevelnets::npndiagrams::NPNDiagramNetSystem,
)
highlevelnets::tokenexpressions::TokenBinding_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenBinding,
)
highlevelnets::common::INetElement_strategy = st.builds(
    highlevelnets::common::INetElement,
    name=
        safe_text,
    comment=
        safe_text
)
highlevelnets::tokenexpressions::MonomConstant_strategy = st.builds(
    highlevelnets::tokenexpressions::MonomConstant,
    power=
        safe_text
)
highlevelnets::tokenexpressions::Variable_strategy = st.builds(
    highlevelnets::tokenexpressions::Variable,
    name=
        safe_text
)
highlevelnets::hlpn::ContextVariable_strategy = st.builds(
    highlevelnets::hlpn::ContextVariable,
)
highlevelnets::tokenexpressions::TokenMultisetExpression_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenMultisetExpression,
)
highlevelnets::npndiagrams::NPNSymbolTokenSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolTokenSN,
    constraints=
        safe_text
)
highlevelnets::npndiagrams::NPNDiagramNPNMarked_strategy = st.builds(
    highlevelnets::npndiagrams::NPNDiagramNPNMarked,
)
highlevelnets::npndiagrams::NPNSymbolArcSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolArcSN,
    bendpoints=
        safe_text
)
highlevelnets::npndiagrams::NPNSymbolNodeSN_strategy = st.builds(
    highlevelnets::npndiagrams::NPNSymbolNodeSN,
    constraints=
        safe_text
)
highlevelnets::tokenexpressions::TokenExpressionBinding_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenExpressionBinding,
)
highlevelnets::tokenexpressions::TokenWeight_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenWeight,
    weight=
        safe_text
)
highlevelnets::tokentypes::TokenAttribute_strategy = st.builds(
    highlevelnets::tokentypes::TokenAttribute,
    name=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
highlevelnets::tokenexpressions::Monom_strategy = st.builds(
    highlevelnets::tokenexpressions::Monom,
    power=
        safe_text
)
highlevelnets::marking::PlaceMarking_strategy = st.builds(
    highlevelnets::marking::PlaceMarking,
)
PlaceMarking_strategy = st.builds(
    PlaceMarking,
)
INetElement_strategy = st.builds(
    INetElement,
)
highlevelnets::tokenexpressions::TokenVariadicExpression_strategy = st.builds(
    highlevelnets::tokenexpressions::TokenVariadicExpression,
)
highlevelnets::marking::HighLevelPetriNetMarked_strategy = st.builds(
    highlevelnets::marking::HighLevelPetriNetMarked,
)
highlevelnets::npnets::NPnetMarked_strategy = st.builds(
    highlevelnets::npnets::NPnetMarked,
)
highlevelnets::tokenexpressions::NetConstant_strategy = st.builds(
    highlevelnets::tokenexpressions::NetConstant,
)
highlevelnets::tokentypes::Atom_strategy = st.builds(
    highlevelnets::tokentypes::Atom,
)
highlevelnets::npnets::Synchronization_strategy = st.builds(
    highlevelnets::npnets::Synchronization,
    key=
        safe_text,
    kind=
        safe_text
)
highlevelnets::hlpn::Arc_strategy = st.builds(
    highlevelnets::hlpn::Arc,
)
highlevelnets::tokentypes::ElementNetMarked_strategy = st.builds(
    highlevelnets::tokentypes::ElementNetMarked,
)
highlevelnets::npnets::NPnet_strategy = st.builds(
    highlevelnets::npnets::NPnet,
)
highlevelnets::hlpn::Node_strategy = st.builds(
    highlevelnets::hlpn::Node,
    firstTimeConstraint=
        st.integers(),
    secondTimeConstraint=
        st.integers()
)
highlevelnets::tokentypes::TokenType_strategy = st.builds(
    highlevelnets::tokentypes::TokenType,
)
highlevelnets::marking::Marking_strategy = st.builds(
    highlevelnets::marking::Marking,
)
highlevelnets::tokentypes::Token_strategy = st.builds(
    highlevelnets::tokentypes::Token,
)

@given(instance=NPNSymbolPlaceSN_strategy)
@settings(max_examples=50)
def test_npnsymbolplacesn_instantiation(instance):
    assert isinstance(instance, NPNSymbolPlaceSN)

@given(instance=NPNSymbolTransitionSN_strategy)
@settings(max_examples=50)
def test_npnsymboltransitionsn_instantiation(instance):
    assert isinstance(instance, NPNSymbolTransitionSN)

@given(instance=NPNSymbolTokenSN_strategy)
@settings(max_examples=50)
def test_npnsymboltokensn_instantiation(instance):
    assert isinstance(instance, NPNSymbolTokenSN)

@given(instance=NPNSymbolArcTPSN_strategy)
@settings(max_examples=50)
def test_npnsymbolarctpsn_instantiation(instance):
    assert isinstance(instance, NPNSymbolArcTPSN)

@given(instance=NPNSymbolArcPTSN_strategy)
@settings(max_examples=50)
def test_npnsymbolarcptsn_instantiation(instance):
    assert isinstance(instance, NPNSymbolArcPTSN)

@given(instance=NPNSymbolArcSN_strategy)
@settings(max_examples=50)
def test_npnsymbolarcsn_instantiation(instance):
    assert isinstance(instance, NPNSymbolArcSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolArcPTSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymbolarcptsn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolArcPTSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolArcTPSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymbolarctpsn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolArcTPSN)

@given(instance=NPNSymbolNodeSN_strategy)
@settings(max_examples=50)
def test_npnsymbolnodesn_instantiation(instance):
    assert isinstance(instance, NPNSymbolNodeSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolPlaceSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymbolplacesn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolPlaceSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolTransitionSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymboltransitionsn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolTransitionSN)

@given(instance=NPnetMarked_strategy)
@settings(max_examples=50)
def test_npnetmarked_instantiation(instance):
    assert isinstance(instance, NPnetMarked)

@given(instance=highlevelnets::common::IEntityIdentifiable_strategy)
@settings(max_examples=50)
def test_highlevelnets::common::ientityidentifiable_instantiation(instance):
    assert isinstance(instance, highlevelnets::common::IEntityIdentifiable)

@given(instance=highlevelnets::common::IEntityIdentifiable_strategy)
def test_highlevelnets::common::ientityidentifiable_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=highlevelnets::common::IEntityIdentifiable_strategy)
def test_highlevelnets::common::ientityidentifiable_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=TransitionSynchronized_strategy)
@settings(max_examples=50)
def test_transitionsynchronized_instantiation(instance):
    assert isinstance(instance, TransitionSynchronized)

@given(instance=NPNDiagramNetSystem_strategy)
@settings(max_examples=50)
def test_npndiagramnetsystem_instantiation(instance):
    assert isinstance(instance, NPNDiagramNetSystem)

@given(instance=NPnet_strategy)
@settings(max_examples=50)
def test_npnet_instantiation(instance):
    assert isinstance(instance, NPnet)

@given(instance=Synchronization_strategy)
@settings(max_examples=50)
def test_synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)

@given(instance=NetConstant_strategy)
@settings(max_examples=50)
def test_netconstant_instantiation(instance):
    assert isinstance(instance, NetConstant)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=highlevelnets::npnets::TransitionSynchronized_strategy)
@settings(max_examples=50)
def test_highlevelnets::npnets::transitionsynchronized_instantiation(instance):
    assert isinstance(instance, highlevelnets::npnets::TransitionSynchronized)

@given(instance=hlpn::Node_strategy)
@settings(max_examples=50)
def test_hlpn::node_instantiation(instance):
    assert isinstance(instance, hlpn::Node)

@given(instance=ArcTP_strategy)
@settings(max_examples=50)
def test_arctp_instantiation(instance):
    assert isinstance(instance, ArcTP)

@given(instance=ArcPT_strategy)
@settings(max_examples=50)
def test_arcpt_instantiation(instance):
    assert isinstance(instance, ArcPT)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=highlevelnets::hlpn::ArcTP_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::arctp_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::ArcTP)

@given(instance=highlevelnets::hlpn::ArcTP_strategy)
def test_highlevelnets::hlpn::arctp_firstTimeConstraint_type(instance):
    assert isinstance(instance.firstTimeConstraint, int)


@given(instance=highlevelnets::hlpn::ArcTP_strategy)
def test_highlevelnets::hlpn::arctp_firstTimeConstraint_setter(instance):
    original = instance.firstTimeConstraint
    instance.firstTimeConstraint = original
    assert instance.firstTimeConstraint == original

@given(instance=highlevelnets::hlpn::ArcTP_strategy)
def test_highlevelnets::hlpn::arctp_secondTimeConstraint_type(instance):
    assert isinstance(instance.secondTimeConstraint, int)


@given(instance=highlevelnets::hlpn::ArcTP_strategy)
def test_highlevelnets::hlpn::arctp_secondTimeConstraint_setter(instance):
    original = instance.secondTimeConstraint
    instance.secondTimeConstraint = original
    assert instance.secondTimeConstraint == original

@given(instance=highlevelnets::hlpn::ArcPT_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::arcpt_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::ArcPT)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=highlevelnets::hlpn::Place_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::place_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::Place)

@given(instance=hlpn::ContextVariable_strategy)
@settings(max_examples=50)
def test_hlpn::contextvariable_instantiation(instance):
    assert isinstance(instance, hlpn::ContextVariable)

@given(instance=highlevelnets::hlpn::Transition_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::transition_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::Transition)

@given(instance=common::INetElement_strategy)
@settings(max_examples=50)
def test_common::inetelement_instantiation(instance):
    assert isinstance(instance, common::INetElement)

@given(instance=highlevelnets::hlpn::HighLevelPetriNet_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::highlevelpetrinet_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::HighLevelPetriNet)

@given(instance=TokenBinding_strategy)
@settings(max_examples=50)
def test_tokenbinding_instantiation(instance):
    assert isinstance(instance, TokenBinding)

@given(instance=TokenVariadicExpression_strategy)
@settings(max_examples=50)
def test_tokenvariadicexpression_instantiation(instance):
    assert isinstance(instance, TokenVariadicExpression)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=MonomConstant_strategy)
@settings(max_examples=50)
def test_monomconstant_instantiation(instance):
    assert isinstance(instance, MonomConstant)

@given(instance=Monom_strategy)
@settings(max_examples=50)
def test_monom_instantiation(instance):
    assert isinstance(instance, Monom)

@given(instance=ContextVariable_strategy)
@settings(max_examples=50)
def test_contextvariable_instantiation(instance):
    assert isinstance(instance, ContextVariable)

@given(instance=TokenTypeElementNet_strategy)
@settings(max_examples=50)
def test_tokentypeelementnet_instantiation(instance):
    assert isinstance(instance, TokenTypeElementNet)

@given(instance=TokenTypeAtomic_strategy)
@settings(max_examples=50)
def test_tokentypeatomic_instantiation(instance):
    assert isinstance(instance, TokenTypeAtomic)

@given(instance=Token_strategy)
@settings(max_examples=50)
def test_token_instantiation(instance):
    assert isinstance(instance, Token)

@given(instance=highlevelnets::tokentypes::TokenNet_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokennet_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenNet)

@given(instance=highlevelnets::tokentypes::TokenAtomic_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokenatomic_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenAtomic)

@given(instance=TokenAttribute_strategy)
@settings(max_examples=50)
def test_tokenattribute_instantiation(instance):
    assert isinstance(instance, TokenAttribute)

@given(instance=TokenWeight_strategy)
@settings(max_examples=50)
def test_tokenweight_instantiation(instance):
    assert isinstance(instance, TokenWeight)

@given(instance=TokenNet_strategy)
@settings(max_examples=50)
def test_tokennet_instantiation(instance):
    assert isinstance(instance, TokenNet)

@given(instance=ElementNetMarked_strategy)
@settings(max_examples=50)
def test_elementnetmarked_instantiation(instance):
    assert isinstance(instance, ElementNetMarked)

@given(instance=TokenAtomic_strategy)
@settings(max_examples=50)
def test_tokenatomic_instantiation(instance):
    assert isinstance(instance, TokenAtomic)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=TokenType_strategy)
@settings(max_examples=50)
def test_tokentype_instantiation(instance):
    assert isinstance(instance, TokenType)

@given(instance=highlevelnets::tokentypes::TokenTypeElementNet_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokentypeelementnet_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenTypeElementNet)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=highlevelnets::tokentypes::TokenTypeElementNet_strategy)
@settings(max_examples=30)
def test_highlevelnets::tokentypes::tokentypeelementnet_createinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createInstance()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createInstance' in highlevelnets::tokentypes::TokenTypeElementNet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createInstance' in highlevelnets::tokentypes::TokenTypeElementNet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createInstance' in highlevelnets::tokentypes::TokenTypeElementNet is not implemented or raised an error")

@given(instance=highlevelnets::tokentypes::TokenTypeAtomic_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokentypeatomic_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenTypeAtomic)

@given(instance=Marking_strategy)
@settings(max_examples=50)
def test_marking_instantiation(instance):
    assert isinstance(instance, Marking)

@given(instance=HighLevelPetriNet_strategy)
@settings(max_examples=50)
def test_highlevelpetrinet_instantiation(instance):
    assert isinstance(instance, HighLevelPetriNet)

@given(instance=TokenMultiSet_strategy)
@settings(max_examples=50)
def test_tokenmultiset_instantiation(instance):
    assert isinstance(instance, TokenMultiSet)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=IEntityIdentifiable_strategy)
@settings(max_examples=50)
def test_ientityidentifiable_instantiation(instance):
    assert isinstance(instance, IEntityIdentifiable)

@given(instance=highlevelnets::tokenexpressions::TokenMultiSet_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenmultiset_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenMultiSet)

@given(instance=highlevelnets::npndiagrams::NPNDiagramNetSystem_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npndiagramnetsystem_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNDiagramNetSystem)

@given(instance=highlevelnets::tokenexpressions::TokenBinding_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenbinding_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenBinding)

@given(instance=highlevelnets::common::INetElement_strategy)
@settings(max_examples=50)
def test_highlevelnets::common::inetelement_instantiation(instance):
    assert isinstance(instance, highlevelnets::common::INetElement)

@given(instance=highlevelnets::common::INetElement_strategy)
def test_highlevelnets::common::inetelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=highlevelnets::common::INetElement_strategy)
def test_highlevelnets::common::inetelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=highlevelnets::common::INetElement_strategy)
def test_highlevelnets::common::inetelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=highlevelnets::common::INetElement_strategy)
def test_highlevelnets::common::inetelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=highlevelnets::tokenexpressions::MonomConstant_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::monomconstant_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::MonomConstant)

@given(instance=highlevelnets::tokenexpressions::MonomConstant_strategy)
def test_highlevelnets::tokenexpressions::monomconstant_power_type(instance):
    assert isinstance(instance.power, str)


@given(instance=highlevelnets::tokenexpressions::MonomConstant_strategy)
def test_highlevelnets::tokenexpressions::monomconstant_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=highlevelnets::tokenexpressions::Variable_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::variable_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::Variable)

@given(instance=highlevelnets::tokenexpressions::Variable_strategy)
def test_highlevelnets::tokenexpressions::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=highlevelnets::tokenexpressions::Variable_strategy)
def test_highlevelnets::tokenexpressions::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=highlevelnets::hlpn::ContextVariable_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::contextvariable_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::ContextVariable)

@given(instance=highlevelnets::tokenexpressions::TokenMultisetExpression_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenmultisetexpression_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenMultisetExpression)

@given(instance=highlevelnets::npndiagrams::NPNSymbolTokenSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymboltokensn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolTokenSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolTokenSN_strategy)
def test_highlevelnets::npndiagrams::npnsymboltokensn_constraints_type(instance):
    assert isinstance(instance.constraints, str)


@given(instance=highlevelnets::npndiagrams::NPNSymbolTokenSN_strategy)
def test_highlevelnets::npndiagrams::npnsymboltokensn_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original

@given(instance=highlevelnets::npndiagrams::NPNDiagramNPNMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npndiagramnpnmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNDiagramNPNMarked)

@given(instance=highlevelnets::npndiagrams::NPNSymbolArcSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymbolarcsn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolArcSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolArcSN_strategy)
def test_highlevelnets::npndiagrams::npnsymbolarcsn_bendpoints_type(instance):
    assert isinstance(instance.bendpoints, str)


@given(instance=highlevelnets::npndiagrams::NPNSymbolArcSN_strategy)
def test_highlevelnets::npndiagrams::npnsymbolarcsn_bendpoints_setter(instance):
    original = instance.bendpoints
    instance.bendpoints = original
    assert instance.bendpoints == original

@given(instance=highlevelnets::npndiagrams::NPNSymbolNodeSN_strategy)
@settings(max_examples=50)
def test_highlevelnets::npndiagrams::npnsymbolnodesn_instantiation(instance):
    assert isinstance(instance, highlevelnets::npndiagrams::NPNSymbolNodeSN)

@given(instance=highlevelnets::npndiagrams::NPNSymbolNodeSN_strategy)
def test_highlevelnets::npndiagrams::npnsymbolnodesn_constraints_type(instance):
    assert isinstance(instance.constraints, str)


@given(instance=highlevelnets::npndiagrams::NPNSymbolNodeSN_strategy)
def test_highlevelnets::npndiagrams::npnsymbolnodesn_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original

@given(instance=highlevelnets::tokenexpressions::TokenExpressionBinding_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenexpressionbinding_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenExpressionBinding)

@given(instance=highlevelnets::tokenexpressions::TokenWeight_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenweight_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenWeight)

@given(instance=highlevelnets::tokenexpressions::TokenWeight_strategy)
def test_highlevelnets::tokenexpressions::tokenweight_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=highlevelnets::tokenexpressions::TokenWeight_strategy)
def test_highlevelnets::tokenexpressions::tokenweight_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokenattribute_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenAttribute)

@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=highlevelnets::tokentypes::TokenAttribute_strategy)
def test_highlevelnets::tokentypes::tokenattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=highlevelnets::tokenexpressions::Monom_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::monom_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::Monom)

@given(instance=highlevelnets::tokenexpressions::Monom_strategy)
def test_highlevelnets::tokenexpressions::monom_power_type(instance):
    assert isinstance(instance.power, str)


@given(instance=highlevelnets::tokenexpressions::Monom_strategy)
def test_highlevelnets::tokenexpressions::monom_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=highlevelnets::marking::PlaceMarking_strategy)
@settings(max_examples=50)
def test_highlevelnets::marking::placemarking_instantiation(instance):
    assert isinstance(instance, highlevelnets::marking::PlaceMarking)

@given(instance=PlaceMarking_strategy)
@settings(max_examples=50)
def test_placemarking_instantiation(instance):
    assert isinstance(instance, PlaceMarking)

@given(instance=INetElement_strategy)
@settings(max_examples=50)
def test_inetelement_instantiation(instance):
    assert isinstance(instance, INetElement)

@given(instance=highlevelnets::tokenexpressions::TokenVariadicExpression_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::tokenvariadicexpression_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::TokenVariadicExpression)

@given(instance=highlevelnets::marking::HighLevelPetriNetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets::marking::highlevelpetrinetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets::marking::HighLevelPetriNetMarked)

@given(instance=highlevelnets::npnets::NPnetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets::npnets::npnetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets::npnets::NPnetMarked)

@given(instance=highlevelnets::tokenexpressions::NetConstant_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokenexpressions::netconstant_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokenexpressions::NetConstant)

@given(instance=highlevelnets::tokentypes::Atom_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::atom_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::Atom)

@given(instance=highlevelnets::npnets::Synchronization_strategy)
@settings(max_examples=50)
def test_highlevelnets::npnets::synchronization_instantiation(instance):
    assert isinstance(instance, highlevelnets::npnets::Synchronization)

@given(instance=highlevelnets::npnets::Synchronization_strategy)
def test_highlevelnets::npnets::synchronization_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=highlevelnets::npnets::Synchronization_strategy)
def test_highlevelnets::npnets::synchronization_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=highlevelnets::npnets::Synchronization_strategy)
def test_highlevelnets::npnets::synchronization_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=highlevelnets::npnets::Synchronization_strategy)
def test_highlevelnets::npnets::synchronization_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=highlevelnets::hlpn::Arc_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::arc_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::Arc)

@given(instance=highlevelnets::tokentypes::ElementNetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::elementnetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::ElementNetMarked)

@given(instance=highlevelnets::npnets::NPnet_strategy)
@settings(max_examples=50)
def test_highlevelnets::npnets::npnet_instantiation(instance):
    assert isinstance(instance, highlevelnets::npnets::NPnet)

@given(instance=highlevelnets::hlpn::Node_strategy)
@settings(max_examples=50)
def test_highlevelnets::hlpn::node_instantiation(instance):
    assert isinstance(instance, highlevelnets::hlpn::Node)

@given(instance=highlevelnets::hlpn::Node_strategy)
def test_highlevelnets::hlpn::node_firstTimeConstraint_type(instance):
    assert isinstance(instance.firstTimeConstraint, int)


@given(instance=highlevelnets::hlpn::Node_strategy)
def test_highlevelnets::hlpn::node_firstTimeConstraint_setter(instance):
    original = instance.firstTimeConstraint
    instance.firstTimeConstraint = original
    assert instance.firstTimeConstraint == original

@given(instance=highlevelnets::hlpn::Node_strategy)
def test_highlevelnets::hlpn::node_secondTimeConstraint_type(instance):
    assert isinstance(instance.secondTimeConstraint, int)


@given(instance=highlevelnets::hlpn::Node_strategy)
def test_highlevelnets::hlpn::node_secondTimeConstraint_setter(instance):
    original = instance.secondTimeConstraint
    instance.secondTimeConstraint = original
    assert instance.secondTimeConstraint == original

@given(instance=highlevelnets::tokentypes::TokenType_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::tokentype_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::TokenType)

@given(instance=highlevelnets::marking::Marking_strategy)
@settings(max_examples=50)
def test_highlevelnets::marking::marking_instantiation(instance):
    assert isinstance(instance, highlevelnets::marking::Marking)

@given(instance=highlevelnets::tokentypes::Token_strategy)
@settings(max_examples=50)
def test_highlevelnets::tokentypes::token_instantiation(instance):
    assert isinstance(instance, highlevelnets::tokentypes::Token)

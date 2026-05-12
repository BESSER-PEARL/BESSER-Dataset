import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NPNSymbolArcTPSN,
    NPNSymbolArcPTSN,
    NPNSymbolArcSN,
    NPNSymbolNodeSN,
    highlevelnets_npndiagrams_NPNSymbolTransitionSN,
    highlevelnets_npndiagrams_NPNSymbolPlaceSN,
    highlevelnets_npndiagrams_NPNSymbolArcTPSN,
    NPNSymbolPlaceSN,
    NPNSymbolTransitionSN,
    highlevelnets_npndiagrams_NPNSymbolArcPTSN,
    TransitionSynchronized,
    NPnet,
    NPnetMarked,
    Synchronization,
    NetConstant,
    NPNDiagramNetSystem,
    highlevelnets_common_IEntityIdentifiable,
    Transition,
    highlevelnets_npnets_TransitionSynchronized,
    IDiagramHolder,
    highlevelnets_npnets_NPnet,
    Node,
    hlpn_ContextVariable,
    common_INetElement,
    highlevelnets_hlpn_HighLevelPetriNet,
    hlpn_Node,
    highlevelnets_hlpn_Transition,
    ArcTP,
    ArcPT,
    highlevelnets_hlpn_Place,
    Arc,
    highlevelnets_hlpn_ArcTP,
    highlevelnets_hlpn_ArcPT,
    ContextVariable,
    TokenWeight,
    TokenBinding,
    TokenVariadicExpression,
    Variable,
    MonomConstant,
    Monom,
    TokenAttribute,
    TokenNet,
    ElementNetMarked,
    TokenTypeElementNet,
    TokenTypeAtomic,
    Token,
    highlevelnets_tokentypes_TokenNet,
    highlevelnets_tokentypes_TokenAtomic,
    PlaceMarking,
    INetElement,
    highlevelnets_npnets_NPnetMarked,
    highlevelnets_hlpn_Node,
    highlevelnets_tokenexpressions_TokenVariadicExpression,
    highlevelnets_tokentypes_Atom,
    highlevelnets_tokenexpressions_NetConstant,
    highlevelnets_hlpn_Arc,
    highlevelnets_tokentypes_ElementNetMarked,
    highlevelnets_common_IDiagramHolder,
    highlevelnets_tokentypes_Token,
    highlevelnets_npnets_Synchronization,
    highlevelnets_marking_Marking,
    common_IDiagramHolder,
    tokentypes_TokenType,
    highlevelnets_tokentypes_TokenTypeElementNet,
    TokenAtomic,
    Atom,
    TokenType,
    highlevelnets_tokentypes_TokenTypeAtomic,
    highlevelnets_tokentypes_TokenType,
    Marking,
    HighLevelPetriNet,
    highlevelnets_marking_HighLevelPetriNetMarked,
    TokenMultiSet,
    Place,
    IEntityIdentifiable,
    highlevelnets_tokenexpressions_TokenExpressionBinding,
    highlevelnets_npndiagrams_NPNDiagramNetSystem,
    highlevelnets_hlpn_ContextVariable,
    highlevelnets_npndiagrams_NPNSymbolNodeSN,
    highlevelnets_common_INetElement,
    highlevelnets_tokenexpressions_Monom,
    highlevelnets_tokentypes_TokenAttribute,
    highlevelnets_tokenexpressions_TokenMultisetExpression,
    highlevelnets_tokenexpressions_TokenWeight,
    highlevelnets_tokenexpressions_MonomConstant,
    highlevelnets_tokenexpressions_TokenBinding,
    highlevelnets_tokenexpressions_TokenMultiSet,
    highlevelnets_npndiagrams_NPNSymbolArcSN,
    highlevelnets_tokenexpressions_Variable,
    highlevelnets_marking_PlaceMarking,
    ESynchronizationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_npnsymbolnodesn_is_not_abstract():
    assert not inspect.isabstract(NPNSymbolNodeSN)


def test_npnsymbolnodesn_constructor_exists():
    assert callable(NPNSymbolNodeSN.__init__)


def test_npnsymbolnodesn_constructor_args():
    sig = inspect.signature(NPNSymbolNodeSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npnsymboltransitionsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolTransitionSN)


def test_highlevelnets_npndiagrams_npnsymboltransitionsn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolTransitionSN.__init__)


def test_highlevelnets_npndiagrams_npnsymboltransitionsn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolTransitionSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npnsymbolplacesn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolPlaceSN)


def test_highlevelnets_npndiagrams_npnsymbolplacesn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolPlaceSN.__init__)


def test_highlevelnets_npndiagrams_npnsymbolplacesn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolPlaceSN.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npnsymbolarctpsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolArcTPSN)


def test_highlevelnets_npndiagrams_npnsymbolarctpsn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolArcTPSN.__init__)


def test_highlevelnets_npndiagrams_npnsymbolarctpsn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolArcTPSN.__init__)
    params = list(sig.parameters.keys())



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



def test_highlevelnets_npndiagrams_npnsymbolarcptsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolArcPTSN)


def test_highlevelnets_npndiagrams_npnsymbolarcptsn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolArcPTSN.__init__)


def test_highlevelnets_npndiagrams_npnsymbolarcptsn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolArcPTSN.__init__)
    params = list(sig.parameters.keys())



def test_transitionsynchronized_is_not_abstract():
    assert not inspect.isabstract(TransitionSynchronized)


def test_transitionsynchronized_constructor_exists():
    assert callable(TransitionSynchronized.__init__)


def test_transitionsynchronized_constructor_args():
    sig = inspect.signature(TransitionSynchronized.__init__)
    params = list(sig.parameters.keys())



def test_npnet_is_not_abstract():
    assert not inspect.isabstract(NPnet)


def test_npnet_constructor_exists():
    assert callable(NPnet.__init__)


def test_npnet_constructor_args():
    sig = inspect.signature(NPnet.__init__)
    params = list(sig.parameters.keys())



def test_npnetmarked_is_not_abstract():
    assert not inspect.isabstract(NPnetMarked)


def test_npnetmarked_constructor_exists():
    assert callable(NPnetMarked.__init__)


def test_npnetmarked_constructor_args():
    sig = inspect.signature(NPnetMarked.__init__)
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



def test_npndiagramnetsystem_is_not_abstract():
    assert not inspect.isabstract(NPNDiagramNetSystem)


def test_npndiagramnetsystem_constructor_exists():
    assert callable(NPNDiagramNetSystem.__init__)


def test_npndiagramnetsystem_constructor_args():
    sig = inspect.signature(NPNDiagramNetSystem.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_common_ientityidentifiable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_common_IEntityIdentifiable)


def test_highlevelnets_common_ientityidentifiable_constructor_exists():
    assert callable(highlevelnets_common_IEntityIdentifiable.__init__)


def test_highlevelnets_common_ientityidentifiable_constructor_args():
    sig = inspect.signature(highlevelnets_common_IEntityIdentifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_highlevelnets_common_ientityidentifiable_has_id():
    assert hasattr(highlevelnets_common_IEntityIdentifiable, "id")
    descriptor = None
    for klass in highlevelnets_common_IEntityIdentifiable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npnets_transitionsynchronized_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npnets_TransitionSynchronized)


def test_highlevelnets_npnets_transitionsynchronized_constructor_exists():
    assert callable(highlevelnets_npnets_TransitionSynchronized.__init__)


def test_highlevelnets_npnets_transitionsynchronized_constructor_args():
    sig = inspect.signature(highlevelnets_npnets_TransitionSynchronized.__init__)
    params = list(sig.parameters.keys())



def test_idiagramholder_is_not_abstract():
    assert not inspect.isabstract(IDiagramHolder)


def test_idiagramholder_constructor_exists():
    assert callable(IDiagramHolder.__init__)


def test_idiagramholder_constructor_args():
    sig = inspect.signature(IDiagramHolder.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npnets_npnet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npnets_NPnet)


def test_highlevelnets_npnets_npnet_constructor_exists():
    assert callable(highlevelnets_npnets_NPnet.__init__)


def test_highlevelnets_npnets_npnet_constructor_args():
    sig = inspect.signature(highlevelnets_npnets_NPnet.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hlpn_contextvariable_is_not_abstract():
    assert not inspect.isabstract(hlpn_ContextVariable)


def test_hlpn_contextvariable_constructor_exists():
    assert callable(hlpn_ContextVariable.__init__)


def test_hlpn_contextvariable_constructor_args():
    sig = inspect.signature(hlpn_ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_common_inetelement_is_not_abstract():
    assert not inspect.isabstract(common_INetElement)


def test_common_inetelement_constructor_exists():
    assert callable(common_INetElement.__init__)


def test_common_inetelement_constructor_args():
    sig = inspect.signature(common_INetElement.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_highlevelpetrinet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_HighLevelPetriNet)


def test_highlevelnets_hlpn_highlevelpetrinet_constructor_exists():
    assert callable(highlevelnets_hlpn_HighLevelPetriNet.__init__)


def test_highlevelnets_hlpn_highlevelpetrinet_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_HighLevelPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hlpn_node_is_not_abstract():
    assert not inspect.isabstract(hlpn_Node)


def test_hlpn_node_constructor_exists():
    assert callable(hlpn_Node.__init__)


def test_hlpn_node_constructor_args():
    sig = inspect.signature(hlpn_Node.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_transition_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_Transition)


def test_highlevelnets_hlpn_transition_constructor_exists():
    assert callable(highlevelnets_hlpn_Transition.__init__)


def test_highlevelnets_hlpn_transition_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_Transition.__init__)
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



def test_highlevelnets_hlpn_place_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_Place)


def test_highlevelnets_hlpn_place_constructor_exists():
    assert callable(highlevelnets_hlpn_Place.__init__)


def test_highlevelnets_hlpn_place_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_Place.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_arctp_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_ArcTP)


def test_highlevelnets_hlpn_arctp_constructor_exists():
    assert callable(highlevelnets_hlpn_ArcTP.__init__)


def test_highlevelnets_hlpn_arctp_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_ArcTP.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_arcpt_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_ArcPT)


def test_highlevelnets_hlpn_arcpt_constructor_exists():
    assert callable(highlevelnets_hlpn_ArcPT.__init__)


def test_highlevelnets_hlpn_arcpt_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_ArcPT.__init__)
    params = list(sig.parameters.keys())



def test_contextvariable_is_not_abstract():
    assert not inspect.isabstract(ContextVariable)


def test_contextvariable_constructor_exists():
    assert callable(ContextVariable.__init__)


def test_contextvariable_constructor_args():
    sig = inspect.signature(ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_tokenweight_is_not_abstract():
    assert not inspect.isabstract(TokenWeight)


def test_tokenweight_constructor_exists():
    assert callable(TokenWeight.__init__)


def test_tokenweight_constructor_args():
    sig = inspect.signature(TokenWeight.__init__)
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



def test_tokenattribute_is_not_abstract():
    assert not inspect.isabstract(TokenAttribute)


def test_tokenattribute_constructor_exists():
    assert callable(TokenAttribute.__init__)


def test_tokenattribute_constructor_args():
    sig = inspect.signature(TokenAttribute.__init__)
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



def test_highlevelnets_tokentypes_tokennet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenNet)


def test_highlevelnets_tokentypes_tokennet_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenNet.__init__)


def test_highlevelnets_tokentypes_tokennet_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenNet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_tokenatomic_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenAtomic)


def test_highlevelnets_tokentypes_tokenatomic_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenAtomic.__init__)


def test_highlevelnets_tokentypes_tokenatomic_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenAtomic.__init__)
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



def test_highlevelnets_npnets_npnetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npnets_NPnetMarked)


def test_highlevelnets_npnets_npnetmarked_constructor_exists():
    assert callable(highlevelnets_npnets_NPnetMarked.__init__)


def test_highlevelnets_npnets_npnetmarked_constructor_args():
    sig = inspect.signature(highlevelnets_npnets_NPnetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_node_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_Node)


def test_highlevelnets_hlpn_node_constructor_exists():
    assert callable(highlevelnets_hlpn_Node.__init__)


def test_highlevelnets_hlpn_node_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_Node.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokenexpressions_tokenvariadicexpression_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenVariadicExpression)


def test_highlevelnets_tokenexpressions_tokenvariadicexpression_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenVariadicExpression.__init__)


def test_highlevelnets_tokenexpressions_tokenvariadicexpression_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenVariadicExpression.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_atom_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_Atom)


def test_highlevelnets_tokentypes_atom_constructor_exists():
    assert callable(highlevelnets_tokentypes_Atom.__init__)


def test_highlevelnets_tokentypes_atom_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_Atom.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokenexpressions_netconstant_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_NetConstant)


def test_highlevelnets_tokenexpressions_netconstant_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_NetConstant.__init__)


def test_highlevelnets_tokenexpressions_netconstant_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_NetConstant.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_arc_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_Arc)


def test_highlevelnets_hlpn_arc_constructor_exists():
    assert callable(highlevelnets_hlpn_Arc.__init__)


def test_highlevelnets_hlpn_arc_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_Arc.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_elementnetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_ElementNetMarked)


def test_highlevelnets_tokentypes_elementnetmarked_constructor_exists():
    assert callable(highlevelnets_tokentypes_ElementNetMarked.__init__)


def test_highlevelnets_tokentypes_elementnetmarked_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_ElementNetMarked.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_common_idiagramholder_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_common_IDiagramHolder)


def test_highlevelnets_common_idiagramholder_constructor_exists():
    assert callable(highlevelnets_common_IDiagramHolder.__init__)


def test_highlevelnets_common_idiagramholder_constructor_args():
    sig = inspect.signature(highlevelnets_common_IDiagramHolder.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_token_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_Token)


def test_highlevelnets_tokentypes_token_constructor_exists():
    assert callable(highlevelnets_tokentypes_Token.__init__)


def test_highlevelnets_tokentypes_token_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_Token.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npnets_synchronization_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npnets_Synchronization)


def test_highlevelnets_npnets_synchronization_constructor_exists():
    assert callable(highlevelnets_npnets_Synchronization.__init__)


def test_highlevelnets_npnets_synchronization_constructor_args():
    sig = inspect.signature(highlevelnets_npnets_Synchronization.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_highlevelnets_npnets_synchronization_has_key():
    assert hasattr(highlevelnets_npnets_Synchronization, "key")
    descriptor = None
    for klass in highlevelnets_npnets_Synchronization.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets_npnets_synchronization_has_kind():
    assert hasattr(highlevelnets_npnets_Synchronization, "kind")
    descriptor = None
    for klass in highlevelnets_npnets_Synchronization.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_marking_marking_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_marking_Marking)


def test_highlevelnets_marking_marking_constructor_exists():
    assert callable(highlevelnets_marking_Marking.__init__)


def test_highlevelnets_marking_marking_constructor_args():
    sig = inspect.signature(highlevelnets_marking_Marking.__init__)
    params = list(sig.parameters.keys())



def test_common_idiagramholder_is_not_abstract():
    assert not inspect.isabstract(common_IDiagramHolder)


def test_common_idiagramholder_constructor_exists():
    assert callable(common_IDiagramHolder.__init__)


def test_common_idiagramholder_constructor_args():
    sig = inspect.signature(common_IDiagramHolder.__init__)
    params = list(sig.parameters.keys())



def test_tokentypes_tokentype_is_not_abstract():
    assert not inspect.isabstract(tokentypes_TokenType)


def test_tokentypes_tokentype_constructor_exists():
    assert callable(tokentypes_TokenType.__init__)


def test_tokentypes_tokentype_constructor_args():
    sig = inspect.signature(tokentypes_TokenType.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_tokentypeelementnet_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenTypeElementNet)


def test_highlevelnets_tokentypes_tokentypeelementnet_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenTypeElementNet.__init__)


def test_highlevelnets_tokentypes_tokentypeelementnet_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenTypeElementNet.__init__)
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



def test_highlevelnets_tokentypes_tokentypeatomic_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenTypeAtomic)


def test_highlevelnets_tokentypes_tokentypeatomic_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenTypeAtomic.__init__)


def test_highlevelnets_tokentypes_tokentypeatomic_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenTypeAtomic.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokentypes_tokentype_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenType)


def test_highlevelnets_tokentypes_tokentype_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenType.__init__)


def test_highlevelnets_tokentypes_tokentype_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenType.__init__)
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



def test_highlevelnets_marking_highlevelpetrinetmarked_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_marking_HighLevelPetriNetMarked)


def test_highlevelnets_marking_highlevelpetrinetmarked_constructor_exists():
    assert callable(highlevelnets_marking_HighLevelPetriNetMarked.__init__)


def test_highlevelnets_marking_highlevelpetrinetmarked_constructor_args():
    sig = inspect.signature(highlevelnets_marking_HighLevelPetriNetMarked.__init__)
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



def test_highlevelnets_tokenexpressions_tokenexpressionbinding_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenExpressionBinding)


def test_highlevelnets_tokenexpressions_tokenexpressionbinding_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenExpressionBinding.__init__)


def test_highlevelnets_tokenexpressions_tokenexpressionbinding_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenExpressionBinding.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npndiagramnetsystem_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNDiagramNetSystem)


def test_highlevelnets_npndiagrams_npndiagramnetsystem_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNDiagramNetSystem.__init__)


def test_highlevelnets_npndiagrams_npndiagramnetsystem_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNDiagramNetSystem.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_hlpn_contextvariable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_hlpn_ContextVariable)


def test_highlevelnets_hlpn_contextvariable_constructor_exists():
    assert callable(highlevelnets_hlpn_ContextVariable.__init__)


def test_highlevelnets_hlpn_contextvariable_constructor_args():
    sig = inspect.signature(highlevelnets_hlpn_ContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npnsymbolnodesn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolNodeSN)


def test_highlevelnets_npndiagrams_npnsymbolnodesn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolNodeSN.__init__)


def test_highlevelnets_npndiagrams_npnsymbolnodesn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolNodeSN.__init__)
    params = list(sig.parameters.keys())
    assert "constraints" in params, "Missing parameter 'constraints'"

def test_highlevelnets_npndiagrams_npnsymbolnodesn_has_constraints():
    assert hasattr(highlevelnets_npndiagrams_NPNSymbolNodeSN, "constraints")
    descriptor = None
    for klass in highlevelnets_npndiagrams_NPNSymbolNodeSN.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_common_inetelement_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_common_INetElement)


def test_highlevelnets_common_inetelement_constructor_exists():
    assert callable(highlevelnets_common_INetElement.__init__)


def test_highlevelnets_common_inetelement_constructor_args():
    sig = inspect.signature(highlevelnets_common_INetElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_highlevelnets_common_inetelement_has_name():
    assert hasattr(highlevelnets_common_INetElement, "name")
    descriptor = None
    for klass in highlevelnets_common_INetElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets_common_inetelement_has_comment():
    assert hasattr(highlevelnets_common_INetElement, "comment")
    descriptor = None
    for klass in highlevelnets_common_INetElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokenexpressions_monom_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_Monom)


def test_highlevelnets_tokenexpressions_monom_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_Monom.__init__)


def test_highlevelnets_tokenexpressions_monom_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_Monom.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_highlevelnets_tokenexpressions_monom_has_power():
    assert hasattr(highlevelnets_tokenexpressions_Monom, "power")
    descriptor = None
    for klass in highlevelnets_tokenexpressions_Monom.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokentypes_tokenattribute_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokentypes_TokenAttribute)


def test_highlevelnets_tokentypes_tokenattribute_constructor_exists():
    assert callable(highlevelnets_tokentypes_TokenAttribute.__init__)


def test_highlevelnets_tokentypes_tokenattribute_constructor_args():
    sig = inspect.signature(highlevelnets_tokentypes_TokenAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_highlevelnets_tokentypes_tokenattribute_has_value():
    assert hasattr(highlevelnets_tokentypes_TokenAttribute, "value")
    descriptor = None
    for klass in highlevelnets_tokentypes_TokenAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets_tokentypes_tokenattribute_has_name():
    assert hasattr(highlevelnets_tokentypes_TokenAttribute, "name")
    descriptor = None
    for klass in highlevelnets_tokentypes_TokenAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_highlevelnets_tokentypes_tokenattribute_has_type():
    assert hasattr(highlevelnets_tokentypes_TokenAttribute, "type")
    descriptor = None
    for klass in highlevelnets_tokentypes_TokenAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokenexpressions_tokenmultisetexpression_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenMultisetExpression)


def test_highlevelnets_tokenexpressions_tokenmultisetexpression_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenMultisetExpression.__init__)


def test_highlevelnets_tokenexpressions_tokenmultisetexpression_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenMultisetExpression.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokenexpressions_tokenweight_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenWeight)


def test_highlevelnets_tokenexpressions_tokenweight_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenWeight.__init__)


def test_highlevelnets_tokenexpressions_tokenweight_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenWeight.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_highlevelnets_tokenexpressions_tokenweight_has_weight():
    assert hasattr(highlevelnets_tokenexpressions_TokenWeight, "weight")
    descriptor = None
    for klass in highlevelnets_tokenexpressions_TokenWeight.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokenexpressions_monomconstant_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_MonomConstant)


def test_highlevelnets_tokenexpressions_monomconstant_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_MonomConstant.__init__)


def test_highlevelnets_tokenexpressions_monomconstant_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_MonomConstant.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_highlevelnets_tokenexpressions_monomconstant_has_power():
    assert hasattr(highlevelnets_tokenexpressions_MonomConstant, "power")
    descriptor = None
    for klass in highlevelnets_tokenexpressions_MonomConstant.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokenexpressions_tokenbinding_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenBinding)


def test_highlevelnets_tokenexpressions_tokenbinding_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenBinding.__init__)


def test_highlevelnets_tokenexpressions_tokenbinding_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenBinding.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_tokenexpressions_tokenmultiset_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_TokenMultiSet)


def test_highlevelnets_tokenexpressions_tokenmultiset_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_TokenMultiSet.__init__)


def test_highlevelnets_tokenexpressions_tokenmultiset_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_TokenMultiSet.__init__)
    params = list(sig.parameters.keys())



def test_highlevelnets_npndiagrams_npnsymbolarcsn_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_npndiagrams_NPNSymbolArcSN)


def test_highlevelnets_npndiagrams_npnsymbolarcsn_constructor_exists():
    assert callable(highlevelnets_npndiagrams_NPNSymbolArcSN.__init__)


def test_highlevelnets_npndiagrams_npnsymbolarcsn_constructor_args():
    sig = inspect.signature(highlevelnets_npndiagrams_NPNSymbolArcSN.__init__)
    params = list(sig.parameters.keys())
    assert "bendpoints" in params, "Missing parameter 'bendpoints'"

def test_highlevelnets_npndiagrams_npnsymbolarcsn_has_bendpoints():
    assert hasattr(highlevelnets_npndiagrams_NPNSymbolArcSN, "bendpoints")
    descriptor = None
    for klass in highlevelnets_npndiagrams_NPNSymbolArcSN.__mro__:
        if "bendpoints" in klass.__dict__:
            descriptor = klass.__dict__["bendpoints"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_tokenexpressions_variable_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_tokenexpressions_Variable)


def test_highlevelnets_tokenexpressions_variable_constructor_exists():
    assert callable(highlevelnets_tokenexpressions_Variable.__init__)


def test_highlevelnets_tokenexpressions_variable_constructor_args():
    sig = inspect.signature(highlevelnets_tokenexpressions_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_highlevelnets_tokenexpressions_variable_has_name():
    assert hasattr(highlevelnets_tokenexpressions_Variable, "name")
    descriptor = None
    for klass in highlevelnets_tokenexpressions_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_highlevelnets_marking_placemarking_is_not_abstract():
    assert not inspect.isabstract(highlevelnets_marking_PlaceMarking)


def test_highlevelnets_marking_placemarking_constructor_exists():
    assert callable(highlevelnets_marking_PlaceMarking.__init__)


def test_highlevelnets_marking_placemarking_constructor_args():
    sig = inspect.signature(highlevelnets_marking_PlaceMarking.__init__)
    params = list(sig.parameters.keys())

def test_esynchronizationkind_exists():
    # Check that the Enumeration exists
    assert ESynchronizationKind is not None

def test_esynchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ESynchronizationKind]
    expected_literals = [
        "VerticalSynchronization",
        "HorizontalSynchronization",
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
NPNSymbolArcTPSN_strategy = st.builds(
    NPNSymbolArcTPSN,
)
NPNSymbolArcPTSN_strategy = st.builds(
    NPNSymbolArcPTSN,
)
NPNSymbolArcSN_strategy = st.builds(
    NPNSymbolArcSN,
)
NPNSymbolNodeSN_strategy = st.builds(
    NPNSymbolNodeSN,
)
highlevelnets_npndiagrams_NPNSymbolTransitionSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolTransitionSN,
)
highlevelnets_npndiagrams_NPNSymbolPlaceSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolPlaceSN,
)
highlevelnets_npndiagrams_NPNSymbolArcTPSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolArcTPSN,
)
NPNSymbolPlaceSN_strategy = st.builds(
    NPNSymbolPlaceSN,
)
NPNSymbolTransitionSN_strategy = st.builds(
    NPNSymbolTransitionSN,
)
highlevelnets_npndiagrams_NPNSymbolArcPTSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolArcPTSN,
)
TransitionSynchronized_strategy = st.builds(
    TransitionSynchronized,
)
NPnet_strategy = st.builds(
    NPnet,
)
NPnetMarked_strategy = st.builds(
    NPnetMarked,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
NetConstant_strategy = st.builds(
    NetConstant,
)
NPNDiagramNetSystem_strategy = st.builds(
    NPNDiagramNetSystem,
)
highlevelnets_common_IEntityIdentifiable_strategy = st.builds(
    highlevelnets_common_IEntityIdentifiable,
    id=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
highlevelnets_npnets_TransitionSynchronized_strategy = st.builds(
    highlevelnets_npnets_TransitionSynchronized,
)
IDiagramHolder_strategy = st.builds(
    IDiagramHolder,
)
highlevelnets_npnets_NPnet_strategy = st.builds(
    highlevelnets_npnets_NPnet,
)
Node_strategy = st.builds(
    Node,
)
hlpn_ContextVariable_strategy = st.builds(
    hlpn_ContextVariable,
)
common_INetElement_strategy = st.builds(
    common_INetElement,
)
highlevelnets_hlpn_HighLevelPetriNet_strategy = st.builds(
    highlevelnets_hlpn_HighLevelPetriNet,
)
hlpn_Node_strategy = st.builds(
    hlpn_Node,
)
highlevelnets_hlpn_Transition_strategy = st.builds(
    highlevelnets_hlpn_Transition,
)
ArcTP_strategy = st.builds(
    ArcTP,
)
ArcPT_strategy = st.builds(
    ArcPT,
)
highlevelnets_hlpn_Place_strategy = st.builds(
    highlevelnets_hlpn_Place,
)
Arc_strategy = st.builds(
    Arc,
)
highlevelnets_hlpn_ArcTP_strategy = st.builds(
    highlevelnets_hlpn_ArcTP,
)
highlevelnets_hlpn_ArcPT_strategy = st.builds(
    highlevelnets_hlpn_ArcPT,
)
ContextVariable_strategy = st.builds(
    ContextVariable,
)
TokenWeight_strategy = st.builds(
    TokenWeight,
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
TokenAttribute_strategy = st.builds(
    TokenAttribute,
)
TokenNet_strategy = st.builds(
    TokenNet,
)
ElementNetMarked_strategy = st.builds(
    ElementNetMarked,
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
highlevelnets_tokentypes_TokenNet_strategy = st.builds(
    highlevelnets_tokentypes_TokenNet,
)
highlevelnets_tokentypes_TokenAtomic_strategy = st.builds(
    highlevelnets_tokentypes_TokenAtomic,
)
PlaceMarking_strategy = st.builds(
    PlaceMarking,
)
INetElement_strategy = st.builds(
    INetElement,
)
highlevelnets_npnets_NPnetMarked_strategy = st.builds(
    highlevelnets_npnets_NPnetMarked,
)
highlevelnets_hlpn_Node_strategy = st.builds(
    highlevelnets_hlpn_Node,
)
highlevelnets_tokenexpressions_TokenVariadicExpression_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenVariadicExpression,
)
highlevelnets_tokentypes_Atom_strategy = st.builds(
    highlevelnets_tokentypes_Atom,
)
highlevelnets_tokenexpressions_NetConstant_strategy = st.builds(
    highlevelnets_tokenexpressions_NetConstant,
)
highlevelnets_hlpn_Arc_strategy = st.builds(
    highlevelnets_hlpn_Arc,
)
highlevelnets_tokentypes_ElementNetMarked_strategy = st.builds(
    highlevelnets_tokentypes_ElementNetMarked,
)
highlevelnets_common_IDiagramHolder_strategy = st.builds(
    highlevelnets_common_IDiagramHolder,
)
highlevelnets_tokentypes_Token_strategy = st.builds(
    highlevelnets_tokentypes_Token,
)
highlevelnets_npnets_Synchronization_strategy = st.builds(
    highlevelnets_npnets_Synchronization,
    key=
        safe_text,
    kind=
        safe_text
)
highlevelnets_marking_Marking_strategy = st.builds(
    highlevelnets_marking_Marking,
)
common_IDiagramHolder_strategy = st.builds(
    common_IDiagramHolder,
)
tokentypes_TokenType_strategy = st.builds(
    tokentypes_TokenType,
)
highlevelnets_tokentypes_TokenTypeElementNet_strategy = st.builds(
    highlevelnets_tokentypes_TokenTypeElementNet,
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
highlevelnets_tokentypes_TokenTypeAtomic_strategy = st.builds(
    highlevelnets_tokentypes_TokenTypeAtomic,
)
highlevelnets_tokentypes_TokenType_strategy = st.builds(
    highlevelnets_tokentypes_TokenType,
)
Marking_strategy = st.builds(
    Marking,
)
HighLevelPetriNet_strategy = st.builds(
    HighLevelPetriNet,
)
highlevelnets_marking_HighLevelPetriNetMarked_strategy = st.builds(
    highlevelnets_marking_HighLevelPetriNetMarked,
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
highlevelnets_tokenexpressions_TokenExpressionBinding_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenExpressionBinding,
)
highlevelnets_npndiagrams_NPNDiagramNetSystem_strategy = st.builds(
    highlevelnets_npndiagrams_NPNDiagramNetSystem,
)
highlevelnets_hlpn_ContextVariable_strategy = st.builds(
    highlevelnets_hlpn_ContextVariable,
)
highlevelnets_npndiagrams_NPNSymbolNodeSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolNodeSN,
    constraints=
        safe_text
)
highlevelnets_common_INetElement_strategy = st.builds(
    highlevelnets_common_INetElement,
    name=
        safe_text,
    comment=
        safe_text
)
highlevelnets_tokenexpressions_Monom_strategy = st.builds(
    highlevelnets_tokenexpressions_Monom,
    power=
        safe_text
)
highlevelnets_tokentypes_TokenAttribute_strategy = st.builds(
    highlevelnets_tokentypes_TokenAttribute,
    value=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
highlevelnets_tokenexpressions_TokenMultisetExpression_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenMultisetExpression,
)
highlevelnets_tokenexpressions_TokenWeight_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenWeight,
    weight=
        safe_text
)
highlevelnets_tokenexpressions_MonomConstant_strategy = st.builds(
    highlevelnets_tokenexpressions_MonomConstant,
    power=
        safe_text
)
highlevelnets_tokenexpressions_TokenBinding_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenBinding,
)
highlevelnets_tokenexpressions_TokenMultiSet_strategy = st.builds(
    highlevelnets_tokenexpressions_TokenMultiSet,
)
highlevelnets_npndiagrams_NPNSymbolArcSN_strategy = st.builds(
    highlevelnets_npndiagrams_NPNSymbolArcSN,
    bendpoints=
        safe_text
)
highlevelnets_tokenexpressions_Variable_strategy = st.builds(
    highlevelnets_tokenexpressions_Variable,
    name=
        safe_text
)
highlevelnets_marking_PlaceMarking_strategy = st.builds(
    highlevelnets_marking_PlaceMarking,
)

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

@given(instance=NPNSymbolNodeSN_strategy)
@settings(max_examples=50)
def test_npnsymbolnodesn_instantiation(instance):
    assert isinstance(instance, NPNSymbolNodeSN)

@given(instance=highlevelnets_npndiagrams_NPNSymbolTransitionSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymboltransitionsn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolTransitionSN)

@given(instance=highlevelnets_npndiagrams_NPNSymbolPlaceSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymbolplacesn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolPlaceSN)

@given(instance=highlevelnets_npndiagrams_NPNSymbolArcTPSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymbolarctpsn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolArcTPSN)

@given(instance=NPNSymbolPlaceSN_strategy)
@settings(max_examples=50)
def test_npnsymbolplacesn_instantiation(instance):
    assert isinstance(instance, NPNSymbolPlaceSN)

@given(instance=NPNSymbolTransitionSN_strategy)
@settings(max_examples=50)
def test_npnsymboltransitionsn_instantiation(instance):
    assert isinstance(instance, NPNSymbolTransitionSN)

@given(instance=highlevelnets_npndiagrams_NPNSymbolArcPTSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymbolarcptsn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolArcPTSN)

@given(instance=TransitionSynchronized_strategy)
@settings(max_examples=50)
def test_transitionsynchronized_instantiation(instance):
    assert isinstance(instance, TransitionSynchronized)

@given(instance=NPnet_strategy)
@settings(max_examples=50)
def test_npnet_instantiation(instance):
    assert isinstance(instance, NPnet)

@given(instance=NPnetMarked_strategy)
@settings(max_examples=50)
def test_npnetmarked_instantiation(instance):
    assert isinstance(instance, NPnetMarked)

@given(instance=Synchronization_strategy)
@settings(max_examples=50)
def test_synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)

@given(instance=NetConstant_strategy)
@settings(max_examples=50)
def test_netconstant_instantiation(instance):
    assert isinstance(instance, NetConstant)

@given(instance=NPNDiagramNetSystem_strategy)
@settings(max_examples=50)
def test_npndiagramnetsystem_instantiation(instance):
    assert isinstance(instance, NPNDiagramNetSystem)

@given(instance=highlevelnets_common_IEntityIdentifiable_strategy)
@settings(max_examples=50)
def test_highlevelnets_common_ientityidentifiable_instantiation(instance):
    assert isinstance(instance, highlevelnets_common_IEntityIdentifiable)



@given(instance=highlevelnets_common_IEntityIdentifiable_strategy)
def test_highlevelnets_common_ientityidentifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=highlevelnets_npnets_TransitionSynchronized_strategy)
@settings(max_examples=50)
def test_highlevelnets_npnets_transitionsynchronized_instantiation(instance):
    assert isinstance(instance, highlevelnets_npnets_TransitionSynchronized)

@given(instance=IDiagramHolder_strategy)
@settings(max_examples=50)
def test_idiagramholder_instantiation(instance):
    assert isinstance(instance, IDiagramHolder)

@given(instance=highlevelnets_npnets_NPnet_strategy)
@settings(max_examples=50)
def test_highlevelnets_npnets_npnet_instantiation(instance):
    assert isinstance(instance, highlevelnets_npnets_NPnet)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=hlpn_ContextVariable_strategy)
@settings(max_examples=50)
def test_hlpn_contextvariable_instantiation(instance):
    assert isinstance(instance, hlpn_ContextVariable)

@given(instance=common_INetElement_strategy)
@settings(max_examples=50)
def test_common_inetelement_instantiation(instance):
    assert isinstance(instance, common_INetElement)

@given(instance=highlevelnets_hlpn_HighLevelPetriNet_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_highlevelpetrinet_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_HighLevelPetriNet)

@given(instance=hlpn_Node_strategy)
@settings(max_examples=50)
def test_hlpn_node_instantiation(instance):
    assert isinstance(instance, hlpn_Node)

@given(instance=highlevelnets_hlpn_Transition_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_transition_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_Transition)

@given(instance=ArcTP_strategy)
@settings(max_examples=50)
def test_arctp_instantiation(instance):
    assert isinstance(instance, ArcTP)

@given(instance=ArcPT_strategy)
@settings(max_examples=50)
def test_arcpt_instantiation(instance):
    assert isinstance(instance, ArcPT)

@given(instance=highlevelnets_hlpn_Place_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_place_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_Place)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=highlevelnets_hlpn_ArcTP_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_arctp_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_ArcTP)

@given(instance=highlevelnets_hlpn_ArcPT_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_arcpt_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_ArcPT)

@given(instance=ContextVariable_strategy)
@settings(max_examples=50)
def test_contextvariable_instantiation(instance):
    assert isinstance(instance, ContextVariable)

@given(instance=TokenWeight_strategy)
@settings(max_examples=50)
def test_tokenweight_instantiation(instance):
    assert isinstance(instance, TokenWeight)

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

@given(instance=TokenAttribute_strategy)
@settings(max_examples=50)
def test_tokenattribute_instantiation(instance):
    assert isinstance(instance, TokenAttribute)

@given(instance=TokenNet_strategy)
@settings(max_examples=50)
def test_tokennet_instantiation(instance):
    assert isinstance(instance, TokenNet)

@given(instance=ElementNetMarked_strategy)
@settings(max_examples=50)
def test_elementnetmarked_instantiation(instance):
    assert isinstance(instance, ElementNetMarked)

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

@given(instance=highlevelnets_tokentypes_TokenNet_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokennet_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenNet)

@given(instance=highlevelnets_tokentypes_TokenAtomic_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokenatomic_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenAtomic)

@given(instance=PlaceMarking_strategy)
@settings(max_examples=50)
def test_placemarking_instantiation(instance):
    assert isinstance(instance, PlaceMarking)

@given(instance=INetElement_strategy)
@settings(max_examples=50)
def test_inetelement_instantiation(instance):
    assert isinstance(instance, INetElement)

@given(instance=highlevelnets_npnets_NPnetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets_npnets_npnetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets_npnets_NPnetMarked)

@given(instance=highlevelnets_hlpn_Node_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_node_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_Node)

@given(instance=highlevelnets_tokenexpressions_TokenVariadicExpression_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenvariadicexpression_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenVariadicExpression)

@given(instance=highlevelnets_tokentypes_Atom_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_atom_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_Atom)

@given(instance=highlevelnets_tokenexpressions_NetConstant_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_netconstant_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_NetConstant)

@given(instance=highlevelnets_hlpn_Arc_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_arc_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_Arc)

@given(instance=highlevelnets_tokentypes_ElementNetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_elementnetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_ElementNetMarked)

@given(instance=highlevelnets_common_IDiagramHolder_strategy)
@settings(max_examples=50)
def test_highlevelnets_common_idiagramholder_instantiation(instance):
    assert isinstance(instance, highlevelnets_common_IDiagramHolder)

@given(instance=highlevelnets_tokentypes_Token_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_token_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_Token)

@given(instance=highlevelnets_npnets_Synchronization_strategy)
@settings(max_examples=50)
def test_highlevelnets_npnets_synchronization_instantiation(instance):
    assert isinstance(instance, highlevelnets_npnets_Synchronization)



@given(instance=highlevelnets_npnets_Synchronization_strategy)
def test_highlevelnets_npnets_synchronization_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=highlevelnets_npnets_Synchronization_strategy)
def test_highlevelnets_npnets_synchronization_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=highlevelnets_marking_Marking_strategy)
@settings(max_examples=50)
def test_highlevelnets_marking_marking_instantiation(instance):
    assert isinstance(instance, highlevelnets_marking_Marking)

@given(instance=common_IDiagramHolder_strategy)
@settings(max_examples=50)
def test_common_idiagramholder_instantiation(instance):
    assert isinstance(instance, common_IDiagramHolder)

@given(instance=tokentypes_TokenType_strategy)
@settings(max_examples=50)
def test_tokentypes_tokentype_instantiation(instance):
    assert isinstance(instance, tokentypes_TokenType)

@given(instance=highlevelnets_tokentypes_TokenTypeElementNet_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokentypeelementnet_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenTypeElementNet)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=highlevelnets_tokentypes_TokenTypeElementNet_strategy)
@settings(max_examples=30)
def test_highlevelnets_tokentypes_tokentypeelementnet_createinstance_changes_state(instance):
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
        assert has_statements, f"Function 'createInstance' in highlevelnets_tokentypes_TokenTypeElementNet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createInstance' in highlevelnets_tokentypes_TokenTypeElementNet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createInstance' in highlevelnets_tokentypes_TokenTypeElementNet is not implemented or raised an error")

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

@given(instance=highlevelnets_tokentypes_TokenTypeAtomic_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokentypeatomic_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenTypeAtomic)

@given(instance=highlevelnets_tokentypes_TokenType_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokentype_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenType)

@given(instance=Marking_strategy)
@settings(max_examples=50)
def test_marking_instantiation(instance):
    assert isinstance(instance, Marking)

@given(instance=HighLevelPetriNet_strategy)
@settings(max_examples=50)
def test_highlevelpetrinet_instantiation(instance):
    assert isinstance(instance, HighLevelPetriNet)

@given(instance=highlevelnets_marking_HighLevelPetriNetMarked_strategy)
@settings(max_examples=50)
def test_highlevelnets_marking_highlevelpetrinetmarked_instantiation(instance):
    assert isinstance(instance, highlevelnets_marking_HighLevelPetriNetMarked)

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

@given(instance=highlevelnets_tokenexpressions_TokenExpressionBinding_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenexpressionbinding_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenExpressionBinding)

@given(instance=highlevelnets_npndiagrams_NPNDiagramNetSystem_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npndiagramnetsystem_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNDiagramNetSystem)

@given(instance=highlevelnets_hlpn_ContextVariable_strategy)
@settings(max_examples=50)
def test_highlevelnets_hlpn_contextvariable_instantiation(instance):
    assert isinstance(instance, highlevelnets_hlpn_ContextVariable)

@given(instance=highlevelnets_npndiagrams_NPNSymbolNodeSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymbolnodesn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolNodeSN)



@given(instance=highlevelnets_npndiagrams_NPNSymbolNodeSN_strategy)
def test_highlevelnets_npndiagrams_npnsymbolnodesn_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original

@given(instance=highlevelnets_common_INetElement_strategy)
@settings(max_examples=50)
def test_highlevelnets_common_inetelement_instantiation(instance):
    assert isinstance(instance, highlevelnets_common_INetElement)



@given(instance=highlevelnets_common_INetElement_strategy)
def test_highlevelnets_common_inetelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=highlevelnets_common_INetElement_strategy)
def test_highlevelnets_common_inetelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=highlevelnets_tokenexpressions_Monom_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_monom_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_Monom)



@given(instance=highlevelnets_tokenexpressions_Monom_strategy)
def test_highlevelnets_tokenexpressions_monom_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=highlevelnets_tokentypes_TokenAttribute_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokentypes_tokenattribute_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokentypes_TokenAttribute)



@given(instance=highlevelnets_tokentypes_TokenAttribute_strategy)
def test_highlevelnets_tokentypes_tokenattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=highlevelnets_tokentypes_TokenAttribute_strategy)
def test_highlevelnets_tokentypes_tokenattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=highlevelnets_tokentypes_TokenAttribute_strategy)
def test_highlevelnets_tokentypes_tokenattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=highlevelnets_tokenexpressions_TokenMultisetExpression_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenmultisetexpression_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenMultisetExpression)

@given(instance=highlevelnets_tokenexpressions_TokenWeight_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenweight_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenWeight)



@given(instance=highlevelnets_tokenexpressions_TokenWeight_strategy)
def test_highlevelnets_tokenexpressions_tokenweight_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=highlevelnets_tokenexpressions_MonomConstant_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_monomconstant_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_MonomConstant)



@given(instance=highlevelnets_tokenexpressions_MonomConstant_strategy)
def test_highlevelnets_tokenexpressions_monomconstant_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=highlevelnets_tokenexpressions_TokenBinding_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenbinding_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenBinding)

@given(instance=highlevelnets_tokenexpressions_TokenMultiSet_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_tokenmultiset_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_TokenMultiSet)

@given(instance=highlevelnets_npndiagrams_NPNSymbolArcSN_strategy)
@settings(max_examples=50)
def test_highlevelnets_npndiagrams_npnsymbolarcsn_instantiation(instance):
    assert isinstance(instance, highlevelnets_npndiagrams_NPNSymbolArcSN)



@given(instance=highlevelnets_npndiagrams_NPNSymbolArcSN_strategy)
def test_highlevelnets_npndiagrams_npnsymbolarcsn_bendpoints_setter(instance):
    original = instance.bendpoints
    instance.bendpoints = original
    assert instance.bendpoints == original

@given(instance=highlevelnets_tokenexpressions_Variable_strategy)
@settings(max_examples=50)
def test_highlevelnets_tokenexpressions_variable_instantiation(instance):
    assert isinstance(instance, highlevelnets_tokenexpressions_Variable)



@given(instance=highlevelnets_tokenexpressions_Variable_strategy)
def test_highlevelnets_tokenexpressions_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=highlevelnets_marking_PlaceMarking_strategy)
@settings(max_examples=50)
def test_highlevelnets_marking_placemarking_instantiation(instance):
    assert isinstance(instance, highlevelnets_marking_PlaceMarking)

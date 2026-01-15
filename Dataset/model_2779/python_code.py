from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ZChild:

    pass
class top_IntegerLiteral(ZChild):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class XChild:

    pass
class top_Y(XChild):

    pass
class WChild:

    pass
class top_XChild(WChild):

    pass
class top_X(WChild):

    pass
class VChild:

    pass
class top_WChild(VChild):

    pass
class top_W(VChild):

    pass
class YChild:

    pass
class top_ZChild(YChild):

    pass
class top_Z(YChild):

    pass
class top_YChild(XChild):

    pass
class SChild:

    pass
class top_TChild(SChild):

    pass
class top_T(SChild):

    pass
class RChild:

    pass
class top_SChild(RChild):

    pass
class top_S(RChild):

    pass
class QChild:

    pass
class top_RChild(QChild):

    pass
class top_R(QChild):

    pass
class UChild:

    pass
class top_VChild(UChild):

    pass
class top_V(UChild):

    pass
class TChild:

    pass
class top_UChild(TChild):

    pass
class top_U(TChild):

    pass
class OChild:

    pass
class top_P(OChild):

    pass
class NChild:

    pass
class top_OChild(NChild):

    pass
class top_O(NChild):

    pass
class MChild:

    pass
class top_NChild(MChild):

    pass
class top_N(MChild):

    pass
class PChild:

    pass
class top_QChild(PChild):

    pass
class top_Q(PChild):

    pass
class top_PChild(OChild):

    pass
class JChild:

    pass
class top_KChild(JChild):

    pass
class top_K(JChild):

    pass
class IChild:

    pass
class top_JChild(IChild):

    pass
class top_J(IChild):

    pass
class HChild:

    pass
class top_IChild(HChild):

    pass
class top_I(HChild):

    pass
class LChild:

    pass
class top_MChild(LChild):

    pass
class top_M(LChild):

    pass
class KChild:

    pass
class top_LChild(KChild):

    pass
class top_L(KChild):

    pass
class FChild:

    pass
class top_G(FChild):

    pass
class EChild:

    pass
class top_FChild(EChild):

    pass
class top_F(EChild):

    pass
class DChild:

    pass
class top_EChild(DChild):

    pass
class top_E(DChild):

    pass
class GChild:

    pass
class top_HChild(GChild):

    pass
class top_H(GChild):

    pass
class top_GChild(FChild):

    pass
class AChild:

    pass
class top_BChild(AChild):

    pass
class top_B(AChild):

    pass
class ExprChild:

    pass
class top_AChild(ExprChild):

    pass
class top_A(ExprChild):

    pass
class top_ExprChild(ABC):

    pass
class top_Expr:

    pass
class CChild:

    pass
class top_DChild(CChild):

    pass
class top_D(CChild):

    pass
class BChild:

    pass
class top_CChild(BChild):

    pass
class top_C(BChild):

    pass
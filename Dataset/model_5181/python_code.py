from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ProtoLink:

    pass
class Component:

    pass
class testgramgen1_CNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class testgramgen1_ProtoLink(Component):

    pass
class CNamedElement:

    pass
class testgramgen1_DerivedLink(CNamedElement, ProtoLink):

    pass
class Node:

    pass
class testgramgen1_D(Node):

    pass
class testgramgen1_C(CNamedElement, Node):

    pass
class testgramgen1_B(Node):

    pass
class testgramgen1_A(Node):

    pass
class testgramgen1_Node(ABC):

    pass
class testgramgen1_DerivedComponent(Component):

    pass
class testgramgen1_Component(CNamedElement):

    pass
class testgramgen1_System:

    pass
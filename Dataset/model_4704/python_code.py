from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OperatorDecl:

    pass
class SortDecl:

    pass
class Operator:

    pass
class terms_BuiltInOperator(Operator):

    pass
class terms_Tuple(Operator):

    pass
class terms_UserOperator(Operator):

    pass
class terms_MultisetOperator(Operator):

    pass
class terms_BuiltInConstant(Operator):

    pass
class TermsDeclaration:

    pass
class terms_SortDecl(TermsDeclaration):

    pass
class terms_OperatorDecl(TermsDeclaration):

    pass
class Term:

    pass
class terms_PartitionElement:

    pass
class terms_HLAnnotation:

    pass
class terms_Condition:

    pass
class terms_HLMarking:

    pass
class terms_NamedOperator(OperatorDecl):

    pass
class terms_Operator(Term):

    pass
class terms_Variable(Term):

    pass
class Sort:

    pass
class terms_UserSort(Sort):

    pass
class terms_BuiltInSort(Sort):

    pass
class terms_Partition:

    pass
class terms_Empty:

    pass
class terms_All:

    pass
class terms_Type:

    pass
class terms_ProductSort(Sort):

    pass
class terms_VariableDecl(TermsDeclaration):

    pass
class terms_NamedSort(SortDecl):

    pass
class terms_MultisetSort(Sort):

    pass
class terms_Sort(ABC):

    pass
class terms_Term(ABC):

    pass
class terms_Declaration:

    pass
class terms_TermsDeclaration(ABC):

    def __init__(self, id: str, name: str, TermsDeclaration: "terms_Declarations" = None, declaration: "terms_Declarations" = None):
        self.id = id
        self.name = name
        self.TermsDeclaration = TermsDeclaration
        self.declaration = declaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def TermsDeclaration(self):
        return self.__TermsDeclaration

    @TermsDeclaration.setter
    def TermsDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_terms_TermsDeclaration__TermsDeclaration", None)
        self.__TermsDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerDeclarations"):
                opp_val = getattr(old_value, "containerDeclarations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerDeclarations"):
                opp_val = getattr(value, "containerDeclarations", None)
                if opp_val is None:
                    setattr(value, "containerDeclarations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_terms_TermsDeclaration__declaration", None)
        self.__declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Declarations"):
                opp_val = getattr(old_value, "Declarations", None)
                if opp_val == self:
                    setattr(old_value, "Declarations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Declarations"):
                opp_val = getattr(value, "Declarations", None)
                setattr(value, "Declarations", self)

class terms_Declarations:

    pass
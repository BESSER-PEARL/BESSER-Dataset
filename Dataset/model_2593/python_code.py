from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class grammar_features_SecondRoot:

    pass
class grammar_features_X:

    def __init__(self, name: str, grammar_features_X3: "grammar_features_MandatoryContainment" = None, grammar_features_X: "grammar_features_OptionalContainment" = None, grammar_features_X9: "grammar_features_OptionalNonContainment" = None, grammar_features_X5: "grammar_features_PlusContainment" = None, grammar_features_X7: "grammar_features_StarContainment" = None, grammar_features_X15: "grammar_features_StarNonContainment" = None, grammar_features_X11: "grammar_features_MandatoryNonContainment" = None, grammar_features_X13: "grammar_features_PlusNonContainment" = None):
        self.name = name
        self.grammar_features_X3 = grammar_features_X3
        self.grammar_features_X = grammar_features_X
        self.grammar_features_X9 = grammar_features_X9
        self.grammar_features_X5 = grammar_features_X5
        self.grammar_features_X7 = grammar_features_X7
        self.grammar_features_X15 = grammar_features_X15
        self.grammar_features_X11 = grammar_features_X11
        self.grammar_features_X13 = grammar_features_X13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def grammar_features_X3(self):
        return self.__grammar_features_X3

    @grammar_features_X3.setter
    def grammar_features_X3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X3", None)
        self.__grammar_features_X3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_MandatoryContainment"):
                opp_val = getattr(old_value, "grammar_features_MandatoryContainment", None)
                if opp_val == self:
                    setattr(old_value, "grammar_features_MandatoryContainment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_MandatoryContainment"):
                opp_val = getattr(value, "grammar_features_MandatoryContainment", None)
                setattr(value, "grammar_features_MandatoryContainment", self)

    @property
    def grammar_features_X9(self):
        return self.__grammar_features_X9

    @grammar_features_X9.setter
    def grammar_features_X9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X9", None)
        self.__grammar_features_X9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_OptionalNonContainment"):
                opp_val = getattr(old_value, "grammar_features_OptionalNonContainment", None)
                if opp_val == self:
                    setattr(old_value, "grammar_features_OptionalNonContainment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_OptionalNonContainment"):
                opp_val = getattr(value, "grammar_features_OptionalNonContainment", None)
                setattr(value, "grammar_features_OptionalNonContainment", self)

    @property
    def grammar_features_X(self):
        return self.__grammar_features_X

    @grammar_features_X.setter
    def grammar_features_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X", None)
        self.__grammar_features_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_OptionalContainment"):
                opp_val = getattr(old_value, "grammar_features_OptionalContainment", None)
                if opp_val == self:
                    setattr(old_value, "grammar_features_OptionalContainment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_OptionalContainment"):
                opp_val = getattr(value, "grammar_features_OptionalContainment", None)
                setattr(value, "grammar_features_OptionalContainment", self)

    @property
    def grammar_features_X13(self):
        return self.__grammar_features_X13

    @grammar_features_X13.setter
    def grammar_features_X13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X13", None)
        self.__grammar_features_X13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_PlusNonContainment"):
                opp_val = getattr(old_value, "grammar_features_PlusNonContainment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_PlusNonContainment"):
                opp_val = getattr(value, "grammar_features_PlusNonContainment", None)
                if opp_val is None:
                    setattr(value, "grammar_features_PlusNonContainment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammar_features_X5(self):
        return self.__grammar_features_X5

    @grammar_features_X5.setter
    def grammar_features_X5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X5", None)
        self.__grammar_features_X5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_PlusContainment"):
                opp_val = getattr(old_value, "grammar_features_PlusContainment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_PlusContainment"):
                opp_val = getattr(value, "grammar_features_PlusContainment", None)
                if opp_val is None:
                    setattr(value, "grammar_features_PlusContainment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammar_features_X7(self):
        return self.__grammar_features_X7

    @grammar_features_X7.setter
    def grammar_features_X7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X7", None)
        self.__grammar_features_X7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_StarContainment"):
                opp_val = getattr(old_value, "grammar_features_StarContainment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_StarContainment"):
                opp_val = getattr(value, "grammar_features_StarContainment", None)
                if opp_val is None:
                    setattr(value, "grammar_features_StarContainment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammar_features_X15(self):
        return self.__grammar_features_X15

    @grammar_features_X15.setter
    def grammar_features_X15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X15", None)
        self.__grammar_features_X15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_StarNonContainment"):
                opp_val = getattr(old_value, "grammar_features_StarNonContainment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_StarNonContainment"):
                opp_val = getattr(value, "grammar_features_StarNonContainment", None)
                if opp_val is None:
                    setattr(value, "grammar_features_StarNonContainment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammar_features_X11(self):
        return self.__grammar_features_X11

    @grammar_features_X11.setter
    def grammar_features_X11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_features_X__grammar_features_X11", None)
        self.__grammar_features_X11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_features_MandatoryNonContainment"):
                opp_val = getattr(old_value, "grammar_features_MandatoryNonContainment", None)
                if opp_val == self:
                    setattr(old_value, "grammar_features_MandatoryNonContainment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_features_MandatoryNonContainment"):
                opp_val = getattr(value, "grammar_features_MandatoryNonContainment", None)
                setattr(value, "grammar_features_MandatoryNonContainment", self)

class Child:

    pass
class grammar_features_OptionalPrefix(Child):

    pass
class grammar_features_OptionalNonContainment(Child):

    pass
class grammar_features_PlusContainment(Child):

    pass
class grammar_features_StarNonContainment(Child):

    pass
class grammar_features_CompoundStar(Child):

    pass
class grammar_features_CompoundPlus(Child):

    pass
class grammar_features_PlusNonContainment(Child):

    pass
class grammar_features_OptionalContainment(Child):

    pass
class grammar_features_PlusPrefix(Child):

    pass
class grammar_features_ClassWithAttributes(Child):

    def __init__(self, a1: str, a2: bool):
        self.a1 = a1
        self.a2 = a2
        
    @property
    def a1(self) -> str:
        return self.__a1

    @a1.setter
    def a1(self, a1: str):
        self.__a1 = a1

    @property
    def a2(self) -> bool:
        return self.__a2

    @a2.setter
    def a2(self, a2: bool):
        self.__a2 = a2

class grammar_features_CompoundOptional(Child):

    pass
class grammar_features_StarContainment(Child):

    pass
class grammar_features_MandatoryContainment(Child):

    pass
class grammar_features_StarPrefix(Child):

    pass
class grammar_features_MandatoryNonContainment(Child):

    pass
class grammar_features_AlternativeSyntax(Child):

    pass
class grammar_features_Child(ABC):

    pass
class grammar_features_Root:

    pass
class AbstractSuperclass:

    pass
class grammar_features_ConcreteSubclassB(AbstractSuperclass):

    pass
class grammar_features_ConcreteSubclassA(AbstractSuperclass):

    pass
class grammar_features_AbstractSuperclass(Child):

    pass
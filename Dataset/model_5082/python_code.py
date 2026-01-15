from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractComponent:

    pass
class testall_Component(AbstractComponent):

    pass
class Interface:

    pass
class testall_Binding:

    pass
class testall_Interface(ABC):

    def __init__(self, name: str, signature: str, testall_Interface8: "testall_Binding" = None, testall_Interface: set["testall_Binding"] = None, testall_Interface11: "testall_Binding" = None):
        self.name = name
        self.signature = signature
        self.testall_Interface8 = testall_Interface8
        self.testall_Interface = testall_Interface if testall_Interface is not None else set()
        self.testall_Interface11 = testall_Interface11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def testall_Interface(self):
        return self.__testall_Interface

    @testall_Interface.setter
    def testall_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_Interface__testall_Interface", None)
        self.__testall_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testall_Binding"):
                    opp_val = getattr(item, "testall_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "testall_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testall_Binding"):
                    opp_val = getattr(item, "testall_Binding", None)
                    
                    setattr(item, "testall_Binding", self)
                    

    @property
    def testall_Interface8(self):
        return self.__testall_Interface8

    @testall_Interface8.setter
    def testall_Interface8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_Interface__testall_Interface8", None)
        self.__testall_Interface8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_Binding7"):
                opp_val = getattr(old_value, "testall_Binding7", None)
                if opp_val == self:
                    setattr(old_value, "testall_Binding7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_Binding7"):
                opp_val = getattr(value, "testall_Binding7", None)
                setattr(value, "testall_Binding7", self)

    @property
    def testall_Interface11(self):
        return self.__testall_Interface11

    @testall_Interface11.setter
    def testall_Interface11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_Interface__testall_Interface11", None)
        self.__testall_Interface11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_Binding10"):
                opp_val = getattr(old_value, "testall_Binding10", None)
                if opp_val == self:
                    setattr(old_value, "testall_Binding10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_Binding10"):
                opp_val = getattr(value, "testall_Binding10", None)
                setattr(value, "testall_Binding10", self)

class testall_Provided(Interface):

    pass
class testall_Required(Interface):

    pass
class testall_Content:

    def __init__(self, expression: str, language: str, testall_Content: "testall_AbstractComponent" = None, testall_Content13: "testall_AbstractComponent" = None):
        self.expression = expression
        self.language = language
        self.testall_Content = testall_Content
        self.testall_Content13 = testall_Content13
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def testall_Content13(self):
        return self.__testall_Content13

    @testall_Content13.setter
    def testall_Content13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_Content__testall_Content13", None)
        self.__testall_Content13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_AbstractComponent14"):
                opp_val = getattr(old_value, "testall_AbstractComponent14", None)
                if opp_val == self:
                    setattr(old_value, "testall_AbstractComponent14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_AbstractComponent14"):
                opp_val = getattr(value, "testall_AbstractComponent14", None)
                setattr(value, "testall_AbstractComponent14", self)

    @property
    def testall_Content(self):
        return self.__testall_Content

    @testall_Content.setter
    def testall_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_Content__testall_Content", None)
        self.__testall_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_AbstractComponent"):
                opp_val = getattr(old_value, "testall_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "testall_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_AbstractComponent"):
                opp_val = getattr(value, "testall_AbstractComponent", None)
                setattr(value, "testall_AbstractComponent", self)

class testall_AbstractComponent(ABC):

    def __init__(self, name: str, testall_AbstractComponent: "testall_Content" = None, testall_AbstractComponent2: set["testall_Required"] = None, testall_AbstractComponent4: set["testall_Provided"] = None, testall_AbstractComponent14: "testall_Content" = None):
        self.name = name
        self.testall_AbstractComponent = testall_AbstractComponent
        self.testall_AbstractComponent2 = testall_AbstractComponent2 if testall_AbstractComponent2 is not None else set()
        self.testall_AbstractComponent4 = testall_AbstractComponent4 if testall_AbstractComponent4 is not None else set()
        self.testall_AbstractComponent14 = testall_AbstractComponent14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testall_AbstractComponent14(self):
        return self.__testall_AbstractComponent14

    @testall_AbstractComponent14.setter
    def testall_AbstractComponent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_AbstractComponent__testall_AbstractComponent14", None)
        self.__testall_AbstractComponent14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_Content13"):
                opp_val = getattr(old_value, "testall_Content13", None)
                if opp_val == self:
                    setattr(old_value, "testall_Content13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_Content13"):
                opp_val = getattr(value, "testall_Content13", None)
                setattr(value, "testall_Content13", self)

    @property
    def testall_AbstractComponent(self):
        return self.__testall_AbstractComponent

    @testall_AbstractComponent.setter
    def testall_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_AbstractComponent__testall_AbstractComponent", None)
        self.__testall_AbstractComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testall_Content"):
                opp_val = getattr(old_value, "testall_Content", None)
                if opp_val == self:
                    setattr(old_value, "testall_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testall_Content"):
                opp_val = getattr(value, "testall_Content", None)
                setattr(value, "testall_Content", self)

    @property
    def testall_AbstractComponent4(self):
        return self.__testall_AbstractComponent4

    @testall_AbstractComponent4.setter
    def testall_AbstractComponent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_AbstractComponent__testall_AbstractComponent4", None)
        self.__testall_AbstractComponent4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testall_Provided"):
                    opp_val = getattr(item, "testall_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "testall_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testall_Provided"):
                    opp_val = getattr(item, "testall_Provided", None)
                    
                    setattr(item, "testall_Provided", self)
                    

    @property
    def testall_AbstractComponent2(self):
        return self.__testall_AbstractComponent2

    @testall_AbstractComponent2.setter
    def testall_AbstractComponent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testall_AbstractComponent__testall_AbstractComponent2", None)
        self.__testall_AbstractComponent2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testall_Required"):
                    opp_val = getattr(item, "testall_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "testall_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testall_Required"):
                    opp_val = getattr(item, "testall_Required", None)
                    
                    setattr(item, "testall_Required", self)
                    

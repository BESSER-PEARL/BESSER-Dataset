from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    INT = "INT"
    STRING = "STRING"
    Boolean = "Boolean"
    Double = "Double"


############################################
# Definition of Classes
############################################

class testintentionsAssistance_Expression:

    pass
class Expression:

    pass
class testintentionsAssistance_Double(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class testintentionsAssistance_Plus(Expression):

    pass
class testintentionsAssistance_And(Expression):

    pass
class testintentionsAssistance_Minus(Expression):

    pass
class testintentionsAssistance_Comparison(Expression):

    def __init__(self, op: str, testintentionsAssistance_Comparison: "testintentionsAssistance_Expression" = None, testintentionsAssistance_Comparison38: "testintentionsAssistance_Expression" = None):
        self.op = op
        self.testintentionsAssistance_Comparison = testintentionsAssistance_Comparison
        self.testintentionsAssistance_Comparison38 = testintentionsAssistance_Comparison38
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def testintentionsAssistance_Comparison(self):
        return self.__testintentionsAssistance_Comparison

    @testintentionsAssistance_Comparison.setter
    def testintentionsAssistance_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Comparison__testintentionsAssistance_Comparison", None)
        self.__testintentionsAssistance_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression36"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression36"):
                opp_val = getattr(value, "testintentionsAssistance_Expression36", None)
                setattr(value, "testintentionsAssistance_Expression36", self)

    @property
    def testintentionsAssistance_Comparison38(self):
        return self.__testintentionsAssistance_Comparison38

    @testintentionsAssistance_Comparison38.setter
    def testintentionsAssistance_Comparison38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Comparison__testintentionsAssistance_Comparison38", None)
        self.__testintentionsAssistance_Comparison38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression39"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression39", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression39"):
                opp_val = getattr(value, "testintentionsAssistance_Expression39", None)
                setattr(value, "testintentionsAssistance_Expression39", self)

class testintentionsAssistance_INT(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class testintentionsAssistance_Not(Expression):

    pass
class testintentionsAssistance_STRING(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class testintentionsAssistance_MulOrDiv(Expression):

    def __init__(self, op: str, testintentionsAssistance_MulOrDiv: "testintentionsAssistance_Expression" = None, testintentionsAssistance_MulOrDiv53: "testintentionsAssistance_Expression" = None):
        self.op = op
        self.testintentionsAssistance_MulOrDiv = testintentionsAssistance_MulOrDiv
        self.testintentionsAssistance_MulOrDiv53 = testintentionsAssistance_MulOrDiv53
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def testintentionsAssistance_MulOrDiv53(self):
        return self.__testintentionsAssistance_MulOrDiv53

    @testintentionsAssistance_MulOrDiv53.setter
    def testintentionsAssistance_MulOrDiv53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_MulOrDiv__testintentionsAssistance_MulOrDiv53", None)
        self.__testintentionsAssistance_MulOrDiv53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression54"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression54"):
                opp_val = getattr(value, "testintentionsAssistance_Expression54", None)
                setattr(value, "testintentionsAssistance_Expression54", self)

    @property
    def testintentionsAssistance_MulOrDiv(self):
        return self.__testintentionsAssistance_MulOrDiv

    @testintentionsAssistance_MulOrDiv.setter
    def testintentionsAssistance_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_MulOrDiv__testintentionsAssistance_MulOrDiv", None)
        self.__testintentionsAssistance_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression51"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression51"):
                opp_val = getattr(value, "testintentionsAssistance_Expression51", None)
                setattr(value, "testintentionsAssistance_Expression51", self)

class testintentionsAssistance_VariableRef(Expression):

    pass
class testintentionsAssistance_Boolean(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class testintentionsAssistance_Equality(Expression):

    def __init__(self, op: str, testintentionsAssistance_Equality: "testintentionsAssistance_Expression" = None, testintentionsAssistance_Equality33: "testintentionsAssistance_Expression" = None):
        self.op = op
        self.testintentionsAssistance_Equality = testintentionsAssistance_Equality
        self.testintentionsAssistance_Equality33 = testintentionsAssistance_Equality33
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def testintentionsAssistance_Equality33(self):
        return self.__testintentionsAssistance_Equality33

    @testintentionsAssistance_Equality33.setter
    def testintentionsAssistance_Equality33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Equality__testintentionsAssistance_Equality33", None)
        self.__testintentionsAssistance_Equality33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression34"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression34"):
                opp_val = getattr(value, "testintentionsAssistance_Expression34", None)
                setattr(value, "testintentionsAssistance_Expression34", self)

    @property
    def testintentionsAssistance_Equality(self):
        return self.__testintentionsAssistance_Equality

    @testintentionsAssistance_Equality.setter
    def testintentionsAssistance_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Equality__testintentionsAssistance_Equality", None)
        self.__testintentionsAssistance_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Expression31"):
                opp_val = getattr(old_value, "testintentionsAssistance_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Expression31"):
                opp_val = getattr(value, "testintentionsAssistance_Expression31", None)
                setattr(value, "testintentionsAssistance_Expression31", self)

class testintentionsAssistance_Or(Expression):

    pass
class testintentionsAssistance_AbstractElement:

    pass
class testintentionsAssistance_Inst:

    pass
class testintentionsAssistance_Variable:

    def __init__(self, name: str, type: str, testintentionsAssistance_Variable: "testintentionsAssistance_Function" = None, testintentionsAssistance_Variable8: "testintentionsAssistance_Function" = None, testintentionsAssistance_Variable12: "testintentionsAssistance_Inst" = None, testintentionsAssistance_Variable58: "testintentionsAssistance_VariableRef" = None):
        self.name = name
        self.type = type
        self.testintentionsAssistance_Variable = testintentionsAssistance_Variable
        self.testintentionsAssistance_Variable8 = testintentionsAssistance_Variable8
        self.testintentionsAssistance_Variable12 = testintentionsAssistance_Variable12
        self.testintentionsAssistance_Variable58 = testintentionsAssistance_Variable58
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testintentionsAssistance_Variable8(self):
        return self.__testintentionsAssistance_Variable8

    @testintentionsAssistance_Variable8.setter
    def testintentionsAssistance_Variable8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Variable__testintentionsAssistance_Variable8", None)
        self.__testintentionsAssistance_Variable8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Function7"):
                opp_val = getattr(old_value, "testintentionsAssistance_Function7", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Function7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Function7"):
                opp_val = getattr(value, "testintentionsAssistance_Function7", None)
                setattr(value, "testintentionsAssistance_Function7", self)

    @property
    def testintentionsAssistance_Variable(self):
        return self.__testintentionsAssistance_Variable

    @testintentionsAssistance_Variable.setter
    def testintentionsAssistance_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Variable__testintentionsAssistance_Variable", None)
        self.__testintentionsAssistance_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Function5"):
                opp_val = getattr(old_value, "testintentionsAssistance_Function5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Function5"):
                opp_val = getattr(value, "testintentionsAssistance_Function5", None)
                if opp_val is None:
                    setattr(value, "testintentionsAssistance_Function5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testintentionsAssistance_Variable58(self):
        return self.__testintentionsAssistance_Variable58

    @testintentionsAssistance_Variable58.setter
    def testintentionsAssistance_Variable58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Variable__testintentionsAssistance_Variable58", None)
        self.__testintentionsAssistance_Variable58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_VariableRef"):
                opp_val = getattr(old_value, "testintentionsAssistance_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_VariableRef"):
                opp_val = getattr(value, "testintentionsAssistance_VariableRef", None)
                setattr(value, "testintentionsAssistance_VariableRef", self)

    @property
    def testintentionsAssistance_Variable12(self):
        return self.__testintentionsAssistance_Variable12

    @testintentionsAssistance_Variable12.setter
    def testintentionsAssistance_Variable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Variable__testintentionsAssistance_Variable12", None)
        self.__testintentionsAssistance_Variable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Inst11"):
                opp_val = getattr(old_value, "testintentionsAssistance_Inst11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Inst11"):
                opp_val = getattr(value, "testintentionsAssistance_Inst11", None)
                if opp_val is None:
                    setattr(value, "testintentionsAssistance_Inst11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testintentionsAssistance_OutVariable:

    def __init__(self, name: str, type: str, testintentionsAssistance_OutVariable: "testintentionsAssistance_Function" = None, testintentionsAssistance_OutVariable19: "testintentionsAssistance_TestIntention" = None):
        self.name = name
        self.type = type
        self.testintentionsAssistance_OutVariable = testintentionsAssistance_OutVariable
        self.testintentionsAssistance_OutVariable19 = testintentionsAssistance_OutVariable19
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testintentionsAssistance_OutVariable(self):
        return self.__testintentionsAssistance_OutVariable

    @testintentionsAssistance_OutVariable.setter
    def testintentionsAssistance_OutVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_OutVariable__testintentionsAssistance_OutVariable", None)
        self.__testintentionsAssistance_OutVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Function"):
                opp_val = getattr(old_value, "testintentionsAssistance_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Function"):
                opp_val = getattr(value, "testintentionsAssistance_Function", None)
                if opp_val is None:
                    setattr(value, "testintentionsAssistance_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testintentionsAssistance_OutVariable19(self):
        return self.__testintentionsAssistance_OutVariable19

    @testintentionsAssistance_OutVariable19.setter
    def testintentionsAssistance_OutVariable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_OutVariable__testintentionsAssistance_OutVariable19", None)
        self.__testintentionsAssistance_OutVariable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_TestIntention18"):
                opp_val = getattr(old_value, "testintentionsAssistance_TestIntention18", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_TestIntention18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_TestIntention18"):
                opp_val = getattr(value, "testintentionsAssistance_TestIntention18", None)
                setattr(value, "testintentionsAssistance_TestIntention18", self)

class AbstractElement:

    pass
class testintentionsAssistance_Function(AbstractElement):

    def __init__(self, methode: str, testintentionsAssistance_Function: set["testintentionsAssistance_OutVariable"] = None, testintentionsAssistance_Function5: set["testintentionsAssistance_Variable"] = None, testintentionsAssistance_Function7: "testintentionsAssistance_Variable" = None):
        self.methode = methode
        self.testintentionsAssistance_Function = testintentionsAssistance_Function if testintentionsAssistance_Function is not None else set()
        self.testintentionsAssistance_Function5 = testintentionsAssistance_Function5 if testintentionsAssistance_Function5 is not None else set()
        self.testintentionsAssistance_Function7 = testintentionsAssistance_Function7
        
    @property
    def methode(self) -> str:
        return self.__methode

    @methode.setter
    def methode(self, methode: str):
        self.__methode = methode

    @property
    def testintentionsAssistance_Function5(self):
        return self.__testintentionsAssistance_Function5

    @testintentionsAssistance_Function5.setter
    def testintentionsAssistance_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Function__testintentionsAssistance_Function5", None)
        self.__testintentionsAssistance_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testintentionsAssistance_Variable"):
                    opp_val = getattr(item, "testintentionsAssistance_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "testintentionsAssistance_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testintentionsAssistance_Variable"):
                    opp_val = getattr(item, "testintentionsAssistance_Variable", None)
                    
                    setattr(item, "testintentionsAssistance_Variable", self)
                    

    @property
    def testintentionsAssistance_Function7(self):
        return self.__testintentionsAssistance_Function7

    @testintentionsAssistance_Function7.setter
    def testintentionsAssistance_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Function__testintentionsAssistance_Function7", None)
        self.__testintentionsAssistance_Function7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Variable8"):
                opp_val = getattr(old_value, "testintentionsAssistance_Variable8", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_Variable8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Variable8"):
                opp_val = getattr(value, "testintentionsAssistance_Variable8", None)
                setattr(value, "testintentionsAssistance_Variable8", self)

    @property
    def testintentionsAssistance_Function(self):
        return self.__testintentionsAssistance_Function

    @testintentionsAssistance_Function.setter
    def testintentionsAssistance_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_Function__testintentionsAssistance_Function", None)
        self.__testintentionsAssistance_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testintentionsAssistance_OutVariable"):
                    opp_val = getattr(item, "testintentionsAssistance_OutVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "testintentionsAssistance_OutVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testintentionsAssistance_OutVariable"):
                    opp_val = getattr(item, "testintentionsAssistance_OutVariable", None)
                    
                    setattr(item, "testintentionsAssistance_OutVariable", self)
                    

class testintentionsAssistance_Data(AbstractElement):

    pass
class testintentionsAssistance_TestIntention(AbstractElement):

    def __init__(self, description: str, testintentionsAssistance_TestIntention: set["testintentionsAssistance_Expression"] = None, testintentionsAssistance_TestIntention18: "testintentionsAssistance_OutVariable" = None):
        self.description = description
        self.testintentionsAssistance_TestIntention = testintentionsAssistance_TestIntention if testintentionsAssistance_TestIntention is not None else set()
        self.testintentionsAssistance_TestIntention18 = testintentionsAssistance_TestIntention18
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def testintentionsAssistance_TestIntention18(self):
        return self.__testintentionsAssistance_TestIntention18

    @testintentionsAssistance_TestIntention18.setter
    def testintentionsAssistance_TestIntention18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_TestIntention__testintentionsAssistance_TestIntention18", None)
        self.__testintentionsAssistance_TestIntention18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_OutVariable19"):
                opp_val = getattr(old_value, "testintentionsAssistance_OutVariable19", None)
                if opp_val == self:
                    setattr(old_value, "testintentionsAssistance_OutVariable19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_OutVariable19"):
                opp_val = getattr(value, "testintentionsAssistance_OutVariable19", None)
                setattr(value, "testintentionsAssistance_OutVariable19", self)

    @property
    def testintentionsAssistance_TestIntention(self):
        return self.__testintentionsAssistance_TestIntention

    @testintentionsAssistance_TestIntention.setter
    def testintentionsAssistance_TestIntention(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_TestIntention__testintentionsAssistance_TestIntention", None)
        self.__testintentionsAssistance_TestIntention = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testintentionsAssistance_Expression16"):
                    opp_val = getattr(item, "testintentionsAssistance_Expression16", None)
                    
                    if opp_val == self:
                        setattr(item, "testintentionsAssistance_Expression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testintentionsAssistance_Expression16"):
                    opp_val = getattr(item, "testintentionsAssistance_Expression16", None)
                    
                    setattr(item, "testintentionsAssistance_Expression16", self)
                    

class testintentionsAssistance_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class testintentionsAssistance_DomainDeclaration(AbstractElement):

    def __init__(self, name: str, testintentionsAssistance_DomainDeclaration: "testintentionsAssistance_Model" = None, testintentionsAssistance_DomainDeclaration2: set["testintentionsAssistance_AbstractElement"] = None):
        self.name = name
        self.testintentionsAssistance_DomainDeclaration = testintentionsAssistance_DomainDeclaration
        self.testintentionsAssistance_DomainDeclaration2 = testintentionsAssistance_DomainDeclaration2 if testintentionsAssistance_DomainDeclaration2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testintentionsAssistance_DomainDeclaration2(self):
        return self.__testintentionsAssistance_DomainDeclaration2

    @testintentionsAssistance_DomainDeclaration2.setter
    def testintentionsAssistance_DomainDeclaration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_DomainDeclaration__testintentionsAssistance_DomainDeclaration2", None)
        self.__testintentionsAssistance_DomainDeclaration2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testintentionsAssistance_AbstractElement"):
                    opp_val = getattr(item, "testintentionsAssistance_AbstractElement", None)
                    
                    if opp_val == self:
                        setattr(item, "testintentionsAssistance_AbstractElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testintentionsAssistance_AbstractElement"):
                    opp_val = getattr(item, "testintentionsAssistance_AbstractElement", None)
                    
                    setattr(item, "testintentionsAssistance_AbstractElement", self)
                    

    @property
    def testintentionsAssistance_DomainDeclaration(self):
        return self.__testintentionsAssistance_DomainDeclaration

    @testintentionsAssistance_DomainDeclaration.setter
    def testintentionsAssistance_DomainDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testintentionsAssistance_DomainDeclaration__testintentionsAssistance_DomainDeclaration", None)
        self.__testintentionsAssistance_DomainDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testintentionsAssistance_Model"):
                opp_val = getattr(old_value, "testintentionsAssistance_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testintentionsAssistance_Model"):
                opp_val = getattr(value, "testintentionsAssistance_Model", None)
                if opp_val is None:
                    setattr(value, "testintentionsAssistance_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testintentionsAssistance_Model:

    pass
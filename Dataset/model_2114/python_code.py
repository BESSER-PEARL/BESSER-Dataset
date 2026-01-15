from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class xtextTest_ReplacePatterns:

    def __init__(self, regex: str, replace: str, xtextTest_ReplacePatterns: "xtextTest_Generator" = None):
        self.regex = regex
        self.replace = replace
        self.xtextTest_ReplacePatterns = xtextTest_ReplacePatterns
        
    @property
    def replace(self) -> str:
        return self.__replace

    @replace.setter
    def replace(self, replace: str):
        self.__replace = replace

    @property
    def regex(self) -> str:
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex

    @property
    def xtextTest_ReplacePatterns(self):
        return self.__xtextTest_ReplacePatterns

    @xtextTest_ReplacePatterns.setter
    def xtextTest_ReplacePatterns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_ReplacePatterns__xtextTest_ReplacePatterns", None)
        self.__xtextTest_ReplacePatterns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Generator45"):
                opp_val = getattr(old_value, "xtextTest_Generator45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Generator45"):
                opp_val = getattr(value, "xtextTest_Generator45", None)
                if opp_val is None:
                    setattr(value, "xtextTest_Generator45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xtextTest_Inner:

    def __init__(self, value: str, assignAsData: str, assignAsBool: str, isNull: bool, isNotNull: bool, isEmpty: bool, parameter: str, xtextTest_Inner: "xtextTest_Element" = None, xtextTest_Inner42: set["xtextTest_Element"] = None, xtextTest_Inner39: "xtextTest_Element" = None):
        self.value = value
        self.assignAsData = assignAsData
        self.assignAsBool = assignAsBool
        self.isNull = isNull
        self.isNotNull = isNotNull
        self.isEmpty = isEmpty
        self.parameter = parameter
        self.xtextTest_Inner = xtextTest_Inner
        self.xtextTest_Inner42 = xtextTest_Inner42 if xtextTest_Inner42 is not None else set()
        self.xtextTest_Inner39 = xtextTest_Inner39
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def isNull(self) -> bool:
        return self.__isNull

    @isNull.setter
    def isNull(self, isNull: bool):
        self.__isNull = isNull

    @property
    def isEmpty(self) -> bool:
        return self.__isEmpty

    @isEmpty.setter
    def isEmpty(self, isEmpty: bool):
        self.__isEmpty = isEmpty

    @property
    def assignAsData(self) -> str:
        return self.__assignAsData

    @assignAsData.setter
    def assignAsData(self, assignAsData: str):
        self.__assignAsData = assignAsData

    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def assignAsBool(self) -> str:
        return self.__assignAsBool

    @assignAsBool.setter
    def assignAsBool(self, assignAsBool: str):
        self.__assignAsBool = assignAsBool

    @property
    def isNotNull(self) -> bool:
        return self.__isNotNull

    @isNotNull.setter
    def isNotNull(self, isNotNull: bool):
        self.__isNotNull = isNotNull

    @property
    def xtextTest_Inner42(self):
        return self.__xtextTest_Inner42

    @xtextTest_Inner42.setter
    def xtextTest_Inner42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Inner__xtextTest_Inner42", None)
        self.__xtextTest_Inner42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtextTest_Element43"):
                    opp_val = getattr(item, "xtextTest_Element43", None)
                    
                    if opp_val == self:
                        setattr(item, "xtextTest_Element43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtextTest_Element43"):
                    opp_val = getattr(item, "xtextTest_Element43", None)
                    
                    setattr(item, "xtextTest_Element43", self)
                    

    @property
    def xtextTest_Inner39(self):
        return self.__xtextTest_Inner39

    @xtextTest_Inner39.setter
    def xtextTest_Inner39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Inner__xtextTest_Inner39", None)
        self.__xtextTest_Inner39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Element40"):
                opp_val = getattr(old_value, "xtextTest_Element40", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Element40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Element40"):
                opp_val = getattr(value, "xtextTest_Element40", None)
                setattr(value, "xtextTest_Element40", self)

    @property
    def xtextTest_Inner(self):
        return self.__xtextTest_Inner

    @xtextTest_Inner.setter
    def xtextTest_Inner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Inner__xtextTest_Inner", None)
        self.__xtextTest_Inner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Element37"):
                opp_val = getattr(old_value, "xtextTest_Element37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Element37"):
                opp_val = getattr(value, "xtextTest_Element37", None)
                if opp_val is None:
                    setattr(value, "xtextTest_Element37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xtextTest_MyTokens:

    def __init__(self, token: str, string: str, count: int, xtextTest_MyTokens: "xtextTest_Tokens" = None):
        self.token = token
        self.string = string
        self.count = count
        self.xtextTest_MyTokens = xtextTest_MyTokens
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def xtextTest_MyTokens(self):
        return self.__xtextTest_MyTokens

    @xtextTest_MyTokens.setter
    def xtextTest_MyTokens(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_MyTokens__xtextTest_MyTokens", None)
        self.__xtextTest_MyTokens = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Tokens35"):
                opp_val = getattr(old_value, "xtextTest_Tokens35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Tokens35"):
                opp_val = getattr(value, "xtextTest_Tokens35", None)
                if opp_val is None:
                    setattr(value, "xtextTest_Tokens35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xtextTest_After:

    pass
class xtextTest_Before:

    pass
class xtextTest_CodeCall:

    def __init__(self, myclass: str, method: str, params: str, xtextTest_CodeCall: "xtextTest_EmfTest" = None, xtextTest_CodeCall21: "xtextTest_EmfTest" = None, xtextTest_CodeCall24: "xtextTest_EmfTest" = None, xtextTest_CodeCall51: "xtextTest_After" = None, xtextTest_CodeCall48: "xtextTest_Before" = None):
        self.myclass = myclass
        self.method = method
        self.params = params
        self.xtextTest_CodeCall = xtextTest_CodeCall
        self.xtextTest_CodeCall21 = xtextTest_CodeCall21
        self.xtextTest_CodeCall24 = xtextTest_CodeCall24
        self.xtextTest_CodeCall51 = xtextTest_CodeCall51
        self.xtextTest_CodeCall48 = xtextTest_CodeCall48
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def myclass(self) -> str:
        return self.__myclass

    @myclass.setter
    def myclass(self, myclass: str):
        self.__myclass = myclass

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def xtextTest_CodeCall24(self):
        return self.__xtextTest_CodeCall24

    @xtextTest_CodeCall24.setter
    def xtextTest_CodeCall24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_CodeCall__xtextTest_CodeCall24", None)
        self.__xtextTest_CodeCall24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_EmfTest23"):
                opp_val = getattr(old_value, "xtextTest_EmfTest23", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_EmfTest23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_EmfTest23"):
                opp_val = getattr(value, "xtextTest_EmfTest23", None)
                setattr(value, "xtextTest_EmfTest23", self)

    @property
    def xtextTest_CodeCall48(self):
        return self.__xtextTest_CodeCall48

    @xtextTest_CodeCall48.setter
    def xtextTest_CodeCall48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_CodeCall__xtextTest_CodeCall48", None)
        self.__xtextTest_CodeCall48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Before47"):
                opp_val = getattr(old_value, "xtextTest_Before47", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Before47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Before47"):
                opp_val = getattr(value, "xtextTest_Before47", None)
                setattr(value, "xtextTest_Before47", self)

    @property
    def xtextTest_CodeCall21(self):
        return self.__xtextTest_CodeCall21

    @xtextTest_CodeCall21.setter
    def xtextTest_CodeCall21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_CodeCall__xtextTest_CodeCall21", None)
        self.__xtextTest_CodeCall21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_EmfTest20"):
                opp_val = getattr(old_value, "xtextTest_EmfTest20", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_EmfTest20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_EmfTest20"):
                opp_val = getattr(value, "xtextTest_EmfTest20", None)
                setattr(value, "xtextTest_EmfTest20", self)

    @property
    def xtextTest_CodeCall51(self):
        return self.__xtextTest_CodeCall51

    @xtextTest_CodeCall51.setter
    def xtextTest_CodeCall51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_CodeCall__xtextTest_CodeCall51", None)
        self.__xtextTest_CodeCall51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_After50"):
                opp_val = getattr(old_value, "xtextTest_After50", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_After50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_After50"):
                opp_val = getattr(value, "xtextTest_After50", None)
                setattr(value, "xtextTest_After50", self)

    @property
    def xtextTest_CodeCall(self):
        return self.__xtextTest_CodeCall

    @xtextTest_CodeCall.setter
    def xtextTest_CodeCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_CodeCall__xtextTest_CodeCall", None)
        self.__xtextTest_CodeCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_EmfTest18"):
                opp_val = getattr(old_value, "xtextTest_EmfTest18", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_EmfTest18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_EmfTest18"):
                opp_val = getattr(value, "xtextTest_EmfTest18", None)
                setattr(value, "xtextTest_EmfTest18", self)

class xtextTest_Import:

    def __init__(self, id: str, alias: str, xtextTest_Import: "xtextTest_EmfTest" = None):
        self.id = id
        self.alias = alias
        self.xtextTest_Import = xtextTest_Import
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xtextTest_Import(self):
        return self.__xtextTest_Import

    @xtextTest_Import.setter
    def xtextTest_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Import__xtextTest_Import", None)
        self.__xtextTest_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_EmfTest16"):
                opp_val = getattr(old_value, "xtextTest_EmfTest16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_EmfTest16"):
                opp_val = getattr(value, "xtextTest_EmfTest16", None)
                if opp_val is None:
                    setattr(value, "xtextTest_EmfTest16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xtextTest_XtextTest:

    def __init__(self, package: str, lang: str, imports: str, boolean: str, timeOut: int, xtextTest_XtextTest4: "xtextTest_Input" = None, xtextTest_XtextTest6: "xtextTest_Tokens" = None, xtextTest_XtextTest8: "xtextTest_Element" = None, xtextTest_XtextTest: "xtextTest_Model" = None, xtextTest_XtextTest14: "xtextTest_After" = None, xtextTest_XtextTest10: "xtextTest_Generator" = None, xtextTest_XtextTest12: "xtextTest_Before" = None):
        self.package = package
        self.lang = lang
        self.imports = imports
        self.boolean = boolean
        self.timeOut = timeOut
        self.xtextTest_XtextTest4 = xtextTest_XtextTest4
        self.xtextTest_XtextTest6 = xtextTest_XtextTest6
        self.xtextTest_XtextTest8 = xtextTest_XtextTest8
        self.xtextTest_XtextTest = xtextTest_XtextTest
        self.xtextTest_XtextTest14 = xtextTest_XtextTest14
        self.xtextTest_XtextTest10 = xtextTest_XtextTest10
        self.xtextTest_XtextTest12 = xtextTest_XtextTest12
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def timeOut(self) -> int:
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: int):
        self.__timeOut = timeOut

    @property
    def xtextTest_XtextTest8(self):
        return self.__xtextTest_XtextTest8

    @xtextTest_XtextTest8.setter
    def xtextTest_XtextTest8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest8", None)
        self.__xtextTest_XtextTest8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Element"):
                opp_val = getattr(old_value, "xtextTest_Element", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Element"):
                opp_val = getattr(value, "xtextTest_Element", None)
                setattr(value, "xtextTest_Element", self)

    @property
    def xtextTest_XtextTest(self):
        return self.__xtextTest_XtextTest

    @xtextTest_XtextTest.setter
    def xtextTest_XtextTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest", None)
        self.__xtextTest_XtextTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Model"):
                opp_val = getattr(old_value, "xtextTest_Model", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Model"):
                opp_val = getattr(value, "xtextTest_Model", None)
                setattr(value, "xtextTest_Model", self)

    @property
    def xtextTest_XtextTest10(self):
        return self.__xtextTest_XtextTest10

    @xtextTest_XtextTest10.setter
    def xtextTest_XtextTest10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest10", None)
        self.__xtextTest_XtextTest10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Generator"):
                opp_val = getattr(old_value, "xtextTest_Generator", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Generator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Generator"):
                opp_val = getattr(value, "xtextTest_Generator", None)
                setattr(value, "xtextTest_Generator", self)

    @property
    def xtextTest_XtextTest6(self):
        return self.__xtextTest_XtextTest6

    @xtextTest_XtextTest6.setter
    def xtextTest_XtextTest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest6", None)
        self.__xtextTest_XtextTest6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Tokens"):
                opp_val = getattr(old_value, "xtextTest_Tokens", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Tokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Tokens"):
                opp_val = getattr(value, "xtextTest_Tokens", None)
                setattr(value, "xtextTest_Tokens", self)

    @property
    def xtextTest_XtextTest12(self):
        return self.__xtextTest_XtextTest12

    @xtextTest_XtextTest12.setter
    def xtextTest_XtextTest12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest12", None)
        self.__xtextTest_XtextTest12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Before"):
                opp_val = getattr(old_value, "xtextTest_Before", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Before", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Before"):
                opp_val = getattr(value, "xtextTest_Before", None)
                setattr(value, "xtextTest_Before", self)

    @property
    def xtextTest_XtextTest14(self):
        return self.__xtextTest_XtextTest14

    @xtextTest_XtextTest14.setter
    def xtextTest_XtextTest14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest14", None)
        self.__xtextTest_XtextTest14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_After"):
                opp_val = getattr(old_value, "xtextTest_After", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_After", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_After"):
                opp_val = getattr(value, "xtextTest_After", None)
                setattr(value, "xtextTest_After", self)

    @property
    def xtextTest_XtextTest4(self):
        return self.__xtextTest_XtextTest4

    @xtextTest_XtextTest4.setter
    def xtextTest_XtextTest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_XtextTest__xtextTest_XtextTest4", None)
        self.__xtextTest_XtextTest4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Input"):
                opp_val = getattr(old_value, "xtextTest_Input", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Input"):
                opp_val = getattr(value, "xtextTest_Input", None)
                setattr(value, "xtextTest_Input", self)

class xtextTest_Model:

    pass
class xtextTest_Generator:

    def __init__(self, output: str, expected: str, isSameAsInputFile: bool, patternFile: str, exception: str, xtextTest_Generator: "xtextTest_XtextTest" = None, xtextTest_Generator45: set["xtextTest_ReplacePatterns"] = None):
        self.output = output
        self.expected = expected
        self.isSameAsInputFile = isSameAsInputFile
        self.patternFile = patternFile
        self.exception = exception
        self.xtextTest_Generator = xtextTest_Generator
        self.xtextTest_Generator45 = xtextTest_Generator45 if xtextTest_Generator45 is not None else set()
        
    @property
    def expected(self) -> str:
        return self.__expected

    @expected.setter
    def expected(self, expected: str):
        self.__expected = expected

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def exception(self) -> str:
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception

    @property
    def isSameAsInputFile(self) -> bool:
        return self.__isSameAsInputFile

    @isSameAsInputFile.setter
    def isSameAsInputFile(self, isSameAsInputFile: bool):
        self.__isSameAsInputFile = isSameAsInputFile

    @property
    def patternFile(self) -> str:
        return self.__patternFile

    @patternFile.setter
    def patternFile(self, patternFile: str):
        self.__patternFile = patternFile

    @property
    def xtextTest_Generator(self):
        return self.__xtextTest_Generator

    @xtextTest_Generator.setter
    def xtextTest_Generator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Generator__xtextTest_Generator", None)
        self.__xtextTest_Generator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_XtextTest10"):
                opp_val = getattr(old_value, "xtextTest_XtextTest10", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_XtextTest10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_XtextTest10"):
                opp_val = getattr(value, "xtextTest_XtextTest10", None)
                setattr(value, "xtextTest_XtextTest10", self)

    @property
    def xtextTest_Generator45(self):
        return self.__xtextTest_Generator45

    @xtextTest_Generator45.setter
    def xtextTest_Generator45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Generator__xtextTest_Generator45", None)
        self.__xtextTest_Generator45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtextTest_ReplacePatterns"):
                    opp_val = getattr(item, "xtextTest_ReplacePatterns", None)
                    
                    if opp_val == self:
                        setattr(item, "xtextTest_ReplacePatterns", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtextTest_ReplacePatterns"):
                    opp_val = getattr(item, "xtextTest_ReplacePatterns", None)
                    
                    setattr(item, "xtextTest_ReplacePatterns", self)
                    

class xtextTest_Element:

    def __init__(self, importing: str, name: str, xtextTest_Element: "xtextTest_XtextTest" = None, xtextTest_Element27: "xtextTest_EmfTest" = None, xtextTest_Element43: "xtextTest_Inner" = None, xtextTest_Element37: set["xtextTest_Inner"] = None, xtextTest_Element40: "xtextTest_Inner" = None):
        self.importing = importing
        self.name = name
        self.xtextTest_Element = xtextTest_Element
        self.xtextTest_Element27 = xtextTest_Element27
        self.xtextTest_Element43 = xtextTest_Element43
        self.xtextTest_Element37 = xtextTest_Element37 if xtextTest_Element37 is not None else set()
        self.xtextTest_Element40 = xtextTest_Element40
        
    @property
    def importing(self) -> str:
        return self.__importing

    @importing.setter
    def importing(self, importing: str):
        self.__importing = importing

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xtextTest_Element37(self):
        return self.__xtextTest_Element37

    @xtextTest_Element37.setter
    def xtextTest_Element37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Element__xtextTest_Element37", None)
        self.__xtextTest_Element37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtextTest_Inner"):
                    opp_val = getattr(item, "xtextTest_Inner", None)
                    
                    if opp_val == self:
                        setattr(item, "xtextTest_Inner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtextTest_Inner"):
                    opp_val = getattr(item, "xtextTest_Inner", None)
                    
                    setattr(item, "xtextTest_Inner", self)
                    

    @property
    def xtextTest_Element43(self):
        return self.__xtextTest_Element43

    @xtextTest_Element43.setter
    def xtextTest_Element43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Element__xtextTest_Element43", None)
        self.__xtextTest_Element43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Inner42"):
                opp_val = getattr(old_value, "xtextTest_Inner42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Inner42"):
                opp_val = getattr(value, "xtextTest_Inner42", None)
                if opp_val is None:
                    setattr(value, "xtextTest_Inner42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtextTest_Element(self):
        return self.__xtextTest_Element

    @xtextTest_Element.setter
    def xtextTest_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Element__xtextTest_Element", None)
        self.__xtextTest_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_XtextTest8"):
                opp_val = getattr(old_value, "xtextTest_XtextTest8", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_XtextTest8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_XtextTest8"):
                opp_val = getattr(value, "xtextTest_XtextTest8", None)
                setattr(value, "xtextTest_XtextTest8", self)

    @property
    def xtextTest_Element27(self):
        return self.__xtextTest_Element27

    @xtextTest_Element27.setter
    def xtextTest_Element27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Element__xtextTest_Element27", None)
        self.__xtextTest_Element27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_EmfTest26"):
                opp_val = getattr(old_value, "xtextTest_EmfTest26", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_EmfTest26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_EmfTest26"):
                opp_val = getattr(value, "xtextTest_EmfTest26", None)
                setattr(value, "xtextTest_EmfTest26", self)

    @property
    def xtextTest_Element40(self):
        return self.__xtextTest_Element40

    @xtextTest_Element40.setter
    def xtextTest_Element40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Element__xtextTest_Element40", None)
        self.__xtextTest_Element40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Inner39"):
                opp_val = getattr(old_value, "xtextTest_Inner39", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Inner39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Inner39"):
                opp_val = getattr(value, "xtextTest_Inner39", None)
                setattr(value, "xtextTest_Inner39", self)

class xtextTest_Tokens:

    pass
class xtextTest_Input:

    def __init__(self, text: str, file: str, xtextTest_Input: "xtextTest_XtextTest" = None):
        self.text = text
        self.file = file
        self.xtextTest_Input = xtextTest_Input
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def xtextTest_Input(self):
        return self.__xtextTest_Input

    @xtextTest_Input.setter
    def xtextTest_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_Input__xtextTest_Input", None)
        self.__xtextTest_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_XtextTest4"):
                opp_val = getattr(old_value, "xtextTest_XtextTest4", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_XtextTest4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_XtextTest4"):
                opp_val = getattr(value, "xtextTest_XtextTest4", None)
                setattr(value, "xtextTest_XtextTest4", self)

class xtextTest_EmfTest:

    def __init__(self, package: str, mydefault: str, timeOut: int, file: str, xtextTest_EmfTest: "xtextTest_Model" = None, xtextTest_EmfTest16: set["xtextTest_Import"] = None, xtextTest_EmfTest18: "xtextTest_CodeCall" = None, xtextTest_EmfTest20: "xtextTest_CodeCall" = None, xtextTest_EmfTest23: "xtextTest_CodeCall" = None, xtextTest_EmfTest26: "xtextTest_Element" = None, xtextTest_EmfTest29: "xtextTest_Before" = None, xtextTest_EmfTest32: "xtextTest_After" = None):
        self.package = package
        self.mydefault = mydefault
        self.timeOut = timeOut
        self.file = file
        self.xtextTest_EmfTest = xtextTest_EmfTest
        self.xtextTest_EmfTest16 = xtextTest_EmfTest16 if xtextTest_EmfTest16 is not None else set()
        self.xtextTest_EmfTest18 = xtextTest_EmfTest18
        self.xtextTest_EmfTest20 = xtextTest_EmfTest20
        self.xtextTest_EmfTest23 = xtextTest_EmfTest23
        self.xtextTest_EmfTest26 = xtextTest_EmfTest26
        self.xtextTest_EmfTest29 = xtextTest_EmfTest29
        self.xtextTest_EmfTest32 = xtextTest_EmfTest32
        
    @property
    def timeOut(self) -> int:
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: int):
        self.__timeOut = timeOut

    @property
    def mydefault(self) -> str:
        return self.__mydefault

    @mydefault.setter
    def mydefault(self, mydefault: str):
        self.__mydefault = mydefault

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def xtextTest_EmfTest29(self):
        return self.__xtextTest_EmfTest29

    @xtextTest_EmfTest29.setter
    def xtextTest_EmfTest29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest29", None)
        self.__xtextTest_EmfTest29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Before30"):
                opp_val = getattr(old_value, "xtextTest_Before30", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Before30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Before30"):
                opp_val = getattr(value, "xtextTest_Before30", None)
                setattr(value, "xtextTest_Before30", self)

    @property
    def xtextTest_EmfTest23(self):
        return self.__xtextTest_EmfTest23

    @xtextTest_EmfTest23.setter
    def xtextTest_EmfTest23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest23", None)
        self.__xtextTest_EmfTest23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_CodeCall24"):
                opp_val = getattr(old_value, "xtextTest_CodeCall24", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_CodeCall24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_CodeCall24"):
                opp_val = getattr(value, "xtextTest_CodeCall24", None)
                setattr(value, "xtextTest_CodeCall24", self)

    @property
    def xtextTest_EmfTest16(self):
        return self.__xtextTest_EmfTest16

    @xtextTest_EmfTest16.setter
    def xtextTest_EmfTest16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest16", None)
        self.__xtextTest_EmfTest16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtextTest_Import"):
                    opp_val = getattr(item, "xtextTest_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "xtextTest_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtextTest_Import"):
                    opp_val = getattr(item, "xtextTest_Import", None)
                    
                    setattr(item, "xtextTest_Import", self)
                    

    @property
    def xtextTest_EmfTest(self):
        return self.__xtextTest_EmfTest

    @xtextTest_EmfTest.setter
    def xtextTest_EmfTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest", None)
        self.__xtextTest_EmfTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Model2"):
                opp_val = getattr(old_value, "xtextTest_Model2", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Model2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Model2"):
                opp_val = getattr(value, "xtextTest_Model2", None)
                setattr(value, "xtextTest_Model2", self)

    @property
    def xtextTest_EmfTest32(self):
        return self.__xtextTest_EmfTest32

    @xtextTest_EmfTest32.setter
    def xtextTest_EmfTest32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest32", None)
        self.__xtextTest_EmfTest32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_After33"):
                opp_val = getattr(old_value, "xtextTest_After33", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_After33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_After33"):
                opp_val = getattr(value, "xtextTest_After33", None)
                setattr(value, "xtextTest_After33", self)

    @property
    def xtextTest_EmfTest18(self):
        return self.__xtextTest_EmfTest18

    @xtextTest_EmfTest18.setter
    def xtextTest_EmfTest18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest18", None)
        self.__xtextTest_EmfTest18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_CodeCall"):
                opp_val = getattr(old_value, "xtextTest_CodeCall", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_CodeCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_CodeCall"):
                opp_val = getattr(value, "xtextTest_CodeCall", None)
                setattr(value, "xtextTest_CodeCall", self)

    @property
    def xtextTest_EmfTest26(self):
        return self.__xtextTest_EmfTest26

    @xtextTest_EmfTest26.setter
    def xtextTest_EmfTest26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest26", None)
        self.__xtextTest_EmfTest26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_Element27"):
                opp_val = getattr(old_value, "xtextTest_Element27", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_Element27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_Element27"):
                opp_val = getattr(value, "xtextTest_Element27", None)
                setattr(value, "xtextTest_Element27", self)

    @property
    def xtextTest_EmfTest20(self):
        return self.__xtextTest_EmfTest20

    @xtextTest_EmfTest20.setter
    def xtextTest_EmfTest20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtextTest_EmfTest__xtextTest_EmfTest20", None)
        self.__xtextTest_EmfTest20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtextTest_CodeCall21"):
                opp_val = getattr(old_value, "xtextTest_CodeCall21", None)
                if opp_val == self:
                    setattr(old_value, "xtextTest_CodeCall21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtextTest_CodeCall21"):
                opp_val = getattr(value, "xtextTest_CodeCall21", None)
                setattr(value, "xtextTest_CodeCall21", self)

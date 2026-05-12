from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class spreadsheetGrammarLanguage_SyntaxSeq:

    pass
class spreadsheetGrammarLanguage_Syntax:

    def __init__(self, is_id: bool, is_string: bool, is_int: bool, token: str, spreadsheetGrammarLanguage_Syntax13: "spreadsheetGrammarLanguage_Rule" = None, spreadsheetGrammarLanguage_Syntax: "spreadsheetGrammarLanguage_RowSpec" = None, spreadsheetGrammarLanguage_Syntax18: "spreadsheetGrammarLanguage_SyntaxSeq" = None):
        self.is_id = is_id
        self.is_string = is_string
        self.is_int = is_int
        self.token = token
        self.spreadsheetGrammarLanguage_Syntax13 = spreadsheetGrammarLanguage_Syntax13
        self.spreadsheetGrammarLanguage_Syntax = spreadsheetGrammarLanguage_Syntax
        self.spreadsheetGrammarLanguage_Syntax18 = spreadsheetGrammarLanguage_Syntax18
        
        pass
    @property
    def is_int(self):
        return self.__is_int

    @is_int.setter
    def is_int(self, is_int: bool):
        self.__is_int = is_int


    @property
    def is_string(self):
        return self.__is_string

    @is_string.setter
    def is_string(self, is_string: bool):
        self.__is_string = is_string


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


    @property
    def is_id(self):
        return self.__is_id

    @is_id.setter
    def is_id(self, is_id: bool):
        self.__is_id = is_id


    @property
    def spreadsheetGrammarLanguage_Syntax13(self):
        return self.__spreadsheetGrammarLanguage_Syntax13

    @spreadsheetGrammarLanguage_Syntax13.setter
    def spreadsheetGrammarLanguage_Syntax13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Syntax__spreadsheetGrammarLanguage_Syntax13", None)
        self.__spreadsheetGrammarLanguage_Syntax13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_Rule"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_Rule", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheetGrammarLanguage_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_Rule"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_Rule", None)
                setattr(value, "spreadsheetGrammarLanguage_Rule", self)

    @property
    def spreadsheetGrammarLanguage_Syntax(self):
        return self.__spreadsheetGrammarLanguage_Syntax

    @spreadsheetGrammarLanguage_Syntax.setter
    def spreadsheetGrammarLanguage_Syntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Syntax__spreadsheetGrammarLanguage_Syntax", None)
        self.__spreadsheetGrammarLanguage_Syntax = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_RowSpec"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_RowSpec", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheetGrammarLanguage_RowSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_RowSpec"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_RowSpec", None)
                setattr(value, "spreadsheetGrammarLanguage_RowSpec", self)

    @property
    def spreadsheetGrammarLanguage_Syntax18(self):
        return self.__spreadsheetGrammarLanguage_Syntax18

    @spreadsheetGrammarLanguage_Syntax18.setter
    def spreadsheetGrammarLanguage_Syntax18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Syntax__spreadsheetGrammarLanguage_Syntax18", None)
        self.__spreadsheetGrammarLanguage_Syntax18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_SyntaxSeq17"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_SyntaxSeq17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_SyntaxSeq17"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_SyntaxSeq17", None)
                if opp_val is None:
                    setattr(value, "spreadsheetGrammarLanguage_SyntaxSeq17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ColumnSpec:

    pass
class spreadsheetGrammarLanguage_BlockSpec(ColumnSpec):

    pass
class spreadsheetGrammarLanguage_RowSpec(ColumnSpec):

    def __init__(self, header: str, spreadsheetGrammarLanguage_RowSpec: "spreadsheetGrammarLanguage_Syntax" = None):
        self.header = header
        self.spreadsheetGrammarLanguage_RowSpec = spreadsheetGrammarLanguage_RowSpec
        
        pass
    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header


    @property
    def spreadsheetGrammarLanguage_RowSpec(self):
        return self.__spreadsheetGrammarLanguage_RowSpec

    @spreadsheetGrammarLanguage_RowSpec.setter
    def spreadsheetGrammarLanguage_RowSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_RowSpec__spreadsheetGrammarLanguage_RowSpec", None)
        self.__spreadsheetGrammarLanguage_RowSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_Syntax"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_Syntax", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheetGrammarLanguage_Syntax", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_Syntax"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_Syntax", None)
                setattr(value, "spreadsheetGrammarLanguage_Syntax", self)

class ColumnDefinition:

    pass
class spreadsheetGrammarLanguage_OptionalColumn(ColumnDefinition):

    pass
class spreadsheetGrammarLanguage_MandatoryColumn(ColumnDefinition):

    pass
class spreadsheetGrammarLanguage_ColumnSpec:

    pass
class spreadsheetGrammarLanguage_ColumnDefinition:

    pass
class spreadsheetGrammarLanguage_Element:

    def __init__(self, name: str, spreadsheetGrammarLanguage_Element: "spreadsheetGrammarLanguage_Grammar" = None):
        self.name = name
        self.spreadsheetGrammarLanguage_Element = spreadsheetGrammarLanguage_Element
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def spreadsheetGrammarLanguage_Element(self):
        return self.__spreadsheetGrammarLanguage_Element

    @spreadsheetGrammarLanguage_Element.setter
    def spreadsheetGrammarLanguage_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Element__spreadsheetGrammarLanguage_Element", None)
        self.__spreadsheetGrammarLanguage_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_Grammar2"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_Grammar2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_Grammar2"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_Grammar2", None)
                if opp_val is None:
                    setattr(value, "spreadsheetGrammarLanguage_Grammar2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spreadsheetGrammarLanguage_Grammar:

    def __init__(self, name: str, spreadsheetGrammarLanguage_Grammar: "spreadsheetGrammarLanguage_Block" = None, spreadsheetGrammarLanguage_Grammar2: set["spreadsheetGrammarLanguage_Element"] = None):
        self.name = name
        self.spreadsheetGrammarLanguage_Grammar = spreadsheetGrammarLanguage_Grammar
        self.spreadsheetGrammarLanguage_Grammar2 = spreadsheetGrammarLanguage_Grammar2 if spreadsheetGrammarLanguage_Grammar2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def spreadsheetGrammarLanguage_Grammar2(self):
        return self.__spreadsheetGrammarLanguage_Grammar2

    @spreadsheetGrammarLanguage_Grammar2.setter
    def spreadsheetGrammarLanguage_Grammar2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Grammar__spreadsheetGrammarLanguage_Grammar2", None)
        self.__spreadsheetGrammarLanguage_Grammar2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheetGrammarLanguage_Element"):
                    opp_val = getattr(item, "spreadsheetGrammarLanguage_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheetGrammarLanguage_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheetGrammarLanguage_Element"):
                    opp_val = getattr(item, "spreadsheetGrammarLanguage_Element", None)
                    
                    setattr(item, "spreadsheetGrammarLanguage_Element", self)
                    

    @property
    def spreadsheetGrammarLanguage_Grammar(self):
        return self.__spreadsheetGrammarLanguage_Grammar

    @spreadsheetGrammarLanguage_Grammar.setter
    def spreadsheetGrammarLanguage_Grammar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Grammar__spreadsheetGrammarLanguage_Grammar", None)
        self.__spreadsheetGrammarLanguage_Grammar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_Block"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_Block", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheetGrammarLanguage_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_Block"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_Block", None)
                setattr(value, "spreadsheetGrammarLanguage_Block", self)

class spreadsheetGrammarLanguage_Column:

    def __init__(self, name: str, multiple: bool, spreadsheetGrammarLanguage_Column: "spreadsheetGrammarLanguage_Block" = None, spreadsheetGrammarLanguage_Column6: "spreadsheetGrammarLanguage_ColumnDefinition" = None):
        self.name = name
        self.multiple = multiple
        self.spreadsheetGrammarLanguage_Column = spreadsheetGrammarLanguage_Column
        self.spreadsheetGrammarLanguage_Column6 = spreadsheetGrammarLanguage_Column6
        
        pass
    @property
    def multiple(self):
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def spreadsheetGrammarLanguage_Column6(self):
        return self.__spreadsheetGrammarLanguage_Column6

    @spreadsheetGrammarLanguage_Column6.setter
    def spreadsheetGrammarLanguage_Column6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Column__spreadsheetGrammarLanguage_Column6", None)
        self.__spreadsheetGrammarLanguage_Column6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_ColumnDefinition"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_ColumnDefinition", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheetGrammarLanguage_ColumnDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_ColumnDefinition"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_ColumnDefinition", None)
                setattr(value, "spreadsheetGrammarLanguage_ColumnDefinition", self)

    @property
    def spreadsheetGrammarLanguage_Column(self):
        return self.__spreadsheetGrammarLanguage_Column

    @spreadsheetGrammarLanguage_Column.setter
    def spreadsheetGrammarLanguage_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheetGrammarLanguage_Column__spreadsheetGrammarLanguage_Column", None)
        self.__spreadsheetGrammarLanguage_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheetGrammarLanguage_Block4"):
                opp_val = getattr(old_value, "spreadsheetGrammarLanguage_Block4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheetGrammarLanguage_Block4"):
                opp_val = getattr(value, "spreadsheetGrammarLanguage_Block4", None)
                if opp_val is None:
                    setattr(value, "spreadsheetGrammarLanguage_Block4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class spreadsheetGrammarLanguage_Rule(Element):

    pass
class spreadsheetGrammarLanguage_Block(Element):

    pass
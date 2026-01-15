from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CONTROL_SENTENCES:

    pass
class tortugaDSL_TO(CONTROL_SENTENCES):

    def __init__(self, name: str, tortugaDSL_TO: set["tortugaDSL_PARAM"] = None, tortugaDSL_TO37: "tortugaDSL_PROCEDURE_CALL" = None):
        self.name = name
        self.tortugaDSL_TO = tortugaDSL_TO if tortugaDSL_TO is not None else set()
        self.tortugaDSL_TO37 = tortugaDSL_TO37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tortugaDSL_TO37(self):
        return self.__tortugaDSL_TO37

    @tortugaDSL_TO37.setter
    def tortugaDSL_TO37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tortugaDSL_TO__tortugaDSL_TO37", None)
        self.__tortugaDSL_TO37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tortugaDSL_PROCEDURE_CALL"):
                opp_val = getattr(old_value, "tortugaDSL_PROCEDURE_CALL", None)
                if opp_val == self:
                    setattr(old_value, "tortugaDSL_PROCEDURE_CALL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tortugaDSL_PROCEDURE_CALL"):
                opp_val = getattr(value, "tortugaDSL_PROCEDURE_CALL", None)
                setattr(value, "tortugaDSL_PROCEDURE_CALL", self)

    @property
    def tortugaDSL_TO(self):
        return self.__tortugaDSL_TO

    @tortugaDSL_TO.setter
    def tortugaDSL_TO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tortugaDSL_TO__tortugaDSL_TO", None)
        self.__tortugaDSL_TO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tortugaDSL_PARAM"):
                    opp_val = getattr(item, "tortugaDSL_PARAM", None)
                    
                    if opp_val == self:
                        setattr(item, "tortugaDSL_PARAM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tortugaDSL_PARAM"):
                    opp_val = getattr(item, "tortugaDSL_PARAM", None)
                    
                    setattr(item, "tortugaDSL_PARAM", self)
                    

class tortugaDSL_REPEAT(CONTROL_SENTENCES):

    pass
class FontStyleValues:

    pass
class tortugaDSL_PLAIN(FontStyleValues):

    pass
class tortugaDSL_ITALIC(FontStyleValues):

    pass
class tortugaDSL_BOLD(FontStyleValues):

    pass
class BOOLEAN_EXPRESSION:

    pass
class tortugaDSL_LESSER_THAN(BOOLEAN_EXPRESSION):

    pass
class tortugaDSL_GREATER_THAN(BOOLEAN_EXPRESSION):

    pass
class tortugaDSL_EQUALS(BOOLEAN_EXPRESSION):

    pass
class tortugaDSL_BOOLEAN_EXPRESSION:

    pass
class tortugaDSL_IF(CONTROL_SENTENCES):

    pass
class REFERENCIABLE:

    pass
class tortugaDSL_PARAM(REFERENCIABLE):

    pass
class tortugaDSL_REFERENCIABLE:

    def __init__(self, name: str, tortugaDSL_REFERENCIABLE: "tortugaDSL_VARIABLE_REF" = None):
        self.name = name
        self.tortugaDSL_REFERENCIABLE = tortugaDSL_REFERENCIABLE
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tortugaDSL_REFERENCIABLE(self):
        return self.__tortugaDSL_REFERENCIABLE

    @tortugaDSL_REFERENCIABLE.setter
    def tortugaDSL_REFERENCIABLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tortugaDSL_REFERENCIABLE__tortugaDSL_REFERENCIABLE", None)
        self.__tortugaDSL_REFERENCIABLE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tortugaDSL_VARIABLE_REF"):
                opp_val = getattr(old_value, "tortugaDSL_VARIABLE_REF", None)
                if opp_val == self:
                    setattr(old_value, "tortugaDSL_VARIABLE_REF", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tortugaDSL_VARIABLE_REF"):
                opp_val = getattr(value, "tortugaDSL_VARIABLE_REF", None)
                setattr(value, "tortugaDSL_VARIABLE_REF", self)

class OPERATION:

    pass
class tortugaDSL_DIVIDE(OPERATION):

    pass
class tortugaDSL_MULTIPLY(OPERATION):

    pass
class tortugaDSL_SUBTRACT(OPERATION):

    pass
class tortugaDSL_SUM(OPERATION):

    pass
class EXPRESSION:

    pass
class tortugaDSL_VALUE(EXPRESSION):

    def __init__(self, val: float):
        self.val = val
        
    @property
    def val(self) -> float:
        return self.__val

    @val.setter
    def val(self, val: float):
        self.__val = val

class tortugaDSL_VARIABLE_REF(EXPRESSION):

    pass
class DRAWING_SENTENCE:

    pass
class tortugaDSL_PENUP(DRAWING_SENTENCE):

    pass
class tortugaDSL_DRAW_STRING(DRAWING_SENTENCE):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class tortugaDSL_PENDOWN(DRAWING_SENTENCE):

    pass
class tortugaDSL_HOME(DRAWING_SENTENCE):

    pass
class tortugaDSL_CLEAR(DRAWING_SENTENCE):

    pass
class tortugaDSL_FontStyleValues:

    pass
class FONT_SPEC:

    pass
class tortugaDSL_FONT_STYLE(FONT_SPEC):

    pass
class tortugaDSL_FONT_SIZE(FONT_SPEC):

    pass
class tortugaDSL_FONT_SPEC(DRAWING_SENTENCE):

    pass
class COLOREABLE:

    pass
class tortugaDSL_CANVAS_COLOR(COLOREABLE):

    pass
class tortugaDSL_PENCOLOR(COLOREABLE):

    pass
class tortugaDSL_COLOR_SPEC:

    pass
class tortugaDSL_COLOREABLE(DRAWING_SENTENCE):

    def __init__(self, color: str, tortugaDSL_COLOREABLE: "tortugaDSL_COLOR_SPEC" = None):
        self.color = color
        self.tortugaDSL_COLOREABLE = tortugaDSL_COLOREABLE
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def tortugaDSL_COLOREABLE(self):
        return self.__tortugaDSL_COLOREABLE

    @tortugaDSL_COLOREABLE.setter
    def tortugaDSL_COLOREABLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tortugaDSL_COLOREABLE__tortugaDSL_COLOREABLE", None)
        self.__tortugaDSL_COLOREABLE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tortugaDSL_COLOR_SPEC"):
                opp_val = getattr(old_value, "tortugaDSL_COLOR_SPEC", None)
                if opp_val == self:
                    setattr(old_value, "tortugaDSL_COLOR_SPEC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tortugaDSL_COLOR_SPEC"):
                opp_val = getattr(value, "tortugaDSL_COLOR_SPEC", None)
                setattr(value, "tortugaDSL_COLOR_SPEC", self)

class MOVE:

    pass
class tortugaDSL_SET_Y(MOVE):

    pass
class tortugaDSL_RIGHT(MOVE):

    pass
class tortugaDSL_LEFT(MOVE):

    pass
class tortugaDSL_SET_X(MOVE):

    pass
class tortugaDSL_FORWARD(MOVE):

    pass
class tortugaDSL_EXPRESSION:

    pass
class SENTENCE:

    pass
class tortugaDSL_PROCEDURE_CALL(SENTENCE):

    pass
class tortugaDSL_CONTROL_SENTENCES(SENTENCE):

    pass
class tortugaDSL_MAKE(SENTENCE, REFERENCIABLE):

    pass
class tortugaDSL_OPERATION(SENTENCE):

    pass
class tortugaDSL_CONTENT(SENTENCE):

    pass
class tortugaDSL_DRAWING_SENTENCE(SENTENCE):

    pass
class tortugaDSL_MOVE(SENTENCE):

    pass
class tortugaDSL_SENTENCE:

    pass
class tortugaDSL_TortugaProgram:

    pass
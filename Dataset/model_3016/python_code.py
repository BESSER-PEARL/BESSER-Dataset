from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_declaration_list:

    pass
class myDsl_function_definition:

    pass
class myDsl_external_declaration:

    pass
class type_specifier:

    pass
class myDsl_voidType(type_specifier):

    def __init__(self, void_type: str):
        self.void_type = void_type
        
    @property
    def void_type(self) -> str:
        return self.__void_type

    @void_type.setter
    def void_type(self, void_type: str):
        self.__void_type = void_type

class myDsl_imaginaryType(type_specifier):

    def __init__(self, imaginary_type: str):
        self.imaginary_type = imaginary_type
        
    @property
    def imaginary_type(self) -> str:
        return self.__imaginary_type

    @imaginary_type.setter
    def imaginary_type(self, imaginary_type: str):
        self.__imaginary_type = imaginary_type

class myDsl_complexType(type_specifier):

    def __init__(self, complex_type: str):
        self.complex_type = complex_type
        
    @property
    def complex_type(self) -> str:
        return self.__complex_type

    @complex_type.setter
    def complex_type(self, complex_type: str):
        self.__complex_type = complex_type

class myDsl_doubleType(type_specifier):

    def __init__(self, double_type: str):
        self.double_type = double_type
        
    @property
    def double_type(self) -> str:
        return self.__double_type

    @double_type.setter
    def double_type(self, double_type: str):
        self.__double_type = double_type

class myDsl_longType(type_specifier):

    def __init__(self, long_type: str):
        self.long_type = long_type
        
    @property
    def long_type(self) -> str:
        return self.__long_type

    @long_type.setter
    def long_type(self, long_type: str):
        self.__long_type = long_type

class myDsl_charType(type_specifier):

    def __init__(self, char_type: str):
        self.char_type = char_type
        
    @property
    def char_type(self) -> str:
        return self.__char_type

    @char_type.setter
    def char_type(self, char_type: str):
        self.__char_type = char_type

class myDsl_signedType(type_specifier):

    def __init__(self, signed_type: str):
        self.signed_type = signed_type
        
    @property
    def signed_type(self) -> str:
        return self.__signed_type

    @signed_type.setter
    def signed_type(self, signed_type: str):
        self.__signed_type = signed_type

class myDsl_shortType(type_specifier):

    def __init__(self, short_type: str):
        self.short_type = short_type
        
    @property
    def short_type(self) -> str:
        return self.__short_type

    @short_type.setter
    def short_type(self, short_type: str):
        self.__short_type = short_type

class myDsl_unsignedType(type_specifier):

    def __init__(self, unsigned_type: str):
        self.unsigned_type = unsigned_type
        
    @property
    def unsigned_type(self) -> str:
        return self.__unsigned_type

    @unsigned_type.setter
    def unsigned_type(self, unsigned_type: str):
        self.__unsigned_type = unsigned_type

class myDsl_declaration_list2:

    pass
class myDsl_block_item:

    pass
class myDsl_jump_statement:

    def __init__(self, goto: str, identifier: str, continue: str, break: str, return: str, myDsl_jump_statement: "myDsl_statement" = None, myDsl_jump_statement356: "myDsl_expression" = None):
        self.goto = goto
        self.identifier = identifier
        self.continue = continue
        self.break = break
        self.return = return
        self.myDsl_jump_statement = myDsl_jump_statement
        self.myDsl_jump_statement356 = myDsl_jump_statement356
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def continue(self) -> str:
        return self.__continue

    @continue.setter
    def continue(self, continue: str):
        self.__continue = continue

    @property
    def goto(self) -> str:
        return self.__goto

    @goto.setter
    def goto(self, goto: str):
        self.__goto = goto

    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def myDsl_jump_statement356(self):
        return self.__myDsl_jump_statement356

    @myDsl_jump_statement356.setter
    def myDsl_jump_statement356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_jump_statement__myDsl_jump_statement356", None)
        self.__myDsl_jump_statement356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression357"):
                opp_val = getattr(old_value, "myDsl_expression357", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression357"):
                opp_val = getattr(value, "myDsl_expression357", None)
                setattr(value, "myDsl_expression357", self)

    @property
    def myDsl_jump_statement(self):
        return self.__myDsl_jump_statement

    @myDsl_jump_statement.setter
    def myDsl_jump_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_jump_statement__myDsl_jump_statement", None)
        self.__myDsl_jump_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement314"):
                opp_val = getattr(old_value, "myDsl_statement314", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement314"):
                opp_val = getattr(value, "myDsl_statement314", None)
                setattr(value, "myDsl_statement314", self)

class myDsl_iteration_statement:

    def __init__(self, while: str, do: str, for: str, myDsl_iteration_statement342: "myDsl_EObject" = None, myDsl_iteration_statement344: "myDsl_statement" = None, myDsl_iteration_statement347: "myDsl_expression_statement" = None, myDsl_iteration_statement: "myDsl_statement" = None, myDsl_iteration_statement350: "myDsl_expression_statement" = None, myDsl_iteration_statement353: "myDsl_declaration" = None):
        self.while = while
        self.do = do
        self.for = for
        self.myDsl_iteration_statement342 = myDsl_iteration_statement342
        self.myDsl_iteration_statement344 = myDsl_iteration_statement344
        self.myDsl_iteration_statement347 = myDsl_iteration_statement347
        self.myDsl_iteration_statement = myDsl_iteration_statement
        self.myDsl_iteration_statement350 = myDsl_iteration_statement350
        self.myDsl_iteration_statement353 = myDsl_iteration_statement353
        
    @property
    def do(self) -> str:
        return self.__do

    @do.setter
    def do(self, do: str):
        self.__do = do

    @property
    def for(self) -> str:
        return self.__for

    @for.setter
    def for(self, for: str):
        self.__for = for

    @property
    def while(self) -> str:
        return self.__while

    @while.setter
    def while(self, while: str):
        self.__while = while

    @property
    def myDsl_iteration_statement342(self):
        return self.__myDsl_iteration_statement342

    @myDsl_iteration_statement342.setter
    def myDsl_iteration_statement342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement342", None)
        self.__myDsl_iteration_statement342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_EObject"):
                opp_val = getattr(old_value, "myDsl_EObject", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_EObject"):
                opp_val = getattr(value, "myDsl_EObject", None)
                setattr(value, "myDsl_EObject", self)

    @property
    def myDsl_iteration_statement353(self):
        return self.__myDsl_iteration_statement353

    @myDsl_iteration_statement353.setter
    def myDsl_iteration_statement353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement353", None)
        self.__myDsl_iteration_statement353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration354"):
                opp_val = getattr(old_value, "myDsl_declaration354", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration354"):
                opp_val = getattr(value, "myDsl_declaration354", None)
                setattr(value, "myDsl_declaration354", self)

    @property
    def myDsl_iteration_statement344(self):
        return self.__myDsl_iteration_statement344

    @myDsl_iteration_statement344.setter
    def myDsl_iteration_statement344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement344", None)
        self.__myDsl_iteration_statement344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement345"):
                opp_val = getattr(old_value, "myDsl_statement345", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement345"):
                opp_val = getattr(value, "myDsl_statement345", None)
                setattr(value, "myDsl_statement345", self)

    @property
    def myDsl_iteration_statement(self):
        return self.__myDsl_iteration_statement

    @myDsl_iteration_statement.setter
    def myDsl_iteration_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement", None)
        self.__myDsl_iteration_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement312"):
                opp_val = getattr(old_value, "myDsl_statement312", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement312"):
                opp_val = getattr(value, "myDsl_statement312", None)
                setattr(value, "myDsl_statement312", self)

    @property
    def myDsl_iteration_statement347(self):
        return self.__myDsl_iteration_statement347

    @myDsl_iteration_statement347.setter
    def myDsl_iteration_statement347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement347", None)
        self.__myDsl_iteration_statement347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression_statement348"):
                opp_val = getattr(old_value, "myDsl_expression_statement348", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression_statement348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression_statement348"):
                opp_val = getattr(value, "myDsl_expression_statement348", None)
                setattr(value, "myDsl_expression_statement348", self)

    @property
    def myDsl_iteration_statement350(self):
        return self.__myDsl_iteration_statement350

    @myDsl_iteration_statement350.setter
    def myDsl_iteration_statement350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_iteration_statement__myDsl_iteration_statement350", None)
        self.__myDsl_iteration_statement350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression_statement351"):
                opp_val = getattr(old_value, "myDsl_expression_statement351", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression_statement351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression_statement351"):
                opp_val = getattr(value, "myDsl_expression_statement351", None)
                setattr(value, "myDsl_expression_statement351", self)

class myDsl_selection_statement:

    def __init__(self, else: str, switch: str, if: str, myDsl_selection_statement333: "myDsl_simple_expression" = None, myDsl_selection_statement336: "myDsl_statement" = None, myDsl_selection_statement339: "myDsl_statement" = None, myDsl_selection_statement: "myDsl_statement" = None):
        self.else = else
        self.switch = switch
        self.if = if
        self.myDsl_selection_statement333 = myDsl_selection_statement333
        self.myDsl_selection_statement336 = myDsl_selection_statement336
        self.myDsl_selection_statement339 = myDsl_selection_statement339
        self.myDsl_selection_statement = myDsl_selection_statement
        
    @property
    def if(self) -> str:
        return self.__if

    @if.setter
    def if(self, if: str):
        self.__if = if

    @property
    def switch(self) -> str:
        return self.__switch

    @switch.setter
    def switch(self, switch: str):
        self.__switch = switch

    @property
    def else(self) -> str:
        return self.__else

    @else.setter
    def else(self, else: str):
        self.__else = else

    @property
    def myDsl_selection_statement336(self):
        return self.__myDsl_selection_statement336

    @myDsl_selection_statement336.setter
    def myDsl_selection_statement336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_selection_statement__myDsl_selection_statement336", None)
        self.__myDsl_selection_statement336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement337"):
                opp_val = getattr(old_value, "myDsl_statement337", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement337"):
                opp_val = getattr(value, "myDsl_statement337", None)
                setattr(value, "myDsl_statement337", self)

    @property
    def myDsl_selection_statement(self):
        return self.__myDsl_selection_statement

    @myDsl_selection_statement.setter
    def myDsl_selection_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_selection_statement__myDsl_selection_statement", None)
        self.__myDsl_selection_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement310"):
                opp_val = getattr(old_value, "myDsl_statement310", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement310"):
                opp_val = getattr(value, "myDsl_statement310", None)
                setattr(value, "myDsl_statement310", self)

    @property
    def myDsl_selection_statement339(self):
        return self.__myDsl_selection_statement339

    @myDsl_selection_statement339.setter
    def myDsl_selection_statement339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_selection_statement__myDsl_selection_statement339", None)
        self.__myDsl_selection_statement339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement340"):
                opp_val = getattr(old_value, "myDsl_statement340", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement340"):
                opp_val = getattr(value, "myDsl_statement340", None)
                setattr(value, "myDsl_statement340", self)

    @property
    def myDsl_selection_statement333(self):
        return self.__myDsl_selection_statement333

    @myDsl_selection_statement333.setter
    def myDsl_selection_statement333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_selection_statement__myDsl_selection_statement333", None)
        self.__myDsl_selection_statement333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression334"):
                opp_val = getattr(old_value, "myDsl_simple_expression334", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression334"):
                opp_val = getattr(value, "myDsl_simple_expression334", None)
                setattr(value, "myDsl_simple_expression334", self)

class myDsl_EObject:

    pass
class myDsl_designator_list2:

    pass
class myDsl_designator:

    def __init__(self, identifier: str, myDsl_designator294: "myDsl_designator_list2" = None, myDsl_designator299: "myDsl_constant_expression" = None, myDsl_designator: "myDsl_designator_list" = None):
        self.identifier = identifier
        self.myDsl_designator294 = myDsl_designator294
        self.myDsl_designator299 = myDsl_designator299
        self.myDsl_designator = myDsl_designator
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_designator299(self):
        return self.__myDsl_designator299

    @myDsl_designator299.setter
    def myDsl_designator299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_designator__myDsl_designator299", None)
        self.__myDsl_designator299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_constant_expression300"):
                opp_val = getattr(old_value, "myDsl_constant_expression300", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_constant_expression300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_constant_expression300"):
                opp_val = getattr(value, "myDsl_constant_expression300", None)
                setattr(value, "myDsl_constant_expression300", self)

    @property
    def myDsl_designator294(self):
        return self.__myDsl_designator294

    @myDsl_designator294.setter
    def myDsl_designator294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_designator__myDsl_designator294", None)
        self.__myDsl_designator294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_designator_list2293"):
                opp_val = getattr(old_value, "myDsl_designator_list2293", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_designator_list2293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_designator_list2293"):
                opp_val = getattr(value, "myDsl_designator_list2293", None)
                setattr(value, "myDsl_designator_list2293", self)

    @property
    def myDsl_designator(self):
        return self.__myDsl_designator

    @myDsl_designator.setter
    def myDsl_designator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_designator__myDsl_designator", None)
        self.__myDsl_designator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_designator_list289"):
                opp_val = getattr(old_value, "myDsl_designator_list289", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_designator_list289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_designator_list289"):
                opp_val = getattr(value, "myDsl_designator_list289", None)
                setattr(value, "myDsl_designator_list289", self)

class myDsl_designator_list:

    pass
class myDsl_initializer_list2:

    pass
class myDsl_designation:

    pass
class myDsl_initializer:

    pass
class myDsl_expression_statement:

    pass
class myDsl_compound_statement:

    pass
class myDsl_labeled_statement:

    def __init__(self, identifier: str, case: str, default: str, myDsl_labeled_statement: "myDsl_statement" = None, myDsl_labeled_statement316: "myDsl_statement" = None, myDsl_labeled_statement319: "myDsl_constant_expression" = None):
        self.identifier = identifier
        self.case = case
        self.default = default
        self.myDsl_labeled_statement = myDsl_labeled_statement
        self.myDsl_labeled_statement316 = myDsl_labeled_statement316
        self.myDsl_labeled_statement319 = myDsl_labeled_statement319
        
    @property
    def case(self) -> str:
        return self.__case

    @case.setter
    def case(self, case: str):
        self.__case = case

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def myDsl_labeled_statement(self):
        return self.__myDsl_labeled_statement

    @myDsl_labeled_statement.setter
    def myDsl_labeled_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_labeled_statement__myDsl_labeled_statement", None)
        self.__myDsl_labeled_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement"):
                opp_val = getattr(old_value, "myDsl_statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement"):
                opp_val = getattr(value, "myDsl_statement", None)
                setattr(value, "myDsl_statement", self)

    @property
    def myDsl_labeled_statement319(self):
        return self.__myDsl_labeled_statement319

    @myDsl_labeled_statement319.setter
    def myDsl_labeled_statement319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_labeled_statement__myDsl_labeled_statement319", None)
        self.__myDsl_labeled_statement319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_constant_expression320"):
                opp_val = getattr(old_value, "myDsl_constant_expression320", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_constant_expression320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_constant_expression320"):
                opp_val = getattr(value, "myDsl_constant_expression320", None)
                setattr(value, "myDsl_constant_expression320", self)

    @property
    def myDsl_labeled_statement316(self):
        return self.__myDsl_labeled_statement316

    @myDsl_labeled_statement316.setter
    def myDsl_labeled_statement316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_labeled_statement__myDsl_labeled_statement316", None)
        self.__myDsl_labeled_statement316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement317"):
                opp_val = getattr(old_value, "myDsl_statement317", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement317"):
                opp_val = getattr(value, "myDsl_statement317", None)
                setattr(value, "myDsl_statement317", self)

class myDsl_statement:

    pass
class myDsl_identifier_list2:

    def __init__(self, identifier: str, myDsl_identifier_list2: "myDsl_identifier_list" = None, myDsl_identifier_list2242: "myDsl_identifier_list2" = None, myDsl_identifier_list2240: "myDsl_identifier_list2" = None):
        self.identifier = identifier
        self.myDsl_identifier_list2 = myDsl_identifier_list2
        self.myDsl_identifier_list2242 = myDsl_identifier_list2242
        self.myDsl_identifier_list2240 = myDsl_identifier_list2240
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_identifier_list2240(self):
        return self.__myDsl_identifier_list2240

    @myDsl_identifier_list2240.setter
    def myDsl_identifier_list2240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list2__myDsl_identifier_list2240", None)
        self.__myDsl_identifier_list2240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list2242"):
                opp_val = getattr(old_value, "myDsl_identifier_list2242", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list2242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list2242"):
                opp_val = getattr(value, "myDsl_identifier_list2242", None)
                setattr(value, "myDsl_identifier_list2242", self)

    @property
    def myDsl_identifier_list2(self):
        return self.__myDsl_identifier_list2

    @myDsl_identifier_list2.setter
    def myDsl_identifier_list2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list2__myDsl_identifier_list2", None)
        self.__myDsl_identifier_list2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list239"):
                opp_val = getattr(old_value, "myDsl_identifier_list239", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list239"):
                opp_val = getattr(value, "myDsl_identifier_list239", None)
                setattr(value, "myDsl_identifier_list239", self)

    @property
    def myDsl_identifier_list2242(self):
        return self.__myDsl_identifier_list2242

    @myDsl_identifier_list2242.setter
    def myDsl_identifier_list2242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list2__myDsl_identifier_list2242", None)
        self.__myDsl_identifier_list2242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list2240"):
                opp_val = getattr(old_value, "myDsl_identifier_list2240", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list2240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list2240"):
                opp_val = getattr(value, "myDsl_identifier_list2240", None)
                setattr(value, "myDsl_identifier_list2240", self)

class myDsl_abstract_declarator:

    pass
class myDsl_parameter_list2:

    pass
class myDsl_parameter_declaration:

    pass
class myDsl_direct_abstract_declarator2:

    def __init__(self, static: str, myDsl_direct_abstract_declarator2: "myDsl_direct_abstract_declarator" = None, myDsl_direct_abstract_declarator2257: "myDsl_type_qualifier_list" = None, myDsl_direct_abstract_declarator2260: "myDsl_assignment_expression" = None, myDsl_direct_abstract_declarator2263: "myDsl_parameter_type_list" = None):
        self.static = static
        self.myDsl_direct_abstract_declarator2 = myDsl_direct_abstract_declarator2
        self.myDsl_direct_abstract_declarator2257 = myDsl_direct_abstract_declarator2257
        self.myDsl_direct_abstract_declarator2260 = myDsl_direct_abstract_declarator2260
        self.myDsl_direct_abstract_declarator2263 = myDsl_direct_abstract_declarator2263
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def myDsl_direct_abstract_declarator2(self):
        return self.__myDsl_direct_abstract_declarator2

    @myDsl_direct_abstract_declarator2.setter
    def myDsl_direct_abstract_declarator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_abstract_declarator2__myDsl_direct_abstract_declarator2", None)
        self.__myDsl_direct_abstract_declarator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_abstract_declarator255"):
                opp_val = getattr(old_value, "myDsl_direct_abstract_declarator255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_abstract_declarator255"):
                opp_val = getattr(value, "myDsl_direct_abstract_declarator255", None)
                if opp_val is None:
                    setattr(value, "myDsl_direct_abstract_declarator255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_direct_abstract_declarator2263(self):
        return self.__myDsl_direct_abstract_declarator2263

    @myDsl_direct_abstract_declarator2263.setter
    def myDsl_direct_abstract_declarator2263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_abstract_declarator2__myDsl_direct_abstract_declarator2263", None)
        self.__myDsl_direct_abstract_declarator2263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_type_list264"):
                opp_val = getattr(old_value, "myDsl_parameter_type_list264", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_type_list264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_type_list264"):
                opp_val = getattr(value, "myDsl_parameter_type_list264", None)
                setattr(value, "myDsl_parameter_type_list264", self)

    @property
    def myDsl_direct_abstract_declarator2257(self):
        return self.__myDsl_direct_abstract_declarator2257

    @myDsl_direct_abstract_declarator2257.setter
    def myDsl_direct_abstract_declarator2257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_abstract_declarator2__myDsl_direct_abstract_declarator2257", None)
        self.__myDsl_direct_abstract_declarator2257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_list258"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_list258", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_list258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_list258"):
                opp_val = getattr(value, "myDsl_type_qualifier_list258", None)
                setattr(value, "myDsl_type_qualifier_list258", self)

    @property
    def myDsl_direct_abstract_declarator2260(self):
        return self.__myDsl_direct_abstract_declarator2260

    @myDsl_direct_abstract_declarator2260.setter
    def myDsl_direct_abstract_declarator2260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_abstract_declarator2__myDsl_direct_abstract_declarator2260", None)
        self.__myDsl_direct_abstract_declarator2260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression261"):
                opp_val = getattr(old_value, "myDsl_assignment_expression261", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression261"):
                opp_val = getattr(value, "myDsl_assignment_expression261", None)
                setattr(value, "myDsl_assignment_expression261", self)

class myDsl_direct_abstract_declarator:

    pass
class myDsl_identifier_list:

    def __init__(self, identifier: str, myDsl_identifier_list: "myDsl_direct_declarator2" = None, myDsl_identifier_list239: "myDsl_identifier_list2" = None):
        self.identifier = identifier
        self.myDsl_identifier_list = myDsl_identifier_list
        self.myDsl_identifier_list239 = myDsl_identifier_list239
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_identifier_list239(self):
        return self.__myDsl_identifier_list239

    @myDsl_identifier_list239.setter
    def myDsl_identifier_list239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list__myDsl_identifier_list239", None)
        self.__myDsl_identifier_list239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list2"):
                opp_val = getattr(old_value, "myDsl_identifier_list2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list2"):
                opp_val = getattr(value, "myDsl_identifier_list2", None)
                setattr(value, "myDsl_identifier_list2", self)

    @property
    def myDsl_identifier_list(self):
        return self.__myDsl_identifier_list

    @myDsl_identifier_list.setter
    def myDsl_identifier_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list__myDsl_identifier_list", None)
        self.__myDsl_identifier_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator2200"):
                opp_val = getattr(old_value, "myDsl_direct_declarator2200", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator2200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator2200"):
                opp_val = getattr(value, "myDsl_direct_declarator2200", None)
                setattr(value, "myDsl_direct_declarator2200", self)

class myDsl_parameter_type_list:

    def __init__(self, ellipsis: str, myDsl_parameter_type_list: "myDsl_direct_declarator2" = None, myDsl_parameter_type_list264: "myDsl_direct_abstract_declarator2" = None, myDsl_parameter_type_list219: "myDsl_parameter_list" = None):
        self.ellipsis = ellipsis
        self.myDsl_parameter_type_list = myDsl_parameter_type_list
        self.myDsl_parameter_type_list264 = myDsl_parameter_type_list264
        self.myDsl_parameter_type_list219 = myDsl_parameter_type_list219
        
    @property
    def ellipsis(self) -> str:
        return self.__ellipsis

    @ellipsis.setter
    def ellipsis(self, ellipsis: str):
        self.__ellipsis = ellipsis

    @property
    def myDsl_parameter_type_list219(self):
        return self.__myDsl_parameter_type_list219

    @myDsl_parameter_type_list219.setter
    def myDsl_parameter_type_list219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_parameter_type_list__myDsl_parameter_type_list219", None)
        self.__myDsl_parameter_type_list219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_list"):
                opp_val = getattr(old_value, "myDsl_parameter_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_list"):
                opp_val = getattr(value, "myDsl_parameter_list", None)
                setattr(value, "myDsl_parameter_list", self)

    @property
    def myDsl_parameter_type_list(self):
        return self.__myDsl_parameter_type_list

    @myDsl_parameter_type_list.setter
    def myDsl_parameter_type_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_parameter_type_list__myDsl_parameter_type_list", None)
        self.__myDsl_parameter_type_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator2198"):
                opp_val = getattr(old_value, "myDsl_direct_declarator2198", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator2198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator2198"):
                opp_val = getattr(value, "myDsl_direct_declarator2198", None)
                setattr(value, "myDsl_direct_declarator2198", self)

    @property
    def myDsl_parameter_type_list264(self):
        return self.__myDsl_parameter_type_list264

    @myDsl_parameter_type_list264.setter
    def myDsl_parameter_type_list264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_parameter_type_list__myDsl_parameter_type_list264", None)
        self.__myDsl_parameter_type_list264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_abstract_declarator2263"):
                opp_val = getattr(old_value, "myDsl_direct_abstract_declarator2263", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_abstract_declarator2263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_abstract_declarator2263"):
                opp_val = getattr(value, "myDsl_direct_abstract_declarator2263", None)
                setattr(value, "myDsl_direct_abstract_declarator2263", self)

class myDsl_type_qualifier_list:

    pass
class myDsl_direct_declarator2:

    def __init__(self, static: str, myDsl_direct_declarator2200: "myDsl_identifier_list" = None, myDsl_direct_declarator2: "myDsl_direct_declarator" = None, myDsl_direct_declarator2191: "myDsl_direct_declarator2" = None, myDsl_direct_declarator2189: set["myDsl_direct_declarator2"] = None, myDsl_direct_declarator2193: "myDsl_type_qualifier_list" = None, myDsl_direct_declarator2195: "myDsl_assignment_expression" = None, myDsl_direct_declarator2198: "myDsl_parameter_type_list" = None):
        self.static = static
        self.myDsl_direct_declarator2200 = myDsl_direct_declarator2200
        self.myDsl_direct_declarator2 = myDsl_direct_declarator2
        self.myDsl_direct_declarator2191 = myDsl_direct_declarator2191
        self.myDsl_direct_declarator2189 = myDsl_direct_declarator2189 if myDsl_direct_declarator2189 is not None else set()
        self.myDsl_direct_declarator2193 = myDsl_direct_declarator2193
        self.myDsl_direct_declarator2195 = myDsl_direct_declarator2195
        self.myDsl_direct_declarator2198 = myDsl_direct_declarator2198
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def myDsl_direct_declarator2193(self):
        return self.__myDsl_direct_declarator2193

    @myDsl_direct_declarator2193.setter
    def myDsl_direct_declarator2193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2193", None)
        self.__myDsl_direct_declarator2193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_list"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_list"):
                opp_val = getattr(value, "myDsl_type_qualifier_list", None)
                setattr(value, "myDsl_type_qualifier_list", self)

    @property
    def myDsl_direct_declarator2198(self):
        return self.__myDsl_direct_declarator2198

    @myDsl_direct_declarator2198.setter
    def myDsl_direct_declarator2198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2198", None)
        self.__myDsl_direct_declarator2198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_type_list"):
                opp_val = getattr(old_value, "myDsl_parameter_type_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_type_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_type_list"):
                opp_val = getattr(value, "myDsl_parameter_type_list", None)
                setattr(value, "myDsl_parameter_type_list", self)

    @property
    def myDsl_direct_declarator2189(self):
        return self.__myDsl_direct_declarator2189

    @myDsl_direct_declarator2189.setter
    def myDsl_direct_declarator2189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2189", None)
        self.__myDsl_direct_declarator2189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_direct_declarator2191"):
                    opp_val = getattr(item, "myDsl_direct_declarator2191", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_direct_declarator2191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_direct_declarator2191"):
                    opp_val = getattr(item, "myDsl_direct_declarator2191", None)
                    
                    setattr(item, "myDsl_direct_declarator2191", self)
                    

    @property
    def myDsl_direct_declarator2191(self):
        return self.__myDsl_direct_declarator2191

    @myDsl_direct_declarator2191.setter
    def myDsl_direct_declarator2191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2191", None)
        self.__myDsl_direct_declarator2191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator2189"):
                opp_val = getattr(old_value, "myDsl_direct_declarator2189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator2189"):
                opp_val = getattr(value, "myDsl_direct_declarator2189", None)
                if opp_val is None:
                    setattr(value, "myDsl_direct_declarator2189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_direct_declarator2(self):
        return self.__myDsl_direct_declarator2

    @myDsl_direct_declarator2.setter
    def myDsl_direct_declarator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2", None)
        self.__myDsl_direct_declarator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator185"):
                opp_val = getattr(old_value, "myDsl_direct_declarator185", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator185"):
                opp_val = getattr(value, "myDsl_direct_declarator185", None)
                setattr(value, "myDsl_direct_declarator185", self)

    @property
    def myDsl_direct_declarator2200(self):
        return self.__myDsl_direct_declarator2200

    @myDsl_direct_declarator2200.setter
    def myDsl_direct_declarator2200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2200", None)
        self.__myDsl_direct_declarator2200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list"):
                opp_val = getattr(old_value, "myDsl_identifier_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list"):
                opp_val = getattr(value, "myDsl_identifier_list", None)
                setattr(value, "myDsl_identifier_list", self)

    @property
    def myDsl_direct_declarator2195(self):
        return self.__myDsl_direct_declarator2195

    @myDsl_direct_declarator2195.setter
    def myDsl_direct_declarator2195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator2__myDsl_direct_declarator2195", None)
        self.__myDsl_direct_declarator2195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression196"):
                opp_val = getattr(old_value, "myDsl_assignment_expression196", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression196"):
                opp_val = getattr(value, "myDsl_assignment_expression196", None)
                setattr(value, "myDsl_assignment_expression196", self)

class myDsl_direct_declarator:

    def __init__(self, name: str, myDsl_direct_declarator: "myDsl_declarator" = None, myDsl_direct_declarator185: "myDsl_direct_declarator2" = None, myDsl_direct_declarator187: "myDsl_declarator" = None):
        self.name = name
        self.myDsl_direct_declarator = myDsl_direct_declarator
        self.myDsl_direct_declarator185 = myDsl_direct_declarator185
        self.myDsl_direct_declarator187 = myDsl_direct_declarator187
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_direct_declarator(self):
        return self.__myDsl_direct_declarator

    @myDsl_direct_declarator.setter
    def myDsl_direct_declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator__myDsl_direct_declarator", None)
        self.__myDsl_direct_declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declarator183"):
                opp_val = getattr(old_value, "myDsl_declarator183", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declarator183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declarator183"):
                opp_val = getattr(value, "myDsl_declarator183", None)
                setattr(value, "myDsl_declarator183", self)

    @property
    def myDsl_direct_declarator185(self):
        return self.__myDsl_direct_declarator185

    @myDsl_direct_declarator185.setter
    def myDsl_direct_declarator185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator__myDsl_direct_declarator185", None)
        self.__myDsl_direct_declarator185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator2"):
                opp_val = getattr(old_value, "myDsl_direct_declarator2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator2"):
                opp_val = getattr(value, "myDsl_direct_declarator2", None)
                setattr(value, "myDsl_direct_declarator2", self)

    @property
    def myDsl_direct_declarator187(self):
        return self.__myDsl_direct_declarator187

    @myDsl_direct_declarator187.setter
    def myDsl_direct_declarator187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator__myDsl_direct_declarator187", None)
        self.__myDsl_direct_declarator187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declarator188"):
                opp_val = getattr(old_value, "myDsl_declarator188", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declarator188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declarator188"):
                opp_val = getattr(value, "myDsl_declarator188", None)
                setattr(value, "myDsl_declarator188", self)

class myDsl_pointer:

    pass
class myDsl_parameter_list:

    pass
class myDsl_type_qualifier_list2:

    pass
class myDsl_enumerator_list2:

    pass
class myDsl_enumerator:

    pass
class myDsl_enumerator_list:

    pass
class myDsl_struct_declarator_list2:

    pass
class myDsl_struct_declarator:

    pass
class myDsl_struct_declaration:

    pass
class struct_or_union_specifier:

    pass
class myDsl_struct_declaration_list:

    pass
class myDsl_struct_or_union(struct_or_union_specifier):

    def __init__(self, struct: str, union: str, myDsl_struct_or_union: "myDsl_struct_or_union_specifier" = None):
        self.struct = struct
        self.union = union
        self.myDsl_struct_or_union = myDsl_struct_or_union
        
    @property
    def struct(self) -> str:
        return self.__struct

    @struct.setter
    def struct(self, struct: str):
        self.__struct = struct

    @property
    def union(self) -> str:
        return self.__union

    @union.setter
    def union(self, union: str):
        self.__union = union

    @property
    def myDsl_struct_or_union(self):
        return self.__myDsl_struct_or_union

    @myDsl_struct_or_union.setter
    def myDsl_struct_or_union(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union__myDsl_struct_or_union", None)
        self.__myDsl_struct_or_union = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_or_union_specifier109"):
                opp_val = getattr(old_value, "myDsl_struct_or_union_specifier109", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_or_union_specifier109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_or_union_specifier109"):
                opp_val = getattr(value, "myDsl_struct_or_union_specifier109", None)
                setattr(value, "myDsl_struct_or_union_specifier109", self)

class myDsl_enum_specifier:

    def __init__(self, enumt: str, identifier: str, myDsl_enum_specifier: "myDsl_type_specifier" = None, myDsl_enum_specifier155: "myDsl_enumerator_list" = None):
        self.enumt = enumt
        self.identifier = identifier
        self.myDsl_enum_specifier = myDsl_enum_specifier
        self.myDsl_enum_specifier155 = myDsl_enum_specifier155
        
    @property
    def enumt(self) -> str:
        return self.__enumt

    @enumt.setter
    def enumt(self, enumt: str):
        self.__enumt = enumt

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_enum_specifier(self):
        return self.__myDsl_enum_specifier

    @myDsl_enum_specifier.setter
    def myDsl_enum_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_enum_specifier__myDsl_enum_specifier", None)
        self.__myDsl_enum_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier107"):
                opp_val = getattr(old_value, "myDsl_type_specifier107", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier107"):
                opp_val = getattr(value, "myDsl_type_specifier107", None)
                setattr(value, "myDsl_type_specifier107", self)

    @property
    def myDsl_enum_specifier155(self):
        return self.__myDsl_enum_specifier155

    @myDsl_enum_specifier155.setter
    def myDsl_enum_specifier155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_enum_specifier__myDsl_enum_specifier155", None)
        self.__myDsl_enum_specifier155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_enumerator_list"):
                opp_val = getattr(old_value, "myDsl_enumerator_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_enumerator_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_enumerator_list"):
                opp_val = getattr(value, "myDsl_enumerator_list", None)
                setattr(value, "myDsl_enumerator_list", self)

class myDsl_struct_or_union_specifier:

    def __init__(self, identifier: str, myDsl_struct_or_union_specifier: "myDsl_type_specifier" = None, myDsl_struct_or_union_specifier109: "myDsl_struct_or_union" = None, myDsl_struct_or_union_specifier111: "myDsl_struct_declaration_list" = None):
        self.identifier = identifier
        self.myDsl_struct_or_union_specifier = myDsl_struct_or_union_specifier
        self.myDsl_struct_or_union_specifier109 = myDsl_struct_or_union_specifier109
        self.myDsl_struct_or_union_specifier111 = myDsl_struct_or_union_specifier111
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_struct_or_union_specifier111(self):
        return self.__myDsl_struct_or_union_specifier111

    @myDsl_struct_or_union_specifier111.setter
    def myDsl_struct_or_union_specifier111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier111", None)
        self.__myDsl_struct_or_union_specifier111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_declaration_list"):
                opp_val = getattr(old_value, "myDsl_struct_declaration_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_declaration_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_declaration_list"):
                opp_val = getattr(value, "myDsl_struct_declaration_list", None)
                setattr(value, "myDsl_struct_declaration_list", self)

    @property
    def myDsl_struct_or_union_specifier109(self):
        return self.__myDsl_struct_or_union_specifier109

    @myDsl_struct_or_union_specifier109.setter
    def myDsl_struct_or_union_specifier109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier109", None)
        self.__myDsl_struct_or_union_specifier109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_or_union"):
                opp_val = getattr(old_value, "myDsl_struct_or_union", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_or_union", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_or_union"):
                opp_val = getattr(value, "myDsl_struct_or_union", None)
                setattr(value, "myDsl_struct_or_union", self)

    @property
    def myDsl_struct_or_union_specifier(self):
        return self.__myDsl_struct_or_union_specifier

    @myDsl_struct_or_union_specifier.setter
    def myDsl_struct_or_union_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier", None)
        self.__myDsl_struct_or_union_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier105"):
                opp_val = getattr(old_value, "myDsl_type_specifier105", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier105"):
                opp_val = getattr(value, "myDsl_type_specifier105", None)
                setattr(value, "myDsl_type_specifier105", self)

class myDsl_atomic_type_specifier:

    def __init__(self, atomic: str, myDsl_atomic_type_specifier: "myDsl_type_specifier" = None, myDsl_atomic_type_specifier172: "myDsl_type_name" = None):
        self.atomic = atomic
        self.myDsl_atomic_type_specifier = myDsl_atomic_type_specifier
        self.myDsl_atomic_type_specifier172 = myDsl_atomic_type_specifier172
        
    @property
    def atomic(self) -> str:
        return self.__atomic

    @atomic.setter
    def atomic(self, atomic: str):
        self.__atomic = atomic

    @property
    def myDsl_atomic_type_specifier(self):
        return self.__myDsl_atomic_type_specifier

    @myDsl_atomic_type_specifier.setter
    def myDsl_atomic_type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_atomic_type_specifier__myDsl_atomic_type_specifier", None)
        self.__myDsl_atomic_type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier103"):
                opp_val = getattr(old_value, "myDsl_type_specifier103", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier103"):
                opp_val = getattr(value, "myDsl_type_specifier103", None)
                setattr(value, "myDsl_type_specifier103", self)

    @property
    def myDsl_atomic_type_specifier172(self):
        return self.__myDsl_atomic_type_specifier172

    @myDsl_atomic_type_specifier172.setter
    def myDsl_atomic_type_specifier172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_atomic_type_specifier__myDsl_atomic_type_specifier172", None)
        self.__myDsl_atomic_type_specifier172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_name173"):
                opp_val = getattr(old_value, "myDsl_type_name173", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_name173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_name173"):
                opp_val = getattr(value, "myDsl_type_name173", None)
                setattr(value, "myDsl_type_name173", self)

class myDsl_struct_declarator_list:

    pass
class myDsl_specifier_qualifier_list:

    pass
class myDsl_struct_declaration_list2:

    pass
class myDsl_init_declarator_list2:

    pass
class myDsl_init_declarator:

    pass
class myDsl_alignment_specifier:

    def __init__(self, alignas: str, myDsl_alignment_specifier: "myDsl_declaration_specifiers" = None, myDsl_alignment_specifier175: "myDsl_type_name" = None, myDsl_alignment_specifier178: "myDsl_constant_expression" = None):
        self.alignas = alignas
        self.myDsl_alignment_specifier = myDsl_alignment_specifier
        self.myDsl_alignment_specifier175 = myDsl_alignment_specifier175
        self.myDsl_alignment_specifier178 = myDsl_alignment_specifier178
        
    @property
    def alignas(self) -> str:
        return self.__alignas

    @alignas.setter
    def alignas(self, alignas: str):
        self.__alignas = alignas

    @property
    def myDsl_alignment_specifier(self):
        return self.__myDsl_alignment_specifier

    @myDsl_alignment_specifier.setter
    def myDsl_alignment_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_alignment_specifier__myDsl_alignment_specifier", None)
        self.__myDsl_alignment_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers86"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers86", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers86"):
                opp_val = getattr(value, "myDsl_declaration_specifiers86", None)
                setattr(value, "myDsl_declaration_specifiers86", self)

    @property
    def myDsl_alignment_specifier178(self):
        return self.__myDsl_alignment_specifier178

    @myDsl_alignment_specifier178.setter
    def myDsl_alignment_specifier178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_alignment_specifier__myDsl_alignment_specifier178", None)
        self.__myDsl_alignment_specifier178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_constant_expression179"):
                opp_val = getattr(old_value, "myDsl_constant_expression179", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_constant_expression179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_constant_expression179"):
                opp_val = getattr(value, "myDsl_constant_expression179", None)
                setattr(value, "myDsl_constant_expression179", self)

    @property
    def myDsl_alignment_specifier175(self):
        return self.__myDsl_alignment_specifier175

    @myDsl_alignment_specifier175.setter
    def myDsl_alignment_specifier175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_alignment_specifier__myDsl_alignment_specifier175", None)
        self.__myDsl_alignment_specifier175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_name176"):
                opp_val = getattr(old_value, "myDsl_type_name176", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_name176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_name176"):
                opp_val = getattr(value, "myDsl_type_name176", None)
                setattr(value, "myDsl_type_name176", self)

class myDsl_function_specifier:

    def __init__(self, inline: str, noreturn: str, myDsl_function_specifier: "myDsl_declaration_specifiers" = None):
        self.inline = inline
        self.noreturn = noreturn
        self.myDsl_function_specifier = myDsl_function_specifier
        
    @property
    def noreturn(self) -> str:
        return self.__noreturn

    @noreturn.setter
    def noreturn(self, noreturn: str):
        self.__noreturn = noreturn

    @property
    def inline(self) -> str:
        return self.__inline

    @inline.setter
    def inline(self, inline: str):
        self.__inline = inline

    @property
    def myDsl_function_specifier(self):
        return self.__myDsl_function_specifier

    @myDsl_function_specifier.setter
    def myDsl_function_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_function_specifier__myDsl_function_specifier", None)
        self.__myDsl_function_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers84"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers84", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers84"):
                opp_val = getattr(value, "myDsl_declaration_specifiers84", None)
                setattr(value, "myDsl_declaration_specifiers84", self)

class myDsl_type_qualifier:

    def __init__(self, const: str, restrict: str, volatile: str, atomic: str, myDsl_type_qualifier: "myDsl_declaration_specifiers" = None, myDsl_type_qualifier209: "myDsl_type_qualifier_list" = None, myDsl_type_qualifier214: "myDsl_type_qualifier_list2" = None):
        self.const = const
        self.restrict = restrict
        self.volatile = volatile
        self.atomic = atomic
        self.myDsl_type_qualifier = myDsl_type_qualifier
        self.myDsl_type_qualifier209 = myDsl_type_qualifier209
        self.myDsl_type_qualifier214 = myDsl_type_qualifier214
        
    @property
    def const(self) -> str:
        return self.__const

    @const.setter
    def const(self, const: str):
        self.__const = const

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def atomic(self) -> str:
        return self.__atomic

    @atomic.setter
    def atomic(self, atomic: str):
        self.__atomic = atomic

    @property
    def restrict(self) -> str:
        return self.__restrict

    @restrict.setter
    def restrict(self, restrict: str):
        self.__restrict = restrict

    @property
    def myDsl_type_qualifier(self):
        return self.__myDsl_type_qualifier

    @myDsl_type_qualifier.setter
    def myDsl_type_qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier", None)
        self.__myDsl_type_qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers82"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers82", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers82"):
                opp_val = getattr(value, "myDsl_declaration_specifiers82", None)
                setattr(value, "myDsl_declaration_specifiers82", self)

    @property
    def myDsl_type_qualifier209(self):
        return self.__myDsl_type_qualifier209

    @myDsl_type_qualifier209.setter
    def myDsl_type_qualifier209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier209", None)
        self.__myDsl_type_qualifier209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_list208"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_list208", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_list208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_list208"):
                opp_val = getattr(value, "myDsl_type_qualifier_list208", None)
                setattr(value, "myDsl_type_qualifier_list208", self)

    @property
    def myDsl_type_qualifier214(self):
        return self.__myDsl_type_qualifier214

    @myDsl_type_qualifier214.setter
    def myDsl_type_qualifier214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier214", None)
        self.__myDsl_type_qualifier214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_list2213"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_list2213", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_list2213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_list2213"):
                opp_val = getattr(value, "myDsl_type_qualifier_list2213", None)
                setattr(value, "myDsl_type_qualifier_list2213", self)

class myDsl_declarator:

    pass
class myDsl_declaration_specifiers:

    pass
class myDsl_declaration:

    pass
class myDsl_constant_expression:

    pass
class myDsl_expression2:

    pass
class myDsl_type_specifier:

    def __init__(self, typedef_name: str, myDsl_type_specifier: "myDsl_declaration_specifiers" = None, myDsl_type_specifier131: "myDsl_specifier_qualifier_list" = None, myDsl_type_specifier103: "myDsl_atomic_type_specifier" = None, myDsl_type_specifier105: "myDsl_struct_or_union_specifier" = None, myDsl_type_specifier107: "myDsl_enum_specifier" = None, myDsl_type_specifier137: "myDsl_specifier_qualifier_list" = None):
        self.typedef_name = typedef_name
        self.myDsl_type_specifier = myDsl_type_specifier
        self.myDsl_type_specifier131 = myDsl_type_specifier131
        self.myDsl_type_specifier103 = myDsl_type_specifier103
        self.myDsl_type_specifier105 = myDsl_type_specifier105
        self.myDsl_type_specifier107 = myDsl_type_specifier107
        self.myDsl_type_specifier137 = myDsl_type_specifier137
        
    @property
    def typedef_name(self) -> str:
        return self.__typedef_name

    @typedef_name.setter
    def typedef_name(self, typedef_name: str):
        self.__typedef_name = typedef_name

    @property
    def myDsl_type_specifier(self):
        return self.__myDsl_type_specifier

    @myDsl_type_specifier.setter
    def myDsl_type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier", None)
        self.__myDsl_type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers80"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers80", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers80"):
                opp_val = getattr(value, "myDsl_declaration_specifiers80", None)
                setattr(value, "myDsl_declaration_specifiers80", self)

    @property
    def myDsl_type_specifier107(self):
        return self.__myDsl_type_specifier107

    @myDsl_type_specifier107.setter
    def myDsl_type_specifier107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier107", None)
        self.__myDsl_type_specifier107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_enum_specifier"):
                opp_val = getattr(old_value, "myDsl_enum_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_enum_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_enum_specifier"):
                opp_val = getattr(value, "myDsl_enum_specifier", None)
                setattr(value, "myDsl_enum_specifier", self)

    @property
    def myDsl_type_specifier131(self):
        return self.__myDsl_type_specifier131

    @myDsl_type_specifier131.setter
    def myDsl_type_specifier131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier131", None)
        self.__myDsl_type_specifier131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_specifier_qualifier_list130"):
                opp_val = getattr(old_value, "myDsl_specifier_qualifier_list130", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_specifier_qualifier_list130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_specifier_qualifier_list130"):
                opp_val = getattr(value, "myDsl_specifier_qualifier_list130", None)
                setattr(value, "myDsl_specifier_qualifier_list130", self)

    @property
    def myDsl_type_specifier103(self):
        return self.__myDsl_type_specifier103

    @myDsl_type_specifier103.setter
    def myDsl_type_specifier103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier103", None)
        self.__myDsl_type_specifier103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_atomic_type_specifier"):
                opp_val = getattr(old_value, "myDsl_atomic_type_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_atomic_type_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_atomic_type_specifier"):
                opp_val = getattr(value, "myDsl_atomic_type_specifier", None)
                setattr(value, "myDsl_atomic_type_specifier", self)

    @property
    def myDsl_type_specifier105(self):
        return self.__myDsl_type_specifier105

    @myDsl_type_specifier105.setter
    def myDsl_type_specifier105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier105", None)
        self.__myDsl_type_specifier105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_or_union_specifier"):
                opp_val = getattr(old_value, "myDsl_struct_or_union_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_or_union_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_or_union_specifier"):
                opp_val = getattr(value, "myDsl_struct_or_union_specifier", None)
                setattr(value, "myDsl_struct_or_union_specifier", self)

    @property
    def myDsl_type_specifier137(self):
        return self.__myDsl_type_specifier137

    @myDsl_type_specifier137.setter
    def myDsl_type_specifier137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier137", None)
        self.__myDsl_type_specifier137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_specifier_qualifier_list136"):
                opp_val = getattr(old_value, "myDsl_specifier_qualifier_list136", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_specifier_qualifier_list136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_specifier_qualifier_list136"):
                opp_val = getattr(value, "myDsl_specifier_qualifier_list136", None)
                setattr(value, "myDsl_specifier_qualifier_list136", self)

class myDsl_storage_class_specifier:

    def __init__(self, typedef: str, extern: str, static: str, thread_local: str, auto: str, register: str, myDsl_storage_class_specifier: "myDsl_declaration_specifiers" = None):
        self.typedef = typedef
        self.extern = extern
        self.static = static
        self.thread_local = thread_local
        self.auto = auto
        self.register = register
        self.myDsl_storage_class_specifier = myDsl_storage_class_specifier
        
    @property
    def auto(self) -> str:
        return self.__auto

    @auto.setter
    def auto(self, auto: str):
        self.__auto = auto

    @property
    def register(self) -> str:
        return self.__register

    @register.setter
    def register(self, register: str):
        self.__register = register

    @property
    def thread_local(self) -> str:
        return self.__thread_local

    @thread_local.setter
    def thread_local(self, thread_local: str):
        self.__thread_local = thread_local

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def extern(self) -> str:
        return self.__extern

    @extern.setter
    def extern(self, extern: str):
        self.__extern = extern

    @property
    def typedef(self) -> str:
        return self.__typedef

    @typedef.setter
    def typedef(self, typedef: str):
        self.__typedef = typedef

    @property
    def myDsl_storage_class_specifier(self):
        return self.__myDsl_storage_class_specifier

    @myDsl_storage_class_specifier.setter
    def myDsl_storage_class_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_storage_class_specifier__myDsl_storage_class_specifier", None)
        self.__myDsl_storage_class_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers75"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers75", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers75"):
                opp_val = getattr(value, "myDsl_declaration_specifiers75", None)
                setattr(value, "myDsl_declaration_specifiers75", self)

class myDsl_static_assert_declaration:

    def __init__(self, static_assert: str, string_literal: str, myDsl_static_assert_declaration: "myDsl_declaration" = None, myDsl_static_assert_declaration128: "myDsl_struct_declaration" = None, myDsl_static_assert_declaration302: "myDsl_constant_expression" = None):
        self.static_assert = static_assert
        self.string_literal = string_literal
        self.myDsl_static_assert_declaration = myDsl_static_assert_declaration
        self.myDsl_static_assert_declaration128 = myDsl_static_assert_declaration128
        self.myDsl_static_assert_declaration302 = myDsl_static_assert_declaration302
        
    @property
    def static_assert(self) -> str:
        return self.__static_assert

    @static_assert.setter
    def static_assert(self, static_assert: str):
        self.__static_assert = static_assert

    @property
    def string_literal(self) -> str:
        return self.__string_literal

    @string_literal.setter
    def string_literal(self, string_literal: str):
        self.__string_literal = string_literal

    @property
    def myDsl_static_assert_declaration(self):
        return self.__myDsl_static_assert_declaration

    @myDsl_static_assert_declaration.setter
    def myDsl_static_assert_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_static_assert_declaration__myDsl_static_assert_declaration", None)
        self.__myDsl_static_assert_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration73"):
                opp_val = getattr(old_value, "myDsl_declaration73", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration73"):
                opp_val = getattr(value, "myDsl_declaration73", None)
                setattr(value, "myDsl_declaration73", self)

    @property
    def myDsl_static_assert_declaration128(self):
        return self.__myDsl_static_assert_declaration128

    @myDsl_static_assert_declaration128.setter
    def myDsl_static_assert_declaration128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_static_assert_declaration__myDsl_static_assert_declaration128", None)
        self.__myDsl_static_assert_declaration128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_declaration127"):
                opp_val = getattr(old_value, "myDsl_struct_declaration127", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_declaration127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_declaration127"):
                opp_val = getattr(value, "myDsl_struct_declaration127", None)
                setattr(value, "myDsl_struct_declaration127", self)

    @property
    def myDsl_static_assert_declaration302(self):
        return self.__myDsl_static_assert_declaration302

    @myDsl_static_assert_declaration302.setter
    def myDsl_static_assert_declaration302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_static_assert_declaration__myDsl_static_assert_declaration302", None)
        self.__myDsl_static_assert_declaration302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_constant_expression303"):
                opp_val = getattr(old_value, "myDsl_constant_expression303", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_constant_expression303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_constant_expression303"):
                opp_val = getattr(value, "myDsl_constant_expression303", None)
                setattr(value, "myDsl_constant_expression303", self)

class myDsl_init_declarator_list:

    pass
class myDsl_conditional_expression:

    pass
class simple_expression:

    pass
class myDsl_MINUS(simple_expression):

    pass
class myDsl_REL(simple_expression):

    def __init__(self, op: str, myDsl_REL: "myDsl_simple_expression" = None, myDsl_REL411: "myDsl_simple_expression" = None):
        self.op = op
        self.myDsl_REL = myDsl_REL
        self.myDsl_REL411 = myDsl_REL411
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_REL(self):
        return self.__myDsl_REL

    @myDsl_REL.setter
    def myDsl_REL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_REL__myDsl_REL", None)
        self.__myDsl_REL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression409"):
                opp_val = getattr(old_value, "myDsl_simple_expression409", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression409"):
                opp_val = getattr(value, "myDsl_simple_expression409", None)
                setattr(value, "myDsl_simple_expression409", self)

    @property
    def myDsl_REL411(self):
        return self.__myDsl_REL411

    @myDsl_REL411.setter
    def myDsl_REL411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_REL__myDsl_REL411", None)
        self.__myDsl_REL411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression412"):
                opp_val = getattr(old_value, "myDsl_simple_expression412", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression412"):
                opp_val = getattr(value, "myDsl_simple_expression412", None)
                setattr(value, "myDsl_simple_expression412", self)

class myDsl_AND(simple_expression):

    pass
class myDsl_LOG_AND(simple_expression):

    pass
class myDsl_ADD(simple_expression):

    pass
class myDsl_MUL(simple_expression):

    def __init__(self, op: str, myDsl_MUL: "myDsl_simple_expression" = None, myDsl_MUL391: "myDsl_simple_expression" = None):
        self.op = op
        self.myDsl_MUL = myDsl_MUL
        self.myDsl_MUL391 = myDsl_MUL391
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_MUL(self):
        return self.__myDsl_MUL

    @myDsl_MUL.setter
    def myDsl_MUL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MUL__myDsl_MUL", None)
        self.__myDsl_MUL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression389"):
                opp_val = getattr(old_value, "myDsl_simple_expression389", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression389"):
                opp_val = getattr(value, "myDsl_simple_expression389", None)
                setattr(value, "myDsl_simple_expression389", self)

    @property
    def myDsl_MUL391(self):
        return self.__myDsl_MUL391

    @myDsl_MUL391.setter
    def myDsl_MUL391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MUL__myDsl_MUL391", None)
        self.__myDsl_MUL391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression392"):
                opp_val = getattr(old_value, "myDsl_simple_expression392", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression392"):
                opp_val = getattr(value, "myDsl_simple_expression392", None)
                setattr(value, "myDsl_simple_expression392", self)

class myDsl_booleanType(type_specifier, simple_expression):

    def __init__(self, value: str, bool_type: str):
        self.value = value
        self.bool_type = bool_type
        
    @property
    def bool_type(self) -> str:
        return self.__bool_type

    @bool_type.setter
    def bool_type(self, bool_type: str):
        self.__bool_type = bool_type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class myDsl_SHF(simple_expression):

    def __init__(self, op: str, myDsl_SHF: "myDsl_simple_expression" = None, myDsl_SHF406: "myDsl_simple_expression" = None):
        self.op = op
        self.myDsl_SHF = myDsl_SHF
        self.myDsl_SHF406 = myDsl_SHF406
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_SHF(self):
        return self.__myDsl_SHF

    @myDsl_SHF.setter
    def myDsl_SHF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SHF__myDsl_SHF", None)
        self.__myDsl_SHF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression404"):
                opp_val = getattr(old_value, "myDsl_simple_expression404", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression404"):
                opp_val = getattr(value, "myDsl_simple_expression404", None)
                setattr(value, "myDsl_simple_expression404", self)

    @property
    def myDsl_SHF406(self):
        return self.__myDsl_SHF406

    @myDsl_SHF406.setter
    def myDsl_SHF406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SHF__myDsl_SHF406", None)
        self.__myDsl_SHF406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression407"):
                opp_val = getattr(old_value, "myDsl_simple_expression407", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression407"):
                opp_val = getattr(value, "myDsl_simple_expression407", None)
                setattr(value, "myDsl_simple_expression407", self)

class myDsl_stringType(simple_expression):

    pass
class myDsl_floatType(type_specifier, simple_expression):

    def __init__(self, value: str, float_type: str):
        self.value = value
        self.float_type = float_type
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def float_type(self) -> str:
        return self.__float_type

    @float_type.setter
    def float_type(self, float_type: str):
        self.__float_type = float_type

class myDsl_variableRef(simple_expression):

    def __init__(self, variable: str):
        self.variable = variable
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class myDsl_INC_OR(simple_expression):

    pass
class myDsl_LOG_OR(simple_expression):

    pass
class myDsl_EQL(simple_expression):

    def __init__(self, op: str, myDsl_EQL: "myDsl_simple_expression" = None, myDsl_EQL416: "myDsl_simple_expression" = None):
        self.op = op
        self.myDsl_EQL = myDsl_EQL
        self.myDsl_EQL416 = myDsl_EQL416
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_EQL416(self):
        return self.__myDsl_EQL416

    @myDsl_EQL416.setter
    def myDsl_EQL416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EQL__myDsl_EQL416", None)
        self.__myDsl_EQL416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression417"):
                opp_val = getattr(old_value, "myDsl_simple_expression417", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression417"):
                opp_val = getattr(value, "myDsl_simple_expression417", None)
                setattr(value, "myDsl_simple_expression417", self)

    @property
    def myDsl_EQL(self):
        return self.__myDsl_EQL

    @myDsl_EQL.setter
    def myDsl_EQL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EQL__myDsl_EQL", None)
        self.__myDsl_EQL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_simple_expression414"):
                opp_val = getattr(old_value, "myDsl_simple_expression414", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_simple_expression414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_simple_expression414"):
                opp_val = getattr(value, "myDsl_simple_expression414", None)
                setattr(value, "myDsl_simple_expression414", self)

class myDsl_intType(type_specifier, simple_expression):

    def __init__(self, value: str, int_type: str):
        self.value = value
        self.int_type = int_type
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def int_type(self) -> str:
        return self.__int_type

    @int_type.setter
    def int_type(self, int_type: str):
        self.__int_type = int_type

class myDsl_EXC_OR(simple_expression):

    pass
class myDsl_unary_expression(simple_expression):

    def __init__(self, inc_op: str, dec_op: str, unary_operator: str, sizeof: str, alignof: str, myDsl_unary_expression53: "myDsl_assignment_expression" = None, myDsl_unary_expression: "myDsl_postfix_expression" = None, myDsl_unary_expression37: "myDsl_unary_expression" = None, myDsl_unary_expression35: "myDsl_unary_expression" = None):
        self.inc_op = inc_op
        self.dec_op = dec_op
        self.unary_operator = unary_operator
        self.sizeof = sizeof
        self.alignof = alignof
        self.myDsl_unary_expression53 = myDsl_unary_expression53
        self.myDsl_unary_expression = myDsl_unary_expression
        self.myDsl_unary_expression37 = myDsl_unary_expression37
        self.myDsl_unary_expression35 = myDsl_unary_expression35
        
    @property
    def inc_op(self) -> str:
        return self.__inc_op

    @inc_op.setter
    def inc_op(self, inc_op: str):
        self.__inc_op = inc_op

    @property
    def dec_op(self) -> str:
        return self.__dec_op

    @dec_op.setter
    def dec_op(self, dec_op: str):
        self.__dec_op = dec_op

    @property
    def unary_operator(self) -> str:
        return self.__unary_operator

    @unary_operator.setter
    def unary_operator(self, unary_operator: str):
        self.__unary_operator = unary_operator

    @property
    def sizeof(self) -> str:
        return self.__sizeof

    @sizeof.setter
    def sizeof(self, sizeof: str):
        self.__sizeof = sizeof

    @property
    def alignof(self) -> str:
        return self.__alignof

    @alignof.setter
    def alignof(self, alignof: str):
        self.__alignof = alignof

    @property
    def myDsl_unary_expression35(self):
        return self.__myDsl_unary_expression35

    @myDsl_unary_expression35.setter
    def myDsl_unary_expression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression35", None)
        self.__myDsl_unary_expression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression37"):
                opp_val = getattr(old_value, "myDsl_unary_expression37", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression37"):
                opp_val = getattr(value, "myDsl_unary_expression37", None)
                setattr(value, "myDsl_unary_expression37", self)

    @property
    def myDsl_unary_expression(self):
        return self.__myDsl_unary_expression

    @myDsl_unary_expression.setter
    def myDsl_unary_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression", None)
        self.__myDsl_unary_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_postfix_expression34"):
                opp_val = getattr(old_value, "myDsl_postfix_expression34", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_postfix_expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_postfix_expression34"):
                opp_val = getattr(value, "myDsl_postfix_expression34", None)
                setattr(value, "myDsl_postfix_expression34", self)

    @property
    def myDsl_unary_expression53(self):
        return self.__myDsl_unary_expression53

    @myDsl_unary_expression53.setter
    def myDsl_unary_expression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression53", None)
        self.__myDsl_unary_expression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression52"):
                opp_val = getattr(old_value, "myDsl_assignment_expression52", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression52"):
                opp_val = getattr(value, "myDsl_assignment_expression52", None)
                setattr(value, "myDsl_assignment_expression52", self)

    @property
    def myDsl_unary_expression37(self):
        return self.__myDsl_unary_expression37

    @myDsl_unary_expression37.setter
    def myDsl_unary_expression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression37", None)
        self.__myDsl_unary_expression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression35"):
                opp_val = getattr(old_value, "myDsl_unary_expression35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression35"):
                opp_val = getattr(value, "myDsl_unary_expression35", None)
                setattr(value, "myDsl_unary_expression35", self)

class postfix_expression2:

    pass
class myDsl_argument_expression_list(postfix_expression2):

    pass
class myDsl_initializer_list:

    pass
class myDsl_postfix_expression2:

    pass
class myDsl_postfix_expression:

    pass
class myDsl_assignment_operator:

    def __init__(self, mul_assign: str, div_assign: str, mod_assign: str, add_assign: str, sub_assign: str, left_assign: str, right_assign: str, and_assign: str, xor_assign: str, or_assign: str, myDsl_assignment_operator: "myDsl_assignment_expression" = None):
        self.mul_assign = mul_assign
        self.div_assign = div_assign
        self.mod_assign = mod_assign
        self.add_assign = add_assign
        self.sub_assign = sub_assign
        self.left_assign = left_assign
        self.right_assign = right_assign
        self.and_assign = and_assign
        self.xor_assign = xor_assign
        self.or_assign = or_assign
        self.myDsl_assignment_operator = myDsl_assignment_operator
        
    @property
    def mul_assign(self) -> str:
        return self.__mul_assign

    @mul_assign.setter
    def mul_assign(self, mul_assign: str):
        self.__mul_assign = mul_assign

    @property
    def div_assign(self) -> str:
        return self.__div_assign

    @div_assign.setter
    def div_assign(self, div_assign: str):
        self.__div_assign = div_assign

    @property
    def add_assign(self) -> str:
        return self.__add_assign

    @add_assign.setter
    def add_assign(self, add_assign: str):
        self.__add_assign = add_assign

    @property
    def mod_assign(self) -> str:
        return self.__mod_assign

    @mod_assign.setter
    def mod_assign(self, mod_assign: str):
        self.__mod_assign = mod_assign

    @property
    def left_assign(self) -> str:
        return self.__left_assign

    @left_assign.setter
    def left_assign(self, left_assign: str):
        self.__left_assign = left_assign

    @property
    def or_assign(self) -> str:
        return self.__or_assign

    @or_assign.setter
    def or_assign(self, or_assign: str):
        self.__or_assign = or_assign

    @property
    def right_assign(self) -> str:
        return self.__right_assign

    @right_assign.setter
    def right_assign(self, right_assign: str):
        self.__right_assign = right_assign

    @property
    def sub_assign(self) -> str:
        return self.__sub_assign

    @sub_assign.setter
    def sub_assign(self, sub_assign: str):
        self.__sub_assign = sub_assign

    @property
    def and_assign(self) -> str:
        return self.__and_assign

    @and_assign.setter
    def and_assign(self, and_assign: str):
        self.__and_assign = and_assign

    @property
    def xor_assign(self) -> str:
        return self.__xor_assign

    @xor_assign.setter
    def xor_assign(self, xor_assign: str):
        self.__xor_assign = xor_assign

    @property
    def myDsl_assignment_operator(self):
        return self.__myDsl_assignment_operator

    @myDsl_assignment_operator.setter
    def myDsl_assignment_operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_operator__myDsl_assignment_operator", None)
        self.__myDsl_assignment_operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression55"):
                opp_val = getattr(old_value, "myDsl_assignment_expression55", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression55"):
                opp_val = getattr(value, "myDsl_assignment_expression55", None)
                setattr(value, "myDsl_assignment_expression55", self)

class myDsl_assignment_expression:

    pass
class myDsl_generic_selection:

    def __init__(self, generic: str, myDsl_generic_selection7: "myDsl_generic_assoc_list" = None, myDsl_generic_selection: "myDsl_assignment_expression" = None):
        self.generic = generic
        self.myDsl_generic_selection7 = myDsl_generic_selection7
        self.myDsl_generic_selection = myDsl_generic_selection
        
    @property
    def generic(self) -> str:
        return self.__generic

    @generic.setter
    def generic(self, generic: str):
        self.__generic = generic

    @property
    def myDsl_generic_selection(self):
        return self.__myDsl_generic_selection

    @myDsl_generic_selection.setter
    def myDsl_generic_selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_selection__myDsl_generic_selection", None)
        self.__myDsl_generic_selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression"):
                opp_val = getattr(old_value, "myDsl_assignment_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression"):
                opp_val = getattr(value, "myDsl_assignment_expression", None)
                setattr(value, "myDsl_assignment_expression", self)

    @property
    def myDsl_generic_selection7(self):
        return self.__myDsl_generic_selection7

    @myDsl_generic_selection7.setter
    def myDsl_generic_selection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_selection__myDsl_generic_selection7", None)
        self.__myDsl_generic_selection7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_assoc_list"):
                opp_val = getattr(old_value, "myDsl_generic_assoc_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_assoc_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_assoc_list"):
                opp_val = getattr(value, "myDsl_generic_assoc_list", None)
                setattr(value, "myDsl_generic_assoc_list", self)

class myDsl_expression(postfix_expression2):

    pass
class myDsl_string_nova:

    def __init__(self, string_literal: str, func_name: str, myDsl_string_nova: "myDsl_stringType" = None):
        self.string_literal = string_literal
        self.func_name = func_name
        self.myDsl_string_nova = myDsl_string_nova
        
    @property
    def func_name(self) -> str:
        return self.__func_name

    @func_name.setter
    def func_name(self, func_name: str):
        self.__func_name = func_name

    @property
    def string_literal(self) -> str:
        return self.__string_literal

    @string_literal.setter
    def string_literal(self, string_literal: str):
        self.__string_literal = string_literal

    @property
    def myDsl_string_nova(self):
        return self.__myDsl_string_nova

    @myDsl_string_nova.setter
    def myDsl_string_nova(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_string_nova__myDsl_string_nova", None)
        self.__myDsl_string_nova = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_stringType"):
                opp_val = getattr(old_value, "myDsl_stringType", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_stringType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_stringType"):
                opp_val = getattr(value, "myDsl_stringType", None)
                setattr(value, "myDsl_stringType", self)

class myDsl_enumeration_constant:

    def __init__(self, identifier: str, myDsl_enumeration_constant: "myDsl_enumerator" = None):
        self.identifier = identifier
        self.myDsl_enumeration_constant = myDsl_enumeration_constant
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_enumeration_constant(self):
        return self.__myDsl_enumeration_constant

    @myDsl_enumeration_constant.setter
    def myDsl_enumeration_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_enumeration_constant__myDsl_enumeration_constant", None)
        self.__myDsl_enumeration_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_enumerator167"):
                opp_val = getattr(old_value, "myDsl_enumerator167", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_enumerator167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_enumerator167"):
                opp_val = getattr(value, "myDsl_enumerator167", None)
                setattr(value, "myDsl_enumerator167", self)

class myDsl_constant:

    def __init__(self, i_constant: str, f_constant: str, enumt: str):
        self.i_constant = i_constant
        self.f_constant = f_constant
        self.enumt = enumt
        
    @property
    def i_constant(self) -> str:
        return self.__i_constant

    @i_constant.setter
    def i_constant(self, i_constant: str):
        self.__i_constant = i_constant

    @property
    def enumt(self) -> str:
        return self.__enumt

    @enumt.setter
    def enumt(self, enumt: str):
        self.__enumt = enumt

    @property
    def f_constant(self) -> str:
        return self.__f_constant

    @f_constant.setter
    def f_constant(self, f_constant: str):
        self.__f_constant = f_constant

class myDsl_type_name:

    pass
class myDsl_simple_expression:

    pass
class myDsl_translation_unit:

    pass
class myDsl_Model:

    pass
class myDsl_generic_association:

    def __init__(self, default: str, myDsl_generic_association: "myDsl_generic_assoc_list" = None, myDsl_generic_association12: "myDsl_generic_assoc_list" = None, myDsl_generic_association14: "myDsl_type_name" = None, myDsl_generic_association17: "myDsl_assignment_expression" = None):
        self.default = default
        self.myDsl_generic_association = myDsl_generic_association
        self.myDsl_generic_association12 = myDsl_generic_association12
        self.myDsl_generic_association14 = myDsl_generic_association14
        self.myDsl_generic_association17 = myDsl_generic_association17
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def myDsl_generic_association(self):
        return self.__myDsl_generic_association

    @myDsl_generic_association.setter
    def myDsl_generic_association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association", None)
        self.__myDsl_generic_association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_assoc_list9"):
                opp_val = getattr(old_value, "myDsl_generic_assoc_list9", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_assoc_list9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_assoc_list9"):
                opp_val = getattr(value, "myDsl_generic_assoc_list9", None)
                setattr(value, "myDsl_generic_assoc_list9", self)

    @property
    def myDsl_generic_association17(self):
        return self.__myDsl_generic_association17

    @myDsl_generic_association17.setter
    def myDsl_generic_association17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association17", None)
        self.__myDsl_generic_association17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression18"):
                opp_val = getattr(old_value, "myDsl_assignment_expression18", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression18"):
                opp_val = getattr(value, "myDsl_assignment_expression18", None)
                setattr(value, "myDsl_assignment_expression18", self)

    @property
    def myDsl_generic_association12(self):
        return self.__myDsl_generic_association12

    @myDsl_generic_association12.setter
    def myDsl_generic_association12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association12", None)
        self.__myDsl_generic_association12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_assoc_list11"):
                opp_val = getattr(old_value, "myDsl_generic_assoc_list11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_assoc_list11"):
                opp_val = getattr(value, "myDsl_generic_assoc_list11", None)
                if opp_val is None:
                    setattr(value, "myDsl_generic_assoc_list11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_generic_association14(self):
        return self.__myDsl_generic_association14

    @myDsl_generic_association14.setter
    def myDsl_generic_association14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association14", None)
        self.__myDsl_generic_association14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_name15"):
                opp_val = getattr(old_value, "myDsl_type_name15", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_name15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_name15"):
                opp_val = getattr(value, "myDsl_type_name15", None)
                setattr(value, "myDsl_type_name15", self)

class myDsl_generic_assoc_list:

    pass
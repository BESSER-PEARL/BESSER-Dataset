from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class declaration_specifiers:

    pass
class myDsl_EObject:

    pass
class postfix_expressionR:

    pass
class struct_or_union_specifier:

    pass
class labeled_statement:

    pass
class identifier_listR:

    pass
class identifier_list:

    pass
class direct_declarator:

    pass
class abstract_declarator:

    pass
class myDsl_argument_expression_listR:

    pass
class myDsl_argument_expression_list:

    pass
class myDsl_struct_declarator_listR:

    pass
class myDsl_struct_declarator:

    pass
class myDsl_struct_declarator_list:

    pass
class type_specifier:

    pass
class myDsl_atomic_type_specifier(type_specifier):

    pass
class myDsl_struct_or_union_specifier(type_specifier):

    def __init__(self, Struct_or_union: str, myDsl_struct_or_union_specifier: "myDsl_struct_declaration_list" = None, myDsl_struct_or_union_specifier323: "myDsl_IDENTIFIER" = None):
        self.Struct_or_union = Struct_or_union
        self.myDsl_struct_or_union_specifier = myDsl_struct_or_union_specifier
        self.myDsl_struct_or_union_specifier323 = myDsl_struct_or_union_specifier323
        
    @property
    def Struct_or_union(self) -> str:
        return self.__Struct_or_union

    @Struct_or_union.setter
    def Struct_or_union(self, Struct_or_union: str):
        self.__Struct_or_union = Struct_or_union

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
            if hasattr(old_value, "myDsl_struct_declaration_list321"):
                opp_val = getattr(old_value, "myDsl_struct_declaration_list321", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_declaration_list321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_declaration_list321"):
                opp_val = getattr(value, "myDsl_struct_declaration_list321", None)
                setattr(value, "myDsl_struct_declaration_list321", self)

    @property
    def myDsl_struct_or_union_specifier323(self):
        return self.__myDsl_struct_or_union_specifier323

    @myDsl_struct_or_union_specifier323.setter
    def myDsl_struct_or_union_specifier323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier323", None)
        self.__myDsl_struct_or_union_specifier323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IDENTIFIER"):
                opp_val = getattr(old_value, "myDsl_IDENTIFIER", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IDENTIFIER", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IDENTIFIER"):
                opp_val = getattr(value, "myDsl_IDENTIFIER", None)
                setattr(value, "myDsl_IDENTIFIER", self)

class declaration:

    pass
class myDsl_struct_declaration_listR:

    pass
class myDsl_struct_declaration:

    pass
class myDsl_struct_declaration_list:

    pass
class myDsl_initializer_listR:

    pass
class myDsl_type_specifier(declaration_specifiers):

    pass
class struct_declaration:

    pass
class myDsl_static_assert_declaration(declaration, struct_declaration):

    pass
class type_name:

    pass
class myDsl_specifier_qualifier_list(type_name, struct_declaration):

    pass
class atomic_type_specifier:

    pass
class static_assert_declaration:

    pass
class designator:

    pass
class myDsl_designator_listR:

    pass
class myDsl_designator:

    pass
class designation:

    pass
class myDsl_designator_list(designation):

    pass
class myDsl_cast_expression:

    pass
class myDsl_multiplicative_expressionR:

    pass
class myDsl_designation:

    pass
class myDsl_postfix_expressionR:

    pass
class myDsl_primary_expression:

    pass
class unary_expression:

    pass
class myDsl_postfix_expression(unary_expression):

    pass
class cast_expression:

    pass
class myDsl_type_name(atomic_type_specifier):

    pass
class myDsl_unary_expression(cast_expression):

    def __init__(self, Unary_operator: str, myDsl_unary_expression: "myDsl_assignment_expression" = None, myDsl_unary_expression245: "myDsl_cast_expression" = None):
        self.Unary_operator = Unary_operator
        self.myDsl_unary_expression = myDsl_unary_expression
        self.myDsl_unary_expression245 = myDsl_unary_expression245
        
    @property
    def Unary_operator(self) -> str:
        return self.__Unary_operator

    @Unary_operator.setter
    def Unary_operator(self, Unary_operator: str):
        self.__Unary_operator = Unary_operator

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
            if hasattr(old_value, "myDsl_assignment_expression235"):
                opp_val = getattr(old_value, "myDsl_assignment_expression235", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression235"):
                opp_val = getattr(value, "myDsl_assignment_expression235", None)
                setattr(value, "myDsl_assignment_expression235", self)

    @property
    def myDsl_unary_expression245(self):
        return self.__myDsl_unary_expression245

    @myDsl_unary_expression245.setter
    def myDsl_unary_expression245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression245", None)
        self.__myDsl_unary_expression245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_cast_expression246"):
                opp_val = getattr(old_value, "myDsl_cast_expression246", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_cast_expression246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_cast_expression246"):
                opp_val = getattr(value, "myDsl_cast_expression246", None)
                setattr(value, "myDsl_cast_expression246", self)

class initializer:

    pass
class myDsl_initializer_list(initializer):

    pass
class myDsl_equality_expressionR:

    pass
class myDsl_relational_expression:

    pass
class myDsl_additive_expressionR:

    pass
class myDsl_multiplicative_expression:

    pass
class shift_expression:

    pass
class myDsl_additive_expression(shift_expression):

    pass
class myDsl_shift_expressionR:

    pass
class myDsl_relational_expressionR:

    pass
class myDsl_shift_expression:

    pass
class myDsl_logical_and_expressionR:

    pass
class myDsl_inclusive_or_expression:

    pass
class myDsl_equality_expression:

    pass
class myDsl_and_expressionR:

    pass
class myDsl_exclusive_or_expressionR:

    pass
class myDsl_and_expression:

    pass
class myDsl_inclusive_or_expressionR:

    pass
class myDsl_exclusive_or_expression:

    pass
class myDsl_logical_or_expressionR:

    pass
class myDsl_logical_and_expression:

    pass
class conditional_expression:

    pass
class myDsl_logical_or_expression(conditional_expression):

    pass
class constant_expression:

    pass
class assignment_expression:

    pass
class myDsl_conditional_expression(assignment_expression, constant_expression):

    pass
class myDsl_expressionR:

    pass
class primary_expression:

    pass
class myDsl_StringC(primary_expression):

    def __init__(self, string: str):
        self.string = string
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

class expression_statement:

    pass
class jump_statement:

    pass
class myDsl_IDENTIFIER(designator, labeled_statement, primary_expression, direct_declarator, identifier_list, identifier_listR, struct_or_union_specifier, jump_statement, postfix_expressionR):

    def __init__(self, name: str, myDsl_IDENTIFIER349: "myDsl_direct_declaratorR" = None, myDsl_IDENTIFIER352: "myDsl_identifier_listR" = None, myDsl_IDENTIFIER: "myDsl_struct_or_union_specifier" = None, myDsl_IDENTIFIER354: "myDsl_statement" = None):
        self.name = name
        self.myDsl_IDENTIFIER349 = myDsl_IDENTIFIER349
        self.myDsl_IDENTIFIER352 = myDsl_IDENTIFIER352
        self.myDsl_IDENTIFIER = myDsl_IDENTIFIER
        self.myDsl_IDENTIFIER354 = myDsl_IDENTIFIER354
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_IDENTIFIER352(self):
        return self.__myDsl_IDENTIFIER352

    @myDsl_IDENTIFIER352.setter
    def myDsl_IDENTIFIER352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IDENTIFIER__myDsl_IDENTIFIER352", None)
        self.__myDsl_IDENTIFIER352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_listR"):
                opp_val = getattr(old_value, "myDsl_identifier_listR", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_listR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_listR"):
                opp_val = getattr(value, "myDsl_identifier_listR", None)
                setattr(value, "myDsl_identifier_listR", self)

    @property
    def myDsl_IDENTIFIER354(self):
        return self.__myDsl_IDENTIFIER354

    @myDsl_IDENTIFIER354.setter
    def myDsl_IDENTIFIER354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IDENTIFIER__myDsl_IDENTIFIER354", None)
        self.__myDsl_IDENTIFIER354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement355"):
                opp_val = getattr(old_value, "myDsl_statement355", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement355"):
                opp_val = getattr(value, "myDsl_statement355", None)
                setattr(value, "myDsl_statement355", self)

    @property
    def myDsl_IDENTIFIER(self):
        return self.__myDsl_IDENTIFIER

    @myDsl_IDENTIFIER.setter
    def myDsl_IDENTIFIER(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IDENTIFIER__myDsl_IDENTIFIER", None)
        self.__myDsl_IDENTIFIER = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_or_union_specifier323"):
                opp_val = getattr(old_value, "myDsl_struct_or_union_specifier323", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_or_union_specifier323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_or_union_specifier323"):
                opp_val = getattr(value, "myDsl_struct_or_union_specifier323", None)
                setattr(value, "myDsl_struct_or_union_specifier323", self)

    @property
    def myDsl_IDENTIFIER349(self):
        return self.__myDsl_IDENTIFIER349

    @myDsl_IDENTIFIER349.setter
    def myDsl_IDENTIFIER349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IDENTIFIER__myDsl_IDENTIFIER349", None)
        self.__myDsl_IDENTIFIER349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declaratorR350"):
                opp_val = getattr(old_value, "myDsl_direct_declaratorR350", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declaratorR350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declaratorR350"):
                opp_val = getattr(value, "myDsl_direct_declaratorR350", None)
                setattr(value, "myDsl_direct_declaratorR350", self)

class parameter_declaration:

    pass
class myDsl_initializer:

    pass
class myDsl_init_declarator_listR:

    pass
class myDsl_init_declarator:

    pass
class myDsl_init_declarator_list:

    pass
class myDsl_expression(expression_statement, primary_expression, jump_statement):

    pass
class myDsl_parameter_listR:

    pass
class block_item:

    pass
class myDsl_statement(block_item):

    pass
class myDsl_block_item_listR:

    pass
class myDsl_block_item:

    pass
class compound_statement:

    pass
class myDsl_block_item_list(compound_statement):

    pass
class statement:

    pass
class myDsl_expression_statement(statement):

    pass
class myDsl_labeled_statement(statement):

    pass
class myDsl_jump_statement(statement):

    pass
class myDsl_iteration_statement(statement):

    pass
class myDsl_selection_statement(statement):

    pass
class myDsl_declaration_listR:

    pass
class myDsl_abstract_declarator:

    pass
class myDsl_pointer(abstract_declarator):

    pass
class struct_declarator:

    pass
class myDsl_constant_expression(designator, struct_declarator, static_assert_declaration):

    pass
class init_declarator:

    pass
class myDsl_compound_statement(statement):

    pass
class myDsl_declaration_list:

    pass
class myDsl_declarator(struct_declarator, init_declarator):

    pass
class myDsl_parameter_declaration:

    pass
class parameter_type_list:

    pass
class myDsl_parameter_list(parameter_type_list):

    pass
class myDsl_identifier_listR:

    pass
class myDsl_identifier_list:

    pass
class myDsl_parameter_type_list:

    pass
class myDsl_assignment_expression(initializer):

    def __init__(self, Assignment_operator: str, myDsl_assignment_expression: "myDsl_direct_declaratorR" = None, myDsl_assignment_expression124: "myDsl_expression" = None, myDsl_assignment_expression129: "myDsl_expressionR" = None, myDsl_assignment_expression235: "myDsl_unary_expression" = None, myDsl_assignment_expression238: "myDsl_assignment_expression" = None, myDsl_assignment_expression236: set["myDsl_assignment_expression"] = None, myDsl_assignment_expression333: "myDsl_argument_expression_list" = None, myDsl_assignment_expression338: "myDsl_argument_expression_listR" = None):
        self.Assignment_operator = Assignment_operator
        self.myDsl_assignment_expression = myDsl_assignment_expression
        self.myDsl_assignment_expression124 = myDsl_assignment_expression124
        self.myDsl_assignment_expression129 = myDsl_assignment_expression129
        self.myDsl_assignment_expression235 = myDsl_assignment_expression235
        self.myDsl_assignment_expression238 = myDsl_assignment_expression238
        self.myDsl_assignment_expression236 = myDsl_assignment_expression236 if myDsl_assignment_expression236 is not None else set()
        self.myDsl_assignment_expression333 = myDsl_assignment_expression333
        self.myDsl_assignment_expression338 = myDsl_assignment_expression338
        
    @property
    def Assignment_operator(self) -> str:
        return self.__Assignment_operator

    @Assignment_operator.setter
    def Assignment_operator(self, Assignment_operator: str):
        self.__Assignment_operator = Assignment_operator

    @property
    def myDsl_assignment_expression129(self):
        return self.__myDsl_assignment_expression129

    @myDsl_assignment_expression129.setter
    def myDsl_assignment_expression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression129", None)
        self.__myDsl_assignment_expression129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expressionR128"):
                opp_val = getattr(old_value, "myDsl_expressionR128", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expressionR128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expressionR128"):
                opp_val = getattr(value, "myDsl_expressionR128", None)
                setattr(value, "myDsl_expressionR128", self)

    @property
    def myDsl_assignment_expression338(self):
        return self.__myDsl_assignment_expression338

    @myDsl_assignment_expression338.setter
    def myDsl_assignment_expression338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression338", None)
        self.__myDsl_assignment_expression338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_argument_expression_listR337"):
                opp_val = getattr(old_value, "myDsl_argument_expression_listR337", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_argument_expression_listR337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_argument_expression_listR337"):
                opp_val = getattr(value, "myDsl_argument_expression_listR337", None)
                setattr(value, "myDsl_argument_expression_listR337", self)

    @property
    def myDsl_assignment_expression(self):
        return self.__myDsl_assignment_expression

    @myDsl_assignment_expression.setter
    def myDsl_assignment_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression", None)
        self.__myDsl_assignment_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declaratorR35"):
                opp_val = getattr(old_value, "myDsl_direct_declaratorR35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declaratorR35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declaratorR35"):
                opp_val = getattr(value, "myDsl_direct_declaratorR35", None)
                setattr(value, "myDsl_direct_declaratorR35", self)

    @property
    def myDsl_assignment_expression236(self):
        return self.__myDsl_assignment_expression236

    @myDsl_assignment_expression236.setter
    def myDsl_assignment_expression236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression236", None)
        self.__myDsl_assignment_expression236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_assignment_expression238"):
                    opp_val = getattr(item, "myDsl_assignment_expression238", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_assignment_expression238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_assignment_expression238"):
                    opp_val = getattr(item, "myDsl_assignment_expression238", None)
                    
                    setattr(item, "myDsl_assignment_expression238", self)
                    

    @property
    def myDsl_assignment_expression235(self):
        return self.__myDsl_assignment_expression235

    @myDsl_assignment_expression235.setter
    def myDsl_assignment_expression235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression235", None)
        self.__myDsl_assignment_expression235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression"):
                opp_val = getattr(old_value, "myDsl_unary_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression"):
                opp_val = getattr(value, "myDsl_unary_expression", None)
                setattr(value, "myDsl_unary_expression", self)

    @property
    def myDsl_assignment_expression238(self):
        return self.__myDsl_assignment_expression238

    @myDsl_assignment_expression238.setter
    def myDsl_assignment_expression238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression238", None)
        self.__myDsl_assignment_expression238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression236"):
                opp_val = getattr(old_value, "myDsl_assignment_expression236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression236"):
                opp_val = getattr(value, "myDsl_assignment_expression236", None)
                if opp_val is None:
                    setattr(value, "myDsl_assignment_expression236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_assignment_expression333(self):
        return self.__myDsl_assignment_expression333

    @myDsl_assignment_expression333.setter
    def myDsl_assignment_expression333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression333", None)
        self.__myDsl_assignment_expression333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_argument_expression_list332"):
                opp_val = getattr(old_value, "myDsl_argument_expression_list332", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_argument_expression_list332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_argument_expression_list332"):
                opp_val = getattr(value, "myDsl_argument_expression_list332", None)
                setattr(value, "myDsl_argument_expression_list332", self)

    @property
    def myDsl_assignment_expression124(self):
        return self.__myDsl_assignment_expression124

    @myDsl_assignment_expression124.setter
    def myDsl_assignment_expression124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression124", None)
        self.__myDsl_assignment_expression124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression123"):
                opp_val = getattr(old_value, "myDsl_expression123", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression123"):
                opp_val = getattr(value, "myDsl_expression123", None)
                setattr(value, "myDsl_expression123", self)

class myDsl_direct_declaratorR:

    pass
class declarator:

    pass
class myDsl_type_qualifier_listR:

    def __init__(self, Type_qualifier: str, myDsl_type_qualifier_listR: "myDsl_type_qualifier_list" = None, myDsl_type_qualifier_listR25: "myDsl_type_qualifier_listR" = None, myDsl_type_qualifier_listR23: set["myDsl_type_qualifier_listR"] = None):
        self.Type_qualifier = Type_qualifier
        self.myDsl_type_qualifier_listR = myDsl_type_qualifier_listR
        self.myDsl_type_qualifier_listR25 = myDsl_type_qualifier_listR25
        self.myDsl_type_qualifier_listR23 = myDsl_type_qualifier_listR23 if myDsl_type_qualifier_listR23 is not None else set()
        
    @property
    def Type_qualifier(self) -> str:
        return self.__Type_qualifier

    @Type_qualifier.setter
    def Type_qualifier(self, Type_qualifier: str):
        self.__Type_qualifier = Type_qualifier

    @property
    def myDsl_type_qualifier_listR23(self):
        return self.__myDsl_type_qualifier_listR23

    @myDsl_type_qualifier_listR23.setter
    def myDsl_type_qualifier_listR23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_listR__myDsl_type_qualifier_listR23", None)
        self.__myDsl_type_qualifier_listR23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_type_qualifier_listR25"):
                    opp_val = getattr(item, "myDsl_type_qualifier_listR25", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_type_qualifier_listR25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_type_qualifier_listR25"):
                    opp_val = getattr(item, "myDsl_type_qualifier_listR25", None)
                    
                    setattr(item, "myDsl_type_qualifier_listR25", self)
                    

    @property
    def myDsl_type_qualifier_listR25(self):
        return self.__myDsl_type_qualifier_listR25

    @myDsl_type_qualifier_listR25.setter
    def myDsl_type_qualifier_listR25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_listR__myDsl_type_qualifier_listR25", None)
        self.__myDsl_type_qualifier_listR25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_listR23"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_listR23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_listR23"):
                opp_val = getattr(value, "myDsl_type_qualifier_listR23", None)
                if opp_val is None:
                    setattr(value, "myDsl_type_qualifier_listR23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_type_qualifier_listR(self):
        return self.__myDsl_type_qualifier_listR

    @myDsl_type_qualifier_listR.setter
    def myDsl_type_qualifier_listR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_listR__myDsl_type_qualifier_listR", None)
        self.__myDsl_type_qualifier_listR = value
        
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

class pointer:

    pass
class myDsl_type_qualifier_list(pointer):

    def __init__(self, Type_qualifier: str, myDsl_type_qualifier_list: "myDsl_type_qualifier_listR" = None, myDsl_type_qualifier_list33: "myDsl_direct_declaratorR" = None, myDsl_type_qualifier_list344: "myDsl_pointer" = None):
        self.Type_qualifier = Type_qualifier
        self.myDsl_type_qualifier_list = myDsl_type_qualifier_list
        self.myDsl_type_qualifier_list33 = myDsl_type_qualifier_list33
        self.myDsl_type_qualifier_list344 = myDsl_type_qualifier_list344
        
    @property
    def Type_qualifier(self) -> str:
        return self.__Type_qualifier

    @Type_qualifier.setter
    def Type_qualifier(self, Type_qualifier: str):
        self.__Type_qualifier = Type_qualifier

    @property
    def myDsl_type_qualifier_list(self):
        return self.__myDsl_type_qualifier_list

    @myDsl_type_qualifier_list.setter
    def myDsl_type_qualifier_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_list__myDsl_type_qualifier_list", None)
        self.__myDsl_type_qualifier_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_listR"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_listR", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_listR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_listR"):
                opp_val = getattr(value, "myDsl_type_qualifier_listR", None)
                setattr(value, "myDsl_type_qualifier_listR", self)

    @property
    def myDsl_type_qualifier_list344(self):
        return self.__myDsl_type_qualifier_list344

    @myDsl_type_qualifier_list344.setter
    def myDsl_type_qualifier_list344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_list__myDsl_type_qualifier_list344", None)
        self.__myDsl_type_qualifier_list344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_pointer343"):
                opp_val = getattr(old_value, "myDsl_pointer343", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_pointer343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_pointer343"):
                opp_val = getattr(value, "myDsl_pointer343", None)
                setattr(value, "myDsl_pointer343", self)

    @property
    def myDsl_type_qualifier_list33(self):
        return self.__myDsl_type_qualifier_list33

    @myDsl_type_qualifier_list33.setter
    def myDsl_type_qualifier_list33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier_list__myDsl_type_qualifier_list33", None)
        self.__myDsl_type_qualifier_list33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declaratorR32"):
                opp_val = getattr(old_value, "myDsl_direct_declaratorR32", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declaratorR32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declaratorR32"):
                opp_val = getattr(value, "myDsl_direct_declaratorR32", None)
                setattr(value, "myDsl_direct_declaratorR32", self)

class myDsl_direct_declarator(declarator):

    pass
class external_declaration:

    pass
class myDsl_declaration(external_declaration, block_item):

    pass
class myDsl_function_definition(external_declaration):

    pass
class myDsl_declaration_specifiers(parameter_declaration):

    def __init__(self, Storage_class_specifier: str, Type_qualifier: str, myDsl_declaration_specifiers: "myDsl_external_declaration" = None, myDsl_declaration_specifiers57: "myDsl_parameter_declaration" = None, myDsl_declaration_specifiers51: "myDsl_parameter_declaration" = None, myDsl_declaration_specifiers113: "myDsl_declaration_specifiers" = None, myDsl_declaration_specifiers111: set["myDsl_declaration_specifiers"] = None, myDsl_declaration_specifiers116: "myDsl_declaration_specifiers" = None, myDsl_declaration_specifiers114: set["myDsl_declaration_specifiers"] = None, myDsl_declaration_specifiers358: "myDsl_type_specifier" = None):
        self.Storage_class_specifier = Storage_class_specifier
        self.Type_qualifier = Type_qualifier
        self.myDsl_declaration_specifiers = myDsl_declaration_specifiers
        self.myDsl_declaration_specifiers57 = myDsl_declaration_specifiers57
        self.myDsl_declaration_specifiers51 = myDsl_declaration_specifiers51
        self.myDsl_declaration_specifiers113 = myDsl_declaration_specifiers113
        self.myDsl_declaration_specifiers111 = myDsl_declaration_specifiers111 if myDsl_declaration_specifiers111 is not None else set()
        self.myDsl_declaration_specifiers116 = myDsl_declaration_specifiers116
        self.myDsl_declaration_specifiers114 = myDsl_declaration_specifiers114 if myDsl_declaration_specifiers114 is not None else set()
        self.myDsl_declaration_specifiers358 = myDsl_declaration_specifiers358
        
    @property
    def Type_qualifier(self) -> str:
        return self.__Type_qualifier

    @Type_qualifier.setter
    def Type_qualifier(self, Type_qualifier: str):
        self.__Type_qualifier = Type_qualifier

    @property
    def Storage_class_specifier(self) -> str:
        return self.__Storage_class_specifier

    @Storage_class_specifier.setter
    def Storage_class_specifier(self, Storage_class_specifier: str):
        self.__Storage_class_specifier = Storage_class_specifier

    @property
    def myDsl_declaration_specifiers111(self):
        return self.__myDsl_declaration_specifiers111

    @myDsl_declaration_specifiers111.setter
    def myDsl_declaration_specifiers111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers111", None)
        self.__myDsl_declaration_specifiers111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_declaration_specifiers113"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers113", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_declaration_specifiers113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_declaration_specifiers113"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers113", None)
                    
                    setattr(item, "myDsl_declaration_specifiers113", self)
                    

    @property
    def myDsl_declaration_specifiers114(self):
        return self.__myDsl_declaration_specifiers114

    @myDsl_declaration_specifiers114.setter
    def myDsl_declaration_specifiers114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers114", None)
        self.__myDsl_declaration_specifiers114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_declaration_specifiers116"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers116", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_declaration_specifiers116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_declaration_specifiers116"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers116", None)
                    
                    setattr(item, "myDsl_declaration_specifiers116", self)
                    

    @property
    def myDsl_declaration_specifiers57(self):
        return self.__myDsl_declaration_specifiers57

    @myDsl_declaration_specifiers57.setter
    def myDsl_declaration_specifiers57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers57", None)
        self.__myDsl_declaration_specifiers57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_declaration56"):
                opp_val = getattr(old_value, "myDsl_parameter_declaration56", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_declaration56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_declaration56"):
                opp_val = getattr(value, "myDsl_parameter_declaration56", None)
                setattr(value, "myDsl_parameter_declaration56", self)

    @property
    def myDsl_declaration_specifiers358(self):
        return self.__myDsl_declaration_specifiers358

    @myDsl_declaration_specifiers358.setter
    def myDsl_declaration_specifiers358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers358", None)
        self.__myDsl_declaration_specifiers358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier357"):
                opp_val = getattr(old_value, "myDsl_type_specifier357", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier357"):
                opp_val = getattr(value, "myDsl_type_specifier357", None)
                setattr(value, "myDsl_type_specifier357", self)

    @property
    def myDsl_declaration_specifiers51(self):
        return self.__myDsl_declaration_specifiers51

    @myDsl_declaration_specifiers51.setter
    def myDsl_declaration_specifiers51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers51", None)
        self.__myDsl_declaration_specifiers51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_declaration50"):
                opp_val = getattr(old_value, "myDsl_parameter_declaration50", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_declaration50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_declaration50"):
                opp_val = getattr(value, "myDsl_parameter_declaration50", None)
                setattr(value, "myDsl_parameter_declaration50", self)

    @property
    def myDsl_declaration_specifiers116(self):
        return self.__myDsl_declaration_specifiers116

    @myDsl_declaration_specifiers116.setter
    def myDsl_declaration_specifiers116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers116", None)
        self.__myDsl_declaration_specifiers116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers114"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers114"):
                opp_val = getattr(value, "myDsl_declaration_specifiers114", None)
                if opp_val is None:
                    setattr(value, "myDsl_declaration_specifiers114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_declaration_specifiers(self):
        return self.__myDsl_declaration_specifiers

    @myDsl_declaration_specifiers.setter
    def myDsl_declaration_specifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers", None)
        self.__myDsl_declaration_specifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_external_declaration12"):
                opp_val = getattr(old_value, "myDsl_external_declaration12", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_external_declaration12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_external_declaration12"):
                opp_val = getattr(value, "myDsl_external_declaration12", None)
                setattr(value, "myDsl_external_declaration12", self)

    @property
    def myDsl_declaration_specifiers113(self):
        return self.__myDsl_declaration_specifiers113

    @myDsl_declaration_specifiers113.setter
    def myDsl_declaration_specifiers113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers113", None)
        self.__myDsl_declaration_specifiers113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers111"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers111"):
                opp_val = getattr(value, "myDsl_declaration_specifiers111", None)
                if opp_val is None:
                    setattr(value, "myDsl_declaration_specifiers111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_translation_unitR:

    pass
class myDsl_external_declaration:

    pass
class myDsl_translation_unit:

    pass
class myDsl_Model:

    pass
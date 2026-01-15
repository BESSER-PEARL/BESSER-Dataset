from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class init_declarator_list_linha:

    pass
class ansic_InitDecclaratorListLinhaAction(init_declarator_list_linha):

    pass
class argument_expression_list_linha:

    pass
class ansic_ArgumentExpressionListLinhaAction(argument_expression_list_linha):

    pass
class postfix_expression_complement:

    pass
class ansic_PostFixEmpryParams(postfix_expression_complement):

    pass
class designator_list_linha:

    pass
class ansic_DesignatorListLinhaAction(designator_list_linha):

    pass
class initializer_list_linha:

    pass
class ansic_InitializerListLinhaAction(initializer_list_linha):

    pass
class postfix_expression_linha:

    pass
class ansic_PostfixExpressionLinhaAction(postfix_expression_linha):

    pass
class generic_assoc_list_linha:

    pass
class ansic_GenericAssocListLinhaAction(generic_assoc_list_linha):

    pass
class translation_unit_linha:

    pass
class ansic_TranlationUnitLinhaAction(translation_unit_linha):

    pass
class unary_expression:

    pass
class ansic_PlusPlus(unary_expression):

    def __init__(self, plus: str):
        self.plus = plus
        
    @property
    def plus(self) -> str:
        return self.__plus

    @plus.setter
    def plus(self, plus: str):
        self.__plus = plus

class direct_abstract_declarator_linha:

    pass
class ansic_DirectAbstractDeclarratorLinhaAction(direct_abstract_declarator_linha):

    pass
class type_qualifier_list_linha:

    pass
class ansic_TypeQualifierListLinhaAtion(type_qualifier_list_linha):

    pass
class declaration_list_linha:

    pass
class ansic_DeclarationListLinhaAction(declaration_list_linha):

    pass
class struct_declarator_list_linha:

    pass
class ansic_StructDeclaratorListLinhaAction(struct_declarator_list_linha):

    pass
class struct_declaration_list_linha:

    pass
class ansic_StructDeclarationListLinhaAction(struct_declaration_list_linha):

    pass
class struct_or_union_specifier_complement:

    pass
class ansic_StructOrUnionSpecifierComplementAction(struct_or_union_specifier_complement):

    pass
class enumerator_list_linha:

    pass
class ansic_EnumeratorListLinhaAction(enumerator_list_linha):

    pass
class ansic_string_ufcg:

    def __init__(self, string_literal: str, __func__: str):
        self.string_literal = string_literal
        self.__func__ = __func__
        
    @property
    def string_literal(self) -> str:
        return self.__string_literal

    @string_literal.setter
    def string_literal(self, string_literal: str):
        self.__string_literal = string_literal

    @property
    def __func__(self) -> str:
        return self.____func__

    @__func__.setter
    def __func__(self, __func__: str):
        self.____func__ = __func__

class identifier_list_linha:

    pass
class ansic_IdentifierListLinhaAction(identifier_list_linha):

    def __init__(self, identifier: str, ansic_IdentifierListLinhaAction: "ansic_identifier_list_linha" = None):
        self.identifier = identifier
        self.ansic_IdentifierListLinhaAction = ansic_IdentifierListLinhaAction
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_IdentifierListLinhaAction(self):
        return self.__ansic_IdentifierListLinhaAction

    @ansic_IdentifierListLinhaAction.setter
    def ansic_IdentifierListLinhaAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_IdentifierListLinhaAction__ansic_IdentifierListLinhaAction", None)
        self.__ansic_IdentifierListLinhaAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_identifier_list_linha518"):
                opp_val = getattr(old_value, "ansic_identifier_list_linha518", None)
                if opp_val == self:
                    setattr(old_value, "ansic_identifier_list_linha518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_identifier_list_linha518"):
                opp_val = getattr(value, "ansic_identifier_list_linha518", None)
                setattr(value, "ansic_identifier_list_linha518", self)

class ansic_init_declarator:

    pass
class ansic_expression_linha:

    pass
class postfix_expression:

    pass
class ansic_conditional_expression_linha:

    pass
class ansic_logical_or_expression_linha:

    pass
class ansic_logical_or_expression:

    pass
class ansic_inclusive_or_expression_linha:

    pass
class ansic_inclusive_or_expression:

    pass
class ansic_exclusive_or_expression_linha:

    pass
class ansic_exclusive_or_expression:

    pass
class ansic_and_expression_linha:

    pass
class ansic_and_expression:

    pass
class ansic_logical_and_expression_linha:

    pass
class ansic_logical_and_expression:

    pass
class ansic_block_item_list_linha:

    pass
class ansic_block_item:

    pass
class ansic_block_item_list:

    pass
class ansic_jump_statement:

    def __init__(self, return: str, identifier: str, break: str, return_vazio: str, ansic_jump_statement325: "ansic_expression" = None, ansic_jump_statement: "ansic_statement" = None):
        self.return = return
        self.identifier = identifier
        self.break = break
        self.return_vazio = return_vazio
        self.ansic_jump_statement325 = ansic_jump_statement325
        self.ansic_jump_statement = ansic_jump_statement
        
    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def return_vazio(self) -> str:
        return self.__return_vazio

    @return_vazio.setter
    def return_vazio(self, return_vazio: str):
        self.__return_vazio = return_vazio

    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def ansic_jump_statement325(self):
        return self.__ansic_jump_statement325

    @ansic_jump_statement325.setter
    def ansic_jump_statement325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_jump_statement__ansic_jump_statement325", None)
        self.__ansic_jump_statement325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_expression326"):
                opp_val = getattr(old_value, "ansic_expression326", None)
                if opp_val == self:
                    setattr(old_value, "ansic_expression326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_expression326"):
                opp_val = getattr(value, "ansic_expression326", None)
                setattr(value, "ansic_expression326", self)

    @property
    def ansic_jump_statement(self):
        return self.__ansic_jump_statement

    @ansic_jump_statement.setter
    def ansic_jump_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_jump_statement__ansic_jump_statement", None)
        self.__ansic_jump_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_statement323"):
                opp_val = getattr(old_value, "ansic_statement323", None)
                if opp_val == self:
                    setattr(old_value, "ansic_statement323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_statement323"):
                opp_val = getattr(value, "ansic_statement323", None)
                setattr(value, "ansic_statement323", self)

class ansic_iteration_statement:

    pass
class ansic_selection_statement:

    pass
class ansic_expression_statement:

    pass
class ansic_labeled_statement:

    def __init__(self, identifier: str, ansic_labeled_statement: "ansic_statement" = None, ansic_labeled_statement352: "ansic_statement" = None, ansic_labeled_statement355: "ansic_conditional_expression" = None):
        self.identifier = identifier
        self.ansic_labeled_statement = ansic_labeled_statement
        self.ansic_labeled_statement352 = ansic_labeled_statement352
        self.ansic_labeled_statement355 = ansic_labeled_statement355
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_labeled_statement355(self):
        return self.__ansic_labeled_statement355

    @ansic_labeled_statement355.setter
    def ansic_labeled_statement355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_labeled_statement__ansic_labeled_statement355", None)
        self.__ansic_labeled_statement355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_conditional_expression356"):
                opp_val = getattr(old_value, "ansic_conditional_expression356", None)
                if opp_val == self:
                    setattr(old_value, "ansic_conditional_expression356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_conditional_expression356"):
                opp_val = getattr(value, "ansic_conditional_expression356", None)
                setattr(value, "ansic_conditional_expression356", self)

    @property
    def ansic_labeled_statement(self):
        return self.__ansic_labeled_statement

    @ansic_labeled_statement.setter
    def ansic_labeled_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_labeled_statement__ansic_labeled_statement", None)
        self.__ansic_labeled_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_statement"):
                opp_val = getattr(old_value, "ansic_statement", None)
                if opp_val == self:
                    setattr(old_value, "ansic_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_statement"):
                opp_val = getattr(value, "ansic_statement", None)
                setattr(value, "ansic_statement", self)

    @property
    def ansic_labeled_statement352(self):
        return self.__ansic_labeled_statement352

    @ansic_labeled_statement352.setter
    def ansic_labeled_statement352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_labeled_statement__ansic_labeled_statement352", None)
        self.__ansic_labeled_statement352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_statement353"):
                opp_val = getattr(old_value, "ansic_statement353", None)
                if opp_val == self:
                    setattr(old_value, "ansic_statement353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_statement353"):
                opp_val = getattr(value, "ansic_statement353", None)
                setattr(value, "ansic_statement353", self)

class ansic_statement:

    pass
class ansic_equality_expression_complement:

    pass
class ansic_relational_expression_linha:

    pass
class ansic_relational_expression:

    pass
class ansic_shift_expression_complement:

    pass
class ansic_shift_expression_linha:

    pass
class ansic_shift_expression:

    pass
class ansic_additive_expression_complement:

    pass
class ansic_additive_expression_linha:

    pass
class ansic_equality_expression_linha:

    pass
class ansic_equality_expression:

    pass
class ansic_relational_expression_complement:

    pass
class ansic_multiplicative_expression_linha:

    pass
class ansic_multiplicative_expression:

    pass
class ansic_cast_expression:

    pass
class ansic_unary_expression:

    def __init__(self, unary_operator: str, ansic_unary_expression: "ansic_postfix_expression" = None, ansic_unary_expression237: "ansic_unary_expression" = None, ansic_unary_expression235: "ansic_unary_expression" = None, ansic_unary_expression239: "ansic_cast_expression" = None, ansic_unary_expression241: "ansic_type_name" = None, ansic_unary_expression245: "ansic_cast_expression" = None, ansic_unary_expression447: "ansic_assignment_expression" = None):
        self.unary_operator = unary_operator
        self.ansic_unary_expression = ansic_unary_expression
        self.ansic_unary_expression237 = ansic_unary_expression237
        self.ansic_unary_expression235 = ansic_unary_expression235
        self.ansic_unary_expression239 = ansic_unary_expression239
        self.ansic_unary_expression241 = ansic_unary_expression241
        self.ansic_unary_expression245 = ansic_unary_expression245
        self.ansic_unary_expression447 = ansic_unary_expression447
        
    @property
    def unary_operator(self) -> str:
        return self.__unary_operator

    @unary_operator.setter
    def unary_operator(self, unary_operator: str):
        self.__unary_operator = unary_operator

    @property
    def ansic_unary_expression447(self):
        return self.__ansic_unary_expression447

    @ansic_unary_expression447.setter
    def ansic_unary_expression447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression447", None)
        self.__ansic_unary_expression447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_assignment_expression446"):
                opp_val = getattr(old_value, "ansic_assignment_expression446", None)
                if opp_val == self:
                    setattr(old_value, "ansic_assignment_expression446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_assignment_expression446"):
                opp_val = getattr(value, "ansic_assignment_expression446", None)
                setattr(value, "ansic_assignment_expression446", self)

    @property
    def ansic_unary_expression245(self):
        return self.__ansic_unary_expression245

    @ansic_unary_expression245.setter
    def ansic_unary_expression245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression245", None)
        self.__ansic_unary_expression245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_cast_expression244"):
                opp_val = getattr(old_value, "ansic_cast_expression244", None)
                if opp_val == self:
                    setattr(old_value, "ansic_cast_expression244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_cast_expression244"):
                opp_val = getattr(value, "ansic_cast_expression244", None)
                setattr(value, "ansic_cast_expression244", self)

    @property
    def ansic_unary_expression(self):
        return self.__ansic_unary_expression

    @ansic_unary_expression.setter
    def ansic_unary_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression", None)
        self.__ansic_unary_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_postfix_expression234"):
                opp_val = getattr(old_value, "ansic_postfix_expression234", None)
                if opp_val == self:
                    setattr(old_value, "ansic_postfix_expression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_postfix_expression234"):
                opp_val = getattr(value, "ansic_postfix_expression234", None)
                setattr(value, "ansic_postfix_expression234", self)

    @property
    def ansic_unary_expression237(self):
        return self.__ansic_unary_expression237

    @ansic_unary_expression237.setter
    def ansic_unary_expression237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression237", None)
        self.__ansic_unary_expression237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_unary_expression235"):
                opp_val = getattr(old_value, "ansic_unary_expression235", None)
                if opp_val == self:
                    setattr(old_value, "ansic_unary_expression235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_unary_expression235"):
                opp_val = getattr(value, "ansic_unary_expression235", None)
                setattr(value, "ansic_unary_expression235", self)

    @property
    def ansic_unary_expression235(self):
        return self.__ansic_unary_expression235

    @ansic_unary_expression235.setter
    def ansic_unary_expression235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression235", None)
        self.__ansic_unary_expression235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_unary_expression237"):
                opp_val = getattr(old_value, "ansic_unary_expression237", None)
                if opp_val == self:
                    setattr(old_value, "ansic_unary_expression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_unary_expression237"):
                opp_val = getattr(value, "ansic_unary_expression237", None)
                setattr(value, "ansic_unary_expression237", self)

    @property
    def ansic_unary_expression239(self):
        return self.__ansic_unary_expression239

    @ansic_unary_expression239.setter
    def ansic_unary_expression239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression239", None)
        self.__ansic_unary_expression239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_cast_expression"):
                opp_val = getattr(old_value, "ansic_cast_expression", None)
                if opp_val == self:
                    setattr(old_value, "ansic_cast_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_cast_expression"):
                opp_val = getattr(value, "ansic_cast_expression", None)
                setattr(value, "ansic_cast_expression", self)

    @property
    def ansic_unary_expression241(self):
        return self.__ansic_unary_expression241

    @ansic_unary_expression241.setter
    def ansic_unary_expression241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_unary_expression__ansic_unary_expression241", None)
        self.__ansic_unary_expression241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_name242"):
                opp_val = getattr(old_value, "ansic_type_name242", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_name242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_name242"):
                opp_val = getattr(value, "ansic_type_name242", None)
                setattr(value, "ansic_type_name242", self)

class ansic_argument_expression_list_linha:

    pass
class ansic_argument_expression_list:

    pass
class ansic_additive_expression:

    pass
class ansic_multiplicative_expression_complement:

    pass
class ansic_designator_list_linha:

    pass
class ansic_designator:

    def __init__(self, identifier: str, ansic_designator222: "ansic_conditional_expression" = None, ansic_designator: "ansic_designator_list" = None, ansic_designator540: "ansic_DesignatorListLinhaAction" = None):
        self.identifier = identifier
        self.ansic_designator222 = ansic_designator222
        self.ansic_designator = ansic_designator
        self.ansic_designator540 = ansic_designator540
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_designator222(self):
        return self.__ansic_designator222

    @ansic_designator222.setter
    def ansic_designator222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_designator__ansic_designator222", None)
        self.__ansic_designator222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_conditional_expression"):
                opp_val = getattr(old_value, "ansic_conditional_expression", None)
                if opp_val == self:
                    setattr(old_value, "ansic_conditional_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_conditional_expression"):
                opp_val = getattr(value, "ansic_conditional_expression", None)
                setattr(value, "ansic_conditional_expression", self)

    @property
    def ansic_designator540(self):
        return self.__ansic_designator540

    @ansic_designator540.setter
    def ansic_designator540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_designator__ansic_designator540", None)
        self.__ansic_designator540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_DesignatorListLinhaAction"):
                opp_val = getattr(old_value, "ansic_DesignatorListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "ansic_DesignatorListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_DesignatorListLinhaAction"):
                opp_val = getattr(value, "ansic_DesignatorListLinhaAction", None)
                setattr(value, "ansic_DesignatorListLinhaAction", self)

    @property
    def ansic_designator(self):
        return self.__ansic_designator

    @ansic_designator.setter
    def ansic_designator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_designator__ansic_designator", None)
        self.__ansic_designator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_designator_list218"):
                opp_val = getattr(old_value, "ansic_designator_list218", None)
                if opp_val == self:
                    setattr(old_value, "ansic_designator_list218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_designator_list218"):
                opp_val = getattr(value, "ansic_designator_list218", None)
                setattr(value, "ansic_designator_list218", self)

class ansic_designator_list:

    pass
class ansic_initializer_list_complement:

    pass
class ansic_initializer_list_linha:

    pass
class ansic_init_declarator_list_linha:

    pass
class ansic_designation:

    pass
class ansic_postfix_expression_linha:

    pass
class ansic_postfix_expression:

    pass
class ansic_postfix_expression_complement:

    def __init__(self, identifier: str, ansic_postfix_expression_complement: "ansic_expression" = None, ansic_postfix_expression_complement229: "ansic_argument_expression_list" = None, ansic_postfix_expression_complement530: "ansic_PostfixExpressionLinhaAction" = None):
        self.identifier = identifier
        self.ansic_postfix_expression_complement = ansic_postfix_expression_complement
        self.ansic_postfix_expression_complement229 = ansic_postfix_expression_complement229
        self.ansic_postfix_expression_complement530 = ansic_postfix_expression_complement530
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_postfix_expression_complement(self):
        return self.__ansic_postfix_expression_complement

    @ansic_postfix_expression_complement.setter
    def ansic_postfix_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_postfix_expression_complement__ansic_postfix_expression_complement", None)
        self.__ansic_postfix_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_expression227"):
                opp_val = getattr(old_value, "ansic_expression227", None)
                if opp_val == self:
                    setattr(old_value, "ansic_expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_expression227"):
                opp_val = getattr(value, "ansic_expression227", None)
                setattr(value, "ansic_expression227", self)

    @property
    def ansic_postfix_expression_complement229(self):
        return self.__ansic_postfix_expression_complement229

    @ansic_postfix_expression_complement229.setter
    def ansic_postfix_expression_complement229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_postfix_expression_complement__ansic_postfix_expression_complement229", None)
        self.__ansic_postfix_expression_complement229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_argument_expression_list"):
                opp_val = getattr(old_value, "ansic_argument_expression_list", None)
                if opp_val == self:
                    setattr(old_value, "ansic_argument_expression_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_argument_expression_list"):
                opp_val = getattr(value, "ansic_argument_expression_list", None)
                setattr(value, "ansic_argument_expression_list", self)

    @property
    def ansic_postfix_expression_complement530(self):
        return self.__ansic_postfix_expression_complement530

    @ansic_postfix_expression_complement530.setter
    def ansic_postfix_expression_complement530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_postfix_expression_complement__ansic_postfix_expression_complement530", None)
        self.__ansic_postfix_expression_complement530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_PostfixExpressionLinhaAction"):
                opp_val = getattr(old_value, "ansic_PostfixExpressionLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "ansic_PostfixExpressionLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_PostfixExpressionLinhaAction"):
                opp_val = getattr(value, "ansic_PostfixExpressionLinhaAction", None)
                setattr(value, "ansic_PostfixExpressionLinhaAction", self)

class ansic_conditional_expression:

    pass
class ansic_generic_selection:

    def __init__(self, _generic: str, ansic_generic_selection188: set["ansic_generic_assoc_list"] = None, ansic_generic_selection: "ansic_primary_expression" = None, ansic_generic_selection185: "ansic_assignment_expression" = None):
        self._generic = _generic
        self.ansic_generic_selection188 = ansic_generic_selection188 if ansic_generic_selection188 is not None else set()
        self.ansic_generic_selection = ansic_generic_selection
        self.ansic_generic_selection185 = ansic_generic_selection185
        
    @property
    def _generic(self) -> str:
        return self.___generic

    @_generic.setter
    def _generic(self, _generic: str):
        self.___generic = _generic

    @property
    def ansic_generic_selection188(self):
        return self.__ansic_generic_selection188

    @ansic_generic_selection188.setter
    def ansic_generic_selection188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_selection__ansic_generic_selection188", None)
        self.__ansic_generic_selection188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ansic_generic_assoc_list"):
                    opp_val = getattr(item, "ansic_generic_assoc_list", None)
                    
                    if opp_val == self:
                        setattr(item, "ansic_generic_assoc_list", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ansic_generic_assoc_list"):
                    opp_val = getattr(item, "ansic_generic_assoc_list", None)
                    
                    setattr(item, "ansic_generic_assoc_list", self)
                    

    @property
    def ansic_generic_selection185(self):
        return self.__ansic_generic_selection185

    @ansic_generic_selection185.setter
    def ansic_generic_selection185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_selection__ansic_generic_selection185", None)
        self.__ansic_generic_selection185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_assignment_expression186"):
                opp_val = getattr(old_value, "ansic_assignment_expression186", None)
                if opp_val == self:
                    setattr(old_value, "ansic_assignment_expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_assignment_expression186"):
                opp_val = getattr(value, "ansic_assignment_expression186", None)
                setattr(value, "ansic_assignment_expression186", self)

    @property
    def ansic_generic_selection(self):
        return self.__ansic_generic_selection

    @ansic_generic_selection.setter
    def ansic_generic_selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_selection__ansic_generic_selection", None)
        self.__ansic_generic_selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_primary_expression183"):
                opp_val = getattr(old_value, "ansic_primary_expression183", None)
                if opp_val == self:
                    setattr(old_value, "ansic_primary_expression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_primary_expression183"):
                opp_val = getattr(value, "ansic_primary_expression183", None)
                setattr(value, "ansic_primary_expression183", self)

class ansic_expression:

    pass
class ansic_constant:

    def __init__(self, i_constant: int, f_constant: str, char: str, enumz: str, ansic_constant: "ansic_primary_expression" = None):
        self.i_constant = i_constant
        self.f_constant = f_constant
        self.char = char
        self.enumz = enumz
        self.ansic_constant = ansic_constant
        
    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def f_constant(self) -> str:
        return self.__f_constant

    @f_constant.setter
    def f_constant(self, f_constant: str):
        self.__f_constant = f_constant

    @property
    def i_constant(self) -> int:
        return self.__i_constant

    @i_constant.setter
    def i_constant(self, i_constant: int):
        self.__i_constant = i_constant

    @property
    def enumz(self) -> str:
        return self.__enumz

    @enumz.setter
    def enumz(self, enumz: str):
        self.__enumz = enumz

    @property
    def ansic_constant(self):
        return self.__ansic_constant

    @ansic_constant.setter
    def ansic_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_constant__ansic_constant", None)
        self.__ansic_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_primary_expression"):
                opp_val = getattr(old_value, "ansic_primary_expression", None)
                if opp_val == self:
                    setattr(old_value, "ansic_primary_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_primary_expression"):
                opp_val = getattr(value, "ansic_primary_expression", None)
                setattr(value, "ansic_primary_expression", self)

class ansic_primary_expression:

    def __init__(self, identifier: str, ansic_primary_expression: "ansic_constant" = None, ansic_primary_expression181: "ansic_expression" = None, ansic_primary_expression183: "ansic_generic_selection" = None, ansic_primary_expression200: "ansic_postfix_expression" = None):
        self.identifier = identifier
        self.ansic_primary_expression = ansic_primary_expression
        self.ansic_primary_expression181 = ansic_primary_expression181
        self.ansic_primary_expression183 = ansic_primary_expression183
        self.ansic_primary_expression200 = ansic_primary_expression200
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_primary_expression200(self):
        return self.__ansic_primary_expression200

    @ansic_primary_expression200.setter
    def ansic_primary_expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_primary_expression__ansic_primary_expression200", None)
        self.__ansic_primary_expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_postfix_expression"):
                opp_val = getattr(old_value, "ansic_postfix_expression", None)
                if opp_val == self:
                    setattr(old_value, "ansic_postfix_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_postfix_expression"):
                opp_val = getattr(value, "ansic_postfix_expression", None)
                setattr(value, "ansic_postfix_expression", self)

    @property
    def ansic_primary_expression183(self):
        return self.__ansic_primary_expression183

    @ansic_primary_expression183.setter
    def ansic_primary_expression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_primary_expression__ansic_primary_expression183", None)
        self.__ansic_primary_expression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_generic_selection"):
                opp_val = getattr(old_value, "ansic_generic_selection", None)
                if opp_val == self:
                    setattr(old_value, "ansic_generic_selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_generic_selection"):
                opp_val = getattr(value, "ansic_generic_selection", None)
                setattr(value, "ansic_generic_selection", self)

    @property
    def ansic_primary_expression181(self):
        return self.__ansic_primary_expression181

    @ansic_primary_expression181.setter
    def ansic_primary_expression181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_primary_expression__ansic_primary_expression181", None)
        self.__ansic_primary_expression181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_expression"):
                opp_val = getattr(old_value, "ansic_expression", None)
                if opp_val == self:
                    setattr(old_value, "ansic_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_expression"):
                opp_val = getattr(value, "ansic_expression", None)
                setattr(value, "ansic_expression", self)

    @property
    def ansic_primary_expression(self):
        return self.__ansic_primary_expression

    @ansic_primary_expression.setter
    def ansic_primary_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_primary_expression__ansic_primary_expression", None)
        self.__ansic_primary_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_constant"):
                opp_val = getattr(old_value, "ansic_constant", None)
                if opp_val == self:
                    setattr(old_value, "ansic_constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_constant"):
                opp_val = getattr(value, "ansic_constant", None)
                setattr(value, "ansic_constant", self)

class ansic_identifier_list_linha:

    pass
class ansic_direct_abstract_declarator_complement:

    pass
class ansic_initializer_list:

    pass
class ansic_generic_assoc_list_linha:

    pass
class ansic_generic_association:

    def __init__(self, default: str, ansic_generic_association: "ansic_generic_assoc_list" = None, ansic_generic_association194: "ansic_type_name" = None, ansic_generic_association197: "ansic_assignment_expression" = None, ansic_generic_association525: "ansic_GenericAssocListLinhaAction" = None):
        self.default = default
        self.ansic_generic_association = ansic_generic_association
        self.ansic_generic_association194 = ansic_generic_association194
        self.ansic_generic_association197 = ansic_generic_association197
        self.ansic_generic_association525 = ansic_generic_association525
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def ansic_generic_association(self):
        return self.__ansic_generic_association

    @ansic_generic_association.setter
    def ansic_generic_association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_association__ansic_generic_association", None)
        self.__ansic_generic_association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_generic_assoc_list190"):
                opp_val = getattr(old_value, "ansic_generic_assoc_list190", None)
                if opp_val == self:
                    setattr(old_value, "ansic_generic_assoc_list190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_generic_assoc_list190"):
                opp_val = getattr(value, "ansic_generic_assoc_list190", None)
                setattr(value, "ansic_generic_assoc_list190", self)

    @property
    def ansic_generic_association197(self):
        return self.__ansic_generic_association197

    @ansic_generic_association197.setter
    def ansic_generic_association197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_association__ansic_generic_association197", None)
        self.__ansic_generic_association197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_assignment_expression198"):
                opp_val = getattr(old_value, "ansic_assignment_expression198", None)
                if opp_val == self:
                    setattr(old_value, "ansic_assignment_expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_assignment_expression198"):
                opp_val = getattr(value, "ansic_assignment_expression198", None)
                setattr(value, "ansic_assignment_expression198", self)

    @property
    def ansic_generic_association194(self):
        return self.__ansic_generic_association194

    @ansic_generic_association194.setter
    def ansic_generic_association194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_association__ansic_generic_association194", None)
        self.__ansic_generic_association194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_name195"):
                opp_val = getattr(old_value, "ansic_type_name195", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_name195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_name195"):
                opp_val = getattr(value, "ansic_type_name195", None)
                setattr(value, "ansic_type_name195", self)

    @property
    def ansic_generic_association525(self):
        return self.__ansic_generic_association525

    @ansic_generic_association525.setter
    def ansic_generic_association525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_generic_association__ansic_generic_association525", None)
        self.__ansic_generic_association525 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_GenericAssocListLinhaAction"):
                opp_val = getattr(old_value, "ansic_GenericAssocListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "ansic_GenericAssocListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_GenericAssocListLinhaAction"):
                opp_val = getattr(value, "ansic_GenericAssocListLinhaAction", None)
                setattr(value, "ansic_GenericAssocListLinhaAction", self)

class ansic_generic_assoc_list:

    pass
class ansic_direct_abstract_declarator:

    pass
class ansic_abstract_declarator:

    pass
class ansic_parameter_list_linha:

    pass
class ansic_parameter_declaration:

    pass
class ansic_parameter_lista:

    pass
class ansic_identifier_list:

    def __init__(self, identifier: str, ansic_identifier_list: "ansic_direct_declarator_complemento" = None, ansic_identifier_list178: "ansic_identifier_list_linha" = None):
        self.identifier = identifier
        self.ansic_identifier_list = ansic_identifier_list
        self.ansic_identifier_list178 = ansic_identifier_list178
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_identifier_list178(self):
        return self.__ansic_identifier_list178

    @ansic_identifier_list178.setter
    def ansic_identifier_list178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_identifier_list__ansic_identifier_list178", None)
        self.__ansic_identifier_list178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_identifier_list_linha"):
                opp_val = getattr(old_value, "ansic_identifier_list_linha", None)
                if opp_val == self:
                    setattr(old_value, "ansic_identifier_list_linha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_identifier_list_linha"):
                opp_val = getattr(value, "ansic_identifier_list_linha", None)
                setattr(value, "ansic_identifier_list_linha", self)

    @property
    def ansic_identifier_list(self):
        return self.__ansic_identifier_list

    @ansic_identifier_list.setter
    def ansic_identifier_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_identifier_list__ansic_identifier_list", None)
        self.__ansic_identifier_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_direct_declarator_complemento128"):
                opp_val = getattr(old_value, "ansic_direct_declarator_complemento128", None)
                if opp_val == self:
                    setattr(old_value, "ansic_direct_declarator_complemento128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_direct_declarator_complemento128"):
                opp_val = getattr(value, "ansic_direct_declarator_complemento128", None)
                setattr(value, "ansic_direct_declarator_complemento128", self)

class ansic_initializer:

    pass
class ansic_parameter_type_list:

    pass
class ansic_direct_abstract_declarator_linha:

    pass
class ansic_assignment_expression:

    def __init__(self, assignment_operator: str, ansic_assignment_expression159: "ansic_direct_abstract_declarator" = None, ansic_assignment_expression: "ansic_direct_declarator_complemento" = None, ansic_assignment_expression168: "ansic_initializer" = None, ansic_assignment_expression170: "ansic_direct_abstract_declarator_complement" = None, ansic_assignment_expression186: "ansic_generic_selection" = None, ansic_assignment_expression198: "ansic_generic_association" = None, ansic_assignment_expression232: "ansic_argument_expression_list" = None, ansic_assignment_expression443: "ansic_conditional_expression" = None, ansic_assignment_expression446: "ansic_unary_expression" = None, ansic_assignment_expression450: "ansic_assignment_expression" = None, ansic_assignment_expression448: "ansic_assignment_expression" = None, ansic_assignment_expression462: "ansic_expression" = None, ansic_assignment_expression467: "ansic_expression_linha" = None, ansic_assignment_expression545: "ansic_ArgumentExpressionListLinhaAction" = None):
        self.assignment_operator = assignment_operator
        self.ansic_assignment_expression159 = ansic_assignment_expression159
        self.ansic_assignment_expression = ansic_assignment_expression
        self.ansic_assignment_expression168 = ansic_assignment_expression168
        self.ansic_assignment_expression170 = ansic_assignment_expression170
        self.ansic_assignment_expression186 = ansic_assignment_expression186
        self.ansic_assignment_expression198 = ansic_assignment_expression198
        self.ansic_assignment_expression232 = ansic_assignment_expression232
        self.ansic_assignment_expression443 = ansic_assignment_expression443
        self.ansic_assignment_expression446 = ansic_assignment_expression446
        self.ansic_assignment_expression450 = ansic_assignment_expression450
        self.ansic_assignment_expression448 = ansic_assignment_expression448
        self.ansic_assignment_expression462 = ansic_assignment_expression462
        self.ansic_assignment_expression467 = ansic_assignment_expression467
        self.ansic_assignment_expression545 = ansic_assignment_expression545
        
    @property
    def assignment_operator(self) -> str:
        return self.__assignment_operator

    @assignment_operator.setter
    def assignment_operator(self, assignment_operator: str):
        self.__assignment_operator = assignment_operator

    @property
    def ansic_assignment_expression186(self):
        return self.__ansic_assignment_expression186

    @ansic_assignment_expression186.setter
    def ansic_assignment_expression186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression186", None)
        self.__ansic_assignment_expression186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_generic_selection185"):
                opp_val = getattr(old_value, "ansic_generic_selection185", None)
                if opp_val == self:
                    setattr(old_value, "ansic_generic_selection185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_generic_selection185"):
                opp_val = getattr(value, "ansic_generic_selection185", None)
                setattr(value, "ansic_generic_selection185", self)

    @property
    def ansic_assignment_expression467(self):
        return self.__ansic_assignment_expression467

    @ansic_assignment_expression467.setter
    def ansic_assignment_expression467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression467", None)
        self.__ansic_assignment_expression467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_expression_linha466"):
                opp_val = getattr(old_value, "ansic_expression_linha466", None)
                if opp_val == self:
                    setattr(old_value, "ansic_expression_linha466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_expression_linha466"):
                opp_val = getattr(value, "ansic_expression_linha466", None)
                setattr(value, "ansic_expression_linha466", self)

    @property
    def ansic_assignment_expression170(self):
        return self.__ansic_assignment_expression170

    @ansic_assignment_expression170.setter
    def ansic_assignment_expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression170", None)
        self.__ansic_assignment_expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_direct_abstract_declarator_complement"):
                opp_val = getattr(old_value, "ansic_direct_abstract_declarator_complement", None)
                if opp_val == self:
                    setattr(old_value, "ansic_direct_abstract_declarator_complement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_direct_abstract_declarator_complement"):
                opp_val = getattr(value, "ansic_direct_abstract_declarator_complement", None)
                setattr(value, "ansic_direct_abstract_declarator_complement", self)

    @property
    def ansic_assignment_expression448(self):
        return self.__ansic_assignment_expression448

    @ansic_assignment_expression448.setter
    def ansic_assignment_expression448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression448", None)
        self.__ansic_assignment_expression448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_assignment_expression450"):
                opp_val = getattr(old_value, "ansic_assignment_expression450", None)
                if opp_val == self:
                    setattr(old_value, "ansic_assignment_expression450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_assignment_expression450"):
                opp_val = getattr(value, "ansic_assignment_expression450", None)
                setattr(value, "ansic_assignment_expression450", self)

    @property
    def ansic_assignment_expression198(self):
        return self.__ansic_assignment_expression198

    @ansic_assignment_expression198.setter
    def ansic_assignment_expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression198", None)
        self.__ansic_assignment_expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_generic_association197"):
                opp_val = getattr(old_value, "ansic_generic_association197", None)
                if opp_val == self:
                    setattr(old_value, "ansic_generic_association197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_generic_association197"):
                opp_val = getattr(value, "ansic_generic_association197", None)
                setattr(value, "ansic_generic_association197", self)

    @property
    def ansic_assignment_expression545(self):
        return self.__ansic_assignment_expression545

    @ansic_assignment_expression545.setter
    def ansic_assignment_expression545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression545", None)
        self.__ansic_assignment_expression545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_ArgumentExpressionListLinhaAction"):
                opp_val = getattr(old_value, "ansic_ArgumentExpressionListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "ansic_ArgumentExpressionListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_ArgumentExpressionListLinhaAction"):
                opp_val = getattr(value, "ansic_ArgumentExpressionListLinhaAction", None)
                setattr(value, "ansic_ArgumentExpressionListLinhaAction", self)

    @property
    def ansic_assignment_expression462(self):
        return self.__ansic_assignment_expression462

    @ansic_assignment_expression462.setter
    def ansic_assignment_expression462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression462", None)
        self.__ansic_assignment_expression462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_expression461"):
                opp_val = getattr(old_value, "ansic_expression461", None)
                if opp_val == self:
                    setattr(old_value, "ansic_expression461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_expression461"):
                opp_val = getattr(value, "ansic_expression461", None)
                setattr(value, "ansic_expression461", self)

    @property
    def ansic_assignment_expression168(self):
        return self.__ansic_assignment_expression168

    @ansic_assignment_expression168.setter
    def ansic_assignment_expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression168", None)
        self.__ansic_assignment_expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_initializer167"):
                opp_val = getattr(old_value, "ansic_initializer167", None)
                if opp_val == self:
                    setattr(old_value, "ansic_initializer167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_initializer167"):
                opp_val = getattr(value, "ansic_initializer167", None)
                setattr(value, "ansic_initializer167", self)

    @property
    def ansic_assignment_expression(self):
        return self.__ansic_assignment_expression

    @ansic_assignment_expression.setter
    def ansic_assignment_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression", None)
        self.__ansic_assignment_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_direct_declarator_complemento124"):
                opp_val = getattr(old_value, "ansic_direct_declarator_complemento124", None)
                if opp_val == self:
                    setattr(old_value, "ansic_direct_declarator_complemento124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_direct_declarator_complemento124"):
                opp_val = getattr(value, "ansic_direct_declarator_complemento124", None)
                setattr(value, "ansic_direct_declarator_complemento124", self)

    @property
    def ansic_assignment_expression446(self):
        return self.__ansic_assignment_expression446

    @ansic_assignment_expression446.setter
    def ansic_assignment_expression446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression446", None)
        self.__ansic_assignment_expression446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_unary_expression447"):
                opp_val = getattr(old_value, "ansic_unary_expression447", None)
                if opp_val == self:
                    setattr(old_value, "ansic_unary_expression447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_unary_expression447"):
                opp_val = getattr(value, "ansic_unary_expression447", None)
                setattr(value, "ansic_unary_expression447", self)

    @property
    def ansic_assignment_expression232(self):
        return self.__ansic_assignment_expression232

    @ansic_assignment_expression232.setter
    def ansic_assignment_expression232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression232", None)
        self.__ansic_assignment_expression232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_argument_expression_list231"):
                opp_val = getattr(old_value, "ansic_argument_expression_list231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_argument_expression_list231"):
                opp_val = getattr(value, "ansic_argument_expression_list231", None)
                if opp_val is None:
                    setattr(value, "ansic_argument_expression_list231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ansic_assignment_expression450(self):
        return self.__ansic_assignment_expression450

    @ansic_assignment_expression450.setter
    def ansic_assignment_expression450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression450", None)
        self.__ansic_assignment_expression450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_assignment_expression448"):
                opp_val = getattr(old_value, "ansic_assignment_expression448", None)
                if opp_val == self:
                    setattr(old_value, "ansic_assignment_expression448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_assignment_expression448"):
                opp_val = getattr(value, "ansic_assignment_expression448", None)
                setattr(value, "ansic_assignment_expression448", self)

    @property
    def ansic_assignment_expression159(self):
        return self.__ansic_assignment_expression159

    @ansic_assignment_expression159.setter
    def ansic_assignment_expression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression159", None)
        self.__ansic_assignment_expression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_direct_abstract_declarator158"):
                opp_val = getattr(old_value, "ansic_direct_abstract_declarator158", None)
                if opp_val == self:
                    setattr(old_value, "ansic_direct_abstract_declarator158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_direct_abstract_declarator158"):
                opp_val = getattr(value, "ansic_direct_abstract_declarator158", None)
                setattr(value, "ansic_direct_abstract_declarator158", self)

    @property
    def ansic_assignment_expression443(self):
        return self.__ansic_assignment_expression443

    @ansic_assignment_expression443.setter
    def ansic_assignment_expression443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_assignment_expression__ansic_assignment_expression443", None)
        self.__ansic_assignment_expression443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_conditional_expression444"):
                opp_val = getattr(old_value, "ansic_conditional_expression444", None)
                if opp_val == self:
                    setattr(old_value, "ansic_conditional_expression444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_conditional_expression444"):
                opp_val = getattr(value, "ansic_conditional_expression444", None)
                setattr(value, "ansic_conditional_expression444", self)

class ansic_direct_declarator_complemento:

    pass
class ansic_direct_declarator_linha:

    pass
class ansic_type_qualifier_list_linha:

    pass
class direct_abstract_declarator_complement:

    pass
class ansic_type_qualifier_list(direct_abstract_declarator_complement):

    pass
class ansic_direct_declarator:

    def __init__(self, identifier: str, ansic_direct_declarator: "ansic_declarator" = None, ansic_direct_declarator111: "ansic_direct_declarator_linha" = None, ansic_direct_declarator113: "ansic_declarator" = None):
        self.identifier = identifier
        self.ansic_direct_declarator = ansic_direct_declarator
        self.ansic_direct_declarator111 = ansic_direct_declarator111
        self.ansic_direct_declarator113 = ansic_direct_declarator113
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_direct_declarator111(self):
        return self.__ansic_direct_declarator111

    @ansic_direct_declarator111.setter
    def ansic_direct_declarator111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_direct_declarator__ansic_direct_declarator111", None)
        self.__ansic_direct_declarator111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_direct_declarator_linha"):
                opp_val = getattr(old_value, "ansic_direct_declarator_linha", None)
                if opp_val == self:
                    setattr(old_value, "ansic_direct_declarator_linha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_direct_declarator_linha"):
                opp_val = getattr(value, "ansic_direct_declarator_linha", None)
                setattr(value, "ansic_direct_declarator_linha", self)

    @property
    def ansic_direct_declarator(self):
        return self.__ansic_direct_declarator

    @ansic_direct_declarator.setter
    def ansic_direct_declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_direct_declarator__ansic_direct_declarator", None)
        self.__ansic_direct_declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declarator99"):
                opp_val = getattr(old_value, "ansic_declarator99", None)
                if opp_val == self:
                    setattr(old_value, "ansic_declarator99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declarator99"):
                opp_val = getattr(value, "ansic_declarator99", None)
                setattr(value, "ansic_declarator99", self)

    @property
    def ansic_direct_declarator113(self):
        return self.__ansic_direct_declarator113

    @ansic_direct_declarator113.setter
    def ansic_direct_declarator113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_direct_declarator__ansic_direct_declarator113", None)
        self.__ansic_direct_declarator113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declarator114"):
                opp_val = getattr(old_value, "ansic_declarator114", None)
                if opp_val == self:
                    setattr(old_value, "ansic_declarator114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declarator114"):
                opp_val = getattr(value, "ansic_declarator114", None)
                setattr(value, "ansic_declarator114", self)

class ansic_pointer:

    pass
class ansic_declaration_list_linha:

    pass
class ansic_compound_statement:

    pass
class ansic_declaration_list:

    pass
class ansic_init_declarator_list:

    pass
class ansic_declarator:

    pass
class ansic_struct_declarator_list_linha:

    pass
class ansic_struct_declarator:

    pass
class ansic_static_assert_declaration:

    pass
class ansic_struct_declarator_list:

    pass
class ansic_specifier_qualifier_list:

    pass
class ansic_struct_declaration_list_linha:

    pass
class ansic_struct_declaration:

    pass
class ansic_enumeration_constant:

    def __init__(self, identifier: str, ansic_enumeration_constant: "ansic_enumerator" = None):
        self.identifier = identifier
        self.ansic_enumeration_constant = ansic_enumeration_constant
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_enumeration_constant(self):
        return self.__ansic_enumeration_constant

    @ansic_enumeration_constant.setter
    def ansic_enumeration_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_enumeration_constant__ansic_enumeration_constant", None)
        self.__ansic_enumeration_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_enumerator34"):
                opp_val = getattr(old_value, "ansic_enumerator34", None)
                if opp_val == self:
                    setattr(old_value, "ansic_enumerator34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_enumerator34"):
                opp_val = getattr(value, "ansic_enumerator34", None)
                setattr(value, "ansic_enumerator34", self)

class ansic_enumerator_list_linha:

    pass
class ansic_enumerator:

    pass
class ansic_enumerator_list:

    pass
class ansic_enum_specifier:

    def __init__(self, identifier: str, ansic_enum_specifier: "ansic_type_specifier" = None, ansic_enum_specifier28: "ansic_enumerator_list" = None):
        self.identifier = identifier
        self.ansic_enum_specifier = ansic_enum_specifier
        self.ansic_enum_specifier28 = ansic_enum_specifier28
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_enum_specifier(self):
        return self.__ansic_enum_specifier

    @ansic_enum_specifier.setter
    def ansic_enum_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_enum_specifier__ansic_enum_specifier", None)
        self.__ansic_enum_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_specifier26"):
                opp_val = getattr(old_value, "ansic_type_specifier26", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_specifier26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_specifier26"):
                opp_val = getattr(value, "ansic_type_specifier26", None)
                setattr(value, "ansic_type_specifier26", self)

    @property
    def ansic_enum_specifier28(self):
        return self.__ansic_enum_specifier28

    @ansic_enum_specifier28.setter
    def ansic_enum_specifier28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_enum_specifier__ansic_enum_specifier28", None)
        self.__ansic_enum_specifier28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_enumerator_list"):
                opp_val = getattr(old_value, "ansic_enumerator_list", None)
                if opp_val == self:
                    setattr(old_value, "ansic_enumerator_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_enumerator_list"):
                opp_val = getattr(value, "ansic_enumerator_list", None)
                setattr(value, "ansic_enumerator_list", self)

class ansic_struct_or_union_specifier:

    def __init__(self, struct_or_union: str, identifier: str, ansic_struct_or_union_specifier42: "ansic_struct_declaration_list" = None, ansic_struct_or_union_specifier44: "ansic_struct_or_union_specifier_complement" = None, ansic_struct_or_union_specifier: "ansic_type_specifier" = None):
        self.struct_or_union = struct_or_union
        self.identifier = identifier
        self.ansic_struct_or_union_specifier42 = ansic_struct_or_union_specifier42
        self.ansic_struct_or_union_specifier44 = ansic_struct_or_union_specifier44
        self.ansic_struct_or_union_specifier = ansic_struct_or_union_specifier
        
    @property
    def struct_or_union(self) -> str:
        return self.__struct_or_union

    @struct_or_union.setter
    def struct_or_union(self, struct_or_union: str):
        self.__struct_or_union = struct_or_union

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ansic_struct_or_union_specifier(self):
        return self.__ansic_struct_or_union_specifier

    @ansic_struct_or_union_specifier.setter
    def ansic_struct_or_union_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_struct_or_union_specifier__ansic_struct_or_union_specifier", None)
        self.__ansic_struct_or_union_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_specifier24"):
                opp_val = getattr(old_value, "ansic_type_specifier24", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_specifier24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_specifier24"):
                opp_val = getattr(value, "ansic_type_specifier24", None)
                setattr(value, "ansic_type_specifier24", self)

    @property
    def ansic_struct_or_union_specifier44(self):
        return self.__ansic_struct_or_union_specifier44

    @ansic_struct_or_union_specifier44.setter
    def ansic_struct_or_union_specifier44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_struct_or_union_specifier__ansic_struct_or_union_specifier44", None)
        self.__ansic_struct_or_union_specifier44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_struct_or_union_specifier_complement"):
                opp_val = getattr(old_value, "ansic_struct_or_union_specifier_complement", None)
                if opp_val == self:
                    setattr(old_value, "ansic_struct_or_union_specifier_complement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_struct_or_union_specifier_complement"):
                opp_val = getattr(value, "ansic_struct_or_union_specifier_complement", None)
                setattr(value, "ansic_struct_or_union_specifier_complement", self)

    @property
    def ansic_struct_or_union_specifier42(self):
        return self.__ansic_struct_or_union_specifier42

    @ansic_struct_or_union_specifier42.setter
    def ansic_struct_or_union_specifier42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_struct_or_union_specifier__ansic_struct_or_union_specifier42", None)
        self.__ansic_struct_or_union_specifier42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_struct_declaration_list"):
                opp_val = getattr(old_value, "ansic_struct_declaration_list", None)
                if opp_val == self:
                    setattr(old_value, "ansic_struct_declaration_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_struct_declaration_list"):
                opp_val = getattr(value, "ansic_struct_declaration_list", None)
                setattr(value, "ansic_struct_declaration_list", self)

class ansic_atomic_type_specifier:

    pass
class ansic_constant_expression:

    pass
class ansic_type_name(postfix_expression):

    pass
class ansic_alignment_specifier:

    pass
class ansic_type_qualifier:

    def __init__(self, namez: str, ansic_type_qualifier: "ansic_declaration_specifiers" = None, ansic_type_qualifier72: "ansic_specifier_qualifier_list" = None, ansic_type_qualifier107: "ansic_type_qualifier_list" = None, ansic_type_qualifier508: "ansic_TypeQualifierListLinhaAtion" = None):
        self.namez = namez
        self.ansic_type_qualifier = ansic_type_qualifier
        self.ansic_type_qualifier72 = ansic_type_qualifier72
        self.ansic_type_qualifier107 = ansic_type_qualifier107
        self.ansic_type_qualifier508 = ansic_type_qualifier508
        
    @property
    def namez(self) -> str:
        return self.__namez

    @namez.setter
    def namez(self, namez: str):
        self.__namez = namez

    @property
    def ansic_type_qualifier508(self):
        return self.__ansic_type_qualifier508

    @ansic_type_qualifier508.setter
    def ansic_type_qualifier508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_qualifier__ansic_type_qualifier508", None)
        self.__ansic_type_qualifier508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_TypeQualifierListLinhaAtion"):
                opp_val = getattr(old_value, "ansic_TypeQualifierListLinhaAtion", None)
                if opp_val == self:
                    setattr(old_value, "ansic_TypeQualifierListLinhaAtion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_TypeQualifierListLinhaAtion"):
                opp_val = getattr(value, "ansic_TypeQualifierListLinhaAtion", None)
                setattr(value, "ansic_TypeQualifierListLinhaAtion", self)

    @property
    def ansic_type_qualifier(self):
        return self.__ansic_type_qualifier

    @ansic_type_qualifier.setter
    def ansic_type_qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_qualifier__ansic_type_qualifier", None)
        self.__ansic_type_qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declaration_specifiers14"):
                opp_val = getattr(old_value, "ansic_declaration_specifiers14", None)
                if opp_val == self:
                    setattr(old_value, "ansic_declaration_specifiers14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declaration_specifiers14"):
                opp_val = getattr(value, "ansic_declaration_specifiers14", None)
                setattr(value, "ansic_declaration_specifiers14", self)

    @property
    def ansic_type_qualifier72(self):
        return self.__ansic_type_qualifier72

    @ansic_type_qualifier72.setter
    def ansic_type_qualifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_qualifier__ansic_type_qualifier72", None)
        self.__ansic_type_qualifier72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_specifier_qualifier_list71"):
                opp_val = getattr(old_value, "ansic_specifier_qualifier_list71", None)
                if opp_val == self:
                    setattr(old_value, "ansic_specifier_qualifier_list71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_specifier_qualifier_list71"):
                opp_val = getattr(value, "ansic_specifier_qualifier_list71", None)
                setattr(value, "ansic_specifier_qualifier_list71", self)

    @property
    def ansic_type_qualifier107(self):
        return self.__ansic_type_qualifier107

    @ansic_type_qualifier107.setter
    def ansic_type_qualifier107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_qualifier__ansic_type_qualifier107", None)
        self.__ansic_type_qualifier107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_qualifier_list106"):
                opp_val = getattr(old_value, "ansic_type_qualifier_list106", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_qualifier_list106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_qualifier_list106"):
                opp_val = getattr(value, "ansic_type_qualifier_list106", None)
                setattr(value, "ansic_type_qualifier_list106", self)

class ansic_struct_or_union_specifier_complement:

    pass
class ansic_struct_declaration_list:

    pass
class ansic_declaration:

    pass
class ansic_function_definition:

    pass
class ansic_translation_unit_linha:

    pass
class ansic_external_declaration:

    pass
class ansic_translation_unit:

    pass
class ansic_DomainModel:

    pass
class ansic_type_specifier:

    def __init__(self, type_name_str: str, ansic_type_specifier: "ansic_declaration_specifiers" = None, ansic_type_specifier22: "ansic_atomic_type_specifier" = None, ansic_type_specifier24: "ansic_struct_or_union_specifier" = None, ansic_type_specifier26: "ansic_enum_specifier" = None, ansic_type_specifier66: "ansic_specifier_qualifier_list" = None):
        self.type_name_str = type_name_str
        self.ansic_type_specifier = ansic_type_specifier
        self.ansic_type_specifier22 = ansic_type_specifier22
        self.ansic_type_specifier24 = ansic_type_specifier24
        self.ansic_type_specifier26 = ansic_type_specifier26
        self.ansic_type_specifier66 = ansic_type_specifier66
        
    @property
    def type_name_str(self) -> str:
        return self.__type_name_str

    @type_name_str.setter
    def type_name_str(self, type_name_str: str):
        self.__type_name_str = type_name_str

    @property
    def ansic_type_specifier(self):
        return self.__ansic_type_specifier

    @ansic_type_specifier.setter
    def ansic_type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_specifier__ansic_type_specifier", None)
        self.__ansic_type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declaration_specifiers12"):
                opp_val = getattr(old_value, "ansic_declaration_specifiers12", None)
                if opp_val == self:
                    setattr(old_value, "ansic_declaration_specifiers12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declaration_specifiers12"):
                opp_val = getattr(value, "ansic_declaration_specifiers12", None)
                setattr(value, "ansic_declaration_specifiers12", self)

    @property
    def ansic_type_specifier24(self):
        return self.__ansic_type_specifier24

    @ansic_type_specifier24.setter
    def ansic_type_specifier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_specifier__ansic_type_specifier24", None)
        self.__ansic_type_specifier24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_struct_or_union_specifier"):
                opp_val = getattr(old_value, "ansic_struct_or_union_specifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_struct_or_union_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_struct_or_union_specifier"):
                opp_val = getattr(value, "ansic_struct_or_union_specifier", None)
                setattr(value, "ansic_struct_or_union_specifier", self)

    @property
    def ansic_type_specifier22(self):
        return self.__ansic_type_specifier22

    @ansic_type_specifier22.setter
    def ansic_type_specifier22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_specifier__ansic_type_specifier22", None)
        self.__ansic_type_specifier22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_atomic_type_specifier"):
                opp_val = getattr(old_value, "ansic_atomic_type_specifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_atomic_type_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_atomic_type_specifier"):
                opp_val = getattr(value, "ansic_atomic_type_specifier", None)
                setattr(value, "ansic_atomic_type_specifier", self)

    @property
    def ansic_type_specifier66(self):
        return self.__ansic_type_specifier66

    @ansic_type_specifier66.setter
    def ansic_type_specifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_specifier__ansic_type_specifier66", None)
        self.__ansic_type_specifier66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_specifier_qualifier_list65"):
                opp_val = getattr(old_value, "ansic_specifier_qualifier_list65", None)
                if opp_val == self:
                    setattr(old_value, "ansic_specifier_qualifier_list65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_specifier_qualifier_list65"):
                opp_val = getattr(value, "ansic_specifier_qualifier_list65", None)
                setattr(value, "ansic_specifier_qualifier_list65", self)

    @property
    def ansic_type_specifier26(self):
        return self.__ansic_type_specifier26

    @ansic_type_specifier26.setter
    def ansic_type_specifier26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_type_specifier__ansic_type_specifier26", None)
        self.__ansic_type_specifier26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_enum_specifier"):
                opp_val = getattr(old_value, "ansic_enum_specifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_enum_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_enum_specifier"):
                opp_val = getattr(value, "ansic_enum_specifier", None)
                setattr(value, "ansic_enum_specifier", self)

class ansic_declaration_specifiers:

    def __init__(self, storage_class_specifier: str, function_specifier: str, ansic_declaration_specifiers: "ansic_declaration_specifiers" = None, ansic_declaration_specifiers9: set["ansic_declaration_specifiers"] = None, ansic_declaration_specifiers12: "ansic_type_specifier" = None, ansic_declaration_specifiers14: "ansic_type_qualifier" = None, ansic_declaration_specifiers16: "ansic_alignment_specifier" = None, ansic_declaration_specifiers83: "ansic_function_definition" = None, ansic_declaration_specifiers75: "ansic_declaration" = None, ansic_declaration_specifiers140: "ansic_parameter_declaration" = None):
        self.storage_class_specifier = storage_class_specifier
        self.function_specifier = function_specifier
        self.ansic_declaration_specifiers = ansic_declaration_specifiers
        self.ansic_declaration_specifiers9 = ansic_declaration_specifiers9 if ansic_declaration_specifiers9 is not None else set()
        self.ansic_declaration_specifiers12 = ansic_declaration_specifiers12
        self.ansic_declaration_specifiers14 = ansic_declaration_specifiers14
        self.ansic_declaration_specifiers16 = ansic_declaration_specifiers16
        self.ansic_declaration_specifiers83 = ansic_declaration_specifiers83
        self.ansic_declaration_specifiers75 = ansic_declaration_specifiers75
        self.ansic_declaration_specifiers140 = ansic_declaration_specifiers140
        
    @property
    def storage_class_specifier(self) -> str:
        return self.__storage_class_specifier

    @storage_class_specifier.setter
    def storage_class_specifier(self, storage_class_specifier: str):
        self.__storage_class_specifier = storage_class_specifier

    @property
    def function_specifier(self) -> str:
        return self.__function_specifier

    @function_specifier.setter
    def function_specifier(self, function_specifier: str):
        self.__function_specifier = function_specifier

    @property
    def ansic_declaration_specifiers(self):
        return self.__ansic_declaration_specifiers

    @ansic_declaration_specifiers.setter
    def ansic_declaration_specifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers", None)
        self.__ansic_declaration_specifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declaration_specifiers9"):
                opp_val = getattr(old_value, "ansic_declaration_specifiers9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declaration_specifiers9"):
                opp_val = getattr(value, "ansic_declaration_specifiers9", None)
                if opp_val is None:
                    setattr(value, "ansic_declaration_specifiers9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ansic_declaration_specifiers14(self):
        return self.__ansic_declaration_specifiers14

    @ansic_declaration_specifiers14.setter
    def ansic_declaration_specifiers14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers14", None)
        self.__ansic_declaration_specifiers14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_qualifier"):
                opp_val = getattr(old_value, "ansic_type_qualifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_qualifier"):
                opp_val = getattr(value, "ansic_type_qualifier", None)
                setattr(value, "ansic_type_qualifier", self)

    @property
    def ansic_declaration_specifiers140(self):
        return self.__ansic_declaration_specifiers140

    @ansic_declaration_specifiers140.setter
    def ansic_declaration_specifiers140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers140", None)
        self.__ansic_declaration_specifiers140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_parameter_declaration139"):
                opp_val = getattr(old_value, "ansic_parameter_declaration139", None)
                if opp_val == self:
                    setattr(old_value, "ansic_parameter_declaration139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_parameter_declaration139"):
                opp_val = getattr(value, "ansic_parameter_declaration139", None)
                setattr(value, "ansic_parameter_declaration139", self)

    @property
    def ansic_declaration_specifiers75(self):
        return self.__ansic_declaration_specifiers75

    @ansic_declaration_specifiers75.setter
    def ansic_declaration_specifiers75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers75", None)
        self.__ansic_declaration_specifiers75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_declaration74"):
                opp_val = getattr(old_value, "ansic_declaration74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_declaration74"):
                opp_val = getattr(value, "ansic_declaration74", None)
                if opp_val is None:
                    setattr(value, "ansic_declaration74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ansic_declaration_specifiers9(self):
        return self.__ansic_declaration_specifiers9

    @ansic_declaration_specifiers9.setter
    def ansic_declaration_specifiers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers9", None)
        self.__ansic_declaration_specifiers9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ansic_declaration_specifiers"):
                    opp_val = getattr(item, "ansic_declaration_specifiers", None)
                    
                    if opp_val == self:
                        setattr(item, "ansic_declaration_specifiers", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ansic_declaration_specifiers"):
                    opp_val = getattr(item, "ansic_declaration_specifiers", None)
                    
                    setattr(item, "ansic_declaration_specifiers", self)
                    

    @property
    def ansic_declaration_specifiers83(self):
        return self.__ansic_declaration_specifiers83

    @ansic_declaration_specifiers83.setter
    def ansic_declaration_specifiers83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers83", None)
        self.__ansic_declaration_specifiers83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_function_definition82"):
                opp_val = getattr(old_value, "ansic_function_definition82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_function_definition82"):
                opp_val = getattr(value, "ansic_function_definition82", None)
                if opp_val is None:
                    setattr(value, "ansic_function_definition82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ansic_declaration_specifiers16(self):
        return self.__ansic_declaration_specifiers16

    @ansic_declaration_specifiers16.setter
    def ansic_declaration_specifiers16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers16", None)
        self.__ansic_declaration_specifiers16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_alignment_specifier"):
                opp_val = getattr(old_value, "ansic_alignment_specifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_alignment_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_alignment_specifier"):
                opp_val = getattr(value, "ansic_alignment_specifier", None)
                setattr(value, "ansic_alignment_specifier", self)

    @property
    def ansic_declaration_specifiers12(self):
        return self.__ansic_declaration_specifiers12

    @ansic_declaration_specifiers12.setter
    def ansic_declaration_specifiers12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ansic_declaration_specifiers__ansic_declaration_specifiers12", None)
        self.__ansic_declaration_specifiers12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ansic_type_specifier"):
                opp_val = getattr(old_value, "ansic_type_specifier", None)
                if opp_val == self:
                    setattr(old_value, "ansic_type_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ansic_type_specifier"):
                opp_val = getattr(value, "ansic_type_specifier", None)
                setattr(value, "ansic_type_specifier", self)

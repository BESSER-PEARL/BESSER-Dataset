from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class init_declarator_list_linha:

    pass
class myDsl_InitDecclaratorListLinhaAction(init_declarator_list_linha):

    pass
class unary_expression:

    pass
class myDsl_PlusPlus(unary_expression):

    def __init__(self, plus: str):
        self.plus = plus
        
    @property
    def plus(self) -> str:
        return self.__plus

    @plus.setter
    def plus(self, plus: str):
        self.__plus = plus

class initializer_list_linha:

    pass
class myDsl_InitializerListLinhaAction(initializer_list_linha):

    pass
class postfix_expression_linha:

    pass
class myDsl_PostfixExpressionLinhaAction(postfix_expression_linha):

    pass
class generic_assoc_list_linha:

    pass
class myDsl_GenericAssocListLinhaAction(generic_assoc_list_linha):

    pass
class translation_unit_linha:

    pass
class myDsl_TranlationUnitLinhaAction(translation_unit_linha):

    pass
class identifier_list_linha:

    pass
class myDsl_IdentifierListLinhaAction(identifier_list_linha):

    def __init__(self, identifier: str, myDsl_IdentifierListLinhaAction: "myDsl_identifier_list_linha" = None):
        self.identifier = identifier
        self.myDsl_IdentifierListLinhaAction = myDsl_IdentifierListLinhaAction
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_IdentifierListLinhaAction(self):
        return self.__myDsl_IdentifierListLinhaAction

    @myDsl_IdentifierListLinhaAction.setter
    def myDsl_IdentifierListLinhaAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierListLinhaAction__myDsl_IdentifierListLinhaAction", None)
        self.__myDsl_IdentifierListLinhaAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list_linha518"):
                opp_val = getattr(old_value, "myDsl_identifier_list_linha518", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list_linha518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list_linha518"):
                opp_val = getattr(value, "myDsl_identifier_list_linha518", None)
                setattr(value, "myDsl_identifier_list_linha518", self)

class argument_expression_list_linha:

    pass
class myDsl_ArgumentExpressionListLinhaAction(argument_expression_list_linha):

    pass
class postfix_expression_complement:

    pass
class myDsl_PostFixEmpryParams(postfix_expression_complement):

    pass
class designator_list_linha:

    pass
class myDsl_DesignatorListLinhaAction(designator_list_linha):

    pass
class struct_declarator_list_linha:

    pass
class myDsl_StructDeclaratorListLinhaAction(struct_declarator_list_linha):

    pass
class struct_declaration_list_linha:

    pass
class myDsl_StructDeclarationListLinhaAction(struct_declaration_list_linha):

    pass
class struct_or_union_specifier_complement:

    pass
class myDsl_StructOrUnionSpecifierComplementAction(struct_or_union_specifier_complement):

    pass
class enumerator_list_linha:

    pass
class myDsl_EnumeratorListLinhaAction(enumerator_list_linha):

    pass
class myDsl_string_dsl:

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

class direct_abstract_declarator_linha:

    pass
class myDsl_DirectAbstractDeclarratorLinhaAction(direct_abstract_declarator_linha):

    pass
class type_qualifier_list_linha:

    pass
class myDsl_TypeQualifierListLinhaAtion(type_qualifier_list_linha):

    pass
class declaration_list_linha:

    pass
class myDsl_DeclarationListLinhaAction(declaration_list_linha):

    pass
class myDsl_expression_linha:

    pass
class postfix_expression:

    pass
class myDsl_init_declarator:

    pass
class myDsl_logical_and_expression_linha:

    pass
class myDsl_logical_and_expression:

    pass
class myDsl_inclusive_or_expression_linha:

    pass
class myDsl_inclusive_or_expression:

    pass
class myDsl_exclusive_or_expression_linha:

    pass
class myDsl_exclusive_or_expression:

    pass
class myDsl_conditional_expression_linha:

    pass
class myDsl_logical_or_expression_linha:

    pass
class myDsl_logical_or_expression:

    pass
class myDsl_block_item_list_linha:

    pass
class myDsl_block_item:

    pass
class myDsl_block_item_list:

    pass
class myDsl_and_expression_linha:

    pass
class myDsl_and_expression:

    pass
class myDsl_jump_statement:

    def __init__(self, return_vazio: str, return: str, identifier: str, break: str, myDsl_jump_statement325: "myDsl_expression" = None, myDsl_jump_statement: "myDsl_statement" = None):
        self.return_vazio = return_vazio
        self.return = return
        self.identifier = identifier
        self.break = break
        self.myDsl_jump_statement325 = myDsl_jump_statement325
        self.myDsl_jump_statement = myDsl_jump_statement
        
    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def return_vazio(self) -> str:
        return self.__return_vazio

    @return_vazio.setter
    def return_vazio(self, return_vazio: str):
        self.__return_vazio = return_vazio

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

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
            if hasattr(old_value, "myDsl_statement323"):
                opp_val = getattr(old_value, "myDsl_statement323", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement323"):
                opp_val = getattr(value, "myDsl_statement323", None)
                setattr(value, "myDsl_statement323", self)

    @property
    def myDsl_jump_statement325(self):
        return self.__myDsl_jump_statement325

    @myDsl_jump_statement325.setter
    def myDsl_jump_statement325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_jump_statement__myDsl_jump_statement325", None)
        self.__myDsl_jump_statement325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression326"):
                opp_val = getattr(old_value, "myDsl_expression326", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression326"):
                opp_val = getattr(value, "myDsl_expression326", None)
                setattr(value, "myDsl_expression326", self)

class myDsl_iteration_statement:

    pass
class myDsl_selection_statement:

    pass
class myDsl_expression_statement:

    pass
class myDsl_labeled_statement:

    def __init__(self, identifier: str, myDsl_labeled_statement: "myDsl_statement" = None, myDsl_labeled_statement352: "myDsl_statement" = None, myDsl_labeled_statement355: "myDsl_conditional_expression" = None):
        self.identifier = identifier
        self.myDsl_labeled_statement = myDsl_labeled_statement
        self.myDsl_labeled_statement352 = myDsl_labeled_statement352
        self.myDsl_labeled_statement355 = myDsl_labeled_statement355
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_labeled_statement352(self):
        return self.__myDsl_labeled_statement352

    @myDsl_labeled_statement352.setter
    def myDsl_labeled_statement352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_labeled_statement__myDsl_labeled_statement352", None)
        self.__myDsl_labeled_statement352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_statement353"):
                opp_val = getattr(old_value, "myDsl_statement353", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_statement353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_statement353"):
                opp_val = getattr(value, "myDsl_statement353", None)
                setattr(value, "myDsl_statement353", self)

    @property
    def myDsl_labeled_statement355(self):
        return self.__myDsl_labeled_statement355

    @myDsl_labeled_statement355.setter
    def myDsl_labeled_statement355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_labeled_statement__myDsl_labeled_statement355", None)
        self.__myDsl_labeled_statement355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_conditional_expression356"):
                opp_val = getattr(old_value, "myDsl_conditional_expression356", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_conditional_expression356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_conditional_expression356"):
                opp_val = getattr(value, "myDsl_conditional_expression356", None)
                setattr(value, "myDsl_conditional_expression356", self)

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

class myDsl_statement:

    pass
class myDsl_equality_expression_complement:

    def __init__(self, igual: str, menor: str, maior: str, menor_igual: str, maior_igual: str, n_igual: str, myDsl_equality_expression_complement: "myDsl_equality_expression_linha" = None, myDsl_equality_expression_complement310: "myDsl_relational_expression" = None):
        self.igual = igual
        self.menor = menor
        self.maior = maior
        self.menor_igual = menor_igual
        self.maior_igual = maior_igual
        self.n_igual = n_igual
        self.myDsl_equality_expression_complement = myDsl_equality_expression_complement
        self.myDsl_equality_expression_complement310 = myDsl_equality_expression_complement310
        
    @property
    def menor(self) -> str:
        return self.__menor

    @menor.setter
    def menor(self, menor: str):
        self.__menor = menor

    @property
    def menor_igual(self) -> str:
        return self.__menor_igual

    @menor_igual.setter
    def menor_igual(self, menor_igual: str):
        self.__menor_igual = menor_igual

    @property
    def maior_igual(self) -> str:
        return self.__maior_igual

    @maior_igual.setter
    def maior_igual(self, maior_igual: str):
        self.__maior_igual = maior_igual

    @property
    def igual(self) -> str:
        return self.__igual

    @igual.setter
    def igual(self, igual: str):
        self.__igual = igual

    @property
    def n_igual(self) -> str:
        return self.__n_igual

    @n_igual.setter
    def n_igual(self, n_igual: str):
        self.__n_igual = n_igual

    @property
    def maior(self) -> str:
        return self.__maior

    @maior.setter
    def maior(self, maior: str):
        self.__maior = maior

    @property
    def myDsl_equality_expression_complement(self):
        return self.__myDsl_equality_expression_complement

    @myDsl_equality_expression_complement.setter
    def myDsl_equality_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_equality_expression_complement__myDsl_equality_expression_complement", None)
        self.__myDsl_equality_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_equality_expression_linha305"):
                opp_val = getattr(old_value, "myDsl_equality_expression_linha305", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_equality_expression_linha305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_equality_expression_linha305"):
                opp_val = getattr(value, "myDsl_equality_expression_linha305", None)
                setattr(value, "myDsl_equality_expression_linha305", self)

    @property
    def myDsl_equality_expression_complement310(self):
        return self.__myDsl_equality_expression_complement310

    @myDsl_equality_expression_complement310.setter
    def myDsl_equality_expression_complement310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_equality_expression_complement__myDsl_equality_expression_complement310", None)
        self.__myDsl_equality_expression_complement310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_relational_expression311"):
                opp_val = getattr(old_value, "myDsl_relational_expression311", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_relational_expression311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_relational_expression311"):
                opp_val = getattr(value, "myDsl_relational_expression311", None)
                setattr(value, "myDsl_relational_expression311", self)

class myDsl_equality_expression_linha:

    pass
class myDsl_shift_expression_complement:

    def __init__(self, sright: str, sleft: str, myDsl_shift_expression_complement294: "myDsl_relational_expression_linha" = None, myDsl_shift_expression_complement: "myDsl_shift_expression_linha" = None, myDsl_shift_expression_complement286: "myDsl_additive_expression" = None):
        self.sright = sright
        self.sleft = sleft
        self.myDsl_shift_expression_complement294 = myDsl_shift_expression_complement294
        self.myDsl_shift_expression_complement = myDsl_shift_expression_complement
        self.myDsl_shift_expression_complement286 = myDsl_shift_expression_complement286
        
    @property
    def sright(self) -> str:
        return self.__sright

    @sright.setter
    def sright(self, sright: str):
        self.__sright = sright

    @property
    def sleft(self) -> str:
        return self.__sleft

    @sleft.setter
    def sleft(self, sleft: str):
        self.__sleft = sleft

    @property
    def myDsl_shift_expression_complement(self):
        return self.__myDsl_shift_expression_complement

    @myDsl_shift_expression_complement.setter
    def myDsl_shift_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_shift_expression_complement__myDsl_shift_expression_complement", None)
        self.__myDsl_shift_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_shift_expression_linha281"):
                opp_val = getattr(old_value, "myDsl_shift_expression_linha281", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_shift_expression_linha281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_shift_expression_linha281"):
                opp_val = getattr(value, "myDsl_shift_expression_linha281", None)
                setattr(value, "myDsl_shift_expression_linha281", self)

    @property
    def myDsl_shift_expression_complement286(self):
        return self.__myDsl_shift_expression_complement286

    @myDsl_shift_expression_complement286.setter
    def myDsl_shift_expression_complement286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_shift_expression_complement__myDsl_shift_expression_complement286", None)
        self.__myDsl_shift_expression_complement286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_additive_expression287"):
                opp_val = getattr(old_value, "myDsl_additive_expression287", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_additive_expression287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_additive_expression287"):
                opp_val = getattr(value, "myDsl_additive_expression287", None)
                setattr(value, "myDsl_additive_expression287", self)

    @property
    def myDsl_shift_expression_complement294(self):
        return self.__myDsl_shift_expression_complement294

    @myDsl_shift_expression_complement294.setter
    def myDsl_shift_expression_complement294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_shift_expression_complement__myDsl_shift_expression_complement294", None)
        self.__myDsl_shift_expression_complement294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_relational_expression_linha293"):
                opp_val = getattr(old_value, "myDsl_relational_expression_linha293", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_relational_expression_linha293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_relational_expression_linha293"):
                opp_val = getattr(value, "myDsl_relational_expression_linha293", None)
                setattr(value, "myDsl_relational_expression_linha293", self)

class myDsl_shift_expression_linha:

    pass
class myDsl_shift_expression:

    pass
class myDsl_additive_expression_complement:

    def __init__(self, mais: str, menos: str, myDsl_additive_expression_complement: "myDsl_additive_expression_linha" = None, myDsl_additive_expression_complement274: "myDsl_multiplicative_expression" = None):
        self.mais = mais
        self.menos = menos
        self.myDsl_additive_expression_complement = myDsl_additive_expression_complement
        self.myDsl_additive_expression_complement274 = myDsl_additive_expression_complement274
        
    @property
    def mais(self) -> str:
        return self.__mais

    @mais.setter
    def mais(self, mais: str):
        self.__mais = mais

    @property
    def menos(self) -> str:
        return self.__menos

    @menos.setter
    def menos(self, menos: str):
        self.__menos = menos

    @property
    def myDsl_additive_expression_complement274(self):
        return self.__myDsl_additive_expression_complement274

    @myDsl_additive_expression_complement274.setter
    def myDsl_additive_expression_complement274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_additive_expression_complement__myDsl_additive_expression_complement274", None)
        self.__myDsl_additive_expression_complement274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_multiplicative_expression275"):
                opp_val = getattr(old_value, "myDsl_multiplicative_expression275", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_multiplicative_expression275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_multiplicative_expression275"):
                opp_val = getattr(value, "myDsl_multiplicative_expression275", None)
                setattr(value, "myDsl_multiplicative_expression275", self)

    @property
    def myDsl_additive_expression_complement(self):
        return self.__myDsl_additive_expression_complement

    @myDsl_additive_expression_complement.setter
    def myDsl_additive_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_additive_expression_complement__myDsl_additive_expression_complement", None)
        self.__myDsl_additive_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_additive_expression_linha269"):
                opp_val = getattr(old_value, "myDsl_additive_expression_linha269", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_additive_expression_linha269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_additive_expression_linha269"):
                opp_val = getattr(value, "myDsl_additive_expression_linha269", None)
                setattr(value, "myDsl_additive_expression_linha269", self)

class myDsl_additive_expression_linha:

    pass
class myDsl_additive_expression:

    pass
class myDsl_equality_expression:

    pass
class myDsl_relational_expression_complement:

    def __init__(self, menor: str, maior: str, menor_igual: str, maior_igual: str, myDsl_relational_expression_complement: "myDsl_shift_expression" = None):
        self.menor = menor
        self.maior = maior
        self.menor_igual = menor_igual
        self.maior_igual = maior_igual
        self.myDsl_relational_expression_complement = myDsl_relational_expression_complement
        
    @property
    def maior(self) -> str:
        return self.__maior

    @maior.setter
    def maior(self, maior: str):
        self.__maior = maior

    @property
    def maior_igual(self) -> str:
        return self.__maior_igual

    @maior_igual.setter
    def maior_igual(self, maior_igual: str):
        self.__maior_igual = maior_igual

    @property
    def menor_igual(self) -> str:
        return self.__menor_igual

    @menor_igual.setter
    def menor_igual(self, menor_igual: str):
        self.__menor_igual = menor_igual

    @property
    def menor(self) -> str:
        return self.__menor

    @menor.setter
    def menor(self, menor: str):
        self.__menor = menor

    @property
    def myDsl_relational_expression_complement(self):
        return self.__myDsl_relational_expression_complement

    @myDsl_relational_expression_complement.setter
    def myDsl_relational_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_relational_expression_complement__myDsl_relational_expression_complement", None)
        self.__myDsl_relational_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_shift_expression299"):
                opp_val = getattr(old_value, "myDsl_shift_expression299", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_shift_expression299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_shift_expression299"):
                opp_val = getattr(value, "myDsl_shift_expression299", None)
                setattr(value, "myDsl_shift_expression299", self)

class myDsl_relational_expression_linha:

    pass
class myDsl_relational_expression:

    pass
class myDsl_unary_expression:

    def __init__(self, unary_operator: str, myDsl_unary_expression239: "myDsl_cast_expression" = None, myDsl_unary_expression241: "myDsl_type_name" = None, myDsl_unary_expression245: "myDsl_cast_expression" = None, myDsl_unary_expression: "myDsl_postfix_expression" = None, myDsl_unary_expression237: "myDsl_unary_expression" = None, myDsl_unary_expression235: "myDsl_unary_expression" = None, myDsl_unary_expression447: "myDsl_assignment_expression" = None):
        self.unary_operator = unary_operator
        self.myDsl_unary_expression239 = myDsl_unary_expression239
        self.myDsl_unary_expression241 = myDsl_unary_expression241
        self.myDsl_unary_expression245 = myDsl_unary_expression245
        self.myDsl_unary_expression = myDsl_unary_expression
        self.myDsl_unary_expression237 = myDsl_unary_expression237
        self.myDsl_unary_expression235 = myDsl_unary_expression235
        self.myDsl_unary_expression447 = myDsl_unary_expression447
        
    @property
    def unary_operator(self) -> str:
        return self.__unary_operator

    @unary_operator.setter
    def unary_operator(self, unary_operator: str):
        self.__unary_operator = unary_operator

    @property
    def myDsl_unary_expression235(self):
        return self.__myDsl_unary_expression235

    @myDsl_unary_expression235.setter
    def myDsl_unary_expression235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression235", None)
        self.__myDsl_unary_expression235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression237"):
                opp_val = getattr(old_value, "myDsl_unary_expression237", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression237"):
                opp_val = getattr(value, "myDsl_unary_expression237", None)
                setattr(value, "myDsl_unary_expression237", self)

    @property
    def myDsl_unary_expression447(self):
        return self.__myDsl_unary_expression447

    @myDsl_unary_expression447.setter
    def myDsl_unary_expression447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression447", None)
        self.__myDsl_unary_expression447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression446"):
                opp_val = getattr(old_value, "myDsl_assignment_expression446", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression446"):
                opp_val = getattr(value, "myDsl_assignment_expression446", None)
                setattr(value, "myDsl_assignment_expression446", self)

    @property
    def myDsl_unary_expression239(self):
        return self.__myDsl_unary_expression239

    @myDsl_unary_expression239.setter
    def myDsl_unary_expression239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression239", None)
        self.__myDsl_unary_expression239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_cast_expression"):
                opp_val = getattr(old_value, "myDsl_cast_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_cast_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_cast_expression"):
                opp_val = getattr(value, "myDsl_cast_expression", None)
                setattr(value, "myDsl_cast_expression", self)

    @property
    def myDsl_unary_expression237(self):
        return self.__myDsl_unary_expression237

    @myDsl_unary_expression237.setter
    def myDsl_unary_expression237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression237", None)
        self.__myDsl_unary_expression237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression235"):
                opp_val = getattr(old_value, "myDsl_unary_expression235", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression235"):
                opp_val = getattr(value, "myDsl_unary_expression235", None)
                setattr(value, "myDsl_unary_expression235", self)

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
            if hasattr(old_value, "myDsl_cast_expression244"):
                opp_val = getattr(old_value, "myDsl_cast_expression244", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_cast_expression244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_cast_expression244"):
                opp_val = getattr(value, "myDsl_cast_expression244", None)
                setattr(value, "myDsl_cast_expression244", self)

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
            if hasattr(old_value, "myDsl_postfix_expression234"):
                opp_val = getattr(old_value, "myDsl_postfix_expression234", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_postfix_expression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_postfix_expression234"):
                opp_val = getattr(value, "myDsl_postfix_expression234", None)
                setattr(value, "myDsl_postfix_expression234", self)

    @property
    def myDsl_unary_expression241(self):
        return self.__myDsl_unary_expression241

    @myDsl_unary_expression241.setter
    def myDsl_unary_expression241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_unary_expression__myDsl_unary_expression241", None)
        self.__myDsl_unary_expression241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_name242"):
                opp_val = getattr(old_value, "myDsl_type_name242", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_name242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_name242"):
                opp_val = getattr(value, "myDsl_type_name242", None)
                setattr(value, "myDsl_type_name242", self)

class myDsl_argument_expression_list_linha:

    pass
class myDsl_argument_expression_list:

    pass
class myDsl_postfix_expression_complement:

    def __init__(self, identifier: str, myDsl_postfix_expression_complement: "myDsl_expression" = None, myDsl_postfix_expression_complement229: "myDsl_argument_expression_list" = None, myDsl_postfix_expression_complement530: "myDsl_PostfixExpressionLinhaAction" = None):
        self.identifier = identifier
        self.myDsl_postfix_expression_complement = myDsl_postfix_expression_complement
        self.myDsl_postfix_expression_complement229 = myDsl_postfix_expression_complement229
        self.myDsl_postfix_expression_complement530 = myDsl_postfix_expression_complement530
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_postfix_expression_complement530(self):
        return self.__myDsl_postfix_expression_complement530

    @myDsl_postfix_expression_complement530.setter
    def myDsl_postfix_expression_complement530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_postfix_expression_complement__myDsl_postfix_expression_complement530", None)
        self.__myDsl_postfix_expression_complement530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PostfixExpressionLinhaAction"):
                opp_val = getattr(old_value, "myDsl_PostfixExpressionLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PostfixExpressionLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PostfixExpressionLinhaAction"):
                opp_val = getattr(value, "myDsl_PostfixExpressionLinhaAction", None)
                setattr(value, "myDsl_PostfixExpressionLinhaAction", self)

    @property
    def myDsl_postfix_expression_complement(self):
        return self.__myDsl_postfix_expression_complement

    @myDsl_postfix_expression_complement.setter
    def myDsl_postfix_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_postfix_expression_complement__myDsl_postfix_expression_complement", None)
        self.__myDsl_postfix_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression227"):
                opp_val = getattr(old_value, "myDsl_expression227", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression227"):
                opp_val = getattr(value, "myDsl_expression227", None)
                setattr(value, "myDsl_expression227", self)

    @property
    def myDsl_postfix_expression_complement229(self):
        return self.__myDsl_postfix_expression_complement229

    @myDsl_postfix_expression_complement229.setter
    def myDsl_postfix_expression_complement229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_postfix_expression_complement__myDsl_postfix_expression_complement229", None)
        self.__myDsl_postfix_expression_complement229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_argument_expression_list"):
                opp_val = getattr(old_value, "myDsl_argument_expression_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_argument_expression_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_argument_expression_list"):
                opp_val = getattr(value, "myDsl_argument_expression_list", None)
                setattr(value, "myDsl_argument_expression_list", self)

class myDsl_conditional_expression:

    pass
class myDsl_multiplicative_expression_complement:

    def __init__(self, multiplica: str, divide: str, modulo: str, myDsl_multiplicative_expression_complement: "myDsl_multiplicative_expression_linha" = None, myDsl_multiplicative_expression_complement262: "myDsl_cast_expression" = None):
        self.multiplica = multiplica
        self.divide = divide
        self.modulo = modulo
        self.myDsl_multiplicative_expression_complement = myDsl_multiplicative_expression_complement
        self.myDsl_multiplicative_expression_complement262 = myDsl_multiplicative_expression_complement262
        
    @property
    def modulo(self) -> str:
        return self.__modulo

    @modulo.setter
    def modulo(self, modulo: str):
        self.__modulo = modulo

    @property
    def divide(self) -> str:
        return self.__divide

    @divide.setter
    def divide(self, divide: str):
        self.__divide = divide

    @property
    def multiplica(self) -> str:
        return self.__multiplica

    @multiplica.setter
    def multiplica(self, multiplica: str):
        self.__multiplica = multiplica

    @property
    def myDsl_multiplicative_expression_complement262(self):
        return self.__myDsl_multiplicative_expression_complement262

    @myDsl_multiplicative_expression_complement262.setter
    def myDsl_multiplicative_expression_complement262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_multiplicative_expression_complement__myDsl_multiplicative_expression_complement262", None)
        self.__myDsl_multiplicative_expression_complement262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_cast_expression263"):
                opp_val = getattr(old_value, "myDsl_cast_expression263", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_cast_expression263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_cast_expression263"):
                opp_val = getattr(value, "myDsl_cast_expression263", None)
                setattr(value, "myDsl_cast_expression263", self)

    @property
    def myDsl_multiplicative_expression_complement(self):
        return self.__myDsl_multiplicative_expression_complement

    @myDsl_multiplicative_expression_complement.setter
    def myDsl_multiplicative_expression_complement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_multiplicative_expression_complement__myDsl_multiplicative_expression_complement", None)
        self.__myDsl_multiplicative_expression_complement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_multiplicative_expression_linha257"):
                opp_val = getattr(old_value, "myDsl_multiplicative_expression_linha257", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_multiplicative_expression_linha257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_multiplicative_expression_linha257"):
                opp_val = getattr(value, "myDsl_multiplicative_expression_linha257", None)
                setattr(value, "myDsl_multiplicative_expression_linha257", self)

class myDsl_multiplicative_expression_linha:

    pass
class myDsl_multiplicative_expression:

    pass
class myDsl_cast_expression:

    pass
class myDsl_postfix_expression:

    pass
class myDsl_generic_assoc_list_linha:

    pass
class myDsl_generic_association:

    def __init__(self, default: str, myDsl_generic_association: "myDsl_generic_assoc_list" = None, myDsl_generic_association194: "myDsl_type_name" = None, myDsl_generic_association197: "myDsl_assignment_expression" = None, myDsl_generic_association525: "myDsl_GenericAssocListLinhaAction" = None):
        self.default = default
        self.myDsl_generic_association = myDsl_generic_association
        self.myDsl_generic_association194 = myDsl_generic_association194
        self.myDsl_generic_association197 = myDsl_generic_association197
        self.myDsl_generic_association525 = myDsl_generic_association525
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def myDsl_generic_association197(self):
        return self.__myDsl_generic_association197

    @myDsl_generic_association197.setter
    def myDsl_generic_association197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association197", None)
        self.__myDsl_generic_association197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression198"):
                opp_val = getattr(old_value, "myDsl_assignment_expression198", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression198"):
                opp_val = getattr(value, "myDsl_assignment_expression198", None)
                setattr(value, "myDsl_assignment_expression198", self)

    @property
    def myDsl_generic_association194(self):
        return self.__myDsl_generic_association194

    @myDsl_generic_association194.setter
    def myDsl_generic_association194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association194", None)
        self.__myDsl_generic_association194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_name195"):
                opp_val = getattr(old_value, "myDsl_type_name195", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_name195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_name195"):
                opp_val = getattr(value, "myDsl_type_name195", None)
                setattr(value, "myDsl_type_name195", self)

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
            if hasattr(old_value, "myDsl_generic_assoc_list190"):
                opp_val = getattr(old_value, "myDsl_generic_assoc_list190", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_assoc_list190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_assoc_list190"):
                opp_val = getattr(value, "myDsl_generic_assoc_list190", None)
                setattr(value, "myDsl_generic_assoc_list190", self)

    @property
    def myDsl_generic_association525(self):
        return self.__myDsl_generic_association525

    @myDsl_generic_association525.setter
    def myDsl_generic_association525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_association__myDsl_generic_association525", None)
        self.__myDsl_generic_association525 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GenericAssocListLinhaAction"):
                opp_val = getattr(old_value, "myDsl_GenericAssocListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GenericAssocListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GenericAssocListLinhaAction"):
                opp_val = getattr(value, "myDsl_GenericAssocListLinhaAction", None)
                setattr(value, "myDsl_GenericAssocListLinhaAction", self)

class myDsl_generic_assoc_list:

    pass
class myDsl_generic_selection:

    def __init__(self, _generic: str, myDsl_generic_selection: "myDsl_primary_expression" = None, myDsl_generic_selection185: "myDsl_assignment_expression" = None, myDsl_generic_selection188: set["myDsl_generic_assoc_list"] = None):
        self._generic = _generic
        self.myDsl_generic_selection = myDsl_generic_selection
        self.myDsl_generic_selection185 = myDsl_generic_selection185
        self.myDsl_generic_selection188 = myDsl_generic_selection188 if myDsl_generic_selection188 is not None else set()
        
    @property
    def _generic(self) -> str:
        return self.___generic

    @_generic.setter
    def _generic(self, _generic: str):
        self.___generic = _generic

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
            if hasattr(old_value, "myDsl_primary_expression183"):
                opp_val = getattr(old_value, "myDsl_primary_expression183", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_primary_expression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_primary_expression183"):
                opp_val = getattr(value, "myDsl_primary_expression183", None)
                setattr(value, "myDsl_primary_expression183", self)

    @property
    def myDsl_generic_selection185(self):
        return self.__myDsl_generic_selection185

    @myDsl_generic_selection185.setter
    def myDsl_generic_selection185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_selection__myDsl_generic_selection185", None)
        self.__myDsl_generic_selection185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression186"):
                opp_val = getattr(old_value, "myDsl_assignment_expression186", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression186"):
                opp_val = getattr(value, "myDsl_assignment_expression186", None)
                setattr(value, "myDsl_assignment_expression186", self)

    @property
    def myDsl_generic_selection188(self):
        return self.__myDsl_generic_selection188

    @myDsl_generic_selection188.setter
    def myDsl_generic_selection188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_generic_selection__myDsl_generic_selection188", None)
        self.__myDsl_generic_selection188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_generic_assoc_list"):
                    opp_val = getattr(item, "myDsl_generic_assoc_list", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_generic_assoc_list", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_generic_assoc_list"):
                    opp_val = getattr(item, "myDsl_generic_assoc_list", None)
                    
                    setattr(item, "myDsl_generic_assoc_list", self)
                    

class myDsl_expression:

    pass
class myDsl_constant:

    def __init__(self, i_constant: int, f_constant: str, char: str, string: str, enumz: str, myDsl_constant: "myDsl_primary_expression" = None):
        self.i_constant = i_constant
        self.f_constant = f_constant
        self.char = char
        self.string = string
        self.enumz = enumz
        self.myDsl_constant = myDsl_constant
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def f_constant(self) -> str:
        return self.__f_constant

    @f_constant.setter
    def f_constant(self, f_constant: str):
        self.__f_constant = f_constant

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

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
    def myDsl_constant(self):
        return self.__myDsl_constant

    @myDsl_constant.setter
    def myDsl_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_constant__myDsl_constant", None)
        self.__myDsl_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_primary_expression"):
                opp_val = getattr(old_value, "myDsl_primary_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_primary_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_primary_expression"):
                opp_val = getattr(value, "myDsl_primary_expression", None)
                setattr(value, "myDsl_primary_expression", self)

class myDsl_designator_list_linha:

    pass
class myDsl_designator:

    def __init__(self, identifier: str, myDsl_designator: "myDsl_designator_list" = None, myDsl_designator222: "myDsl_conditional_expression" = None, myDsl_designator540: "myDsl_DesignatorListLinhaAction" = None):
        self.identifier = identifier
        self.myDsl_designator = myDsl_designator
        self.myDsl_designator222 = myDsl_designator222
        self.myDsl_designator540 = myDsl_designator540
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

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
            if hasattr(old_value, "myDsl_designator_list218"):
                opp_val = getattr(old_value, "myDsl_designator_list218", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_designator_list218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_designator_list218"):
                opp_val = getattr(value, "myDsl_designator_list218", None)
                setattr(value, "myDsl_designator_list218", self)

    @property
    def myDsl_designator222(self):
        return self.__myDsl_designator222

    @myDsl_designator222.setter
    def myDsl_designator222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_designator__myDsl_designator222", None)
        self.__myDsl_designator222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_conditional_expression"):
                opp_val = getattr(old_value, "myDsl_conditional_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_conditional_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_conditional_expression"):
                opp_val = getattr(value, "myDsl_conditional_expression", None)
                setattr(value, "myDsl_conditional_expression", self)

    @property
    def myDsl_designator540(self):
        return self.__myDsl_designator540

    @myDsl_designator540.setter
    def myDsl_designator540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_designator__myDsl_designator540", None)
        self.__myDsl_designator540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DesignatorListLinhaAction"):
                opp_val = getattr(old_value, "myDsl_DesignatorListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DesignatorListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DesignatorListLinhaAction"):
                opp_val = getattr(value, "myDsl_DesignatorListLinhaAction", None)
                setattr(value, "myDsl_DesignatorListLinhaAction", self)

class myDsl_primary_expression:

    def __init__(self, identifier: str, myDsl_primary_expression: "myDsl_constant" = None, myDsl_primary_expression181: "myDsl_expression" = None, myDsl_primary_expression183: "myDsl_generic_selection" = None, myDsl_primary_expression200: "myDsl_postfix_expression" = None):
        self.identifier = identifier
        self.myDsl_primary_expression = myDsl_primary_expression
        self.myDsl_primary_expression181 = myDsl_primary_expression181
        self.myDsl_primary_expression183 = myDsl_primary_expression183
        self.myDsl_primary_expression200 = myDsl_primary_expression200
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_primary_expression(self):
        return self.__myDsl_primary_expression

    @myDsl_primary_expression.setter
    def myDsl_primary_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_primary_expression__myDsl_primary_expression", None)
        self.__myDsl_primary_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_constant"):
                opp_val = getattr(old_value, "myDsl_constant", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_constant"):
                opp_val = getattr(value, "myDsl_constant", None)
                setattr(value, "myDsl_constant", self)

    @property
    def myDsl_primary_expression183(self):
        return self.__myDsl_primary_expression183

    @myDsl_primary_expression183.setter
    def myDsl_primary_expression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_primary_expression__myDsl_primary_expression183", None)
        self.__myDsl_primary_expression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_selection"):
                opp_val = getattr(old_value, "myDsl_generic_selection", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_selection"):
                opp_val = getattr(value, "myDsl_generic_selection", None)
                setattr(value, "myDsl_generic_selection", self)

    @property
    def myDsl_primary_expression181(self):
        return self.__myDsl_primary_expression181

    @myDsl_primary_expression181.setter
    def myDsl_primary_expression181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_primary_expression__myDsl_primary_expression181", None)
        self.__myDsl_primary_expression181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression"):
                opp_val = getattr(old_value, "myDsl_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression"):
                opp_val = getattr(value, "myDsl_expression", None)
                setattr(value, "myDsl_expression", self)

    @property
    def myDsl_primary_expression200(self):
        return self.__myDsl_primary_expression200

    @myDsl_primary_expression200.setter
    def myDsl_primary_expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_primary_expression__myDsl_primary_expression200", None)
        self.__myDsl_primary_expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_postfix_expression"):
                opp_val = getattr(old_value, "myDsl_postfix_expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_postfix_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_postfix_expression"):
                opp_val = getattr(value, "myDsl_postfix_expression", None)
                setattr(value, "myDsl_postfix_expression", self)

class myDsl_designator_list:

    pass
class myDsl_initializer_list_complement:

    pass
class myDsl_initializer_list_linha:

    pass
class myDsl_init_declarator_list_linha:

    pass
class myDsl_designation:

    pass
class myDsl_postfix_expression_linha:

    pass
class myDsl_direct_abstract_declarator_complement:

    pass
class myDsl_initializer_list:

    pass
class myDsl_initializer:

    pass
class myDsl_direct_abstract_declarator_linha:

    pass
class myDsl_direct_abstract_declarator:

    pass
class myDsl_identifier_list_linha:

    pass
class myDsl_parameter_lista:

    pass
class myDsl_identifier_list:

    def __init__(self, identifier: str, myDsl_identifier_list: "myDsl_direct_declarator_complemento" = None, myDsl_identifier_list178: "myDsl_identifier_list_linha" = None):
        self.identifier = identifier
        self.myDsl_identifier_list = myDsl_identifier_list
        self.myDsl_identifier_list178 = myDsl_identifier_list178
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

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
            if hasattr(old_value, "myDsl_direct_declarator_complemento128"):
                opp_val = getattr(old_value, "myDsl_direct_declarator_complemento128", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator_complemento128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator_complemento128"):
                opp_val = getattr(value, "myDsl_direct_declarator_complemento128", None)
                setattr(value, "myDsl_direct_declarator_complemento128", self)

    @property
    def myDsl_identifier_list178(self):
        return self.__myDsl_identifier_list178

    @myDsl_identifier_list178.setter
    def myDsl_identifier_list178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_identifier_list__myDsl_identifier_list178", None)
        self.__myDsl_identifier_list178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_identifier_list_linha"):
                opp_val = getattr(old_value, "myDsl_identifier_list_linha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_identifier_list_linha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_identifier_list_linha"):
                opp_val = getattr(value, "myDsl_identifier_list_linha", None)
                setattr(value, "myDsl_identifier_list_linha", self)

class myDsl_parameter_type_list:

    pass
class myDsl_assignment_expression:

    def __init__(self, assignment_operator: str, myDsl_assignment_expression: "myDsl_direct_declarator_complemento" = None, myDsl_assignment_expression159: "myDsl_direct_abstract_declarator" = None, myDsl_assignment_expression168: "myDsl_initializer" = None, myDsl_assignment_expression170: "myDsl_direct_abstract_declarator_complement" = None, myDsl_assignment_expression186: "myDsl_generic_selection" = None, myDsl_assignment_expression198: "myDsl_generic_association" = None, myDsl_assignment_expression232: "myDsl_argument_expression_list" = None, myDsl_assignment_expression467: "myDsl_expression_linha" = None, myDsl_assignment_expression443: "myDsl_conditional_expression" = None, myDsl_assignment_expression446: "myDsl_unary_expression" = None, myDsl_assignment_expression450: "myDsl_assignment_expression" = None, myDsl_assignment_expression448: "myDsl_assignment_expression" = None, myDsl_assignment_expression462: "myDsl_expression" = None, myDsl_assignment_expression545: "myDsl_ArgumentExpressionListLinhaAction" = None):
        self.assignment_operator = assignment_operator
        self.myDsl_assignment_expression = myDsl_assignment_expression
        self.myDsl_assignment_expression159 = myDsl_assignment_expression159
        self.myDsl_assignment_expression168 = myDsl_assignment_expression168
        self.myDsl_assignment_expression170 = myDsl_assignment_expression170
        self.myDsl_assignment_expression186 = myDsl_assignment_expression186
        self.myDsl_assignment_expression198 = myDsl_assignment_expression198
        self.myDsl_assignment_expression232 = myDsl_assignment_expression232
        self.myDsl_assignment_expression467 = myDsl_assignment_expression467
        self.myDsl_assignment_expression443 = myDsl_assignment_expression443
        self.myDsl_assignment_expression446 = myDsl_assignment_expression446
        self.myDsl_assignment_expression450 = myDsl_assignment_expression450
        self.myDsl_assignment_expression448 = myDsl_assignment_expression448
        self.myDsl_assignment_expression462 = myDsl_assignment_expression462
        self.myDsl_assignment_expression545 = myDsl_assignment_expression545
        
    @property
    def assignment_operator(self) -> str:
        return self.__assignment_operator

    @assignment_operator.setter
    def assignment_operator(self, assignment_operator: str):
        self.__assignment_operator = assignment_operator

    @property
    def myDsl_assignment_expression198(self):
        return self.__myDsl_assignment_expression198

    @myDsl_assignment_expression198.setter
    def myDsl_assignment_expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression198", None)
        self.__myDsl_assignment_expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_association197"):
                opp_val = getattr(old_value, "myDsl_generic_association197", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_association197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_association197"):
                opp_val = getattr(value, "myDsl_generic_association197", None)
                setattr(value, "myDsl_generic_association197", self)

    @property
    def myDsl_assignment_expression467(self):
        return self.__myDsl_assignment_expression467

    @myDsl_assignment_expression467.setter
    def myDsl_assignment_expression467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression467", None)
        self.__myDsl_assignment_expression467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression_linha466"):
                opp_val = getattr(old_value, "myDsl_expression_linha466", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression_linha466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression_linha466"):
                opp_val = getattr(value, "myDsl_expression_linha466", None)
                setattr(value, "myDsl_expression_linha466", self)

    @property
    def myDsl_assignment_expression443(self):
        return self.__myDsl_assignment_expression443

    @myDsl_assignment_expression443.setter
    def myDsl_assignment_expression443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression443", None)
        self.__myDsl_assignment_expression443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_conditional_expression444"):
                opp_val = getattr(old_value, "myDsl_conditional_expression444", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_conditional_expression444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_conditional_expression444"):
                opp_val = getattr(value, "myDsl_conditional_expression444", None)
                setattr(value, "myDsl_conditional_expression444", self)

    @property
    def myDsl_assignment_expression170(self):
        return self.__myDsl_assignment_expression170

    @myDsl_assignment_expression170.setter
    def myDsl_assignment_expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression170", None)
        self.__myDsl_assignment_expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_abstract_declarator_complement"):
                opp_val = getattr(old_value, "myDsl_direct_abstract_declarator_complement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_abstract_declarator_complement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_abstract_declarator_complement"):
                opp_val = getattr(value, "myDsl_direct_abstract_declarator_complement", None)
                setattr(value, "myDsl_direct_abstract_declarator_complement", self)

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
            if hasattr(old_value, "myDsl_direct_declarator_complemento124"):
                opp_val = getattr(old_value, "myDsl_direct_declarator_complemento124", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator_complemento124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator_complemento124"):
                opp_val = getattr(value, "myDsl_direct_declarator_complemento124", None)
                setattr(value, "myDsl_direct_declarator_complemento124", self)

    @property
    def myDsl_assignment_expression446(self):
        return self.__myDsl_assignment_expression446

    @myDsl_assignment_expression446.setter
    def myDsl_assignment_expression446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression446", None)
        self.__myDsl_assignment_expression446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_unary_expression447"):
                opp_val = getattr(old_value, "myDsl_unary_expression447", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_unary_expression447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_unary_expression447"):
                opp_val = getattr(value, "myDsl_unary_expression447", None)
                setattr(value, "myDsl_unary_expression447", self)

    @property
    def myDsl_assignment_expression448(self):
        return self.__myDsl_assignment_expression448

    @myDsl_assignment_expression448.setter
    def myDsl_assignment_expression448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression448", None)
        self.__myDsl_assignment_expression448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression450"):
                opp_val = getattr(old_value, "myDsl_assignment_expression450", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression450"):
                opp_val = getattr(value, "myDsl_assignment_expression450", None)
                setattr(value, "myDsl_assignment_expression450", self)

    @property
    def myDsl_assignment_expression545(self):
        return self.__myDsl_assignment_expression545

    @myDsl_assignment_expression545.setter
    def myDsl_assignment_expression545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression545", None)
        self.__myDsl_assignment_expression545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ArgumentExpressionListLinhaAction"):
                opp_val = getattr(old_value, "myDsl_ArgumentExpressionListLinhaAction", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ArgumentExpressionListLinhaAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ArgumentExpressionListLinhaAction"):
                opp_val = getattr(value, "myDsl_ArgumentExpressionListLinhaAction", None)
                setattr(value, "myDsl_ArgumentExpressionListLinhaAction", self)

    @property
    def myDsl_assignment_expression450(self):
        return self.__myDsl_assignment_expression450

    @myDsl_assignment_expression450.setter
    def myDsl_assignment_expression450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression450", None)
        self.__myDsl_assignment_expression450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assignment_expression448"):
                opp_val = getattr(old_value, "myDsl_assignment_expression448", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assignment_expression448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assignment_expression448"):
                opp_val = getattr(value, "myDsl_assignment_expression448", None)
                setattr(value, "myDsl_assignment_expression448", self)

    @property
    def myDsl_assignment_expression186(self):
        return self.__myDsl_assignment_expression186

    @myDsl_assignment_expression186.setter
    def myDsl_assignment_expression186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression186", None)
        self.__myDsl_assignment_expression186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_generic_selection185"):
                opp_val = getattr(old_value, "myDsl_generic_selection185", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_generic_selection185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_generic_selection185"):
                opp_val = getattr(value, "myDsl_generic_selection185", None)
                setattr(value, "myDsl_generic_selection185", self)

    @property
    def myDsl_assignment_expression159(self):
        return self.__myDsl_assignment_expression159

    @myDsl_assignment_expression159.setter
    def myDsl_assignment_expression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression159", None)
        self.__myDsl_assignment_expression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_abstract_declarator158"):
                opp_val = getattr(old_value, "myDsl_direct_abstract_declarator158", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_abstract_declarator158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_abstract_declarator158"):
                opp_val = getattr(value, "myDsl_direct_abstract_declarator158", None)
                setattr(value, "myDsl_direct_abstract_declarator158", self)

    @property
    def myDsl_assignment_expression232(self):
        return self.__myDsl_assignment_expression232

    @myDsl_assignment_expression232.setter
    def myDsl_assignment_expression232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression232", None)
        self.__myDsl_assignment_expression232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_argument_expression_list231"):
                opp_val = getattr(old_value, "myDsl_argument_expression_list231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_argument_expression_list231"):
                opp_val = getattr(value, "myDsl_argument_expression_list231", None)
                if opp_val is None:
                    setattr(value, "myDsl_argument_expression_list231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_assignment_expression168(self):
        return self.__myDsl_assignment_expression168

    @myDsl_assignment_expression168.setter
    def myDsl_assignment_expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression168", None)
        self.__myDsl_assignment_expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_initializer167"):
                opp_val = getattr(old_value, "myDsl_initializer167", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_initializer167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_initializer167"):
                opp_val = getattr(value, "myDsl_initializer167", None)
                setattr(value, "myDsl_initializer167", self)

    @property
    def myDsl_assignment_expression462(self):
        return self.__myDsl_assignment_expression462

    @myDsl_assignment_expression462.setter
    def myDsl_assignment_expression462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assignment_expression__myDsl_assignment_expression462", None)
        self.__myDsl_assignment_expression462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_expression461"):
                opp_val = getattr(old_value, "myDsl_expression461", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_expression461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_expression461"):
                opp_val = getattr(value, "myDsl_expression461", None)
                setattr(value, "myDsl_expression461", self)

class myDsl_direct_declarator_complemento:

    pass
class myDsl_direct_declarator_linha:

    pass
class myDsl_type_qualifier_list_linha:

    pass
class direct_abstract_declarator_complement:

    pass
class myDsl_abstract_declarator:

    pass
class myDsl_parameter_list_linha:

    pass
class myDsl_parameter_declaration:

    pass
class myDsl_compound_statement:

    pass
class myDsl_declaration_list:

    pass
class myDsl_init_declarator_list:

    pass
class myDsl_declarator:

    pass
class myDsl_struct_declarator_list_linha:

    pass
class myDsl_type_qualifier_list(direct_abstract_declarator_complement):

    pass
class myDsl_direct_declarator:

    def __init__(self, identifier: str, myDsl_direct_declarator: "myDsl_declarator" = None, myDsl_direct_declarator111: "myDsl_direct_declarator_linha" = None, myDsl_direct_declarator113: "myDsl_declarator" = None):
        self.identifier = identifier
        self.myDsl_direct_declarator = myDsl_direct_declarator
        self.myDsl_direct_declarator111 = myDsl_direct_declarator111
        self.myDsl_direct_declarator113 = myDsl_direct_declarator113
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

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
            if hasattr(old_value, "myDsl_declarator99"):
                opp_val = getattr(old_value, "myDsl_declarator99", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declarator99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declarator99"):
                opp_val = getattr(value, "myDsl_declarator99", None)
                setattr(value, "myDsl_declarator99", self)

    @property
    def myDsl_direct_declarator111(self):
        return self.__myDsl_direct_declarator111

    @myDsl_direct_declarator111.setter
    def myDsl_direct_declarator111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator__myDsl_direct_declarator111", None)
        self.__myDsl_direct_declarator111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_direct_declarator_linha"):
                opp_val = getattr(old_value, "myDsl_direct_declarator_linha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_direct_declarator_linha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_direct_declarator_linha"):
                opp_val = getattr(value, "myDsl_direct_declarator_linha", None)
                setattr(value, "myDsl_direct_declarator_linha", self)

    @property
    def myDsl_direct_declarator113(self):
        return self.__myDsl_direct_declarator113

    @myDsl_direct_declarator113.setter
    def myDsl_direct_declarator113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_direct_declarator__myDsl_direct_declarator113", None)
        self.__myDsl_direct_declarator113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declarator114"):
                opp_val = getattr(old_value, "myDsl_declarator114", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declarator114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declarator114"):
                opp_val = getattr(value, "myDsl_declarator114", None)
                setattr(value, "myDsl_declarator114", self)

class myDsl_pointer:

    pass
class myDsl_declaration_list_linha:

    pass
class myDsl_struct_or_union_specifier_complement:

    pass
class myDsl_struct_declaration_list:

    pass
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
            if hasattr(old_value, "myDsl_enumerator34"):
                opp_val = getattr(old_value, "myDsl_enumerator34", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_enumerator34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_enumerator34"):
                opp_val = getattr(value, "myDsl_enumerator34", None)
                setattr(value, "myDsl_enumerator34", self)

class myDsl_enumerator_list_linha:

    pass
class myDsl_enumerator:

    pass
class myDsl_enumerator_list:

    pass
class myDsl_enum_specifier:

    def __init__(self, identifier: str, myDsl_enum_specifier: "myDsl_type_specifier" = None, myDsl_enum_specifier28: "myDsl_enumerator_list" = None):
        self.identifier = identifier
        self.myDsl_enum_specifier = myDsl_enum_specifier
        self.myDsl_enum_specifier28 = myDsl_enum_specifier28
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def myDsl_enum_specifier28(self):
        return self.__myDsl_enum_specifier28

    @myDsl_enum_specifier28.setter
    def myDsl_enum_specifier28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_enum_specifier__myDsl_enum_specifier28", None)
        self.__myDsl_enum_specifier28 = value
        
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
            if hasattr(old_value, "myDsl_type_specifier26"):
                opp_val = getattr(old_value, "myDsl_type_specifier26", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier26"):
                opp_val = getattr(value, "myDsl_type_specifier26", None)
                setattr(value, "myDsl_type_specifier26", self)

class myDsl_struct_or_union_specifier:

    def __init__(self, struct_or_union: str, identifier: str, myDsl_struct_or_union_specifier: "myDsl_type_specifier" = None, myDsl_struct_or_union_specifier42: "myDsl_struct_declaration_list" = None, myDsl_struct_or_union_specifier44: "myDsl_struct_or_union_specifier_complement" = None):
        self.struct_or_union = struct_or_union
        self.identifier = identifier
        self.myDsl_struct_or_union_specifier = myDsl_struct_or_union_specifier
        self.myDsl_struct_or_union_specifier42 = myDsl_struct_or_union_specifier42
        self.myDsl_struct_or_union_specifier44 = myDsl_struct_or_union_specifier44
        
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
    def myDsl_struct_or_union_specifier(self):
        return self.__myDsl_struct_or_union_specifier

    @myDsl_struct_or_union_specifier.setter
    def myDsl_struct_or_union_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier", None)
        self.__myDsl_struct_or_union_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier24"):
                opp_val = getattr(old_value, "myDsl_type_specifier24", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier24"):
                opp_val = getattr(value, "myDsl_type_specifier24", None)
                setattr(value, "myDsl_type_specifier24", self)

    @property
    def myDsl_struct_or_union_specifier44(self):
        return self.__myDsl_struct_or_union_specifier44

    @myDsl_struct_or_union_specifier44.setter
    def myDsl_struct_or_union_specifier44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier44", None)
        self.__myDsl_struct_or_union_specifier44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_struct_or_union_specifier_complement"):
                opp_val = getattr(old_value, "myDsl_struct_or_union_specifier_complement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_struct_or_union_specifier_complement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_struct_or_union_specifier_complement"):
                opp_val = getattr(value, "myDsl_struct_or_union_specifier_complement", None)
                setattr(value, "myDsl_struct_or_union_specifier_complement", self)

    @property
    def myDsl_struct_or_union_specifier42(self):
        return self.__myDsl_struct_or_union_specifier42

    @myDsl_struct_or_union_specifier42.setter
    def myDsl_struct_or_union_specifier42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_struct_or_union_specifier__myDsl_struct_or_union_specifier42", None)
        self.__myDsl_struct_or_union_specifier42 = value
        
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

class myDsl_atomic_type_specifier:

    pass
class myDsl_struct_declarator:

    pass
class myDsl_static_assert_declaration:

    pass
class myDsl_struct_declarator_list:

    pass
class myDsl_specifier_qualifier_list:

    pass
class myDsl_struct_declaration_list_linha:

    pass
class myDsl_struct_declaration:

    pass
class myDsl_declaration_specifiers:

    def __init__(self, function_specifier: str, storage_class_specifier: str, myDsl_declaration_specifiers: "myDsl_declaration_specifiers" = None, myDsl_declaration_specifiers9: set["myDsl_declaration_specifiers"] = None, myDsl_declaration_specifiers12: "myDsl_type_specifier" = None, myDsl_declaration_specifiers14: "myDsl_type_qualifier" = None, myDsl_declaration_specifiers16: "myDsl_alignment_specifier" = None, myDsl_declaration_specifiers75: "myDsl_declaration" = None, myDsl_declaration_specifiers83: "myDsl_function_definition" = None, myDsl_declaration_specifiers140: "myDsl_parameter_declaration" = None):
        self.function_specifier = function_specifier
        self.storage_class_specifier = storage_class_specifier
        self.myDsl_declaration_specifiers = myDsl_declaration_specifiers
        self.myDsl_declaration_specifiers9 = myDsl_declaration_specifiers9 if myDsl_declaration_specifiers9 is not None else set()
        self.myDsl_declaration_specifiers12 = myDsl_declaration_specifiers12
        self.myDsl_declaration_specifiers14 = myDsl_declaration_specifiers14
        self.myDsl_declaration_specifiers16 = myDsl_declaration_specifiers16
        self.myDsl_declaration_specifiers75 = myDsl_declaration_specifiers75
        self.myDsl_declaration_specifiers83 = myDsl_declaration_specifiers83
        self.myDsl_declaration_specifiers140 = myDsl_declaration_specifiers140
        
    @property
    def function_specifier(self) -> str:
        return self.__function_specifier

    @function_specifier.setter
    def function_specifier(self, function_specifier: str):
        self.__function_specifier = function_specifier

    @property
    def storage_class_specifier(self) -> str:
        return self.__storage_class_specifier

    @storage_class_specifier.setter
    def storage_class_specifier(self, storage_class_specifier: str):
        self.__storage_class_specifier = storage_class_specifier

    @property
    def myDsl_declaration_specifiers12(self):
        return self.__myDsl_declaration_specifiers12

    @myDsl_declaration_specifiers12.setter
    def myDsl_declaration_specifiers12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers12", None)
        self.__myDsl_declaration_specifiers12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_specifier"):
                opp_val = getattr(old_value, "myDsl_type_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_specifier"):
                opp_val = getattr(value, "myDsl_type_specifier", None)
                setattr(value, "myDsl_type_specifier", self)

    @property
    def myDsl_declaration_specifiers83(self):
        return self.__myDsl_declaration_specifiers83

    @myDsl_declaration_specifiers83.setter
    def myDsl_declaration_specifiers83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers83", None)
        self.__myDsl_declaration_specifiers83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_function_definition82"):
                opp_val = getattr(old_value, "myDsl_function_definition82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_function_definition82"):
                opp_val = getattr(value, "myDsl_function_definition82", None)
                if opp_val is None:
                    setattr(value, "myDsl_function_definition82", set([self]))
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
            if hasattr(old_value, "myDsl_declaration_specifiers9"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers9"):
                opp_val = getattr(value, "myDsl_declaration_specifiers9", None)
                if opp_val is None:
                    setattr(value, "myDsl_declaration_specifiers9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_declaration_specifiers9(self):
        return self.__myDsl_declaration_specifiers9

    @myDsl_declaration_specifiers9.setter
    def myDsl_declaration_specifiers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers9", None)
        self.__myDsl_declaration_specifiers9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_declaration_specifiers"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_declaration_specifiers", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_declaration_specifiers"):
                    opp_val = getattr(item, "myDsl_declaration_specifiers", None)
                    
                    setattr(item, "myDsl_declaration_specifiers", self)
                    

    @property
    def myDsl_declaration_specifiers75(self):
        return self.__myDsl_declaration_specifiers75

    @myDsl_declaration_specifiers75.setter
    def myDsl_declaration_specifiers75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers75", None)
        self.__myDsl_declaration_specifiers75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration74"):
                opp_val = getattr(old_value, "myDsl_declaration74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration74"):
                opp_val = getattr(value, "myDsl_declaration74", None)
                if opp_val is None:
                    setattr(value, "myDsl_declaration74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_declaration_specifiers140(self):
        return self.__myDsl_declaration_specifiers140

    @myDsl_declaration_specifiers140.setter
    def myDsl_declaration_specifiers140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers140", None)
        self.__myDsl_declaration_specifiers140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_parameter_declaration139"):
                opp_val = getattr(old_value, "myDsl_parameter_declaration139", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_parameter_declaration139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_parameter_declaration139"):
                opp_val = getattr(value, "myDsl_parameter_declaration139", None)
                setattr(value, "myDsl_parameter_declaration139", self)

    @property
    def myDsl_declaration_specifiers14(self):
        return self.__myDsl_declaration_specifiers14

    @myDsl_declaration_specifiers14.setter
    def myDsl_declaration_specifiers14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers14", None)
        self.__myDsl_declaration_specifiers14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier"):
                opp_val = getattr(old_value, "myDsl_type_qualifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier"):
                opp_val = getattr(value, "myDsl_type_qualifier", None)
                setattr(value, "myDsl_type_qualifier", self)

    @property
    def myDsl_declaration_specifiers16(self):
        return self.__myDsl_declaration_specifiers16

    @myDsl_declaration_specifiers16.setter
    def myDsl_declaration_specifiers16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_declaration_specifiers__myDsl_declaration_specifiers16", None)
        self.__myDsl_declaration_specifiers16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_alignment_specifier"):
                opp_val = getattr(old_value, "myDsl_alignment_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_alignment_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_alignment_specifier"):
                opp_val = getattr(value, "myDsl_alignment_specifier", None)
                setattr(value, "myDsl_alignment_specifier", self)

class myDsl_declaration:

    pass
class myDsl_function_definition:

    pass
class myDsl_translation_unit_linha:

    pass
class myDsl_external_declaration:

    pass
class myDsl_translation_unit:

    pass
class myDsl_Model:

    pass
class myDsl_constant_expression:

    pass
class myDsl_type_name(postfix_expression):

    pass
class myDsl_alignment_specifier:

    pass
class myDsl_type_qualifier:

    def __init__(self, namez: str, myDsl_type_qualifier: "myDsl_declaration_specifiers" = None, myDsl_type_qualifier72: "myDsl_specifier_qualifier_list" = None, myDsl_type_qualifier107: "myDsl_type_qualifier_list" = None, myDsl_type_qualifier508: "myDsl_TypeQualifierListLinhaAtion" = None):
        self.namez = namez
        self.myDsl_type_qualifier = myDsl_type_qualifier
        self.myDsl_type_qualifier72 = myDsl_type_qualifier72
        self.myDsl_type_qualifier107 = myDsl_type_qualifier107
        self.myDsl_type_qualifier508 = myDsl_type_qualifier508
        
    @property
    def namez(self) -> str:
        return self.__namez

    @namez.setter
    def namez(self, namez: str):
        self.__namez = namez

    @property
    def myDsl_type_qualifier508(self):
        return self.__myDsl_type_qualifier508

    @myDsl_type_qualifier508.setter
    def myDsl_type_qualifier508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier508", None)
        self.__myDsl_type_qualifier508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeQualifierListLinhaAtion"):
                opp_val = getattr(old_value, "myDsl_TypeQualifierListLinhaAtion", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeQualifierListLinhaAtion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeQualifierListLinhaAtion"):
                opp_val = getattr(value, "myDsl_TypeQualifierListLinhaAtion", None)
                setattr(value, "myDsl_TypeQualifierListLinhaAtion", self)

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
            if hasattr(old_value, "myDsl_declaration_specifiers14"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers14", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers14"):
                opp_val = getattr(value, "myDsl_declaration_specifiers14", None)
                setattr(value, "myDsl_declaration_specifiers14", self)

    @property
    def myDsl_type_qualifier107(self):
        return self.__myDsl_type_qualifier107

    @myDsl_type_qualifier107.setter
    def myDsl_type_qualifier107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier107", None)
        self.__myDsl_type_qualifier107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_type_qualifier_list106"):
                opp_val = getattr(old_value, "myDsl_type_qualifier_list106", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_type_qualifier_list106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_type_qualifier_list106"):
                opp_val = getattr(value, "myDsl_type_qualifier_list106", None)
                setattr(value, "myDsl_type_qualifier_list106", self)

    @property
    def myDsl_type_qualifier72(self):
        return self.__myDsl_type_qualifier72

    @myDsl_type_qualifier72.setter
    def myDsl_type_qualifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_qualifier__myDsl_type_qualifier72", None)
        self.__myDsl_type_qualifier72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_specifier_qualifier_list71"):
                opp_val = getattr(old_value, "myDsl_specifier_qualifier_list71", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_specifier_qualifier_list71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_specifier_qualifier_list71"):
                opp_val = getattr(value, "myDsl_specifier_qualifier_list71", None)
                setattr(value, "myDsl_specifier_qualifier_list71", self)

class myDsl_type_specifier:

    def __init__(self, type_name_str: str, myDsl_type_specifier: "myDsl_declaration_specifiers" = None, myDsl_type_specifier22: "myDsl_atomic_type_specifier" = None, myDsl_type_specifier24: "myDsl_struct_or_union_specifier" = None, myDsl_type_specifier26: "myDsl_enum_specifier" = None, myDsl_type_specifier66: "myDsl_specifier_qualifier_list" = None):
        self.type_name_str = type_name_str
        self.myDsl_type_specifier = myDsl_type_specifier
        self.myDsl_type_specifier22 = myDsl_type_specifier22
        self.myDsl_type_specifier24 = myDsl_type_specifier24
        self.myDsl_type_specifier26 = myDsl_type_specifier26
        self.myDsl_type_specifier66 = myDsl_type_specifier66
        
    @property
    def type_name_str(self) -> str:
        return self.__type_name_str

    @type_name_str.setter
    def type_name_str(self, type_name_str: str):
        self.__type_name_str = type_name_str

    @property
    def myDsl_type_specifier24(self):
        return self.__myDsl_type_specifier24

    @myDsl_type_specifier24.setter
    def myDsl_type_specifier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier24", None)
        self.__myDsl_type_specifier24 = value
        
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
    def myDsl_type_specifier26(self):
        return self.__myDsl_type_specifier26

    @myDsl_type_specifier26.setter
    def myDsl_type_specifier26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier26", None)
        self.__myDsl_type_specifier26 = value
        
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
    def myDsl_type_specifier(self):
        return self.__myDsl_type_specifier

    @myDsl_type_specifier.setter
    def myDsl_type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier", None)
        self.__myDsl_type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_declaration_specifiers12"):
                opp_val = getattr(old_value, "myDsl_declaration_specifiers12", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_declaration_specifiers12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_declaration_specifiers12"):
                opp_val = getattr(value, "myDsl_declaration_specifiers12", None)
                setattr(value, "myDsl_declaration_specifiers12", self)

    @property
    def myDsl_type_specifier66(self):
        return self.__myDsl_type_specifier66

    @myDsl_type_specifier66.setter
    def myDsl_type_specifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier66", None)
        self.__myDsl_type_specifier66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_specifier_qualifier_list65"):
                opp_val = getattr(old_value, "myDsl_specifier_qualifier_list65", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_specifier_qualifier_list65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_specifier_qualifier_list65"):
                opp_val = getattr(value, "myDsl_specifier_qualifier_list65", None)
                setattr(value, "myDsl_specifier_qualifier_list65", self)

    @property
    def myDsl_type_specifier22(self):
        return self.__myDsl_type_specifier22

    @myDsl_type_specifier22.setter
    def myDsl_type_specifier22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_type_specifier__myDsl_type_specifier22", None)
        self.__myDsl_type_specifier22 = value
        
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

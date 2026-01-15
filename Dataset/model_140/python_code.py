from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeOrVoid:

    pass
class cSharp_Void(TypeOrVoid):

    pass
class BuiltInClassType:

    pass
class cSharp_String(BuiltInClassType):

    pass
class cSharp_Object(BuiltInClassType):

    pass
class IntegralType:

    pass
class cSharp_Char(IntegralType):

    pass
class cSharp_UInt(IntegralType):

    pass
class cSharp_Long(IntegralType):

    pass
class cSharp_UShort(IntegralType):

    pass
class cSharp_Short(IntegralType):

    pass
class cSharp_Int(IntegralType):

    pass
class cSharp_ULong(IntegralType):

    pass
class cSharp_Byte(IntegralType):

    pass
class cSharp_SByte(IntegralType):

    pass
class GetAccessorDeclaration:

    pass
class SetAccessorDeclaration:

    pass
class MaybeEmptyBlock:

    pass
class AddAccessorDeclaration:

    pass
class RemoveAccessorDeclaration:

    pass
class cSharp_ElsePart:

    pass
class cSharp_SwitchLabel:

    pass
class cSharp_SwitchSection:

    pass
class cSharp_SwitchStatement:

    pass
class cSharp_IfStatement:

    pass
class cSharp_StatementExpressionList:

    pass
class cSharp_ForInitializer:

    pass
class cSharp_ForeachStatement:

    pass
class cSharp_ForStatement:

    pass
class cSharp_DoStatement:

    pass
class cSharp_WhileStatement:

    pass
class cSharp_GeneralCatchclause:

    pass
class cSharp_SpecificCatchClause:

    pass
class cSharp_ThrowStatement:

    pass
class cSharp_ReturnStatement:

    pass
class cSharp_GotoStatement:

    pass
class cSharp_ContinueStatement:

    pass
class cSharp_BreakStatement:

    pass
class cSharp_UsingStatement:

    pass
class cSharp_LockStatement:

    pass
class cSharp_Block(MaybeEmptyBlock, AddAccessorDeclaration, RemoveAccessorDeclaration):

    pass
class cSharp_TryStatement:

    pass
class cSharp_FinallyClause:

    pass
class cSharp_CatchClauses:

    pass
class cSharp_JumpStatement:

    pass
class cSharp_IterationStatement:

    pass
class cSharp_ResourceAquisition:

    pass
class cSharp_SelectionStatement:

    pass
class cSharp_StatementExpression:

    def __init__(self, incrimentDecrement: str, assignementOperator: str, cSharp_StatementExpression: "cSharp_EmbeddedStatement" = None, cSharp_StatementExpression670: "cSharp_Type" = None, cSharp_StatementExpression673: "cSharp_ArgumentList" = None, cSharp_StatementExpression676: "cSharp_PrimaryExpression" = None, cSharp_StatementExpression679: "cSharp_UnaryExpression" = None, cSharp_StatementExpression682: "cSharp_Expression" = None, cSharp_StatementExpression665: "cSharp_StatementExpressionList" = None, cSharp_StatementExpression668: "cSharp_StatementExpressionList" = None):
        self.incrimentDecrement = incrimentDecrement
        self.assignementOperator = assignementOperator
        self.cSharp_StatementExpression = cSharp_StatementExpression
        self.cSharp_StatementExpression670 = cSharp_StatementExpression670
        self.cSharp_StatementExpression673 = cSharp_StatementExpression673
        self.cSharp_StatementExpression676 = cSharp_StatementExpression676
        self.cSharp_StatementExpression679 = cSharp_StatementExpression679
        self.cSharp_StatementExpression682 = cSharp_StatementExpression682
        self.cSharp_StatementExpression665 = cSharp_StatementExpression665
        self.cSharp_StatementExpression668 = cSharp_StatementExpression668
        
    @property
    def assignementOperator(self) -> str:
        return self.__assignementOperator

    @assignementOperator.setter
    def assignementOperator(self, assignementOperator: str):
        self.__assignementOperator = assignementOperator

    @property
    def incrimentDecrement(self) -> str:
        return self.__incrimentDecrement

    @incrimentDecrement.setter
    def incrimentDecrement(self, incrimentDecrement: str):
        self.__incrimentDecrement = incrimentDecrement

    @property
    def cSharp_StatementExpression668(self):
        return self.__cSharp_StatementExpression668

    @cSharp_StatementExpression668.setter
    def cSharp_StatementExpression668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression668", None)
        self.__cSharp_StatementExpression668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_StatementExpressionList667"):
                opp_val = getattr(old_value, "cSharp_StatementExpressionList667", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_StatementExpressionList667"):
                opp_val = getattr(value, "cSharp_StatementExpressionList667", None)
                if opp_val is None:
                    setattr(value, "cSharp_StatementExpressionList667", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharp_StatementExpression(self):
        return self.__cSharp_StatementExpression

    @cSharp_StatementExpression.setter
    def cSharp_StatementExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression", None)
        self.__cSharp_StatementExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_EmbeddedStatement535"):
                opp_val = getattr(old_value, "cSharp_EmbeddedStatement535", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_EmbeddedStatement535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_EmbeddedStatement535"):
                opp_val = getattr(value, "cSharp_EmbeddedStatement535", None)
                setattr(value, "cSharp_EmbeddedStatement535", self)

    @property
    def cSharp_StatementExpression673(self):
        return self.__cSharp_StatementExpression673

    @cSharp_StatementExpression673.setter
    def cSharp_StatementExpression673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression673", None)
        self.__cSharp_StatementExpression673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ArgumentList674"):
                opp_val = getattr(old_value, "cSharp_ArgumentList674", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ArgumentList674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ArgumentList674"):
                opp_val = getattr(value, "cSharp_ArgumentList674", None)
                setattr(value, "cSharp_ArgumentList674", self)

    @property
    def cSharp_StatementExpression679(self):
        return self.__cSharp_StatementExpression679

    @cSharp_StatementExpression679.setter
    def cSharp_StatementExpression679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression679", None)
        self.__cSharp_StatementExpression679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_UnaryExpression680"):
                opp_val = getattr(old_value, "cSharp_UnaryExpression680", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_UnaryExpression680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_UnaryExpression680"):
                opp_val = getattr(value, "cSharp_UnaryExpression680", None)
                setattr(value, "cSharp_UnaryExpression680", self)

    @property
    def cSharp_StatementExpression682(self):
        return self.__cSharp_StatementExpression682

    @cSharp_StatementExpression682.setter
    def cSharp_StatementExpression682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression682", None)
        self.__cSharp_StatementExpression682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Expression683"):
                opp_val = getattr(old_value, "cSharp_Expression683", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Expression683", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Expression683"):
                opp_val = getattr(value, "cSharp_Expression683", None)
                setattr(value, "cSharp_Expression683", self)

    @property
    def cSharp_StatementExpression670(self):
        return self.__cSharp_StatementExpression670

    @cSharp_StatementExpression670.setter
    def cSharp_StatementExpression670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression670", None)
        self.__cSharp_StatementExpression670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Type671"):
                opp_val = getattr(old_value, "cSharp_Type671", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Type671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Type671"):
                opp_val = getattr(value, "cSharp_Type671", None)
                setattr(value, "cSharp_Type671", self)

    @property
    def cSharp_StatementExpression665(self):
        return self.__cSharp_StatementExpression665

    @cSharp_StatementExpression665.setter
    def cSharp_StatementExpression665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression665", None)
        self.__cSharp_StatementExpression665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_StatementExpressionList664"):
                opp_val = getattr(old_value, "cSharp_StatementExpressionList664", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_StatementExpressionList664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_StatementExpressionList664"):
                opp_val = getattr(value, "cSharp_StatementExpressionList664", None)
                setattr(value, "cSharp_StatementExpressionList664", self)

    @property
    def cSharp_StatementExpression676(self):
        return self.__cSharp_StatementExpression676

    @cSharp_StatementExpression676.setter
    def cSharp_StatementExpression676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StatementExpression__cSharp_StatementExpression676", None)
        self.__cSharp_StatementExpression676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_PrimaryExpression677"):
                opp_val = getattr(old_value, "cSharp_PrimaryExpression677", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_PrimaryExpression677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_PrimaryExpression677"):
                opp_val = getattr(value, "cSharp_PrimaryExpression677", None)
                setattr(value, "cSharp_PrimaryExpression677", self)

class cSharp_LocalconstantDeclaration:

    pass
class cSharp_EmbeddedStatement:

    pass
class cSharp_DeclarationStatment:

    pass
class cSharp_LabeledStatement:

    pass
class cSharp_Statement:

    pass
class DelegateDeclaration:

    pass
class cSharp_FixedParameter:

    pass
class FormalParameterList:

    pass
class cSharp_FixedParameters(FormalParameterList):

    pass
class cSharp_ParameterArray:

    pass
class cSharp_AddAccessorDeclaration:

    pass
class cSharp_MethodHeader:

    def __init__(self, modifier: str, cSharp_MethodHeader: "cSharp_MethodDeclaration" = None, cSharp_MethodHeader445: "cSharp_TypeOrVoid" = None, cSharp_MethodHeader451: "cSharp_FormalParameterList" = None, cSharp_MethodHeader448: "cSharp_QualifiedIdentifier" = None):
        self.modifier = modifier
        self.cSharp_MethodHeader = cSharp_MethodHeader
        self.cSharp_MethodHeader445 = cSharp_MethodHeader445
        self.cSharp_MethodHeader451 = cSharp_MethodHeader451
        self.cSharp_MethodHeader448 = cSharp_MethodHeader448
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def cSharp_MethodHeader(self):
        return self.__cSharp_MethodHeader

    @cSharp_MethodHeader.setter
    def cSharp_MethodHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_MethodHeader__cSharp_MethodHeader", None)
        self.__cSharp_MethodHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_MethodDeclaration440"):
                opp_val = getattr(old_value, "cSharp_MethodDeclaration440", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_MethodDeclaration440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_MethodDeclaration440"):
                opp_val = getattr(value, "cSharp_MethodDeclaration440", None)
                setattr(value, "cSharp_MethodDeclaration440", self)

    @property
    def cSharp_MethodHeader448(self):
        return self.__cSharp_MethodHeader448

    @cSharp_MethodHeader448.setter
    def cSharp_MethodHeader448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_MethodHeader__cSharp_MethodHeader448", None)
        self.__cSharp_MethodHeader448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_QualifiedIdentifier449"):
                opp_val = getattr(old_value, "cSharp_QualifiedIdentifier449", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_QualifiedIdentifier449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_QualifiedIdentifier449"):
                opp_val = getattr(value, "cSharp_QualifiedIdentifier449", None)
                setattr(value, "cSharp_QualifiedIdentifier449", self)

    @property
    def cSharp_MethodHeader445(self):
        return self.__cSharp_MethodHeader445

    @cSharp_MethodHeader445.setter
    def cSharp_MethodHeader445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_MethodHeader__cSharp_MethodHeader445", None)
        self.__cSharp_MethodHeader445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_TypeOrVoid446"):
                opp_val = getattr(old_value, "cSharp_TypeOrVoid446", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_TypeOrVoid446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_TypeOrVoid446"):
                opp_val = getattr(value, "cSharp_TypeOrVoid446", None)
                setattr(value, "cSharp_TypeOrVoid446", self)

    @property
    def cSharp_MethodHeader451(self):
        return self.__cSharp_MethodHeader451

    @cSharp_MethodHeader451.setter
    def cSharp_MethodHeader451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_MethodHeader__cSharp_MethodHeader451", None)
        self.__cSharp_MethodHeader451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_FormalParameterList452"):
                opp_val = getattr(old_value, "cSharp_FormalParameterList452", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_FormalParameterList452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_FormalParameterList452"):
                opp_val = getattr(value, "cSharp_FormalParameterList452", None)
                setattr(value, "cSharp_FormalParameterList452", self)

class cSharp_SetAccessorDeclaration:

    pass
class cSharp_GetAccessorDeclaration:

    pass
class cSharp_RemoveAccessorDeclaration:

    pass
class cSharp_IndexerDeclarator:

    pass
class cSharp_OperatorDeclarator:

    pass
class OperatorDeclarator:

    pass
class cSharp_BinaryOperatorDeclarator(OperatorDeclarator):

    def __init__(self, overBinOperator: str, cSharp_BinaryOperatorDeclarator: "cSharp_Type" = None, cSharp_BinaryOperatorDeclarator392: "cSharp_Identifier" = None, cSharp_BinaryOperatorDeclarator395: "cSharp_Type" = None, cSharp_BinaryOperatorDeclarator398: "cSharp_Identifier" = None):
        self.overBinOperator = overBinOperator
        self.cSharp_BinaryOperatorDeclarator = cSharp_BinaryOperatorDeclarator
        self.cSharp_BinaryOperatorDeclarator392 = cSharp_BinaryOperatorDeclarator392
        self.cSharp_BinaryOperatorDeclarator395 = cSharp_BinaryOperatorDeclarator395
        self.cSharp_BinaryOperatorDeclarator398 = cSharp_BinaryOperatorDeclarator398
        
    @property
    def overBinOperator(self) -> str:
        return self.__overBinOperator

    @overBinOperator.setter
    def overBinOperator(self, overBinOperator: str):
        self.__overBinOperator = overBinOperator

    @property
    def cSharp_BinaryOperatorDeclarator398(self):
        return self.__cSharp_BinaryOperatorDeclarator398

    @cSharp_BinaryOperatorDeclarator398.setter
    def cSharp_BinaryOperatorDeclarator398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_BinaryOperatorDeclarator__cSharp_BinaryOperatorDeclarator398", None)
        self.__cSharp_BinaryOperatorDeclarator398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Identifier399"):
                opp_val = getattr(old_value, "cSharp_Identifier399", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Identifier399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Identifier399"):
                opp_val = getattr(value, "cSharp_Identifier399", None)
                setattr(value, "cSharp_Identifier399", self)

    @property
    def cSharp_BinaryOperatorDeclarator392(self):
        return self.__cSharp_BinaryOperatorDeclarator392

    @cSharp_BinaryOperatorDeclarator392.setter
    def cSharp_BinaryOperatorDeclarator392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_BinaryOperatorDeclarator__cSharp_BinaryOperatorDeclarator392", None)
        self.__cSharp_BinaryOperatorDeclarator392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Identifier393"):
                opp_val = getattr(old_value, "cSharp_Identifier393", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Identifier393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Identifier393"):
                opp_val = getattr(value, "cSharp_Identifier393", None)
                setattr(value, "cSharp_Identifier393", self)

    @property
    def cSharp_BinaryOperatorDeclarator(self):
        return self.__cSharp_BinaryOperatorDeclarator

    @cSharp_BinaryOperatorDeclarator.setter
    def cSharp_BinaryOperatorDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_BinaryOperatorDeclarator__cSharp_BinaryOperatorDeclarator", None)
        self.__cSharp_BinaryOperatorDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Type390"):
                opp_val = getattr(old_value, "cSharp_Type390", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Type390", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Type390"):
                opp_val = getattr(value, "cSharp_Type390", None)
                setattr(value, "cSharp_Type390", self)

    @property
    def cSharp_BinaryOperatorDeclarator395(self):
        return self.__cSharp_BinaryOperatorDeclarator395

    @cSharp_BinaryOperatorDeclarator395.setter
    def cSharp_BinaryOperatorDeclarator395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_BinaryOperatorDeclarator__cSharp_BinaryOperatorDeclarator395", None)
        self.__cSharp_BinaryOperatorDeclarator395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Type396"):
                opp_val = getattr(old_value, "cSharp_Type396", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Type396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Type396"):
                opp_val = getattr(value, "cSharp_Type396", None)
                setattr(value, "cSharp_Type396", self)

class cSharp_UnaryOperatorDeclarator(OperatorDeclarator):

    pass
class cSharp_ConversionOperatorDeclarator(OperatorDeclarator):

    pass
class cSharp_MaybeEmptyBlock(GetAccessorDeclaration, SetAccessorDeclaration):

    pass
class cSharp_StaticConstructorDeclaration:

    def __init__(self, staticCosntModifier: str, cSharp_StaticConstructorDeclaration: "cSharp_ClassMemberDeclaration" = None, cSharp_StaticConstructorDeclaration348: "cSharp_Identifier" = None, cSharp_StaticConstructorDeclaration351: "cSharp_MaybeEmptyBlock" = None):
        self.staticCosntModifier = staticCosntModifier
        self.cSharp_StaticConstructorDeclaration = cSharp_StaticConstructorDeclaration
        self.cSharp_StaticConstructorDeclaration348 = cSharp_StaticConstructorDeclaration348
        self.cSharp_StaticConstructorDeclaration351 = cSharp_StaticConstructorDeclaration351
        
    @property
    def staticCosntModifier(self) -> str:
        return self.__staticCosntModifier

    @staticCosntModifier.setter
    def staticCosntModifier(self, staticCosntModifier: str):
        self.__staticCosntModifier = staticCosntModifier

    @property
    def cSharp_StaticConstructorDeclaration(self):
        return self.__cSharp_StaticConstructorDeclaration

    @cSharp_StaticConstructorDeclaration.setter
    def cSharp_StaticConstructorDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StaticConstructorDeclaration__cSharp_StaticConstructorDeclaration", None)
        self.__cSharp_StaticConstructorDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassMemberDeclaration346"):
                opp_val = getattr(old_value, "cSharp_ClassMemberDeclaration346", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassMemberDeclaration346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassMemberDeclaration346"):
                opp_val = getattr(value, "cSharp_ClassMemberDeclaration346", None)
                setattr(value, "cSharp_ClassMemberDeclaration346", self)

    @property
    def cSharp_StaticConstructorDeclaration348(self):
        return self.__cSharp_StaticConstructorDeclaration348

    @cSharp_StaticConstructorDeclaration348.setter
    def cSharp_StaticConstructorDeclaration348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StaticConstructorDeclaration__cSharp_StaticConstructorDeclaration348", None)
        self.__cSharp_StaticConstructorDeclaration348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Identifier349"):
                opp_val = getattr(old_value, "cSharp_Identifier349", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Identifier349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Identifier349"):
                opp_val = getattr(value, "cSharp_Identifier349", None)
                setattr(value, "cSharp_Identifier349", self)

    @property
    def cSharp_StaticConstructorDeclaration351(self):
        return self.__cSharp_StaticConstructorDeclaration351

    @cSharp_StaticConstructorDeclaration351.setter
    def cSharp_StaticConstructorDeclaration351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_StaticConstructorDeclaration__cSharp_StaticConstructorDeclaration351", None)
        self.__cSharp_StaticConstructorDeclaration351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_MaybeEmptyBlock"):
                opp_val = getattr(old_value, "cSharp_MaybeEmptyBlock", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_MaybeEmptyBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_MaybeEmptyBlock"):
                opp_val = getattr(value, "cSharp_MaybeEmptyBlock", None)
                setattr(value, "cSharp_MaybeEmptyBlock", self)

class cSharp_Argument:

    pass
class ConstructorInitializer:

    pass
class cSharp_ConstructorInitializer:

    pass
class cSharp_ConstructorDeclarator:

    pass
class cSharp_ClassMemberDeclaration:

    pass
class cSharp_ClassBody:

    pass
class cSharp_ClassBase:

    pass
class cSharp_DestructorDeclaration:

    pass
class cSharp_ConstructorDeclaration:

    def __init__(self, constModifier: str, cSharp_ConstructorDeclaration: "cSharp_ClassMemberDeclaration" = None, cSharp_ConstructorDeclaration359: "cSharp_ConstructorDeclarator" = None, cSharp_ConstructorDeclaration361: "cSharp_MaybeEmptyBlock" = None):
        self.constModifier = constModifier
        self.cSharp_ConstructorDeclaration = cSharp_ConstructorDeclaration
        self.cSharp_ConstructorDeclaration359 = cSharp_ConstructorDeclaration359
        self.cSharp_ConstructorDeclaration361 = cSharp_ConstructorDeclaration361
        
    @property
    def constModifier(self) -> str:
        return self.__constModifier

    @constModifier.setter
    def constModifier(self, constModifier: str):
        self.__constModifier = constModifier

    @property
    def cSharp_ConstructorDeclaration(self):
        return self.__cSharp_ConstructorDeclaration

    @cSharp_ConstructorDeclaration.setter
    def cSharp_ConstructorDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ConstructorDeclaration__cSharp_ConstructorDeclaration", None)
        self.__cSharp_ConstructorDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassMemberDeclaration342"):
                opp_val = getattr(old_value, "cSharp_ClassMemberDeclaration342", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassMemberDeclaration342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassMemberDeclaration342"):
                opp_val = getattr(value, "cSharp_ClassMemberDeclaration342", None)
                setattr(value, "cSharp_ClassMemberDeclaration342", self)

    @property
    def cSharp_ConstructorDeclaration361(self):
        return self.__cSharp_ConstructorDeclaration361

    @cSharp_ConstructorDeclaration361.setter
    def cSharp_ConstructorDeclaration361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ConstructorDeclaration__cSharp_ConstructorDeclaration361", None)
        self.__cSharp_ConstructorDeclaration361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_MaybeEmptyBlock362"):
                opp_val = getattr(old_value, "cSharp_MaybeEmptyBlock362", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_MaybeEmptyBlock362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_MaybeEmptyBlock362"):
                opp_val = getattr(value, "cSharp_MaybeEmptyBlock362", None)
                setattr(value, "cSharp_MaybeEmptyBlock362", self)

    @property
    def cSharp_ConstructorDeclaration359(self):
        return self.__cSharp_ConstructorDeclaration359

    @cSharp_ConstructorDeclaration359.setter
    def cSharp_ConstructorDeclaration359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ConstructorDeclaration__cSharp_ConstructorDeclaration359", None)
        self.__cSharp_ConstructorDeclaration359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ConstructorDeclarator"):
                opp_val = getattr(old_value, "cSharp_ConstructorDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ConstructorDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ConstructorDeclarator"):
                opp_val = getattr(value, "cSharp_ConstructorDeclarator", None)
                setattr(value, "cSharp_ConstructorDeclarator", self)

class cSharp_OperatorDeclaration:

    def __init__(self, opModifier: str, cSharp_OperatorDeclaration: "cSharp_ClassMemberDeclaration" = None, cSharp_OperatorDeclaration377: "cSharp_OperatorDeclarator" = None, cSharp_OperatorDeclaration379: "cSharp_MaybeEmptyBlock" = None):
        self.opModifier = opModifier
        self.cSharp_OperatorDeclaration = cSharp_OperatorDeclaration
        self.cSharp_OperatorDeclaration377 = cSharp_OperatorDeclaration377
        self.cSharp_OperatorDeclaration379 = cSharp_OperatorDeclaration379
        
    @property
    def opModifier(self) -> str:
        return self.__opModifier

    @opModifier.setter
    def opModifier(self, opModifier: str):
        self.__opModifier = opModifier

    @property
    def cSharp_OperatorDeclaration(self):
        return self.__cSharp_OperatorDeclaration

    @cSharp_OperatorDeclaration.setter
    def cSharp_OperatorDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_OperatorDeclaration__cSharp_OperatorDeclaration", None)
        self.__cSharp_OperatorDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassMemberDeclaration340"):
                opp_val = getattr(old_value, "cSharp_ClassMemberDeclaration340", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassMemberDeclaration340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassMemberDeclaration340"):
                opp_val = getattr(value, "cSharp_ClassMemberDeclaration340", None)
                setattr(value, "cSharp_ClassMemberDeclaration340", self)

    @property
    def cSharp_OperatorDeclaration379(self):
        return self.__cSharp_OperatorDeclaration379

    @cSharp_OperatorDeclaration379.setter
    def cSharp_OperatorDeclaration379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_OperatorDeclaration__cSharp_OperatorDeclaration379", None)
        self.__cSharp_OperatorDeclaration379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_MaybeEmptyBlock380"):
                opp_val = getattr(old_value, "cSharp_MaybeEmptyBlock380", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_MaybeEmptyBlock380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_MaybeEmptyBlock380"):
                opp_val = getattr(value, "cSharp_MaybeEmptyBlock380", None)
                setattr(value, "cSharp_MaybeEmptyBlock380", self)

    @property
    def cSharp_OperatorDeclaration377(self):
        return self.__cSharp_OperatorDeclaration377

    @cSharp_OperatorDeclaration377.setter
    def cSharp_OperatorDeclaration377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_OperatorDeclaration__cSharp_OperatorDeclaration377", None)
        self.__cSharp_OperatorDeclaration377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_OperatorDeclarator"):
                opp_val = getattr(old_value, "cSharp_OperatorDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_OperatorDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_OperatorDeclarator"):
                opp_val = getattr(value, "cSharp_OperatorDeclarator", None)
                setattr(value, "cSharp_OperatorDeclarator", self)

class cSharp_IndexerDeclaration:

    def __init__(self, idModifier: str, cSharp_IndexerDeclaration: "cSharp_ClassMemberDeclaration" = None, cSharp_IndexerDeclaration406: "cSharp_IndexerDeclarator" = None, cSharp_IndexerDeclaration408: "cSharp_AccessorDeclarations" = None):
        self.idModifier = idModifier
        self.cSharp_IndexerDeclaration = cSharp_IndexerDeclaration
        self.cSharp_IndexerDeclaration406 = cSharp_IndexerDeclaration406
        self.cSharp_IndexerDeclaration408 = cSharp_IndexerDeclaration408
        
    @property
    def idModifier(self) -> str:
        return self.__idModifier

    @idModifier.setter
    def idModifier(self, idModifier: str):
        self.__idModifier = idModifier

    @property
    def cSharp_IndexerDeclaration(self):
        return self.__cSharp_IndexerDeclaration

    @cSharp_IndexerDeclaration.setter
    def cSharp_IndexerDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_IndexerDeclaration__cSharp_IndexerDeclaration", None)
        self.__cSharp_IndexerDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassMemberDeclaration335"):
                opp_val = getattr(old_value, "cSharp_ClassMemberDeclaration335", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassMemberDeclaration335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassMemberDeclaration335"):
                opp_val = getattr(value, "cSharp_ClassMemberDeclaration335", None)
                setattr(value, "cSharp_ClassMemberDeclaration335", self)

    @property
    def cSharp_IndexerDeclaration406(self):
        return self.__cSharp_IndexerDeclaration406

    @cSharp_IndexerDeclaration406.setter
    def cSharp_IndexerDeclaration406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_IndexerDeclaration__cSharp_IndexerDeclaration406", None)
        self.__cSharp_IndexerDeclaration406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_IndexerDeclarator"):
                opp_val = getattr(old_value, "cSharp_IndexerDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_IndexerDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_IndexerDeclarator"):
                opp_val = getattr(value, "cSharp_IndexerDeclarator", None)
                setattr(value, "cSharp_IndexerDeclarator", self)

    @property
    def cSharp_IndexerDeclaration408(self):
        return self.__cSharp_IndexerDeclaration408

    @cSharp_IndexerDeclaration408.setter
    def cSharp_IndexerDeclaration408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_IndexerDeclaration__cSharp_IndexerDeclaration408", None)
        self.__cSharp_IndexerDeclaration408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_AccessorDeclarations409"):
                opp_val = getattr(old_value, "cSharp_AccessorDeclarations409", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_AccessorDeclarations409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_AccessorDeclarations409"):
                opp_val = getattr(value, "cSharp_AccessorDeclarations409", None)
                setattr(value, "cSharp_AccessorDeclarations409", self)

class cSharp_EventDeclaration:

    pass
class cSharp_PropertyDeclaration:

    pass
class cSharp_ConstantDeclaration:

    pass
class cSharp_MethodDeclaration:

    pass
class cSharp_FieldDeclaration:

    pass
class cSharp_InterfaceAccessors:

    pass
class cSharp_FormalParameterList:

    pass
class cSharp_EnumMemberDeclaration:

    pass
class cSharp_InterfacePropertyDeclaration:

    pass
class cSharp_InterfaceIndexerDeclaration:

    pass
class cSharp_InterfaceEventDeclaration:

    pass
class cSharp_InterfaceMethodDeclaration:

    pass
class cSharp_InterfaceMemberDeclaration:

    pass
class cSharp_InterfaceBody:

    pass
class cSharp_NamespaceBody:

    pass
class cSharp_TypeDeclaration:

    pass
class cSharp_NamespaceDeclaration:

    pass
class cSharp_EnumBody:

    pass
class cSharp_DelegateDeclaration:

    pass
class cSharp_EnumDeclaration:

    pass
class cSharp_InterfaceDeclaration:

    pass
class cSharp_ClassDeclaration:

    def __init__(self, classModifier: str, cSharp_ClassDeclaration: "cSharp_TypeDeclaration" = None, cSharp_ClassDeclaration313: "cSharp_Identifier" = None, cSharp_ClassDeclaration316: "cSharp_ClassBase" = None, cSharp_ClassDeclaration318: "cSharp_ClassBody" = None):
        self.classModifier = classModifier
        self.cSharp_ClassDeclaration = cSharp_ClassDeclaration
        self.cSharp_ClassDeclaration313 = cSharp_ClassDeclaration313
        self.cSharp_ClassDeclaration316 = cSharp_ClassDeclaration316
        self.cSharp_ClassDeclaration318 = cSharp_ClassDeclaration318
        
    @property
    def classModifier(self) -> str:
        return self.__classModifier

    @classModifier.setter
    def classModifier(self, classModifier: str):
        self.__classModifier = classModifier

    @property
    def cSharp_ClassDeclaration(self):
        return self.__cSharp_ClassDeclaration

    @cSharp_ClassDeclaration.setter
    def cSharp_ClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ClassDeclaration__cSharp_ClassDeclaration", None)
        self.__cSharp_ClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_TypeDeclaration229"):
                opp_val = getattr(old_value, "cSharp_TypeDeclaration229", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_TypeDeclaration229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_TypeDeclaration229"):
                opp_val = getattr(value, "cSharp_TypeDeclaration229", None)
                setattr(value, "cSharp_TypeDeclaration229", self)

    @property
    def cSharp_ClassDeclaration313(self):
        return self.__cSharp_ClassDeclaration313

    @cSharp_ClassDeclaration313.setter
    def cSharp_ClassDeclaration313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ClassDeclaration__cSharp_ClassDeclaration313", None)
        self.__cSharp_ClassDeclaration313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Identifier314"):
                opp_val = getattr(old_value, "cSharp_Identifier314", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Identifier314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Identifier314"):
                opp_val = getattr(value, "cSharp_Identifier314", None)
                setattr(value, "cSharp_Identifier314", self)

    @property
    def cSharp_ClassDeclaration318(self):
        return self.__cSharp_ClassDeclaration318

    @cSharp_ClassDeclaration318.setter
    def cSharp_ClassDeclaration318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ClassDeclaration__cSharp_ClassDeclaration318", None)
        self.__cSharp_ClassDeclaration318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassBody"):
                opp_val = getattr(old_value, "cSharp_ClassBody", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassBody"):
                opp_val = getattr(value, "cSharp_ClassBody", None)
                setattr(value, "cSharp_ClassBody", self)

    @property
    def cSharp_ClassDeclaration316(self):
        return self.__cSharp_ClassDeclaration316

    @cSharp_ClassDeclaration316.setter
    def cSharp_ClassDeclaration316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_ClassDeclaration__cSharp_ClassDeclaration316", None)
        self.__cSharp_ClassDeclaration316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ClassBase"):
                opp_val = getattr(old_value, "cSharp_ClassBase", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ClassBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ClassBase"):
                opp_val = getattr(value, "cSharp_ClassBase", None)
                setattr(value, "cSharp_ClassBase", self)

class cSharp_AccessorDeclarations:

    pass
class cSharp_EventAccessorDeclarations:

    pass
class cSharp_QualifiedIdentifierList:

    pass
class ClassBase:

    pass
class ArrayType:

    pass
class BuiltInType:

    pass
class cSharp_Double(BuiltInType):

    pass
class cSharp_Bool(BuiltInType):

    pass
class cSharp_Decimal(BuiltInType):

    pass
class cSharp_Float(BuiltInType):

    pass
class cSharp_BuiltInClassType(ClassBase, BuiltInType):

    pass
class cSharp_IntegralType(BuiltInType):

    pass
class cSharp_ConstantDeclarator:

    pass
class cSharp_VariableDeclarator:

    pass
class ConstantDeclaration:

    pass
class FieldDeclaration:

    pass
class PropertyDeclaration:

    pass
class EventDeclaration:

    pass
class cSharp_VariableInitializer:

    pass
class cSharp_NonArrayType(ArrayType):

    pass
class cSharp_PrimaryExpression:

    def __init__(self, rankSpecifier: str, literal: str, predefinedType: str, cSharp_PrimaryExpression125: "cSharp_NonArrayType" = None, cSharp_PrimaryExpression127: "cSharp_ExpressionList" = None, cSharp_PrimaryExpression130: set["cSharp_ArrayInitializer"] = None, cSharp_PrimaryExpression132: "cSharp_ArrayType" = None, cSharp_PrimaryExpression134: "cSharp_ArrayInitializer" = None, cSharp_PrimaryExpression137: "cSharp_Type" = None, cSharp_PrimaryExpression140: "cSharp_ArgumentList" = None, cSharp_PrimaryExpression142: "cSharp_Identifier" = None, cSharp_PrimaryExpression145: "cSharp_Expression" = None, cSharp_PrimaryExpression148: "cSharp_TypeOrVoid" = None, cSharp_PrimaryExpression150: "cSharp_PrimaryExpression2" = None, cSharp_PrimaryExpression: "cSharp_UnaryExpression" = None, cSharp_PrimaryExpression677: "cSharp_StatementExpression" = None):
        self.rankSpecifier = rankSpecifier
        self.literal = literal
        self.predefinedType = predefinedType
        self.cSharp_PrimaryExpression125 = cSharp_PrimaryExpression125
        self.cSharp_PrimaryExpression127 = cSharp_PrimaryExpression127
        self.cSharp_PrimaryExpression130 = cSharp_PrimaryExpression130 if cSharp_PrimaryExpression130 is not None else set()
        self.cSharp_PrimaryExpression132 = cSharp_PrimaryExpression132
        self.cSharp_PrimaryExpression134 = cSharp_PrimaryExpression134
        self.cSharp_PrimaryExpression137 = cSharp_PrimaryExpression137
        self.cSharp_PrimaryExpression140 = cSharp_PrimaryExpression140
        self.cSharp_PrimaryExpression142 = cSharp_PrimaryExpression142
        self.cSharp_PrimaryExpression145 = cSharp_PrimaryExpression145
        self.cSharp_PrimaryExpression148 = cSharp_PrimaryExpression148
        self.cSharp_PrimaryExpression150 = cSharp_PrimaryExpression150
        self.cSharp_PrimaryExpression = cSharp_PrimaryExpression
        self.cSharp_PrimaryExpression677 = cSharp_PrimaryExpression677
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def rankSpecifier(self) -> str:
        return self.__rankSpecifier

    @rankSpecifier.setter
    def rankSpecifier(self, rankSpecifier: str):
        self.__rankSpecifier = rankSpecifier

    @property
    def predefinedType(self) -> str:
        return self.__predefinedType

    @predefinedType.setter
    def predefinedType(self, predefinedType: str):
        self.__predefinedType = predefinedType

    @property
    def cSharp_PrimaryExpression677(self):
        return self.__cSharp_PrimaryExpression677

    @cSharp_PrimaryExpression677.setter
    def cSharp_PrimaryExpression677(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression677", None)
        self.__cSharp_PrimaryExpression677 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_StatementExpression676"):
                opp_val = getattr(old_value, "cSharp_StatementExpression676", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_StatementExpression676", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_StatementExpression676"):
                opp_val = getattr(value, "cSharp_StatementExpression676", None)
                setattr(value, "cSharp_StatementExpression676", self)

    @property
    def cSharp_PrimaryExpression140(self):
        return self.__cSharp_PrimaryExpression140

    @cSharp_PrimaryExpression140.setter
    def cSharp_PrimaryExpression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression140", None)
        self.__cSharp_PrimaryExpression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ArgumentList"):
                opp_val = getattr(old_value, "cSharp_ArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ArgumentList"):
                opp_val = getattr(value, "cSharp_ArgumentList", None)
                setattr(value, "cSharp_ArgumentList", self)

    @property
    def cSharp_PrimaryExpression(self):
        return self.__cSharp_PrimaryExpression

    @cSharp_PrimaryExpression.setter
    def cSharp_PrimaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression", None)
        self.__cSharp_PrimaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_UnaryExpression123"):
                opp_val = getattr(old_value, "cSharp_UnaryExpression123", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_UnaryExpression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_UnaryExpression123"):
                opp_val = getattr(value, "cSharp_UnaryExpression123", None)
                setattr(value, "cSharp_UnaryExpression123", self)

    @property
    def cSharp_PrimaryExpression125(self):
        return self.__cSharp_PrimaryExpression125

    @cSharp_PrimaryExpression125.setter
    def cSharp_PrimaryExpression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression125", None)
        self.__cSharp_PrimaryExpression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_NonArrayType"):
                opp_val = getattr(old_value, "cSharp_NonArrayType", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_NonArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_NonArrayType"):
                opp_val = getattr(value, "cSharp_NonArrayType", None)
                setattr(value, "cSharp_NonArrayType", self)

    @property
    def cSharp_PrimaryExpression145(self):
        return self.__cSharp_PrimaryExpression145

    @cSharp_PrimaryExpression145.setter
    def cSharp_PrimaryExpression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression145", None)
        self.__cSharp_PrimaryExpression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Expression146"):
                opp_val = getattr(old_value, "cSharp_Expression146", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Expression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Expression146"):
                opp_val = getattr(value, "cSharp_Expression146", None)
                setattr(value, "cSharp_Expression146", self)

    @property
    def cSharp_PrimaryExpression137(self):
        return self.__cSharp_PrimaryExpression137

    @cSharp_PrimaryExpression137.setter
    def cSharp_PrimaryExpression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression137", None)
        self.__cSharp_PrimaryExpression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Type138"):
                opp_val = getattr(old_value, "cSharp_Type138", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Type138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Type138"):
                opp_val = getattr(value, "cSharp_Type138", None)
                setattr(value, "cSharp_Type138", self)

    @property
    def cSharp_PrimaryExpression130(self):
        return self.__cSharp_PrimaryExpression130

    @cSharp_PrimaryExpression130.setter
    def cSharp_PrimaryExpression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression130", None)
        self.__cSharp_PrimaryExpression130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharp_ArrayInitializer"):
                    opp_val = getattr(item, "cSharp_ArrayInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharp_ArrayInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharp_ArrayInitializer"):
                    opp_val = getattr(item, "cSharp_ArrayInitializer", None)
                    
                    setattr(item, "cSharp_ArrayInitializer", self)
                    

    @property
    def cSharp_PrimaryExpression134(self):
        return self.__cSharp_PrimaryExpression134

    @cSharp_PrimaryExpression134.setter
    def cSharp_PrimaryExpression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression134", None)
        self.__cSharp_PrimaryExpression134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ArrayInitializer135"):
                opp_val = getattr(old_value, "cSharp_ArrayInitializer135", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ArrayInitializer135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ArrayInitializer135"):
                opp_val = getattr(value, "cSharp_ArrayInitializer135", None)
                setattr(value, "cSharp_ArrayInitializer135", self)

    @property
    def cSharp_PrimaryExpression142(self):
        return self.__cSharp_PrimaryExpression142

    @cSharp_PrimaryExpression142.setter
    def cSharp_PrimaryExpression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression142", None)
        self.__cSharp_PrimaryExpression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Identifier143"):
                opp_val = getattr(old_value, "cSharp_Identifier143", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Identifier143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Identifier143"):
                opp_val = getattr(value, "cSharp_Identifier143", None)
                setattr(value, "cSharp_Identifier143", self)

    @property
    def cSharp_PrimaryExpression132(self):
        return self.__cSharp_PrimaryExpression132

    @cSharp_PrimaryExpression132.setter
    def cSharp_PrimaryExpression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression132", None)
        self.__cSharp_PrimaryExpression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ArrayType"):
                opp_val = getattr(old_value, "cSharp_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ArrayType"):
                opp_val = getattr(value, "cSharp_ArrayType", None)
                setattr(value, "cSharp_ArrayType", self)

    @property
    def cSharp_PrimaryExpression150(self):
        return self.__cSharp_PrimaryExpression150

    @cSharp_PrimaryExpression150.setter
    def cSharp_PrimaryExpression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression150", None)
        self.__cSharp_PrimaryExpression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_PrimaryExpression2"):
                opp_val = getattr(old_value, "cSharp_PrimaryExpression2", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_PrimaryExpression2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_PrimaryExpression2"):
                opp_val = getattr(value, "cSharp_PrimaryExpression2", None)
                setattr(value, "cSharp_PrimaryExpression2", self)

    @property
    def cSharp_PrimaryExpression148(self):
        return self.__cSharp_PrimaryExpression148

    @cSharp_PrimaryExpression148.setter
    def cSharp_PrimaryExpression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression148", None)
        self.__cSharp_PrimaryExpression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_TypeOrVoid"):
                opp_val = getattr(old_value, "cSharp_TypeOrVoid", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_TypeOrVoid", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_TypeOrVoid"):
                opp_val = getattr(value, "cSharp_TypeOrVoid", None)
                setattr(value, "cSharp_TypeOrVoid", self)

    @property
    def cSharp_PrimaryExpression127(self):
        return self.__cSharp_PrimaryExpression127

    @cSharp_PrimaryExpression127.setter
    def cSharp_PrimaryExpression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression__cSharp_PrimaryExpression127", None)
        self.__cSharp_PrimaryExpression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_ExpressionList128"):
                opp_val = getattr(old_value, "cSharp_ExpressionList128", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_ExpressionList128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_ExpressionList128"):
                opp_val = getattr(value, "cSharp_ExpressionList128", None)
                setattr(value, "cSharp_ExpressionList128", self)

class cSharp_Type(ConstantDeclaration, EventDeclaration, PropertyDeclaration, FieldDeclaration):

    pass
class cSharp_PrimaryExpression2:

    def __init__(self, incrementeDecrement: str, cSharp_PrimaryExpression2: "cSharp_PrimaryExpression" = None, cSharp_PrimaryExpression2152: set["cSharp_Identifier"] = None, cSharp_PrimaryExpression2155: set["cSharp_ArgumentList"] = None, cSharp_PrimaryExpression2158: set["cSharp_ExpressionList"] = None, cSharp_PrimaryExpression2162: "cSharp_PrimaryExpression2" = None, cSharp_PrimaryExpression2160: set["cSharp_PrimaryExpression2"] = None):
        self.incrementeDecrement = incrementeDecrement
        self.cSharp_PrimaryExpression2 = cSharp_PrimaryExpression2
        self.cSharp_PrimaryExpression2152 = cSharp_PrimaryExpression2152 if cSharp_PrimaryExpression2152 is not None else set()
        self.cSharp_PrimaryExpression2155 = cSharp_PrimaryExpression2155 if cSharp_PrimaryExpression2155 is not None else set()
        self.cSharp_PrimaryExpression2158 = cSharp_PrimaryExpression2158 if cSharp_PrimaryExpression2158 is not None else set()
        self.cSharp_PrimaryExpression2162 = cSharp_PrimaryExpression2162
        self.cSharp_PrimaryExpression2160 = cSharp_PrimaryExpression2160 if cSharp_PrimaryExpression2160 is not None else set()
        
    @property
    def incrementeDecrement(self) -> str:
        return self.__incrementeDecrement

    @incrementeDecrement.setter
    def incrementeDecrement(self, incrementeDecrement: str):
        self.__incrementeDecrement = incrementeDecrement

    @property
    def cSharp_PrimaryExpression2(self):
        return self.__cSharp_PrimaryExpression2

    @cSharp_PrimaryExpression2.setter
    def cSharp_PrimaryExpression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2", None)
        self.__cSharp_PrimaryExpression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_PrimaryExpression150"):
                opp_val = getattr(old_value, "cSharp_PrimaryExpression150", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_PrimaryExpression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_PrimaryExpression150"):
                opp_val = getattr(value, "cSharp_PrimaryExpression150", None)
                setattr(value, "cSharp_PrimaryExpression150", self)

    @property
    def cSharp_PrimaryExpression2162(self):
        return self.__cSharp_PrimaryExpression2162

    @cSharp_PrimaryExpression2162.setter
    def cSharp_PrimaryExpression2162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2162", None)
        self.__cSharp_PrimaryExpression2162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_PrimaryExpression2160"):
                opp_val = getattr(old_value, "cSharp_PrimaryExpression2160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_PrimaryExpression2160"):
                opp_val = getattr(value, "cSharp_PrimaryExpression2160", None)
                if opp_val is None:
                    setattr(value, "cSharp_PrimaryExpression2160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharp_PrimaryExpression2152(self):
        return self.__cSharp_PrimaryExpression2152

    @cSharp_PrimaryExpression2152.setter
    def cSharp_PrimaryExpression2152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2152", None)
        self.__cSharp_PrimaryExpression2152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharp_Identifier153"):
                    opp_val = getattr(item, "cSharp_Identifier153", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharp_Identifier153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharp_Identifier153"):
                    opp_val = getattr(item, "cSharp_Identifier153", None)
                    
                    setattr(item, "cSharp_Identifier153", self)
                    

    @property
    def cSharp_PrimaryExpression2155(self):
        return self.__cSharp_PrimaryExpression2155

    @cSharp_PrimaryExpression2155.setter
    def cSharp_PrimaryExpression2155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2155", None)
        self.__cSharp_PrimaryExpression2155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharp_ArgumentList156"):
                    opp_val = getattr(item, "cSharp_ArgumentList156", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharp_ArgumentList156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharp_ArgumentList156"):
                    opp_val = getattr(item, "cSharp_ArgumentList156", None)
                    
                    setattr(item, "cSharp_ArgumentList156", self)
                    

    @property
    def cSharp_PrimaryExpression2160(self):
        return self.__cSharp_PrimaryExpression2160

    @cSharp_PrimaryExpression2160.setter
    def cSharp_PrimaryExpression2160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2160", None)
        self.__cSharp_PrimaryExpression2160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharp_PrimaryExpression2162"):
                    opp_val = getattr(item, "cSharp_PrimaryExpression2162", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharp_PrimaryExpression2162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharp_PrimaryExpression2162"):
                    opp_val = getattr(item, "cSharp_PrimaryExpression2162", None)
                    
                    setattr(item, "cSharp_PrimaryExpression2162", self)
                    

    @property
    def cSharp_PrimaryExpression2158(self):
        return self.__cSharp_PrimaryExpression2158

    @cSharp_PrimaryExpression2158.setter
    def cSharp_PrimaryExpression2158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_PrimaryExpression2__cSharp_PrimaryExpression2158", None)
        self.__cSharp_PrimaryExpression2158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharp_ExpressionList159"):
                    opp_val = getattr(item, "cSharp_ExpressionList159", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharp_ExpressionList159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharp_ExpressionList159"):
                    opp_val = getattr(item, "cSharp_ExpressionList159", None)
                    
                    setattr(item, "cSharp_ExpressionList159", self)
                    

class cSharp_TypeOrVoid(DelegateDeclaration):

    pass
class cSharp_ArgumentList(ConstructorInitializer):

    pass
class cSharp_BuiltInType:

    pass
class cSharp_AttributeArguments:

    pass
class cSharp_Expression2:

    pass
class cSharp_UnaryExpression:

    def __init__(self, expUnaryOperator: str, cSharp_UnaryExpression: "cSharp_Expression" = None, cSharp_UnaryExpression118: "cSharp_Type" = None, cSharp_UnaryExpression121: "cSharp_UnaryExpression" = None, cSharp_UnaryExpression119: "cSharp_UnaryExpression" = None, cSharp_UnaryExpression123: "cSharp_PrimaryExpression" = None, cSharp_UnaryExpression680: "cSharp_StatementExpression" = None):
        self.expUnaryOperator = expUnaryOperator
        self.cSharp_UnaryExpression = cSharp_UnaryExpression
        self.cSharp_UnaryExpression118 = cSharp_UnaryExpression118
        self.cSharp_UnaryExpression121 = cSharp_UnaryExpression121
        self.cSharp_UnaryExpression119 = cSharp_UnaryExpression119
        self.cSharp_UnaryExpression123 = cSharp_UnaryExpression123
        self.cSharp_UnaryExpression680 = cSharp_UnaryExpression680
        
    @property
    def expUnaryOperator(self) -> str:
        return self.__expUnaryOperator

    @expUnaryOperator.setter
    def expUnaryOperator(self, expUnaryOperator: str):
        self.__expUnaryOperator = expUnaryOperator

    @property
    def cSharp_UnaryExpression(self):
        return self.__cSharp_UnaryExpression

    @cSharp_UnaryExpression.setter
    def cSharp_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression", None)
        self.__cSharp_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Expression31"):
                opp_val = getattr(old_value, "cSharp_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Expression31"):
                opp_val = getattr(value, "cSharp_Expression31", None)
                setattr(value, "cSharp_Expression31", self)

    @property
    def cSharp_UnaryExpression118(self):
        return self.__cSharp_UnaryExpression118

    @cSharp_UnaryExpression118.setter
    def cSharp_UnaryExpression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression118", None)
        self.__cSharp_UnaryExpression118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_Type"):
                opp_val = getattr(old_value, "cSharp_Type", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_Type"):
                opp_val = getattr(value, "cSharp_Type", None)
                setattr(value, "cSharp_Type", self)

    @property
    def cSharp_UnaryExpression121(self):
        return self.__cSharp_UnaryExpression121

    @cSharp_UnaryExpression121.setter
    def cSharp_UnaryExpression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression121", None)
        self.__cSharp_UnaryExpression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_UnaryExpression119"):
                opp_val = getattr(old_value, "cSharp_UnaryExpression119", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_UnaryExpression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_UnaryExpression119"):
                opp_val = getattr(value, "cSharp_UnaryExpression119", None)
                setattr(value, "cSharp_UnaryExpression119", self)

    @property
    def cSharp_UnaryExpression123(self):
        return self.__cSharp_UnaryExpression123

    @cSharp_UnaryExpression123.setter
    def cSharp_UnaryExpression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression123", None)
        self.__cSharp_UnaryExpression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_PrimaryExpression"):
                opp_val = getattr(old_value, "cSharp_PrimaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_PrimaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_PrimaryExpression"):
                opp_val = getattr(value, "cSharp_PrimaryExpression", None)
                setattr(value, "cSharp_PrimaryExpression", self)

    @property
    def cSharp_UnaryExpression680(self):
        return self.__cSharp_UnaryExpression680

    @cSharp_UnaryExpression680.setter
    def cSharp_UnaryExpression680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression680", None)
        self.__cSharp_UnaryExpression680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_StatementExpression679"):
                opp_val = getattr(old_value, "cSharp_StatementExpression679", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_StatementExpression679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_StatementExpression679"):
                opp_val = getattr(value, "cSharp_StatementExpression679", None)
                setattr(value, "cSharp_StatementExpression679", self)

    @property
    def cSharp_UnaryExpression119(self):
        return self.__cSharp_UnaryExpression119

    @cSharp_UnaryExpression119.setter
    def cSharp_UnaryExpression119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharp_UnaryExpression__cSharp_UnaryExpression119", None)
        self.__cSharp_UnaryExpression119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharp_UnaryExpression121"):
                opp_val = getattr(old_value, "cSharp_UnaryExpression121", None)
                if opp_val == self:
                    setattr(old_value, "cSharp_UnaryExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharp_UnaryExpression121"):
                opp_val = getattr(value, "cSharp_UnaryExpression121", None)
                setattr(value, "cSharp_UnaryExpression121", self)

class ResourceAquisition:

    pass
class cSharp_LocalVariableDeclaration(ResourceAquisition):

    pass
class Argument:

    pass
class VariableInitializer:

    pass
class cSharp_ArrayInitializer(VariableInitializer):

    pass
class cSharp_Expression(VariableInitializer, Argument, ResourceAquisition):

    pass
class cSharp_ExpressionList:

    pass
class cSharp_GlobalAttributeSection:

    pass
class cSharp_ArrayType:

    pass
class cSharp_AttributeName:

    pass
class cSharp_Attribute:

    pass
class AttributeSection:

    pass
class cSharp_AttributeList(AttributeSection):

    pass
class cSharp_AttributeSection:

    pass
class cSharp_Attributes:

    pass
class cSharp_CompilationUnit:

    pass
class cSharp_QualifiedIdentifier:

    pass
class cSharp_Identifier:

    pass
class cSharp_NamespaceMemberDeclaration:

    pass
class cSharp_GlobalAttributes:

    pass
class cSharp_UsingDirective:

    pass
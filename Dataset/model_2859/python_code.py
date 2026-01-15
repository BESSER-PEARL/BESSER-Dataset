from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class go_imaginary_lit:

    pass
class go_ImportPath:

    pass
class go_ImportSpec:

    pass
class go_exponent:

    pass
class float_lit:

    pass
class go_CommCase:

    pass
class go_CommClause:

    pass
class go_RecvExpr:

    pass
class go_RecvStmt:

    pass
class go_ForClause:

    pass
class go_Condition:

    pass
class go_TypeList:

    pass
class go_TypeSwitchCase:

    pass
class go_PostStmt:

    pass
class go_InitStmt:

    pass
class go_RangeClause:

    pass
class go_Channel:

    pass
class go_TypeCaseClause:

    pass
class go_TypeSwitchGuard:

    pass
class go_ExprSwitchCase:

    pass
class go_ExprCaseClause:

    pass
class go_switch_stmt_linha:

    pass
class SwitchStmt:

    pass
class go_DeferStmt:

    pass
class go_ForStmt:

    pass
class go_SelectStmt:

    pass
class go_SwitchStmt:

    pass
class go_IfStmt:

    pass
class go_GotoStmt:

    pass
class go_Label:

    pass
class go_Assignment:

    def __init__(self, assign_op: str, go_Assignment: "go_SimpleStmt" = None, go_Assignment423: set["go_ExpressionList"] = None):
        self.assign_op = assign_op
        self.go_Assignment = go_Assignment
        self.go_Assignment423 = go_Assignment423 if go_Assignment423 is not None else set()
        
    @property
    def assign_op(self) -> str:
        return self.__assign_op

    @assign_op.setter
    def assign_op(self, assign_op: str):
        self.__assign_op = assign_op

    @property
    def go_Assignment(self):
        return self.__go_Assignment

    @go_Assignment.setter
    def go_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment", None)
        self.__go_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_SimpleStmt396"):
                opp_val = getattr(old_value, "go_SimpleStmt396", None)
                if opp_val == self:
                    setattr(old_value, "go_SimpleStmt396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_SimpleStmt396"):
                opp_val = getattr(value, "go_SimpleStmt396", None)
                setattr(value, "go_SimpleStmt396", self)

    @property
    def go_Assignment423(self):
        return self.__go_Assignment423

    @go_Assignment423.setter
    def go_Assignment423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment423", None)
        self.__go_Assignment423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_ExpressionList424"):
                    opp_val = getattr(item, "go_ExpressionList424", None)
                    
                    if opp_val == self:
                        setattr(item, "go_ExpressionList424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_ExpressionList424"):
                    opp_val = getattr(item, "go_ExpressionList424", None)
                    
                    setattr(item, "go_ExpressionList424", self)
                    

class go_IncDecStmt:

    pass
class go_SendStmt:

    pass
class go_ExpressionStmt:

    pass
class go_ContinueStmt:

    pass
class go_BreakStmt:

    pass
class go_ReturnStmt:

    pass
class go_GoStmt:

    pass
class go_SimpleStmt(SwitchStmt):

    def __init__(self, EmptyStmt: str, go_SimpleStmt: "go_Statement" = None, go_SimpleStmt390: "go_ExpressionStmt" = None, go_SimpleStmt392: "go_SendStmt" = None, go_SimpleStmt394: "go_IncDecStmt" = None, go_SimpleStmt396: "go_Assignment" = None, go_SimpleStmt398: "go_ShortVarDecl" = None, go_SimpleStmt427: "go_IfStmt" = None, go_SimpleStmt496: "go_InitStmt" = None, go_SimpleStmt499: "go_PostStmt" = None):
        self.EmptyStmt = EmptyStmt
        self.go_SimpleStmt = go_SimpleStmt
        self.go_SimpleStmt390 = go_SimpleStmt390
        self.go_SimpleStmt392 = go_SimpleStmt392
        self.go_SimpleStmt394 = go_SimpleStmt394
        self.go_SimpleStmt396 = go_SimpleStmt396
        self.go_SimpleStmt398 = go_SimpleStmt398
        self.go_SimpleStmt427 = go_SimpleStmt427
        self.go_SimpleStmt496 = go_SimpleStmt496
        self.go_SimpleStmt499 = go_SimpleStmt499
        
    @property
    def EmptyStmt(self) -> str:
        return self.__EmptyStmt

    @EmptyStmt.setter
    def EmptyStmt(self, EmptyStmt: str):
        self.__EmptyStmt = EmptyStmt

    @property
    def go_SimpleStmt427(self):
        return self.__go_SimpleStmt427

    @go_SimpleStmt427.setter
    def go_SimpleStmt427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt427", None)
        self.__go_SimpleStmt427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IfStmt426"):
                opp_val = getattr(old_value, "go_IfStmt426", None)
                if opp_val == self:
                    setattr(old_value, "go_IfStmt426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IfStmt426"):
                opp_val = getattr(value, "go_IfStmt426", None)
                setattr(value, "go_IfStmt426", self)

    @property
    def go_SimpleStmt392(self):
        return self.__go_SimpleStmt392

    @go_SimpleStmt392.setter
    def go_SimpleStmt392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt392", None)
        self.__go_SimpleStmt392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_SendStmt"):
                opp_val = getattr(old_value, "go_SendStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_SendStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_SendStmt"):
                opp_val = getattr(value, "go_SendStmt", None)
                setattr(value, "go_SendStmt", self)

    @property
    def go_SimpleStmt398(self):
        return self.__go_SimpleStmt398

    @go_SimpleStmt398.setter
    def go_SimpleStmt398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt398", None)
        self.__go_SimpleStmt398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ShortVarDecl399"):
                opp_val = getattr(old_value, "go_ShortVarDecl399", None)
                if opp_val == self:
                    setattr(old_value, "go_ShortVarDecl399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ShortVarDecl399"):
                opp_val = getattr(value, "go_ShortVarDecl399", None)
                setattr(value, "go_ShortVarDecl399", self)

    @property
    def go_SimpleStmt496(self):
        return self.__go_SimpleStmt496

    @go_SimpleStmt496.setter
    def go_SimpleStmt496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt496", None)
        self.__go_SimpleStmt496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_InitStmt495"):
                opp_val = getattr(old_value, "go_InitStmt495", None)
                if opp_val == self:
                    setattr(old_value, "go_InitStmt495", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_InitStmt495"):
                opp_val = getattr(value, "go_InitStmt495", None)
                setattr(value, "go_InitStmt495", self)

    @property
    def go_SimpleStmt396(self):
        return self.__go_SimpleStmt396

    @go_SimpleStmt396.setter
    def go_SimpleStmt396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt396", None)
        self.__go_SimpleStmt396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Assignment"):
                opp_val = getattr(old_value, "go_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "go_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Assignment"):
                opp_val = getattr(value, "go_Assignment", None)
                setattr(value, "go_Assignment", self)

    @property
    def go_SimpleStmt(self):
        return self.__go_SimpleStmt

    @go_SimpleStmt.setter
    def go_SimpleStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt", None)
        self.__go_SimpleStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Statement365"):
                opp_val = getattr(old_value, "go_Statement365", None)
                if opp_val == self:
                    setattr(old_value, "go_Statement365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Statement365"):
                opp_val = getattr(value, "go_Statement365", None)
                setattr(value, "go_Statement365", self)

    @property
    def go_SimpleStmt390(self):
        return self.__go_SimpleStmt390

    @go_SimpleStmt390.setter
    def go_SimpleStmt390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt390", None)
        self.__go_SimpleStmt390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ExpressionStmt"):
                opp_val = getattr(old_value, "go_ExpressionStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_ExpressionStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ExpressionStmt"):
                opp_val = getattr(value, "go_ExpressionStmt", None)
                setattr(value, "go_ExpressionStmt", self)

    @property
    def go_SimpleStmt499(self):
        return self.__go_SimpleStmt499

    @go_SimpleStmt499.setter
    def go_SimpleStmt499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt499", None)
        self.__go_SimpleStmt499 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PostStmt498"):
                opp_val = getattr(old_value, "go_PostStmt498", None)
                if opp_val == self:
                    setattr(old_value, "go_PostStmt498", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PostStmt498"):
                opp_val = getattr(value, "go_PostStmt498", None)
                setattr(value, "go_PostStmt498", self)

    @property
    def go_SimpleStmt394(self):
        return self.__go_SimpleStmt394

    @go_SimpleStmt394.setter
    def go_SimpleStmt394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SimpleStmt__go_SimpleStmt394", None)
        self.__go_SimpleStmt394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IncDecStmt"):
                opp_val = getattr(old_value, "go_IncDecStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_IncDecStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IncDecStmt"):
                opp_val = getattr(value, "go_IncDecStmt", None)
                setattr(value, "go_IncDecStmt", self)

class go_LabeledStmt:

    pass
class go_decimals(float_lit):

    def __init__(self, DECIMAL_DIGIT: str, go_decimals: "go_Slice" = None, go_decimals568: "go_decimals" = None, go_decimals566: "go_decimals" = None, go_decimals570: "go_exponent" = None, go_decimals572: "go_exponent" = None, go_decimals576: "go_exponent" = None, go_decimals578: "go_imaginary_lit" = None):
        self.DECIMAL_DIGIT = DECIMAL_DIGIT
        self.go_decimals = go_decimals
        self.go_decimals568 = go_decimals568
        self.go_decimals566 = go_decimals566
        self.go_decimals570 = go_decimals570
        self.go_decimals572 = go_decimals572
        self.go_decimals576 = go_decimals576
        self.go_decimals578 = go_decimals578
        
    @property
    def DECIMAL_DIGIT(self) -> str:
        return self.__DECIMAL_DIGIT

    @DECIMAL_DIGIT.setter
    def DECIMAL_DIGIT(self, DECIMAL_DIGIT: str):
        self.__DECIMAL_DIGIT = DECIMAL_DIGIT

    @property
    def go_decimals566(self):
        return self.__go_decimals566

    @go_decimals566.setter
    def go_decimals566(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals566", None)
        self.__go_decimals566 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_decimals568"):
                opp_val = getattr(old_value, "go_decimals568", None)
                if opp_val == self:
                    setattr(old_value, "go_decimals568", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_decimals568"):
                opp_val = getattr(value, "go_decimals568", None)
                setattr(value, "go_decimals568", self)

    @property
    def go_decimals572(self):
        return self.__go_decimals572

    @go_decimals572.setter
    def go_decimals572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals572", None)
        self.__go_decimals572 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_exponent573"):
                opp_val = getattr(old_value, "go_exponent573", None)
                if opp_val == self:
                    setattr(old_value, "go_exponent573", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_exponent573"):
                opp_val = getattr(value, "go_exponent573", None)
                setattr(value, "go_exponent573", self)

    @property
    def go_decimals578(self):
        return self.__go_decimals578

    @go_decimals578.setter
    def go_decimals578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals578", None)
        self.__go_decimals578 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_imaginary_lit"):
                opp_val = getattr(old_value, "go_imaginary_lit", None)
                if opp_val == self:
                    setattr(old_value, "go_imaginary_lit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_imaginary_lit"):
                opp_val = getattr(value, "go_imaginary_lit", None)
                setattr(value, "go_imaginary_lit", self)

    @property
    def go_decimals(self):
        return self.__go_decimals

    @go_decimals.setter
    def go_decimals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals", None)
        self.__go_decimals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Slice317"):
                opp_val = getattr(old_value, "go_Slice317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Slice317"):
                opp_val = getattr(value, "go_Slice317", None)
                if opp_val is None:
                    setattr(value, "go_Slice317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_decimals570(self):
        return self.__go_decimals570

    @go_decimals570.setter
    def go_decimals570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals570", None)
        self.__go_decimals570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_exponent"):
                opp_val = getattr(old_value, "go_exponent", None)
                if opp_val == self:
                    setattr(old_value, "go_exponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_exponent"):
                opp_val = getattr(value, "go_exponent", None)
                setattr(value, "go_exponent", self)

    @property
    def go_decimals568(self):
        return self.__go_decimals568

    @go_decimals568.setter
    def go_decimals568(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals568", None)
        self.__go_decimals568 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_decimals566"):
                opp_val = getattr(old_value, "go_decimals566", None)
                if opp_val == self:
                    setattr(old_value, "go_decimals566", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_decimals566"):
                opp_val = getattr(value, "go_decimals566", None)
                setattr(value, "go_decimals566", self)

    @property
    def go_decimals576(self):
        return self.__go_decimals576

    @go_decimals576.setter
    def go_decimals576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_decimals__go_decimals576", None)
        self.__go_decimals576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_exponent575"):
                opp_val = getattr(old_value, "go_exponent575", None)
                if opp_val == self:
                    setattr(old_value, "go_exponent575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_exponent575"):
                opp_val = getattr(value, "go_exponent575", None)
                setattr(value, "go_exponent575", self)

class go_Slice:

    pass
class go_Index:

    pass
class go_binary_op:

    def __init__(self, rel_op: str, add_op: str, mul_op: str, go_binary_op: "go_ExpressionLinha" = None):
        self.rel_op = rel_op
        self.add_op = add_op
        self.mul_op = mul_op
        self.go_binary_op = go_binary_op
        
    @property
    def mul_op(self) -> str:
        return self.__mul_op

    @mul_op.setter
    def mul_op(self, mul_op: str):
        self.__mul_op = mul_op

    @property
    def add_op(self) -> str:
        return self.__add_op

    @add_op.setter
    def add_op(self, add_op: str):
        self.__add_op = add_op

    @property
    def rel_op(self) -> str:
        return self.__rel_op

    @rel_op.setter
    def rel_op(self, rel_op: str):
        self.__rel_op = rel_op

    @property
    def go_binary_op(self):
        return self.__go_binary_op

    @go_binary_op.setter
    def go_binary_op(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_binary_op__go_binary_op", None)
        self.__go_binary_op = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ExpressionLinha340"):
                opp_val = getattr(old_value, "go_ExpressionLinha340", None)
                if opp_val == self:
                    setattr(old_value, "go_ExpressionLinha340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ExpressionLinha340"):
                opp_val = getattr(value, "go_ExpressionLinha340", None)
                setattr(value, "go_ExpressionLinha340", self)

class go_ExpressionLinha:

    pass
class go_UnaryExpr:

    def __init__(self, unary_op: str, go_UnaryExpr: "go_Expression" = None, go_UnaryExpr348: "go_PrimaryExpr" = None, go_UnaryExpr352: "go_UnaryExpr" = None, go_UnaryExpr350: "go_UnaryExpr" = None):
        self.unary_op = unary_op
        self.go_UnaryExpr = go_UnaryExpr
        self.go_UnaryExpr348 = go_UnaryExpr348
        self.go_UnaryExpr352 = go_UnaryExpr352
        self.go_UnaryExpr350 = go_UnaryExpr350
        
    @property
    def unary_op(self) -> str:
        return self.__unary_op

    @unary_op.setter
    def unary_op(self, unary_op: str):
        self.__unary_op = unary_op

    @property
    def go_UnaryExpr348(self):
        return self.__go_UnaryExpr348

    @go_UnaryExpr348.setter
    def go_UnaryExpr348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_UnaryExpr__go_UnaryExpr348", None)
        self.__go_UnaryExpr348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PrimaryExpr349"):
                opp_val = getattr(old_value, "go_PrimaryExpr349", None)
                if opp_val == self:
                    setattr(old_value, "go_PrimaryExpr349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PrimaryExpr349"):
                opp_val = getattr(value, "go_PrimaryExpr349", None)
                setattr(value, "go_PrimaryExpr349", self)

    @property
    def go_UnaryExpr350(self):
        return self.__go_UnaryExpr350

    @go_UnaryExpr350.setter
    def go_UnaryExpr350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_UnaryExpr__go_UnaryExpr350", None)
        self.__go_UnaryExpr350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_UnaryExpr352"):
                opp_val = getattr(old_value, "go_UnaryExpr352", None)
                if opp_val == self:
                    setattr(old_value, "go_UnaryExpr352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_UnaryExpr352"):
                opp_val = getattr(value, "go_UnaryExpr352", None)
                setattr(value, "go_UnaryExpr352", self)

    @property
    def go_UnaryExpr352(self):
        return self.__go_UnaryExpr352

    @go_UnaryExpr352.setter
    def go_UnaryExpr352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_UnaryExpr__go_UnaryExpr352", None)
        self.__go_UnaryExpr352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_UnaryExpr350"):
                opp_val = getattr(old_value, "go_UnaryExpr350", None)
                if opp_val == self:
                    setattr(old_value, "go_UnaryExpr350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_UnaryExpr350"):
                opp_val = getattr(value, "go_UnaryExpr350", None)
                setattr(value, "go_UnaryExpr350", self)

    @property
    def go_UnaryExpr(self):
        return self.__go_UnaryExpr

    @go_UnaryExpr.setter
    def go_UnaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_UnaryExpr__go_UnaryExpr", None)
        self.__go_UnaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Expression336"):
                opp_val = getattr(old_value, "go_Expression336", None)
                if opp_val == self:
                    setattr(old_value, "go_Expression336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Expression336"):
                opp_val = getattr(value, "go_Expression336", None)
                setattr(value, "go_Expression336", self)

class go_ReceiverType:

    pass
class go_PrimaryExprLinha:

    pass
class go_PrimaryExpr:

    pass
class go_FieldName:

    pass
class go_TypeAssertion:

    pass
class go_Selector:

    pass
class go_cochetes:

    pass
class go_ponto:

    pass
class go_Arguments:

    pass
class go_MethodExpr:

    pass
class go_Conversion:

    pass
class go_LiteralTypeLinha:

    pass
class go_LiteralValue:

    pass
class go_LiteralType:

    pass
class Literal:

    pass
class go_FunctionLit(Literal):

    pass
class go_CompositeLit(Literal):

    pass
class go_Key:

    pass
class go_Element:

    pass
class go_KeyedElement:

    pass
class go_ElementList:

    pass
class go_Literal:

    pass
class go_Operand:

    pass
class go_MethodDecl:

    pass
class go_PackageName:

    pass
class OperandName:

    pass
class go_rune_lit:

    def __init__(self, unicode_value: str, byte_value: str, go_rune_lit: "go_BasicLit" = None):
        self.unicode_value = unicode_value
        self.byte_value = byte_value
        self.go_rune_lit = go_rune_lit
        
    @property
    def byte_value(self) -> str:
        return self.__byte_value

    @byte_value.setter
    def byte_value(self, byte_value: str):
        self.__byte_value = byte_value

    @property
    def unicode_value(self) -> str:
        return self.__unicode_value

    @unicode_value.setter
    def unicode_value(self, unicode_value: str):
        self.__unicode_value = unicode_value

    @property
    def go_rune_lit(self):
        return self.__go_rune_lit

    @go_rune_lit.setter
    def go_rune_lit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_rune_lit__go_rune_lit", None)
        self.__go_rune_lit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BasicLit217"):
                opp_val = getattr(old_value, "go_BasicLit217", None)
                if opp_val == self:
                    setattr(old_value, "go_BasicLit217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BasicLit217"):
                opp_val = getattr(value, "go_BasicLit217", None)
                setattr(value, "go_BasicLit217", self)

class go_float_lit:

    pass
class go_BasicLit:

    def __init__(self, int_lit: str, go_BasicLit: "go_Literal" = None, go_BasicLit215: "go_float_lit" = None, go_BasicLit217: "go_rune_lit" = None, go_BasicLit219: "go_string_lit" = None):
        self.int_lit = int_lit
        self.go_BasicLit = go_BasicLit
        self.go_BasicLit215 = go_BasicLit215
        self.go_BasicLit217 = go_BasicLit217
        self.go_BasicLit219 = go_BasicLit219
        
    @property
    def int_lit(self) -> str:
        return self.__int_lit

    @int_lit.setter
    def int_lit(self, int_lit: str):
        self.__int_lit = int_lit

    @property
    def go_BasicLit217(self):
        return self.__go_BasicLit217

    @go_BasicLit217.setter
    def go_BasicLit217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicLit__go_BasicLit217", None)
        self.__go_BasicLit217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_rune_lit"):
                opp_val = getattr(old_value, "go_rune_lit", None)
                if opp_val == self:
                    setattr(old_value, "go_rune_lit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_rune_lit"):
                opp_val = getattr(value, "go_rune_lit", None)
                setattr(value, "go_rune_lit", self)

    @property
    def go_BasicLit215(self):
        return self.__go_BasicLit215

    @go_BasicLit215.setter
    def go_BasicLit215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicLit__go_BasicLit215", None)
        self.__go_BasicLit215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_float_lit"):
                opp_val = getattr(old_value, "go_float_lit", None)
                if opp_val == self:
                    setattr(old_value, "go_float_lit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_float_lit"):
                opp_val = getattr(value, "go_float_lit", None)
                setattr(value, "go_float_lit", self)

    @property
    def go_BasicLit219(self):
        return self.__go_BasicLit219

    @go_BasicLit219.setter
    def go_BasicLit219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicLit__go_BasicLit219", None)
        self.__go_BasicLit219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_string_lit220"):
                opp_val = getattr(old_value, "go_string_lit220", None)
                if opp_val == self:
                    setattr(old_value, "go_string_lit220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_string_lit220"):
                opp_val = getattr(value, "go_string_lit220", None)
                setattr(value, "go_string_lit220", self)

    @property
    def go_BasicLit(self):
        return self.__go_BasicLit

    @go_BasicLit.setter
    def go_BasicLit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicLit__go_BasicLit", None)
        self.__go_BasicLit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Literal213"):
                opp_val = getattr(old_value, "go_Literal213", None)
                if opp_val == self:
                    setattr(old_value, "go_Literal213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Literal213"):
                opp_val = getattr(value, "go_Literal213", None)
                setattr(value, "go_Literal213", self)

class go_OperandName:

    pass
class TypeSpec:

    pass
class go_TypeDef(TypeSpec):

    pass
class go_AliasDecl(TypeSpec):

    pass
class go_FunctionDecl:

    pass
class go_ShortVarDecl:

    pass
class go_FunctionName:

    pass
class go_VarSpec:

    pass
class go_topLevelDeclLinha:

    pass
class go_VarDecl:

    pass
class go_TypeDecl:

    pass
class go_ConstDecl:

    pass
class go_Declaration:

    pass
class go_Statement:

    def __init__(self, FallthroughStmt: str, go_Statement: "go_StatementList" = None, go_Statement360: "go_Declaration" = None, go_Statement363: "go_LabeledStmt" = None, go_Statement365: "go_SimpleStmt" = None, go_Statement367: "go_GoStmt" = None, go_Statement369: "go_ReturnStmt" = None, go_Statement371: "go_BreakStmt" = None, go_Statement404: "go_LabeledStmt" = None, go_Statement373: "go_ContinueStmt" = None, go_Statement375: "go_GotoStmt" = None, go_Statement377: "go_Block" = None, go_Statement380: "go_IfStmt" = None, go_Statement382: "go_SwitchStmt" = None, go_Statement384: "go_SelectStmt" = None, go_Statement386: "go_ForStmt" = None, go_Statement388: "go_DeferStmt" = None):
        self.FallthroughStmt = FallthroughStmt
        self.go_Statement = go_Statement
        self.go_Statement360 = go_Statement360
        self.go_Statement363 = go_Statement363
        self.go_Statement365 = go_Statement365
        self.go_Statement367 = go_Statement367
        self.go_Statement369 = go_Statement369
        self.go_Statement371 = go_Statement371
        self.go_Statement404 = go_Statement404
        self.go_Statement373 = go_Statement373
        self.go_Statement375 = go_Statement375
        self.go_Statement377 = go_Statement377
        self.go_Statement380 = go_Statement380
        self.go_Statement382 = go_Statement382
        self.go_Statement384 = go_Statement384
        self.go_Statement386 = go_Statement386
        self.go_Statement388 = go_Statement388
        
    @property
    def FallthroughStmt(self) -> str:
        return self.__FallthroughStmt

    @FallthroughStmt.setter
    def FallthroughStmt(self, FallthroughStmt: str):
        self.__FallthroughStmt = FallthroughStmt

    @property
    def go_Statement382(self):
        return self.__go_Statement382

    @go_Statement382.setter
    def go_Statement382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement382", None)
        self.__go_Statement382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_SwitchStmt"):
                opp_val = getattr(old_value, "go_SwitchStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_SwitchStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_SwitchStmt"):
                opp_val = getattr(value, "go_SwitchStmt", None)
                setattr(value, "go_SwitchStmt", self)

    @property
    def go_Statement365(self):
        return self.__go_Statement365

    @go_Statement365.setter
    def go_Statement365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement365", None)
        self.__go_Statement365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_SimpleStmt"):
                opp_val = getattr(old_value, "go_SimpleStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_SimpleStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_SimpleStmt"):
                opp_val = getattr(value, "go_SimpleStmt", None)
                setattr(value, "go_SimpleStmt", self)

    @property
    def go_Statement363(self):
        return self.__go_Statement363

    @go_Statement363.setter
    def go_Statement363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement363", None)
        self.__go_Statement363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_LabeledStmt"):
                opp_val = getattr(old_value, "go_LabeledStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_LabeledStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_LabeledStmt"):
                opp_val = getattr(value, "go_LabeledStmt", None)
                setattr(value, "go_LabeledStmt", self)

    @property
    def go_Statement371(self):
        return self.__go_Statement371

    @go_Statement371.setter
    def go_Statement371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement371", None)
        self.__go_Statement371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BreakStmt"):
                opp_val = getattr(old_value, "go_BreakStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_BreakStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BreakStmt"):
                opp_val = getattr(value, "go_BreakStmt", None)
                setattr(value, "go_BreakStmt", self)

    @property
    def go_Statement388(self):
        return self.__go_Statement388

    @go_Statement388.setter
    def go_Statement388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement388", None)
        self.__go_Statement388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DeferStmt"):
                opp_val = getattr(old_value, "go_DeferStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_DeferStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DeferStmt"):
                opp_val = getattr(value, "go_DeferStmt", None)
                setattr(value, "go_DeferStmt", self)

    @property
    def go_Statement369(self):
        return self.__go_Statement369

    @go_Statement369.setter
    def go_Statement369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement369", None)
        self.__go_Statement369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ReturnStmt"):
                opp_val = getattr(old_value, "go_ReturnStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_ReturnStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ReturnStmt"):
                opp_val = getattr(value, "go_ReturnStmt", None)
                setattr(value, "go_ReturnStmt", self)

    @property
    def go_Statement380(self):
        return self.__go_Statement380

    @go_Statement380.setter
    def go_Statement380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement380", None)
        self.__go_Statement380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IfStmt"):
                opp_val = getattr(old_value, "go_IfStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_IfStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IfStmt"):
                opp_val = getattr(value, "go_IfStmt", None)
                setattr(value, "go_IfStmt", self)

    @property
    def go_Statement384(self):
        return self.__go_Statement384

    @go_Statement384.setter
    def go_Statement384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement384", None)
        self.__go_Statement384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_SelectStmt"):
                opp_val = getattr(old_value, "go_SelectStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_SelectStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_SelectStmt"):
                opp_val = getattr(value, "go_SelectStmt", None)
                setattr(value, "go_SelectStmt", self)

    @property
    def go_Statement360(self):
        return self.__go_Statement360

    @go_Statement360.setter
    def go_Statement360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement360", None)
        self.__go_Statement360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Declaration361"):
                opp_val = getattr(old_value, "go_Declaration361", None)
                if opp_val == self:
                    setattr(old_value, "go_Declaration361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Declaration361"):
                opp_val = getattr(value, "go_Declaration361", None)
                setattr(value, "go_Declaration361", self)

    @property
    def go_Statement386(self):
        return self.__go_Statement386

    @go_Statement386.setter
    def go_Statement386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement386", None)
        self.__go_Statement386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ForStmt"):
                opp_val = getattr(old_value, "go_ForStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_ForStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ForStmt"):
                opp_val = getattr(value, "go_ForStmt", None)
                setattr(value, "go_ForStmt", self)

    @property
    def go_Statement404(self):
        return self.__go_Statement404

    @go_Statement404.setter
    def go_Statement404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement404", None)
        self.__go_Statement404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_LabeledStmt403"):
                opp_val = getattr(old_value, "go_LabeledStmt403", None)
                if opp_val == self:
                    setattr(old_value, "go_LabeledStmt403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_LabeledStmt403"):
                opp_val = getattr(value, "go_LabeledStmt403", None)
                setattr(value, "go_LabeledStmt403", self)

    @property
    def go_Statement377(self):
        return self.__go_Statement377

    @go_Statement377.setter
    def go_Statement377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement377", None)
        self.__go_Statement377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Block378"):
                opp_val = getattr(old_value, "go_Block378", None)
                if opp_val == self:
                    setattr(old_value, "go_Block378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Block378"):
                opp_val = getattr(value, "go_Block378", None)
                setattr(value, "go_Block378", self)

    @property
    def go_Statement375(self):
        return self.__go_Statement375

    @go_Statement375.setter
    def go_Statement375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement375", None)
        self.__go_Statement375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_GotoStmt"):
                opp_val = getattr(old_value, "go_GotoStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_GotoStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_GotoStmt"):
                opp_val = getattr(value, "go_GotoStmt", None)
                setattr(value, "go_GotoStmt", self)

    @property
    def go_Statement(self):
        return self.__go_Statement

    @go_Statement.setter
    def go_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement", None)
        self.__go_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_StatementList118"):
                opp_val = getattr(old_value, "go_StatementList118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_StatementList118"):
                opp_val = getattr(value, "go_StatementList118", None)
                if opp_val is None:
                    setattr(value, "go_StatementList118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_Statement373(self):
        return self.__go_Statement373

    @go_Statement373.setter
    def go_Statement373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement373", None)
        self.__go_Statement373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ContinueStmt"):
                opp_val = getattr(old_value, "go_ContinueStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_ContinueStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ContinueStmt"):
                opp_val = getattr(value, "go_ContinueStmt", None)
                setattr(value, "go_ContinueStmt", self)

    @property
    def go_Statement367(self):
        return self.__go_Statement367

    @go_Statement367.setter
    def go_Statement367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Statement__go_Statement367", None)
        self.__go_Statement367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_GoStmt"):
                opp_val = getattr(old_value, "go_GoStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_GoStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_GoStmt"):
                opp_val = getattr(value, "go_GoStmt", None)
                setattr(value, "go_GoStmt", self)

class go_TypeSpec:

    pass
class go_ExpressionList:

    pass
class go_ConstSpec:

    pass
class go_Receiver:

    pass
class go_FunctionBody:

    pass
class go_MethodSpec:

    pass
class go_ParameterDecl:

    pass
class go_ParameterList:

    pass
class Receiver:

    pass
class go_StatementList:

    pass
class go_Block:

    pass
class go_KeyType:

    pass
class go_InterfaceTypeName:

    pass
class go_MethodName:

    pass
class go_IdentifierList:

    pass
class go_FieldDecl:

    pass
class go_Expression:

    pass
class go_ElementType:

    pass
class go_ArrayLength:

    pass
class go_Result:

    pass
class go_Parameters(Receiver):

    pass
class go_Signature:

    pass
class go_string_lit:

    def __init__(self, raw_string_lit: str, interpreted_string_lit: str, go_string_lit: "go_Tag" = None, go_string_lit220: "go_BasicLit" = None, go_string_lit565: "go_ImportPath" = None):
        self.raw_string_lit = raw_string_lit
        self.interpreted_string_lit = interpreted_string_lit
        self.go_string_lit = go_string_lit
        self.go_string_lit220 = go_string_lit220
        self.go_string_lit565 = go_string_lit565
        
    @property
    def raw_string_lit(self) -> str:
        return self.__raw_string_lit

    @raw_string_lit.setter
    def raw_string_lit(self, raw_string_lit: str):
        self.__raw_string_lit = raw_string_lit

    @property
    def interpreted_string_lit(self) -> str:
        return self.__interpreted_string_lit

    @interpreted_string_lit.setter
    def interpreted_string_lit(self, interpreted_string_lit: str):
        self.__interpreted_string_lit = interpreted_string_lit

    @property
    def go_string_lit220(self):
        return self.__go_string_lit220

    @go_string_lit220.setter
    def go_string_lit220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_string_lit__go_string_lit220", None)
        self.__go_string_lit220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BasicLit219"):
                opp_val = getattr(old_value, "go_BasicLit219", None)
                if opp_val == self:
                    setattr(old_value, "go_BasicLit219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BasicLit219"):
                opp_val = getattr(value, "go_BasicLit219", None)
                setattr(value, "go_BasicLit219", self)

    @property
    def go_string_lit(self):
        return self.__go_string_lit

    @go_string_lit.setter
    def go_string_lit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_string_lit__go_string_lit", None)
        self.__go_string_lit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Tag64"):
                opp_val = getattr(old_value, "go_Tag64", None)
                if opp_val == self:
                    setattr(old_value, "go_Tag64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Tag64"):
                opp_val = getattr(value, "go_Tag64", None)
                setattr(value, "go_Tag64", self)

    @property
    def go_string_lit565(self):
        return self.__go_string_lit565

    @go_string_lit565.setter
    def go_string_lit565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_string_lit__go_string_lit565", None)
        self.__go_string_lit565 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ImportPath564"):
                opp_val = getattr(old_value, "go_ImportPath564", None)
                if opp_val == self:
                    setattr(old_value, "go_ImportPath564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ImportPath564"):
                opp_val = getattr(value, "go_ImportPath564", None)
                setattr(value, "go_ImportPath564", self)

class go_Tag:

    pass
class go_EmbeddedField:

    pass
class go_ChannelType:

    pass
class go_MapType:

    pass
class go_InterfaceType:

    pass
class go_FunctionType:

    pass
class go_PointerType:

    pass
class go_StructType:

    pass
class go_TopLevelDecl:

    pass
class go_ImportDecl:

    pass
class go_PackageClause:

    pass
class go_SouceFile:

    pass
class go_TypeLitLinha:

    pass
class go_QualifiedIdent(OperandName):

    pass
class go_TypeNameLinha:

    pass
class go_identifier(OperandName):

    def __init__(self, LETTER: str, DECIMAL_DIGIT: str, go_identifier: "go_TypeName" = None, go_identifier17: "go_TypeNameLinha" = None, go_identifier101: "go_MethodName" = None, go_identifier153: "go_IdentifierList" = None, go_identifier161: "go_TypeSpec" = None, go_identifier225: "go_QualifiedIdent" = None, go_identifier191: "go_FunctionName" = None, go_identifier273: "go_FieldName" = None, go_identifier312: "go_Selector" = None, go_identifier407: "go_Label" = None, go_identifier461: "go_TypeSwitchGuard" = None, go_identifier555: "go_PackageName" = None):
        self.LETTER = LETTER
        self.DECIMAL_DIGIT = DECIMAL_DIGIT
        self.go_identifier = go_identifier
        self.go_identifier17 = go_identifier17
        self.go_identifier101 = go_identifier101
        self.go_identifier153 = go_identifier153
        self.go_identifier161 = go_identifier161
        self.go_identifier225 = go_identifier225
        self.go_identifier191 = go_identifier191
        self.go_identifier273 = go_identifier273
        self.go_identifier312 = go_identifier312
        self.go_identifier407 = go_identifier407
        self.go_identifier461 = go_identifier461
        self.go_identifier555 = go_identifier555
        
    @property
    def DECIMAL_DIGIT(self) -> str:
        return self.__DECIMAL_DIGIT

    @DECIMAL_DIGIT.setter
    def DECIMAL_DIGIT(self, DECIMAL_DIGIT: str):
        self.__DECIMAL_DIGIT = DECIMAL_DIGIT

    @property
    def LETTER(self) -> str:
        return self.__LETTER

    @LETTER.setter
    def LETTER(self, LETTER: str):
        self.__LETTER = LETTER

    @property
    def go_identifier101(self):
        return self.__go_identifier101

    @go_identifier101.setter
    def go_identifier101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier101", None)
        self.__go_identifier101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_MethodName100"):
                opp_val = getattr(old_value, "go_MethodName100", None)
                if opp_val == self:
                    setattr(old_value, "go_MethodName100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_MethodName100"):
                opp_val = getattr(value, "go_MethodName100", None)
                setattr(value, "go_MethodName100", self)

    @property
    def go_identifier17(self):
        return self.__go_identifier17

    @go_identifier17.setter
    def go_identifier17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier17", None)
        self.__go_identifier17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TypeNameLinha16"):
                opp_val = getattr(old_value, "go_TypeNameLinha16", None)
                if opp_val == self:
                    setattr(old_value, "go_TypeNameLinha16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TypeNameLinha16"):
                opp_val = getattr(value, "go_TypeNameLinha16", None)
                setattr(value, "go_TypeNameLinha16", self)

    @property
    def go_identifier225(self):
        return self.__go_identifier225

    @go_identifier225.setter
    def go_identifier225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier225", None)
        self.__go_identifier225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_QualifiedIdent224"):
                opp_val = getattr(old_value, "go_QualifiedIdent224", None)
                if opp_val == self:
                    setattr(old_value, "go_QualifiedIdent224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_QualifiedIdent224"):
                opp_val = getattr(value, "go_QualifiedIdent224", None)
                setattr(value, "go_QualifiedIdent224", self)

    @property
    def go_identifier407(self):
        return self.__go_identifier407

    @go_identifier407.setter
    def go_identifier407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier407", None)
        self.__go_identifier407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Label406"):
                opp_val = getattr(old_value, "go_Label406", None)
                if opp_val == self:
                    setattr(old_value, "go_Label406", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Label406"):
                opp_val = getattr(value, "go_Label406", None)
                setattr(value, "go_Label406", self)

    @property
    def go_identifier555(self):
        return self.__go_identifier555

    @go_identifier555.setter
    def go_identifier555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier555", None)
        self.__go_identifier555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PackageName554"):
                opp_val = getattr(old_value, "go_PackageName554", None)
                if opp_val == self:
                    setattr(old_value, "go_PackageName554", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PackageName554"):
                opp_val = getattr(value, "go_PackageName554", None)
                setattr(value, "go_PackageName554", self)

    @property
    def go_identifier461(self):
        return self.__go_identifier461

    @go_identifier461.setter
    def go_identifier461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier461", None)
        self.__go_identifier461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TypeSwitchGuard460"):
                opp_val = getattr(old_value, "go_TypeSwitchGuard460", None)
                if opp_val == self:
                    setattr(old_value, "go_TypeSwitchGuard460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TypeSwitchGuard460"):
                opp_val = getattr(value, "go_TypeSwitchGuard460", None)
                setattr(value, "go_TypeSwitchGuard460", self)

    @property
    def go_identifier273(self):
        return self.__go_identifier273

    @go_identifier273.setter
    def go_identifier273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier273", None)
        self.__go_identifier273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_FieldName272"):
                opp_val = getattr(old_value, "go_FieldName272", None)
                if opp_val == self:
                    setattr(old_value, "go_FieldName272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_FieldName272"):
                opp_val = getattr(value, "go_FieldName272", None)
                setattr(value, "go_FieldName272", self)

    @property
    def go_identifier312(self):
        return self.__go_identifier312

    @go_identifier312.setter
    def go_identifier312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier312", None)
        self.__go_identifier312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Selector311"):
                opp_val = getattr(old_value, "go_Selector311", None)
                if opp_val == self:
                    setattr(old_value, "go_Selector311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Selector311"):
                opp_val = getattr(value, "go_Selector311", None)
                setattr(value, "go_Selector311", self)

    @property
    def go_identifier191(self):
        return self.__go_identifier191

    @go_identifier191.setter
    def go_identifier191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier191", None)
        self.__go_identifier191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_FunctionName190"):
                opp_val = getattr(old_value, "go_FunctionName190", None)
                if opp_val == self:
                    setattr(old_value, "go_FunctionName190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_FunctionName190"):
                opp_val = getattr(value, "go_FunctionName190", None)
                setattr(value, "go_FunctionName190", self)

    @property
    def go_identifier(self):
        return self.__go_identifier

    @go_identifier.setter
    def go_identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier", None)
        self.__go_identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TypeName12"):
                opp_val = getattr(old_value, "go_TypeName12", None)
                if opp_val == self:
                    setattr(old_value, "go_TypeName12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TypeName12"):
                opp_val = getattr(value, "go_TypeName12", None)
                setattr(value, "go_TypeName12", self)

    @property
    def go_identifier153(self):
        return self.__go_identifier153

    @go_identifier153.setter
    def go_identifier153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier153", None)
        self.__go_identifier153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IdentifierList152"):
                opp_val = getattr(old_value, "go_IdentifierList152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IdentifierList152"):
                opp_val = getattr(value, "go_IdentifierList152", None)
                if opp_val is None:
                    setattr(value, "go_IdentifierList152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_identifier161(self):
        return self.__go_identifier161

    @go_identifier161.setter
    def go_identifier161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_identifier__go_identifier161", None)
        self.__go_identifier161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TypeSpec160"):
                opp_val = getattr(old_value, "go_TypeSpec160", None)
                if opp_val == self:
                    setattr(old_value, "go_TypeSpec160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TypeSpec160"):
                opp_val = getattr(value, "go_TypeSpec160", None)
                setattr(value, "go_TypeSpec160", self)

class go_TypeLit:

    pass
class go_TypeName:

    pass
class go_Type:

    pass
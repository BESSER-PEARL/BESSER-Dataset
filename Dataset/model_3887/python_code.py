from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TerminalExpression:

    pass
class gaml_DoubleLiteral(TerminalExpression):

    pass
class gaml_StringLiteral(TerminalExpression):

    pass
class gaml_ColorLiteral(TerminalExpression):

    pass
class gaml_IntLiteral(TerminalExpression):

    pass
class gaml_ReservedLiteral(TerminalExpression):

    pass
class gaml_BooleanLiteral(TerminalExpression):

    pass
class S_Definition:

    pass
class gaml_S_Var(S_Definition):

    pass
class gaml_S_Action(S_Definition):

    pass
class GamlDefinition:

    pass
class gaml_UnitFakeDefinition(GamlDefinition):

    pass
class gaml_SkillFakeDefinition(GamlDefinition):

    pass
class gaml_ActionDefinition(GamlDefinition):

    pass
class gaml_EquationDefinition(GamlDefinition):

    pass
class gaml_GamlDefinition:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gaml_VarDefinition(GamlDefinition):

    pass
class gaml_TypeInfo:

    pass
class S_Assignment:

    pass
class gaml_S_Set(S_Assignment):

    pass
class gaml_S_DirectAssignment(S_Assignment):

    pass
class gaml_ActionArguments:

    pass
class ActionDefinition:

    pass
class gaml_TypeDefinition(GamlDefinition, ActionDefinition):

    pass
class gaml_ActionFakeDefinition(ActionDefinition):

    pass
class gaml_EObject:

    pass
class Expression:

    pass
class gaml_Unary(Expression):

    pass
class gaml_If(Expression):

    pass
class gaml_SkillRef(Expression):

    pass
class gaml_Array(Expression):

    pass
class gaml_ArgumentPair(Expression):

    pass
class gaml_TypeRef(Expression):

    pass
class gaml_TerminalExpression(Expression):

    pass
class gaml_Point(Expression):

    pass
class gaml_UnitName(Expression):

    pass
class gaml_Binary(Expression):

    pass
class gaml_EquationRef(Expression):

    pass
class gaml_Cast(Expression):

    pass
class gaml_Unit(Expression):

    pass
class gaml_ActionRef(Expression):

    pass
class gaml_Function(Expression):

    pass
class gaml_Pair(Expression):

    pass
class gaml_Access(Expression):

    def __init__(self, named_exp: str, gaml_Access: "gaml_ExpressionList" = None):
        self.named_exp = named_exp
        self.gaml_Access = gaml_Access
        
    @property
    def named_exp(self) -> str:
        return self.__named_exp

    @named_exp.setter
    def named_exp(self, named_exp: str):
        self.__named_exp = named_exp

    @property
    def gaml_Access(self):
        return self.__gaml_Access

    @gaml_Access.setter
    def gaml_Access(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Access__gaml_Access", None)
        self.__gaml_Access = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_ExpressionList81"):
                opp_val = getattr(old_value, "gaml_ExpressionList81", None)
                if opp_val == self:
                    setattr(old_value, "gaml_ExpressionList81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_ExpressionList81"):
                opp_val = getattr(value, "gaml_ExpressionList81", None)
                setattr(value, "gaml_ExpressionList81", self)

class gaml_VariableRef(Expression):

    pass
class gaml_ExpressionList(Expression):

    pass
class gaml_Parameter(Expression):

    def __init__(self, builtInFacetKey: str):
        self.builtInFacetKey = builtInFacetKey
        
    @property
    def builtInFacetKey(self) -> str:
        return self.__builtInFacetKey

    @builtInFacetKey.setter
    def builtInFacetKey(self, builtInFacetKey: str):
        self.__builtInFacetKey = builtInFacetKey

class gaml_Parameters(Expression):

    pass
class EquationDefinition:

    pass
class gaml_EquationFakeDefinition(EquationDefinition):

    pass
class gaml_HeadlessExperiment:

    def __init__(self, key: str, firstFacet: str, name: str, importURI: str, gaml_HeadlessExperiment15: set["gaml_Facet"] = None, gaml_HeadlessExperiment17: "gaml_Block" = None, gaml_HeadlessExperiment: "gaml_ExperimentFileStructure" = None):
        self.key = key
        self.firstFacet = firstFacet
        self.name = name
        self.importURI = importURI
        self.gaml_HeadlessExperiment15 = gaml_HeadlessExperiment15 if gaml_HeadlessExperiment15 is not None else set()
        self.gaml_HeadlessExperiment17 = gaml_HeadlessExperiment17
        self.gaml_HeadlessExperiment = gaml_HeadlessExperiment
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def firstFacet(self) -> str:
        return self.__firstFacet

    @firstFacet.setter
    def firstFacet(self, firstFacet: str):
        self.__firstFacet = firstFacet

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def gaml_HeadlessExperiment(self):
        return self.__gaml_HeadlessExperiment

    @gaml_HeadlessExperiment.setter
    def gaml_HeadlessExperiment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_HeadlessExperiment__gaml_HeadlessExperiment", None)
        self.__gaml_HeadlessExperiment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_ExperimentFileStructure"):
                opp_val = getattr(old_value, "gaml_ExperimentFileStructure", None)
                if opp_val == self:
                    setattr(old_value, "gaml_ExperimentFileStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_ExperimentFileStructure"):
                opp_val = getattr(value, "gaml_ExperimentFileStructure", None)
                setattr(value, "gaml_ExperimentFileStructure", self)

    @property
    def gaml_HeadlessExperiment15(self):
        return self.__gaml_HeadlessExperiment15

    @gaml_HeadlessExperiment15.setter
    def gaml_HeadlessExperiment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_HeadlessExperiment__gaml_HeadlessExperiment15", None)
        self.__gaml_HeadlessExperiment15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gaml_Facet"):
                    opp_val = getattr(item, "gaml_Facet", None)
                    
                    if opp_val == self:
                        setattr(item, "gaml_Facet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gaml_Facet"):
                    opp_val = getattr(item, "gaml_Facet", None)
                    
                    setattr(item, "gaml_Facet", self)
                    

    @property
    def gaml_HeadlessExperiment17(self):
        return self.__gaml_HeadlessExperiment17

    @gaml_HeadlessExperiment17.setter
    def gaml_HeadlessExperiment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_HeadlessExperiment__gaml_HeadlessExperiment17", None)
        self.__gaml_HeadlessExperiment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block18"):
                opp_val = getattr(old_value, "gaml_Block18", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block18"):
                opp_val = getattr(value, "gaml_Block18", None)
                setattr(value, "gaml_Block18", self)

class gaml_Statement:

    def __init__(self, key: str, firstFacet: str, gaml_Statement20: "gaml_Expression" = None, gaml_Statement23: set["gaml_Facet"] = None, gaml_Statement26: "gaml_Block" = None, gaml_Statement: "gaml_Block" = None):
        self.key = key
        self.firstFacet = firstFacet
        self.gaml_Statement20 = gaml_Statement20
        self.gaml_Statement23 = gaml_Statement23 if gaml_Statement23 is not None else set()
        self.gaml_Statement26 = gaml_Statement26
        self.gaml_Statement = gaml_Statement
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def firstFacet(self) -> str:
        return self.__firstFacet

    @firstFacet.setter
    def firstFacet(self, firstFacet: str):
        self.__firstFacet = firstFacet

    @property
    def gaml_Statement20(self):
        return self.__gaml_Statement20

    @gaml_Statement20.setter
    def gaml_Statement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement20", None)
        self.__gaml_Statement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression21"):
                opp_val = getattr(old_value, "gaml_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression21"):
                opp_val = getattr(value, "gaml_Expression21", None)
                setattr(value, "gaml_Expression21", self)

    @property
    def gaml_Statement(self):
        return self.__gaml_Statement

    @gaml_Statement.setter
    def gaml_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement", None)
        self.__gaml_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block9"):
                opp_val = getattr(old_value, "gaml_Block9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block9"):
                opp_val = getattr(value, "gaml_Block9", None)
                if opp_val is None:
                    setattr(value, "gaml_Block9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Statement23(self):
        return self.__gaml_Statement23

    @gaml_Statement23.setter
    def gaml_Statement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement23", None)
        self.__gaml_Statement23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gaml_Facet24"):
                    opp_val = getattr(item, "gaml_Facet24", None)
                    
                    if opp_val == self:
                        setattr(item, "gaml_Facet24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gaml_Facet24"):
                    opp_val = getattr(item, "gaml_Facet24", None)
                    
                    setattr(item, "gaml_Facet24", self)
                    

    @property
    def gaml_Statement26(self):
        return self.__gaml_Statement26

    @gaml_Statement26.setter
    def gaml_Statement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement26", None)
        self.__gaml_Statement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block27"):
                opp_val = getattr(old_value, "gaml_Block27", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block27"):
                opp_val = getattr(value, "gaml_Block27", None)
                setattr(value, "gaml_Block27", self)

class TypeDefinition:

    pass
class gaml_TypeFakeDefinition(TypeDefinition):

    pass
class S_Declaration:

    pass
class gaml_S_Loop(S_Declaration):

    pass
class gaml_S_Reflex(S_Declaration):

    pass
class gaml_S_Definition(S_Declaration, ActionDefinition):

    pass
class Statement:

    pass
class gaml_S_Equations(Statement, EquationDefinition):

    pass
class gaml_S_Do(Statement):

    pass
class gaml_S_Assignment(Statement):

    pass
class gaml_speciesOrGridDisplayStatement(Statement):

    pass
class gaml_S_Species(Statement, S_Declaration, TypeDefinition):

    pass
class gaml_S_Other(Statement):

    pass
class gaml_S_Return(Statement):

    pass
class gaml_S_If(Statement):

    pass
class gaml_S_Solve(Statement):

    pass
class gaml_S_Display(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gaml_S_Global(Statement):

    pass
class gaml_Pragma:

    def __init__(self, name: str, gaml_Pragma: "gaml_Model" = None):
        self.name = name
        self.gaml_Pragma = gaml_Pragma
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gaml_Pragma(self):
        return self.__gaml_Pragma

    @gaml_Pragma.setter
    def gaml_Pragma(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Pragma__gaml_Pragma", None)
        self.__gaml_Pragma = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Model"):
                opp_val = getattr(old_value, "gaml_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Model"):
                opp_val = getattr(value, "gaml_Model", None)
                if opp_val is None:
                    setattr(value, "gaml_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VarDefinition:

    pass
class gaml_S_Declaration(Statement, VarDefinition):

    pass
class gaml_S_Experiment(Statement, VarDefinition):

    pass
class gaml_Import(VarDefinition):

    def __init__(self, importURI: str, gaml_Import: "gaml_Model" = None):
        self.importURI = importURI
        self.gaml_Import = gaml_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def gaml_Import(self):
        return self.__gaml_Import

    @gaml_Import.setter
    def gaml_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Import__gaml_Import", None)
        self.__gaml_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Model4"):
                opp_val = getattr(old_value, "gaml_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Model4"):
                opp_val = getattr(value, "gaml_Model4", None)
                if opp_val is None:
                    setattr(value, "gaml_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gaml_Facet(VarDefinition):

    def __init__(self, key: str, gaml_Facet: "gaml_HeadlessExperiment" = None, gaml_Facet24: "gaml_Statement" = None, gaml_Facet47: "gaml_Expression" = None, gaml_Facet50: "gaml_Block" = None):
        self.key = key
        self.gaml_Facet = gaml_Facet
        self.gaml_Facet24 = gaml_Facet24
        self.gaml_Facet47 = gaml_Facet47
        self.gaml_Facet50 = gaml_Facet50
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def gaml_Facet(self):
        return self.__gaml_Facet

    @gaml_Facet.setter
    def gaml_Facet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet", None)
        self.__gaml_Facet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_HeadlessExperiment15"):
                opp_val = getattr(old_value, "gaml_HeadlessExperiment15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_HeadlessExperiment15"):
                opp_val = getattr(value, "gaml_HeadlessExperiment15", None)
                if opp_val is None:
                    setattr(value, "gaml_HeadlessExperiment15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Facet50(self):
        return self.__gaml_Facet50

    @gaml_Facet50.setter
    def gaml_Facet50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet50", None)
        self.__gaml_Facet50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block51"):
                opp_val = getattr(old_value, "gaml_Block51", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block51"):
                opp_val = getattr(value, "gaml_Block51", None)
                setattr(value, "gaml_Block51", self)

    @property
    def gaml_Facet24(self):
        return self.__gaml_Facet24

    @gaml_Facet24.setter
    def gaml_Facet24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet24", None)
        self.__gaml_Facet24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Statement23"):
                opp_val = getattr(old_value, "gaml_Statement23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Statement23"):
                opp_val = getattr(value, "gaml_Statement23", None)
                if opp_val is None:
                    setattr(value, "gaml_Statement23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Facet47(self):
        return self.__gaml_Facet47

    @gaml_Facet47.setter
    def gaml_Facet47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet47", None)
        self.__gaml_Facet47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression48"):
                opp_val = getattr(old_value, "gaml_Expression48", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression48"):
                opp_val = getattr(value, "gaml_Expression48", None)
                setattr(value, "gaml_Expression48", self)

class gaml_VarFakeDefinition(VarDefinition):

    pass
class gaml_ArgumentDefinition(VarDefinition):

    pass
class gaml_Expression:

    def __init__(self, op: str, gaml_Expression: "gaml_StringEvaluator" = None, gaml_Expression21: "gaml_Statement" = None, gaml_Expression12: "gaml_Block" = None, gaml_Expression42: "gaml_ArgumentDefinition" = None, gaml_Expression45: "gaml_ArgumentDefinition" = None, gaml_Expression30: "gaml_S_Definition" = None, gaml_Expression34: "gaml_S_Assignment" = None, gaml_Expression70: "gaml_ExpressionList" = None, gaml_Expression74: "gaml_TypeInfo" = None, gaml_Expression77: "gaml_TypeInfo" = None, gaml_Expression48: "gaml_Facet" = None, gaml_Expression54: "gaml_Expression" = None, gaml_Expression52: "gaml_Expression" = None, gaml_Expression57: "gaml_Expression" = None, gaml_Expression55: "gaml_Expression" = None, gaml_Expression59: "gaml_Function" = None, gaml_Expression85: "gaml_Point" = None, gaml_Expression79: "gaml_If" = None):
        self.op = op
        self.gaml_Expression = gaml_Expression
        self.gaml_Expression21 = gaml_Expression21
        self.gaml_Expression12 = gaml_Expression12
        self.gaml_Expression42 = gaml_Expression42
        self.gaml_Expression45 = gaml_Expression45
        self.gaml_Expression30 = gaml_Expression30
        self.gaml_Expression34 = gaml_Expression34
        self.gaml_Expression70 = gaml_Expression70
        self.gaml_Expression74 = gaml_Expression74
        self.gaml_Expression77 = gaml_Expression77
        self.gaml_Expression48 = gaml_Expression48
        self.gaml_Expression54 = gaml_Expression54
        self.gaml_Expression52 = gaml_Expression52
        self.gaml_Expression57 = gaml_Expression57
        self.gaml_Expression55 = gaml_Expression55
        self.gaml_Expression59 = gaml_Expression59
        self.gaml_Expression85 = gaml_Expression85
        self.gaml_Expression79 = gaml_Expression79
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_Expression52(self):
        return self.__gaml_Expression52

    @gaml_Expression52.setter
    def gaml_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression52", None)
        self.__gaml_Expression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression54"):
                opp_val = getattr(old_value, "gaml_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression54"):
                opp_val = getattr(value, "gaml_Expression54", None)
                setattr(value, "gaml_Expression54", self)

    @property
    def gaml_Expression70(self):
        return self.__gaml_Expression70

    @gaml_Expression70.setter
    def gaml_Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression70", None)
        self.__gaml_Expression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_ExpressionList69"):
                opp_val = getattr(old_value, "gaml_ExpressionList69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_ExpressionList69"):
                opp_val = getattr(value, "gaml_ExpressionList69", None)
                if opp_val is None:
                    setattr(value, "gaml_ExpressionList69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Expression54(self):
        return self.__gaml_Expression54

    @gaml_Expression54.setter
    def gaml_Expression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression54", None)
        self.__gaml_Expression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression52"):
                opp_val = getattr(old_value, "gaml_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression52"):
                opp_val = getattr(value, "gaml_Expression52", None)
                setattr(value, "gaml_Expression52", self)

    @property
    def gaml_Expression45(self):
        return self.__gaml_Expression45

    @gaml_Expression45.setter
    def gaml_Expression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression45", None)
        self.__gaml_Expression45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_ArgumentDefinition44"):
                opp_val = getattr(old_value, "gaml_ArgumentDefinition44", None)
                if opp_val == self:
                    setattr(old_value, "gaml_ArgumentDefinition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_ArgumentDefinition44"):
                opp_val = getattr(value, "gaml_ArgumentDefinition44", None)
                setattr(value, "gaml_ArgumentDefinition44", self)

    @property
    def gaml_Expression48(self):
        return self.__gaml_Expression48

    @gaml_Expression48.setter
    def gaml_Expression48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression48", None)
        self.__gaml_Expression48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Facet47"):
                opp_val = getattr(old_value, "gaml_Facet47", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Facet47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Facet47"):
                opp_val = getattr(value, "gaml_Facet47", None)
                setattr(value, "gaml_Facet47", self)

    @property
    def gaml_Expression74(self):
        return self.__gaml_Expression74

    @gaml_Expression74.setter
    def gaml_Expression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression74", None)
        self.__gaml_Expression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_TypeInfo73"):
                opp_val = getattr(old_value, "gaml_TypeInfo73", None)
                if opp_val == self:
                    setattr(old_value, "gaml_TypeInfo73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_TypeInfo73"):
                opp_val = getattr(value, "gaml_TypeInfo73", None)
                setattr(value, "gaml_TypeInfo73", self)

    @property
    def gaml_Expression21(self):
        return self.__gaml_Expression21

    @gaml_Expression21.setter
    def gaml_Expression21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression21", None)
        self.__gaml_Expression21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Statement20"):
                opp_val = getattr(old_value, "gaml_Statement20", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Statement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Statement20"):
                opp_val = getattr(value, "gaml_Statement20", None)
                setattr(value, "gaml_Statement20", self)

    @property
    def gaml_Expression55(self):
        return self.__gaml_Expression55

    @gaml_Expression55.setter
    def gaml_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression55", None)
        self.__gaml_Expression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression57"):
                opp_val = getattr(old_value, "gaml_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression57"):
                opp_val = getattr(value, "gaml_Expression57", None)
                setattr(value, "gaml_Expression57", self)

    @property
    def gaml_Expression(self):
        return self.__gaml_Expression

    @gaml_Expression.setter
    def gaml_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression", None)
        self.__gaml_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_StringEvaluator"):
                opp_val = getattr(old_value, "gaml_StringEvaluator", None)
                if opp_val == self:
                    setattr(old_value, "gaml_StringEvaluator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_StringEvaluator"):
                opp_val = getattr(value, "gaml_StringEvaluator", None)
                setattr(value, "gaml_StringEvaluator", self)

    @property
    def gaml_Expression79(self):
        return self.__gaml_Expression79

    @gaml_Expression79.setter
    def gaml_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression79", None)
        self.__gaml_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_If"):
                opp_val = getattr(old_value, "gaml_If", None)
                if opp_val == self:
                    setattr(old_value, "gaml_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_If"):
                opp_val = getattr(value, "gaml_If", None)
                setattr(value, "gaml_If", self)

    @property
    def gaml_Expression30(self):
        return self.__gaml_Expression30

    @gaml_Expression30.setter
    def gaml_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression30", None)
        self.__gaml_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_S_Definition"):
                opp_val = getattr(old_value, "gaml_S_Definition", None)
                if opp_val == self:
                    setattr(old_value, "gaml_S_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_S_Definition"):
                opp_val = getattr(value, "gaml_S_Definition", None)
                setattr(value, "gaml_S_Definition", self)

    @property
    def gaml_Expression12(self):
        return self.__gaml_Expression12

    @gaml_Expression12.setter
    def gaml_Expression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression12", None)
        self.__gaml_Expression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block11"):
                opp_val = getattr(old_value, "gaml_Block11", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block11"):
                opp_val = getattr(value, "gaml_Block11", None)
                setattr(value, "gaml_Block11", self)

    @property
    def gaml_Expression59(self):
        return self.__gaml_Expression59

    @gaml_Expression59.setter
    def gaml_Expression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression59", None)
        self.__gaml_Expression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Function"):
                opp_val = getattr(old_value, "gaml_Function", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Function"):
                opp_val = getattr(value, "gaml_Function", None)
                setattr(value, "gaml_Function", self)

    @property
    def gaml_Expression42(self):
        return self.__gaml_Expression42

    @gaml_Expression42.setter
    def gaml_Expression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression42", None)
        self.__gaml_Expression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_ArgumentDefinition41"):
                opp_val = getattr(old_value, "gaml_ArgumentDefinition41", None)
                if opp_val == self:
                    setattr(old_value, "gaml_ArgumentDefinition41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_ArgumentDefinition41"):
                opp_val = getattr(value, "gaml_ArgumentDefinition41", None)
                setattr(value, "gaml_ArgumentDefinition41", self)

    @property
    def gaml_Expression85(self):
        return self.__gaml_Expression85

    @gaml_Expression85.setter
    def gaml_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression85", None)
        self.__gaml_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Point"):
                opp_val = getattr(old_value, "gaml_Point", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Point"):
                opp_val = getattr(value, "gaml_Point", None)
                setattr(value, "gaml_Point", self)

    @property
    def gaml_Expression57(self):
        return self.__gaml_Expression57

    @gaml_Expression57.setter
    def gaml_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression57", None)
        self.__gaml_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression55"):
                opp_val = getattr(old_value, "gaml_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression55"):
                opp_val = getattr(value, "gaml_Expression55", None)
                setattr(value, "gaml_Expression55", self)

    @property
    def gaml_Expression34(self):
        return self.__gaml_Expression34

    @gaml_Expression34.setter
    def gaml_Expression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression34", None)
        self.__gaml_Expression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_S_Assignment"):
                opp_val = getattr(old_value, "gaml_S_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "gaml_S_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_S_Assignment"):
                opp_val = getattr(value, "gaml_S_Assignment", None)
                setattr(value, "gaml_S_Assignment", self)

    @property
    def gaml_Expression77(self):
        return self.__gaml_Expression77

    @gaml_Expression77.setter
    def gaml_Expression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Expression__gaml_Expression77", None)
        self.__gaml_Expression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_TypeInfo76"):
                opp_val = getattr(old_value, "gaml_TypeInfo76", None)
                if opp_val == self:
                    setattr(old_value, "gaml_TypeInfo76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_TypeInfo76"):
                opp_val = getattr(value, "gaml_TypeInfo76", None)
                setattr(value, "gaml_TypeInfo76", self)

class gaml_Block:

    pass
class Entry:

    pass
class gaml_StringEvaluator(Entry):

    def __init__(self, toto: str, gaml_StringEvaluator: "gaml_Expression" = None):
        self.toto = toto
        self.gaml_StringEvaluator = gaml_StringEvaluator
        
    @property
    def toto(self) -> str:
        return self.__toto

    @toto.setter
    def toto(self, toto: str):
        self.__toto = toto

    @property
    def gaml_StringEvaluator(self):
        return self.__gaml_StringEvaluator

    @gaml_StringEvaluator.setter
    def gaml_StringEvaluator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_StringEvaluator__gaml_StringEvaluator", None)
        self.__gaml_StringEvaluator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression"):
                opp_val = getattr(old_value, "gaml_Expression", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression"):
                opp_val = getattr(value, "gaml_Expression", None)
                setattr(value, "gaml_Expression", self)

class gaml_Model(Entry, VarDefinition):

    pass
class gaml_ExperimentFileStructure(Entry):

    pass
class gaml_StandaloneBlock(Entry):

    pass
class gaml_Entry:

    pass
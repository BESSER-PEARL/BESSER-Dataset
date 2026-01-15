from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class S_Definition:

    pass
class gaml_S_Var(S_Definition):

    pass
class gaml_S_Action(S_Definition):

    pass
class TerminalExpression:

    pass
class gaml_DoubleLiteral(TerminalExpression):

    pass
class gaml_IntLiteral(TerminalExpression):

    pass
class gaml_BooleanLiteral(TerminalExpression):

    pass
class gaml_ReservedLiteral(TerminalExpression):

    pass
class gaml_StringLiteral(TerminalExpression):

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

class gaml_TypeInfo:

    pass
class Expression:

    pass
class gaml_TerminalExpression(Expression):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class gaml_Unit(Expression):

    def __init__(self, op: str, gaml_Unit: "gaml_Expression" = None, gaml_Unit76: "gaml_Expression" = None):
        self.op = op
        self.gaml_Unit = gaml_Unit
        self.gaml_Unit76 = gaml_Unit76
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_Unit76(self):
        return self.__gaml_Unit76

    @gaml_Unit76.setter
    def gaml_Unit76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Unit__gaml_Unit76", None)
        self.__gaml_Unit76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression77"):
                opp_val = getattr(old_value, "gaml_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression77"):
                opp_val = getattr(value, "gaml_Expression77", None)
                setattr(value, "gaml_Expression77", self)

    @property
    def gaml_Unit(self):
        return self.__gaml_Unit

    @gaml_Unit.setter
    def gaml_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Unit__gaml_Unit", None)
        self.__gaml_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression74"):
                opp_val = getattr(old_value, "gaml_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression74"):
                opp_val = getattr(value, "gaml_Expression74", None)
                setattr(value, "gaml_Expression74", self)

class gaml_Point(Expression):

    def __init__(self, op: str, gaml_Point: "gaml_Expression" = None, gaml_Point90: "gaml_Expression" = None, gaml_Point93: "gaml_Expression" = None):
        self.op = op
        self.gaml_Point = gaml_Point
        self.gaml_Point90 = gaml_Point90
        self.gaml_Point93 = gaml_Point93
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_Point(self):
        return self.__gaml_Point

    @gaml_Point.setter
    def gaml_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Point__gaml_Point", None)
        self.__gaml_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression88"):
                opp_val = getattr(old_value, "gaml_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression88"):
                opp_val = getattr(value, "gaml_Expression88", None)
                setattr(value, "gaml_Expression88", self)

    @property
    def gaml_Point93(self):
        return self.__gaml_Point93

    @gaml_Point93.setter
    def gaml_Point93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Point__gaml_Point93", None)
        self.__gaml_Point93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression94"):
                opp_val = getattr(old_value, "gaml_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression94"):
                opp_val = getattr(value, "gaml_Expression94", None)
                setattr(value, "gaml_Expression94", self)

    @property
    def gaml_Point90(self):
        return self.__gaml_Point90

    @gaml_Point90.setter
    def gaml_Point90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Point__gaml_Point90", None)
        self.__gaml_Point90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression91"):
                opp_val = getattr(old_value, "gaml_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression91"):
                opp_val = getattr(value, "gaml_Expression91", None)
                setattr(value, "gaml_Expression91", self)

class gaml_VariableRef(Expression):

    pass
class gaml_UnitName(Expression):

    pass
class gaml_Function(Expression):

    pass
class gaml_Access(Expression):

    def __init__(self, op: str, gaml_Access: "gaml_Expression" = None, gaml_Access83: "gaml_Expression" = None):
        self.op = op
        self.gaml_Access = gaml_Access
        self.gaml_Access83 = gaml_Access83
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_Access83(self):
        return self.__gaml_Access83

    @gaml_Access83.setter
    def gaml_Access83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Access__gaml_Access83", None)
        self.__gaml_Access83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression84"):
                opp_val = getattr(old_value, "gaml_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression84"):
                opp_val = getattr(value, "gaml_Expression84", None)
                setattr(value, "gaml_Expression84", self)

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
            if hasattr(old_value, "gaml_Expression81"):
                opp_val = getattr(old_value, "gaml_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression81"):
                opp_val = getattr(value, "gaml_Expression81", None)
                setattr(value, "gaml_Expression81", self)

class gaml_EquationRef(Expression):

    pass
class gaml_SkillRef(Expression):

    pass
class gaml_BinaryOperator(Expression):

    def __init__(self, op: str, gaml_BinaryOperator: "gaml_Expression" = None, gaml_BinaryOperator63: "gaml_Expression" = None):
        self.op = op
        self.gaml_BinaryOperator = gaml_BinaryOperator
        self.gaml_BinaryOperator63 = gaml_BinaryOperator63
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_BinaryOperator(self):
        return self.__gaml_BinaryOperator

    @gaml_BinaryOperator.setter
    def gaml_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_BinaryOperator__gaml_BinaryOperator", None)
        self.__gaml_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression61"):
                opp_val = getattr(old_value, "gaml_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression61"):
                opp_val = getattr(value, "gaml_Expression61", None)
                setattr(value, "gaml_Expression61", self)

    @property
    def gaml_BinaryOperator63(self):
        return self.__gaml_BinaryOperator63

    @gaml_BinaryOperator63.setter
    def gaml_BinaryOperator63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_BinaryOperator__gaml_BinaryOperator63", None)
        self.__gaml_BinaryOperator63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression64"):
                opp_val = getattr(old_value, "gaml_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression64"):
                opp_val = getattr(value, "gaml_Expression64", None)
                setattr(value, "gaml_Expression64", self)

class gaml_Array(Expression):

    pass
class gaml_Parameter(Expression):

    def __init__(self, builtInFacetKey: str, gaml_Parameter: "gaml_VariableRef" = None, gaml_Parameter106: "gaml_Expression" = None):
        self.builtInFacetKey = builtInFacetKey
        self.gaml_Parameter = gaml_Parameter
        self.gaml_Parameter106 = gaml_Parameter106
        
    @property
    def builtInFacetKey(self) -> str:
        return self.__builtInFacetKey

    @builtInFacetKey.setter
    def builtInFacetKey(self, builtInFacetKey: str):
        self.__builtInFacetKey = builtInFacetKey

    @property
    def gaml_Parameter(self):
        return self.__gaml_Parameter

    @gaml_Parameter.setter
    def gaml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Parameter__gaml_Parameter", None)
        self.__gaml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_VariableRef104"):
                opp_val = getattr(old_value, "gaml_VariableRef104", None)
                if opp_val == self:
                    setattr(old_value, "gaml_VariableRef104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_VariableRef104"):
                opp_val = getattr(value, "gaml_VariableRef104", None)
                setattr(value, "gaml_VariableRef104", self)

    @property
    def gaml_Parameter106(self):
        return self.__gaml_Parameter106

    @gaml_Parameter106.setter
    def gaml_Parameter106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Parameter__gaml_Parameter106", None)
        self.__gaml_Parameter106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression107"):
                opp_val = getattr(old_value, "gaml_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression107"):
                opp_val = getattr(value, "gaml_Expression107", None)
                setattr(value, "gaml_Expression107", self)

class gaml_If(Expression):

    def __init__(self, op: str, gaml_If: "gaml_Expression" = None, gaml_If68: "gaml_Expression" = None, gaml_If71: "gaml_Expression" = None):
        self.op = op
        self.gaml_If = gaml_If
        self.gaml_If68 = gaml_If68
        self.gaml_If71 = gaml_If71
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_If71(self):
        return self.__gaml_If71

    @gaml_If71.setter
    def gaml_If71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_If__gaml_If71", None)
        self.__gaml_If71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression72"):
                opp_val = getattr(old_value, "gaml_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression72"):
                opp_val = getattr(value, "gaml_Expression72", None)
                setattr(value, "gaml_Expression72", self)

    @property
    def gaml_If68(self):
        return self.__gaml_If68

    @gaml_If68.setter
    def gaml_If68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_If__gaml_If68", None)
        self.__gaml_If68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression69"):
                opp_val = getattr(old_value, "gaml_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression69"):
                opp_val = getattr(value, "gaml_Expression69", None)
                setattr(value, "gaml_Expression69", self)

    @property
    def gaml_If(self):
        return self.__gaml_If

    @gaml_If.setter
    def gaml_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_If__gaml_If", None)
        self.__gaml_If = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression66"):
                opp_val = getattr(old_value, "gaml_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression66"):
                opp_val = getattr(value, "gaml_Expression66", None)
                setattr(value, "gaml_Expression66", self)

class gaml_TypeRef(Expression):

    pass
class gaml_ExpressionList(Expression):

    pass
class gaml_Unary(Expression):

    def __init__(self, op: str, gaml_Unary: "gaml_Expression" = None):
        self.op = op
        self.gaml_Unary = gaml_Unary
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_Unary(self):
        return self.__gaml_Unary

    @gaml_Unary.setter
    def gaml_Unary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Unary__gaml_Unary", None)
        self.__gaml_Unary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression79"):
                opp_val = getattr(old_value, "gaml_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression79"):
                opp_val = getattr(value, "gaml_Expression79", None)
                setattr(value, "gaml_Expression79", self)

class gaml_ActionRef(Expression):

    pass
class gaml_ArgumentPair(Expression):

    def __init__(self, op: str, gaml_ArgumentPair: "gaml_Expression" = None):
        self.op = op
        self.gaml_ArgumentPair = gaml_ArgumentPair
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def gaml_ArgumentPair(self):
        return self.__gaml_ArgumentPair

    @gaml_ArgumentPair.setter
    def gaml_ArgumentPair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_ArgumentPair__gaml_ArgumentPair", None)
        self.__gaml_ArgumentPair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression51"):
                opp_val = getattr(old_value, "gaml_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression51"):
                opp_val = getattr(value, "gaml_Expression51", None)
                setattr(value, "gaml_Expression51", self)

class GamlDefinition:

    pass
class gaml_EquationDefinition(GamlDefinition):

    pass
class gaml_ActionDefinition(GamlDefinition):

    pass
class gaml_VarDefinition(GamlDefinition):

    pass
class gaml_UnitFakeDefinition(GamlDefinition):

    pass
class gaml_SkillFakeDefinition(GamlDefinition):

    pass
class EquationDefinition:

    pass
class gaml_EquationFakeDefinition(EquationDefinition):

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
class gaml_ActionFakeDefinition(ActionDefinition):

    pass
class gaml_TypeDefinition(GamlDefinition, ActionDefinition):

    pass
class gaml_EObject:

    pass
class TypeDefinition:

    pass
class gaml_TypeFakeDefinition(TypeDefinition):

    pass
class S_Declaration:

    pass
class gaml_S_Loop(S_Declaration):

    pass
class gaml_S_Definition(S_Declaration, ActionDefinition):

    pass
class gaml_S_Reflex(S_Declaration):

    pass
class Statement:

    pass
class gaml_S_Species(Statement, S_Declaration, TypeDefinition):

    pass
class gaml_S_Other(Statement):

    pass
class gaml_S_Equations(EquationDefinition, Statement):

    pass
class gaml_S_Solve(Statement):

    pass
class gaml_S_Return(Statement):

    pass
class gaml_speciesOrGridDisplayStatement(Statement):

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

class gaml_S_Assignment(Statement):

    pass
class gaml_S_Try(Statement):

    pass
class gaml_S_If(Statement):

    pass
class gaml_S_Do(Statement):

    pass
class gaml_S_Global(Statement):

    pass
class gaml_HeadlessExperiment:

    def __init__(self, key: str, firstFacet: str, name: str, importURI: str, gaml_HeadlessExperiment: "gaml_ExperimentFileStructure" = None, gaml_HeadlessExperiment12: set["gaml_Facet"] = None, gaml_HeadlessExperiment14: "gaml_Block" = None):
        self.key = key
        self.firstFacet = firstFacet
        self.name = name
        self.importURI = importURI
        self.gaml_HeadlessExperiment = gaml_HeadlessExperiment
        self.gaml_HeadlessExperiment12 = gaml_HeadlessExperiment12 if gaml_HeadlessExperiment12 is not None else set()
        self.gaml_HeadlessExperiment14 = gaml_HeadlessExperiment14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def firstFacet(self) -> str:
        return self.__firstFacet

    @firstFacet.setter
    def firstFacet(self, firstFacet: str):
        self.__firstFacet = firstFacet

    @property
    def gaml_HeadlessExperiment14(self):
        return self.__gaml_HeadlessExperiment14

    @gaml_HeadlessExperiment14.setter
    def gaml_HeadlessExperiment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_HeadlessExperiment__gaml_HeadlessExperiment14", None)
        self.__gaml_HeadlessExperiment14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block15"):
                opp_val = getattr(old_value, "gaml_Block15", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block15"):
                opp_val = getattr(value, "gaml_Block15", None)
                setattr(value, "gaml_Block15", self)

    @property
    def gaml_HeadlessExperiment12(self):
        return self.__gaml_HeadlessExperiment12

    @gaml_HeadlessExperiment12.setter
    def gaml_HeadlessExperiment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_HeadlessExperiment__gaml_HeadlessExperiment12", None)
        self.__gaml_HeadlessExperiment12 = value if value is not None else set()
        
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

class gaml_Statement:

    def __init__(self, key: str, firstFacet: str, gaml_Statement: "gaml_Block" = None, gaml_Statement17: "gaml_Expression" = None, gaml_Statement20: set["gaml_Facet"] = None, gaml_Statement23: "gaml_Block" = None):
        self.key = key
        self.firstFacet = firstFacet
        self.gaml_Statement = gaml_Statement
        self.gaml_Statement17 = gaml_Statement17
        self.gaml_Statement20 = gaml_Statement20 if gaml_Statement20 is not None else set()
        self.gaml_Statement23 = gaml_Statement23
        
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
    def gaml_Statement20(self):
        return self.__gaml_Statement20

    @gaml_Statement20.setter
    def gaml_Statement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement20", None)
        self.__gaml_Statement20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gaml_Facet21"):
                    opp_val = getattr(item, "gaml_Facet21", None)
                    
                    if opp_val == self:
                        setattr(item, "gaml_Facet21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gaml_Facet21"):
                    opp_val = getattr(item, "gaml_Facet21", None)
                    
                    setattr(item, "gaml_Facet21", self)
                    

    @property
    def gaml_Statement23(self):
        return self.__gaml_Statement23

    @gaml_Statement23.setter
    def gaml_Statement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement23", None)
        self.__gaml_Statement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block24"):
                opp_val = getattr(old_value, "gaml_Block24", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block24"):
                opp_val = getattr(value, "gaml_Block24", None)
                setattr(value, "gaml_Block24", self)

    @property
    def gaml_Statement17(self):
        return self.__gaml_Statement17

    @gaml_Statement17.setter
    def gaml_Statement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Statement__gaml_Statement17", None)
        self.__gaml_Statement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression18"):
                opp_val = getattr(old_value, "gaml_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression18"):
                opp_val = getattr(value, "gaml_Expression18", None)
                setattr(value, "gaml_Expression18", self)

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
class gaml_ArgumentDefinition(VarDefinition):

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

    def __init__(self, key: str, gaml_Facet: "gaml_HeadlessExperiment" = None, gaml_Facet21: "gaml_Statement" = None, gaml_Facet45: "gaml_Expression" = None, gaml_Facet48: "gaml_Block" = None):
        self.key = key
        self.gaml_Facet = gaml_Facet
        self.gaml_Facet21 = gaml_Facet21
        self.gaml_Facet45 = gaml_Facet45
        self.gaml_Facet48 = gaml_Facet48
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def gaml_Facet21(self):
        return self.__gaml_Facet21

    @gaml_Facet21.setter
    def gaml_Facet21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet21", None)
        self.__gaml_Facet21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Statement20"):
                opp_val = getattr(old_value, "gaml_Statement20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Statement20"):
                opp_val = getattr(value, "gaml_Statement20", None)
                if opp_val is None:
                    setattr(value, "gaml_Statement20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Facet48(self):
        return self.__gaml_Facet48

    @gaml_Facet48.setter
    def gaml_Facet48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet48", None)
        self.__gaml_Facet48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Block49"):
                opp_val = getattr(old_value, "gaml_Block49", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Block49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Block49"):
                opp_val = getattr(value, "gaml_Block49", None)
                setattr(value, "gaml_Block49", self)

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
            if hasattr(old_value, "gaml_HeadlessExperiment12"):
                opp_val = getattr(old_value, "gaml_HeadlessExperiment12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_HeadlessExperiment12"):
                opp_val = getattr(value, "gaml_HeadlessExperiment12", None)
                if opp_val is None:
                    setattr(value, "gaml_HeadlessExperiment12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gaml_Facet45(self):
        return self.__gaml_Facet45

    @gaml_Facet45.setter
    def gaml_Facet45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gaml_Facet__gaml_Facet45", None)
        self.__gaml_Facet45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gaml_Expression46"):
                opp_val = getattr(old_value, "gaml_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "gaml_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gaml_Expression46"):
                opp_val = getattr(value, "gaml_Expression46", None)
                setattr(value, "gaml_Expression46", self)

class gaml_S_Experiment(Statement, VarDefinition):

    pass
class gaml_VarFakeDefinition(VarDefinition):

    pass
class gaml_Expression:

    pass
class gaml_Block:

    pass
class Entry:

    pass
class gaml_ExperimentFileStructure(Entry):

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
class gaml_StandaloneBlock(Entry):

    pass
class gaml_Entry:

    pass
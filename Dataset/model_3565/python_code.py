from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_ImportSpec:

    def __init__(self, sTRING_LIT: str, myDsl_ImportSpec: "myDsl_ImportDecl" = None, myDsl_ImportSpec579: "myDsl_ImportDecl" = None, myDsl_ImportSpec581: "myDsl_PackageName" = None):
        self.sTRING_LIT = sTRING_LIT
        self.myDsl_ImportSpec = myDsl_ImportSpec
        self.myDsl_ImportSpec579 = myDsl_ImportSpec579
        self.myDsl_ImportSpec581 = myDsl_ImportSpec581
        
    @property
    def sTRING_LIT(self) -> str:
        return self.__sTRING_LIT

    @sTRING_LIT.setter
    def sTRING_LIT(self, sTRING_LIT: str):
        self.__sTRING_LIT = sTRING_LIT

    @property
    def myDsl_ImportSpec(self):
        return self.__myDsl_ImportSpec

    @myDsl_ImportSpec.setter
    def myDsl_ImportSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportSpec__myDsl_ImportSpec", None)
        self.__myDsl_ImportSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ImportDecl576"):
                opp_val = getattr(old_value, "myDsl_ImportDecl576", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ImportDecl576", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ImportDecl576"):
                opp_val = getattr(value, "myDsl_ImportDecl576", None)
                setattr(value, "myDsl_ImportDecl576", self)

    @property
    def myDsl_ImportSpec579(self):
        return self.__myDsl_ImportSpec579

    @myDsl_ImportSpec579.setter
    def myDsl_ImportSpec579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportSpec__myDsl_ImportSpec579", None)
        self.__myDsl_ImportSpec579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ImportDecl578"):
                opp_val = getattr(old_value, "myDsl_ImportDecl578", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ImportDecl578"):
                opp_val = getattr(value, "myDsl_ImportDecl578", None)
                if opp_val is None:
                    setattr(value, "myDsl_ImportDecl578", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_ImportSpec581(self):
        return self.__myDsl_ImportSpec581

    @myDsl_ImportSpec581.setter
    def myDsl_ImportSpec581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportSpec__myDsl_ImportSpec581", None)
        self.__myDsl_ImportSpec581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PackageName582"):
                opp_val = getattr(old_value, "myDsl_PackageName582", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PackageName582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PackageName582"):
                opp_val = getattr(value, "myDsl_PackageName582", None)
                setattr(value, "myDsl_PackageName582", self)

class myDsl_PackageName:

    def __init__(self, id: str, myDsl_PackageName: "myDsl_PackageClause" = None, myDsl_PackageName582: "myDsl_ImportSpec" = None):
        self.id = id
        self.myDsl_PackageName = myDsl_PackageName
        self.myDsl_PackageName582 = myDsl_PackageName582
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_PackageName582(self):
        return self.__myDsl_PackageName582

    @myDsl_PackageName582.setter
    def myDsl_PackageName582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PackageName__myDsl_PackageName582", None)
        self.__myDsl_PackageName582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ImportSpec581"):
                opp_val = getattr(old_value, "myDsl_ImportSpec581", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ImportSpec581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ImportSpec581"):
                opp_val = getattr(value, "myDsl_ImportSpec581", None)
                setattr(value, "myDsl_ImportSpec581", self)

    @property
    def myDsl_PackageName(self):
        return self.__myDsl_PackageName

    @myDsl_PackageName.setter
    def myDsl_PackageName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PackageName__myDsl_PackageName", None)
        self.__myDsl_PackageName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PackageClause574"):
                opp_val = getattr(old_value, "myDsl_PackageClause574", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PackageClause574", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PackageClause574"):
                opp_val = getattr(value, "myDsl_PackageClause574", None)
                setattr(value, "myDsl_PackageClause574", self)

class myDsl_ImportDecl:

    def __init__(self, importt: str, myDsl_ImportDecl: "myDsl_SourceFile" = None, myDsl_ImportDecl576: "myDsl_ImportSpec" = None, myDsl_ImportDecl578: set["myDsl_ImportSpec"] = None):
        self.importt = importt
        self.myDsl_ImportDecl = myDsl_ImportDecl
        self.myDsl_ImportDecl576 = myDsl_ImportDecl576
        self.myDsl_ImportDecl578 = myDsl_ImportDecl578 if myDsl_ImportDecl578 is not None else set()
        
    @property
    def importt(self) -> str:
        return self.__importt

    @importt.setter
    def importt(self, importt: str):
        self.__importt = importt

    @property
    def myDsl_ImportDecl576(self):
        return self.__myDsl_ImportDecl576

    @myDsl_ImportDecl576.setter
    def myDsl_ImportDecl576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportDecl__myDsl_ImportDecl576", None)
        self.__myDsl_ImportDecl576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ImportSpec"):
                opp_val = getattr(old_value, "myDsl_ImportSpec", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ImportSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ImportSpec"):
                opp_val = getattr(value, "myDsl_ImportSpec", None)
                setattr(value, "myDsl_ImportSpec", self)

    @property
    def myDsl_ImportDecl578(self):
        return self.__myDsl_ImportDecl578

    @myDsl_ImportDecl578.setter
    def myDsl_ImportDecl578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportDecl__myDsl_ImportDecl578", None)
        self.__myDsl_ImportDecl578 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ImportSpec579"):
                    opp_val = getattr(item, "myDsl_ImportSpec579", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ImportSpec579", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ImportSpec579"):
                    opp_val = getattr(item, "myDsl_ImportSpec579", None)
                    
                    setattr(item, "myDsl_ImportSpec579", self)
                    

    @property
    def myDsl_ImportDecl(self):
        return self.__myDsl_ImportDecl

    @myDsl_ImportDecl.setter
    def myDsl_ImportDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ImportDecl__myDsl_ImportDecl", None)
        self.__myDsl_ImportDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SourceFile569"):
                opp_val = getattr(old_value, "myDsl_SourceFile569", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SourceFile569"):
                opp_val = getattr(value, "myDsl_SourceFile569", None)
                if opp_val is None:
                    setattr(value, "myDsl_SourceFile569", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_PackageClause:

    def __init__(self, package: str, myDsl_PackageClause: "myDsl_SourceFile" = None, myDsl_PackageClause574: "myDsl_PackageName" = None):
        self.package = package
        self.myDsl_PackageClause = myDsl_PackageClause
        self.myDsl_PackageClause574 = myDsl_PackageClause574
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def myDsl_PackageClause574(self):
        return self.__myDsl_PackageClause574

    @myDsl_PackageClause574.setter
    def myDsl_PackageClause574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PackageClause__myDsl_PackageClause574", None)
        self.__myDsl_PackageClause574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PackageName"):
                opp_val = getattr(old_value, "myDsl_PackageName", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PackageName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PackageName"):
                opp_val = getattr(value, "myDsl_PackageName", None)
                setattr(value, "myDsl_PackageName", self)

    @property
    def myDsl_PackageClause(self):
        return self.__myDsl_PackageClause

    @myDsl_PackageClause.setter
    def myDsl_PackageClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PackageClause__myDsl_PackageClause", None)
        self.__myDsl_PackageClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SourceFile567"):
                opp_val = getattr(old_value, "myDsl_SourceFile567", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SourceFile567", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SourceFile567"):
                opp_val = getattr(value, "myDsl_SourceFile567", None)
                setattr(value, "myDsl_SourceFile567", self)

class myDsl_RecvExpr:

    pass
class myDsl_CommClause:

    pass
class myDsl_CommCaseLinha:

    pass
class myDsl_CommCase:

    def __init__(self, case: str, default: str, myDsl_CommCase: "myDsl_CommClause" = None, myDsl_CommCase533: "myDsl_Expression" = None, myDsl_CommCase536: "myDsl_CommCaseLinha" = None):
        self.case = case
        self.default = default
        self.myDsl_CommCase = myDsl_CommCase
        self.myDsl_CommCase533 = myDsl_CommCase533
        self.myDsl_CommCase536 = myDsl_CommCase536
        
    @property
    def case(self) -> str:
        return self.__case

    @case.setter
    def case(self, case: str):
        self.__case = case

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def myDsl_CommCase536(self):
        return self.__myDsl_CommCase536

    @myDsl_CommCase536.setter
    def myDsl_CommCase536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CommCase__myDsl_CommCase536", None)
        self.__myDsl_CommCase536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_CommCaseLinha"):
                opp_val = getattr(old_value, "myDsl_CommCaseLinha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_CommCaseLinha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_CommCaseLinha"):
                opp_val = getattr(value, "myDsl_CommCaseLinha", None)
                setattr(value, "myDsl_CommCaseLinha", self)

    @property
    def myDsl_CommCase(self):
        return self.__myDsl_CommCase

    @myDsl_CommCase.setter
    def myDsl_CommCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CommCase__myDsl_CommCase", None)
        self.__myDsl_CommCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_CommClause528"):
                opp_val = getattr(old_value, "myDsl_CommClause528", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_CommClause528", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_CommClause528"):
                opp_val = getattr(value, "myDsl_CommClause528", None)
                setattr(value, "myDsl_CommClause528", self)

    @property
    def myDsl_CommCase533(self):
        return self.__myDsl_CommCase533

    @myDsl_CommCase533.setter
    def myDsl_CommCase533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CommCase__myDsl_CommCase533", None)
        self.__myDsl_CommCase533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression534"):
                opp_val = getattr(old_value, "myDsl_Expression534", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression534"):
                opp_val = getattr(value, "myDsl_Expression534", None)
                setattr(value, "myDsl_Expression534", self)

class myDsl_ForStmtLinhaLinha:

    def __init__(self, range: str, myDsl_ForStmtLinhaLinha502: "myDsl_assign_op" = None, myDsl_ForStmtLinhaLinha505: "myDsl_ExpressionList" = None, myDsl_ForStmtLinhaLinha508: "myDsl_Condition" = None, myDsl_ForStmtLinhaLinha511: "myDsl_PostStmt" = None, myDsl_ForStmtLinhaLinha: "myDsl_ForStmtLinha" = None, myDsl_ForStmtLinhaLinha514: "myDsl_Expression" = None):
        self.range = range
        self.myDsl_ForStmtLinhaLinha502 = myDsl_ForStmtLinhaLinha502
        self.myDsl_ForStmtLinhaLinha505 = myDsl_ForStmtLinhaLinha505
        self.myDsl_ForStmtLinhaLinha508 = myDsl_ForStmtLinhaLinha508
        self.myDsl_ForStmtLinhaLinha511 = myDsl_ForStmtLinhaLinha511
        self.myDsl_ForStmtLinhaLinha = myDsl_ForStmtLinhaLinha
        self.myDsl_ForStmtLinhaLinha514 = myDsl_ForStmtLinhaLinha514
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def myDsl_ForStmtLinhaLinha511(self):
        return self.__myDsl_ForStmtLinhaLinha511

    @myDsl_ForStmtLinhaLinha511.setter
    def myDsl_ForStmtLinhaLinha511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha511", None)
        self.__myDsl_ForStmtLinhaLinha511 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PostStmt512"):
                opp_val = getattr(old_value, "myDsl_PostStmt512", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PostStmt512", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PostStmt512"):
                opp_val = getattr(value, "myDsl_PostStmt512", None)
                setattr(value, "myDsl_PostStmt512", self)

    @property
    def myDsl_ForStmtLinhaLinha508(self):
        return self.__myDsl_ForStmtLinhaLinha508

    @myDsl_ForStmtLinhaLinha508.setter
    def myDsl_ForStmtLinhaLinha508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha508", None)
        self.__myDsl_ForStmtLinhaLinha508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Condition509"):
                opp_val = getattr(old_value, "myDsl_Condition509", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Condition509", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Condition509"):
                opp_val = getattr(value, "myDsl_Condition509", None)
                setattr(value, "myDsl_Condition509", self)

    @property
    def myDsl_ForStmtLinhaLinha(self):
        return self.__myDsl_ForStmtLinhaLinha

    @myDsl_ForStmtLinhaLinha.setter
    def myDsl_ForStmtLinhaLinha(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha", None)
        self.__myDsl_ForStmtLinhaLinha = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmtLinha491"):
                opp_val = getattr(old_value, "myDsl_ForStmtLinha491", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmtLinha491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmtLinha491"):
                opp_val = getattr(value, "myDsl_ForStmtLinha491", None)
                setattr(value, "myDsl_ForStmtLinha491", self)

    @property
    def myDsl_ForStmtLinhaLinha514(self):
        return self.__myDsl_ForStmtLinhaLinha514

    @myDsl_ForStmtLinhaLinha514.setter
    def myDsl_ForStmtLinhaLinha514(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha514", None)
        self.__myDsl_ForStmtLinhaLinha514 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression515"):
                opp_val = getattr(old_value, "myDsl_Expression515", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression515", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression515"):
                opp_val = getattr(value, "myDsl_Expression515", None)
                setattr(value, "myDsl_Expression515", self)

    @property
    def myDsl_ForStmtLinhaLinha502(self):
        return self.__myDsl_ForStmtLinhaLinha502

    @myDsl_ForStmtLinhaLinha502.setter
    def myDsl_ForStmtLinhaLinha502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha502", None)
        self.__myDsl_ForStmtLinhaLinha502 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assign_op503"):
                opp_val = getattr(old_value, "myDsl_assign_op503", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assign_op503", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assign_op503"):
                opp_val = getattr(value, "myDsl_assign_op503", None)
                setattr(value, "myDsl_assign_op503", self)

    @property
    def myDsl_ForStmtLinhaLinha505(self):
        return self.__myDsl_ForStmtLinhaLinha505

    @myDsl_ForStmtLinhaLinha505.setter
    def myDsl_ForStmtLinhaLinha505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinhaLinha__myDsl_ForStmtLinhaLinha505", None)
        self.__myDsl_ForStmtLinhaLinha505 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExpressionList506"):
                opp_val = getattr(old_value, "myDsl_ExpressionList506", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExpressionList506", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExpressionList506"):
                opp_val = getattr(value, "myDsl_ExpressionList506", None)
                setattr(value, "myDsl_ExpressionList506", self)

class myDsl_TypeList:

    pass
class myDsl_PostStmt:

    pass
class myDsl_Condition:

    pass
class myDsl_ForStmtLinha:

    def __init__(self, vazio: str, myDsl_ForStmtLinha: "myDsl_ForStmt" = None, myDsl_ForStmtLinha499: "myDsl_PostStmt" = None, myDsl_ForStmtLinha488: set["myDsl_Expression"] = None, myDsl_ForStmtLinha491: "myDsl_ForStmtLinhaLinha" = None, myDsl_ForStmtLinha493: "myDsl_Expression" = None, myDsl_ForStmtLinha496: "myDsl_Condition" = None):
        self.vazio = vazio
        self.myDsl_ForStmtLinha = myDsl_ForStmtLinha
        self.myDsl_ForStmtLinha499 = myDsl_ForStmtLinha499
        self.myDsl_ForStmtLinha488 = myDsl_ForStmtLinha488 if myDsl_ForStmtLinha488 is not None else set()
        self.myDsl_ForStmtLinha491 = myDsl_ForStmtLinha491
        self.myDsl_ForStmtLinha493 = myDsl_ForStmtLinha493
        self.myDsl_ForStmtLinha496 = myDsl_ForStmtLinha496
        
    @property
    def vazio(self) -> str:
        return self.__vazio

    @vazio.setter
    def vazio(self, vazio: str):
        self.__vazio = vazio

    @property
    def myDsl_ForStmtLinha493(self):
        return self.__myDsl_ForStmtLinha493

    @myDsl_ForStmtLinha493.setter
    def myDsl_ForStmtLinha493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha493", None)
        self.__myDsl_ForStmtLinha493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression494"):
                opp_val = getattr(old_value, "myDsl_Expression494", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression494"):
                opp_val = getattr(value, "myDsl_Expression494", None)
                setattr(value, "myDsl_Expression494", self)

    @property
    def myDsl_ForStmtLinha(self):
        return self.__myDsl_ForStmtLinha

    @myDsl_ForStmtLinha.setter
    def myDsl_ForStmtLinha(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha", None)
        self.__myDsl_ForStmtLinha = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmt470"):
                opp_val = getattr(old_value, "myDsl_ForStmt470", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmt470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmt470"):
                opp_val = getattr(value, "myDsl_ForStmt470", None)
                setattr(value, "myDsl_ForStmt470", self)

    @property
    def myDsl_ForStmtLinha488(self):
        return self.__myDsl_ForStmtLinha488

    @myDsl_ForStmtLinha488.setter
    def myDsl_ForStmtLinha488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha488", None)
        self.__myDsl_ForStmtLinha488 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Expression489"):
                    opp_val = getattr(item, "myDsl_Expression489", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Expression489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Expression489"):
                    opp_val = getattr(item, "myDsl_Expression489", None)
                    
                    setattr(item, "myDsl_Expression489", self)
                    

    @property
    def myDsl_ForStmtLinha499(self):
        return self.__myDsl_ForStmtLinha499

    @myDsl_ForStmtLinha499.setter
    def myDsl_ForStmtLinha499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha499", None)
        self.__myDsl_ForStmtLinha499 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PostStmt500"):
                opp_val = getattr(old_value, "myDsl_PostStmt500", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PostStmt500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PostStmt500"):
                opp_val = getattr(value, "myDsl_PostStmt500", None)
                setattr(value, "myDsl_PostStmt500", self)

    @property
    def myDsl_ForStmtLinha496(self):
        return self.__myDsl_ForStmtLinha496

    @myDsl_ForStmtLinha496.setter
    def myDsl_ForStmtLinha496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha496", None)
        self.__myDsl_ForStmtLinha496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Condition497"):
                opp_val = getattr(old_value, "myDsl_Condition497", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Condition497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Condition497"):
                opp_val = getattr(value, "myDsl_Condition497", None)
                setattr(value, "myDsl_Condition497", self)

    @property
    def myDsl_ForStmtLinha491(self):
        return self.__myDsl_ForStmtLinha491

    @myDsl_ForStmtLinha491.setter
    def myDsl_ForStmtLinha491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmtLinha__myDsl_ForStmtLinha491", None)
        self.__myDsl_ForStmtLinha491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmtLinhaLinha"):
                opp_val = getattr(old_value, "myDsl_ForStmtLinhaLinha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmtLinhaLinha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmtLinhaLinha"):
                opp_val = getattr(value, "myDsl_ForStmtLinhaLinha", None)
                setattr(value, "myDsl_ForStmtLinhaLinha", self)

class myDsl_TypeCaseClause:

    pass
class myDsl_TypeSwitchGuard:

    def __init__(self, id: str, type: str, myDsl_TypeSwitchGuard451: "myDsl_PrimaryExpr" = None, myDsl_TypeSwitchGuard: "myDsl_TypeSwitchStmt" = None):
        self.id = id
        self.type = type
        self.myDsl_TypeSwitchGuard451 = myDsl_TypeSwitchGuard451
        self.myDsl_TypeSwitchGuard = myDsl_TypeSwitchGuard
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_TypeSwitchGuard(self):
        return self.__myDsl_TypeSwitchGuard

    @myDsl_TypeSwitchGuard.setter
    def myDsl_TypeSwitchGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchGuard__myDsl_TypeSwitchGuard", None)
        self.__myDsl_TypeSwitchGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeSwitchStmt447"):
                opp_val = getattr(old_value, "myDsl_TypeSwitchStmt447", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeSwitchStmt447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeSwitchStmt447"):
                opp_val = getattr(value, "myDsl_TypeSwitchStmt447", None)
                setattr(value, "myDsl_TypeSwitchStmt447", self)

    @property
    def myDsl_TypeSwitchGuard451(self):
        return self.__myDsl_TypeSwitchGuard451

    @myDsl_TypeSwitchGuard451.setter
    def myDsl_TypeSwitchGuard451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchGuard__myDsl_TypeSwitchGuard451", None)
        self.__myDsl_TypeSwitchGuard451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PrimaryExpr452"):
                opp_val = getattr(old_value, "myDsl_PrimaryExpr452", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PrimaryExpr452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PrimaryExpr452"):
                opp_val = getattr(value, "myDsl_PrimaryExpr452", None)
                setattr(value, "myDsl_PrimaryExpr452", self)

class myDsl_TypeSwitchCase:

    def __init__(self, case: str, default: str, myDsl_TypeSwitchCase: "myDsl_TypeCaseClause" = None, myDsl_TypeSwitchCase459: "myDsl_TypeList" = None):
        self.case = case
        self.default = default
        self.myDsl_TypeSwitchCase = myDsl_TypeSwitchCase
        self.myDsl_TypeSwitchCase459 = myDsl_TypeSwitchCase459
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def case(self) -> str:
        return self.__case

    @case.setter
    def case(self, case: str):
        self.__case = case

    @property
    def myDsl_TypeSwitchCase(self):
        return self.__myDsl_TypeSwitchCase

    @myDsl_TypeSwitchCase.setter
    def myDsl_TypeSwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchCase__myDsl_TypeSwitchCase", None)
        self.__myDsl_TypeSwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeCaseClause454"):
                opp_val = getattr(old_value, "myDsl_TypeCaseClause454", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeCaseClause454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeCaseClause454"):
                opp_val = getattr(value, "myDsl_TypeCaseClause454", None)
                setattr(value, "myDsl_TypeCaseClause454", self)

    @property
    def myDsl_TypeSwitchCase459(self):
        return self.__myDsl_TypeSwitchCase459

    @myDsl_TypeSwitchCase459.setter
    def myDsl_TypeSwitchCase459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchCase__myDsl_TypeSwitchCase459", None)
        self.__myDsl_TypeSwitchCase459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeList"):
                opp_val = getattr(old_value, "myDsl_TypeList", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeList"):
                opp_val = getattr(value, "myDsl_TypeList", None)
                setattr(value, "myDsl_TypeList", self)

class myDsl_TypeSwitchStmt:

    def __init__(self, switch: str, myDsl_TypeSwitchStmt: "myDsl_SwitchStmt" = None, myDsl_TypeSwitchStmt444: "myDsl_SimpleStmt" = None, myDsl_TypeSwitchStmt447: "myDsl_TypeSwitchGuard" = None, myDsl_TypeSwitchStmt449: set["myDsl_TypeCaseClause"] = None):
        self.switch = switch
        self.myDsl_TypeSwitchStmt = myDsl_TypeSwitchStmt
        self.myDsl_TypeSwitchStmt444 = myDsl_TypeSwitchStmt444
        self.myDsl_TypeSwitchStmt447 = myDsl_TypeSwitchStmt447
        self.myDsl_TypeSwitchStmt449 = myDsl_TypeSwitchStmt449 if myDsl_TypeSwitchStmt449 is not None else set()
        
    @property
    def switch(self) -> str:
        return self.__switch

    @switch.setter
    def switch(self, switch: str):
        self.__switch = switch

    @property
    def myDsl_TypeSwitchStmt(self):
        return self.__myDsl_TypeSwitchStmt

    @myDsl_TypeSwitchStmt.setter
    def myDsl_TypeSwitchStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchStmt__myDsl_TypeSwitchStmt", None)
        self.__myDsl_TypeSwitchStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SwitchStmt426"):
                opp_val = getattr(old_value, "myDsl_SwitchStmt426", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SwitchStmt426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SwitchStmt426"):
                opp_val = getattr(value, "myDsl_SwitchStmt426", None)
                setattr(value, "myDsl_SwitchStmt426", self)

    @property
    def myDsl_TypeSwitchStmt447(self):
        return self.__myDsl_TypeSwitchStmt447

    @myDsl_TypeSwitchStmt447.setter
    def myDsl_TypeSwitchStmt447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchStmt__myDsl_TypeSwitchStmt447", None)
        self.__myDsl_TypeSwitchStmt447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeSwitchGuard"):
                opp_val = getattr(old_value, "myDsl_TypeSwitchGuard", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeSwitchGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeSwitchGuard"):
                opp_val = getattr(value, "myDsl_TypeSwitchGuard", None)
                setattr(value, "myDsl_TypeSwitchGuard", self)

    @property
    def myDsl_TypeSwitchStmt444(self):
        return self.__myDsl_TypeSwitchStmt444

    @myDsl_TypeSwitchStmt444.setter
    def myDsl_TypeSwitchStmt444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchStmt__myDsl_TypeSwitchStmt444", None)
        self.__myDsl_TypeSwitchStmt444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmt445"):
                opp_val = getattr(old_value, "myDsl_SimpleStmt445", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmt445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmt445"):
                opp_val = getattr(value, "myDsl_SimpleStmt445", None)
                setattr(value, "myDsl_SimpleStmt445", self)

    @property
    def myDsl_TypeSwitchStmt449(self):
        return self.__myDsl_TypeSwitchStmt449

    @myDsl_TypeSwitchStmt449.setter
    def myDsl_TypeSwitchStmt449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeSwitchStmt__myDsl_TypeSwitchStmt449", None)
        self.__myDsl_TypeSwitchStmt449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_TypeCaseClause"):
                    opp_val = getattr(item, "myDsl_TypeCaseClause", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_TypeCaseClause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_TypeCaseClause"):
                    opp_val = getattr(item, "myDsl_TypeCaseClause", None)
                    
                    setattr(item, "myDsl_TypeCaseClause", self)
                    

class myDsl_ExprSwitchStmt:

    def __init__(self, switch: str, myDsl_ExprSwitchStmt428: "myDsl_SimpleStmt" = None, myDsl_ExprSwitchStmt431: "myDsl_Expression" = None, myDsl_ExprSwitchStmt434: set["myDsl_ExprCaseClause"] = None, myDsl_ExprSwitchStmt: "myDsl_SwitchStmt" = None):
        self.switch = switch
        self.myDsl_ExprSwitchStmt428 = myDsl_ExprSwitchStmt428
        self.myDsl_ExprSwitchStmt431 = myDsl_ExprSwitchStmt431
        self.myDsl_ExprSwitchStmt434 = myDsl_ExprSwitchStmt434 if myDsl_ExprSwitchStmt434 is not None else set()
        self.myDsl_ExprSwitchStmt = myDsl_ExprSwitchStmt
        
    @property
    def switch(self) -> str:
        return self.__switch

    @switch.setter
    def switch(self, switch: str):
        self.__switch = switch

    @property
    def myDsl_ExprSwitchStmt431(self):
        return self.__myDsl_ExprSwitchStmt431

    @myDsl_ExprSwitchStmt431.setter
    def myDsl_ExprSwitchStmt431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchStmt__myDsl_ExprSwitchStmt431", None)
        self.__myDsl_ExprSwitchStmt431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression432"):
                opp_val = getattr(old_value, "myDsl_Expression432", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression432"):
                opp_val = getattr(value, "myDsl_Expression432", None)
                setattr(value, "myDsl_Expression432", self)

    @property
    def myDsl_ExprSwitchStmt428(self):
        return self.__myDsl_ExprSwitchStmt428

    @myDsl_ExprSwitchStmt428.setter
    def myDsl_ExprSwitchStmt428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchStmt__myDsl_ExprSwitchStmt428", None)
        self.__myDsl_ExprSwitchStmt428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmt429"):
                opp_val = getattr(old_value, "myDsl_SimpleStmt429", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmt429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmt429"):
                opp_val = getattr(value, "myDsl_SimpleStmt429", None)
                setattr(value, "myDsl_SimpleStmt429", self)

    @property
    def myDsl_ExprSwitchStmt434(self):
        return self.__myDsl_ExprSwitchStmt434

    @myDsl_ExprSwitchStmt434.setter
    def myDsl_ExprSwitchStmt434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchStmt__myDsl_ExprSwitchStmt434", None)
        self.__myDsl_ExprSwitchStmt434 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ExprCaseClause"):
                    opp_val = getattr(item, "myDsl_ExprCaseClause", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ExprCaseClause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ExprCaseClause"):
                    opp_val = getattr(item, "myDsl_ExprCaseClause", None)
                    
                    setattr(item, "myDsl_ExprCaseClause", self)
                    

    @property
    def myDsl_ExprSwitchStmt(self):
        return self.__myDsl_ExprSwitchStmt

    @myDsl_ExprSwitchStmt.setter
    def myDsl_ExprSwitchStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchStmt__myDsl_ExprSwitchStmt", None)
        self.__myDsl_ExprSwitchStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SwitchStmt424"):
                opp_val = getattr(old_value, "myDsl_SwitchStmt424", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SwitchStmt424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SwitchStmt424"):
                opp_val = getattr(value, "myDsl_SwitchStmt424", None)
                setattr(value, "myDsl_SwitchStmt424", self)

class myDsl_ExprSwitchCase:

    def __init__(self, case: str, default: str, myDsl_ExprSwitchCase: "myDsl_ExprCaseClause" = None, myDsl_ExprSwitchCase441: "myDsl_ExpressionList" = None):
        self.case = case
        self.default = default
        self.myDsl_ExprSwitchCase = myDsl_ExprSwitchCase
        self.myDsl_ExprSwitchCase441 = myDsl_ExprSwitchCase441
        
    @property
    def case(self) -> str:
        return self.__case

    @case.setter
    def case(self, case: str):
        self.__case = case

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def myDsl_ExprSwitchCase441(self):
        return self.__myDsl_ExprSwitchCase441

    @myDsl_ExprSwitchCase441.setter
    def myDsl_ExprSwitchCase441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchCase__myDsl_ExprSwitchCase441", None)
        self.__myDsl_ExprSwitchCase441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExpressionList442"):
                opp_val = getattr(old_value, "myDsl_ExpressionList442", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExpressionList442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExpressionList442"):
                opp_val = getattr(value, "myDsl_ExpressionList442", None)
                setattr(value, "myDsl_ExpressionList442", self)

    @property
    def myDsl_ExprSwitchCase(self):
        return self.__myDsl_ExprSwitchCase

    @myDsl_ExprSwitchCase.setter
    def myDsl_ExprSwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSwitchCase__myDsl_ExprSwitchCase", None)
        self.__myDsl_ExprSwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprCaseClause436"):
                opp_val = getattr(old_value, "myDsl_ExprCaseClause436", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprCaseClause436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprCaseClause436"):
                opp_val = getattr(value, "myDsl_ExprCaseClause436", None)
                setattr(value, "myDsl_ExprCaseClause436", self)

class myDsl_ExprCaseClause:

    pass
class myDsl_Label:

    def __init__(self, id: str, myDsl_Label: "myDsl_LabeledStmt" = None, myDsl_Label556: "myDsl_BreakStmt" = None, myDsl_Label559: "myDsl_ContinueStmt" = None, myDsl_Label562: "myDsl_GotoStmt" = None):
        self.id = id
        self.myDsl_Label = myDsl_Label
        self.myDsl_Label556 = myDsl_Label556
        self.myDsl_Label559 = myDsl_Label559
        self.myDsl_Label562 = myDsl_Label562
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_Label562(self):
        return self.__myDsl_Label562

    @myDsl_Label562.setter
    def myDsl_Label562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Label__myDsl_Label562", None)
        self.__myDsl_Label562 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GotoStmt561"):
                opp_val = getattr(old_value, "myDsl_GotoStmt561", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GotoStmt561", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GotoStmt561"):
                opp_val = getattr(value, "myDsl_GotoStmt561", None)
                setattr(value, "myDsl_GotoStmt561", self)

    @property
    def myDsl_Label556(self):
        return self.__myDsl_Label556

    @myDsl_Label556.setter
    def myDsl_Label556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Label__myDsl_Label556", None)
        self.__myDsl_Label556 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_BreakStmt555"):
                opp_val = getattr(old_value, "myDsl_BreakStmt555", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_BreakStmt555", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_BreakStmt555"):
                opp_val = getattr(value, "myDsl_BreakStmt555", None)
                setattr(value, "myDsl_BreakStmt555", self)

    @property
    def myDsl_Label(self):
        return self.__myDsl_Label

    @myDsl_Label.setter
    def myDsl_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Label__myDsl_Label", None)
        self.__myDsl_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LabeledStmt384"):
                opp_val = getattr(old_value, "myDsl_LabeledStmt384", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_LabeledStmt384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LabeledStmt384"):
                opp_val = getattr(value, "myDsl_LabeledStmt384", None)
                setattr(value, "myDsl_LabeledStmt384", self)

    @property
    def myDsl_Label559(self):
        return self.__myDsl_Label559

    @myDsl_Label559.setter
    def myDsl_Label559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Label__myDsl_Label559", None)
        self.__myDsl_Label559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ContinueStmt558"):
                opp_val = getattr(old_value, "myDsl_ContinueStmt558", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ContinueStmt558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ContinueStmt558"):
                opp_val = getattr(value, "myDsl_ContinueStmt558", None)
                setattr(value, "myDsl_ContinueStmt558", self)

class myDsl_assign_op:

    def __init__(self, aDD_OP: str, mUL_OP: str, myDsl_assign_op: "myDsl_SimpleStmtLinha" = None, myDsl_assign_op503: "myDsl_ForStmtLinhaLinha" = None):
        self.aDD_OP = aDD_OP
        self.mUL_OP = mUL_OP
        self.myDsl_assign_op = myDsl_assign_op
        self.myDsl_assign_op503 = myDsl_assign_op503
        
    @property
    def aDD_OP(self) -> str:
        return self.__aDD_OP

    @aDD_OP.setter
    def aDD_OP(self, aDD_OP: str):
        self.__aDD_OP = aDD_OP

    @property
    def mUL_OP(self) -> str:
        return self.__mUL_OP

    @mUL_OP.setter
    def mUL_OP(self, mUL_OP: str):
        self.__mUL_OP = mUL_OP

    @property
    def myDsl_assign_op503(self):
        return self.__myDsl_assign_op503

    @myDsl_assign_op503.setter
    def myDsl_assign_op503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assign_op__myDsl_assign_op503", None)
        self.__myDsl_assign_op503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmtLinhaLinha502"):
                opp_val = getattr(old_value, "myDsl_ForStmtLinhaLinha502", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmtLinhaLinha502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmtLinhaLinha502"):
                opp_val = getattr(value, "myDsl_ForStmtLinhaLinha502", None)
                setattr(value, "myDsl_ForStmtLinhaLinha502", self)

    @property
    def myDsl_assign_op(self):
        return self.__myDsl_assign_op

    @myDsl_assign_op.setter
    def myDsl_assign_op(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_assign_op__myDsl_assign_op", None)
        self.__myDsl_assign_op = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmtLinha379"):
                opp_val = getattr(old_value, "myDsl_SimpleStmtLinha379", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmtLinha379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmtLinha379"):
                opp_val = getattr(value, "myDsl_SimpleStmtLinha379", None)
                setattr(value, "myDsl_SimpleStmtLinha379", self)

class myDsl_IfStmtLinha:

    def __init__(self, else: str, myDsl_IfStmtLinha: "myDsl_IfStmt" = None, myDsl_IfStmtLinha409: "myDsl_SimpleStmtLinha" = None, myDsl_IfStmtLinha412: "myDsl_Expression" = None, myDsl_IfStmtLinha415: "myDsl_Block" = None, myDsl_IfStmtLinha418: "myDsl_IfStmt" = None, myDsl_IfStmtLinha421: "myDsl_Block" = None):
        self.else = else
        self.myDsl_IfStmtLinha = myDsl_IfStmtLinha
        self.myDsl_IfStmtLinha409 = myDsl_IfStmtLinha409
        self.myDsl_IfStmtLinha412 = myDsl_IfStmtLinha412
        self.myDsl_IfStmtLinha415 = myDsl_IfStmtLinha415
        self.myDsl_IfStmtLinha418 = myDsl_IfStmtLinha418
        self.myDsl_IfStmtLinha421 = myDsl_IfStmtLinha421
        
    @property
    def else(self) -> str:
        return self.__else

    @else.setter
    def else(self, else: str):
        self.__else = else

    @property
    def myDsl_IfStmtLinha(self):
        return self.__myDsl_IfStmtLinha

    @myDsl_IfStmtLinha.setter
    def myDsl_IfStmtLinha(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha", None)
        self.__myDsl_IfStmtLinha = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmt392"):
                opp_val = getattr(old_value, "myDsl_IfStmt392", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmt392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmt392"):
                opp_val = getattr(value, "myDsl_IfStmt392", None)
                setattr(value, "myDsl_IfStmt392", self)

    @property
    def myDsl_IfStmtLinha421(self):
        return self.__myDsl_IfStmtLinha421

    @myDsl_IfStmtLinha421.setter
    def myDsl_IfStmtLinha421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha421", None)
        self.__myDsl_IfStmtLinha421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block422"):
                opp_val = getattr(old_value, "myDsl_Block422", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block422"):
                opp_val = getattr(value, "myDsl_Block422", None)
                setattr(value, "myDsl_Block422", self)

    @property
    def myDsl_IfStmtLinha418(self):
        return self.__myDsl_IfStmtLinha418

    @myDsl_IfStmtLinha418.setter
    def myDsl_IfStmtLinha418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha418", None)
        self.__myDsl_IfStmtLinha418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmt419"):
                opp_val = getattr(old_value, "myDsl_IfStmt419", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmt419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmt419"):
                opp_val = getattr(value, "myDsl_IfStmt419", None)
                setattr(value, "myDsl_IfStmt419", self)

    @property
    def myDsl_IfStmtLinha412(self):
        return self.__myDsl_IfStmtLinha412

    @myDsl_IfStmtLinha412.setter
    def myDsl_IfStmtLinha412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha412", None)
        self.__myDsl_IfStmtLinha412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression413"):
                opp_val = getattr(old_value, "myDsl_Expression413", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression413"):
                opp_val = getattr(value, "myDsl_Expression413", None)
                setattr(value, "myDsl_Expression413", self)

    @property
    def myDsl_IfStmtLinha415(self):
        return self.__myDsl_IfStmtLinha415

    @myDsl_IfStmtLinha415.setter
    def myDsl_IfStmtLinha415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha415", None)
        self.__myDsl_IfStmtLinha415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block416"):
                opp_val = getattr(old_value, "myDsl_Block416", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block416"):
                opp_val = getattr(value, "myDsl_Block416", None)
                setattr(value, "myDsl_Block416", self)

    @property
    def myDsl_IfStmtLinha409(self):
        return self.__myDsl_IfStmtLinha409

    @myDsl_IfStmtLinha409.setter
    def myDsl_IfStmtLinha409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmtLinha__myDsl_IfStmtLinha409", None)
        self.__myDsl_IfStmtLinha409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmtLinha410"):
                opp_val = getattr(old_value, "myDsl_SimpleStmtLinha410", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmtLinha410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmtLinha410"):
                opp_val = getattr(value, "myDsl_SimpleStmtLinha410", None)
                setattr(value, "myDsl_SimpleStmtLinha410", self)

class myDsl_EmptyStmt:

    def __init__(self, aNY_OTHER: str, myDsl_EmptyStmt: "myDsl_SimpleStmt" = None, myDsl_EmptyStmt395: "myDsl_IfStmt" = None, myDsl_EmptyStmt473: "myDsl_ForStmt" = None):
        self.aNY_OTHER = aNY_OTHER
        self.myDsl_EmptyStmt = myDsl_EmptyStmt
        self.myDsl_EmptyStmt395 = myDsl_EmptyStmt395
        self.myDsl_EmptyStmt473 = myDsl_EmptyStmt473
        
    @property
    def aNY_OTHER(self) -> str:
        return self.__aNY_OTHER

    @aNY_OTHER.setter
    def aNY_OTHER(self, aNY_OTHER: str):
        self.__aNY_OTHER = aNY_OTHER

    @property
    def myDsl_EmptyStmt473(self):
        return self.__myDsl_EmptyStmt473

    @myDsl_EmptyStmt473.setter
    def myDsl_EmptyStmt473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EmptyStmt__myDsl_EmptyStmt473", None)
        self.__myDsl_EmptyStmt473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmt472"):
                opp_val = getattr(old_value, "myDsl_ForStmt472", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmt472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmt472"):
                opp_val = getattr(value, "myDsl_ForStmt472", None)
                setattr(value, "myDsl_ForStmt472", self)

    @property
    def myDsl_EmptyStmt(self):
        return self.__myDsl_EmptyStmt

    @myDsl_EmptyStmt.setter
    def myDsl_EmptyStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EmptyStmt__myDsl_EmptyStmt", None)
        self.__myDsl_EmptyStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmt363"):
                opp_val = getattr(old_value, "myDsl_SimpleStmt363", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmt363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmt363"):
                opp_val = getattr(value, "myDsl_SimpleStmt363", None)
                setattr(value, "myDsl_SimpleStmt363", self)

    @property
    def myDsl_EmptyStmt395(self):
        return self.__myDsl_EmptyStmt395

    @myDsl_EmptyStmt395.setter
    def myDsl_EmptyStmt395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EmptyStmt__myDsl_EmptyStmt395", None)
        self.__myDsl_EmptyStmt395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmt394"):
                opp_val = getattr(old_value, "myDsl_IfStmt394", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmt394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmt394"):
                opp_val = getattr(value, "myDsl_IfStmt394", None)
                setattr(value, "myDsl_IfStmt394", self)

class myDsl_DeferStmt:

    def __init__(self, defer: str, myDsl_DeferStmt: "myDsl_Statement" = None, myDsl_DeferStmt564: "myDsl_Expression" = None):
        self.defer = defer
        self.myDsl_DeferStmt = myDsl_DeferStmt
        self.myDsl_DeferStmt564 = myDsl_DeferStmt564
        
    @property
    def defer(self) -> str:
        return self.__defer

    @defer.setter
    def defer(self, defer: str):
        self.__defer = defer

    @property
    def myDsl_DeferStmt(self):
        return self.__myDsl_DeferStmt

    @myDsl_DeferStmt.setter
    def myDsl_DeferStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DeferStmt__myDsl_DeferStmt", None)
        self.__myDsl_DeferStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement361"):
                opp_val = getattr(old_value, "myDsl_Statement361", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement361"):
                opp_val = getattr(value, "myDsl_Statement361", None)
                setattr(value, "myDsl_Statement361", self)

    @property
    def myDsl_DeferStmt564(self):
        return self.__myDsl_DeferStmt564

    @myDsl_DeferStmt564.setter
    def myDsl_DeferStmt564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DeferStmt__myDsl_DeferStmt564", None)
        self.__myDsl_DeferStmt564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression565"):
                opp_val = getattr(old_value, "myDsl_Expression565", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression565"):
                opp_val = getattr(value, "myDsl_Expression565", None)
                setattr(value, "myDsl_Expression565", self)

class myDsl_ForStmt:

    def __init__(self, for: str, range: str, myDsl_ForStmt: "myDsl_Statement" = None, myDsl_ForStmt470: "myDsl_ForStmtLinha" = None, myDsl_ForStmt472: "myDsl_EmptyStmt" = None, myDsl_ForStmt475: "myDsl_ShortVarDecl" = None, myDsl_ForStmt478: "myDsl_Condition" = None, myDsl_ForStmt480: "myDsl_PostStmt" = None, myDsl_ForStmt482: "myDsl_IdentifierList" = None, myDsl_ForStmt467: "myDsl_Expression" = None, myDsl_ForStmt485: "myDsl_Block" = None):
        self.for = for
        self.range = range
        self.myDsl_ForStmt = myDsl_ForStmt
        self.myDsl_ForStmt470 = myDsl_ForStmt470
        self.myDsl_ForStmt472 = myDsl_ForStmt472
        self.myDsl_ForStmt475 = myDsl_ForStmt475
        self.myDsl_ForStmt478 = myDsl_ForStmt478
        self.myDsl_ForStmt480 = myDsl_ForStmt480
        self.myDsl_ForStmt482 = myDsl_ForStmt482
        self.myDsl_ForStmt467 = myDsl_ForStmt467
        self.myDsl_ForStmt485 = myDsl_ForStmt485
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def for(self) -> str:
        return self.__for

    @for.setter
    def for(self, for: str):
        self.__for = for

    @property
    def myDsl_ForStmt472(self):
        return self.__myDsl_ForStmt472

    @myDsl_ForStmt472.setter
    def myDsl_ForStmt472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt472", None)
        self.__myDsl_ForStmt472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_EmptyStmt473"):
                opp_val = getattr(old_value, "myDsl_EmptyStmt473", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_EmptyStmt473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_EmptyStmt473"):
                opp_val = getattr(value, "myDsl_EmptyStmt473", None)
                setattr(value, "myDsl_EmptyStmt473", self)

    @property
    def myDsl_ForStmt485(self):
        return self.__myDsl_ForStmt485

    @myDsl_ForStmt485.setter
    def myDsl_ForStmt485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt485", None)
        self.__myDsl_ForStmt485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block486"):
                opp_val = getattr(old_value, "myDsl_Block486", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block486", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block486"):
                opp_val = getattr(value, "myDsl_Block486", None)
                setattr(value, "myDsl_Block486", self)

    @property
    def myDsl_ForStmt(self):
        return self.__myDsl_ForStmt

    @myDsl_ForStmt.setter
    def myDsl_ForStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt", None)
        self.__myDsl_ForStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement359"):
                opp_val = getattr(old_value, "myDsl_Statement359", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement359"):
                opp_val = getattr(value, "myDsl_Statement359", None)
                setattr(value, "myDsl_Statement359", self)

    @property
    def myDsl_ForStmt470(self):
        return self.__myDsl_ForStmt470

    @myDsl_ForStmt470.setter
    def myDsl_ForStmt470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt470", None)
        self.__myDsl_ForStmt470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmtLinha"):
                opp_val = getattr(old_value, "myDsl_ForStmtLinha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmtLinha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmtLinha"):
                opp_val = getattr(value, "myDsl_ForStmtLinha", None)
                setattr(value, "myDsl_ForStmtLinha", self)

    @property
    def myDsl_ForStmt482(self):
        return self.__myDsl_ForStmt482

    @myDsl_ForStmt482.setter
    def myDsl_ForStmt482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt482", None)
        self.__myDsl_ForStmt482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IdentifierList483"):
                opp_val = getattr(old_value, "myDsl_IdentifierList483", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IdentifierList483", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IdentifierList483"):
                opp_val = getattr(value, "myDsl_IdentifierList483", None)
                setattr(value, "myDsl_IdentifierList483", self)

    @property
    def myDsl_ForStmt478(self):
        return self.__myDsl_ForStmt478

    @myDsl_ForStmt478.setter
    def myDsl_ForStmt478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt478", None)
        self.__myDsl_ForStmt478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Condition"):
                opp_val = getattr(old_value, "myDsl_Condition", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Condition"):
                opp_val = getattr(value, "myDsl_Condition", None)
                setattr(value, "myDsl_Condition", self)

    @property
    def myDsl_ForStmt480(self):
        return self.__myDsl_ForStmt480

    @myDsl_ForStmt480.setter
    def myDsl_ForStmt480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt480", None)
        self.__myDsl_ForStmt480 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PostStmt"):
                opp_val = getattr(old_value, "myDsl_PostStmt", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PostStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PostStmt"):
                opp_val = getattr(value, "myDsl_PostStmt", None)
                setattr(value, "myDsl_PostStmt", self)

    @property
    def myDsl_ForStmt467(self):
        return self.__myDsl_ForStmt467

    @myDsl_ForStmt467.setter
    def myDsl_ForStmt467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt467", None)
        self.__myDsl_ForStmt467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression468"):
                opp_val = getattr(old_value, "myDsl_Expression468", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression468"):
                opp_val = getattr(value, "myDsl_Expression468", None)
                setattr(value, "myDsl_Expression468", self)

    @property
    def myDsl_ForStmt475(self):
        return self.__myDsl_ForStmt475

    @myDsl_ForStmt475.setter
    def myDsl_ForStmt475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ForStmt__myDsl_ForStmt475", None)
        self.__myDsl_ForStmt475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ShortVarDecl476"):
                opp_val = getattr(old_value, "myDsl_ShortVarDecl476", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ShortVarDecl476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ShortVarDecl476"):
                opp_val = getattr(value, "myDsl_ShortVarDecl476", None)
                setattr(value, "myDsl_ShortVarDecl476", self)

class myDsl_SelectStmt:

    def __init__(self, select: str, myDsl_SelectStmt: "myDsl_Statement" = None, myDsl_SelectStmt526: set["myDsl_CommClause"] = None):
        self.select = select
        self.myDsl_SelectStmt = myDsl_SelectStmt
        self.myDsl_SelectStmt526 = myDsl_SelectStmt526 if myDsl_SelectStmt526 is not None else set()
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

    @property
    def myDsl_SelectStmt526(self):
        return self.__myDsl_SelectStmt526

    @myDsl_SelectStmt526.setter
    def myDsl_SelectStmt526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SelectStmt__myDsl_SelectStmt526", None)
        self.__myDsl_SelectStmt526 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_CommClause"):
                    opp_val = getattr(item, "myDsl_CommClause", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_CommClause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_CommClause"):
                    opp_val = getattr(item, "myDsl_CommClause", None)
                    
                    setattr(item, "myDsl_CommClause", self)
                    

    @property
    def myDsl_SelectStmt(self):
        return self.__myDsl_SelectStmt

    @myDsl_SelectStmt.setter
    def myDsl_SelectStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SelectStmt__myDsl_SelectStmt", None)
        self.__myDsl_SelectStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement357"):
                opp_val = getattr(old_value, "myDsl_Statement357", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement357"):
                opp_val = getattr(value, "myDsl_Statement357", None)
                setattr(value, "myDsl_Statement357", self)

class myDsl_SimpleStmtLinha:

    def __init__(self, aNY_OTHER: str, myDsl_SimpleStmtLinha: "myDsl_SimpleStmt" = None, myDsl_SimpleStmtLinha373: "myDsl_Expression" = None, myDsl_SimpleStmtLinha376: set["myDsl_Expression"] = None, myDsl_SimpleStmtLinha379: "myDsl_assign_op" = None, myDsl_SimpleStmtLinha381: "myDsl_ExpressionList" = None, myDsl_SimpleStmtLinha410: "myDsl_IfStmtLinha" = None):
        self.aNY_OTHER = aNY_OTHER
        self.myDsl_SimpleStmtLinha = myDsl_SimpleStmtLinha
        self.myDsl_SimpleStmtLinha373 = myDsl_SimpleStmtLinha373
        self.myDsl_SimpleStmtLinha376 = myDsl_SimpleStmtLinha376 if myDsl_SimpleStmtLinha376 is not None else set()
        self.myDsl_SimpleStmtLinha379 = myDsl_SimpleStmtLinha379
        self.myDsl_SimpleStmtLinha381 = myDsl_SimpleStmtLinha381
        self.myDsl_SimpleStmtLinha410 = myDsl_SimpleStmtLinha410
        
    @property
    def aNY_OTHER(self) -> str:
        return self.__aNY_OTHER

    @aNY_OTHER.setter
    def aNY_OTHER(self, aNY_OTHER: str):
        self.__aNY_OTHER = aNY_OTHER

    @property
    def myDsl_SimpleStmtLinha376(self):
        return self.__myDsl_SimpleStmtLinha376

    @myDsl_SimpleStmtLinha376.setter
    def myDsl_SimpleStmtLinha376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha376", None)
        self.__myDsl_SimpleStmtLinha376 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Expression377"):
                    opp_val = getattr(item, "myDsl_Expression377", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Expression377", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Expression377"):
                    opp_val = getattr(item, "myDsl_Expression377", None)
                    
                    setattr(item, "myDsl_Expression377", self)
                    

    @property
    def myDsl_SimpleStmtLinha381(self):
        return self.__myDsl_SimpleStmtLinha381

    @myDsl_SimpleStmtLinha381.setter
    def myDsl_SimpleStmtLinha381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha381", None)
        self.__myDsl_SimpleStmtLinha381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExpressionList382"):
                opp_val = getattr(old_value, "myDsl_ExpressionList382", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExpressionList382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExpressionList382"):
                opp_val = getattr(value, "myDsl_ExpressionList382", None)
                setattr(value, "myDsl_ExpressionList382", self)

    @property
    def myDsl_SimpleStmtLinha410(self):
        return self.__myDsl_SimpleStmtLinha410

    @myDsl_SimpleStmtLinha410.setter
    def myDsl_SimpleStmtLinha410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha410", None)
        self.__myDsl_SimpleStmtLinha410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmtLinha409"):
                opp_val = getattr(old_value, "myDsl_IfStmtLinha409", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmtLinha409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmtLinha409"):
                opp_val = getattr(value, "myDsl_IfStmtLinha409", None)
                setattr(value, "myDsl_IfStmtLinha409", self)

    @property
    def myDsl_SimpleStmtLinha379(self):
        return self.__myDsl_SimpleStmtLinha379

    @myDsl_SimpleStmtLinha379.setter
    def myDsl_SimpleStmtLinha379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha379", None)
        self.__myDsl_SimpleStmtLinha379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_assign_op"):
                opp_val = getattr(old_value, "myDsl_assign_op", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_assign_op", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_assign_op"):
                opp_val = getattr(value, "myDsl_assign_op", None)
                setattr(value, "myDsl_assign_op", self)

    @property
    def myDsl_SimpleStmtLinha(self):
        return self.__myDsl_SimpleStmtLinha

    @myDsl_SimpleStmtLinha.setter
    def myDsl_SimpleStmtLinha(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha", None)
        self.__myDsl_SimpleStmtLinha = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SimpleStmt368"):
                opp_val = getattr(old_value, "myDsl_SimpleStmt368", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SimpleStmt368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SimpleStmt368"):
                opp_val = getattr(value, "myDsl_SimpleStmt368", None)
                setattr(value, "myDsl_SimpleStmt368", self)

    @property
    def myDsl_SimpleStmtLinha373(self):
        return self.__myDsl_SimpleStmtLinha373

    @myDsl_SimpleStmtLinha373.setter
    def myDsl_SimpleStmtLinha373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SimpleStmtLinha__myDsl_SimpleStmtLinha373", None)
        self.__myDsl_SimpleStmtLinha373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression374"):
                opp_val = getattr(old_value, "myDsl_Expression374", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression374"):
                opp_val = getattr(value, "myDsl_Expression374", None)
                setattr(value, "myDsl_Expression374", self)

class myDsl_ContinueStmt:

    def __init__(self, continue: str, myDsl_ContinueStmt: "myDsl_Statement" = None, myDsl_ContinueStmt558: "myDsl_Label" = None):
        self.continue = continue
        self.myDsl_ContinueStmt = myDsl_ContinueStmt
        self.myDsl_ContinueStmt558 = myDsl_ContinueStmt558
        
    @property
    def continue(self) -> str:
        return self.__continue

    @continue.setter
    def continue(self, continue: str):
        self.__continue = continue

    @property
    def myDsl_ContinueStmt(self):
        return self.__myDsl_ContinueStmt

    @myDsl_ContinueStmt.setter
    def myDsl_ContinueStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ContinueStmt__myDsl_ContinueStmt", None)
        self.__myDsl_ContinueStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement344"):
                opp_val = getattr(old_value, "myDsl_Statement344", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement344"):
                opp_val = getattr(value, "myDsl_Statement344", None)
                setattr(value, "myDsl_Statement344", self)

    @property
    def myDsl_ContinueStmt558(self):
        return self.__myDsl_ContinueStmt558

    @myDsl_ContinueStmt558.setter
    def myDsl_ContinueStmt558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ContinueStmt__myDsl_ContinueStmt558", None)
        self.__myDsl_ContinueStmt558 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Label559"):
                opp_val = getattr(old_value, "myDsl_Label559", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Label559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Label559"):
                opp_val = getattr(value, "myDsl_Label559", None)
                setattr(value, "myDsl_Label559", self)

class myDsl_BreakStmt:

    def __init__(self, break: str, myDsl_BreakStmt: "myDsl_Statement" = None, myDsl_BreakStmt555: "myDsl_Label" = None):
        self.break = break
        self.myDsl_BreakStmt = myDsl_BreakStmt
        self.myDsl_BreakStmt555 = myDsl_BreakStmt555
        
    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def myDsl_BreakStmt(self):
        return self.__myDsl_BreakStmt

    @myDsl_BreakStmt.setter
    def myDsl_BreakStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BreakStmt__myDsl_BreakStmt", None)
        self.__myDsl_BreakStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement342"):
                opp_val = getattr(old_value, "myDsl_Statement342", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement342"):
                opp_val = getattr(value, "myDsl_Statement342", None)
                setattr(value, "myDsl_Statement342", self)

    @property
    def myDsl_BreakStmt555(self):
        return self.__myDsl_BreakStmt555

    @myDsl_BreakStmt555.setter
    def myDsl_BreakStmt555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BreakStmt__myDsl_BreakStmt555", None)
        self.__myDsl_BreakStmt555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Label556"):
                opp_val = getattr(old_value, "myDsl_Label556", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Label556", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Label556"):
                opp_val = getattr(value, "myDsl_Label556", None)
                setattr(value, "myDsl_Label556", self)

class myDsl_ReturnStmt:

    def __init__(self, return: str, myDsl_ReturnStmt: "myDsl_Statement" = None, myDsl_ReturnStmt552: "myDsl_ExpressionList" = None):
        self.return = return
        self.myDsl_ReturnStmt = myDsl_ReturnStmt
        self.myDsl_ReturnStmt552 = myDsl_ReturnStmt552
        
    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def myDsl_ReturnStmt552(self):
        return self.__myDsl_ReturnStmt552

    @myDsl_ReturnStmt552.setter
    def myDsl_ReturnStmt552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReturnStmt__myDsl_ReturnStmt552", None)
        self.__myDsl_ReturnStmt552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExpressionList553"):
                opp_val = getattr(old_value, "myDsl_ExpressionList553", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExpressionList553", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExpressionList553"):
                opp_val = getattr(value, "myDsl_ExpressionList553", None)
                setattr(value, "myDsl_ExpressionList553", self)

    @property
    def myDsl_ReturnStmt(self):
        return self.__myDsl_ReturnStmt

    @myDsl_ReturnStmt.setter
    def myDsl_ReturnStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReturnStmt__myDsl_ReturnStmt", None)
        self.__myDsl_ReturnStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement340"):
                opp_val = getattr(old_value, "myDsl_Statement340", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement340"):
                opp_val = getattr(value, "myDsl_Statement340", None)
                setattr(value, "myDsl_Statement340", self)

class myDsl_GoStmt:

    def __init__(self, go: str, myDsl_GoStmt: "myDsl_Statement" = None, myDsl_GoStmt523: "myDsl_Expression" = None):
        self.go = go
        self.myDsl_GoStmt = myDsl_GoStmt
        self.myDsl_GoStmt523 = myDsl_GoStmt523
        
    @property
    def go(self) -> str:
        return self.__go

    @go.setter
    def go(self, go: str):
        self.__go = go

    @property
    def myDsl_GoStmt(self):
        return self.__myDsl_GoStmt

    @myDsl_GoStmt.setter
    def myDsl_GoStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_GoStmt__myDsl_GoStmt", None)
        self.__myDsl_GoStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement338"):
                opp_val = getattr(old_value, "myDsl_Statement338", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement338"):
                opp_val = getattr(value, "myDsl_Statement338", None)
                setattr(value, "myDsl_Statement338", self)

    @property
    def myDsl_GoStmt523(self):
        return self.__myDsl_GoStmt523

    @myDsl_GoStmt523.setter
    def myDsl_GoStmt523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_GoStmt__myDsl_GoStmt523", None)
        self.__myDsl_GoStmt523 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression524"):
                opp_val = getattr(old_value, "myDsl_Expression524", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression524", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression524"):
                opp_val = getattr(value, "myDsl_Expression524", None)
                setattr(value, "myDsl_Expression524", self)

class myDsl_SimpleStmt:

    pass
class myDsl_SwitchStmt:

    pass
class myDsl_IfStmt:

    def __init__(self, if: str, else: str, myDsl_IfStmt: "myDsl_Statement" = None, myDsl_IfStmt389: "myDsl_Expression" = None, myDsl_IfStmt392: "myDsl_IfStmtLinha" = None, myDsl_IfStmt404: "myDsl_IfStmt" = None, myDsl_IfStmt402: "myDsl_IfStmt" = None, myDsl_IfStmt406: "myDsl_Block" = None, myDsl_IfStmt394: "myDsl_EmptyStmt" = None, myDsl_IfStmt397: "myDsl_ShortVarDecl" = None, myDsl_IfStmt400: "myDsl_Block" = None, myDsl_IfStmt419: "myDsl_IfStmtLinha" = None):
        self.if = if
        self.else = else
        self.myDsl_IfStmt = myDsl_IfStmt
        self.myDsl_IfStmt389 = myDsl_IfStmt389
        self.myDsl_IfStmt392 = myDsl_IfStmt392
        self.myDsl_IfStmt404 = myDsl_IfStmt404
        self.myDsl_IfStmt402 = myDsl_IfStmt402
        self.myDsl_IfStmt406 = myDsl_IfStmt406
        self.myDsl_IfStmt394 = myDsl_IfStmt394
        self.myDsl_IfStmt397 = myDsl_IfStmt397
        self.myDsl_IfStmt400 = myDsl_IfStmt400
        self.myDsl_IfStmt419 = myDsl_IfStmt419
        
    @property
    def else(self) -> str:
        return self.__else

    @else.setter
    def else(self, else: str):
        self.__else = else

    @property
    def if(self) -> str:
        return self.__if

    @if.setter
    def if(self, if: str):
        self.__if = if

    @property
    def myDsl_IfStmt397(self):
        return self.__myDsl_IfStmt397

    @myDsl_IfStmt397.setter
    def myDsl_IfStmt397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt397", None)
        self.__myDsl_IfStmt397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ShortVarDecl398"):
                opp_val = getattr(old_value, "myDsl_ShortVarDecl398", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ShortVarDecl398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ShortVarDecl398"):
                opp_val = getattr(value, "myDsl_ShortVarDecl398", None)
                setattr(value, "myDsl_ShortVarDecl398", self)

    @property
    def myDsl_IfStmt402(self):
        return self.__myDsl_IfStmt402

    @myDsl_IfStmt402.setter
    def myDsl_IfStmt402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt402", None)
        self.__myDsl_IfStmt402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmt404"):
                opp_val = getattr(old_value, "myDsl_IfStmt404", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmt404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmt404"):
                opp_val = getattr(value, "myDsl_IfStmt404", None)
                setattr(value, "myDsl_IfStmt404", self)

    @property
    def myDsl_IfStmt(self):
        return self.__myDsl_IfStmt

    @myDsl_IfStmt.setter
    def myDsl_IfStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt", None)
        self.__myDsl_IfStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement353"):
                opp_val = getattr(old_value, "myDsl_Statement353", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement353"):
                opp_val = getattr(value, "myDsl_Statement353", None)
                setattr(value, "myDsl_Statement353", self)

    @property
    def myDsl_IfStmt419(self):
        return self.__myDsl_IfStmt419

    @myDsl_IfStmt419.setter
    def myDsl_IfStmt419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt419", None)
        self.__myDsl_IfStmt419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmtLinha418"):
                opp_val = getattr(old_value, "myDsl_IfStmtLinha418", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmtLinha418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmtLinha418"):
                opp_val = getattr(value, "myDsl_IfStmtLinha418", None)
                setattr(value, "myDsl_IfStmtLinha418", self)

    @property
    def myDsl_IfStmt394(self):
        return self.__myDsl_IfStmt394

    @myDsl_IfStmt394.setter
    def myDsl_IfStmt394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt394", None)
        self.__myDsl_IfStmt394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_EmptyStmt395"):
                opp_val = getattr(old_value, "myDsl_EmptyStmt395", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_EmptyStmt395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_EmptyStmt395"):
                opp_val = getattr(value, "myDsl_EmptyStmt395", None)
                setattr(value, "myDsl_EmptyStmt395", self)

    @property
    def myDsl_IfStmt392(self):
        return self.__myDsl_IfStmt392

    @myDsl_IfStmt392.setter
    def myDsl_IfStmt392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt392", None)
        self.__myDsl_IfStmt392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmtLinha"):
                opp_val = getattr(old_value, "myDsl_IfStmtLinha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmtLinha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmtLinha"):
                opp_val = getattr(value, "myDsl_IfStmtLinha", None)
                setattr(value, "myDsl_IfStmtLinha", self)

    @property
    def myDsl_IfStmt404(self):
        return self.__myDsl_IfStmt404

    @myDsl_IfStmt404.setter
    def myDsl_IfStmt404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt404", None)
        self.__myDsl_IfStmt404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IfStmt402"):
                opp_val = getattr(old_value, "myDsl_IfStmt402", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IfStmt402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IfStmt402"):
                opp_val = getattr(value, "myDsl_IfStmt402", None)
                setattr(value, "myDsl_IfStmt402", self)

    @property
    def myDsl_IfStmt400(self):
        return self.__myDsl_IfStmt400

    @myDsl_IfStmt400.setter
    def myDsl_IfStmt400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt400", None)
        self.__myDsl_IfStmt400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block401"):
                opp_val = getattr(old_value, "myDsl_Block401", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block401"):
                opp_val = getattr(value, "myDsl_Block401", None)
                setattr(value, "myDsl_Block401", self)

    @property
    def myDsl_IfStmt389(self):
        return self.__myDsl_IfStmt389

    @myDsl_IfStmt389.setter
    def myDsl_IfStmt389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt389", None)
        self.__myDsl_IfStmt389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression390"):
                opp_val = getattr(old_value, "myDsl_Expression390", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression390", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression390"):
                opp_val = getattr(value, "myDsl_Expression390", None)
                setattr(value, "myDsl_Expression390", self)

    @property
    def myDsl_IfStmt406(self):
        return self.__myDsl_IfStmt406

    @myDsl_IfStmt406.setter
    def myDsl_IfStmt406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IfStmt__myDsl_IfStmt406", None)
        self.__myDsl_IfStmt406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block407"):
                opp_val = getattr(old_value, "myDsl_Block407", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block407"):
                opp_val = getattr(value, "myDsl_Block407", None)
                setattr(value, "myDsl_Block407", self)

class myDsl_FallthroughStmt:

    def __init__(self, fallthrough: str, myDsl_FallthroughStmt: "myDsl_Statement" = None):
        self.fallthrough = fallthrough
        self.myDsl_FallthroughStmt = myDsl_FallthroughStmt
        
    @property
    def fallthrough(self) -> str:
        return self.__fallthrough

    @fallthrough.setter
    def fallthrough(self, fallthrough: str):
        self.__fallthrough = fallthrough

    @property
    def myDsl_FallthroughStmt(self):
        return self.__myDsl_FallthroughStmt

    @myDsl_FallthroughStmt.setter
    def myDsl_FallthroughStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FallthroughStmt__myDsl_FallthroughStmt", None)
        self.__myDsl_FallthroughStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement348"):
                opp_val = getattr(old_value, "myDsl_Statement348", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement348"):
                opp_val = getattr(value, "myDsl_Statement348", None)
                setattr(value, "myDsl_Statement348", self)

class myDsl_GotoStmt:

    def __init__(self, goto: str, myDsl_GotoStmt: "myDsl_Statement" = None, myDsl_GotoStmt561: "myDsl_Label" = None):
        self.goto = goto
        self.myDsl_GotoStmt = myDsl_GotoStmt
        self.myDsl_GotoStmt561 = myDsl_GotoStmt561
        
    @property
    def goto(self) -> str:
        return self.__goto

    @goto.setter
    def goto(self, goto: str):
        self.__goto = goto

    @property
    def myDsl_GotoStmt(self):
        return self.__myDsl_GotoStmt

    @myDsl_GotoStmt.setter
    def myDsl_GotoStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_GotoStmt__myDsl_GotoStmt", None)
        self.__myDsl_GotoStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement346"):
                opp_val = getattr(old_value, "myDsl_Statement346", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement346"):
                opp_val = getattr(value, "myDsl_Statement346", None)
                setattr(value, "myDsl_Statement346", self)

    @property
    def myDsl_GotoStmt561(self):
        return self.__myDsl_GotoStmt561

    @myDsl_GotoStmt561.setter
    def myDsl_GotoStmt561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_GotoStmt__myDsl_GotoStmt561", None)
        self.__myDsl_GotoStmt561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Label562"):
                opp_val = getattr(old_value, "myDsl_Label562", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Label562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Label562"):
                opp_val = getattr(value, "myDsl_Label562", None)
                setattr(value, "myDsl_Label562", self)

class myDsl_BINARY_OP:

    def __init__(self, rEL_OP: str, aDD_OP: str, myDsl_BINARY_OP: "myDsl_Expression_Linha" = None):
        self.rEL_OP = rEL_OP
        self.aDD_OP = aDD_OP
        self.myDsl_BINARY_OP = myDsl_BINARY_OP
        
    @property
    def aDD_OP(self) -> str:
        return self.__aDD_OP

    @aDD_OP.setter
    def aDD_OP(self, aDD_OP: str):
        self.__aDD_OP = aDD_OP

    @property
    def rEL_OP(self) -> str:
        return self.__rEL_OP

    @rEL_OP.setter
    def rEL_OP(self, rEL_OP: str):
        self.__rEL_OP = rEL_OP

    @property
    def myDsl_BINARY_OP(self):
        return self.__myDsl_BINARY_OP

    @myDsl_BINARY_OP.setter
    def myDsl_BINARY_OP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BINARY_OP__myDsl_BINARY_OP", None)
        self.__myDsl_BINARY_OP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_Linha314"):
                opp_val = getattr(old_value, "myDsl_Expression_Linha314", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_Linha314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_Linha314"):
                opp_val = getattr(value, "myDsl_Expression_Linha314", None)
                setattr(value, "myDsl_Expression_Linha314", self)

class myDsl_LabeledStmt:

    pass
class myDsl_ReceiverType:

    pass
class myDsl_Expression1:

    pass
class myDsl_Expression_Linha:

    pass
class myDsl_UnaryExpr:

    pass
class myDsl_Arguments:

    pass
class myDsl_TypeAssertion:

    pass
class myDsl_Slice:

    pass
class myDsl_Index:

    pass
class myDsl_PrimaryExpr:

    pass
class myDsl_Selector:

    def __init__(self, id: str, myDsl_Selector: "myDsl_PrimaryExprLinha" = None):
        self.id = id
        self.myDsl_Selector = myDsl_Selector
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_Selector(self):
        return self.__myDsl_Selector

    @myDsl_Selector.setter
    def myDsl_Selector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Selector__myDsl_Selector", None)
        self.__myDsl_Selector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PrimaryExprLinha263"):
                opp_val = getattr(old_value, "myDsl_PrimaryExprLinha263", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_PrimaryExprLinha263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PrimaryExprLinha263"):
                opp_val = getattr(value, "myDsl_PrimaryExprLinha263", None)
                setattr(value, "myDsl_PrimaryExprLinha263", self)

class myDsl_MethodExpr:

    pass
class myDsl_Conversion:

    pass
class myDsl_PrimaryExprLinha:

    pass
class myDsl_Element:

    pass
class myDsl_Key:

    pass
class myDsl_FieldName:

    def __init__(self, id: str, myDsl_FieldName: "myDsl_Key" = None):
        self.id = id
        self.myDsl_FieldName = myDsl_FieldName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_FieldName(self):
        return self.__myDsl_FieldName

    @myDsl_FieldName.setter
    def myDsl_FieldName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FieldName__myDsl_FieldName", None)
        self.__myDsl_FieldName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Key235"):
                opp_val = getattr(old_value, "myDsl_Key235", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Key235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Key235"):
                opp_val = getattr(value, "myDsl_Key235", None)
                setattr(value, "myDsl_Key235", self)

class myDsl_ElementList:

    pass
class myDsl_KeyedElement:

    pass
class myDsl_LiteralValue:

    pass
class myDsl_LiteralType:

    pass
class myDsl_LiteralTypeLinha:

    pass
class myDsl_FunctionLit:

    def __init__(self, func: str, myDsl_FunctionLit: "myDsl_Literal" = None, myDsl_FunctionLit249: "myDsl_Signature" = None, myDsl_FunctionLit252: "myDsl_FunctionBody" = None):
        self.func = func
        self.myDsl_FunctionLit = myDsl_FunctionLit
        self.myDsl_FunctionLit249 = myDsl_FunctionLit249
        self.myDsl_FunctionLit252 = myDsl_FunctionLit252
        
    @property
    def func(self) -> str:
        return self.__func

    @func.setter
    def func(self, func: str):
        self.__func = func

    @property
    def myDsl_FunctionLit252(self):
        return self.__myDsl_FunctionLit252

    @myDsl_FunctionLit252.setter
    def myDsl_FunctionLit252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionLit__myDsl_FunctionLit252", None)
        self.__myDsl_FunctionLit252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FunctionBody253"):
                opp_val = getattr(old_value, "myDsl_FunctionBody253", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_FunctionBody253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FunctionBody253"):
                opp_val = getattr(value, "myDsl_FunctionBody253", None)
                setattr(value, "myDsl_FunctionBody253", self)

    @property
    def myDsl_FunctionLit(self):
        return self.__myDsl_FunctionLit

    @myDsl_FunctionLit.setter
    def myDsl_FunctionLit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionLit__myDsl_FunctionLit", None)
        self.__myDsl_FunctionLit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Literal201"):
                opp_val = getattr(old_value, "myDsl_Literal201", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Literal201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Literal201"):
                opp_val = getattr(value, "myDsl_Literal201", None)
                setattr(value, "myDsl_Literal201", self)

    @property
    def myDsl_FunctionLit249(self):
        return self.__myDsl_FunctionLit249

    @myDsl_FunctionLit249.setter
    def myDsl_FunctionLit249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionLit__myDsl_FunctionLit249", None)
        self.__myDsl_FunctionLit249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Signature250"):
                opp_val = getattr(old_value, "myDsl_Signature250", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Signature250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Signature250"):
                opp_val = getattr(value, "myDsl_Signature250", None)
                setattr(value, "myDsl_Signature250", self)

class myDsl_CompositeLit:

    pass
class myDsl_Literal:

    pass
class myDsl_Operand:

    pass
class myDsl_BasicLit:

    def __init__(self, float_lit: str, imaginary_lit: str, rune_lit: str, string_lit: str, int_lit: str, myDsl_BasicLit: "myDsl_Literal" = None):
        self.float_lit = float_lit
        self.imaginary_lit = imaginary_lit
        self.rune_lit = rune_lit
        self.string_lit = string_lit
        self.int_lit = int_lit
        self.myDsl_BasicLit = myDsl_BasicLit
        
    @property
    def int_lit(self) -> str:
        return self.__int_lit

    @int_lit.setter
    def int_lit(self, int_lit: str):
        self.__int_lit = int_lit

    @property
    def float_lit(self) -> str:
        return self.__float_lit

    @float_lit.setter
    def float_lit(self, float_lit: str):
        self.__float_lit = float_lit

    @property
    def rune_lit(self) -> str:
        return self.__rune_lit

    @rune_lit.setter
    def rune_lit(self, rune_lit: str):
        self.__rune_lit = rune_lit

    @property
    def string_lit(self) -> str:
        return self.__string_lit

    @string_lit.setter
    def string_lit(self, string_lit: str):
        self.__string_lit = string_lit

    @property
    def imaginary_lit(self) -> str:
        return self.__imaginary_lit

    @imaginary_lit.setter
    def imaginary_lit(self, imaginary_lit: str):
        self.__imaginary_lit = imaginary_lit

    @property
    def myDsl_BasicLit(self):
        return self.__myDsl_BasicLit

    @myDsl_BasicLit.setter
    def myDsl_BasicLit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BasicLit__myDsl_BasicLit", None)
        self.__myDsl_BasicLit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Literal197"):
                opp_val = getattr(old_value, "myDsl_Literal197", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Literal197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Literal197"):
                opp_val = getattr(value, "myDsl_Literal197", None)
                setattr(value, "myDsl_Literal197", self)

class myDsl_OperandName:

    def __init__(self, id: str, myDsl_OperandName: "myDsl_Operand" = None):
        self.id = id
        self.myDsl_OperandName = myDsl_OperandName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_OperandName(self):
        return self.__myDsl_OperandName

    @myDsl_OperandName.setter
    def myDsl_OperandName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OperandName__myDsl_OperandName", None)
        self.__myDsl_OperandName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Operand192"):
                opp_val = getattr(old_value, "myDsl_Operand192", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Operand192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Operand192"):
                opp_val = getattr(value, "myDsl_Operand192", None)
                setattr(value, "myDsl_Operand192", self)

class myDsl_Receiver:

    pass
class myDsl_ShortVarDecl:

    pass
class myDsl_FunctionBody:

    pass
class myDsl_FunctionName:

    def __init__(self, id: str, myDsl_FunctionName: "myDsl_FunctionDecl" = None):
        self.id = id
        self.myDsl_FunctionName = myDsl_FunctionName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_FunctionName(self):
        return self.__myDsl_FunctionName

    @myDsl_FunctionName.setter
    def myDsl_FunctionName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionName__myDsl_FunctionName", None)
        self.__myDsl_FunctionName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FunctionDecl167"):
                opp_val = getattr(old_value, "myDsl_FunctionDecl167", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_FunctionDecl167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FunctionDecl167"):
                opp_val = getattr(value, "myDsl_FunctionDecl167", None)
                setattr(value, "myDsl_FunctionDecl167", self)

class myDsl_VarSpec:

    pass
class myDsl_TypeDef:

    def __init__(self, id: str, myDsl_TypeDef145: "myDsl_Type" = None, myDsl_TypeDef: "myDsl_TypeSpec" = None):
        self.id = id
        self.myDsl_TypeDef145 = myDsl_TypeDef145
        self.myDsl_TypeDef = myDsl_TypeDef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_TypeDef(self):
        return self.__myDsl_TypeDef

    @myDsl_TypeDef.setter
    def myDsl_TypeDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeDef__myDsl_TypeDef", None)
        self.__myDsl_TypeDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeSpec140"):
                opp_val = getattr(old_value, "myDsl_TypeSpec140", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeSpec140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeSpec140"):
                opp_val = getattr(value, "myDsl_TypeSpec140", None)
                setattr(value, "myDsl_TypeSpec140", self)

    @property
    def myDsl_TypeDef145(self):
        return self.__myDsl_TypeDef145

    @myDsl_TypeDef145.setter
    def myDsl_TypeDef145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeDef__myDsl_TypeDef145", None)
        self.__myDsl_TypeDef145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type146"):
                opp_val = getattr(old_value, "myDsl_Type146", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type146"):
                opp_val = getattr(value, "myDsl_Type146", None)
                setattr(value, "myDsl_Type146", self)

class myDsl_AliasDecl:

    def __init__(self, id: str, myDsl_AliasDecl142: "myDsl_Type" = None, myDsl_AliasDecl: "myDsl_TypeSpec" = None):
        self.id = id
        self.myDsl_AliasDecl142 = myDsl_AliasDecl142
        self.myDsl_AliasDecl = myDsl_AliasDecl
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_AliasDecl(self):
        return self.__myDsl_AliasDecl

    @myDsl_AliasDecl.setter
    def myDsl_AliasDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AliasDecl__myDsl_AliasDecl", None)
        self.__myDsl_AliasDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeSpec138"):
                opp_val = getattr(old_value, "myDsl_TypeSpec138", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeSpec138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeSpec138"):
                opp_val = getattr(value, "myDsl_TypeSpec138", None)
                setattr(value, "myDsl_TypeSpec138", self)

    @property
    def myDsl_AliasDecl142(self):
        return self.__myDsl_AliasDecl142

    @myDsl_AliasDecl142.setter
    def myDsl_AliasDecl142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AliasDecl__myDsl_AliasDecl142", None)
        self.__myDsl_AliasDecl142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type143"):
                opp_val = getattr(old_value, "myDsl_Type143", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type143"):
                opp_val = getattr(value, "myDsl_Type143", None)
                setattr(value, "myDsl_Type143", self)

class myDsl_TypeSpec:

    pass
class myDsl_ExpressionList:

    pass
class myDsl_FunctionDecl:

    pass
class myDsl_TopLevelDecl:

    pass
class myDsl_ConstSpec:

    pass
class myDsl_MethodDecl:

    pass
class myDsl_Statement:

    pass
class myDsl_StatementList:

    pass
class myDsl_Block:

    pass
class myDsl_VarDecl:

    def __init__(self, var: str, myDsl_VarDecl: "myDsl_Declaration" = None, myDsl_VarDecl148: "myDsl_VarSpec" = None, myDsl_VarDecl150: set["myDsl_VarSpec"] = None):
        self.var = var
        self.myDsl_VarDecl = myDsl_VarDecl
        self.myDsl_VarDecl148 = myDsl_VarDecl148
        self.myDsl_VarDecl150 = myDsl_VarDecl150 if myDsl_VarDecl150 is not None else set()
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def myDsl_VarDecl(self):
        return self.__myDsl_VarDecl

    @myDsl_VarDecl.setter
    def myDsl_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_VarDecl__myDsl_VarDecl", None)
        self.__myDsl_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Declaration106"):
                opp_val = getattr(old_value, "myDsl_Declaration106", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Declaration106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Declaration106"):
                opp_val = getattr(value, "myDsl_Declaration106", None)
                setattr(value, "myDsl_Declaration106", self)

    @property
    def myDsl_VarDecl150(self):
        return self.__myDsl_VarDecl150

    @myDsl_VarDecl150.setter
    def myDsl_VarDecl150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_VarDecl__myDsl_VarDecl150", None)
        self.__myDsl_VarDecl150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_VarSpec151"):
                    opp_val = getattr(item, "myDsl_VarSpec151", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_VarSpec151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_VarSpec151"):
                    opp_val = getattr(item, "myDsl_VarSpec151", None)
                    
                    setattr(item, "myDsl_VarSpec151", self)
                    

    @property
    def myDsl_VarDecl148(self):
        return self.__myDsl_VarDecl148

    @myDsl_VarDecl148.setter
    def myDsl_VarDecl148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_VarDecl__myDsl_VarDecl148", None)
        self.__myDsl_VarDecl148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_VarSpec"):
                opp_val = getattr(old_value, "myDsl_VarSpec", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_VarSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_VarSpec"):
                opp_val = getattr(value, "myDsl_VarSpec", None)
                setattr(value, "myDsl_VarSpec", self)

class myDsl_TypeDecl:

    def __init__(self, typekeyword: str, myDsl_TypeDecl: "myDsl_Declaration" = None, myDsl_TypeDecl133: "myDsl_TypeSpec" = None, myDsl_TypeDecl135: set["myDsl_TypeSpec"] = None):
        self.typekeyword = typekeyword
        self.myDsl_TypeDecl = myDsl_TypeDecl
        self.myDsl_TypeDecl133 = myDsl_TypeDecl133
        self.myDsl_TypeDecl135 = myDsl_TypeDecl135 if myDsl_TypeDecl135 is not None else set()
        
    @property
    def typekeyword(self) -> str:
        return self.__typekeyword

    @typekeyword.setter
    def typekeyword(self, typekeyword: str):
        self.__typekeyword = typekeyword

    @property
    def myDsl_TypeDecl(self):
        return self.__myDsl_TypeDecl

    @myDsl_TypeDecl.setter
    def myDsl_TypeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeDecl__myDsl_TypeDecl", None)
        self.__myDsl_TypeDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Declaration104"):
                opp_val = getattr(old_value, "myDsl_Declaration104", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Declaration104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Declaration104"):
                opp_val = getattr(value, "myDsl_Declaration104", None)
                setattr(value, "myDsl_Declaration104", self)

    @property
    def myDsl_TypeDecl135(self):
        return self.__myDsl_TypeDecl135

    @myDsl_TypeDecl135.setter
    def myDsl_TypeDecl135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeDecl__myDsl_TypeDecl135", None)
        self.__myDsl_TypeDecl135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_TypeSpec136"):
                    opp_val = getattr(item, "myDsl_TypeSpec136", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_TypeSpec136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_TypeSpec136"):
                    opp_val = getattr(item, "myDsl_TypeSpec136", None)
                    
                    setattr(item, "myDsl_TypeSpec136", self)
                    

    @property
    def myDsl_TypeDecl133(self):
        return self.__myDsl_TypeDecl133

    @myDsl_TypeDecl133.setter
    def myDsl_TypeDecl133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeDecl__myDsl_TypeDecl133", None)
        self.__myDsl_TypeDecl133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeSpec"):
                opp_val = getattr(old_value, "myDsl_TypeSpec", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeSpec"):
                opp_val = getattr(value, "myDsl_TypeSpec", None)
                setattr(value, "myDsl_TypeSpec", self)

class myDsl_ConstDecl:

    def __init__(self, const: str, myDsl_ConstDecl: "myDsl_Declaration" = None, myDsl_ConstDecl114: "myDsl_ConstSpec" = None, myDsl_ConstDecl116: set["myDsl_ConstSpec"] = None):
        self.const = const
        self.myDsl_ConstDecl = myDsl_ConstDecl
        self.myDsl_ConstDecl114 = myDsl_ConstDecl114
        self.myDsl_ConstDecl116 = myDsl_ConstDecl116 if myDsl_ConstDecl116 is not None else set()
        
    @property
    def const(self) -> str:
        return self.__const

    @const.setter
    def const(self, const: str):
        self.__const = const

    @property
    def myDsl_ConstDecl114(self):
        return self.__myDsl_ConstDecl114

    @myDsl_ConstDecl114.setter
    def myDsl_ConstDecl114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ConstDecl__myDsl_ConstDecl114", None)
        self.__myDsl_ConstDecl114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ConstSpec"):
                opp_val = getattr(old_value, "myDsl_ConstSpec", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ConstSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ConstSpec"):
                opp_val = getattr(value, "myDsl_ConstSpec", None)
                setattr(value, "myDsl_ConstSpec", self)

    @property
    def myDsl_ConstDecl(self):
        return self.__myDsl_ConstDecl

    @myDsl_ConstDecl.setter
    def myDsl_ConstDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ConstDecl__myDsl_ConstDecl", None)
        self.__myDsl_ConstDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Declaration"):
                opp_val = getattr(old_value, "myDsl_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Declaration"):
                opp_val = getattr(value, "myDsl_Declaration", None)
                setattr(value, "myDsl_Declaration", self)

    @property
    def myDsl_ConstDecl116(self):
        return self.__myDsl_ConstDecl116

    @myDsl_ConstDecl116.setter
    def myDsl_ConstDecl116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ConstDecl__myDsl_ConstDecl116", None)
        self.__myDsl_ConstDecl116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ConstSpec117"):
                    opp_val = getattr(item, "myDsl_ConstSpec117", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ConstSpec117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ConstSpec117"):
                    opp_val = getattr(item, "myDsl_ConstSpec117", None)
                    
                    setattr(item, "myDsl_ConstSpec117", self)
                    

class myDsl_Declaration:

    pass
class myDsl_ChannelTypeLinha:

    def __init__(self, aNY_OTHER: str, myDsl_ChannelTypeLinha: "myDsl_ChannelType" = None):
        self.aNY_OTHER = aNY_OTHER
        self.myDsl_ChannelTypeLinha = myDsl_ChannelTypeLinha
        
    @property
    def aNY_OTHER(self) -> str:
        return self.__aNY_OTHER

    @aNY_OTHER.setter
    def aNY_OTHER(self, aNY_OTHER: str):
        self.__aNY_OTHER = aNY_OTHER

    @property
    def myDsl_ChannelTypeLinha(self):
        return self.__myDsl_ChannelTypeLinha

    @myDsl_ChannelTypeLinha.setter
    def myDsl_ChannelTypeLinha(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ChannelTypeLinha__myDsl_ChannelTypeLinha", None)
        self.__myDsl_ChannelTypeLinha = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ChannelType95"):
                opp_val = getattr(old_value, "myDsl_ChannelType95", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ChannelType95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ChannelType95"):
                opp_val = getattr(value, "myDsl_ChannelType95", None)
                setattr(value, "myDsl_ChannelType95", self)

class myDsl_InterfaceTypeName:

    pass
class myDsl_KeyType:

    pass
class myDsl_MethodName:

    def __init__(self, id: str, myDsl_MethodName: "myDsl_MethodSpec" = None, myDsl_MethodName180: "myDsl_MethodDecl" = None, myDsl_MethodName300: "myDsl_MethodExpr" = None):
        self.id = id
        self.myDsl_MethodName = myDsl_MethodName
        self.myDsl_MethodName180 = myDsl_MethodName180
        self.myDsl_MethodName300 = myDsl_MethodName300
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_MethodName180(self):
        return self.__myDsl_MethodName180

    @myDsl_MethodName180.setter
    def myDsl_MethodName180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodName__myDsl_MethodName180", None)
        self.__myDsl_MethodName180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MethodDecl179"):
                opp_val = getattr(old_value, "myDsl_MethodDecl179", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MethodDecl179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MethodDecl179"):
                opp_val = getattr(value, "myDsl_MethodDecl179", None)
                setattr(value, "myDsl_MethodDecl179", self)

    @property
    def myDsl_MethodName300(self):
        return self.__myDsl_MethodName300

    @myDsl_MethodName300.setter
    def myDsl_MethodName300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodName__myDsl_MethodName300", None)
        self.__myDsl_MethodName300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MethodExpr299"):
                opp_val = getattr(old_value, "myDsl_MethodExpr299", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MethodExpr299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MethodExpr299"):
                opp_val = getattr(value, "myDsl_MethodExpr299", None)
                setattr(value, "myDsl_MethodExpr299", self)

    @property
    def myDsl_MethodName(self):
        return self.__myDsl_MethodName

    @myDsl_MethodName.setter
    def myDsl_MethodName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodName__myDsl_MethodName", None)
        self.__myDsl_MethodName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MethodSpec77"):
                opp_val = getattr(old_value, "myDsl_MethodSpec77", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MethodSpec77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MethodSpec77"):
                opp_val = getattr(value, "myDsl_MethodSpec77", None)
                setattr(value, "myDsl_MethodSpec77", self)

class myDsl_MethodSpec:

    pass
class myDsl_ParameterDecl:

    pass
class myDsl_ParameterList:

    pass
class myDsl_Signature:

    pass
class myDsl_Result:

    pass
class myDsl_Parameters:

    pass
class myDsl_Tag:

    def __init__(self, string_lit: str, myDsl_Tag: "myDsl_FieldDecl" = None):
        self.string_lit = string_lit
        self.myDsl_Tag = myDsl_Tag
        
    @property
    def string_lit(self) -> str:
        return self.__string_lit

    @string_lit.setter
    def string_lit(self, string_lit: str):
        self.__string_lit = string_lit

    @property
    def myDsl_Tag(self):
        return self.__myDsl_Tag

    @myDsl_Tag.setter
    def myDsl_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Tag__myDsl_Tag", None)
        self.__myDsl_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FieldDecl40"):
                opp_val = getattr(old_value, "myDsl_FieldDecl40", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_FieldDecl40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FieldDecl40"):
                opp_val = getattr(value, "myDsl_FieldDecl40", None)
                setattr(value, "myDsl_FieldDecl40", self)

class myDsl_EmbeddedField:

    pass
class myDsl_BaseType:

    pass
class myDsl_FieldDecl:

    pass
class myDsl_Expression:

    pass
class myDsl_IdentifierList:

    def __init__(self, id: str, id1: str, myDsl_IdentifierList: "myDsl_FieldDecl" = None, myDsl_IdentifierList70: "myDsl_ParameterDecl" = None, myDsl_IdentifierList120: "myDsl_ConstSpec" = None, myDsl_IdentifierList154: "myDsl_VarSpec" = None, myDsl_IdentifierList162: "myDsl_ShortVarDecl" = None, myDsl_IdentifierList483: "myDsl_ForStmt" = None, myDsl_IdentifierList545: "myDsl_CommCaseLinha" = None):
        self.id = id
        self.id1 = id1
        self.myDsl_IdentifierList = myDsl_IdentifierList
        self.myDsl_IdentifierList70 = myDsl_IdentifierList70
        self.myDsl_IdentifierList120 = myDsl_IdentifierList120
        self.myDsl_IdentifierList154 = myDsl_IdentifierList154
        self.myDsl_IdentifierList162 = myDsl_IdentifierList162
        self.myDsl_IdentifierList483 = myDsl_IdentifierList483
        self.myDsl_IdentifierList545 = myDsl_IdentifierList545
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def id1(self) -> str:
        return self.__id1

    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def myDsl_IdentifierList483(self):
        return self.__myDsl_IdentifierList483

    @myDsl_IdentifierList483.setter
    def myDsl_IdentifierList483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList483", None)
        self.__myDsl_IdentifierList483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ForStmt482"):
                opp_val = getattr(old_value, "myDsl_ForStmt482", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ForStmt482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ForStmt482"):
                opp_val = getattr(value, "myDsl_ForStmt482", None)
                setattr(value, "myDsl_ForStmt482", self)

    @property
    def myDsl_IdentifierList154(self):
        return self.__myDsl_IdentifierList154

    @myDsl_IdentifierList154.setter
    def myDsl_IdentifierList154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList154", None)
        self.__myDsl_IdentifierList154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_VarSpec153"):
                opp_val = getattr(old_value, "myDsl_VarSpec153", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_VarSpec153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_VarSpec153"):
                opp_val = getattr(value, "myDsl_VarSpec153", None)
                setattr(value, "myDsl_VarSpec153", self)

    @property
    def myDsl_IdentifierList(self):
        return self.__myDsl_IdentifierList

    @myDsl_IdentifierList.setter
    def myDsl_IdentifierList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList", None)
        self.__myDsl_IdentifierList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FieldDecl33"):
                opp_val = getattr(old_value, "myDsl_FieldDecl33", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_FieldDecl33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FieldDecl33"):
                opp_val = getattr(value, "myDsl_FieldDecl33", None)
                setattr(value, "myDsl_FieldDecl33", self)

    @property
    def myDsl_IdentifierList545(self):
        return self.__myDsl_IdentifierList545

    @myDsl_IdentifierList545.setter
    def myDsl_IdentifierList545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList545", None)
        self.__myDsl_IdentifierList545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_CommCaseLinha544"):
                opp_val = getattr(old_value, "myDsl_CommCaseLinha544", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_CommCaseLinha544", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_CommCaseLinha544"):
                opp_val = getattr(value, "myDsl_CommCaseLinha544", None)
                setattr(value, "myDsl_CommCaseLinha544", self)

    @property
    def myDsl_IdentifierList70(self):
        return self.__myDsl_IdentifierList70

    @myDsl_IdentifierList70.setter
    def myDsl_IdentifierList70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList70", None)
        self.__myDsl_IdentifierList70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ParameterDecl69"):
                opp_val = getattr(old_value, "myDsl_ParameterDecl69", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ParameterDecl69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ParameterDecl69"):
                opp_val = getattr(value, "myDsl_ParameterDecl69", None)
                setattr(value, "myDsl_ParameterDecl69", self)

    @property
    def myDsl_IdentifierList162(self):
        return self.__myDsl_IdentifierList162

    @myDsl_IdentifierList162.setter
    def myDsl_IdentifierList162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList162", None)
        self.__myDsl_IdentifierList162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ShortVarDecl"):
                opp_val = getattr(old_value, "myDsl_ShortVarDecl", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ShortVarDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ShortVarDecl"):
                opp_val = getattr(value, "myDsl_ShortVarDecl", None)
                setattr(value, "myDsl_ShortVarDecl", self)

    @property
    def myDsl_IdentifierList120(self):
        return self.__myDsl_IdentifierList120

    @myDsl_IdentifierList120.setter
    def myDsl_IdentifierList120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IdentifierList__myDsl_IdentifierList120", None)
        self.__myDsl_IdentifierList120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ConstSpec119"):
                opp_val = getattr(old_value, "myDsl_ConstSpec119", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ConstSpec119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ConstSpec119"):
                opp_val = getattr(value, "myDsl_ConstSpec119", None)
                setattr(value, "myDsl_ConstSpec119", self)

class myDsl_InterfaceType:

    def __init__(self, interface: str, myDsl_InterfaceType: "myDsl_TypeLit" = None, myDsl_InterfaceType75: set["myDsl_MethodSpec"] = None):
        self.interface = interface
        self.myDsl_InterfaceType = myDsl_InterfaceType
        self.myDsl_InterfaceType75 = myDsl_InterfaceType75 if myDsl_InterfaceType75 is not None else set()
        
    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def myDsl_InterfaceType75(self):
        return self.__myDsl_InterfaceType75

    @myDsl_InterfaceType75.setter
    def myDsl_InterfaceType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_InterfaceType__myDsl_InterfaceType75", None)
        self.__myDsl_InterfaceType75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_MethodSpec"):
                    opp_val = getattr(item, "myDsl_MethodSpec", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_MethodSpec", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_MethodSpec"):
                    opp_val = getattr(item, "myDsl_MethodSpec", None)
                    
                    setattr(item, "myDsl_MethodSpec", self)
                    

    @property
    def myDsl_InterfaceType(self):
        return self.__myDsl_InterfaceType

    @myDsl_InterfaceType.setter
    def myDsl_InterfaceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_InterfaceType__myDsl_InterfaceType", None)
        self.__myDsl_InterfaceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeLit16"):
                opp_val = getattr(old_value, "myDsl_TypeLit16", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeLit16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeLit16"):
                opp_val = getattr(value, "myDsl_TypeLit16", None)
                setattr(value, "myDsl_TypeLit16", self)

class myDsl_FunctionType:

    def __init__(self, func: str, myDsl_FunctionType: "myDsl_TypeLit" = None, myDsl_FunctionType50: "myDsl_Signature" = None):
        self.func = func
        self.myDsl_FunctionType = myDsl_FunctionType
        self.myDsl_FunctionType50 = myDsl_FunctionType50
        
    @property
    def func(self) -> str:
        return self.__func

    @func.setter
    def func(self, func: str):
        self.__func = func

    @property
    def myDsl_FunctionType(self):
        return self.__myDsl_FunctionType

    @myDsl_FunctionType.setter
    def myDsl_FunctionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionType__myDsl_FunctionType", None)
        self.__myDsl_FunctionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeLit14"):
                opp_val = getattr(old_value, "myDsl_TypeLit14", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeLit14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeLit14"):
                opp_val = getattr(value, "myDsl_TypeLit14", None)
                setattr(value, "myDsl_TypeLit14", self)

    @property
    def myDsl_FunctionType50(self):
        return self.__myDsl_FunctionType50

    @myDsl_FunctionType50.setter
    def myDsl_FunctionType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FunctionType__myDsl_FunctionType50", None)
        self.__myDsl_FunctionType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Signature"):
                opp_val = getattr(old_value, "myDsl_Signature", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Signature"):
                opp_val = getattr(value, "myDsl_Signature", None)
                setattr(value, "myDsl_Signature", self)

class myDsl_PointerType:

    pass
class myDsl_StructType:

    def __init__(self, struct: str, myDsl_StructType: "myDsl_TypeLit" = None, myDsl_StructType31: set["myDsl_FieldDecl"] = None, myDsl_StructType208: "myDsl_LiteralType" = None):
        self.struct = struct
        self.myDsl_StructType = myDsl_StructType
        self.myDsl_StructType31 = myDsl_StructType31 if myDsl_StructType31 is not None else set()
        self.myDsl_StructType208 = myDsl_StructType208
        
    @property
    def struct(self) -> str:
        return self.__struct

    @struct.setter
    def struct(self, struct: str):
        self.__struct = struct

    @property
    def myDsl_StructType208(self):
        return self.__myDsl_StructType208

    @myDsl_StructType208.setter
    def myDsl_StructType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_StructType__myDsl_StructType208", None)
        self.__myDsl_StructType208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LiteralType207"):
                opp_val = getattr(old_value, "myDsl_LiteralType207", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_LiteralType207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LiteralType207"):
                opp_val = getattr(value, "myDsl_LiteralType207", None)
                setattr(value, "myDsl_LiteralType207", self)

    @property
    def myDsl_StructType31(self):
        return self.__myDsl_StructType31

    @myDsl_StructType31.setter
    def myDsl_StructType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_StructType__myDsl_StructType31", None)
        self.__myDsl_StructType31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_FieldDecl"):
                    opp_val = getattr(item, "myDsl_FieldDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_FieldDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_FieldDecl"):
                    opp_val = getattr(item, "myDsl_FieldDecl", None)
                    
                    setattr(item, "myDsl_FieldDecl", self)
                    

    @property
    def myDsl_StructType(self):
        return self.__myDsl_StructType

    @myDsl_StructType.setter
    def myDsl_StructType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_StructType__myDsl_StructType", None)
        self.__myDsl_StructType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeLit10"):
                opp_val = getattr(old_value, "myDsl_TypeLit10", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeLit10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeLit10"):
                opp_val = getattr(value, "myDsl_TypeLit10", None)
                setattr(value, "myDsl_TypeLit10", self)

class myDsl_TypeLitLinha:

    pass
class myDsl_TypeNameLinha:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class myDsl_ElementType:

    pass
class myDsl_ArrayLength:

    pass
class myDsl_ChannelType:

    def __init__(self, chan: str, myDsl_ChannelType: "myDsl_TypeLit" = None, myDsl_ChannelType95: "myDsl_ChannelTypeLinha" = None, myDsl_ChannelType97: "myDsl_ElementType" = None):
        self.chan = chan
        self.myDsl_ChannelType = myDsl_ChannelType
        self.myDsl_ChannelType95 = myDsl_ChannelType95
        self.myDsl_ChannelType97 = myDsl_ChannelType97
        
    @property
    def chan(self) -> str:
        return self.__chan

    @chan.setter
    def chan(self, chan: str):
        self.__chan = chan

    @property
    def myDsl_ChannelType(self):
        return self.__myDsl_ChannelType

    @myDsl_ChannelType.setter
    def myDsl_ChannelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ChannelType__myDsl_ChannelType", None)
        self.__myDsl_ChannelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeLit20"):
                opp_val = getattr(old_value, "myDsl_TypeLit20", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeLit20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeLit20"):
                opp_val = getattr(value, "myDsl_TypeLit20", None)
                setattr(value, "myDsl_TypeLit20", self)

    @property
    def myDsl_ChannelType95(self):
        return self.__myDsl_ChannelType95

    @myDsl_ChannelType95.setter
    def myDsl_ChannelType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ChannelType__myDsl_ChannelType95", None)
        self.__myDsl_ChannelType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ChannelTypeLinha"):
                opp_val = getattr(old_value, "myDsl_ChannelTypeLinha", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ChannelTypeLinha", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ChannelTypeLinha"):
                opp_val = getattr(value, "myDsl_ChannelTypeLinha", None)
                setattr(value, "myDsl_ChannelTypeLinha", self)

    @property
    def myDsl_ChannelType97(self):
        return self.__myDsl_ChannelType97

    @myDsl_ChannelType97.setter
    def myDsl_ChannelType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ChannelType__myDsl_ChannelType97", None)
        self.__myDsl_ChannelType97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ElementType98"):
                opp_val = getattr(old_value, "myDsl_ElementType98", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ElementType98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ElementType98"):
                opp_val = getattr(value, "myDsl_ElementType98", None)
                setattr(value, "myDsl_ElementType98", self)

class myDsl_MapType:

    def __init__(self, map: str, myDsl_MapType: "myDsl_TypeLit" = None, myDsl_MapType87: "myDsl_KeyType" = None, myDsl_MapType89: "myDsl_ElementType" = None, myDsl_MapType211: "myDsl_LiteralType" = None):
        self.map = map
        self.myDsl_MapType = myDsl_MapType
        self.myDsl_MapType87 = myDsl_MapType87
        self.myDsl_MapType89 = myDsl_MapType89
        self.myDsl_MapType211 = myDsl_MapType211
        
    @property
    def map(self) -> str:
        return self.__map

    @map.setter
    def map(self, map: str):
        self.__map = map

    @property
    def myDsl_MapType(self):
        return self.__myDsl_MapType

    @myDsl_MapType.setter
    def myDsl_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MapType__myDsl_MapType", None)
        self.__myDsl_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeLit18"):
                opp_val = getattr(old_value, "myDsl_TypeLit18", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeLit18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeLit18"):
                opp_val = getattr(value, "myDsl_TypeLit18", None)
                setattr(value, "myDsl_TypeLit18", self)

    @property
    def myDsl_MapType87(self):
        return self.__myDsl_MapType87

    @myDsl_MapType87.setter
    def myDsl_MapType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MapType__myDsl_MapType87", None)
        self.__myDsl_MapType87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_KeyType"):
                opp_val = getattr(old_value, "myDsl_KeyType", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_KeyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_KeyType"):
                opp_val = getattr(value, "myDsl_KeyType", None)
                setattr(value, "myDsl_KeyType", self)

    @property
    def myDsl_MapType89(self):
        return self.__myDsl_MapType89

    @myDsl_MapType89.setter
    def myDsl_MapType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MapType__myDsl_MapType89", None)
        self.__myDsl_MapType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ElementType90"):
                opp_val = getattr(old_value, "myDsl_ElementType90", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ElementType90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ElementType90"):
                opp_val = getattr(value, "myDsl_ElementType90", None)
                setattr(value, "myDsl_ElementType90", self)

    @property
    def myDsl_MapType211(self):
        return self.__myDsl_MapType211

    @myDsl_MapType211.setter
    def myDsl_MapType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MapType__myDsl_MapType211", None)
        self.__myDsl_MapType211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LiteralType210"):
                opp_val = getattr(old_value, "myDsl_LiteralType210", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_LiteralType210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LiteralType210"):
                opp_val = getattr(value, "myDsl_LiteralType210", None)
                setattr(value, "myDsl_LiteralType210", self)

class myDsl_SourceFile:

    pass
class myDsl_Model:

    pass
class myDsl_TypeLit:

    pass
class myDsl_TypeName:

    def __init__(self, id: str, myDsl_TypeName: "myDsl_Type" = None, myDsl_TypeName43: "myDsl_EmbeddedField" = None, myDsl_TypeName85: "myDsl_InterfaceTypeName" = None, myDsl_TypeName214: "myDsl_LiteralType" = None):
        self.id = id
        self.myDsl_TypeName = myDsl_TypeName
        self.myDsl_TypeName43 = myDsl_TypeName43
        self.myDsl_TypeName85 = myDsl_TypeName85
        self.myDsl_TypeName214 = myDsl_TypeName214
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_TypeName214(self):
        return self.__myDsl_TypeName214

    @myDsl_TypeName214.setter
    def myDsl_TypeName214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeName__myDsl_TypeName214", None)
        self.__myDsl_TypeName214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LiteralType213"):
                opp_val = getattr(old_value, "myDsl_LiteralType213", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_LiteralType213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LiteralType213"):
                opp_val = getattr(value, "myDsl_LiteralType213", None)
                setattr(value, "myDsl_LiteralType213", self)

    @property
    def myDsl_TypeName85(self):
        return self.__myDsl_TypeName85

    @myDsl_TypeName85.setter
    def myDsl_TypeName85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeName__myDsl_TypeName85", None)
        self.__myDsl_TypeName85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_InterfaceTypeName84"):
                opp_val = getattr(old_value, "myDsl_InterfaceTypeName84", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_InterfaceTypeName84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_InterfaceTypeName84"):
                opp_val = getattr(value, "myDsl_InterfaceTypeName84", None)
                setattr(value, "myDsl_InterfaceTypeName84", self)

    @property
    def myDsl_TypeName43(self):
        return self.__myDsl_TypeName43

    @myDsl_TypeName43.setter
    def myDsl_TypeName43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeName__myDsl_TypeName43", None)
        self.__myDsl_TypeName43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_EmbeddedField42"):
                opp_val = getattr(old_value, "myDsl_EmbeddedField42", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_EmbeddedField42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_EmbeddedField42"):
                opp_val = getattr(value, "myDsl_EmbeddedField42", None)
                setattr(value, "myDsl_EmbeddedField42", self)

    @property
    def myDsl_TypeName(self):
        return self.__myDsl_TypeName

    @myDsl_TypeName.setter
    def myDsl_TypeName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_TypeName__myDsl_TypeName", None)
        self.__myDsl_TypeName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type"):
                opp_val = getattr(old_value, "myDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type"):
                opp_val = getattr(value, "myDsl_Type", None)
                setattr(value, "myDsl_Type", self)

class myDsl_Type:

    pass
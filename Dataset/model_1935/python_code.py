from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class OclUndefinedExp:

    pass
class emig_OclUndefinedExp(OclUndefinedExp):

    pass
class OclExpression:

    pass
class emig_NavigationOrAttributeCallExp(OclExpression):

    pass
class EReference:

    pass
class emig_Reference(EReference):

    pass
class EAttribute:

    pass
class emig_Attribute(EAttribute):

    pass
class EClass:

    pass
class emig_Class(EClass):

    pass
class MapExp:

    pass
class emig_MapExp(MapExp):

    pass
class TupleExp:

    pass
class emig_TupleExp(TupleExp):

    pass
class SetExp:

    pass
class emig_SetExp(SetExp):

    pass
class SequenceExp:

    pass
class emig_SequenceExp(SequenceExp):

    pass
class OrderedSetExp:

    pass
class emig_OrderedSetExp(OrderedSetExp):

    pass
class BagExp:

    pass
class emig_BagExp(BagExp):

    pass
class SuperExp:

    pass
class emig_SuperExp(SuperExp):

    pass
class VariableExp:

    pass
class emig_VariableExp(VariableExp):

    pass
class emig_EObject:

    pass
class emig_DotNavigationObjSX:

    pass
class emig_OclExpression:

    pass
class EPackage:

    pass
class emig_Package(EPackage):

    pass
class emig_DotNavigationObjDX:

    pass
class emig_FilterMigrator:

    pass
class emig_VariableDeclaration:

    pass
class Migrator:

    pass
class emig_MigratorDX(Migrator):

    def __init__(self, name: str, emig_MigratorDX63: "emig_EClass" = None, emig_MigratorDX66: set["emig_FilterMigrator"] = None, emig_MigratorDX: "emig_RewritingRule" = None):
        self.name = name
        self.emig_MigratorDX63 = emig_MigratorDX63
        self.emig_MigratorDX66 = emig_MigratorDX66 if emig_MigratorDX66 is not None else set()
        self.emig_MigratorDX = emig_MigratorDX
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emig_MigratorDX63(self):
        return self.__emig_MigratorDX63

    @emig_MigratorDX63.setter
    def emig_MigratorDX63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigratorDX__emig_MigratorDX63", None)
        self.__emig_MigratorDX63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_EClass64"):
                opp_val = getattr(old_value, "emig_EClass64", None)
                if opp_val == self:
                    setattr(old_value, "emig_EClass64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_EClass64"):
                opp_val = getattr(value, "emig_EClass64", None)
                setattr(value, "emig_EClass64", self)

    @property
    def emig_MigratorDX66(self):
        return self.__emig_MigratorDX66

    @emig_MigratorDX66.setter
    def emig_MigratorDX66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigratorDX__emig_MigratorDX66", None)
        self.__emig_MigratorDX66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_FilterMigrator67"):
                    opp_val = getattr(item, "emig_FilterMigrator67", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_FilterMigrator67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_FilterMigrator67"):
                    opp_val = getattr(item, "emig_FilterMigrator67", None)
                    
                    setattr(item, "emig_FilterMigrator67", self)
                    

    @property
    def emig_MigratorDX(self):
        return self.__emig_MigratorDX

    @emig_MigratorDX.setter
    def emig_MigratorDX(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigratorDX__emig_MigratorDX", None)
        self.__emig_MigratorDX = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_RewritingRule51"):
                opp_val = getattr(old_value, "emig_RewritingRule51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_RewritingRule51"):
                opp_val = getattr(value, "emig_RewritingRule51", None)
                if opp_val is None:
                    setattr(value, "emig_RewritingRule51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emig_MigratorSX(Migrator):

    pass
class emig_Migrator:

    pass
class emig_Parameter:

    def __init__(self, name: str, emig_Parameter: "emig_setterDef" = None):
        self.name = name
        self.emig_Parameter = emig_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emig_Parameter(self):
        return self.__emig_Parameter

    @emig_Parameter.setter
    def emig_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Parameter__emig_Parameter", None)
        self.__emig_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_setterDef47"):
                opp_val = getattr(old_value, "emig_setterDef47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_setterDef47"):
                opp_val = getattr(value, "emig_setterDef47", None)
                if opp_val is None:
                    setattr(value, "emig_setterDef47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emig_EStructuralFeature:

    pass
class emig_EReference:

    pass
class emig_EAttribute:

    pass
class emig_EClass:

    pass
class OpDef:

    pass
class emig_EAttributeOpDef(OpDef):

    pass
class emig_EClassOpDef(OpDef):

    pass
class emig_EReferenceOpDef(OpDef):

    pass
class emig_EPackageOpDef(OpDef):

    pass
class emig_setterDef:

    def __init__(self, operator: str, emig_setterDef: "emig_OpDef" = None, emig_setterDef45: "emig_EStructuralFeature" = None, emig_setterDef47: set["emig_Parameter"] = None):
        self.operator = operator
        self.emig_setterDef = emig_setterDef
        self.emig_setterDef45 = emig_setterDef45
        self.emig_setterDef47 = emig_setterDef47 if emig_setterDef47 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def emig_setterDef(self):
        return self.__emig_setterDef

    @emig_setterDef.setter
    def emig_setterDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_setterDef__emig_setterDef", None)
        self.__emig_setterDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_OpDef17"):
                opp_val = getattr(old_value, "emig_OpDef17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_OpDef17"):
                opp_val = getattr(value, "emig_OpDef17", None)
                if opp_val is None:
                    setattr(value, "emig_OpDef17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emig_setterDef45(self):
        return self.__emig_setterDef45

    @emig_setterDef45.setter
    def emig_setterDef45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_setterDef__emig_setterDef45", None)
        self.__emig_setterDef45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_EStructuralFeature"):
                opp_val = getattr(old_value, "emig_EStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "emig_EStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_EStructuralFeature"):
                opp_val = getattr(value, "emig_EStructuralFeature", None)
                setattr(value, "emig_EStructuralFeature", self)

    @property
    def emig_setterDef47(self):
        return self.__emig_setterDef47

    @emig_setterDef47.setter
    def emig_setterDef47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_setterDef__emig_setterDef47", None)
        self.__emig_setterDef47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_Parameter"):
                    opp_val = getattr(item, "emig_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_Parameter"):
                    opp_val = getattr(item, "emig_Parameter", None)
                    
                    setattr(item, "emig_Parameter", self)
                    

class emig_RewritingRule:

    pass
class emig_OpDef:

    def __init__(self, op: str, emig_OpDef: "emig_Rule" = None, emig_OpDef17: set["emig_setterDef"] = None):
        self.op = op
        self.emig_OpDef = emig_OpDef
        self.emig_OpDef17 = emig_OpDef17 if emig_OpDef17 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def emig_OpDef17(self):
        return self.__emig_OpDef17

    @emig_OpDef17.setter
    def emig_OpDef17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_OpDef__emig_OpDef17", None)
        self.__emig_OpDef17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_setterDef"):
                    opp_val = getattr(item, "emig_setterDef", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_setterDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_setterDef"):
                    opp_val = getattr(item, "emig_setterDef", None)
                    
                    setattr(item, "emig_setterDef", self)
                    

    @property
    def emig_OpDef(self):
        return self.__emig_OpDef

    @emig_OpDef.setter
    def emig_OpDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_OpDef__emig_OpDef", None)
        self.__emig_OpDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_Rule13"):
                opp_val = getattr(old_value, "emig_Rule13", None)
                if opp_val == self:
                    setattr(old_value, "emig_Rule13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_Rule13"):
                opp_val = getattr(value, "emig_Rule13", None)
                setattr(value, "emig_Rule13", self)

class emig_EPackage:

    pass
class emig_Artifact:

    def __init__(self, type: str, emig_Artifact: "emig_MigrationProgram" = None):
        self.type = type
        self.emig_Artifact = emig_Artifact
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def emig_Artifact(self):
        return self.__emig_Artifact

    @emig_Artifact.setter
    def emig_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Artifact__emig_Artifact", None)
        self.__emig_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_MigrationProgram6"):
                opp_val = getattr(old_value, "emig_MigrationProgram6", None)
                if opp_val == self:
                    setattr(old_value, "emig_MigrationProgram6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_MigrationProgram6"):
                opp_val = getattr(value, "emig_MigrationProgram6", None)
                setattr(value, "emig_MigrationProgram6", self)

class emig_Rule:

    def __init__(self, name: str, emig_Rule: "emig_MigrationLibrary" = None, emig_Rule11: "emig_MigrationProgram" = None, emig_Rule13: "emig_OpDef" = None, emig_Rule15: set["emig_RewritingRule"] = None):
        self.name = name
        self.emig_Rule = emig_Rule
        self.emig_Rule11 = emig_Rule11
        self.emig_Rule13 = emig_Rule13
        self.emig_Rule15 = emig_Rule15 if emig_Rule15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emig_Rule11(self):
        return self.__emig_Rule11

    @emig_Rule11.setter
    def emig_Rule11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Rule__emig_Rule11", None)
        self.__emig_Rule11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_MigrationProgram10"):
                opp_val = getattr(old_value, "emig_MigrationProgram10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_MigrationProgram10"):
                opp_val = getattr(value, "emig_MigrationProgram10", None)
                if opp_val is None:
                    setattr(value, "emig_MigrationProgram10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emig_Rule13(self):
        return self.__emig_Rule13

    @emig_Rule13.setter
    def emig_Rule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Rule__emig_Rule13", None)
        self.__emig_Rule13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_OpDef"):
                opp_val = getattr(old_value, "emig_OpDef", None)
                if opp_val == self:
                    setattr(old_value, "emig_OpDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_OpDef"):
                opp_val = getattr(value, "emig_OpDef", None)
                setattr(value, "emig_OpDef", self)

    @property
    def emig_Rule15(self):
        return self.__emig_Rule15

    @emig_Rule15.setter
    def emig_Rule15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Rule__emig_Rule15", None)
        self.__emig_Rule15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_RewritingRule"):
                    opp_val = getattr(item, "emig_RewritingRule", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_RewritingRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_RewritingRule"):
                    opp_val = getattr(item, "emig_RewritingRule", None)
                    
                    setattr(item, "emig_RewritingRule", self)
                    

    @property
    def emig_Rule(self):
        return self.__emig_Rule

    @emig_Rule.setter
    def emig_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_Rule__emig_Rule", None)
        self.__emig_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_MigrationLibrary4"):
                opp_val = getattr(old_value, "emig_MigrationLibrary4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_MigrationLibrary4"):
                opp_val = getattr(value, "emig_MigrationLibrary4", None)
                if opp_val is None:
                    setattr(value, "emig_MigrationLibrary4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emig_MigrationProgram:

    def __init__(self, libs: str, migr: str, name: str, delta: str, emig_MigrationProgram: "emig_MyModel" = None, emig_MigrationProgram6: "emig_Artifact" = None, emig_MigrationProgram8: set["emig_EPackage"] = None, emig_MigrationProgram10: set["emig_Rule"] = None):
        self.libs = libs
        self.migr = migr
        self.name = name
        self.delta = delta
        self.emig_MigrationProgram = emig_MigrationProgram
        self.emig_MigrationProgram6 = emig_MigrationProgram6
        self.emig_MigrationProgram8 = emig_MigrationProgram8 if emig_MigrationProgram8 is not None else set()
        self.emig_MigrationProgram10 = emig_MigrationProgram10 if emig_MigrationProgram10 is not None else set()
        
    @property
    def migr(self) -> str:
        return self.__migr

    @migr.setter
    def migr(self, migr: str):
        self.__migr = migr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libs(self) -> str:
        return self.__libs

    @libs.setter
    def libs(self, libs: str):
        self.__libs = libs

    @property
    def delta(self) -> str:
        return self.__delta

    @delta.setter
    def delta(self, delta: str):
        self.__delta = delta

    @property
    def emig_MigrationProgram6(self):
        return self.__emig_MigrationProgram6

    @emig_MigrationProgram6.setter
    def emig_MigrationProgram6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationProgram__emig_MigrationProgram6", None)
        self.__emig_MigrationProgram6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_Artifact"):
                opp_val = getattr(old_value, "emig_Artifact", None)
                if opp_val == self:
                    setattr(old_value, "emig_Artifact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_Artifact"):
                opp_val = getattr(value, "emig_Artifact", None)
                setattr(value, "emig_Artifact", self)

    @property
    def emig_MigrationProgram10(self):
        return self.__emig_MigrationProgram10

    @emig_MigrationProgram10.setter
    def emig_MigrationProgram10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationProgram__emig_MigrationProgram10", None)
        self.__emig_MigrationProgram10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_Rule11"):
                    opp_val = getattr(item, "emig_Rule11", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_Rule11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_Rule11"):
                    opp_val = getattr(item, "emig_Rule11", None)
                    
                    setattr(item, "emig_Rule11", self)
                    

    @property
    def emig_MigrationProgram8(self):
        return self.__emig_MigrationProgram8

    @emig_MigrationProgram8.setter
    def emig_MigrationProgram8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationProgram__emig_MigrationProgram8", None)
        self.__emig_MigrationProgram8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_EPackage"):
                    opp_val = getattr(item, "emig_EPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_EPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_EPackage"):
                    opp_val = getattr(item, "emig_EPackage", None)
                    
                    setattr(item, "emig_EPackage", self)
                    

    @property
    def emig_MigrationProgram(self):
        return self.__emig_MigrationProgram

    @emig_MigrationProgram.setter
    def emig_MigrationProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationProgram__emig_MigrationProgram", None)
        self.__emig_MigrationProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_MyModel2"):
                opp_val = getattr(old_value, "emig_MyModel2", None)
                if opp_val == self:
                    setattr(old_value, "emig_MyModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_MyModel2"):
                opp_val = getattr(value, "emig_MyModel2", None)
                setattr(value, "emig_MyModel2", self)

class emig_MigrationLibrary:

    def __init__(self, title: str, emig_MigrationLibrary: "emig_MyModel" = None, emig_MigrationLibrary4: set["emig_Rule"] = None):
        self.title = title
        self.emig_MigrationLibrary = emig_MigrationLibrary
        self.emig_MigrationLibrary4 = emig_MigrationLibrary4 if emig_MigrationLibrary4 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def emig_MigrationLibrary4(self):
        return self.__emig_MigrationLibrary4

    @emig_MigrationLibrary4.setter
    def emig_MigrationLibrary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationLibrary__emig_MigrationLibrary4", None)
        self.__emig_MigrationLibrary4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emig_Rule"):
                    opp_val = getattr(item, "emig_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "emig_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emig_Rule"):
                    opp_val = getattr(item, "emig_Rule", None)
                    
                    setattr(item, "emig_Rule", self)
                    

    @property
    def emig_MigrationLibrary(self):
        return self.__emig_MigrationLibrary

    @emig_MigrationLibrary.setter
    def emig_MigrationLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emig_MigrationLibrary__emig_MigrationLibrary", None)
        self.__emig_MigrationLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emig_MyModel"):
                opp_val = getattr(old_value, "emig_MyModel", None)
                if opp_val == self:
                    setattr(old_value, "emig_MyModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emig_MyModel"):
                opp_val = getattr(value, "emig_MyModel", None)
                setattr(value, "emig_MyModel", self)

class emig_MyModel:

    pass
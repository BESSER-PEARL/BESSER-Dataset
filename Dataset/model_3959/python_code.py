from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Association:

    pass
class Class:

    pass
class ClassesProv_AssociationClass(Class, Association):

    pass
class DataType:

    pass
class ClassesProv_Enumeration(DataType):

    pass
class ClassesProv_PrimitiveType(DataType):

    pass
class Realization:

    pass
class ClassesProv_InterfaceRealization(Realization):

    pass
class Abstraction:

    pass
class ClassesProv_Realization(Abstraction):

    pass
class Dependency:

    pass
class ClassesProv_Abstraction(Dependency):

    pass
class ClassesProv_Usage(Dependency):

    pass
class InstanceSpecification:

    pass
class ClassesProv_EnumerationLiteral(InstanceSpecification):

    pass
class Classifier:

    pass
class BehavioralFeature:

    pass
class ClassesProv_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, isOrdered: bool, isUnique: bool, upper: int, lower: int, ClassesProv_Operation: "ClassesProv_Type" = None, ClassesProv_Operation182: set["ClassesProv_Constraint"] = None, ClassesProv_Operation185: set["ClassesProv_Constraint"] = None, ClassesProv_Operation188: set["ClassesProv_Constraint"] = None, ClassesProv_Operation191: "ClassesProv_Class" = None, ClassesProv_Operation194: "ClassesProv_DataType" = None, ClassesProv_Operation197: "ClassesProv_Interface" = None, ClassesProv_Operation204: "ClassesProv_Class" = None, ClassesProv_Operation225: "ClassesProv_DataType" = None, ClassesProv_Operation260: "ClassesProv_Interface" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.ClassesProv_Operation = ClassesProv_Operation
        self.ClassesProv_Operation182 = ClassesProv_Operation182 if ClassesProv_Operation182 is not None else set()
        self.ClassesProv_Operation185 = ClassesProv_Operation185 if ClassesProv_Operation185 is not None else set()
        self.ClassesProv_Operation188 = ClassesProv_Operation188 if ClassesProv_Operation188 is not None else set()
        self.ClassesProv_Operation191 = ClassesProv_Operation191
        self.ClassesProv_Operation194 = ClassesProv_Operation194
        self.ClassesProv_Operation197 = ClassesProv_Operation197
        self.ClassesProv_Operation204 = ClassesProv_Operation204
        self.ClassesProv_Operation225 = ClassesProv_Operation225
        self.ClassesProv_Operation260 = ClassesProv_Operation260
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def ClassesProv_Operation191(self):
        return self.__ClassesProv_Operation191

    @ClassesProv_Operation191.setter
    def ClassesProv_Operation191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation191", None)
        self.__ClassesProv_Operation191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Class192"):
                opp_val = getattr(old_value, "ClassesProv_Class192", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Class192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Class192"):
                opp_val = getattr(value, "ClassesProv_Class192", None)
                setattr(value, "ClassesProv_Class192", self)

    @property
    def ClassesProv_Operation182(self):
        return self.__ClassesProv_Operation182

    @ClassesProv_Operation182.setter
    def ClassesProv_Operation182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation182", None)
        self.__ClassesProv_Operation182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Constraint183"):
                    opp_val = getattr(item, "ClassesProv_Constraint183", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Constraint183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Constraint183"):
                    opp_val = getattr(item, "ClassesProv_Constraint183", None)
                    
                    setattr(item, "ClassesProv_Constraint183", self)
                    

    @property
    def ClassesProv_Operation225(self):
        return self.__ClassesProv_Operation225

    @ClassesProv_Operation225.setter
    def ClassesProv_Operation225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation225", None)
        self.__ClassesProv_Operation225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_DataType224"):
                opp_val = getattr(old_value, "ClassesProv_DataType224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_DataType224"):
                opp_val = getattr(value, "ClassesProv_DataType224", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_DataType224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Operation194(self):
        return self.__ClassesProv_Operation194

    @ClassesProv_Operation194.setter
    def ClassesProv_Operation194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation194", None)
        self.__ClassesProv_Operation194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_DataType195"):
                opp_val = getattr(old_value, "ClassesProv_DataType195", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_DataType195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_DataType195"):
                opp_val = getattr(value, "ClassesProv_DataType195", None)
                setattr(value, "ClassesProv_DataType195", self)

    @property
    def ClassesProv_Operation(self):
        return self.__ClassesProv_Operation

    @ClassesProv_Operation.setter
    def ClassesProv_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation", None)
        self.__ClassesProv_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Type180"):
                opp_val = getattr(old_value, "ClassesProv_Type180", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Type180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Type180"):
                opp_val = getattr(value, "ClassesProv_Type180", None)
                setattr(value, "ClassesProv_Type180", self)

    @property
    def ClassesProv_Operation185(self):
        return self.__ClassesProv_Operation185

    @ClassesProv_Operation185.setter
    def ClassesProv_Operation185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation185", None)
        self.__ClassesProv_Operation185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Constraint186"):
                    opp_val = getattr(item, "ClassesProv_Constraint186", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Constraint186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Constraint186"):
                    opp_val = getattr(item, "ClassesProv_Constraint186", None)
                    
                    setattr(item, "ClassesProv_Constraint186", self)
                    

    @property
    def ClassesProv_Operation204(self):
        return self.__ClassesProv_Operation204

    @ClassesProv_Operation204.setter
    def ClassesProv_Operation204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation204", None)
        self.__ClassesProv_Operation204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Class203"):
                opp_val = getattr(old_value, "ClassesProv_Class203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Class203"):
                opp_val = getattr(value, "ClassesProv_Class203", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Class203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Operation260(self):
        return self.__ClassesProv_Operation260

    @ClassesProv_Operation260.setter
    def ClassesProv_Operation260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation260", None)
        self.__ClassesProv_Operation260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Interface259"):
                opp_val = getattr(old_value, "ClassesProv_Interface259", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Interface259"):
                opp_val = getattr(value, "ClassesProv_Interface259", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Interface259", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Operation188(self):
        return self.__ClassesProv_Operation188

    @ClassesProv_Operation188.setter
    def ClassesProv_Operation188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation188", None)
        self.__ClassesProv_Operation188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Constraint189"):
                    opp_val = getattr(item, "ClassesProv_Constraint189", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Constraint189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Constraint189"):
                    opp_val = getattr(item, "ClassesProv_Constraint189", None)
                    
                    setattr(item, "ClassesProv_Constraint189", self)
                    

    @property
    def ClassesProv_Operation197(self):
        return self.__ClassesProv_Operation197

    @ClassesProv_Operation197.setter
    def ClassesProv_Operation197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Operation__ClassesProv_Operation197", None)
        self.__ClassesProv_Operation197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Interface198"):
                opp_val = getattr(old_value, "ClassesProv_Interface198", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Interface198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Interface198"):
                opp_val = getattr(value, "ClassesProv_Interface198", None)
                setattr(value, "ClassesProv_Interface198", self)

class ClassesProv_Interface(Classifier):

    pass
class ClassesProv_DataType(Classifier):

    pass
class Type:

    pass
class RedefinableElement:

    pass
class ClassesProv_Class(Classifier):

    pass
class StructuralFeature:

    pass
class MultiplicityElement:

    pass
class Feature:

    pass
class ClassesProv_Substitution(Realization):

    pass
class ClassesProv_Property(StructuralFeature):

    def __init__(self, isDerived: bool, isDerivedUnion: bool, default: str, isComposite: bool, isID: bool, ClassesProv_Property: "ClassesProv_Classifier" = None, ClassesProv_Property132: "ClassesProv_Class" = None, ClassesProv_Property144: "ClassesProv_Property" = None, ClassesProv_Property142: "ClassesProv_Property" = None, ClassesProv_Property146: "ClassesProv_Association" = None, ClassesProv_Property148: "ClassesProv_Association" = None, ClassesProv_Property151: "ClassesProv_DataType" = None, ClassesProv_Property153: "ClassesProv_Interface" = None, ClassesProv_Property156: "ClassesProv_Property" = None, ClassesProv_Property154: set["ClassesProv_Property"] = None, ClassesProv_Property159: "ClassesProv_Property" = None, ClassesProv_Property157: "ClassesProv_Property" = None, ClassesProv_Property135: "ClassesProv_Property" = None, ClassesProv_Property133: set["ClassesProv_Property"] = None, ClassesProv_Property137: "ClassesProv_ValueSpecification" = None, ClassesProv_Property141: "ClassesProv_Property" = None, ClassesProv_Property139: "ClassesProv_Property" = None, ClassesProv_Property210: "ClassesProv_Class" = None, ClassesProv_Property213: "ClassesProv_Association" = None, ClassesProv_Property216: "ClassesProv_Association" = None, ClassesProv_Property219: "ClassesProv_Association" = None, ClassesProv_Property222: "ClassesProv_DataType" = None, ClassesProv_Property257: "ClassesProv_Interface" = None):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.isComposite = isComposite
        self.isID = isID
        self.ClassesProv_Property = ClassesProv_Property
        self.ClassesProv_Property132 = ClassesProv_Property132
        self.ClassesProv_Property144 = ClassesProv_Property144
        self.ClassesProv_Property142 = ClassesProv_Property142
        self.ClassesProv_Property146 = ClassesProv_Property146
        self.ClassesProv_Property148 = ClassesProv_Property148
        self.ClassesProv_Property151 = ClassesProv_Property151
        self.ClassesProv_Property153 = ClassesProv_Property153
        self.ClassesProv_Property156 = ClassesProv_Property156
        self.ClassesProv_Property154 = ClassesProv_Property154 if ClassesProv_Property154 is not None else set()
        self.ClassesProv_Property159 = ClassesProv_Property159
        self.ClassesProv_Property157 = ClassesProv_Property157
        self.ClassesProv_Property135 = ClassesProv_Property135
        self.ClassesProv_Property133 = ClassesProv_Property133 if ClassesProv_Property133 is not None else set()
        self.ClassesProv_Property137 = ClassesProv_Property137
        self.ClassesProv_Property141 = ClassesProv_Property141
        self.ClassesProv_Property139 = ClassesProv_Property139
        self.ClassesProv_Property210 = ClassesProv_Property210
        self.ClassesProv_Property213 = ClassesProv_Property213
        self.ClassesProv_Property216 = ClassesProv_Property216
        self.ClassesProv_Property219 = ClassesProv_Property219
        self.ClassesProv_Property222 = ClassesProv_Property222
        self.ClassesProv_Property257 = ClassesProv_Property257
        
    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isID(self) -> bool:
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def ClassesProv_Property159(self):
        return self.__ClassesProv_Property159

    @ClassesProv_Property159.setter
    def ClassesProv_Property159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property159", None)
        self.__ClassesProv_Property159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property157"):
                opp_val = getattr(old_value, "ClassesProv_Property157", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property157"):
                opp_val = getattr(value, "ClassesProv_Property157", None)
                setattr(value, "ClassesProv_Property157", self)

    @property
    def ClassesProv_Property132(self):
        return self.__ClassesProv_Property132

    @ClassesProv_Property132.setter
    def ClassesProv_Property132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property132", None)
        self.__ClassesProv_Property132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Class"):
                opp_val = getattr(old_value, "ClassesProv_Class", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Class"):
                opp_val = getattr(value, "ClassesProv_Class", None)
                setattr(value, "ClassesProv_Class", self)

    @property
    def ClassesProv_Property210(self):
        return self.__ClassesProv_Property210

    @ClassesProv_Property210.setter
    def ClassesProv_Property210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property210", None)
        self.__ClassesProv_Property210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Class209"):
                opp_val = getattr(old_value, "ClassesProv_Class209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Class209"):
                opp_val = getattr(value, "ClassesProv_Class209", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Class209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property153(self):
        return self.__ClassesProv_Property153

    @ClassesProv_Property153.setter
    def ClassesProv_Property153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property153", None)
        self.__ClassesProv_Property153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Interface"):
                opp_val = getattr(old_value, "ClassesProv_Interface", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Interface"):
                opp_val = getattr(value, "ClassesProv_Interface", None)
                setattr(value, "ClassesProv_Interface", self)

    @property
    def ClassesProv_Property137(self):
        return self.__ClassesProv_Property137

    @ClassesProv_Property137.setter
    def ClassesProv_Property137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property137", None)
        self.__ClassesProv_Property137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification138"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification138", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification138"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification138", None)
                setattr(value, "ClassesProv_ValueSpecification138", self)

    @property
    def ClassesProv_Property139(self):
        return self.__ClassesProv_Property139

    @ClassesProv_Property139.setter
    def ClassesProv_Property139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property139", None)
        self.__ClassesProv_Property139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property141"):
                opp_val = getattr(old_value, "ClassesProv_Property141", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property141"):
                opp_val = getattr(value, "ClassesProv_Property141", None)
                setattr(value, "ClassesProv_Property141", self)

    @property
    def ClassesProv_Property148(self):
        return self.__ClassesProv_Property148

    @ClassesProv_Property148.setter
    def ClassesProv_Property148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property148", None)
        self.__ClassesProv_Property148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Association149"):
                opp_val = getattr(old_value, "ClassesProv_Association149", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Association149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Association149"):
                opp_val = getattr(value, "ClassesProv_Association149", None)
                setattr(value, "ClassesProv_Association149", self)

    @property
    def ClassesProv_Property141(self):
        return self.__ClassesProv_Property141

    @ClassesProv_Property141.setter
    def ClassesProv_Property141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property141", None)
        self.__ClassesProv_Property141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property139"):
                opp_val = getattr(old_value, "ClassesProv_Property139", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property139"):
                opp_val = getattr(value, "ClassesProv_Property139", None)
                setattr(value, "ClassesProv_Property139", self)

    @property
    def ClassesProv_Property142(self):
        return self.__ClassesProv_Property142

    @ClassesProv_Property142.setter
    def ClassesProv_Property142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property142", None)
        self.__ClassesProv_Property142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property144"):
                opp_val = getattr(old_value, "ClassesProv_Property144", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property144"):
                opp_val = getattr(value, "ClassesProv_Property144", None)
                setattr(value, "ClassesProv_Property144", self)

    @property
    def ClassesProv_Property216(self):
        return self.__ClassesProv_Property216

    @ClassesProv_Property216.setter
    def ClassesProv_Property216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property216", None)
        self.__ClassesProv_Property216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Association215"):
                opp_val = getattr(old_value, "ClassesProv_Association215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Association215"):
                opp_val = getattr(value, "ClassesProv_Association215", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Association215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property144(self):
        return self.__ClassesProv_Property144

    @ClassesProv_Property144.setter
    def ClassesProv_Property144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property144", None)
        self.__ClassesProv_Property144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property142"):
                opp_val = getattr(old_value, "ClassesProv_Property142", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property142"):
                opp_val = getattr(value, "ClassesProv_Property142", None)
                setattr(value, "ClassesProv_Property142", self)

    @property
    def ClassesProv_Property213(self):
        return self.__ClassesProv_Property213

    @ClassesProv_Property213.setter
    def ClassesProv_Property213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property213", None)
        self.__ClassesProv_Property213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Association212"):
                opp_val = getattr(old_value, "ClassesProv_Association212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Association212"):
                opp_val = getattr(value, "ClassesProv_Association212", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Association212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property157(self):
        return self.__ClassesProv_Property157

    @ClassesProv_Property157.setter
    def ClassesProv_Property157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property157", None)
        self.__ClassesProv_Property157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property159"):
                opp_val = getattr(old_value, "ClassesProv_Property159", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property159"):
                opp_val = getattr(value, "ClassesProv_Property159", None)
                setattr(value, "ClassesProv_Property159", self)

    @property
    def ClassesProv_Property(self):
        return self.__ClassesProv_Property

    @ClassesProv_Property.setter
    def ClassesProv_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property", None)
        self.__ClassesProv_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier115"):
                opp_val = getattr(old_value, "ClassesProv_Classifier115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier115"):
                opp_val = getattr(value, "ClassesProv_Classifier115", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property133(self):
        return self.__ClassesProv_Property133

    @ClassesProv_Property133.setter
    def ClassesProv_Property133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property133", None)
        self.__ClassesProv_Property133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property135"):
                    opp_val = getattr(item, "ClassesProv_Property135", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property135"):
                    opp_val = getattr(item, "ClassesProv_Property135", None)
                    
                    setattr(item, "ClassesProv_Property135", self)
                    

    @property
    def ClassesProv_Property151(self):
        return self.__ClassesProv_Property151

    @ClassesProv_Property151.setter
    def ClassesProv_Property151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property151", None)
        self.__ClassesProv_Property151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_DataType"):
                opp_val = getattr(old_value, "ClassesProv_DataType", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_DataType"):
                opp_val = getattr(value, "ClassesProv_DataType", None)
                setattr(value, "ClassesProv_DataType", self)

    @property
    def ClassesProv_Property219(self):
        return self.__ClassesProv_Property219

    @ClassesProv_Property219.setter
    def ClassesProv_Property219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property219", None)
        self.__ClassesProv_Property219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Association218"):
                opp_val = getattr(old_value, "ClassesProv_Association218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Association218"):
                opp_val = getattr(value, "ClassesProv_Association218", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Association218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property146(self):
        return self.__ClassesProv_Property146

    @ClassesProv_Property146.setter
    def ClassesProv_Property146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property146", None)
        self.__ClassesProv_Property146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Association"):
                opp_val = getattr(old_value, "ClassesProv_Association", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Association"):
                opp_val = getattr(value, "ClassesProv_Association", None)
                setattr(value, "ClassesProv_Association", self)

    @property
    def ClassesProv_Property222(self):
        return self.__ClassesProv_Property222

    @ClassesProv_Property222.setter
    def ClassesProv_Property222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property222", None)
        self.__ClassesProv_Property222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_DataType221"):
                opp_val = getattr(old_value, "ClassesProv_DataType221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_DataType221"):
                opp_val = getattr(value, "ClassesProv_DataType221", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_DataType221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property257(self):
        return self.__ClassesProv_Property257

    @ClassesProv_Property257.setter
    def ClassesProv_Property257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property257", None)
        self.__ClassesProv_Property257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Interface256"):
                opp_val = getattr(old_value, "ClassesProv_Interface256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Interface256"):
                opp_val = getattr(value, "ClassesProv_Interface256", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Interface256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property154(self):
        return self.__ClassesProv_Property154

    @ClassesProv_Property154.setter
    def ClassesProv_Property154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property154", None)
        self.__ClassesProv_Property154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property156"):
                    opp_val = getattr(item, "ClassesProv_Property156", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property156"):
                    opp_val = getattr(item, "ClassesProv_Property156", None)
                    
                    setattr(item, "ClassesProv_Property156", self)
                    

    @property
    def ClassesProv_Property135(self):
        return self.__ClassesProv_Property135

    @ClassesProv_Property135.setter
    def ClassesProv_Property135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property135", None)
        self.__ClassesProv_Property135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property133"):
                opp_val = getattr(old_value, "ClassesProv_Property133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property133"):
                opp_val = getattr(value, "ClassesProv_Property133", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Property133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Property156(self):
        return self.__ClassesProv_Property156

    @ClassesProv_Property156.setter
    def ClassesProv_Property156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Property__ClassesProv_Property156", None)
        self.__ClassesProv_Property156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property154"):
                opp_val = getattr(old_value, "ClassesProv_Property154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property154"):
                opp_val = getattr(value, "ClassesProv_Property154", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Property154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassesProv_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, ClassesProv_Feature: "ClassesProv_Classifier" = None, ClassesProv_Feature129: set["ClassesProv_Classifier"] = None):
        self.isStatic = isStatic
        self.ClassesProv_Feature = ClassesProv_Feature
        self.ClassesProv_Feature129 = ClassesProv_Feature129 if ClassesProv_Feature129 is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def ClassesProv_Feature(self):
        return self.__ClassesProv_Feature

    @ClassesProv_Feature.setter
    def ClassesProv_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Feature__ClassesProv_Feature", None)
        self.__ClassesProv_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier113"):
                opp_val = getattr(old_value, "ClassesProv_Classifier113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier113"):
                opp_val = getattr(value, "ClassesProv_Classifier113", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Feature129(self):
        return self.__ClassesProv_Feature129

    @ClassesProv_Feature129.setter
    def ClassesProv_Feature129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Feature__ClassesProv_Feature129", None)
        self.__ClassesProv_Feature129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Classifier130"):
                    opp_val = getattr(item, "ClassesProv_Classifier130", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Classifier130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Classifier130"):
                    opp_val = getattr(item, "ClassesProv_Classifier130", None)
                    
                    setattr(item, "ClassesProv_Classifier130", self)
                    

class ValueSpecification:

    pass
class ClassesProv_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, ClassesProv_OpaqueExpression: "ClassesProv_Abstraction" = None):
        self.body = body
        self.language = language
        self.ClassesProv_OpaqueExpression = ClassesProv_OpaqueExpression
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def ClassesProv_OpaqueExpression(self):
        return self.__ClassesProv_OpaqueExpression

    @ClassesProv_OpaqueExpression.setter
    def ClassesProv_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_OpaqueExpression__ClassesProv_OpaqueExpression", None)
        self.__ClassesProv_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Abstraction"):
                opp_val = getattr(old_value, "ClassesProv_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Abstraction"):
                opp_val = getattr(value, "ClassesProv_Abstraction", None)
                setattr(value, "ClassesProv_Abstraction", self)

class ClassesProv_Expression(ValueSpecification):

    def __init__(self, symbol: str, ClassesProv_Expression: "ClassesProv_ValueSpecification" = None):
        self.symbol = symbol
        self.ClassesProv_Expression = ClassesProv_Expression
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def ClassesProv_Expression(self):
        return self.__ClassesProv_Expression

    @ClassesProv_Expression.setter
    def ClassesProv_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Expression__ClassesProv_Expression", None)
        self.__ClassesProv_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification76"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification76", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification76"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification76", None)
                setattr(value, "ClassesProv_ValueSpecification76", self)

class ClassesProv_InstanceValue:

    pass
class LiteralSpecification:

    pass
class ClassesProv_LiteralUnilimitedNatural(LiteralSpecification):

    pass
class ClassesProv_LiteralString(LiteralSpecification):

    pass
class ClassesProv_LiteralInteger(LiteralSpecification):

    pass
class ClassesProv_LiteralBoolean(LiteralSpecification):

    pass
class ClassesProv_LiteralReal(LiteralSpecification):

    pass
class ClassesProv_LiteralNull(LiteralSpecification):

    pass
class ClassesProv_LiteralSpecification(ValueSpecification):

    pass
class TypedElement:

    pass
class ClassesProv_Parameter(TypedElement):

    def __init__(self, default: str, ClassesProv_Parameter: "ClassesProv_BehavioralFeature" = None, ClassesProv_Parameter174: "ClassesProv_BehavioralFeature" = None, ClassesProv_Parameter177: "ClassesProv_ValueSpecification" = None):
        self.default = default
        self.ClassesProv_Parameter = ClassesProv_Parameter
        self.ClassesProv_Parameter174 = ClassesProv_Parameter174
        self.ClassesProv_Parameter177 = ClassesProv_Parameter177
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def ClassesProv_Parameter174(self):
        return self.__ClassesProv_Parameter174

    @ClassesProv_Parameter174.setter
    def ClassesProv_Parameter174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Parameter__ClassesProv_Parameter174", None)
        self.__ClassesProv_Parameter174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_BehavioralFeature175"):
                opp_val = getattr(old_value, "ClassesProv_BehavioralFeature175", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_BehavioralFeature175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_BehavioralFeature175"):
                opp_val = getattr(value, "ClassesProv_BehavioralFeature175", None)
                setattr(value, "ClassesProv_BehavioralFeature175", self)

    @property
    def ClassesProv_Parameter(self):
        return self.__ClassesProv_Parameter

    @ClassesProv_Parameter.setter
    def ClassesProv_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Parameter__ClassesProv_Parameter", None)
        self.__ClassesProv_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_BehavioralFeature"):
                opp_val = getattr(old_value, "ClassesProv_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_BehavioralFeature"):
                opp_val = getattr(value, "ClassesProv_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Parameter177(self):
        return self.__ClassesProv_Parameter177

    @ClassesProv_Parameter177.setter
    def ClassesProv_Parameter177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Parameter__ClassesProv_Parameter177", None)
        self.__ClassesProv_Parameter177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification178"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification178", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification178"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification178", None)
                setattr(value, "ClassesProv_ValueSpecification178", self)

class ClassesProv_StructuralFeature(TypedElement, MultiplicityElement, Feature):

    def __init__(self, isReadOnly: bool, ClassesProv_StructuralFeature: "ClassesProv_Slot" = None):
        self.isReadOnly = isReadOnly
        self.ClassesProv_StructuralFeature = ClassesProv_StructuralFeature
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def ClassesProv_StructuralFeature(self):
        return self.__ClassesProv_StructuralFeature

    @ClassesProv_StructuralFeature.setter
    def ClassesProv_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_StructuralFeature__ClassesProv_StructuralFeature", None)
        self.__ClassesProv_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Slot103"):
                opp_val = getattr(old_value, "ClassesProv_Slot103", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Slot103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Slot103"):
                opp_val = getattr(value, "ClassesProv_Slot103", None)
                setattr(value, "ClassesProv_Slot103", self)

class Relationship:

    pass
class ClassesProv_Association(Classifier, Relationship):

    def __init__(self, isDerived: bool, ClassesProv_Association: "ClassesProv_Property" = None, ClassesProv_Association149: "ClassesProv_Property" = None, ClassesProv_Association212: set["ClassesProv_Property"] = None, ClassesProv_Association215: set["ClassesProv_Property"] = None, ClassesProv_Association218: set["ClassesProv_Property"] = None):
        self.isDerived = isDerived
        self.ClassesProv_Association = ClassesProv_Association
        self.ClassesProv_Association149 = ClassesProv_Association149
        self.ClassesProv_Association212 = ClassesProv_Association212 if ClassesProv_Association212 is not None else set()
        self.ClassesProv_Association215 = ClassesProv_Association215 if ClassesProv_Association215 is not None else set()
        self.ClassesProv_Association218 = ClassesProv_Association218 if ClassesProv_Association218 is not None else set()
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def ClassesProv_Association(self):
        return self.__ClassesProv_Association

    @ClassesProv_Association.setter
    def ClassesProv_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Association__ClassesProv_Association", None)
        self.__ClassesProv_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property146"):
                opp_val = getattr(old_value, "ClassesProv_Property146", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property146"):
                opp_val = getattr(value, "ClassesProv_Property146", None)
                setattr(value, "ClassesProv_Property146", self)

    @property
    def ClassesProv_Association218(self):
        return self.__ClassesProv_Association218

    @ClassesProv_Association218.setter
    def ClassesProv_Association218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Association__ClassesProv_Association218", None)
        self.__ClassesProv_Association218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property219"):
                    opp_val = getattr(item, "ClassesProv_Property219", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property219"):
                    opp_val = getattr(item, "ClassesProv_Property219", None)
                    
                    setattr(item, "ClassesProv_Property219", self)
                    

    @property
    def ClassesProv_Association212(self):
        return self.__ClassesProv_Association212

    @ClassesProv_Association212.setter
    def ClassesProv_Association212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Association__ClassesProv_Association212", None)
        self.__ClassesProv_Association212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property213"):
                    opp_val = getattr(item, "ClassesProv_Property213", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property213"):
                    opp_val = getattr(item, "ClassesProv_Property213", None)
                    
                    setattr(item, "ClassesProv_Property213", self)
                    

    @property
    def ClassesProv_Association149(self):
        return self.__ClassesProv_Association149

    @ClassesProv_Association149.setter
    def ClassesProv_Association149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Association__ClassesProv_Association149", None)
        self.__ClassesProv_Association149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Property148"):
                opp_val = getattr(old_value, "ClassesProv_Property148", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Property148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Property148"):
                opp_val = getattr(value, "ClassesProv_Property148", None)
                setattr(value, "ClassesProv_Property148", self)

    @property
    def ClassesProv_Association215(self):
        return self.__ClassesProv_Association215

    @ClassesProv_Association215.setter
    def ClassesProv_Association215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Association__ClassesProv_Association215", None)
        self.__ClassesProv_Association215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property216"):
                    opp_val = getattr(item, "ClassesProv_Property216", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property216"):
                    opp_val = getattr(item, "ClassesProv_Property216", None)
                    
                    setattr(item, "ClassesProv_Property216", self)
                    

class ClassesProv_DirectedRelationship(Relationship):

    pass
class NamedElement:

    pass
class ClassesProv_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, ClassesProv_RedefinableElement: "ClassesProv_RedefinableElement" = None, ClassesProv_RedefinableElement104: set["ClassesProv_RedefinableElement"] = None, ClassesProv_RedefinableElement107: set["ClassesProv_Classifier"] = None):
        self.isLeaf = isLeaf
        self.ClassesProv_RedefinableElement = ClassesProv_RedefinableElement
        self.ClassesProv_RedefinableElement104 = ClassesProv_RedefinableElement104 if ClassesProv_RedefinableElement104 is not None else set()
        self.ClassesProv_RedefinableElement107 = ClassesProv_RedefinableElement107 if ClassesProv_RedefinableElement107 is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def ClassesProv_RedefinableElement104(self):
        return self.__ClassesProv_RedefinableElement104

    @ClassesProv_RedefinableElement104.setter
    def ClassesProv_RedefinableElement104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_RedefinableElement__ClassesProv_RedefinableElement104", None)
        self.__ClassesProv_RedefinableElement104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_RedefinableElement"):
                    opp_val = getattr(item, "ClassesProv_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_RedefinableElement"):
                    opp_val = getattr(item, "ClassesProv_RedefinableElement", None)
                    
                    setattr(item, "ClassesProv_RedefinableElement", self)
                    

    @property
    def ClassesProv_RedefinableElement107(self):
        return self.__ClassesProv_RedefinableElement107

    @ClassesProv_RedefinableElement107.setter
    def ClassesProv_RedefinableElement107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_RedefinableElement__ClassesProv_RedefinableElement107", None)
        self.__ClassesProv_RedefinableElement107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Classifier108"):
                    opp_val = getattr(item, "ClassesProv_Classifier108", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Classifier108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Classifier108"):
                    opp_val = getattr(item, "ClassesProv_Classifier108", None)
                    
                    setattr(item, "ClassesProv_Classifier108", self)
                    

    @property
    def ClassesProv_RedefinableElement(self):
        return self.__ClassesProv_RedefinableElement

    @ClassesProv_RedefinableElement.setter
    def ClassesProv_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_RedefinableElement__ClassesProv_RedefinableElement", None)
        self.__ClassesProv_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_RedefinableElement104"):
                opp_val = getattr(old_value, "ClassesProv_RedefinableElement104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_RedefinableElement104"):
                opp_val = getattr(value, "ClassesProv_RedefinableElement104", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_RedefinableElement104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassesProv_TypedElement(NamedElement):

    pass
class ClassesProv_PackageableElement(NamedElement):

    pass
class ClassesProv_Namespace(NamedElement):

    pass
class PackageableElement:

    pass
class ClassesProv_InstanceSpecification(PackageableElement):

    pass
class ClassesProv_ValueSpecification(TypedElement, PackageableElement):

    pass
class ClassesProv_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, ClassesProv_GeneralizationSet: "ClassesProv_Classifier" = None, ClassesProv_GeneralizationSet168: "ClassesProv_Generalization" = None, ClassesProv_GeneralizationSet264: "ClassesProv_Classifier" = None, ClassesProv_GeneralizationSet267: set["ClassesProv_Generalization"] = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.ClassesProv_GeneralizationSet = ClassesProv_GeneralizationSet
        self.ClassesProv_GeneralizationSet168 = ClassesProv_GeneralizationSet168
        self.ClassesProv_GeneralizationSet264 = ClassesProv_GeneralizationSet264
        self.ClassesProv_GeneralizationSet267 = ClassesProv_GeneralizationSet267 if ClassesProv_GeneralizationSet267 is not None else set()
        
    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def ClassesProv_GeneralizationSet264(self):
        return self.__ClassesProv_GeneralizationSet264

    @ClassesProv_GeneralizationSet264.setter
    def ClassesProv_GeneralizationSet264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_GeneralizationSet__ClassesProv_GeneralizationSet264", None)
        self.__ClassesProv_GeneralizationSet264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier265"):
                opp_val = getattr(old_value, "ClassesProv_Classifier265", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Classifier265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier265"):
                opp_val = getattr(value, "ClassesProv_Classifier265", None)
                setattr(value, "ClassesProv_Classifier265", self)

    @property
    def ClassesProv_GeneralizationSet267(self):
        return self.__ClassesProv_GeneralizationSet267

    @ClassesProv_GeneralizationSet267.setter
    def ClassesProv_GeneralizationSet267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_GeneralizationSet__ClassesProv_GeneralizationSet267", None)
        self.__ClassesProv_GeneralizationSet267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Generalization268"):
                    opp_val = getattr(item, "ClassesProv_Generalization268", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Generalization268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Generalization268"):
                    opp_val = getattr(item, "ClassesProv_Generalization268", None)
                    
                    setattr(item, "ClassesProv_Generalization268", self)
                    

    @property
    def ClassesProv_GeneralizationSet(self):
        return self.__ClassesProv_GeneralizationSet

    @ClassesProv_GeneralizationSet.setter
    def ClassesProv_GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_GeneralizationSet__ClassesProv_GeneralizationSet", None)
        self.__ClassesProv_GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier127"):
                opp_val = getattr(old_value, "ClassesProv_Classifier127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier127"):
                opp_val = getattr(value, "ClassesProv_Classifier127", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_GeneralizationSet168(self):
        return self.__ClassesProv_GeneralizationSet168

    @ClassesProv_GeneralizationSet168.setter
    def ClassesProv_GeneralizationSet168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_GeneralizationSet__ClassesProv_GeneralizationSet168", None)
        self.__ClassesProv_GeneralizationSet168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Generalization167"):
                opp_val = getattr(old_value, "ClassesProv_Generalization167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Generalization167"):
                opp_val = getattr(value, "ClassesProv_Generalization167", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Generalization167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassesProv_Type(PackageableElement):

    pass
class Namespace:

    pass
class ClassesProv_Classifier(Type, Namespace, RedefinableElement):

    def __init__(self, isFinalSpecialization: bool, isAbstract: bool, ClassesProv_Classifier: "ClassesProv_InstanceSpecification" = None, ClassesProv_Classifier110: set["ClassesProv_NamedElement"] = None, ClassesProv_Classifier113: set["ClassesProv_Feature"] = None, ClassesProv_Classifier115: set["ClassesProv_Property"] = None, ClassesProv_Classifier118: "ClassesProv_Classifier" = None, ClassesProv_Classifier116: set["ClassesProv_Classifier"] = None, ClassesProv_Classifier121: "ClassesProv_Classifier" = None, ClassesProv_Classifier119: set["ClassesProv_Classifier"] = None, ClassesProv_Classifier123: set["ClassesProv_Generalization"] = None, ClassesProv_Classifier125: set["ClassesProv_Substitution"] = None, ClassesProv_Classifier127: set["ClassesProv_GeneralizationSet"] = None, ClassesProv_Classifier130: "ClassesProv_Feature" = None, ClassesProv_Classifier108: "ClassesProv_RedefinableElement" = None, ClassesProv_Classifier162: "ClassesProv_Generalization" = None, ClassesProv_Classifier165: "ClassesProv_Generalization" = None, ClassesProv_Classifier201: "ClassesProv_Class" = None, ClassesProv_Classifier245: "ClassesProv_Substitution" = None, ClassesProv_Classifier248: "ClassesProv_Substitution" = None, ClassesProv_Classifier265: "ClassesProv_GeneralizationSet" = None, ClassesProv_Classifier251: "ClassesProv_Interface" = None):
        self.isFinalSpecialization = isFinalSpecialization
        self.isAbstract = isAbstract
        self.ClassesProv_Classifier = ClassesProv_Classifier
        self.ClassesProv_Classifier110 = ClassesProv_Classifier110 if ClassesProv_Classifier110 is not None else set()
        self.ClassesProv_Classifier113 = ClassesProv_Classifier113 if ClassesProv_Classifier113 is not None else set()
        self.ClassesProv_Classifier115 = ClassesProv_Classifier115 if ClassesProv_Classifier115 is not None else set()
        self.ClassesProv_Classifier118 = ClassesProv_Classifier118
        self.ClassesProv_Classifier116 = ClassesProv_Classifier116 if ClassesProv_Classifier116 is not None else set()
        self.ClassesProv_Classifier121 = ClassesProv_Classifier121
        self.ClassesProv_Classifier119 = ClassesProv_Classifier119 if ClassesProv_Classifier119 is not None else set()
        self.ClassesProv_Classifier123 = ClassesProv_Classifier123 if ClassesProv_Classifier123 is not None else set()
        self.ClassesProv_Classifier125 = ClassesProv_Classifier125 if ClassesProv_Classifier125 is not None else set()
        self.ClassesProv_Classifier127 = ClassesProv_Classifier127 if ClassesProv_Classifier127 is not None else set()
        self.ClassesProv_Classifier130 = ClassesProv_Classifier130
        self.ClassesProv_Classifier108 = ClassesProv_Classifier108
        self.ClassesProv_Classifier162 = ClassesProv_Classifier162
        self.ClassesProv_Classifier165 = ClassesProv_Classifier165
        self.ClassesProv_Classifier201 = ClassesProv_Classifier201
        self.ClassesProv_Classifier245 = ClassesProv_Classifier245
        self.ClassesProv_Classifier248 = ClassesProv_Classifier248
        self.ClassesProv_Classifier265 = ClassesProv_Classifier265
        self.ClassesProv_Classifier251 = ClassesProv_Classifier251
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isFinalSpecialization(self) -> bool:
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: bool):
        self.__isFinalSpecialization = isFinalSpecialization

    @property
    def ClassesProv_Classifier125(self):
        return self.__ClassesProv_Classifier125

    @ClassesProv_Classifier125.setter
    def ClassesProv_Classifier125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier125", None)
        self.__ClassesProv_Classifier125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Substitution"):
                    opp_val = getattr(item, "ClassesProv_Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Substitution"):
                    opp_val = getattr(item, "ClassesProv_Substitution", None)
                    
                    setattr(item, "ClassesProv_Substitution", self)
                    

    @property
    def ClassesProv_Classifier245(self):
        return self.__ClassesProv_Classifier245

    @ClassesProv_Classifier245.setter
    def ClassesProv_Classifier245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier245", None)
        self.__ClassesProv_Classifier245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Substitution244"):
                opp_val = getattr(old_value, "ClassesProv_Substitution244", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Substitution244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Substitution244"):
                opp_val = getattr(value, "ClassesProv_Substitution244", None)
                setattr(value, "ClassesProv_Substitution244", self)

    @property
    def ClassesProv_Classifier118(self):
        return self.__ClassesProv_Classifier118

    @ClassesProv_Classifier118.setter
    def ClassesProv_Classifier118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier118", None)
        self.__ClassesProv_Classifier118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier116"):
                opp_val = getattr(old_value, "ClassesProv_Classifier116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier116"):
                opp_val = getattr(value, "ClassesProv_Classifier116", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier116(self):
        return self.__ClassesProv_Classifier116

    @ClassesProv_Classifier116.setter
    def ClassesProv_Classifier116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier116", None)
        self.__ClassesProv_Classifier116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Classifier118"):
                    opp_val = getattr(item, "ClassesProv_Classifier118", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Classifier118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Classifier118"):
                    opp_val = getattr(item, "ClassesProv_Classifier118", None)
                    
                    setattr(item, "ClassesProv_Classifier118", self)
                    

    @property
    def ClassesProv_Classifier265(self):
        return self.__ClassesProv_Classifier265

    @ClassesProv_Classifier265.setter
    def ClassesProv_Classifier265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier265", None)
        self.__ClassesProv_Classifier265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_GeneralizationSet264"):
                opp_val = getattr(old_value, "ClassesProv_GeneralizationSet264", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_GeneralizationSet264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_GeneralizationSet264"):
                opp_val = getattr(value, "ClassesProv_GeneralizationSet264", None)
                setattr(value, "ClassesProv_GeneralizationSet264", self)

    @property
    def ClassesProv_Classifier165(self):
        return self.__ClassesProv_Classifier165

    @ClassesProv_Classifier165.setter
    def ClassesProv_Classifier165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier165", None)
        self.__ClassesProv_Classifier165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Generalization164"):
                opp_val = getattr(old_value, "ClassesProv_Generalization164", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Generalization164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Generalization164"):
                opp_val = getattr(value, "ClassesProv_Generalization164", None)
                setattr(value, "ClassesProv_Generalization164", self)

    @property
    def ClassesProv_Classifier119(self):
        return self.__ClassesProv_Classifier119

    @ClassesProv_Classifier119.setter
    def ClassesProv_Classifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier119", None)
        self.__ClassesProv_Classifier119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Classifier121"):
                    opp_val = getattr(item, "ClassesProv_Classifier121", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Classifier121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Classifier121"):
                    opp_val = getattr(item, "ClassesProv_Classifier121", None)
                    
                    setattr(item, "ClassesProv_Classifier121", self)
                    

    @property
    def ClassesProv_Classifier123(self):
        return self.__ClassesProv_Classifier123

    @ClassesProv_Classifier123.setter
    def ClassesProv_Classifier123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier123", None)
        self.__ClassesProv_Classifier123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Generalization"):
                    opp_val = getattr(item, "ClassesProv_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Generalization"):
                    opp_val = getattr(item, "ClassesProv_Generalization", None)
                    
                    setattr(item, "ClassesProv_Generalization", self)
                    

    @property
    def ClassesProv_Classifier251(self):
        return self.__ClassesProv_Classifier251

    @ClassesProv_Classifier251.setter
    def ClassesProv_Classifier251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier251", None)
        self.__ClassesProv_Classifier251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Interface250"):
                opp_val = getattr(old_value, "ClassesProv_Interface250", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Interface250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Interface250"):
                opp_val = getattr(value, "ClassesProv_Interface250", None)
                setattr(value, "ClassesProv_Interface250", self)

    @property
    def ClassesProv_Classifier(self):
        return self.__ClassesProv_Classifier

    @ClassesProv_Classifier.setter
    def ClassesProv_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier", None)
        self.__ClassesProv_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_InstanceSpecification86"):
                opp_val = getattr(old_value, "ClassesProv_InstanceSpecification86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_InstanceSpecification86"):
                opp_val = getattr(value, "ClassesProv_InstanceSpecification86", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_InstanceSpecification86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier162(self):
        return self.__ClassesProv_Classifier162

    @ClassesProv_Classifier162.setter
    def ClassesProv_Classifier162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier162", None)
        self.__ClassesProv_Classifier162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Generalization161"):
                opp_val = getattr(old_value, "ClassesProv_Generalization161", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Generalization161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Generalization161"):
                opp_val = getattr(value, "ClassesProv_Generalization161", None)
                setattr(value, "ClassesProv_Generalization161", self)

    @property
    def ClassesProv_Classifier113(self):
        return self.__ClassesProv_Classifier113

    @ClassesProv_Classifier113.setter
    def ClassesProv_Classifier113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier113", None)
        self.__ClassesProv_Classifier113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Feature"):
                    opp_val = getattr(item, "ClassesProv_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Feature"):
                    opp_val = getattr(item, "ClassesProv_Feature", None)
                    
                    setattr(item, "ClassesProv_Feature", self)
                    

    @property
    def ClassesProv_Classifier127(self):
        return self.__ClassesProv_Classifier127

    @ClassesProv_Classifier127.setter
    def ClassesProv_Classifier127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier127", None)
        self.__ClassesProv_Classifier127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_GeneralizationSet"):
                    opp_val = getattr(item, "ClassesProv_GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_GeneralizationSet"):
                    opp_val = getattr(item, "ClassesProv_GeneralizationSet", None)
                    
                    setattr(item, "ClassesProv_GeneralizationSet", self)
                    

    @property
    def ClassesProv_Classifier130(self):
        return self.__ClassesProv_Classifier130

    @ClassesProv_Classifier130.setter
    def ClassesProv_Classifier130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier130", None)
        self.__ClassesProv_Classifier130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Feature129"):
                opp_val = getattr(old_value, "ClassesProv_Feature129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Feature129"):
                opp_val = getattr(value, "ClassesProv_Feature129", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Feature129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier110(self):
        return self.__ClassesProv_Classifier110

    @ClassesProv_Classifier110.setter
    def ClassesProv_Classifier110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier110", None)
        self.__ClassesProv_Classifier110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_NamedElement111"):
                    opp_val = getattr(item, "ClassesProv_NamedElement111", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_NamedElement111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_NamedElement111"):
                    opp_val = getattr(item, "ClassesProv_NamedElement111", None)
                    
                    setattr(item, "ClassesProv_NamedElement111", self)
                    

    @property
    def ClassesProv_Classifier115(self):
        return self.__ClassesProv_Classifier115

    @ClassesProv_Classifier115.setter
    def ClassesProv_Classifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier115", None)
        self.__ClassesProv_Classifier115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Property"):
                    opp_val = getattr(item, "ClassesProv_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Property"):
                    opp_val = getattr(item, "ClassesProv_Property", None)
                    
                    setattr(item, "ClassesProv_Property", self)
                    

    @property
    def ClassesProv_Classifier108(self):
        return self.__ClassesProv_Classifier108

    @ClassesProv_Classifier108.setter
    def ClassesProv_Classifier108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier108", None)
        self.__ClassesProv_Classifier108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_RedefinableElement107"):
                opp_val = getattr(old_value, "ClassesProv_RedefinableElement107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_RedefinableElement107"):
                opp_val = getattr(value, "ClassesProv_RedefinableElement107", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_RedefinableElement107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier201(self):
        return self.__ClassesProv_Classifier201

    @ClassesProv_Classifier201.setter
    def ClassesProv_Classifier201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier201", None)
        self.__ClassesProv_Classifier201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Class200"):
                opp_val = getattr(old_value, "ClassesProv_Class200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Class200"):
                opp_val = getattr(value, "ClassesProv_Class200", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Class200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier121(self):
        return self.__ClassesProv_Classifier121

    @ClassesProv_Classifier121.setter
    def ClassesProv_Classifier121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier121", None)
        self.__ClassesProv_Classifier121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier119"):
                opp_val = getattr(old_value, "ClassesProv_Classifier119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier119"):
                opp_val = getattr(value, "ClassesProv_Classifier119", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Classifier248(self):
        return self.__ClassesProv_Classifier248

    @ClassesProv_Classifier248.setter
    def ClassesProv_Classifier248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Classifier__ClassesProv_Classifier248", None)
        self.__ClassesProv_Classifier248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Substitution247"):
                opp_val = getattr(old_value, "ClassesProv_Substitution247", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Substitution247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Substitution247"):
                opp_val = getattr(value, "ClassesProv_Substitution247", None)
                setattr(value, "ClassesProv_Substitution247", self)

class ClassesProv_BehavioralFeature(Namespace, Feature):

    pass
class ClassesProv_Package(PackageableElement, Namespace):

    def __init__(self, URI: str, ClassesProv_Package: "ClassesProv_PackageImport" = None, ClassesProv_Package35: "ClassesProv_Package" = None, ClassesProv_Package33: set["ClassesProv_Package"] = None, ClassesProv_Package38: "ClassesProv_Package" = None, ClassesProv_Package36: "ClassesProv_Package" = None, ClassesProv_Package40: set["ClassesProv_PackageableElement"] = None, ClassesProv_Package74: "ClassesProv_Type" = None, ClassesProv_Package43: set["ClassesProv_Type"] = None, ClassesProv_Package45: set["ClassesProv_PackageMerge"] = None, ClassesProv_Package232: "ClassesProv_PackageMerge" = None, ClassesProv_Package235: "ClassesProv_PackageMerge" = None):
        self.URI = URI
        self.ClassesProv_Package = ClassesProv_Package
        self.ClassesProv_Package35 = ClassesProv_Package35
        self.ClassesProv_Package33 = ClassesProv_Package33 if ClassesProv_Package33 is not None else set()
        self.ClassesProv_Package38 = ClassesProv_Package38
        self.ClassesProv_Package36 = ClassesProv_Package36
        self.ClassesProv_Package40 = ClassesProv_Package40 if ClassesProv_Package40 is not None else set()
        self.ClassesProv_Package74 = ClassesProv_Package74
        self.ClassesProv_Package43 = ClassesProv_Package43 if ClassesProv_Package43 is not None else set()
        self.ClassesProv_Package45 = ClassesProv_Package45 if ClassesProv_Package45 is not None else set()
        self.ClassesProv_Package232 = ClassesProv_Package232
        self.ClassesProv_Package235 = ClassesProv_Package235
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def ClassesProv_Package38(self):
        return self.__ClassesProv_Package38

    @ClassesProv_Package38.setter
    def ClassesProv_Package38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package38", None)
        self.__ClassesProv_Package38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Package36"):
                opp_val = getattr(old_value, "ClassesProv_Package36", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Package36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Package36"):
                opp_val = getattr(value, "ClassesProv_Package36", None)
                setattr(value, "ClassesProv_Package36", self)

    @property
    def ClassesProv_Package74(self):
        return self.__ClassesProv_Package74

    @ClassesProv_Package74.setter
    def ClassesProv_Package74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package74", None)
        self.__ClassesProv_Package74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Type73"):
                opp_val = getattr(old_value, "ClassesProv_Type73", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Type73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Type73"):
                opp_val = getattr(value, "ClassesProv_Type73", None)
                setattr(value, "ClassesProv_Type73", self)

    @property
    def ClassesProv_Package36(self):
        return self.__ClassesProv_Package36

    @ClassesProv_Package36.setter
    def ClassesProv_Package36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package36", None)
        self.__ClassesProv_Package36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Package38"):
                opp_val = getattr(old_value, "ClassesProv_Package38", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Package38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Package38"):
                opp_val = getattr(value, "ClassesProv_Package38", None)
                setattr(value, "ClassesProv_Package38", self)

    @property
    def ClassesProv_Package33(self):
        return self.__ClassesProv_Package33

    @ClassesProv_Package33.setter
    def ClassesProv_Package33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package33", None)
        self.__ClassesProv_Package33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Package35"):
                    opp_val = getattr(item, "ClassesProv_Package35", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Package35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Package35"):
                    opp_val = getattr(item, "ClassesProv_Package35", None)
                    
                    setattr(item, "ClassesProv_Package35", self)
                    

    @property
    def ClassesProv_Package45(self):
        return self.__ClassesProv_Package45

    @ClassesProv_Package45.setter
    def ClassesProv_Package45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package45", None)
        self.__ClassesProv_Package45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_PackageMerge"):
                    opp_val = getattr(item, "ClassesProv_PackageMerge", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_PackageMerge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_PackageMerge"):
                    opp_val = getattr(item, "ClassesProv_PackageMerge", None)
                    
                    setattr(item, "ClassesProv_PackageMerge", self)
                    

    @property
    def ClassesProv_Package232(self):
        return self.__ClassesProv_Package232

    @ClassesProv_Package232.setter
    def ClassesProv_Package232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package232", None)
        self.__ClassesProv_Package232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_PackageMerge231"):
                opp_val = getattr(old_value, "ClassesProv_PackageMerge231", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_PackageMerge231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_PackageMerge231"):
                opp_val = getattr(value, "ClassesProv_PackageMerge231", None)
                setattr(value, "ClassesProv_PackageMerge231", self)

    @property
    def ClassesProv_Package35(self):
        return self.__ClassesProv_Package35

    @ClassesProv_Package35.setter
    def ClassesProv_Package35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package35", None)
        self.__ClassesProv_Package35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Package33"):
                opp_val = getattr(old_value, "ClassesProv_Package33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Package33"):
                opp_val = getattr(value, "ClassesProv_Package33", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Package33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Package40(self):
        return self.__ClassesProv_Package40

    @ClassesProv_Package40.setter
    def ClassesProv_Package40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package40", None)
        self.__ClassesProv_Package40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_PackageableElement41"):
                    opp_val = getattr(item, "ClassesProv_PackageableElement41", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_PackageableElement41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_PackageableElement41"):
                    opp_val = getattr(item, "ClassesProv_PackageableElement41", None)
                    
                    setattr(item, "ClassesProv_PackageableElement41", self)
                    

    @property
    def ClassesProv_Package235(self):
        return self.__ClassesProv_Package235

    @ClassesProv_Package235.setter
    def ClassesProv_Package235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package235", None)
        self.__ClassesProv_Package235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_PackageMerge234"):
                opp_val = getattr(old_value, "ClassesProv_PackageMerge234", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_PackageMerge234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_PackageMerge234"):
                opp_val = getattr(value, "ClassesProv_PackageMerge234", None)
                setattr(value, "ClassesProv_PackageMerge234", self)

    @property
    def ClassesProv_Package(self):
        return self.__ClassesProv_Package

    @ClassesProv_Package.setter
    def ClassesProv_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package", None)
        self.__ClassesProv_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_PackageImport29"):
                opp_val = getattr(old_value, "ClassesProv_PackageImport29", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_PackageImport29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_PackageImport29"):
                opp_val = getattr(value, "ClassesProv_PackageImport29", None)
                setattr(value, "ClassesProv_PackageImport29", self)

    @property
    def ClassesProv_Package43(self):
        return self.__ClassesProv_Package43

    @ClassesProv_Package43.setter
    def ClassesProv_Package43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Package__ClassesProv_Package43", None)
        self.__ClassesProv_Package43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Type"):
                    opp_val = getattr(item, "ClassesProv_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Type"):
                    opp_val = getattr(item, "ClassesProv_Type", None)
                    
                    setattr(item, "ClassesProv_Type", self)
                    

class DirectedRelationship:

    pass
class ClassesProv_Dependency(DirectedRelationship, PackageableElement):

    pass
class ClassesProv_PackageMerge(DirectedRelationship):

    pass
class ClassesProv_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, ClassesProv_Generalization: "ClassesProv_Classifier" = None, ClassesProv_Generalization161: "ClassesProv_Classifier" = None, ClassesProv_Generalization164: "ClassesProv_Classifier" = None, ClassesProv_Generalization167: set["ClassesProv_GeneralizationSet"] = None, ClassesProv_Generalization268: "ClassesProv_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.ClassesProv_Generalization = ClassesProv_Generalization
        self.ClassesProv_Generalization161 = ClassesProv_Generalization161
        self.ClassesProv_Generalization164 = ClassesProv_Generalization164
        self.ClassesProv_Generalization167 = ClassesProv_Generalization167 if ClassesProv_Generalization167 is not None else set()
        self.ClassesProv_Generalization268 = ClassesProv_Generalization268
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def ClassesProv_Generalization161(self):
        return self.__ClassesProv_Generalization161

    @ClassesProv_Generalization161.setter
    def ClassesProv_Generalization161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Generalization__ClassesProv_Generalization161", None)
        self.__ClassesProv_Generalization161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier162"):
                opp_val = getattr(old_value, "ClassesProv_Classifier162", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Classifier162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier162"):
                opp_val = getattr(value, "ClassesProv_Classifier162", None)
                setattr(value, "ClassesProv_Classifier162", self)

    @property
    def ClassesProv_Generalization(self):
        return self.__ClassesProv_Generalization

    @ClassesProv_Generalization.setter
    def ClassesProv_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Generalization__ClassesProv_Generalization", None)
        self.__ClassesProv_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier123"):
                opp_val = getattr(old_value, "ClassesProv_Classifier123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier123"):
                opp_val = getattr(value, "ClassesProv_Classifier123", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Generalization268(self):
        return self.__ClassesProv_Generalization268

    @ClassesProv_Generalization268.setter
    def ClassesProv_Generalization268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Generalization__ClassesProv_Generalization268", None)
        self.__ClassesProv_Generalization268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_GeneralizationSet267"):
                opp_val = getattr(old_value, "ClassesProv_GeneralizationSet267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_GeneralizationSet267"):
                opp_val = getattr(value, "ClassesProv_GeneralizationSet267", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_GeneralizationSet267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_Generalization164(self):
        return self.__ClassesProv_Generalization164

    @ClassesProv_Generalization164.setter
    def ClassesProv_Generalization164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Generalization__ClassesProv_Generalization164", None)
        self.__ClassesProv_Generalization164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier165"):
                opp_val = getattr(old_value, "ClassesProv_Classifier165", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Classifier165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier165"):
                opp_val = getattr(value, "ClassesProv_Classifier165", None)
                setattr(value, "ClassesProv_Classifier165", self)

    @property
    def ClassesProv_Generalization167(self):
        return self.__ClassesProv_Generalization167

    @ClassesProv_Generalization167.setter
    def ClassesProv_Generalization167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_Generalization__ClassesProv_Generalization167", None)
        self.__ClassesProv_Generalization167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_GeneralizationSet168"):
                    opp_val = getattr(item, "ClassesProv_GeneralizationSet168", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_GeneralizationSet168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_GeneralizationSet168"):
                    opp_val = getattr(item, "ClassesProv_GeneralizationSet168", None)
                    
                    setattr(item, "ClassesProv_GeneralizationSet168", self)
                    

class ClassesProv_Constraint(PackageableElement):

    pass
class ClassesProv_PackageImport(DirectedRelationship):

    pass
class ClassesProv_ElementImport(DirectedRelationship):

    def __init__(self, alias: str, ClassesProv_ElementImport: "ClassesProv_Namespace" = None, ClassesProv_ElementImport23: "ClassesProv_PackageableElement" = None, ClassesProv_ElementImport26: "ClassesProv_Namespace" = None):
        self.alias = alias
        self.ClassesProv_ElementImport = ClassesProv_ElementImport
        self.ClassesProv_ElementImport23 = ClassesProv_ElementImport23
        self.ClassesProv_ElementImport26 = ClassesProv_ElementImport26
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def ClassesProv_ElementImport26(self):
        return self.__ClassesProv_ElementImport26

    @ClassesProv_ElementImport26.setter
    def ClassesProv_ElementImport26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_ElementImport__ClassesProv_ElementImport26", None)
        self.__ClassesProv_ElementImport26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Namespace27"):
                opp_val = getattr(old_value, "ClassesProv_Namespace27", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Namespace27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Namespace27"):
                opp_val = getattr(value, "ClassesProv_Namespace27", None)
                setattr(value, "ClassesProv_Namespace27", self)

    @property
    def ClassesProv_ElementImport23(self):
        return self.__ClassesProv_ElementImport23

    @ClassesProv_ElementImport23.setter
    def ClassesProv_ElementImport23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_ElementImport__ClassesProv_ElementImport23", None)
        self.__ClassesProv_ElementImport23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_PackageableElement24"):
                opp_val = getattr(old_value, "ClassesProv_PackageableElement24", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_PackageableElement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_PackageableElement24"):
                opp_val = getattr(value, "ClassesProv_PackageableElement24", None)
                setattr(value, "ClassesProv_PackageableElement24", self)

    @property
    def ClassesProv_ElementImport(self):
        return self.__ClassesProv_ElementImport

    @ClassesProv_ElementImport.setter
    def ClassesProv_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_ElementImport__ClassesProv_ElementImport", None)
        self.__ClassesProv_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Namespace17"):
                opp_val = getattr(old_value, "ClassesProv_Namespace17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Namespace17"):
                opp_val = getattr(value, "ClassesProv_Namespace17", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Namespace17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class ClassesProv_Relationship(Element):

    pass
class ClassesProv_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, upper: int, lower: int, ClassesProv_MultiplicityElement: "ClassesProv_ValueSpecification" = None, ClassesProv_MultiplicityElement55: "ClassesProv_ValueSpecification" = None, ClassesProv_MultiplicityElement59: "ClassesProv_ValueSpecification" = None, ClassesProv_MultiplicityElement62: "ClassesProv_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.ClassesProv_MultiplicityElement = ClassesProv_MultiplicityElement
        self.ClassesProv_MultiplicityElement55 = ClassesProv_MultiplicityElement55
        self.ClassesProv_MultiplicityElement59 = ClassesProv_MultiplicityElement59
        self.ClassesProv_MultiplicityElement62 = ClassesProv_MultiplicityElement62
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def ClassesProv_MultiplicityElement59(self):
        return self.__ClassesProv_MultiplicityElement59

    @ClassesProv_MultiplicityElement59.setter
    def ClassesProv_MultiplicityElement59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_MultiplicityElement__ClassesProv_MultiplicityElement59", None)
        self.__ClassesProv_MultiplicityElement59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification58"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification58", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification58"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification58", None)
                setattr(value, "ClassesProv_ValueSpecification58", self)

    @property
    def ClassesProv_MultiplicityElement(self):
        return self.__ClassesProv_MultiplicityElement

    @ClassesProv_MultiplicityElement.setter
    def ClassesProv_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_MultiplicityElement__ClassesProv_MultiplicityElement", None)
        self.__ClassesProv_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification", None)
                setattr(value, "ClassesProv_ValueSpecification", self)

    @property
    def ClassesProv_MultiplicityElement62(self):
        return self.__ClassesProv_MultiplicityElement62

    @ClassesProv_MultiplicityElement62.setter
    def ClassesProv_MultiplicityElement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_MultiplicityElement__ClassesProv_MultiplicityElement62", None)
        self.__ClassesProv_MultiplicityElement62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification61"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification61", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification61"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification61", None)
                setattr(value, "ClassesProv_ValueSpecification61", self)

    @property
    def ClassesProv_MultiplicityElement55(self):
        return self.__ClassesProv_MultiplicityElement55

    @ClassesProv_MultiplicityElement55.setter
    def ClassesProv_MultiplicityElement55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_MultiplicityElement__ClassesProv_MultiplicityElement55", None)
        self.__ClassesProv_MultiplicityElement55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_ValueSpecification56"):
                opp_val = getattr(old_value, "ClassesProv_ValueSpecification56", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_ValueSpecification56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_ValueSpecification56"):
                opp_val = getattr(value, "ClassesProv_ValueSpecification56", None)
                setattr(value, "ClassesProv_ValueSpecification56", self)

class ClassesProv_Slot(Element):

    pass
class ClassesProv_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, ClassesProv_NamedElement15: "ClassesProv_Namespace" = None, ClassesProv_NamedElement: "ClassesProv_Namespace" = None, ClassesProv_NamedElement7: set["ClassesProv_Dependency"] = None, ClassesProv_NamedElement12: "ClassesProv_Namespace" = None, ClassesProv_NamedElement111: "ClassesProv_Classifier" = None, ClassesProv_NamedElement238: "ClassesProv_Dependency" = None, ClassesProv_NamedElement241: "ClassesProv_Dependency" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.ClassesProv_NamedElement15 = ClassesProv_NamedElement15
        self.ClassesProv_NamedElement = ClassesProv_NamedElement
        self.ClassesProv_NamedElement7 = ClassesProv_NamedElement7 if ClassesProv_NamedElement7 is not None else set()
        self.ClassesProv_NamedElement12 = ClassesProv_NamedElement12
        self.ClassesProv_NamedElement111 = ClassesProv_NamedElement111
        self.ClassesProv_NamedElement238 = ClassesProv_NamedElement238
        self.ClassesProv_NamedElement241 = ClassesProv_NamedElement241
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def ClassesProv_NamedElement12(self):
        return self.__ClassesProv_NamedElement12

    @ClassesProv_NamedElement12.setter
    def ClassesProv_NamedElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement12", None)
        self.__ClassesProv_NamedElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Namespace11"):
                opp_val = getattr(old_value, "ClassesProv_Namespace11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Namespace11"):
                opp_val = getattr(value, "ClassesProv_Namespace11", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Namespace11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_NamedElement111(self):
        return self.__ClassesProv_NamedElement111

    @ClassesProv_NamedElement111.setter
    def ClassesProv_NamedElement111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement111", None)
        self.__ClassesProv_NamedElement111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Classifier110"):
                opp_val = getattr(old_value, "ClassesProv_Classifier110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Classifier110"):
                opp_val = getattr(value, "ClassesProv_Classifier110", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Classifier110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_NamedElement238(self):
        return self.__ClassesProv_NamedElement238

    @ClassesProv_NamedElement238.setter
    def ClassesProv_NamedElement238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement238", None)
        self.__ClassesProv_NamedElement238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Dependency237"):
                opp_val = getattr(old_value, "ClassesProv_Dependency237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Dependency237"):
                opp_val = getattr(value, "ClassesProv_Dependency237", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Dependency237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_NamedElement241(self):
        return self.__ClassesProv_NamedElement241

    @ClassesProv_NamedElement241.setter
    def ClassesProv_NamedElement241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement241", None)
        self.__ClassesProv_NamedElement241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Dependency240"):
                opp_val = getattr(old_value, "ClassesProv_Dependency240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Dependency240"):
                opp_val = getattr(value, "ClassesProv_Dependency240", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Dependency240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_NamedElement(self):
        return self.__ClassesProv_NamedElement

    @ClassesProv_NamedElement.setter
    def ClassesProv_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement", None)
        self.__ClassesProv_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Namespace"):
                opp_val = getattr(old_value, "ClassesProv_Namespace", None)
                if opp_val == self:
                    setattr(old_value, "ClassesProv_Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Namespace"):
                opp_val = getattr(value, "ClassesProv_Namespace", None)
                setattr(value, "ClassesProv_Namespace", self)

    @property
    def ClassesProv_NamedElement15(self):
        return self.__ClassesProv_NamedElement15

    @ClassesProv_NamedElement15.setter
    def ClassesProv_NamedElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement15", None)
        self.__ClassesProv_NamedElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassesProv_Namespace14"):
                opp_val = getattr(old_value, "ClassesProv_Namespace14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassesProv_Namespace14"):
                opp_val = getattr(value, "ClassesProv_Namespace14", None)
                if opp_val is None:
                    setattr(value, "ClassesProv_Namespace14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassesProv_NamedElement7(self):
        return self.__ClassesProv_NamedElement7

    @ClassesProv_NamedElement7.setter
    def ClassesProv_NamedElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassesProv_NamedElement__ClassesProv_NamedElement7", None)
        self.__ClassesProv_NamedElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassesProv_Dependency"):
                    opp_val = getattr(item, "ClassesProv_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassesProv_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassesProv_Dependency"):
                    opp_val = getattr(item, "ClassesProv_Dependency", None)
                    
                    setattr(item, "ClassesProv_Dependency", self)
                    

class ClassesProv_Element(ABC):

    pass
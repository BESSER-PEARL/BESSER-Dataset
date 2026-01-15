from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MappingCardinality(Enum):
    OneToOne = "OneToOne"
    NToOne = "NToOne"
    OneToN = "OneToN"
class ResolveTraceCardinality(Enum):
    ONE_ONE = "ONE_ONE"
    ZERO_OR_ONE = "ZERO_OR_ONE"
    MANY = "MANY"
class BinaryOp(Enum):
    EQUAL = "EQUAL"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"


############################################
# Definition of Classes
############################################

class frontend_core_PutTraceParameter:

    pass
class PutTraceParameter:

    pass
class frontend_core_TraceCompareExpression:

    def __init__(self, multivaluedTag: bool, frontend_core_TraceCompareExpression: "TraceElement" = None, frontend_core_TraceCompareExpression324: "Expression" = None):
        self.multivaluedTag = multivaluedTag
        self.frontend_core_TraceCompareExpression = frontend_core_TraceCompareExpression
        self.frontend_core_TraceCompareExpression324 = frontend_core_TraceCompareExpression324
        
    @property
    def multivaluedTag(self) -> bool:
        return self.__multivaluedTag

    @multivaluedTag.setter
    def multivaluedTag(self, multivaluedTag: bool):
        self.__multivaluedTag = multivaluedTag

    @property
    def frontend_core_TraceCompareExpression(self):
        return self.__frontend_core_TraceCompareExpression

    @frontend_core_TraceCompareExpression.setter
    def frontend_core_TraceCompareExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_TraceCompareExpression__frontend_core_TraceCompareExpression", None)
        self.__frontend_core_TraceCompareExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceElement322"):
                opp_val = getattr(old_value, "TraceElement322", None)
                if opp_val == self:
                    setattr(old_value, "TraceElement322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceElement322"):
                opp_val = getattr(value, "TraceElement322", None)
                setattr(value, "TraceElement322", self)

    @property
    def frontend_core_TraceCompareExpression324(self):
        return self.__frontend_core_TraceCompareExpression324

    @frontend_core_TraceCompareExpression324.setter
    def frontend_core_TraceCompareExpression324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_TraceCompareExpression__frontend_core_TraceCompareExpression324", None)
        self.__frontend_core_TraceCompareExpression324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression325"):
                opp_val = getattr(old_value, "Expression325", None)
                if opp_val == self:
                    setattr(old_value, "Expression325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression325"):
                opp_val = getattr(value, "Expression325", None)
                setattr(value, "Expression325", self)

class TraceCompareExpression:

    pass
class InlineFeature:

    pass
class frontend_core_InlineAttribute(InlineFeature):

    pass
class frontend_core_InlineReference(InlineFeature):

    pass
class InlineClass:

    pass
class core_ModuleDefinition:

    pass
class TraceElement:

    pass
class frontend_core_TypedWithClass(ABC):

    pass
class TraceDefinition:

    pass
class core_ImplicitlyAnnotableElement:

    pass
class core_TypeExpression:

    pass
class frontend_core_ClassUse(core_TypeExpression, core_ImplicitlyAnnotableElement):

    def __init__(self, className: str, strictType: bool, frontend_core_ClassUse: "RepresentModel" = None):
        self.className = className
        self.strictType = strictType
        self.frontend_core_ClassUse = frontend_core_ClassUse
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def strictType(self) -> bool:
        return self.__strictType

    @strictType.setter
    def strictType(self, strictType: bool):
        self.__strictType = strictType

    @property
    def frontend_core_ClassUse(self):
        return self.__frontend_core_ClassUse

    @frontend_core_ClassUse.setter
    def frontend_core_ClassUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_ClassUse__frontend_core_ClassUse", None)
        self.__frontend_core_ClassUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentModel304"):
                opp_val = getattr(old_value, "RepresentModel304", None)
                if opp_val == self:
                    setattr(old_value, "RepresentModel304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentModel304"):
                opp_val = getattr(value, "RepresentModel304", None)
                setattr(value, "RepresentModel304", self)

class frontend_core_TypeExpression(ABC):

    pass
class frontend_core_IfBranch:

    pass
class IfBranch:

    pass
class ClosureParameter:

    pass
class KeywordParameter:

    pass
class frontend_core_KeywordParameter:

    def __init__(self, keyword: str, frontend_core_KeywordParameter: "Expression" = None):
        self.keyword = keyword
        self.frontend_core_KeywordParameter = frontend_core_KeywordParameter
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def frontend_core_KeywordParameter(self):
        return self.__frontend_core_KeywordParameter

    @frontend_core_KeywordParameter.setter
    def frontend_core_KeywordParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_KeywordParameter__frontend_core_KeywordParameter", None)
        self.__frontend_core_KeywordParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression276"):
                opp_val = getattr(old_value, "Expression276", None)
                if opp_val == self:
                    setattr(old_value, "Expression276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression276"):
                opp_val = getattr(value, "Expression276", None)
                setattr(value, "Expression276", self)

class core_Expression:

    pass
class frontend_core_Variable(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class frontend_core_RequireParameter(ABC):

    def __init__(self, formalParameterName: str):
        self.formalParameterName = formalParameterName
        
    @property
    def formalParameterName(self) -> str:
        return self.__formalParameterName

    @formalParameterName.setter
    def formalParameterName(self, formalParameterName: str):
        self.__formalParameterName = formalParameterName

class RequireParameter:

    pass
class frontend_core_RequireModelParameter(RequireParameter):

    pass
class core_DefinitionParameter:

    pass
class AnnotationParameter:

    pass
class frontend_core_GenericAnnotation:

    def __init__(self, name: str, frontend_core_GenericAnnotation: set["AnnotationParameter"] = None):
        self.name = name
        self.frontend_core_GenericAnnotation = frontend_core_GenericAnnotation if frontend_core_GenericAnnotation is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frontend_core_GenericAnnotation(self):
        return self.__frontend_core_GenericAnnotation

    @frontend_core_GenericAnnotation.setter
    def frontend_core_GenericAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_GenericAnnotation__frontend_core_GenericAnnotation", None)
        self.__frontend_core_GenericAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnnotationParameter"):
                    opp_val = getattr(item, "AnnotationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "AnnotationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnnotationParameter"):
                    opp_val = getattr(item, "AnnotationParameter", None)
                    
                    setattr(item, "AnnotationParameter", self)
                    

class RequireDeclaration:

    pass
class InlineModel:

    pass
class ImportedModel:

    pass
class ModuleDefinition:

    pass
class frontend_core_TraceInterface(ModuleDefinition):

    pass
class frontend_core_TransformationDefinition(ModuleDefinition):

    pass
class frontend_core_AnnotationParameter(ABC):

    pass
class AnnotableElement:

    pass
class frontend_core_RepresentModel(AnnotableElement):

    pass
class frontend_core_Annotation(ABC):

    pass
class SingleAnnotation:

    pass
class frontend_core_PotencyAnnotation(SingleAnnotation):

    def __init__(self, value: str, SingleAnnotation: "frontend_core_ImplicitlyAnnotableElement"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class core_AnnotableElement:

    pass
class DefinitionParameter:

    pass
class frontend_core_ModuleParameter(DefinitionParameter):

    pass
class frontend_core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class frontend_core_LocatedElement(ABC):

    def __init__(self, row: int, column: int, file: str):
        self.row = row
        self.column = column
        self.file = file
        
    @property
    def row(self) -> int:
        return self.__row

    @row.setter
    def row(self, row: int):
        self.__row = row

    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class frontend_core_ImplicitlyAnnotableElement:

    pass
class Annotation:

    pass
class frontend_core_MetamodelModelAnnotation(Annotation):

    def __init__(self, metamodel: str, core: "frontend_core_AnnotableElement", Annotation247: "frontend_core_TransformationDefinition"):
        self.metamodel = metamodel
        
    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

class frontend_core_SingleAnnotation(Annotation):

    pass
class frontend_core_OptimizationsAnnotation(Annotation):

    def __init__(self, enabled: bool, core: "frontend_core_AnnotableElement", Annotation247: "frontend_core_TransformationDefinition"):
        self.enabled = enabled
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

class frontend_core_AnnotableElement(ABC):

    pass
class tao_Assignment:

    pass
class ObjectSourceVariable:

    pass
class SourceExpression:

    pass
class frontend_tao_WithOptionalVariableExpression(SourceExpression):

    pass
class TemplateRootObject:

    pass
class ReferenceAssignment:

    pass
class frontend_tao_Invocation(ReferenceAssignment):

    pass
class frontend_tao_ObjectSyntax(ReferenceAssignment):

    pass
class TemplateParameter:

    pass
class ObjectInstantiation:

    pass
class frontend_tao_TemplateRootObject(ObjectInstantiation):

    pass
class Assignment:

    pass
class frontend_tao_AttributeAssigment(Assignment):

    def __init__(self, targetFeature: str, frontend_tao_AttributeAssigment: "SourceExpression" = None, Assignment: "frontend_tao_ObjectInstantiation"):
        self.targetFeature = targetFeature
        self.frontend_tao_AttributeAssigment = frontend_tao_AttributeAssigment
        
    @property
    def targetFeature(self) -> str:
        return self.__targetFeature

    @targetFeature.setter
    def targetFeature(self, targetFeature: str):
        self.__targetFeature = targetFeature

    @property
    def frontend_tao_AttributeAssigment(self):
        return self.__frontend_tao_AttributeAssigment

    @frontend_tao_AttributeAssigment.setter
    def frontend_tao_AttributeAssigment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_tao_AttributeAssigment__frontend_tao_AttributeAssigment", None)
        self.__frontend_tao_AttributeAssigment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceExpression"):
                opp_val = getattr(old_value, "SourceExpression", None)
                if opp_val == self:
                    setattr(old_value, "SourceExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceExpression"):
                opp_val = getattr(value, "SourceExpression", None)
                setattr(value, "SourceExpression", self)

class frontend_facilities_CopierCallbackDefinition:

    def __init__(self, stop: bool, frontend_facilities_CopierCallbackDefinition: "Expression" = None, frontend_facilities_CopierCallbackDefinition209: "Expression" = None):
        self.stop = stop
        self.frontend_facilities_CopierCallbackDefinition = frontend_facilities_CopierCallbackDefinition
        self.frontend_facilities_CopierCallbackDefinition209 = frontend_facilities_CopierCallbackDefinition209
        
    @property
    def stop(self) -> bool:
        return self.__stop

    @stop.setter
    def stop(self, stop: bool):
        self.__stop = stop

    @property
    def frontend_facilities_CopierCallbackDefinition209(self):
        return self.__frontend_facilities_CopierCallbackDefinition209

    @frontend_facilities_CopierCallbackDefinition209.setter
    def frontend_facilities_CopierCallbackDefinition209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_facilities_CopierCallbackDefinition__frontend_facilities_CopierCallbackDefinition209", None)
        self.__frontend_facilities_CopierCallbackDefinition209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression210"):
                opp_val = getattr(old_value, "Expression210", None)
                if opp_val == self:
                    setattr(old_value, "Expression210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression210"):
                opp_val = getattr(value, "Expression210", None)
                setattr(value, "Expression210", self)

    @property
    def frontend_facilities_CopierCallbackDefinition(self):
        return self.__frontend_facilities_CopierCallbackDefinition

    @frontend_facilities_CopierCallbackDefinition.setter
    def frontend_facilities_CopierCallbackDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_facilities_CopierCallbackDefinition__frontend_facilities_CopierCallbackDefinition", None)
        self.__frontend_facilities_CopierCallbackDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression207"):
                opp_val = getattr(old_value, "Expression207", None)
                if opp_val == self:
                    setattr(old_value, "Expression207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression207"):
                opp_val = getattr(value, "Expression207", None)
                setattr(value, "Expression207", self)

class facilities_CopierCallbackDefinition:

    pass
class Template:

    pass
class TransformationDefinitionParameter:

    pass
class frontend_qool_InvocationParameter:

    def __init__(self, calleeModelName: str, frontend_qool_InvocationParameter: "TransformationDefinitionParameter" = None):
        self.calleeModelName = calleeModelName
        self.frontend_qool_InvocationParameter = frontend_qool_InvocationParameter
        
    @property
    def calleeModelName(self) -> str:
        return self.__calleeModelName

    @calleeModelName.setter
    def calleeModelName(self, calleeModelName: str):
        self.__calleeModelName = calleeModelName

    @property
    def frontend_qool_InvocationParameter(self):
        return self.__frontend_qool_InvocationParameter

    @frontend_qool_InvocationParameter.setter
    def frontend_qool_InvocationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvocationParameter__frontend_qool_InvocationParameter", None)
        self.__frontend_qool_InvocationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransformationDefinitionParameter"):
                opp_val = getattr(old_value, "TransformationDefinitionParameter", None)
                if opp_val == self:
                    setattr(old_value, "TransformationDefinitionParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransformationDefinitionParameter"):
                opp_val = getattr(value, "TransformationDefinitionParameter", None)
                setattr(value, "TransformationDefinitionParameter", self)

class InvokeTransformation:

    pass
class frontend_qool_InvokeInternal(InvokeTransformation):

    pass
class frontend_qool_InvokeExternal(InvokeTransformation):

    def __init__(self, queueName: str, traceAttributeName: str, frontend_qool_InvokeExternal: "Expression" = None):
        self.queueName = queueName
        self.traceAttributeName = traceAttributeName
        self.frontend_qool_InvokeExternal = frontend_qool_InvokeExternal
        
    @property
    def queueName(self) -> str:
        return self.__queueName

    @queueName.setter
    def queueName(self, queueName: str):
        self.__queueName = queueName

    @property
    def traceAttributeName(self) -> str:
        return self.__traceAttributeName

    @traceAttributeName.setter
    def traceAttributeName(self, traceAttributeName: str):
        self.__traceAttributeName = traceAttributeName

    @property
    def frontend_qool_InvokeExternal(self):
        return self.__frontend_qool_InvokeExternal

    @frontend_qool_InvokeExternal.setter
    def frontend_qool_InvokeExternal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeExternal__frontend_qool_InvokeExternal", None)
        self.__frontend_qool_InvokeExternal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression195"):
                opp_val = getattr(old_value, "Expression195", None)
                if opp_val == self:
                    setattr(old_value, "Expression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression195"):
                opp_val = getattr(value, "Expression195", None)
                setattr(value, "Expression195", self)

class NamedInvocationParameter:

    pass
class frontend_qool_NamedInvocationParameter:

    def __init__(self, formalName: str, frontend_qool_NamedInvocationParameter: "Expression" = None):
        self.formalName = formalName
        self.frontend_qool_NamedInvocationParameter = frontend_qool_NamedInvocationParameter
        
    @property
    def formalName(self) -> str:
        return self.__formalName

    @formalName.setter
    def formalName(self, formalName: str):
        self.__formalName = formalName

    @property
    def frontend_qool_NamedInvocationParameter(self):
        return self.__frontend_qool_NamedInvocationParameter

    @frontend_qool_NamedInvocationParameter.setter
    def frontend_qool_NamedInvocationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_NamedInvocationParameter__frontend_qool_NamedInvocationParameter", None)
        self.__frontend_qool_NamedInvocationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression198"):
                opp_val = getattr(old_value, "Expression198", None)
                if opp_val == self:
                    setattr(old_value, "Expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression198"):
                opp_val = getattr(value, "Expression198", None)
                setattr(value, "Expression198", self)

class frontend_qool_MatchPredicate(ABC):

    pass
class MatchPredicate:

    pass
class frontend_qool_PropertyEqualsPredicate(MatchPredicate):

    def __init__(self, propertyName: str, frontend_qool_PropertyEqualsPredicate: "Expression" = None, MatchPredicate: "frontend_qool_MatchExpression"):
        self.propertyName = propertyName
        self.frontend_qool_PropertyEqualsPredicate = frontend_qool_PropertyEqualsPredicate
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def frontend_qool_PropertyEqualsPredicate(self):
        return self.__frontend_qool_PropertyEqualsPredicate

    @frontend_qool_PropertyEqualsPredicate.setter
    def frontend_qool_PropertyEqualsPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_PropertyEqualsPredicate__frontend_qool_PropertyEqualsPredicate", None)
        self.__frontend_qool_PropertyEqualsPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression181"):
                opp_val = getattr(old_value, "Expression181", None)
                if opp_val == self:
                    setattr(old_value, "Expression181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression181"):
                opp_val = getattr(value, "Expression181", None)
                setattr(value, "Expression181", self)

class frontend_qool_KindOfPredicate(MatchPredicate):

    pass
class InvocationParameter:

    pass
class IteratorStatement:

    pass
class frontend_qool_ForEachStatement(IteratorStatement):

    pass
class frontend_qool_ForAllStatement(IteratorStatement):

    pass
class core_Statement:

    pass
class TypeExpression:

    pass
class frontend_core_TraceUse(TypeExpression):

    pass
class frontend_qool_QueueOptimization(ABC):

    pass
class QueueOptimization:

    pass
class frontend_qool_AccessByFeatureOptimization(QueueOptimization):

    def __init__(self, featureName: str, force: bool, QueueOptimization: "frontend_qool_QoolQueue"):
        self.featureName = featureName
        self.force = force
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def force(self) -> bool:
        return self.__force

    @force.setter
    def force(self, force: bool):
        self.__force = force

class Segment:

    pass
class mappings_MetamodelElementRef:

    pass
class QoolQueue:

    pass
class frontend_qool_ModelElementQueue(QoolQueue):

    pass
class frontend_qool_LocalQueue(QoolQueue):

    pass
class MetamodelElementRef:

    pass
class frontend_mappings_AttributeRef(MetamodelElementRef):

    def __init__(self, featureName: str, multivalued: bool, frontend_mappings_AttributeRef: "MatchedElement" = None):
        self.featureName = featureName
        self.multivalued = multivalued
        self.frontend_mappings_AttributeRef = frontend_mappings_AttributeRef
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def frontend_mappings_AttributeRef(self):
        return self.__frontend_mappings_AttributeRef

    @frontend_mappings_AttributeRef.setter
    def frontend_mappings_AttributeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_AttributeRef__frontend_mappings_AttributeRef", None)
        self.__frontend_mappings_AttributeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedElement145"):
                opp_val = getattr(old_value, "MatchedElement145", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement145"):
                opp_val = getattr(value, "MatchedElement145", None)
                setattr(value, "MatchedElement145", self)

class frontend_mappings_ReferenceRef(MetamodelElementRef):

    def __init__(self, featureName: str, multivalued: bool, frontend_mappings_ReferenceRef: "MatchedElement" = None):
        self.featureName = featureName
        self.multivalued = multivalued
        self.frontend_mappings_ReferenceRef = frontend_mappings_ReferenceRef
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def frontend_mappings_ReferenceRef(self):
        return self.__frontend_mappings_ReferenceRef

    @frontend_mappings_ReferenceRef.setter
    def frontend_mappings_ReferenceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_ReferenceRef__frontend_mappings_ReferenceRef", None)
        self.__frontend_mappings_ReferenceRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedElement147"):
                opp_val = getattr(old_value, "MatchedElement147", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement147"):
                opp_val = getattr(value, "MatchedElement147", None)
                setattr(value, "MatchedElement147", self)

class frontend_mappings_ClassRef(MetamodelElementRef):

    pass
class frontend_mappings_MetamodelElementRef(ABC):

    pass
class DefaultValue:

    pass
class frontend_mappings_IntDefaultValue(DefaultValue):

    def __init__(self, defaultValue: str):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

class Modifier:

    pass
class frontend_mappings_AttributeModifier(Modifier):

    pass
class frontend_mappings_Modifier(ABC):

    pass
class ReferenceRef:

    pass
class Class2Class:

    pass
class mappings_AttributeRightPart:

    pass
class mappings_Feature2Feature:

    pass
class frontend_mappings_FeatureRef(mappings_MetamodelElementRef, mappings_Feature2Feature):

    def __init__(self, featureName: str, multivalued: bool, frontend_mappings_FeatureRef: "MatchedElement" = None):
        self.featureName = featureName
        self.multivalued = multivalued
        self.frontend_mappings_FeatureRef = frontend_mappings_FeatureRef
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def frontend_mappings_FeatureRef(self):
        return self.__frontend_mappings_FeatureRef

    @frontend_mappings_FeatureRef.setter
    def frontend_mappings_FeatureRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_FeatureRef__frontend_mappings_FeatureRef", None)
        self.__frontend_mappings_FeatureRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedElement143"):
                opp_val = getattr(old_value, "MatchedElement143", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement143"):
                opp_val = getattr(value, "MatchedElement143", None)
                setattr(value, "MatchedElement143", self)

class frontend_mappings_Attribute2Attribute(mappings_AttributeRightPart, mappings_Feature2Feature):

    def __init__(self, cardinality: str, frontend_mappings_Attribute2Attribute135: set["AttributeModifier"] = None, Class2Class: "Class2Class" = None, frontend_mappings_Attribute2Attribute: set["AttributeRef"] = None):
        self.cardinality = cardinality
        self.frontend_mappings_Attribute2Attribute135 = frontend_mappings_Attribute2Attribute135 if frontend_mappings_Attribute2Attribute135 is not None else set()
        self.Class2Class = Class2Class
        self.frontend_mappings_Attribute2Attribute = frontend_mappings_Attribute2Attribute if frontend_mappings_Attribute2Attribute is not None else set()
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def Class2Class(self):
        return self.__Class2Class

    @Class2Class.setter
    def Class2Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Attribute2Attribute__Class2Class", None)
        self.__Class2Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings131"):
                opp_val = getattr(old_value, "mappings131", None)
                if opp_val == self:
                    setattr(old_value, "mappings131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings131"):
                opp_val = getattr(value, "mappings131", None)
                setattr(value, "mappings131", self)

    @property
    def frontend_mappings_Attribute2Attribute135(self):
        return self.__frontend_mappings_Attribute2Attribute135

    @frontend_mappings_Attribute2Attribute135.setter
    def frontend_mappings_Attribute2Attribute135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Attribute2Attribute__frontend_mappings_Attribute2Attribute135", None)
        self.__frontend_mappings_Attribute2Attribute135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeModifier"):
                    opp_val = getattr(item, "AttributeModifier", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeModifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeModifier"):
                    opp_val = getattr(item, "AttributeModifier", None)
                    
                    setattr(item, "AttributeModifier", self)
                    

    @property
    def frontend_mappings_Attribute2Attribute(self):
        return self.__frontend_mappings_Attribute2Attribute

    @frontend_mappings_Attribute2Attribute.setter
    def frontend_mappings_Attribute2Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Attribute2Attribute__frontend_mappings_Attribute2Attribute", None)
        self.__frontend_mappings_Attribute2Attribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeRef133"):
                    opp_val = getattr(item, "AttributeRef133", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeRef133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeRef133"):
                    opp_val = getattr(item, "AttributeRef133", None)
                    
                    setattr(item, "AttributeRef133", self)
                    

class Operator:

    pass
class frontend_mappings_Join(Operator):

    pass
class frontend_mappings_Split(Operator):

    pass
class AttributeModifier:

    pass
class frontend_mappings_DefaultValue(AttributeModifier):

    pass
class frontend_mappings_ConvertModifier(AttributeModifier):

    def __init__(self, converter: str, AttributeModifier: "frontend_mappings_Attribute2Attribute"):
        self.converter = converter
        
    @property
    def converter(self) -> str:
        return self.__converter

    @converter.setter
    def converter(self, converter: str):
        self.__converter = converter

class Attribute2Attribute:

    pass
class ClassRef:

    pass
class ClassMapping:

    pass
class frontend_mappings_Class2Class(ClassMapping):

    def __init__(self, cardinality: str, frontend_mappings_Class2Class: set["C2CModifier"] = None, frontend_mappings_Class2Class113: set["ClassRef"] = None, frontend_mappings_Class2Class115: set["ClassRef"] = None, Attribute2Attribute: set["Attribute2Attribute"] = None, ClassMapping129: "frontend_mappings_Join", ClassMapping: "frontend_mappings_Split"):
        self.cardinality = cardinality
        self.frontend_mappings_Class2Class = frontend_mappings_Class2Class if frontend_mappings_Class2Class is not None else set()
        self.frontend_mappings_Class2Class113 = frontend_mappings_Class2Class113 if frontend_mappings_Class2Class113 is not None else set()
        self.frontend_mappings_Class2Class115 = frontend_mappings_Class2Class115 if frontend_mappings_Class2Class115 is not None else set()
        self.Attribute2Attribute = Attribute2Attribute if Attribute2Attribute is not None else set()
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def frontend_mappings_Class2Class115(self):
        return self.__frontend_mappings_Class2Class115

    @frontend_mappings_Class2Class115.setter
    def frontend_mappings_Class2Class115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Class2Class__frontend_mappings_Class2Class115", None)
        self.__frontend_mappings_Class2Class115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassRef116"):
                    opp_val = getattr(item, "ClassRef116", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassRef116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassRef116"):
                    opp_val = getattr(item, "ClassRef116", None)
                    
                    setattr(item, "ClassRef116", self)
                    

    @property
    def frontend_mappings_Class2Class(self):
        return self.__frontend_mappings_Class2Class

    @frontend_mappings_Class2Class.setter
    def frontend_mappings_Class2Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Class2Class__frontend_mappings_Class2Class", None)
        self.__frontend_mappings_Class2Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C2CModifier111"):
                    opp_val = getattr(item, "C2CModifier111", None)
                    
                    if opp_val == self:
                        setattr(item, "C2CModifier111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C2CModifier111"):
                    opp_val = getattr(item, "C2CModifier111", None)
                    
                    setattr(item, "C2CModifier111", self)
                    

    @property
    def frontend_mappings_Class2Class113(self):
        return self.__frontend_mappings_Class2Class113

    @frontend_mappings_Class2Class113.setter
    def frontend_mappings_Class2Class113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Class2Class__frontend_mappings_Class2Class113", None)
        self.__frontend_mappings_Class2Class113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassRef"):
                    opp_val = getattr(item, "ClassRef", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassRef"):
                    opp_val = getattr(item, "ClassRef", None)
                    
                    setattr(item, "ClassRef", self)
                    

    @property
    def Attribute2Attribute(self):
        return self.__Attribute2Attribute

    @Attribute2Attribute.setter
    def Attribute2Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Class2Class__Attribute2Attribute", None)
        self.__Attribute2Attribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings"):
                    opp_val = getattr(item, "mappings", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings"):
                    opp_val = getattr(item, "mappings", None)
                    
                    setattr(item, "mappings", self)
                    

class NamedElement:

    pass
class frontend_core_DefinitionParameter(NamedElement):

    pass
class frontend_core_TraceElement(NamedElement):

    pass
class frontend_core_InlineFeature(NamedElement):

    def __init__(self, multivalued: bool, frontend_core_InlineFeature: "TypeExpression" = None):
        self.multivalued = multivalued
        self.frontend_core_InlineFeature = frontend_core_InlineFeature
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def frontend_core_InlineFeature(self):
        return self.__frontend_core_InlineFeature

    @frontend_core_InlineFeature.setter
    def frontend_core_InlineFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_InlineFeature__frontend_core_InlineFeature", None)
        self.__frontend_core_InlineFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeExpression316"):
                opp_val = getattr(old_value, "TypeExpression316", None)
                if opp_val == self:
                    setattr(old_value, "TypeExpression316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeExpression316"):
                opp_val = getattr(value, "TypeExpression316", None)
                setattr(value, "TypeExpression316", self)

class frontend_qool_Segment(NamedElement):

    pass
class frontend_core_TraceDefinition(NamedElement):

    pass
class frontend_core_InlineClass(NamedElement):

    pass
class frontend_mappings_Tag(NamedElement):

    pass
class ResolveLink:

    pass
class frontend_mappings_AttributeRightPart(ABC):

    pass
class AttributeRightPart:

    pass
class frontend_mappings_AttributeIsBoolean(AttributeRightPart):

    def __init__(self, boolValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping"):
        self.boolValue = boolValue
        
    @property
    def boolValue(self) -> str:
        return self.__boolValue

    @boolValue.setter
    def boolValue(self, boolValue: str):
        self.__boolValue = boolValue

class frontend_mappings_AttributeIsString(AttributeRightPart):

    def __init__(self, strValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping"):
        self.strValue = strValue
        
    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

class frontend_mappings_AttributeIsDouble(AttributeRightPart):

    def __init__(self, doubleValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping"):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> str:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: str):
        self.__doubleValue = doubleValue

class frontend_mappings_AttributeIsResolveLink(AttributeRightPart):

    pass
class AttributeRef:

    pass
class Feature2Feature:

    pass
class frontend_mappings_Reference2Reference(Feature2Feature):

    def __init__(self, cardinality: str, resolverName: str, frontend_mappings_Reference2Reference: set["ReferenceRef"] = None, frontend_mappings_Reference2Reference138: set["ReferenceRef"] = None):
        self.cardinality = cardinality
        self.resolverName = resolverName
        self.frontend_mappings_Reference2Reference = frontend_mappings_Reference2Reference if frontend_mappings_Reference2Reference is not None else set()
        self.frontend_mappings_Reference2Reference138 = frontend_mappings_Reference2Reference138 if frontend_mappings_Reference2Reference138 is not None else set()
        
    @property
    def resolverName(self) -> str:
        return self.__resolverName

    @resolverName.setter
    def resolverName(self, resolverName: str):
        self.__resolverName = resolverName

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def frontend_mappings_Reference2Reference138(self):
        return self.__frontend_mappings_Reference2Reference138

    @frontend_mappings_Reference2Reference138.setter
    def frontend_mappings_Reference2Reference138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Reference2Reference__frontend_mappings_Reference2Reference138", None)
        self.__frontend_mappings_Reference2Reference138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReferenceRef139"):
                    opp_val = getattr(item, "ReferenceRef139", None)
                    
                    if opp_val == self:
                        setattr(item, "ReferenceRef139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReferenceRef139"):
                    opp_val = getattr(item, "ReferenceRef139", None)
                    
                    setattr(item, "ReferenceRef139", self)
                    

    @property
    def frontend_mappings_Reference2Reference(self):
        return self.__frontend_mappings_Reference2Reference

    @frontend_mappings_Reference2Reference.setter
    def frontend_mappings_Reference2Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Reference2Reference__frontend_mappings_Reference2Reference", None)
        self.__frontend_mappings_Reference2Reference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReferenceRef"):
                    opp_val = getattr(item, "ReferenceRef", None)
                    
                    if opp_val == self:
                        setattr(item, "ReferenceRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReferenceRef"):
                    opp_val = getattr(item, "ReferenceRef", None)
                    
                    setattr(item, "ReferenceRef", self)
                    

class frontend_mappings_AttributeMapping(Feature2Feature):

    pass
class Converter:

    pass
class frontend_mappings_Converter:

    def __init__(self, isExternal: str, converterName: str, frontend_mappings_Converter: "UseDeclaration" = None):
        self.isExternal = isExternal
        self.converterName = converterName
        self.frontend_mappings_Converter = frontend_mappings_Converter
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def converterName(self) -> str:
        return self.__converterName

    @converterName.setter
    def converterName(self, converterName: str):
        self.__converterName = converterName

    @property
    def frontend_mappings_Converter(self):
        return self.__frontend_mappings_Converter

    @frontend_mappings_Converter.setter
    def frontend_mappings_Converter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Converter__frontend_mappings_Converter", None)
        self.__frontend_mappings_Converter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseDeclaration109"):
                opp_val = getattr(old_value, "UseDeclaration109", None)
                if opp_val == self:
                    setattr(old_value, "UseDeclaration109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseDeclaration109"):
                opp_val = getattr(value, "UseDeclaration109", None)
                setattr(value, "UseDeclaration109", self)

class frontend_mappings_AttributeIsInteger(AttributeRightPart):

    def __init__(self, intValue: int, AttributeRightPart: "frontend_mappings_AttributeMapping"):
        self.intValue = intValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

class Section:

    pass
class C2CModifier:

    pass
class frontend_mappings_EqualityFilter(C2CModifier):

    def __init__(self, filter: str, frontend_mappings_EqualityFilter: "AttributeRef" = None, C2CModifier111: "frontend_mappings_Class2Class", C2CModifier: "frontend_mappings_Context"):
        self.filter = filter
        self.frontend_mappings_EqualityFilter = frontend_mappings_EqualityFilter
        
    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def frontend_mappings_EqualityFilter(self):
        return self.__frontend_mappings_EqualityFilter

    @frontend_mappings_EqualityFilter.setter
    def frontend_mappings_EqualityFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_EqualityFilter__frontend_mappings_EqualityFilter", None)
        self.__frontend_mappings_EqualityFilter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeRef126"):
                opp_val = getattr(old_value, "AttributeRef126", None)
                if opp_val == self:
                    setattr(old_value, "AttributeRef126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeRef126"):
                opp_val = getattr(value, "AttributeRef126", None)
                setattr(value, "AttributeRef126", self)

class frontend_mappings_LinkedBy(C2CModifier):

    pass
class frontend_mappings_RelatedBy(C2CModifier):

    pass
class MappingElement:

    pass
class frontend_mappings_ClassMapping(MappingElement):

    pass
class frontend_mappings_C2CModifier(MappingElement):

    pass
class FeatureRef:

    pass
class frontend_mappings_Feature2Feature(MappingElement):

    pass
class UseDeclaration:

    pass
class MatchedElement:

    pass
class mappings_MappingVariable:

    pass
class core_ClassUse:

    pass
class frontend_core_ModelReference(core_ClassUse, core_Expression):

    pass
class frontend_mappings_MatchedElement(core_ClassUse, mappings_MappingVariable):

    pass
class Context:

    pass
class Delegate:

    pass
class PReference:

    pass
class frontend_patterns_CollectionReference(PReference):

    pass
class Tag:

    pass
class PFeature:

    pass
class frontend_patterns_PAttribute(PFeature):

    pass
class frontend_patterns_POutputVariable:

    pass
class POutputVariable:

    pass
class PObject:

    pass
class frontend_patterns_PReference(PFeature):

    pass
class Pattern:

    pass
class core_TransformationDefinition:

    pass
class chain_AvailableTransformation:

    pass
class frontend_chain_CompositeTransformation(chain_AvailableTransformation, core_TransformationDefinition):

    pass
class frontend_chain_AvailableTransformation(ABC):

    pass
class RepresentModel:

    pass
class frontend_core_UseDeclaration(RepresentModel):

    def __init__(self, module: str, as: str, RepresentModel: "frontend_chain_TransformationExecution", RepresentModel304: "frontend_core_ClassUse", RepresentModel256: "frontend_core_RequireModelParameter", RepresentModel58: "frontend_chain_TransformationExecution"):
        self.module = module
        self.as = as
        
    @property
    def module(self) -> str:
        return self.__module

    @module.setter
    def module(self, module: str):
        self.__module = module

    @property
    def as(self) -> str:
        return self.__as

    @as.setter
    def as(self, as: str):
        self.__as = as

class frontend_core_RequireDeclaration(RepresentModel):

    def __init__(self, name: str, default: str, frontend_core_RequireDeclaration: set["RequireParameter"] = None, RepresentModel: "frontend_chain_TransformationExecution", RepresentModel304: "frontend_core_ClassUse", RepresentModel256: "frontend_core_RequireModelParameter", RepresentModel58: "frontend_chain_TransformationExecution"):
        self.name = name
        self.default = default
        self.frontend_core_RequireDeclaration = frontend_core_RequireDeclaration if frontend_core_RequireDeclaration is not None else set()
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frontend_core_RequireDeclaration(self):
        return self.__frontend_core_RequireDeclaration

    @frontend_core_RequireDeclaration.setter
    def frontend_core_RequireDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_RequireDeclaration__frontend_core_RequireDeclaration", None)
        self.__frontend_core_RequireDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequireParameter"):
                    opp_val = getattr(item, "RequireParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "RequireParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequireParameter"):
                    opp_val = getattr(item, "RequireParameter", None)
                    
                    setattr(item, "RequireParameter", self)
                    

class AvailableTransformation:

    pass
class core_RepresentModel:

    pass
class frontend_core_InlineModel(core_RepresentModel, core_ModuleDefinition):

    pass
class frontend_core_TransformationDefinitionParameter(core_RepresentModel, core_DefinitionParameter):

    pass
class frontend_core_TracedModelParameter(core_RepresentModel, core_DefinitionParameter):

    pass
class GeneratedModel:

    pass
class ExternalTransformation:

    pass
class CompositeTransformation:

    pass
class MethodSelf:

    pass
class MethodParameter:

    pass
class TransformationExecution:

    pass
class Variable:

    pass
class frontend_imperative_MethodSelf(Variable):

    pass
class frontend_tao_TemplateParameter(Variable):

    pass
class frontend_core_ClosureParameter(Variable):

    pass
class frontend_mappings_MappingVariable(Variable):

    pass
class frontend_imperative_MethodParameter(Variable):

    pass
class frontend_tao_ObjectSourceVariable(Variable):

    pass
class frontend_attribution_RuleSelf(Variable):

    pass
class Expression:

    pass
class frontend_core_KeywordMethodCall(Expression):

    pass
class frontend_core_IfExpr(Expression):

    pass
class frontend_core_PropertyWrite(Expression):

    def __init__(self, property: str, frontend_core_PropertyWrite: "Variable" = None, frontend_core_PropertyWrite262: "Expression" = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.property = property
        self.frontend_core_PropertyWrite = frontend_core_PropertyWrite
        self.frontend_core_PropertyWrite262 = frontend_core_PropertyWrite262
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

    @property
    def frontend_core_PropertyWrite(self):
        return self.__frontend_core_PropertyWrite

    @frontend_core_PropertyWrite.setter
    def frontend_core_PropertyWrite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_PropertyWrite__frontend_core_PropertyWrite", None)
        self.__frontend_core_PropertyWrite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable260"):
                opp_val = getattr(old_value, "Variable260", None)
                if opp_val == self:
                    setattr(old_value, "Variable260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable260"):
                opp_val = getattr(value, "Variable260", None)
                setattr(value, "Variable260", self)

    @property
    def frontend_core_PropertyWrite262(self):
        return self.__frontend_core_PropertyWrite262

    @frontend_core_PropertyWrite262.setter
    def frontend_core_PropertyWrite262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_PropertyWrite__frontend_core_PropertyWrite262", None)
        self.__frontend_core_PropertyWrite262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression263"):
                opp_val = getattr(old_value, "Expression263", None)
                if opp_val == self:
                    setattr(old_value, "Expression263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression263"):
                opp_val = getattr(value, "Expression263", None)
                setattr(value, "Expression263", self)

class frontend_facilities_Copier(Expression):

    pass
class frontend_qool_InvokeTransformation(Expression):

    def __init__(self, transformationName: str, entryPointName: str, frontend_qool_InvokeTransformation: set["InvocationParameter"] = None, frontend_qool_InvokeTransformation184: set["InvocationParameter"] = None, frontend_qool_InvokeTransformation187: set["NamedInvocationParameter"] = None, frontend_qool_InvokeTransformation189: "Variable" = None, frontend_qool_InvokeTransformation192: set["Expression"] = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.transformationName = transformationName
        self.entryPointName = entryPointName
        self.frontend_qool_InvokeTransformation = frontend_qool_InvokeTransformation if frontend_qool_InvokeTransformation is not None else set()
        self.frontend_qool_InvokeTransformation184 = frontend_qool_InvokeTransformation184 if frontend_qool_InvokeTransformation184 is not None else set()
        self.frontend_qool_InvokeTransformation187 = frontend_qool_InvokeTransformation187 if frontend_qool_InvokeTransformation187 is not None else set()
        self.frontend_qool_InvokeTransformation189 = frontend_qool_InvokeTransformation189
        self.frontend_qool_InvokeTransformation192 = frontend_qool_InvokeTransformation192 if frontend_qool_InvokeTransformation192 is not None else set()
        
    @property
    def transformationName(self) -> str:
        return self.__transformationName

    @transformationName.setter
    def transformationName(self, transformationName: str):
        self.__transformationName = transformationName

    @property
    def entryPointName(self) -> str:
        return self.__entryPointName

    @entryPointName.setter
    def entryPointName(self, entryPointName: str):
        self.__entryPointName = entryPointName

    @property
    def frontend_qool_InvokeTransformation189(self):
        return self.__frontend_qool_InvokeTransformation189

    @frontend_qool_InvokeTransformation189.setter
    def frontend_qool_InvokeTransformation189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation189", None)
        self.__frontend_qool_InvokeTransformation189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable190"):
                opp_val = getattr(old_value, "Variable190", None)
                if opp_val == self:
                    setattr(old_value, "Variable190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable190"):
                opp_val = getattr(value, "Variable190", None)
                setattr(value, "Variable190", self)

    @property
    def frontend_qool_InvokeTransformation184(self):
        return self.__frontend_qool_InvokeTransformation184

    @frontend_qool_InvokeTransformation184.setter
    def frontend_qool_InvokeTransformation184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation184", None)
        self.__frontend_qool_InvokeTransformation184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvocationParameter185"):
                    opp_val = getattr(item, "InvocationParameter185", None)
                    
                    if opp_val == self:
                        setattr(item, "InvocationParameter185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvocationParameter185"):
                    opp_val = getattr(item, "InvocationParameter185", None)
                    
                    setattr(item, "InvocationParameter185", self)
                    

    @property
    def frontend_qool_InvokeTransformation187(self):
        return self.__frontend_qool_InvokeTransformation187

    @frontend_qool_InvokeTransformation187.setter
    def frontend_qool_InvokeTransformation187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation187", None)
        self.__frontend_qool_InvokeTransformation187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedInvocationParameter"):
                    opp_val = getattr(item, "NamedInvocationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedInvocationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedInvocationParameter"):
                    opp_val = getattr(item, "NamedInvocationParameter", None)
                    
                    setattr(item, "NamedInvocationParameter", self)
                    

    @property
    def frontend_qool_InvokeTransformation192(self):
        return self.__frontend_qool_InvokeTransformation192

    @frontend_qool_InvokeTransformation192.setter
    def frontend_qool_InvokeTransformation192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation192", None)
        self.__frontend_qool_InvokeTransformation192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression193"):
                    opp_val = getattr(item, "Expression193", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression193"):
                    opp_val = getattr(item, "Expression193", None)
                    
                    setattr(item, "Expression193", self)
                    

    @property
    def frontend_qool_InvokeTransformation(self):
        return self.__frontend_qool_InvokeTransformation

    @frontend_qool_InvokeTransformation.setter
    def frontend_qool_InvokeTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation", None)
        self.__frontend_qool_InvokeTransformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvocationParameter"):
                    opp_val = getattr(item, "InvocationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "InvocationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvocationParameter"):
                    opp_val = getattr(item, "InvocationParameter", None)
                    
                    setattr(item, "InvocationParameter", self)
                    

class frontend_core_ClosureDeclaration(Expression):

    pass
class frontend_core_NumLiteral(Expression):

    def __init__(self, value: int, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class frontend_core_BinaryExpr(Expression):

    def __init__(self, binaryOp: str, frontend_core_BinaryExpr: "Expression" = None, frontend_core_BinaryExpr280: "Expression" = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.binaryOp = binaryOp
        self.frontend_core_BinaryExpr = frontend_core_BinaryExpr
        self.frontend_core_BinaryExpr280 = frontend_core_BinaryExpr280
        
    @property
    def binaryOp(self) -> str:
        return self.__binaryOp

    @binaryOp.setter
    def binaryOp(self, binaryOp: str):
        self.__binaryOp = binaryOp

    @property
    def frontend_core_BinaryExpr280(self):
        return self.__frontend_core_BinaryExpr280

    @frontend_core_BinaryExpr280.setter
    def frontend_core_BinaryExpr280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_BinaryExpr__frontend_core_BinaryExpr280", None)
        self.__frontend_core_BinaryExpr280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression281"):
                opp_val = getattr(old_value, "Expression281", None)
                if opp_val == self:
                    setattr(old_value, "Expression281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression281"):
                opp_val = getattr(value, "Expression281", None)
                setattr(value, "Expression281", self)

    @property
    def frontend_core_BinaryExpr(self):
        return self.__frontend_core_BinaryExpr

    @frontend_core_BinaryExpr.setter
    def frontend_core_BinaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_BinaryExpr__frontend_core_BinaryExpr", None)
        self.__frontend_core_BinaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression278"):
                opp_val = getattr(old_value, "Expression278", None)
                if opp_val == self:
                    setattr(old_value, "Expression278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression278"):
                opp_val = getattr(value, "Expression278", None)
                setattr(value, "Expression278", self)

class frontend_core_BooleanLiteral(Expression):

    def __init__(self, value: bool, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class frontend_core_MatchTrace(Expression):

    def __init__(self, cardinality: str, frontend_core_MatchTrace: "TraceDefinition" = None, frontend_core_MatchTrace320: "TraceCompareExpression" = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.cardinality = cardinality
        self.frontend_core_MatchTrace = frontend_core_MatchTrace
        self.frontend_core_MatchTrace320 = frontend_core_MatchTrace320
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def frontend_core_MatchTrace320(self):
        return self.__frontend_core_MatchTrace320

    @frontend_core_MatchTrace320.setter
    def frontend_core_MatchTrace320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MatchTrace__frontend_core_MatchTrace320", None)
        self.__frontend_core_MatchTrace320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceCompareExpression"):
                opp_val = getattr(old_value, "TraceCompareExpression", None)
                if opp_val == self:
                    setattr(old_value, "TraceCompareExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceCompareExpression"):
                opp_val = getattr(value, "TraceCompareExpression", None)
                setattr(value, "TraceCompareExpression", self)

    @property
    def frontend_core_MatchTrace(self):
        return self.__frontend_core_MatchTrace

    @frontend_core_MatchTrace.setter
    def frontend_core_MatchTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MatchTrace__frontend_core_MatchTrace", None)
        self.__frontend_core_MatchTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceDefinition318"):
                opp_val = getattr(old_value, "TraceDefinition318", None)
                if opp_val == self:
                    setattr(old_value, "TraceDefinition318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceDefinition318"):
                opp_val = getattr(value, "TraceDefinition318", None)
                setattr(value, "TraceDefinition318", self)

class frontend_attribution_AttributeUse(Expression):

    pass
class frontend_core_MethodCall(Expression):

    def __init__(self, methodName: str, withParameters: bool, frontend_core_MethodCall: "Expression" = None, frontend_core_MethodCall269: set["Expression"] = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.methodName = methodName
        self.withParameters = withParameters
        self.frontend_core_MethodCall = frontend_core_MethodCall
        self.frontend_core_MethodCall269 = frontend_core_MethodCall269 if frontend_core_MethodCall269 is not None else set()
        
    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def withParameters(self) -> bool:
        return self.__withParameters

    @withParameters.setter
    def withParameters(self, withParameters: bool):
        self.__withParameters = withParameters

    @property
    def frontend_core_MethodCall269(self):
        return self.__frontend_core_MethodCall269

    @frontend_core_MethodCall269.setter
    def frontend_core_MethodCall269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MethodCall__frontend_core_MethodCall269", None)
        self.__frontend_core_MethodCall269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression270"):
                    opp_val = getattr(item, "Expression270", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression270"):
                    opp_val = getattr(item, "Expression270", None)
                    
                    setattr(item, "Expression270", self)
                    

    @property
    def frontend_core_MethodCall(self):
        return self.__frontend_core_MethodCall

    @frontend_core_MethodCall.setter
    def frontend_core_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MethodCall__frontend_core_MethodCall", None)
        self.__frontend_core_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression267"):
                opp_val = getattr(old_value, "Expression267", None)
                if opp_val == self:
                    setattr(old_value, "Expression267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression267"):
                opp_val = getattr(value, "Expression267", None)
                setattr(value, "Expression267", self)

class frontend_qool_MatchExpression(Expression):

    pass
class frontend_core_ResolveLink(Expression):

    def __init__(self, isExternal: str, linkName: str, featureName: str, frontend_core_ResolveLink: "Expression" = None, frontend_core_ResolveLink289: "UseDeclaration" = None, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.isExternal = isExternal
        self.linkName = linkName
        self.featureName = featureName
        self.frontend_core_ResolveLink = frontend_core_ResolveLink
        self.frontend_core_ResolveLink289 = frontend_core_ResolveLink289
        
    @property
    def linkName(self) -> str:
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName

    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def frontend_core_ResolveLink(self):
        return self.__frontend_core_ResolveLink

    @frontend_core_ResolveLink.setter
    def frontend_core_ResolveLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_ResolveLink__frontend_core_ResolveLink", None)
        self.__frontend_core_ResolveLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression287"):
                opp_val = getattr(old_value, "Expression287", None)
                if opp_val == self:
                    setattr(old_value, "Expression287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression287"):
                opp_val = getattr(value, "Expression287", None)
                setattr(value, "Expression287", self)

    @property
    def frontend_core_ResolveLink289(self):
        return self.__frontend_core_ResolveLink289

    @frontend_core_ResolveLink289.setter
    def frontend_core_ResolveLink289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_ResolveLink__frontend_core_ResolveLink289", None)
        self.__frontend_core_ResolveLink289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseDeclaration290"):
                opp_val = getattr(old_value, "UseDeclaration290", None)
                if opp_val == self:
                    setattr(old_value, "UseDeclaration290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseDeclaration290"):
                opp_val = getattr(value, "UseDeclaration290", None)
                setattr(value, "UseDeclaration290", self)

class frontend_core_StringLiteral(Expression):

    def __init__(self, value: str, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class frontend_core_VariableReference(Expression):

    pass
class frontend_core_PutTrace(Expression):

    pass
class frontend_core_DoubleLiteral(Expression):

    def __init__(self, value: float, Expression258: "frontend_core_DefineVariable", Expression200: "frontend_facilities_Copier", Expression299: "frontend_core_IfBranch", Expression161: "frontend_qool_IteratorStatement", Expression195: "frontend_qool_InvokeExternal", Expression287: "frontend_core_ResolveLink", Expression173: "frontend_qool_EmitStatement", Expression210: "frontend_facilities_CopierCallbackDefinition", Expression207: "frontend_facilities_CopierCallbackDefinition", Expression331: "frontend_core_PutTraceParameter", Expression198: "frontend_qool_NamedInvocationParameter", Expression30: "frontend_attribution_AttributeInit", Expression72: "frontend_patterns_PAttribute", Expression32: "frontend_attribution_AttributeUse", Expression193: "frontend_qool_InvokeTransformation", Expression325: "frontend_core_TraceCompareExpression", Expression278: "frontend_core_BinaryExpr", Expression168: "frontend_qool_ForEachStatement", Expression276: "frontend_core_KeywordParameter", Expression267: "frontend_core_MethodCall", Expression270: "frontend_core_MethodCall", Expression281: "frontend_core_BinaryExpr", Expression225: "frontend_tao_WithOptionalVariableExpression", Expression27: "frontend_attribution_AttributeInit", Expression272: "frontend_core_KeywordMethodCall", Expression181: "frontend_qool_PropertyEqualsPredicate", Expression263: "frontend_core_PropertyWrite", Expression: "frontend_attribution_AttributionRule"):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class MethodDefinition:

    pass
class core_TypedWithClass:

    pass
class AttributionRule:

    pass
class AttributeDcl:

    pass
class frontend_attribution_InheritedAttributeDcl(AttributeDcl):

    pass
class frontend_attribution_SynthesizedAttributeDcl(AttributeDcl):

    pass
class ClassUse:

    pass
class core_Variable:

    pass
class frontend_qool_IteratorStatement(core_Statement, core_Variable):

    pass
class frontend_tao_ObjectInstantiation(core_Statement, core_Variable):

    pass
class frontend_tao_ReferenceAssignment(core_Variable, tao_Assignment):

    def __init__(self, multivalued: bool, targetFeature: str, frontend_tao_ReferenceAssignment: "SourceExpression" = None):
        self.multivalued = multivalued
        self.targetFeature = targetFeature
        self.frontend_tao_ReferenceAssignment = frontend_tao_ReferenceAssignment
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def targetFeature(self) -> str:
        return self.__targetFeature

    @targetFeature.setter
    def targetFeature(self, targetFeature: str):
        self.__targetFeature = targetFeature

    @property
    def frontend_tao_ReferenceAssignment(self):
        return self.__frontend_tao_ReferenceAssignment

    @frontend_tao_ReferenceAssignment.setter
    def frontend_tao_ReferenceAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_tao_ReferenceAssignment__frontend_tao_ReferenceAssignment", None)
        self.__frontend_tao_ReferenceAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceExpression227"):
                opp_val = getattr(old_value, "SourceExpression227", None)
                if opp_val == self:
                    setattr(old_value, "SourceExpression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceExpression227"):
                opp_val = getattr(value, "SourceExpression227", None)
                setattr(value, "SourceExpression227", self)

class frontend_core_DefineVariable(core_Statement, core_Variable):

    pass
class koan_Matcher:

    pass
class frontend_koan_ForAllMatcher(core_Variable, koan_Matcher):

    pass
class LocatedElement:

    pass
class frontend_chain_TransformationExecution(LocatedElement):

    pass
class frontend_mappings_Operator(LocatedElement):

    pass
class frontend_mappings_Section(LocatedElement):

    def __init__(self, sectionType: str, frontend_mappings_Section: set["MappingElement"] = None):
        self.sectionType = sectionType
        self.frontend_mappings_Section = frontend_mappings_Section if frontend_mappings_Section is not None else set()
        
    @property
    def sectionType(self) -> str:
        return self.__sectionType

    @sectionType.setter
    def sectionType(self, sectionType: str):
        self.__sectionType = sectionType

    @property
    def frontend_mappings_Section(self):
        return self.__frontend_mappings_Section

    @frontend_mappings_Section.setter
    def frontend_mappings_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Section__frontend_mappings_Section", None)
        self.__frontend_mappings_Section = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MappingElement100"):
                    opp_val = getattr(item, "MappingElement100", None)
                    
                    if opp_val == self:
                        setattr(item, "MappingElement100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MappingElement100"):
                    opp_val = getattr(item, "MappingElement100", None)
                    
                    setattr(item, "MappingElement100", self)
                    

class frontend_mappings_Context(LocatedElement):

    pass
class frontend_core_Statement(LocatedElement):

    pass
class frontend_mappings_Delegate(LocatedElement):

    def __init__(self, isExternal: str, linkName: str, featureName: str, frontend_mappings_Delegate84: set["Tag"] = None, frontend_mappings_Delegate: set["MatchedElement"] = None, frontend_mappings_Delegate82: "UseDeclaration" = None):
        self.isExternal = isExternal
        self.linkName = linkName
        self.featureName = featureName
        self.frontend_mappings_Delegate84 = frontend_mappings_Delegate84 if frontend_mappings_Delegate84 is not None else set()
        self.frontend_mappings_Delegate = frontend_mappings_Delegate if frontend_mappings_Delegate is not None else set()
        self.frontend_mappings_Delegate82 = frontend_mappings_Delegate82
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def linkName(self) -> str:
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName

    @property
    def frontend_mappings_Delegate84(self):
        return self.__frontend_mappings_Delegate84

    @frontend_mappings_Delegate84.setter
    def frontend_mappings_Delegate84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Delegate__frontend_mappings_Delegate84", None)
        self.__frontend_mappings_Delegate84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    setattr(item, "Tag", self)
                    

    @property
    def frontend_mappings_Delegate82(self):
        return self.__frontend_mappings_Delegate82

    @frontend_mappings_Delegate82.setter
    def frontend_mappings_Delegate82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Delegate__frontend_mappings_Delegate82", None)
        self.__frontend_mappings_Delegate82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseDeclaration"):
                opp_val = getattr(old_value, "UseDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "UseDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseDeclaration"):
                opp_val = getattr(value, "UseDeclaration", None)
                setattr(value, "UseDeclaration", self)

    @property
    def frontend_mappings_Delegate(self):
        return self.__frontend_mappings_Delegate

    @frontend_mappings_Delegate.setter
    def frontend_mappings_Delegate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Delegate__frontend_mappings_Delegate", None)
        self.__frontend_mappings_Delegate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchedElement"):
                    opp_val = getattr(item, "MatchedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchedElement"):
                    opp_val = getattr(item, "MatchedElement", None)
                    
                    setattr(item, "MatchedElement", self)
                    

class frontend_patterns_Pattern(LocatedElement):

    def __init__(self, name: str, frontend_patterns_Pattern: set["PObject"] = None, frontend_patterns_Pattern64: set["POutputVariable"] = None):
        self.name = name
        self.frontend_patterns_Pattern = frontend_patterns_Pattern if frontend_patterns_Pattern is not None else set()
        self.frontend_patterns_Pattern64 = frontend_patterns_Pattern64 if frontend_patterns_Pattern64 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frontend_patterns_Pattern(self):
        return self.__frontend_patterns_Pattern

    @frontend_patterns_Pattern.setter
    def frontend_patterns_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_patterns_Pattern__frontend_patterns_Pattern", None)
        self.__frontend_patterns_Pattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PObject"):
                    opp_val = getattr(item, "PObject", None)
                    
                    if opp_val == self:
                        setattr(item, "PObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PObject"):
                    opp_val = getattr(item, "PObject", None)
                    
                    setattr(item, "PObject", self)
                    

    @property
    def frontend_patterns_Pattern64(self):
        return self.__frontend_patterns_Pattern64

    @frontend_patterns_Pattern64.setter
    def frontend_patterns_Pattern64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_patterns_Pattern__frontend_patterns_Pattern64", None)
        self.__frontend_patterns_Pattern64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "POutputVariable"):
                    opp_val = getattr(item, "POutputVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "POutputVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "POutputVariable"):
                    opp_val = getattr(item, "POutputVariable", None)
                    
                    setattr(item, "POutputVariable", self)
                    

class frontend_mappings_MappingElement(LocatedElement):

    pass
class frontend_imperative_MethodDefinition(LocatedElement):

    def __init__(self, name: str, frontend_imperative_MethodDefinition: set["MethodParameter"] = None, frontend_imperative_MethodDefinition39: "MethodSelf" = None, frontend_imperative_MethodDefinition41: "ClassUse" = None, frontend_imperative_MethodDefinition44: set["Statement"] = None):
        self.name = name
        self.frontend_imperative_MethodDefinition = frontend_imperative_MethodDefinition if frontend_imperative_MethodDefinition is not None else set()
        self.frontend_imperative_MethodDefinition39 = frontend_imperative_MethodDefinition39
        self.frontend_imperative_MethodDefinition41 = frontend_imperative_MethodDefinition41
        self.frontend_imperative_MethodDefinition44 = frontend_imperative_MethodDefinition44 if frontend_imperative_MethodDefinition44 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frontend_imperative_MethodDefinition41(self):
        return self.__frontend_imperative_MethodDefinition41

    @frontend_imperative_MethodDefinition41.setter
    def frontend_imperative_MethodDefinition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_imperative_MethodDefinition__frontend_imperative_MethodDefinition41", None)
        self.__frontend_imperative_MethodDefinition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassUse42"):
                opp_val = getattr(old_value, "ClassUse42", None)
                if opp_val == self:
                    setattr(old_value, "ClassUse42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassUse42"):
                opp_val = getattr(value, "ClassUse42", None)
                setattr(value, "ClassUse42", self)

    @property
    def frontend_imperative_MethodDefinition44(self):
        return self.__frontend_imperative_MethodDefinition44

    @frontend_imperative_MethodDefinition44.setter
    def frontend_imperative_MethodDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_imperative_MethodDefinition__frontend_imperative_MethodDefinition44", None)
        self.__frontend_imperative_MethodDefinition44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement45"):
                    opp_val = getattr(item, "Statement45", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement45"):
                    opp_val = getattr(item, "Statement45", None)
                    
                    setattr(item, "Statement45", self)
                    

    @property
    def frontend_imperative_MethodDefinition39(self):
        return self.__frontend_imperative_MethodDefinition39

    @frontend_imperative_MethodDefinition39.setter
    def frontend_imperative_MethodDefinition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_imperative_MethodDefinition__frontend_imperative_MethodDefinition39", None)
        self.__frontend_imperative_MethodDefinition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodSelf"):
                opp_val = getattr(old_value, "MethodSelf", None)
                if opp_val == self:
                    setattr(old_value, "MethodSelf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodSelf"):
                opp_val = getattr(value, "MethodSelf", None)
                setattr(value, "MethodSelf", self)

    @property
    def frontend_imperative_MethodDefinition(self):
        return self.__frontend_imperative_MethodDefinition

    @frontend_imperative_MethodDefinition.setter
    def frontend_imperative_MethodDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_imperative_MethodDefinition__frontend_imperative_MethodDefinition", None)
        self.__frontend_imperative_MethodDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodParameter"):
                    opp_val = getattr(item, "MethodParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodParameter"):
                    opp_val = getattr(item, "MethodParameter", None)
                    
                    setattr(item, "MethodParameter", self)
                    

class frontend_attribution_AttributionRule(LocatedElement):

    pass
class frontend_patterns_PFeature(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class frontend_tao_SourceExpression(LocatedElement):

    pass
class RuleSelf:

    pass
class Matcher:

    pass
class core_NamedElement:

    pass
class frontend_core_ImportedModel(core_RepresentModel, core_NamedElement):

    pass
class frontend_chain_GeneratedModel(core_RepresentModel, core_NamedElement):

    pass
class frontend_chain_ExternalTransformation(chain_AvailableTransformation, core_NamedElement):

    pass
class core_LocatedElement:

    pass
class frontend_core_ModuleDefinition(core_AnnotableElement, core_LocatedElement, core_NamedElement):

    pass
class frontend_tao_Template(core_LocatedElement, core_NamedElement):

    pass
class frontend_attribution_AttributeDcl(core_LocatedElement, core_Variable, core_TypedWithClass):

    pass
class frontend_patterns_PObject(core_LocatedElement, core_Variable):

    pass
class frontend_qool_QoolQueue(core_LocatedElement, core_NamedElement):

    pass
class frontend_koan_KoanRule(core_LocatedElement, core_NamedElement):

    pass
class KoanRule:

    pass
class TraceInterface:

    pass
class Statement:

    pass
class frontend_qool_EmitStatement(Statement):

    pass
class frontend_core_Expression(Statement):

    pass
class frontend_attribution_AttributeInit(Statement):

    pass
class frontend_tao_Assignment(Statement):

    pass
class TransformationDefinition:

    pass
class frontend_attribution_AttributionTransformation(TransformationDefinition):

    pass
class frontend_mappings_MappingTransformation(TransformationDefinition):

    pass
class frontend_patterns_PatternSpecification(TransformationDefinition):

    pass
class frontend_core_EclecticTransformationDefinition(TransformationDefinition):

    pass
class frontend_imperative_ImperativeTransformation(TransformationDefinition):

    pass
class frontend_tao_TaoTransformation(TransformationDefinition):

    pass
class frontend_qool_QoolTransformation(TransformationDefinition):

    pass
class frontend_chain_ChainTransformation(TransformationDefinition):

    pass
class frontend_koan_KoanTransformation(TransformationDefinition):

    pass
class frontend_script_ScriptedTransformation(TransformationDefinition):

    pass
class frontend_DummyRootMetaclass:

    pass
class frontend_koan_Matcher(LocatedElement):

    pass
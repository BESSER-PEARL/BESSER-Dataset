from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOp(Enum):
    EQUAL = "EQUAL"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
class MappingCardinality(Enum):
    OneToOne = "OneToOne"
    NToOne = "NToOne"
    OneToN = "OneToN"
class ResolveTraceCardinality(Enum):
    ONE_ONE = "ONE_ONE"
    ZERO_OR_ONE = "ZERO_OR_ONE"
    MANY = "MANY"


############################################
# Definition of Classes
############################################

class frontend_core_KeywordParameter:

    def __init__(self, keyword: str, frontend_core_KeywordParameter: "Expression" = None):
        self.keyword = keyword
        self.frontend_core_KeywordParameter = frontend_core_KeywordParameter
        
        pass
    @property
    def keyword(self):
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
            if hasattr(old_value, "Expression274"):
                opp_val = getattr(old_value, "Expression274", None)
                if opp_val == self:
                    setattr(old_value, "Expression274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression274"):
                opp_val = getattr(value, "Expression274", None)
                setattr(value, "Expression274", self)

class KeywordParameter:

    pass
class core_Expression:

    pass
class ClosureParameter:

    pass
class frontend_core_Variable(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class frontend_core_RequireParameter(ABC):

    def __init__(self, formalParameterName: str):
        self.formalParameterName = formalParameterName
        
        pass
    @property
    def formalParameterName(self):
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
class RequireDeclaration:

    pass
class InlineModel:

    pass
class AnnotableElement:

    pass
class frontend_core_Annotation(ABC):

    pass
class SingleAnnotation:

    pass
class frontend_core_ImplicitlyAnnotableElement:

    pass
class Annotation:

    pass
class frontend_core_OptimizationsAnnotation(Annotation):

    def __init__(self, enabled: bool, Annotation245: "frontend_core_TransformationDefinition" = None, Annotation: "frontend_core_AnnotableElement" = None):
        self.enabled = enabled
        
        pass
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


class frontend_core_MetamodelModelAnnotation(Annotation):

    def __init__(self, metamodel: str, Annotation245: "frontend_core_TransformationDefinition" = None, Annotation: "frontend_core_AnnotableElement" = None):
        self.metamodel = metamodel
        
        pass
    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel


class frontend_core_AnnotableElement(ABC):

    pass
class core_AnnotableElement:

    pass
class DefinitionParameter:

    pass
class frontend_core_ModuleParameter(DefinitionParameter):

    pass
class frontend_core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class frontend_core_LocatedElement(ABC):

    def __init__(self, row: int, column: int, file: str):
        self.row = row
        self.column = column
        self.file = file
        
        pass
    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, row: int):
        self.__row = row


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column


class ImportedModel:

    pass
class ModuleDefinition:

    pass
class frontend_core_TransformationDefinition(ModuleDefinition):

    pass
class frontend_core_RepresentModel(AnnotableElement):

    pass
class frontend_core_AnnotationParameter(ABC):

    pass
class AnnotationParameter:

    pass
class frontend_core_GenericAnnotation:

    def __init__(self, name: str, frontend_core_GenericAnnotation: set["AnnotationParameter"] = None):
        self.name = name
        self.frontend_core_GenericAnnotation = frontend_core_GenericAnnotation if frontend_core_GenericAnnotation is not None else set()
        
        pass
    @property
    def name(self):
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
                    

class frontend_core_PotencyAnnotation(SingleAnnotation):

    def __init__(self, value: str, SingleAnnotation: "frontend_core_ImplicitlyAnnotableElement" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class frontend_core_SingleAnnotation(Annotation):

    pass
class ObjectSourceVariable:

    pass
class SourceExpression:

    pass
class frontend_tao_WithOptionalVariableExpression(SourceExpression):

    pass
class TemplateRootObject:

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

    def __init__(self, targetFeature: str, frontend_tao_AttributeAssigment: "SourceExpression" = None, Assignment: "frontend_tao_ObjectInstantiation" = None):
        self.targetFeature = targetFeature
        self.frontend_tao_AttributeAssigment = frontend_tao_AttributeAssigment
        
        pass
    @property
    def targetFeature(self):
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

class ReferenceAssignment:

    pass
class frontend_tao_Invocation(ReferenceAssignment):

    pass
class frontend_tao_ObjectSyntax(ReferenceAssignment):

    pass
class tao_Assignment:

    pass
class frontend_facilities_CopierCallbackDefinition:

    def __init__(self, stop: bool, frontend_facilities_CopierCallbackDefinition: "Expression" = None, frontend_facilities_CopierCallbackDefinition208: "Expression" = None):
        self.stop = stop
        self.frontend_facilities_CopierCallbackDefinition = frontend_facilities_CopierCallbackDefinition
        self.frontend_facilities_CopierCallbackDefinition208 = frontend_facilities_CopierCallbackDefinition208
        
        pass
    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, stop: bool):
        self.__stop = stop


    @property
    def frontend_facilities_CopierCallbackDefinition208(self):
        return self.__frontend_facilities_CopierCallbackDefinition208

    @frontend_facilities_CopierCallbackDefinition208.setter
    def frontend_facilities_CopierCallbackDefinition208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_facilities_CopierCallbackDefinition__frontend_facilities_CopierCallbackDefinition208", None)
        self.__frontend_facilities_CopierCallbackDefinition208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression209"):
                opp_val = getattr(old_value, "Expression209", None)
                if opp_val == self:
                    setattr(old_value, "Expression209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression209"):
                opp_val = getattr(value, "Expression209", None)
                setattr(value, "Expression209", self)

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
            if hasattr(old_value, "Expression206"):
                opp_val = getattr(old_value, "Expression206", None)
                if opp_val == self:
                    setattr(old_value, "Expression206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression206"):
                opp_val = getattr(value, "Expression206", None)
                setattr(value, "Expression206", self)

class facilities_CopierCallbackDefinition:

    pass
class Template:

    pass
class InvokeTransformation:

    pass
class frontend_qool_InvokeExternal(InvokeTransformation):

    def __init__(self, queueName: str, traceAttributeName: str, frontend_qool_InvokeExternal: "Expression" = None):
        self.queueName = queueName
        self.traceAttributeName = traceAttributeName
        self.frontend_qool_InvokeExternal = frontend_qool_InvokeExternal
        
        pass
    @property
    def traceAttributeName(self):
        return self.__traceAttributeName

    @traceAttributeName.setter
    def traceAttributeName(self, traceAttributeName: str):
        self.__traceAttributeName = traceAttributeName


    @property
    def queueName(self):
        return self.__queueName

    @queueName.setter
    def queueName(self, queueName: str):
        self.__queueName = queueName


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
            if hasattr(old_value, "Expression194"):
                opp_val = getattr(old_value, "Expression194", None)
                if opp_val == self:
                    setattr(old_value, "Expression194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression194"):
                opp_val = getattr(value, "Expression194", None)
                setattr(value, "Expression194", self)

class NamedInvocationParameter:

    pass
class InvocationParameter:

    pass
class frontend_qool_NamedInvocationParameter:

    def __init__(self, formalName: str, frontend_qool_NamedInvocationParameter: "Expression" = None):
        self.formalName = formalName
        self.frontend_qool_NamedInvocationParameter = frontend_qool_NamedInvocationParameter
        
        pass
    @property
    def formalName(self):
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
            if hasattr(old_value, "Expression197"):
                opp_val = getattr(old_value, "Expression197", None)
                if opp_val == self:
                    setattr(old_value, "Expression197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression197"):
                opp_val = getattr(value, "Expression197", None)
                setattr(value, "Expression197", self)

class TransformationDefinitionParameter:

    pass
class frontend_qool_InvocationParameter:

    def __init__(self, calleeModelName: str, frontend_qool_InvocationParameter: "TransformationDefinitionParameter" = None):
        self.calleeModelName = calleeModelName
        self.frontend_qool_InvocationParameter = frontend_qool_InvocationParameter
        
        pass
    @property
    def calleeModelName(self):
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

class frontend_qool_InvokeInternal(InvokeTransformation):

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
class frontend_qool_QueueOptimization(ABC):

    pass
class QueueOptimization:

    pass
class frontend_qool_AccessByFeatureOptimization(QueueOptimization):

    def __init__(self, featureName: str, force: bool, QueueOptimization: "frontend_qool_QoolQueue" = None):
        self.featureName = featureName
        self.force = force
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def force(self):
        return self.__force

    @force.setter
    def force(self, force: bool):
        self.__force = force


class frontend_qool_MatchPredicate(ABC):

    pass
class MatchPredicate:

    pass
class frontend_qool_PropertyEqualsPredicate(MatchPredicate):

    def __init__(self, propertyName: str, frontend_qool_PropertyEqualsPredicate: "Expression" = None, MatchPredicate: "frontend_qool_MatchExpression" = None):
        self.propertyName = propertyName
        self.frontend_qool_PropertyEqualsPredicate = frontend_qool_PropertyEqualsPredicate
        
        pass
    @property
    def propertyName(self):
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
            if hasattr(old_value, "Expression180"):
                opp_val = getattr(old_value, "Expression180", None)
                if opp_val == self:
                    setattr(old_value, "Expression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression180"):
                opp_val = getattr(value, "Expression180", None)
                setattr(value, "Expression180", self)

class frontend_qool_KindOfPredicate(MatchPredicate):

    pass
class mappings_MetamodelElementRef:

    pass
class MetamodelElementRef:

    pass
class frontend_mappings_AttributeRef(MetamodelElementRef):

    def __init__(self, featureName: str, multivalued: bool, frontend_mappings_AttributeRef: "MatchedElement" = None):
        self.featureName = featureName
        self.multivalued = multivalued
        self.frontend_mappings_AttributeRef = frontend_mappings_AttributeRef
        
        pass
    @property
    def multivalued(self):
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued


    @property
    def featureName(self):
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
            if hasattr(old_value, "MatchedElement144"):
                opp_val = getattr(old_value, "MatchedElement144", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement144"):
                opp_val = getattr(value, "MatchedElement144", None)
                setattr(value, "MatchedElement144", self)

class frontend_mappings_ClassRef(MetamodelElementRef):

    pass
class frontend_mappings_MetamodelElementRef(ABC):

    pass
class DefaultValue:

    pass
class frontend_mappings_IntDefaultValue(DefaultValue):

    def __init__(self, defaultValue: str):
        self.defaultValue = defaultValue
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


class Segment:

    pass
class QoolQueue:

    pass
class frontend_qool_ModelElementQueue(QoolQueue):

    pass
class frontend_qool_LocalQueue(QoolQueue):

    pass
class frontend_mappings_ReferenceRef(MetamodelElementRef):

    def __init__(self, featureName: str, multivalued: bool, frontend_mappings_ReferenceRef: "MatchedElement" = None):
        self.featureName = featureName
        self.multivalued = multivalued
        self.frontend_mappings_ReferenceRef = frontend_mappings_ReferenceRef
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def multivalued(self):
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
            if hasattr(old_value, "MatchedElement146"):
                opp_val = getattr(old_value, "MatchedElement146", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement146"):
                opp_val = getattr(value, "MatchedElement146", None)
                setattr(value, "MatchedElement146", self)

class AttributeModifier:

    pass
class frontend_mappings_DefaultValue(AttributeModifier):

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
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def multivalued(self):
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
            if hasattr(old_value, "MatchedElement142"):
                opp_val = getattr(old_value, "MatchedElement142", None)
                if opp_val == self:
                    setattr(old_value, "MatchedElement142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedElement142"):
                opp_val = getattr(value, "MatchedElement142", None)
                setattr(value, "MatchedElement142", self)

class frontend_mappings_Attribute2Attribute(mappings_AttributeRightPart, mappings_Feature2Feature):

    def __init__(self, cardinality: str, scopedAttributes: "Class2Class" = None, frontend_mappings_Attribute2Attribute: set["AttributeRef"] = None, frontend_mappings_Attribute2Attribute134: set["AttributeModifier"] = None):
        self.cardinality = cardinality
        self.scopedAttributes = scopedAttributes
        self.frontend_mappings_Attribute2Attribute = frontend_mappings_Attribute2Attribute if frontend_mappings_Attribute2Attribute is not None else set()
        self.frontend_mappings_Attribute2Attribute134 = frontend_mappings_Attribute2Attribute134 if frontend_mappings_Attribute2Attribute134 is not None else set()
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality


    @property
    def frontend_mappings_Attribute2Attribute134(self):
        return self.__frontend_mappings_Attribute2Attribute134

    @frontend_mappings_Attribute2Attribute134.setter
    def frontend_mappings_Attribute2Attribute134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Attribute2Attribute__frontend_mappings_Attribute2Attribute134", None)
        self.__frontend_mappings_Attribute2Attribute134 = value if value is not None else set()
        
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
    def scopedAttributes(self):
        return self.__scopedAttributes

    @scopedAttributes.setter
    def scopedAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Attribute2Attribute__scopedAttributes", None)
        self.__scopedAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class2Class"):
                opp_val = getattr(old_value, "Class2Class", None)
                if opp_val == self:
                    setattr(old_value, "Class2Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class2Class"):
                opp_val = getattr(value, "Class2Class", None)
                setattr(value, "Class2Class", self)

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
                if hasattr(item, "AttributeRef132"):
                    opp_val = getattr(item, "AttributeRef132", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeRef132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeRef132"):
                    opp_val = getattr(item, "AttributeRef132", None)
                    
                    setattr(item, "AttributeRef132", self)
                    

class Operator:

    pass
class frontend_mappings_Join(Operator):

    pass
class frontend_mappings_Split(Operator):

    pass
class frontend_mappings_ConvertModifier(AttributeModifier):

    def __init__(self, converter: str, AttributeModifier: "frontend_mappings_Attribute2Attribute" = None):
        self.converter = converter
        
        pass
    @property
    def converter(self):
        return self.__converter

    @converter.setter
    def converter(self, converter: str):
        self.__converter = converter


class Modifier:

    pass
class frontend_mappings_AttributeModifier(Modifier):

    pass
class frontend_mappings_Modifier(ABC):

    pass
class ClassRef:

    pass
class ReferenceRef:

    pass
class ClassMapping:

    pass
class frontend_mappings_Class2Class(ClassMapping):

    def __init__(self, cardinality: str, frontend_mappings_Class2Class115: set["ClassRef"] = None, context: set["Attribute2Attribute"] = None, frontend_mappings_Class2Class: set["C2CModifier"] = None, frontend_mappings_Class2Class113: set["ClassRef"] = None, ClassMapping: "frontend_mappings_Split" = None, ClassMapping129: "frontend_mappings_Join" = None):
        self.cardinality = cardinality
        self.frontend_mappings_Class2Class115 = frontend_mappings_Class2Class115 if frontend_mappings_Class2Class115 is not None else set()
        self.context = context if context is not None else set()
        self.frontend_mappings_Class2Class = frontend_mappings_Class2Class if frontend_mappings_Class2Class is not None else set()
        self.frontend_mappings_Class2Class113 = frontend_mappings_Class2Class113 if frontend_mappings_Class2Class113 is not None else set()
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Class2Class__context", None)
        self.__context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute2Attribute"):
                    opp_val = getattr(item, "Attribute2Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute2Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute2Attribute"):
                    opp_val = getattr(item, "Attribute2Attribute", None)
                    
                    setattr(item, "Attribute2Attribute", self)
                    

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
                    

class NamedElement:

    pass
class frontend_core_DefinitionParameter(NamedElement):

    pass
class frontend_qool_Segment(NamedElement):

    pass
class frontend_mappings_Tag(NamedElement):

    pass
class frontend_mappings_Converter:

    def __init__(self, isExternal: str, converterName: str, frontend_mappings_Converter: "UseDeclaration" = None):
        self.isExternal = isExternal
        self.converterName = converterName
        self.frontend_mappings_Converter = frontend_mappings_Converter
        
        pass
    @property
    def converterName(self):
        return self.__converterName

    @converterName.setter
    def converterName(self, converterName: str):
        self.__converterName = converterName


    @property
    def isExternal(self):
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal


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

class ResolveLink:

    pass
class Attribute2Attribute:

    pass
class Section:

    pass
class C2CModifier:

    pass
class frontend_mappings_RelatedBy(C2CModifier):

    pass
class frontend_mappings_LinkedBy(C2CModifier):

    pass
class frontend_mappings_EqualityFilter(C2CModifier):

    def __init__(self, filter: str, frontend_mappings_EqualityFilter: "AttributeRef" = None, C2CModifier111: "frontend_mappings_Class2Class" = None, C2CModifier: "frontend_mappings_Context" = None):
        self.filter = filter
        self.frontend_mappings_EqualityFilter = frontend_mappings_EqualityFilter
        
        pass
    @property
    def filter(self):
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

class MappingElement:

    pass
class frontend_mappings_C2CModifier(MappingElement):

    pass
class Tag:

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
class frontend_mappings_AttributeRightPart(ABC):

    pass
class AttributeRightPart:

    pass
class frontend_mappings_AttributeIsInteger(AttributeRightPart):

    def __init__(self, intValue: int, AttributeRightPart: "frontend_mappings_AttributeMapping" = None):
        self.intValue = intValue
        
        pass
    @property
    def intValue(self):
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue


class frontend_mappings_AttributeIsDouble(AttributeRightPart):

    def __init__(self, doubleValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping" = None):
        self.doubleValue = doubleValue
        
        pass
    @property
    def doubleValue(self):
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: str):
        self.__doubleValue = doubleValue


class frontend_mappings_AttributeIsString(AttributeRightPart):

    def __init__(self, strValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping" = None):
        self.strValue = strValue
        
        pass
    @property
    def strValue(self):
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue


class frontend_mappings_AttributeIsBoolean(AttributeRightPart):

    def __init__(self, boolValue: str, AttributeRightPart: "frontend_mappings_AttributeMapping" = None):
        self.boolValue = boolValue
        
        pass
    @property
    def boolValue(self):
        return self.__boolValue

    @boolValue.setter
    def boolValue(self, boolValue: str):
        self.__boolValue = boolValue


class frontend_mappings_AttributeIsResolveLink(AttributeRightPart):

    pass
class AttributeRef:

    pass
class Feature2Feature:

    pass
class frontend_mappings_Reference2Reference(Feature2Feature):

    def __init__(self, resolverName: str, cardinality: str, frontend_mappings_Reference2Reference: set["ReferenceRef"] = None, frontend_mappings_Reference2Reference137: set["ReferenceRef"] = None):
        self.resolverName = resolverName
        self.cardinality = cardinality
        self.frontend_mappings_Reference2Reference = frontend_mappings_Reference2Reference if frontend_mappings_Reference2Reference is not None else set()
        self.frontend_mappings_Reference2Reference137 = frontend_mappings_Reference2Reference137 if frontend_mappings_Reference2Reference137 is not None else set()
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality


    @property
    def resolverName(self):
        return self.__resolverName

    @resolverName.setter
    def resolverName(self, resolverName: str):
        self.__resolverName = resolverName


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
                    

    @property
    def frontend_mappings_Reference2Reference137(self):
        return self.__frontend_mappings_Reference2Reference137

    @frontend_mappings_Reference2Reference137.setter
    def frontend_mappings_Reference2Reference137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_mappings_Reference2Reference__frontend_mappings_Reference2Reference137", None)
        self.__frontend_mappings_Reference2Reference137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReferenceRef138"):
                    opp_val = getattr(item, "ReferenceRef138", None)
                    
                    if opp_val == self:
                        setattr(item, "ReferenceRef138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReferenceRef138"):
                    opp_val = getattr(item, "ReferenceRef138", None)
                    
                    setattr(item, "ReferenceRef138", self)
                    

class frontend_mappings_AttributeMapping(Feature2Feature):

    pass
class Converter:

    pass
class FeatureRef:

    pass
class frontend_mappings_Feature2Feature(MappingElement):

    pass
class frontend_mappings_ClassMapping(MappingElement):

    pass
class frontend_patterns_POutputVariable:

    pass
class POutputVariable:

    pass
class PObject:

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
class frontend_core_RequireDeclaration(RepresentModel):

    def __init__(self, name: str, default: str, frontend_core_RequireDeclaration: set["RequireParameter"] = None, RepresentModel302: "frontend_core_ClassUse" = None, RepresentModel254: "frontend_core_RequireModelParameter" = None, RepresentModel: "frontend_chain_TransformationExecution" = None, RepresentModel58: "frontend_chain_TransformationExecution" = None):
        self.name = name
        self.default = default
        self.frontend_core_RequireDeclaration = frontend_core_RequireDeclaration if frontend_core_RequireDeclaration is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


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
                    

class frontend_core_UseDeclaration(RepresentModel):

    def __init__(self, module: str, as_: str, RepresentModel302: "frontend_core_ClassUse" = None, RepresentModel254: "frontend_core_RequireModelParameter" = None, RepresentModel: "frontend_chain_TransformationExecution" = None, RepresentModel58: "frontend_chain_TransformationExecution" = None):
        self.module = module
        self.as_ = as_
        
        pass
    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, module: str):
        self.__module = module


    @property
    def as_(self):
        return self.__as_

    @as_.setter
    def as_(self, as_: str):
        self.__as_ = as_


class AvailableTransformation:

    pass
class Delegate:

    pass
class PReference:

    pass
class frontend_patterns_CollectionReference(PReference):

    pass
class PFeature:

    pass
class frontend_patterns_PReference(PFeature):

    pass
class frontend_patterns_PAttribute(PFeature):

    pass
class MethodSelf:

    pass
class MethodParameter:

    pass
class MethodDefinition:

    pass
class Variable:

    pass
class frontend_tao_TemplateParameter(Variable):

    pass
class frontend_mappings_MappingVariable(Variable):

    pass
class frontend_tao_ObjectSourceVariable(Variable):

    pass
class frontend_core_ClosureParameter(Variable):

    pass
class frontend_attribution_RuleSelf(Variable):

    pass
class Expression:

    pass
class frontend_core_MethodCall(Expression):

    def __init__(self, methodName: str, withParameters: bool, frontend_core_MethodCall: "Expression" = None, frontend_core_MethodCall267: set["Expression"] = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.methodName = methodName
        self.withParameters = withParameters
        self.frontend_core_MethodCall = frontend_core_MethodCall
        self.frontend_core_MethodCall267 = frontend_core_MethodCall267 if frontend_core_MethodCall267 is not None else set()
        
        pass
    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def withParameters(self):
        return self.__withParameters

    @withParameters.setter
    def withParameters(self, withParameters: bool):
        self.__withParameters = withParameters


    @property
    def frontend_core_MethodCall267(self):
        return self.__frontend_core_MethodCall267

    @frontend_core_MethodCall267.setter
    def frontend_core_MethodCall267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MethodCall__frontend_core_MethodCall267", None)
        self.__frontend_core_MethodCall267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression268"):
                    opp_val = getattr(item, "Expression268", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression268"):
                    opp_val = getattr(item, "Expression268", None)
                    
                    setattr(item, "Expression268", self)
                    

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
            if hasattr(old_value, "Expression265"):
                opp_val = getattr(old_value, "Expression265", None)
                if opp_val == self:
                    setattr(old_value, "Expression265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression265"):
                opp_val = getattr(value, "Expression265", None)
                setattr(value, "Expression265", self)

class frontend_facilities_Copier(Expression):

    pass
class frontend_core_ResolveLink(Expression):

    def __init__(self, isExternal: str, linkName: str, featureName: str, frontend_core_ResolveLink: "Expression" = None, frontend_core_ResolveLink287: "UseDeclaration" = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.isExternal = isExternal
        self.linkName = linkName
        self.featureName = featureName
        self.frontend_core_ResolveLink = frontend_core_ResolveLink
        self.frontend_core_ResolveLink287 = frontend_core_ResolveLink287
        
        pass
    @property
    def isExternal(self):
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal


    @property
    def linkName(self):
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def frontend_core_ResolveLink287(self):
        return self.__frontend_core_ResolveLink287

    @frontend_core_ResolveLink287.setter
    def frontend_core_ResolveLink287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_ResolveLink__frontend_core_ResolveLink287", None)
        self.__frontend_core_ResolveLink287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseDeclaration288"):
                opp_val = getattr(old_value, "UseDeclaration288", None)
                if opp_val == self:
                    setattr(old_value, "UseDeclaration288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseDeclaration288"):
                opp_val = getattr(value, "UseDeclaration288", None)
                setattr(value, "UseDeclaration288", self)

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
            if hasattr(old_value, "Expression285"):
                opp_val = getattr(old_value, "Expression285", None)
                if opp_val == self:
                    setattr(old_value, "Expression285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression285"):
                opp_val = getattr(value, "Expression285", None)
                setattr(value, "Expression285", self)

class frontend_attribution_AttributeUse(Expression):

    pass
class frontend_core_VariableReference(Expression):

    pass
class frontend_qool_MatchExpression(Expression):

    pass
class frontend_qool_InvokeTransformation(Expression):

    def __init__(self, transformationName: str, entryPointName: str, frontend_qool_InvokeTransformation: set["InvocationParameter"] = None, frontend_qool_InvokeTransformation183: set["InvocationParameter"] = None, frontend_qool_InvokeTransformation186: set["NamedInvocationParameter"] = None, frontend_qool_InvokeTransformation188: "Variable" = None, frontend_qool_InvokeTransformation191: set["Expression"] = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.transformationName = transformationName
        self.entryPointName = entryPointName
        self.frontend_qool_InvokeTransformation = frontend_qool_InvokeTransformation if frontend_qool_InvokeTransformation is not None else set()
        self.frontend_qool_InvokeTransformation183 = frontend_qool_InvokeTransformation183 if frontend_qool_InvokeTransformation183 is not None else set()
        self.frontend_qool_InvokeTransformation186 = frontend_qool_InvokeTransformation186 if frontend_qool_InvokeTransformation186 is not None else set()
        self.frontend_qool_InvokeTransformation188 = frontend_qool_InvokeTransformation188
        self.frontend_qool_InvokeTransformation191 = frontend_qool_InvokeTransformation191 if frontend_qool_InvokeTransformation191 is not None else set()
        
        pass
    @property
    def entryPointName(self):
        return self.__entryPointName

    @entryPointName.setter
    def entryPointName(self, entryPointName: str):
        self.__entryPointName = entryPointName


    @property
    def transformationName(self):
        return self.__transformationName

    @transformationName.setter
    def transformationName(self, transformationName: str):
        self.__transformationName = transformationName


    @property
    def frontend_qool_InvokeTransformation186(self):
        return self.__frontend_qool_InvokeTransformation186

    @frontend_qool_InvokeTransformation186.setter
    def frontend_qool_InvokeTransformation186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation186", None)
        self.__frontend_qool_InvokeTransformation186 = value if value is not None else set()
        
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
                    

    @property
    def frontend_qool_InvokeTransformation188(self):
        return self.__frontend_qool_InvokeTransformation188

    @frontend_qool_InvokeTransformation188.setter
    def frontend_qool_InvokeTransformation188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation188", None)
        self.__frontend_qool_InvokeTransformation188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable189"):
                opp_val = getattr(old_value, "Variable189", None)
                if opp_val == self:
                    setattr(old_value, "Variable189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable189"):
                opp_val = getattr(value, "Variable189", None)
                setattr(value, "Variable189", self)

    @property
    def frontend_qool_InvokeTransformation183(self):
        return self.__frontend_qool_InvokeTransformation183

    @frontend_qool_InvokeTransformation183.setter
    def frontend_qool_InvokeTransformation183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation183", None)
        self.__frontend_qool_InvokeTransformation183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvocationParameter184"):
                    opp_val = getattr(item, "InvocationParameter184", None)
                    
                    if opp_val == self:
                        setattr(item, "InvocationParameter184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvocationParameter184"):
                    opp_val = getattr(item, "InvocationParameter184", None)
                    
                    setattr(item, "InvocationParameter184", self)
                    

    @property
    def frontend_qool_InvokeTransformation191(self):
        return self.__frontend_qool_InvokeTransformation191

    @frontend_qool_InvokeTransformation191.setter
    def frontend_qool_InvokeTransformation191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_qool_InvokeTransformation__frontend_qool_InvokeTransformation191", None)
        self.__frontend_qool_InvokeTransformation191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression192"):
                    opp_val = getattr(item, "Expression192", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression192"):
                    opp_val = getattr(item, "Expression192", None)
                    
                    setattr(item, "Expression192", self)
                    

class frontend_core_NumLiteral(Expression):

    def __init__(self, value: int, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class frontend_core_ClosureDeclaration(Expression):

    pass
class frontend_core_BinaryExpr(Expression):

    def __init__(self, binaryOp: str, frontend_core_BinaryExpr278: "Expression" = None, frontend_core_BinaryExpr: "Expression" = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.binaryOp = binaryOp
        self.frontend_core_BinaryExpr278 = frontend_core_BinaryExpr278
        self.frontend_core_BinaryExpr = frontend_core_BinaryExpr
        
        pass
    @property
    def binaryOp(self):
        return self.__binaryOp

    @binaryOp.setter
    def binaryOp(self, binaryOp: str):
        self.__binaryOp = binaryOp


    @property
    def frontend_core_BinaryExpr278(self):
        return self.__frontend_core_BinaryExpr278

    @frontend_core_BinaryExpr278.setter
    def frontend_core_BinaryExpr278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_BinaryExpr__frontend_core_BinaryExpr278", None)
        self.__frontend_core_BinaryExpr278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression279"):
                opp_val = getattr(old_value, "Expression279", None)
                if opp_val == self:
                    setattr(old_value, "Expression279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression279"):
                opp_val = getattr(value, "Expression279", None)
                setattr(value, "Expression279", self)

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
            if hasattr(old_value, "Expression276"):
                opp_val = getattr(old_value, "Expression276", None)
                if opp_val == self:
                    setattr(old_value, "Expression276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression276"):
                opp_val = getattr(value, "Expression276", None)
                setattr(value, "Expression276", self)

class frontend_core_PropertyWrite(Expression):

    def __init__(self, _property: str, frontend_core_PropertyWrite: "Variable" = None, frontend_core_PropertyWrite260: "Expression" = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self._property = _property
        self.frontend_core_PropertyWrite = frontend_core_PropertyWrite
        self.frontend_core_PropertyWrite260 = frontend_core_PropertyWrite260
        
        pass
    @property
    def _property(self):
        return self.___property

    @_property.setter
    def _property(self, _property: str):
        self.___property = _property


    @property
    def frontend_core_PropertyWrite260(self):
        return self.__frontend_core_PropertyWrite260

    @frontend_core_PropertyWrite260.setter
    def frontend_core_PropertyWrite260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_PropertyWrite__frontend_core_PropertyWrite260", None)
        self.__frontend_core_PropertyWrite260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression261"):
                opp_val = getattr(old_value, "Expression261", None)
                if opp_val == self:
                    setattr(old_value, "Expression261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression261"):
                opp_val = getattr(value, "Expression261", None)
                setattr(value, "Expression261", self)

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
            if hasattr(old_value, "Variable258"):
                opp_val = getattr(old_value, "Variable258", None)
                if opp_val == self:
                    setattr(old_value, "Variable258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable258"):
                opp_val = getattr(value, "Variable258", None)
                setattr(value, "Variable258", self)

class frontend_core_KeywordMethodCall(Expression):

    pass
class RuleSelf:

    pass
class core_RepresentModel:

    pass
class frontend_core_TransformationDefinitionParameter(core_DefinitionParameter, core_RepresentModel):

    pass
class TransformationExecution:

    pass
class GeneratedModel:

    pass
class ExternalTransformation:

    pass
class CompositeTransformation:

    pass
class frontend_imperative_MethodParameter(Variable):

    pass
class frontend_imperative_MethodSelf(Variable):

    pass
class Matcher:

    pass
class core_NamedElement:

    pass
class frontend_core_ImportedModel(core_NamedElement, core_RepresentModel):

    pass
class frontend_chain_ExternalTransformation(chain_AvailableTransformation, core_NamedElement):

    pass
class frontend_chain_GeneratedModel(core_NamedElement, core_RepresentModel):

    pass
class core_LocatedElement:

    pass
class frontend_tao_Template(core_NamedElement, core_LocatedElement):

    pass
class frontend_qool_QoolQueue(core_NamedElement, core_LocatedElement):

    pass
class frontend_core_ModuleDefinition(core_NamedElement, core_AnnotableElement, core_LocatedElement):

    pass
class frontend_koan_KoanRule(core_NamedElement, core_LocatedElement):

    pass
class KoanRule:

    pass
class TraceInterface:

    pass
class Statement:

    pass
class frontend_tao_Assignment(Statement):

    pass
class frontend_qool_EmitStatement(Statement):

    pass
class frontend_core_Expression(Statement):

    pass
class frontend_attribution_AttributeInit(Statement):

    pass
class TransformationDefinition:

    pass
class frontend_qool_QoolTransformation(TransformationDefinition):

    pass
class frontend_patterns_PatternSpecification(TransformationDefinition):

    pass
class frontend_chain_ChainTransformation(TransformationDefinition):

    pass
class frontend_koan_KoanTransformation(TransformationDefinition):

    pass
class frontend_core_EclecticTransformationDefinition(TransformationDefinition):

    pass
class frontend_mappings_MappingTransformation(TransformationDefinition):

    pass
class frontend_imperative_ImperativeTransformation(TransformationDefinition):

    pass
class frontend_tao_TaoTransformation(TransformationDefinition):

    pass
class frontend_script_ScriptedTransformation(TransformationDefinition):

    pass
class frontend_DummyRootMetaclass:

    pass
class frontend_core_PutTraceParameter:

    pass
class PutTraceParameter:

    pass
class frontend_core_PutTrace(Expression):

    pass
class frontend_core_InlineFeature(NamedElement):

    def __init__(self, multivalued: bool, frontend_core_InlineFeature: "TypeExpression" = None):
        self.multivalued = multivalued
        self.frontend_core_InlineFeature = frontend_core_InlineFeature
        
        pass
    @property
    def multivalued(self):
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
            if hasattr(old_value, "TypeExpression314"):
                opp_val = getattr(old_value, "TypeExpression314", None)
                if opp_val == self:
                    setattr(old_value, "TypeExpression314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeExpression314"):
                opp_val = getattr(value, "TypeExpression314", None)
                setattr(value, "TypeExpression314", self)

class InlineFeature:

    pass
class frontend_core_InlineClass(NamedElement):

    pass
class InlineClass:

    pass
class core_ModuleDefinition:

    pass
class frontend_core_InlineModel(core_ModuleDefinition, core_RepresentModel):

    pass
class frontend_core_TraceElement(NamedElement):

    pass
class TraceElement:

    pass
class frontend_core_TraceDefinition(NamedElement):

    pass
class frontend_core_TracedModelParameter(core_DefinitionParameter, core_RepresentModel):

    pass
class frontend_core_TraceInterface(ModuleDefinition):

    pass
class frontend_core_TypedWithClass(ABC):

    pass
class TraceDefinition:

    pass
class frontend_core_TraceUse(TypeExpression):

    pass
class frontend_core_TraceCompareExpression:

    def __init__(self, multivaluedTag: bool, frontend_core_TraceCompareExpression: "TraceElement" = None, frontend_core_TraceCompareExpression322: "Expression" = None):
        self.multivaluedTag = multivaluedTag
        self.frontend_core_TraceCompareExpression = frontend_core_TraceCompareExpression
        self.frontend_core_TraceCompareExpression322 = frontend_core_TraceCompareExpression322
        
        pass
    @property
    def multivaluedTag(self):
        return self.__multivaluedTag

    @multivaluedTag.setter
    def multivaluedTag(self, multivaluedTag: bool):
        self.__multivaluedTag = multivaluedTag


    @property
    def frontend_core_TraceCompareExpression322(self):
        return self.__frontend_core_TraceCompareExpression322

    @frontend_core_TraceCompareExpression322.setter
    def frontend_core_TraceCompareExpression322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_TraceCompareExpression__frontend_core_TraceCompareExpression322", None)
        self.__frontend_core_TraceCompareExpression322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression323"):
                opp_val = getattr(old_value, "Expression323", None)
                if opp_val == self:
                    setattr(old_value, "Expression323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression323"):
                opp_val = getattr(value, "Expression323", None)
                setattr(value, "Expression323", self)

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
            if hasattr(old_value, "TraceElement320"):
                opp_val = getattr(old_value, "TraceElement320", None)
                if opp_val == self:
                    setattr(old_value, "TraceElement320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceElement320"):
                opp_val = getattr(value, "TraceElement320", None)
                setattr(value, "TraceElement320", self)

class TraceCompareExpression:

    pass
class frontend_core_MatchTrace(Expression):

    def __init__(self, cardinality: str, frontend_core_MatchTrace: "TraceDefinition" = None, frontend_core_MatchTrace318: "TraceCompareExpression" = None, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.cardinality = cardinality
        self.frontend_core_MatchTrace = frontend_core_MatchTrace
        self.frontend_core_MatchTrace318 = frontend_core_MatchTrace318
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality


    @property
    def frontend_core_MatchTrace318(self):
        return self.__frontend_core_MatchTrace318

    @frontend_core_MatchTrace318.setter
    def frontend_core_MatchTrace318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frontend_core_MatchTrace__frontend_core_MatchTrace318", None)
        self.__frontend_core_MatchTrace318 = value
        
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
            if hasattr(old_value, "TraceDefinition316"):
                opp_val = getattr(old_value, "TraceDefinition316", None)
                if opp_val == self:
                    setattr(old_value, "TraceDefinition316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceDefinition316"):
                opp_val = getattr(value, "TraceDefinition316", None)
                setattr(value, "TraceDefinition316", self)

class frontend_core_InlineReference(InlineFeature):

    pass
class frontend_core_InlineAttribute(InlineFeature):

    pass
class frontend_core_IfBranch:

    pass
class IfBranch:

    pass
class frontend_core_IfExpr(Expression):

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
        
        pass
    @property
    def strictType(self):
        return self.__strictType

    @strictType.setter
    def strictType(self, strictType: bool):
        self.__strictType = strictType


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


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
            if hasattr(old_value, "RepresentModel302"):
                opp_val = getattr(old_value, "RepresentModel302", None)
                if opp_val == self:
                    setattr(old_value, "RepresentModel302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentModel302"):
                opp_val = getattr(value, "RepresentModel302", None)
                setattr(value, "RepresentModel302", self)

class frontend_core_TypeExpression(ABC):

    pass
class frontend_core_BooleanLiteral(Expression):

    def __init__(self, value: bool, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class frontend_core_StringLiteral(Expression):

    def __init__(self, value: str, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class frontend_core_DoubleLiteral(Expression):

    def __init__(self, value: float, Expression72: "frontend_patterns_PAttribute" = None, Expression197: "frontend_qool_NamedInvocationParameter" = None, Expression270: "frontend_core_KeywordMethodCall" = None, Expression297: "frontend_core_IfBranch" = None, Expression274: "frontend_core_KeywordParameter" = None, Expression285: "frontend_core_ResolveLink" = None, Expression192: "frontend_qool_InvokeTransformation" = None, Expression27: "frontend_attribution_AttributeInit" = None, Expression194: "frontend_qool_InvokeExternal" = None, Expression160: "frontend_qool_IteratorStatement" = None, Expression276: "frontend_core_BinaryExpr" = None, Expression209: "frontend_facilities_CopierCallbackDefinition" = None, Expression268: "frontend_core_MethodCall" = None, Expression329: "frontend_core_PutTraceParameter" = None, Expression261: "frontend_core_PropertyWrite" = None, Expression256: "frontend_core_DefineVariable" = None, Expression323: "frontend_core_TraceCompareExpression" = None, Expression30: "frontend_attribution_AttributeInit" = None, Expression167: "frontend_qool_ForEachStatement" = None, Expression206: "frontend_facilities_CopierCallbackDefinition" = None, Expression32: "frontend_attribution_AttributeUse" = None, Expression172: "frontend_qool_EmitStatement" = None, Expression: "frontend_attribution_AttributionRule" = None, Expression279: "frontend_core_BinaryExpr" = None, Expression199: "frontend_facilities_Copier" = None, Expression265: "frontend_core_MethodCall" = None, Expression180: "frontend_qool_PropertyEqualsPredicate" = None, Expression224: "frontend_tao_WithOptionalVariableExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


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
class frontend_attribution_AttributionTransformation(TransformationDefinition):

    pass
class ClassUse:

    pass
class core_Variable:

    pass
class frontend_core_DefineVariable(core_Variable, core_Statement):

    pass
class frontend_qool_IteratorStatement(core_Variable, core_Statement):

    pass
class frontend_patterns_PObject(core_Variable, core_LocatedElement):

    pass
class frontend_tao_ReferenceAssignment(core_Variable, tao_Assignment):

    def __init__(self, targetFeature: str, multivalued: bool, frontend_tao_ReferenceAssignment: "SourceExpression" = None):
        self.targetFeature = targetFeature
        self.multivalued = multivalued
        self.frontend_tao_ReferenceAssignment = frontend_tao_ReferenceAssignment
        
        pass
    @property
    def targetFeature(self):
        return self.__targetFeature

    @targetFeature.setter
    def targetFeature(self, targetFeature: str):
        self.__targetFeature = targetFeature


    @property
    def multivalued(self):
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued


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
            if hasattr(old_value, "SourceExpression226"):
                opp_val = getattr(old_value, "SourceExpression226", None)
                if opp_val == self:
                    setattr(old_value, "SourceExpression226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceExpression226"):
                opp_val = getattr(value, "SourceExpression226", None)
                setattr(value, "SourceExpression226", self)

class frontend_tao_ObjectInstantiation(core_Variable, core_Statement):

    pass
class frontend_attribution_AttributeDcl(core_TypedWithClass, core_Variable, core_LocatedElement):

    pass
class koan_Matcher:

    pass
class frontend_koan_ForAllMatcher(koan_Matcher, core_Variable):

    pass
class LocatedElement:

    pass
class frontend_core_Statement(LocatedElement):

    pass
class frontend_patterns_PFeature(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class frontend_mappings_Operator(LocatedElement):

    pass
class frontend_mappings_MappingElement(LocatedElement):

    pass
class frontend_chain_TransformationExecution(LocatedElement):

    pass
class frontend_mappings_Delegate(LocatedElement):

    def __init__(self, isExternal: str, linkName: str, featureName: str, frontend_mappings_Delegate: set["MatchedElement"] = None, frontend_mappings_Delegate82: "UseDeclaration" = None, frontend_mappings_Delegate84: set["Tag"] = None):
        self.isExternal = isExternal
        self.linkName = linkName
        self.featureName = featureName
        self.frontend_mappings_Delegate = frontend_mappings_Delegate if frontend_mappings_Delegate is not None else set()
        self.frontend_mappings_Delegate82 = frontend_mappings_Delegate82
        self.frontend_mappings_Delegate84 = frontend_mappings_Delegate84 if frontend_mappings_Delegate84 is not None else set()
        
        pass
    @property
    def isExternal(self):
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def linkName(self):
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName


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
                    

class frontend_imperative_MethodDefinition(LocatedElement):

    def __init__(self, name: str, frontend_imperative_MethodDefinition39: "MethodSelf" = None, frontend_imperative_MethodDefinition41: "ClassUse" = None, frontend_imperative_MethodDefinition44: set["Statement"] = None, frontend_imperative_MethodDefinition: set["MethodParameter"] = None):
        self.name = name
        self.frontend_imperative_MethodDefinition39 = frontend_imperative_MethodDefinition39
        self.frontend_imperative_MethodDefinition41 = frontend_imperative_MethodDefinition41
        self.frontend_imperative_MethodDefinition44 = frontend_imperative_MethodDefinition44 if frontend_imperative_MethodDefinition44 is not None else set()
        self.frontend_imperative_MethodDefinition = frontend_imperative_MethodDefinition if frontend_imperative_MethodDefinition is not None else set()
        
        pass
    @property
    def name(self):
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
                    

class frontend_mappings_Context(LocatedElement):

    pass
class frontend_patterns_Pattern(LocatedElement):

    def __init__(self, name: str, frontend_patterns_Pattern: set["PObject"] = None, frontend_patterns_Pattern64: set["POutputVariable"] = None):
        self.name = name
        self.frontend_patterns_Pattern = frontend_patterns_Pattern if frontend_patterns_Pattern is not None else set()
        self.frontend_patterns_Pattern64 = frontend_patterns_Pattern64 if frontend_patterns_Pattern64 is not None else set()
        
        pass
    @property
    def name(self):
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
                    

class frontend_attribution_AttributionRule(LocatedElement):

    pass
class frontend_mappings_Section(LocatedElement):

    def __init__(self, sectionType: str, frontend_mappings_Section: set["MappingElement"] = None):
        self.sectionType = sectionType
        self.frontend_mappings_Section = frontend_mappings_Section if frontend_mappings_Section is not None else set()
        
        pass
    @property
    def sectionType(self):
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
                    

class frontend_tao_SourceExpression(LocatedElement):

    pass
class frontend_koan_Matcher(LocatedElement):

    pass
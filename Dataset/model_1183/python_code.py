from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class gbind_dsl_BaseHelper:

    def __init__(self, feature: str, BindingModel286: "BindingModel" = None, gbind_dsl_BaseHelper: "OclExpression" = None, gbind_dsl_BaseHelper283: "OclType" = None):
        self.feature = feature
        self.BindingModel286 = BindingModel286
        self.gbind_dsl_BaseHelper = gbind_dsl_BaseHelper
        self.gbind_dsl_BaseHelper283 = gbind_dsl_BaseHelper283
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def gbind_dsl_BaseHelper(self):
        return self.__gbind_dsl_BaseHelper

    @gbind_dsl_BaseHelper.setter
    def gbind_dsl_BaseHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__gbind_dsl_BaseHelper", None)
        self.__gbind_dsl_BaseHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression281"):
                opp_val = getattr(old_value, "OclExpression281", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression281"):
                opp_val = getattr(value, "OclExpression281", None)
                setattr(value, "OclExpression281", self)

    @property
    def gbind_dsl_BaseHelper283(self):
        return self.__gbind_dsl_BaseHelper283

    @gbind_dsl_BaseHelper283.setter
    def gbind_dsl_BaseHelper283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__gbind_dsl_BaseHelper283", None)
        self.__gbind_dsl_BaseHelper283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType284"):
                opp_val = getattr(old_value, "OclType284", None)
                if opp_val == self:
                    setattr(old_value, "OclType284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType284"):
                opp_val = getattr(value, "OclType284", None)
                setattr(value, "OclType284", self)

    @property
    def BindingModel286(self):
        return self.__BindingModel286

    @BindingModel286.setter
    def BindingModel286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__BindingModel286", None)
        self.__BindingModel286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl287"):
                opp_val = getattr(old_value, "dsl287", None)
                if opp_val == self:
                    setattr(old_value, "dsl287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl287"):
                opp_val = getattr(value, "dsl287", None)
                setattr(value, "dsl287", self)

class HelperParameter:

    pass
class VirtualFeature:

    pass
class gbind_dsl_VirtualAttribute(VirtualFeature):

    pass
class gbind_dsl_VirtualReference(VirtualFeature):

    pass
class gbind_dsl_VirtualFeature:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gbind_dsl_ConceptFeatureRef:

    def __init__(self, featureName: str, gbind_dsl_ConceptFeatureRef: "ConceptMetaclass" = None):
        self.featureName = featureName
        self.gbind_dsl_ConceptFeatureRef = gbind_dsl_ConceptFeatureRef
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def gbind_dsl_ConceptFeatureRef(self):
        return self.__gbind_dsl_ConceptFeatureRef

    @gbind_dsl_ConceptFeatureRef.setter
    def gbind_dsl_ConceptFeatureRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_ConceptFeatureRef__gbind_dsl_ConceptFeatureRef", None)
        self.__gbind_dsl_ConceptFeatureRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass272"):
                opp_val = getattr(old_value, "ConceptMetaclass272", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass272"):
                opp_val = getattr(value, "ConceptMetaclass272", None)
                setattr(value, "ConceptMetaclass272", self)

class ConceptFeatureRef:

    pass
class BindingModel:

    pass
class gbind_dsl_ConceptBinding(ABC):

    def __init__(self, debugName: str, BindingModel: "BindingModel" = None):
        self.debugName = debugName
        self.BindingModel = BindingModel
        
    @property
    def debugName(self) -> str:
        return self.__debugName

    @debugName.setter
    def debugName(self, debugName: str):
        self.__debugName = debugName

    @property
    def BindingModel(self):
        return self.__BindingModel

    @BindingModel.setter
    def BindingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_ConceptBinding__BindingModel", None)
        self.__BindingModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl234"):
                opp_val = getattr(old_value, "dsl234", None)
                if opp_val == self:
                    setattr(old_value, "dsl234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl234"):
                opp_val = getattr(value, "dsl234", None)
                setattr(value, "dsl234", self)

class VirtualAttribute:

    pass
class Metaclass:

    pass
class gbind_dsl_ConcreteMetaclass(Metaclass):

    pass
class gbind_dsl_ConceptMetaclass(Metaclass):

    pass
class VirtualReference:

    pass
class dsl_gbind_EClass:

    pass
class gbind_dsl_VirtualMetaclass(Metaclass):

    pass
class gbind_dsl_Metaclass(ABC):

    def __init__(self, name: str, gbind_dsl_Metaclass: "dsl_gbind_EClass" = None):
        self.name = name
        self.gbind_dsl_Metaclass = gbind_dsl_Metaclass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gbind_dsl_Metaclass(self):
        return self.__gbind_dsl_Metaclass

    @gbind_dsl_Metaclass.setter
    def gbind_dsl_Metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_Metaclass__gbind_dsl_Metaclass", None)
        self.__gbind_dsl_Metaclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_gbind_EClass"):
                opp_val = getattr(old_value, "dsl_gbind_EClass", None)
                if opp_val == self:
                    setattr(old_value, "dsl_gbind_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_gbind_EClass"):
                opp_val = getattr(value, "dsl_gbind_EClass", None)
                setattr(value, "dsl_gbind_EClass", self)

class BaseFeatureBinding:

    pass
class gbind_dsl_OclFeatureBinding(BaseFeatureBinding):

    pass
class gbind_dsl_RenamingFeatureBinding(BaseFeatureBinding):

    def __init__(self, concreteFeature: str, BaseFeatureBinding: "gbind_dsl_IntermediateClassBinding"):
        self.concreteFeature = concreteFeature
        
    @property
    def concreteFeature(self) -> str:
        return self.__concreteFeature

    @concreteFeature.setter
    def concreteFeature(self, concreteFeature: str):
        self.__concreteFeature = concreteFeature

class gbind_dsl_BindingOptions:

    def __init__(self, enableClassMerge: bool):
        self.enableClassMerge = enableClassMerge
        
    @property
    def enableClassMerge(self) -> bool:
        return self.__enableClassMerge

    @enableClassMerge.setter
    def enableClassMerge(self, enableClassMerge: bool):
        self.__enableClassMerge = enableClassMerge

class ConcreteReferencDeclaringVar:

    pass
class ConcreteMetaclass:

    pass
class ConceptMetaclass:

    pass
class BaseHelper:

    pass
class gbind_dsl_LocalHelper(BaseHelper):

    pass
class gbind_dsl_ConceptHelper(BaseHelper):

    pass
class ConceptBinding:

    pass
class gbind_dsl_IntermediateClassBinding(ConceptBinding):

    def __init__(self, conceptReferenceName: str, gbind_dsl_IntermediateClassBinding: "ConceptMetaclass" = None, gbind_dsl_IntermediateClassBinding246: "ConcreteMetaclass" = None, gbind_dsl_IntermediateClassBinding249: "ConcreteReferencDeclaringVar" = None, gbind_dsl_IntermediateClassBinding251: "ConceptMetaclass" = None, gbind_dsl_IntermediateClassBinding254: set["BaseFeatureBinding"] = None, dsl: "gbind_dsl_BindingModel"):
        self.conceptReferenceName = conceptReferenceName
        self.gbind_dsl_IntermediateClassBinding = gbind_dsl_IntermediateClassBinding
        self.gbind_dsl_IntermediateClassBinding246 = gbind_dsl_IntermediateClassBinding246
        self.gbind_dsl_IntermediateClassBinding249 = gbind_dsl_IntermediateClassBinding249
        self.gbind_dsl_IntermediateClassBinding251 = gbind_dsl_IntermediateClassBinding251
        self.gbind_dsl_IntermediateClassBinding254 = gbind_dsl_IntermediateClassBinding254 if gbind_dsl_IntermediateClassBinding254 is not None else set()
        
    @property
    def conceptReferenceName(self) -> str:
        return self.__conceptReferenceName

    @conceptReferenceName.setter
    def conceptReferenceName(self, conceptReferenceName: str):
        self.__conceptReferenceName = conceptReferenceName

    @property
    def gbind_dsl_IntermediateClassBinding246(self):
        return self.__gbind_dsl_IntermediateClassBinding246

    @gbind_dsl_IntermediateClassBinding246.setter
    def gbind_dsl_IntermediateClassBinding246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding246", None)
        self.__gbind_dsl_IntermediateClassBinding246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass247"):
                opp_val = getattr(old_value, "ConcreteMetaclass247", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass247"):
                opp_val = getattr(value, "ConcreteMetaclass247", None)
                setattr(value, "ConcreteMetaclass247", self)

    @property
    def gbind_dsl_IntermediateClassBinding249(self):
        return self.__gbind_dsl_IntermediateClassBinding249

    @gbind_dsl_IntermediateClassBinding249.setter
    def gbind_dsl_IntermediateClassBinding249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding249", None)
        self.__gbind_dsl_IntermediateClassBinding249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteReferencDeclaringVar"):
                opp_val = getattr(old_value, "ConcreteReferencDeclaringVar", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteReferencDeclaringVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteReferencDeclaringVar"):
                opp_val = getattr(value, "ConcreteReferencDeclaringVar", None)
                setattr(value, "ConcreteReferencDeclaringVar", self)

    @property
    def gbind_dsl_IntermediateClassBinding(self):
        return self.__gbind_dsl_IntermediateClassBinding

    @gbind_dsl_IntermediateClassBinding.setter
    def gbind_dsl_IntermediateClassBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding", None)
        self.__gbind_dsl_IntermediateClassBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass244"):
                opp_val = getattr(old_value, "ConceptMetaclass244", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass244"):
                opp_val = getattr(value, "ConceptMetaclass244", None)
                setattr(value, "ConceptMetaclass244", self)

    @property
    def gbind_dsl_IntermediateClassBinding254(self):
        return self.__gbind_dsl_IntermediateClassBinding254

    @gbind_dsl_IntermediateClassBinding254.setter
    def gbind_dsl_IntermediateClassBinding254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding254", None)
        self.__gbind_dsl_IntermediateClassBinding254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseFeatureBinding"):
                    opp_val = getattr(item, "BaseFeatureBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseFeatureBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseFeatureBinding"):
                    opp_val = getattr(item, "BaseFeatureBinding", None)
                    
                    setattr(item, "BaseFeatureBinding", self)
                    

    @property
    def gbind_dsl_IntermediateClassBinding251(self):
        return self.__gbind_dsl_IntermediateClassBinding251

    @gbind_dsl_IntermediateClassBinding251.setter
    def gbind_dsl_IntermediateClassBinding251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding251", None)
        self.__gbind_dsl_IntermediateClassBinding251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass252"):
                opp_val = getattr(old_value, "ConceptMetaclass252", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass252"):
                opp_val = getattr(value, "ConceptMetaclass252", None)
                setattr(value, "ConceptMetaclass252", self)

class gbind_dsl_BaseFeatureBinding(ConceptBinding):

    def __init__(self, conceptFeature: str, gbind_dsl_BaseFeatureBinding: "ConceptMetaclass" = None, gbind_dsl_BaseFeatureBinding276: "ConcreteMetaclass" = None, dsl: "gbind_dsl_BindingModel"):
        self.conceptFeature = conceptFeature
        self.gbind_dsl_BaseFeatureBinding = gbind_dsl_BaseFeatureBinding
        self.gbind_dsl_BaseFeatureBinding276 = gbind_dsl_BaseFeatureBinding276
        
    @property
    def conceptFeature(self) -> str:
        return self.__conceptFeature

    @conceptFeature.setter
    def conceptFeature(self, conceptFeature: str):
        self.__conceptFeature = conceptFeature

    @property
    def gbind_dsl_BaseFeatureBinding276(self):
        return self.__gbind_dsl_BaseFeatureBinding276

    @gbind_dsl_BaseFeatureBinding276.setter
    def gbind_dsl_BaseFeatureBinding276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseFeatureBinding__gbind_dsl_BaseFeatureBinding276", None)
        self.__gbind_dsl_BaseFeatureBinding276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass277"):
                opp_val = getattr(old_value, "ConcreteMetaclass277", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass277"):
                opp_val = getattr(value, "ConcreteMetaclass277", None)
                setattr(value, "ConcreteMetaclass277", self)

    @property
    def gbind_dsl_BaseFeatureBinding(self):
        return self.__gbind_dsl_BaseFeatureBinding

    @gbind_dsl_BaseFeatureBinding.setter
    def gbind_dsl_BaseFeatureBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseFeatureBinding__gbind_dsl_BaseFeatureBinding", None)
        self.__gbind_dsl_BaseFeatureBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass274"):
                opp_val = getattr(old_value, "ConceptMetaclass274", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass274"):
                opp_val = getattr(value, "ConceptMetaclass274", None)
                setattr(value, "ConceptMetaclass274", self)

class gbind_dsl_VirtualClassBinding(ConceptBinding):

    pass
class gbind_dsl_ClassBinding(ConceptBinding):

    pass
class gbind_dsl_BindingModel:

    def __init__(self, name: str, targetBinding: bool, gbind_dsl_BindingModel224: set["VirtualMetaclass"] = None, gbind_dsl_BindingModel226: "MetamodelDeclaration" = None, gbind_dsl_BindingModel228: set["MetamodelDeclaration"] = None, gbind_dsl_BindingModel231: "BindingOptions" = None, ConceptBinding: set["ConceptBinding"] = None, BaseHelper: set["BaseHelper"] = None, gbind_dsl_BindingModel: set["ConceptMetaclass"] = None, gbind_dsl_BindingModel222: set["ConcreteMetaclass"] = None):
        self.name = name
        self.targetBinding = targetBinding
        self.gbind_dsl_BindingModel224 = gbind_dsl_BindingModel224 if gbind_dsl_BindingModel224 is not None else set()
        self.gbind_dsl_BindingModel226 = gbind_dsl_BindingModel226
        self.gbind_dsl_BindingModel228 = gbind_dsl_BindingModel228 if gbind_dsl_BindingModel228 is not None else set()
        self.gbind_dsl_BindingModel231 = gbind_dsl_BindingModel231
        self.ConceptBinding = ConceptBinding if ConceptBinding is not None else set()
        self.BaseHelper = BaseHelper if BaseHelper is not None else set()
        self.gbind_dsl_BindingModel = gbind_dsl_BindingModel if gbind_dsl_BindingModel is not None else set()
        self.gbind_dsl_BindingModel222 = gbind_dsl_BindingModel222 if gbind_dsl_BindingModel222 is not None else set()
        
    @property
    def targetBinding(self) -> bool:
        return self.__targetBinding

    @targetBinding.setter
    def targetBinding(self, targetBinding: bool):
        self.__targetBinding = targetBinding

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gbind_dsl_BindingModel226(self):
        return self.__gbind_dsl_BindingModel226

    @gbind_dsl_BindingModel226.setter
    def gbind_dsl_BindingModel226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel226", None)
        self.__gbind_dsl_BindingModel226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetamodelDeclaration"):
                opp_val = getattr(old_value, "MetamodelDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "MetamodelDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetamodelDeclaration"):
                opp_val = getattr(value, "MetamodelDeclaration", None)
                setattr(value, "MetamodelDeclaration", self)

    @property
    def BaseHelper(self):
        return self.__BaseHelper

    @BaseHelper.setter
    def BaseHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__BaseHelper", None)
        self.__BaseHelper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl219"):
                    opp_val = getattr(item, "dsl219", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl219"):
                    opp_val = getattr(item, "dsl219", None)
                    
                    setattr(item, "dsl219", self)
                    

    @property
    def gbind_dsl_BindingModel(self):
        return self.__gbind_dsl_BindingModel

    @gbind_dsl_BindingModel.setter
    def gbind_dsl_BindingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel", None)
        self.__gbind_dsl_BindingModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConceptMetaclass"):
                    opp_val = getattr(item, "ConceptMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "ConceptMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConceptMetaclass"):
                    opp_val = getattr(item, "ConceptMetaclass", None)
                    
                    setattr(item, "ConceptMetaclass", self)
                    

    @property
    def gbind_dsl_BindingModel231(self):
        return self.__gbind_dsl_BindingModel231

    @gbind_dsl_BindingModel231.setter
    def gbind_dsl_BindingModel231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel231", None)
        self.__gbind_dsl_BindingModel231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingOptions"):
                opp_val = getattr(old_value, "BindingOptions", None)
                if opp_val == self:
                    setattr(old_value, "BindingOptions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingOptions"):
                opp_val = getattr(value, "BindingOptions", None)
                setattr(value, "BindingOptions", self)

    @property
    def gbind_dsl_BindingModel224(self):
        return self.__gbind_dsl_BindingModel224

    @gbind_dsl_BindingModel224.setter
    def gbind_dsl_BindingModel224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel224", None)
        self.__gbind_dsl_BindingModel224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VirtualMetaclass"):
                    opp_val = getattr(item, "VirtualMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "VirtualMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VirtualMetaclass"):
                    opp_val = getattr(item, "VirtualMetaclass", None)
                    
                    setattr(item, "VirtualMetaclass", self)
                    

    @property
    def ConceptBinding(self):
        return self.__ConceptBinding

    @ConceptBinding.setter
    def ConceptBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__ConceptBinding", None)
        self.__ConceptBinding = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl"):
                    opp_val = getattr(item, "dsl", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl"):
                    opp_val = getattr(item, "dsl", None)
                    
                    setattr(item, "dsl", self)
                    

    @property
    def gbind_dsl_BindingModel222(self):
        return self.__gbind_dsl_BindingModel222

    @gbind_dsl_BindingModel222.setter
    def gbind_dsl_BindingModel222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel222", None)
        self.__gbind_dsl_BindingModel222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConcreteMetaclass"):
                    opp_val = getattr(item, "ConcreteMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "ConcreteMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConcreteMetaclass"):
                    opp_val = getattr(item, "ConcreteMetaclass", None)
                    
                    setattr(item, "ConcreteMetaclass", self)
                    

    @property
    def gbind_dsl_BindingModel228(self):
        return self.__gbind_dsl_BindingModel228

    @gbind_dsl_BindingModel228.setter
    def gbind_dsl_BindingModel228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel228", None)
        self.__gbind_dsl_BindingModel228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetamodelDeclaration229"):
                    opp_val = getattr(item, "MetamodelDeclaration229", None)
                    
                    if opp_val == self:
                        setattr(item, "MetamodelDeclaration229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetamodelDeclaration229"):
                    opp_val = getattr(item, "MetamodelDeclaration229", None)
                    
                    setattr(item, "MetamodelDeclaration229", self)
                    

class OclInstanceModel:

    pass
class BindingOptions:

    pass
class MetamodelDeclaration:

    pass
class VirtualMetaclass:

    pass
class Parameter:

    pass
class OclFeatureDefinition:

    pass
class OclModelElement:

    pass
class TupleType:

    pass
class OclFeature:

    pass
class gbind_simpleocl_Operation(OclFeature):

    pass
class gbind_simpleocl_Attribute(OclFeature):

    pass
class Primitive:

    pass
class gbind_simpleocl_BooleanType(Primitive):

    pass
class gbind_simpleocl_NumericType(Primitive):

    pass
class gbind_simpleocl_StringType(Primitive):

    pass
class OclModel:

    pass
class gbind_simpleocl_OclMetamodel(OclModel):

    def __init__(self, uri: str, OclInstanceModel: set["OclInstanceModel"] = None, OclModel: "gbind_simpleocl_OclModelElementExp", simpleocl170: "gbind_simpleocl_OclModelElement"):
        self.uri = uri
        self.OclInstanceModel = OclInstanceModel if OclInstanceModel is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def OclInstanceModel(self):
        return self.__OclInstanceModel

    @OclInstanceModel.setter
    def OclInstanceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclMetamodel__OclInstanceModel", None)
        self.__OclInstanceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleocl213"):
                    opp_val = getattr(item, "simpleocl213", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleocl213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleocl213"):
                    opp_val = getattr(item, "simpleocl213", None)
                    
                    setattr(item, "simpleocl213", self)
                    

class gbind_simpleocl_OclInstanceModel(OclModel):

    pass
class LambdaType:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class gbind_simpleocl_SetType(CollectionType):

    pass
class gbind_simpleocl_SequenceType(CollectionType):

    pass
class gbind_simpleocl_OrderedSetType(CollectionType):

    pass
class gbind_simpleocl_BagType(CollectionType):

    pass
class NumericType:

    pass
class gbind_simpleocl_RealType(NumericType):

    pass
class gbind_simpleocl_IntegerType(NumericType):

    pass
class OclContextDefinition:

    pass
class IterateExp:

    pass
class MapType:

    pass
class VariableExp:

    pass
class gbind_simpleocl_LambdaCallExp(VariableExp):

    pass
class Iterator:

    pass
class PropertyCall:

    pass
class gbind_simpleocl_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str, simpleocl64: "gbind_simpleocl_PropertyCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gbind_simpleocl_LoopExp(PropertyCall):

    pass
class StaticPropertyCallExp:

    pass
class StaticPropertyCall:

    pass
class gbind_simpleocl_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, gbind_simpleocl_StaticOperationCall: set["OclExpression"] = None, simpleocl58: "gbind_simpleocl_StaticPropertyCallExp"):
        self.operationName = operationName
        self.gbind_simpleocl_StaticOperationCall = gbind_simpleocl_StaticOperationCall if gbind_simpleocl_StaticOperationCall is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def gbind_simpleocl_StaticOperationCall(self):
        return self.__gbind_simpleocl_StaticOperationCall

    @gbind_simpleocl_StaticOperationCall.setter
    def gbind_simpleocl_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_StaticOperationCall__gbind_simpleocl_StaticOperationCall", None)
        self.__gbind_simpleocl_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression62"):
                    opp_val = getattr(item, "OclExpression62", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression62"):
                    opp_val = getattr(item, "OclExpression62", None)
                    
                    setattr(item, "OclExpression62", self)
                    

class gbind_simpleocl_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str, simpleocl58: "gbind_simpleocl_StaticPropertyCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gbind_simpleocl_OperationCall(PropertyCall):

    def __init__(self, operationName: str, OclExpression72: set["OclExpression"] = None, simpleocl64: "gbind_simpleocl_PropertyCallExp"):
        self.operationName = operationName
        self.OclExpression72 = OclExpression72 if OclExpression72 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression72(self):
        return self.__OclExpression72

    @OclExpression72.setter
    def OclExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperationCall__OclExpression72", None)
        self.__OclExpression72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleocl73"):
                    opp_val = getattr(item, "simpleocl73", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleocl73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleocl73"):
                    opp_val = getattr(item, "simpleocl73", None)
                    
                    setattr(item, "simpleocl73", self)
                    

class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class gbind_dsl_VirtualTupleExp(TupleExp):

    def __init__(self, typeName: str, simpleocl44: "gbind_simpleocl_TuplePart"):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class TuplePart:

    pass
class NumericExp:

    pass
class gbind_simpleocl_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class gbind_simpleocl_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class gbind_simpleocl_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class VariableDeclaration:

    pass
class gbind_simpleocl_Parameter(VariableDeclaration):

    pass
class gbind_dsl_ConcreteReferencDeclaringVar(VariableDeclaration):

    pass
class gbind_simpleocl_Iterator(VariableDeclaration):

    pass
class gbind_dsl_HelperParameter(VariableDeclaration):

    pass
class gbind_simpleocl_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, LetExp112: "LetExp" = None, OclExpression115: "OclExpression" = None, IterateExp: "IterateExp" = None, simpleocl150: "gbind_simpleocl_OclType", simpleocl38: "gbind_simpleocl_VariableExp"):
        self.eq = eq
        self.LetExp112 = LetExp112
        self.OclExpression115 = OclExpression115
        self.IterateExp = IterateExp
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def OclExpression115(self):
        return self.__OclExpression115

    @OclExpression115.setter
    def OclExpression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__OclExpression115", None)
        self.__OclExpression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl116"):
                opp_val = getattr(old_value, "simpleocl116", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl116"):
                opp_val = getattr(value, "simpleocl116", None)
                setattr(value, "simpleocl116", self)

    @property
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl118"):
                opp_val = getattr(old_value, "simpleocl118", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl118"):
                opp_val = getattr(value, "simpleocl118", None)
                setattr(value, "simpleocl118", self)

    @property
    def LetExp112(self):
        return self.__LetExp112

    @LetExp112.setter
    def LetExp112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__LetExp112", None)
        self.__LetExp112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl113"):
                opp_val = getattr(old_value, "simpleocl113", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl113"):
                opp_val = getattr(value, "simpleocl113", None)
                setattr(value, "simpleocl113", self)

class OclExpression:

    pass
class gbind_simpleocl_CollectionExp(OclExpression):

    pass
class gbind_simpleocl_BraceExp(OclExpression):

    pass
class gbind_simpleocl_OclModelElementExp(OclExpression):

    def __init__(self, name: str, gbind_simpleocl_OclModelElementExp: "OclModel" = None, simpleocl198: "gbind_simpleocl_Attribute", OclExpression279: "gbind_dsl_OclFeatureBinding", simpleocl102: "gbind_simpleocl_IfExp", simpleocl73: "gbind_simpleocl_OperationCall", simpleocl105: "gbind_simpleocl_IfExp", OclExpression53: "gbind_simpleocl_MapElement", OclExpression82: "gbind_simpleocl_BraceExp", simpleocl40: "gbind_simpleocl_CollectionExp", OclExpression260: "gbind_dsl_VirtualMetaclass", OclExpression50: "gbind_simpleocl_MapElement", OclExpression80: "gbind_simpleocl_LambdaCallExp", OclExpression75: "gbind_simpleocl_OperatorCallExp", OclExpression62: "gbind_simpleocl_StaticOperationCall", simpleocl78: "gbind_simpleocl_OperatorCallExp", simpleocl85: "gbind_simpleocl_LoopExp", simpleocl67: "gbind_simpleocl_PropertyCallExp", simpleocl96: "gbind_simpleocl_LetExp", simpleocl116: "gbind_simpleocl_LocalVariable", simpleocl209: "gbind_simpleocl_Operation", OclExpression242: "gbind_dsl_ClassBinding", simpleocl99: "gbind_simpleocl_IfExp", OclExpression281: "gbind_dsl_BaseHelper", simpleocl132: "gbind_simpleocl_OclType"):
        self.name = name
        self.gbind_simpleocl_OclModelElementExp = gbind_simpleocl_OclModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gbind_simpleocl_OclModelElementExp(self):
        return self.__gbind_simpleocl_OclModelElementExp

    @gbind_simpleocl_OclModelElementExp.setter
    def gbind_simpleocl_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclModelElementExp__gbind_simpleocl_OclModelElementExp", None)
        self.__gbind_simpleocl_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel"):
                opp_val = getattr(old_value, "OclModel", None)
                if opp_val == self:
                    setattr(old_value, "OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel"):
                opp_val = getattr(value, "OclModel", None)
                setattr(value, "OclModel", self)

class gbind_simpleocl_IfExp(OclExpression):

    pass
class gbind_simpleocl_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, simpleocl198: "gbind_simpleocl_Attribute", OclExpression279: "gbind_dsl_OclFeatureBinding", simpleocl102: "gbind_simpleocl_IfExp", simpleocl73: "gbind_simpleocl_OperationCall", simpleocl105: "gbind_simpleocl_IfExp", OclExpression53: "gbind_simpleocl_MapElement", OclExpression82: "gbind_simpleocl_BraceExp", simpleocl40: "gbind_simpleocl_CollectionExp", OclExpression260: "gbind_dsl_VirtualMetaclass", OclExpression50: "gbind_simpleocl_MapElement", OclExpression80: "gbind_simpleocl_LambdaCallExp", OclExpression75: "gbind_simpleocl_OperatorCallExp", OclExpression62: "gbind_simpleocl_StaticOperationCall", simpleocl78: "gbind_simpleocl_OperatorCallExp", simpleocl85: "gbind_simpleocl_LoopExp", simpleocl67: "gbind_simpleocl_PropertyCallExp", simpleocl96: "gbind_simpleocl_LetExp", simpleocl116: "gbind_simpleocl_LocalVariable", simpleocl209: "gbind_simpleocl_Operation", OclExpression242: "gbind_dsl_ClassBinding", simpleocl99: "gbind_simpleocl_IfExp", OclExpression281: "gbind_dsl_BaseHelper", simpleocl132: "gbind_simpleocl_OclType"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gbind_simpleocl_PrimitiveExp(OclExpression):

    pass
class gbind_simpleocl_SuperExp(OclExpression):

    pass
class gbind_simpleocl_SelfExp(OclExpression):

    pass
class gbind_simpleocl_PropertyCallExp(OclExpression):

    pass
class gbind_simpleocl_LetExp(OclExpression):

    pass
class gbind_simpleocl_StaticPropertyCallExp(OclExpression):

    pass
class gbind_simpleocl_MapExp(OclExpression):

    pass
class gbind_simpleocl_TupleExp(OclExpression):

    pass
class gbind_simpleocl_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, gbind_simpleocl_OperatorCallExp: "OclExpression" = None, OclExpression77: "OclExpression" = None, simpleocl198: "gbind_simpleocl_Attribute", OclExpression279: "gbind_dsl_OclFeatureBinding", simpleocl102: "gbind_simpleocl_IfExp", simpleocl73: "gbind_simpleocl_OperationCall", simpleocl105: "gbind_simpleocl_IfExp", OclExpression53: "gbind_simpleocl_MapElement", OclExpression82: "gbind_simpleocl_BraceExp", simpleocl40: "gbind_simpleocl_CollectionExp", OclExpression260: "gbind_dsl_VirtualMetaclass", OclExpression50: "gbind_simpleocl_MapElement", OclExpression80: "gbind_simpleocl_LambdaCallExp", OclExpression75: "gbind_simpleocl_OperatorCallExp", OclExpression62: "gbind_simpleocl_StaticOperationCall", simpleocl78: "gbind_simpleocl_OperatorCallExp", simpleocl85: "gbind_simpleocl_LoopExp", simpleocl67: "gbind_simpleocl_PropertyCallExp", simpleocl96: "gbind_simpleocl_LetExp", simpleocl116: "gbind_simpleocl_LocalVariable", simpleocl209: "gbind_simpleocl_Operation", OclExpression242: "gbind_dsl_ClassBinding", simpleocl99: "gbind_simpleocl_IfExp", OclExpression281: "gbind_dsl_BaseHelper", simpleocl132: "gbind_simpleocl_OclType"):
        self.operationName = operationName
        self.gbind_simpleocl_OperatorCallExp = gbind_simpleocl_OperatorCallExp
        self.OclExpression77 = OclExpression77
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression77(self):
        return self.__OclExpression77

    @OclExpression77.setter
    def OclExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperatorCallExp__OclExpression77", None)
        self.__OclExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl78"):
                opp_val = getattr(old_value, "simpleocl78", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl78"):
                opp_val = getattr(value, "simpleocl78", None)
                setattr(value, "simpleocl78", self)

    @property
    def gbind_simpleocl_OperatorCallExp(self):
        return self.__gbind_simpleocl_OperatorCallExp

    @gbind_simpleocl_OperatorCallExp.setter
    def gbind_simpleocl_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperatorCallExp__gbind_simpleocl_OperatorCallExp", None)
        self.__gbind_simpleocl_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression75"):
                opp_val = getattr(old_value, "OclExpression75", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression75"):
                opp_val = getattr(value, "OclExpression75", None)
                setattr(value, "OclExpression75", self)

class gbind_simpleocl_OclUndefinedExp(OclExpression):

    pass
class gbind_simpleocl_EnvExp(OclExpression):

    pass
class gbind_simpleocl_VariableExp(OclExpression):

    pass
class OperatorCallExp:

    pass
class gbind_simpleocl_AddOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_IntOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_NotOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_MulOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_EqOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_RelOpCallExp(OperatorCallExp):

    pass
class Attribute:

    pass
class Operation:

    pass
class LocalVariable:

    pass
class gbind_simpleocl_TuplePart(LocalVariable):

    pass
class OperationCall:

    pass
class gbind_simpleocl_CollectionOperationCall(OperationCall):

    pass
class LoopExp:

    pass
class gbind_simpleocl_IteratorExp(LoopExp):

    def __init__(self, name: str, simpleocl20: "gbind_simpleocl_OclExpression", simpleocl121: "gbind_simpleocl_Iterator"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gbind_simpleocl_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class gbind_simpleocl_NumericExp(PrimitiveExp):

    pass
class gbind_simpleocl_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class IfExp:

    pass
class OclType:

    pass
class gbind_simpleocl_CollectionType(OclType):

    pass
class gbind_simpleocl_Primitive(OclType):

    pass
class gbind_simpleocl_EnvType(OclType):

    pass
class gbind_simpleocl_OclAnyType(OclType):

    pass
class gbind_simpleocl_TupleType(OclType):

    pass
class gbind_simpleocl_OclModelElement(OclType):

    pass
class gbind_simpleocl_LambdaType(OclType):

    pass
class gbind_simpleocl_MapType(OclType):

    pass
class Module:

    pass
class ModuleElement:

    pass
class gbind_simpleocl_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, OclFeature: "OclFeature" = None, OclContextDefinition186: "OclContextDefinition" = None, simpleocl3: "gbind_simpleocl_Module"):
        self.static = static
        self.OclFeature = OclFeature
        self.OclContextDefinition186 = OclContextDefinition186
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def OclContextDefinition186(self):
        return self.__OclContextDefinition186

    @OclContextDefinition186.setter
    def OclContextDefinition186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeatureDefinition__OclContextDefinition186", None)
        self.__OclContextDefinition186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl187"):
                opp_val = getattr(old_value, "simpleocl187", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl187"):
                opp_val = getattr(value, "simpleocl187", None)
                setattr(value, "simpleocl187", self)

    @property
    def OclFeature(self):
        return self.__OclFeature

    @OclFeature.setter
    def OclFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeatureDefinition__OclFeature", None)
        self.__OclFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl184"):
                opp_val = getattr(old_value, "simpleocl184", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl184"):
                opp_val = getattr(value, "simpleocl184", None)
                setattr(value, "simpleocl184", self)

class Import:

    pass
class OclMetamodel:

    pass
class gbind_dsl_MetamodelDeclaration(OclMetamodel):

    def __init__(self, metamodelURI: str, resource: str, simpleocl216: "gbind_simpleocl_OclInstanceModel", OclMetamodel: "gbind_simpleocl_Module"):
        self.metamodelURI = metamodelURI
        self.resource = resource
        
    @property
    def metamodelURI(self) -> str:
        return self.__metamodelURI

    @metamodelURI.setter
    def metamodelURI(self, metamodelURI: str):
        self.__metamodelURI = metamodelURI

    @property
    def resource(self) -> str:
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource

class NamedElement:

    pass
class gbind_simpleocl_Import(NamedElement):

    pass
class gbind_simpleocl_OclFeature(NamedElement):

    def __init__(self, eq: str, OclFeatureDefinition194: "OclFeatureDefinition" = None):
        self.eq = eq
        self.OclFeatureDefinition194 = OclFeatureDefinition194
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def OclFeatureDefinition194(self):
        return self.__OclFeatureDefinition194

    @OclFeatureDefinition194.setter
    def OclFeatureDefinition194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeature__OclFeatureDefinition194", None)
        self.__OclFeatureDefinition194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl195"):
                opp_val = getattr(old_value, "simpleocl195", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl195"):
                opp_val = getattr(value, "simpleocl195", None)
                setattr(value, "simpleocl195", self)

class gbind_simpleocl_OclModel(NamedElement):

    pass
class gbind_simpleocl_Module(NamedElement):

    pass
class LocatedElement:

    pass
class gbind_simpleocl_OclExpression(LocatedElement):

    pass
class gbind_simpleocl_OclContextDefinition(LocatedElement):

    pass
class gbind_simpleocl_ModuleElement(LocatedElement):

    pass
class gbind_simpleocl_OclType(LocatedElement):

    def __init__(self, name: str, Operation134: "Operation" = None, MapType: "MapType" = None, Attribute139: "Attribute" = None, MapType142: "MapType" = None, OclContextDefinition: "OclContextDefinition" = None, OclExpression131: "OclExpression" = None, CollectionType: "CollectionType" = None, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration149: "VariableDeclaration" = None, LambdaType: "LambdaType" = None, LambdaType154: "LambdaType" = None, StaticPropertyCallExp157: "StaticPropertyCallExp" = None):
        self.name = name
        self.Operation134 = Operation134
        self.MapType = MapType
        self.Attribute139 = Attribute139
        self.MapType142 = MapType142
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression131 = OclExpression131
        self.CollectionType = CollectionType
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration149 = VariableDeclaration149
        self.LambdaType = LambdaType
        self.LambdaType154 = LambdaType154
        self.StaticPropertyCallExp157 = StaticPropertyCallExp157
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl145"):
                opp_val = getattr(old_value, "simpleocl145", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl145"):
                opp_val = getattr(value, "simpleocl145", None)
                setattr(value, "simpleocl145", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl129"):
                opp_val = getattr(old_value, "simpleocl129", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl129"):
                opp_val = getattr(value, "simpleocl129", None)
                setattr(value, "simpleocl129", self)

    @property
    def LambdaType154(self):
        return self.__LambdaType154

    @LambdaType154.setter
    def LambdaType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__LambdaType154", None)
        self.__LambdaType154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl155"):
                opp_val = getattr(old_value, "simpleocl155", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl155"):
                opp_val = getattr(value, "simpleocl155", None)
                setattr(value, "simpleocl155", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl147"):
                opp_val = getattr(old_value, "simpleocl147", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl147"):
                opp_val = getattr(value, "simpleocl147", None)
                setattr(value, "simpleocl147", self)

    @property
    def Attribute139(self):
        return self.__Attribute139

    @Attribute139.setter
    def Attribute139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__Attribute139", None)
        self.__Attribute139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl140"):
                opp_val = getattr(old_value, "simpleocl140", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl140"):
                opp_val = getattr(value, "simpleocl140", None)
                setattr(value, "simpleocl140", self)

    @property
    def Operation134(self):
        return self.__Operation134

    @Operation134.setter
    def Operation134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__Operation134", None)
        self.__Operation134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl135"):
                opp_val = getattr(old_value, "simpleocl135", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl135"):
                opp_val = getattr(value, "simpleocl135", None)
                setattr(value, "simpleocl135", self)

    @property
    def LambdaType(self):
        return self.__LambdaType

    @LambdaType.setter
    def LambdaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__LambdaType", None)
        self.__LambdaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl152"):
                opp_val = getattr(old_value, "simpleocl152", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl152"):
                opp_val = getattr(value, "simpleocl152", None)
                setattr(value, "simpleocl152", self)

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl137"):
                opp_val = getattr(old_value, "simpleocl137", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl137"):
                opp_val = getattr(value, "simpleocl137", None)
                setattr(value, "simpleocl137", self)

    @property
    def MapType142(self):
        return self.__MapType142

    @MapType142.setter
    def MapType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__MapType142", None)
        self.__MapType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl143"):
                opp_val = getattr(old_value, "simpleocl143", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl143"):
                opp_val = getattr(value, "simpleocl143", None)
                setattr(value, "simpleocl143", self)

    @property
    def OclExpression131(self):
        return self.__OclExpression131

    @OclExpression131.setter
    def OclExpression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__OclExpression131", None)
        self.__OclExpression131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl132"):
                opp_val = getattr(old_value, "simpleocl132", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl132"):
                opp_val = getattr(value, "simpleocl132", None)
                setattr(value, "simpleocl132", self)

    @property
    def StaticPropertyCallExp157(self):
        return self.__StaticPropertyCallExp157

    @StaticPropertyCallExp157.setter
    def StaticPropertyCallExp157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__StaticPropertyCallExp157", None)
        self.__StaticPropertyCallExp157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl158"):
                opp_val = getattr(old_value, "simpleocl158", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl158"):
                opp_val = getattr(value, "simpleocl158", None)
                setattr(value, "simpleocl158", self)

    @property
    def VariableDeclaration149(self):
        return self.__VariableDeclaration149

    @VariableDeclaration149.setter
    def VariableDeclaration149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__VariableDeclaration149", None)
        self.__VariableDeclaration149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl150"):
                opp_val = getattr(old_value, "simpleocl150", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl150"):
                opp_val = getattr(value, "simpleocl150", None)
                setattr(value, "simpleocl150", self)

class gbind_simpleocl_StaticPropertyCall(LocatedElement):

    pass
class gbind_simpleocl_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, OclType107: "OclType" = None, VariableExp: set["VariableExp"] = None):
        self.varName = varName
        self.OclType107 = OclType107
        self.VariableExp = VariableExp if VariableExp is not None else set()
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def OclType107(self):
        return self.__OclType107

    @OclType107.setter
    def OclType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_VariableDeclaration__OclType107", None)
        self.__OclType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl108"):
                opp_val = getattr(old_value, "simpleocl108", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl108"):
                opp_val = getattr(value, "simpleocl108", None)
                setattr(value, "simpleocl108", self)

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleocl110"):
                    opp_val = getattr(item, "simpleocl110", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleocl110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleocl110"):
                    opp_val = getattr(item, "simpleocl110", None)
                    
                    setattr(item, "simpleocl110", self)
                    

class gbind_simpleocl_PropertyCall(LocatedElement):

    pass
class gbind_simpleocl_MapElement(LocatedElement):

    pass
class gbind_simpleocl_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, OclType164: "OclType" = None, TupleType: "TupleType" = None):
        self.name = name
        self.OclType164 = OclType164
        self.TupleType = TupleType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType164(self):
        return self.__OclType164

    @OclType164.setter
    def OclType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_TupleTypeAttribute__OclType164", None)
        self.__OclType164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl165"):
                opp_val = getattr(old_value, "simpleocl165", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl165"):
                opp_val = getattr(value, "simpleocl165", None)
                setattr(value, "simpleocl165", self)

    @property
    def TupleType(self):
        return self.__TupleType

    @TupleType.setter
    def TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl167"):
                opp_val = getattr(old_value, "simpleocl167", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl167"):
                opp_val = getattr(value, "simpleocl167", None)
                setattr(value, "simpleocl167", self)

class gbind_simpleocl_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CollectionExp:

    pass
class gbind_simpleocl_SequenceExp(CollectionExp):

    pass
class gbind_simpleocl_SetExp(CollectionExp):

    pass
class gbind_simpleocl_BagExp(CollectionExp):

    pass
class gbind_simpleocl_OrderedSetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class gbind_simpleocl_LocatedElement(ABC):

    def __init__(self, line: str, column: str, charStart: str, charEnd: str):
        self.line = line
        self.column = column
        self.charStart = charStart
        self.charEnd = charEnd
        
    @property
    def charStart(self) -> str:
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart

    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def charEnd(self) -> str:
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd

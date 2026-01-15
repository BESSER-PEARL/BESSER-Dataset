from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Feature:

    pass
class BasicFMmetamodel_OrGroup(Feature):

    pass
class BasicFMmetamodel_Alternative(Feature):

    pass
class BasicFMmetamodel_CrossTreeConstraint(ABC):

    pass
class BasicFMmetamodel_Feature:

    def __init__(self, id: str, name: str, mandatory: bool, selected: bool, BasicFMmetamodel_Feature: "BasicFMmetamodel_FeatureModel" = None, Feature: "BasicFMmetamodel_Feature" = None, parent: set["BasicFMmetamodel_Feature"] = None, Feature7: "BasicFMmetamodel_Feature" = None, children: "BasicFMmetamodel_Feature" = None):
        self.id = id
        self.name = name
        self.mandatory = mandatory
        self.selected = selected
        self.BasicFMmetamodel_Feature = BasicFMmetamodel_Feature
        self.Feature = Feature
        self.parent = parent if parent is not None else set()
        self.Feature7 = Feature7
        self.children = children
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_Feature__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature7"):
                opp_val = getattr(old_value, "Feature7", None)
                if opp_val == self:
                    setattr(old_value, "Feature7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature7"):
                opp_val = getattr(value, "Feature7", None)
                setattr(value, "Feature7", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_Feature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def Feature7(self):
        return self.__Feature7

    @Feature7.setter
    def Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_Feature__Feature7", None)
        self.__Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BasicFMmetamodel_Feature(self):
        return self.__BasicFMmetamodel_Feature

    @BasicFMmetamodel_Feature.setter
    def BasicFMmetamodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_Feature__BasicFMmetamodel_Feature", None)
        self.__BasicFMmetamodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicFMmetamodel_FeatureModel"):
                opp_val = getattr(old_value, "BasicFMmetamodel_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "BasicFMmetamodel_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicFMmetamodel_FeatureModel"):
                opp_val = getattr(value, "BasicFMmetamodel_FeatureModel", None)
                setattr(value, "BasicFMmetamodel_FeatureModel", self)

    def isRoot(self) -> bool:
        # TODO: Implement isRoot method
        pass

    def isLeaf(self) -> bool:
        # TODO: Implement isLeaf method
        pass

class BasicFMmetamodel_FeatureModel:

    def __init__(self, name: str, BasicFMmetamodel_FeatureModel: "BasicFMmetamodel_Feature" = None, BasicFMmetamodel_FeatureModel2: set["BasicFMmetamodel_CrossTreeConstraint"] = None):
        self.name = name
        self.BasicFMmetamodel_FeatureModel = BasicFMmetamodel_FeatureModel
        self.BasicFMmetamodel_FeatureModel2 = BasicFMmetamodel_FeatureModel2 if BasicFMmetamodel_FeatureModel2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BasicFMmetamodel_FeatureModel2(self):
        return self.__BasicFMmetamodel_FeatureModel2

    @BasicFMmetamodel_FeatureModel2.setter
    def BasicFMmetamodel_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_FeatureModel__BasicFMmetamodel_FeatureModel2", None)
        self.__BasicFMmetamodel_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicFMmetamodel_CrossTreeConstraint"):
                    opp_val = getattr(item, "BasicFMmetamodel_CrossTreeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicFMmetamodel_CrossTreeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicFMmetamodel_CrossTreeConstraint"):
                    opp_val = getattr(item, "BasicFMmetamodel_CrossTreeConstraint", None)
                    
                    setattr(item, "BasicFMmetamodel_CrossTreeConstraint", self)
                    

    @property
    def BasicFMmetamodel_FeatureModel(self):
        return self.__BasicFMmetamodel_FeatureModel

    @BasicFMmetamodel_FeatureModel.setter
    def BasicFMmetamodel_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasicFMmetamodel_FeatureModel__BasicFMmetamodel_FeatureModel", None)
        self.__BasicFMmetamodel_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicFMmetamodel_Feature"):
                opp_val = getattr(old_value, "BasicFMmetamodel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "BasicFMmetamodel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicFMmetamodel_Feature"):
                opp_val = getattr(value, "BasicFMmetamodel_Feature", None)
                setattr(value, "BasicFMmetamodel_Feature", self)

    def getFeature(self, id: str) -> str:
        # TODO: Implement getFeature method
        pass

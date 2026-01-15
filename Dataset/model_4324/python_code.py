from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ElementKind(Enum):
    metamodel = "metamodel"
    model = "model"
    package = "package"
    interface = "interface"
    class = "class"
class ModelKind(Enum):
    KM3 = "KM3"
    UML2 = "UML2"


############################################
# Definition of Classes
############################################

class Measure:

    pass
class Measure_DoubleMeasure(Measure):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Measure_PercentageMeasure(Measure):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Measure_IntegerMeasure(Measure):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Measure_Measure(ABC):

    pass
class Measure_Metric:

    def __init__(self, name: str, desc: str, preferredValue: str, Metric: "Measure_Category" = None, Measure_Metric: "Measure_Measure" = None, metrics: "Measure_Category" = None):
        self.name = name
        self.desc = desc
        self.preferredValue = preferredValue
        self.Metric = Metric
        self.Measure_Metric = Measure_Metric
        self.metrics = metrics
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def preferredValue(self) -> str:
        return self.__preferredValue

    @preferredValue.setter
    def preferredValue(self, preferredValue: str):
        self.__preferredValue = preferredValue

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def Measure_Metric(self):
        return self.__Measure_Metric

    @Measure_Metric.setter
    def Measure_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Metric__Measure_Metric", None)
        self.__Measure_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measure_Measure"):
                opp_val = getattr(old_value, "Measure_Measure", None)
                if opp_val == self:
                    setattr(old_value, "Measure_Measure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measure_Measure"):
                opp_val = getattr(value, "Measure_Measure", None)
                setattr(value, "Measure_Measure", self)

    @property
    def metrics(self):
        return self.__metrics

    @metrics.setter
    def metrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Metric__metrics", None)
        self.__metrics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category6"):
                opp_val = getattr(old_value, "Category6", None)
                if opp_val == self:
                    setattr(old_value, "Category6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category6"):
                opp_val = getattr(value, "Category6", None)
                setattr(value, "Category6", self)

    @property
    def Metric(self):
        return self.__Metric

    @Metric.setter
    def Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Metric__Metric", None)
        self.__Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Measure_MeasureSet:

    def __init__(self, elementType: str, elementName: str, MeasureSet: "Measure_RootMeasureSet" = None, owner: set["Measure_Measure"] = None, measureSets: "Measure_RootMeasureSet" = None, MeasureSet12: "Measure_MeasureSet" = None, parent: set["Measure_MeasureSet"] = None, MeasureSet15: "Measure_MeasureSet" = None, subsets: "Measure_MeasureSet" = None, MeasureSet18: "Measure_Measure" = None):
        self.elementType = elementType
        self.elementName = elementName
        self.MeasureSet = MeasureSet
        self.owner = owner if owner is not None else set()
        self.measureSets = measureSets
        self.MeasureSet12 = MeasureSet12
        self.parent = parent if parent is not None else set()
        self.MeasureSet15 = MeasureSet15
        self.subsets = subsets
        self.MeasureSet18 = MeasureSet18
        
    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    setattr(item, "Measure", self)
                    

    @property
    def MeasureSet(self):
        return self.__MeasureSet

    @MeasureSet.setter
    def MeasureSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__MeasureSet", None)
        self.__MeasureSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root2"):
                opp_val = getattr(old_value, "root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root2"):
                opp_val = getattr(value, "root2", None)
                if opp_val is None:
                    setattr(value, "root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def measureSets(self):
        return self.__measureSets

    @measureSets.setter
    def measureSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__measureSets", None)
        self.__measureSets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootMeasureSet9"):
                opp_val = getattr(old_value, "RootMeasureSet9", None)
                if opp_val == self:
                    setattr(old_value, "RootMeasureSet9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootMeasureSet9"):
                opp_val = getattr(value, "RootMeasureSet9", None)
                setattr(value, "RootMeasureSet9", self)

    @property
    def subsets(self):
        return self.__subsets

    @subsets.setter
    def subsets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__subsets", None)
        self.__subsets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MeasureSet15"):
                opp_val = getattr(old_value, "MeasureSet15", None)
                if opp_val == self:
                    setattr(old_value, "MeasureSet15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MeasureSet15"):
                opp_val = getattr(value, "MeasureSet15", None)
                setattr(value, "MeasureSet15", self)

    @property
    def MeasureSet12(self):
        return self.__MeasureSet12

    @MeasureSet12.setter
    def MeasureSet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__MeasureSet12", None)
        self.__MeasureSet12 = value
        
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
    def MeasureSet15(self):
        return self.__MeasureSet15

    @MeasureSet15.setter
    def MeasureSet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__MeasureSet15", None)
        self.__MeasureSet15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subsets"):
                opp_val = getattr(old_value, "subsets", None)
                if opp_val == self:
                    setattr(old_value, "subsets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subsets"):
                opp_val = getattr(value, "subsets", None)
                setattr(value, "subsets", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureSet12"):
                    opp_val = getattr(item, "MeasureSet12", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureSet12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureSet12"):
                    opp_val = getattr(item, "MeasureSet12", None)
                    
                    setattr(item, "MeasureSet12", self)
                    

    @property
    def MeasureSet18(self):
        return self.__MeasureSet18

    @MeasureSet18.setter
    def MeasureSet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_MeasureSet__MeasureSet18", None)
        self.__MeasureSet18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures"):
                opp_val = getattr(old_value, "measures", None)
                if opp_val == self:
                    setattr(old_value, "measures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures"):
                opp_val = getattr(value, "measures", None)
                setattr(value, "measures", self)

class Measure_Category:

    def __init__(self, name: str, desc: str, Category: "Measure_RootMeasureSet" = None, category: set["Measure_Metric"] = None, categories: "Measure_RootMeasureSet" = None, Category6: "Measure_Metric" = None):
        self.name = name
        self.desc = desc
        self.Category = Category
        self.category = category if category is not None else set()
        self.categories = categories
        self.Category6 = Category6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def Category6(self):
        return self.__Category6

    @Category6.setter
    def Category6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Category__Category6", None)
        self.__Category6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics"):
                opp_val = getattr(old_value, "metrics", None)
                if opp_val == self:
                    setattr(old_value, "metrics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics"):
                opp_val = getattr(value, "metrics", None)
                setattr(value, "metrics", self)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Category__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    setattr(item, "Metric", self)
                    

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Category__categories", None)
        self.__categories = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootMeasureSet"):
                opp_val = getattr(old_value, "RootMeasureSet", None)
                if opp_val == self:
                    setattr(old_value, "RootMeasureSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootMeasureSet"):
                opp_val = getattr(value, "RootMeasureSet", None)
                setattr(value, "RootMeasureSet", self)

    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_Category__Category", None)
        self.__Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root"):
                opp_val = getattr(old_value, "root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root"):
                opp_val = getattr(value, "root", None)
                if opp_val is None:
                    setattr(value, "root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Measure_RootMeasureSet:

    def __init__(self, modelType: str, root: set["Measure_Category"] = None, root2: set["Measure_MeasureSet"] = None, RootMeasureSet: "Measure_Category" = None, RootMeasureSet9: "Measure_MeasureSet" = None):
        self.modelType = modelType
        self.root = root if root is not None else set()
        self.root2 = root2 if root2 is not None else set()
        self.RootMeasureSet = RootMeasureSet
        self.RootMeasureSet9 = RootMeasureSet9
        
    @property
    def modelType(self) -> str:
        return self.__modelType

    @modelType.setter
    def modelType(self, modelType: str):
        self.__modelType = modelType

    @property
    def RootMeasureSet(self):
        return self.__RootMeasureSet

    @RootMeasureSet.setter
    def RootMeasureSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_RootMeasureSet__RootMeasureSet", None)
        self.__RootMeasureSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categories"):
                opp_val = getattr(old_value, "categories", None)
                if opp_val == self:
                    setattr(old_value, "categories", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categories"):
                opp_val = getattr(value, "categories", None)
                setattr(value, "categories", self)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_RootMeasureSet__root", None)
        self.__root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    if opp_val == self:
                        setattr(item, "Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    setattr(item, "Category", self)
                    

    @property
    def RootMeasureSet9(self):
        return self.__RootMeasureSet9

    @RootMeasureSet9.setter
    def RootMeasureSet9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_RootMeasureSet__RootMeasureSet9", None)
        self.__RootMeasureSet9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measureSets"):
                opp_val = getattr(old_value, "measureSets", None)
                if opp_val == self:
                    setattr(old_value, "measureSets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measureSets"):
                opp_val = getattr(value, "measureSets", None)
                setattr(value, "measureSets", self)

    @property
    def root2(self):
        return self.__root2

    @root2.setter
    def root2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure_RootMeasureSet__root2", None)
        self.__root2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureSet"):
                    opp_val = getattr(item, "MeasureSet", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureSet"):
                    opp_val = getattr(item, "MeasureSet", None)
                    
                    setattr(item, "MeasureSet", self)
                    

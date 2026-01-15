from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class java_AnnotationInstanceParameter:

    def __init__(self, name: str, parameter: set["java_AnnotationInstanceValue"] = None, parameters: "java_AnnotationInstance" = None, AnnotationInstanceParameter62: "java_AnnotationInstanceValue" = None, AnnotationInstanceParameter: "java_AnnotationInstance" = None):
        self.name = name
        self.parameter = parameter if parameter is not None else set()
        self.parameters = parameters
        self.AnnotationInstanceParameter62 = AnnotationInstanceParameter62
        self.AnnotationInstanceParameter = AnnotationInstanceParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationInstance60"):
                opp_val = getattr(old_value, "AnnotationInstance60", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationInstance60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationInstance60"):
                opp_val = getattr(value, "AnnotationInstance60", None)
                setattr(value, "AnnotationInstance60", self)

    @property
    def AnnotationInstanceParameter(self):
        return self.__AnnotationInstanceParameter

    @AnnotationInstanceParameter.setter
    def AnnotationInstanceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceParameter__AnnotationInstanceParameter", None)
        self.__AnnotationInstanceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance"):
                opp_val = getattr(old_value, "instance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance"):
                opp_val = getattr(value, "instance", None)
                if opp_val is None:
                    setattr(value, "instance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AnnotationInstanceParameter62(self):
        return self.__AnnotationInstanceParameter62

    @AnnotationInstanceParameter62.setter
    def AnnotationInstanceParameter62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceParameter__AnnotationInstanceParameter62", None)
        self.__AnnotationInstanceParameter62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "values"):
                opp_val = getattr(old_value, "values", None)
                if opp_val == self:
                    setattr(old_value, "values", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "values"):
                opp_val = getattr(value, "values", None)
                setattr(value, "values", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceParameter__parameter", None)
        self.__parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnnotationInstanceValue"):
                    opp_val = getattr(item, "AnnotationInstanceValue", None)
                    
                    if opp_val == self:
                        setattr(item, "AnnotationInstanceValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnnotationInstanceValue"):
                    opp_val = getattr(item, "AnnotationInstanceValue", None)
                    
                    setattr(item, "AnnotationInstanceValue", self)
                    

class java_AnnotationInstanceValue:

    def __init__(self, value: str, id: int, name: str, AnnotationInstanceValue: "java_AnnotationInstanceParameter" = None, values: "java_AnnotationInstanceParameter" = None):
        self.value = value
        self.id = id
        self.name = name
        self.AnnotationInstanceValue = AnnotationInstanceValue
        self.values = values
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceValue__values", None)
        self.__values = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationInstanceParameter62"):
                opp_val = getattr(old_value, "AnnotationInstanceParameter62", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationInstanceParameter62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationInstanceParameter62"):
                opp_val = getattr(value, "AnnotationInstanceParameter62", None)
                setattr(value, "AnnotationInstanceParameter62", self)

    @property
    def AnnotationInstanceValue(self):
        return self.__AnnotationInstanceValue

    @AnnotationInstanceValue.setter
    def AnnotationInstanceValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstanceValue__AnnotationInstanceValue", None)
        self.__AnnotationInstanceValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter"):
                opp_val = getattr(old_value, "parameter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter"):
                opp_val = getattr(value, "parameter", None)
                if opp_val is None:
                    setattr(value, "parameter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_AnnotationInstance:

    def __init__(self, name: str, AnnotationInstance: "java_Annotable" = None, AnnotationInstance60: "java_AnnotationInstanceParameter" = None, java_AnnotationInstance: "java_Annotation" = None, instance: set["java_AnnotationInstanceParameter"] = None, annotationInstances: "java_Annotable" = None):
        self.name = name
        self.AnnotationInstance = AnnotationInstance
        self.AnnotationInstance60 = AnnotationInstance60
        self.java_AnnotationInstance = java_AnnotationInstance
        self.instance = instance if instance is not None else set()
        self.annotationInstances = annotationInstances
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_AnnotationInstance(self):
        return self.__java_AnnotationInstance

    @java_AnnotationInstance.setter
    def java_AnnotationInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstance__java_AnnotationInstance", None)
        self.__java_AnnotationInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Annotation"):
                opp_val = getattr(old_value, "java_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "java_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Annotation"):
                opp_val = getattr(value, "java_Annotation", None)
                setattr(value, "java_Annotation", self)

    @property
    def annotationInstances(self):
        return self.__annotationInstances

    @annotationInstances.setter
    def annotationInstances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstance__annotationInstances", None)
        self.__annotationInstances = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Annotable"):
                opp_val = getattr(old_value, "Annotable", None)
                if opp_val == self:
                    setattr(old_value, "Annotable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Annotable"):
                opp_val = getattr(value, "Annotable", None)
                setattr(value, "Annotable", self)

    @property
    def AnnotationInstance(self):
        return self.__AnnotationInstance

    @AnnotationInstance.setter
    def AnnotationInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstance__AnnotationInstance", None)
        self.__AnnotationInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotable"):
                opp_val = getattr(old_value, "annotable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotable"):
                opp_val = getattr(value, "annotable", None)
                if opp_val is None:
                    setattr(value, "annotable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AnnotationInstance60(self):
        return self.__AnnotationInstance60

    @AnnotationInstance60.setter
    def AnnotationInstance60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstance__AnnotationInstance60", None)
        self.__AnnotationInstance60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotationInstance__instance", None)
        self.__instance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnnotationInstanceParameter"):
                    opp_val = getattr(item, "AnnotationInstanceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "AnnotationInstanceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnnotationInstanceParameter"):
                    opp_val = getattr(item, "AnnotationInstanceParameter", None)
                    
                    setattr(item, "AnnotationInstanceParameter", self)
                    

class java_Annotable(ABC):

    pass
class java_Argument:

    def __init__(self, name: str, order: int, Argument: "java_Method" = None, java_Argument: "java_Classifier" = None, arguments: "java_Method" = None):
        self.name = name
        self.order = order
        self.Argument = Argument
        self.java_Argument = java_Argument
        self.arguments = arguments
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arguments(self):
        return self.__arguments

    @arguments.setter
    def arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Argument__arguments", None)
        self.__arguments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method45"):
                opp_val = getattr(old_value, "Method45", None)
                if opp_val == self:
                    setattr(old_value, "Method45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method45"):
                opp_val = getattr(value, "Method45", None)
                setattr(value, "Method45", self)

    @property
    def Argument(self):
        return self.__Argument

    @Argument.setter
    def Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Argument__Argument", None)
        self.__Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usingMethod"):
                opp_val = getattr(old_value, "usingMethod", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usingMethod"):
                opp_val = getattr(value, "usingMethod", None)
                if opp_val is None:
                    setattr(value, "usingMethod", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Argument(self):
        return self.__java_Argument

    @java_Argument.setter
    def java_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Argument__java_Argument", None)
        self.__java_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier43"):
                opp_val = getattr(old_value, "java_Classifier43", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier43"):
                opp_val = getattr(value, "java_Classifier43", None)
                setattr(value, "java_Classifier43", self)

class java_GETExpression:

    def __init__(self, rightSide: str, leftSide: str, GETExpression: "java_AssertStatement" = None, assertion: "java_AssertStatement" = None):
        self.rightSide = rightSide
        self.leftSide = leftSide
        self.GETExpression = GETExpression
        self.assertion = assertion
        
    @property
    def rightSide(self) -> str:
        return self.__rightSide

    @rightSide.setter
    def rightSide(self, rightSide: str):
        self.__rightSide = rightSide

    @property
    def leftSide(self) -> str:
        return self.__leftSide

    @leftSide.setter
    def leftSide(self, leftSide: str):
        self.__leftSide = leftSide

    @property
    def GETExpression(self):
        return self.__GETExpression

    @GETExpression.setter
    def GETExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GETExpression__GETExpression", None)
        self.__GETExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerStatement"):
                opp_val = getattr(old_value, "containerStatement", None)
                if opp_val == self:
                    setattr(old_value, "containerStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerStatement"):
                opp_val = getattr(value, "containerStatement", None)
                setattr(value, "containerStatement", self)

    @property
    def assertion(self):
        return self.__assertion

    @assertion.setter
    def assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GETExpression__assertion", None)
        self.__assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssertStatement"):
                opp_val = getattr(old_value, "AssertStatement", None)
                if opp_val == self:
                    setattr(old_value, "AssertStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssertStatement"):
                opp_val = getattr(value, "AssertStatement", None)
                setattr(value, "AssertStatement", self)

class Statement:

    pass
class java_AssertStatement(Statement):

    pass
class java_Statement(ABC):

    def __init__(self, name: str, Statement: "java_Method" = None, body: "java_Method" = None):
        self.name = name
        self.Statement = Statement
        self.body = body
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Statement(self):
        return self.__Statement

    @Statement.setter
    def Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__Statement", None)
        self.__Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "method"):
                opp_val = getattr(old_value, "method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "method"):
                opp_val = getattr(value, "method", None)
                if opp_val is None:
                    setattr(value, "method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method39"):
                opp_val = getattr(old_value, "Method39", None)
                if opp_val == self:
                    setattr(old_value, "Method39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method39"):
                opp_val = getattr(value, "Method39", None)
                setattr(value, "Method39", self)

class java_Import:

    def __init__(self, name: str, java_Import: "java_Classifier" = None, imports: "java_Classifier" = None, Import: "java_Classifier" = None):
        self.name = name
        self.java_Import = java_Import
        self.imports = imports
        self.Import = Import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imports(self):
        return self.__imports

    @imports.setter
    def imports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Import__imports", None)
        self.__imports = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier26"):
                opp_val = getattr(old_value, "Classifier26", None)
                if opp_val == self:
                    setattr(old_value, "Classifier26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier26"):
                opp_val = getattr(value, "Classifier26", None)
                setattr(value, "Classifier26", self)

    @property
    def Import(self):
        return self.__Import

    @Import.setter
    def Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Import__Import", None)
        self.__Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importing"):
                opp_val = getattr(old_value, "importing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importing"):
                opp_val = getattr(value, "importing", None)
                if opp_val is None:
                    setattr(value, "importing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Import(self):
        return self.__java_Import

    @java_Import.setter
    def java_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Import__java_Import", None)
        self.__java_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier24"):
                opp_val = getattr(old_value, "java_Classifier24", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier24"):
                opp_val = getattr(value, "java_Classifier24", None)
                setattr(value, "java_Classifier24", self)

class java_Container(ABC):

    pass
class java_Contained(ABC):

    def __init__(self, visibility: str, containedElements: "java_Container" = None, java_Contained: set["java_Class"] = None, Contained: "java_Container" = None):
        self.visibility = visibility
        self.containedElements = containedElements
        self.java_Contained = java_Contained if java_Contained is not None else set()
        self.Contained = Contained
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def Contained(self):
        return self.__Contained

    @Contained.setter
    def Contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Contained__Contained", None)
        self.__Contained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Contained(self):
        return self.__java_Contained

    @java_Contained.setter
    def java_Contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Contained__java_Contained", None)
        self.__java_Contained = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Class"):
                    opp_val = getattr(item, "java_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Class"):
                    opp_val = getattr(item, "java_Class", None)
                    
                    setattr(item, "java_Class", self)
                    

    @property
    def containedElements(self):
        return self.__containedElements

    @containedElements.setter
    def containedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Contained__containedElements", None)
        self.__containedElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Container"):
                opp_val = getattr(old_value, "Container", None)
                if opp_val == self:
                    setattr(old_value, "Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Container"):
                opp_val = getattr(value, "Container", None)
                setattr(value, "Container", self)

class java_Generalization:

    def __init__(self, name: str, java_Generalization: "java_Classifier" = None, generalization: "java_Classifier" = None, Generalization: "java_Classifier" = None):
        self.name = name
        self.java_Generalization = java_Generalization
        self.generalization = generalization
        self.Generalization = Generalization
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier11"):
                opp_val = getattr(old_value, "Classifier11", None)
                if opp_val == self:
                    setattr(old_value, "Classifier11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier11"):
                opp_val = getattr(value, "Classifier11", None)
                setattr(value, "Classifier11", self)

    @property
    def java_Generalization(self):
        return self.__java_Generalization

    @java_Generalization.setter
    def java_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Generalization__java_Generalization", None)
        self.__java_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier"):
                opp_val = getattr(old_value, "java_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier"):
                opp_val = getattr(value, "java_Classifier", None)
                setattr(value, "java_Classifier", self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalizator"):
                opp_val = getattr(old_value, "generalizator", None)
                if opp_val == self:
                    setattr(old_value, "generalizator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalizator"):
                opp_val = getattr(value, "generalizator", None)
                setattr(value, "generalizator", self)

class java_InterfaceImplementation:

    def __init__(self, name: str, InterfaceImplementation: "java_Classifier" = None, java_InterfaceImplementation: "java_Interface" = None, interfaceImplementations: "java_Classifier" = None):
        self.name = name
        self.InterfaceImplementation = InterfaceImplementation
        self.java_InterfaceImplementation = java_InterfaceImplementation
        self.interfaceImplementations = interfaceImplementations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def interfaceImplementations(self):
        return self.__interfaceImplementations

    @interfaceImplementations.setter
    def interfaceImplementations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InterfaceImplementation__interfaceImplementations", None)
        self.__interfaceImplementations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

    @property
    def InterfaceImplementation(self):
        return self.__InterfaceImplementation

    @InterfaceImplementation.setter
    def InterfaceImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InterfaceImplementation__InterfaceImplementation", None)
        self.__InterfaceImplementation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "implementer"):
                opp_val = getattr(old_value, "implementer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "implementer"):
                opp_val = getattr(value, "implementer", None)
                if opp_val is None:
                    setattr(value, "implementer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_InterfaceImplementation(self):
        return self.__java_InterfaceImplementation

    @java_InterfaceImplementation.setter
    def java_InterfaceImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InterfaceImplementation__java_InterfaceImplementation", None)
        self.__java_InterfaceImplementation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Interface"):
                opp_val = getattr(old_value, "java_Interface", None)
                if opp_val == self:
                    setattr(old_value, "java_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Interface"):
                opp_val = getattr(value, "java_Interface", None)
                setattr(value, "java_Interface", self)

class java_GenericBinding:

    def __init__(self, name: str, GenericBinding: "java_Classifier" = None, java_GenericBinding: set["java_Classifier"] = None, java_GenericBinding50: "java_Classifier" = None, genericBindings: "java_Classifier" = None):
        self.name = name
        self.GenericBinding = GenericBinding
        self.java_GenericBinding = java_GenericBinding if java_GenericBinding is not None else set()
        self.java_GenericBinding50 = java_GenericBinding50
        self.genericBindings = genericBindings
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_GenericBinding50(self):
        return self.__java_GenericBinding50

    @java_GenericBinding50.setter
    def java_GenericBinding50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GenericBinding__java_GenericBinding50", None)
        self.__java_GenericBinding50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier51"):
                opp_val = getattr(old_value, "java_Classifier51", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier51"):
                opp_val = getattr(value, "java_Classifier51", None)
                setattr(value, "java_Classifier51", self)

    @property
    def genericBindings(self):
        return self.__genericBindings

    @genericBindings.setter
    def genericBindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GenericBinding__genericBindings", None)
        self.__genericBindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier53"):
                opp_val = getattr(old_value, "Classifier53", None)
                if opp_val == self:
                    setattr(old_value, "Classifier53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier53"):
                opp_val = getattr(value, "Classifier53", None)
                setattr(value, "Classifier53", self)

    @property
    def java_GenericBinding(self):
        return self.__java_GenericBinding

    @java_GenericBinding.setter
    def java_GenericBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GenericBinding__java_GenericBinding", None)
        self.__java_GenericBinding = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Classifier48"):
                    opp_val = getattr(item, "java_Classifier48", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Classifier48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Classifier48"):
                    opp_val = getattr(item, "java_Classifier48", None)
                    
                    setattr(item, "java_Classifier48", self)
                    

    @property
    def GenericBinding(self):
        return self.__GenericBinding

    @GenericBinding.setter
    def GenericBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_GenericBinding__GenericBinding", None)
        self.__GenericBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usingClassifier"):
                opp_val = getattr(old_value, "usingClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usingClassifier"):
                opp_val = getattr(value, "usingClassifier", None)
                if opp_val is None:
                    setattr(value, "usingClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Annotable:

    pass
class Contained:

    pass
class java_Method(Contained, Annotable):

    def __init__(self, concurrency: str, isAbstract: bool, isDefault: bool, name: str, isFinal: bool, isStatic: bool, Method: "java_Classifier" = None, java_Method35: set["java_Classifier"] = None, method: set["java_Statement"] = None, Method39: "java_Statement" = None, java_Method: "java_Classifier" = None, usingMethod: set["java_Argument"] = None, methods: "java_Classifier" = None, Method45: "java_Argument" = None):
        self.concurrency = concurrency
        self.isAbstract = isAbstract
        self.isDefault = isDefault
        self.name = name
        self.isFinal = isFinal
        self.isStatic = isStatic
        self.Method = Method
        self.java_Method35 = java_Method35 if java_Method35 is not None else set()
        self.method = method if method is not None else set()
        self.Method39 = Method39
        self.java_Method = java_Method
        self.usingMethod = usingMethod if usingMethod is not None else set()
        self.methods = methods
        self.Method45 = Method45
        
    @property
    def isDefault(self) -> bool:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def Method39(self):
        return self.__Method39

    @Method39.setter
    def Method39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__Method39", None)
        self.__Method39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "body"):
                opp_val = getattr(old_value, "body", None)
                if opp_val == self:
                    setattr(old_value, "body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "body"):
                opp_val = getattr(value, "body", None)
                setattr(value, "body", self)

    @property
    def Method45(self):
        return self.__Method45

    @Method45.setter
    def Method45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__Method45", None)
        self.__Method45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arguments"):
                opp_val = getattr(old_value, "arguments", None)
                if opp_val == self:
                    setattr(old_value, "arguments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arguments"):
                opp_val = getattr(value, "arguments", None)
                setattr(value, "arguments", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingClassifier15"):
                opp_val = getattr(old_value, "containingClassifier15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingClassifier15"):
                opp_val = getattr(value, "containingClassifier15", None)
                if opp_val is None:
                    setattr(value, "containingClassifier15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Method(self):
        return self.__java_Method

    @java_Method.setter
    def java_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__java_Method", None)
        self.__java_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier30"):
                opp_val = getattr(old_value, "java_Classifier30", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier30"):
                opp_val = getattr(value, "java_Classifier30", None)
                setattr(value, "java_Classifier30", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier33"):
                opp_val = getattr(old_value, "Classifier33", None)
                if opp_val == self:
                    setattr(old_value, "Classifier33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier33"):
                opp_val = getattr(value, "Classifier33", None)
                setattr(value, "Classifier33", self)

    @property
    def usingMethod(self):
        return self.__usingMethod

    @usingMethod.setter
    def usingMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__usingMethod", None)
        self.__usingMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    setattr(item, "Argument", self)
                    

    @property
    def java_Method35(self):
        return self.__java_Method35

    @java_Method35.setter
    def java_Method35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__java_Method35", None)
        self.__java_Method35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Classifier36"):
                    opp_val = getattr(item, "java_Classifier36", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Classifier36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Classifier36"):
                    opp_val = getattr(item, "java_Classifier36", None)
                    
                    setattr(item, "java_Classifier36", self)
                    

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method__method", None)
        self.__method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

class java_Field(Contained, Annotable):

    def __init__(self, default: str, isStatic: bool, isFinal: bool, name: str, Field: "java_Classifier" = None, java_Field: "java_Classifier" = None, fields: "java_Classifier" = None):
        self.default = default
        self.isStatic = isStatic
        self.isFinal = isFinal
        self.name = name
        self.Field = Field
        self.java_Field = java_Field
        self.fields = fields
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier22"):
                opp_val = getattr(old_value, "Classifier22", None)
                if opp_val == self:
                    setattr(old_value, "Classifier22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier22"):
                opp_val = getattr(value, "Classifier22", None)
                setattr(value, "Classifier22", self)

    @property
    def Field(self):
        return self.__Field

    @Field.setter
    def Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field__Field", None)
        self.__Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingClassifier"):
                opp_val = getattr(old_value, "containingClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingClassifier"):
                opp_val = getattr(value, "containingClassifier", None)
                if opp_val is None:
                    setattr(value, "containingClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Field(self):
        return self.__java_Field

    @java_Field.setter
    def java_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field__java_Field", None)
        self.__java_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Classifier20"):
                opp_val = getattr(old_value, "java_Classifier20", None)
                if opp_val == self:
                    setattr(old_value, "java_Classifier20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Classifier20"):
                opp_val = getattr(value, "java_Classifier20", None)
                setattr(value, "java_Classifier20", self)

class java_System:

    def __init__(self, name: str, system: set["java_Package"] = None, System: "java_Package" = None):
        self.name = name
        self.system = system if system is not None else set()
        self.System = System
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_System__system", None)
        self.__system = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_System__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packages"):
                opp_val = getattr(old_value, "packages", None)
                if opp_val == self:
                    setattr(old_value, "packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packages"):
                opp_val = getattr(value, "packages", None)
                setattr(value, "packages", self)

class Classifier:

    pass
class java_Annotation(Classifier):

    pass
class java_Class(Classifier):

    def __init__(self, isAbstract: bool, isFinal: bool, isStatic: bool, Class: "java_Class" = None, extendingClasses: "java_Class" = None, Class6: "java_Class" = None, extendedClass: "java_Class" = None, java_Class: "java_Contained" = None):
        self.isAbstract = isAbstract
        self.isFinal = isFinal
        self.isStatic = isStatic
        self.Class = Class
        self.extendingClasses = extendingClasses
        self.Class6 = Class6
        self.extendedClass = extendedClass
        self.java_Class = java_Class
        
    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def Class6(self):
        return self.__Class6

    @Class6.setter
    def Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__Class6", None)
        self.__Class6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedClass"):
                opp_val = getattr(old_value, "extendedClass", None)
                if opp_val == self:
                    setattr(old_value, "extendedClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedClass"):
                opp_val = getattr(value, "extendedClass", None)
                setattr(value, "extendedClass", self)

    @property
    def extendingClasses(self):
        return self.__extendingClasses

    @extendingClasses.setter
    def extendingClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__extendingClasses", None)
        self.__extendingClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def java_Class(self):
        return self.__java_Class

    @java_Class.setter
    def java_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__java_Class", None)
        self.__java_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Contained"):
                opp_val = getattr(old_value, "java_Contained", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Contained"):
                opp_val = getattr(value, "java_Contained", None)
                if opp_val is None:
                    setattr(value, "java_Contained", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendingClasses"):
                opp_val = getattr(old_value, "extendingClasses", None)
                if opp_val == self:
                    setattr(old_value, "extendingClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendingClasses"):
                opp_val = getattr(value, "extendingClasses", None)
                setattr(value, "extendingClasses", self)

    @property
    def extendedClass(self):
        return self.__extendedClass

    @extendedClass.setter
    def extendedClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__extendedClass", None)
        self.__extendedClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class6"):
                opp_val = getattr(old_value, "Class6", None)
                if opp_val == self:
                    setattr(old_value, "Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class6"):
                opp_val = getattr(value, "Class6", None)
                setattr(value, "Class6", self)

class Container:

    pass
class java_Interface(Classifier, Contained, Container):

    pass
class java_Classifier(Contained, Container, Annotable):

    def __init__(self, name: str, usingClassifier: set["java_GenericBinding"] = None, containingClassifier: set["java_Field"] = None, containingClassifier15: set["java_Method"] = None, implementer: set["java_InterfaceImplementation"] = None, Classifier: "java_InterfaceImplementation" = None, java_Classifier: "java_Generalization" = None, Classifier11: "java_Generalization" = None, java_Classifier24: "java_Import" = None, Classifier26: "java_Import" = None, generalizator: "java_Generalization" = None, importing: set["java_Import"] = None, java_Classifier20: "java_Field" = None, Classifier22: "java_Field" = None, java_Classifier36: "java_Method" = None, java_Classifier30: "java_Method" = None, Classifier33: "java_Method" = None, java_Classifier48: "java_GenericBinding" = None, java_Classifier51: "java_GenericBinding" = None, Classifier53: "java_GenericBinding" = None, java_Classifier43: "java_Argument" = None):
        self.name = name
        self.usingClassifier = usingClassifier if usingClassifier is not None else set()
        self.containingClassifier = containingClassifier if containingClassifier is not None else set()
        self.containingClassifier15 = containingClassifier15 if containingClassifier15 is not None else set()
        self.implementer = implementer if implementer is not None else set()
        self.Classifier = Classifier
        self.java_Classifier = java_Classifier
        self.Classifier11 = Classifier11
        self.java_Classifier24 = java_Classifier24
        self.Classifier26 = Classifier26
        self.generalizator = generalizator
        self.importing = importing if importing is not None else set()
        self.java_Classifier20 = java_Classifier20
        self.Classifier22 = Classifier22
        self.java_Classifier36 = java_Classifier36
        self.java_Classifier30 = java_Classifier30
        self.Classifier33 = Classifier33
        self.java_Classifier48 = java_Classifier48
        self.java_Classifier51 = java_Classifier51
        self.Classifier53 = Classifier53
        self.java_Classifier43 = java_Classifier43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Classifier20(self):
        return self.__java_Classifier20

    @java_Classifier20.setter
    def java_Classifier20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier20", None)
        self.__java_Classifier20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Field"):
                opp_val = getattr(old_value, "java_Field", None)
                if opp_val == self:
                    setattr(old_value, "java_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Field"):
                opp_val = getattr(value, "java_Field", None)
                setattr(value, "java_Field", self)

    @property
    def java_Classifier30(self):
        return self.__java_Classifier30

    @java_Classifier30.setter
    def java_Classifier30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier30", None)
        self.__java_Classifier30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Method"):
                opp_val = getattr(old_value, "java_Method", None)
                if opp_val == self:
                    setattr(old_value, "java_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Method"):
                opp_val = getattr(value, "java_Method", None)
                setattr(value, "java_Method", self)

    @property
    def java_Classifier43(self):
        return self.__java_Classifier43

    @java_Classifier43.setter
    def java_Classifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier43", None)
        self.__java_Classifier43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Argument"):
                opp_val = getattr(old_value, "java_Argument", None)
                if opp_val == self:
                    setattr(old_value, "java_Argument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Argument"):
                opp_val = getattr(value, "java_Argument", None)
                setattr(value, "java_Argument", self)

    @property
    def java_Classifier(self):
        return self.__java_Classifier

    @java_Classifier.setter
    def java_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier", None)
        self.__java_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Generalization"):
                opp_val = getattr(old_value, "java_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "java_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Generalization"):
                opp_val = getattr(value, "java_Generalization", None)
                setattr(value, "java_Generalization", self)

    @property
    def Classifier33(self):
        return self.__Classifier33

    @Classifier33.setter
    def Classifier33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier33", None)
        self.__Classifier33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def java_Classifier48(self):
        return self.__java_Classifier48

    @java_Classifier48.setter
    def java_Classifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier48", None)
        self.__java_Classifier48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_GenericBinding"):
                opp_val = getattr(old_value, "java_GenericBinding", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_GenericBinding"):
                opp_val = getattr(value, "java_GenericBinding", None)
                if opp_val is None:
                    setattr(value, "java_GenericBinding", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier11(self):
        return self.__Classifier11

    @Classifier11.setter
    def Classifier11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier11", None)
        self.__Classifier11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def Classifier26(self):
        return self.__Classifier26

    @Classifier26.setter
    def Classifier26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier26", None)
        self.__Classifier26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imports"):
                opp_val = getattr(old_value, "imports", None)
                if opp_val == self:
                    setattr(old_value, "imports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imports"):
                opp_val = getattr(value, "imports", None)
                setattr(value, "imports", self)

    @property
    def java_Classifier51(self):
        return self.__java_Classifier51

    @java_Classifier51.setter
    def java_Classifier51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier51", None)
        self.__java_Classifier51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_GenericBinding50"):
                opp_val = getattr(old_value, "java_GenericBinding50", None)
                if opp_val == self:
                    setattr(old_value, "java_GenericBinding50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_GenericBinding50"):
                opp_val = getattr(value, "java_GenericBinding50", None)
                setattr(value, "java_GenericBinding50", self)

    @property
    def implementer(self):
        return self.__implementer

    @implementer.setter
    def implementer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__implementer", None)
        self.__implementer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InterfaceImplementation"):
                    opp_val = getattr(item, "InterfaceImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "InterfaceImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InterfaceImplementation"):
                    opp_val = getattr(item, "InterfaceImplementation", None)
                    
                    setattr(item, "InterfaceImplementation", self)
                    

    @property
    def java_Classifier24(self):
        return self.__java_Classifier24

    @java_Classifier24.setter
    def java_Classifier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier24", None)
        self.__java_Classifier24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Import"):
                opp_val = getattr(old_value, "java_Import", None)
                if opp_val == self:
                    setattr(old_value, "java_Import", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Import"):
                opp_val = getattr(value, "java_Import", None)
                setattr(value, "java_Import", self)

    @property
    def generalizator(self):
        return self.__generalizator

    @generalizator.setter
    def generalizator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__generalizator", None)
        self.__generalizator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Generalization"):
                opp_val = getattr(old_value, "Generalization", None)
                if opp_val == self:
                    setattr(old_value, "Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Generalization"):
                opp_val = getattr(value, "Generalization", None)
                setattr(value, "Generalization", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interfaceImplementations"):
                opp_val = getattr(old_value, "interfaceImplementations", None)
                if opp_val == self:
                    setattr(old_value, "interfaceImplementations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interfaceImplementations"):
                opp_val = getattr(value, "interfaceImplementations", None)
                setattr(value, "interfaceImplementations", self)

    @property
    def usingClassifier(self):
        return self.__usingClassifier

    @usingClassifier.setter
    def usingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__usingClassifier", None)
        self.__usingClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GenericBinding"):
                    opp_val = getattr(item, "GenericBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "GenericBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GenericBinding"):
                    opp_val = getattr(item, "GenericBinding", None)
                    
                    setattr(item, "GenericBinding", self)
                    

    @property
    def Classifier22(self):
        return self.__Classifier22

    @Classifier22.setter
    def Classifier22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier22", None)
        self.__Classifier22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fields"):
                opp_val = getattr(old_value, "fields", None)
                if opp_val == self:
                    setattr(old_value, "fields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fields"):
                opp_val = getattr(value, "fields", None)
                setattr(value, "fields", self)

    @property
    def containingClassifier(self):
        return self.__containingClassifier

    @containingClassifier.setter
    def containingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__containingClassifier", None)
        self.__containingClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    if opp_val == self:
                        setattr(item, "Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    setattr(item, "Field", self)
                    

    @property
    def Classifier53(self):
        return self.__Classifier53

    @Classifier53.setter
    def Classifier53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__Classifier53", None)
        self.__Classifier53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericBindings"):
                opp_val = getattr(old_value, "genericBindings", None)
                if opp_val == self:
                    setattr(old_value, "genericBindings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericBindings"):
                opp_val = getattr(value, "genericBindings", None)
                setattr(value, "genericBindings", self)

    @property
    def importing(self):
        return self.__importing

    @importing.setter
    def importing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__importing", None)
        self.__importing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    if opp_val == self:
                        setattr(item, "Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    setattr(item, "Import", self)
                    

    @property
    def containingClassifier15(self):
        return self.__containingClassifier15

    @containingClassifier15.setter
    def containingClassifier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__containingClassifier15", None)
        self.__containingClassifier15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def java_Classifier36(self):
        return self.__java_Classifier36

    @java_Classifier36.setter
    def java_Classifier36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier36", None)
        self.__java_Classifier36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Method35"):
                opp_val = getattr(old_value, "java_Method35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Method35"):
                opp_val = getattr(value, "java_Method35", None)
                if opp_val is None:
                    setattr(value, "java_Method35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Package(Container):

    def __init__(self, name: str, Package: "java_System" = None, packages: "java_System" = None):
        self.name = name
        self.Package = Package
        self.packages = packages
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Package__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system"):
                opp_val = getattr(old_value, "system", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system"):
                opp_val = getattr(value, "system", None)
                if opp_val is None:
                    setattr(value, "system", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

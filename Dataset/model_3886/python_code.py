from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EGamaLink:

    pass
class EExperiment:

    pass
class gama_EBatchExperiment(EExperiment):

    pass
class gama_EGUIExperiment(EExperiment):

    pass
class gama_EDisplayLink(EGamaLink):

    pass
class gama_EInheritLink(EGamaLink):

    pass
class ESpecies:

    pass
class gama_EWorldAgent(ESpecies):

    pass
class gama_EGrid(ESpecies):

    pass
class gama_EExperiment(ESpecies):

    pass
class gama_EEquationLink(EGamaLink):

    pass
class gama_ERuleLink(EGamaLink):

    pass
class gama_EPerceiveLink(EGamaLink):

    pass
class gama_ETaskLink(EGamaLink):

    pass
class gama_EStateLink(EGamaLink):

    pass
class gama_EPlanLink(EGamaLink):

    pass
class gama_ESubSpeciesLink(EGamaLink):

    pass
class gama_EReflexLink(EGamaLink):

    pass
class gama_EActionLink(EGamaLink):

    pass
class gama_EAspectLink(EGamaLink):

    pass
class gama_EExperimentLink(EGamaLink):

    pass
class gama_EVariable:

    def __init__(self, init: str, min: str, max: str, update: str, function: str, type: str, name: str, hasError: str, error: str, gama_EVariable: "gama_ESpecies" = None, gama_EVariable40: "gama_EAction" = None, gama_EVariable96: "gama_EGamaObject" = None):
        self.init = init
        self.min = min
        self.max = max
        self.update = update
        self.function = function
        self.type = type
        self.name = name
        self.hasError = hasError
        self.error = error
        self.gama_EVariable = gama_EVariable
        self.gama_EVariable40 = gama_EVariable40
        self.gama_EVariable96 = gama_EVariable96
        
    @property
    def hasError(self) -> str:
        return self.__hasError

    @hasError.setter
    def hasError(self, hasError: str):
        self.__hasError = hasError

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def init(self) -> str:
        return self.__init

    @init.setter
    def init(self, init: str):
        self.__init = init

    @property
    def update(self) -> str:
        return self.__update

    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def gama_EVariable96(self):
        return self.__gama_EVariable96

    @gama_EVariable96.setter
    def gama_EVariable96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EVariable__gama_EVariable96", None)
        self.__gama_EVariable96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EGamaObject97"):
                opp_val = getattr(old_value, "gama_EGamaObject97", None)
                if opp_val == self:
                    setattr(old_value, "gama_EGamaObject97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EGamaObject97"):
                opp_val = getattr(value, "gama_EGamaObject97", None)
                setattr(value, "gama_EGamaObject97", self)

    @property
    def gama_EVariable(self):
        return self.__gama_EVariable

    @gama_EVariable.setter
    def gama_EVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EVariable__gama_EVariable", None)
        self.__gama_EVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ESpecies"):
                opp_val = getattr(old_value, "gama_ESpecies", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ESpecies"):
                opp_val = getattr(value, "gama_ESpecies", None)
                if opp_val is None:
                    setattr(value, "gama_ESpecies", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gama_EVariable40(self):
        return self.__gama_EVariable40

    @gama_EVariable40.setter
    def gama_EVariable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EVariable__gama_EVariable40", None)
        self.__gama_EVariable40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EAction39"):
                opp_val = getattr(old_value, "gama_EAction39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EAction39"):
                opp_val = getattr(value, "gama_EAction39", None)
                if opp_val is None:
                    setattr(value, "gama_EAction39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EGamaObject:

    pass
class gama_EDisplay(EGamaObject):

    def __init__(self, layerList: str, gamlCode: str, defineGamlCode: bool, gama_EDisplay: "gama_EDisplayLink" = None, gama_EDisplay91: set["gama_ELayer"] = None, gama_EDisplay93: "gama_EDisplayLink" = None, gama_EDisplay100: "gama_ELayer" = None):
        self.layerList = layerList
        self.gamlCode = gamlCode
        self.defineGamlCode = defineGamlCode
        self.gama_EDisplay = gama_EDisplay
        self.gama_EDisplay91 = gama_EDisplay91 if gama_EDisplay91 is not None else set()
        self.gama_EDisplay93 = gama_EDisplay93
        self.gama_EDisplay100 = gama_EDisplay100
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def layerList(self) -> str:
        return self.__layerList

    @layerList.setter
    def layerList(self, layerList: str):
        self.__layerList = layerList

    @property
    def defineGamlCode(self) -> bool:
        return self.__defineGamlCode

    @defineGamlCode.setter
    def defineGamlCode(self, defineGamlCode: bool):
        self.__defineGamlCode = defineGamlCode

    @property
    def gama_EDisplay100(self):
        return self.__gama_EDisplay100

    @gama_EDisplay100.setter
    def gama_EDisplay100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EDisplay__gama_EDisplay100", None)
        self.__gama_EDisplay100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ELayer99"):
                opp_val = getattr(old_value, "gama_ELayer99", None)
                if opp_val == self:
                    setattr(old_value, "gama_ELayer99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ELayer99"):
                opp_val = getattr(value, "gama_ELayer99", None)
                setattr(value, "gama_ELayer99", self)

    @property
    def gama_EDisplay(self):
        return self.__gama_EDisplay

    @gama_EDisplay.setter
    def gama_EDisplay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EDisplay__gama_EDisplay", None)
        self.__gama_EDisplay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EDisplayLink89"):
                opp_val = getattr(old_value, "gama_EDisplayLink89", None)
                if opp_val == self:
                    setattr(old_value, "gama_EDisplayLink89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EDisplayLink89"):
                opp_val = getattr(value, "gama_EDisplayLink89", None)
                setattr(value, "gama_EDisplayLink89", self)

    @property
    def gama_EDisplay93(self):
        return self.__gama_EDisplay93

    @gama_EDisplay93.setter
    def gama_EDisplay93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EDisplay__gama_EDisplay93", None)
        self.__gama_EDisplay93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EDisplayLink94"):
                opp_val = getattr(old_value, "gama_EDisplayLink94", None)
                if opp_val == self:
                    setattr(old_value, "gama_EDisplayLink94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EDisplayLink94"):
                opp_val = getattr(value, "gama_EDisplayLink94", None)
                setattr(value, "gama_EDisplayLink94", self)

    @property
    def gama_EDisplay91(self):
        return self.__gama_EDisplay91

    @gama_EDisplay91.setter
    def gama_EDisplay91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EDisplay__gama_EDisplay91", None)
        self.__gama_EDisplay91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ELayer"):
                    opp_val = getattr(item, "gama_ELayer", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ELayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ELayer"):
                    opp_val = getattr(item, "gama_ELayer", None)
                    
                    setattr(item, "gama_ELayer", self)
                    

class gama_EEquation(EGamaObject):

    def __init__(self, gamlCode: str, gama_EEquation: set["gama_EEquationLink"] = None, gama_EEquation165: "gama_EEquationLink" = None):
        self.gamlCode = gamlCode
        self.gama_EEquation = gama_EEquation if gama_EEquation is not None else set()
        self.gama_EEquation165 = gama_EEquation165
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EEquation165(self):
        return self.__gama_EEquation165

    @gama_EEquation165.setter
    def gama_EEquation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EEquation__gama_EEquation165", None)
        self.__gama_EEquation165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EEquationLink164"):
                opp_val = getattr(old_value, "gama_EEquationLink164", None)
                if opp_val == self:
                    setattr(old_value, "gama_EEquationLink164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EEquationLink164"):
                opp_val = getattr(value, "gama_EEquationLink164", None)
                setattr(value, "gama_EEquationLink164", self)

    @property
    def gama_EEquation(self):
        return self.__gama_EEquation

    @gama_EEquation.setter
    def gama_EEquation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EEquation__gama_EEquation", None)
        self.__gama_EEquation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EEquationLink162"):
                    opp_val = getattr(item, "gama_EEquationLink162", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EEquationLink162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EEquationLink162"):
                    opp_val = getattr(item, "gama_EEquationLink162", None)
                    
                    setattr(item, "gama_EEquationLink162", self)
                    

class gama_ETask(EGamaObject):

    def __init__(self, gamlCode: str, gama_ETask: set["gama_ETaskLink"] = None, gama_ETask141: "gama_ETaskLink" = None):
        self.gamlCode = gamlCode
        self.gama_ETask = gama_ETask if gama_ETask is not None else set()
        self.gama_ETask141 = gama_ETask141
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_ETask141(self):
        return self.__gama_ETask141

    @gama_ETask141.setter
    def gama_ETask141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ETask__gama_ETask141", None)
        self.__gama_ETask141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ETaskLink140"):
                opp_val = getattr(old_value, "gama_ETaskLink140", None)
                if opp_val == self:
                    setattr(old_value, "gama_ETaskLink140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ETaskLink140"):
                opp_val = getattr(value, "gama_ETaskLink140", None)
                setattr(value, "gama_ETaskLink140", self)

    @property
    def gama_ETask(self):
        return self.__gama_ETask

    @gama_ETask.setter
    def gama_ETask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ETask__gama_ETask", None)
        self.__gama_ETask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ETaskLink126"):
                    opp_val = getattr(item, "gama_ETaskLink126", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ETaskLink126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ETaskLink126"):
                    opp_val = getattr(item, "gama_ETaskLink126", None)
                    
                    setattr(item, "gama_ETaskLink126", self)
                    

class gama_EAction(EGamaObject):

    def __init__(self, gamlCode: str, returnType: str, gama_EAction: set["gama_EActionLink"] = None, gama_EAction39: set["gama_EVariable"] = None, gama_EAction70: "gama_EActionLink" = None):
        self.gamlCode = gamlCode
        self.returnType = returnType
        self.gama_EAction = gama_EAction if gama_EAction is not None else set()
        self.gama_EAction39 = gama_EAction39 if gama_EAction39 is not None else set()
        self.gama_EAction70 = gama_EAction70
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def gama_EAction(self):
        return self.__gama_EAction

    @gama_EAction.setter
    def gama_EAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAction__gama_EAction", None)
        self.__gama_EAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EActionLink37"):
                    opp_val = getattr(item, "gama_EActionLink37", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EActionLink37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EActionLink37"):
                    opp_val = getattr(item, "gama_EActionLink37", None)
                    
                    setattr(item, "gama_EActionLink37", self)
                    

    @property
    def gama_EAction39(self):
        return self.__gama_EAction39

    @gama_EAction39.setter
    def gama_EAction39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAction__gama_EAction39", None)
        self.__gama_EAction39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EVariable40"):
                    opp_val = getattr(item, "gama_EVariable40", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EVariable40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EVariable40"):
                    opp_val = getattr(item, "gama_EVariable40", None)
                    
                    setattr(item, "gama_EVariable40", self)
                    

    @property
    def gama_EAction70(self):
        return self.__gama_EAction70

    @gama_EAction70.setter
    def gama_EAction70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAction__gama_EAction70", None)
        self.__gama_EAction70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EActionLink69"):
                opp_val = getattr(old_value, "gama_EActionLink69", None)
                if opp_val == self:
                    setattr(old_value, "gama_EActionLink69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EActionLink69"):
                opp_val = getattr(value, "gama_EActionLink69", None)
                setattr(value, "gama_EActionLink69", self)

class gama_EChartLayer(EGamaObject):

    def __init__(self, style: str, color: str, value: str, gama_EChartLayer: "gama_ELayer" = None):
        self.style = style
        self.color = color
        self.value = value
        self.gama_EChartLayer = gama_EChartLayer
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def gama_EChartLayer(self):
        return self.__gama_EChartLayer

    @gama_EChartLayer.setter
    def gama_EChartLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EChartLayer__gama_EChartLayer", None)
        self.__gama_EChartLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ELayer102"):
                opp_val = getattr(old_value, "gama_ELayer102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ELayer102"):
                opp_val = getattr(value, "gama_ELayer102", None)
                if opp_val is None:
                    setattr(value, "gama_ELayer102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gama_EParameter(EGamaObject):

    def __init__(self, variable: str, min: str, init: str, step: str, max: str, among: str, category: str, gama_EParameter: "gama_EExperiment" = None):
        self.variable = variable
        self.min = min
        self.init = init
        self.step = step
        self.max = max
        self.among = among
        self.category = category
        self.gama_EParameter = gama_EParameter
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def step(self) -> str:
        return self.__step

    @step.setter
    def step(self, step: str):
        self.__step = step

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def init(self) -> str:
        return self.__init

    @init.setter
    def init(self, init: str):
        self.__init = init

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def among(self) -> str:
        return self.__among

    @among.setter
    def among(self, among: str):
        self.__among = among

    @property
    def gama_EParameter(self):
        return self.__gama_EParameter

    @gama_EParameter.setter
    def gama_EParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EParameter__gama_EParameter", None)
        self.__gama_EParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EExperiment52"):
                opp_val = getattr(old_value, "gama_EExperiment52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EExperiment52"):
                opp_val = getattr(value, "gama_EExperiment52", None)
                if opp_val is None:
                    setattr(value, "gama_EExperiment52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gama_EReflex(EGamaObject):

    def __init__(self, gamlCode: str, gama_EReflex: set["gama_EReflexLink"] = None, gama_EReflex82: "gama_EReflexLink" = None):
        self.gamlCode = gamlCode
        self.gama_EReflex = gama_EReflex if gama_EReflex is not None else set()
        self.gama_EReflex82 = gama_EReflex82
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EReflex(self):
        return self.__gama_EReflex

    @gama_EReflex.setter
    def gama_EReflex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EReflex__gama_EReflex", None)
        self.__gama_EReflex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EReflexLink46"):
                    opp_val = getattr(item, "gama_EReflexLink46", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EReflexLink46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EReflexLink46"):
                    opp_val = getattr(item, "gama_EReflexLink46", None)
                    
                    setattr(item, "gama_EReflexLink46", self)
                    

    @property
    def gama_EReflex82(self):
        return self.__gama_EReflex82

    @gama_EReflex82.setter
    def gama_EReflex82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EReflex__gama_EReflex82", None)
        self.__gama_EReflex82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EReflexLink81"):
                opp_val = getattr(old_value, "gama_EReflexLink81", None)
                if opp_val == self:
                    setattr(old_value, "gama_EReflexLink81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EReflexLink81"):
                opp_val = getattr(value, "gama_EReflexLink81", None)
                setattr(value, "gama_EReflexLink81", self)

class gama_ELayer(EGamaObject):

    def __init__(self, gamlCode: str, type: str, file: str, isColorCst: str, colorRBG: str, grid: str, chart_type: str, showLines: bool, text: str, size: str, species: str, agents: str, aspect: str, color: str, gama_ELayer: "gama_EDisplay" = None, gama_ELayer99: "gama_EDisplay" = None, gama_ELayer102: set["gama_EChartLayer"] = None):
        self.gamlCode = gamlCode
        self.type = type
        self.file = file
        self.isColorCst = isColorCst
        self.colorRBG = colorRBG
        self.grid = grid
        self.chart_type = chart_type
        self.showLines = showLines
        self.text = text
        self.size = size
        self.species = species
        self.agents = agents
        self.aspect = aspect
        self.color = color
        self.gama_ELayer = gama_ELayer
        self.gama_ELayer99 = gama_ELayer99
        self.gama_ELayer102 = gama_ELayer102 if gama_ELayer102 is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def grid(self) -> str:
        return self.__grid

    @grid.setter
    def grid(self, grid: str):
        self.__grid = grid

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isColorCst(self) -> str:
        return self.__isColorCst

    @isColorCst.setter
    def isColorCst(self, isColorCst: str):
        self.__isColorCst = isColorCst

    @property
    def species(self) -> str:
        return self.__species

    @species.setter
    def species(self, species: str):
        self.__species = species

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def colorRBG(self) -> str:
        return self.__colorRBG

    @colorRBG.setter
    def colorRBG(self, colorRBG: str):
        self.__colorRBG = colorRBG

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def showLines(self) -> bool:
        return self.__showLines

    @showLines.setter
    def showLines(self, showLines: bool):
        self.__showLines = showLines

    @property
    def agents(self) -> str:
        return self.__agents

    @agents.setter
    def agents(self, agents: str):
        self.__agents = agents

    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def aspect(self) -> str:
        return self.__aspect

    @aspect.setter
    def aspect(self, aspect: str):
        self.__aspect = aspect

    @property
    def chart_type(self) -> str:
        return self.__chart_type

    @chart_type.setter
    def chart_type(self, chart_type: str):
        self.__chart_type = chart_type

    @property
    def gama_ELayer99(self):
        return self.__gama_ELayer99

    @gama_ELayer99.setter
    def gama_ELayer99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ELayer__gama_ELayer99", None)
        self.__gama_ELayer99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EDisplay100"):
                opp_val = getattr(old_value, "gama_EDisplay100", None)
                if opp_val == self:
                    setattr(old_value, "gama_EDisplay100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EDisplay100"):
                opp_val = getattr(value, "gama_EDisplay100", None)
                setattr(value, "gama_EDisplay100", self)

    @property
    def gama_ELayer(self):
        return self.__gama_ELayer

    @gama_ELayer.setter
    def gama_ELayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ELayer__gama_ELayer", None)
        self.__gama_ELayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EDisplay91"):
                opp_val = getattr(old_value, "gama_EDisplay91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EDisplay91"):
                opp_val = getattr(value, "gama_EDisplay91", None)
                if opp_val is None:
                    setattr(value, "gama_EDisplay91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gama_ELayer102(self):
        return self.__gama_ELayer102

    @gama_ELayer102.setter
    def gama_ELayer102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ELayer__gama_ELayer102", None)
        self.__gama_ELayer102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EChartLayer"):
                    opp_val = getattr(item, "gama_EChartLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EChartLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EChartLayer"):
                    opp_val = getattr(item, "gama_EChartLayer", None)
                    
                    setattr(item, "gama_EChartLayer", self)
                    

class gama_EPlan(EGamaObject):

    def __init__(self, gamlCode: str, gama_EPlan: set["gama_EPlanLink"] = None, gama_EPlan129: "gama_EPlanLink" = None):
        self.gamlCode = gamlCode
        self.gama_EPlan = gama_EPlan if gama_EPlan is not None else set()
        self.gama_EPlan129 = gama_EPlan129
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EPlan129(self):
        return self.__gama_EPlan129

    @gama_EPlan129.setter
    def gama_EPlan129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EPlan__gama_EPlan129", None)
        self.__gama_EPlan129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EPlanLink128"):
                opp_val = getattr(old_value, "gama_EPlanLink128", None)
                if opp_val == self:
                    setattr(old_value, "gama_EPlanLink128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EPlanLink128"):
                opp_val = getattr(value, "gama_EPlanLink128", None)
                setattr(value, "gama_EPlanLink128", self)

    @property
    def gama_EPlan(self):
        return self.__gama_EPlan

    @gama_EPlan.setter
    def gama_EPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EPlan__gama_EPlan", None)
        self.__gama_EPlan = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EPlanLink122"):
                    opp_val = getattr(item, "gama_EPlanLink122", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EPlanLink122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EPlanLink122"):
                    opp_val = getattr(item, "gama_EPlanLink122", None)
                    
                    setattr(item, "gama_EPlanLink122", self)
                    

class gama_EPerceive(EGamaObject):

    def __init__(self, gamlCode: str, gama_EPerceive: set["gama_EPerceiveLink"] = None, gama_EPerceive149: "gama_EPerceiveLink" = None):
        self.gamlCode = gamlCode
        self.gama_EPerceive = gama_EPerceive if gama_EPerceive is not None else set()
        self.gama_EPerceive149 = gama_EPerceive149
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EPerceive(self):
        return self.__gama_EPerceive

    @gama_EPerceive.setter
    def gama_EPerceive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EPerceive__gama_EPerceive", None)
        self.__gama_EPerceive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EPerceiveLink146"):
                    opp_val = getattr(item, "gama_EPerceiveLink146", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EPerceiveLink146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EPerceiveLink146"):
                    opp_val = getattr(item, "gama_EPerceiveLink146", None)
                    
                    setattr(item, "gama_EPerceiveLink146", self)
                    

    @property
    def gama_EPerceive149(self):
        return self.__gama_EPerceive149

    @gama_EPerceive149.setter
    def gama_EPerceive149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EPerceive__gama_EPerceive149", None)
        self.__gama_EPerceive149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EPerceiveLink148"):
                opp_val = getattr(old_value, "gama_EPerceiveLink148", None)
                if opp_val == self:
                    setattr(old_value, "gama_EPerceiveLink148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EPerceiveLink148"):
                opp_val = getattr(value, "gama_EPerceiveLink148", None)
                setattr(value, "gama_EPerceiveLink148", self)

class gama_ELayerAspect(EGamaObject):

    def __init__(self, gamlCode: str, shape: str, color: str, empty: str, rotate: str, size: str, width: str, heigth: str, radius: str, path: str, text: str, type: str, expression: str, points: str, at: str, shapeType: str, isColorCst: str, textSize: str, imageSize: str, colorRBG: str, depth: str, texture: str, gama_ELayerAspect: "gama_EAspect" = None, gama_ELayerAspect110: "gama_EAspect" = None):
        self.gamlCode = gamlCode
        self.shape = shape
        self.color = color
        self.empty = empty
        self.rotate = rotate
        self.size = size
        self.width = width
        self.heigth = heigth
        self.radius = radius
        self.path = path
        self.text = text
        self.type = type
        self.expression = expression
        self.points = points
        self.at = at
        self.shapeType = shapeType
        self.isColorCst = isColorCst
        self.textSize = textSize
        self.imageSize = imageSize
        self.colorRBG = colorRBG
        self.depth = depth
        self.texture = texture
        self.gama_ELayerAspect = gama_ELayerAspect
        self.gama_ELayerAspect110 = gama_ELayerAspect110
        
    @property
    def empty(self) -> str:
        return self.__empty

    @empty.setter
    def empty(self, empty: str):
        self.__empty = empty

    @property
    def rotate(self) -> str:
        return self.__rotate

    @rotate.setter
    def rotate(self, rotate: str):
        self.__rotate = rotate

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def radius(self) -> str:
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius

    @property
    def heigth(self) -> str:
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth: str):
        self.__heigth = heigth

    @property
    def shapeType(self) -> str:
        return self.__shapeType

    @shapeType.setter
    def shapeType(self, shapeType: str):
        self.__shapeType = shapeType

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def imageSize(self) -> str:
        return self.__imageSize

    @imageSize.setter
    def imageSize(self, imageSize: str):
        self.__imageSize = imageSize

    @property
    def texture(self) -> str:
        return self.__texture

    @texture.setter
    def texture(self, texture: str):
        self.__texture = texture

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def at(self) -> str:
        return self.__at

    @at.setter
    def at(self, at: str):
        self.__at = at

    @property
    def isColorCst(self) -> str:
        return self.__isColorCst

    @isColorCst.setter
    def isColorCst(self, isColorCst: str):
        self.__isColorCst = isColorCst

    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def colorRBG(self) -> str:
        return self.__colorRBG

    @colorRBG.setter
    def colorRBG(self, colorRBG: str):
        self.__colorRBG = colorRBG

    @property
    def textSize(self) -> str:
        return self.__textSize

    @textSize.setter
    def textSize(self, textSize: str):
        self.__textSize = textSize

    @property
    def gama_ELayerAspect110(self):
        return self.__gama_ELayerAspect110

    @gama_ELayerAspect110.setter
    def gama_ELayerAspect110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ELayerAspect__gama_ELayerAspect110", None)
        self.__gama_ELayerAspect110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EAspect111"):
                opp_val = getattr(old_value, "gama_EAspect111", None)
                if opp_val == self:
                    setattr(old_value, "gama_EAspect111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EAspect111"):
                opp_val = getattr(value, "gama_EAspect111", None)
                setattr(value, "gama_EAspect111", self)

    @property
    def gama_ELayerAspect(self):
        return self.__gama_ELayerAspect

    @gama_ELayerAspect.setter
    def gama_ELayerAspect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ELayerAspect__gama_ELayerAspect", None)
        self.__gama_ELayerAspect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EAspect44"):
                opp_val = getattr(old_value, "gama_EAspect44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EAspect44"):
                opp_val = getattr(value, "gama_EAspect44", None)
                if opp_val is None:
                    setattr(value, "gama_EAspect44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gama_ERule(EGamaObject):

    def __init__(self, gamlCode: str, gama_ERule: set["gama_ERuleLink"] = None, gama_ERule157: "gama_ERuleLink" = None):
        self.gamlCode = gamlCode
        self.gama_ERule = gama_ERule if gama_ERule is not None else set()
        self.gama_ERule157 = gama_ERule157
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_ERule157(self):
        return self.__gama_ERule157

    @gama_ERule157.setter
    def gama_ERule157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ERule__gama_ERule157", None)
        self.__gama_ERule157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ERuleLink156"):
                opp_val = getattr(old_value, "gama_ERuleLink156", None)
                if opp_val == self:
                    setattr(old_value, "gama_ERuleLink156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ERuleLink156"):
                opp_val = getattr(value, "gama_ERuleLink156", None)
                setattr(value, "gama_ERuleLink156", self)

    @property
    def gama_ERule(self):
        return self.__gama_ERule

    @gama_ERule.setter
    def gama_ERule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ERule__gama_ERule", None)
        self.__gama_ERule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ERuleLink154"):
                    opp_val = getattr(item, "gama_ERuleLink154", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ERuleLink154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ERuleLink154"):
                    opp_val = getattr(item, "gama_ERuleLink154", None)
                    
                    setattr(item, "gama_ERuleLink154", self)
                    

class gama_EAspect(EGamaObject):

    def __init__(self, gamlCode: str, defineGamlCode: bool, gama_EAspect: set["gama_EAspectLink"] = None, gama_EAspect44: set["gama_ELayerAspect"] = None, gama_EAspect76: "gama_EAspectLink" = None, gama_EAspect111: "gama_ELayerAspect" = None):
        self.gamlCode = gamlCode
        self.defineGamlCode = defineGamlCode
        self.gama_EAspect = gama_EAspect if gama_EAspect is not None else set()
        self.gama_EAspect44 = gama_EAspect44 if gama_EAspect44 is not None else set()
        self.gama_EAspect76 = gama_EAspect76
        self.gama_EAspect111 = gama_EAspect111
        
    @property
    def defineGamlCode(self) -> bool:
        return self.__defineGamlCode

    @defineGamlCode.setter
    def defineGamlCode(self, defineGamlCode: bool):
        self.__defineGamlCode = defineGamlCode

    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EAspect111(self):
        return self.__gama_EAspect111

    @gama_EAspect111.setter
    def gama_EAspect111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAspect__gama_EAspect111", None)
        self.__gama_EAspect111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ELayerAspect110"):
                opp_val = getattr(old_value, "gama_ELayerAspect110", None)
                if opp_val == self:
                    setattr(old_value, "gama_ELayerAspect110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ELayerAspect110"):
                opp_val = getattr(value, "gama_ELayerAspect110", None)
                setattr(value, "gama_ELayerAspect110", self)

    @property
    def gama_EAspect44(self):
        return self.__gama_EAspect44

    @gama_EAspect44.setter
    def gama_EAspect44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAspect__gama_EAspect44", None)
        self.__gama_EAspect44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ELayerAspect"):
                    opp_val = getattr(item, "gama_ELayerAspect", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ELayerAspect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ELayerAspect"):
                    opp_val = getattr(item, "gama_ELayerAspect", None)
                    
                    setattr(item, "gama_ELayerAspect", self)
                    

    @property
    def gama_EAspect76(self):
        return self.__gama_EAspect76

    @gama_EAspect76.setter
    def gama_EAspect76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAspect__gama_EAspect76", None)
        self.__gama_EAspect76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EAspectLink75"):
                opp_val = getattr(old_value, "gama_EAspectLink75", None)
                if opp_val == self:
                    setattr(old_value, "gama_EAspectLink75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EAspectLink75"):
                opp_val = getattr(value, "gama_EAspectLink75", None)
                setattr(value, "gama_EAspectLink75", self)

    @property
    def gama_EAspect(self):
        return self.__gama_EAspect

    @gama_EAspect.setter
    def gama_EAspect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EAspect__gama_EAspect", None)
        self.__gama_EAspect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EAspectLink42"):
                    opp_val = getattr(item, "gama_EAspectLink42", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EAspectLink42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EAspectLink42"):
                    opp_val = getattr(item, "gama_EAspectLink42", None)
                    
                    setattr(item, "gama_EAspectLink42", self)
                    

class gama_EState(EGamaObject):

    def __init__(self, gamlCode: str, gama_EState: set["gama_EStateLink"] = None, gama_EState135: "gama_EStateLink" = None):
        self.gamlCode = gamlCode
        self.gama_EState = gama_EState if gama_EState is not None else set()
        self.gama_EState135 = gama_EState135
        
    @property
    def gamlCode(self) -> str:
        return self.__gamlCode

    @gamlCode.setter
    def gamlCode(self, gamlCode: str):
        self.__gamlCode = gamlCode

    @property
    def gama_EState135(self):
        return self.__gama_EState135

    @gama_EState135.setter
    def gama_EState135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EState__gama_EState135", None)
        self.__gama_EState135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EStateLink134"):
                opp_val = getattr(old_value, "gama_EStateLink134", None)
                if opp_val == self:
                    setattr(old_value, "gama_EStateLink134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EStateLink134"):
                opp_val = getattr(value, "gama_EStateLink134", None)
                setattr(value, "gama_EStateLink134", self)

    @property
    def gama_EState(self):
        return self.__gama_EState

    @gama_EState.setter
    def gama_EState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EState__gama_EState", None)
        self.__gama_EState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EStateLink124"):
                    opp_val = getattr(item, "gama_EStateLink124", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EStateLink124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EStateLink124"):
                    opp_val = getattr(item, "gama_EStateLink124", None)
                    
                    setattr(item, "gama_EStateLink124", self)
                    

class gama_EMonitor(EGamaObject):

    def __init__(self, value: str, gama_EMonitor: "gama_EExperiment" = None):
        self.value = value
        self.gama_EMonitor = gama_EMonitor
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def gama_EMonitor(self):
        return self.__gama_EMonitor

    @gama_EMonitor.setter
    def gama_EMonitor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EMonitor__gama_EMonitor", None)
        self.__gama_EMonitor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EExperiment54"):
                opp_val = getattr(old_value, "gama_EExperiment54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EExperiment54"):
                opp_val = getattr(value, "gama_EExperiment54", None)
                if opp_val is None:
                    setattr(value, "gama_EExperiment54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gama_ESpecies(EGamaObject):

    def __init__(self, reflexList: str, skills: str, init: str, gama_ESpecies: set["gama_EVariable"] = None, gama_ESpecies7: set["gama_EExperimentLink"] = None, gama_ESpecies9: set["gama_EAspectLink"] = None, gama_ESpecies11: set["gama_EActionLink"] = None, gama_ESpecies13: set["gama_EReflexLink"] = None, gama_ESpecies15: set["gama_ESubSpeciesLink"] = None, gama_ESpecies17: set["gama_ESubSpeciesLink"] = None, gama_ESpecies21: "gama_ESpecies" = None, gama_ESpecies19: "gama_ESpecies" = None, gama_ESpecies25: set["gama_EPlanLink"] = None, gama_ESpecies27: set["gama_EStateLink"] = None, gama_ESpecies29: set["gama_ETaskLink"] = None, gama_ESpecies31: set["gama_EPerceiveLink"] = None, gama_ESpecies33: set["gama_ERuleLink"] = None, gama_ESpecies35: set["gama_EEquationLink"] = None, gama_ESpecies23: set["gama_EInheritLink"] = None, gama_ESpecies64: "gama_ESubSpeciesLink" = None, gama_ESpecies67: "gama_ESubSpeciesLink" = None, gama_ESpecies73: "gama_EActionLink" = None, gama_ESpecies85: "gama_EReflexLink" = None, gama_ESpecies79: "gama_EAspectLink" = None, gama_ESpecies105: "gama_EExperimentLink" = None, gama_ESpecies117: "gama_EInheritLink" = None, gama_ESpecies114: "gama_EInheritLink" = None, gama_ESpecies138: "gama_EStateLink" = None, gama_ESpecies144: "gama_ETaskLink" = None, gama_ESpecies152: "gama_EPerceiveLink" = None, gama_ESpecies160: "gama_ERuleLink" = None, gama_ESpecies132: "gama_EPlanLink" = None, gama_ESpecies168: "gama_EEquationLink" = None):
        self.reflexList = reflexList
        self.skills = skills
        self.init = init
        self.gama_ESpecies = gama_ESpecies if gama_ESpecies is not None else set()
        self.gama_ESpecies7 = gama_ESpecies7 if gama_ESpecies7 is not None else set()
        self.gama_ESpecies9 = gama_ESpecies9 if gama_ESpecies9 is not None else set()
        self.gama_ESpecies11 = gama_ESpecies11 if gama_ESpecies11 is not None else set()
        self.gama_ESpecies13 = gama_ESpecies13 if gama_ESpecies13 is not None else set()
        self.gama_ESpecies15 = gama_ESpecies15 if gama_ESpecies15 is not None else set()
        self.gama_ESpecies17 = gama_ESpecies17 if gama_ESpecies17 is not None else set()
        self.gama_ESpecies21 = gama_ESpecies21
        self.gama_ESpecies19 = gama_ESpecies19
        self.gama_ESpecies25 = gama_ESpecies25 if gama_ESpecies25 is not None else set()
        self.gama_ESpecies27 = gama_ESpecies27 if gama_ESpecies27 is not None else set()
        self.gama_ESpecies29 = gama_ESpecies29 if gama_ESpecies29 is not None else set()
        self.gama_ESpecies31 = gama_ESpecies31 if gama_ESpecies31 is not None else set()
        self.gama_ESpecies33 = gama_ESpecies33 if gama_ESpecies33 is not None else set()
        self.gama_ESpecies35 = gama_ESpecies35 if gama_ESpecies35 is not None else set()
        self.gama_ESpecies23 = gama_ESpecies23 if gama_ESpecies23 is not None else set()
        self.gama_ESpecies64 = gama_ESpecies64
        self.gama_ESpecies67 = gama_ESpecies67
        self.gama_ESpecies73 = gama_ESpecies73
        self.gama_ESpecies85 = gama_ESpecies85
        self.gama_ESpecies79 = gama_ESpecies79
        self.gama_ESpecies105 = gama_ESpecies105
        self.gama_ESpecies117 = gama_ESpecies117
        self.gama_ESpecies114 = gama_ESpecies114
        self.gama_ESpecies138 = gama_ESpecies138
        self.gama_ESpecies144 = gama_ESpecies144
        self.gama_ESpecies152 = gama_ESpecies152
        self.gama_ESpecies160 = gama_ESpecies160
        self.gama_ESpecies132 = gama_ESpecies132
        self.gama_ESpecies168 = gama_ESpecies168
        
    @property
    def reflexList(self) -> str:
        return self.__reflexList

    @reflexList.setter
    def reflexList(self, reflexList: str):
        self.__reflexList = reflexList

    @property
    def init(self) -> str:
        return self.__init

    @init.setter
    def init(self, init: str):
        self.__init = init

    @property
    def skills(self) -> str:
        return self.__skills

    @skills.setter
    def skills(self, skills: str):
        self.__skills = skills

    @property
    def gama_ESpecies67(self):
        return self.__gama_ESpecies67

    @gama_ESpecies67.setter
    def gama_ESpecies67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies67", None)
        self.__gama_ESpecies67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ESubSpeciesLink66"):
                opp_val = getattr(old_value, "gama_ESubSpeciesLink66", None)
                if opp_val == self:
                    setattr(old_value, "gama_ESubSpeciesLink66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ESubSpeciesLink66"):
                opp_val = getattr(value, "gama_ESubSpeciesLink66", None)
                setattr(value, "gama_ESubSpeciesLink66", self)

    @property
    def gama_ESpecies35(self):
        return self.__gama_ESpecies35

    @gama_ESpecies35.setter
    def gama_ESpecies35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies35", None)
        self.__gama_ESpecies35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EEquationLink"):
                    opp_val = getattr(item, "gama_EEquationLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EEquationLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EEquationLink"):
                    opp_val = getattr(item, "gama_EEquationLink", None)
                    
                    setattr(item, "gama_EEquationLink", self)
                    

    @property
    def gama_ESpecies105(self):
        return self.__gama_ESpecies105

    @gama_ESpecies105.setter
    def gama_ESpecies105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies105", None)
        self.__gama_ESpecies105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EExperimentLink104"):
                opp_val = getattr(old_value, "gama_EExperimentLink104", None)
                if opp_val == self:
                    setattr(old_value, "gama_EExperimentLink104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EExperimentLink104"):
                opp_val = getattr(value, "gama_EExperimentLink104", None)
                setattr(value, "gama_EExperimentLink104", self)

    @property
    def gama_ESpecies19(self):
        return self.__gama_ESpecies19

    @gama_ESpecies19.setter
    def gama_ESpecies19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies19", None)
        self.__gama_ESpecies19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ESpecies21"):
                opp_val = getattr(old_value, "gama_ESpecies21", None)
                if opp_val == self:
                    setattr(old_value, "gama_ESpecies21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ESpecies21"):
                opp_val = getattr(value, "gama_ESpecies21", None)
                setattr(value, "gama_ESpecies21", self)

    @property
    def gama_ESpecies25(self):
        return self.__gama_ESpecies25

    @gama_ESpecies25.setter
    def gama_ESpecies25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies25", None)
        self.__gama_ESpecies25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EPlanLink"):
                    opp_val = getattr(item, "gama_EPlanLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EPlanLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EPlanLink"):
                    opp_val = getattr(item, "gama_EPlanLink", None)
                    
                    setattr(item, "gama_EPlanLink", self)
                    

    @property
    def gama_ESpecies117(self):
        return self.__gama_ESpecies117

    @gama_ESpecies117.setter
    def gama_ESpecies117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies117", None)
        self.__gama_ESpecies117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EInheritLink116"):
                opp_val = getattr(old_value, "gama_EInheritLink116", None)
                if opp_val == self:
                    setattr(old_value, "gama_EInheritLink116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EInheritLink116"):
                opp_val = getattr(value, "gama_EInheritLink116", None)
                setattr(value, "gama_EInheritLink116", self)

    @property
    def gama_ESpecies85(self):
        return self.__gama_ESpecies85

    @gama_ESpecies85.setter
    def gama_ESpecies85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies85", None)
        self.__gama_ESpecies85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EReflexLink84"):
                opp_val = getattr(old_value, "gama_EReflexLink84", None)
                if opp_val == self:
                    setattr(old_value, "gama_EReflexLink84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EReflexLink84"):
                opp_val = getattr(value, "gama_EReflexLink84", None)
                setattr(value, "gama_EReflexLink84", self)

    @property
    def gama_ESpecies15(self):
        return self.__gama_ESpecies15

    @gama_ESpecies15.setter
    def gama_ESpecies15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies15", None)
        self.__gama_ESpecies15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ESubSpeciesLink"):
                    opp_val = getattr(item, "gama_ESubSpeciesLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ESubSpeciesLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ESubSpeciesLink"):
                    opp_val = getattr(item, "gama_ESubSpeciesLink", None)
                    
                    setattr(item, "gama_ESubSpeciesLink", self)
                    

    @property
    def gama_ESpecies160(self):
        return self.__gama_ESpecies160

    @gama_ESpecies160.setter
    def gama_ESpecies160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies160", None)
        self.__gama_ESpecies160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ERuleLink159"):
                opp_val = getattr(old_value, "gama_ERuleLink159", None)
                if opp_val == self:
                    setattr(old_value, "gama_ERuleLink159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ERuleLink159"):
                opp_val = getattr(value, "gama_ERuleLink159", None)
                setattr(value, "gama_ERuleLink159", self)

    @property
    def gama_ESpecies17(self):
        return self.__gama_ESpecies17

    @gama_ESpecies17.setter
    def gama_ESpecies17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies17", None)
        self.__gama_ESpecies17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ESubSpeciesLink18"):
                    opp_val = getattr(item, "gama_ESubSpeciesLink18", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ESubSpeciesLink18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ESubSpeciesLink18"):
                    opp_val = getattr(item, "gama_ESubSpeciesLink18", None)
                    
                    setattr(item, "gama_ESubSpeciesLink18", self)
                    

    @property
    def gama_ESpecies11(self):
        return self.__gama_ESpecies11

    @gama_ESpecies11.setter
    def gama_ESpecies11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies11", None)
        self.__gama_ESpecies11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EActionLink"):
                    opp_val = getattr(item, "gama_EActionLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EActionLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EActionLink"):
                    opp_val = getattr(item, "gama_EActionLink", None)
                    
                    setattr(item, "gama_EActionLink", self)
                    

    @property
    def gama_ESpecies27(self):
        return self.__gama_ESpecies27

    @gama_ESpecies27.setter
    def gama_ESpecies27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies27", None)
        self.__gama_ESpecies27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EStateLink"):
                    opp_val = getattr(item, "gama_EStateLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EStateLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EStateLink"):
                    opp_val = getattr(item, "gama_EStateLink", None)
                    
                    setattr(item, "gama_EStateLink", self)
                    

    @property
    def gama_ESpecies13(self):
        return self.__gama_ESpecies13

    @gama_ESpecies13.setter
    def gama_ESpecies13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies13", None)
        self.__gama_ESpecies13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EReflexLink"):
                    opp_val = getattr(item, "gama_EReflexLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EReflexLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EReflexLink"):
                    opp_val = getattr(item, "gama_EReflexLink", None)
                    
                    setattr(item, "gama_EReflexLink", self)
                    

    @property
    def gama_ESpecies29(self):
        return self.__gama_ESpecies29

    @gama_ESpecies29.setter
    def gama_ESpecies29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies29", None)
        self.__gama_ESpecies29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ETaskLink"):
                    opp_val = getattr(item, "gama_ETaskLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ETaskLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ETaskLink"):
                    opp_val = getattr(item, "gama_ETaskLink", None)
                    
                    setattr(item, "gama_ETaskLink", self)
                    

    @property
    def gama_ESpecies33(self):
        return self.__gama_ESpecies33

    @gama_ESpecies33.setter
    def gama_ESpecies33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies33", None)
        self.__gama_ESpecies33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_ERuleLink"):
                    opp_val = getattr(item, "gama_ERuleLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_ERuleLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_ERuleLink"):
                    opp_val = getattr(item, "gama_ERuleLink", None)
                    
                    setattr(item, "gama_ERuleLink", self)
                    

    @property
    def gama_ESpecies138(self):
        return self.__gama_ESpecies138

    @gama_ESpecies138.setter
    def gama_ESpecies138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies138", None)
        self.__gama_ESpecies138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EStateLink137"):
                opp_val = getattr(old_value, "gama_EStateLink137", None)
                if opp_val == self:
                    setattr(old_value, "gama_EStateLink137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EStateLink137"):
                opp_val = getattr(value, "gama_EStateLink137", None)
                setattr(value, "gama_EStateLink137", self)

    @property
    def gama_ESpecies79(self):
        return self.__gama_ESpecies79

    @gama_ESpecies79.setter
    def gama_ESpecies79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies79", None)
        self.__gama_ESpecies79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EAspectLink78"):
                opp_val = getattr(old_value, "gama_EAspectLink78", None)
                if opp_val == self:
                    setattr(old_value, "gama_EAspectLink78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EAspectLink78"):
                opp_val = getattr(value, "gama_EAspectLink78", None)
                setattr(value, "gama_EAspectLink78", self)

    @property
    def gama_ESpecies21(self):
        return self.__gama_ESpecies21

    @gama_ESpecies21.setter
    def gama_ESpecies21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies21", None)
        self.__gama_ESpecies21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ESpecies19"):
                opp_val = getattr(old_value, "gama_ESpecies19", None)
                if opp_val == self:
                    setattr(old_value, "gama_ESpecies19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ESpecies19"):
                opp_val = getattr(value, "gama_ESpecies19", None)
                setattr(value, "gama_ESpecies19", self)

    @property
    def gama_ESpecies152(self):
        return self.__gama_ESpecies152

    @gama_ESpecies152.setter
    def gama_ESpecies152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies152", None)
        self.__gama_ESpecies152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EPerceiveLink151"):
                opp_val = getattr(old_value, "gama_EPerceiveLink151", None)
                if opp_val == self:
                    setattr(old_value, "gama_EPerceiveLink151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EPerceiveLink151"):
                opp_val = getattr(value, "gama_EPerceiveLink151", None)
                setattr(value, "gama_EPerceiveLink151", self)

    @property
    def gama_ESpecies144(self):
        return self.__gama_ESpecies144

    @gama_ESpecies144.setter
    def gama_ESpecies144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies144", None)
        self.__gama_ESpecies144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ETaskLink143"):
                opp_val = getattr(old_value, "gama_ETaskLink143", None)
                if opp_val == self:
                    setattr(old_value, "gama_ETaskLink143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ETaskLink143"):
                opp_val = getattr(value, "gama_ETaskLink143", None)
                setattr(value, "gama_ETaskLink143", self)

    @property
    def gama_ESpecies73(self):
        return self.__gama_ESpecies73

    @gama_ESpecies73.setter
    def gama_ESpecies73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies73", None)
        self.__gama_ESpecies73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EActionLink72"):
                opp_val = getattr(old_value, "gama_EActionLink72", None)
                if opp_val == self:
                    setattr(old_value, "gama_EActionLink72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EActionLink72"):
                opp_val = getattr(value, "gama_EActionLink72", None)
                setattr(value, "gama_EActionLink72", self)

    @property
    def gama_ESpecies31(self):
        return self.__gama_ESpecies31

    @gama_ESpecies31.setter
    def gama_ESpecies31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies31", None)
        self.__gama_ESpecies31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EPerceiveLink"):
                    opp_val = getattr(item, "gama_EPerceiveLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EPerceiveLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EPerceiveLink"):
                    opp_val = getattr(item, "gama_EPerceiveLink", None)
                    
                    setattr(item, "gama_EPerceiveLink", self)
                    

    @property
    def gama_ESpecies132(self):
        return self.__gama_ESpecies132

    @gama_ESpecies132.setter
    def gama_ESpecies132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies132", None)
        self.__gama_ESpecies132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EPlanLink131"):
                opp_val = getattr(old_value, "gama_EPlanLink131", None)
                if opp_val == self:
                    setattr(old_value, "gama_EPlanLink131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EPlanLink131"):
                opp_val = getattr(value, "gama_EPlanLink131", None)
                setattr(value, "gama_EPlanLink131", self)

    @property
    def gama_ESpecies168(self):
        return self.__gama_ESpecies168

    @gama_ESpecies168.setter
    def gama_ESpecies168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies168", None)
        self.__gama_ESpecies168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EEquationLink167"):
                opp_val = getattr(old_value, "gama_EEquationLink167", None)
                if opp_val == self:
                    setattr(old_value, "gama_EEquationLink167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EEquationLink167"):
                opp_val = getattr(value, "gama_EEquationLink167", None)
                setattr(value, "gama_EEquationLink167", self)

    @property
    def gama_ESpecies64(self):
        return self.__gama_ESpecies64

    @gama_ESpecies64.setter
    def gama_ESpecies64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies64", None)
        self.__gama_ESpecies64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_ESubSpeciesLink63"):
                opp_val = getattr(old_value, "gama_ESubSpeciesLink63", None)
                if opp_val == self:
                    setattr(old_value, "gama_ESubSpeciesLink63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_ESubSpeciesLink63"):
                opp_val = getattr(value, "gama_ESubSpeciesLink63", None)
                setattr(value, "gama_ESubSpeciesLink63", self)

    @property
    def gama_ESpecies114(self):
        return self.__gama_ESpecies114

    @gama_ESpecies114.setter
    def gama_ESpecies114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies114", None)
        self.__gama_ESpecies114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EInheritLink113"):
                opp_val = getattr(old_value, "gama_EInheritLink113", None)
                if opp_val == self:
                    setattr(old_value, "gama_EInheritLink113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EInheritLink113"):
                opp_val = getattr(value, "gama_EInheritLink113", None)
                setattr(value, "gama_EInheritLink113", self)

    @property
    def gama_ESpecies7(self):
        return self.__gama_ESpecies7

    @gama_ESpecies7.setter
    def gama_ESpecies7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies7", None)
        self.__gama_ESpecies7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EExperimentLink"):
                    opp_val = getattr(item, "gama_EExperimentLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EExperimentLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EExperimentLink"):
                    opp_val = getattr(item, "gama_EExperimentLink", None)
                    
                    setattr(item, "gama_EExperimentLink", self)
                    

    @property
    def gama_ESpecies(self):
        return self.__gama_ESpecies

    @gama_ESpecies.setter
    def gama_ESpecies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies", None)
        self.__gama_ESpecies = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EVariable"):
                    opp_val = getattr(item, "gama_EVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EVariable"):
                    opp_val = getattr(item, "gama_EVariable", None)
                    
                    setattr(item, "gama_EVariable", self)
                    

    @property
    def gama_ESpecies9(self):
        return self.__gama_ESpecies9

    @gama_ESpecies9.setter
    def gama_ESpecies9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies9", None)
        self.__gama_ESpecies9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EAspectLink"):
                    opp_val = getattr(item, "gama_EAspectLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EAspectLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EAspectLink"):
                    opp_val = getattr(item, "gama_EAspectLink", None)
                    
                    setattr(item, "gama_EAspectLink", self)
                    

    @property
    def gama_ESpecies23(self):
        return self.__gama_ESpecies23

    @gama_ESpecies23.setter
    def gama_ESpecies23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_ESpecies__gama_ESpecies23", None)
        self.__gama_ESpecies23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EInheritLink"):
                    opp_val = getattr(item, "gama_EInheritLink", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EInheritLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EInheritLink"):
                    opp_val = getattr(item, "gama_EInheritLink", None)
                    
                    setattr(item, "gama_EInheritLink", self)
                    

class gama_EFacet:

    def __init__(self, name: str, value: str, gama_EFacet: "gama_EGamaObject" = None, gama_EFacet119: "gama_EGamaObject" = None):
        self.name = name
        self.value = value
        self.gama_EFacet = gama_EFacet
        self.gama_EFacet119 = gama_EFacet119
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def gama_EFacet(self):
        return self.__gama_EFacet

    @gama_EFacet.setter
    def gama_EFacet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EFacet__gama_EFacet", None)
        self.__gama_EFacet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EGamaObject"):
                opp_val = getattr(old_value, "gama_EGamaObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EGamaObject"):
                opp_val = getattr(value, "gama_EGamaObject", None)
                if opp_val is None:
                    setattr(value, "gama_EGamaObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gama_EFacet119(self):
        return self.__gama_EFacet119

    @gama_EFacet119.setter
    def gama_EFacet119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EFacet__gama_EFacet119", None)
        self.__gama_EFacet119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EGamaObject120"):
                opp_val = getattr(old_value, "gama_EGamaObject120", None)
                if opp_val == self:
                    setattr(old_value, "gama_EGamaObject120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EGamaObject120"):
                opp_val = getattr(value, "gama_EGamaObject120", None)
                setattr(value, "gama_EGamaObject120", self)

class gama_EGamaLink:

    pass
class gama_EGamaObject:

    def __init__(self, name: str, colorPicto: str, hasError: str, error: str, EGamaObject: "gama_EGamaModel" = None, objects: "gama_EGamaModel" = None, gama_EGamaObject: set["gama_EFacet"] = None, gama_EGamaObject56: "gama_EGamaLink" = None, gama_EGamaObject59: "gama_EGamaLink" = None, gama_EGamaObject97: "gama_EVariable" = None, gama_EGamaObject120: "gama_EFacet" = None):
        self.name = name
        self.colorPicto = colorPicto
        self.hasError = hasError
        self.error = error
        self.EGamaObject = EGamaObject
        self.objects = objects
        self.gama_EGamaObject = gama_EGamaObject if gama_EGamaObject is not None else set()
        self.gama_EGamaObject56 = gama_EGamaObject56
        self.gama_EGamaObject59 = gama_EGamaObject59
        self.gama_EGamaObject97 = gama_EGamaObject97
        self.gama_EGamaObject120 = gama_EGamaObject120
        
    @property
    def colorPicto(self) -> str:
        return self.__colorPicto

    @colorPicto.setter
    def colorPicto(self, colorPicto: str):
        self.__colorPicto = colorPicto

    @property
    def hasError(self) -> str:
        return self.__hasError

    @hasError.setter
    def hasError(self, hasError: str):
        self.__hasError = hasError

    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EGamaObject(self):
        return self.__EGamaObject

    @EGamaObject.setter
    def EGamaObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__EGamaObject", None)
        self.__EGamaObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gama_EGamaObject97(self):
        return self.__gama_EGamaObject97

    @gama_EGamaObject97.setter
    def gama_EGamaObject97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__gama_EGamaObject97", None)
        self.__gama_EGamaObject97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EVariable96"):
                opp_val = getattr(old_value, "gama_EVariable96", None)
                if opp_val == self:
                    setattr(old_value, "gama_EVariable96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EVariable96"):
                opp_val = getattr(value, "gama_EVariable96", None)
                setattr(value, "gama_EVariable96", self)

    @property
    def gama_EGamaObject120(self):
        return self.__gama_EGamaObject120

    @gama_EGamaObject120.setter
    def gama_EGamaObject120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__gama_EGamaObject120", None)
        self.__gama_EGamaObject120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EFacet119"):
                opp_val = getattr(old_value, "gama_EFacet119", None)
                if opp_val == self:
                    setattr(old_value, "gama_EFacet119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EFacet119"):
                opp_val = getattr(value, "gama_EFacet119", None)
                setattr(value, "gama_EFacet119", self)

    @property
    def gama_EGamaObject(self):
        return self.__gama_EGamaObject

    @gama_EGamaObject.setter
    def gama_EGamaObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__gama_EGamaObject", None)
        self.__gama_EGamaObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gama_EFacet"):
                    opp_val = getattr(item, "gama_EFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "gama_EFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gama_EFacet"):
                    opp_val = getattr(item, "gama_EFacet", None)
                    
                    setattr(item, "gama_EFacet", self)
                    

    @property
    def gama_EGamaObject59(self):
        return self.__gama_EGamaObject59

    @gama_EGamaObject59.setter
    def gama_EGamaObject59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__gama_EGamaObject59", None)
        self.__gama_EGamaObject59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EGamaLink58"):
                opp_val = getattr(old_value, "gama_EGamaLink58", None)
                if opp_val == self:
                    setattr(old_value, "gama_EGamaLink58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EGamaLink58"):
                opp_val = getattr(value, "gama_EGamaLink58", None)
                setattr(value, "gama_EGamaLink58", self)

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__objects", None)
        self.__objects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EGamaModel"):
                opp_val = getattr(old_value, "EGamaModel", None)
                if opp_val == self:
                    setattr(old_value, "EGamaModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EGamaModel"):
                opp_val = getattr(value, "EGamaModel", None)
                setattr(value, "EGamaModel", self)

    @property
    def gama_EGamaObject56(self):
        return self.__gama_EGamaObject56

    @gama_EGamaObject56.setter
    def gama_EGamaObject56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaObject__gama_EGamaObject56", None)
        self.__gama_EGamaObject56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gama_EGamaLink"):
                opp_val = getattr(old_value, "gama_EGamaLink", None)
                if opp_val == self:
                    setattr(old_value, "gama_EGamaLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gama_EGamaLink"):
                opp_val = getattr(value, "gama_EGamaLink", None)
                setattr(value, "gama_EGamaLink", self)

class gama_EGamaModel:

    def __init__(self, name: str, model: set["gama_EGamaObject"] = None, model2: set["gama_EGamaLink"] = None, EGamaModel: "gama_EGamaObject" = None, EGamaModel61: "gama_EGamaLink" = None):
        self.name = name
        self.model = model if model is not None else set()
        self.model2 = model2 if model2 is not None else set()
        self.EGamaModel = EGamaModel
        self.EGamaModel61 = EGamaModel61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EGamaModel(self):
        return self.__EGamaModel

    @EGamaModel.setter
    def EGamaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaModel__EGamaModel", None)
        self.__EGamaModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "objects"):
                opp_val = getattr(old_value, "objects", None)
                if opp_val == self:
                    setattr(old_value, "objects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "objects"):
                opp_val = getattr(value, "objects", None)
                setattr(value, "objects", self)

    @property
    def model2(self):
        return self.__model2

    @model2.setter
    def model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaModel__model2", None)
        self.__model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGamaLink"):
                    opp_val = getattr(item, "EGamaLink", None)
                    
                    if opp_val == self:
                        setattr(item, "EGamaLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGamaLink"):
                    opp_val = getattr(item, "EGamaLink", None)
                    
                    setattr(item, "EGamaLink", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaModel__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGamaObject"):
                    opp_val = getattr(item, "EGamaObject", None)
                    
                    if opp_val == self:
                        setattr(item, "EGamaObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGamaObject"):
                    opp_val = getattr(item, "EGamaObject", None)
                    
                    setattr(item, "EGamaObject", self)
                    

    @property
    def EGamaModel61(self):
        return self.__EGamaModel61

    @EGamaModel61.setter
    def EGamaModel61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gama_EGamaModel__EGamaModel61", None)
        self.__EGamaModel61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links"):
                opp_val = getattr(old_value, "links", None)
                if opp_val == self:
                    setattr(old_value, "links", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links"):
                opp_val = getattr(value, "links", None)
                setattr(value, "links", self)

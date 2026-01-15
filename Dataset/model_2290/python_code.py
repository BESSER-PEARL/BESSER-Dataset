from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sedml_variable:

    def __init__(self, id: str, target: str, symbol: str, sedml_variable: "sedml_listOfVariables" = None, sedml_variable38: "sedml_task" = None):
        self.id = id
        self.target = target
        self.symbol = symbol
        self.sedml_variable = sedml_variable
        self.sedml_variable38 = sedml_variable38
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def sedml_variable(self):
        return self.__sedml_variable

    @sedml_variable.setter
    def sedml_variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_variable__sedml_variable", None)
        self.__sedml_variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfVariables36"):
                opp_val = getattr(old_value, "sedml_listOfVariables36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfVariables36"):
                opp_val = getattr(value, "sedml_listOfVariables36", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfVariables36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sedml_variable38(self):
        return self.__sedml_variable38

    @sedml_variable38.setter
    def sedml_variable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_variable__sedml_variable38", None)
        self.__sedml_variable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_task39"):
                opp_val = getattr(old_value, "sedml_task39", None)
                if opp_val == self:
                    setattr(old_value, "sedml_task39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_task39"):
                opp_val = getattr(value, "sedml_task39", None)
                setattr(value, "sedml_task39", self)

class sedml_math:

    def __init__(self, xlms: str, sedml_math: "sedml_dataGenerator" = None):
        self.xlms = xlms
        self.sedml_math = sedml_math
        
    @property
    def xlms(self) -> str:
        return self.__xlms

    @xlms.setter
    def xlms(self, xlms: str):
        self.__xlms = xlms

    @property
    def sedml_math(self):
        return self.__sedml_math

    @sedml_math.setter
    def sedml_math(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_math__sedml_math", None)
        self.__sedml_math = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_dataGenerator34"):
                opp_val = getattr(old_value, "sedml_dataGenerator34", None)
                if opp_val == self:
                    setattr(old_value, "sedml_dataGenerator34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_dataGenerator34"):
                opp_val = getattr(value, "sedml_dataGenerator34", None)
                setattr(value, "sedml_dataGenerator34", self)

class sedml_listOfVariables:

    pass
class sedml_curve:

    def __init__(self, id: str, logX: str, logY: str, xDataReference: str, yDataReference: str, sedml_curve: "sedml_listOfCurves" = None):
        self.id = id
        self.logX = logX
        self.logY = logY
        self.xDataReference = xDataReference
        self.yDataReference = yDataReference
        self.sedml_curve = sedml_curve
        
    @property
    def yDataReference(self) -> str:
        return self.__yDataReference

    @yDataReference.setter
    def yDataReference(self, yDataReference: str):
        self.__yDataReference = yDataReference

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xDataReference(self) -> str:
        return self.__xDataReference

    @xDataReference.setter
    def xDataReference(self, xDataReference: str):
        self.__xDataReference = xDataReference

    @property
    def logX(self) -> str:
        return self.__logX

    @logX.setter
    def logX(self, logX: str):
        self.__logX = logX

    @property
    def logY(self) -> str:
        return self.__logY

    @logY.setter
    def logY(self, logY: str):
        self.__logY = logY

    @property
    def sedml_curve(self):
        return self.__sedml_curve

    @sedml_curve.setter
    def sedml_curve(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_curve__sedml_curve", None)
        self.__sedml_curve = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfCurves30"):
                opp_val = getattr(old_value, "sedml_listOfCurves30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfCurves30"):
                opp_val = getattr(value, "sedml_listOfCurves30", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfCurves30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sedml_listOfCurves:

    pass
class sedml_algorithm:

    def __init__(self, kisaoID: str, sedml_algorithm: "sedml_uniformTimeCourse" = None):
        self.kisaoID = kisaoID
        self.sedml_algorithm = sedml_algorithm
        
    @property
    def kisaoID(self) -> str:
        return self.__kisaoID

    @kisaoID.setter
    def kisaoID(self, kisaoID: str):
        self.__kisaoID = kisaoID

    @property
    def sedml_algorithm(self):
        return self.__sedml_algorithm

    @sedml_algorithm.setter
    def sedml_algorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_algorithm__sedml_algorithm", None)
        self.__sedml_algorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_uniformTimeCourse20"):
                opp_val = getattr(old_value, "sedml_uniformTimeCourse20", None)
                if opp_val == self:
                    setattr(old_value, "sedml_uniformTimeCourse20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_uniformTimeCourse20"):
                opp_val = getattr(value, "sedml_uniformTimeCourse20", None)
                setattr(value, "sedml_uniformTimeCourse20", self)

class sedml_model:

    def __init__(self, id: str, language: str, source: str, name: str, sedml_model: "sedml_listOfModels" = None, sedml_model23: "sedml_task" = None):
        self.id = id
        self.language = language
        self.source = source
        self.name = name
        self.sedml_model = sedml_model
        self.sedml_model23 = sedml_model23
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sedml_model(self):
        return self.__sedml_model

    @sedml_model.setter
    def sedml_model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_model__sedml_model", None)
        self.__sedml_model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfModels12"):
                opp_val = getattr(old_value, "sedml_listOfModels12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfModels12"):
                opp_val = getattr(value, "sedml_listOfModels12", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfModels12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sedml_model23(self):
        return self.__sedml_model23

    @sedml_model23.setter
    def sedml_model23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_model__sedml_model23", None)
        self.__sedml_model23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_task22"):
                opp_val = getattr(old_value, "sedml_task22", None)
                if opp_val == self:
                    setattr(old_value, "sedml_task22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_task22"):
                opp_val = getattr(value, "sedml_task22", None)
                setattr(value, "sedml_task22", self)

class sedml_plot2D:

    def __init__(self, id: str, name: str, sedml_plot2D: "sedml_listOfOutputs" = None, sedml_plot2D28: "sedml_listOfCurves" = None):
        self.id = id
        self.name = name
        self.sedml_plot2D = sedml_plot2D
        self.sedml_plot2D28 = sedml_plot2D28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sedml_plot2D28(self):
        return self.__sedml_plot2D28

    @sedml_plot2D28.setter
    def sedml_plot2D28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_plot2D__sedml_plot2D28", None)
        self.__sedml_plot2D28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfCurves"):
                opp_val = getattr(old_value, "sedml_listOfCurves", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfCurves", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfCurves"):
                opp_val = getattr(value, "sedml_listOfCurves", None)
                setattr(value, "sedml_listOfCurves", self)

    @property
    def sedml_plot2D(self):
        return self.__sedml_plot2D

    @sedml_plot2D.setter
    def sedml_plot2D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_plot2D__sedml_plot2D", None)
        self.__sedml_plot2D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfOutputs18"):
                opp_val = getattr(old_value, "sedml_listOfOutputs18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfOutputs18"):
                opp_val = getattr(value, "sedml_listOfOutputs18", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfOutputs18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sedml_dataGenerator:

    def __init__(self, id: str, name: str, sedml_dataGenerator: "sedml_listOfDataGenerators" = None, sedml_dataGenerator32: "sedml_listOfVariables" = None, sedml_dataGenerator34: "sedml_math" = None):
        self.id = id
        self.name = name
        self.sedml_dataGenerator = sedml_dataGenerator
        self.sedml_dataGenerator32 = sedml_dataGenerator32
        self.sedml_dataGenerator34 = sedml_dataGenerator34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sedml_dataGenerator34(self):
        return self.__sedml_dataGenerator34

    @sedml_dataGenerator34.setter
    def sedml_dataGenerator34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_dataGenerator__sedml_dataGenerator34", None)
        self.__sedml_dataGenerator34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_math"):
                opp_val = getattr(old_value, "sedml_math", None)
                if opp_val == self:
                    setattr(old_value, "sedml_math", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_math"):
                opp_val = getattr(value, "sedml_math", None)
                setattr(value, "sedml_math", self)

    @property
    def sedml_dataGenerator(self):
        return self.__sedml_dataGenerator

    @sedml_dataGenerator.setter
    def sedml_dataGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_dataGenerator__sedml_dataGenerator", None)
        self.__sedml_dataGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfDataGenerators16"):
                opp_val = getattr(old_value, "sedml_listOfDataGenerators16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfDataGenerators16"):
                opp_val = getattr(value, "sedml_listOfDataGenerators16", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfDataGenerators16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sedml_dataGenerator32(self):
        return self.__sedml_dataGenerator32

    @sedml_dataGenerator32.setter
    def sedml_dataGenerator32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_dataGenerator__sedml_dataGenerator32", None)
        self.__sedml_dataGenerator32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfVariables"):
                opp_val = getattr(old_value, "sedml_listOfVariables", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfVariables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfVariables"):
                opp_val = getattr(value, "sedml_listOfVariables", None)
                setattr(value, "sedml_listOfVariables", self)

class sedml_task:

    def __init__(self, name: str, id: str, sedml_task: "sedml_listOfTasks" = None, sedml_task22: "sedml_model" = None, sedml_task25: "sedml_uniformTimeCourse" = None, sedml_task39: "sedml_variable" = None):
        self.name = name
        self.id = id
        self.sedml_task = sedml_task
        self.sedml_task22 = sedml_task22
        self.sedml_task25 = sedml_task25
        self.sedml_task39 = sedml_task39
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sedml_task25(self):
        return self.__sedml_task25

    @sedml_task25.setter
    def sedml_task25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_task__sedml_task25", None)
        self.__sedml_task25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_uniformTimeCourse26"):
                opp_val = getattr(old_value, "sedml_uniformTimeCourse26", None)
                if opp_val == self:
                    setattr(old_value, "sedml_uniformTimeCourse26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_uniformTimeCourse26"):
                opp_val = getattr(value, "sedml_uniformTimeCourse26", None)
                setattr(value, "sedml_uniformTimeCourse26", self)

    @property
    def sedml_task39(self):
        return self.__sedml_task39

    @sedml_task39.setter
    def sedml_task39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_task__sedml_task39", None)
        self.__sedml_task39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_variable38"):
                opp_val = getattr(old_value, "sedml_variable38", None)
                if opp_val == self:
                    setattr(old_value, "sedml_variable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_variable38"):
                opp_val = getattr(value, "sedml_variable38", None)
                setattr(value, "sedml_variable38", self)

    @property
    def sedml_task22(self):
        return self.__sedml_task22

    @sedml_task22.setter
    def sedml_task22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_task__sedml_task22", None)
        self.__sedml_task22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_model23"):
                opp_val = getattr(old_value, "sedml_model23", None)
                if opp_val == self:
                    setattr(old_value, "sedml_model23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_model23"):
                opp_val = getattr(value, "sedml_model23", None)
                setattr(value, "sedml_model23", self)

    @property
    def sedml_task(self):
        return self.__sedml_task

    @sedml_task.setter
    def sedml_task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_task__sedml_task", None)
        self.__sedml_task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfTasks14"):
                opp_val = getattr(old_value, "sedml_listOfTasks14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfTasks14"):
                opp_val = getattr(value, "sedml_listOfTasks14", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfTasks14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sedml_listOfTasks:

    pass
class sedml_uniformTimeCourse:

    def __init__(self, id: str, outputEndTime: int, numberOfPoints: int, initialTime: int, outputStartTime: int, sedml_uniformTimeCourse: "sedml_listOfSimulations" = None, sedml_uniformTimeCourse20: "sedml_algorithm" = None, sedml_uniformTimeCourse26: "sedml_task" = None):
        self.id = id
        self.outputEndTime = outputEndTime
        self.numberOfPoints = numberOfPoints
        self.initialTime = initialTime
        self.outputStartTime = outputStartTime
        self.sedml_uniformTimeCourse = sedml_uniformTimeCourse
        self.sedml_uniformTimeCourse20 = sedml_uniformTimeCourse20
        self.sedml_uniformTimeCourse26 = sedml_uniformTimeCourse26
        
    @property
    def initialTime(self) -> int:
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime

    @property
    def outputStartTime(self) -> int:
        return self.__outputStartTime

    @outputStartTime.setter
    def outputStartTime(self, outputStartTime: int):
        self.__outputStartTime = outputStartTime

    @property
    def numberOfPoints(self) -> int:
        return self.__numberOfPoints

    @numberOfPoints.setter
    def numberOfPoints(self, numberOfPoints: int):
        self.__numberOfPoints = numberOfPoints

    @property
    def outputEndTime(self) -> int:
        return self.__outputEndTime

    @outputEndTime.setter
    def outputEndTime(self, outputEndTime: int):
        self.__outputEndTime = outputEndTime

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sedml_uniformTimeCourse20(self):
        return self.__sedml_uniformTimeCourse20

    @sedml_uniformTimeCourse20.setter
    def sedml_uniformTimeCourse20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_uniformTimeCourse__sedml_uniformTimeCourse20", None)
        self.__sedml_uniformTimeCourse20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_algorithm"):
                opp_val = getattr(old_value, "sedml_algorithm", None)
                if opp_val == self:
                    setattr(old_value, "sedml_algorithm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_algorithm"):
                opp_val = getattr(value, "sedml_algorithm", None)
                setattr(value, "sedml_algorithm", self)

    @property
    def sedml_uniformTimeCourse(self):
        return self.__sedml_uniformTimeCourse

    @sedml_uniformTimeCourse.setter
    def sedml_uniformTimeCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_uniformTimeCourse__sedml_uniformTimeCourse", None)
        self.__sedml_uniformTimeCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfSimulations10"):
                opp_val = getattr(old_value, "sedml_listOfSimulations10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfSimulations10"):
                opp_val = getattr(value, "sedml_listOfSimulations10", None)
                if opp_val is None:
                    setattr(value, "sedml_listOfSimulations10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sedml_uniformTimeCourse26(self):
        return self.__sedml_uniformTimeCourse26

    @sedml_uniformTimeCourse26.setter
    def sedml_uniformTimeCourse26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_uniformTimeCourse__sedml_uniformTimeCourse26", None)
        self.__sedml_uniformTimeCourse26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_task25"):
                opp_val = getattr(old_value, "sedml_task25", None)
                if opp_val == self:
                    setattr(old_value, "sedml_task25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_task25"):
                opp_val = getattr(value, "sedml_task25", None)
                setattr(value, "sedml_task25", self)

class sedml_listOfOutputs:

    pass
class sedml_listOfDataGenerators:

    pass
class sedml_listOfModels:

    pass
class sedml_listOfSimulations:

    pass
class sedml_sedML:

    def __init__(self, version: int, level: int, sedml_sedML: "sedml_listOfSimulations" = None, sedml_sedML6: "sedml_listOfDataGenerators" = None, sedml_sedML8: "sedml_listOfOutputs" = None, sedml_sedML2: "sedml_listOfModels" = None, sedml_sedML4: "sedml_listOfTasks" = None):
        self.version = version
        self.level = level
        self.sedml_sedML = sedml_sedML
        self.sedml_sedML6 = sedml_sedML6
        self.sedml_sedML8 = sedml_sedML8
        self.sedml_sedML2 = sedml_sedML2
        self.sedml_sedML4 = sedml_sedML4
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def sedml_sedML4(self):
        return self.__sedml_sedML4

    @sedml_sedML4.setter
    def sedml_sedML4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_sedML__sedml_sedML4", None)
        self.__sedml_sedML4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfTasks"):
                opp_val = getattr(old_value, "sedml_listOfTasks", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfTasks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfTasks"):
                opp_val = getattr(value, "sedml_listOfTasks", None)
                setattr(value, "sedml_listOfTasks", self)

    @property
    def sedml_sedML(self):
        return self.__sedml_sedML

    @sedml_sedML.setter
    def sedml_sedML(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_sedML__sedml_sedML", None)
        self.__sedml_sedML = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfSimulations"):
                opp_val = getattr(old_value, "sedml_listOfSimulations", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfSimulations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfSimulations"):
                opp_val = getattr(value, "sedml_listOfSimulations", None)
                setattr(value, "sedml_listOfSimulations", self)

    @property
    def sedml_sedML6(self):
        return self.__sedml_sedML6

    @sedml_sedML6.setter
    def sedml_sedML6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_sedML__sedml_sedML6", None)
        self.__sedml_sedML6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfDataGenerators"):
                opp_val = getattr(old_value, "sedml_listOfDataGenerators", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfDataGenerators", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfDataGenerators"):
                opp_val = getattr(value, "sedml_listOfDataGenerators", None)
                setattr(value, "sedml_listOfDataGenerators", self)

    @property
    def sedml_sedML2(self):
        return self.__sedml_sedML2

    @sedml_sedML2.setter
    def sedml_sedML2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_sedML__sedml_sedML2", None)
        self.__sedml_sedML2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfModels"):
                opp_val = getattr(old_value, "sedml_listOfModels", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfModels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfModels"):
                opp_val = getattr(value, "sedml_listOfModels", None)
                setattr(value, "sedml_listOfModels", self)

    @property
    def sedml_sedML8(self):
        return self.__sedml_sedML8

    @sedml_sedML8.setter
    def sedml_sedML8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sedml_sedML__sedml_sedML8", None)
        self.__sedml_sedML8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedml_listOfOutputs"):
                opp_val = getattr(old_value, "sedml_listOfOutputs", None)
                if opp_val == self:
                    setattr(old_value, "sedml_listOfOutputs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedml_listOfOutputs"):
                opp_val = getattr(value, "sedml_listOfOutputs", None)
                setattr(value, "sedml_listOfOutputs", self)

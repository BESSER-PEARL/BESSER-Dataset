from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResultSetScopeType(Enum):
    EXECUTION = "EXECUTION"
    APPLICATION = "APPLICATION"


############################################
# Definition of Classes
############################################

class dbrouting_ResultSet:

    def __init__(self, name: str, scope: str, timeToLive: str, dbrouting_ResultSet: "dbrouting_Executor" = None):
        self.name = name
        self.scope = scope
        self.timeToLive = timeToLive
        self.dbrouting_ResultSet = dbrouting_ResultSet
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def timeToLive(self):
        return self.__timeToLive

    @timeToLive.setter
    def timeToLive(self, timeToLive: str):
        self.__timeToLive = timeToLive


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def dbrouting_ResultSet(self):
        return self.__dbrouting_ResultSet

    @dbrouting_ResultSet.setter
    def dbrouting_ResultSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_ResultSet__dbrouting_ResultSet", None)
        self.__dbrouting_ResultSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbrouting_Executor9"):
                opp_val = getattr(old_value, "dbrouting_Executor9", None)
                if opp_val == self:
                    setattr(old_value, "dbrouting_Executor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_Executor9"):
                opp_val = getattr(value, "dbrouting_Executor9", None)
                setattr(value, "dbrouting_Executor9", self)

class ElementVisitor:

    pass
class dbrouting_ResultSetRowSelector(ElementVisitor):

    def __init__(self, executeBefore: str, resultSetName: str, selectRowOnElement: str, where: str, failedSelectError: str, beanId: str, dbrouting_ResultSetRowSelector: "dbrouting_DocumentRoot" = None):
        self.executeBefore = executeBefore
        self.resultSetName = resultSetName
        self.selectRowOnElement = selectRowOnElement
        self.where = where
        self.failedSelectError = failedSelectError
        self.beanId = beanId
        self.dbrouting_ResultSetRowSelector = dbrouting_ResultSetRowSelector
        
        pass
    @property
    def failedSelectError(self):
        return self.__failedSelectError

    @failedSelectError.setter
    def failedSelectError(self, failedSelectError: str):
        self.__failedSelectError = failedSelectError


    @property
    def resultSetName(self):
        return self.__resultSetName

    @resultSetName.setter
    def resultSetName(self, resultSetName: str):
        self.__resultSetName = resultSetName


    @property
    def where(self):
        return self.__where

    @where.setter
    def where(self, where: str):
        self.__where = where


    @property
    def executeBefore(self):
        return self.__executeBefore

    @executeBefore.setter
    def executeBefore(self, executeBefore: str):
        self.__executeBefore = executeBefore


    @property
    def beanId(self):
        return self.__beanId

    @beanId.setter
    def beanId(self, beanId: str):
        self.__beanId = beanId


    @property
    def selectRowOnElement(self):
        return self.__selectRowOnElement

    @selectRowOnElement.setter
    def selectRowOnElement(self, selectRowOnElement: str):
        self.__selectRowOnElement = selectRowOnElement


    @property
    def dbrouting_ResultSetRowSelector(self):
        return self.__dbrouting_ResultSetRowSelector

    @dbrouting_ResultSetRowSelector.setter
    def dbrouting_ResultSetRowSelector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_ResultSetRowSelector__dbrouting_ResultSetRowSelector", None)
        self.__dbrouting_ResultSetRowSelector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbrouting_DocumentRoot7"):
                opp_val = getattr(old_value, "dbrouting_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_DocumentRoot7"):
                opp_val = getattr(value, "dbrouting_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "dbrouting_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbrouting_EStringToStringMapEntry:

    pass
class dbrouting_DocumentRoot:

    def __init__(self, mixed: str, dbrouting_DocumentRoot: set["dbrouting_EStringToStringMapEntry"] = None, dbrouting_DocumentRoot2: set["dbrouting_EStringToStringMapEntry"] = None, dbrouting_DocumentRoot5: set["dbrouting_Executor"] = None, dbrouting_DocumentRoot7: set["dbrouting_ResultSetRowSelector"] = None):
        self.mixed = mixed
        self.dbrouting_DocumentRoot = dbrouting_DocumentRoot if dbrouting_DocumentRoot is not None else set()
        self.dbrouting_DocumentRoot2 = dbrouting_DocumentRoot2 if dbrouting_DocumentRoot2 is not None else set()
        self.dbrouting_DocumentRoot5 = dbrouting_DocumentRoot5 if dbrouting_DocumentRoot5 is not None else set()
        self.dbrouting_DocumentRoot7 = dbrouting_DocumentRoot7 if dbrouting_DocumentRoot7 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def dbrouting_DocumentRoot2(self):
        return self.__dbrouting_DocumentRoot2

    @dbrouting_DocumentRoot2.setter
    def dbrouting_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DocumentRoot__dbrouting_DocumentRoot2", None)
        self.__dbrouting_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbrouting_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "dbrouting_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "dbrouting_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbrouting_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "dbrouting_EStringToStringMapEntry3", None)
                    
                    setattr(item, "dbrouting_EStringToStringMapEntry3", self)
                    

    @property
    def dbrouting_DocumentRoot(self):
        return self.__dbrouting_DocumentRoot

    @dbrouting_DocumentRoot.setter
    def dbrouting_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DocumentRoot__dbrouting_DocumentRoot", None)
        self.__dbrouting_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbrouting_EStringToStringMapEntry"):
                    opp_val = getattr(item, "dbrouting_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "dbrouting_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbrouting_EStringToStringMapEntry"):
                    opp_val = getattr(item, "dbrouting_EStringToStringMapEntry", None)
                    
                    setattr(item, "dbrouting_EStringToStringMapEntry", self)
                    

    @property
    def dbrouting_DocumentRoot7(self):
        return self.__dbrouting_DocumentRoot7

    @dbrouting_DocumentRoot7.setter
    def dbrouting_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DocumentRoot__dbrouting_DocumentRoot7", None)
        self.__dbrouting_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbrouting_ResultSetRowSelector"):
                    opp_val = getattr(item, "dbrouting_ResultSetRowSelector", None)
                    
                    if opp_val == self:
                        setattr(item, "dbrouting_ResultSetRowSelector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbrouting_ResultSetRowSelector"):
                    opp_val = getattr(item, "dbrouting_ResultSetRowSelector", None)
                    
                    setattr(item, "dbrouting_ResultSetRowSelector", self)
                    

    @property
    def dbrouting_DocumentRoot5(self):
        return self.__dbrouting_DocumentRoot5

    @dbrouting_DocumentRoot5.setter
    def dbrouting_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DocumentRoot__dbrouting_DocumentRoot5", None)
        self.__dbrouting_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbrouting_Executor"):
                    opp_val = getattr(item, "dbrouting_Executor", None)
                    
                    if opp_val == self:
                        setattr(item, "dbrouting_Executor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbrouting_Executor"):
                    opp_val = getattr(item, "dbrouting_Executor", None)
                    
                    setattr(item, "dbrouting_Executor", self)
                    

class dbrouting_Executor(ElementVisitor):

    def __init__(self, executeBefore: str, executeOnElement: str, executeOnElementNS: str, statement: str, datasource: str, dbrouting_Executor: "dbrouting_DocumentRoot" = None, dbrouting_Executor9: "dbrouting_ResultSet" = None):
        self.executeBefore = executeBefore
        self.executeOnElement = executeOnElement
        self.executeOnElementNS = executeOnElementNS
        self.statement = statement
        self.datasource = datasource
        self.dbrouting_Executor = dbrouting_Executor
        self.dbrouting_Executor9 = dbrouting_Executor9
        
        pass
    @property
    def executeOnElementNS(self):
        return self.__executeOnElementNS

    @executeOnElementNS.setter
    def executeOnElementNS(self, executeOnElementNS: str):
        self.__executeOnElementNS = executeOnElementNS


    @property
    def statement(self):
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement


    @property
    def executeBefore(self):
        return self.__executeBefore

    @executeBefore.setter
    def executeBefore(self, executeBefore: str):
        self.__executeBefore = executeBefore


    @property
    def datasource(self):
        return self.__datasource

    @datasource.setter
    def datasource(self, datasource: str):
        self.__datasource = datasource


    @property
    def executeOnElement(self):
        return self.__executeOnElement

    @executeOnElement.setter
    def executeOnElement(self, executeOnElement: str):
        self.__executeOnElement = executeOnElement


    @property
    def dbrouting_Executor(self):
        return self.__dbrouting_Executor

    @dbrouting_Executor.setter
    def dbrouting_Executor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_Executor__dbrouting_Executor", None)
        self.__dbrouting_Executor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbrouting_DocumentRoot5"):
                opp_val = getattr(old_value, "dbrouting_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_DocumentRoot5"):
                opp_val = getattr(value, "dbrouting_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "dbrouting_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbrouting_Executor9(self):
        return self.__dbrouting_Executor9

    @dbrouting_Executor9.setter
    def dbrouting_Executor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_Executor__dbrouting_Executor9", None)
        self.__dbrouting_Executor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbrouting_ResultSet"):
                opp_val = getattr(old_value, "dbrouting_ResultSet", None)
                if opp_val == self:
                    setattr(old_value, "dbrouting_ResultSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_ResultSet"):
                opp_val = getattr(value, "dbrouting_ResultSet", None)
                setattr(value, "dbrouting_ResultSet", self)

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

    def __init__(self, timeToLive: str, name: str, scope: str, dbrouting_ResultSet: "dbrouting_Executor" = None):
        self.timeToLive = timeToLive
        self.name = name
        self.scope = scope
        self.dbrouting_ResultSet = dbrouting_ResultSet
        
        pass
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
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
class dbrouting_Executor(ElementVisitor):

    def __init__(self, statement: str, executeBefore: str, executeOnElement: str, executeOnElementNS: str, datasource: str, dbrouting_Executor: "dbrouting_DBRoutingDocumentRoot" = None, dbrouting_Executor9: "dbrouting_ResultSet" = None):
        self.statement = statement
        self.executeBefore = executeBefore
        self.executeOnElement = executeOnElement
        self.executeOnElementNS = executeOnElementNS
        self.datasource = datasource
        self.dbrouting_Executor = dbrouting_Executor
        self.dbrouting_Executor9 = dbrouting_Executor9
        
        pass
    @property
    def executeBefore(self):
        return self.__executeBefore

    @executeBefore.setter
    def executeBefore(self, executeBefore: str):
        self.__executeBefore = executeBefore


    @property
    def statement(self):
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement


    @property
    def datasource(self):
        return self.__datasource

    @datasource.setter
    def datasource(self, datasource: str):
        self.__datasource = datasource


    @property
    def executeOnElementNS(self):
        return self.__executeOnElementNS

    @executeOnElementNS.setter
    def executeOnElementNS(self, executeOnElementNS: str):
        self.__executeOnElementNS = executeOnElementNS


    @property
    def executeOnElement(self):
        return self.__executeOnElement

    @executeOnElement.setter
    def executeOnElement(self, executeOnElement: str):
        self.__executeOnElement = executeOnElement


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
            if hasattr(old_value, "dbrouting_DBRoutingDocumentRoot5"):
                opp_val = getattr(old_value, "dbrouting_DBRoutingDocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_DBRoutingDocumentRoot5"):
                opp_val = getattr(value, "dbrouting_DBRoutingDocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "dbrouting_DBRoutingDocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbrouting_ResultSetRowSelector(ElementVisitor):

    def __init__(self, where: str, executeBefore: str, resultSetName: str, selectRowOnElement: str, failedSelectError: str, beanId: str, dbrouting_ResultSetRowSelector: "dbrouting_DBRoutingDocumentRoot" = None):
        self.where = where
        self.executeBefore = executeBefore
        self.resultSetName = resultSetName
        self.selectRowOnElement = selectRowOnElement
        self.failedSelectError = failedSelectError
        self.beanId = beanId
        self.dbrouting_ResultSetRowSelector = dbrouting_ResultSetRowSelector
        
        pass
    @property
    def beanId(self):
        return self.__beanId

    @beanId.setter
    def beanId(self, beanId: str):
        self.__beanId = beanId


    @property
    def where(self):
        return self.__where

    @where.setter
    def where(self, where: str):
        self.__where = where


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
    def executeBefore(self):
        return self.__executeBefore

    @executeBefore.setter
    def executeBefore(self, executeBefore: str):
        self.__executeBefore = executeBefore


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
            if hasattr(old_value, "dbrouting_DBRoutingDocumentRoot7"):
                opp_val = getattr(old_value, "dbrouting_DBRoutingDocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbrouting_DBRoutingDocumentRoot7"):
                opp_val = getattr(value, "dbrouting_DBRoutingDocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "dbrouting_DBRoutingDocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbrouting_DBRoutingDocumentRoot:

    def __init__(self, mixed: str, dbrouting_DBRoutingDocumentRoot: set["dbrouting_EStringToStringMapEntry"] = None, dbrouting_DBRoutingDocumentRoot2: set["dbrouting_EStringToStringMapEntry"] = None, dbrouting_DBRoutingDocumentRoot5: set["dbrouting_Executor"] = None, dbrouting_DBRoutingDocumentRoot7: set["dbrouting_ResultSetRowSelector"] = None):
        self.mixed = mixed
        self.dbrouting_DBRoutingDocumentRoot = dbrouting_DBRoutingDocumentRoot if dbrouting_DBRoutingDocumentRoot is not None else set()
        self.dbrouting_DBRoutingDocumentRoot2 = dbrouting_DBRoutingDocumentRoot2 if dbrouting_DBRoutingDocumentRoot2 is not None else set()
        self.dbrouting_DBRoutingDocumentRoot5 = dbrouting_DBRoutingDocumentRoot5 if dbrouting_DBRoutingDocumentRoot5 is not None else set()
        self.dbrouting_DBRoutingDocumentRoot7 = dbrouting_DBRoutingDocumentRoot7 if dbrouting_DBRoutingDocumentRoot7 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def dbrouting_DBRoutingDocumentRoot(self):
        return self.__dbrouting_DBRoutingDocumentRoot

    @dbrouting_DBRoutingDocumentRoot.setter
    def dbrouting_DBRoutingDocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DBRoutingDocumentRoot__dbrouting_DBRoutingDocumentRoot", None)
        self.__dbrouting_DBRoutingDocumentRoot = value if value is not None else set()
        
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
    def dbrouting_DBRoutingDocumentRoot2(self):
        return self.__dbrouting_DBRoutingDocumentRoot2

    @dbrouting_DBRoutingDocumentRoot2.setter
    def dbrouting_DBRoutingDocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DBRoutingDocumentRoot__dbrouting_DBRoutingDocumentRoot2", None)
        self.__dbrouting_DBRoutingDocumentRoot2 = value if value is not None else set()
        
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
    def dbrouting_DBRoutingDocumentRoot5(self):
        return self.__dbrouting_DBRoutingDocumentRoot5

    @dbrouting_DBRoutingDocumentRoot5.setter
    def dbrouting_DBRoutingDocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DBRoutingDocumentRoot__dbrouting_DBRoutingDocumentRoot5", None)
        self.__dbrouting_DBRoutingDocumentRoot5 = value if value is not None else set()
        
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
                    

    @property
    def dbrouting_DBRoutingDocumentRoot7(self):
        return self.__dbrouting_DBRoutingDocumentRoot7

    @dbrouting_DBRoutingDocumentRoot7.setter
    def dbrouting_DBRoutingDocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbrouting_DBRoutingDocumentRoot__dbrouting_DBRoutingDocumentRoot7", None)
        self.__dbrouting_DBRoutingDocumentRoot7 = value if value is not None else set()
        
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
                    

class dbrouting_EStringToStringMapEntry:

    pass
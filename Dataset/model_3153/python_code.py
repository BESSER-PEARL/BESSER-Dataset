from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class transformationtrace_RuleParameterTrace:

    def __init__(self, parameterName: str, objectId: str, transformationtrace_RuleParameterTrace: "transformationtrace_ActivationTrace" = None):
        self.parameterName = parameterName
        self.objectId = objectId
        self.transformationtrace_RuleParameterTrace = transformationtrace_RuleParameterTrace
        
    @property
    def objectId(self) -> str:
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId

    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def transformationtrace_RuleParameterTrace(self):
        return self.__transformationtrace_RuleParameterTrace

    @transformationtrace_RuleParameterTrace.setter
    def transformationtrace_RuleParameterTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformationtrace_RuleParameterTrace__transformationtrace_RuleParameterTrace", None)
        self.__transformationtrace_RuleParameterTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformationtrace_ActivationTrace2"):
                opp_val = getattr(old_value, "transformationtrace_ActivationTrace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformationtrace_ActivationTrace2"):
                opp_val = getattr(value, "transformationtrace_ActivationTrace2", None)
                if opp_val is None:
                    setattr(value, "transformationtrace_ActivationTrace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class transformationtrace_ActivationTrace:

    def __init__(self, ruleName: str, transformationtrace_ActivationTrace2: set["transformationtrace_RuleParameterTrace"] = None, transformationtrace_ActivationTrace: "transformationtrace_TransformationTrace" = None):
        self.ruleName = ruleName
        self.transformationtrace_ActivationTrace2 = transformationtrace_ActivationTrace2 if transformationtrace_ActivationTrace2 is not None else set()
        self.transformationtrace_ActivationTrace = transformationtrace_ActivationTrace
        
    @property
    def ruleName(self) -> str:
        return self.__ruleName

    @ruleName.setter
    def ruleName(self, ruleName: str):
        self.__ruleName = ruleName

    @property
    def transformationtrace_ActivationTrace(self):
        return self.__transformationtrace_ActivationTrace

    @transformationtrace_ActivationTrace.setter
    def transformationtrace_ActivationTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformationtrace_ActivationTrace__transformationtrace_ActivationTrace", None)
        self.__transformationtrace_ActivationTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformationtrace_TransformationTrace"):
                opp_val = getattr(old_value, "transformationtrace_TransformationTrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformationtrace_TransformationTrace"):
                opp_val = getattr(value, "transformationtrace_TransformationTrace", None)
                if opp_val is None:
                    setattr(value, "transformationtrace_TransformationTrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transformationtrace_ActivationTrace2(self):
        return self.__transformationtrace_ActivationTrace2

    @transformationtrace_ActivationTrace2.setter
    def transformationtrace_ActivationTrace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformationtrace_ActivationTrace__transformationtrace_ActivationTrace2", None)
        self.__transformationtrace_ActivationTrace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformationtrace_RuleParameterTrace"):
                    opp_val = getattr(item, "transformationtrace_RuleParameterTrace", None)
                    
                    if opp_val == self:
                        setattr(item, "transformationtrace_RuleParameterTrace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformationtrace_RuleParameterTrace"):
                    opp_val = getattr(item, "transformationtrace_RuleParameterTrace", None)
                    
                    setattr(item, "transformationtrace_RuleParameterTrace", self)
                    

class transformationtrace_TransformationTrace:

    pass
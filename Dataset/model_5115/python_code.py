from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class benchmark_Property:

    def __init__(self, value: str, name: str, benchmark_Property: "benchmark_NamedElement" = None, benchmark_Property13: "benchmark_TimeResult" = None):
        self.value = value
        self.name = name
        self.benchmark_Property = benchmark_Property
        self.benchmark_Property13 = benchmark_Property13
        
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
    def benchmark_Property(self):
        return self.__benchmark_Property

    @benchmark_Property.setter
    def benchmark_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_Property__benchmark_Property", None)
        self.__benchmark_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "benchmark_NamedElement"):
                opp_val = getattr(old_value, "benchmark_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "benchmark_NamedElement"):
                opp_val = getattr(value, "benchmark_NamedElement", None)
                if opp_val is None:
                    setattr(value, "benchmark_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def benchmark_Property13(self):
        return self.__benchmark_Property13

    @benchmark_Property13.setter
    def benchmark_Property13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_Property__benchmark_Property13", None)
        self.__benchmark_Property13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "benchmark_TimeResult12"):
                opp_val = getattr(old_value, "benchmark_TimeResult12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "benchmark_TimeResult12"):
                opp_val = getattr(value, "benchmark_TimeResult12", None)
                if opp_val is None:
                    setattr(value, "benchmark_TimeResult12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class benchmark_TimeResult:

    def __init__(self, elapsedTime: str, elapsedMaxTime: str, results: "benchmark_Variant" = None, benchmark_TimeResult12: set["benchmark_Property"] = None, benchmark_TimeResult: "benchmark_TestCase" = None, TimeResult: "benchmark_Variant" = None):
        self.elapsedTime = elapsedTime
        self.elapsedMaxTime = elapsedMaxTime
        self.results = results
        self.benchmark_TimeResult12 = benchmark_TimeResult12 if benchmark_TimeResult12 is not None else set()
        self.benchmark_TimeResult = benchmark_TimeResult
        self.TimeResult = TimeResult
        
    @property
    def elapsedTime(self) -> str:
        return self.__elapsedTime

    @elapsedTime.setter
    def elapsedTime(self, elapsedTime: str):
        self.__elapsedTime = elapsedTime

    @property
    def elapsedMaxTime(self) -> str:
        return self.__elapsedMaxTime

    @elapsedMaxTime.setter
    def elapsedMaxTime(self, elapsedMaxTime: str):
        self.__elapsedMaxTime = elapsedMaxTime

    @property
    def TimeResult(self):
        return self.__TimeResult

    @TimeResult.setter
    def TimeResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_TimeResult__TimeResult", None)
        self.__TimeResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variant"):
                opp_val = getattr(old_value, "variant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variant"):
                opp_val = getattr(value, "variant", None)
                if opp_val is None:
                    setattr(value, "variant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def benchmark_TimeResult(self):
        return self.__benchmark_TimeResult

    @benchmark_TimeResult.setter
    def benchmark_TimeResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_TimeResult__benchmark_TimeResult", None)
        self.__benchmark_TimeResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "benchmark_TestCase7"):
                opp_val = getattr(old_value, "benchmark_TestCase7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "benchmark_TestCase7"):
                opp_val = getattr(value, "benchmark_TestCase7", None)
                if opp_val is None:
                    setattr(value, "benchmark_TestCase7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def results(self):
        return self.__results

    @results.setter
    def results(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_TimeResult__results", None)
        self.__results = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variant"):
                opp_val = getattr(old_value, "Variant", None)
                if opp_val == self:
                    setattr(old_value, "Variant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variant"):
                opp_val = getattr(value, "Variant", None)
                setattr(value, "Variant", self)

    @property
    def benchmark_TimeResult12(self):
        return self.__benchmark_TimeResult12

    @benchmark_TimeResult12.setter
    def benchmark_TimeResult12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_TimeResult__benchmark_TimeResult12", None)
        self.__benchmark_TimeResult12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "benchmark_Property13"):
                    opp_val = getattr(item, "benchmark_Property13", None)
                    
                    if opp_val == self:
                        setattr(item, "benchmark_Property13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "benchmark_Property13"):
                    opp_val = getattr(item, "benchmark_Property13", None)
                    
                    setattr(item, "benchmark_Property13", self)
                    

class NamedElement:

    pass
class benchmark_Variant(NamedElement):

    pass
class benchmark_TestCase(NamedElement):

    pass
class benchmark_InputData(NamedElement):

    pass
class benchmark_Scenario(NamedElement):

    pass
class benchmark_NamedElement:

    def __init__(self, name: str, benchmark_NamedElement: set["benchmark_Property"] = None):
        self.name = name
        self.benchmark_NamedElement = benchmark_NamedElement if benchmark_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def benchmark_NamedElement(self):
        return self.__benchmark_NamedElement

    @benchmark_NamedElement.setter
    def benchmark_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_benchmark_NamedElement__benchmark_NamedElement", None)
        self.__benchmark_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "benchmark_Property"):
                    opp_val = getattr(item, "benchmark_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "benchmark_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "benchmark_Property"):
                    opp_val = getattr(item, "benchmark_Property", None)
                    
                    setattr(item, "benchmark_Property", self)
                    

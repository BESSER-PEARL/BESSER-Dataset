from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test7_FiniteDomainSCValueReference:

    def __init__(self, value: str, test7_FiniteDomainSCValueReference: "test7_FiniteDomainSC" = None):
        self.value = value
        self.test7_FiniteDomainSCValueReference = test7_FiniteDomainSCValueReference
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test7_FiniteDomainSCValueReference(self):
        return self.__test7_FiniteDomainSCValueReference

    @test7_FiniteDomainSCValueReference.setter
    def test7_FiniteDomainSCValueReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FiniteDomainSCValueReference__test7_FiniteDomainSCValueReference", None)
        self.__test7_FiniteDomainSCValueReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FiniteDomainSC34"):
                opp_val = getattr(old_value, "test7_FiniteDomainSC34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FiniteDomainSC34"):
                opp_val = getattr(value, "test7_FiniteDomainSC34", None)
                if opp_val is None:
                    setattr(value, "test7_FiniteDomainSC34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_FeatureAttributeReference:

    pass
class SolutionConstraint:

    pass
class test7_FiniteDomainSC(SolutionConstraint):

    pass
class test7_SelectionStateSC(SolutionConstraint):

    def __init__(self, state: str, test7_SelectionStateSC: "test7_Feature" = None):
        self.state = state
        self.test7_SelectionStateSC = test7_SelectionStateSC
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def test7_SelectionStateSC(self):
        return self.__test7_SelectionStateSC

    @test7_SelectionStateSC.setter
    def test7_SelectionStateSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_SelectionStateSC__test7_SelectionStateSC", None)
        self.__test7_SelectionStateSC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_Feature27"):
                opp_val = getattr(old_value, "test7_Feature27", None)
                if opp_val == self:
                    setattr(old_value, "test7_Feature27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_Feature27"):
                opp_val = getattr(value, "test7_Feature27", None)
                setattr(value, "test7_Feature27", self)

class test7_HardLimitSC(SolutionConstraint):

    def __init__(self, op1: str, value1: str, op2: str, value2: str, test7_HardLimitSC: "test7_AttributeType" = None):
        self.op1 = op1
        self.value1 = value1
        self.op2 = op2
        self.value2 = value2
        self.test7_HardLimitSC = test7_HardLimitSC
        
    @property
    def op2(self) -> str:
        return self.__op2

    @op2.setter
    def op2(self, op2: str):
        self.__op2 = op2

    @property
    def value2(self) -> str:
        return self.__value2

    @value2.setter
    def value2(self, value2: str):
        self.__value2 = value2

    @property
    def value1(self) -> str:
        return self.__value1

    @value1.setter
    def value1(self, value1: str):
        self.__value1 = value1

    @property
    def op1(self) -> str:
        return self.__op1

    @op1.setter
    def op1(self, op1: str):
        self.__op1 = op1

    @property
    def test7_HardLimitSC(self):
        return self.__test7_HardLimitSC

    @test7_HardLimitSC.setter
    def test7_HardLimitSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_HardLimitSC__test7_HardLimitSC", None)
        self.__test7_HardLimitSC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType25"):
                opp_val = getattr(old_value, "test7_AttributeType25", None)
                if opp_val == self:
                    setattr(old_value, "test7_AttributeType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType25"):
                opp_val = getattr(value, "test7_AttributeType25", None)
                setattr(value, "test7_AttributeType25", self)

class test7_OptimizationSC(SolutionConstraint):

    def __init__(self, funct: str, test7_OptimizationSC: "test7_AttributeType" = None):
        self.funct = funct
        self.test7_OptimizationSC = test7_OptimizationSC
        
    @property
    def funct(self) -> str:
        return self.__funct

    @funct.setter
    def funct(self, funct: str):
        self.__funct = funct

    @property
    def test7_OptimizationSC(self):
        return self.__test7_OptimizationSC

    @test7_OptimizationSC.setter
    def test7_OptimizationSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_OptimizationSC__test7_OptimizationSC", None)
        self.__test7_OptimizationSC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType23"):
                opp_val = getattr(old_value, "test7_AttributeType23", None)
                if opp_val == self:
                    setattr(old_value, "test7_AttributeType23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType23"):
                opp_val = getattr(value, "test7_AttributeType23", None)
                setattr(value, "test7_AttributeType23", self)

class test7_AttributeTypeElement:

    def __init__(self, name: str, dataType: str, test7_AttributeTypeElement: "test7_AttributeType" = None):
        self.name = name
        self.dataType = dataType
        self.test7_AttributeTypeElement = test7_AttributeTypeElement
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test7_AttributeTypeElement(self):
        return self.__test7_AttributeTypeElement

    @test7_AttributeTypeElement.setter
    def test7_AttributeTypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeTypeElement__test7_AttributeTypeElement", None)
        self.__test7_AttributeTypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType8"):
                opp_val = getattr(old_value, "test7_AttributeType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType8"):
                opp_val = getattr(value, "test7_AttributeType8", None)
                if opp_val is None:
                    setattr(value, "test7_AttributeType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_FeatureAttributeElement:

    def __init__(self, value: str, test7_FeatureAttributeElement: "test7_FeatureAttribute" = None):
        self.value = value
        self.test7_FeatureAttributeElement = test7_FeatureAttributeElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test7_FeatureAttributeElement(self):
        return self.__test7_FeatureAttributeElement

    @test7_FeatureAttributeElement.setter
    def test7_FeatureAttributeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttributeElement__test7_FeatureAttributeElement", None)
        self.__test7_FeatureAttributeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FeatureAttribute16"):
                opp_val = getattr(old_value, "test7_FeatureAttribute16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FeatureAttribute16"):
                opp_val = getattr(value, "test7_FeatureAttribute16", None)
                if opp_val is None:
                    setattr(value, "test7_FeatureAttribute16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_AttributeType:

    def __init__(self, name: str, test7_AttributeType: "test7_Model" = None, test7_AttributeType14: "test7_FeatureAttribute" = None, test7_AttributeType8: set["test7_AttributeTypeElement"] = None, test7_AttributeType11: "test7_AttributeType" = None, test7_AttributeType9: "test7_AttributeType" = None, test7_AttributeType23: "test7_OptimizationSC" = None, test7_AttributeType25: "test7_HardLimitSC" = None):
        self.name = name
        self.test7_AttributeType = test7_AttributeType
        self.test7_AttributeType14 = test7_AttributeType14
        self.test7_AttributeType8 = test7_AttributeType8 if test7_AttributeType8 is not None else set()
        self.test7_AttributeType11 = test7_AttributeType11
        self.test7_AttributeType9 = test7_AttributeType9
        self.test7_AttributeType23 = test7_AttributeType23
        self.test7_AttributeType25 = test7_AttributeType25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test7_AttributeType14(self):
        return self.__test7_AttributeType14

    @test7_AttributeType14.setter
    def test7_AttributeType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType14", None)
        self.__test7_AttributeType14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FeatureAttribute13"):
                opp_val = getattr(old_value, "test7_FeatureAttribute13", None)
                if opp_val == self:
                    setattr(old_value, "test7_FeatureAttribute13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FeatureAttribute13"):
                opp_val = getattr(value, "test7_FeatureAttribute13", None)
                setattr(value, "test7_FeatureAttribute13", self)

    @property
    def test7_AttributeType9(self):
        return self.__test7_AttributeType9

    @test7_AttributeType9.setter
    def test7_AttributeType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType9", None)
        self.__test7_AttributeType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType11"):
                opp_val = getattr(old_value, "test7_AttributeType11", None)
                if opp_val == self:
                    setattr(old_value, "test7_AttributeType11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType11"):
                opp_val = getattr(value, "test7_AttributeType11", None)
                setattr(value, "test7_AttributeType11", self)

    @property
    def test7_AttributeType23(self):
        return self.__test7_AttributeType23

    @test7_AttributeType23.setter
    def test7_AttributeType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType23", None)
        self.__test7_AttributeType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_OptimizationSC"):
                opp_val = getattr(old_value, "test7_OptimizationSC", None)
                if opp_val == self:
                    setattr(old_value, "test7_OptimizationSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_OptimizationSC"):
                opp_val = getattr(value, "test7_OptimizationSC", None)
                setattr(value, "test7_OptimizationSC", self)

    @property
    def test7_AttributeType25(self):
        return self.__test7_AttributeType25

    @test7_AttributeType25.setter
    def test7_AttributeType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType25", None)
        self.__test7_AttributeType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_HardLimitSC"):
                opp_val = getattr(old_value, "test7_HardLimitSC", None)
                if opp_val == self:
                    setattr(old_value, "test7_HardLimitSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_HardLimitSC"):
                opp_val = getattr(value, "test7_HardLimitSC", None)
                setattr(value, "test7_HardLimitSC", self)

    @property
    def test7_AttributeType11(self):
        return self.__test7_AttributeType11

    @test7_AttributeType11.setter
    def test7_AttributeType11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType11", None)
        self.__test7_AttributeType11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType9"):
                opp_val = getattr(old_value, "test7_AttributeType9", None)
                if opp_val == self:
                    setattr(old_value, "test7_AttributeType9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType9"):
                opp_val = getattr(value, "test7_AttributeType9", None)
                setattr(value, "test7_AttributeType9", self)

    @property
    def test7_AttributeType8(self):
        return self.__test7_AttributeType8

    @test7_AttributeType8.setter
    def test7_AttributeType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType8", None)
        self.__test7_AttributeType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test7_AttributeTypeElement"):
                    opp_val = getattr(item, "test7_AttributeTypeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "test7_AttributeTypeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test7_AttributeTypeElement"):
                    opp_val = getattr(item, "test7_AttributeTypeElement", None)
                    
                    setattr(item, "test7_AttributeTypeElement", self)
                    

    @property
    def test7_AttributeType(self):
        return self.__test7_AttributeType

    @test7_AttributeType.setter
    def test7_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_AttributeType__test7_AttributeType", None)
        self.__test7_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_Model"):
                opp_val = getattr(old_value, "test7_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_Model"):
                opp_val = getattr(value, "test7_Model", None)
                if opp_val is None:
                    setattr(value, "test7_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_Model:

    pass
class test7_SolutionConstraint:

    def __init__(self, type: str, name: str, test7_SolutionConstraint: "test7_Model" = None):
        self.type = type
        self.name = name
        self.test7_SolutionConstraint = test7_SolutionConstraint
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test7_SolutionConstraint(self):
        return self.__test7_SolutionConstraint

    @test7_SolutionConstraint.setter
    def test7_SolutionConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_SolutionConstraint__test7_SolutionConstraint", None)
        self.__test7_SolutionConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_Model6"):
                opp_val = getattr(old_value, "test7_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_Model6"):
                opp_val = getattr(value, "test7_Model6", None)
                if opp_val is None:
                    setattr(value, "test7_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_Feature:

    def __init__(self, name: str, test7_Feature: "test7_Model" = None, test7_Feature20: set["test7_FeatureAttributeReference"] = None, test7_Feature27: "test7_SelectionStateSC" = None, test7_Feature29: "test7_FiniteDomainSC" = None):
        self.name = name
        self.test7_Feature = test7_Feature
        self.test7_Feature20 = test7_Feature20 if test7_Feature20 is not None else set()
        self.test7_Feature27 = test7_Feature27
        self.test7_Feature29 = test7_Feature29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test7_Feature20(self):
        return self.__test7_Feature20

    @test7_Feature20.setter
    def test7_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_Feature__test7_Feature20", None)
        self.__test7_Feature20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test7_FeatureAttributeReference21"):
                    opp_val = getattr(item, "test7_FeatureAttributeReference21", None)
                    
                    if opp_val == self:
                        setattr(item, "test7_FeatureAttributeReference21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test7_FeatureAttributeReference21"):
                    opp_val = getattr(item, "test7_FeatureAttributeReference21", None)
                    
                    setattr(item, "test7_FeatureAttributeReference21", self)
                    

    @property
    def test7_Feature27(self):
        return self.__test7_Feature27

    @test7_Feature27.setter
    def test7_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_Feature__test7_Feature27", None)
        self.__test7_Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_SelectionStateSC"):
                opp_val = getattr(old_value, "test7_SelectionStateSC", None)
                if opp_val == self:
                    setattr(old_value, "test7_SelectionStateSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_SelectionStateSC"):
                opp_val = getattr(value, "test7_SelectionStateSC", None)
                setattr(value, "test7_SelectionStateSC", self)

    @property
    def test7_Feature29(self):
        return self.__test7_Feature29

    @test7_Feature29.setter
    def test7_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_Feature__test7_Feature29", None)
        self.__test7_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FiniteDomainSC"):
                opp_val = getattr(old_value, "test7_FiniteDomainSC", None)
                if opp_val == self:
                    setattr(old_value, "test7_FiniteDomainSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FiniteDomainSC"):
                opp_val = getattr(value, "test7_FiniteDomainSC", None)
                setattr(value, "test7_FiniteDomainSC", self)

    @property
    def test7_Feature(self):
        return self.__test7_Feature

    @test7_Feature.setter
    def test7_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_Feature__test7_Feature", None)
        self.__test7_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_Model4"):
                opp_val = getattr(old_value, "test7_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_Model4"):
                opp_val = getattr(value, "test7_Model4", None)
                if opp_val is None:
                    setattr(value, "test7_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test7_FeatureAttribute:

    def __init__(self, name: str, test7_FeatureAttribute: "test7_Model" = None, test7_FeatureAttribute13: "test7_AttributeType" = None, test7_FeatureAttribute16: set["test7_FeatureAttributeElement"] = None, test7_FeatureAttribute18: "test7_FeatureAttributeReference" = None, test7_FeatureAttribute32: "test7_FiniteDomainSC" = None):
        self.name = name
        self.test7_FeatureAttribute = test7_FeatureAttribute
        self.test7_FeatureAttribute13 = test7_FeatureAttribute13
        self.test7_FeatureAttribute16 = test7_FeatureAttribute16 if test7_FeatureAttribute16 is not None else set()
        self.test7_FeatureAttribute18 = test7_FeatureAttribute18
        self.test7_FeatureAttribute32 = test7_FeatureAttribute32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test7_FeatureAttribute18(self):
        return self.__test7_FeatureAttribute18

    @test7_FeatureAttribute18.setter
    def test7_FeatureAttribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttribute__test7_FeatureAttribute18", None)
        self.__test7_FeatureAttribute18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FeatureAttributeReference"):
                opp_val = getattr(old_value, "test7_FeatureAttributeReference", None)
                if opp_val == self:
                    setattr(old_value, "test7_FeatureAttributeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FeatureAttributeReference"):
                opp_val = getattr(value, "test7_FeatureAttributeReference", None)
                setattr(value, "test7_FeatureAttributeReference", self)

    @property
    def test7_FeatureAttribute16(self):
        return self.__test7_FeatureAttribute16

    @test7_FeatureAttribute16.setter
    def test7_FeatureAttribute16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttribute__test7_FeatureAttribute16", None)
        self.__test7_FeatureAttribute16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test7_FeatureAttributeElement"):
                    opp_val = getattr(item, "test7_FeatureAttributeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "test7_FeatureAttributeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test7_FeatureAttributeElement"):
                    opp_val = getattr(item, "test7_FeatureAttributeElement", None)
                    
                    setattr(item, "test7_FeatureAttributeElement", self)
                    

    @property
    def test7_FeatureAttribute13(self):
        return self.__test7_FeatureAttribute13

    @test7_FeatureAttribute13.setter
    def test7_FeatureAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttribute__test7_FeatureAttribute13", None)
        self.__test7_FeatureAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_AttributeType14"):
                opp_val = getattr(old_value, "test7_AttributeType14", None)
                if opp_val == self:
                    setattr(old_value, "test7_AttributeType14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_AttributeType14"):
                opp_val = getattr(value, "test7_AttributeType14", None)
                setattr(value, "test7_AttributeType14", self)

    @property
    def test7_FeatureAttribute(self):
        return self.__test7_FeatureAttribute

    @test7_FeatureAttribute.setter
    def test7_FeatureAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttribute__test7_FeatureAttribute", None)
        self.__test7_FeatureAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_Model2"):
                opp_val = getattr(old_value, "test7_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_Model2"):
                opp_val = getattr(value, "test7_Model2", None)
                if opp_val is None:
                    setattr(value, "test7_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test7_FeatureAttribute32(self):
        return self.__test7_FeatureAttribute32

    @test7_FeatureAttribute32.setter
    def test7_FeatureAttribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test7_FeatureAttribute__test7_FeatureAttribute32", None)
        self.__test7_FeatureAttribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test7_FiniteDomainSC31"):
                opp_val = getattr(old_value, "test7_FiniteDomainSC31", None)
                if opp_val == self:
                    setattr(old_value, "test7_FiniteDomainSC31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test7_FiniteDomainSC31"):
                opp_val = getattr(value, "test7_FiniteDomainSC31", None)
                setattr(value, "test7_FiniteDomainSC31", self)

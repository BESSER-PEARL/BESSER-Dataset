from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class feaMo_FeamoFSelector:

    pass
class feaMo_Feature:

    def __init__(self, name: str, feaMo_Feature: "feaMo_SimpleFeature" = None, feaMo_Feature23: "feaMo_SimpleFeature" = None, feaMo_Feature26: "feaMo_FeatureDef" = None, feaMo_Feature32: "feaMo_FeatureConstraint" = None, feaMo_Feature35: "feaMo_FeatureConstraint" = None, feaMo_Feature37: "feaMo_FeamoFSelector" = None, feaMo_Feature43: "feaMo_FeamoFeatureConfig" = None):
        self.name = name
        self.feaMo_Feature = feaMo_Feature
        self.feaMo_Feature23 = feaMo_Feature23
        self.feaMo_Feature26 = feaMo_Feature26
        self.feaMo_Feature32 = feaMo_Feature32
        self.feaMo_Feature35 = feaMo_Feature35
        self.feaMo_Feature37 = feaMo_Feature37
        self.feaMo_Feature43 = feaMo_Feature43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def feaMo_Feature35(self):
        return self.__feaMo_Feature35

    @feaMo_Feature35.setter
    def feaMo_Feature35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature35", None)
        self.__feaMo_Feature35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureConstraint34"):
                opp_val = getattr(old_value, "feaMo_FeatureConstraint34", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeatureConstraint34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureConstraint34"):
                opp_val = getattr(value, "feaMo_FeatureConstraint34", None)
                setattr(value, "feaMo_FeatureConstraint34", self)

    @property
    def feaMo_Feature(self):
        return self.__feaMo_Feature

    @feaMo_Feature.setter
    def feaMo_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature", None)
        self.__feaMo_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_SimpleFeature20"):
                opp_val = getattr(old_value, "feaMo_SimpleFeature20", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_SimpleFeature20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_SimpleFeature20"):
                opp_val = getattr(value, "feaMo_SimpleFeature20", None)
                setattr(value, "feaMo_SimpleFeature20", self)

    @property
    def feaMo_Feature43(self):
        return self.__feaMo_Feature43

    @feaMo_Feature43.setter
    def feaMo_Feature43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature43", None)
        self.__feaMo_Feature43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeamoFeatureConfig42"):
                opp_val = getattr(old_value, "feaMo_FeamoFeatureConfig42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeamoFeatureConfig42"):
                opp_val = getattr(value, "feaMo_FeamoFeatureConfig42", None)
                if opp_val is None:
                    setattr(value, "feaMo_FeamoFeatureConfig42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feaMo_Feature23(self):
        return self.__feaMo_Feature23

    @feaMo_Feature23.setter
    def feaMo_Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature23", None)
        self.__feaMo_Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_SimpleFeature22"):
                opp_val = getattr(old_value, "feaMo_SimpleFeature22", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_SimpleFeature22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_SimpleFeature22"):
                opp_val = getattr(value, "feaMo_SimpleFeature22", None)
                setattr(value, "feaMo_SimpleFeature22", self)

    @property
    def feaMo_Feature37(self):
        return self.__feaMo_Feature37

    @feaMo_Feature37.setter
    def feaMo_Feature37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature37", None)
        self.__feaMo_Feature37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeamoFSelector"):
                opp_val = getattr(old_value, "feaMo_FeamoFSelector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeamoFSelector"):
                opp_val = getattr(value, "feaMo_FeamoFSelector", None)
                if opp_val is None:
                    setattr(value, "feaMo_FeamoFSelector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feaMo_Feature26(self):
        return self.__feaMo_Feature26

    @feaMo_Feature26.setter
    def feaMo_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature26", None)
        self.__feaMo_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureDef25"):
                opp_val = getattr(old_value, "feaMo_FeatureDef25", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeatureDef25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureDef25"):
                opp_val = getattr(value, "feaMo_FeatureDef25", None)
                setattr(value, "feaMo_FeatureDef25", self)

    @property
    def feaMo_Feature32(self):
        return self.__feaMo_Feature32

    @feaMo_Feature32.setter
    def feaMo_Feature32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_Feature__feaMo_Feature32", None)
        self.__feaMo_Feature32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureConstraint31"):
                opp_val = getattr(old_value, "feaMo_FeatureConstraint31", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeatureConstraint31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureConstraint31"):
                opp_val = getattr(value, "feaMo_FeatureConstraint31", None)
                setattr(value, "feaMo_FeatureConstraint31", self)

class feaMo_SimpleFeature:

    pass
class feaMo_FeatureGroup:

    pass
class feaMo_FeatureConstraint:

    def __init__(self, rel: str, feaMo_FeatureConstraint: "feaMo_FeatureModel" = None, feaMo_FeatureConstraint31: "feaMo_Feature" = None, feaMo_FeatureConstraint34: "feaMo_Feature" = None):
        self.rel = rel
        self.feaMo_FeatureConstraint = feaMo_FeatureConstraint
        self.feaMo_FeatureConstraint31 = feaMo_FeatureConstraint31
        self.feaMo_FeatureConstraint34 = feaMo_FeatureConstraint34
        
    @property
    def rel(self) -> str:
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel

    @property
    def feaMo_FeatureConstraint34(self):
        return self.__feaMo_FeatureConstraint34

    @feaMo_FeatureConstraint34.setter
    def feaMo_FeatureConstraint34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureConstraint__feaMo_FeatureConstraint34", None)
        self.__feaMo_FeatureConstraint34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_Feature35"):
                opp_val = getattr(old_value, "feaMo_Feature35", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_Feature35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_Feature35"):
                opp_val = getattr(value, "feaMo_Feature35", None)
                setattr(value, "feaMo_Feature35", self)

    @property
    def feaMo_FeatureConstraint31(self):
        return self.__feaMo_FeatureConstraint31

    @feaMo_FeatureConstraint31.setter
    def feaMo_FeatureConstraint31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureConstraint__feaMo_FeatureConstraint31", None)
        self.__feaMo_FeatureConstraint31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_Feature32"):
                opp_val = getattr(old_value, "feaMo_Feature32", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_Feature32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_Feature32"):
                opp_val = getattr(value, "feaMo_Feature32", None)
                setattr(value, "feaMo_Feature32", self)

    @property
    def feaMo_FeatureConstraint(self):
        return self.__feaMo_FeatureConstraint

    @feaMo_FeatureConstraint.setter
    def feaMo_FeatureConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureConstraint__feaMo_FeatureConstraint", None)
        self.__feaMo_FeatureConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureModel8"):
                opp_val = getattr(old_value, "feaMo_FeatureModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureModel8"):
                opp_val = getattr(value, "feaMo_FeatureModel8", None)
                if opp_val is None:
                    setattr(value, "feaMo_FeatureModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feaMo_FeatureDef:

    pass
class feaMo_FeatureDetails:

    pass
class feaMo_FeamoFeatureConfig:

    def __init__(self, name: str, feaMo_FeamoFeatureConfig: "feaMo_Model" = None, feaMo_FeamoFeatureConfig42: set["feaMo_Feature"] = None, feaMo_FeamoFeatureConfig39: "feaMo_FeatureModel" = None):
        self.name = name
        self.feaMo_FeamoFeatureConfig = feaMo_FeamoFeatureConfig
        self.feaMo_FeamoFeatureConfig42 = feaMo_FeamoFeatureConfig42 if feaMo_FeamoFeatureConfig42 is not None else set()
        self.feaMo_FeamoFeatureConfig39 = feaMo_FeamoFeatureConfig39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def feaMo_FeamoFeatureConfig(self):
        return self.__feaMo_FeamoFeatureConfig

    @feaMo_FeamoFeatureConfig.setter
    def feaMo_FeamoFeatureConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeamoFeatureConfig__feaMo_FeamoFeatureConfig", None)
        self.__feaMo_FeamoFeatureConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_Model2"):
                opp_val = getattr(old_value, "feaMo_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_Model2"):
                opp_val = getattr(value, "feaMo_Model2", None)
                if opp_val is None:
                    setattr(value, "feaMo_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feaMo_FeamoFeatureConfig39(self):
        return self.__feaMo_FeamoFeatureConfig39

    @feaMo_FeamoFeatureConfig39.setter
    def feaMo_FeamoFeatureConfig39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeamoFeatureConfig__feaMo_FeamoFeatureConfig39", None)
        self.__feaMo_FeamoFeatureConfig39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureModel40"):
                opp_val = getattr(old_value, "feaMo_FeatureModel40", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeatureModel40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureModel40"):
                opp_val = getattr(value, "feaMo_FeatureModel40", None)
                setattr(value, "feaMo_FeatureModel40", self)

    @property
    def feaMo_FeamoFeatureConfig42(self):
        return self.__feaMo_FeamoFeatureConfig42

    @feaMo_FeamoFeatureConfig42.setter
    def feaMo_FeamoFeatureConfig42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeamoFeatureConfig__feaMo_FeamoFeatureConfig42", None)
        self.__feaMo_FeamoFeatureConfig42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feaMo_Feature43"):
                    opp_val = getattr(item, "feaMo_Feature43", None)
                    
                    if opp_val == self:
                        setattr(item, "feaMo_Feature43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feaMo_Feature43"):
                    opp_val = getattr(item, "feaMo_Feature43", None)
                    
                    setattr(item, "feaMo_Feature43", self)
                    

class feaMo_FeatureModel:

    def __init__(self, name: str, feaMo_FeatureModel: "feaMo_Model" = None, feaMo_FeatureModel4: "feaMo_FeatureDetails" = None, feaMo_FeatureModel6: set["feaMo_FeatureDef"] = None, feaMo_FeatureModel8: set["feaMo_FeatureConstraint"] = None, feaMo_FeatureModel40: "feaMo_FeamoFeatureConfig" = None):
        self.name = name
        self.feaMo_FeatureModel = feaMo_FeatureModel
        self.feaMo_FeatureModel4 = feaMo_FeatureModel4
        self.feaMo_FeatureModel6 = feaMo_FeatureModel6 if feaMo_FeatureModel6 is not None else set()
        self.feaMo_FeatureModel8 = feaMo_FeatureModel8 if feaMo_FeatureModel8 is not None else set()
        self.feaMo_FeatureModel40 = feaMo_FeatureModel40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def feaMo_FeatureModel8(self):
        return self.__feaMo_FeatureModel8

    @feaMo_FeatureModel8.setter
    def feaMo_FeatureModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureModel__feaMo_FeatureModel8", None)
        self.__feaMo_FeatureModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feaMo_FeatureConstraint"):
                    opp_val = getattr(item, "feaMo_FeatureConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "feaMo_FeatureConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feaMo_FeatureConstraint"):
                    opp_val = getattr(item, "feaMo_FeatureConstraint", None)
                    
                    setattr(item, "feaMo_FeatureConstraint", self)
                    

    @property
    def feaMo_FeatureModel4(self):
        return self.__feaMo_FeatureModel4

    @feaMo_FeatureModel4.setter
    def feaMo_FeatureModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureModel__feaMo_FeatureModel4", None)
        self.__feaMo_FeatureModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeatureDetails"):
                opp_val = getattr(old_value, "feaMo_FeatureDetails", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeatureDetails", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeatureDetails"):
                opp_val = getattr(value, "feaMo_FeatureDetails", None)
                setattr(value, "feaMo_FeatureDetails", self)

    @property
    def feaMo_FeatureModel40(self):
        return self.__feaMo_FeatureModel40

    @feaMo_FeatureModel40.setter
    def feaMo_FeatureModel40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureModel__feaMo_FeatureModel40", None)
        self.__feaMo_FeatureModel40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_FeamoFeatureConfig39"):
                opp_val = getattr(old_value, "feaMo_FeamoFeatureConfig39", None)
                if opp_val == self:
                    setattr(old_value, "feaMo_FeamoFeatureConfig39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_FeamoFeatureConfig39"):
                opp_val = getattr(value, "feaMo_FeamoFeatureConfig39", None)
                setattr(value, "feaMo_FeamoFeatureConfig39", self)

    @property
    def feaMo_FeatureModel(self):
        return self.__feaMo_FeatureModel

    @feaMo_FeatureModel.setter
    def feaMo_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureModel__feaMo_FeatureModel", None)
        self.__feaMo_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feaMo_Model"):
                opp_val = getattr(old_value, "feaMo_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feaMo_Model"):
                opp_val = getattr(value, "feaMo_Model", None)
                if opp_val is None:
                    setattr(value, "feaMo_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feaMo_FeatureModel6(self):
        return self.__feaMo_FeatureModel6

    @feaMo_FeatureModel6.setter
    def feaMo_FeatureModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feaMo_FeatureModel__feaMo_FeatureModel6", None)
        self.__feaMo_FeatureModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feaMo_FeatureDef"):
                    opp_val = getattr(item, "feaMo_FeatureDef", None)
                    
                    if opp_val == self:
                        setattr(item, "feaMo_FeatureDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feaMo_FeatureDef"):
                    opp_val = getattr(item, "feaMo_FeatureDef", None)
                    
                    setattr(item, "feaMo_FeatureDef", self)
                    

class feaMo_Model:

    pass
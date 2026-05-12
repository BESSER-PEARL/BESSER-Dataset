from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sqlview_Right:

    def __init__(self, value: str, sqlview_Right55: set["sqlview_MetamodelName"] = None, sqlview_Right: "sqlview_Comparison" = None, sqlview_Right58: set["sqlview_Class"] = None, sqlview_Right61: "sqlview_Attribute" = None):
        self.value = value
        self.sqlview_Right55 = sqlview_Right55 if sqlview_Right55 is not None else set()
        self.sqlview_Right = sqlview_Right
        self.sqlview_Right58 = sqlview_Right58 if sqlview_Right58 is not None else set()
        self.sqlview_Right61 = sqlview_Right61
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def sqlview_Right55(self):
        return self.__sqlview_Right55

    @sqlview_Right55.setter
    def sqlview_Right55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Right__sqlview_Right55", None)
        self.__sqlview_Right55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_MetamodelName56"):
                    opp_val = getattr(item, "sqlview_MetamodelName56", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_MetamodelName56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_MetamodelName56"):
                    opp_val = getattr(item, "sqlview_MetamodelName56", None)
                    
                    setattr(item, "sqlview_MetamodelName56", self)
                    

    @property
    def sqlview_Right61(self):
        return self.__sqlview_Right61

    @sqlview_Right61.setter
    def sqlview_Right61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Right__sqlview_Right61", None)
        self.__sqlview_Right61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Attribute62"):
                opp_val = getattr(old_value, "sqlview_Attribute62", None)
                if opp_val == self:
                    setattr(old_value, "sqlview_Attribute62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Attribute62"):
                opp_val = getattr(value, "sqlview_Attribute62", None)
                setattr(value, "sqlview_Attribute62", self)

    @property
    def sqlview_Right58(self):
        return self.__sqlview_Right58

    @sqlview_Right58.setter
    def sqlview_Right58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Right__sqlview_Right58", None)
        self.__sqlview_Right58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_Class59"):
                    opp_val = getattr(item, "sqlview_Class59", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_Class59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_Class59"):
                    opp_val = getattr(item, "sqlview_Class59", None)
                    
                    setattr(item, "sqlview_Class59", self)
                    

    @property
    def sqlview_Right(self):
        return self.__sqlview_Right

    @sqlview_Right.setter
    def sqlview_Right(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Right__sqlview_Right", None)
        self.__sqlview_Right = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Comparison44"):
                opp_val = getattr(old_value, "sqlview_Comparison44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Comparison44"):
                opp_val = getattr(value, "sqlview_Comparison44", None)
                if opp_val is None:
                    setattr(value, "sqlview_Comparison44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlview_Left:

    pass
class sqlview_Comparison:

    pass
class sqlview_EclExpression:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sqlview_EObject:

    pass
class sqlview_Join:

    pass
class sqlview_Attribute:

    def __init__(self, name: str, sqlview_Attribute: "sqlview_SelectAttribute" = None, sqlview_Attribute53: "sqlview_Left" = None, sqlview_Attribute62: "sqlview_Right" = None):
        self.name = name
        self.sqlview_Attribute = sqlview_Attribute
        self.sqlview_Attribute53 = sqlview_Attribute53
        self.sqlview_Attribute62 = sqlview_Attribute62
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlview_Attribute(self):
        return self.__sqlview_Attribute

    @sqlview_Attribute.setter
    def sqlview_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Attribute__sqlview_Attribute", None)
        self.__sqlview_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_SelectAttribute19"):
                opp_val = getattr(old_value, "sqlview_SelectAttribute19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_SelectAttribute19"):
                opp_val = getattr(value, "sqlview_SelectAttribute19", None)
                if opp_val is None:
                    setattr(value, "sqlview_SelectAttribute19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Attribute62(self):
        return self.__sqlview_Attribute62

    @sqlview_Attribute62.setter
    def sqlview_Attribute62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Attribute__sqlview_Attribute62", None)
        self.__sqlview_Attribute62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Right61"):
                opp_val = getattr(old_value, "sqlview_Right61", None)
                if opp_val == self:
                    setattr(old_value, "sqlview_Right61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Right61"):
                opp_val = getattr(value, "sqlview_Right61", None)
                setattr(value, "sqlview_Right61", self)

    @property
    def sqlview_Attribute53(self):
        return self.__sqlview_Attribute53

    @sqlview_Attribute53.setter
    def sqlview_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Attribute__sqlview_Attribute53", None)
        self.__sqlview_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Left52"):
                opp_val = getattr(old_value, "sqlview_Left52", None)
                if opp_val == self:
                    setattr(old_value, "sqlview_Left52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Left52"):
                opp_val = getattr(value, "sqlview_Left52", None)
                setattr(value, "sqlview_Left52", self)

class sqlview_Class:

    def __init__(self, name: str, sqlview_Class: "sqlview_SelectAttribute" = None, sqlview_Class33: "sqlview_JoinLeft" = None, sqlview_Class39: "sqlview_JoinRight" = None, sqlview_Class50: "sqlview_Left" = None, sqlview_Class59: "sqlview_Right" = None):
        self.name = name
        self.sqlview_Class = sqlview_Class
        self.sqlview_Class33 = sqlview_Class33
        self.sqlview_Class39 = sqlview_Class39
        self.sqlview_Class50 = sqlview_Class50
        self.sqlview_Class59 = sqlview_Class59
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlview_Class33(self):
        return self.__sqlview_Class33

    @sqlview_Class33.setter
    def sqlview_Class33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Class__sqlview_Class33", None)
        self.__sqlview_Class33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_JoinLeft32"):
                opp_val = getattr(old_value, "sqlview_JoinLeft32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_JoinLeft32"):
                opp_val = getattr(value, "sqlview_JoinLeft32", None)
                if opp_val is None:
                    setattr(value, "sqlview_JoinLeft32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Class59(self):
        return self.__sqlview_Class59

    @sqlview_Class59.setter
    def sqlview_Class59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Class__sqlview_Class59", None)
        self.__sqlview_Class59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Right58"):
                opp_val = getattr(old_value, "sqlview_Right58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Right58"):
                opp_val = getattr(value, "sqlview_Right58", None)
                if opp_val is None:
                    setattr(value, "sqlview_Right58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Class39(self):
        return self.__sqlview_Class39

    @sqlview_Class39.setter
    def sqlview_Class39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Class__sqlview_Class39", None)
        self.__sqlview_Class39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_JoinRight38"):
                opp_val = getattr(old_value, "sqlview_JoinRight38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_JoinRight38"):
                opp_val = getattr(value, "sqlview_JoinRight38", None)
                if opp_val is None:
                    setattr(value, "sqlview_JoinRight38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Class(self):
        return self.__sqlview_Class

    @sqlview_Class.setter
    def sqlview_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Class__sqlview_Class", None)
        self.__sqlview_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_SelectAttribute17"):
                opp_val = getattr(old_value, "sqlview_SelectAttribute17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_SelectAttribute17"):
                opp_val = getattr(value, "sqlview_SelectAttribute17", None)
                if opp_val is None:
                    setattr(value, "sqlview_SelectAttribute17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Class50(self):
        return self.__sqlview_Class50

    @sqlview_Class50.setter
    def sqlview_Class50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Class__sqlview_Class50", None)
        self.__sqlview_Class50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Left49"):
                opp_val = getattr(old_value, "sqlview_Left49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Left49"):
                opp_val = getattr(value, "sqlview_Left49", None)
                if opp_val is None:
                    setattr(value, "sqlview_Left49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlview_Relation:

    def __init__(self, name: str, sqlview_Relation: "sqlview_Join" = None):
        self.name = name
        self.sqlview_Relation = sqlview_Relation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlview_Relation(self):
        return self.__sqlview_Relation

    @sqlview_Relation.setter
    def sqlview_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Relation__sqlview_Relation", None)
        self.__sqlview_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Join27"):
                opp_val = getattr(old_value, "sqlview_Join27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Join27"):
                opp_val = getattr(value, "sqlview_Join27", None)
                if opp_val is None:
                    setattr(value, "sqlview_Join27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlview_JoinRight:

    pass
class sqlview_JoinLeft:

    pass
class sqlview_Condition:

    pass
class sqlview_From:

    pass
class sqlview_Select:

    def __init__(self, select: str, sqlview_Select12: set["sqlview_SelectAttribute"] = None, sqlview_Select: "sqlview_Expression" = None):
        self.select = select
        self.sqlview_Select12 = sqlview_Select12 if sqlview_Select12 is not None else set()
        self.sqlview_Select = sqlview_Select
        
        pass
    @property
    def select(self):
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select


    @property
    def sqlview_Select12(self):
        return self.__sqlview_Select12

    @sqlview_Select12.setter
    def sqlview_Select12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Select__sqlview_Select12", None)
        self.__sqlview_Select12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_SelectAttribute"):
                    opp_val = getattr(item, "sqlview_SelectAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_SelectAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_SelectAttribute"):
                    opp_val = getattr(item, "sqlview_SelectAttribute", None)
                    
                    setattr(item, "sqlview_SelectAttribute", self)
                    

    @property
    def sqlview_Select(self):
        return self.__sqlview_Select

    @sqlview_Select.setter
    def sqlview_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Select__sqlview_Select", None)
        self.__sqlview_Select = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Expression6"):
                opp_val = getattr(old_value, "sqlview_Expression6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Expression6"):
                opp_val = getattr(value, "sqlview_Expression6", None)
                if opp_val is None:
                    setattr(value, "sqlview_Expression6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlview_MetamodelName:

    def __init__(self, name: str, sqlview_MetamodelName: "sqlview_Metamodel" = None, sqlview_MetamodelName15: "sqlview_SelectAttribute" = None, sqlview_MetamodelName30: "sqlview_JoinLeft" = None, sqlview_MetamodelName36: "sqlview_JoinRight" = None, sqlview_MetamodelName56: "sqlview_Right" = None, sqlview_MetamodelName47: "sqlview_Left" = None):
        self.name = name
        self.sqlview_MetamodelName = sqlview_MetamodelName
        self.sqlview_MetamodelName15 = sqlview_MetamodelName15
        self.sqlview_MetamodelName30 = sqlview_MetamodelName30
        self.sqlview_MetamodelName36 = sqlview_MetamodelName36
        self.sqlview_MetamodelName56 = sqlview_MetamodelName56
        self.sqlview_MetamodelName47 = sqlview_MetamodelName47
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlview_MetamodelName15(self):
        return self.__sqlview_MetamodelName15

    @sqlview_MetamodelName15.setter
    def sqlview_MetamodelName15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName15", None)
        self.__sqlview_MetamodelName15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_SelectAttribute14"):
                opp_val = getattr(old_value, "sqlview_SelectAttribute14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_SelectAttribute14"):
                opp_val = getattr(value, "sqlview_SelectAttribute14", None)
                if opp_val is None:
                    setattr(value, "sqlview_SelectAttribute14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_MetamodelName36(self):
        return self.__sqlview_MetamodelName36

    @sqlview_MetamodelName36.setter
    def sqlview_MetamodelName36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName36", None)
        self.__sqlview_MetamodelName36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_JoinRight35"):
                opp_val = getattr(old_value, "sqlview_JoinRight35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_JoinRight35"):
                opp_val = getattr(value, "sqlview_JoinRight35", None)
                if opp_val is None:
                    setattr(value, "sqlview_JoinRight35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_MetamodelName30(self):
        return self.__sqlview_MetamodelName30

    @sqlview_MetamodelName30.setter
    def sqlview_MetamodelName30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName30", None)
        self.__sqlview_MetamodelName30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_JoinLeft29"):
                opp_val = getattr(old_value, "sqlview_JoinLeft29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_JoinLeft29"):
                opp_val = getattr(value, "sqlview_JoinLeft29", None)
                if opp_val is None:
                    setattr(value, "sqlview_JoinLeft29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_MetamodelName47(self):
        return self.__sqlview_MetamodelName47

    @sqlview_MetamodelName47.setter
    def sqlview_MetamodelName47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName47", None)
        self.__sqlview_MetamodelName47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Left46"):
                opp_val = getattr(old_value, "sqlview_Left46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Left46"):
                opp_val = getattr(value, "sqlview_Left46", None)
                if opp_val is None:
                    setattr(value, "sqlview_Left46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_MetamodelName(self):
        return self.__sqlview_MetamodelName

    @sqlview_MetamodelName.setter
    def sqlview_MetamodelName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName", None)
        self.__sqlview_MetamodelName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Metamodel4"):
                opp_val = getattr(old_value, "sqlview_Metamodel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Metamodel4"):
                opp_val = getattr(value, "sqlview_Metamodel4", None)
                if opp_val is None:
                    setattr(value, "sqlview_Metamodel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_MetamodelName56(self):
        return self.__sqlview_MetamodelName56

    @sqlview_MetamodelName56.setter
    def sqlview_MetamodelName56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_MetamodelName__sqlview_MetamodelName56", None)
        self.__sqlview_MetamodelName56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Right55"):
                opp_val = getattr(old_value, "sqlview_Right55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Right55"):
                opp_val = getattr(value, "sqlview_Right55", None)
                if opp_val is None:
                    setattr(value, "sqlview_Right55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlview_SelectAttribute:

    pass
class sqlview_Expression:

    pass
class sqlview_Metamodel:

    def __init__(self, metamodelURL: str, sqlview_Metamodel4: set["sqlview_MetamodelName"] = None, sqlview_Metamodel: "sqlview_Model" = None):
        self.metamodelURL = metamodelURL
        self.sqlview_Metamodel4 = sqlview_Metamodel4 if sqlview_Metamodel4 is not None else set()
        self.sqlview_Metamodel = sqlview_Metamodel
        
        pass
    @property
    def metamodelURL(self):
        return self.__metamodelURL

    @metamodelURL.setter
    def metamodelURL(self, metamodelURL: str):
        self.__metamodelURL = metamodelURL


    @property
    def sqlview_Metamodel(self):
        return self.__sqlview_Metamodel

    @sqlview_Metamodel.setter
    def sqlview_Metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Metamodel__sqlview_Metamodel", None)
        self.__sqlview_Metamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlview_Model"):
                opp_val = getattr(old_value, "sqlview_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlview_Model"):
                opp_val = getattr(value, "sqlview_Model", None)
                if opp_val is None:
                    setattr(value, "sqlview_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlview_Metamodel4(self):
        return self.__sqlview_Metamodel4

    @sqlview_Metamodel4.setter
    def sqlview_Metamodel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Metamodel__sqlview_Metamodel4", None)
        self.__sqlview_Metamodel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_MetamodelName"):
                    opp_val = getattr(item, "sqlview_MetamodelName", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_MetamodelName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_MetamodelName"):
                    opp_val = getattr(item, "sqlview_MetamodelName", None)
                    
                    setattr(item, "sqlview_MetamodelName", self)
                    

class sqlview_Model:

    def __init__(self, viewName: str, sqlview_Model: set["sqlview_Metamodel"] = None, sqlview_Model2: set["sqlview_Expression"] = None):
        self.viewName = viewName
        self.sqlview_Model = sqlview_Model if sqlview_Model is not None else set()
        self.sqlview_Model2 = sqlview_Model2 if sqlview_Model2 is not None else set()
        
        pass
    @property
    def viewName(self):
        return self.__viewName

    @viewName.setter
    def viewName(self, viewName: str):
        self.__viewName = viewName


    @property
    def sqlview_Model(self):
        return self.__sqlview_Model

    @sqlview_Model.setter
    def sqlview_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Model__sqlview_Model", None)
        self.__sqlview_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_Metamodel"):
                    opp_val = getattr(item, "sqlview_Metamodel", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_Metamodel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_Metamodel"):
                    opp_val = getattr(item, "sqlview_Metamodel", None)
                    
                    setattr(item, "sqlview_Metamodel", self)
                    

    @property
    def sqlview_Model2(self):
        return self.__sqlview_Model2

    @sqlview_Model2.setter
    def sqlview_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlview_Model__sqlview_Model2", None)
        self.__sqlview_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlview_Expression"):
                    opp_val = getattr(item, "sqlview_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlview_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlview_Expression"):
                    opp_val = getattr(item, "sqlview_Expression", None)
                    
                    setattr(item, "sqlview_Expression", self)
                    

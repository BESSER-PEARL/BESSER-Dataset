from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class unql_Select:

    def __init__(self, relations: str, conditions: str, attributes: str, unql_Select: "unql_Program" = None):
        self.relations = relations
        self.conditions = conditions
        self.attributes = attributes
        self.unql_Select = unql_Select
        
        pass
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def conditions(self):
        return self.__conditions

    @conditions.setter
    def conditions(self, conditions: str):
        self.__conditions = conditions


    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, relations: str):
        self.__relations = relations


    @property
    def unql_Select(self):
        return self.__unql_Select

    @unql_Select.setter
    def unql_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_unql_Select__unql_Select", None)
        self.__unql_Select = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "unql_Program4"):
                opp_val = getattr(old_value, "unql_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "unql_Program4"):
                opp_val = getattr(value, "unql_Program4", None)
                if opp_val is None:
                    setattr(value, "unql_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class unql_Connection:

    def __init__(self, name: str, url: str, username: str, password: str, unql_Connection: "unql_Program" = None):
        self.name = name
        self.url = url
        self.username = username
        self.password = password
        self.unql_Connection = unql_Connection
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def unql_Connection(self):
        return self.__unql_Connection

    @unql_Connection.setter
    def unql_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_unql_Connection__unql_Connection", None)
        self.__unql_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "unql_Program2"):
                opp_val = getattr(old_value, "unql_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "unql_Program2"):
                opp_val = getattr(value, "unql_Program2", None)
                if opp_val is None:
                    setattr(value, "unql_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class unql_Definition:

    def __init__(self, name: str, type: str, unql_Definition: "unql_Program" = None):
        self.name = name
        self.type = type
        self.unql_Definition = unql_Definition
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def unql_Definition(self):
        return self.__unql_Definition

    @unql_Definition.setter
    def unql_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_unql_Definition__unql_Definition", None)
        self.__unql_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "unql_Program"):
                opp_val = getattr(old_value, "unql_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "unql_Program"):
                opp_val = getattr(value, "unql_Program", None)
                if opp_val is None:
                    setattr(value, "unql_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class unql_Program:

    pass
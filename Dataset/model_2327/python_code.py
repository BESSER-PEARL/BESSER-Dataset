from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pdb2_Person:

    def __init__(self, name: str, birthday: str, placeOfBirth: str, id: str, incrementalID: str, Person: "pdb2_Database" = None, persons: "pdb2_Database" = None):
        self.name = name
        self.birthday = birthday
        self.placeOfBirth = placeOfBirth
        self.id = id
        self.incrementalID = incrementalID
        self.Person = Person
        self.persons = persons
        
    @property
    def placeOfBirth(self) -> str:
        return self.__placeOfBirth

    @placeOfBirth.setter
    def placeOfBirth(self, placeOfBirth: str):
        self.__placeOfBirth = placeOfBirth

    @property
    def incrementalID(self) -> str:
        return self.__incrementalID

    @incrementalID.setter
    def incrementalID(self, incrementalID: str):
        self.__incrementalID = incrementalID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def birthday(self) -> str:
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: str):
        self.__birthday = birthday

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pdb2_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database"):
                opp_val = getattr(old_value, "database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database"):
                opp_val = getattr(value, "database", None)
                if opp_val is None:
                    setattr(value, "database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pdb2_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database"):
                opp_val = getattr(old_value, "Database", None)
                if opp_val == self:
                    setattr(old_value, "Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database"):
                opp_val = getattr(value, "Database", None)
                setattr(value, "Database", self)

class pdb2_Database:

    def __init__(self, name: str, database: set["pdb2_Person"] = None, Database: "pdb2_Person" = None):
        self.name = name
        self.database = database if database is not None else set()
        self.Database = Database
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pdb2_Database__database", None)
        self.__database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Database(self):
        return self.__Database

    @Database.setter
    def Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pdb2_Database__Database", None)
        self.__Database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons"):
                opp_val = getattr(old_value, "persons", None)
                if opp_val == self:
                    setattr(old_value, "persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons"):
                opp_val = getattr(value, "persons", None)
                setattr(value, "persons", self)

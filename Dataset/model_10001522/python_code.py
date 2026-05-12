from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class cash:

    pass


class credit_card:

    pass


class library:

    pass


class transaction:

    pass


class fine:

    pass


class library_member:

    pass


class librarian:

    pass


class book:

    pass


class File:

    def __init__(self, file_type: File, data_File_13: "Data" = None, upload5: "User" = None):
        self.file_type = file_type
        self.data_File_13 = data_File_13
        self.upload5 = upload5
        
        pass
    @property
    def file_type(self):
        return self.__file_type
    @file_type.setter
    def file_type(self, file_type: File):
        self.__file_type = file_type

    @property
    def data_File_13(self):
        return self.__data_File_13
    @data_File_13.setter
    def data_File_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_File__data_File_13", None)
        self.__data_File_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parse2"):
                opp_val = getattr(old_value, "parse2", None)
                if opp_val == self:
                    setattr(old_value, "parse2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parse2"):
                opp_val = getattr(value, "parse2", None)
                setattr(value, "parse2", self)

    @property
    def upload5(self):
        return self.__upload5
    @upload5.setter
    def upload5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_File__upload5", None)
        self.__upload5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parser4"):
                opp_val = getattr(old_value, "parser4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parser4"):
                opp_val = getattr(value, "parser4", None)
                if opp_val is None:
                    setattr(value, "parser4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class XML:

    def __init__(self, element: str, attribute: str):
        self.element = element
        self.attribute = attribute
        
        pass
    @property
    def element(self):
        return self.__element
    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class CSV:

    def __init__(self, cloumn: str, row: str):
        self.cloumn = cloumn
        self.row = row
        
        pass
    @property
    def row(self):
        return self.__row
    @row.setter
    def row(self, row: str):
        self.__row = row

    @property
    def cloumn(self):
        return self.__cloumn
    @cloumn.setter
    def cloumn(self, cloumn: str):
        self.__cloumn = cloumn



class Data:

    def __init__(self, key: str, value: str, modify1: "User" = None, parse2: "File" = None):
        self.key = key
        self.value = value
        self.modify1 = modify1
        self.parse2 = parse2
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self):
        return self.__key
    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def parse2(self):
        return self.__parse2
    @parse2.setter
    def parse2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data__parse2", None)
        self.__parse2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_File_13"):
                opp_val = getattr(old_value, "data_File_13", None)
                if opp_val == self:
                    setattr(old_value, "data_File_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_File_13"):
                opp_val = getattr(value, "data_File_13", None)
                setattr(value, "data_File_13", self)

    @property
    def modify1(self):
        return self.__modify1
    @modify1.setter
    def modify1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data__modify1", None)
        self.__modify1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_data_00"):
                opp_val = getattr(old_value, "User_data_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_data_00"):
                opp_val = getattr(value, "User_data_00", None)
                if opp_val is None:
                    setattr(value, "User_data_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, user_id: User, User_data_00: set["Data"] = None, parser4: set["File"] = None):
        self.user_id = user_id
        self.User_data_00 = User_data_00 if User_data_00 is not None else set()
        self.parser4 = parser4 if parser4 is not None else set()
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: User):
        self.__user_id = user_id

    @property
    def parser4(self):
        return self.__parser4
    @parser4.setter
    def parser4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__parser4", None)
        self.__parser4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "upload5"):
                    opp_val = getattr(item, "upload5", None)
                    
                    if opp_val == self:
                        setattr(item, "upload5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "upload5"):
                    opp_val = getattr(item, "upload5", None)
                    
                    setattr(item, "upload5", self)
                    

    @property
    def User_data_00(self):
        return self.__User_data_00
    @User_data_00.setter
    def User_data_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_data_00", None)
        self.__User_data_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modify1"):
                    opp_val = getattr(item, "modify1", None)
                    
                    if opp_val == self:
                        setattr(item, "modify1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modify1"):
                    opp_val = getattr(item, "modify1", None)
                    
                    setattr(item, "modify1", self)
                    



class member_profile:

    pass


class status_of_book:

    pass

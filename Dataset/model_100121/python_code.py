from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Schema:

    pass
class Database:

    pass
class Diagram:

    pass
class ui_diagram_DMDiagram(Diagram):

    pass
class schema_DataModelerNamedElement:

    pass
class schema_FunctionalElement:

    pass
class ui_project_Project(schema_DataModelerNamedElement, schema_FunctionalElement):

    def __init__(self, application: str, description: str, ui_project_Project: "Database" = None, ui_project_Project2: set["Schema"] = None):
        self.application = application
        self.description = description
        self.ui_project_Project = ui_project_Project
        self.ui_project_Project2 = ui_project_Project2 if ui_project_Project2 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application


    @property
    def ui_project_Project(self):
        return self.__ui_project_Project

    @ui_project_Project.setter
    def ui_project_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ui_project_Project__ui_project_Project", None)
        self.__ui_project_Project = value
        
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

    @property
    def ui_project_Project2(self):
        return self.__ui_project_Project2

    @ui_project_Project2.setter
    def ui_project_Project2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ui_project_Project__ui_project_Project2", None)
        self.__ui_project_Project2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Schema"):
                    opp_val = getattr(item, "Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Schema"):
                    opp_val = getattr(item, "Schema", None)
                    
                    setattr(item, "Schema", self)
                    

    def isValid(self, ui_diagnostics, ui_context) :
        # TODO: Implement isValid method
        pass

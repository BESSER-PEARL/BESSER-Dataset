from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mvc_ReturnParameter:

    pass
class View:

    pass
class mvc_SocialComponent(View):

    def __init__(self, social: str, socialname: str):
        self.social = social
        self.socialname = socialname
        
    @property
    def socialname(self) -> str:
        return self.__socialname

    @socialname.setter
    def socialname(self, socialname: str):
        self.__socialname = socialname

    @property
    def social(self) -> str:
        return self.__social

    @social.setter
    def social(self, social: str):
        self.__social = social

class mvc_MapComponent(View):

    def __init__(self, marker: bool, latitude: float, longitude: float):
        self.marker = marker
        self.latitude = latitude
        self.longitude = longitude
        
    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def marker(self) -> bool:
        return self.__marker

    @marker.setter
    def marker(self, marker: bool):
        self.__marker = marker

    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

class mvc_GraphicComponent(View):

    def __init__(self, stepSize: int, mvc_GraphicComponent: "mvc_Attribute" = None, mvc_GraphicComponent21: "mvc_Attribute" = None):
        self.stepSize = stepSize
        self.mvc_GraphicComponent = mvc_GraphicComponent
        self.mvc_GraphicComponent21 = mvc_GraphicComponent21
        
    @property
    def stepSize(self) -> int:
        return self.__stepSize

    @stepSize.setter
    def stepSize(self, stepSize: int):
        self.__stepSize = stepSize

    @property
    def mvc_GraphicComponent(self):
        return self.__mvc_GraphicComponent

    @mvc_GraphicComponent.setter
    def mvc_GraphicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_GraphicComponent__mvc_GraphicComponent", None)
        self.__mvc_GraphicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Attribute19"):
                opp_val = getattr(old_value, "mvc_Attribute19", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Attribute19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Attribute19"):
                opp_val = getattr(value, "mvc_Attribute19", None)
                setattr(value, "mvc_Attribute19", self)

    @property
    def mvc_GraphicComponent21(self):
        return self.__mvc_GraphicComponent21

    @mvc_GraphicComponent21.setter
    def mvc_GraphicComponent21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_GraphicComponent__mvc_GraphicComponent21", None)
        self.__mvc_GraphicComponent21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Attribute22"):
                opp_val = getattr(old_value, "mvc_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Attribute22"):
                opp_val = getattr(value, "mvc_Attribute22", None)
                setattr(value, "mvc_Attribute22", self)

class Model:

    pass
class mvc_DataBase(Model):

    pass
class mvc_Client(Model):

    def __init__(self, nameservice: str, mvc_Client: "mvc_Method" = None):
        self.nameservice = nameservice
        self.mvc_Client = mvc_Client
        
    @property
    def nameservice(self) -> str:
        return self.__nameservice

    @nameservice.setter
    def nameservice(self, nameservice: str):
        self.__nameservice = nameservice

    @property
    def mvc_Client(self):
        return self.__mvc_Client

    @mvc_Client.setter
    def mvc_Client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Client__mvc_Client", None)
        self.__mvc_Client = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Method15"):
                opp_val = getattr(old_value, "mvc_Method15", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Method15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Method15"):
                opp_val = getattr(value, "mvc_Method15", None)
                setattr(value, "mvc_Method15", self)

class mvc_Method:

    def __init__(self, type: str, namemethod: str, mvc_Method: set["mvc_Attribute"] = None, mvc_Method15: "mvc_Client" = None):
        self.type = type
        self.namemethod = namemethod
        self.mvc_Method = mvc_Method if mvc_Method is not None else set()
        self.mvc_Method15 = mvc_Method15
        
    @property
    def namemethod(self) -> str:
        return self.__namemethod

    @namemethod.setter
    def namemethod(self, namemethod: str):
        self.__namemethod = namemethod

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mvc_Method(self):
        return self.__mvc_Method

    @mvc_Method.setter
    def mvc_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Method__mvc_Method", None)
        self.__mvc_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Attribute"):
                    opp_val = getattr(item, "mvc_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Attribute"):
                    opp_val = getattr(item, "mvc_Attribute", None)
                    
                    setattr(item, "mvc_Attribute", self)
                    

    @property
    def mvc_Method15(self):
        return self.__mvc_Method15

    @mvc_Method15.setter
    def mvc_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Method__mvc_Method15", None)
        self.__mvc_Method15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Client"):
                opp_val = getattr(old_value, "mvc_Client", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Client", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Client"):
                opp_val = getattr(value, "mvc_Client", None)
                setattr(value, "mvc_Client", self)

class mvc_Attribute:

    def __init__(self, nameattribute: str, typeattribute: str, mvc_Attribute: "mvc_Method" = None, mvc_Attribute17: "mvc_DataBase" = None, mvc_Attribute19: "mvc_GraphicComponent" = None, mvc_Attribute22: "mvc_GraphicComponent" = None):
        self.nameattribute = nameattribute
        self.typeattribute = typeattribute
        self.mvc_Attribute = mvc_Attribute
        self.mvc_Attribute17 = mvc_Attribute17
        self.mvc_Attribute19 = mvc_Attribute19
        self.mvc_Attribute22 = mvc_Attribute22
        
    @property
    def nameattribute(self) -> str:
        return self.__nameattribute

    @nameattribute.setter
    def nameattribute(self, nameattribute: str):
        self.__nameattribute = nameattribute

    @property
    def typeattribute(self) -> str:
        return self.__typeattribute

    @typeattribute.setter
    def typeattribute(self, typeattribute: str):
        self.__typeattribute = typeattribute

    @property
    def mvc_Attribute22(self):
        return self.__mvc_Attribute22

    @mvc_Attribute22.setter
    def mvc_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute22", None)
        self.__mvc_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_GraphicComponent21"):
                opp_val = getattr(old_value, "mvc_GraphicComponent21", None)
                if opp_val == self:
                    setattr(old_value, "mvc_GraphicComponent21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_GraphicComponent21"):
                opp_val = getattr(value, "mvc_GraphicComponent21", None)
                setattr(value, "mvc_GraphicComponent21", self)

    @property
    def mvc_Attribute(self):
        return self.__mvc_Attribute

    @mvc_Attribute.setter
    def mvc_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute", None)
        self.__mvc_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Method"):
                opp_val = getattr(old_value, "mvc_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Method"):
                opp_val = getattr(value, "mvc_Method", None)
                if opp_val is None:
                    setattr(value, "mvc_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Attribute19(self):
        return self.__mvc_Attribute19

    @mvc_Attribute19.setter
    def mvc_Attribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute19", None)
        self.__mvc_Attribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_GraphicComponent"):
                opp_val = getattr(old_value, "mvc_GraphicComponent", None)
                if opp_val == self:
                    setattr(old_value, "mvc_GraphicComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_GraphicComponent"):
                opp_val = getattr(value, "mvc_GraphicComponent", None)
                setattr(value, "mvc_GraphicComponent", self)

    @property
    def mvc_Attribute17(self):
        return self.__mvc_Attribute17

    @mvc_Attribute17.setter
    def mvc_Attribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute17", None)
        self.__mvc_Attribute17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_DataBase"):
                opp_val = getattr(old_value, "mvc_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_DataBase"):
                opp_val = getattr(value, "mvc_DataBase", None)
                if opp_val is None:
                    setattr(value, "mvc_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Position:

    def __init__(self, above: int, align_left: int, wide: int, long: int, name: str, mvc_Position: "mvc_View" = None):
        self.above = above
        self.align_left = align_left
        self.wide = wide
        self.long = long
        self.name = name
        self.mvc_Position = mvc_Position
        
    @property
    def long(self) -> int:
        return self.__long

    @long.setter
    def long(self, long: int):
        self.__long = long

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def align_left(self) -> int:
        return self.__align_left

    @align_left.setter
    def align_left(self, align_left: int):
        self.__align_left = align_left

    @property
    def above(self) -> int:
        return self.__above

    @above.setter
    def above(self, above: int):
        self.__above = above

    @property
    def wide(self) -> int:
        return self.__wide

    @wide.setter
    def wide(self, wide: int):
        self.__wide = wide

    @property
    def mvc_Position(self):
        return self.__mvc_Position

    @mvc_Position.setter
    def mvc_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Position__mvc_Position", None)
        self.__mvc_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_View12"):
                opp_val = getattr(old_value, "mvc_View12", None)
                if opp_val == self:
                    setattr(old_value, "mvc_View12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_View12"):
                opp_val = getattr(value, "mvc_View12", None)
                setattr(value, "mvc_View12", self)

class mvc_Controller:

    def __init__(self, name: str, mvc_Controller: "mvc_MvcApplication" = None, controller: "mvc_Model" = None, Controller: "mvc_Model" = None, Controller10: "mvc_View" = None, controller7: "mvc_View" = None):
        self.name = name
        self.mvc_Controller = mvc_Controller
        self.controller = controller
        self.Controller = Controller
        self.Controller10 = Controller10
        self.controller7 = controller7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def controller7(self):
        return self.__controller7

    @controller7.setter
    def controller7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__controller7", None)
        self.__controller7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "View"):
                opp_val = getattr(old_value, "View", None)
                if opp_val == self:
                    setattr(old_value, "View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "View"):
                opp_val = getattr(value, "View", None)
                setattr(value, "View", self)

    @property
    def Controller10(self):
        return self.__Controller10

    @Controller10.setter
    def Controller10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__Controller10", None)
        self.__Controller10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view"):
                opp_val = getattr(old_value, "view", None)
                if opp_val == self:
                    setattr(old_value, "view", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view"):
                opp_val = getattr(value, "view", None)
                setattr(value, "view", self)

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__controller", None)
        self.__controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model"):
                opp_val = getattr(old_value, "Model", None)
                if opp_val == self:
                    setattr(old_value, "Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model"):
                opp_val = getattr(value, "Model", None)
                setattr(value, "Model", self)

    @property
    def Controller(self):
        return self.__Controller

    @Controller.setter
    def Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__Controller", None)
        self.__Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if opp_val == self:
                    setattr(old_value, "model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                setattr(value, "model", self)

    @property
    def mvc_Controller(self):
        return self.__mvc_Controller

    @mvc_Controller.setter
    def mvc_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller", None)
        self.__mvc_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MvcApplication4"):
                opp_val = getattr(old_value, "mvc_MvcApplication4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MvcApplication4"):
                opp_val = getattr(value, "mvc_MvcApplication4", None)
                if opp_val is None:
                    setattr(value, "mvc_MvcApplication4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Model:

    def __init__(self, nameclass: str, type: str, mvc_Model: "mvc_MvcApplication" = None, Model: "mvc_Controller" = None, model: "mvc_Controller" = None):
        self.nameclass = nameclass
        self.type = type
        self.mvc_Model = mvc_Model
        self.Model = Model
        self.model = model
        
    @property
    def nameclass(self) -> str:
        return self.__nameclass

    @nameclass.setter
    def nameclass(self, nameclass: str):
        self.__nameclass = nameclass

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mvc_Model(self):
        return self.__mvc_Model

    @mvc_Model.setter
    def mvc_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model", None)
        self.__mvc_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MvcApplication2"):
                opp_val = getattr(old_value, "mvc_MvcApplication2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MvcApplication2"):
                opp_val = getattr(value, "mvc_MvcApplication2", None)
                if opp_val is None:
                    setattr(value, "mvc_MvcApplication2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller"):
                opp_val = getattr(old_value, "controller", None)
                if opp_val == self:
                    setattr(old_value, "controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller"):
                opp_val = getattr(value, "controller", None)
                setattr(value, "controller", self)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controller"):
                opp_val = getattr(old_value, "Controller", None)
                if opp_val == self:
                    setattr(old_value, "Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controller"):
                opp_val = getattr(value, "Controller", None)
                setattr(value, "Controller", self)

class mvc_View:

    def __init__(self, name: str, type: str, mvc_View: "mvc_MvcApplication" = None, view: "mvc_Controller" = None, mvc_View12: "mvc_Position" = None, View: "mvc_Controller" = None):
        self.name = name
        self.type = type
        self.mvc_View = mvc_View
        self.view = view
        self.mvc_View12 = mvc_View12
        self.View = View
        
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
    def mvc_View12(self):
        return self.__mvc_View12

    @mvc_View12.setter
    def mvc_View12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View12", None)
        self.__mvc_View12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Position"):
                opp_val = getattr(old_value, "mvc_Position", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Position"):
                opp_val = getattr(value, "mvc_Position", None)
                setattr(value, "mvc_Position", self)

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__view", None)
        self.__view = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controller10"):
                opp_val = getattr(old_value, "Controller10", None)
                if opp_val == self:
                    setattr(old_value, "Controller10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controller10"):
                opp_val = getattr(value, "Controller10", None)
                setattr(value, "Controller10", self)

    @property
    def View(self):
        return self.__View

    @View.setter
    def View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__View", None)
        self.__View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller7"):
                opp_val = getattr(old_value, "controller7", None)
                if opp_val == self:
                    setattr(old_value, "controller7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller7"):
                opp_val = getattr(value, "controller7", None)
                setattr(value, "controller7", self)

    @property
    def mvc_View(self):
        return self.__mvc_View

    @mvc_View.setter
    def mvc_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View", None)
        self.__mvc_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MvcApplication"):
                opp_val = getattr(old_value, "mvc_MvcApplication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MvcApplication"):
                opp_val = getattr(value, "mvc_MvcApplication", None)
                if opp_val is None:
                    setattr(value, "mvc_MvcApplication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_MvcApplication:

    def __init__(self, name: str, picture: str, description: str, email: str, pagelink: str, mvc_MvcApplication: set["mvc_View"] = None, mvc_MvcApplication2: set["mvc_Model"] = None, mvc_MvcApplication4: set["mvc_Controller"] = None):
        self.name = name
        self.picture = picture
        self.description = description
        self.email = email
        self.pagelink = pagelink
        self.mvc_MvcApplication = mvc_MvcApplication if mvc_MvcApplication is not None else set()
        self.mvc_MvcApplication2 = mvc_MvcApplication2 if mvc_MvcApplication2 is not None else set()
        self.mvc_MvcApplication4 = mvc_MvcApplication4 if mvc_MvcApplication4 is not None else set()
        
    @property
    def pagelink(self) -> str:
        return self.__pagelink

    @pagelink.setter
    def pagelink(self, pagelink: str):
        self.__pagelink = pagelink

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def mvc_MvcApplication(self):
        return self.__mvc_MvcApplication

    @mvc_MvcApplication.setter
    def mvc_MvcApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MvcApplication__mvc_MvcApplication", None)
        self.__mvc_MvcApplication = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_View"):
                    opp_val = getattr(item, "mvc_View", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_View"):
                    opp_val = getattr(item, "mvc_View", None)
                    
                    setattr(item, "mvc_View", self)
                    

    @property
    def mvc_MvcApplication4(self):
        return self.__mvc_MvcApplication4

    @mvc_MvcApplication4.setter
    def mvc_MvcApplication4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MvcApplication__mvc_MvcApplication4", None)
        self.__mvc_MvcApplication4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Controller"):
                    opp_val = getattr(item, "mvc_Controller", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Controller", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Controller"):
                    opp_val = getattr(item, "mvc_Controller", None)
                    
                    setattr(item, "mvc_Controller", self)
                    

    @property
    def mvc_MvcApplication2(self):
        return self.__mvc_MvcApplication2

    @mvc_MvcApplication2.setter
    def mvc_MvcApplication2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MvcApplication__mvc_MvcApplication2", None)
        self.__mvc_MvcApplication2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Model"):
                    opp_val = getattr(item, "mvc_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Model"):
                    opp_val = getattr(item, "mvc_Model", None)
                    
                    setattr(item, "mvc_Model", self)
                    

from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SmartHouse_CoffeeMaker:

    def __init__(self, loaded: bool, on: bool, warming: bool, CoffeeMaker: "SmartHouse_Room" = None, cm: "SmartHouse_Room" = None):
        self.loaded = loaded
        self.on = on
        self.warming = warming
        self.CoffeeMaker = CoffeeMaker
        self.cm = cm
        
    @property
    def loaded(self) -> bool:
        return self.__loaded

    @loaded.setter
    def loaded(self, loaded: bool):
        self.__loaded = loaded

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def warming(self) -> bool:
        return self.__warming

    @warming.setter
    def warming(self, warming: bool):
        self.__warming = warming

    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_CoffeeMaker__cm", None)
        self.__cm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room46"):
                opp_val = getattr(old_value, "Room46", None)
                if opp_val == self:
                    setattr(old_value, "Room46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room46"):
                opp_val = getattr(value, "Room46", None)
                setattr(value, "Room46", self)

    @property
    def CoffeeMaker(self):
        return self.__CoffeeMaker

    @CoffeeMaker.setter
    def CoffeeMaker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_CoffeeMaker__CoffeeMaker", None)
        self.__CoffeeMaker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room38"):
                opp_val = getattr(old_value, "room38", None)
                if opp_val == self:
                    setattr(old_value, "room38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room38"):
                opp_val = getattr(value, "room38", None)
                setattr(value, "room38", self)

class SmartHouse_WashingMachine:

    def __init__(self, loaded: bool, on: bool, WashingMachine: "SmartHouse_Room" = None, wm: "SmartHouse_Room" = None):
        self.loaded = loaded
        self.on = on
        self.WashingMachine = WashingMachine
        self.wm = wm
        
    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def loaded(self) -> bool:
        return self.__loaded

    @loaded.setter
    def loaded(self, loaded: bool):
        self.__loaded = loaded

    @property
    def WashingMachine(self):
        return self.__WashingMachine

    @WashingMachine.setter
    def WashingMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_WashingMachine__WashingMachine", None)
        self.__WashingMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room36"):
                opp_val = getattr(old_value, "room36", None)
                if opp_val == self:
                    setattr(old_value, "room36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room36"):
                opp_val = getattr(value, "room36", None)
                setattr(value, "room36", self)

    @property
    def wm(self):
        return self.__wm

    @wm.setter
    def wm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_WashingMachine__wm", None)
        self.__wm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room44"):
                opp_val = getattr(old_value, "Room44", None)
                if opp_val == self:
                    setattr(old_value, "Room44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room44"):
                opp_val = getattr(value, "Room44", None)
                setattr(value, "Room44", self)

class SmartHouse_Cooker:

    def __init__(self, on: bool, SmartHouse_Cooker: "SmartHouse_Room" = None):
        self.on = on
        self.SmartHouse_Cooker = SmartHouse_Cooker
        
    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def SmartHouse_Cooker(self):
        return self.__SmartHouse_Cooker

    @SmartHouse_Cooker.setter
    def SmartHouse_Cooker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Cooker__SmartHouse_Cooker", None)
        self.__SmartHouse_Cooker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room34"):
                opp_val = getattr(old_value, "SmartHouse_Room34", None)
                if opp_val == self:
                    setattr(old_value, "SmartHouse_Room34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room34"):
                opp_val = getattr(value, "SmartHouse_Room34", None)
                setattr(value, "SmartHouse_Room34", self)

class SmartHouse_Projector:

    def __init__(self, on: bool, brightness: str, volume: str, Projector: "SmartHouse_Room" = None, projector: "SmartHouse_Room" = None):
        self.on = on
        self.brightness = brightness
        self.volume = volume
        self.Projector = Projector
        self.projector = projector
        
    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def brightness(self) -> str:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: str):
        self.__brightness = brightness

    @property
    def Projector(self):
        return self.__Projector

    @Projector.setter
    def Projector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Projector__Projector", None)
        self.__Projector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room32"):
                opp_val = getattr(old_value, "room32", None)
                if opp_val == self:
                    setattr(old_value, "room32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room32"):
                opp_val = getattr(value, "room32", None)
                setattr(value, "room32", self)

    @property
    def projector(self):
        return self.__projector

    @projector.setter
    def projector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Projector__projector", None)
        self.__projector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room42"):
                opp_val = getattr(old_value, "Room42", None)
                if opp_val == self:
                    setattr(old_value, "Room42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room42"):
                opp_val = getattr(value, "Room42", None)
                setattr(value, "Room42", self)

class SmartHouse_Sensor:

    def __init__(self, temp: bool, air: bool, brightness: bool, battery: str, circle: str, SmartHouse_Sensor: "SmartHouse_Room" = None):
        self.temp = temp
        self.air = air
        self.brightness = brightness
        self.battery = battery
        self.circle = circle
        self.SmartHouse_Sensor = SmartHouse_Sensor
        
    @property
    def battery(self) -> str:
        return self.__battery

    @battery.setter
    def battery(self, battery: str):
        self.__battery = battery

    @property
    def circle(self) -> str:
        return self.__circle

    @circle.setter
    def circle(self, circle: str):
        self.__circle = circle

    @property
    def air(self) -> bool:
        return self.__air

    @air.setter
    def air(self, air: bool):
        self.__air = air

    @property
    def temp(self) -> bool:
        return self.__temp

    @temp.setter
    def temp(self, temp: bool):
        self.__temp = temp

    @property
    def brightness(self) -> bool:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: bool):
        self.__brightness = brightness

    @property
    def SmartHouse_Sensor(self):
        return self.__SmartHouse_Sensor

    @SmartHouse_Sensor.setter
    def SmartHouse_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Sensor__SmartHouse_Sensor", None)
        self.__SmartHouse_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room30"):
                opp_val = getattr(old_value, "SmartHouse_Room30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room30"):
                opp_val = getattr(value, "SmartHouse_Room30", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_Room30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_AirConditioner:

    def __init__(self, level: str, freshAir: bool, AirConditioner: "SmartHouse_Room" = None, ac: "SmartHouse_Room" = None):
        self.level = level
        self.freshAir = freshAir
        self.AirConditioner = AirConditioner
        self.ac = ac
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def freshAir(self) -> bool:
        return self.__freshAir

    @freshAir.setter
    def freshAir(self, freshAir: bool):
        self.__freshAir = freshAir

    @property
    def ac(self):
        return self.__ac

    @ac.setter
    def ac(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_AirConditioner__ac", None)
        self.__ac = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room40"):
                opp_val = getattr(old_value, "Room40", None)
                if opp_val == self:
                    setattr(old_value, "Room40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room40"):
                opp_val = getattr(value, "Room40", None)
                setattr(value, "Room40", self)

    @property
    def AirConditioner(self):
        return self.__AirConditioner

    @AirConditioner.setter
    def AirConditioner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_AirConditioner__AirConditioner", None)
        self.__AirConditioner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room25"):
                opp_val = getattr(old_value, "room25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room25"):
                opp_val = getattr(value, "room25", None)
                if opp_val is None:
                    setattr(value, "room25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_Light:

    def __init__(self, level: str, SmartHouse_Light: "SmartHouse_Room" = None):
        self.level = level
        self.SmartHouse_Light = SmartHouse_Light
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def SmartHouse_Light(self):
        return self.__SmartHouse_Light

    @SmartHouse_Light.setter
    def SmartHouse_Light(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Light__SmartHouse_Light", None)
        self.__SmartHouse_Light = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room23"):
                opp_val = getattr(old_value, "SmartHouse_Room23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room23"):
                opp_val = getattr(value, "SmartHouse_Room23", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_Room23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_Heating:

    def __init__(self, name: str, level: int, SmartHouse_Heating: "SmartHouse_Room" = None):
        self.name = name
        self.level = level
        self.SmartHouse_Heating = SmartHouse_Heating
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SmartHouse_Heating(self):
        return self.__SmartHouse_Heating

    @SmartHouse_Heating.setter
    def SmartHouse_Heating(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Heating__SmartHouse_Heating", None)
        self.__SmartHouse_Heating = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room21"):
                opp_val = getattr(old_value, "SmartHouse_Room21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room21"):
                opp_val = getattr(value, "SmartHouse_Room21", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_Room21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_Window:

    def __init__(self, curtainOn: bool, opened: bool, name: str, SmartHouse_Window: "SmartHouse_Room" = None):
        self.curtainOn = curtainOn
        self.opened = opened
        self.name = name
        self.SmartHouse_Window = SmartHouse_Window
        
    @property
    def opened(self) -> bool:
        return self.__opened

    @opened.setter
    def opened(self, opened: bool):
        self.__opened = opened

    @property
    def curtainOn(self) -> bool:
        return self.__curtainOn

    @curtainOn.setter
    def curtainOn(self, curtainOn: bool):
        self.__curtainOn = curtainOn

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SmartHouse_Window(self):
        return self.__SmartHouse_Window

    @SmartHouse_Window.setter
    def SmartHouse_Window(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Window__SmartHouse_Window", None)
        self.__SmartHouse_Window = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room"):
                opp_val = getattr(old_value, "SmartHouse_Room", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room"):
                opp_val = getattr(value, "SmartHouse_Room", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_Room", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_Security:

    def __init__(self, on: bool, sec: "SmartHouse_House" = None, Security: "SmartHouse_House" = None):
        self.on = on
        self.sec = sec
        self.Security = Security
        
    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def Security(self):
        return self.__Security

    @Security.setter
    def Security(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Security__Security", None)
        self.__Security = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "house9"):
                opp_val = getattr(old_value, "house9", None)
                if opp_val == self:
                    setattr(old_value, "house9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "house9"):
                opp_val = getattr(value, "house9", None)
                setattr(value, "house9", self)

    @property
    def sec(self):
        return self.__sec

    @sec.setter
    def sec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Security__sec", None)
        self.__sec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "House12"):
                opp_val = getattr(old_value, "House12", None)
                if opp_val == self:
                    setattr(old_value, "House12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "House12"):
                opp_val = getattr(value, "House12", None)
                setattr(value, "House12", self)

class SmartHouse_Gate:

    def __init__(self, outlocked: bool, gate: "SmartHouse_House" = None, Gate: "SmartHouse_House" = None):
        self.outlocked = outlocked
        self.gate = gate
        self.Gate = Gate
        
    @property
    def outlocked(self) -> bool:
        return self.__outlocked

    @outlocked.setter
    def outlocked(self, outlocked: bool):
        self.__outlocked = outlocked

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Gate__gate", None)
        self.__gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "House"):
                opp_val = getattr(old_value, "House", None)
                if opp_val == self:
                    setattr(old_value, "House", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "House"):
                opp_val = getattr(value, "House", None)
                setattr(value, "House", self)

    @property
    def Gate(self):
        return self.__Gate

    @Gate.setter
    def Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Gate__Gate", None)
        self.__Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "house7"):
                opp_val = getattr(old_value, "house7", None)
                if opp_val == self:
                    setattr(old_value, "house7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "house7"):
                opp_val = getattr(value, "house7", None)
                setattr(value, "house7", self)

class SmartHouse_EV:

    def __init__(self, name: str, pluged: bool, level: str, charging: bool, EV: "SmartHouse_House" = None, ev: "SmartHouse_House" = None):
        self.name = name
        self.pluged = pluged
        self.level = level
        self.charging = charging
        self.EV = EV
        self.ev = ev
        
    @property
    def pluged(self) -> bool:
        return self.__pluged

    @pluged.setter
    def pluged(self, pluged: bool):
        self.__pluged = pluged

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def charging(self) -> bool:
        return self.__charging

    @charging.setter
    def charging(self, charging: bool):
        self.__charging = charging

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def ev(self):
        return self.__ev

    @ev.setter
    def ev(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_EV__ev", None)
        self.__ev = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "House16"):
                opp_val = getattr(old_value, "House16", None)
                if opp_val == self:
                    setattr(old_value, "House16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "House16"):
                opp_val = getattr(value, "House16", None)
                setattr(value, "House16", self)

    @property
    def EV(self):
        return self.__EV

    @EV.setter
    def EV(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_EV__EV", None)
        self.__EV = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "house5"):
                opp_val = getattr(old_value, "house5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "house5"):
                opp_val = getattr(value, "house5", None)
                if opp_val is None:
                    setattr(value, "house5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_WaterHeater:

    def __init__(self, temp: str, on: bool, boost: bool, WaterHeater: "SmartHouse_House" = None, wh: "SmartHouse_House" = None):
        self.temp = temp
        self.on = on
        self.boost = boost
        self.WaterHeater = WaterHeater
        self.wh = wh
        
    @property
    def boost(self) -> bool:
        return self.__boost

    @boost.setter
    def boost(self, boost: bool):
        self.__boost = boost

    @property
    def temp(self) -> str:
        return self.__temp

    @temp.setter
    def temp(self, temp: str):
        self.__temp = temp

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, on: bool):
        self.__on = on

    @property
    def wh(self):
        return self.__wh

    @wh.setter
    def wh(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_WaterHeater__wh", None)
        self.__wh = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "House14"):
                opp_val = getattr(old_value, "House14", None)
                if opp_val == self:
                    setattr(old_value, "House14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "House14"):
                opp_val = getattr(value, "House14", None)
                setattr(value, "House14", self)

    @property
    def WaterHeater(self):
        return self.__WaterHeater

    @WaterHeater.setter
    def WaterHeater(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_WaterHeater__WaterHeater", None)
        self.__WaterHeater = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "house3"):
                opp_val = getattr(old_value, "house3", None)
                if opp_val == self:
                    setattr(old_value, "house3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "house3"):
                opp_val = getattr(value, "house3", None)
                setattr(value, "house3", self)

class SmartHouse_Person:

    def __init__(self, name: str, SmartHouse_Person: "SmartHouse_House" = None, SmartHouse_Person28: "SmartHouse_Room" = None):
        self.name = name
        self.SmartHouse_Person = SmartHouse_Person
        self.SmartHouse_Person28 = SmartHouse_Person28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SmartHouse_Person28(self):
        return self.__SmartHouse_Person28

    @SmartHouse_Person28.setter
    def SmartHouse_Person28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Person__SmartHouse_Person28", None)
        self.__SmartHouse_Person28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Room27"):
                opp_val = getattr(old_value, "SmartHouse_Room27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Room27"):
                opp_val = getattr(value, "SmartHouse_Room27", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_Room27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SmartHouse_Person(self):
        return self.__SmartHouse_Person

    @SmartHouse_Person.setter
    def SmartHouse_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Person__SmartHouse_Person", None)
        self.__SmartHouse_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_House"):
                opp_val = getattr(old_value, "SmartHouse_House", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_House"):
                opp_val = getattr(value, "SmartHouse_House", None)
                if opp_val is None:
                    setattr(value, "SmartHouse_House", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHouse_Room:

    def __init__(self, temp: float, bright: str, air: int, name: str, Room: "SmartHouse_House" = None, room: "SmartHouse_House" = None, SmartHouse_Room: set["SmartHouse_Window"] = None, SmartHouse_Room21: set["SmartHouse_Heating"] = None, SmartHouse_Room23: set["SmartHouse_Light"] = None, room25: set["SmartHouse_AirConditioner"] = None, Room40: "SmartHouse_AirConditioner" = None, SmartHouse_Room27: set["SmartHouse_Person"] = None, SmartHouse_Room30: set["SmartHouse_Sensor"] = None, room32: "SmartHouse_Projector" = None, SmartHouse_Room34: "SmartHouse_Cooker" = None, room36: "SmartHouse_WashingMachine" = None, room38: "SmartHouse_CoffeeMaker" = None, Room42: "SmartHouse_Projector" = None, Room44: "SmartHouse_WashingMachine" = None, Room46: "SmartHouse_CoffeeMaker" = None):
        self.temp = temp
        self.bright = bright
        self.air = air
        self.name = name
        self.Room = Room
        self.room = room
        self.SmartHouse_Room = SmartHouse_Room if SmartHouse_Room is not None else set()
        self.SmartHouse_Room21 = SmartHouse_Room21 if SmartHouse_Room21 is not None else set()
        self.SmartHouse_Room23 = SmartHouse_Room23 if SmartHouse_Room23 is not None else set()
        self.room25 = room25 if room25 is not None else set()
        self.Room40 = Room40
        self.SmartHouse_Room27 = SmartHouse_Room27 if SmartHouse_Room27 is not None else set()
        self.SmartHouse_Room30 = SmartHouse_Room30 if SmartHouse_Room30 is not None else set()
        self.room32 = room32
        self.SmartHouse_Room34 = SmartHouse_Room34
        self.room36 = room36
        self.room38 = room38
        self.Room42 = Room42
        self.Room44 = Room44
        self.Room46 = Room46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def air(self) -> int:
        return self.__air

    @air.setter
    def air(self, air: int):
        self.__air = air

    @property
    def temp(self) -> float:
        return self.__temp

    @temp.setter
    def temp(self, temp: float):
        self.__temp = temp

    @property
    def bright(self) -> str:
        return self.__bright

    @bright.setter
    def bright(self, bright: str):
        self.__bright = bright

    @property
    def room32(self):
        return self.__room32

    @room32.setter
    def room32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__room32", None)
        self.__room32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projector"):
                opp_val = getattr(old_value, "Projector", None)
                if opp_val == self:
                    setattr(old_value, "Projector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projector"):
                opp_val = getattr(value, "Projector", None)
                setattr(value, "Projector", self)

    @property
    def SmartHouse_Room30(self):
        return self.__SmartHouse_Room30

    @SmartHouse_Room30.setter
    def SmartHouse_Room30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room30", None)
        self.__SmartHouse_Room30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Sensor"):
                    opp_val = getattr(item, "SmartHouse_Sensor", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Sensor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Sensor"):
                    opp_val = getattr(item, "SmartHouse_Sensor", None)
                    
                    setattr(item, "SmartHouse_Sensor", self)
                    

    @property
    def SmartHouse_Room(self):
        return self.__SmartHouse_Room

    @SmartHouse_Room.setter
    def SmartHouse_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room", None)
        self.__SmartHouse_Room = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Window"):
                    opp_val = getattr(item, "SmartHouse_Window", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Window", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Window"):
                    opp_val = getattr(item, "SmartHouse_Window", None)
                    
                    setattr(item, "SmartHouse_Window", self)
                    

    @property
    def Room46(self):
        return self.__Room46

    @Room46.setter
    def Room46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__Room46", None)
        self.__Room46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cm"):
                opp_val = getattr(old_value, "cm", None)
                if opp_val == self:
                    setattr(old_value, "cm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cm"):
                opp_val = getattr(value, "cm", None)
                setattr(value, "cm", self)

    @property
    def room36(self):
        return self.__room36

    @room36.setter
    def room36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__room36", None)
        self.__room36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WashingMachine"):
                opp_val = getattr(old_value, "WashingMachine", None)
                if opp_val == self:
                    setattr(old_value, "WashingMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WashingMachine"):
                opp_val = getattr(value, "WashingMachine", None)
                setattr(value, "WashingMachine", self)

    @property
    def SmartHouse_Room34(self):
        return self.__SmartHouse_Room34

    @SmartHouse_Room34.setter
    def SmartHouse_Room34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room34", None)
        self.__SmartHouse_Room34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHouse_Cooker"):
                opp_val = getattr(old_value, "SmartHouse_Cooker", None)
                if opp_val == self:
                    setattr(old_value, "SmartHouse_Cooker", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHouse_Cooker"):
                opp_val = getattr(value, "SmartHouse_Cooker", None)
                setattr(value, "SmartHouse_Cooker", self)

    @property
    def SmartHouse_Room23(self):
        return self.__SmartHouse_Room23

    @SmartHouse_Room23.setter
    def SmartHouse_Room23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room23", None)
        self.__SmartHouse_Room23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Light"):
                    opp_val = getattr(item, "SmartHouse_Light", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Light", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Light"):
                    opp_val = getattr(item, "SmartHouse_Light", None)
                    
                    setattr(item, "SmartHouse_Light", self)
                    

    @property
    def Room(self):
        return self.__Room

    @Room.setter
    def Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__Room", None)
        self.__Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "house"):
                opp_val = getattr(old_value, "house", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "house"):
                opp_val = getattr(value, "house", None)
                if opp_val is None:
                    setattr(value, "house", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SmartHouse_Room27(self):
        return self.__SmartHouse_Room27

    @SmartHouse_Room27.setter
    def SmartHouse_Room27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room27", None)
        self.__SmartHouse_Room27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Person28"):
                    opp_val = getattr(item, "SmartHouse_Person28", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Person28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Person28"):
                    opp_val = getattr(item, "SmartHouse_Person28", None)
                    
                    setattr(item, "SmartHouse_Person28", self)
                    

    @property
    def room38(self):
        return self.__room38

    @room38.setter
    def room38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__room38", None)
        self.__room38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoffeeMaker"):
                opp_val = getattr(old_value, "CoffeeMaker", None)
                if opp_val == self:
                    setattr(old_value, "CoffeeMaker", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoffeeMaker"):
                opp_val = getattr(value, "CoffeeMaker", None)
                setattr(value, "CoffeeMaker", self)

    @property
    def SmartHouse_Room21(self):
        return self.__SmartHouse_Room21

    @SmartHouse_Room21.setter
    def SmartHouse_Room21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__SmartHouse_Room21", None)
        self.__SmartHouse_Room21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Heating"):
                    opp_val = getattr(item, "SmartHouse_Heating", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Heating", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Heating"):
                    opp_val = getattr(item, "SmartHouse_Heating", None)
                    
                    setattr(item, "SmartHouse_Heating", self)
                    

    @property
    def room25(self):
        return self.__room25

    @room25.setter
    def room25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__room25", None)
        self.__room25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AirConditioner"):
                    opp_val = getattr(item, "AirConditioner", None)
                    
                    if opp_val == self:
                        setattr(item, "AirConditioner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AirConditioner"):
                    opp_val = getattr(item, "AirConditioner", None)
                    
                    setattr(item, "AirConditioner", self)
                    

    @property
    def Room40(self):
        return self.__Room40

    @Room40.setter
    def Room40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__Room40", None)
        self.__Room40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ac"):
                opp_val = getattr(old_value, "ac", None)
                if opp_val == self:
                    setattr(old_value, "ac", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ac"):
                opp_val = getattr(value, "ac", None)
                setattr(value, "ac", self)

    @property
    def Room42(self):
        return self.__Room42

    @Room42.setter
    def Room42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__Room42", None)
        self.__Room42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projector"):
                opp_val = getattr(old_value, "projector", None)
                if opp_val == self:
                    setattr(old_value, "projector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projector"):
                opp_val = getattr(value, "projector", None)
                setattr(value, "projector", self)

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__room", None)
        self.__room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "House18"):
                opp_val = getattr(old_value, "House18", None)
                if opp_val == self:
                    setattr(old_value, "House18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "House18"):
                opp_val = getattr(value, "House18", None)
                setattr(value, "House18", self)

    @property
    def Room44(self):
        return self.__Room44

    @Room44.setter
    def Room44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_Room__Room44", None)
        self.__Room44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wm"):
                opp_val = getattr(old_value, "wm", None)
                if opp_val == self:
                    setattr(old_value, "wm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wm"):
                opp_val = getattr(value, "wm", None)
                setattr(value, "wm", self)

class SmartHouse_House:

    def __init__(self, name: str, eprice: str, time: str, outtemp: str, House12: "SmartHouse_Security" = None, house: set["SmartHouse_Room"] = None, SmartHouse_House: set["SmartHouse_Person"] = None, house3: "SmartHouse_WaterHeater" = None, house5: set["SmartHouse_EV"] = None, house7: "SmartHouse_Gate" = None, house9: "SmartHouse_Security" = None, House: "SmartHouse_Gate" = None, House18: "SmartHouse_Room" = None, House14: "SmartHouse_WaterHeater" = None, House16: "SmartHouse_EV" = None):
        self.name = name
        self.eprice = eprice
        self.time = time
        self.outtemp = outtemp
        self.House12 = House12
        self.house = house if house is not None else set()
        self.SmartHouse_House = SmartHouse_House if SmartHouse_House is not None else set()
        self.house3 = house3
        self.house5 = house5 if house5 is not None else set()
        self.house7 = house7
        self.house9 = house9
        self.House = House
        self.House18 = House18
        self.House14 = House14
        self.House16 = House16
        
    @property
    def outtemp(self) -> str:
        return self.__outtemp

    @outtemp.setter
    def outtemp(self, outtemp: str):
        self.__outtemp = outtemp

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def eprice(self) -> str:
        return self.__eprice

    @eprice.setter
    def eprice(self, eprice: str):
        self.__eprice = eprice

    @property
    def house3(self):
        return self.__house3

    @house3.setter
    def house3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__house3", None)
        self.__house3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaterHeater"):
                opp_val = getattr(old_value, "WaterHeater", None)
                if opp_val == self:
                    setattr(old_value, "WaterHeater", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaterHeater"):
                opp_val = getattr(value, "WaterHeater", None)
                setattr(value, "WaterHeater", self)

    @property
    def House(self):
        return self.__House

    @House.setter
    def House(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__House", None)
        self.__House = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gate"):
                opp_val = getattr(old_value, "gate", None)
                if opp_val == self:
                    setattr(old_value, "gate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gate"):
                opp_val = getattr(value, "gate", None)
                setattr(value, "gate", self)

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__house", None)
        self.__house = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room"):
                    opp_val = getattr(item, "Room", None)
                    
                    if opp_val == self:
                        setattr(item, "Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room"):
                    opp_val = getattr(item, "Room", None)
                    
                    setattr(item, "Room", self)
                    

    @property
    def SmartHouse_House(self):
        return self.__SmartHouse_House

    @SmartHouse_House.setter
    def SmartHouse_House(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__SmartHouse_House", None)
        self.__SmartHouse_House = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHouse_Person"):
                    opp_val = getattr(item, "SmartHouse_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHouse_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHouse_Person"):
                    opp_val = getattr(item, "SmartHouse_Person", None)
                    
                    setattr(item, "SmartHouse_Person", self)
                    

    @property
    def house5(self):
        return self.__house5

    @house5.setter
    def house5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__house5", None)
        self.__house5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EV"):
                    opp_val = getattr(item, "EV", None)
                    
                    if opp_val == self:
                        setattr(item, "EV", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EV"):
                    opp_val = getattr(item, "EV", None)
                    
                    setattr(item, "EV", self)
                    

    @property
    def House14(self):
        return self.__House14

    @House14.setter
    def House14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__House14", None)
        self.__House14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh"):
                opp_val = getattr(old_value, "wh", None)
                if opp_val == self:
                    setattr(old_value, "wh", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh"):
                opp_val = getattr(value, "wh", None)
                setattr(value, "wh", self)

    @property
    def House18(self):
        return self.__House18

    @House18.setter
    def House18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__House18", None)
        self.__House18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room"):
                opp_val = getattr(old_value, "room", None)
                if opp_val == self:
                    setattr(old_value, "room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room"):
                opp_val = getattr(value, "room", None)
                setattr(value, "room", self)

    @property
    def house9(self):
        return self.__house9

    @house9.setter
    def house9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__house9", None)
        self.__house9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Security"):
                opp_val = getattr(old_value, "Security", None)
                if opp_val == self:
                    setattr(old_value, "Security", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Security"):
                opp_val = getattr(value, "Security", None)
                setattr(value, "Security", self)

    @property
    def House16(self):
        return self.__House16

    @House16.setter
    def House16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__House16", None)
        self.__House16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ev"):
                opp_val = getattr(old_value, "ev", None)
                if opp_val == self:
                    setattr(old_value, "ev", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ev"):
                opp_val = getattr(value, "ev", None)
                setattr(value, "ev", self)

    @property
    def House12(self):
        return self.__House12

    @House12.setter
    def House12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__House12", None)
        self.__House12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sec"):
                opp_val = getattr(old_value, "sec", None)
                if opp_val == self:
                    setattr(old_value, "sec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sec"):
                opp_val = getattr(value, "sec", None)
                setattr(value, "sec", self)

    @property
    def house7(self):
        return self.__house7

    @house7.setter
    def house7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHouse_House__house7", None)
        self.__house7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate"):
                opp_val = getattr(old_value, "Gate", None)
                if opp_val == self:
                    setattr(old_value, "Gate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate"):
                opp_val = getattr(value, "Gate", None)
                setattr(value, "Gate", self)

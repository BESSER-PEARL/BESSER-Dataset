from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Model_IDLE:

    pass


class Model_BalanceInquiryTransaction:

    pass


class Model_Init:

    pass


class Model_ISO:

    pass


class Model_Communication:

    pass


class Model_WithdrawTransaction:

    def __init__(self, amount: int):
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount



class Model_Queue:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Model_Transaction:

    def __init__(self, attribute: str, presenter: Presenter):
        self.attribute = attribute
        self.presenter = presenter
        
        pass
    @property
    def presenter(self):
        return self.__presenter
    @presenter.setter
    def presenter(self, presenter: Presenter):
        self.__presenter = presenter

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Model_Session:

    def __init__(self, DeviceStatus: str, pan: int, track2: str):
        self.DeviceStatus = DeviceStatus
        self.pan = pan
        self.track2 = track2
        
        pass
    @property
    def track2(self):
        return self.__track2
    @track2.setter
    def track2(self, track2: str):
        self.__track2 = track2

    @property
    def pan(self):
        return self.__pan
    @pan.setter
    def pan(self, pan: int):
        self.__pan = pan

    @property
    def DeviceStatus(self):
        return self.__DeviceStatus
    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus: str):
        self.__DeviceStatus = DeviceStatus



class Presenter:

    def __init__(self, currentView: str, session: str):
        self.currentView = currentView
        self.session = session
        
        pass
    @property
    def currentView(self):
        return self.__currentView
    @currentView.setter
    def currentView(self, currentView: str):
        self.__currentView = currentView

    @property
    def session(self):
        return self.__session
    @session.setter
    def session(self, session: str):
        self.__session = session


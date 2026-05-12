import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    TimeData,
    Station,
    Route,
    Reservation,
    RequestCarInfo,
    OverviewPolyline,
    Trip,
    FollowUpSubscriber,
    FollowUp,
    EventRegistrationInformation,
    EventPoint,
    Event,
    LatLng,
    Driver,
    User,
    AccountStatus,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_timedata_is_not_abstract():
    assert not inspect.isabstract(TimeData)


def test_timedata_constructor_exists():
    assert callable(TimeData.__init__)


def test_timedata_constructor_args():
    sig = inspect.signature(TimeData.__init__)
    params = list(sig.parameters.keys())
    assert "routes" in params, "Missing parameter 'routes'"

def test_timedata_has_routes():
    assert hasattr(TimeData, "routes")
    descriptor = None
    for klass in TimeData.__mro__:
        if "routes" in klass.__dict__:
            descriptor = klass.__dict__["routes"]
            break
    assert isinstance(descriptor, property)



def test_station_is_not_abstract():
    assert not inspect.isabstract(Station)


def test_station_constructor_exists():
    assert callable(Station.__init__)


def test_station_constructor_args():
    sig = inspect.signature(Station.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "nameEng" in params, "Missing parameter 'nameEng'"
    assert "nameAra" in params, "Missing parameter 'nameAra'"

def test_station_has_location():
    assert hasattr(Station, "location")
    descriptor = None
    for klass in Station.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_station_has_uid():
    assert hasattr(Station, "uid")
    descriptor = None
    for klass in Station.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_station_has_nameEng():
    assert hasattr(Station, "nameEng")
    descriptor = None
    for klass in Station.__mro__:
        if "nameEng" in klass.__dict__:
            descriptor = klass.__dict__["nameEng"]
            break
    assert isinstance(descriptor, property)

def test_station_has_nameAra():
    assert hasattr(Station, "nameAra")
    descriptor = None
    for klass in Station.__mro__:
        if "nameAra" in klass.__dict__:
            descriptor = klass.__dict__["nameAra"]
            break
    assert isinstance(descriptor, property)



def test_route_is_not_abstract():
    assert not inspect.isabstract(Route)


def test_route_constructor_exists():
    assert callable(Route.__init__)


def test_route_constructor_args():
    sig = inspect.signature(Route.__init__)
    params = list(sig.parameters.keys())
    assert "overviewPolyline" in params, "Missing parameter 'overviewPolyline'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "stations" in params, "Missing parameter 'stations'"
    assert "waypoints" in params, "Missing parameter 'waypoints'"
    assert "routeName" in params, "Missing parameter 'routeName'"

def test_route_has_overviewPolyline():
    assert hasattr(Route, "overviewPolyline")
    descriptor = None
    for klass in Route.__mro__:
        if "overviewPolyline" in klass.__dict__:
            descriptor = klass.__dict__["overviewPolyline"]
            break
    assert isinstance(descriptor, property)

def test_route_has_uid():
    assert hasattr(Route, "uid")
    descriptor = None
    for klass in Route.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_route_has_stations():
    assert hasattr(Route, "stations")
    descriptor = None
    for klass in Route.__mro__:
        if "stations" in klass.__dict__:
            descriptor = klass.__dict__["stations"]
            break
    assert isinstance(descriptor, property)

def test_route_has_waypoints():
    assert hasattr(Route, "waypoints")
    descriptor = None
    for klass in Route.__mro__:
        if "waypoints" in klass.__dict__:
            descriptor = klass.__dict__["waypoints"]
            break
    assert isinstance(descriptor, property)

def test_route_has_routeName():
    assert hasattr(Route, "routeName")
    descriptor = None
    for klass in Route.__mro__:
        if "routeName" in klass.__dict__:
            descriptor = klass.__dict__["routeName"]
            break
    assert isinstance(descriptor, property)



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(Reservation)


def test_reservation_constructor_exists():
    assert callable(Reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "inCar" in params, "Missing parameter 'inCar'"
    assert "dueAmout" in params, "Missing parameter 'dueAmout'"
    assert "route" in params, "Missing parameter 'route'"
    assert "reachedDest" in params, "Missing parameter 'reachedDest'"
    assert "paid" in params, "Missing parameter 'paid'"
    assert "reservationState" in params, "Missing parameter 'reservationState'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "paymentMethod" in params, "Missing parameter 'paymentMethod'"
    assert "reservedSeats" in params, "Missing parameter 'reservedSeats'"
    assert "user" in params, "Missing parameter 'user'"
    assert "pickupLocation" in params, "Missing parameter 'pickupLocation'"

def test_reservation_has_inCar():
    assert hasattr(Reservation, "inCar")
    descriptor = None
    for klass in Reservation.__mro__:
        if "inCar" in klass.__dict__:
            descriptor = klass.__dict__["inCar"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_dueAmout():
    assert hasattr(Reservation, "dueAmout")
    descriptor = None
    for klass in Reservation.__mro__:
        if "dueAmout" in klass.__dict__:
            descriptor = klass.__dict__["dueAmout"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_route():
    assert hasattr(Reservation, "route")
    descriptor = None
    for klass in Reservation.__mro__:
        if "route" in klass.__dict__:
            descriptor = klass.__dict__["route"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_reachedDest():
    assert hasattr(Reservation, "reachedDest")
    descriptor = None
    for klass in Reservation.__mro__:
        if "reachedDest" in klass.__dict__:
            descriptor = klass.__dict__["reachedDest"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_paid():
    assert hasattr(Reservation, "paid")
    descriptor = None
    for klass in Reservation.__mro__:
        if "paid" in klass.__dict__:
            descriptor = klass.__dict__["paid"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_reservationState():
    assert hasattr(Reservation, "reservationState")
    descriptor = None
    for klass in Reservation.__mro__:
        if "reservationState" in klass.__dict__:
            descriptor = klass.__dict__["reservationState"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_uid():
    assert hasattr(Reservation, "uid")
    descriptor = None
    for klass in Reservation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_paymentMethod():
    assert hasattr(Reservation, "paymentMethod")
    descriptor = None
    for klass in Reservation.__mro__:
        if "paymentMethod" in klass.__dict__:
            descriptor = klass.__dict__["paymentMethod"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_reservedSeats():
    assert hasattr(Reservation, "reservedSeats")
    descriptor = None
    for klass in Reservation.__mro__:
        if "reservedSeats" in klass.__dict__:
            descriptor = klass.__dict__["reservedSeats"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_user():
    assert hasattr(Reservation, "user")
    descriptor = None
    for klass in Reservation.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_pickupLocation():
    assert hasattr(Reservation, "pickupLocation")
    descriptor = None
    for klass in Reservation.__mro__:
        if "pickupLocation" in klass.__dict__:
            descriptor = klass.__dict__["pickupLocation"]
            break
    assert isinstance(descriptor, property)



def test_requestcarinfo_is_not_abstract():
    assert not inspect.isabstract(RequestCarInfo)


def test_requestcarinfo_constructor_exists():
    assert callable(RequestCarInfo.__init__)


def test_requestcarinfo_constructor_args():
    sig = inspect.signature(RequestCarInfo.__init__)
    params = list(sig.parameters.keys())
    assert "user" in params, "Missing parameter 'user'"
    assert "to" in params, "Missing parameter 'to'"
    assert "state" in params, "Missing parameter 'state'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberOfPassengers" in params, "Missing parameter 'numberOfPassengers'"
    assert "from" in params, "Missing parameter 'from'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "time" in params, "Missing parameter 'time'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "numberOfDays" in params, "Missing parameter 'numberOfDays'"

def test_requestcarinfo_has_user():
    assert hasattr(RequestCarInfo, "user")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_to():
    assert hasattr(RequestCarInfo, "to")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_state():
    assert hasattr(RequestCarInfo, "state")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_type():
    assert hasattr(RequestCarInfo, "type")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_numberOfPassengers():
    assert hasattr(RequestCarInfo, "numberOfPassengers")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "numberOfPassengers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPassengers"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_from():
    assert hasattr(RequestCarInfo, "from")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "from" in klass.__dict__:
            descriptor = klass.__dict__["from"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_uid():
    assert hasattr(RequestCarInfo, "uid")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_time():
    assert hasattr(RequestCarInfo, "time")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_comment():
    assert hasattr(RequestCarInfo, "comment")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_requestcarinfo_has_numberOfDays():
    assert hasattr(RequestCarInfo, "numberOfDays")
    descriptor = None
    for klass in RequestCarInfo.__mro__:
        if "numberOfDays" in klass.__dict__:
            descriptor = klass.__dict__["numberOfDays"]
            break
    assert isinstance(descriptor, property)



def test_overviewpolyline_is_not_abstract():
    assert not inspect.isabstract(OverviewPolyline)


def test_overviewpolyline_constructor_exists():
    assert callable(OverviewPolyline.__init__)


def test_overviewpolyline_constructor_args():
    sig = inspect.signature(OverviewPolyline.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_overviewpolyline_has_points():
    assert hasattr(OverviewPolyline, "points")
    descriptor = None
    for klass in OverviewPolyline.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_trip_is_not_abstract():
    assert not inspect.isabstract(Trip)


def test_trip_constructor_exists():
    assert callable(Trip.__init__)


def test_trip_constructor_args():
    sig = inspect.signature(Trip.__init__)
    params = list(sig.parameters.keys())
    assert "route" in params, "Missing parameter 'route'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "time" in params, "Missing parameter 'time'"
    assert "reservedSeats" in params, "Missing parameter 'reservedSeats'"
    assert "freeSeats" in params, "Missing parameter 'freeSeats'"
    assert "seatPrice" in params, "Missing parameter 'seatPrice'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "driver" in params, "Missing parameter 'driver'"
    assert "isLive" in params, "Missing parameter 'isLive'"
    assert "isIntercity" in params, "Missing parameter 'isIntercity'"

def test_trip_has_route():
    assert hasattr(Trip, "route")
    descriptor = None
    for klass in Trip.__mro__:
        if "route" in klass.__dict__:
            descriptor = klass.__dict__["route"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_uid():
    assert hasattr(Trip, "uid")
    descriptor = None
    for klass in Trip.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_time():
    assert hasattr(Trip, "time")
    descriptor = None
    for klass in Trip.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_reservedSeats():
    assert hasattr(Trip, "reservedSeats")
    descriptor = None
    for klass in Trip.__mro__:
        if "reservedSeats" in klass.__dict__:
            descriptor = klass.__dict__["reservedSeats"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_freeSeats():
    assert hasattr(Trip, "freeSeats")
    descriptor = None
    for klass in Trip.__mro__:
        if "freeSeats" in klass.__dict__:
            descriptor = klass.__dict__["freeSeats"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_seatPrice():
    assert hasattr(Trip, "seatPrice")
    descriptor = None
    for klass in Trip.__mro__:
        if "seatPrice" in klass.__dict__:
            descriptor = klass.__dict__["seatPrice"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_capacity():
    assert hasattr(Trip, "capacity")
    descriptor = None
    for klass in Trip.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_driver():
    assert hasattr(Trip, "driver")
    descriptor = None
    for klass in Trip.__mro__:
        if "driver" in klass.__dict__:
            descriptor = klass.__dict__["driver"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_isLive():
    assert hasattr(Trip, "isLive")
    descriptor = None
    for klass in Trip.__mro__:
        if "isLive" in klass.__dict__:
            descriptor = klass.__dict__["isLive"]
            break
    assert isinstance(descriptor, property)

def test_trip_has_isIntercity():
    assert hasattr(Trip, "isIntercity")
    descriptor = None
    for klass in Trip.__mro__:
        if "isIntercity" in klass.__dict__:
            descriptor = klass.__dict__["isIntercity"]
            break
    assert isinstance(descriptor, property)



def test_followupsubscriber_is_not_abstract():
    assert not inspect.isabstract(FollowUpSubscriber)


def test_followupsubscriber_constructor_exists():
    assert callable(FollowUpSubscriber.__init__)


def test_followupsubscriber_constructor_args():
    sig = inspect.signature(FollowUpSubscriber.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "followUpId" in params, "Missing parameter 'followUpId'"
    assert "user" in params, "Missing parameter 'user'"

def test_followupsubscriber_has_location():
    assert hasattr(FollowUpSubscriber, "location")
    descriptor = None
    for klass in FollowUpSubscriber.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_followupsubscriber_has_followUpId():
    assert hasattr(FollowUpSubscriber, "followUpId")
    descriptor = None
    for klass in FollowUpSubscriber.__mro__:
        if "followUpId" in klass.__dict__:
            descriptor = klass.__dict__["followUpId"]
            break
    assert isinstance(descriptor, property)

def test_followupsubscriber_has_user():
    assert hasattr(FollowUpSubscriber, "user")
    descriptor = None
    for klass in FollowUpSubscriber.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_followup_is_not_abstract():
    assert not inspect.isabstract(FollowUp)


def test_followup_constructor_exists():
    assert callable(FollowUp.__init__)


def test_followup_constructor_args():
    sig = inspect.signature(FollowUp.__init__)
    params = list(sig.parameters.keys())
    assert "from" in params, "Missing parameter 'from'"
    assert "freePickup" in params, "Missing parameter 'freePickup'"
    assert "password" in params, "Missing parameter 'password'"
    assert "time" in params, "Missing parameter 'time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "stations" in params, "Missing parameter 'stations'"
    assert "info" in params, "Missing parameter 'info'"
    assert "to" in params, "Missing parameter 'to'"
    assert "key" in params, "Missing parameter 'key'"
    assert "type" in params, "Missing parameter 'type'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "driver" in params, "Missing parameter 'driver'"

def test_followup_has_from():
    assert hasattr(FollowUp, "from")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "from" in klass.__dict__:
            descriptor = klass.__dict__["from"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_freePickup():
    assert hasattr(FollowUp, "freePickup")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "freePickup" in klass.__dict__:
            descriptor = klass.__dict__["freePickup"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_password():
    assert hasattr(FollowUp, "password")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_time():
    assert hasattr(FollowUp, "time")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_name():
    assert hasattr(FollowUp, "name")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_stations():
    assert hasattr(FollowUp, "stations")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "stations" in klass.__dict__:
            descriptor = klass.__dict__["stations"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_info():
    assert hasattr(FollowUp, "info")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_to():
    assert hasattr(FollowUp, "to")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_key():
    assert hasattr(FollowUp, "key")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_type():
    assert hasattr(FollowUp, "type")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_uid():
    assert hasattr(FollowUp, "uid")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_followup_has_driver():
    assert hasattr(FollowUp, "driver")
    descriptor = None
    for klass in FollowUp.__mro__:
        if "driver" in klass.__dict__:
            descriptor = klass.__dict__["driver"]
            break
    assert isinstance(descriptor, property)



def test_eventregistrationinformation_is_not_abstract():
    assert not inspect.isabstract(EventRegistrationInformation)


def test_eventregistrationinformation_constructor_exists():
    assert callable(EventRegistrationInformation.__init__)


def test_eventregistrationinformation_constructor_args():
    sig = inspect.signature(EventRegistrationInformation.__init__)
    params = list(sig.parameters.keys())
    assert "isPaid" in params, "Missing parameter 'isPaid'"
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"
    assert "state" in params, "Missing parameter 'state'"
    assert "paymentMethod" in params, "Missing parameter 'paymentMethod'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "eventId" in params, "Missing parameter 'eventId'"
    assert "passenger" in params, "Missing parameter 'passenger'"

def test_eventregistrationinformation_has_isPaid():
    assert hasattr(EventRegistrationInformation, "isPaid")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "isPaid" in klass.__dict__:
            descriptor = klass.__dict__["isPaid"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_numberOfSeats():
    assert hasattr(EventRegistrationInformation, "numberOfSeats")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "numberOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSeats"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_state():
    assert hasattr(EventRegistrationInformation, "state")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_paymentMethod():
    assert hasattr(EventRegistrationInformation, "paymentMethod")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "paymentMethod" in klass.__dict__:
            descriptor = klass.__dict__["paymentMethod"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_uid():
    assert hasattr(EventRegistrationInformation, "uid")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_eventId():
    assert hasattr(EventRegistrationInformation, "eventId")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "eventId" in klass.__dict__:
            descriptor = klass.__dict__["eventId"]
            break
    assert isinstance(descriptor, property)

def test_eventregistrationinformation_has_passenger():
    assert hasattr(EventRegistrationInformation, "passenger")
    descriptor = None
    for klass in EventRegistrationInformation.__mro__:
        if "passenger" in klass.__dict__:
            descriptor = klass.__dict__["passenger"]
            break
    assert isinstance(descriptor, property)



def test_eventpoint_is_not_abstract():
    assert not inspect.isabstract(EventPoint)


def test_eventpoint_constructor_exists():
    assert callable(EventPoint.__init__)


def test_eventpoint_constructor_args():
    sig = inspect.signature(EventPoint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "time" in params, "Missing parameter 'time'"
    assert "location" in params, "Missing parameter 'location'"

def test_eventpoint_has_type():
    assert hasattr(EventPoint, "type")
    descriptor = None
    for klass in EventPoint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_eventpoint_has_time():
    assert hasattr(EventPoint, "time")
    descriptor = None
    for klass in EventPoint.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_eventpoint_has_location():
    assert hasattr(EventPoint, "location")
    descriptor = None
    for klass in EventPoint.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "type" in params, "Missing parameter 'type'"
    assert "eventPoints" in params, "Missing parameter 'eventPoints'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"
    assert "status" in params, "Missing parameter 'status'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "freeSeats" in params, "Missing parameter 'freeSeats'"
    assert "bannerUrl" in params, "Missing parameter 'bannerUrl'"
    assert "time" in params, "Missing parameter 'time'"
    assert "info" in params, "Missing parameter 'info'"

def test_event_has_uid():
    assert hasattr(Event, "uid")
    descriptor = None
    for klass in Event.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_event_has_type():
    assert hasattr(Event, "type")
    descriptor = None
    for klass in Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_event_has_eventPoints():
    assert hasattr(Event, "eventPoints")
    descriptor = None
    for klass in Event.__mro__:
        if "eventPoints" in klass.__dict__:
            descriptor = klass.__dict__["eventPoints"]
            break
    assert isinstance(descriptor, property)

def test_event_has_phoneNumber():
    assert hasattr(Event, "phoneNumber")
    descriptor = None
    for klass in Event.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_event_has_startTime():
    assert hasattr(Event, "startTime")
    descriptor = None
    for klass in Event.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
            break
    assert isinstance(descriptor, property)

def test_event_has_price():
    assert hasattr(Event, "price")
    descriptor = None
    for klass in Event.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_event_has_name():
    assert hasattr(Event, "name")
    descriptor = None
    for klass in Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_event_has_status():
    assert hasattr(Event, "status")
    descriptor = None
    for klass in Event.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_event_has_endTime():
    assert hasattr(Event, "endTime")
    descriptor = None
    for klass in Event.__mro__:
        if "endTime" in klass.__dict__:
            descriptor = klass.__dict__["endTime"]
            break
    assert isinstance(descriptor, property)

def test_event_has_freeSeats():
    assert hasattr(Event, "freeSeats")
    descriptor = None
    for klass in Event.__mro__:
        if "freeSeats" in klass.__dict__:
            descriptor = klass.__dict__["freeSeats"]
            break
    assert isinstance(descriptor, property)

def test_event_has_bannerUrl():
    assert hasattr(Event, "bannerUrl")
    descriptor = None
    for klass in Event.__mro__:
        if "bannerUrl" in klass.__dict__:
            descriptor = klass.__dict__["bannerUrl"]
            break
    assert isinstance(descriptor, property)

def test_event_has_time():
    assert hasattr(Event, "time")
    descriptor = None
    for klass in Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_event_has_info():
    assert hasattr(Event, "info")
    descriptor = None
    for klass in Event.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_latlng_is_not_abstract():
    assert not inspect.isabstract(LatLng)


def test_latlng_constructor_exists():
    assert callable(LatLng.__init__)


def test_latlng_constructor_args():
    sig = inspect.signature(LatLng.__init__)
    params = list(sig.parameters.keys())
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"

def test_latlng_has_latitude():
    assert hasattr(LatLng, "latitude")
    descriptor = None
    for klass in LatLng.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_latlng_has_longitude():
    assert hasattr(LatLng, "longitude")
    descriptor = None
    for klass in LatLng.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)



def test_driver_is_not_abstract():
    assert not inspect.isabstract(Driver)


def test_driver_constructor_exists():
    assert callable(Driver.__init__)


def test_driver_constructor_args():
    sig = inspect.signature(Driver.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfRatings" in params, "Missing parameter 'numberOfRatings'"
    assert "email" in params, "Missing parameter 'email'"
    assert "averageRating" in params, "Missing parameter 'averageRating'"
    assert "username" in params, "Missing parameter 'username'"
    assert "avatar" in params, "Missing parameter 'avatar'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "carLicense" in params, "Missing parameter 'carLicense'"

def test_driver_has_numberOfRatings():
    assert hasattr(Driver, "numberOfRatings")
    descriptor = None
    for klass in Driver.__mro__:
        if "numberOfRatings" in klass.__dict__:
            descriptor = klass.__dict__["numberOfRatings"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_email():
    assert hasattr(Driver, "email")
    descriptor = None
    for klass in Driver.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_averageRating():
    assert hasattr(Driver, "averageRating")
    descriptor = None
    for klass in Driver.__mro__:
        if "averageRating" in klass.__dict__:
            descriptor = klass.__dict__["averageRating"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_username():
    assert hasattr(Driver, "username")
    descriptor = None
    for klass in Driver.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_avatar():
    assert hasattr(Driver, "avatar")
    descriptor = None
    for klass in Driver.__mro__:
        if "avatar" in klass.__dict__:
            descriptor = klass.__dict__["avatar"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_phoneNumber():
    assert hasattr(Driver, "phoneNumber")
    descriptor = None
    for klass in Driver.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_carLicense():
    assert hasattr(Driver, "carLicense")
    descriptor = None
    for klass in Driver.__mro__:
        if "carLicense" in klass.__dict__:
            descriptor = klass.__dict__["carLicense"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "referrer" in params, "Missing parameter 'referrer'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "numberOfReferrals" in params, "Missing parameter 'numberOfReferrals'"
    assert "avatar" in params, "Missing parameter 'avatar'"
    assert "id" in params, "Missing parameter 'id'"
    assert "accountStatus" in params, "Missing parameter 'accountStatus'"
    assert "referralCode" in params, "Missing parameter 'referralCode'"
    assert "username" in params, "Missing parameter 'username'"
    assert "email" in params, "Missing parameter 'email'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_user_has_referrer():
    assert hasattr(User, "referrer")
    descriptor = None
    for klass in User.__mro__:
        if "referrer" in klass.__dict__:
            descriptor = klass.__dict__["referrer"]
            break
    assert isinstance(descriptor, property)

def test_user_has_birthDate():
    assert hasattr(User, "birthDate")
    descriptor = None
    for klass in User.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phoneNumber():
    assert hasattr(User, "phoneNumber")
    descriptor = None
    for klass in User.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_user_has_numberOfReferrals():
    assert hasattr(User, "numberOfReferrals")
    descriptor = None
    for klass in User.__mro__:
        if "numberOfReferrals" in klass.__dict__:
            descriptor = klass.__dict__["numberOfReferrals"]
            break
    assert isinstance(descriptor, property)

def test_user_has_avatar():
    assert hasattr(User, "avatar")
    descriptor = None
    for klass in User.__mro__:
        if "avatar" in klass.__dict__:
            descriptor = klass.__dict__["avatar"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id():
    assert hasattr(User, "id")
    descriptor = None
    for klass in User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_accountStatus():
    assert hasattr(User, "accountStatus")
    descriptor = None
    for klass in User.__mro__:
        if "accountStatus" in klass.__dict__:
            descriptor = klass.__dict__["accountStatus"]
            break
    assert isinstance(descriptor, property)

def test_user_has_referralCode():
    assert hasattr(User, "referralCode")
    descriptor = None
    for klass in User.__mro__:
        if "referralCode" in klass.__dict__:
            descriptor = klass.__dict__["referralCode"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_gender():
    assert hasattr(User, "gender")
    descriptor = None
    for klass in User.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_user_has_balance():
    assert hasattr(User, "balance")
    descriptor = None
    for klass in User.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_accountstatus_exists():
    # Check that the Enumeration exists
    assert AccountStatus is not None

def test_accountstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccountStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccountStatus"

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Class_strategy = st.builds(
    Class,
)
TimeData_strategy = st.builds(
    TimeData,
    routes=
        safe_text
)
Station_strategy = st.builds(
    Station,
    location=
        st.none(),
    uid=
        safe_text,
    nameEng=
        safe_text,
    nameAra=
        safe_text
)
Route_strategy = st.builds(
    Route,
    overviewPolyline=
        st.none(),
    uid=
        safe_text,
    stations=
        safe_text,
    waypoints=
        safe_text,
    routeName=
        safe_text
)
Reservation_strategy = st.builds(
    Reservation,
    inCar=
        st.booleans(),
    dueAmout=
        safe_text,
    route=
        st.none(),
    reachedDest=
        st.booleans(),
    paid=
        st.booleans(),
    reservationState=
        st.integers(),
    uid=
        safe_text,
    paymentMethod=
        st.integers(),
    reservedSeats=
        st.integers(),
    user=
        st.none(),
    pickupLocation=
        st.none()
)
RequestCarInfo_strategy = st.builds(
    RequestCarInfo,
    user=
        st.none(),
    to=
        safe_text,
    state=
        st.integers(),
    type=
        st.integers(),
    numberOfPassengers=
        st.integers(),
    from=
        safe_text,
    uid=
        safe_text,
    time=
        safe_text,
    comment=
        safe_text,
    numberOfDays=
        st.integers()
)
OverviewPolyline_strategy = st.builds(
    OverviewPolyline,
    points=
        safe_text
)
Trip_strategy = st.builds(
    Trip,
    route=
        st.none(),
    uid=
        safe_text,
    time=
        safe_text,
    reservedSeats=
        st.integers(),
    freeSeats=
        st.integers(),
    seatPrice=
        safe_text,
    capacity=
        st.integers(),
    driver=
        st.none(),
    isLive=
        st.booleans(),
    isIntercity=
        st.booleans()
)
FollowUpSubscriber_strategy = st.builds(
    FollowUpSubscriber,
    location=
        st.none(),
    followUpId=
        safe_text,
    user=
        st.none()
)
FollowUp_strategy = st.builds(
    FollowUp,
    from=
        safe_text,
    freePickup=
        st.booleans(),
    password=
        safe_text,
    time=
        safe_text,
    name=
        safe_text,
    stations=
        safe_text,
    info=
        safe_text,
    to=
        safe_text,
    key=
        safe_text,
    type=
        st.integers(),
    uid=
        safe_text,
    driver=
        st.none()
)
EventRegistrationInformation_strategy = st.builds(
    EventRegistrationInformation,
    isPaid=
        st.booleans(),
    numberOfSeats=
        st.integers(),
    state=
        st.integers(),
    paymentMethod=
        st.integers(),
    uid=
        safe_text,
    eventId=
        safe_text,
    passenger=
        st.none()
)
EventPoint_strategy = st.builds(
    EventPoint,
    type=
        st.integers(),
    time=
        safe_text,
    location=
        st.none()
)
Event_strategy = st.builds(
    Event,
    uid=
        safe_text,
    type=
        st.integers(),
    eventPoints=
        safe_text,
    phoneNumber=
        safe_text,
    startTime=
        safe_text,
    price=
        safe_text,
    name=
        safe_text,
    status=
        safe_text,
    endTime=
        safe_text,
    freeSeats=
        st.integers(),
    bannerUrl=
        safe_text,
    time=
        safe_text,
    info=
        safe_text
)
LatLng_strategy = st.builds(
    LatLng,
    latitude=
        safe_text,
    longitude=
        safe_text
)
Driver_strategy = st.builds(
    Driver,
    numberOfRatings=
        st.integers(),
    email=
        safe_text,
    averageRating=
        safe_text,
    username=
        safe_text,
    avatar=
        safe_text,
    phoneNumber=
        safe_text,
    carLicense=
        safe_text
)
User_strategy = st.builds(
    User,
    referrer=
        safe_text,
    birthDate=
        safe_text,
    phoneNumber=
        safe_text,
    numberOfReferrals=
        st.integers(),
    avatar=
        safe_text,
    id=
        safe_text,
    accountStatus=
        st.none(),
    referralCode=
        safe_text,
    username=
        safe_text,
    email=
        safe_text,
    gender=
        st.integers(),
    balance=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=TimeData_strategy)
@settings(max_examples=50)
def test_timedata_instantiation(instance):
    assert isinstance(instance, TimeData)



@given(instance=TimeData_strategy)
def test_timedata_routes_setter(instance):
    original = instance.routes
    instance.routes = original
    assert instance.routes == original

@given(instance=Station_strategy)
@settings(max_examples=50)
def test_station_instantiation(instance):
    assert isinstance(instance, Station)



@given(instance=Station_strategy)
def test_station_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Station_strategy)
def test_station_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Station_strategy)
def test_station_nameEng_setter(instance):
    original = instance.nameEng
    instance.nameEng = original
    assert instance.nameEng == original



@given(instance=Station_strategy)
def test_station_nameAra_setter(instance):
    original = instance.nameAra
    instance.nameAra = original
    assert instance.nameAra == original

@given(instance=Route_strategy)
@settings(max_examples=50)
def test_route_instantiation(instance):
    assert isinstance(instance, Route)



@given(instance=Route_strategy)
def test_route_overviewPolyline_setter(instance):
    original = instance.overviewPolyline
    instance.overviewPolyline = original
    assert instance.overviewPolyline == original



@given(instance=Route_strategy)
def test_route_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Route_strategy)
def test_route_stations_setter(instance):
    original = instance.stations
    instance.stations = original
    assert instance.stations == original



@given(instance=Route_strategy)
def test_route_waypoints_setter(instance):
    original = instance.waypoints
    instance.waypoints = original
    assert instance.waypoints == original



@given(instance=Route_strategy)
def test_route_routeName_setter(instance):
    original = instance.routeName
    instance.routeName = original
    assert instance.routeName == original

@given(instance=Reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, Reservation)



@given(instance=Reservation_strategy)
def test_reservation_inCar_setter(instance):
    original = instance.inCar
    instance.inCar = original
    assert instance.inCar == original



@given(instance=Reservation_strategy)
def test_reservation_dueAmout_setter(instance):
    original = instance.dueAmout
    instance.dueAmout = original
    assert instance.dueAmout == original



@given(instance=Reservation_strategy)
def test_reservation_route_setter(instance):
    original = instance.route
    instance.route = original
    assert instance.route == original



@given(instance=Reservation_strategy)
def test_reservation_reachedDest_setter(instance):
    original = instance.reachedDest
    instance.reachedDest = original
    assert instance.reachedDest == original



@given(instance=Reservation_strategy)
def test_reservation_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original



@given(instance=Reservation_strategy)
def test_reservation_reservationState_setter(instance):
    original = instance.reservationState
    instance.reservationState = original
    assert instance.reservationState == original



@given(instance=Reservation_strategy)
def test_reservation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Reservation_strategy)
def test_reservation_paymentMethod_setter(instance):
    original = instance.paymentMethod
    instance.paymentMethod = original
    assert instance.paymentMethod == original



@given(instance=Reservation_strategy)
def test_reservation_reservedSeats_setter(instance):
    original = instance.reservedSeats
    instance.reservedSeats = original
    assert instance.reservedSeats == original



@given(instance=Reservation_strategy)
def test_reservation_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=Reservation_strategy)
def test_reservation_pickupLocation_setter(instance):
    original = instance.pickupLocation
    instance.pickupLocation = original
    assert instance.pickupLocation == original

@given(instance=RequestCarInfo_strategy)
@settings(max_examples=50)
def test_requestcarinfo_instantiation(instance):
    assert isinstance(instance, RequestCarInfo)



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_numberOfPassengers_setter(instance):
    original = instance.numberOfPassengers
    instance.numberOfPassengers = original
    assert instance.numberOfPassengers == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_from_setter(instance):
    original = instance.from
    instance.from = original
    assert instance.from == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=RequestCarInfo_strategy)
def test_requestcarinfo_numberOfDays_setter(instance):
    original = instance.numberOfDays
    instance.numberOfDays = original
    assert instance.numberOfDays == original

@given(instance=OverviewPolyline_strategy)
@settings(max_examples=50)
def test_overviewpolyline_instantiation(instance):
    assert isinstance(instance, OverviewPolyline)



@given(instance=OverviewPolyline_strategy)
def test_overviewpolyline_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=Trip_strategy)
@settings(max_examples=50)
def test_trip_instantiation(instance):
    assert isinstance(instance, Trip)



@given(instance=Trip_strategy)
def test_trip_route_setter(instance):
    original = instance.route
    instance.route = original
    assert instance.route == original



@given(instance=Trip_strategy)
def test_trip_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Trip_strategy)
def test_trip_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Trip_strategy)
def test_trip_reservedSeats_setter(instance):
    original = instance.reservedSeats
    instance.reservedSeats = original
    assert instance.reservedSeats == original



@given(instance=Trip_strategy)
def test_trip_freeSeats_setter(instance):
    original = instance.freeSeats
    instance.freeSeats = original
    assert instance.freeSeats == original



@given(instance=Trip_strategy)
def test_trip_seatPrice_setter(instance):
    original = instance.seatPrice
    instance.seatPrice = original
    assert instance.seatPrice == original



@given(instance=Trip_strategy)
def test_trip_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=Trip_strategy)
def test_trip_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original



@given(instance=Trip_strategy)
def test_trip_isLive_setter(instance):
    original = instance.isLive
    instance.isLive = original
    assert instance.isLive == original



@given(instance=Trip_strategy)
def test_trip_isIntercity_setter(instance):
    original = instance.isIntercity
    instance.isIntercity = original
    assert instance.isIntercity == original

@given(instance=FollowUpSubscriber_strategy)
@settings(max_examples=50)
def test_followupsubscriber_instantiation(instance):
    assert isinstance(instance, FollowUpSubscriber)



@given(instance=FollowUpSubscriber_strategy)
def test_followupsubscriber_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=FollowUpSubscriber_strategy)
def test_followupsubscriber_followUpId_setter(instance):
    original = instance.followUpId
    instance.followUpId = original
    assert instance.followUpId == original



@given(instance=FollowUpSubscriber_strategy)
def test_followupsubscriber_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=FollowUp_strategy)
@settings(max_examples=50)
def test_followup_instantiation(instance):
    assert isinstance(instance, FollowUp)



@given(instance=FollowUp_strategy)
def test_followup_from_setter(instance):
    original = instance.from
    instance.from = original
    assert instance.from == original



@given(instance=FollowUp_strategy)
def test_followup_freePickup_setter(instance):
    original = instance.freePickup
    instance.freePickup = original
    assert instance.freePickup == original



@given(instance=FollowUp_strategy)
def test_followup_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=FollowUp_strategy)
def test_followup_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=FollowUp_strategy)
def test_followup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FollowUp_strategy)
def test_followup_stations_setter(instance):
    original = instance.stations
    instance.stations = original
    assert instance.stations == original



@given(instance=FollowUp_strategy)
def test_followup_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original



@given(instance=FollowUp_strategy)
def test_followup_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=FollowUp_strategy)
def test_followup_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=FollowUp_strategy)
def test_followup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=FollowUp_strategy)
def test_followup_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=FollowUp_strategy)
def test_followup_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original

@given(instance=EventRegistrationInformation_strategy)
@settings(max_examples=50)
def test_eventregistrationinformation_instantiation(instance):
    assert isinstance(instance, EventRegistrationInformation)



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_isPaid_setter(instance):
    original = instance.isPaid
    instance.isPaid = original
    assert instance.isPaid == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_paymentMethod_setter(instance):
    original = instance.paymentMethod
    instance.paymentMethod = original
    assert instance.paymentMethod == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original



@given(instance=EventRegistrationInformation_strategy)
def test_eventregistrationinformation_passenger_setter(instance):
    original = instance.passenger
    instance.passenger = original
    assert instance.passenger == original

@given(instance=EventPoint_strategy)
@settings(max_examples=50)
def test_eventpoint_instantiation(instance):
    assert isinstance(instance, EventPoint)



@given(instance=EventPoint_strategy)
def test_eventpoint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=EventPoint_strategy)
def test_eventpoint_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=EventPoint_strategy)
def test_eventpoint_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Event_strategy)
def test_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Event_strategy)
def test_event_eventPoints_setter(instance):
    original = instance.eventPoints
    instance.eventPoints = original
    assert instance.eventPoints == original



@given(instance=Event_strategy)
def test_event_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Event_strategy)
def test_event_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Event_strategy)
def test_event_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Event_strategy)
def test_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Event_strategy)
def test_event_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Event_strategy)
def test_event_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Event_strategy)
def test_event_freeSeats_setter(instance):
    original = instance.freeSeats
    instance.freeSeats = original
    assert instance.freeSeats == original



@given(instance=Event_strategy)
def test_event_bannerUrl_setter(instance):
    original = instance.bannerUrl
    instance.bannerUrl = original
    assert instance.bannerUrl == original



@given(instance=Event_strategy)
def test_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Event_strategy)
def test_event_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=LatLng_strategy)
@settings(max_examples=50)
def test_latlng_instantiation(instance):
    assert isinstance(instance, LatLng)



@given(instance=LatLng_strategy)
def test_latlng_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=LatLng_strategy)
def test_latlng_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=Driver_strategy)
@settings(max_examples=50)
def test_driver_instantiation(instance):
    assert isinstance(instance, Driver)



@given(instance=Driver_strategy)
def test_driver_numberOfRatings_setter(instance):
    original = instance.numberOfRatings
    instance.numberOfRatings = original
    assert instance.numberOfRatings == original



@given(instance=Driver_strategy)
def test_driver_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Driver_strategy)
def test_driver_averageRating_setter(instance):
    original = instance.averageRating
    instance.averageRating = original
    assert instance.averageRating == original



@given(instance=Driver_strategy)
def test_driver_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Driver_strategy)
def test_driver_avatar_setter(instance):
    original = instance.avatar
    instance.avatar = original
    assert instance.avatar == original



@given(instance=Driver_strategy)
def test_driver_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Driver_strategy)
def test_driver_carLicense_setter(instance):
    original = instance.carLicense
    instance.carLicense = original
    assert instance.carLicense == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_referrer_setter(instance):
    original = instance.referrer
    instance.referrer = original
    assert instance.referrer == original



@given(instance=User_strategy)
def test_user_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=User_strategy)
def test_user_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=User_strategy)
def test_user_numberOfReferrals_setter(instance):
    original = instance.numberOfReferrals
    instance.numberOfReferrals = original
    assert instance.numberOfReferrals == original



@given(instance=User_strategy)
def test_user_avatar_setter(instance):
    original = instance.avatar
    instance.avatar = original
    assert instance.avatar == original



@given(instance=User_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_user_accountStatus_setter(instance):
    original = instance.accountStatus
    instance.accountStatus = original
    assert instance.accountStatus == original



@given(instance=User_strategy)
def test_user_referralCode_setter(instance):
    original = instance.referralCode
    instance.referralCode = original
    assert instance.referralCode == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_user_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=User_strategy)
def test_user_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

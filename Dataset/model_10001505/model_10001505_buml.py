####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

AccountStatus: Enumeration = Enumeration(
    name="AccountStatus",
    literals={
            
    }
)

# Classes
User = Class(name="User")
Driver = Class(name="Driver")
LatLng = Class(name="LatLng")
Event = Class(name="Event")
EventPoint = Class(name="EventPoint")
EventRegistrationInformation = Class(name="EventRegistrationInformation")
FollowUp = Class(name="FollowUp")
FollowUpSubscriber = Class(name="FollowUpSubscriber")
Trip = Class(name="Trip")
OverviewPolyline = Class(name="OverviewPolyline")
RequestCarInfo = Class(name="RequestCarInfo")
Reservation = Class(name="Reservation")
Route = Class(name="Route")
Station = Class(name="Station")
TimeData = Class(name="TimeData")
Class_ = Class(name="Class")

# User class attributes and methods
User_id: Property = Property(name="id", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_avatar: Property = Property(name="avatar", type=StringType)
User_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
User_gender: Property = Property(name="gender", type=IntegerType)
User_birthDate: Property = Property(name="birthDate", type=StringType)
User_referralCode: Property = Property(name="referralCode", type=StringType)
User_numberOfReferrals: Property = Property(name="numberOfReferrals", type=IntegerType)
User_balance: Property = Property(name="balance", type=StringType)
User_referrer: Property = Property(name="referrer", type=StringType)
User_accountStatus: Property = Property(name="accountStatus", type=AccountStatus)
User.attributes={User_email, User_birthDate, User_referrer, User_gender, User_balance, User_referralCode, User_avatar, User_username, User_id, User_accountStatus, User_numberOfReferrals, User_phoneNumber}

# Driver class attributes and methods
Driver_username: Property = Property(name="username", type=StringType)
Driver_email: Property = Property(name="email", type=StringType)
Driver_carLicense: Property = Property(name="carLicense", type=StringType)
Driver_averageRating: Property = Property(name="averageRating", type=StringType)
Driver_numberOfRatings: Property = Property(name="numberOfRatings", type=IntegerType)
Driver_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Driver_avatar: Property = Property(name="avatar", type=StringType)
Driver.attributes={Driver_avatar, Driver_numberOfRatings, Driver_carLicense, Driver_phoneNumber, Driver_averageRating, Driver_username, Driver_email}

# LatLng class attributes and methods
LatLng_latitude: Property = Property(name="latitude", type=StringType)
LatLng_longitude: Property = Property(name="longitude", type=StringType)
LatLng.attributes={LatLng_longitude, LatLng_latitude}

# Event class attributes and methods
Event_name: Property = Property(name="name", type=StringType)
Event_uid: Property = Property(name="uid", type=StringType)
Event_info: Property = Property(name="info", type=StringType)
Event_price: Property = Property(name="price", type=StringType)
Event_bannerUrl: Property = Property(name="bannerUrl", type=StringType)
Event_status: Property = Property(name="status", type=StringType)
Event_time: Property = Property(name="time", type=StringType)
Event_startTime: Property = Property(name="startTime", type=StringType)
Event_endTime: Property = Property(name="endTime", type=StringType)
Event_freeSeats: Property = Property(name="freeSeats", type=IntegerType)
Event_type: Property = Property(name="type", type=IntegerType)
Event_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Event_eventPoints: Property = Property(name="eventPoints", type=StringType)
Event.attributes={Event_time, Event_price, Event_bannerUrl, Event_freeSeats, Event_type, Event_endTime, Event_info, Event_startTime, Event_status, Event_eventPoints, Event_phoneNumber, Event_uid, Event_name}

# EventPoint class attributes and methods
EventPoint_location: Property = Property(name="location", type=LatLng)
EventPoint_time: Property = Property(name="time", type=StringType)
EventPoint_type: Property = Property(name="type", type=IntegerType)
EventPoint.attributes={EventPoint_type, EventPoint_time, EventPoint_location}

# EventRegistrationInformation class attributes and methods
EventRegistrationInformation_uid: Property = Property(name="uid", type=StringType)
EventRegistrationInformation_passenger: Property = Property(name="passenger", type=User)
EventRegistrationInformation_numberOfSeats: Property = Property(name="numberOfSeats", type=IntegerType)
EventRegistrationInformation_eventId: Property = Property(name="eventId", type=StringType)
EventRegistrationInformation_state: Property = Property(name="state", type=IntegerType)
EventRegistrationInformation_paymentMethod: Property = Property(name="paymentMethod", type=IntegerType)
EventRegistrationInformation_isPaid: Property = Property(name="isPaid", type=BooleanType)
EventRegistrationInformation.attributes={EventRegistrationInformation_state, EventRegistrationInformation_passenger, EventRegistrationInformation_uid, EventRegistrationInformation_isPaid, EventRegistrationInformation_eventId, EventRegistrationInformation_numberOfSeats, EventRegistrationInformation_paymentMethod}

# FollowUp class attributes and methods
FollowUp_uid: Property = Property(name="uid", type=StringType)
FollowUp_type: Property = Property(name="type", type=IntegerType)
FollowUp_key: Property = Property(name="key", type=StringType)
FollowUp_name: Property = Property(name="name", type=StringType)
FollowUp_from: Property = Property(name="from", type=StringType)
FollowUp_to: Property = Property(name="to", type=StringType)
FollowUp_driver: Property = Property(name="driver", type=Driver)
FollowUp_info: Property = Property(name="info", type=StringType)
FollowUp_password: Property = Property(name="password", type=StringType)
FollowUp_time: Property = Property(name="time", type=StringType)
FollowUp_stations: Property = Property(name="stations", type=StringType)
FollowUp_freePickup: Property = Property(name="freePickup", type=BooleanType)
FollowUp.attributes={FollowUp_to, FollowUp_freePickup, FollowUp_from, FollowUp_info, FollowUp_password, FollowUp_time, FollowUp_name, FollowUp_key, FollowUp_uid, FollowUp_type, FollowUp_stations, FollowUp_driver}

# FollowUpSubscriber class attributes and methods
FollowUpSubscriber_location: Property = Property(name="location", type=LatLng)
FollowUpSubscriber_user: Property = Property(name="user", type=User)
FollowUpSubscriber_followUpId: Property = Property(name="followUpId", type=StringType)
FollowUpSubscriber.attributes={FollowUpSubscriber_followUpId, FollowUpSubscriber_user, FollowUpSubscriber_location}

# Trip class attributes and methods
Trip_route: Property = Property(name="route", type=Route)
Trip_time: Property = Property(name="time", type=StringType)
Trip_driver: Property = Property(name="driver", type=Driver)
Trip_uid: Property = Property(name="uid", type=StringType)
Trip_freeSeats: Property = Property(name="freeSeats", type=IntegerType)
Trip_reservedSeats: Property = Property(name="reservedSeats", type=IntegerType)
Trip_capacity: Property = Property(name="capacity", type=IntegerType)
Trip_seatPrice: Property = Property(name="seatPrice", type=StringType)
Trip_isLive: Property = Property(name="isLive", type=BooleanType)
Trip_isIntercity: Property = Property(name="isIntercity", type=BooleanType)
Trip.attributes={Trip_capacity, Trip_reservedSeats, Trip_isLive, Trip_time, Trip_route, Trip_freeSeats, Trip_uid, Trip_driver, Trip_seatPrice, Trip_isIntercity}

# OverviewPolyline class attributes and methods
OverviewPolyline_points: Property = Property(name="points", type=StringType)
OverviewPolyline.attributes={OverviewPolyline_points}

# RequestCarInfo class attributes and methods
RequestCarInfo_uid: Property = Property(name="uid", type=StringType)
RequestCarInfo_user: Property = Property(name="user", type=User)
RequestCarInfo_from: Property = Property(name="from", type=StringType)
RequestCarInfo_to: Property = Property(name="to", type=StringType)
RequestCarInfo_time: Property = Property(name="time", type=StringType)
RequestCarInfo_numberOfPassengers: Property = Property(name="numberOfPassengers", type=IntegerType)
RequestCarInfo_numberOfDays: Property = Property(name="numberOfDays", type=IntegerType)
RequestCarInfo_state: Property = Property(name="state", type=IntegerType)
RequestCarInfo_type: Property = Property(name="type", type=IntegerType)
RequestCarInfo_comment: Property = Property(name="comment", type=StringType)
RequestCarInfo.attributes={RequestCarInfo_from, RequestCarInfo_uid, RequestCarInfo_to, RequestCarInfo_comment, RequestCarInfo_numberOfPassengers, RequestCarInfo_state, RequestCarInfo_time, RequestCarInfo_type, RequestCarInfo_user, RequestCarInfo_numberOfDays}

# Reservation class attributes and methods
Reservation_uid: Property = Property(name="uid", type=StringType)
Reservation_user: Property = Property(name="user", type=User)
Reservation_reservationState: Property = Property(name="reservationState", type=IntegerType)
Reservation_route: Property = Property(name="route", type=Route)
Reservation_pickupLocation: Property = Property(name="pickupLocation", type=LatLng)
Reservation_dueAmout: Property = Property(name="dueAmout", type=StringType)
Reservation_paymentMethod: Property = Property(name="paymentMethod", type=IntegerType)
Reservation_reservedSeats: Property = Property(name="reservedSeats", type=IntegerType)
Reservation_reachedDest: Property = Property(name="reachedDest", type=BooleanType)
Reservation_inCar: Property = Property(name="inCar", type=BooleanType)
Reservation_paid: Property = Property(name="paid", type=BooleanType)
Reservation.attributes={Reservation_user, Reservation_route, Reservation_reachedDest, Reservation_dueAmout, Reservation_inCar, Reservation_pickupLocation, Reservation_uid, Reservation_paymentMethod, Reservation_reservedSeats, Reservation_paid, Reservation_reservationState}

# Route class attributes and methods
Route_uid: Property = Property(name="uid", type=StringType)
Route_routeName: Property = Property(name="routeName", type=StringType)
Route_overviewPolyline: Property = Property(name="overviewPolyline", type=OverviewPolyline)
Route_stations: Property = Property(name="stations", type=StringType)
Route_waypoints: Property = Property(name="waypoints", type=StringType)
Route.attributes={Route_stations, Route_uid, Route_routeName, Route_waypoints, Route_overviewPolyline}

# Station class attributes and methods
Station_uid: Property = Property(name="uid", type=StringType)
Station_nameEng: Property = Property(name="nameEng", type=StringType)
Station_nameAra: Property = Property(name="nameAra", type=StringType)
Station_location: Property = Property(name="location", type=LatLng)
Station.attributes={Station_location, Station_nameEng, Station_uid, Station_nameAra}

# TimeData class attributes and methods
TimeData_routes: Property = Property(name="routes", type=StringType)
TimeData.attributes={TimeData_routes}

# Class class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_BZt5MLJKEemcsc4aPpxbEQ",
    types={User, Driver, LatLng, Event, EventPoint, EventRegistrationInformation, FollowUp, FollowUpSubscriber, Trip, OverviewPolyline, RequestCarInfo, Reservation, Route, Station, TimeData, Class_, Enumeration_, AccountStatus},
    associations={},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
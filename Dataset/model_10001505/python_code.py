from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass
class AccountStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Class:

    pass


class TimeData:

    def __init__(self, routes: str):
        self.routes = routes
        
        pass
    @property
    def routes(self):
        return self.__routes
    @routes.setter
    def routes(self, routes: str):
        self.__routes = routes



class Station:

    def __init__(self, uid: str, nameEng: str, nameAra: str, location: LatLng):
        self.uid = uid
        self.nameEng = nameEng
        self.nameAra = nameAra
        self.location = location
        
        pass
    @property
    def nameEng(self):
        return self.__nameEng
    @nameEng.setter
    def nameEng(self, nameEng: str):
        self.__nameEng = nameEng

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: LatLng):
        self.__location = location

    @property
    def nameAra(self):
        return self.__nameAra
    @nameAra.setter
    def nameAra(self, nameAra: str):
        self.__nameAra = nameAra



class Route:

    def __init__(self, uid: str, routeName: str, overviewPolyline: OverviewPolyline, stations: str, waypoints: str):
        self.uid = uid
        self.routeName = routeName
        self.overviewPolyline = overviewPolyline
        self.stations = stations
        self.waypoints = waypoints
        
        pass
    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def overviewPolyline(self):
        return self.__overviewPolyline
    @overviewPolyline.setter
    def overviewPolyline(self, overviewPolyline: OverviewPolyline):
        self.__overviewPolyline = overviewPolyline

    @property
    def stations(self):
        return self.__stations
    @stations.setter
    def stations(self, stations: str):
        self.__stations = stations

    @property
    def waypoints(self):
        return self.__waypoints
    @waypoints.setter
    def waypoints(self, waypoints: str):
        self.__waypoints = waypoints

    @property
    def routeName(self):
        return self.__routeName
    @routeName.setter
    def routeName(self, routeName: str):
        self.__routeName = routeName



class Reservation:

    def __init__(self, uid: str, user: User, reservationState: int, route: Route, pickupLocation: LatLng, dueAmout: str, paymentMethod: int, reservedSeats: int, reachedDest: bool, inCar: bool, paid: bool):
        self.uid = uid
        self.user = user
        self.reservationState = reservationState
        self.route = route
        self.pickupLocation = pickupLocation
        self.dueAmout = dueAmout
        self.paymentMethod = paymentMethod
        self.reservedSeats = reservedSeats
        self.reachedDest = reachedDest
        self.inCar = inCar
        self.paid = paid
        
        pass
    @property
    def pickupLocation(self):
        return self.__pickupLocation
    @pickupLocation.setter
    def pickupLocation(self, pickupLocation: LatLng):
        self.__pickupLocation = pickupLocation

    @property
    def reservedSeats(self):
        return self.__reservedSeats
    @reservedSeats.setter
    def reservedSeats(self, reservedSeats: int):
        self.__reservedSeats = reservedSeats

    @property
    def paid(self):
        return self.__paid
    @paid.setter
    def paid(self, paid: bool):
        self.__paid = paid

    @property
    def dueAmout(self):
        return self.__dueAmout
    @dueAmout.setter
    def dueAmout(self, dueAmout: str):
        self.__dueAmout = dueAmout

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def paymentMethod(self):
        return self.__paymentMethod
    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: int):
        self.__paymentMethod = paymentMethod

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: User):
        self.__user = user

    @property
    def route(self):
        return self.__route
    @route.setter
    def route(self, route: Route):
        self.__route = route

    @property
    def reachedDest(self):
        return self.__reachedDest
    @reachedDest.setter
    def reachedDest(self, reachedDest: bool):
        self.__reachedDest = reachedDest

    @property
    def reservationState(self):
        return self.__reservationState
    @reservationState.setter
    def reservationState(self, reservationState: int):
        self.__reservationState = reservationState

    @property
    def inCar(self):
        return self.__inCar
    @inCar.setter
    def inCar(self, inCar: bool):
        self.__inCar = inCar



class RequestCarInfo:

    def __init__(self, uid: str, user: User, from1: str, to: str, time: str, numberOfPassengers: int, numberOfDays: int, state: int, type: int, comment: str):
        self.uid = uid
        self.user = user
        self.from1 = from1
        self.to = to
        self.time = time
        self.numberOfPassengers = numberOfPassengers
        self.numberOfDays = numberOfDays
        self.state = state
        self.type = type
        self.comment = comment
        
        pass
    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: User):
        self.__user = user

    @property
    def numberOfDays(self):
        return self.__numberOfDays
    @numberOfDays.setter
    def numberOfDays(self, numberOfDays: int):
        self.__numberOfDays = numberOfDays

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def to(self):
        return self.__to
    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: int):
        self.__state = state

    @property
    def from1(self):
        return self.__from1
    @from1.setter
    def from1(self, from1: str):
        self.__from1 = from1

    @property
    def numberOfPassengers(self):
        return self.__numberOfPassengers
    @numberOfPassengers.setter
    def numberOfPassengers(self, numberOfPassengers: int):
        self.__numberOfPassengers = numberOfPassengers

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type



class OverviewPolyline:

    def __init__(self, points: str):
        self.points = points
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: str):
        self.__points = points



class Trip:

    def __init__(self, isLive: bool, isIntercity: bool, route: Route, time: str, driver: Driver, uid: str, freeSeats: int, reservedSeats: int, capacity: int, seatPrice: str):
        self.isLive = isLive
        self.isIntercity = isIntercity
        self.route = route
        self.time = time
        self.driver = driver
        self.uid = uid
        self.freeSeats = freeSeats
        self.reservedSeats = reservedSeats
        self.capacity = capacity
        self.seatPrice = seatPrice
        
        pass
    @property
    def isIntercity(self):
        return self.__isIntercity
    @isIntercity.setter
    def isIntercity(self, isIntercity: bool):
        self.__isIntercity = isIntercity

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def seatPrice(self):
        return self.__seatPrice
    @seatPrice.setter
    def seatPrice(self, seatPrice: str):
        self.__seatPrice = seatPrice

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def reservedSeats(self):
        return self.__reservedSeats
    @reservedSeats.setter
    def reservedSeats(self, reservedSeats: int):
        self.__reservedSeats = reservedSeats

    @property
    def freeSeats(self):
        return self.__freeSeats
    @freeSeats.setter
    def freeSeats(self, freeSeats: int):
        self.__freeSeats = freeSeats

    @property
    def isLive(self):
        return self.__isLive
    @isLive.setter
    def isLive(self, isLive: bool):
        self.__isLive = isLive

    @property
    def route(self):
        return self.__route
    @route.setter
    def route(self, route: Route):
        self.__route = route

    @property
    def driver(self):
        return self.__driver
    @driver.setter
    def driver(self, driver: Driver):
        self.__driver = driver

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid



class FollowUpSubscriber:

    def __init__(self, location: LatLng, user: User, followUpId: str):
        self.location = location
        self.user = user
        self.followUpId = followUpId
        
        pass
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: User):
        self.__user = user

    @property
    def followUpId(self):
        return self.__followUpId
    @followUpId.setter
    def followUpId(self, followUpId: str):
        self.__followUpId = followUpId

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: LatLng):
        self.__location = location



class FollowUp:

    def __init__(self, uid: str, type: int, key: str, name: str, from1: str, to: str, driver: Driver, info: str, password: str, time: str, stations: str, freePickup: bool):
        self.uid = uid
        self.type = type
        self.key = key
        self.name = name
        self.from1 = from1
        self.to = to
        self.driver = driver
        self.info = info
        self.password = password
        self.time = time
        self.stations = stations
        self.freePickup = freePickup
        
        pass
    @property
    def key(self):
        return self.__key
    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def to(self):
        return self.__to
    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def from1(self):
        return self.__from1
    @from1.setter
    def from1(self, from1: str):
        self.__from1 = from1

    @property
    def driver(self):
        return self.__driver
    @driver.setter
    def driver(self, driver: Driver):
        self.__driver = driver

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def freePickup(self):
        return self.__freePickup
    @freePickup.setter
    def freePickup(self, freePickup: bool):
        self.__freePickup = freePickup

    @property
    def stations(self):
        return self.__stations
    @stations.setter
    def stations(self, stations: str):
        self.__stations = stations

    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class EventRegistrationInformation:

    def __init__(self, uid: str, passenger: User, numberOfSeats: int, eventId: str, state: int, paymentMethod: int, isPaid: bool):
        self.uid = uid
        self.passenger = passenger
        self.numberOfSeats = numberOfSeats
        self.eventId = eventId
        self.state = state
        self.paymentMethod = paymentMethod
        self.isPaid = isPaid
        
        pass
    @property
    def passenger(self):
        return self.__passenger
    @passenger.setter
    def passenger(self, passenger: User):
        self.__passenger = passenger

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def isPaid(self):
        return self.__isPaid
    @isPaid.setter
    def isPaid(self, isPaid: bool):
        self.__isPaid = isPaid

    @property
    def paymentMethod(self):
        return self.__paymentMethod
    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: int):
        self.__paymentMethod = paymentMethod

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: int):
        self.__state = state

    @property
    def numberOfSeats(self):
        return self.__numberOfSeats
    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: int):
        self.__numberOfSeats = numberOfSeats

    @property
    def eventId(self):
        return self.__eventId
    @eventId.setter
    def eventId(self, eventId: str):
        self.__eventId = eventId



class EventPoint:

    def __init__(self, location: LatLng, time: str, type: int):
        self.location = location
        self.time = time
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: LatLng):
        self.__location = location

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time



class Event:

    def __init__(self, name: str, uid: str, info: str, price: str, bannerUrl: str, status: str, time: str, startTime: str, endTime: str, freeSeats: int, type: int, phoneNumber: str, eventPoints: str):
        self.name = name
        self.uid = uid
        self.info = info
        self.price = price
        self.bannerUrl = bannerUrl
        self.status = status
        self.time = time
        self.startTime = startTime
        self.endTime = endTime
        self.freeSeats = freeSeats
        self.type = type
        self.phoneNumber = phoneNumber
        self.eventPoints = eventPoints
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def eventPoints(self):
        return self.__eventPoints
    @eventPoints.setter
    def eventPoints(self, eventPoints: str):
        self.__eventPoints = eventPoints

    @property
    def freeSeats(self):
        return self.__freeSeats
    @freeSeats.setter
    def freeSeats(self, freeSeats: int):
        self.__freeSeats = freeSeats

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def bannerUrl(self):
        return self.__bannerUrl
    @bannerUrl.setter
    def bannerUrl(self, bannerUrl: str):
        self.__bannerUrl = bannerUrl

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time



class LatLng:

    def __init__(self, latitude: str, longitude: str):
        self.latitude = latitude
        self.longitude = longitude
        
        pass
    @property
    def latitude(self):
        return self.__latitude
    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude
    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude



class Driver:

    def __init__(self, username: str, email: str, carLicense: str, averageRating: str, numberOfRatings: int, phoneNumber: str, avatar: str):
        self.username = username
        self.email = email
        self.carLicense = carLicense
        self.averageRating = averageRating
        self.numberOfRatings = numberOfRatings
        self.phoneNumber = phoneNumber
        self.avatar = avatar
        
        pass
    @property
    def carLicense(self):
        return self.__carLicense
    @carLicense.setter
    def carLicense(self, carLicense: str):
        self.__carLicense = carLicense

    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def numberOfRatings(self):
        return self.__numberOfRatings
    @numberOfRatings.setter
    def numberOfRatings(self, numberOfRatings: int):
        self.__numberOfRatings = numberOfRatings

    @property
    def averageRating(self):
        return self.__averageRating
    @averageRating.setter
    def averageRating(self, averageRating: str):
        self.__averageRating = averageRating

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class User:

    def __init__(self, id: str, username: str, email: str, avatar: str, phoneNumber: str, gender: int, birthDate: str, referralCode: str, numberOfReferrals: int, balance: str, referrer: str, accountStatus: AccountStatus):
        self.id = id
        self.username = username
        self.email = email
        self.avatar = avatar
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.birthDate = birthDate
        self.referralCode = referralCode
        self.numberOfReferrals = numberOfReferrals
        self.balance = balance
        self.referrer = referrer
        self.accountStatus = accountStatus
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def referralCode(self):
        return self.__referralCode
    @referralCode.setter
    def referralCode(self, referralCode: str):
        self.__referralCode = referralCode

    @property
    def numberOfReferrals(self):
        return self.__numberOfReferrals
    @numberOfReferrals.setter
    def numberOfReferrals(self, numberOfReferrals: int):
        self.__numberOfReferrals = numberOfReferrals

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def birthDate(self):
        return self.__birthDate
    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: int):
        self.__gender = gender

    @property
    def accountStatus(self):
        return self.__accountStatus
    @accountStatus.setter
    def accountStatus(self, accountStatus: AccountStatus):
        self.__accountStatus = accountStatus

    @property
    def referrer(self):
        return self.__referrer
    @referrer.setter
    def referrer(self, referrer: str):
        self.__referrer = referrer

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance


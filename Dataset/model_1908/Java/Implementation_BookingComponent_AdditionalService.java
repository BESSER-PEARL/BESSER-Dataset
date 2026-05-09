




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_AdditionalService  {

    private String location;
    private String guestCount;
    private LocalDate dateTime;
    private String name;
    private int price;





    private Implementation_BookingComponent_Booking implementation_bookingcomponent_booking;


    public Implementation_BookingComponent_AdditionalService(
        String location,        String guestCount,        LocalDate dateTime,        String name,        int price    ) {
        this.location = location;
        this.guestCount = guestCount;
        this.dateTime = dateTime;
        this.name = name;
        this.price = price;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getGuestcount() {
        return guestCount;
    }

    public void setGuestcount(String guestCount) {
        this.guestCount = guestCount;
    }
    public LocalDate getDatetime() {
        return dateTime;
    }

    public void setDatetime(LocalDate dateTime) {
        this.dateTime = dateTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Implementation_BookingComponent_Booking getImplementation_bookingcomponent_booking() {
        return implementation_bookingcomponent_booking;
    }

    public void setImplementation_bookingcomponent_booking(Implementation_BookingComponent_Booking implementation_bookingcomponent_booking) {
        this.implementation_bookingcomponent_booking = implementation_bookingcomponent_booking;
    }

}
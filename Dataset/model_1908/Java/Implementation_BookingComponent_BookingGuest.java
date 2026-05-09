





import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_BookingGuest  {

    private String lastName;
    private String phoneNumber;
    private String firstName;
    private String address;





    private Implementation_BookingComponent_Booking implementation_bookingcomponent_booking;


    public Implementation_BookingComponent_BookingGuest(
        String lastName,        String phoneNumber,        String firstName,        String address    ) {
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
        this.firstName = firstName;
        this.address = address;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Implementation_BookingComponent_Booking getImplementation_bookingcomponent_booking() {
        return implementation_bookingcomponent_booking;
    }

    public void setImplementation_bookingcomponent_booking(Implementation_BookingComponent_Booking implementation_bookingcomponent_booking) {
        this.implementation_bookingcomponent_booking = implementation_bookingcomponent_booking;
    }

}
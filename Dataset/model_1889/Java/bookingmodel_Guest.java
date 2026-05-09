





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_Guest extends Person {

    private String guestTypes;
    private String roomNr;





    private bookingmodel_Booking bookingmodel_booking;


    public bookingmodel_Guest(
        String guestTypes,        String roomNr    ) {
        super(
        );
        this.guestTypes = guestTypes;
        this.roomNr = roomNr;
    }


    public String getGuesttypes() {
        return guestTypes;
    }

    public void setGuesttypes(String guestTypes) {
        this.guestTypes = guestTypes;
    }
    public String getRoomnr() {
        return roomNr;
    }

    public void setRoomnr(String roomNr) {
        this.roomNr = roomNr;
    }

    public bookingmodel_Booking getBookingmodel_booking() {
        return bookingmodel_booking;
    }

    public void setBookingmodel_booking(bookingmodel_Booking bookingmodel_booking) {
        this.bookingmodel_booking = bookingmodel_booking;
    }

}
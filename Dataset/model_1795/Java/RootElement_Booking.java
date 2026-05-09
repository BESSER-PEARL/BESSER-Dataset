





import java.util.List;
import java.util.ArrayList;

public class RootElement_Booking  {

    private String bookingID;





    private RootElement_Guest rootelement_guest;




    private RootElement_BookingHandler rootelement_bookinghandler;


    public RootElement_Booking(
        String bookingID    ) {
        this.bookingID = bookingID;
    }


    public String getBookingid() {
        return bookingID;
    }

    public void setBookingid(String bookingID) {
        this.bookingID = bookingID;
    }

    public RootElement_Guest getRootelement_guest() {
        return rootelement_guest;
    }

    public void setRootelement_guest(RootElement_Guest rootelement_guest) {
        this.rootelement_guest = rootelement_guest;
    }
    public RootElement_BookingHandler getRootelement_bookinghandler() {
        return rootelement_bookinghandler;
    }

    public void setRootelement_bookinghandler(RootElement_BookingHandler rootelement_bookinghandler) {
        this.rootelement_bookinghandler = rootelement_bookinghandler;
    }

}
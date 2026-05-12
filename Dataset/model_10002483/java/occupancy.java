





import java.util.List;
import java.util.ArrayList;

public class occupancy  {

    private int booking_id;





    private Booking booking;


    public occupancy(
        int booking_id    ) {
        this.booking_id = booking_id;
    }


    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}
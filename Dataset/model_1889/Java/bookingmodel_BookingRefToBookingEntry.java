





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_BookingRefToBookingEntry  {

    private String key;





    private bookingmodel_Booking bookingmodel_booking;


    public bookingmodel_BookingRefToBookingEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public bookingmodel_Booking getBookingmodel_booking() {
        return bookingmodel_booking;
    }

    public void setBookingmodel_booking(bookingmodel_Booking bookingmodel_booking) {
        this.bookingmodel_booking = bookingmodel_booking;
    }

}
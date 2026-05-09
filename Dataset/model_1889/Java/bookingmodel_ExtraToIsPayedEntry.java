





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_ExtraToIsPayedEntry  {

    private String key;
    private String value;





    private bookingmodel_Booking bookingmodel_booking;


    public bookingmodel_ExtraToIsPayedEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public bookingmodel_Booking getBookingmodel_booking() {
        return bookingmodel_booking;
    }

    public void setBookingmodel_booking(bookingmodel_Booking bookingmodel_booking) {
        this.bookingmodel_booking = bookingmodel_booking;
    }

}
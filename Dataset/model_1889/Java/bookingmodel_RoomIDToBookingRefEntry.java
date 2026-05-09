





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_RoomIDToBookingRefEntry  {

    private String key;
    private String value;





    private bookingmodel_BookingHandler bookingmodel_bookinghandler;


    public bookingmodel_RoomIDToBookingRefEntry(
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

    public bookingmodel_BookingHandler getBookingmodel_bookinghandler() {
        return bookingmodel_bookinghandler;
    }

    public void setBookingmodel_bookinghandler(bookingmodel_BookingHandler bookingmodel_bookinghandler) {
        this.bookingmodel_bookinghandler = bookingmodel_bookinghandler;
    }

}
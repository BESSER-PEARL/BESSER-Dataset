





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_GuestEmailToRoomIDEntry  {

    private int value;
    private String key;





    private bookingmodel_BookingHandler bookingmodel_bookinghandler;


    public bookingmodel_GuestEmailToRoomIDEntry(
        int value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public bookingmodel_BookingHandler getBookingmodel_bookinghandler() {
        return bookingmodel_bookinghandler;
    }

    public void setBookingmodel_bookinghandler(bookingmodel_BookingHandler bookingmodel_bookinghandler) {
        this.bookingmodel_bookinghandler = bookingmodel_bookinghandler;
    }

}
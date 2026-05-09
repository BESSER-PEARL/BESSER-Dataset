





import java.util.List;
import java.util.ArrayList;

public class se_bookingSystem_AbstractEvent extends IEvent {

    private String eventType;
    private int bookingID;
    private String timestamp;



    public se_bookingSystem_AbstractEvent(
        String eventType,        int bookingID,        String timestamp    ) {
        super(
        );
        this.eventType = eventType;
        this.bookingID = bookingID;
        this.timestamp = timestamp;
    }


    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public int getBookingid() {
        return bookingID;
    }

    public void setBookingid(int bookingID) {
        this.bookingID = bookingID;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }


}






import java.util.List;
import java.util.ArrayList;

public class tda593_booking_TravelInformation  {

    private int id;
    private String trackingId;
    private String comment;



    public tda593_booking_TravelInformation(
        int id,        String trackingId,        String comment    ) {
        this.id = id;
        this.trackingId = trackingId;
        this.comment = comment;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getTrackingid() {
        return trackingId;
    }

    public void setTrackingid(String trackingId) {
        this.trackingId = trackingId;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}
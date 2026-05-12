





import java.util.List;
import java.util.ArrayList;

public class TrackOrder  {

    private String OrderTime_Date;
    private String OrderTrack;



    public TrackOrder(
        String OrderTime_Date,        String OrderTrack    ) {
        this.OrderTime_Date = OrderTime_Date;
        this.OrderTrack = OrderTrack;
    }


    public String getOrdertime_date() {
        return OrderTime_Date;
    }

    public void setOrdertime_date(String OrderTime_Date) {
        this.OrderTime_Date = OrderTime_Date;
    }
    public String getOrdertrack() {
        return OrderTrack;
    }

    public void setOrdertrack(String OrderTrack) {
        this.OrderTrack = OrderTrack;
    }


}
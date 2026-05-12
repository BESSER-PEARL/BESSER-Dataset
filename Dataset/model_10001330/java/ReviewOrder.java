





import java.util.List;
import java.util.ArrayList;

public class ReviewOrder  {

    private String Review;
    private String RiderName;
    private String OrderTime_Date;



    public ReviewOrder(
        String Review,        String RiderName,        String OrderTime_Date    ) {
        this.Review = Review;
        this.RiderName = RiderName;
        this.OrderTime_Date = OrderTime_Date;
    }


    public String getReview() {
        return Review;
    }

    public void setReview(String Review) {
        this.Review = Review;
    }
    public String getRidername() {
        return RiderName;
    }

    public void setRidername(String RiderName) {
        this.RiderName = RiderName;
    }
    public String getOrdertime_date() {
        return OrderTime_Date;
    }

    public void setOrdertime_date(String OrderTime_Date) {
        this.OrderTime_Date = OrderTime_Date;
    }


}






import java.util.List;
import java.util.ArrayList;

public class OrderHistory  {

    private String OrderDate_Time;
    private String OrderStatus;
    private String OrderRider;
    private String OrderReview;



    public OrderHistory(
        String OrderDate_Time,        String OrderStatus,        String OrderRider,        String OrderReview    ) {
        this.OrderDate_Time = OrderDate_Time;
        this.OrderStatus = OrderStatus;
        this.OrderRider = OrderRider;
        this.OrderReview = OrderReview;
    }


    public String getOrderdate_time() {
        return OrderDate_Time;
    }

    public void setOrderdate_time(String OrderDate_Time) {
        this.OrderDate_Time = OrderDate_Time;
    }
    public String getOrderstatus() {
        return OrderStatus;
    }

    public void setOrderstatus(String OrderStatus) {
        this.OrderStatus = OrderStatus;
    }
    public String getOrderrider() {
        return OrderRider;
    }

    public void setOrderrider(String OrderRider) {
        this.OrderRider = OrderRider;
    }
    public String getOrderreview() {
        return OrderReview;
    }

    public void setOrderreview(String OrderReview) {
        this.OrderReview = OrderReview;
    }


}
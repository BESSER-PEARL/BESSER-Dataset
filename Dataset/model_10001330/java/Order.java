





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String OrderReview;
    private String OrderStatus;
    private String OrderPrice;
    private String OrderTime_Date;
    private String OrderRider;



    public Order(
        String OrderReview,        String OrderStatus,        String OrderPrice,        String OrderTime_Date,        String OrderRider    ) {
        this.OrderReview = OrderReview;
        this.OrderStatus = OrderStatus;
        this.OrderPrice = OrderPrice;
        this.OrderTime_Date = OrderTime_Date;
        this.OrderRider = OrderRider;
    }


    public String getOrderreview() {
        return OrderReview;
    }

    public void setOrderreview(String OrderReview) {
        this.OrderReview = OrderReview;
    }
    public String getOrderstatus() {
        return OrderStatus;
    }

    public void setOrderstatus(String OrderStatus) {
        this.OrderStatus = OrderStatus;
    }
    public String getOrderprice() {
        return OrderPrice;
    }

    public void setOrderprice(String OrderPrice) {
        this.OrderPrice = OrderPrice;
    }
    public String getOrdertime_date() {
        return OrderTime_Date;
    }

    public void setOrdertime_date(String OrderTime_Date) {
        this.OrderTime_Date = OrderTime_Date;
    }
    public String getOrderrider() {
        return OrderRider;
    }

    public void setOrderrider(String OrderRider) {
        this.OrderRider = OrderRider;
    }


}
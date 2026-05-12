





import java.util.List;
import java.util.ArrayList;

public class CompanyTrackOrder  {

    private String OrderRider;
    private String OrderDate_Time;
    private String OrderStatus;
    private String CustomerName;



    public CompanyTrackOrder(
        String OrderRider,        String OrderDate_Time,        String OrderStatus,        String CustomerName    ) {
        this.OrderRider = OrderRider;
        this.OrderDate_Time = OrderDate_Time;
        this.OrderStatus = OrderStatus;
        this.CustomerName = CustomerName;
    }


    public String getOrderrider() {
        return OrderRider;
    }

    public void setOrderrider(String OrderRider) {
        this.OrderRider = OrderRider;
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
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }


}
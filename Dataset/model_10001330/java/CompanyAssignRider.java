





import java.util.List;
import java.util.ArrayList;

public class CompanyAssignRider  {

    private String OrderDate_Time;
    private String OrderRider;
    private String CustomerName;



    public CompanyAssignRider(
        String OrderDate_Time,        String OrderRider,        String CustomerName    ) {
        this.OrderDate_Time = OrderDate_Time;
        this.OrderRider = OrderRider;
        this.CustomerName = CustomerName;
    }


    public String getOrderdate_time() {
        return OrderDate_Time;
    }

    public void setOrderdate_time(String OrderDate_Time) {
        this.OrderDate_Time = OrderDate_Time;
    }
    public String getOrderrider() {
        return OrderRider;
    }

    public void setOrderrider(String OrderRider) {
        this.OrderRider = OrderRider;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }


}
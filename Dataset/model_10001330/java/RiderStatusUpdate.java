





import java.util.List;
import java.util.ArrayList;

public class RiderStatusUpdate  {

    private String CustomerName;
    private String OrderDate_Time;
    private String ItemList;



    public RiderStatusUpdate(
        String CustomerName,        String OrderDate_Time,        String ItemList    ) {
        this.CustomerName = CustomerName;
        this.OrderDate_Time = OrderDate_Time;
        this.ItemList = ItemList;
    }


    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public String getOrderdate_time() {
        return OrderDate_Time;
    }

    public void setOrderdate_time(String OrderDate_Time) {
        this.OrderDate_Time = OrderDate_Time;
    }
    public String getItemlist() {
        return ItemList;
    }

    public void setItemlist(String ItemList) {
        this.ItemList = ItemList;
    }


}






import java.util.List;
import java.util.ArrayList;

public class GPSLocation  {

    private String GPS;





    private Order order;


    public GPSLocation(
        String GPS    ) {
        this.GPS = GPS;
    }


    public String getGps() {
        return GPS;
    }

    public void setGps(String GPS) {
        this.GPS = GPS;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
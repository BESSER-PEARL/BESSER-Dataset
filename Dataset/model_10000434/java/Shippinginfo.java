





import java.util.List;
import java.util.ArrayList;

public class Shippinginfo  {

    private String total;
    private String region;
    private String shippingid;
    private String type;
    private String cost;





    private Order order;


    public Shippinginfo(
        String total,        String region,        String shippingid,        String type,        String cost    ) {
        this.total = total;
        this.region = region;
        this.shippingid = shippingid;
        this.type = type;
        this.cost = cost;
    }


    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
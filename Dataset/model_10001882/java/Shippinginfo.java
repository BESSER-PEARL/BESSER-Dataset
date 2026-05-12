





import java.util.List;
import java.util.ArrayList;

public class Shippinginfo  {

    private String cost;
    private String shippingid;
    private String total;
    private String type;
    private String region;





    private Order order;


    public Shippinginfo(
        String cost,        String shippingid,        String total,        String type,        String region    ) {
        this.cost = cost;
        this.shippingid = shippingid;
        this.total = total;
        this.type = type;
        this.region = region;
    }


    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
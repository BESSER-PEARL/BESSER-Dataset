





import java.util.List;
import java.util.ArrayList;

public class shippinginfo  {

    private int shippingcost;
    private int shippingId;





    private order order;


    public shippinginfo(
        int shippingcost,        int shippingId    ) {
        this.shippingcost = shippingcost;
        this.shippingId = shippingId;
    }


    public int getShippingcost() {
        return shippingcost;
    }

    public void setShippingcost(int shippingcost) {
        this.shippingcost = shippingcost;
    }
    public int getShippingid() {
        return shippingId;
    }

    public void setShippingid(int shippingId) {
        this.shippingId = shippingId;
    }

    public order getOrder() {
        return order;
    }

    public void setOrder(order order) {
        this.order = order;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ShippingInfo  {

    private int shippingCharges;
    private String estimatedDeliveryDate;
    private String deliveryAddress;
    private String deliveryType;





    private Order order;


    public ShippingInfo(
        int shippingCharges,        String estimatedDeliveryDate,        String deliveryAddress,        String deliveryType    ) {
        this.shippingCharges = shippingCharges;
        this.estimatedDeliveryDate = estimatedDeliveryDate;
        this.deliveryAddress = deliveryAddress;
        this.deliveryType = deliveryType;
    }


    public int getShippingcharges() {
        return shippingCharges;
    }

    public void setShippingcharges(int shippingCharges) {
        this.shippingCharges = shippingCharges;
    }
    public String getEstimateddeliverydate() {
        return estimatedDeliveryDate;
    }

    public void setEstimateddeliverydate(String estimatedDeliveryDate) {
        this.estimatedDeliveryDate = estimatedDeliveryDate;
    }
    public String getDeliveryaddress() {
        return deliveryAddress;
    }

    public void setDeliveryaddress(String deliveryAddress) {
        this.deliveryAddress = deliveryAddress;
    }
    public String getDeliverytype() {
        return deliveryType;
    }

    public void setDeliverytype(String deliveryType) {
        this.deliveryType = deliveryType;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Shipping  {

    private int shippingId;
    private String shippingType;
    private String shippingAddress;
    private int _attr;
    private String ShippingType;





    private ShippingType_Interface shippingtype_interface;




    private Order order;




    private Order order;


    public Shipping(
        int shippingId,        String shippingType,        String shippingAddress,        int _attr,        String ShippingType    ) {
        this.shippingId = shippingId;
        this.shippingType = shippingType;
        this.shippingAddress = shippingAddress;
        this._attr = _attr;
        this.ShippingType = ShippingType;
    }


    public int getShippingid() {
        return shippingId;
    }

    public void setShippingid(int shippingId) {
        this.shippingId = shippingId;
    }
    public String getShippingtype() {
        return shippingType;
    }

    public void setShippingtype(String shippingType) {
        this.shippingType = shippingType;
    }
    public String getShippingaddress() {
        return shippingAddress;
    }

    public void setShippingaddress(String shippingAddress) {
        this.shippingAddress = shippingAddress;
    }
    public int get_attr() {
        return _attr;
    }

    public void set_attr(int _attr) {
        this._attr = _attr;
    }
    public String getShippingtype() {
        return ShippingType;
    }

    public void setShippingtype(String ShippingType) {
        this.ShippingType = ShippingType;
    }

    public ShippingType_Interface getShippingtype_interface() {
        return shippingtype_interface;
    }

    public void setShippingtype_interface(ShippingType_Interface shippingtype_interface) {
        this.shippingtype_interface = shippingtype_interface;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
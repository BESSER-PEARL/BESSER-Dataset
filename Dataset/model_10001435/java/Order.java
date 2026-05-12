





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int CustomerId;
    private String OrderDate;
    private int OrderId;
    private String ShipDate;





    private Product product;


    public Order(
        int CustomerId,        String OrderDate,        int OrderId,        String ShipDate    ) {
        this.CustomerId = CustomerId;
        this.OrderDate = OrderDate;
        this.OrderId = OrderId;
        this.ShipDate = ShipDate;
    }


    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }
    public String getOrderdate() {
        return OrderDate;
    }

    public void setOrderdate(String OrderDate) {
        this.OrderDate = OrderDate;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public String getShipdate() {
        return ShipDate;
    }

    public void setShipdate(String ShipDate) {
        this.ShipDate = ShipDate;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}
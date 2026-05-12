





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String ShipDate;
    private String OrderDate;
    private int OrderId;
    private int CustomerId;





    private Product product;


    public Order(
        String ShipDate,        String OrderDate,        int OrderId,        int CustomerId    ) {
        this.ShipDate = ShipDate;
        this.OrderDate = OrderDate;
        this.OrderId = OrderId;
        this.CustomerId = CustomerId;
    }


    public String getShipdate() {
        return ShipDate;
    }

    public void setShipdate(String ShipDate) {
        this.ShipDate = ShipDate;
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
    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}
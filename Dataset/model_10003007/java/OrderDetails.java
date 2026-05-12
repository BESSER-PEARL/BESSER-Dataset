





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int Quantity;
    private int ProductId;
    private int OrderId;
    private int UnitCost;





    private Order order;


    public OrderDetails(
        int Quantity,        int ProductId,        int OrderId,        int UnitCost    ) {
        this.Quantity = Quantity;
        this.ProductId = ProductId;
        this.OrderId = OrderId;
        this.UnitCost = UnitCost;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getProductid() {
        return ProductId;
    }

    public void setProductid(int ProductId) {
        this.ProductId = ProductId;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public int getUnitcost() {
        return UnitCost;
    }

    public void setUnitcost(int UnitCost) {
        this.UnitCost = UnitCost;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}






import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int OrderId;
    private int UnitCost;
    private int ProductId;
    private int Quantity;





    private Order order;


    public OrderDetails(
        int OrderId,        int UnitCost,        int ProductId,        int Quantity    ) {
        this.OrderId = OrderId;
        this.UnitCost = UnitCost;
        this.ProductId = ProductId;
        this.Quantity = Quantity;
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
    public int getProductid() {
        return ProductId;
    }

    public void setProductid(int ProductId) {
        this.ProductId = ProductId;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
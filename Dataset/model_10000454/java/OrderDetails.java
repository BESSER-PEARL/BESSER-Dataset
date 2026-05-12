





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int Quantity;
    private int SubTotal;
    private String ProductName;
    private int UnitCost;
    private int ProductID;
    private int OrderID;





    private Order order;


    public OrderDetails(
        int Quantity,        int SubTotal,        String ProductName,        int UnitCost,        int ProductID,        int OrderID    ) {
        this.Quantity = Quantity;
        this.SubTotal = SubTotal;
        this.ProductName = ProductName;
        this.UnitCost = UnitCost;
        this.ProductID = ProductID;
        this.OrderID = OrderID;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getSubtotal() {
        return SubTotal;
    }

    public void setSubtotal(int SubTotal) {
        this.SubTotal = SubTotal;
    }
    public String getProductname() {
        return ProductName;
    }

    public void setProductname(String ProductName) {
        this.ProductName = ProductName;
    }
    public int getUnitcost() {
        return UnitCost;
    }

    public void setUnitcost(int UnitCost) {
        this.UnitCost = UnitCost;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
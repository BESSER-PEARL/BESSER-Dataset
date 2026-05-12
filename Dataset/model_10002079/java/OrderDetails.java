





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int ProductID;
    private int OrderID;
    private String ProductName;
    private int UnitCost;
    private int Quantity;
    private int SubTotal;





    private Order order;


    public OrderDetails(
        int ProductID,        int OrderID,        String ProductName,        int UnitCost,        int Quantity,        int SubTotal    ) {
        this.ProductID = ProductID;
        this.OrderID = OrderID;
        this.ProductName = ProductName;
        this.UnitCost = UnitCost;
        this.Quantity = Quantity;
        this.SubTotal = SubTotal;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
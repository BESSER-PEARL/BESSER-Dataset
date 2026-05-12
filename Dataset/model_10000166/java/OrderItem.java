




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OrderItem  {

    private String ItemName;
    private LocalDate RemaningTime;
    private int Completed;
    private int OrderID;
    private int OrderItemID;





    private Order order;




    private ViewOrder vieworder;


    public OrderItem(
        String ItemName,        LocalDate RemaningTime,        int Completed,        int OrderID,        int OrderItemID    ) {
        this.ItemName = ItemName;
        this.RemaningTime = RemaningTime;
        this.Completed = Completed;
        this.OrderID = OrderID;
        this.OrderItemID = OrderItemID;
    }


    public String getItemname() {
        return ItemName;
    }

    public void setItemname(String ItemName) {
        this.ItemName = ItemName;
    }
    public LocalDate getRemaningtime() {
        return RemaningTime;
    }

    public void setRemaningtime(LocalDate RemaningTime) {
        this.RemaningTime = RemaningTime;
    }
    public int getCompleted() {
        return Completed;
    }

    public void setCompleted(int Completed) {
        this.Completed = Completed;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getOrderitemid() {
        return OrderItemID;
    }

    public void setOrderitemid(int OrderItemID) {
        this.OrderItemID = OrderItemID;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public ViewOrder getVieworder() {
        return vieworder;
    }

    public void setVieworder(ViewOrder vieworder) {
        this.vieworder = vieworder;
    }

}
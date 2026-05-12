




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OrderItem  {

    private LocalDate RemaningTime;
    private int OrderItemID;
    private int Completed;
    private String ItemName;
    private int OrderID;





    private ViewOrder vieworder;




    private Order order;


    public OrderItem(
        LocalDate RemaningTime,        int OrderItemID,        int Completed,        String ItemName,        int OrderID    ) {
        this.RemaningTime = RemaningTime;
        this.OrderItemID = OrderItemID;
        this.Completed = Completed;
        this.ItemName = ItemName;
        this.OrderID = OrderID;
    }


    public LocalDate getRemaningtime() {
        return RemaningTime;
    }

    public void setRemaningtime(LocalDate RemaningTime) {
        this.RemaningTime = RemaningTime;
    }
    public int getOrderitemid() {
        return OrderItemID;
    }

    public void setOrderitemid(int OrderItemID) {
        this.OrderItemID = OrderItemID;
    }
    public int getCompleted() {
        return Completed;
    }

    public void setCompleted(int Completed) {
        this.Completed = Completed;
    }
    public String getItemname() {
        return ItemName;
    }

    public void setItemname(String ItemName) {
        this.ItemName = ItemName;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }

    public ViewOrder getVieworder() {
        return vieworder;
    }

    public void setVieworder(ViewOrder vieworder) {
        this.vieworder = vieworder;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
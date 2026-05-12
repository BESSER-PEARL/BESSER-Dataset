




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OrderList  {

    private int OrderItemID;
    private int OrderID;
    private String ItemName;
    private LocalDate RemaningTime;





    private ViewOrder vieworder;




    private Order order;


    public OrderList(
        int OrderItemID,        int OrderID,        String ItemName,        LocalDate RemaningTime    ) {
        this.OrderItemID = OrderItemID;
        this.OrderID = OrderID;
        this.ItemName = ItemName;
        this.RemaningTime = RemaningTime;
    }


    public int getOrderitemid() {
        return OrderItemID;
    }

    public void setOrderitemid(int OrderItemID) {
        this.OrderItemID = OrderItemID;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
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





import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OrderItem  {

    private int Completed;
    private LocalDate RemaningTime;
    private String ItemName;





    private Order order;




    private ViewOrder vieworder;


    public OrderItem(
        int Completed,        LocalDate RemaningTime,        String ItemName    ) {
        this.Completed = Completed;
        this.RemaningTime = RemaningTime;
        this.ItemName = ItemName;
    }


    public int getCompleted() {
        return Completed;
    }

    public void setCompleted(int Completed) {
        this.Completed = Completed;
    }
    public LocalDate getRemaningtime() {
        return RemaningTime;
    }

    public void setRemaningtime(LocalDate RemaningTime) {
        this.RemaningTime = RemaningTime;
    }
    public String getItemname() {
        return ItemName;
    }

    public void setItemname(String ItemName) {
        this.ItemName = ItemName;
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
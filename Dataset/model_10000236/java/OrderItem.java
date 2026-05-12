




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OrderItem  {

    private String ItemName;
    private LocalDate RemaningTime;
    private int Completed;





    private Order order;




    private ViewOrder vieworder;


    public OrderItem(
        String ItemName,        LocalDate RemaningTime,        int Completed    ) {
        this.ItemName = ItemName;
        this.RemaningTime = RemaningTime;
        this.Completed = Completed;
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
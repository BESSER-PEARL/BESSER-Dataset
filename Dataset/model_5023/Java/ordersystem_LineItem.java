





import java.util.List;
import java.util.ArrayList;

public class ordersystem_LineItem  {

    private int quantity;
    private float discount;





    private ordersystem_Order ordersystem_order;




    private ordersystem_Order ordersystem_order;


    public ordersystem_LineItem(
        int quantity,        float discount    ) {
        this.quantity = quantity;
        this.discount = discount;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getDiscount() {
        return discount;
    }

    public void setDiscount(float discount) {
        this.discount = discount;
    }

    public ordersystem_Order getOrdersystem_order() {
        return ordersystem_order;
    }

    public void setOrdersystem_order(ordersystem_Order ordersystem_order) {
        this.ordersystem_order = ordersystem_order;
    }
    public ordersystem_Order getOrdersystem_order() {
        return ordersystem_order;
    }

    public void setOrdersystem_order(ordersystem_Order ordersystem_order) {
        this.ordersystem_order = ordersystem_order;
    }

}
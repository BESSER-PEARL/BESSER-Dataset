





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Line_item  {

    private String price;
    private int quantity;





    private NO_Queue_mobile_application__Shopping_Cart no_queue_mobile_application__shopping_cart;




    private NO_Queue_mobile_application__Order no_queue_mobile_application__order;


    public NO_Queue_mobile_application__Line_item(
        String price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public NO_Queue_mobile_application__Shopping_Cart getNo_queue_mobile_application__shopping_cart() {
        return no_queue_mobile_application__shopping_cart;
    }

    public void setNo_queue_mobile_application__shopping_cart(NO_Queue_mobile_application__Shopping_Cart no_queue_mobile_application__shopping_cart) {
        this.no_queue_mobile_application__shopping_cart = no_queue_mobile_application__shopping_cart;
    }
    public NO_Queue_mobile_application__Order getNo_queue_mobile_application__order() {
        return no_queue_mobile_application__order;
    }

    public void setNo_queue_mobile_application__order(NO_Queue_mobile_application__Order no_queue_mobile_application__order) {
        this.no_queue_mobile_application__order = no_queue_mobile_application__order;
    }

}
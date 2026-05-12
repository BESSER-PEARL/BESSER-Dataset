





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int OrderID;
    private String MealID;
    private int quantity;
    private String orderTime;
    private String status;
    private String totPrice;





    private Orders orders;




    private Cart cart;


    public OrderDetails(
        int OrderID,        String MealID,        int quantity,        String orderTime,        String status,        String totPrice    ) {
        this.OrderID = OrderID;
        this.MealID = MealID;
        this.quantity = quantity;
        this.orderTime = orderTime;
        this.status = status;
        this.totPrice = totPrice;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getMealid() {
        return MealID;
    }

    public void setMealid(String MealID) {
        this.MealID = MealID;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getOrdertime() {
        return orderTime;
    }

    public void setOrdertime(String orderTime) {
        this.orderTime = orderTime;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getTotprice() {
        return totPrice;
    }

    public void setTotprice(String totPrice) {
        this.totPrice = totPrice;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }
    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }

}
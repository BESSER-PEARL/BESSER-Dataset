





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int customerId;
    private int NumberOfBooks;
    private String price;
    private int orderId;





    private Shopping_Cart shopping_cart;




    private Admin admin;


    public Order(
        int customerId,        int NumberOfBooks,        String price,        int orderId    ) {
        this.customerId = customerId;
        this.NumberOfBooks = NumberOfBooks;
        this.price = price;
        this.orderId = orderId;
    }


    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public int getNumberofbooks() {
        return NumberOfBooks;
    }

    public void setNumberofbooks(int NumberOfBooks) {
        this.NumberOfBooks = NumberOfBooks;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }

    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}
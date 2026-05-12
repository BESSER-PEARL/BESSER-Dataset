





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String email;
    private String credit_card_info;
    private String shipping_info;
    private String customer;
    private String address;





    private User user;




    private List<Orders> orderss;




    private List<Shopping_Cart> shopping_carts;


    public Customer(
        String email,        String credit_card_info,        String shipping_info,        String customer,        String address    ) {
        this.email = email;
        this.credit_card_info = credit_card_info;
        this.shipping_info = shipping_info;
        this.customer = customer;
        this.address = address;
        this.orderss = new ArrayList<>();
        this.shopping_carts = new ArrayList<>();
    }

    public Customer(
        String email,        String credit_card_info,        String shipping_info,        String customer,        String address        ArrayList<Orders> orderss,        ArrayList<Shopping_Cart> shopping_carts    ) {
        this.email = email;
        this.credit_card_info = credit_card_info;
        this.shipping_info = shipping_info;
        this.customer = customer;
        this.address = address;
        this.orderss = orderss;
        this.shopping_carts = shopping_carts;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCredit_card_info() {
        return credit_card_info;
    }

    public void setCredit_card_info(String credit_card_info) {
        this.credit_card_info = credit_card_info;
    }
    public String getShipping_info() {
        return shipping_info;
    }

    public void setShipping_info(String shipping_info) {
        this.shipping_info = shipping_info;
    }
    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }
    public List<Shopping_Cart> getShopping_carts() {
        return shopping_carts;
    }

    public void addShopping_cart(Shopping_cart shopping_cart) {
        this.shopping_carts.add(shopping_cart);
    }

}
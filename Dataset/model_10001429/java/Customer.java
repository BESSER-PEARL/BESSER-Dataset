





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String e_mail;
    private String surname;
    private String name;
    private String address;
    private int u_id;





    private Statistics statistics;




    private List<Orders> orderss;




    private ShoppingCart shoppingcart;




    private ShoppingCart shoppingcart;


    public Customer(
        String e_mail,        String surname,        String name,        String address,        int u_id    ) {
        this.e_mail = e_mail;
        this.surname = surname;
        this.name = name;
        this.address = address;
        this.u_id = u_id;
        this.orderss = new ArrayList<>();
    }

    public Customer(
        String e_mail,        String surname,        String name,        String address,        int u_id        ArrayList<Orders> orderss    ) {
        this.e_mail = e_mail;
        this.surname = surname;
        this.name = name;
        this.address = address;
        this.u_id = u_id;
        this.orderss = orderss;
    }

    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }

    public Statistics getStatistics() {
        return statistics;
    }

    public void setStatistics(Statistics statistics) {
        this.statistics = statistics;
    }
    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}
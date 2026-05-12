





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int cust_id;
    private String email;
    private int mobile;
    private String name;
    private String Address;





    private Restaurant restaurant;


    public Customer(
        int cust_id,        String email,        int mobile,        String name,        String Address    ) {
        this.cust_id = cust_id;
        this.email = email;
        this.mobile = mobile;
        this.name = name;
        this.Address = Address;
    }


    public int getCust_id() {
        return cust_id;
    }

    public void setCust_id(int cust_id) {
        this.cust_id = cust_id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getMobile() {
        return mobile;
    }

    public void setMobile(int mobile) {
        this.mobile = mobile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(Restaurant restaurant) {
        this.restaurant = restaurant;
    }

}
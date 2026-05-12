





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private String phone;
    private String name;
    private String email;





    private New_Customer new_customer;




    private Registered_Customer registered_customer;




    private Product product;


    public Customer(
        String address,        String phone,        String name,        String email    ) {
        this.address = address;
        this.phone = phone;
        this.name = name;
        this.email = email;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public New_Customer getNew_customer() {
        return new_customer;
    }

    public void setNew_customer(New_Customer new_customer) {
        this.new_customer = new_customer;
    }
    public Registered_Customer getRegistered_customer() {
        return registered_customer;
    }

    public void setRegistered_customer(Registered_Customer registered_customer) {
        this.registered_customer = registered_customer;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}
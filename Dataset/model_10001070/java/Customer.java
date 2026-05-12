





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private String phone;
    private String address;
    private String email;





    private Registered_Customer registered_customer;




    private Product product;




    private New_Customer new_customer;


    public Customer(
        String name,        String phone,        String address,        String email    ) {
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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
    public New_Customer getNew_customer() {
        return new_customer;
    }

    public void setNew_customer(New_Customer new_customer) {
        this.new_customer = new_customer;
    }

}
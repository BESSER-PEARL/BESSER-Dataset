





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Gender;
    private String CustomerName;
    private int CustomerID;
    private String Address;
    private String Email;
    private String Phone;





    private Order order;


    public Customer(
        int Gender,        String CustomerName,        int CustomerID,        String Address,        String Email,        String Phone    ) {
        this.Gender = Gender;
        this.CustomerName = CustomerName;
        this.CustomerID = CustomerID;
        this.Address = Address;
        this.Email = Email;
        this.Phone = Phone;
    }


    public int getGender() {
        return Gender;
    }

    public void setGender(int Gender) {
        this.Gender = Gender;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
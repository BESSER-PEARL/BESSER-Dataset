





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Email;
    private int Phone_num;
    private String Address;
    private String Name;





    private Delivery delivery;




    private Order order;


    public User(
        String Email,        int Phone_num,        String Address,        String Name    ) {
        this.Email = Email;
        this.Phone_num = Phone_num;
        this.Address = Address;
        this.Name = Name;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getPhone_num() {
        return Phone_num;
    }

    public void setPhone_num(int Phone_num) {
        this.Phone_num = Phone_num;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Delivery getDelivery() {
        return delivery;
    }

    public void setDelivery(Delivery delivery) {
        this.delivery = delivery;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}
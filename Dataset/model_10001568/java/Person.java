





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String Address;
    private String Name;
    private String Surname;
    private String Email;





    private User user;




    private List<Order> orders;


    public Person(
        String Address,        String Name,        String Surname,        String Email    ) {
        this.Address = Address;
        this.Name = Name;
        this.Surname = Surname;
        this.Email = Email;
        this.orders = new ArrayList<>();
    }

    public Person(
        String Address,        String Name,        String Surname,        String Email        ArrayList<Order> orders    ) {
        this.Address = Address;
        this.Name = Name;
        this.Surname = Surname;
        this.Email = Email;
        this.orders = orders;
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
    public String getSurname() {
        return Surname;
    }

    public void setSurname(String Surname) {
        this.Surname = Surname;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}
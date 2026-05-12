





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String Name;
    private String Address;
    private int Contact;
    private int ID;
    private String Personalnformation;





    private Customer customer;




    private Waiter waiter;


    public Manager(
        String Name,        String Address,        int Contact,        int ID,        String Personalnformation    ) {
        this.Name = Name;
        this.Address = Address;
        this.Contact = Contact;
        this.ID = ID;
        this.Personalnformation = Personalnformation;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getContact() {
        return Contact;
    }

    public void setContact(int Contact) {
        this.Contact = Contact;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getPersonalnformation() {
        return Personalnformation;
    }

    public void setPersonalnformation(String Personalnformation) {
        this.Personalnformation = Personalnformation;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}
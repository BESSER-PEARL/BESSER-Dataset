





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String Name;
    private String Personalnformation;
    private String Address;
    private int ID;
    private int Contact;





    private Waiter waiter;




    private Customer customer;


    public Manager(
        String Name,        String Personalnformation,        String Address,        int ID,        int Contact    ) {
        this.Name = Name;
        this.Personalnformation = Personalnformation;
        this.Address = Address;
        this.ID = ID;
        this.Contact = Contact;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPersonalnformation() {
        return Personalnformation;
    }

    public void setPersonalnformation(String Personalnformation) {
        this.Personalnformation = Personalnformation;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getContact() {
        return Contact;
    }

    public void setContact(int Contact) {
        this.Contact = Contact;
    }

    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}
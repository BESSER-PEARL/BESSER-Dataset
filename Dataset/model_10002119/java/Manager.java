





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String Personalnformation;
    private int ID;
    private String Name;
    private int Contact;
    private String Address;





    private Waiter waiter;




    private Customer customer;


    public Manager(
        String Personalnformation,        int ID,        String Name,        int Contact,        String Address    ) {
        this.Personalnformation = Personalnformation;
        this.ID = ID;
        this.Name = Name;
        this.Contact = Contact;
        this.Address = Address;
    }


    public String getPersonalnformation() {
        return Personalnformation;
    }

    public void setPersonalnformation(String Personalnformation) {
        this.Personalnformation = Personalnformation;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getContact() {
        return Contact;
    }

    public void setContact(int Contact) {
        this.Contact = Contact;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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
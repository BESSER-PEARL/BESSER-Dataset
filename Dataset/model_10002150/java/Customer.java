





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Name;
    private String Contact;
    private String Address;



    public Customer(
        String Name,        String Contact,        String Address    ) {
        this.Name = Name;
        this.Contact = Contact;
        this.Address = Address;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getContact() {
        return Contact;
    }

    public void setContact(String Contact) {
        this.Contact = Contact;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}
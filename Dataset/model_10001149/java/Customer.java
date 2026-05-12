





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Address;
    private String Contact;
    private String Name;



    public Customer(
        String Address,        String Contact,        String Name    ) {
        this.Address = Address;
        this.Contact = Contact;
        this.Name = Name;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getContact() {
        return Contact;
    }

    public void setContact(String Contact) {
        this.Contact = Contact;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}
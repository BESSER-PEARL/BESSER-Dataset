





import java.util.List;
import java.util.ArrayList;

public class Waiter  {

    private int Contact;
    private String Name;
    private String ID;
    private String Personal_Information;
    private String Address;



    public Waiter(
        int Contact,        String Name,        String ID,        String Personal_Information,        String Address    ) {
        this.Contact = Contact;
        this.Name = Name;
        this.ID = ID;
        this.Personal_Information = Personal_Information;
        this.Address = Address;
    }


    public int getContact() {
        return Contact;
    }

    public void setContact(int Contact) {
        this.Contact = Contact;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getPersonal_information() {
        return Personal_Information;
    }

    public void setPersonal_information(String Personal_Information) {
        this.Personal_Information = Personal_Information;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}
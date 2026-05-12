





import java.util.List;
import java.util.ArrayList;

public class Waiter  {

    private String Personal_Information;
    private String Name;
    private int Contact;
    private String ID;
    private String Address;





    private Chef chef;


    public Waiter(
        String Personal_Information,        String Name,        int Contact,        String ID,        String Address    ) {
        this.Personal_Information = Personal_Information;
        this.Name = Name;
        this.Contact = Contact;
        this.ID = ID;
        this.Address = Address;
    }


    public String getPersonal_information() {
        return Personal_Information;
    }

    public void setPersonal_information(String Personal_Information) {
        this.Personal_Information = Personal_Information;
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
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Chef getChef() {
        return chef;
    }

    public void setChef(Chef chef) {
        this.chef = chef;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Waiter  {

    private String Personal_Information;
    private String Address;
    private String ID;
    private String Name;
    private int Contact;





    private Chef chef;


    public Waiter(
        String Personal_Information,        String Address,        String ID,        String Name,        int Contact    ) {
        this.Personal_Information = Personal_Information;
        this.Address = Address;
        this.ID = ID;
        this.Name = Name;
        this.Contact = Contact;
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
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
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

    public Chef getChef() {
        return chef;
    }

    public void setChef(Chef chef) {
        this.chef = chef;
    }

}
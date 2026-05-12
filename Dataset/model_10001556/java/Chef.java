





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private int ID;
    private String PersonalInformation;
    private String Domain;
    private String Address;
    private String Name;
    private int Contact;



    public Chef(
        int ID,        String PersonalInformation,        String Domain,        String Address,        String Name,        int Contact    ) {
        this.ID = ID;
        this.PersonalInformation = PersonalInformation;
        this.Domain = Domain;
        this.Address = Address;
        this.Name = Name;
        this.Contact = Contact;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getPersonalinformation() {
        return PersonalInformation;
    }

    public void setPersonalinformation(String PersonalInformation) {
        this.PersonalInformation = PersonalInformation;
    }
    public String getDomain() {
        return Domain;
    }

    public void setDomain(String Domain) {
        this.Domain = Domain;
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
    public int getContact() {
        return Contact;
    }

    public void setContact(int Contact) {
        this.Contact = Contact;
    }


}
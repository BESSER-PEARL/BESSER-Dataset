





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private String PersonalInformation;
    private int Contact;
    private String Address;
    private String Domain;
    private int ID;
    private String Name;



    public Chef(
        String PersonalInformation,        int Contact,        String Address,        String Domain,        int ID,        String Name    ) {
        this.PersonalInformation = PersonalInformation;
        this.Contact = Contact;
        this.Address = Address;
        this.Domain = Domain;
        this.ID = ID;
        this.Name = Name;
    }


    public String getPersonalinformation() {
        return PersonalInformation;
    }

    public void setPersonalinformation(String PersonalInformation) {
        this.PersonalInformation = PersonalInformation;
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
    public String getDomain() {
        return Domain;
    }

    public void setDomain(String Domain) {
        this.Domain = Domain;
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


}
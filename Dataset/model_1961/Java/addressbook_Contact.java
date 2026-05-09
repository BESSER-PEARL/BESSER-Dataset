





import java.util.List;
import java.util.ArrayList;

public class addressbook_Contact  {

    private String Name;
    private String EMail;
    private String Phone;
    private String Website;





    private List<addressbook_Contact> addressbook_contacts;


    public addressbook_Contact(
        String Name,        String EMail,        String Phone,        String Website    ) {
        this.Name = Name;
        this.EMail = EMail;
        this.Phone = Phone;
        this.Website = Website;
        this.addressbook_contacts = new ArrayList<>();
    }

    public addressbook_Contact(
        String Name,        String EMail,        String Phone,        String Website        ArrayList<addressbook_Contact> addressbook_contacts    ) {
        this.Name = Name;
        this.EMail = EMail;
        this.Phone = Phone;
        this.Website = Website;
        this.addressbook_contacts = addressbook_contacts;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return EMail;
    }

    public void setEmail(String EMail) {
        this.EMail = EMail;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getWebsite() {
        return Website;
    }

    public void setWebsite(String Website) {
        this.Website = Website;
    }

    public List<addressbook_Contact> getAddressbook_contacts() {
        return addressbook_contacts;
    }

    public void addAddressbook_contact(Addressbook_contact addressbook_contact) {
        this.addressbook_contacts.add(addressbook_contact);
    }

}
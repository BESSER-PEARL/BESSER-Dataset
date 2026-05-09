





import java.util.List;
import java.util.ArrayList;

public class addressbook_People  {

    private String name;





    private List<addressbook_Contact> addressbook_contacts;


    public addressbook_People(
        String name    ) {
        this.name = name;
        this.addressbook_contacts = new ArrayList<>();
    }

    public addressbook_People(
        String name        ArrayList<addressbook_Contact> addressbook_contacts    ) {
        this.name = name;
        this.addressbook_contacts = addressbook_contacts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<addressbook_Contact> getAddressbook_contacts() {
        return addressbook_contacts;
    }

    public void addAddressbook_contact(Addressbook_contact addressbook_contact) {
        this.addressbook_contacts.add(addressbook_contact);
    }

}






import java.util.List;
import java.util.ArrayList;

public class addressbook_AddressBook  {






    private List<addressbook_Contact> addressbook_contacts;


    public addressbook_AddressBook(
    ) {
        this.addressbook_contacts = new ArrayList<>();
    }

    public addressbook_AddressBook(
        ArrayList<addressbook_Contact> addressbook_contacts    ) {
        this.addressbook_contacts = addressbook_contacts;
    }


    public List<addressbook_Contact> getAddressbook_contacts() {
        return addressbook_contacts;
    }

    public void addAddressbook_contact(Addressbook_contact addressbook_contact) {
        this.addressbook_contacts.add(addressbook_contact);
    }

}